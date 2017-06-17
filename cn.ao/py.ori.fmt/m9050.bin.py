from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9050.bin",                # FileName
        "m9050",                    # MapName
        "m9050",                    # Location
        0x00C0,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 192, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9050",                  # 0
        "暴君龙",                 # 1
        "暴君龙",                 # 2
        "bm9030",                 # 3
        "bm9030",                 # 4
        "bm9030",                 # 5
        "bm9030",                 # 6
        "bm9030",                 # 7
    ))

    ATBonus("ATBonus_66C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_67C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_425F", 18,  15,  23,  12,  0,   0,   0)
    Sepith("Sepith_4267", 9,   9,   9,   9,   6,   6,   6)
    Sepith("Sepith_4257", 8,   11,  8,   15,  8,   6,   2)

    MonsterBattlePostion("MonsterBattlePostion_6BC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_720", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_724", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_728", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_730", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_734", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_69C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 2, 13, 180)

    # monster count: 21

    BattleInfo(
        "BattleInfo_7D8", 0x0000, 103, 6, 45, 10, 1, 30, 24, "bm9030", "Sepith_425F", 40, 30, 20, 0,
        (
            ("ms87700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms87700.dat", "ms87700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms87700.dat", "ms87700.dat", "ms87700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_874", 0x0000, 103, 6, 45, 10, 1, 40, 24, "bm9030", "Sepith_4267", 80, 20, 0, 0,
        (
            ("ms82003.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms82003.dat", "ms82003.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_73C", 0x0000, 103, 6, 45, 10, 1, 40, 24, "bm9030", "Sepith_4257", 40, 30, 20, 0,
        (
            ("ms78800.dat", "ms78800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms78800.dat", "ms78800.dat", "ms78800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6BC", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            ("ms78800.dat", "ms78800.dat", "ms78800.dat", "ms78800.dat", 0, 0, 0, 0, "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_66C"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_8E4", 0x0C00, 255, 6, 0, 0, 3, 0, 24, "bm9030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87700.dat", "ms87700.dat", "ms87700.dat", "ms78800.dat", "ms78800.dat", "ms87700.dat", "ms78800.dat", "ms87700.dat", "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_67C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_928", 0x0C00, 255, 6, 0, 0, 3, 0, 24, "bm9030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87700.dat", "ms87700.dat", "ms87700.dat", "ms87700.dat", "ms78800.dat", "ms87700.dat", "ms78800.dat", "ms78800.dat", "MonsterBattlePostion_69C", "MonsterBattlePostion_71C", "ed7452", "ed7453", "ATBonus_67C"),
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
        "monster/ch78850.itc",               # 10
        "monster/ch78851.itc",               # 11
        "monster/ch87750.itc",               # 12
        "monster/ch87751.itc",               # 13
        "monster/ch82050.itc",               # 14
        "monster/ch82051.itc",               # 15
    ))

    DeclNpc(48000,   4500,    -15000,  0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-90000,  -3500,   -51500,  0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-19800,  -99480,  0,       0x101000B,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33470,   -89190,  4019,    0x1010153,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(30940,   -65129,  4019,    0x10100C5,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(49150,   -51510,  8029,    0x10100E1,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(26990,   -114680, 30,      0x1010020,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-56300,  -107420, -3980,   0x1010075,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-46760,  -78340,  -4000,   0x10100D2,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-87530,  -55260,  -3980,   0x1010093,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-64890,  -3480,   -3970,   0x101008E,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-76120,  17740,   -4000,   0x1010090,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-22910,  47430,   30,      0x1010124,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-57610,  83990,   -4000,   0x101004D,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(3420,    67390,   30,      0x1010111,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33240,   68170,   0,       0x1010128,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(55460,   45270,   0,       0x1010141,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(67320,   13360,   0,       0x1010089,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(76330,   -18070,  0,       0x101012D,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(64410,   -90760,  0,       0x1010037,    "BattleInfo_7D8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(43270,   -53130,  8029,    0x1010077,    "BattleInfo_874", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(6820,    -49800,  12000,   0x1010059,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-22110,  -58460,  12030,   0x1010040,    "BattleInfo_73C", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-26000,  12000,   -59000,  1200,    -26000,  13000,   -59000,  0x007C, 0,  3,  0x0000)
    DeclActor(-23000,  0,       -104000, 1200,    -23000,  1000,    -104000, 0x007C, 0,  4,  0x0000)
    DeclActor(32000,   8000,    -45000,  1200,    32000,   9000,    -45000,  0x007C, 0,  5,  0x0000)
    DeclActor(58000,   0,       -80000,  1200,    58000,   1000,    -80000,  0x007C, 0,  6,  0x0000)
    DeclActor(92000,   4000,    -50000,  1200,    92000,   5000,    -50000,  0x007C, 0,  7,  0x0000)
    DeclActor(55000,   0,       11000,   1200,    55000,   1000,    11000,   0x007C, 0,  8,  0x0000)
    DeclActor(48000,   4000,    -15000,  1200,    48000,   5000,    -15000,  0x007C, 0,  9,  0x0000)
    DeclActor(-90000,  -4000,   -51500,  1200,    -90000,  -3000,   -51500,  0x007C, 0,  10, 0x0000)
    DeclActor(-71500,  -8000,   78500,   1200,    -71500,  -7000,   78500,   0x007C, 0,  11, 0x0000)
    DeclActor(-63000,  -4000,   81000,   1200,    -63000,  -3000,   81000,   0x007C, 0,  12, 0x0000)
    DeclActor(4000,    0,       -73000,  1200,    4000,    1000,    -73000,  0x007C, 0,  13, 0x0000)
    DeclActor(-24500,  0,       -114000, 1200,    -24500,  1000,    -114000, 0x007C, 0,  14, 0x0000)
    DeclActor(-57000,  0,       -50000,  1200,    -57000,  1000,    -50000,  0x007C, 0,  15, 0x0000)
    DeclActor(-62000,  -4000,   40500,   1200,    -62000,  -3000,   40500,   0x007C, 0,  15, 0x0000)
    DeclActor(-32000,  0,       86000,   1200,    -32000,  1000,    86000,   0x007C, 0,  15, 0x0000)
    DeclActor(101000,  -4000,   12000,   1200,    101000,  -3000,   12000,   0x007C, 0,  15, 0x0000)
    DeclActor(73000,   4000,    -43000,  1200,    73000,   4000,    -43000,  0x007C, 0,  15, 0x0000)
    DeclActor(-12000,  12000,   -34000,  1200,    -12000,  13000,   -34000,  0x007C, 0,  15, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5

    ScpFunction((
        "Function_0_A2C",          # 00, 0
        "Function_1_A4B",          # 01, 1
        "Function_2_A7D",          # 02, 2
        "Function_3_19C1",         # 03, 3
        "Function_4_1AFC",         # 04, 4
        "Function_5_1C37",         # 05, 5
        "Function_6_1D72",         # 06, 6
        "Function_7_1E2D",         # 07, 7
        "Function_8_1F94",         # 08, 8
        "Function_9_20CF",         # 09, 9
        "Function_10_22CD",        # 0A, 10
        "Function_11_24CB",        # 0B, 11
        "Function_12_2606",        # 0C, 12
        "Function_13_2741",        # 0D, 13
        "Function_14_274B",        # 0E, 14
        "Function_15_2755",        # 0F, 15
        "Function_16_281D",        # 10, 16
        "Function_17_2D90",        # 11, 17
        "Function_18_300E",        # 12, 18
        "Function_19_3161",        # 13, 19
        "Function_20_31A2",        # 14, 20
        "Function_21_369E",        # 15, 21
        "Function_22_3708",        # 16, 22
        "Function_23_3772",        # 17, 23
        "Function_24_37DC",        # 18, 24
        "Function_25_3846",        # 19, 25
        "Function_26_38B0",        # 1A, 26
        "Function_27_391A",        # 1B, 27
        "Function_28_3CCF",        # 1C, 28
        "Function_29_4046",        # 1D, 29
    ))


    def Function_0_A2C(): pass

    label("Function_0_A2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4A")
    OP_A1(0xFE, 0x2BC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_A2C")

    label("loc_A4A")

    Return()

    # Function_0_A2C end

    def Function_1_A4B(): pass

    label("Function_1_A4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    Event(0, 17)

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6D")
    Event(0, 20)

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A7C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 29)

    label("loc_A7C")

    Return()

    # Function_1_A4B end

    def Function_2_A7D(): pass

    label("Function_2_A7D")

    OP_F0(0x1, 0x320)
    OP_1B(0x0, 0x0, 0x12)
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
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFrame(0xFF, "hasira_7s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0ss", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_15E6")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0ss", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    Jump("loc_18D4")

    label("loc_15E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 4)), scpexpr(EXPR_END)), "loc_1777")
    SetMapObjFrame(0xA, "black_add", 0x2, "night")
    SetMapObjFrame(0xB, "black_add", 0x2, "night")
    SetMapObjFrame(0xC, "black_add", 0x2, "night")
    SetMapObjFrame(0xD, "black_add", 0x2, "night")
    SetMapObjFrame(0xE, "black_add", 0x2, "night")
    SetMapObjFrame(0xF, "black_add", 0x2, "night")
    SetMapObjFrame(0x10, "black_add", 0x2, "night")
    SetMapObjFrame(0x11, "black_add", 0x2, "night")
    SetMapObjFrame(0xA, "blue", 0x2, "night")
    SetMapObjFrame(0xB, "blue", 0x2, "night")
    SetMapObjFrame(0xC, "blue", 0x2, "night")
    SetMapObjFrame(0xD, "blue", 0x2, "night")
    SetMapObjFrame(0xE, "blue", 0x2, "night")
    SetMapObjFrame(0xF, "blue", 0x2, "night")
    SetMapObjFrame(0x10, "blue", 0x2, "night")
    SetMapObjFrame(0x11, "blue", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "night")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    OP_7D(0xD2, 0xDC, 0xFF, 0x0, 0x0)
    Jump("loc_18D4")

    label("loc_1777")

    SetMapObjFrame(0xA, "black_add", 0x2, "day")
    SetMapObjFrame(0xB, "black_add", 0x2, "day")
    SetMapObjFrame(0xC, "black_add", 0x2, "day")
    SetMapObjFrame(0xD, "black_add", 0x2, "day")
    SetMapObjFrame(0xE, "black_add", 0x2, "day")
    SetMapObjFrame(0xF, "black_add", 0x2, "day")
    SetMapObjFrame(0x10, "black_add", 0x2, "day")
    SetMapObjFrame(0x11, "black_add", 0x2, "day")
    SetMapObjFrame(0xA, "blue", 0x2, "day")
    SetMapObjFrame(0xB, "blue", 0x2, "day")
    SetMapObjFrame(0xC, "blue", 0x2, "day")
    SetMapObjFrame(0xD, "blue", 0x2, "day")
    SetMapObjFrame(0xE, "blue", 0x2, "day")
    SetMapObjFrame(0xF, "blue", 0x2, "day")
    SetMapObjFrame(0x10, "blue", 0x2, "day")
    SetMapObjFrame(0x11, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "day")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E7")
    OP_70(0x0, 0x0)
    Jump("loc_18EB")

    label("loc_18E7")

    OP_70(0x0, 0x1E)

    label("loc_18EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FE")
    OP_70(0x1, 0x0)
    Jump("loc_1902")

    label("loc_18FE")

    OP_70(0x1, 0x1E)

    label("loc_1902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1915")
    OP_70(0x2, 0x0)
    Jump("loc_1919")

    label("loc_1915")

    OP_70(0x2, 0x1E)

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192C")
    OP_70(0x3, 0x0)
    Jump("loc_1930")

    label("loc_192C")

    OP_70(0x3, 0x1E)

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1943")
    OP_70(0x4, 0x0)
    Jump("loc_1947")

    label("loc_1943")

    OP_70(0x4, 0x1E)

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195A")
    OP_70(0x5, 0x0)
    Jump("loc_195E")

    label("loc_195A")

    OP_70(0x5, 0x1E)

    label("loc_195E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1971")
    OP_70(0x6, 0x0)
    Jump("loc_1975")

    label("loc_1971")

    OP_70(0x6, 0x1E)

    label("loc_1975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1988")
    OP_70(0x7, 0x0)
    Jump("loc_198C")

    label("loc_1988")

    OP_70(0x7, 0x1E)

    label("loc_198C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199F")
    OP_70(0x8, 0x0)
    Jump("loc_19A3")

    label("loc_199F")

    OP_70(0x8, 0x1E)

    label("loc_19A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B6")
    OP_70(0x9, 0x0)
    Jump("loc_19BA")

    label("loc_19B6")

    OP_70(0x9, 0x1E)

    label("loc_19BA")

    Sound(124, 1, 100, 0)
    Return()

    # Function_2_A7D end

    def Function_3_19C1(): pass

    label("Function_3_19C1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB3")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药·改', 1)"), scpexpr(EXPR_END)), "loc_1A44")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1AAE")

    label("loc_1A44")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1AAE")

    Jump("loc_1AF0")

    label("loc_1AB3")

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

    label("loc_1AF0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_19C1 end

    def Function_4_1AFC(): pass

    label("Function_4_1AFC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEE")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_1B7F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1BE9")

    label("loc_1B7F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BE9")

    Jump("loc_1C2B")

    label("loc_1BEE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_1C2B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1AFC end

    def Function_5_1C37(): pass

    label("Function_5_1C37")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D29")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('冻结之刃２', 1)"), scpexpr(EXPR_END)), "loc_1CBA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '冻结之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1D24")

    label("loc_1CBA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '冻结之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '冻结之刃２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D24")

    Jump("loc_1D66")

    label("loc_1D29")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_1D66")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1C37 end

    def Function_6_1D72(): pass

    label("Function_6_1D72")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFE")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x1, 2000)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片×２０００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x203, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E1B")

    label("loc_1DFE")


    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1E1B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1D72 end

    def Function_7_1E2D(): pass

    label("Function_7_1E2D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F65")
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

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x203, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1F82")

    label("loc_1F65")


    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1F82")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1E2D end

    def Function_8_1F94(): pass

    label("Function_8_1F94")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2086")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('全回复药', 1)"), scpexpr(EXPR_END)), "loc_2017")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '全回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_2081")

    label("loc_2017")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '全回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '全回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2081")

    Jump("loc_20C3")

    label("loc_2086")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
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

    label("loc_20C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1F94 end

    def Function_9_20CF(): pass

    label("Function_9_20CF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228F")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CC")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_212C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_212C)

    def lambda_2146():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2146)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0017
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
    Battle("BattleInfo_8E4", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_21AD"),
        (2, "loc_21BC"),
        (1, "loc_21C9"),
        (SWITCH_DEFAULT, "loc_21CC"),
    )


    label("loc_21AD")

    SetScenarioFlags(0x218, 6)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_21CC")

    label("loc_21BC")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_21C9")

    OP_B9(0x0)
    Return()

    label("loc_21CC")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('灵剑·莫邪', 1)"), scpexpr(EXPR_END)), "loc_2223")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0018
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '灵剑·莫邪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_228A")

    label("loc_2223")

    FadeToDark(300, 0, 100)

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '灵剑·莫邪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '灵剑·莫邪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_228A")

    Jump("loc_22C1")

    label("loc_228F")

    FadeToDark(300, 0, 100)

    #A0020
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

    label("loc_22C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_20CF end

    def Function_10_22CD(): pass

    label("Function_10_22CD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248D")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CA")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_232A():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_232A)

    def lambda_2344():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2344)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0021
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_928", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_23AB"),
        (2, "loc_23BA"),
        (1, "loc_23C7"),
        (SWITCH_DEFAULT, "loc_23CA"),
    )


    label("loc_23AB")

    SetScenarioFlags(0x218, 7)
    OP_70(0x7, 0x1E)
    Sleep(500)
    Jump("loc_23CA")

    label("loc_23BA")

    OP_70(0x7, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_23C7")

    OP_B9(0x0)
    Return()

    label("loc_23CA")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('七耀极星圣衣', 1)"), scpexpr(EXPR_END)), "loc_2421")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0022
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '七耀极星圣衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x203, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_2488")

    label("loc_2421")

    FadeToDark(300, 0, 100)

    #A0023
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '七耀极星圣衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '七耀极星圣衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2488")

    Jump("loc_24BF")

    label("loc_248D")

    FadeToDark(300, 0, 100)

    #A0024
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

    label("loc_24BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_22CD end

    def Function_11_24CB(): pass

    label("Function_11_24CB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BD")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('寂静之蓝', 1)"), scpexpr(EXPR_END)), "loc_254E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '寂静之蓝'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x204, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_25B8")

    label("loc_254E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '寂静之蓝'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '寂静之蓝'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_25B8")

    Jump("loc_25FA")

    label("loc_25BD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0027
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

    label("loc_25FA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_24CB end

    def Function_12_2606(): pass

    label("Function_12_2606")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F8")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_2689")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x204, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_26F3")

    label("loc_2689")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_26F3")

    Jump("loc_2735")

    label("loc_26F8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0030
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

    label("loc_2735")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_2606 end

    def Function_13_2741(): pass

    label("Function_13_2741")

    SetScenarioFlags(0x0, 0)
    Call(0, 15)
    ClearScenarioFlags(0x0, 0)
    Return()

    # Function_13_2741 end

    def Function_14_274B(): pass

    label("Function_14_274B")

    SetScenarioFlags(0x0, 1)
    Call(0, 15)
    ClearScenarioFlags(0x0, 1)
    Return()

    # Function_14_274B end

    def Function_15_2755(): pass

    label("Function_15_2755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_278B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经没有反应了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2815")

    label("loc_278B")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一块水晶。\x01",
            "要触碰吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_27ED")
    Call(0, 27)

    label("loc_27ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27F9")
    Call(0, 28)

    label("loc_27F9")

    Return()

    label("loc_27FA")

    Fade(500)
    SetCameraDistance(35000, 0)
    OP_0D()
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Call(0, 16)

    label("loc_2815")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_2755 end

    def Function_16_281D(): pass

    label("Function_16_281D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 4)), scpexpr(EXPR_END)), "loc_282E")
    ClearScenarioFlags(0x1B0, 4)
    Jump("loc_2831")

    label("loc_282E")

    SetScenarioFlags(0x1B0, 4)

    label("loc_2831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 4)), scpexpr(EXPR_END)), "loc_2AF9")
    OP_7D(0xD2, 0xDC, 0xFF, 0x0, 0x1388)
    SetMapObjFrame(0xA, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xB, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xC, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xD, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xE, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xF, "black_add", 0x2, "to_n")
    SetMapObjFrame(0x10, "black_add", 0x2, "to_n")
    SetMapObjFrame(0x11, "black_add", 0x2, "to_n")
    SetMapObjFrame(0xA, "blue", 0x2, "to_n")
    SetMapObjFrame(0xB, "blue", 0x2, "to_n")
    SetMapObjFrame(0xC, "blue", 0x2, "to_n")
    SetMapObjFrame(0xD, "blue", 0x2, "to_n")
    SetMapObjFrame(0xE, "blue", 0x2, "to_n")
    SetMapObjFrame(0xF, "blue", 0x2, "to_n")
    SetMapObjFrame(0x10, "blue", 0x2, "to_n")
    SetMapObjFrame(0x11, "blue", 0x2, "to_n")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "to_n")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "to_n")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "to_n")
    Sleep(1300)
    Sound(278, 0, 50, 0)
    Sleep(1900)
    SetMapObjFrame(0xA, "black_add", 0x2, "night")
    SetMapObjFrame(0xB, "black_add", 0x2, "night")
    SetMapObjFrame(0xC, "black_add", 0x2, "night")
    SetMapObjFrame(0xD, "black_add", 0x2, "night")
    SetMapObjFrame(0xE, "black_add", 0x2, "night")
    SetMapObjFrame(0xF, "black_add", 0x2, "night")
    SetMapObjFrame(0x10, "black_add", 0x2, "night")
    SetMapObjFrame(0x11, "black_add", 0x2, "night")
    SetMapObjFrame(0xA, "blue", 0x2, "night")
    SetMapObjFrame(0xB, "blue", 0x2, "night")
    SetMapObjFrame(0xC, "blue", 0x2, "night")
    SetMapObjFrame(0xD, "blue", 0x2, "night")
    SetMapObjFrame(0xE, "blue", 0x2, "night")
    SetMapObjFrame(0xF, "blue", 0x2, "night")
    SetMapObjFrame(0x10, "blue", 0x2, "night")
    SetMapObjFrame(0x11, "blue", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "night")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "night")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    Jump("loc_2D8D")

    label("loc_2AF9")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1388)
    SetMapObjFrame(0xA, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xB, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xC, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xD, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xE, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xF, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x10, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x11, "black_add", 0x2, "to_d")
    SetMapObjFrame(0xA, "blue", 0x2, "to_d")
    SetMapObjFrame(0xB, "blue", 0x2, "to_d")
    SetMapObjFrame(0xC, "blue", 0x2, "to_d")
    SetMapObjFrame(0xD, "blue", 0x2, "to_d")
    SetMapObjFrame(0xE, "blue", 0x2, "to_d")
    SetMapObjFrame(0xF, "blue", 0x2, "to_d")
    SetMapObjFrame(0x10, "blue", 0x2, "to_d")
    SetMapObjFrame(0x11, "blue", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "to_d")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "to_d")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "to_d")
    Sleep(1300)
    Sound(278, 0, 50, 0)
    Sleep(1900)
    SetMapObjFrame(0xA, "black_add", 0x2, "day")
    SetMapObjFrame(0xB, "black_add", 0x2, "day")
    SetMapObjFrame(0xC, "black_add", 0x2, "day")
    SetMapObjFrame(0xD, "black_add", 0x2, "day")
    SetMapObjFrame(0xE, "black_add", 0x2, "day")
    SetMapObjFrame(0xF, "black_add", 0x2, "day")
    SetMapObjFrame(0x10, "black_add", 0x2, "day")
    SetMapObjFrame(0x11, "black_add", 0x2, "day")
    SetMapObjFrame(0xA, "blue", 0x2, "day")
    SetMapObjFrame(0xB, "blue", 0x2, "day")
    SetMapObjFrame(0xC, "blue", 0x2, "day")
    SetMapObjFrame(0xD, "blue", 0x2, "day")
    SetMapObjFrame(0xE, "blue", 0x2, "day")
    SetMapObjFrame(0xF, "blue", 0x2, "day")
    SetMapObjFrame(0x10, "blue", 0x2, "day")
    SetMapObjFrame(0x11, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_5d", 0x2, "day")
    SetMapObjFrame(0xFF, "hasira_6n", 0x2, "day")
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)

    label("loc_2D8D")

    OP_E2(0x4)
    Return()

    # Function_16_281D end

    def Function_17_2D90(): pass

    label("Function_17_2D90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    OP_68(-2630, 1500, -103410, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13980, 0)
    SetChrPos(0x0, -3000, 0, -102500, 45)
    SetChrPos(0x1, -3000, 0, -102500, 45)
    SetChrPos(0x2, -3000, 0, -102500, 45)
    SetChrPos(0x3, -3000, 0, -102500, 45)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2E9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2E9E)

    def lambda_2EAF():
        OP_95(0xFE, -860, 0, -100390, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2EAF)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2F06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2F06)

    def lambda_2F17():
        OP_95(0xFE, -1940, 0, -99810, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2F17)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2F74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2F74)

    def lambda_2F85():
        OP_95(0xFE, -440, 0, -101980, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2F85)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2FDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2FDC)

    def lambda_2FED():
        OP_95(0xFE, -590, 0, -103280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2FED)
    WaitChrThread(0x3, 1)
    Sleep(1000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_2D90 end

    def Function_18_300E(): pass

    label("Function_18_300E")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3067():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3067)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_30B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_30B2)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_30FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_30FD)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3148():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_3148)
    Sleep(1000)
    NewScene("m9002", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_18_300E end

    def Function_19_3161(): pass

    label("Function_19_3161")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3179")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_3179")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_318D")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_318D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A1")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_31A1")

    Return()

    # Function_19_3161 end

    def Function_20_31A2(): pass

    label("Function_20_31A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    LoadEffect(0x1, "event\\ev202_00.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31DC")
    Call(0, 19)

    label("loc_31DC")

    SetChrPos(0xF4, -3000, 0, -102500, 20)
    SetChrPos(0x101, -3000, 0, -102500, 39)
    SetChrPos(0x103, -3000, 0, -102500, 26)
    SetChrPos(0x102, -3000, 0, -102500, 2)
    SetChrPos(0x104, -3000, 0, -102500, 52)
    SetChrPos(0xF5, -3000, 0, -102500, 352)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-15370, 5300, -100130, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18410, 0)
    OP_68(-14530, 5300, -82830, 6000)
    MoveCamera(3, 12, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(18410, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-2970, 4790, -102780, 0)
    MoveCamera(9, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(69700, 0)
    OP_68(-2960, 4790, -102730, 7500)
    MoveCamera(3, 11, 0, 7500)
    OP_6E(600, 7500)
    SetCameraDistance(69700, 7500)
    Sleep(1000)
    PlaceName2(340, 200, "c_plac59", 0x0, 0)
    Sleep(500)
    BeginChrThread(0xF4, 0, 0, 21)
    Sound(920, 0, 40, 0)
    Sleep(600)
    BeginChrThread(0x101, 0, 0, 22)
    Sleep(600)
    BeginChrThread(0x102, 0, 0, 23)
    Sound(920, 0, 40, 0)
    Sleep(600)
    BeginChrThread(0x103, 0, 0, 24)
    Sleep(600)
    BeginChrThread(0x104, 0, 0, 25)
    Sound(920, 0, 40, 0)
    Sleep(600)
    BeginChrThread(0xF5, 0, 0, 26)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-1400, 1300, -99100, 0)
    MoveCamera(352, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-1290, 1300, -98150, 0)
    MoveCamera(345, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345B")

    #C0033
    ChrTalk(
        0x102,
        "#00105F#6P这里就是『领域』……\x02",
    )

    CloseMessageWindow()
    Jump("loc_347D")

    label("loc_345B")


    #C0034
    ChrTalk(
        0x102,
        "#00105F#6P另一个『领域』……\x02",
    )

    CloseMessageWindow()

    label("loc_347D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34BF")

    #C0035
    ChrTalk(
        0x10A,
        (
            "#00605F#6P又是一处……\x01",
            "让人意外的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3542")

    label("loc_34BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3501")

    #C0036
    ChrTalk(
        0x105,
        (
            "#10405F#6P又是一处……\x01",
            "让人意外的场所。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3542")

    label("loc_3501")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3542")

    #C0037
    ChrTalk(
        0x109,
        (
            "#10105F#6P真是一处……\x01",
            "让人有些意外的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3542")


    #C0038
    ChrTalk(
        0x103,
        (
            "#00208F#6P完全不像是那个凶狠的\x01",
            "谢莉小姐的内在一面……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#00301F#6P的确……\x01",
            "不，也不能这么说吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x106,
        (
            "#10703F#5P嗯，人的内心\x01",
            "都会有各种各样的『颜色』……\x02\x03",

            "#10708F这或许也是她\x01",
            "不为人知的另一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00006F#5P原来如此……\x02\x03",

            "#00001F不知接下来将会发生什么，\x01",
            "我们小心谨慎地探索吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1700, 0, -101200, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_31A2 end

    def Function_21_369E(): pass

    label("Function_21_369E")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_36DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36DD)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_21_369E end

    def Function_22_3708(): pass

    label("Function_22_3708")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3747():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3747)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_22_3708 end

    def Function_23_3772(): pass

    label("Function_23_3772")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_37B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37B1)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_23_3772 end

    def Function_24_37DC(): pass

    label("Function_24_37DC")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_381B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_381B)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_37DC end

    def Function_25_3846(): pass

    label("Function_25_3846")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3885():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3885)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_25_3846 end

    def Function_26_38B0(): pass

    label("Function_26_38B0")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_38EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38EF)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_26_38B0 end

    def Function_27_391A(): pass

    label("Function_27_391A")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3935")
    Call(0, 19)

    label("loc_3935")

    SetChrPos(0x101, 3300, 0, -75000, 0)
    SetChrPos(0xF4, 4700, 0, -75000, 0)
    SetChrPos(0x102, 5800, 0, -73900, 315)
    SetChrPos(0x103, 2200, 0, -74400, 45)
    SetChrPos(0x104, 5800, 0, -76000, 0)
    SetChrPos(0xF5, 2800, 0, -76300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(3920, 2050, -73740, 0)
    MoveCamera(72, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21140, 0)
    OP_68(4000, 1530, -74500, 0)
    MoveCamera(356, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    SetCameraDistance(35000, 0)
    Fade(500)
    OP_0D()
    Sound(211, 0, 100, 0)
    Sleep(300)
    Call(0, 16)
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

    #C0042
    ChrTalk(
        0x101,
        "#00011F#5P天色变了……？\x02",
    )

    CloseMessageWindow()
    OP_68(6650, 130, -74490, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23330, 0)
    Fade(500)
    OP_0D()

    def lambda_3B16():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B16)
    Sleep(50)

    def lambda_3B26():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3B26)
    Sleep(50)

    def lambda_3B36():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3B36)
    Sleep(50)

    def lambda_3B46():
        OP_93(0x106, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3B46)
    Sleep(50)

    def lambda_3B56():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B56)
    Sleep(50)

    def lambda_3B66():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3B66)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0043
    ChrTalk(
        0x102,
        (
            "#00108F#5P道路似乎也发生了\x01",
            "一些变化……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#00201F#5P看样子，要想前往深处，\x01",
            "恐怕得花费一番工夫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#00306F#6P竟然像猫眼一样，\x01",
            "说变就变了……\x02\x03",

            "#00301F这个地方的确与她那\x01",
            "善变的性格很相符。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x106,
        (
            "#10708F#5P（……血腥谢莉，\x01",
            "  在最强猎兵团成长的少女……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 4000, 20, -76000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A8, 2)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_391A end

    def Function_28_3CCF(): pass

    label("Function_28_3CCF")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CEA")
    Call(0, 19)

    label("loc_3CEA")

    SetChrPos(0x101, -24820, 0, -116430, 45)
    SetChrPos(0xF4, -26080, 0, -115840, 45)
    SetChrPos(0x102, -26620, 0, -114380, 90)
    SetChrPos(0x103, -23910, 0, -117300, 45)
    SetChrPos(0x104, -25620, 0, -117520, 45)
    SetChrPos(0xF5, -23350, 0, -115900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-26000, 1530, -115500, 0)
    MoveCamera(12, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(35000, 0)
    Fade(500)
    OP_0D()
    Sound(211, 0, 100, 0)
    Call(0, 16)
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

    #C0047
    ChrTalk(
        0x101,
        "#00005F#5P天色变了……？\x02",
    )

    CloseMessageWindow()
    OP_68(-28110, 430, -114690, 0)
    MoveCamera(62, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26530, 0)
    Fade(500)
    OP_0D()
    Sleep(600)

    def lambda_3E94():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E94)
    Sleep(50)

    def lambda_3EA4():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3EA4)
    Sleep(50)

    def lambda_3EB4():
        OP_93(0xF5, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3EB4)
    Sleep(50)

    def lambda_3EC4():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3EC4)
    Sleep(50)

    def lambda_3ED4():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3ED4)
    Sleep(50)

    def lambda_3EE4():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3EE4)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0048
    ChrTalk(
        0x102,
        (
            "#00108F#11P道路似乎也\x01",
            "发生了一些变化……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#00201F#11P要想前往深处，\x01",
            "似乎得动脑筋想想办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#00306F#12P竟然像猫眼一样，\x01",
            "说变就变了……\x02\x03",

            "#00301F这个地方的确与她那\x01",
            "善变的性格很相符。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x106,
        (
            "#10708F#11P（……血腥谢莉，\x01",
            "  在最强猎兵团成长的少女……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -25000, 30, -116600, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A8, 2)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_3CCF end

    def Function_29_4046(): pass

    label("Function_29_4046")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x2, 0x0)
    OP_68(4000, 600, -73000, 0)
    MoveCamera(355, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    SetCameraDistance(50000, 6000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    Sound(202, 0, 80, 0)
    Sound(278, 0, 50, 0)
    SetMapObjFrame(0xFF, "pnrm02", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_day", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_night", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_day", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_night", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_7s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0s", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_0ss", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasira_5d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_6n", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0d", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasira_0n", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    Sleep(2500)
    StopSound(124, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9002", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4046 end

    SaveToFile()

Try(main)
