from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1580.bin",                # FileName
        "c1580",                    # MapName
        "c1580",                    # Location
        0x00B4,                     # MapIndex
        "ed7352",
        0x00000000,                 # Flags
        ("c1580", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 165000, 0, 0, 0, 0, 1, 180, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1580",                  # 0
        "bc1510",                 # 1
        "bc1510",                 # 2
        "bc1520",                 # 3
        "bc1510",                 # 4
    ))

    ATBonus("ATBonus_3F8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_255D", 16,  4,   16,  4,   12,  4,   4)
    Sepith("Sepith_254D", 10,  9,   10,  9,   0,   8,   8)
    Sepith("Sepith_2545", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_448", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_428", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 2, 13, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_69C", 0x0010, 95, 6, 60, 4, 1, 20, 0, "bc1510", "Sepith_255D", 60, 25, 10, 0,
        (
            ("ms79200.dat", 0, 0, 0, 0, 0, "ms82600.dat", 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms79200.dat", "ms82600.dat", 0, 0, 0, 0, "ms82600.dat", 0, "MonsterBattlePostion_428", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms79200.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, "ms82600.dat", 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_564", 0x0000, 95, 6, 60, 4, 1, 30, 0, "bc1510", "Sepith_254D", 60, 30, 10, 0,
        (
            ("ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms82600.dat", "ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4C8", 0x0000, 95, 6, 60, 4, 1, 25, 0, "bc1510", "Sepith_2545", 60, 30, 10, 0,
        (
            ("ms85101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms85101.dat", "ms82600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms85101.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_600", 0x0000, 95, 6, 60, 4, 1, 30, 0, "bc1520", "Sepith_254D", 60, 25, 10, 0,
        (
            ("ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_448", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
            ("ms82600.dat", "ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_4A8", "ed7450", "ed7453", "ATBonus_3F8"),
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
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "monster/ch82650.itc",               # 12
        "monster/ch82651.itc",               # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch79250.itc",               # 16
        "monster/ch79250.itc",               # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
    ))

    DeclMonster(-13500,  -4920,   15000,   0x1010045,    "BattleInfo_69C", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-9390,   21590,   19750,   0x10100CA,    "BattleInfo_564", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6710,    16059,   19750,   0x1010017,    "BattleInfo_4C8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(12230,   6740,    25000,   0x1010094,    "BattleInfo_69C", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(2250,    -20040,  29750,   0x1010056,    "BattleInfo_564", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-5090,   -23890,  29750,   0x101000D,    "BattleInfo_4C8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4370,    25220,   39750,   0x10100BD,    "BattleInfo_564", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-2670,   16070,   39750,   0x1010133,    "BattleInfo_4C8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-160850, -104170, 0,       0x1010059,    "BattleInfo_600", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-252100, -94930,  0,       0x1010087,    "BattleInfo_600", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6700,    -12110,  45000,   0x1010041,    "BattleInfo_564", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(11890,   7010,    45000,   0x1010091,    "BattleInfo_4C8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-18680,  13900,   49750,   0x10100D9,    "BattleInfo_69C", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-14050,  4620,    49750,   0x10100C8,    "BattleInfo_4C8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-14080,  -4970,   49750,   0x1010152,    "BattleInfo_4C8", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-13250,  15000,   -7230,   1200,    -13250,  16000,   -7230,   0x007C, 0,  2,  0x0000)
    DeclActor(10970,   25000,   -7610,   1200,    10970,   26000,   -7610,   0x007C, 0,  3,  0x0000)
    DeclActor(-18960,  49750,   16140,   1200,    -18960,  50750,   16140,   0x007C, 0,  4,  0x0000)
    DeclActor(-257529, 0,       -102040, 1200,    -257529, 1000,    -102040, 0x007C, 0,  5,  0x0000)
    DeclActor(-250000, 0,       4330,    1200,    -250000, 1000,    4330,    0x007C, 0,  9,  0x0000)
    DeclActor(0,       45000,   10750,   1200,    0,       46000,   10750,   0x007C, 0,  10, 0x0000)
    DeclActor(163630,  0,       3030,    1200,    163630,  1000,    3030,    0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_7B0",          # 00, 0
        "Function_1_7E3",          # 01, 1
        "Function_2_10E7",         # 02, 2
        "Function_3_1238",         # 03, 3
        "Function_4_1389",         # 04, 4
        "Function_5_14DA",         # 05, 5
        "Function_6_164F",         # 06, 6
        "Function_7_1653",         # 07, 7
        "Function_8_174F",         # 08, 8
        "Function_9_1756",         # 09, 9
        "Function_10_195C",        # 0A, 10
        "Function_11_1B0F",        # 0B, 11
    ))


    def Function_0_7B0(): pass

    label("Function_0_7B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C8")
    ClearScenarioFlags(0x25, 1)
    Call(0, 8)

    label("loc_7C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E2")
    Event(0, 11)

    label("loc_7E2")

    Return()

    # Function_0_7B0 end

    def Function_1_7E3(): pass

    label("Function_1_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7")
    OP_C9(0x0, 0x8)

    label("loc_7F7")

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
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0x15, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    ClearMapObjFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 0)), scpexpr(EXPR_END)), "loc_FAE")
    OP_70(0x8, 0x1E)
    OP_70(0xA, 0x1E)
    OP_70(0x15, 0x1E)
    ClearMapObjFlags(0x8, 0x2)
    ClearMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0x15, 0x2)
    SetMapObjFrame(0xFF, "monita01_add", 0x1, 0x1)
    Jump("loc_FC2")

    label("loc_FAE")

    SetMapObjFrame(0xFF, "monita01_add", 0x0, 0x1)

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 2)), scpexpr(EXPR_END)), "loc_FF8")
    OP_70(0x7, 0x1E)
    OP_70(0x9, 0x1E)
    ClearMapObjFlags(0x7, 0x2)
    ClearMapObjFlags(0x9, 0x2)
    SetMapObjFrame(0xFF, "monita02_add", 0x1, 0x1)
    Jump("loc_100C")

    label("loc_FF8")

    SetMapObjFrame(0xFF, "monita02_add", 0x0, 0x1)

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101F")
    OP_70(0x1, 0x0)
    Jump("loc_1023")

    label("loc_101F")

    OP_70(0x1, 0x1E)

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1036")
    OP_70(0x2, 0x0)
    Jump("loc_103A")

    label("loc_1036")

    OP_70(0x2, 0x1E)

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104D")
    OP_70(0x3, 0x0)
    Jump("loc_1051")

    label("loc_104D")

    OP_70(0x3, 0x1E)

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1064")
    OP_70(0x4, 0x0)
    Jump("loc_1068")

    label("loc_1064")

    OP_70(0x4, 0x1E)

    label("loc_1068")

    OP_1C(0x0, 0xB, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0xC, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0xD, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0xE, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x11, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x12, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x13, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Sound(927, 1, 100, 0)
    Return()

    # Function_1_7E3 end

    def Function_2_10E7(): pass

    label("Function_2_10E7")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E7")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20C, 1)"), scpexpr(EXPR_END)), "loc_1170")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_11E2")

    label("loc_1170")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11E2")

    Jump("loc_122C")

    label("loc_11E7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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

    label("loc_122C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_10E7 end

    def Function_3_1238(): pass

    label("Function_3_1238")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1338")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5F1, 1)"), scpexpr(EXPR_END)), "loc_12C1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5F1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1333")

    label("loc_12C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5F1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5F1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1333")

    Jump("loc_137D")

    label("loc_1338")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_137D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1238 end

    def Function_4_1389(): pass

    label("Function_4_1389")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1489")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x655, 1)"), scpexpr(EXPR_END)), "loc_1412")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x655),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1484")

    label("loc_1412")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x655),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x655),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1484")

    Jump("loc_14CE")

    label("loc_1489")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_14CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1389 end

    def Function_5_14DA(): pass

    label("Function_5_14DA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1618")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x4, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×２００\x01\x07\x02",

            "#57I水のセピス×２００\x01\x07\x02",

            "#58I火のセピス×２００\x01\x07\x02",

            "#59I風のセピス×２００\x01\x07\x02",

            "#60I時のセピス×２００\x01\x07\x02",

            "#61I空のセピス×２００\x01\x07\x02",

            "#62I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F8, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_163D")

    label("loc_1618")


    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_163D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_14DA end

    def Function_6_164F(): pass

    label("Function_6_164F")

    Call(1, 6)
    Return()

    # Function_6_164F end

    def Function_7_1653(): pass

    label("Function_7_1653")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1740")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x14, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x14, 0x0)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x14)
    OP_71(0x14, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x14, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1740")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_7_1653 end

    def Function_8_174F(): pass

    label("Function_8_174F")

    Sound(160, 0, 100, 0)
    Return()

    # Function_8_174F end

    def Function_9_1756(): pass

    label("Function_9_1756")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 0)), scpexpr(EXPR_END)), "loc_1795")
    TalkBegin(0xFF)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_195B")

    label("loc_1795")

    EventBegin(0x1)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1954")
    Fade(500)
    OP_68(-250850, 1300, 2880, 0)
    MoveCamera(40, 40, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16760, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita01_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-243220, 1300, -980, 0)
    MoveCamera(58, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16760, 0)
    OP_0D()
    Sleep(500)
    Sound(164, 0, 100, 0)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x2)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(1200)
    Fade(500)
    OP_68(-154020, 1300, -1270, 0)
    MoveCamera(56, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17640, 0)
    OP_0D()
    Sleep(500)
    Sound(164, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x2)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(1200)
    Fade(500)
    OP_68(14560, 20750, 19190, 0)
    MoveCamera(238, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20720, 0)
    OP_0D()
    Sleep(500)
    Sound(164, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x2)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(1700)
    SetScenarioFlags(0x1B6, 0)

    label("loc_1954")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_195B")

    Return()

    # Function_9_1756 end

    def Function_10_195C(): pass

    label("Function_10_195C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 2)), scpexpr(EXPR_END)), "loc_199B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1B0E")

    label("loc_199B")

    EventBegin(0x1)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B03")
    OP_69(0x0, 0x0)
    Fade(500)
    OP_68(220, 46000, 11700, 0)
    MoveCamera(212, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13640, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita02_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(13210, 46000, -1170, 0)
    MoveCamera(244, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15520, 0)
    OP_0D()
    Sleep(500)
    Sound(164, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x2)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(1200)
    Fade(500)
    OP_68(-23860, 50750, -1010, 0)
    MoveCamera(116, 43, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15520, 0)
    OP_0D()
    Sleep(500)
    Sound(164, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    ClearMapObjFlags(0x9, 0x2)
    Sleep(700)
    Sound(143, 0, 100, 0)
    Sleep(1300)
    SetScenarioFlags(0x1B6, 2)

    label("loc_1B03")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_1B0E")

    Return()

    # Function_10_195C end

    def Function_11_1B0F(): pass

    label("Function_11_1B0F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, 70, 9750, -22000, 0)
    SetChrPos(0x102, -660, 9750, -23530, 0)
    SetChrPos(0x103, 800, 9750, -23330, 0)
    SetChrPos(0xF5, -70, 9750, -25290, 0)
    SetChrPos(0xF4, -1170, 9750, -24900, 0)
    SetChrPos(0x104, 1160, 9750, -25020, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    PlayBGM("ed7572", 0)
    OP_69(0x0, 0x0)
    OP_68(0, 15000, 0, 0)
    MoveCamera(300, -5, -15, 0)
    OP_6E(900, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 48000, 0, 15000)
    MoveCamera(1060, 20, 15, 15000)
    SetCameraDistance(55000, 15000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 25000, 0, 0)
    MoveCamera(255, 57, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(75000, 0)
    OP_68(0, 40000, 0, 8000)
    MoveCamera(285, 57, 0, 8000)
    SetCameraDistance(80000, 8000)
    Sleep(3500)
    PlaceName2(340, 200, "c_plac56", 0x0, 0)
    OP_6F(0x79)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x101,
        "#00011F#N#6P…………な………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0018
    ChrTalk(
        0x102,
        "#00105F#N#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 11000, -22000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    OP_68(0, 20000, -14000, 4000)
    MoveCamera(40, -9, 0, 4000)
    SetCameraDistance(45000, 4000)
    Sleep(1000)
    OP_82(0xC8, 0x64, 0xBB8, 0x1F4)

    #C0019
    ChrTalk(
        0x104,
        "#00307F#5S#22Aな、なんだこりゃああっ！？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10800, 30550, 1710, 0)
    MoveCamera(83, -38, 0, 0)
    MoveCamera(83, -38, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(40110, 0)
    MoveCamera(90, -38, 0, 20000)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF0")

    #C0020
    ChrTalk(
        0x109,
        "#10111F#Nし、信じられない……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E59")

    label("loc_1DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E26")

    #C0021
    ChrTalk(
        0x10A,
        "#00610F#Nし、信じられん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E59")

    label("loc_1E26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E59")

    #C0022
    ChrTalk(
        0x106,
        "#10712F#N……信じられない……\x02",
    )

    CloseMessageWindow()

    label("loc_1E59")

    OP_57(0x0)
    OP_5A()

    #C0023
    ChrTalk(
        0x103,
        (
            "#00206F#Nこれが《魔導科学》の精華……\x02\x03",

            "#00201Fクロイス家の錬金術と\x01",
            "最新の導力技術の融合ですか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F6E")

    #C0024
    ChrTalk(
        0x105,
        (
            "#10406F#N……千年以上にも及ぶ\x01",
            "彼らの妄執を感じるね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F66")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10708F#N（《銀#2Rイン#》の名も\x01",
            "  道を失えばひょっとして……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F66")

    OP_57(0x0)
    OP_5A()
    Jump("loc_2045")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FF3")

    #C0026
    ChrTalk(
        0x106,
        (
            "#10703F#Nこれが千年以上に及ぶ\x01",
            "妄執の果て……\x02\x03",

            "#10708F（《銀#2Rイン#》の名も\x01",
            "  道を失えばひょっとして……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2045")

    #C0027
    ChrTalk(
        0x10A,
        (
            "#00606F#Nこれが千年にも及ぶという\x01",
            "妄執の果てというわけか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2045")

    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00106F#N……その妄執が\x01",
            "《教団》という傀儡#4Rかいらい#を産み落とし……\x02\x03",

            "#00108F数多の人々を犠牲にしてきた……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00006F#Nああ……\x02\x03",

            "#00008F……そして今もなお、\x01",
            "キーアに《至宝》という運命を\x01",
            "押し付けようとしている……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(500)
    OP_68(0, 10750, -23300, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00003F#5P……この場所の是非を\x01",
            "問える立場に俺たちはない。\x02\x03",

            "#00008Fだが、それでも……\x01",
            "この先にキーアやアリオスさん、\x01",
            "大統領たちがいるのなら……\x02\x03",

            "#00013F俺たちは何としても\x01",
            "ここを突破しなくちゃならない。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetCameraDistance(14600, 800)

    def lambda_2262():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2262)

    def lambda_226F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_226F)

    def lambda_227C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_227C)

    def lambda_2289():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2289)
    Sleep(0)

    def lambda_2299():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2299)
    Sleep(0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0031
    ChrTalk(
        0x101,
        (
            "#00007F──行こう、みんな！\x02\x03",

            "過去の妄執と幻想を打ち払い、\x01",
            "現在#4Rい ま#のクロスベルを掴むために！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#00107F#6Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#00207F#12P……はい！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#12P#00307F合点承知だ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C1")

    #C0035
    ChrTalk(
        0x109,
        "#6P#10107F準備は万全です！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2424")

    label("loc_23C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23F4")

    #C0036
    ChrTalk(
        0x10A,
        "#6P#00607F備えは十分だ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2424")

    label("loc_23F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2424")

    #C0037
    ChrTalk(
        0x106,
        "#6P#10707F備えは万全です！\x02",
    )

    CloseMessageWindow()

    label("loc_2424")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_245D")

    #C0038
    ChrTalk(
        0x105,
        "#6P#10407F行くとしようか……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_24C0")

    label("loc_245D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2494")

    #C0039
    ChrTalk(
        0x106,
        "#6P#10707F行きましょう……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_24C0")

    label("loc_2494")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24C0")

    #C0040
    ChrTalk(
        0x10A,
        "#6P#00607F行くぞ……！\x02",
    )

    CloseMessageWindow()

    label("loc_24C0")

    SetCameraDistance(14350, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 9750, -24000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 2)
    OP_29(0xB1, 0x1, 0xB)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7352")
    ReplaceBGM("ed7550", "ed7352")
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_1B0F end

    SaveToFile()

Try(main)
