from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1030.bin",                # FileName
        "t1030",                    # MapName
        "t1030",                    # Location
        0x0041,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1030",                  # 0
        "ティオ",                 # 1
        "ツァイト",               # 2
        "シュリ",                 # 3
        "みっしぃ",               # 4
        "ＭＷＬスタッフ",         # 5
        "ＭＷＬスタッフ",         # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "メルスン",               # 13
        "コロナ",                 # 14
        "リマ",                   # 15
        "職員ハンクス",           # 16
        "神狼ツァイト",           # 17
        "猟兵",                   # 18
        "猟兵",                   # 19
        "猟兵",                   # 20
        "猟兵",                   # 21
        "猟兵",                   # 22
        "猟兵",                   # 23
        "猟兵",                   # 24
        "猟兵",                   # 25
        "父",                     # 26
        "母",                     # 27
        "男の子",                 # 28
        "幻獣",                   # 29
        "SE制御",                 # 30
        "bt1030",                 # 31
        "ホテル・デルフィニア方面",# 32
        "テーマパーク方面",       # 33
    ))

    ATBonus("ATBonus_5B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_674", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_690", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_658", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_65C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_660", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_664", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_668", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_66C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_694", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bt1030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_674", "MonsterBattlePostion_654", "ed7454", "ed7453", "ATBonus_5B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00200.itc",                   # 00
        "chr/ch02702.itc",                   # 01
        "chr/ch10100.itc",                   # 02
        "chr/ch28100.itc",                   # 03
        "chr/ch10200.itc",                   # 04
        "chr/ch44500.itc",                   # 05
        "chr/ch32300.itc",                   # 06
        "chr/ch32400.itc",                   # 07
        "chr/ch24200.itc",                   # 08
        "chr/ch24300.itc",                   # 09
        "chr/ch24600.itc",                   # 0A
        "chr/ch24700.itc",                   # 0B
        "chr/ch26200.itc",                   # 0C
        "chr/ch22700.itc",                   # 0D
        "chr/ch20700.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(360,     4159,    -15840,  180,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4750,    4400,    0,       180,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-13500,  4000,    -6500,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-13500,  4000,    -5500,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6139,   4000,    -15340,  90,   389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       4159,    -15840,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1049,   4000,    -16770,  45,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(600,     4000,    -17229,  315,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(7699,    4000,    -1519,   135,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9159,    4000,    -1759,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(7889,    4000,    -3069,   0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-8270,   4000,    389,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 20,  0.0,                   -28.0,                 -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  9.333333969116211,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 38,  0.0,                   2.5,                   3.4000000953674316,    100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -1.25,                 -0.6800000071525574,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  39, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  40, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "テーマパーク方面")

    ChipFrameInfo(1916, 0)                                       # 0

    ScpFunction((
        "Function_0_77C",          # 00, 0
        "Function_1_82C",          # 01, 1
        "Function_2_A27",          # 02, 2
        "Function_3_BA2",          # 03, 3
        "Function_4_C3B",          # 04, 4
        "Function_5_CE1",          # 05, 5
        "Function_6_D5C",          # 06, 6
        "Function_7_1013",         # 07, 7
        "Function_8_11D8",         # 08, 8
        "Function_9_1471",         # 09, 9
        "Function_10_1568",        # 0A, 10
        "Function_11_1604",        # 0B, 11
        "Function_12_169D",        # 0C, 12
        "Function_13_173F",        # 0D, 13
        "Function_14_1816",        # 0E, 14
        "Function_15_18BA",        # 0F, 15
        "Function_16_1A27",        # 10, 16
        "Function_17_1AB8",        # 11, 17
        "Function_18_1B59",        # 12, 18
        "Function_19_1B60",        # 13, 19
        "Function_20_2724",        # 14, 20
        "Function_21_2CA8",        # 15, 21
        "Function_22_2CCD",        # 16, 22
        "Function_23_317E",        # 17, 23
        "Function_24_319A",        # 18, 24
        "Function_25_394F",        # 19, 25
        "Function_26_3A4E",        # 1A, 26
        "Function_27_3C2F",        # 1B, 27
        "Function_28_3C60",        # 1C, 28
        "Function_29_3C8C",        # 1D, 29
        "Function_30_4002",        # 1E, 30
        "Function_31_4D39",        # 1F, 31
        "Function_32_57E2",        # 20, 32
        "Function_33_580B",        # 21, 33
        "Function_34_5834",        # 22, 34
        "Function_35_585D",        # 23, 35
        "Function_36_585E",        # 24, 36
        "Function_37_585F",        # 25, 37
        "Function_38_5885",        # 26, 38
        "Function_39_5A7E",        # 27, 39
        "Function_40_5AFE",        # 28, 40
    ))


    def Function_0_77C(): pass

    label("Function_0_77C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7B4"),
        (1, "loc_7C0"),
        (2, "loc_7CC"),
        (3, "loc_7D8"),
        (4, "loc_7E4"),
        (5, "loc_7F0"),
        (6, "loc_7FC"),
        (SWITCH_DEFAULT, "loc_808"),
    )


    label("loc_7B4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7C0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7CC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7D8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7E4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7F0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_7FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_808")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_814")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_814")

    label("loc_82B")

    Return()

    # Function_0_77C end

    def Function_1_82C(): pass

    label("Function_1_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_840")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)
    Jump("loc_886")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_857")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 1)
    Event(0, 31)
    Jump("loc_886")

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_86B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 30)
    Jump("loc_886")

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_886")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_886")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AC")
    ClearChrFlags(0x17, 0x80)

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8BA")
    Jump("loc_A26")

    label("loc_8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_8C8")
    Jump("loc_A26")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8D6")
    Jump("loc_A26")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_8E4")
    Jump("loc_A26")

    label("loc_8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_968")
    SetChrPos(0x8, -7400, 4000, -11000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -6400, 4000, -10000, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -8600, 4000, -11000, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -3940, 1730, -25670, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_A26")

    label("loc_968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9AA")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 1910, -25230, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_A26")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9B8")
    Jump("loc_A26")

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A1D")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -6040, 4000, -16340, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_A26")

    label("loc_A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_A26")

    label("loc_A26")

    Return()

    # Function_1_82C end

    def Function_2_A27(): pass

    label("Function_2_A27")

    SetMapObjFrame(0xFF, "t1030_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A65")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)
    Jump("loc_A77")

    label("loc_A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A77")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A77")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB1")
    SetMapObjFrame(0xFF, "t1030_water", 0x2, "loop_off")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEC")
    OP_24(0x335)
    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    SoundLoad(918)
    BeginChrThread(0x25, 3, 0, 37)
    Jump("loc_B1F")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_B19")
    OP_24(0x335)
    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    Jump("loc_B1F")

    label("loc_B19")

    Sound(821, 1, 40, 0)

    label("loc_B1F")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B58")
    ModifyEventFlags(0, 1, 0x80)

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B7F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_BA1")

    label("loc_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BA1")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_BA1")

    Return()

    # Function_2_A27 end

    def Function_3_BA2(): pass

    label("Function_3_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB9")
    Call(0, 19)
    Return()

    label("loc_BB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BCA")
    Jump("loc_C37")

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BD8")
    Jump("loc_C37")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BE6")
    Jump("loc_C37")

    label("loc_BE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_BF6")
    Jump("loc_C37")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C04")
    Jump("loc_C37")

    label("loc_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C12")
    Jump("loc_C37")

    label("loc_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_C37")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C2E")
    Jump("loc_C37")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_C37")

    label("loc_C37")

    TalkEnd(0xFE)
    Return()

    # Function_3_BA2 end

    def Function_4_C3B(): pass

    label("Function_4_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C52")
    Call(0, 19)
    Return()

    label("loc_C52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C63")
    Jump("loc_CDD")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C71")
    Jump("loc_CDD")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C7F")
    Jump("loc_CDD")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_CAA")

    #C0001
    ChrTalk(
        0x9,
        "#01200F……グルルル……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDD")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CB8")
    Jump("loc_CDD")

    label("loc_CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_CC6")
    Jump("loc_CDD")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_CD4")
    Jump("loc_CDD")

    label("loc_CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_CDD")

    label("loc_CDD")

    TalkEnd(0xFE)
    Return()

    # Function_4_C3B end

    def Function_5_CE1(): pass

    label("Function_5_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF8")
    Call(0, 19)
    Return()

    label("loc_CF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_D09")
    Jump("loc_D58")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D17")
    Jump("loc_D58")

    label("loc_D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_D25")
    Jump("loc_D58")

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_D33")
    Jump("loc_D58")

    label("loc_D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D41")
    Jump("loc_D58")

    label("loc_D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_D4F")
    Jump("loc_D58")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_D58")

    label("loc_D58")

    TalkEnd(0xFE)
    Return()

    # Function_5_CE1 end

    def Function_6_D5C(): pass

    label("Function_6_D5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_D6D")
    Jump("loc_100F")

    label("loc_D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D7B")
    Jump("loc_100F")

    label("loc_D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_100F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA9")

    #C0002
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "こんにちはっ！\x01",
            "ワンダーランドにようこそっ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでいってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00002Fおお、みっしぃだな。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、ティオすけも\x01",
            "連れて来てやればよかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10304Fまあ、午後にまた来るんだし\x01",
            "楽しみはとってあげてた方が\x01",
            "彼女も喜ぶんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100F")

    label("loc_EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA6")

    #C0007
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ところで、お兄さんは\x01",
            "男の子たちだけで来たの～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "でも大丈夫！\x01",
            "コイビトなんていなくても、\x01",
            "きっと楽しいワンダーランド♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでいってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006F（……なんか無性に\x01",
            "  悲しくなるんですけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_100F")

    label("loc_FA6")


    #C0011
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "コイビトなんていなくても、\x01",
            "きっと楽しいワンダーランド♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでいってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100F")

    TalkEnd(0xFE)
    Return()

    # Function_6_D5C end

    def Function_7_1013(): pass

    label("Function_7_1013")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1024")
    Jump("loc_11D4")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10CD")

    #C0013
    ChrTalk(
        0xC,
        (
            "あちらの案内板の前の子達、\x01",
            "さっきからみっしぃについて\x01",
            "熱く語っているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "ふふ、ワンダーランドのスタッフとして\x01",
            "なんだか嬉しい気分ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D4")

    label("loc_10CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_11D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116C")

    #C0015
    ChrTalk(
        0xC,
        (
            "ミシュラムの誇る\x01",
            "テーマパークへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "最近新しく導入された\x01",
            "アトラクションが大人気です。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "入場の際はお見逃し無く！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11D4")

    label("loc_116C")


    #C0018
    ChrTalk(
        0xC,
        (
            "テーマパークでは、\x01",
            "最近新しく導入された\x01",
            "アトラクションが大人気です。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        "入場の際はお見逃し無く！\x02",
    )

    CloseMessageWindow()

    label("loc_11D4")

    TalkEnd(0xFE)
    Return()

    # Function_7_1013 end

    def Function_8_11D8(): pass

    label("Function_8_11D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_11E9")
    Jump("loc_146D")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1276")

    #C0020
    ChrTalk(
        0xD,
        (
            "みっしぃなら、\x01",
            "今はテーマパーク内を\x01",
            "うろうろしていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xD,
        (
            "見つけたら、どうぞお気軽に\x01",
            "写真を申し込んでみて下さいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_146D")

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_146D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CF")

    #C0022
    ChrTalk(
        0xD,
        (
            "近頃、子供たちの間で\x01",
            "みっしぃのお尻を蹴るというのが\x01",
            "流行してましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xD,
        (
            "発祥は些細なイタズラですが、\x01",
            "最近では『蹴ると幸せになる』\x01",
            "という噂までも流れているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xD,
        (
            "ふふ、小さなお子さんには\x01",
            "是非ともみっしぃへのキックを\x01",
            "させてみてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00006F（よ、要するにスタッフも\x01",
            "  ノリノリなんだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_146D")

    label("loc_13CF")


    #C0026
    ChrTalk(
        0xD,
        (
            "近頃、子供たちの間で\x01",
            "みっしぃのお尻を蹴るというのが\x01",
            "流行してましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "ふふ、小さなお子さんには\x01",
            "是非ともみっしぃへのキックを\x01",
            "させてみてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146D")

    TalkEnd(0xFE)
    Return()

    # Function_8_11D8 end

    def Function_9_1471(): pass

    label("Function_9_1471")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1482")
    Jump("loc_1564")

    label("loc_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_14DA")

    #C0028
    ChrTalk(
        0xE,
        "うおー、ここがＭ・Ｗ・Ｌ……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xE,
        "今から入って遊びつくせるかなー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1564")

    label("loc_14DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1564")

    #C0030
    ChrTalk(
        0xE,
        (
            "テーマパークを回るには、\x01",
            "やっぱ計画性が大事だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xE,
        (
            "彼女と一緒に\x01",
            "一つでも多く回れるように、\x01",
            "作戦をしっかり立てないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1564")

    TalkEnd(0xFE)
    Return()

    # Function_9_1471 end

    def Function_10_1568(): pass

    label("Function_10_1568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1579")
    Jump("loc_1600")

    label("loc_1579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1587")
    Jump("loc_1600")

    label("loc_1587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1600")

    #C0032
    ChrTalk(
        0xF,
        (
            "もう、そんなのいいから\x01",
            "さっさと入らない？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xF,
        (
            "こうしてる間にも遊べる時間が\x01",
            "どんどん減っていくんですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1600")

    TalkEnd(0xFE)
    Return()

    # Function_10_1568 end

    def Function_11_1604(): pass

    label("Function_11_1604")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1615")
    Jump("loc_1699")

    label("loc_1615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1623")
    Jump("loc_1699")

    label("loc_1623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1699")

    #C0034
    ChrTalk(
        0x10,
        (
            "おお、あそこにいるのが\x01",
            "みっしぃか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x10,
        (
            "よし、お父さんが\x01",
            "写真を取ってあげるから、\x01",
            "隣にいきなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1699")

    TalkEnd(0xFE)
    Return()

    # Function_11_1604 end

    def Function_12_169D(): pass

    label("Function_12_169D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_16AE")
    Jump("loc_173B")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1732")

    #C0036
    ChrTalk(
        0x11,
        (
            "みっしぃはテーマパークの中に\x01",
            "入っちゃったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x11,
        (
            "よ～し、こうなったら\x01",
            "お母さんも気合入れて探しちゃうよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173B")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_173B")

    label("loc_173B")

    TalkEnd(0xFE)
    Return()

    # Function_12_169D end

    def Function_13_173F(): pass

    label("Function_13_173F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1750")
    Jump("loc_1812")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_17D8")

    #C0038
    ChrTalk(
        0x12,
        (
            "ボク、今日こそみっしぃに\x01",
            "キックを成功させるんだ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x12,
        (
            "そうすると幸せになれるんだって。\x01",
            "みっしぃって、すごいよね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1812")

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1812")

    #C0040
    ChrTalk(
        0x12,
        (
            "わ～い、みっしぃだ！\x01",
            "本物のみっしぃだよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1812")

    TalkEnd(0xFE)
    Return()

    # Function_13_173F end

    def Function_14_1816(): pass

    label("Function_14_1816")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1827")
    Jump("loc_18B6")

    label("loc_1827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_18AD")

    #C0041
    ChrTalk(
        0x13,
        (
            "や～ん、キックするなんて\x01",
            "みっしぃがカワイソーだよぉ！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x13,
        (
            "お兄ちゃんにさせるぐらいなら\x01",
            "あたしがやってやるもーん！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_18B6")

    label("loc_18B6")

    TalkEnd(0xFE)
    Return()

    # Function_14_1816 end

    def Function_15_18BA(): pass

    label("Function_15_18BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_18CB")
    Jump("loc_1A23")

    label("loc_18CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_18D9")
    Jump("loc_1A23")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_18E7")
    Jump("loc_1A23")

    label("loc_18E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1989")
    OP_4B(0x16, 0xFF)

    #C0043
    ChrTalk(
        0x14,
        "さて、ようやく着いたな。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x14,
        (
            "よ～し、リマ、コロナ。\x01",
            "早速みんなでテーマパークに\x01",
            "入るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x16,
        "さんせ～い！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0x16, 0xFF)
    Jump("loc_1A15")

    label("loc_1989")


    #C0046
    ChrTalk(
        0x14,
        (
            "今日のために、\x01",
            "一日有効なフリーパスを\x01",
            "買っておいたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x14,
        (
            "普段苦労させてる分、\x01",
            "リマとコロナにはたっぷり\x01",
            "楽しんでもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A15")

    Jump("loc_1A23")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1A23")

    label("loc_1A23")

    TalkEnd(0xFE)
    Return()

    # Function_15_18BA end

    def Function_16_1A27(): pass

    label("Function_16_1A27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1A38")
    Jump("loc_1AB4")

    label("loc_1A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1A46")
    Jump("loc_1AB4")

    label("loc_1A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1A54")
    Jump("loc_1AB4")

    label("loc_1A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1AAB")

    #C0048
    ChrTalk(
        0x15,
        (
            "テーマパークの中は\x01",
            "どうなってるのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x15,
        "ふふ、楽しみです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AB4")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1AB4")

    label("loc_1AB4")

    TalkEnd(0xFE)
    Return()

    # Function_16_1A27 end

    def Function_17_1AB8(): pass

    label("Function_17_1AB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1AC9")
    Jump("loc_1B55")

    label("loc_1AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1AD7")
    Jump("loc_1B55")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1AE5")
    Jump("loc_1B55")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B4C")

    #C0050
    ChrTalk(
        0x16,
        (
            "今日はね、パパとママと\x01",
            "一日中テーマパークで遊ぶんだよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x16,
        "ふふっ、楽しみー！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B55")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1B55")

    label("loc_1B55")

    TalkEnd(0xFE)
    Return()

    # Function_17_1AB8 end

    def Function_18_1B59(): pass

    label("Function_18_1B59")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_18_1B59 end

    def Function_19_1B60(): pass

    label("Function_19_1B60")

    EventBegin(0x0)
    Fade(500)
    OP_68(-8000, 5000, -11750, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(24000, 1500)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrPos(0x101, -8600, 4000, -12500, 0)
    SetChrPos(0x153, -7400, 4000, -12500, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2216")

    #C0052
    ChrTalk(
        0x153,
        "#01110F#6Pえへへ、おまたせー。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "#00202F#11Pロイドさん、キーア。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "#14000F#11P……よう。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        "#01200F#11Pウォン。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1FAA")

    #C0056
    ChrTalk(
        0x101,
        (
            "#00009F#6Pティオ、もう来てたんだな。\x02\x03",

            "#00002Fさっきはお疲れ。\x01",
            "おかげで助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#00211F#11P……わたしは多少、恥ずかしい思いを\x01",
            "してしまいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00006F#6Pうぐっ……面目ない。\x01",
            "俺の力が足りないばっかりに……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#00203F#11Pいえ、別にロイドさんが\x01",
            "謝ることでは。\x02\x03",

            "#00202F結果オーライでしたし\x01",
            "気にしないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "#04205F#5Pそういえばさっき\x01",
            "ビーチの方に行ってたらしいけど……\x01",
            "そこで何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00012F#6Pい、いや、ははは……\x02\x03",

            "#00000Fそ、それにしても、他のみんなは\x01",
            "まだ集まっていないみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#00204F#11Pええ、わたしたちは少し早めに\x01",
            "来てしまいましたので。\x02\x03",

            "#00202Fシュリさんにみっしぃの可愛さを\x01",
            "レクチャーしていたところです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    #C0063
    ChrTalk(
        0xA,
        (
            "#14011F#5Pい、いや、違うからな！？\x02\x03",

            "#14012F別に可愛いなんて\x01",
            "これっぽっちも思って──\x02\x03",

            "#14006Fっていうか、話題を変えんなっつの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20FE")

    label("loc_1FAA")


    #C0064
    ChrTalk(
        0x101,
        (
            "#00009F#6Pやあ、先に来てたのか。\x02\x03",

            "#00002F他のみんなはまだ\x01",
            "集まっていないみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#00204F#11Pわたしたちは少し早めに\x01",
            "来てしまいましたので。\x02\x03",

            "#00202Fシュリさんにみっしぃの可愛さを\x01",
            "レクチャーしていたところです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    #C0066
    ChrTalk(
        0xA,
        (
            "#14011F#5Pい、いや、違うからな！？\x02\x03",

            "#14012F別に可愛いなんて\x01",
            "これっぽっちも思って──\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FE")

    OP_93(0x8, 0x10E, 0x1F4)

    #C0067
    ChrTalk(
        0x8,
        (
            "#00203F#12P誤魔化しても無駄です。\x02\x03",

            "#00202F先ほどからシュリさんの\x01",
            "“気になるオーラ”を\x01",
            "バッチリ感知していますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        "#14011F#5Pなんだそのオーラって！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x153,
        "#01109F#6Pえへへ、仲良しだねー。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00002F#6P（うーん、ここでこのまま\x01",
            "  他の人たちを待つかな？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x145, 3)
    Jump("loc_2321")

    label("loc_2216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_2284")

    #C0071
    ChrTalk(
        0x8,
        (
            "#00202F#11P……先ほどはお疲れ様でした。\x02\x03",

            "ロイドさんたちも、\x01",
            "ここで皆さんを待っていますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C6")

    label("loc_2284")


    #C0072
    ChrTalk(
        0x8,
        (
            "#00200F#11Pロイドさんたちも、\x01",
            "ここで皆さんを待っていますか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C6")


    #C0073
    ChrTalk(
        0xA,
        "#14000F#11Pせっかくだし付き合っていけよ。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00002F#6P（うーん、どうしようかな？）\x02",
    )

    CloseMessageWindow()

    label("loc_2321")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",          # 0
            "【ここで他のみんなを待つ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2393"),
        (0, "loc_265B"),
        (SWITCH_DEFAULT, "loc_2723"),
    )


    label("loc_2393")


    def lambda_2398():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2398)
    Sleep(50)

    def lambda_23A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_23A8)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    #C0075
    ChrTalk(
        0x8,
        (
            "#00203F#11Pそれではお２人にも\x01",
            "改めてお伝えしましょう。\x02\x03",

            "#00201Fみっしぃがいかに\x01",
            "その愛らしさでゼムリア大陸の\x01",
            "平和に貢献しているかを……！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x153,
        "#01105F#6Pおー！\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)

    #C0077
    ChrTalk(
        0xA,
        "#14011F#5Pま、まだ続くのかっ！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    #C0078
    ChrTalk(
        0xA,
        (
            "#14007F#11Pおい、アンタも見てないで\x01",
            "ストップしてくれよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00006F#6P……まあ、諦めてくれ。\x02\x03",

            "#00012Fティオはみっしぃに関しては\x01",
            "とことん入れ込んでるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        "#14006F#11Pすでに諦めモードかよっ！？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やがて、ショッピングなどを\x01",
            "楽しんでいた他の面々も\x01",
            "待ち合わせ場所にやって来た。\x02\x03",

            "ロイドたちは受付に\x01",
            "入園用のパスポートを見せて\x01",
            "テーマパーク内へと足を踏み入れた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x52, 0xFF)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2723")

    label("loc_265B")


    def lambda_2660():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2660)
    Sleep(50)

    def lambda_2670():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2670)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    #C0082
    ChrTalk(
        0x8,
        (
            "#00200F#11Pあまり時間はないので\x01",
            "用を済ませるならお早めに。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#14003F#11Pフン……\x01",
            "とっとと戻って来いよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -8000, 4000, -12500, 0)
    EventEnd(0x5)
    Jump("loc_2723")

    label("loc_2723")

    Return()

    # Function_19_1B60 end

    def Function_20_2724(): pass

    label("Function_20_2724")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\cr036301.eff")
    OP_90(0x101, -4000, 5000, -30300, 0)
    OP_90(0x102, -4900, 5000, -31000, 0)
    OP_90(0x103, -3100, 5000, -31200, 0)
    OP_90(0x104, -4000, 5000, -32000, 0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x0, 0x24)
    OP_49()
    SetChrPos(0x24, 0, 4150, -17000, 195)
    OP_D5(0x24, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x1)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0x1, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4000, 3000, -26000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(16500, 2500)

    def lambda_287F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_287F)
    Sleep(100)

    def lambda_2897():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2897)
    Sleep(100)

    def lambda_28AF():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28AF)
    Sleep(100)

    def lambda_28C7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28C7)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0084
    ChrTalk(
        0x103,
        (
            "#00207F#6P──霊圧の上昇を感知！\x01",
            "気をつけてください！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00010F#5Pなに……！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_68(0, 6150, -17000, 2500)
    MoveCamera(330, 20, 0, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)
    SetCameraDistance(17500, 3000)
    Sound(919, 0, 100, 0)
    BeginChrThread(0x24, 0, 0, 21)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x24, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)

    def lambda_29F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_29F5)
    OP_75(0x0, 0x2, 0x3E8)
    WaitChrThread(0x24, 2)
    CancelBlur(1000)
    EndChrThread(0x24, 0x0)
    OP_6F(0x79)
    OP_68(-760, 4750, -26040, 2000)
    MoveCamera(336, 3, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(16870, 2000)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0086
    ChrTalk(
        0x102,
        "#00110F#5Pこ、これって……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        "#00307F#5P湿地帯に現れた化物かよ！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_71(0x0, 0x40, 0x63, 0x0, 0x8)
    Sound(842, 0, 100, 0)
    OP_82(0x64, 0x64, 0x1F40, 0x3E8)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(300)
    CancelBlur(1000)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Sleep(800)

    #C0088
    ChrTalk(
        0x103,
        (
            "#00207F#5P上位三属性の発動も\x01",
            "確認しました……！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00007F#5P迷ってる暇はない！\x01",
            "迎撃するぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#00301F#5Pアイサー！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#00107F#5P了解よ！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x8)
    OP_79(0x0)
    ClearChrFlags(0x24, 0x1)
    BlurSwitch(0x2BC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-1850, 3450, -26400, 800)
    SetCameraDistance(13000, 750)
    Sound(809, 0, 100, 0)
    Sound(251, 0, 100, 0)
    OP_74(0x0, 0x10)
    OP_71(0x0, 0xE5, 0xF8, 0x0, 0x8)

    def lambda_2C6B():
        OP_9D(0xFE, 0xFFFFF6D2, 0xB40, 0xFFFFA6FA, 0x708, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2C6B)
    Sleep(600)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_694", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 22)
    Return()

    # Function_20_2724 end

    def Function_21_2CA8(): pass

    label("Function_21_2CA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CCC")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_21_2CA8")

    label("loc_2CCC")

    Return()

    # Function_21_2CA8 end

    def Function_22_2CCD(): pass

    label("Function_22_2CCD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\bs000000.eff")
    LoadEffect(0x1, "battle\\bs000001.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_90(0x101, -4000, 5000, -21000, 45)
    OP_90(0x102, -5000, 5000, -22000, 45)
    OP_90(0x103, -3000, 5000, -22000, 45)
    OP_90(0x104, -4000, 5000, -23000, 45)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x0, 0x24)
    OP_49()
    SetChrPos(0x24, 0, 4150, -17000, 195)
    OP_D5(0x24, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x1)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0x2, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 6150, -17000, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    MoveCamera(330, 20, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x24, 0, 0, 21)
    BeginChrThread(0x24, 3, 0, 23)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x24, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x24, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_2EE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2EE8)
    OP_75(0x0, 0x1, 0x3E8)
    WaitChrThread(0x24, 2)
    CancelBlur(1000)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x24, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0x24, 0x80)
    Sleep(500)
    OP_68(-4000, 4400, -22000, 3000)
    MoveCamera(0, 20, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15000, 3000)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    #C0092
    ChrTalk(
        0x104,
        (
            "#00310F#6Pチッ……なんでこんな場所に\x01",
            "《幻獣》が現れやがったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#00203F#5P分かりません……\x02\x03",

            "#00201Fですが、この霊圧の高まりと\x01",
            "関係していると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#00106F#6Pそれと《僧院》と同じく\x01",
            "鐘の音も関係しているのかも\x01",
            "しれないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00008F#5Pそんな場所にキーアと\x01",
            "アリオスさんは……\x02\x03",

            "#00013Fとにかく中に入るぞ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0096
    ChrTalk(
        0x102,
        "#00107F#1K#1Pええ！\x02",
    )


    #C0097
    ChrTalk(
        0x103,
        "#00201F#1K#2Pはい！\x02",
    )


    #C0098
    ChrTalk(
        0x104,
        "#00307F#1K#6Pおおっ！\x02",
    )

    #Sound(2153, 255, 100, 0)    #voice#Elie
    #Sound(2249, 255, 100, 1)    #voice#Tio
    #Sound(2343, 255, 100, 2)    #voice#Randy
    OP_57(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, -4000, 4000, -19000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 6)
    OP_29(0xAD, 0x1, 0x3)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_22_2CCD end

    def Function_23_317E(): pass

    label("Function_23_317E")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_23_317E end

    def Function_24_319A(): pass

    label("Function_24_319A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41950.itc", 0x1E)
    LoadChrToIndex("chr/ch41951.itc", 0x1F)
    LoadChrToIndex("chr/ch41952.itc", 0x20)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(2953)
    SoundLoad(2954)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x106, 0x8)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x19, -2500, 0, -32000, 0)
    SetChrPos(0x1A, -3300, 0, -33500, 0)
    SetChrPos(0x1B, -4100, 0, -31500, 0)
    SetChrPos(0x1C, -4900, 0, -33000, 0)
    SetChrPos(0x1D, 2500, 0, -33500, 315)
    SetChrPos(0x1E, 3300, 0, -32000, 315)
    SetChrPos(0x1F, 4100, 0, -33000, 315)
    SetChrPos(0x20, 4900, 0, -31500, 315)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x1, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 4150, -17000, 180)
    OP_D5(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x1)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    OP_68(0, 8500, -17000, 0)
    MoveCamera(40, 38, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 7000, -17000, 2500)
    MoveCamera(0, -3, 0, 2500)
    SetCameraDistance(24000, 2500)
    Sound(913, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xBB8)
    BlurSwitch(0x5DC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x65, 0x8C, 0x0, 0x8)
    OP_79(0x1)
    CancelBlur(500)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x18, 0, 3900, -17000, 180)
    OP_68(0, 4550, -30000, 0)
    OP_68(0, 3550, -30000, 1500)
    MoveCamera(335, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    Sleep(500)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x19,
        "#5Pうおおっ！？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1E,
        "#11P報告にあった“神狼”か！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x1A,
        (
            "#5P怯むな！\x01",
            "連携して“狩る”ぞ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(180, 100, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetChrName("猟兵たち")

    #A0102
    AnonymousTalk(
        0xFF,
        "#4S了解#4Rヤ ー#！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_82(0x0, 0x64, 0xBB8, 0x1770)
    OP_68(0, 4550, -25000, 6000)
    MoveCamera(25, 0, 0, 6000)
    BeginChrThread(0x25, 1, 0, 28)
    BeginChrThread(0x19, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1A, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1B, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1C, 3, 0, 25)
    Sleep(50)
    OP_93(0x1D, 0x0, 0x0)
    BeginChrThread(0x1D, 3, 0, 25)
    Sleep(50)
    OP_93(0x1E, 0x0, 0x0)
    BeginChrThread(0x1E, 3, 0, 25)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x0)
    BeginChrThread(0x1F, 3, 0, 25)
    Sleep(50)
    OP_93(0x20, 0x0, 0x0)
    BeginChrThread(0x20, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0x18, 0, 0, 26)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x18, 0, 4150, -17000, 180)
    OP_68(-670, 8200, -20260, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Fade(250)
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x1, 0x1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(40, 150, -1, -1)
    SetChrName("神狼ツァイト")

    #A0103
    AnonymousTalk(
        0xFF,
        "#2953V#3C#4S#40W#35Aフム──意気やよし。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetCameraDistance(11500, 500)
    Sleep(1000)
    SetMessageWindowPos(20, 150, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetChrName("神狼ツァイト")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            "#2954V#3C#5S#30W#40Aならばこちらも\x01",
            "遠慮なく行かせてもらうぞ！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 7500, -20000, 1000)
    MoveCamera(25, 9, 0, 1000)
    SetCameraDistance(15000, 1000)
    EndChrThread(0x25, 0x1)
    Sound(913, 0, 100, 0)
    OP_82(0x0, 0x32, 0x1388, 0x3E8)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1E0, 0x1EA, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x118, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    OP_6F(0x79)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2000)
    OP_68(0, 7500, -28000, 500)
    MoveCamera(15, 0, 0, 500)
    SetCameraDistance(22000, 500)
    ClearChrFlags(0x18, 0x1)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x18, 3, 0, 27)
    Sleep(500)
    FadeToDark(500, 0, -1)
    StopSound(861, 1000, 50)
    StopSound(865, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_319A end

    def Function_25_394F(): pass

    label("Function_25_394F")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    TurnDirection(0xFE, 0x18, 500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)

    label("loc_397D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A4D")
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    Sleep(1000)
    Jump("loc_397D")

    label("loc_3A4D")

    Return()

    # Function_25_394F end

    def Function_26_3A4E(): pass

    label("Function_26_3A4E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C2E")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 3620, 4000, -18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 380, 2970, -22580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1120, 3400, -21510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -3740, 4000, -18570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -5270, 3340, -21650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 4550, 2940, -22640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -3250, 4160, -14820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 6190, 4000, -15970, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_26_3A4E")

    label("loc_3C2E")

    Return()

    # Function_26_3A4E end

    def Function_27_3C2F(): pass

    label("Function_27_3C2F")


    def lambda_3C34():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFF6F78, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C34)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x1EA, 0x1EF, 0x64, 0x8)
    OP_79(0x1)
    Return()

    # Function_27_3C2F end

    def Function_28_3C60(): pass

    label("Function_28_3C60")

    Sleep(1200)
    Sound(861, 2, 60, 0)

    label("loc_3C69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C8B")
    Sound(865, 2, 60, 0)
    Sleep(1000)
    StopSound(865, 200, 50)
    Sleep(400)
    Jump("loc_3C69")

    label("loc_3C8B")

    Return()

    # Function_28_3C60 end

    def Function_29_3C8C(): pass

    label("Function_29_3C8C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 600, 0, -62250, 0)
    SetChrPos(0x153, -600, 0, -62250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3D30():
        OP_95(0xFE, 600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D30)

    def lambda_3D4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D4A)
    Sleep(200)

    def lambda_3D5E():
        OP_95(0xFE, -600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3D5E)

    def lambda_3D78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_3D78)
    Sound(107, 0, 100, 0)
    SetCameraDistance(25000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x153, 2)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(3029, 255, 100, 0)    #voice#KeA

    #C0105
    ChrTalk(
        0x153,
        "#01102Fうわぁ……！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 4500, -47400, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(10020, 3000)
    OP_6F(0x79)
    OP_25(0x335, 0x50)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4250, -9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-20, 9500, -8210, 0)
    MoveCamera(337, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27300, 0)
    OP_68(-20, 5300, -8210, 8000)
    OP_6F(0x1)
    OP_0D()
    OP_25(0x335, 0x28)
    Fade(1000)
    StopEffect(0x0, 0x0)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()

    #C0106
    ChrTalk(
        0x153,
        "#01109F#5P……ロイド、何だかスゴそうだよ！！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00009F#6Pああ、俺もちょっと\x01",
            "ワクワクしてきたよ。\x02\x03",

            "#00000Fさて、と……\x01",
            "もしかしたらもう誰かが\x01",
            "来てるかもしれない。\x02\x03",

            "とりあえず行ってみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x153,
        "#01110F#5Pうんっ！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15B, 1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_29_3C8C end

    def Function_30_4002(): pass

    label("Function_30_4002")

    EventBegin(0x0)
    OP_4B(0x17, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5830, 7000, -1410, 0)
    MoveCamera(306, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -8720, 4000, -6130, 0)
    SetChrPos(0x102, -7550, 4000, -6410, 0)
    SetChrPos(0x103, -9480, 4000, -6890, 0)
    SetChrPos(0x104, -7960, 4000, -7290, 0)
    SetChrPos(0x109, -8800, 4000, -8240, 0)
    SetChrPos(0x105, -7400, 4000, -8240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0x17,
        (
            "#11Pああ困った。\x01",
            "午前のスケジュールも\x01",
            "あるのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-6020, 6700, -2510, 3000)
    MoveCamera(310, 29, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20870, 3000)

    def lambda_4130():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4130)
    Sleep(50)

    def lambda_414D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_414D)
    Sleep(50)

    def lambda_416A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_416A)
    Sleep(50)

    def lambda_4187():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4187)
    Sleep(50)

    def lambda_41A4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41A4)
    Sleep(50)

    def lambda_41C1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41C1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0110
    ChrTalk(
        0x101,
        (
            "#00000Fあの、失礼します。\x01",
            "特務支援課の者です。\x02\x03",

            "要請をみて伺ったのですが……\x01",
            "あなたがハンクスさんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x17,
        (
            "おお、おお！\x01",
            "君たちが特務支援課かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x17,
        "ふむ、ふむふむふむ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x17, 0xB4, 0x1F4)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x17,
        (
            "……うん、きみなら\x01",
            "ばっちり体格が合いそうだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00005Fた、体格……？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        (
            "#6P#00100Fあの、よろしければ事情を\x01",
            "聞かせていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x17,
        (
            "ああ、そうだった！\x01",
            "僕としたことが……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x17,
        (
            "……君たちはもちろん、\x01",
            "あの『みっしぃ』を\x01",
            "知っているよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x103,
        "#00203Fええ、人並みには。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        (
            "#6P#00306Fティオすけは\x01",
            "マニアの域だろ……\x02\x03",

            "#00300Fまあ、クロスベルに住んでて\x01",
            "みっしぃを知らない奴なんて\x01",
            "ほとんどいないとは思うが。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x105,
        (
            "#6P#10300Fそのみっしぃが\x01",
            "どうかしたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x17,
        (
            "ああ、実は……\x01",
            "今朝方ある連絡があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x17,
        (
            "創設時からみっしぃを\x01",
            "演じてた役者さんが、\x01",
            "事情で来れなくなったんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x109,
        (
            "#6P#10105F事情で……\x01",
            "なにか問題があったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x17,
        "どうも、急な腹痛らしくてね。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x17,
        (
            "ウルスラ病院で\x01",
            "薬をもらってから\x01",
            "来るそうなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x17,
        (
            "午前の部には\x01",
            "完全に間に合わない\x01",
            "みたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x17,
        (
            "そこで、君たちには……\x01",
            "みっしぃの着ぐるみの\x01",
            "代役をやって欲しいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#00005Fみっしぃの代役を……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#6P#00309Fへえ……\x01",
            "面白そうじゃねぇか。\x02\x03",

            "#00304Fよし、ここはこの俺が──！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x17,
        (
            "いやー、キミじゃちょっと\x01",
            "サイズが合わないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x17,
        (
            "ちょうど、そこの\x01",
            "真面目そうなきみに\x01",
            "ピッタリくらいだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00011Fお、俺ですか？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x104,
        (
            "#6P#4S#00307Fガガーン！！\x02\x03",

            "#00306F観光客の女の子と\x01",
            "いちゃいちゃする計画が……！\x02\x03",

            "#00310Fおのれ、ロイド……！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#00006Fあ、あのな……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x109,
        "#6P#10112Fさすがに言いがかりでは……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x17,
        (
            "それじゃあ……\x01",
            "アルバイトを引き受けて\x01",
            "くれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#00000F分かりました、\x01",
            "お引き受けしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x17,
        (
            "ああ、ありがとう。\x01",
            "じゃあさっそく……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0x103)
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0139
    ChrTalk(
        0x102,
        (
            "#12P#00105F……ティオちゃん？\x01",
            "どうしたの、黙っちゃって……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_495C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_495C)
    Sleep(50)

    def lambda_496C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_496C)
    Sleep(50)

    def lambda_497C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_497C)
    Sleep(300)

    #C0140
    ChrTalk(
        0x103,
        (
            "#00205F……着ぐるみ……中の人……\x01",
            "…………腹痛で薬を…………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x109,
        (
            "#6P#10111F（な、なんだか\x01",
            "  様子がおかしいですね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x105,
        (
            "#6P#10303F（まあ、これだけ\x01",
            "  楽屋裏の話を聞かされれば\x01",
            "  普通はショックなんじゃない？）\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#11P#00011F（そ、それもそうか……）\x02\x03",

            "#00012F……そ、その……ティオ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0144
    ChrTalk(
        0x103,
        (
            "#00203F……何でもありません。\x02\x03",

            "#00201Fみっしぃのためならば、\x01",
            "わたしも喜んで協力します。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#12P#00309Fはは、その意気だぜ。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#11P#00006F（ホントに大丈夫なのかな……）\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x17,
        "話はまとまったかな？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x17,
        (
            "それじゃあロッカールームに\x01",
            "案内させていただくよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C36():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C36)
    Sleep(50)

    def lambda_4C46():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4C46)
    Sleep(50)

    def lambda_4C56():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4C56)
    Sleep(50)

    def lambda_4C66():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4C66)
    Sleep(50)

    def lambda_4C76():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4C76)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0149
    ChrTalk(
        0x101,
        (
            "#00012Fあ……\x01",
            "え、ええ、お願いします。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【テーマパークのアルバイト】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x176, 4)
    SetScenarioFlags(0x22, 0)
    NewScene("t1390", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_4002 end

    def Function_31_4D39(): pass

    label("Function_31_4D39")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch20200.itc", 0x20)
    LoadChrToIndex("chr/ch20300.itc", 0x21)
    LoadChrToIndex("chr/ch23800.itc", 0x22)
    LoadEffect(0x0, "battle/ms00109.eff")
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x21)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x22)
    SetChrFlags(0x23, 0x8000)
    OP_52(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(3220, 7060, -19270, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19020, 0)
    SetChrPos(0x101, 360, 4160, -15840, 180)
    SetChrPos(0x103, -1060, 4140, -15840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)
    SetCameraDistance(17900, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0151
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206Fふう……\x01",
            "いよいよ始まってしまったな。\x01",
            "どうなることやら……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F──あ。\x01",
            "さっそく来ましたよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3750, 7160, -21000, 5000)
    SetCameraDistance(19340, 5000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x21, -470, 480, -28790, 0)
    SetChrPos(0x22, 980, 480, -28800, 0)
    SetChrPos(0x23, 130, 1110, -27230, 0)

    def lambda_4F58():
        OP_95(0xFE, 130, 4000, -16840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_4F58)
    Sleep(50)

    def lambda_4F75():
        OP_95(0xFE, -470, 4000, -18440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4F75)
    Sleep(50)

    def lambda_4F92():
        OP_95(0xFE, 980, 4000, -18640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4F92)
    Sleep(50)

    def lambda_4FAF():
        OP_95(0xFE, -7890, 4000, -16239, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FAF)
    WaitChrThread(0x103, 1)

    def lambda_4FCD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4FCD)
    WaitChrThread(0x23, 1)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x23,
        "うわ～、みっしぃだあ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    #C0154
    ChrTalk(
        0x23,
        (
            "ねえ、みっしぃだよ！\x01",
            "ほんものだよ～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x21,
        "はは、そうだともそうだとも。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x22,
        (
            "ふふ、こんなところで\x01",
            "はしゃいでたら\x01",
            "元気が持たないわよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x0, 0x3E8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)

    #C0157
    ChrTalk(
        0x23,
        (
            "わ～い、わ～い！\x01",
            "みっしぃ、みっしぃ～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（え、えーっと……\x01",
            "  こういうとき、みっしぃなら\x01",
            "  どう答えるべきか……？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "みししっ、楽しんでいってネ～♪\x01",      # 0
            "入場券はあっちで買ってネ～♪\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5205"),
        (1, "loc_5262"),
        (SWITCH_DEFAULT, "loc_52D5"),
    )


    label("loc_5205")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 5)

    #C0159
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでいってネ～♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x23,
        "うん、ありがとうみっしぃ～！\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x1)
    Jump("loc_52D5")

    label("loc_5262")


    #C0161
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "入場券はあっちで買ってネ～♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x23,
        (
            "う、うん……\x01",
            "ありがとうみっしぃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x2)
    Jump("loc_52D5")

    label("loc_52D5")

    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    #C0163
    ChrTalk(
        0x23,
        (
            "おとーさんおかーさん、\x01",
            "早く入ろうよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x21,
        "はは、わかったわかった。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x22,
        "今日は一日楽しみましょ～。\x02",
    )

    CloseMessageWindow()
    OP_68(3220, 7060, -19270, 3000)
    MoveCamera(315, 20, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19020, 3000)
    BeginChrThread(0x23, 3, 0, 34)
    Sleep(50)
    BeginChrThread(0x22, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x21, 3, 0, 32)
    Sleep(50)

    def lambda_5398():

        label("loc_5398")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_5398")

    QueueWorkItem2(0x101, 1, lambda_5398)
    Sleep(300)

    def lambda_53AD():
        OP_95(0xFE, -1060, 4140, -15840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53AD)
    WaitChrThread(0x103, 1)

    def lambda_53CB():

        label("loc_53CB")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_53CB")

    QueueWorkItem2(0x103, 1, lambda_53CB)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x21, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AA")

    #C0166
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202Fふう、何とかなったか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0167
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524Fロイドさん、ナイスです。\x02\x03",

            "#05522Fみっしぃの笑い方も\x01",
            "なかなか自然でしたし。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0168
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212Fちょ、ちょっとだけ\x01",
            "恥ずかしいけどな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05529Fみししっ♪\x02\x03",

            "#05526F……コホン。\x01",
            "慣れればどうという\x01",
            "ことはないです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212Fお、おみそれしました。\x01",
            "（なるほど、\x01",
            "  普通にかわいいな……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522Fこの調子でがんばりましょう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57CA")

    label("loc_55AA")


    #C0172
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202Fふう、何とかなった……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 360, 4300, -15840, 90, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    #Sound(2030, 255, 70, 0)    #voice#Lloyd

    #C0173
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211Fうっ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x7EE)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0174
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05531F……何とかなってません。\x02\x03",

            "#05526Fロイドさん、みっしぃは\x01",
            "従業員ではないんですから……\x01",
            "『入場券』はないでしょう。\x02\x03",

            "#05521F夢の世界へとにこやかに\x01",
            "迎え入れてあげるべき存在としては\x01",
            "禁句レベルの発言ですよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0175
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206Fす、すみませんでした。\x01",
            "（難しいな……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526Fまったく……\x01",
            "次はちゃんとしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57CA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4D39 end

    def Function_32_57E2(): pass

    label("Function_32_57E2")

    OP_97(0x21, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x21, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_32_57E2 end

    def Function_33_580B(): pass

    label("Function_33_580B")

    OP_97(0x22, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x22, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_33_580B end

    def Function_34_5834(): pass

    label("Function_34_5834")

    OP_97(0x23, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x23, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_34_5834 end

    def Function_35_585D(): pass

    label("Function_35_585D")

    Return()

    # Function_35_585D end

    def Function_36_585E(): pass

    label("Function_36_585E")

    Return()

    # Function_36_585E end

    def Function_37_585F(): pass

    label("Function_37_585F")

    Sleep(1000)

    label("loc_5862")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5884")
    Sound(918, 0, 40, 0)
    Sleep(2200)
    Sound(918, 0, 30, 0)
    Sleep(5000)
    Jump("loc_5862")

    label("loc_5884")

    Return()

    # Function_37_585F end

    def Function_38_5885(): pass

    label("Function_38_5885")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_597C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_593C")

    #C0177
    ChrTalk(
        0x101,
        "#00000Fこっちはテーマパークだな。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、焦らなくても\x01",
            "午後はここで遊ぶんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#00309Fおうよ、今はとにかく\x01",
            "ビーチに向かうぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_597C")

    label("loc_593C")


    #C0180
    ChrTalk(
        0x101,
        (
            "#00000Fテーマパークは午後の予定だ。\x01",
            "今はビーチに向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_597C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A21")

    #C0181
    ChrTalk(
        0x153,
        (
            "#01105Fねえ、ロイド。\x01",
            "先に入っちゃうの？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ごめん。\x01",
            "抜け駆けはいけないな。\x02\x03",

            "#00004F中に入るならみんなを待とう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5A69")

    label("loc_5A21")


    #C0183
    ChrTalk(
        0x101,
        (
            "#00000Fおっと、抜け駆けはいけないな。\x01",
            "中に入るならみんなを待とう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A69")

    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_38_5885 end

    def Function_39_5A7E(): pass

    label("Function_39_5A7E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークの\x01",
            "見取り図が描かれている。\x02\x03",

            "広大な敷地に\x01",
            "さまざまなアミューズメント施設が\x01",
            "並んでいるようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_39_5A7E end

    def Function_40_5AFE(): pass

    label("Function_40_5AFE")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ～こ来園のみなさまへ～\x01\x01",
            "当テーマパーク内での\x01",
            "暴走行為や危険物の持ち込みは\x01",
            "固くお断り申し上げます。\x01\x01",
            "また、お子様には必ず\x01",
            "保護者の方が同伴なさるよう\x01",
            "お願い申し上げます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_40_5AFE end

    SaveToFile()

Try(main)
