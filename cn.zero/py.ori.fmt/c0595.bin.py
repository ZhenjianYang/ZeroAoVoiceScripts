from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0595.bin",                # FileName
        "c0595",                    # MapName
        "c0595",                    # Location
        0x0029,                     # MapIndex
        "ed7122",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0595",                  # 0
        "bc0540",                 # 1
        "bc0540",                 # 2
        "bc0540",                 # 3
        "bc0540",                 # 4
    ))

    ATBonus("ATBonus_230", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_11B1", 0,   10,  20,  5,   20,  0,   0)
    Sepith("Sepith_11A9", 16,  0,   0,   0,   12,  12,  12)
    Sepith("Sepith_11A1", 0,   15,  0,   20,  20,  0,   0)
    Sepith("Sepith_1199", 12,  7,   0,   18,  0,   0,   18)

    MonsterBattlePostion("MonsterBattlePostion_290", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_300", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_304", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_308", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_270", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_3D8", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_11B1", 40, 30, 20, 10,
        (
            ("ms76800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76800.dat", "ms76800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
        )
    )

    BattleInfo(
        "BattleInfo_568", 0x0000, 33, 6, 60, 4, 1, 30, 0, "bc0540", "Sepith_11A9", 40, 30, 20, 10,
        (
            ("ms76500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76500.dat", "ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76500.dat", "ms76500.dat", "ms76500.dat", "ms76500.dat", 0, 0, 0, 0, "MonsterBattlePostion_270", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
        )
    )

    BattleInfo(
        "BattleInfo_4A0", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_11A1", 40, 30, 20, 10,
        (
            ("ms76700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76700.dat", "ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
        )
    )

    BattleInfo(
        "BattleInfo_310", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_1199", 40, 30, 20, 10,
        (
            ("ms76900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, "MonsterBattlePostion_290", "MonsterBattlePostion_2F0", "ed7400", "ed7403", "ATBonus_230"),
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
        "monster/ch76950.itc",               # 10
        "monster/ch76951.itc",               # 11
        "monster/ch76850.itc",               # 12
        "monster/ch76850.itc",               # 13
        "monster/ch76750.itc",               # 14
        "monster/ch76750.itc",               # 15
        "monster/ch76550.itc",               # 16
        "monster/ch76551.itc",               # 17
    ))

    DeclMonster(-19740,  -4460,   1500,    0x1010000,    "BattleInfo_3D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-26110,  7760,    0,       0x1010000,    "BattleInfo_568", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-33300,  -6030,   0,       0x1010000,    "BattleInfo_4A0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-3460,   3290,    3030,    0x1010000,    "BattleInfo_3D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-32100,  14020,   3030,    0x1010000,    "BattleInfo_310", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-6380,   15850,   3000,    0x1010000,    "BattleInfo_4A0", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-15000,  0,       0,       1200,    -15000,  1000,    0,       0x007C, 0,  2,  0x0000)
    DeclActor(-34000,  0,       -3000,   1200,    -34000,  1000,    -3000,   0x007C, 0,  3,  0x0000)
    DeclActor(-5000,   3000,    16000,   1200,    -5000,   4000,    16000,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_6A8",          # 00, 0
        "Function_1_6A9",          # 01, 1
        "Function_2_C67",          # 02, 2
        "Function_3_D9D",          # 03, 3
        "Function_4_E72",          # 04, 4
        "Function_5_F47",          # 05, 5
    ))


    def Function_0_6A8(): pass

    label("Function_0_6A8")

    Return()

    # Function_0_6A8 end

    def Function_1_6A9(): pass

    label("Function_1_6A9")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -26000, 3000, 6000, 3000, 1000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -26000, 3000, 2000, 3000, 1000, 0)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -28000, 0, 4000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -24000, 0, 4000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -16000, 3000, 4000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -12000, 3000, 4000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, -14000, 6000, 6000, 3000, 1000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, -14000, 6000, 2000, 3000, 1000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 3)), scpexpr(EXPR_END)), "loc_7E7")
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jump("loc_82F")

    label("loc_7E7")

    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_82F")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C62")
    OP_70(0x0, 0x0)
    Jump("loc_C66")

    label("loc_C62")

    OP_70(0x0, 0x1E)

    label("loc_C66")

    Return()

    # Function_1_6A9 end

    def Function_2_C67(): pass

    label("Function_2_C67")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D54")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('移动１', 1)"), scpexpr(EXPR_END)), "loc_CE6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_D4F")

    label("loc_CE6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D4F")

    Jump("loc_D91")

    label("loc_D54")

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

    label("loc_D91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_C67 end

    def Function_3_D9D(): pass

    label("Function_3_D9D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机控制装置。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6A")
    Fade(500)
    SetChrPos(0x0, -34310, 0, -4019, 0)
    SetChrPos(0x1, -33650, 0, -5260, 0)
    SetChrPos(0x2, -34730, 0, -5310, 0)
    SetChrPos(0x3, -34240, 0, -6580, 0)
    OP_68(-34700, 500, -4019, 0)
    MoveCamera(45, 53, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Call(0, 5)

    label("loc_E6A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_D9D end

    def Function_4_E72(): pass

    label("Function_4_E72")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机控制装置。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3F")
    Fade(500)
    SetChrPos(0x0, -6030, 3000, 15820, 89)
    SetChrPos(0x1, -7250, 3000, 16460, 89)
    SetChrPos(0x2, -7400, 3030, 14910, 89)
    SetChrPos(0x3, -8140, 3000, 15730, 89)
    OP_68(-6260, 3500, 15770, 0)
    MoveCamera(45, 52, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Call(0, 5)

    label("loc_F3F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_E72 end

    def Function_5_F47(): pass

    label("Function_5_F47")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 3)), scpexpr(EXPR_END)), "loc_1064")
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-26060, 3490, 3700, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x1, 0x2D, 0x0, 0x0, 0x0)
    OP_79(0x1)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-14340, 6500, 3700, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x2, 0x2D, 0x0, 0x0, 0x0)
    OP_79(0x2)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    ClearScenarioFlags(0xD5, 3)
    Jump("loc_1170")

    label("loc_1064")

    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-26060, 3490, 3700, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x1, 0x0, 0x2D, 0x0, 0x0)
    OP_79(0x1)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-14340, 6500, 3700, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x2, 0x0, 0x2D, 0x0, 0x0)
    OP_79(0x2)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetScenarioFlags(0xD5, 3)

    label("loc_1170")

    Return()

    # Function_5_F47 end

    SaveToFile()

Try(main)
