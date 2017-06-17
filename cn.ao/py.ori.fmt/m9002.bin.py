from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9002.bin",                # FileName
        "m9002",                    # MapName
        "m9002",                    # Location
        0x00BE,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 190, 0, 2, 0, 3],
    )

    BuildStringList((
        "m9002",                  # 0
        "玛丽亚贝尔",             # 1
        "幻兽",                   # 2
        "黄金雕像",               # 3
        "黑暗苍蓝地带",           # 4
        "bm9010",                 # 5
        "bm9010",                 # 6
        "bm9010",                 # 7
        "bm9010",                 # 8
        "bm9010",                 # 9
        "bm9010",                 # 10
        "bm9010",                 # 11
        "bm9010",                 # 12
        "bm9010",                 # 13
    ))

    ATBonus("ATBonus_510", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_520", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_530", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_6BE3", 7,   7,   7,   7,   11,  11,  11)
    Sepith("Sepith_6BFB", 9,   9,   9,   9,   10,  10,  10)
    Sepith("Sepith_6BDB", 13,  13,  13,  13,  4,   4,   4)
    Sepith("Sepith_6C03", 11,  23,  0,   15,  0,   0,   19)
    Sepith("Sepith_6BF3", 0,   0,   0,   0,   15,  38,  15)

    MonsterBattlePostion("MonsterBattlePostion_570", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_550", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 1, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 15, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 1, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 15, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_6AC", 0x0000, 100, 6, 60, 10, 1, 40, 0, "bm9010", "Sepith_6BE3", 40, 30, 20, 10,
        (
            ("ms80900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_6BFB", 40, 30, 20, 10,
        (
            ("ms79900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
        )
    )

    BattleInfo(
        "BattleInfo_610", 0x0000, 100, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_6BDB", 50, 30, 20, 0,
        (
            ("ms85300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_6C03", 100, 0, 0, 0,
        (
            ("ms85200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0010, 100, 6, 180, 10, 1, 5, 0, "bm9010", "Sepith_6BF3", 50, 35, 15, 0,
        (
            ("ms74200.dat", 0, 0, 0, 0, 0, "ms85200.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms74200.dat", "ms74200.dat", 0, 0, 0, 0, "ms85200.dat", 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms74200.dat", "ms74200.dat", "ms74200.dat", 0, 0, 0, "ms85200.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_A28", 0x0C10, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74200.dat", "ms74200.dat", "ms74200.dat", "ms74200.dat", "ms74200.dat", "ms74200.dat", "ms85200.dat", 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A6C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9E4", 0x0040, 255, 6, 45, 10, 1, 30, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89300.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", 0, "MonsterBattlePostion_5F0", "MonsterBattlePostion_5D0", "ed7554", "ed7453", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51735.itc",                   # 00
        "apl/ch51736.itc",                   # 01
        "apl/ch51768.itc",                   # 02
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
        "monster/ch85350.itc",               # 10
        "monster/ch85350.itc",               # 11
        "monster/ch80950.itc",               # 12
        "monster/ch80950.itc",               # 13
        "monster/ch85050.itc",               # 14
        "monster/ch85050.itc",               # 15
        "monster/ch74250.itc",               # 16
        "monster/ch74250.itc",               # 17
        "monster/ch79950.itc",               # 18
        "monster/ch79950.itc",               # 19
        "monster/ch85250.itc",               # 1A
        "monster/ch85251.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-170339, -24500,  -72849,  0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(89839,   10500,   -86760,  0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-122600, -138710, -25000,  0x1010137,    "BattleInfo_6AC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-153580, -103440, -24980,  0x1010092,    "BattleInfo_8D8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-117630, -90150,  -25000,  0x10100E8,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-84210,  -114510, -25000,  0x10100D8,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-92860,  -126180, -25000,  0x1010024,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-59120,  -142440, -25000,  0x1010124,    "BattleInfo_9A0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(75510,   -128630, -25000,  0x101003B,    "BattleInfo_9A0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(106200,  -109150, -25000,  0x10100E1,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(138550,  66010,   0,       0x101009A,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(117460,  60040,   10000,   0x1010098,    "BattleInfo_6AC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(128900,  -16340,  10000,   0x1010007,    "BattleInfo_83C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(125970,  -48030,  10000,   0x1010015,    "BattleInfo_8D8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(104070,  -73590,  10000,   0x1010023,    "BattleInfo_9A0", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 12,  0.0,                   -148.0,                19.5,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  49.333335876464844,    -3.9000000953674316,   1.0])
    DeclEvent(0x0040, 0, 29,  -14.0,                 -127.0,                24.5,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.799999952316284,     25.399999618530273,    -4.900000095367432,    1.0])
    DeclEvent(0x0040, 0, 34,  14.0,                  -127.0,                24.5,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.799999952316284,    25.399999618530273,    -4.900000095367432,    1.0])
    DeclEvent(0x0040, 0, 7,   125.0999984741211,     -64.55999755859375,    -0.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -15.637499809265137,   8.069999694824219,     -0.0,                  1.0])

    DeclActor(-170340, -25000,  -72850,  1200,    -170340, -24000,  -72850,  0x007C, 0,  4,  0x0000)
    DeclActor(68500,   -25000,  -130000, 1200,    68500,   -24000,  -130000, 0x007C, 0,  5,  0x0000)
    DeclActor(89840,   10000,   -86760,  1200,    89840,   11000,   -86760,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3])                          # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5
    ChipFrameInfo(1000, 0, [0])                                  # 6
    ChipFrameInfo(1000, 0, [0])                                  # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 8
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_BEC",          # 00, 0
        "Function_1_C04",          # 01, 1
        "Function_2_C23",          # 02, 2
        "Function_3_C8B",          # 03, 3
        "Function_4_18C8",         # 04, 4
        "Function_5_1AC6",         # 05, 5
        "Function_6_1C01",         # 06, 6
        "Function_7_1DFF",         # 07, 7
        "Function_8_1E78",         # 08, 8
        "Function_9_20F8",         # 09, 9
        "Function_10_2251",        # 0A, 10
        "Function_11_24D1",        # 0B, 11
        "Function_12_262A",        # 0C, 12
        "Function_13_3C30",        # 0D, 13
        "Function_14_3CD9",        # 0E, 14
        "Function_15_3CEE",        # 0F, 15
        "Function_16_3D03",        # 10, 16
        "Function_17_3D18",        # 11, 17
        "Function_18_3D2D",        # 12, 18
        "Function_19_3D42",        # 13, 19
        "Function_20_3D57",        # 14, 20
        "Function_21_3D6C",        # 15, 21
        "Function_22_3D8B",        # 16, 22
        "Function_23_3DA0",        # 17, 23
        "Function_24_3DB5",        # 18, 24
        "Function_25_3DCA",        # 19, 25
        "Function_26_3DDF",        # 1A, 26
        "Function_27_3E20",        # 1B, 27
        "Function_28_3E61",        # 1C, 28
        "Function_29_3F2F",        # 1D, 29
        "Function_30_494F",        # 1E, 30
        "Function_31_49D5",        # 1F, 31
        "Function_32_49E0",        # 20, 32
        "Function_33_4A21",        # 21, 33
        "Function_34_4A55",        # 22, 34
        "Function_35_5548",        # 23, 35
        "Function_36_55CE",        # 24, 36
        "Function_37_55D9",        # 25, 37
        "Function_38_561A",        # 26, 38
        "Function_39_564E",        # 27, 39
        "Function_40_5EDE",        # 28, 40
        "Function_41_69F3",        # 29, 41
        "Function_42_6AD3",        # 2A, 42
    ))


    def Function_0_BEC(): pass

    label("Function_0_BEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C03")
    OP_A1(0xFE, 0x3E8, 0x1, 0x0)
    Jump("Function_0_BEC")

    label("loc_C03")

    Return()

    # Function_0_BEC end

    def Function_1_C04(): pass

    label("Function_1_C04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C22")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_1_C04")

    label("loc_C22")

    Return()

    # Function_1_C04 end

    def Function_2_C23(): pass

    label("Function_2_C23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    Event(0, 8)

    label("loc_C34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C45")
    Event(0, 10)

    label("loc_C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C56")
    Event(0, 39)

    label("loc_C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    Event(0, 40)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C7B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 41)
    Jump("loc_C8A")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C8A")
    ClearScenarioFlags(0x22, 1)
    Event(0, 42)

    label("loc_C8A")

    Return()

    # Function_2_C23 end

    def Function_3_C8B(): pass

    label("Function_3_C8B")

    OP_F0(0x1, 0x320)
    OP_1B(0x8, 0x0, 0x9)
    OP_1B(0x9, 0x0, 0xB)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB1")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_CB1")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CDE")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_CDE")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0B")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_D0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D2D")
    ModifyEventFlags(0, 3, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_D96")

    label("loc_D2D")

    OP_78(0x5, 0x9)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x1)
    SetChrPos(0x9, 125100, 0, -64560, 207)
    OP_93(0x9, 0xCF, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 125100, 0, -64560, 3000, 3000, 207000)

    label("loc_D96")

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
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175B")
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    Jump("loc_176A")

    label("loc_175B")

    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_17AC")
    SetMapObjFrame(0xFF, "magi_00a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07a_add", 0x0, 0x1)
    ClearMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_17F3")

    label("loc_17AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_END)), "loc_17E7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D6")
    ClearMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_17E2")

    label("loc_17D6")

    SetMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x4, 0x4)

    label("loc_17E2")

    Jump("loc_17F3")

    label("loc_17E7")

    SetMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x4, 0x4)

    label("loc_17F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_END)), "loc_1835")
    SetMapObjFrame(0xFF, "magi_00b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07b_add", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_187C")

    label("loc_1835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_END)), "loc_1870")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185F")
    ClearMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_186B")

    label("loc_185F")

    SetMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x3, 0x4)

    label("loc_186B")

    Jump("loc_187C")

    label("loc_1870")

    SetMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x3, 0x4)

    label("loc_187C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188F")
    OP_70(0x0, 0x0)
    Jump("loc_1893")

    label("loc_188F")

    OP_70(0x0, 0x1E)

    label("loc_1893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A6")
    OP_70(0x1, 0x0)
    Jump("loc_18AA")

    label("loc_18A6")

    OP_70(0x1, 0x1E)

    label("loc_18AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18BD")
    OP_70(0x2, 0x0)
    Jump("loc_18C1")

    label("loc_18BD")

    OP_70(0x2, 0x1E)

    label("loc_18C1")

    Sound(112, 1, 50, 0)
    Return()

    # Function_3_C8B end

    def Function_4_18C8(): pass

    label("Function_4_18C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A88")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C5")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1925():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1925)

    def lambda_193F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_193F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

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
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_A28", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_19A6"),
        (2, "loc_19B5"),
        (1, "loc_19C2"),
        (SWITCH_DEFAULT, "loc_19C5"),
    )


    label("loc_19A6")

    SetScenarioFlags(0x218, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_19C5")

    label("loc_19B5")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_19C2")

    OP_B9(0x0)
    Return()

    label("loc_19C5")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('绝耀珠', 1)"), scpexpr(EXPR_END)), "loc_1A1C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1A83")

    label("loc_1A1C")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A83")

    Jump("loc_1ABA")

    label("loc_1A88")

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

    label("loc_1ABA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_18C8 end

    def Function_5_1AC6(): pass

    label("Function_5_1AC6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB8")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_1B49")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1BB3")

    label("loc_1B49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BB3")

    Jump("loc_1BF5")

    label("loc_1BB8")

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

    label("loc_1BF5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1AC6 end

    def Function_6_1C01(): pass

    label("Function_6_1C01")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC1")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFE")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1C5E():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C5E)

    def lambda_1C78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1C78)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_A6C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1CDF"),
        (2, "loc_1CEE"),
        (1, "loc_1CFB"),
        (SWITCH_DEFAULT, "loc_1CFE"),
    )


    label("loc_1CDF")

    SetScenarioFlags(0x218, 5)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1CFE")

    label("loc_1CEE")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1CFB")

    OP_B9(0x0)
    Return()

    label("loc_1CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('光耀珠', 1)"), scpexpr(EXPR_END)), "loc_1D55")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1DBC")

    label("loc_1D55")

    FadeToDark(300, 0, 100)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1DBC")

    Jump("loc_1DF3")

    label("loc_1DC1")

    FadeToDark(300, 0, 100)

    #A0011
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

    label("loc_1DF3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C01 end

    def Function_7_1DFF(): pass

    label("Function_7_1DFF")

    Battle("BattleInfo_9E4", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E46")
    OP_90(0x0, 123300, -2590, -74250, 187)
    EventEnd(0x5)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_1E77")

    label("loc_1E46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E59")
    Jump("loc_1E77")

    label("loc_1E59")

    ModifyEventFlags(0, 3, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetScenarioFlags(0x1B8, 2)
    EventEnd(0x5)

    label("loc_1E77")

    Return()

    # Function_7_1DFF end

    def Function_8_1E78(): pass

    label("Function_8_1E78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(11820, 26000, -128070, 0)
    MoveCamera(355, 42, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14700, 0)
    SetChrPos(0x0, 14000, 25500, -127000, 135)
    SetChrPos(0x1, 14000, 25500, -127000, 135)
    SetChrPos(0x2, 14000, 25500, -127000, 135)
    SetChrPos(0x3, 14000, 25500, -127000, 135)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1F88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1F88)

    def lambda_1F99():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F99)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1FF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1FF0)

    def lambda_2001():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2001)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_205E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_205E)

    def lambda_206F():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_206F)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_20C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_20C6)

    def lambda_20D7():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_20D7)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_1E78 end

    def Function_9_20F8(): pass

    label("Function_9_20F8")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2151():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2151)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_219C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_219C)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_21E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_21E7)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2232():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2232)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9050", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_20F8 end

    def Function_10_2251(): pass

    label("Function_10_2251")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-13590, 26000, -128639, 0)
    MoveCamera(1, 46, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14700, 0)
    SetChrPos(0x0, -14000, 25500, -127000, 135)
    SetChrPos(0x1, -14000, 25500, -127000, 135)
    SetChrPos(0x2, -14000, 25500, -127000, 135)
    SetChrPos(0x3, -14000, 25500, -127000, 135)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2361():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2361)

    def lambda_2372():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2372)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_23C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_23C9)

    def lambda_23DA():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_23DA)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2437():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2437)

    def lambda_2448():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2448)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_249F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_249F)

    def lambda_24B0():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_24B0)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_2251 end

    def Function_11_24D1(): pass

    label("Function_11_24D1")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_252A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_252A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2575():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2575)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_25C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_25C0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_260B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_260B)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9060", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_24D1 end

    def Function_12_262A(): pass

    label("Function_12_262A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch03700.itc", 0x1E)
    SoundLoad(3788)
    OP_69(0x3, 0x0)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10801.itp")
    OP_68(0, 24100, -149710, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19420, 0)
    SetChrPos(0x101, 0, 20000, -151000, 0)
    SetChrPos(0x102, 1300, 20000, -151500, 0)
    SetChrPos(0x103, 200, 20000, -152300, 0)
    SetChrPos(0x104, -1300, 20000, -152300, 0)
    SetChrPos(0xF4, -700, 20000, -153800, 0)
    SetChrPos(0xF5, 900, 20000, -153500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    FadeToBright(1000, 0)

    def lambda_2751():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2751)
    Sleep(50)

    def lambda_2769():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2769)
    Sleep(50)

    def lambda_2781():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2781)
    Sleep(50)

    def lambda_2799():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2799)
    Sleep(50)

    def lambda_27B1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_27B1)
    Sleep(50)

    def lambda_27C9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_27C9)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x101,
        "#00005F#5P这里是……\x02",
    )

    CloseMessageWindow()

    def lambda_2882():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2882)
    Sleep(50)

    def lambda_289A():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_289A)
    Sleep(50)

    def lambda_28B2():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28B2)
    Sleep(50)

    def lambda_28CA():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28CA)
    Sleep(50)

    def lambda_28E2():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_28E2)
    Sleep(50)

    def lambda_28FA():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_28FA)
    OP_68(0, 26100, -126840, 6000)
    MoveCamera(23, 9, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(16970, 6000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    BeginChrThread(0x101, 0, 0, 14)
    BeginChrThread(0x102, 0, 0, 15)
    BeginChrThread(0x103, 0, 0, 16)
    BeginChrThread(0x104, 0, 0, 17)
    BeginChrThread(0xF4, 0, 0, 18)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_2991():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2991)
    Sleep(50)

    def lambda_29A1():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29A1)
    Sleep(50)

    def lambda_29B1():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_29B1)
    Sleep(50)

    def lambda_29C1():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_29C1)
    Sleep(50)

    def lambda_29D1():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_29D1)
    Sleep(50)

    def lambda_29E1():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_29E1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0013
    ChrTalk(
        0x104,
        (
            "#00301F#6P怎么回事……？\x01",
            "被屏障一样的\x01",
            "东西阻挡住了……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#00208F#12P我想应该是\x01",
            "某种『结界』……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00108F#12P中央暂且不提……\x01",
            "左右两边的都是什么呢？\x02",
        )
    )

    WaitChrThread(0x102, 0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(921, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 30, -1, -1)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3788V#40W#50A呵呵……\x01",
            "那是通往『领域』的入口。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
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
    Fade(500)
    OP_68(0, 26900, -131200, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10640, 0)
    OP_68(0, 28500, -129850, 4000)
    MoveCamera(358, 13, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(22230, 4000)
    BeginChrThread(0x101, 0, 0, 20)
    BeginChrThread(0x102, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0x104, 0, 0, 23)
    BeginChrThread(0xF4, 0, 0, 24)
    BeginChrThread(0xF5, 0, 0, 25)
    OP_6F(0x79)

    #C0017
    ChrTalk(
        0x102,
        (
            "#00107F#5P贝尔……！？\x01",
            "……是贝尔吗！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_68(0, 28000, -129850, 2000)
    MoveCamera(359, 8, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(16340, 2000)
    Sleep(500)
    Sound(223, 0, 60, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 27800, -126500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 3, 0, 13)
    Sleep(800)

    def lambda_2D03():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D03)
    Sleep(50)

    def lambda_2D13():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D13)
    Sleep(50)

    def lambda_2D23():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2D23)
    Sleep(50)

    def lambda_2D33():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2D33)
    Sleep(50)

    def lambda_2D43():
        TurnDirection(0xF4, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2D43)
    Sleep(50)

    def lambda_2D53():
        TurnDirection(0xF5, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2D53)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(500)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W呵呵……\x01",
            "艾莉，这还用问吗？\x02\x03",

            "欢迎来到『碧之大树』。\x02\x03",

            "要是知道你们来了，\x01",
            "琪雅大概也会很高兴的。\x02\x03",

            "不……呵呵，\x01",
            "也许反而会很难过吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)

    #C0019
    ChrTalk(
        0x102,
        "#00101F#12P#N贝尔……你……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N先不说你们的意图是什么……\x02\x03",

            "#00001F看样子，你并不打算\x01",
            "阻止我们的行动呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W是的，这个『神域』\x01",
            "就是琪雅的内心……\x02\x03",

            "她既希望你们来，\x01",
            "又不希望你们来，此地将她矛盾的\x01",
            "心理原原本本地反映了出来。\x02\x03",

            "而这种心理就以四处徘徊的\x01",
            "守护者的形式所显现。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3073")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3046")
    OP_FC(0x6)
    Jump("loc_3049")

    label("loc_3046")

    OP_FC(0xC)

    label("loc_3049")


    #C0022
    ChrTalk(
        0x10A,
        "#00601F#13P#N原来是这种原理……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3120")

    label("loc_3073")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_309D")
    OP_FC(0x6)
    Jump("loc_30A0")

    label("loc_309D")

    OP_FC(0xC)

    label("loc_30A0")


    #C0023
    ChrTalk(
        0x109,
        "#10111F#13P#N原、原来是这种原理……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3120")

    label("loc_30CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3120")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30F8")
    OP_FC(0x6)
    Jump("loc_30FB")

    label("loc_30F8")

    OP_FC(0xC)

    label("loc_30FB")


    #C0024
    ChrTalk(
        0x106,
        "#10712F#13P#N原来是这种原理……\x02",
    )

    CloseMessageWindow()

    label("loc_3120")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3195")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_314D")
    OP_FC(0x6)
    Jump("loc_3150")

    label("loc_314D")

    OP_FC(0xC)

    label("loc_3150")


    #C0025
    ChrTalk(
        0x105,
        (
            "#10406F#13P#N光靠她的精神面\x01",
            "就能构筑出这么广阔的空间吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3260")

    label("loc_3195")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3205")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31BF")
    OP_FC(0x6)
    Jump("loc_31C2")

    label("loc_31BF")

    OP_FC(0xC)

    label("loc_31C2")


    #C0026
    ChrTalk(
        0x106,
        (
            "#10706F#13P#N光靠她的精神面\x01",
            "就能构筑出这么广阔的空间……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3260")

    label("loc_3205")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3260")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_322F")
    OP_FC(0x6)
    Jump("loc_3232")

    label("loc_322F")

    OP_FC(0xC)

    label("loc_3232")


    #C0027
    ChrTalk(
        0x109,
        (
            "#10108F#13P#N这就是小琪雅\x01",
            "内心的空间……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3260")

    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W呵呵，这是最后的宴会了。\x02\x03",

            "为了能让大家玩得更加开心，\x01",
            "我特别为你们准备了分会场。\x02\x03",

            "入口就是——你们眼前的『门』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
    OP_68(-10270, 25300, -123110, 0)
    MoveCamera(308, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21680, 0)
    Fade(500)
    OP_0D()

    def lambda_3357():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3357)
    Sleep(50)

    def lambda_3367():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3367)
    Sleep(50)

    def lambda_3377():
        OP_93(0xF4, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3377)
    Sleep(50)

    def lambda_3387():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3387)
    Sleep(50)

    def lambda_3397():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3397)
    Sleep(50)

    def lambda_33A7():
        OP_93(0xF5, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_33A7)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_68(10270, 25300, -123110, 0)
    MoveCamera(52, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21680, 0)
    Fade(500)
    OP_0D()

    def lambda_3403():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3403)
    Sleep(50)

    def lambda_3413():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3413)
    Sleep(50)

    def lambda_3423():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3423)
    Sleep(50)

    def lambda_3433():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3433)
    Sleep(50)

    def lambda_3443():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3443)
    Sleep(50)

    def lambda_3453():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3453)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 28000, -129850, 0)
    MoveCamera(359, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16340, 0)
    OP_0D()
    Sleep(200)

    def lambda_34B2():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34B2)
    Sleep(50)

    def lambda_34C2():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_34C2)
    Sleep(50)

    def lambda_34D2():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_34D2)
    Sleep(50)

    def lambda_34E2():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_34E2)
    Sleep(50)

    def lambda_34F2():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_34F2)
    Sleep(50)

    def lambda_3502():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3502)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0029
    ChrTalk(
        0x103,
        "#00201F#6P#N分会场……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0030
    ChrTalk(
        0x104,
        (
            "#00306F#6P#N喂喂……能不能\x01",
            "不要再故弄玄虚了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W呵呵，解释起来很简单啊。\x02\x03",

            "就像这个『神域』\x01",
            "反映了琪雅的内心一样……\x02\x03",

            "这些门也通往\x01",
            "反映了其他人\x01",
            "内心的『领域』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
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

    #C0032
    ChrTalk(
        0x101,
        "#00007F#6P#N其他人……？！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x102,
        "#00101F#12P#N难、难道说……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W呵呵，只要有『有缘之人』同行，\x01",
            "就可以进入这些分会场。\x02\x03",

            "那么，介绍到此为止，\x01",
            "我在主会场恭候你们的到来。\x02\x03",

            "但前提是你们能够\x01",
            "平安无事地抵达。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
    Sound(223, 0, 60, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    OP_68(0, 26500, -131690, 2500)
    MoveCamera(0, 22, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(11640, 2500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)

    #C0035
    ChrTalk(
        0x102,
        "#00106F#11P……贝尔………\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00003F#5P这个玩笑开得有点过头了啊……\x02\x03",

            "#00008F但是，中央的门暂且不管，\x01",
            "左右两扇门似乎是可以进去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00201F#6P问题是，在前方等待着\x01",
            "我们的究竟是什么人……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    #C0038
    ChrTalk(
        0x104,
        (
            "#00306F#5P好啦，不管怎么说，我们赶快试试看吧。\x02\x03",

            "#00300F看样子，如果没有特定的人员同行，\x01",
            "就不能进去呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A68():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A68)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A9A")
    OP_FC(0x6)
    Jump("loc_3A9D")

    label("loc_3A9A")

    OP_FC(0xC)

    label("loc_3A9D")


    #C0039
    ChrTalk(
        0x105,
        "#10408F#13P是啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3AB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AFE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AE0")
    OP_FC(0x6)
    Jump("loc_3AE3")

    label("loc_3AE0")

    OP_FC(0xC)

    label("loc_3AE3")


    #C0040
    ChrTalk(
        0x106,
        "#10708F#13P……是的。\x02",
    )

    CloseMessageWindow()

    label("loc_3AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B28")
    OP_FC(0x6)
    Jump("loc_3B2B")

    label("loc_3B28")

    OP_FC(0xC)

    label("loc_3B2B")


    #C0041
    ChrTalk(
        0x109,
        (
            "#10101F#13P如果觉得有必要，\x01",
            "或许还是先回\x01",
            "梅尔卡瓦一趟为好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BDF")

    label("loc_3B71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B9B")
    OP_FC(0x6)
    Jump("loc_3B9E")

    label("loc_3B9B")

    OP_FC(0xC)

    label("loc_3B9E")


    #C0042
    ChrTalk(
        0x10A,
        (
            "#00601F#13P如果认为有必要，\x01",
            "或许还是先回\x01",
            "梅尔卡瓦一趟为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BDF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 25000, -131700, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 3)
    OP_29(0xB2, 0x1, 0x2)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_262A end

    def Function_13_3C30(): pass

    label("Function_13_3C30")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x1F4)

    def lambda_3C40():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C40)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x320)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x96)

    label("loc_3C7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C92")
    Sleep(50)
    Jump("loc_3C7B")

    label("loc_3C92")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x96)
    Sleep(300)
    Sleep(50)

    def lambda_3CA8():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CA8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    Sleep(300)
    Return()

    # Function_13_3C30 end

    def Function_14_3CD9(): pass

    label("Function_14_3CD9")

    Sleep(100)
    OP_93(0xFE, 0x4B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xC3, 0x1F4)
    Return()

    # Function_14_3CD9 end

    def Function_15_3CEE(): pass

    label("Function_15_3CEE")

    Sleep(200)
    OP_93(0xFE, 0x11D, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xA5, 0x1F4)
    Return()

    # Function_15_3CEE end

    def Function_16_3D03(): pass

    label("Function_16_3D03")

    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_16_3D03 end

    def Function_17_3D18(): pass

    label("Function_17_3D18")

    Sleep(400)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x14A, 0x1F4)
    Return()

    # Function_17_3D18 end

    def Function_18_3D2D(): pass

    label("Function_18_3D2D")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_18_3D2D end

    def Function_19_3D42(): pass

    label("Function_19_3D42")

    Sleep(600)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_19_3D42 end

    def Function_20_3D57(): pass

    label("Function_20_3D57")

    Sleep(500)
    OP_93(0xFE, 0xC3, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x4B, 0x1F4)
    Return()

    # Function_20_3D57 end

    def Function_21_3D6C(): pass

    label("Function_21_3D6C")

    Sleep(200)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_21_3D6C end

    def Function_22_3D8B(): pass

    label("Function_22_3D8B")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_22_3D8B end

    def Function_23_3DA0(): pass

    label("Function_23_3DA0")

    Sleep(400)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_3DA0 end

    def Function_24_3DB5(): pass

    label("Function_24_3DB5")

    Sleep(650)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(450)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_24_3DB5 end

    def Function_25_3DCA(): pass

    label("Function_25_3DCA")

    Sleep(550)
    OP_93(0xFE, 0x6E, 0x1F4)
    Sleep(550)
    OP_93(0xFE, 0xE6, 0x1F4)
    Return()

    # Function_25_3DCA end

    def Function_26_3DDF(): pass

    label("Function_26_3DDF")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DF7")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_3DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E0B")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_3E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E1F")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3E1F")

    Return()

    # Function_26_3DDF end

    def Function_27_3E20(): pass

    label("Function_27_3E20")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E38")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_3E38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E4C")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_3E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E60")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3E60")

    Return()

    # Function_27_3E20 end

    def Function_28_3E61(): pass

    label("Function_28_3E61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EC0")
    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E8E")
    OP_CF(0x1, 0xF5, 0x4)
    Jump("loc_3EBB")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EA7")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_3EBB")

    label("loc_3EA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EBB")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3EBB")

    Jump("loc_3F2E")

    label("loc_3EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F06")
    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EED")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_3F01")

    label("loc_3EED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F01")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3F01")

    Jump("loc_3F2E")

    label("loc_3F06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2E")
    OP_CF(0x1, 0xF4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2E")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3F2E")

    Return()

    # Function_28_3E61 end

    def Function_29_3F2F(): pass

    label("Function_29_3F2F")

    EventBegin(0x0)
    OP_E2(0x3)
    SoundLoad(3577)
    SoundLoad(3578)
    SoundLoad(3579)
    Fade(500)
    OP_69(0x3, 0x0)
    OP_68(-12140, 25800, -128789, 0)
    MoveCamera(356, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F8B")
    Call(0, 26)
    Jump("loc_3F8E")

    label("loc_3F8B")

    Call(0, 28)

    label("loc_3F8E")

    SetChrPos(0x101, -12000, 25800, -129000, 315)
    SetChrPos(0x102, -10750, 25800, -130250, 315)
    SetChrPos(0x103, -12200, 25000, -131200, 315)
    SetChrPos(0x104, -9800, 25000, -128800, 315)
    SetChrPos(0xF4, -10750, 25000, -131500, 315)
    SetChrPos(0xF5, -9500, 25000, -130250, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F6")
    BeginChrThread(0x101, 0, 0, 30)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_409E")

    #C0043
    ChrTalk(
        0x101,
        (
            "#00006F#5P……不行。\x02\x03",

            "#00001F看来无法\x01",
            "靠攻击来破坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00108F#12P如果能想办法\x01",
            "知道里面的人是谁……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F6")

    label("loc_409E")


    #C0045
    ChrTalk(
        0x101,
        "#00003F#5P……和右边的门一样啊。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00101F#12P这道门里面的人……\x01",
            "到底会是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F6")

    OP_68(-14000, 26500, -127000, 2000)
    MoveCamera(340, 17, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(15680, 2000)
    OP_6F(0x79)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 31)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    Sleep(300)

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3577V#50W#40A哼哼哼……哈哈哈………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3578V#50W#50A……我的力量……\x01",
            "我的力量是最强大的……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3579V#50W#50A哼哼，不错……\x01",
            "比那家伙还要强大……！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_68(-11820, 26000, -128740, 2000)
    MoveCamera(346, 20, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13300, 2000)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47E5")

    #C0050
    ChrTalk(
        0x105,
        (
            "#10408F#12P……真是的，\x01",
            "为什么对我这种人\x01",
            "如此执著啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_4333():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4333)
    Sleep(50)

    def lambda_4343():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4343)
    Sleep(50)

    def lambda_4353():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4353)
    Sleep(50)

    def lambda_4363():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4363)
    Sleep(50)

    def lambda_4373():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4373)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)

    #C0051
    ChrTalk(
        0x101,
        "#00008F#5P瓦吉…\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x105,
        (
            "#10403F#12P让开一下，罗伊德。\x02\x03",

            "#10401F看样子，『他』似乎\x01",
            "想与我做个了结。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#00006F#5P……我明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_441A():
        OP_96(0xFE, 0xFFFFD508, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_441A)

    def lambda_4434():

        label("loc_4434")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4434")

    QueueWorkItem2(0x101, 2, lambda_4434)

    def lambda_4446():

        label("loc_4446")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4446")

    QueueWorkItem2(0x102, 2, lambda_4446)

    def lambda_4458():

        label("loc_4458")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4458")

    QueueWorkItem2(0x103, 2, lambda_4458)

    def lambda_446A():

        label("loc_446A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_446A")

    QueueWorkItem2(0x104, 2, lambda_446A)

    def lambda_447C():

        label("loc_447C")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_447C")

    QueueWorkItem2(0xF5, 2, lambda_447C)
    Sleep(300)
    OP_68(-12230, 26000, -127620, 2000)
    MoveCamera(358, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_44BF():
        OP_95(0xFE, -12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44BF)
    Sleep(150)

    def lambda_44DC():
        OP_9B(0x1, 0xFE, 0x2D, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44DC)
    Sleep(500)

    def lambda_44F4():
        OP_96(0xFE, 0xFFFFD602, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44F4)
    WaitChrThread(0x105, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x105, 0, 0, 32)
    WaitChrThread(0x105, 0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0x4, 0x1, 0x3E8)
    Sleep(1000)
    Sleep(500)
    BeginChrThread(0x105, 0, 0, 33)
    WaitChrThread(0x105, 0)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF5, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D6")

    #C0054
    ChrTalk(
        0x102,
        "#00105F#12P壁障消失了……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#00301F#11P这样一来，就可以前往\x01",
            "那个叫做『领域』的地方了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_462A")

    label("loc_45D6")


    #C0056
    ChrTalk(
        0x103,
        "#00201F#6P#N消失了呢……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0057
    ChrTalk(
        0x101,
        "#00001F#11P这样一来，就可以前往『领域』了……\x02",
    )

    CloseMessageWindow()

    label("loc_462A")

    Sleep(200)
    OP_93(0x105, 0x87, 0x1F4)

    #C0058
    ChrTalk(
        0x105,
        (
            "#10406F#5P是啊……但等待着\x01",
            "我们的可不是游戏。\x02\x03",

            "#10400F做好万全准备之后再出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4757")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46D5")

    #C0059
    ChrTalk(
        0x109,
        (
            "#10108F#12P最好先回梅尔卡瓦\x01",
            "准备一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_46D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4716")

    #C0060
    ChrTalk(
        0x10A,
        (
            "#00603F#12P最好先回梅尔卡瓦\x01",
            "准备一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4752")

    label("loc_4716")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4752")

    #C0061
    ChrTalk(
        0x106,
        (
            "#10708F#12P最好先回梅尔卡瓦\x01",
            "准备一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4752")

    Jump("loc_47D8")

    label("loc_4757")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4785")

    #C0062
    ChrTalk(
        0x109,
        "#10101F#12P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_47D8")

    label("loc_4785")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47AF")

    #C0063
    ChrTalk(
        0x10A,
        "#00601F#12P嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47D8")

    label("loc_47AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47D8")

    #C0064
    ChrTalk(
        0x106,
        "#10701F#12P是……！\x02",
    )

    CloseMessageWindow()

    label("loc_47D8")

    SetScenarioFlags(0x1AA, 1)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_4910")

    label("loc_47E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_END)), "loc_4898")

    #C0065
    ChrTalk(
        0x103,
        (
            "#00205F#12P壁障恢复原状了呢……\x02\x03",

            "#00203F看样子，瓦吉先生不在的时候，\x01",
            "我们是无法进入这个『领域』的。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00006F#11P是啊……我们这就回梅尔卡瓦，\x01",
            "把瓦吉带来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_4898")


    #C0067
    ChrTalk(
        0x103,
        (
            "#00208F#12P……里面的人是谁，\x01",
            "似乎已经相当明确了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#00006F#11P是啊……我们这就回梅尔卡瓦，\x01",
            "带那家伙过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4910")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -10750, 25800, -130250, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 4)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_3F2F end

    def Function_30_494F(): pass

    label("Function_30_494F")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Return()

    # Function_30_494F end

    def Function_31_49D5(): pass

    label("Function_31_49D5")

    Sleep(800)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_49D5 end

    def Function_32_49E0(): pass

    label("Function_32_49E0")

    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_32_49E0 end

    def Function_33_4A21(): pass

    label("Function_33_4A21")

    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    Sleep(200)
    Return()

    # Function_33_4A21 end

    def Function_34_4A55(): pass

    label("Function_34_4A55")

    EventBegin(0x0)
    OP_E2(0x3)
    SoundLoad(3961)
    SoundLoad(3962)
    SoundLoad(3963)
    Fade(500)
    OP_69(0x3, 0x0)
    OP_68(12140, 25800, -128789, 0)
    MoveCamera(4, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AB1")
    Call(0, 27)
    Jump("loc_4AB4")

    label("loc_4AB1")

    Call(0, 28)

    label("loc_4AB4")

    SetChrPos(0x101, 12000, 25800, -129000, 45)
    SetChrPos(0x102, 10750, 25800, -130250, 45)
    SetChrPos(0x103, 12200, 25000, -131200, 45)
    SetChrPos(0x104, 9800, 25000, -128800, 45)
    SetChrPos(0xF4, 10750, 25000, -131500, 45)
    SetChrPos(0xF5, 9500, 25000, -130250, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C15")
    BeginChrThread(0x101, 0, 0, 35)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BBD")

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006F#11P……不行。\x02\x03",

            "看来无法\x01",
            "靠攻击来破坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00108F#6P如果能想办法\x01",
            "知道里面的人是谁……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C15")

    label("loc_4BBD")


    #C0071
    ChrTalk(
        0x101,
        "#00003F#11P……和左边的门一样啊。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#00101F#6P这道门里面的人……\x01",
            "到底会是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C15")

    OP_68(14000, 26500, -127000, 2000)
    MoveCamera(20, 17, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(15680, 2000)
    OP_6F(0x79)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 36)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    Sleep(300)

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3961V#40W#40A呵呵呵……啊哈哈哈哈………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3962V#40W#38A好慢啊……\x01",
            "还不来吗……？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3963V#40W#38A实在太期待了，\x01",
            "我已经等不及了啊……！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_68(11820, 26000, -128740, 2000)
    MoveCamera(14, 20, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13300, 2000)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53AD")

    #C0076
    ChrTalk(
        0x106,
        "#10708F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#00306F#5P哎呀呀……是她啊。\x02\x03",

            "#00301F而且，她等的人\x01",
            "好像不是我。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_4E78():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E78)
    Sleep(50)

    def lambda_4E88():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4E88)
    Sleep(50)

    def lambda_4E98():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4E98)
    Sleep(50)

    def lambda_4EA8():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4EA8)
    Sleep(50)

    def lambda_4EB8():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4EB8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)

    #C0078
    ChrTalk(
        0x101,
        (
            "#00003F#11P……我说，莉夏。\x02\x03",

            "#00001F如果你不介意，\x01",
            "就把她交给我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x106,
        (
            "#10706F#6P不。\x02\x03",

            "#10708F从某种意义上来说，\x01",
            "我和她的境遇很相似。\x02\x03",

            "就算是为了让自己\x01",
            "找到未来的道路……\x02\x03",

            "#10701F我也必须要\x01",
            "再见她一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00006F#11P………我明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_4FD1():
        OP_96(0xFE, 0x2AF8, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD1)

    def lambda_4FEB():

        label("loc_4FEB")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_4FEB")

    QueueWorkItem2(0x101, 2, lambda_4FEB)

    def lambda_4FFD():

        label("loc_4FFD")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_4FFD")

    QueueWorkItem2(0x102, 2, lambda_4FFD)

    def lambda_500F():

        label("loc_500F")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_500F")

    QueueWorkItem2(0x103, 2, lambda_500F)

    def lambda_5021():

        label("loc_5021")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5021")

    QueueWorkItem2(0x104, 2, lambda_5021)

    def lambda_5033():

        label("loc_5033")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5033")

    QueueWorkItem2(0xF5, 2, lambda_5033)
    Sleep(300)
    OP_68(12230, 26000, -127620, 2000)
    MoveCamera(2, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_5076():
        OP_95(0xFE, 12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5076)
    Sleep(150)

    def lambda_5093():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5093)
    WaitChrThread(0x106, 1)

    def lambda_50AC():
        OP_96(0xFE, 0x29FE, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50AC)
    WaitChrThread(0x106, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x106, 0, 0, 37)
    WaitChrThread(0x106, 0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0x3, 0x1, 0x3E8)
    Sleep(1000)
    Sleep(500)
    BeginChrThread(0x106, 0, 0, 38)
    WaitChrThread(0x106, 0)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF5, 0x2)
    ClearMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518C")

    #C0081
    ChrTalk(
        0x102,
        "#00105F#6P壁障消失了……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#00301F#5P如此一来，就可以前往\x01",
            "那个叫做『领域』的地方了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_51DF")

    label("loc_518C")


    #C0083
    ChrTalk(
        0x103,
        "#00201F#6P#N消失了呢……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0084
    ChrTalk(
        0x101,
        "#00001F#5P这样一来，就可以前往『领域』了……\x02",
    )

    CloseMessageWindow()

    label("loc_51DF")

    Sleep(200)
    OP_93(0x106, 0xE1, 0x1F4)

    #C0085
    ChrTalk(
        0x106,
        (
            "#10703F……#11P对方不是寻常的对手。\x02\x03",

            "#10710F为了避免被她单方面压制，\x01",
            "我们做好万全准备之后再出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_531C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_529C")

    #C0086
    ChrTalk(
        0x109,
        (
            "#10106F#6P最好先回梅尔卡瓦\x01",
            "准备一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5317")

    label("loc_529C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52DC")

    #C0087
    ChrTalk(
        0x10A,
        (
            "#00603F#6P最好先回梅尔卡瓦\x01",
            "准备一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5317")

    label("loc_52DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5317")

    #C0088
    ChrTalk(
        0x105,
        (
            "#10404F#6P最好先回梅尔卡瓦\x01",
            "准备一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5317")

    Jump("loc_53A0")

    label("loc_531C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_534B")

    #C0089
    ChrTalk(
        0x109,
        "#10101F#6P是啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_53A0")

    label("loc_534B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5374")

    #C0090
    ChrTalk(
        0x10A,
        "#00601F#6P嗯。\x02",
    )

    CloseMessageWindow()
    Jump("loc_53A0")

    label("loc_5374")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53A0")

    #C0091
    ChrTalk(
        0x105,
        "#10402F#6P说得没错呢。\x02",
    )

    CloseMessageWindow()

    label("loc_53A0")

    SetScenarioFlags(0x1AA, 2)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_5509")

    label("loc_53AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_END)), "loc_5457")

    #C0092
    ChrTalk(
        0x104,
        (
            "#00305F#5P壁障恢复原状了……\x02\x03",

            "#00303F看样子，如果莉夏不在，\x01",
            "我们就无法进入\x01",
            "这个『领域』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006F#5P是啊……我们这就回梅尔卡瓦\x01",
            "把莉夏带过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5509")

    label("loc_5457")


    #C0094
    ChrTalk(
        0x104,
        (
            "#00306F#5P哎呀呀……是她啊。\x02\x03",

            "#00301F而且，她等的人\x01",
            "好像不是我。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00006F#5P是啊……\x02\x03",

            "#00008F（似乎需要回梅尔卡瓦\x01",
            "  带『她』过来……）\x02\x03",

            "（可是……把她带来，真的好吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5509")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 10750, 25800, -130250, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 5)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_4A55 end

    def Function_35_5548(): pass

    label("Function_35_5548")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Return()

    # Function_35_5548 end

    def Function_36_55CE(): pass

    label("Function_36_55CE")

    Sleep(800)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_36_55CE end

    def Function_37_55D9(): pass

    label("Function_37_55D9")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_37_55D9 end

    def Function_38_561A(): pass

    label("Function_38_561A")

    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    Sleep(200)
    Return()

    # Function_38_561A end

    def Function_39_564E(): pass

    label("Function_39_564E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_69(0x3, 0x0)
    OP_68(-13590, 26000, -128639, 0)
    MoveCamera(1, 46, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13700, 0)
    SetChrPos(0x101, -14000, 25500, -127000, 135)
    SetChrPos(0x102, -14000, 25500, -127000, 135)
    SetChrPos(0x103, -14000, 25500, -127000, 135)
    SetChrPos(0x104, -14000, 25500, -127000, 135)
    SetChrPos(0xF4, -14000, 25500, -127000, 135)
    SetChrPos(0xF5, -14000, 25500, -127000, 135)
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
    SetMapObjFrame(0xFF, "magi_00a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07a_add", 0x0, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    SetCameraDistance(14700, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_57E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57E4)

    def lambda_57F5():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57F5)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_584C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_584C)

    def lambda_585D():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_585D)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_58BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_58BA)

    def lambda_58CB():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58CB)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5922():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5922)

    def lambda_5933():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5933)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5990():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_5990)

    def lambda_59A1():
        OP_95(0xFE, -12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_59A1)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_59F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_59F8)

    def lambda_5A09():
        OP_95(0xFE, -11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_5A09)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_END)), "loc_5C7D")
    OP_29(0xB2, 0x1, 0x5)
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
    OP_68(-8500, 26200, -127000, 2500)
    MoveCamera(20, 18, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(19020, 2500)

    def lambda_5AFD():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5AFD)
    Sleep(50)

    def lambda_5B0D():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B0D)
    Sleep(50)

    def lambda_5B1D():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5B1D)
    Sleep(50)

    def lambda_5B2D():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5B2D)
    Sleep(50)

    def lambda_5B3D():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_5B3D)
    Sleep(50)

    def lambda_5B4D():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5B4D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0096
    ChrTalk(
        0x102,
        "#00102F#6P#N结界……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0097
    ChrTalk(
        0x104,
        (
            "#00306F#6P#N似乎是因为我们\x01",
            "把两个『领域』都开放了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0098
    ChrTalk(
        0x105,
        (
            "#10404F#6P呵呵，这下终于\x01",
            "可以继续前进了呢。\x02\x03",

            "#10408F……但在此之前，\x01",
            "真想先回飞船休息一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00000F#5P说的也是……我们还要向大家做个报告，\x01",
            "不妨先回梅尔卡瓦一趟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EA1")

    label("loc_5C7D")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-8500, 26200, -127000, 3000)
    MoveCamera(20, 18, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(19020, 3000)

    def lambda_5D25():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5D25)
    Sleep(50)

    def lambda_5D35():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5D35)
    Sleep(50)

    def lambda_5D45():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5D45)
    Sleep(50)

    def lambda_5D55():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5D55)
    Sleep(50)

    def lambda_5D65():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_5D65)
    Sleep(50)

    def lambda_5D75():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5D75)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0100
    ChrTalk(
        0x101,
        (
            "#00005F#6P中央之门的结界……\x01",
            "变薄了？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#00203F#6P恐怕是因为瓦鲁多先生的\x01",
            "『领域』已经开放了吧。\x02\x03",

            "#00201F我想，这个『神域』\x01",
            "应该与每个人的『领域』\x01",
            "联动。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00105F#6P#N也就是说，\x01",
            "只要将另一个『领域』开放……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10400F#6P那个结界\x01",
            "应该就会完全消失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EA1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -12000, 25500, -129300, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_39_564E end

    def Function_40_5EDE(): pass

    label("Function_40_5EDE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_69(0x3, 0x0)
    OP_68(11820, 26000, -128070, 0)
    MoveCamera(355, 42, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13700, 0)
    SetChrPos(0x101, 14000, 25500, -127000, 225)
    SetChrPos(0x102, 14000, 25500, -127000, 225)
    SetChrPos(0x103, 14000, 25500, -127000, 225)
    SetChrPos(0x104, 14000, 25500, -127000, 225)
    SetChrPos(0xF4, 14000, 25500, -127000, 225)
    SetChrPos(0xF5, 14000, 25500, -127000, 225)
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
    SetMapObjFrame(0xFF, "magi_00b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07b_add", 0x0, 0x1)
    ModifyEventFlags(0, 2, 0x80)
    SetCameraDistance(14700, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62BF")
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_607C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_607C)

    def lambda_608D():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_608D)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_60E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_60E4)

    def lambda_60F5():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60F5)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6152():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6152)

    def lambda_6163():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6163)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_61BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_61BA)

    def lambda_61CB():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_61CB)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6228():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6228)

    def lambda_6239():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_6239)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6290():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6290)

    def lambda_62A1():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_62A1)
    WaitChrThread(0xF5, 1)
    Jump("loc_6542")

    label("loc_62BF")

    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6304():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6304)

    def lambda_6315():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_6315)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_636C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_636C)

    def lambda_637D():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_637D)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_63DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_63DA)

    def lambda_63EB():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63EB)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6442)

    def lambda_6453():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6453)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_64B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64B0)

    def lambda_64C1():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64C1)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6518():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6518)

    def lambda_6529():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_6529)
    WaitChrThread(0xF5, 1)

    label("loc_6542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_6790")
    OP_29(0xB2, 0x1, 0x5)
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
    OP_68(8500, 26200, -127000, 2500)
    MoveCamera(340, 18, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(19020, 2500)

    def lambda_661D():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_661D)
    Sleep(50)

    def lambda_662D():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_662D)
    Sleep(50)

    def lambda_663D():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_663D)
    Sleep(50)

    def lambda_664D():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_664D)
    Sleep(50)

    def lambda_665D():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_665D)
    Sleep(50)

    def lambda_666D():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_666D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0104
    ChrTalk(
        0x102,
        "#00102F#12P结界……！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#00306F#12P#N似乎是因为我们\x01",
            "把两个『领域』都开放了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0106
    ChrTalk(
        0x106,
        (
            "#10702F#12P如此一来，\x01",
            "总算可以继续前进了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00006F#11P是啊，话说回来，\x01",
            "真是一场严酷的战斗呢……\x02\x03",

            "#00000F我们还要向大家做个报告，\x01",
            "不妨先回梅尔卡瓦一趟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B6")

    label("loc_6790")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(8500, 26200, -127000, 3000)
    MoveCamera(340, 18, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(19020, 3000)

    def lambda_6838():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6838)
    Sleep(50)

    def lambda_6848():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6848)
    Sleep(50)

    def lambda_6858():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6858)
    Sleep(50)

    def lambda_6868():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6868)
    Sleep(50)

    def lambda_6878():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6878)
    Sleep(50)

    def lambda_6888():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6888)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0108
    ChrTalk(
        0x101,
        (
            "#00005F#12P中央之门的结界……\x01",
            "变薄了？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#00203F#12P#N恐怕是因为谢莉小姐的\x01",
            "『领域』已经开放了吧。\x02\x03",

            "#00201F我想，这个『神域』\x01",
            "应该与每个人的『领域』\x01",
            "联动。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0110
    ChrTalk(
        0x102,
        (
            "#00105F#12P也就是说，\x01",
            "只要将另一个『领域』开放……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x106,
        (
            "#10702F#12P那个结界\x01",
            "应该就会完全消失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 12000, 25500, -129300, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_5EDE end

    def Function_41_69F3(): pass

    label("Function_41_69F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "event/ev17015.eff")
    OP_69(0x3, 0x0)
    OP_68(0, 27700, -122500, 0)
    MoveCamera(21, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17850, 0)
    SetCameraDistance(22850, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 28500, -122500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    SetMapObjFrame(0xFF, "magi_07a_add", 0x0, 0x1)
    Sleep(3000)
    StopSound(112, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9062", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_69F3 end

    def Function_42_6AD3(): pass

    label("Function_42_6AD3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "event/ev17014.eff")
    OP_69(0x3, 0x0)
    OP_68(0, 27700, -122500, 0)
    MoveCamera(339, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17850, 0)
    SetCameraDistance(22850, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 28500, -122500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    SetMapObjFrame(0xFF, "magi_07b_add", 0x0, 0x1)
    Sleep(3000)
    StopSound(112, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9052", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_6AD3 end

    SaveToFile()

Try(main)
