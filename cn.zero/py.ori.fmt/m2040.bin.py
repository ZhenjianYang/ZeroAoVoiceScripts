from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m2040.bin",                # FileName
        "M2040",                    # MapName
        "M2040",                    # Location
        0x0074,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 1, 0, 2],
    )

    BuildStringList((
        "m2040",                  # 0
        "亡灵引导者",             # 1
        "bm2000",                 # 2
        "bm2000",                 # 3
        "bm2000",                 # 4
        "bm2000",                 # 5
        "bm2000",                 # 6
    ))

    ATBonus("ATBonus_27C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_26C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_110C", 4,   19,  6,   4,   11,  0,   5)
    Sepith("Sepith_1114", 8,   6,   0,   4,   14,  18,  0)
    Sepith("Sepith_1104", 11,  10,  0,   7,   12,  0,   11)
    Sepith("Sepith_10FC", 16,  12,  3,   9,   5,   0,   5)

    MonsterBattlePostion("MonsterBattlePostion_2CC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_330", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_334", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_338", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_33C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_340", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_344", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_4DC", 0x0000, 30, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_110C", 40, 30, 20, 10,
        (
            ("ms74500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74500.dat", "ms74500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74500.dat", "ms74400.dat", "ms74500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74500.dat", "ms74500.dat", "ms74400.dat", "ms74500.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
        )
    )

    BattleInfo(
        "BattleInfo_5A4", 0x0000, 30, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_1114", 40, 30, 20, 10,
        (
            ("ms74600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74600.dat", "ms74600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74600.dat", "ms74500.dat", "ms74600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74600.dat", "ms74600.dat", "ms74500.dat", "ms74600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
        )
    )

    BattleInfo(
        "BattleInfo_414", 0x0000, 30, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_1104", 40, 30, 20, 10,
        (
            ("ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
        )
    )

    BattleInfo(
        "BattleInfo_34C", 0x0000, 30, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_10FC", 40, 30, 20, 10,
        (
            ("ms74300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74300.dat", "ms74300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74300.dat", "ms74600.dat", "ms74300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
            ("ms74300.dat", "ms74300.dat", "ms74600.dat", "ms74300.dat", 0, 0, 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7400", "ed7403", "ATBonus_27C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_66C", 0x0000, 30, 6, 45, 0, 1, 0, 0, "bm2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74600.dat", "ms74600.dat", "ms74500.dat", "ms74600.dat", "ms74500.dat", "ms74600.dat", 0, 0, "MonsterBattlePostion_2AC", "MonsterBattlePostion_32C", "ed7401", "ed7403", "ATBonus_26C"),
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
        "monster/ch74350.itc",               # 10
        "monster/ch74350.itc",               # 11
        "monster/ch74450.itc",               # 12
        "monster/ch74450.itc",               # 13
        "monster/ch74550.itc",               # 14
        "monster/ch74551.itc",               # 15
        "monster/ch74650.itc",               # 16
        "monster/ch74651.itc",               # 17
    ))

    DeclNpc(-13000,  12500,   16000,   0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-11020,  16020,   4000,    0x1010000,    "BattleInfo_4DC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-10380,  15850,   -4000,   0x1010000,    "BattleInfo_5A4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-10020,  16470,   -12000,  0x1010000,    "BattleInfo_5A4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(2170,    -217110, 4000,    0x1010000,    "BattleInfo_414", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(1740,    -216120, 12000,   0x1010000,    "BattleInfo_34C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4280,    -216520, 20000,   0x1010000,    "BattleInfo_5A4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(150,     -96740,  0,       0x1010000,    "BattleInfo_4DC", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-13000,  12000,   16000,   1200,    -13000,  13000,   16000,   0x007C, 0,  4,  0x0000)
    DeclActor(-13000,  -16000,  -1000,   1200,    -13000,  -15000,  -1000,   0x007C, 0,  5,  0x0000)
    DeclActor(-16500,  8000,    0,       1200,    -16500,  10000,   0,       0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(3000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_72C",          # 00, 0
        "Function_1_747",          # 01, 1
        "Function_2_748",          # 02, 2
        "Function_3_C1D",          # 03, 3
        "Function_4_C58",          # 04, 4
        "Function_5_E52",          # 05, 5
        "Function_6_F88",          # 06, 6
    ))


    def Function_0_72C(): pass

    label("Function_0_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_746")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_0_72C")

    label("loc_746")

    Return()

    # Function_0_72C end

    def Function_1_747(): pass

    label("Function_1_747")

    Return()

    # Function_1_747 end

    def Function_2_748(): pass

    label("Function_2_748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_75A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_769")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_7CA")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_819")
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)

    label("loc_819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 2)), scpexpr(EXPR_END)), "loc_838")
    SetMapObjFrame(0x4, "root", 0x2, "on")
    ClearMapObjFlags(0x4, 0x2)
    Jump("loc_84A")

    label("loc_838")

    SetMapObjFrame(0x4, "root", 0x2, "off")
    SetMapObjFlags(0x4, 0x2)

    label("loc_84A")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1D, 0x0, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x1, 0xA, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x2, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x3, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x4, 0xD, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x5, 0xE, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x6, 0xF, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEE")
    OP_70(0x5, 0x0)
    Jump("loc_BF2")

    label("loc_BEE")

    OP_70(0x5, 0x1E)

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C05")
    OP_70(0x6, 0x0)
    Jump("loc_C09")

    label("loc_C05")

    OP_70(0x6, 0x1E)

    label("loc_C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C19")
    Sound(129, 1, 100, 0)

    label("loc_C19")

    Call(0, 3)
    Return()

    # Function_2_748 end

    def Function_3_C1D(): pass

    label("Function_3_C1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C51")
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_C57")

    label("loc_C51")

    ClearMapObjFlags(0x6, 0x4)

    label("loc_C57")

    Return()

    # Function_3_C1D end

    def Function_4_C58(): pass

    label("Function_4_C58")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E14")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D51")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_CB1():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CB1)

    def lambda_CCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CCB)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_66C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D32"),
        (2, "loc_D41"),
        (1, "loc_D4E"),
        (SWITCH_DEFAULT, "loc_D51"),
    )


    label("loc_D32")

    SetScenarioFlags(0x75, 6)
    OP_70(0x5, 0x1E)
    Sleep(500)
    Jump("loc_D51")

    label("loc_D41")

    OP_70(0x5, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D4E")

    OP_B7(0x0)
    Return()

    label("loc_D51")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('龙华树之服', 1)"), scpexpr(EXPR_END)), "loc_DA8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11C, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_E0F")

    label("loc_DA8")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '龙华树之服'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E0F")

    Jump("loc_E46")

    label("loc_E14")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_E46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C58 end

    def Function_5_E52(): pass

    label("Function_5_E52")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3F")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_ED1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11C, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_F3A")

    label("loc_ED1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F3A")

    Jump("loc_F7C")

    label("loc_F3F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_F7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E52 end

    def Function_6_F88(): pass

    label("Function_6_F88")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 2)), scpexpr(EXPR_END)), "loc_FC3")
    TalkBegin(0xFF)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门已经被打开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_10AB")

    label("loc_FC3")

    EventBegin(0x1)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上挂着锁。\x01",
            "要打开吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A4")
    Fade(500)
    SetChrPos(0x0, -15520, 8000, -260, 285)
    SetChrPos(0x1, -14110, 8000, 400, 285)
    SetChrPos(0x2, -14300, 8000, -900, 285)
    SetChrPos(0x3, -12190, 8000, 350, 285)
    OP_68(-12910, 8600, 1580, 0)
    MoveCamera(60, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    Sleep(1000)
    Sound(119, 0, 100, 0)
    SetMapObjFrame(0x4, "root", 0x2, "move")
    Sleep(1500)
    ClearMapObjFlags(0x4, 0x2)
    SetScenarioFlags(0xD4, 2)

    label("loc_10A4")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_10AB")

    Return()

    # Function_6_F88 end

    SaveToFile()

Try(main)
