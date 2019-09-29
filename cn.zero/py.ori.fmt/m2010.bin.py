from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m2010.bin",                # FileName
        "M2010",                    # MapName
        "M2010",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2010",                  # 0
        "bm2000",                 # 1
        "bm2000",                 # 2
        "bm2000",                 # 3
    ))

    ATBonus("ATBonus_1B0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_A9C", 12,  0,   0,   7,   16,  16,  0)
    Sepith("Sepith_AA4", 13,  0,   8,   8,   13,  8,   0)
    Sepith("Sepith_AAC", 10,  5,   5,   4,   4,   8,   15)

    MonsterBattlePostion("MonsterBattlePostion_200", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_264", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_268", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_26C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_270", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_274", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_278", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 2, 13, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_280", 0x0000, 30, 6, 45, 6, 1, 30, 0, "bm2000", "Sepith_A9C", 40, 30, 20, 10,
        (
            ("ms73600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_200", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            ("ms73600.dat", "ms73600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E0", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            ("ms73600.dat", "ms73600.dat", "ms73600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_200", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            ("ms73600.dat", "ms73600.dat", "ms73600.dat", "ms73600.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E0", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
        )
    )

    BattleInfo(
        "BattleInfo_348", 0x0000, 30, 6, 45, 6, 1, 30, 0, "bm2000", "Sepith_AA4", 40, 30, 20, 10,
        (
            ("ms73700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_200", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            ("ms73700.dat", "ms73700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E0", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            ("ms73700.dat", "ms73700.dat", "ms73700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_200", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            ("ms73700.dat", "ms73700.dat", "ms73700.dat", "ms73700.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E0", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
        )
    )

    BattleInfo(
        "BattleInfo_410", 0x0000, 30, 6, 45, 6, 1, 30, 0, "bm2000", "Sepith_AAC", 100, 0, 0, 0,
        (
            ("ms74000.dat", "ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E0", "MonsterBattlePostion_260", "ed7400", "ed7403", "ATBonus_1B0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch73650.itc",               # 10
        "monster/ch73651.itc",               # 11
        "monster/ch73750.itc",               # 12
        "monster/ch73751.itc",               # 13
        "monster/ch74050.itc",               # 14
        "monster/ch74051.itc",               # 15
    ))

    DeclMonster(111400,  50,      0,       0x1010000,    "BattleInfo_280", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(3560,    15590,   -4000,   0x1010000,    "BattleInfo_348", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-12370,  15540,   -8000,   0x1010000,    "BattleInfo_280", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-127590, -1580,   0,       0x1010000,    "BattleInfo_410", 0,   20,  0xFFFF, 4,  5)

    DeclActor(115270,  0,       310,     1200,    115270,  1000,    310,     0x007C, 0,  2,  0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 1])                          # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_4A8",          # 00, 0
        "Function_1_4A9",          # 01, 1
        "Function_2_936",          # 02, 2
    ))


    def Function_0_4A8(): pass

    label("Function_0_4A8")

    Return()

    # Function_0_4A8 end

    def Function_1_4A9(): pass

    label("Function_1_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4BB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4CA")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_52B")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_55C")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)

    label("loc_55C")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1D, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x1, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x2, 0xA, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x3, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921")
    OP_70(0x2, 0x0)
    Jump("loc_925")

    label("loc_921")

    OP_70(0x2, 0x1E)

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_935")
    Sound(129, 1, 100, 0)

    label("loc_935")

    Return()

    # Function_1_4A9 end

    def Function_2_936(): pass

    label("Function_2_936")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A23")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_9B5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11C, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_A1E")

    label("loc_9B5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A1E")

    Jump("loc_A60")

    label("loc_A23")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_A60")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_936 end

    SaveToFile()

Try(main)
