from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1582.bin",                # FileName
        "c1582",                    # MapName
        "c1582",                    # Location
        0x00B5,                     # MapIndex
        "ed7352",
        0x00000000,                 # Flags
        ("c1582", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 160000, 0, -4000, 0, 0, 1, 181, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1582",                  # 0
        "デヴァイン・デルフ",     # 1
        "bc1530",                 # 2
        "bc1530",                 # 3
        "bc1530",                 # 4
        "bc1520",                 # 5
    ))

    ATBonus("ATBonus_3D0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3E0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_3016", 9,   9,   9,   9,   0,   12,  10)
    Sepith("Sepith_301E", 16,  4,   16,  4,   12,  4,   4)
    Sepith("Sepith_3026", 0,   18,  0,   18,  4,   6,   12)

    MonsterBattlePostion("MonsterBattlePostion_420", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_484", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_488", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_48C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_490", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_494", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_498", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_400", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 2, 13, 180)

    # monster count: 14

    BattleInfo(
        "BattleInfo_4A0", 0x0000, 95, 6, 60, 6, 1, 30, 0, "bc1530", "Sepith_3016", 40, 30, 20, 10,
        (
            ("ms79100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79100.dat", "ms79300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_400", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79100.dat", "ms79300.dat", "ms79300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79100.dat", "ms79300.dat", "ms79300.dat", "ms79300.dat", 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
        )
    )

    BattleInfo(
        "BattleInfo_568", 0x0010, 95, 6, 60, 6, 1, 20, 0, "bc1530", "Sepith_301E", 40, 30, 20, 10,
        (
            ("ms79200.dat", 0, 0, 0, 0, 0, "ms79300.dat", 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79200.dat", "ms82600.dat", 0, 0, 0, 0, "ms79300.dat", 0, "MonsterBattlePostion_400", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79200.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, "ms79300.dat", 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79200.dat", "ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, "ms79300.dat", 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
        )
    )

    BattleInfo(
        "BattleInfo_630", 0x0000, 95, 6, 60, 10, 1, 35, 0, "bc1530", "Sepith_3026", 40, 30, 20, 10,
        (
            ("ms79300.dat", "ms79300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_400", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79300.dat", "ms82600.dat", "ms79300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79300.dat", "ms82600.dat", "ms79300.dat", "ms82600.dat", 0, 0, 0, 0, "MonsterBattlePostion_400", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
            ("ms79300.dat", "ms82600.dat", "ms79300.dat", "ms82600.dat", "ms79300.dat", 0, 0, 0, "MonsterBattlePostion_420", "MonsterBattlePostion_480", "ed7450", "ed7453", "ATBonus_3D0"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6F8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bc1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79100.dat", "ms79100.dat", "ms79100.dat", "ms79100.dat", "ms79300.dat", "ms79300.dat", "ms79300.dat", "ms79300.dat", "MonsterBattlePostion_400", "MonsterBattlePostion_480", "ed7451", "ed7453", "ATBonus_3E0"),
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "monster/ch82650.itc",               # 12
        "monster/ch82651.itc",               # 13
        "monster/ch79150.itc",               # 14
        "monster/ch79151.itc",               # 15
        "monster/ch79250.itc",               # 16
        "monster/ch79250.itc",               # 17
        "monster/ch79350.itc",               # 18
        "monster/ch79350.itc",               # 19
    ))

    DeclNpc(-160029, 500,     -1509,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(20190,   19110,   10000,   0x1010110,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(-20550,  19310,   10000,   0x1010084,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(-20790,  -19450,  0,       0x101008A,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(-2340,   -23360,  0,       0x1010033,    "BattleInfo_568", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(19920,   -19820,  0,       0x101013A,    "BattleInfo_630", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-18500,  -340,    30250,   0x1010058,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(-19150,  -19850,  30250,   0x1010139,    "BattleInfo_568", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(20,      -20520,  35500,   0x101010B,    "BattleInfo_630", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(19680,   -17440,  40250,   0x1010138,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(19610,   -130,    40250,   0x101002E,    "BattleInfo_630", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(19320,   17210,   40250,   0x1010088,    "BattleInfo_568", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(-160,    20440,   45500,   0x1010057,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)
    DeclMonster(-20390,  10890,   50250,   0x1010156,    "BattleInfo_630", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-21050,  -1080,   50250,   0x1010136,    "BattleInfo_4A0", 0,   20,  0xFFFF, 0,  1)

    DeclActor(-160030, 0,       -1510,   1200,    -160030, 1000,    -1510,   0x007C, 0,  3,  0x0000)
    DeclActor(0,       0,       -15000,  1200,    0,       1000,    -15000,  0x007C, 0,  5,  0x0000)
    DeclActor(0,       10000,   10000,   1200,    0,       11000,   10000,   0x007C, 0,  6,  0x0000)
    DeclActor(0,       30000,   10000,   1200,    0,       31000,   10000,   0x007C, 0,  6,  0x0000)
    DeclActor(17000,   40250,   0,       1200,    17000,   41250,   0,       0x007C, 0,  7,  0x0000)
    DeclActor(0,       75000,   28500,   1200,    0,       76000,   28500,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_7AC",          # 00, 0
        "Function_1_7C8",          # 01, 1
        "Function_2_7E3",          # 02, 2
        "Function_3_198C",         # 03, 3
        "Function_4_1BA3",         # 04, 4
        "Function_5_1BA7",         # 05, 5
        "Function_6_1DED",         # 06, 6
        "Function_7_2378",         # 07, 7
        "Function_8_26DF",         # 08, 8
        "Function_9_2A30",         # 09, 9
    ))


    def Function_0_7AC(): pass

    label("Function_0_7AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C7")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_7AC")

    label("loc_7C7")

    Return()

    # Function_0_7AC end

    def Function_1_7C8(): pass

    label("Function_1_7C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E2")
    Event(0, 9)

    label("loc_7E2")

    Return()

    # Function_1_7C8 end

    def Function_2_7E3(): pass

    label("Function_2_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7")
    OP_C9(0x0, 0x8)

    label("loc_7F7")

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
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, 9990, 15000, 5000, 2000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -15000, 30250, 0, 5000, 2000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -15000, 50250, 0, 5000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 0, 50250, -15000, 5000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 15000, 75000, 0, 5000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -15000, 75000, 0, 5000, 2000, 90000)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita02a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita04_add", 0x0, 0x1)
    Switch(
        (scpexpr(EXPR_23, 0x1), scpexpr(EXPR_END)),
        (0, "loc_15CC"),
        (1, "loc_1617"),
        (2, "loc_1661"),
        (3, "loc_16AC"),
        (4, "loc_16E6"),
        (SWITCH_DEFAULT, "loc_1713"),
    )


    label("loc_15CC")

    SetBarrier(0x2, 0x1, 0x1)
    OP_71(0xB, 0x64, 0x69, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    Jump("loc_1713")

    label("loc_1617")

    SetBarrier(0x2, 0x0, 0x1)
    OP_71(0xB, 0x0, 0x5, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    Jump("loc_1713")

    label("loc_1661")

    SetBarrier(0x2, 0x1, 0x1)
    OP_71(0xB, 0x64, 0x69, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    Jump("loc_1713")

    label("loc_16AC")

    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    OP_71(0xB, 0xC8, 0xCD, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    Jump("loc_1713")

    label("loc_16E6")

    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    OP_71(0xB, 0x12C, 0x131, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01d_add", 0x1, 0x1)
    Jump("loc_1713")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 3)), scpexpr(EXPR_END)), "loc_1730")
    SetMapObjFrame(0xFF, "monita01_add", 0x1, 0x1)

    label("loc_1730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 4)), scpexpr(EXPR_END)), "loc_174D")
    SetMapObjFrame(0xFF, "monita03_add", 0x1, 0x1)

    label("loc_174D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 5)), scpexpr(EXPR_END)), "loc_176A")
    SetMapObjFrame(0xFF, "monita04_add", 0x1, 0x1)

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_180D")
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mahou01d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "suikomi_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rai00_add", 0x0, 0x1)

    label("loc_180D")

    OP_C3(0x0, 0x6, 0x3, 0xA, 0x0, 0x1, 0, -1000, 0, 20000, 2000, 0)
    OP_C3(0x1, 0x6, 0x3, 0xA, 0x0, 0x1, 0, 9000, 0, 20000, 2000, 0)
    OP_C3(0x2, 0x6, 0x3, 0xA, 0x0, 0x1, 0, 29000, 0, 22000, 2000, 0)
    OP_C3(0x3, 0x6, 0x3, 0xA, 0x0, 0x1, 0, 39000, 0, 22000, 2000, 0)
    OP_C3(0x4, 0x6, 0x3, 0xA, 0x0, 0x1, 0, 49000, 0, 21000, 2000, 0)
    OP_C3(0x5, 0x6, 0x3, 0xA, 0x0, 0x1, 0, 74000, 0, 50000, 30000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg0.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1900")
    OP_70(0x6, 0x0)
    Jump("loc_1904")

    label("loc_1900")

    OP_70(0x6, 0x1E)

    label("loc_1904")

    OP_1C(0x0, 0x7, 0x0, 0x32, 0x0, 0x4, 0x0, 0x0)
    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0x4, 0x0, 0x0)
    OP_1C(0x0, 0x9, 0x0, 0x32, 0x0, 0x4, 0x0, 0x0)
    OP_1C(0x0, 0xA, 0x0, 0x32, 0x0, 0x4, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Sound(927, 1, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1988")
    Sound(933, 1, 80, 0)
    Jump("loc_198B")

    label("loc_1988")

    OP_24(0x3A5)

    label("loc_198B")

    Return()

    # Function_2_7E3 end

    def Function_3_198C(): pass

    label("Function_3_198C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5D")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8B")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_19E9():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19E9)

    def lambda_1A03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A03)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_6F8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1A6C"),
        (2, "loc_1A7B"),
        (1, "loc_1A88"),
        (SWITCH_DEFAULT, "loc_1A8B"),
    )


    label("loc_1A6C")

    SetScenarioFlags(0x218, 3)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_1A8B")

    label("loc_1A7B")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A88")

    OP_B9(0x0)
    Return()

    label("loc_1A8B")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x86, 1)"), scpexpr(EXPR_END)), "loc_1AE8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F9, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1B58")

    label("loc_1AE8")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B58")

    Jump("loc_1B97")

    label("loc_1B5D")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1B97")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_198C end

    def Function_4_1BA3(): pass

    label("Function_4_1BA3")

    Call(1, 6)
    Return()

    # Function_4_1BA3 end

    def Function_5_1BA7(): pass

    label("Function_5_1BA7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEB")
    TalkBegin(0xFF)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1DEC")

    label("loc_1BEB")

    EventBegin(0x1)
    SoundLoad(579)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの操作盤がある。\x01",
            "遠隔操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE1")
    OP_E2(0x3)
    OP_69(0x0, 0x0)
    Fade(500)
    OP_68(0, 1000, -16540, 0)
    MoveCamera(28, 39, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16070, 0)
    SetChrPos(0x0, 0, 0, -16200, 0)
    SetChrPos(0x1, 800, 0, -17000, 0)
    SetChrPos(0x2, -800, 0, -17000, 0)
    SetChrPos(0x3, 0, 0, -17800, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita01_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 15000, 0, 0)
    MoveCamera(224, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(70070, 0)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    OP_0D()
    Sleep(500)
    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0x1F9, 0x258, 0x0, 0x0)
    OP_68(0, 0, 0, 4000)
    MoveCamera(204, 33, 0, 4000)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1800)
    SetMapObjFrame(0xFF, "mahou01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    OP_71(0xB, 0x0, 0x5, 0x0, 0x20)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1B6, 3)
    OP_E2(0x2)

    label("loc_1DE1")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_1DEC")

    Return()

    # Function_5_1BA7 end

    def Function_6_1DED(): pass

    label("Function_6_1DED")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E3A")
    TalkBegin(0xFF)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2377")

    label("loc_1E3A")

    EventBegin(0x1)
    SoundLoad(579)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの操作盤がある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236C")
    OP_E2(0x3)
    OP_69(0x0, 0x0)
    Fade(500)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F30")
    OP_68(0, 11000, 11200, 0)
    MoveCamera(147, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13570, 0)
    SetChrPos(0x0, 0, 10000, 11200, 180)
    SetChrPos(0x1, -800, 10000, 12000, 180)
    SetChrPos(0x2, 800, 10000, 12000, 180)
    SetChrPos(0x3, 0, 10000, 12800, 180)
    Jump("loc_1FA2")

    label("loc_1F30")

    OP_68(0, 31250, 11200, 0)
    MoveCamera(147, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13570, 0)
    SetChrPos(0x0, 0, 30250, 11200, 180)
    SetChrPos(0x1, -800, 30250, 12000, 180)
    SetChrPos(0x2, 800, 30250, 12000, 180)
    SetChrPos(0x3, 0, 30250, 12800, 180)

    label("loc_1FA2")

    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita02a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203F")
    OP_68(0, 11000, 11200, 0)
    MoveCamera(147, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22110, 0)
    SetMapObjFrame(0xFF, "mahou01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    Jump("loc_208E")

    label("loc_203F")

    OP_68(0, 31250, 11200, 0)
    MoveCamera(147, 38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22110, 0)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)

    label("loc_208E")

    SetMapObjFrame(0xFF, "monita02a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x0, 0x1)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    SetChrFlags(0x3, 0x4)
    SetChrFlags(0x0, 0x40)
    SetChrFlags(0x1, 0x40)
    SetChrFlags(0x2, 0x40)
    SetChrFlags(0x3, 0x40)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    SetChrFlags(0x3, 0x20)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x2, 0x1000)
    SetChrFlags(0x3, 0x1000)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221D")
    OP_68(-190, 31000, 10950, 4000)
    MoveCamera(160, 40, 0, 4000)
    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0x5, 0x64, 0x0, 0x0)

    def lambda_2153():
        OP_96(0xFE, 0x0, 0x762A, 0x2BC0, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2153)

    def lambda_216D():
        OP_96(0xFE, 0xFFFFFCE0, 0x762A, 0x2EE0, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_216D)

    def lambda_2187():
        OP_96(0xFE, 0x320, 0x762A, 0x2EE0, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2187)

    def lambda_21A1():
        OP_96(0xFE, 0x0, 0x762A, 0x3200, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_21A1)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1200)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    OP_71(0xB, 0x64, 0x69, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    Jump("loc_231A")

    label("loc_221D")

    OP_68(-190, 11000, 10950, 4000)
    MoveCamera(160, 40, 0, 4000)
    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0x1F9, 0x258, 0x0, 0x0)

    def lambda_2256():
        OP_96(0xFE, 0x0, 0x2710, 0x2BC0, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2256)

    def lambda_2270():
        OP_96(0xFE, 0xFFFFFCE0, 0x2710, 0x2EE0, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2270)

    def lambda_228A():
        OP_96(0xFE, 0x320, 0x2710, 0x2EE0, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_228A)

    def lambda_22A4():
        OP_96(0xFE, 0x0, 0x2710, 0x3200, 0x1900, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_22A4)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1200)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    OP_71(0xB, 0x0, 0x5, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)

    label("loc_231A")

    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    ClearChrFlags(0x3, 0x4)
    ClearChrFlags(0x0, 0x40)
    ClearChrFlags(0x1, 0x40)
    ClearChrFlags(0x2, 0x40)
    ClearChrFlags(0x3, 0x40)
    ClearChrFlags(0x0, 0x20)
    ClearChrFlags(0x1, 0x20)
    ClearChrFlags(0x2, 0x20)
    ClearChrFlags(0x3, 0x20)
    ClearChrFlags(0x0, 0x1000)
    ClearChrFlags(0x1, 0x1000)
    ClearChrFlags(0x2, 0x1000)
    ClearChrFlags(0x3, 0x1000)
    OP_E2(0x2)

    label("loc_236C")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_2377")

    Return()

    # Function_6_1DED end

    def Function_7_2378(): pass

    label("Function_7_2378")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23C5")
    TalkBegin(0xFF)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_26DE")

    label("loc_23C5")

    EventBegin(0x1)
    SoundLoad(579)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの操作盤がある。\x01",
            "遠隔操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D3")
    OP_E2(0x3)
    OP_69(0x0, 0x0)
    Fade(500)
    OP_68(18470, 41250, 40, 0)
    MoveCamera(236, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13090, 0)
    SetChrPos(0x0, 18500, 40250, 0, 270)
    SetChrPos(0x1, 19500, 40250, 800, 270)
    SetChrPos(0x2, 19500, 40250, -800, 270)
    SetChrPos(0x3, 20500, 40250, 0, 270)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita03_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2549")
    OP_68(0, 41250, 0, 0)
    MoveCamera(243, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(56720, 0)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    Jump("loc_2598")

    label("loc_2549")

    OP_68(0, 41250, 0, 0)
    MoveCamera(223, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(56720, 0)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)

    label("loc_2598")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2634")
    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0x69, 0xC8, 0x0, 0x0)
    OP_68(0, 50250, 0, 4000)
    MoveCamera(223, 45, 0, 4000)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1200)
    OP_71(0xB, 0xC8, 0xCD, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    Jump("loc_26CE")

    label("loc_2634")

    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0x195, 0x1F4, 0x0, 0x0)
    OP_68(0, 31250, 0, 4000)
    MoveCamera(243, 45, 0, 4000)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1200)
    OP_71(0xB, 0x64, 0x69, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita02b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)

    label("loc_26CE")

    SetScenarioFlags(0x1B6, 4)
    OP_E2(0x2)

    label("loc_26D3")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_26DE")

    Return()

    # Function_7_2378 end

    def Function_8_26DF(): pass

    label("Function_8_26DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_272C")
    TalkBegin(0xFF)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2A2F")

    label("loc_272C")

    EventBegin(0x1)
    SoundLoad(579)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの操作盤がある。\x01",
            "遠隔操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A24")
    OP_E2(0x3)
    OP_69(0x0, 0x0)
    Fade(500)
    OP_68(1010, 78150, 30520, 0)
    MoveCamera(214, 48, 0, 0)
    OP_6E(820, 0)
    SetCameraDistance(8250, 0)
    SetChrPos(0x0, 0, 75000, 29500, 180)
    SetChrPos(0x1, -800, 75000, 30500, 180)
    SetChrPos(0x2, 800, 75000, 30500, 180)
    SetChrPos(0x3, 0, 75000, 31500, 180)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita04_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 68150, 0, 0)
    MoveCamera(213, 36, 0, 0)
    OP_6E(820, 0)
    SetCameraDistance(55990, 0)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C9")
    OP_68(0, 68150, 0, 0)
    MoveCamera(213, 36, 0, 0)
    OP_6E(820, 0)
    SetCameraDistance(55990, 0)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    Jump("loc_290B")

    label("loc_28C9")

    OP_68(0, 78150, 0, 0)
    MoveCamera(233, 36, 0, 0)
    OP_6E(820, 0)
    SetCameraDistance(55990, 0)
    SetMapObjFrame(0xFF, "mahou01d_add", 0x0, 0x1)

    label("loc_290B")

    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299A")
    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0xCD, 0x12C, 0x0, 0x0)
    OP_68(0, 78150, 0, 4000)
    MoveCamera(233, 36, 0, 4000)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1200)
    OP_71(0xB, 0x12C, 0x131, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01d_add", 0x1, 0x1)
    Jump("loc_2A1F")

    label("loc_299A")

    Sound(579, 2, 80, 0)
    Sound(151, 0, 80, 0)
    OP_71(0xB, 0x131, 0x190, 0x0, 0x0)
    OP_68(0, 68150, 0, 4000)
    MoveCamera(213, 36, 0, 4000)
    OP_D2(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    Sleep(3300)
    OP_24(0x243)
    Sound(151, 0, 80, 0)
    Sleep(1200)
    OP_71(0xB, 0xC8, 0xCD, 0x0, 0x20)
    SetMapObjFrame(0xFF, "mahou01c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)

    label("loc_2A1F")

    SetScenarioFlags(0x1B6, 5)
    OP_E2(0x2)

    label("loc_2A24")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_2A2F")

    Return()

    # Function_8_26DF end

    def Function_9_2A30(): pass

    label("Function_9_2A30")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x0, 0x0)
    OP_68(0, 11000, 24000, 0)
    MoveCamera(180, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17750, 0)
    SetChrPos(0x101, 0, 10000, 23600, 180)
    SetChrPos(0x102, -1000, 10000, 24600, 180)
    SetChrPos(0x103, 900, 10000, 24700, 180)
    SetChrPos(0x104, 0, 10000, 26600, 180)
    SetChrPos(0xF5, 1300, 10000, 26200, 180)
    SetChrPos(0xF4, -1300, 10000, 26200, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 14500, 9000, 4000)
    MoveCamera(180, 39, 0, 4000)
    SetCameraDistance(47000, 4000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x101, 0, -40000, 23600, 180)
    SetChrPos(0x102, -1000, -40000, 24600, 180)
    SetChrPos(0x103, 1000, -40000, 24600, 180)
    SetChrPos(0x104, 0, -40000, 26600, 180)
    SetChrPos(0xF5, 1300, -40000, 26200, 180)
    SetChrPos(0xF4, -1300, -40000, 26200, 180)
    OP_68(0, -4000, 0, 0)
    MoveCamera(90, -40, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(55500, 0)
    MoveCamera(180, -40, 0, 10000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C92")

    #C0013
    ChrTalk(
        0x109,
        "#10111F#N凄い……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2C92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CC4")

    #C0014
    ChrTalk(
        0x106,
        "#10712F#N……この光は……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2CC4")


    #C0015
    ChrTalk(
        0x104,
        (
            "#00306F#Nおいおい、こりゃまた\x01",
            "とんでもない場所に出たな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0016
    ChrTalk(
        0x102,
        (
            "#00101F#Nこれは……\x01",
            "七耀の霊子エネルギー？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DB2")

    #C0017
    ChrTalk(
        0x105,
        (
            "#10406F#Nああ、間違いないだろうね。\x02\x03",

            "#10401F四属性のジオフロントを通って\x01",
            "純化されているみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2DB2")


    #C0018
    ChrTalk(
        0x103,
        (
            "#00203F#Nどうやら上層に向けて\x01",
            "吸い上げているようです。\x02\x03",

            "#00201Fあの光に直接当たると\x01",
            "エニグマなどの導力器#6Rオーブメント#にも\x01",
            "影響があるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F16")

    #C0019
    ChrTalk(
        0x10A,
        (
            "#00606F#Nチッ、厄介だな……\x02\x03",

            "#00610F見たところ、上層に抜けるには\x01",
            "光の流れる場所を通るしかない……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00013F#N通る時は一気に駆け抜けるしか\x01",
            "方法は無さそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2F9F")

    label("loc_2F16")


    #C0021
    ChrTalk(
        0x101,
        (
            "#00006F#N見たところ、上層に抜けるには\x01",
            "光の流れる場所を通るしかない……\x02\x03",

            "#00013F通る時は一気に駆け抜けるしか\x01",
            "方法は無さそうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2F9F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 10000, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 4)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_9_2A30 end

    SaveToFile()

Try(main)
