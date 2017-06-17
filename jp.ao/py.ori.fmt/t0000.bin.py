from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0000.bin",                # FileName
        "t0000",                    # MapName
        "t0000",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0000",                  # 0
        "カミーユ",               # 1
        "エルキン",               # 2
        "プーリー",               # 3
        "ステファン",             # 4
        "デリック",               # 5
        "ミンネス",               # 6
        "アレサ",                 # 7
        "ソフィア",               # 8
        "コリン",                 # 9
        "遊撃士スコット",         # 10
        "バス",                   # 11
        "特務支援車",             # 12
        "メルカバ玖号機",         # 13
        "メルカバ光学迷彩",       # 14
        "メルカバ影",             # 15
        "キース",                 # 16
        "遊撃士リン",             # 17
        "遊撃士エオリア",         # 18
        "アンジェ",               # 19
        "ゴーファン",             # 20
        "シーリィ",               # 21
        "トルタ村長",             # 22
        "ピート",                 # 23
        "ハロルド",               # 24
        "猫型魔獣",               # 25
        "猫型魔獣",               # 26
        "猫型魔獣",               # 27
        "猫型魔獣",               # 28
        "猫型魔獣",               # 29
        "黒い運搬車",             # 30
        "アルム",                 # 31
        "エアリー",               # 32
        "SE制御",                 # 33
        "bt0000",                 # 34
        "bt0000",                 # 35
        "アルモリカ古道",         # 36
    ))

    ATBonus("ATBonus_6B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_6D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_758", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_75C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_760", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_764", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_768", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_76C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_774", 0x0062, 255, 6, 45, 3, 3, 30, 0, "bt0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32000.dat", "ms32100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_754", "ed7451", "ed7453", "ATBonus_6B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7B8", 0x0062, 255, 6, 45, 3, 3, 30, 0, "bt0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32001.dat", "ms32101.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_754", "ed7452", "ed7453", "ATBonus_6B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24600.itc",                   # 00
        "chr/ch24400.itc",                   # 01
        "chr/ch24700.itc",                   # 02
        "chr/ch20600.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch45200.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch09400.itc",                   # 07
        "chr/ch07200.itc",                   # 08
        "chr/ch27200.itc",                   # 09
        "chr/ch46300.itc",                   # 0A
        "chr/ch46200.itc",                   # 0B
    ))

    DeclNpc(-6869,   0,       24790,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8409,    0,       -12479,  17,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-6110,   0,       23270,   315,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-7829,   0,       23860,   107,  261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(12779,   3500,    40220,   298,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-500,    500,     6000,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(11369,   0,       19389,   280,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(10010,   0,       19659,   280,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-8699,   0,       25250,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(3170,    0,       14229,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2119,    0,       13670,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 33,  8.40999984741211,      -12.479999542236328,   -1.0,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -1.6820000410079956,   2.496000051498413,     0.3333333432674408,    1.0])
    DeclEvent(0x0000, 0, 34,  -2.130000114440918,    12.520000457763672,    -1.100000023841858,    270.27362060546875,    [0.24330902099609375,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1250000149011612,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333730697632,    0.0,                   0.5182482600212097,    -1.565000295639038,    0.366666704416275,     1.0])
    DeclEvent(0x0000, 0, 64,  0.5400000214576721,    -8.800000190734863,    -0.0,                  144.0,                 [0.16666655242443085,  0.10825320333242416,   -0.0,                  0.0,                   -0.2886752188205719,   0.06249995902180672,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -2.6303420066833496,   0.49154290556907654,   -0.0,                  1.0])

    DeclActor(-2000,   0,       -15000,  1500,    -2000,   1500,    -15000,  0x007C, 0,  23, 0x0000)
    DeclActor(11740,   0,       3950,    1200,    10890,   -1450,   1210,    0x007C, 0,  24, 0x0000)
    DeclActor(15990,   0,       -19440,  1200,    15990,   2000,    -19440,  0x007C, 0,  22, 0x0000)
    DeclActor(-17300,  3500,    63700,   1500,    -41000,  1000,    91000,   0x007C, 0,  22, 0x0000)
    DeclActor(15550,   3520,    47700,   1200,    15550,   4520,    47700,   0x007C, 0,  65, 0x0000)

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "アルモリカ古道")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2404, 0)                                       # 0

    ScpFunction((
        "Function_0_964",          # 00, 0
        "Function_1_A1C",          # 01, 1
        "Function_2_12CF",         # 02, 2
        "Function_3_175B",         # 03, 3
        "Function_4_184B",         # 04, 4
        "Function_5_195E",         # 05, 5
        "Function_6_1994",         # 06, 6
        "Function_7_19E5",         # 07, 7
        "Function_8_1A79",         # 08, 8
        "Function_9_3054",         # 09, 9
        "Function_10_3B50",        # 0A, 10
        "Function_11_3DE6",        # 0B, 11
        "Function_12_447D",        # 0C, 12
        "Function_13_4C7D",        # 0D, 13
        "Function_14_5401",        # 0E, 14
        "Function_15_5521",        # 0F, 15
        "Function_16_55F9",        # 10, 16
        "Function_17_5786",        # 11, 17
        "Function_18_584E",        # 12, 18
        "Function_19_5900",        # 13, 19
        "Function_20_5C89",        # 14, 20
        "Function_21_5DCC",        # 15, 21
        "Function_22_5EC9",        # 16, 22
        "Function_23_620C",        # 17, 23
        "Function_24_6258",        # 18, 24
        "Function_25_632C",        # 19, 25
        "Function_26_656E",        # 1A, 26
        "Function_27_78A4",        # 1B, 27
        "Function_28_8D98",        # 1C, 28
        "Function_29_8F64",        # 1D, 29
        "Function_30_BAF6",        # 1E, 30
        "Function_31_BC0A",        # 1F, 31
        "Function_32_BC27",        # 20, 32
        "Function_33_C0F7",        # 21, 33
        "Function_34_CB66",        # 22, 34
        "Function_35_12DA0",       # 23, 35
        "Function_36_12DD4",       # 24, 36
        "Function_37_12E08",       # 25, 37
        "Function_38_12E3C",       # 26, 38
        "Function_39_12E70",       # 27, 39
        "Function_40_12EA4",       # 28, 40
        "Function_41_12ED8",       # 29, 41
        "Function_42_12F0C",       # 2A, 42
        "Function_43_12F40",       # 2B, 43
        "Function_44_12F74",       # 2C, 44
        "Function_45_12FA8",       # 2D, 45
        "Function_46_12FDC",       # 2E, 46
        "Function_47_13010",       # 2F, 47
        "Function_48_13044",       # 30, 48
        "Function_49_13078",       # 31, 49
        "Function_50_130AC",       # 32, 50
        "Function_51_130D4",       # 33, 51
        "Function_52_130F7",       # 34, 52
        "Function_53_1316C",       # 35, 53
        "Function_54_131F5",       # 36, 54
        "Function_55_1326A",       # 37, 55
        "Function_56_132F3",       # 38, 56
        "Function_57_13368",       # 39, 57
        "Function_58_133B3",       # 3A, 58
        "Function_59_133FE",       # 3B, 59
        "Function_60_13449",       # 3C, 60
        "Function_61_13494",       # 3D, 61
        "Function_62_134DF",       # 3E, 62
        "Function_63_1353E",       # 3F, 63
        "Function_64_13558",       # 40, 64
        "Function_65_1383B",       # 41, 65
        "Function_66_13D12",       # 42, 66
        "Function_67_14347",       # 43, 67
        "Function_68_14375",       # 44, 68
        "Function_69_143B7",       # 45, 69
        "Function_70_143F9",       # 46, 70
        "Function_71_1443B",       # 47, 71
        "Function_72_1447D",       # 48, 72
        "Function_73_144BF",       # 49, 73
        "Function_74_14501",       # 4A, 74
        "Function_75_14C04",       # 4B, 75
        "Function_76_14C46",       # 4C, 76
        "Function_77_15D0A",       # 4D, 77
        "Function_78_162BE",       # 4E, 78
        "Function_79_16303",       # 4F, 79
        "Function_80_16351",       # 50, 80
        "Function_81_163B6",       # 51, 81
        "Function_82_1669D",       # 52, 82
        "Function_83_166C8",       # 53, 83
        "Function_84_166F3",       # 54, 84
        "Function_85_1671E",       # 55, 85
        "Function_86_1674D",       # 56, 86
        "Function_87_174B7",       # 57, 87
        "Function_88_17598",       # 58, 88
        "Function_89_175AE",       # 59, 89
    ))


    def Function_0_964(): pass

    label("Function_0_964")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9A4"),
        (1, "loc_9B0"),
        (2, "loc_9BC"),
        (3, "loc_9C8"),
        (4, "loc_9D4"),
        (5, "loc_9E0"),
        (6, "loc_9EC"),
        (SWITCH_DEFAULT, "loc_9F8"),
    )


    label("loc_9A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_A04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A1B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_A1B")

    Return()

    # Function_0_964 end

    def Function_1_A1C(): pass

    label("Function_1_A1C")

    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A5B")
    SetChrPos(0x9, 11050, 0, -22040, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -19420, 3500, 60540, 330)
    Jump("loc_C7C")

    label("loc_A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ADA")
    SetChrPos(0x8, -7700, 0, 24530, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    SetChrPos(0xB, -6700, 0, 25250, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5850, 0, 15680, 175)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD5")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_AD5")

    Jump("loc_C7C")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AFE")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18860, 3500, 52530, 240)
    Jump("loc_C7C")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B66")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 7300, 0, -11420, 135)
    TurnDirection(0x9, 0xC, 0)
    SetChrPos(0x8, -7700, 0, 24530, 0)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B61")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_B61")

    Jump("loc_C7C")

    label("loc_B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B74")
    Jump("loc_C7C")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B96")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_C7C")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BA4")
    Jump("loc_C7C")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_END)), "loc_BBB")
    SetChrFlags(0x9, 0x10)

    label("loc_BBB")

    Jump("loc_C7C")

    label("loc_BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE2")
    SetChrFlags(0x9, 0x80)

    label("loc_BE2")

    SetChrFlags(0xB, 0x10)
    Jump("loc_C7C")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C13")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_C7C")

    label("loc_C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C30")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C7C")

    label("loc_C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C52")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_C7C")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C65")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_C7C")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C73")
    Jump("loc_C7C")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C7C")

    label("loc_C7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D09")
    SetScenarioFlags(0x38, 0)

    label("loc_D09")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1F")
    SetScenarioFlags(0x38, 1)

    label("loc_D1F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    SetScenarioFlags(0x38, 2)

    label("loc_D35")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    SetScenarioFlags(0x38, 3)

    label("loc_D4B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    SetScenarioFlags(0x38, 4)

    label("loc_D61")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    SetScenarioFlags(0x38, 5)

    label("loc_D77")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8D")
    SetScenarioFlags(0x38, 6)

    label("loc_D8D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA3")
    SetScenarioFlags(0x38, 7)

    label("loc_DA3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB9")
    SetScenarioFlags(0x39, 0)

    label("loc_DB9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF")
    SetScenarioFlags(0x39, 1)

    label("loc_DCF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE5")
    SetScenarioFlags(0x39, 2)

    label("loc_DE5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFB")
    SetScenarioFlags(0x39, 3)

    label("loc_DFB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E11")
    SetScenarioFlags(0x39, 4)

    label("loc_E11")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E27")
    SetScenarioFlags(0x39, 5)

    label("loc_E27")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D")
    SetScenarioFlags(0x39, 6)

    label("loc_E3D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E53")
    SetScenarioFlags(0x39, 7)

    label("loc_E53")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E69")
    SetScenarioFlags(0x3A, 0)

    label("loc_E69")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7F")
    SetScenarioFlags(0x3A, 1)

    label("loc_E7F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E95")
    SetScenarioFlags(0x3A, 2)

    label("loc_E95")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAB")
    SetScenarioFlags(0x3A, 3)

    label("loc_EAB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC1")
    SetScenarioFlags(0x3A, 4)

    label("loc_EC1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED7")
    SetScenarioFlags(0x3A, 5)

    label("loc_ED7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EED")
    SetScenarioFlags(0x3A, 6)

    label("loc_EED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F03")
    SetScenarioFlags(0x3A, 7)

    label("loc_F03")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F19")
    SetScenarioFlags(0x3B, 0)

    label("loc_F19")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2F")
    SetScenarioFlags(0x3B, 1)

    label("loc_F2F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F45")
    SetScenarioFlags(0x3B, 2)

    label("loc_F45")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5B")
    SetScenarioFlags(0x3B, 3)

    label("loc_F5B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F71")
    SetScenarioFlags(0x3B, 4)

    label("loc_F71")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F87")
    SetScenarioFlags(0x3B, 5)

    label("loc_F87")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9D")
    SetScenarioFlags(0x3B, 6)

    label("loc_F9D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB3")
    SetScenarioFlags(0x3B, 7)

    label("loc_FB3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC9")
    SetScenarioFlags(0x3D, 5)

    label("loc_FC9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")
    SetScenarioFlags(0x3D, 6)

    label("loc_FDF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF5")
    SetScenarioFlags(0x3D, 7)

    label("loc_FF5")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1030")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1120")

    label("loc_1030")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1053")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1120")

    label("loc_1053")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1076")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1120")

    label("loc_1076")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1120")

    label("loc_1099")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BC")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1120")

    label("loc_10BC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DF")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1120")

    label("loc_10DF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1120")

    label("loc_1102")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    SetScenarioFlags(0x3C, 7)

    label("loc_1120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1136")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117E")
    SetChrPos(0x0, 15150, 0, -19900, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 7)

    label("loc_117E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_11B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B1")
    SetChrPos(0x0, -17300, 3500, 63700, 150)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_11DB")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D8")
    Event(0, 86)
    Jump("loc_11DB")

    label("loc_11D8")

    Event(0, 6)

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11F2")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1, 4)
    Event(0, 25)
    Jump("loc_1232")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1209")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 4)
    Event(0, 66)
    Jump("loc_1232")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1220")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 4)
    Event(0, 74)
    Jump("loc_1232")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1232")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 76)

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1248")
    Event(0, 77)
    Jump("loc_12CE")

    label("loc_1248")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1267")
    Event(0, 81)
    Jump("loc_12CE")

    label("loc_1267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129C")
    Event(0, 32)
    Jump("loc_12CE")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CE")
    SetMapFlags(0x10000000)
    Event(0, 86)

    label("loc_12CE")

    Return()

    # Function_1_A1C end

    def Function_2_12CF(): pass

    label("Function_2_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_12E1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_12F5")
    OP_24(0x7B)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_132B")

    label("loc_12F5")

    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0x1B26, 0x1F4, 0x143C)
    OP_E3(0x7936, 0x1F4, 0xFFFFFD6C)

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1346")
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x0)

    label("loc_1346")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1366")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_14FA")

    label("loc_1366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1393")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13C0")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D4")
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_14FA")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1454")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144F")
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0x25)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    OP_74(0xD, 0x1E)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 13000, 0, -11540, 20)
    OP_D5(0x25, 0x0, 0x4E20, 0x0, 0x0)

    label("loc_144F")

    Jump("loc_14FA")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1492")
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_147A")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_147A")

    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14A6")
    ClearMapObjFlags(0xD, 0x4)
    Jump("loc_14FA")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_14B4")
    Jump("loc_14FA")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14C2")
    Jump("loc_14FA")

    label("loc_14C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14E3")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_14E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14F1")
    Jump("loc_14FA")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_14FA")

    label("loc_14FA")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151B")
    OP_66(0x4, 0x1)

    label("loc_151B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_154A")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_157C")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1686")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "flower00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "p_kusa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point0_add", 0x1, 0x1)
    Jump("loc_16C6")

    label("loc_1686")

    SetMapObjFrame(0xFF, "flower00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "p_kusa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point0_add", 0x0, 0x1)

    label("loc_16C6")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_16FD")
    ClearMapObjFlags(0x11, 0x4)

    label("loc_16FD")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 10890, -1450, 1210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175A")
    OP_1B(0x0, 0x0, 0x59)

    label("loc_175A")

    Return()

    # Function_2_12CF end

    def Function_3_175B(): pass

    label("Function_3_175B")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kバス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市東口\x01",      # 0
            "タングラム門\x01",          # 1
            "停留所（三叉路）\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FE")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1843")

    label("loc_17FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1823")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1843")

    label("loc_1823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1843")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_1843")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_3_175B end

    def Function_4_184B(): pass

    label("Function_4_184B")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_195A")
    Fade(500)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -400, 0, -15300, 135)
    SetChrPos(0x1, -1230, 0, -15500, 135)
    SetChrPos(0x2, -2000, 0, -15700, 135)
    SetChrPos(0x3, -2750, 0, -15900, 135)
    ClearChrFlags(0x12, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x12)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x12, 13270, 0, -22560, 0)
    OP_D5(0x12, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x12, 1, 0, 5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_195A")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_4_184B end

    def Function_5_195E(): pass

    label("Function_5_195E")

    OP_95(0x12, 10630, 0, -20520, 4000, 0x0)
    OP_9E(0x12, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xFA0, 0x1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_5_195E end

    def Function_6_1994(): pass

    label("Function_6_1994")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -700, 0, -13900, 135)
    OP_31(0x1)
    OP_68(-690, 1500, -13900, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    EventEnd(0x5)
    Return()

    # Function_6_1994 end

    def Function_7_19E5(): pass

    label("Function_7_19E5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1A40")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A35")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1A3B")

    label("loc_1A35")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1A3B")

    Jump("loc_1A64")

    label("loc_1A40")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A5E")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1A64")

    label("loc_1A5E")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1A64")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_19E5 end

    def Function_8_1A79(): pass

    label("Function_8_1A79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B56")

    #C0002
    ChrTalk(
        0x9,
        (
            "お、おったまげただ……\x01",
            "あの大きな樹は一体なんなんだぁ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "いきなりあんなものが現れるなんて、\x01",
            "どう考えても普通じゃねえだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "楽しく運転が出来る日々には\x01",
            "もう戻れねえだか……！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BDA")

    label("loc_1B56")


    #C0005
    ChrTalk(
        0x9,
        (
            "いきなりあんなものが現れるなんて、\x01",
            "クロスベルはどうなっちまうんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "楽しく運転が出来る日々には\x01",
            "もう戻れねえだか……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDA")

    Jump("loc_3050")

    label("loc_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC4")

    #C0007
    ChrTalk(
        0x9,
        (
            "独立国の無効宣言が\x01",
            "出されたんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "実際、気ままにドライブを楽しめる\x01",
            "元のクロスベルの方がいいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "独立なんてよく分からなかったし、\x01",
            "このまま何もかもが\x01",
            "元に戻ってくれればいいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D6C")

    label("loc_1CC4")


    #C0010
    ChrTalk(
        0x9,
        (
            "独立国なんかより、\x01",
            "気ままにドライブを楽しめる\x01",
            "元のクロスベルの方がいいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "無効宣言も出されたみたいだし、\x01",
            "このまま何もかもが\x01",
            "元に戻ってくれればいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6C")

    Jump("loc_3050")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7B")

    #C0012
    ChrTalk(
        0x9,
        (
            "街道の移動規制で\x01",
            "バスも車もほとんど来ない状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "たまに村に来る国防軍の装甲車も\x01",
            "カッコイイとは思うけど……\x01",
            "正直、見飽きちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "《幻獣》なんかが出るから\x01",
            "気ままにドライブもできないし……\x01",
            "こんな状態、いつまで続くんだ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F17")

    label("loc_1E7B")


    #C0015
    ChrTalk(
        0x9,
        (
            "街道の移動規制で、\x01",
            "村には国防軍の装甲車が\x01",
            "たまに来るくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "《幻獣》なんかが出るから\x01",
            "ドライブもできないし……\x01",
            "こんな状態、いつまで続くんだ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_3050")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FAA")

    #C0017
    ChrTalk(
        0xFE,
        (
            "あんな襲撃事件があったんじゃ、\x01",
            "街道に出るのも恐ろしくなるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "こういうときこそ、僕たちが\x01",
            "村を守っていかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3050")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FB8")
    Jump("loc_3050")

    label("loc_1FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_230A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205E")

    #C0019
    ChrTalk(
        0xFE,
        (
            "デリックとミンネスさんの計画は\x01",
            "かなり佳境まで来ているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "この村がどんな風に\x01",
            "発展していくのか……\x01",
            "ふふ、楽しみでならないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_205E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A6")

    #C0021
    ChrTalk(
        0xFE,
        (
            "はあ、でもまさかミンネスさんが\x01",
            "詐欺師だったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "なあ君たち、彼から\x01",
            "買ってしまったこの導力車……\x01",
            "どうしたらいいと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x109,
        (
            "#10101F確か、５０万ミラほどが\x01",
            "相場の導力トラックを、\x01",
            "５万ミラで買ったって話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#00003Fう、う～ん……\x01",
            "確かに微妙な問題だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#00100F一旦、警察に引き渡して\x01",
            "判断を任せたほうが\x01",
            "いいかもしれないわね。\x02\x03",

            "#00104F正式な取引で売買されたのだから、\x01",
            "多分すぐに返還されるとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#00200Fそうですね、車自体に違法性がないか\x01",
            "調べる意味でもそうした方がいいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "そうかあ……\x01",
            "まあ、警察に連絡してみるかなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 7)
    Jump("loc_2305")

    label("loc_22A6")


    #C0028
    ChrTalk(
        0xFE,
        (
            "詐欺師から新型トラックを\x01",
            "買ってしまったわけだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "まあ、警察に連絡してみるかなあ。\x02",
    )

    CloseMessageWindow()

    label("loc_2305")

    Jump("loc_3050")

    label("loc_230A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2573")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E7")

    #C0030
    ChrTalk(
        0xFE,
        (
            "デリックなら、\x01",
            "ミンネスさんと会う為に\x01",
            "街に残ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "今頃、歓楽街のホテルで\x01",
            "お話してるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……さ～てと、\x01",
            "せっかくの最新型だ。\x01",
            "よくメンテしとかないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2439")

    label("loc_23E7")


    #C0033
    ChrTalk(
        0xFE,
        (
            "デリックなら今頃、\x01",
            "歓楽街のホテルでミンネスさんと\x01",
            "お話してるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2439")

    Jump("loc_256E")

    label("loc_243E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FD")

    #C0034
    ChrTalk(
        0xFE,
        (
            "ミンネスさんは\x01",
            "本当に太っ腹なひとだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "さすが、大手製菓会社の\x01",
            "クインシー社に\x01",
            "勤めてるだけはあるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "デリックとの計画も、\x01",
            "ぜひ応援していきたい\x01",
            "ところだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_256E")

    label("loc_24FD")


    #C0037
    ChrTalk(
        0xFE,
        (
            "ミンネスさんは\x01",
            "本当に太っ腹なひとだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "さすが、大手製菓会社の\x01",
            "クインシー社に\x01",
            "勤めてるだけはあるよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256E")

    Jump("loc_3050")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_293E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_END)), "loc_2745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2650")

    #C0039
    ChrTalk(
        0xFE,
        (
            "えっ……\x01",
            "私有地の鍵が開けられてたって！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "うはあ、そうか……\x01",
            "迷惑なことをするヤツも\x01",
            "いたもんだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "伝えてくれてありがとう。\x01",
            "あとでトラックに乗って\x01",
            "閉めにいくとするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2740")

    label("loc_2650")


    #C0042
    ChrTalk(
        0xFE,
        (
            "私有地の鍵……\x01",
            "あとでトラックに乗って\x01",
            "閉めにいかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "……ふう、実を言うと\x01",
            "最近トラックにガタがきててさ。\x01",
            "運転するのが憂鬱なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "でも、新しい導力トラックを買う\x01",
            "予算なんか村にはないし……\x01",
            "なんとか整備しないとなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2740")

    Jump("loc_2939")

    label("loc_2745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2859")

    #C0045
    ChrTalk(
        0xFE,
        (
            "アルモリカ古道の途中に、\x01",
            "村で管理している私有地があってね。\x01",
            "さっき帰ってきたところなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "あそこは農具や資材なんかを\x01",
            "保管している場所だから、\x01",
            "無闇に入っちゃいけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "まあ、普段は鍵をかけて\x01",
            "入れないようにしてるから\x01",
            "大丈夫だとは思うけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2939")

    label("loc_2859")


    #C0048
    ChrTalk(
        0xFE,
        (
            "アルモリカ古道の途中に、\x01",
            "村で管理している私有地があってね。\x01",
            "さっき帰ってきたところなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "……そういえば、村に外国の\x01",
            "お客さんが来てるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "この黒い運搬車も彼のなのかな？\x01",
            "かなりの高級車みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2939")

    Jump("loc_3050")

    label("loc_293E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E0")

    #C0051
    ChrTalk(
        0x9,
        (
            "特訓を見てたけど、\x01",
            "さっきのはなかなか\x01",
            "凄い技だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "いやあ、さっきの勝負といい\x01",
            "さすがは遊撃士さんって所かな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A5A")

    label("loc_29E0")


    #C0053
    ChrTalk(
        0x9,
        (
            "あ～、さっきの手合わせを見て\x01",
            "まだ興奮が冷めきらないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "ふふ、また遊撃士さんとの\x01",
            "手合わせを見物させてくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5A")

    Jump("loc_2BCE")

    label("loc_2A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6F")

    #C0055
    ChrTalk(
        0x9,
        (
            "僕って、興奮すると\x01",
            "ついつい訛りがでちゃうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "今時の若者らしくないから\x01",
            "できれば直したいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "ミリア姉さんに相談してみたら、\x01",
            "『気にしなくていい』って言うんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ちぇっ、他人事だと思って……\x01",
            "これじゃ田舎者まるだしじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BCE")

    label("loc_2B6F")


    #C0059
    ChrTalk(
        0xFE,
        (
            "ミリア姉さん、僕の訛りを\x01",
            "気にしなくていいっていうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "ちぇっ、他人事だと思って……\x02",
    )

    CloseMessageWindow()

    label("loc_2BCE")

    Jump("loc_3050")

    label("loc_2BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3050")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAB")

    #C0061
    ChrTalk(
        0x9,
        "やあ、アルモリカ村へようこそ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x9,
        (
            "って……\x01",
            "な、なんだァ、あの導力車は！？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "ヴェルヌ社製でも\x01",
            "ラインフォルト社製でもない……\x01",
            "あんなクルマ、初めて見ただよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#10104Fふふ、あの車はＺＣＦ製なんです。\x02\x03",

            "#10102F搭載された新型エンジンのお陰で\x01",
            "最高時速は１５００セルジュにも\x01",
            "なるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "へぇえええ～……\x01",
            "そりゃいいなあ、すげえなあ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00012F（ノエル、すごく誇らしげだなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 5)
    Jump("loc_2F1B")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E91")

    #C0067
    ChrTalk(
        0x9,
        (
            "最高時速１５００セルジュ……\x01",
            "ＺＣＦもニクイもんを\x01",
            "作っちまっただなあ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "いいなあ、いいなあ！\x01",
            "オラも新型トラックが\x01",
            "欲しくなってきただよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "……コホン。\x01",
            "いや、興奮してついつい\x01",
            "訛りがでちゃったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F1B")

    label("loc_2E91")


    #C0070
    ChrTalk(
        0x9,
        (
            "……そういえば、この間の怪しい人たちは\x01",
            "なんだったのかなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "ま、別に何でもいいんだけどね。\x01",
            "僕の導力車ライフに支障がなければ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1B")

    Jump("loc_3050")

    label("loc_2F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC6")

    #C0072
    ChrTalk(
        0x9,
        "やあ、アルモリカ村へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "この村では養蜂業や農業、\x01",
            "牧畜をやってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "眺めもいいし、よかったら\x01",
            "ゆっくりしていったらどうだい？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3050")

    label("loc_2FC6")


    #C0075
    ChrTalk(
        0x9,
        (
            "……そういえば、この間の怪しい人たちは\x01",
            "なんだったのかなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "ま、別に何でもいいんだけどね。\x01",
            "僕の導力車ライフに支障がなければ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3050")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A79 end

    def Function_9_3054(): pass

    label("Function_9_3054")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EC")

    #C0077
    ChrTalk(
        0x8,
        (
            "大人たちが騒いでたけど……\x01",
            "あの木、ほんとすっげーよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "あんなでっかい木で木登りしたら\x01",
            "すっごく楽しそうだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3164")

    label("loc_30EC")


    #C0079
    ChrTalk(
        0x8,
        (
            "あんなでっかい木で木登りしたら\x01",
            "すっごく楽しそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "でっかいカブトムシとかも\x01",
            "とまってたりするんだろうな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3164")

    Jump("loc_3B4C")

    label("loc_3169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_32E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324D")

    #C0081
    ChrTalk(
        0x8,
        (
            "よーし、そんじゃあ今日は\x01",
            "缶けりでもやろっか！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    #C0082
    ChrTalk(
        0x10,
        (
            "#03805Fかんけり～？\x01",
            "それってなあに～？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "え、缶けり知らないの！？\x01",
            "しょーがねーなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "えっとさ、基本は\x01",
            "かくれんぼなんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0x10, 0xFF)
    Jump("loc_32DC")

    label("loc_324D")


    #C0085
    ChrTalk(
        0x8,
        (
            "そんでな、オニがいない間に\x01",
            "この缶を……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    #C0086
    ChrTalk(
        0x10,
        (
            "#03809F知ってるよ～、つぶして\x01",
            "ゴミにだすんでしょ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        "だ、だからちがうってば～。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_32DC")

    Jump("loc_3B4C")

    label("loc_32E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A9")

    #C0088
    ChrTalk(
        0x8,
        (
            "こないだ、ハロルドおじさんが\x01",
            "コドモを連れてやってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "うーん、弟がいたら\x01",
            "あんな感じなんだろうなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "年上としては、しっかりと\x01",
            "メンドー見てやんないとな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3411")

    label("loc_33A9")


    #C0091
    ChrTalk(
        0x8,
        (
            "ハロルドおじさんも、\x01",
            "村に引っ越せばいいのになー。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "そしたらコリンも\x01",
            "ずっとこっちで遊べるしさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    Jump("loc_3B4C")

    label("loc_3416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3576")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FD")

    #C0093
    ChrTalk(
        0x8,
        (
            "なんか、この間クロスベル市で\x01",
            "コエー奴らが暴れまわったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "この村って退屈だから、\x01",
            "何か事件が起きないかなーって\x01",
            "よく思ってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "さすがに襲撃事件なんてのは\x01",
            "まっぴらごめんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3571")

    label("loc_34FD")


    #C0096
    ChrTalk(
        0x8,
        (
            "この村って平和すぎて退屈だって\x01",
            "ずっと思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "もしかしてそれって、\x01",
            "かなりゼータクだったのかなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3571")

    Jump("loc_3B4C")

    label("loc_3576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3584")
    Jump("loc_3B4C")

    label("loc_3584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3760")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FA")

    #C0098
    ChrTalk(
        0x8,
        "あーあ、今日は退屈だぜ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "ここらで目が覚めるような\x01",
            "大事件でも起こらないかなあ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375B")

    label("loc_35FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D8")

    #C0100
    ChrTalk(
        0x8,
        (
            "なーなー、さっきのすごかったよな！\x01",
            "でっかい猫がばーって出てきてさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "もしかして、あのおじさんって\x01",
            "どっかのサーカスで\x01",
            "猛獣使いでもやってんのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "うわー、サインでも\x01",
            "もらっときゃよかったぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_375B")

    label("loc_36D8")


    #C0103
    ChrTalk(
        0x8,
        (
            "もしかして、あのおじさんって\x01",
            "どっかのサーカスで\x01",
            "猛獣使いでもやってんのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "うわー、サインでも\x01",
            "もらっときゃよかったぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_375B")

    Jump("loc_3B4C")

    label("loc_3760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_38E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383D")

    #C0105
    ChrTalk(
        0x8,
        (
            "こないだ、村によく来てる\x01",
            "外国人のおじさんが\x01",
            "俺たちにお菓子をくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "シツレーなことしちゃったから\x01",
            "怒られるかと思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "いやー、世の中には\x01",
            "親切な人がいるもんだよなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38E4")

    label("loc_383D")


    #C0108
    ChrTalk(
        0x8,
        (
            "外国人のおじさんに\x01",
            "シツレーなことしちゃったんだけど、\x01",
            "怒られるどころかお菓子をくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "……そのあと、あらためて母さんに\x01",
            "こっぴどく叱られちゃったけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E4")

    Jump("loc_3B4C")

    label("loc_38E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_398B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3904")
    Call(0, 10)
    Jump("loc_3986")

    label("loc_3904")


    #C0110
    ChrTalk(
        0x8,
        (
            "うーん、同じタカオニでも\x01",
            "微妙にルールが違うみたいだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "そんじゃ、今日はステファンの\x01",
            "クロスベル式タカオニにしようぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3986")

    Jump("loc_3B4C")

    label("loc_398B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A6")
    Call(0, 10)
    Jump("loc_39F9")

    label("loc_39A6")


    #C0112
    ChrTalk(
        0x8,
        (
            "そうか、街にはそんな\x01",
            "でっけえ建物があんのか～。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "一回探検してみたいな～。\x02",
    )

    CloseMessageWindow()

    label("loc_39F9")

    Jump("loc_3B4C")

    label("loc_39FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD3")

    #C0114
    ChrTalk(
        0x8,
        (
            "ちぇっ、この村って\x01",
            "平和すぎて退屈なんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "最近のニュースって言えば、\x01",
            "『牧場の牛がコドモを産んだ』とか\x01",
            "そんなのばっかりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "あーあ、何か大事件でも\x01",
            "起きないかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B4C")

    label("loc_3AD3")


    #C0117
    ChrTalk(
        0x8,
        (
            "まー、確かに牛のコドモは\x01",
            "可愛かったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "俺が求めてる大事件って、\x01",
            "そんな平和なことじゃ\x01",
            "ないんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B4C")

    TalkEnd(0xFE)
    Return()

    # Function_9_3054 end

    def Function_10_3B50(): pass

    label("Function_10_3B50")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C95")

    #C0119
    ChrTalk(
        0x8,
        (
            "よーし、そんじゃあ\x01",
            "タカオニでもすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "オニは絶対に高いところに\x01",
            "上っちゃだめだかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        "プーリー、オニさんがいい！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "え？　３秒以内なら\x01",
            "高いところにいても\x01",
            "大丈夫なんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "……なにそれ。\x01",
            "初めて聞いたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "ねえねえーってばー！\x01",
            "プーリー、オニさんがいいー！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jump("loc_3DD6")

    label("loc_3C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3DD6")

    #C0125
    ChrTalk(
        0xB,
        (
            "そういえば今日は、\x01",
            "街でオルキスタワーの除幕式を\x01",
            "やってたんじゃなかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "オルキスタワー？\x01",
            "なにそれ、食えんの？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        "おやつー？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "い、いやいや、違うから。\x01",
            "すっごく大きな建物だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "噂じゃ、てっぺんから\x01",
            "クロスベル中を\x01",
            "見渡せるそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "へー、すげえ！\x01",
            "一回行ってみたいな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)

    label("loc_3DD6")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_3B50 end

    def Function_11_3DE6(): pass

    label("Function_11_3DE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E6E")

    #C0131
    ChrTalk(
        0xA,
        (
            "コリンくん、\x01",
            "ハロルドおじちゃんと一緒に\x01",
            "街に帰っちゃったんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "また遊びに来てねって\x01",
            "ヤクソクしたんだよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4479")

    label("loc_3E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F81")

    #C0133
    ChrTalk(
        0xA,
        (
            "おにいちゃんが\x01",
            "コリンくんばっかりかまって\x01",
            "つまんなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "おかあさんが、プーリーのほうが\x01",
            "おねえちゃんなんだから\x01",
            "ちょっとガマンしなさいって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0135
    ChrTalk(
        0xA,
        (
            "プーリー、がまんするよー。\x01",
            "……だって、おねえちゃんだし♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_401E")

    label("loc_3F81")


    #C0136
    ChrTalk(
        0xA,
        (
            "プーリーはコリンくんよりも\x01",
            "ちょっとだけおねえちゃんなんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "おにいちゃんがとられても\x01",
            "ちょっとならがまんするよー。\x01",
            "……だって、おねえちゃんだし♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401E")

    Jump("loc_4479")

    label("loc_4023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_40B3")

    #C0138
    ChrTalk(
        0xA,
        (
            "おにいちゃん、\x01",
            "最近はコリンくんばっかり\x01",
            "かまってるんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "おにいちゃんは\x01",
            "プーリーのおにいちゃんなのに……\x01",
            "ずるいよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4479")

    label("loc_40B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4127")

    #C0140
    ChrTalk(
        0xA,
        (
            "ステファンくん、さっき村に\x01",
            "もどってきたみた～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "はやくあそびにこないかな～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41AA")

    label("loc_4127")


    #C0142
    ChrTalk(
        0xA,
        (
            "さいきんはずっと、\x01",
            "おにいちゃんとふたりで\x01",
            "あそんでたんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "でも、やっぱりステファンくんも\x01",
            "いたほうがたのしいよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41AA")

    Jump("loc_4479")

    label("loc_41AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_41BD")
    Jump("loc_4479")

    label("loc_41BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_42A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41FF")

    #C0144
    ChrTalk(
        0xA,
        (
            "プーリー、\x01",
            "遊撃士ごっこしたーい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A1")

    label("loc_41FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4268")

    #C0145
    ChrTalk(
        0xA,
        (
            "にゃーにゃー。\x01",
            "おっきなネコちゃんだったね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        "あんましかわいくなかったけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42A1")

    label("loc_4268")


    #C0147
    ChrTalk(
        0xA,
        (
            "プーリーはやっぱり、\x01",
            "ちっちゃいネコちゃんがすき～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A1")

    Jump("loc_4479")

    label("loc_42A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4336")

    #C0148
    ChrTalk(
        0xA,
        (
            "おにいちゃん、こないだ\x01",
            "おかあさんに\x01",
            "おしりぺんぺんされてたの～。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "ぷぷぷ。\x01",
            "おしりがリンゴみたいに\x01",
            "まっかになってたよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4479")

    label("loc_4336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4351")
    Call(0, 10)
    Jump("loc_437C")

    label("loc_4351")


    #C0150
    ChrTalk(
        0xA,
        (
            "プーリー、\x01",
            "オニさんがいーいーのー！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437C")

    Jump("loc_4479")

    label("loc_4381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439C")
    Call(0, 10)
    Jump("loc_43E2")

    label("loc_439C")


    #C0151
    ChrTalk(
        0xA,
        (
            "おにいちゃんに\x01",
            "かたぐるましてもらうのと、\x01",
            "どっちがたかいかなー？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E2")

    Jump("loc_4479")

    label("loc_43E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4479")

    #C0152
    ChrTalk(
        0xA,
        (
            "プーリーは、\x01",
            "おにいちゃんがいるから\x01",
            "ぜんぜんつまんなくないよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "さいきんはステファンくんも\x01",
            "あそんでくれるからたのしいんだ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4479")

    TalkEnd(0xFE)
    Return()

    # Function_11_3DE6 end

    def Function_12_447D(): pass

    label("Function_12_447D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_45FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4561")

    #C0154
    ChrTalk(
        0xB,
        (
            "うーん、何気にものすごい\x01",
            "大事件だと思うんだけど……\x01",
            "こんなにノンキでいいのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "まあ、これがこの２人の\x01",
            "いい所でもあるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "何かあった時のために、\x01",
            "僕だけは注意してあげないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45F8")

    label("loc_4561")


    #C0157
    ChrTalk(
        0xB,
        (
            "いつでもノンキなのがこの２人の\x01",
            "いい所でもあるんだけど……\x01",
            "流石にものすごい大事件だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "何かあった時のために、\x01",
            "僕だけは注意してあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F8")

    Jump("loc_4C79")

    label("loc_45FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_471C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BC")

    #C0159
    ChrTalk(
        0xB,
        (
            "コリン君って、ちょっと\x01",
            "危なっかしい所があるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xB,
        (
            "さっきも、あの蒼い花が綺麗だって\x01",
            "街道の方に出て行こうとしてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        "ちゃんと僕達がよく見てないとね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4717")

    label("loc_46BC")


    #C0162
    ChrTalk(
        0xB,
        (
            "コリン君って、ちょっと\x01",
            "危なっかしい所があるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        "ちゃんと僕達がよく見てないとね。\x02",
    )

    CloseMessageWindow()

    label("loc_4717")

    Jump("loc_4C79")

    label("loc_471C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_47CB")

    #C0164
    ChrTalk(
        0xB,
        (
            "ハロルドさんたちは、しばらく\x01",
            "《トネリコ亭》に滞在してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "僕とお母さんが越してきた時も\x01",
            "色々と世話になったし、\x01",
            "この村の人たちは本当に心が広いよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_47CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47D9")
    Jump("loc_4C79")

    label("loc_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_47E7")
    Jump("loc_4C79")

    label("loc_47E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_491D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4841")

    #C0166
    ChrTalk(
        0xB,
        (
            "もう、遊撃士ごっこなんて\x01",
            "いい加減飽きてるんだけどなあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4918")

    label("loc_4841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CA")

    #C0167
    ChrTalk(
        0xB,
        (
            "あのおじさん、やっぱり\x01",
            "悪い奴だったんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "まさか村の中に\x01",
            "魔獣を放つなんて……\x01",
            "食べられちゃうかと思ったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4918")

    label("loc_48CA")


    #C0169
    ChrTalk(
        0xB,
        (
            "それにしても、魔獣に\x01",
            "襲われそうになったのに、\x01",
            "この兄妹はノンキだなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4918")

    Jump("loc_4C79")

    label("loc_491D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49A6")

    #C0170
    ChrTalk(
        0xB,
        (
            "あのおじさん、\x01",
            "僕はなんだかニガテだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "確かにニコニコしてて\x01",
            "優しそうなんだけど、\x01",
            "目が笑ってないっていうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_49A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C1")
    Call(0, 10)
    Jump("loc_4A48")

    label("loc_49C1")


    #C0172
    ChrTalk(
        0xB,
        (
            "クロスベル市だと、\x01",
            "オニは３秒まで高いところに\x01",
            "いていいことになってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "こういうの、たしか\x01",
            "ローカルルールって言うんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A48")

    Jump("loc_4C79")

    label("loc_4A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A68")
    Call(0, 10)
    Jump("loc_4B02")

    label("loc_4A68")


    #C0174
    ChrTalk(
        0xB,
        (
            "うーん、そっか。\x01",
            "今までは大きな幕が下がってたし\x01",
            "知らなくてもヘンじゃないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "あの幕がとれたんなら、\x01",
            "街のほうはすっごく\x01",
            "盛り上がっただろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B02")

    Jump("loc_4C79")

    label("loc_4B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFA")

    #C0176
    ChrTalk(
        0xB,
        (
            "前は、お母さんと一緒に\x01",
            "クロスベル市に\x01",
            "住んでたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "アルモリカ村で\x01",
            "過ごすようになってから、\x01",
            "なんだか毎日が新鮮だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "なんで最初はあんなに\x01",
            "嫌がってたのか、\x01",
            "自分でもよくわかんないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0x6B, 0x0)
    Jump("loc_4C79")

    label("loc_4BFA")


    #C0179
    ChrTalk(
        0xB,
        (
            "牛の出産なんてのが\x01",
            "身近で起こるっていうのは\x01",
            "充分すごいと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "村に住んでたら\x01",
            "当たり前になっちゃうのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C79")

    TalkEnd(0xFE)
    Return()

    # Function_12_447D end

    def Function_13_4C7D(): pass

    label("Function_13_4C7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C8E")
    Jump("loc_53FD")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6B")

    #C0181
    ChrTalk(
        0xC,
        (
            "独立国の無効宣言……\x01",
            "もともと縁遠いこの村には\x01",
            "ほとんど影響はないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "だが、事態の急激な変化に\x01",
            "不安を感じている村人も少なくない。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "やはり、村の家を一軒一軒\x01",
            "回っておかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4DD9")

    label("loc_4D6B")


    #C0184
    ChrTalk(
        0xC,
        (
            "事態の急激な変化に\x01",
            "不安を感じている村人も少なくない。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "やはり、村の家を一軒一軒\x01",
            "回っておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD9")

    Jump("loc_53FD")

    label("loc_4DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC1")

    #C0186
    ChrTalk(
        0xC,
        (
            "あの不気味な蒼い花……\x01",
            "少し前から、レンゲ畑で\x01",
            "咲くようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "花の成長に影響がありそうだし\x01",
            "何とか除草したいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "くそっ、何度抜いても生えてくる。\x01",
            "今のところはお手上げだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4F5A")

    label("loc_4EC1")


    #C0189
    ChrTalk(
        0xC,
        (
            "このレンゲ畑は、\x01",
            "村にとって最も大事な場所だから、\x01",
            "あの蒼い花をなんとかしたいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        (
            "くそっ、何度抜いても生えてくる。\x01",
            "今のところはお手上げだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5A")

    Jump("loc_53FD")

    label("loc_4F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_504F")

    #C0191
    ChrTalk(
        0xC,
        (
            "街の襲撃事件以来、\x01",
            "村の周辺の見回りを\x01",
            "交代でするようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        (
            "あんな事があった以上、\x01",
            "どこで何が起こっても\x01",
            "不思議じゃないからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xC,
        (
            "とにかく、村の安全を守る為に\x01",
            "できる限りのことはしなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_50BD")

    label("loc_504F")


    #C0194
    ChrTalk(
        0xC,
        (
            "村の周辺の見回りを\x01",
            "交代でするようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "村の安全を守る為に\x01",
            "できる限りのことはしなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50BD")

    Jump("loc_53FD")

    label("loc_50C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_50D0")
    Jump("loc_53FD")

    label("loc_50D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50DE")
    Jump("loc_53FD")

    label("loc_50DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50EC")
    Jump("loc_53FD")

    label("loc_50EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50FA")
    Jump("loc_53FD")

    label("loc_50FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51EF")

    #C0196
    ChrTalk(
        0xC,
        (
            "アルモリカ村の存続のため、\x01",
            "昨日も色々な改革案を\x01",
            "村長に提言したんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xC,
        (
            "全部却下されて\x01",
            "結局、最後はいつもどおりの\x01",
            "口論になってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xC,
        (
            "親父は……村長は、\x01",
            "アルモリカ村の現状に\x01",
            "危機を感じていないのか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_527D")

    label("loc_51EF")


    #C0199
    ChrTalk(
        0xC,
        (
            "昨日も色々な改革案を\x01",
            "提言したんだが……\x01",
            "村長は一つも認めなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        (
            "親父は……村長は、\x01",
            "アルモリカ村の現状に\x01",
            "危機を感じていないのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_527D")

    Jump("loc_53FD")

    label("loc_5282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536A")

    #C0201
    ChrTalk(
        0xC,
        (
            "最近は、農業も牧畜もあまり\x01",
            "好調とは言えなくてな。\x01",
            "村の財政は厳しい状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xC,
        (
            "だが親父……村長は、\x01",
            "いまだに保守的な考えを\x01",
            "改めようとしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "……やはり次期村長として、\x01",
            "俺が何とかしなくてはな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_53FD")

    label("loc_536A")


    #C0204
    ChrTalk(
        0xC,
        (
            "アルモリカ村の存続のためには、\x01",
            "伝統などに縛られて現状を\x01",
            "維持していくだけじゃダメだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        (
            "……やはり次期村長として、\x01",
            "俺が何とかしなくてはな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FD")

    TalkEnd(0xFE)
    Return()

    # Function_13_4C7D end

    def Function_14_5401(): pass

    label("Function_14_5401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B4")

    #N0206
    NpcTalk(
        0xD,
        "身なりのいい男性",
        (
            "ここがアルモリカ村……\x01",
            "聞いたとおり、\x01",
            "なかなかいい村ですな。\x02",
        )
    )

    CloseMessageWindow()

    #N0207
    NpcTalk(
        0xD,
        "身なりのいい男性",
        (
            "ふふ、早速仕事に\x01",
            "取り掛かるとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_551D")

    label("loc_54B4")


    #N0208
    NpcTalk(
        0xD,
        "身なりのいい男性",
        (
            "早速仕事に\x01",
            "取り掛かるとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #N0209
    NpcTalk(
        0xD,
        "身なりのいい男性",
        "さて、村長殿の家はと……\x02",
    )

    CloseMessageWindow()

    label("loc_551D")

    TalkEnd(0xFE)
    Return()

    # Function_14_5401 end

    def Function_15_5521(): pass

    label("Function_15_5521")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5532")
    Jump("loc_55F5")

    label("loc_5532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_55EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_554D")
    Call(0, 16)
    Jump("loc_55E7")

    label("loc_554D")


    #C0210
    ChrTalk(
        0xE,
        (
            "ふふ、ソフィアさんったら\x01",
            "コリンくんのことになると\x01",
            "本当に心配性になるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xE,
        (
            "でも大丈夫、子供は\x01",
            "ちょっとずつ怪我しながら\x01",
            "成長していくものだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E7")

    Jump("loc_55F5")

    label("loc_55EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_55F5")

    label("loc_55F5")

    TalkEnd(0xFE)
    Return()

    # Function_15_5521 end

    def Function_16_55F9(): pass

    label("Function_16_55F9")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0212
    ChrTalk(
        0xF,
        "#03708Fコリン、大丈夫かしら……（そわそわ）\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xE,
        (
            "ふふ、ソフィアさん。\x01",
            "そこまで心配しなくて大丈夫よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        (
            "うちのステファンも、\x01",
            "最初はもやしっこだったから\x01",
            "心配だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xE,
        (
            "子供は丈夫に出来てるから、\x01",
            "ちょっとくらいやんちゃな遊びを\x01",
            "させたほうがいいと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)

    #C0216
    ChrTalk(
        0xF,
        (
            "#03700Fそ、そうですね。\x01",
            "私があまり過保護だと、\x01",
            "コリンも楽しめないでしょうし……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0x118, 0x0)
    Return()

    # Function_16_55F9 end

    def Function_17_5786(): pass

    label("Function_17_5786")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5797")
    Jump("loc_584A")

    label("loc_5797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B2")
    Call(0, 16)
    Jump("loc_582E")

    label("loc_57B2")


    #C0217
    ChrTalk(
        0xF,
        (
            "#03700F……私もあまり過保護なのは\x01",
            "よくないのかもしれませんね。\x02\x03",

            "#03709Fだってコリン、あんなにも\x01",
            "楽しそうなんですもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582E")

    Jump("loc_584A")

    label("loc_5833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5841")
    Jump("loc_584A")

    label("loc_5841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_584A")

    label("loc_584A")

    TalkEnd(0xFE)
    Return()

    # Function_17_5786 end

    def Function_18_584E(): pass

    label("Function_18_584E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_585F")
    Jump("loc_58FC")

    label("loc_585F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_58E5")

    #C0218
    ChrTalk(
        0x10,
        (
            "#03800Fたくさんのおともだちと\x01",
            "あそぶのって楽しいね～！\x02\x03",

            "#03809Fこんど、サニータちゃんも\x01",
            "連れてきてあげようかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58FC")

    label("loc_58E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_58F3")
    Jump("loc_58FC")

    label("loc_58F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_58FC")

    label("loc_58FC")

    TalkEnd(0xFE)
    Return()

    # Function_18_584E end

    def Function_19_5900(): pass

    label("Function_19_5900")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD9")

    #C0219
    ChrTalk(
        0xFE,
        (
            "このレンゲ畑の《プレロマ草》を\x01",
            "何とかする方法を探している所でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "抜いてもすぐに生えてくるらしいし……\x01",
            "なんとか根絶できるといいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00003Fそうですね……\x01",
            "《幻獣》出現の原因になりますし、\x01",
            "最優先で対処した方がよさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "ま、とりあえず色々と試してみるよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0223
    ChrTalk(
        0xFE,
        (
            "そうだ、君達に是非、\x01",
            "聞いて欲しいことがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "……実は今度、婚約者のパールと\x01",
            "結婚式を挙げることにしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "こんな状況だから、パールには\x01",
            "まだ内緒にしてるんだが……\x01",
            "色々と段取りを始めたところなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#00102Fまあ……\x01",
            "ふふ、おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "はは、こんな時だからこそ\x01",
            "守るべきものを持とうと\x01",
            "改めて思えてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "式の日取りが決まったら\x01",
            "君たちも招待するから、\x01",
            "是非来てくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 1)
    Jump("loc_5C85")

    label("loc_5BD9")


    #C0229
    ChrTalk(
        0xFE,
        (
            "パールには随分と待たせて\x01",
            "しまったけど……近いうちに\x01",
            "結婚式を挙げることにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "彼女を守っていくためにも、\x01",
            "クロスベルの遊撃士として\x01",
            "一層精進していかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C85")

    TalkEnd(0xFE)
    Return()

    # Function_19_5900 end

    def Function_20_5C89(): pass

    label("Function_20_5C89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D54")

    #C0231
    ChrTalk(
        0x26,
        (
            "僕たちはしばらく\x01",
            "ここで観光してから\x01",
            "リベールに帰るとするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x26,
        (
            "君たちにはお礼をいくら言っても\x01",
            "言い足りないくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x26,
        (
            "父さんと再会させてくれたこと、\x01",
            "改めてありがとうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5DC8")

    label("loc_5D54")


    #C0234
    ChrTalk(
        0x26,
        (
            "君たちにはお礼をいくら言っても\x01",
            "言い足りないくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x26,
        (
            "父さんと再会させてくれたこと、\x01",
            "改めてありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC8")

    TalkEnd(0xFE)
    Return()

    # Function_20_5C89 end

    def Function_21_5DCC(): pass

    label("Function_21_5DCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E63")

    #C0236
    ChrTalk(
        0xFE,
        (
            "うふふ、アルミンも\x01",
            "お義父さまに会えて\x01",
            "本当に嬉しそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "お～よちよち、\x01",
            "よかったわねアルミン㈱\x02",
        )
    )

    CloseMessageWindow()

    #N0238
    NpcTalk(
        0xFE,
        "赤ん坊",
        "きゃっきゃっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5EC5")

    label("loc_5E63")


    #C0239
    ChrTalk(
        0xFE,
        (
            "お～よちよち、あとでお義父さまに\x01",
            "もう一度挨拶に行きましょうね～㈱\x02",
        )
    )

    CloseMessageWindow()

    #N0240
    NpcTalk(
        0xFE,
        "赤ん坊",
        "きゃっきゃっ。\x02",
    )

    CloseMessageWindow()

    label("loc_5EC5")

    TalkEnd(0xFE)
    Return()

    # Function_21_5DCC end

    def Function_22_5EC9(): pass

    label("Function_22_5EC9")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EFB")
    SetScenarioFlags(0x31, 2)

    label("loc_5EFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_5F3B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F30")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_5F36")

    label("loc_5F30")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_5F36")

    Jump("loc_5F41")

    label("loc_5F3B")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_5F41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_5FBA")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F9A"),
        (SWITCH_DEFAULT, "loc_5FAB"),
    )


    label("loc_5F9A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FB5")

    label("loc_5FAB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FB5")

    Jump("loc_61F9")

    label("loc_5FBA")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5FEE")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_5FEE")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6022"),
        (1, "loc_6126"),
        (2, "loc_61B7"),
        (SWITCH_DEFAULT, "loc_61EF"),
    )


    label("loc_6022")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6053")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_6063")

    label("loc_6053")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_6063")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60B9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60B9")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60DC")
    Sound(461, 0, 100, 0)

    label("loc_60DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_60FC")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_610C")

    label("loc_60FC")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_610C")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_5F41")

    label("loc_6126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6198")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_615B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6173")

    label("loc_615B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_616E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6173")

    label("loc_616E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6173")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B2")

    label("loc_6198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_61A8")
    OP_AF(0xFB)
    Jump("loc_61B2")

    label("loc_61A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B2")

    Jump("loc_61F9")

    label("loc_61B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61EA")

    label("loc_61D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_61E0")
    OP_AF(0xFB)
    Jump("loc_61EA")

    label("loc_61E0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61EA")

    Jump("loc_61F9")

    label("loc_61EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61F9")

    Jump("loc_5F41")

    label("loc_61FE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_5EC9 end

    def Function_23_620C(): pass

    label("Function_23_620C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6254")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力バスは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_6254")

    Call(0, 3)
    Return()

    # Function_23_620C end

    def Function_24_6258(): pass

    label("Function_24_6258")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0242
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(11620, 1500, 1410, 1500)
    MoveCamera(328, 26, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16250, 1500)
    Sleep(1000)
    SetChrName("")

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6327")
    OP_E2(0x2)
    MiniGame(0x6, 0x1B, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_6327")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_6258 end

    def Function_25_632C(): pass

    label("Function_25_632C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    Call(0, 26)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x2B)
    LoadChrToIndex("chr/ch00153.itc", 0x2C)
    LoadChrToIndex("chr/ch00353.itc", 0x2D)
    LoadChrToIndex("chr/ch02953.itc", 0x2E)
    LoadChrToIndex("chr/ch03053.itc", 0x2F)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    LoadChrToIndex("chr/ch32053.itc", 0x30)
    LoadChrToIndex("chr/ch32153.itc", 0x31)
    LoadChrToIndex("chr/ch32154.itc", 0x32)
    LoadEffect(0x0, "event/ev12020.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg130_00.eff")
    Call(0, 27)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x2B)
    LoadChrToIndex("chr/ch00153.itc", 0x2C)
    LoadChrToIndex("chr/ch00353.itc", 0x2D)
    LoadChrToIndex("chr/ch02953.itc", 0x2E)
    LoadChrToIndex("chr/ch03053.itc", 0x2F)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    LoadChrToIndex("chr/ch32053.itc", 0x30)
    LoadChrToIndex("chr/ch32153.itc", 0x31)
    LoadChrToIndex("chr/ch32154.itc", 0x32)
    LoadChrToIndex("chr/ch00052.itc", 0x33)
    LoadChrToIndex("chr/ch00057.itc", 0x34)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg130_00.eff")
    LoadEffect(0x4, "battle\\cr000500.eff")
    LoadEffect(0x5, "battle\\cr000501.eff")
    LoadEffect(0x6, "battle\\cr000102.eff")
    Call(0, 29)
    Return()

    # Function_25_632C end

    def Function_26_656E(): pass

    label("Function_26_656E")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7840, 2500, -21280, 0)
    MoveCamera(358, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16070, 0)
    SetChrPos(0x101, 7290, 0, -20490, 46)
    SetChrPos(0x102, 8520, 0, -22110, 46)
    SetChrPos(0x104, 8230, 0, -23660, 46)
    SetChrPos(0x109, 6700, 0, -22920, 46)
    SetChrPos(0x105, 6010, 0, -21490, 46)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(7840, 1200, -21280, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    #C0244
    ChrTalk(
        0x101,
        (
            "#6P#00005Fそれにしても……\x01",
            "結構ギャラリーがいるんですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67BC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67BC)
    Sleep(50)

    def lambda_67CC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_67CC)

    def lambda_67D9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67D9)
    Sleep(50)

    def lambda_67E9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_67E9)

    def lambda_67F6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67F6)
    Sleep(50)

    def lambda_6806():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6806)
    Sleep(300)

    #C0245
    ChrTalk(
        0x18,
        (
            "#12Pああ、どうやら\x01",
            "話が広まってしまったようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4450, 1500, -14100, 3000)
    MoveCamera(7, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16620, 3000)
    OP_6F(0x79)

    #C0246
    ChrTalk(
        0x8,
        "#5Pへへっ、遊撃士は無敵だぜ。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "#5P警察なんか、\x01",
            "ちょちょいのちょい、ってな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0248
    ChrTalk(
        0xA,
        (
            "#11Pちょちょ？\x01",
            "ちょちょい、ってなにー？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0249
    ChrTalk(
        0xB,
        (
            "#5Pえっと、つまり\x01",
            "相手にならないってことだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x96, 0x1F4)

    #C0250
    ChrTalk(
        0xB,
        (
            "#5Pでもどうかな、\x01",
            "特務支援課のお兄さんたちも\x01",
            "かなりやると思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x96, 0x1F4)

    #C0251
    ChrTalk(
        0x9,
        "#5Pおおっ、バリバリ燃えて来ただァ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1D, 500)

    #C0252
    ChrTalk(
        0x9,
        (
            "#11Pなぁ、村長は\x01",
            "どっちに分があると思うだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x1D,
        (
            "#5Pふむ、そうじゃな……\x01",
            "どちらにも普段から\x01",
            "お世話になっておるからの。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x9, 0x96, 0x1F4)
    Fade(500)
    OP_68(7840, 1200, -21280, 0)
    MoveCamera(358, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16070, 0)
    OP_0D()

    #C0254
    ChrTalk(
        0x102,
        "#12P#00106Fそ、村長さんまで……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0255
    ChrTalk(
        0x19,
        (
            "#12Pっていうか、\x01",
            "手合わせの話は村長さんにしか\x01",
            "してないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        "#6P#10302Fフフ、さすがは田舎と言うべきか。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        "#6P#00306Fああ、情報の回りが恐ろしく早えな。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x109,
        (
            "#6P#10112Fあはは……\x01",
            "また違った意味で緊張しそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x18,
        (
            "#12Pふふ、まぁたまには\x01",
            "こんなのもいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0xEE, 0x1F4)
    Sleep(300)

    #C0260
    ChrTalk(
        0x18,
        (
            "#11Pさて、さっそく\x01",
            "手合わせと行きたい所だけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C01():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C01)
    Sleep(50)

    def lambda_6C11():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C11)

    def lambda_6C1E():
        OP_93(0xFE, 0xEE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6C1E)
    Sleep(50)

    def lambda_6C2E():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C2E)
    Sleep(50)

    def lambda_6C3E():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C3E)
    Sleep(50)

    def lambda_6C4E():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C4E)
    Sleep(300)

    #C0261
    ChrTalk(
        0x18,
        "#11Pまずは形式を決めないとね。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x19,
        (
            "#11Pう～ん、パターンは\x01",
            "色々あるとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x19,
        (
            "#11Pここはやっぱり２人１組#8Rツーマンセル#――\x01",
            "２対２の戦闘でしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x18,
        (
            "#5Pああ、私もそれで\x01",
            "行きたいと思っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x18,
        "#11Pそちらは大丈夫かい？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#6P#00004Fええ、お２人の依頼ですし、\x01",
            "問題はありませんが……\x02\x03",

            "#00000F誰が出るかは\x01",
            "こちらで決めていいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x18,
        "#11Pああ、任せるよ。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x18,
        (
            "#11Pただしロイド、\x01",
            "アンタだけは確定で頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#6P#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x18,
        (
            "#11Pはは、そんなに\x01",
            "驚くことじゃないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x18,
        (
            "#11P私たちは別に\x01",
            "個人の身体能力だけを\x01",
            "見たいわけじゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x18,
        (
            "#11Pロイドを中心とした\x01",
            "特務支援課の結束力……\x01",
            "それを見せてもらいたいのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x19,
        (
            "そうそう、なのに\x01",
            "肝心のリーダーがいないんじゃ\x01",
            "意味がないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#6P#00005Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        (
            "#6P#00301Fくそっ、ロイドのやつ……！\x02\x03",

            "こんなに素敵なお姉さん方から\x01",
            "こうも求められるとは……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、なるほどね。\x01",
            "これが噂の弟貴族というヤツか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0277
    ChrTalk(
        0x101,
        (
            "#6P#00006F何だか、不当なコメントが\x01",
            "聞こえた気がするけど……\x01",
            "まあいいや。\x02\x03",

            "#00000Fとりあえず、\x01",
            "そういうことなら了解です。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#6P#00100Fそれじゃあ、\x01",
            "ロイドは誰をパートナーに\x01",
            "選ぶのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        "#6P#00003Fああ、そうだな……\x02",
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
            "エリィと一緒に戦う\x01",        # 0
            "ランディと一緒に戦う\x01",      # 1
            "ノエルと一緒に戦う\x01",        # 2
            "ワジと一緒に戦う\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_726B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0280
    ChrTalk(
        0x101,
        "#5P#00000Fエリィ、お願いしていいかな？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0281
    ChrTalk(
        0x102,
        (
            "#12P#00104Fふふ、もちろんよ。\x02\x03",

            "#00102F私たちのコンビネーション……\x01",
            "お２人に見てもらいましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C9")

    label("loc_726B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732D")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x2)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0282
    ChrTalk(
        0x101,
        "#5P#00000Fランディ、頼まれてくれるか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x104,
        (
            "#12P#00309Fおうよ、もちろんだ！\x02\x03",

            "#00300F俺たちの連携技……\x01",
            "お姉さん方にぶつけてやろうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C9")

    label("loc_732D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F7")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0284
    ChrTalk(
        0x101,
        "#11P#00000Fノエル、君に頼んでいいかな？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0285
    ChrTalk(
        0x109,
        (
            "#6P#10109Fええ、もちろんです！\x02\x03",

            "#10100F私たちのコンビクラフト……\x01",
            "お２人にぶつけていきましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C9")

    label("loc_73F7")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x4)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0286
    ChrTalk(
        0x101,
        "#11P#00000Fワジ、一緒に戦ってくれるか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0287
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、君の頼みなら喜んで。\x02\x03",

            "#10302F僕たちの連携#4Rデュエット#で、お姉さんたちを\x01",
            "アッと言わせて見せようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74C9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFA, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7502")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_755A")

    label("loc_7502")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7526")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_755A")

    label("loc_7526")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754A")
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_755A")

    label("loc_754A")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_755A")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(8610, 1700, -21420, 0)
    MoveCamera(4, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12790, 0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75FB")
    SetChrPos(0x104, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_76EF")

    label("loc_75FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7653")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_76EF")

    label("loc_7653")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76AB")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_76EF")

    label("loc_76AB")

    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x109, 13100, 0, -12850, 225)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_76EF")

    FadeToBright(1000, 0)
    OP_0D()

    #C0288
    ChrTalk(
        0x19,
        "#11P決まりね！\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x18,
        "#11P２人とも、武器を構えな。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10960, 1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776D")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_77B3")

    label("loc_776D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7789")
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_77B3")

    label("loc_7789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77AB")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_77B3")

    label("loc_77AB")

    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_77B3")

    OP_0D()
    Fade(500)
    Sound(812, 0, 100, 0)
    Sound(859, 0, 50, 0)
    SetChrChipByIndex(0x18, 0x29)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x1)
    OP_0D()

    #C0290
    ChrTalk(
        0x18,
        "#4S#11Pそれじゃ、行くよ！\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7820")
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7875")

    label("loc_7820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7843")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7875")

    label("loc_7843")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7866")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7875")

    label("loc_7866")

    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)

    label("loc_7875")

    Battle("BattleInfo_774", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x109, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    Return()

    # Function_26_656E end

    def Function_27_78A4(): pass

    label("Function_27_78A4")

    EventBegin(0x0)
    SoundLoad(832)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F14")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA9")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x3)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_7BB5")

    label("loc_7AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B09")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_7BB5")

    label("loc_7B09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B69")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_7BB5")

    label("loc_7B69")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x3)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_7BB5")

    FadeToBright(1000, 0)
    OP_0D()

    #C0291
    ChrTalk(
        0x101,
        "#6P#00006Fはあはあ……ダメか！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C34")

    #C0292
    ChrTalk(
        0x102,
        (
            "#6P#00106Fそんな……向こうは\x01",
            "本気じゃなかったのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF8")

    label("loc_7C34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C83")

    #C0293
    ChrTalk(
        0x104,
        (
            "#6P#00306Fくッ、向こうは\x01",
            "全力でもねえっつうのに……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF8")

    label("loc_7C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CCE")

    #C0294
    ChrTalk(
        0x109,
        (
            "#6P#10106Fくッ……完全に\x01",
            "出方を誤りましたね……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF8")

    label("loc_7CCE")


    #C0295
    ChrTalk(
        0x105,
        "#6P#10306Fやれやれ……油断したね……\x02",
    )

    CloseMessageWindow()

    label("loc_7CF8")


    #C0296
    ChrTalk(
        0x18,
        (
            "#11Pふう、まさかこの程度とは……\x01",
            "ちょっと拍子抜けだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x19,
        (
            "#11Pう～ん、もう少し\x01",
            "やると思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x18,
        (
            "#11Pま、コンビでの戦闘経験が\x01",
            "まだまだ浅いって所かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x18,
        (
            "#11Pまあいい、次はチーム\x01",
            "全体で向かってきてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E93")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Jump("loc_7F0F")

    label("loc_7E93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC3")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Jump("loc_7F0F")

    label("loc_7EC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF3")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Jump("loc_7F0F")

    label("loc_7EF3")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    label("loc_7F0F")

    Jump("loc_8541")

    label("loc_7F14")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F8D")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_8099")

    label("loc_7F8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FED")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_8099")

    label("loc_7FED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804D")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_8099")

    label("loc_804D")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_8099")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0300
    ChrTalk(
        0x101,
        "#6P#00000Fふう……やったか？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_813A")

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#00102Fええ……といっても\x01",
            "向こうは手加減してくれていた\x01",
            "みたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8247")

    label("loc_813A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8197")

    #C0302
    ChrTalk(
        0x104,
        (
            "#6P#00304Fま、向こうは\x01",
            "全力じゃねえみたいだし、\x01",
            "こんなもんだろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8247")

    label("loc_8197")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81FE")

    #C0303
    ChrTalk(
        0x109,
        (
            "#6P#10104Fはい……といっても\x01",
            "お２人は手加減してくれていた\x01",
            "みたいですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8247")

    label("loc_81FE")


    #C0304
    ChrTalk(
        0x105,
        (
            "#6P#10304Fああ、とはいえ\x01",
            "２人は本気じゃなかった\x01",
            "みたいだけどね。\x02",
        )
    )

    OP_57(0x0)
    OP_5A()
    CloseMessageWindow()

    label("loc_8247")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    #C0305
    ChrTalk(
        0x18,
        (
            "#11Pふふ、驚いた。\x01",
            "結構やるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x19,
        (
            "#11Pうんうん、思っていた以上に\x01",
            "息が合っててビックリしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#6P#00012Fあはは……余裕そうですね。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x18,
        (
            "#11Pふふ、手を抜いたのは事実だが\x01",
            "そんなに余裕ではないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x18,
        (
            "#11Pま、とにかく\x01",
            "いいものを見せてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        (
            "#6P#00105Fえっと……ではこれで\x01",
            "訓練終了でいいんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x18,
        (
            "#11Pふふ、まあそう\x01",
            "焦らないでおくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x19,
        (
            "#11Pそうそう、こんなのじゃ\x01",
            "ロイド君たちも消化不良でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#6P#00005Fそ、そんなことはありませんが……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x18,
        "#11Pはは、何を遠慮してるんだい。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x18,
        (
            "#11Pそうだね、次は私たち\x01",
            "２人と特務支援課、\x01",
            "この対決でお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_8541")


    def lambda_8546():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8546)
    Sleep(50)

    def lambda_8556():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8556)
    Sleep(50)

    def lambda_8566():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8566)
    Sleep(50)

    def lambda_8576():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8576)
    Sleep(300)

    #C0316
    ChrTalk(
        0x101,
        "#6P#00005Fお、俺たち５人とですか？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        (
            "#6P#00306Fさすがに全員を相手にすんのは\x01",
            "キツくないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x18,
        (
            "#11Pふふ、だからこそ\x01",
            "訓練になるんじゃないか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    #C0319
    ChrTalk(
        0x18,
        "#11P#4S――破#2Rは#！\x02",
    )

    CloseMessageWindow()
    Sound(620, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 9600, 0, -18150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    #C0320
    ChrTalk(
        0x102,
        "#6P#00105F凄い……力が迸#2Rほとばし#ってる！\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#6P#00303F東方武術の“気功”ってヤツか。\x02\x03",

            "#00301F……こいつは厄介そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x18,
        "#11Pへえ、さすがに詳しいじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x18,
        "#11P――エオリア！\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x19,
        "#11P了解！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8770():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8770)
    Sleep(50)

    def lambda_8780():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8780)
    Sleep(50)

    def lambda_8790():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8790)
    Sleep(50)

    def lambda_87A0():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_87A0)
    Sleep(50)
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    #C0325
    ChrTalk(
        0x109,
        "#6P#10105Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x105,
        (
            "#6P#10304Fふふ、これで全員が\x01",
            "完全回復ってわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x18,
        "#11Pこれで心置きなく戦えるだろう？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x18,
        (
            "#11Pさあ、アンタたち！\x01",
            "ぐずぐずしてないで構えな！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10960, 1000)
    Fade(500)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x1)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_0D()

    #C0329
    ChrTalk(
        0x104,
        "#6P#00300Fハッ、やるしかなさそうだな。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#6P#00100Fロイド……\x01",
            "誰をサポートに回すの？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#6P#00003Fああ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "エリィをサポートに回す\x01",        # 0
            "ランディをサポートに回す\x01",      # 1
            "ノエルをサポートに回す\x01",        # 2
            "ワジをサポートに回す\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A05")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_8A5D")

    label("loc_8A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A29")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_8A5D")

    label("loc_8A29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A4D")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_8A5D")

    label("loc_8A4D")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_8A5D")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF8")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_8BEC")

    label("loc_8AF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B50")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_8BEC")

    label("loc_8B50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BA8")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_8BEC")

    label("loc_8BA8")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_8BEC")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C50")

    #C0332
    ChrTalk(
        0x101,
        "#6P#00000Fエリィ、サポートを頼む！\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x102,
        "#6P#00100Fええ、了解よ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5E")

    label("loc_8C50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB8")

    #C0334
    ChrTalk(
        0x101,
        "#6P#00000Fランディ、サポートに回ってくれ！\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        "#6P#00300Fがってん承知の介だ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5E")

    label("loc_8CB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D18")

    #C0336
    ChrTalk(
        0x101,
        "#6P#00000Fノエル、サポートは君に任せた！\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        "#6P#10100Fイエス・サー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5E")

    label("loc_8D18")


    #C0338
    ChrTalk(
        0x101,
        "#6P#00000Fワジ、サポートは任せたぞ！\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x105,
        "#6P#10300Fフフ、了解！\x02",
    )

    CloseMessageWindow()

    label("loc_8D5E")


    #C0340
    ChrTalk(
        0x18,
        "#4S#11P――行くよ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_7B8", 0x30200011, 0x0, 0x100, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    Return()

    # Function_27_78A4 end

    def Function_28_8D98(): pass

    label("Function_28_8D98")

    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    Sound(357, 0, 80, 0)
    PlayEffect(0x1, 0x1, 0x19, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x19, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x19, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x1, 0x2)
    Sound(280, 0, 30, 0)
    PlayEffect(0x2, 0x2, 0x19, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x19, 0x3)
    Sleep(500)
    Sound(226, 0, 80, 0)
    PlayEffect(0x3, 0xFF, 0x101, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x102, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x104, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x109, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x19, 0x4)
    Sleep(2000)
    StopEffect(0x3, 0x2)
    Return()

    # Function_28_8D98 end

    def Function_29_8F64(): pass

    label("Function_29_8F64")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96C4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_917E")
    SetChrPos(0x102, 8370, 0, -22800, 16)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_92D2")

    label("loc_917E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F6")
    SetChrPos(0x104, 8370, 0, -22800, 16)
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_92D2")

    label("loc_91F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_926E")
    SetChrPos(0x109, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_92D2")

    label("loc_926E")

    SetChrPos(0x105, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)

    label("loc_92D2")

    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0341
    ChrTalk(
        0x101,
        "#6P#00006Fハア、ハア、ハア……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#6P#00301Fなんてこった……まさか\x01",
            "全員で行って敵わねえとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x109,
        "#6P#10108Fあたしたちの完敗……ですね。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x18,
        (
            "#11Pふう……さすがに\x01",
            "今度ばかりはこっちも\x01",
            "ダメかと思ったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x19,
        (
            "#11Pええ、何とか\x01",
            "勝ちを拾わせてもらったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x19,
        "#11Pこれも一重に経験の差、かな？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    #C0347
    ChrTalk(
        0x101,
        "#6P#00002Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    #C0348
    ChrTalk(
        0x102,
        (
            "#6P#00105Fさっきまでのダメージが\x01",
            "すっかりなくなってる……\x02\x03",

            "#00102F本当に凄い回復技術だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        (
            "#6P#00301Fしかし、やられた上に\x01",
            "回復までしてもらうたあ……\x02\x03",

            "#00306Fはあ、男として情けねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x19,
        (
            "#11Pごめんなさい。\x01",
            "余計なお世話だったかしらね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0351
    ChrTalk(
        0x104,
        (
            "#6P#00309Fいやあ、トンデモないッス！\x02\x03",

            "#00300Fエオリアさんの\x01",
            "暖かいアーツにかかれるなんて\x01",
            "こんな幸せ、他にないッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x109,
        "#6P#10106Fラ、ランディ先輩……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x105,
        (
            "#6P#10300Fハハ、さっきまでの\x01",
            "プライドはどこへやら、だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        (
            "#6P#00106Fはあ、まったく……\x01",
            "緊張感に欠けるというか\x01",
            "何というか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE3")

    label("loc_96C4")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9755")
    SetChrPos(0x102, 8370, 0, -22800, 16)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_98A9")

    label("loc_9755")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97CD")
    SetChrPos(0x104, 8370, 0, -22800, 16)
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_98A9")

    label("loc_97CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9845")
    SetChrPos(0x109, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_98A9")

    label("loc_9845")

    SetChrPos(0x105, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)

    label("loc_98A9")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0355
    ChrTalk(
        0x101,
        (
            "#6P#00006Fハア、ハア……\x01",
            "お、終わったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        (
            "#6P#00304Fああ、何とかな。\x02\x03",

            "#00302Fしかし、この５人を相手に\x01",
            "ここまでやるたあ、\x01",
            "全くトンでもねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#6P#00104Fええ、本当に……\x01",
            "最後まで気を抜けなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    #C0358
    ChrTalk(
        0x18,
        (
            "#11Pふう……\x01",
            "さすがにダメだったか。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    #C0359
    ChrTalk(
        0x19,
        (
            "#11Pうまくやれば、もう少し\x01",
            "いけると思ったんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x19,
        (
            "#11Pま、何を言っても\x01",
            "後からじゃ、しょうがないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x19,
        (
            "#11P貴方たちは本当に強かったわ。\x01",
            "今回は私たちの完敗よ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    #C0362
    ChrTalk(
        0x101,
        "#6P#00005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#6P#00102F凄い……\x02\x03",

            "さっきまでのダメージが\x01",
            "すっかりなくなったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#6P#00309Fエオリアさんの回復アーツに\x01",
            "１日に２度もかかれるなんて……\x01",
            "まさに天にも昇る心地ッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x19,
        "#11Pありがとう、ランディ君。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(859, 0, 50, 0)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x1)
    OP_0D()

    #C0366
    ChrTalk(
        0x19,
        (
            "#11Pじゃあ、３度目にかかれるように\x01",
            "もう一度、攻撃を受けてみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x104,
        "#6P#00306Fうげっ、そいつだけは勘弁ッス。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、今度は本当の意味で\x01",
            "天に昇っちゃうかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x109,
        "#6P#10106Fワ、ワジ君……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0370
    ChrTalk(
        0x102,
        (
            "#6P#00106Fはあ、まったく……\x01",
            "緊張感に欠けるというか\x01",
            "何というか。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    label("loc_9CE3")


    #C0371
    ChrTalk(
        0x18,
        (
            "#11Pはは、アンタたち最高だね。\x01",
            "見ていて飽きないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        "#11P#00012Fそ、それはどうも。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(5620, 1500, -16800, 3000)
    MoveCamera(9, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18740, 3000)
    TurnDirection(0x18, 0x1D, 500)
    Sleep(300)
    OP_6F(0x79)

    #C0373
    ChrTalk(
        0x18,
        (
            "#12Pはいはい、手合わせは\x01",
            "これにて終了だよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1D, 500)
    Sleep(300)

    #C0374
    ChrTalk(
        0x19,
        (
            "#12Pそうそう、これ以上待っても\x01",
            "面白いものは見れないからね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E0F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E0F)
    Sleep(50)

    def lambda_9E1F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E1F)
    Sleep(50)

    def lambda_9E2F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E2F)
    Sleep(50)

    def lambda_9E3F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E3F)
    Sleep(50)

    def lambda_9E4F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E4F)
    Sleep(300)

    #C0375
    ChrTalk(
        0x1D,
        (
            "#5Pふむ、そういうことなら\x01",
            "我々はここで解散じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x1D,
        (
            "#5Pみんな仕事もあるじゃろう。\x01",
            "ほれ、休憩は終わりじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)
    Sleep(300)

    #C0377
    ChrTalk(
        0x1B,
        "#11Pはは、了解です。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x8, 500)
    Sleep(300)

    #C0378
    ChrTalk(
        0x1A,
        "#11Pほら、みんな行くよ。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x9,
        "#11Pいんや～、いい戦いだっただァ！\x02",
    )

    CloseMessageWindow()
    OP_68(7360, 1500, -16890, 5000)
    MoveCamera(20, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16070, 5000)

    def lambda_9F75():
        OP_95(0xFE, 8600, 0, -6460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9F75)
    Sleep(50)

    def lambda_9F92():
        OP_95(0xFE, -2960, 0, -6890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9F92)
    Sleep(50)

    def lambda_9FAF():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9FAF)
    Sleep(1000)

    def lambda_9FCC():
        OP_95(0xFE, 1980, 0, -8140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9FCC)
    Sleep(50)

    def lambda_9FE9():
        OP_95(0xFE, -470, 0, -11050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9FE9)
    Sleep(50)

    def lambda_A006():
        OP_95(0xFE, 280, 0, -10190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A006)
    Sleep(50)

    def lambda_A023():
        OP_95(0xFE, 1220, 0, -9620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A023)
    Sleep(1200)

    def lambda_A040():
        OP_95(0xFE, 3110, 0, -9910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A040)
    WaitChrThread(0x9, 1)

    def lambda_A05E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A05E)
    WaitChrThread(0x8, 1)

    def lambda_A06F():
        OP_95(0xFE, -5810, 0, -6140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A06F)
    WaitChrThread(0xA, 1)

    def lambda_A08D():
        OP_95(0xFE, -5250, 0, -4930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A08D)
    WaitChrThread(0xB, 1)

    def lambda_A0AB():
        OP_95(0xFE, -4680, 0, -3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A0AB)
    WaitChrThread(0x1A, 1)

    def lambda_A0C9():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A0C9)
    WaitChrThread(0x1B, 1)

    def lambda_A0E7():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A0E7)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6F(0x1)

    #C0380
    ChrTalk(
        0x18,
        (
            "#12Pああ、それと村長さん。\x01",
            "場所を使わせてもらって\x01",
            "ありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x18,
        "#12Pおかげで、いい訓練になったよ。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x1D,
        (
            "#5Pいやいや、\x01",
            "それを言うならこちらこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x1D,
        (
            "#5Pあんたたちには世話になっとるし、\x01",
            "またいつでも何でも言ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x1D,
        "#5Pそれじゃあの。\x02",
    )

    CloseMessageWindow()

    def lambda_A225():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A225)
    Sleep(2000)
    Fade(500)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_0D()
    OP_6F(0x79)

    #C0385
    ChrTalk(
        0x101,
        (
            "#6P#00009Fはは、まさか\x01",
            "あんなに喜んでくれるとは\x01",
            "思わなかったな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18, 500)
    Sleep(300)

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#00005Fでも、リンさん……\x01",
            "肝心の手合わせの内容は\x01",
            "どうでしたか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A31A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A31A)
    Sleep(50)

    def lambda_A32A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A32A)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A383")

    def lambda_A346():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A346)
    Sleep(50)

    def lambda_A356():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A356)
    Sleep(50)

    def lambda_A366():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A366)
    Sleep(50)

    def lambda_A376():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A376)
    Jump("loc_A462")

    label("loc_A383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3D4")

    def lambda_A397():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A397)
    Sleep(50)

    def lambda_A3A7():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3A7)
    Sleep(50)

    def lambda_A3B7():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A3B7)
    Sleep(50)

    def lambda_A3C7():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A3C7)
    Jump("loc_A462")

    label("loc_A3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A425")

    def lambda_A3E8():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A3E8)
    Sleep(50)

    def lambda_A3F8():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3F8)
    Sleep(50)

    def lambda_A408():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A408)
    Sleep(50)

    def lambda_A418():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A418)
    Jump("loc_A462")

    label("loc_A425")


    def lambda_A42A():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A42A)
    Sleep(50)

    def lambda_A43A():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A43A)
    Sleep(50)

    def lambda_A44A():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A44A)
    Sleep(50)

    def lambda_A45A():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A45A)

    label("loc_A462")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5C9")
    OP_2C(0x75, 0x2)
    OP_29(0x75, 0x1, 0x5)

    #C0387
    ChrTalk(
        0x18,
        (
            "#11Pああ、みんな\x01",
            "思っていた以上に手強くて\x01",
            "身をもって驚かされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x18,
        "#11P訓練の成果も上々って所かな。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x19,
        (
            "#11Pふふ、でも私たちも\x01",
            "負けっぱなしは趣味じゃないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x19,
        (
            "#11Pまたいつか\x01",
            "リベンジさせてもらうわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#6P#00000Fええ、機会があれば\x01",
            "是非お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        "#6P#00309F俺ならいつでもオッケーっす㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_A764")

    label("loc_A5C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6B3")
    OP_29(0x75, 0x1, 0x6)

    #C0393
    ChrTalk(
        0x18,
        (
            "#11Pそうだね、もう少し粘ってくれたら\x01",
            "更にいい訓練になったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x19,
        (
            "#11Pそうね、ちょっと\x01",
            "物足りなかったかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        "#6P#00006Fめ、面目ないです。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x18,
        "#11Pまあ、それでも成果はあったけどね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A764")

    label("loc_A6B3")

    OP_2C(0x75, 0x1)
    OP_29(0x75, 0x1, 0x7)

    #C0397
    ChrTalk(
        0x18,
        (
            "#11Pああ、みんなよくやってくれたし\x01",
            "訓練としては十分だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x19,
        (
            "#11Pうんうん、機会があったら\x01",
            "またお願いしたいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#6P#00000Fええ、その時は是非お願いします。\x02",
    )

    CloseMessageWindow()

    label("loc_A764")

    OP_29(0x75, 0x1, 0x8)

    #C0400
    ChrTalk(
        0x18,
        (
            "#11Pあとはやっぱり、\x01",
            "それぞれの戦闘スタイルを間近で\x01",
            "見られたことが収穫だったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x18,
        (
            "#11P特にロイド。\x01",
            "私にはあんたのトンファー術が\x01",
            "なかなか興味深かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x18,
        (
            "#11P確か警察で教えている\x01",
            "制圧術の一種なんだったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#6P#00000Fええ、よくご存知ですね。\x02\x03",

            "#00005Fでも興味深いというのは……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x18, 500)

    #C0404
    ChrTalk(
        0x104,
        (
            "#6P#00304Fそういや、トンファーといやぁ、\x01",
            "元々東方から伝わったもんッスよね。\x02\x03",

            "#00305Fリンさんも扱えたりするんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x18,
        "#11Pまあ、それなりにね。\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x18,
        (
            "#11P他にも偃月輪#6Rえんげつりん#や三節棍――\x01",
            "東方武具と呼ばれるものは\x01",
            "門下生時代に一通り扱ったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x18,
        (
            "#11Pその観点から言わせてもらうと\x01",
            "ロイド、あんたの回転技は\x01",
            "もしかしたら化けるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0408
    ChrTalk(
        0x101,
        (
            "#6P#00005F化けるって……技が\x01",
            "より強力になるということですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x18,
        "#11Pまあ、あくまで可能性だけどね。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x18,
        (
            "#11Pアンタさえよければ、\x01",
            "この場で指南してもいいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x18,
        "#11P何だったら試してみるかい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0412
    ChrTalk(
        0x101,
        "#6P#00002Fええ、教えてもらえるならぜひ！\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x19,
        "#11Pいいな～、ロイド君。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x19,
        (
            "#11Pリンが人に物を教えるなんて、\x01",
            "滅多にないことなんだからね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x19, 500)

    #C0415
    ChrTalk(
        0x104,
        (
            "#6P#00309F俺はエオリアさんに\x01",
            "色々と指南してもらいたいッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x19,
        "#11Pん～、パス？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x104,
        "#6P#00306Fがくっ。\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x109,
        "#6P#10106Fランディ先輩、懲りないですね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0419
    ChrTalk(
        0x101,
        (
            "#11P#00006Fみんな、ゴメン……\x02\x03",

            "#00000Fそういうことなんだけど、\x01",
            "ちょっと時間をもらっていいかな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACA2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACA2)
    Sleep(50)

    def lambda_ACB2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ACB2)
    Sleep(50)

    def lambda_ACC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACC2)
    Sleep(50)

    def lambda_ACD2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACD2)
    Sleep(300)

    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#00100Fええ、せっかくの機会だし、\x01",
            "教えて頂いたらいいんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、それじゃ僕たちは\x01",
            "その様子を見学させてもらうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x109,
        "#6P#10100F頑張ってくださいね、ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        "#6P#00300Fおう、俺の分まで気合い入れてけよ！\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x101,
        "#11P#00012Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x18,
        (
            "#11Pはは、それじゃさっそく\x01",
            "始めようかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0426
    ChrTalk(
        0x101,
        "#6P#00000Fお願いします！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7680, 1400, -21510, 0)
    MoveCamera(7, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12760, 0)
    SetChrPos(0x101, 7680, 0, -20400, 45)
    SetChrPos(0x102, 3320, 0, -22300, 45)
    SetChrPos(0x104, 4550, 0, -24210, 45)
    SetChrPos(0x109, 2930, 0, -19450, 90)
    SetChrPos(0x105, 7610, 0, -25120, 0)
    SetChrPos(0x18, 10880, 0, -16800, 225)
    SetChrPos(0x19, 12130, 0, -18530, 225)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 30)
    WaitChrThread(0x101, 3)
    TurnDirection(0x101, 0x18, 0)
    Sleep(1000)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0427
    ChrTalk(
        0x101,
        (
            "#6P#00000Fい、今のは\x01",
            "いい感じでしたかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x18,
        "#11Pああ、十分合格点さ。\x02",
    )

    CloseMessageWindow()
    OP_68(7310, 1400, -21350, 2000)
    MoveCamera(12, 19, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14340, 2000)

    def lambda_AFDD():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AFDD)
    Sleep(50)

    def lambda_AFF5():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AFF5)
    Sleep(50)

    def lambda_B00D():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B00D)

    def lambda_B022():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B022)
    Sleep(50)

    def lambda_B03A():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B03A)
    Sleep(50)

    def lambda_B052():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B052)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    #C0429
    ChrTalk(
        0x18,
        (
            "#11P後は実戦で使い込めば、\x01",
            "すぐにものに出来るだろう。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    OP_0D()

    #C0430
    ChrTalk(
        0x101,
        (
            "#6P#00000Fふう、よかった……\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        "#6P#00100Fふふ、やったわね。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x109,
        "#6P#10100Fロイドさん、お疲れ様でした。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0xFA, 0x1F4)

    #C0433
    ChrTalk(
        0x101,
        (
            "#11P#00000Fああ、ありがとう。\x02\x03",

            "#00003Fでもすごいな……\x01",
            "型一つで、こんなに\x01",
            "力の伝わり方が変わるものなのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x18,
        (
            "#11Pふふ、今アンタに教えたのは\x01",
            "俗に《螺旋》と呼ばれる型に\x01",
            "分類される立ち回りの一つでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x3A, 0x1F4)

    #C0435
    ChrTalk(
        0x18,
        (
            "#11Pアリオスさんの使う\x01",
            "《八葉一刀流》にも取り入れられている\x01",
            "いわば武術の一つの形なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x18,
        (
            "#11P全ての基本であり応用でもある\x01",
            "この型から派生する技は、\x01",
            "それこそ星の数ほどあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x18,
        (
            "#11P《螺旋》を極め、《無》を操る者は\x01",
            "全ての武術の究極にして到達点、\x01",
            "《理》に至るなんて言われるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        "#6P#00005F螺旋に無、それに《理》ですか……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x18,
        (
            "#11Pま、この辺りは判ろうとして\x01",
            "判るものでもないし、\x01",
            "講釈はこの位にしておくけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x18,
        (
            "#11P詰まる所、《理》ってのは\x01",
            "常人には一生かかっても辿り着けない\x01",
            "達人の境地みたいなものでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x18,
        (
            "#11Pその境地に至った者は\x01",
            "大陸にもせいぜい数人しかいないと\x01",
            "言われているのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        "#6P#00005Fた、大陸に数人……\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x104,
        (
            "#6P#00303F噂にこそ聞いたことはあるが、\x01",
            "ほんと途方もねえ話ッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x18,
        "#11Pはは、確かにね。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x18,
        (
            "#11Pまあ流石に《理》とまでは言わないが、\x01",
            "これからも精進することだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        "#6P#00002Fええ、分かりました！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0447
    ChrTalk(
        0x18,
        (
            "#11Pおっと、そうこうしている間に\x01",
            "次の時間が迫って来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x19,
        (
            "#11Pうん、お互いにちょっと\x01",
            "急がないとヤバイ感じね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B60C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B60C)
    Sleep(50)

    def lambda_B61C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B61C)
    Sleep(300)

    #C0449
    ChrTalk(
        0x102,
        "#6P#00100Fやはり随分お忙しいんですね。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x18,
        (
            "#11Pああ、特に今は通商会議の\x01",
            "おかげで色々とタイトでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x19,
        (
            "#11Pそれだけにミシェルの\x01",
            "シフトが重要なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x19,
        (
            "#11P今はそれが数分単位で\x01",
            "刻まれちゃってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x109,
        "#6P#10105Fそ、それはとんでもないですね。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x18,
        (
            "#11Pふふ、といっても\x01",
            "適度に休んではいるけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x18,
        (
            "#11Pそれじゃ私たちは失礼するが、\x01",
            "みんなも精進を怠らないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x19,
        "#11Pまたね～、ロイド君たち。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#00000Fはい、どうも\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16340, 3000)

    def lambda_B80D():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B80D)
    Sleep(50)

    def lambda_B82A():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B82A)

    def lambda_B844():

        label("loc_B844")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B844")

    QueueWorkItem2(0x101, 1, lambda_B844)
    Sleep(50)

    def lambda_B859():

        label("loc_B859")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B859")

    QueueWorkItem2(0x102, 1, lambda_B859)
    Sleep(50)

    def lambda_B86E():

        label("loc_B86E")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B86E")

    QueueWorkItem2(0x104, 1, lambda_B86E)
    Sleep(50)

    def lambda_B883():

        label("loc_B883")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B883")

    QueueWorkItem2(0x109, 1, lambda_B883)
    Sleep(50)

    def lambda_B898():

        label("loc_B898")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B898")

    QueueWorkItem2(0x105, 1, lambda_B898)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0458
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドは\x01",
            "レイジングスピンを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0459
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドのクラフト『アクセルラッシュ』が\x01",
            "『レイジングスピン』に強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0460
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "攻撃力が上がる他、より広範囲の敵を巻き込み、\x01",
            "さらに一箇所に引き寄せることが可能になります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddCraft(0x0, 0x9B)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0461
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【遊撃士訓練への参加要請】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x9, 8410, 0, -12480, 17)
    SetChrPos(0x8, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    SetChrPos(0xB, -7830, 0, 23860, 107)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    SetChrPos(0x0, 8140, 0, -18700, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    OP_29(0x75, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_29_8F64 end

    def Function_30_BAF6(): pass

    label("Function_30_BAF6")

    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x0)
    Sound(257, 0, 40, 0)
    Sound(252, 0, 80, 0)
    PlayEffect(0x4, 0x4, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x101, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    StopEffect(0x4, 0x2)
    Sleep(300)
    StopEffect(0x6, 0x2)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x33)
    SetChrSubChip(0x101, 0x0)
    SetChrChip(0x0, 0xFE, 0xF, 0x12C)
    Sound(253, 0, 100, 0)
    PlayEffect(0x5, 0x5, 0x101, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    SetScenarioFlags(0x1, 1)

    def lambda_BBD9():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2EE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBD9)
    BeginChrThread(0x101, 0, 0, 31)
    WaitChrThread(0x101, 1)
    StopEffect(0x5, 0x2)
    ClearScenarioFlags(0x1, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_BAF6 end

    def Function_31_BC0A(): pass

    label("Function_31_BC0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_BC26")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_31_BC0A")

    label("loc_BC26")

    Return()

    # Function_31_BC0A end

    def Function_32_BC27(): pass

    label("Function_32_BC27")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3060, 1800, 24920, 0)
    MoveCamera(311, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16950, 0)
    SetChrPos(0x101, -2630, 0, 25660, 180)
    SetChrPos(0x102, -820, 0, 25800, 225)
    SetChrPos(0x103, -360, 0, 23860, 270)
    SetChrPos(0x104, -3500, 0, 24030, 90)
    SetChrPos(0x109, -2890, 0, 22410, 0)
    SetChrPos(0x105, -970, 0, 22610, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-3060, 700, 24920, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0462
    ChrTalk(
        0x101,
        (
            "#00003F一通り聞き込みしてみたけど……\x01",
            "色々と情報が得られたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x102,
        (
            "#00103F名前は『ミンネス』……\x01",
            "どうやらなにかの商売人と\x01",
            "見られているみたいね。\x02\x03",

            "#00101Fそれになんというか、\x01",
            "意外にも好印象な人物だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x105,
        (
            "#10302F礼儀正しく、子供に優しい……\x01",
            "そんな印象だったね。\x02\x03",

            "#10304Fフフ、ここまでくると\x01",
            "逆に怪しくなってくるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x109,
        "#10106Fた、確かに……\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x103,
        (
            "#00200F実際、目的がいまいち\x01",
            "見えてきませんしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#00303F村長の息子と、\x01",
            "何を話しているかも\x01",
            "気になるところだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x101,
        (
            "#00003Fああ……\x01",
            "もう少し聞き込みを\x01",
            "続けた方がよさそうだな。\x02\x03",

            "#00005Fえっと……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    ClearChrFlags(0x9, 0x80)
    Fade(500)
    OP_68(8510, 1500, -12620, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    SetCameraDistance(15000, 3000)
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3000)

    def lambda_BFA3():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFA3)

    def lambda_BFB0():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BFB0)

    def lambda_BFBD():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BFBD)

    def lambda_BFCA():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BFCA)

    def lambda_BFD7():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BFD7)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(-3060, 700, 24920, 0)
    MoveCamera(311, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16950, 0)
    OP_0D()

    #C0469
    ChrTalk(
        0x101,
        (
            "#00005Fあの人……もしかして、\x01",
            "デリックさんと一緒に\x01",
            "街に行っていたっていう人かな。\x02\x03",

            "#00003Fついさっき村に\x01",
            "戻ってきたみたいだし……\x01",
            "話を聞いてみるか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(1, 0, 0x80)
    SetScenarioFlags(0x174, 4)
    OP_29(0x82, 0x1, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2850, 0, 24480, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_BC27 end

    def Function_33_C0F7(): pass

    label("Function_33_C0F7")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7300, 1800, -12910, 0)
    MoveCamera(349, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13740, 0)
    SetChrPos(0x101, 6500, 0, -11950, 135)
    SetChrPos(0x102, 6210, 0, -13080, 90)
    SetChrPos(0x103, 5100, 0, -12190, 90)
    SetChrPos(0x104, 5560, 0, -10540, 135)
    SetChrPos(0x109, 6300, 0, -9770, 135)
    SetChrPos(0x105, 4430, 0, -10630, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0470
    ChrTalk(
        0x9,
        "フンフフ～ン……♪\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#00000Fあの、すみません。\x01",
            "エルキンさんですね？\x02\x03",

            "ちょっとお聞きしたいことが\x01",
            "あるのですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0472
    ChrTalk(
        0x9,
        "お、なんだい？\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x9,
        (
            "もしかして、この\x01",
            "新型導力トラックについて\x01",
            "聞きたいことがあるのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0474
    ChrTalk(
        0x101,
        (
            "#00012Fい、いやいや……\x01",
            "そういうわけじゃ\x01",
            "ないんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x9,
        "ちぇっ、違うのか。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x9,
        (
            "せっかくミンネスさんに\x01",
            "安く譲ってもらった\x01",
            "ヴェルヌの最新型なのに……\x02",
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

    #C0477
    ChrTalk(
        0x102,
        (
            "#00105Fえっ……？\x02\x03",

            "#00101Fミンネスさんっていうのは、\x01",
            "この村に最近来ている\x01",
            "外国人の……？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x109,
        (
            "#10105Fや、安く譲ってもらったって……\x01",
            "いくらくらいなんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x9,
        "んふふ、それがね……\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x9,
        (
            "なんと、たったの５万ミラ程度で\x01",
            "譲ってもらえたんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        "#00011Fご、５万！？\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x109,
        (
            "#10106Fそんな値段で新車が\x01",
            "買えちゃうなんて……\x01",
            "い、いいなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#00306Fおいおい、うらやましがる\x01",
            "トコじゃねえだろうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x109,
        "#10112Fそ、そうでした……つい。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x103,
        (
            "#00203Fコホン……ともかく。\x02\x03",

            "#00200F新車ともなると\x01",
            "５０万ミラ相当はするはずですし、\x01",
            "破格の値段といえますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x105,
        (
            "#10302Fなんせ９割引だからね。\x01",
            "いやはや、相当に\x01",
            "太っ腹な人物みたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x9,
        (
            "俺たちの仕事が\x01",
            "スムーズになるようにって、\x01",
            "安く譲ってくれたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x9,
        (
            "色々とデリックと\x01",
            "計画を進めているらしいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x9,
        (
            "ふふ、ミンネスさんには\x01",
            "頭があがらないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        "#00305F計画……？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x9,
        (
            "お、おっと。\x01",
            "これはデリックに\x01",
            "口止めされてるんだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "まあとにかく……\x01",
            "ミンネスさんっていう人は\x01",
            "信用できる人だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど……\x02\x03",

            "#00005F……あれ、そういえば。\x01",
            "エルキンさんは１人なんですか？\x02\x03",

            "村長からは、デリックさんと一緒に\x01",
            "街に向かったと聞いたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x9,
        (
            "ああ、デリックなら\x01",
            "後でバスで帰るんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x9,
        (
            "なんでも、歓楽街のホテルに\x01",
            "用があるらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x9,
        (
            "どうやら、そのミンネスさんと\x01",
            "会う約束をしてるみたいなんだ。\x02",
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
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0497
    ChrTalk(
        0x102,
        "#00101Fねえロイド、これって……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0498
    ChrTalk(
        0x101,
        (
            "#00003Fああ、もしかしたら\x01",
            "直接話が聞けるかもしれない。\x02\x03",

            "#00001F行ってみる価値はあるだろう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0499
    ChrTalk(
        0x101,
        (
            "#00000Fご協力ありがとうございます。\x01",
            "おかげで色々参考になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x9,
        "いえいえ、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x9,
        (
            "なんだかよく分からないけど\x01",
            "がんばってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 5)
    OP_29(0x82, 0x1, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 6100, 0, -11400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    EventEnd(0x5)
    Return()

    # Function_33_C0F7 end

    def Function_34_CB66(): pass

    label("Function_34_CB66")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1470, 1500, 10410, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch22200.itc", 0x20)
    LoadChrToIndex("monster/ch82050.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    LoadChrToIndex("chr/ch00051.itc", 0x28)
    LoadChrToIndex("chr/ch00151.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00351.itc", 0x2B)
    LoadChrToIndex("chr/ch02951.itc", 0x2C)
    LoadChrToIndex("chr/ch03051.itc", 0x2D)
    LoadChrToIndex("monster/ch82051.itc", 0x2E)
    LoadChrToIndex("monster/ch82052.itc", 0x2F)
    SoundLoad(325)
    SoundLoad(948)
    SoundLoad(809)
    SoundLoad(805)
    SoundLoad(531)
    SoundLoad(494)
    SoundLoad(487)
    SoundLoad(486)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x21)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x101, -1320, 0, 11720, 90)
    SetChrPos(0x102, -2330, 0, 11520, 90)
    SetChrPos(0x103, -1550, 0, 10520, 90)
    SetChrPos(0x104, -2360, 60, 10120, 90)
    SetChrPos(0x109, -1360, 200, 9200, 90)
    SetChrPos(0x105, -2510, 260, 8760, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x105, 0x1000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0xC, 12240, 0, 17850, 180)
    SetChrPos(0xD, 12050, 0, 16440, 0)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    OP_68(12280, 1500, 16050, 5000)
    OP_6F(0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0502
    ChrTalk(
        0x101,
        (
            "#N#1P#00010Fしまった……\x01",
            "もう取引きを終えたのか……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_CEC4():
        OP_95(0xFE, 3850, 0, 19250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CEC4)
    Sleep(100)

    def lambda_CEE1():
        OP_95(0xFE, 4270, 0, 18270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CEE1)
    OP_68(3150, 1500, 17270, 5000)
    MoveCamera(293, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(13200, 5000)
    BeginChrThread(0x101, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 36)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 39)
    Sleep(200)
    BeginChrThread(0x105, 3, 0, 40)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CF8C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CF8C)
    Sleep(100)

    def lambda_CF9C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CF9C)
    Sleep(300)

    #C0503
    ChrTalk(
        0xD,
        "おや、あなた方は……\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xC,
        "特務支援課の……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#00001Fデリックさん、ミンネスさん……\x01",
            "本日はどういった取引きをしたか、\x01",
            "お聞かせ願えますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        "ふう、また親父の差し金か……\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xD,
        (
            "ふふ、いいではありませんか\x01",
            "デリックさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xD,
        (
            "もはや我々の計画は\x01",
            "始動したのですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        "#00105Fそれは……どういう意味ですか？\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xD,
        (
            "──実は先ほど、デリックさんと\x01",
            "最後の取引きを行いましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xD,
        (
            "村の皆様からお借りした土地を使い、\x01",
            "レンゲ畑の拡大に着手することが\x01",
            "決定いたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xD,
        (
            "そして、レンゲ畑そのものの管理は\x01",
            "我が『クインシー社』にて\x01",
            "引き受けることになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#00011Fなっ……！\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x105,
        (
            "#10303F……今の話だと、\x01",
            "村の農場のほとんどを\x01",
            "譲り渡すという話だけど……\x02\x03",

            "#10300Fデリックさんは、\x01",
            "本当にいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        "……どういう意味だ？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xC,
        (
            "あくまで、管理を\x01",
            "お任せするだけだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xD,
        "ええ、もちろんですとも。\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xD,
        (
            "蜂蜜の収穫を我が社で行うことで\x01",
            "より効率的に製菓事業を\x01",
            "運営していけるようになるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xD,
        (
            "その為には一旦、\x01",
            "我が社に権利を移したほうが\x01",
            "色々と効率がいいのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x104,
        (
            "#00310F（チッ……\x01",
            "  口の上手い野郎だぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x103,
        (
            "#00206F（計画はほぼ最終段階に\x01",
            "  来ているようですね。）\x02\x03",

            "#00208F（だとすると、あとは……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    #C0522
    ChrTalk(
        0xD,
        (
            "ふふ、それではデリックさん。\x01",
            "私はこの契約書を\x01",
            "本社に届けて参ります。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0523
    ChrTalk(
        0xD,
        (
            "明日にもいい連絡を差し上げる事が\x01",
            "できると思いますので、\x01",
            "楽しみにお待ちしていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xC,
        "ええ、お待ちしています。\x02",
    )

    CloseMessageWindow()
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0525
    ChrTalk(
        0x109,
        "#10101F（ロ、ロイドさん……！）\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        (
            "#00003F（ああ……\x01",
            "  ここで逃がすわけにはいかない！）\x02\x03",

            "#00001F──ミンネスさん、その前に……\x01",
            "いくつか尋ねたいことがあります。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D641():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D641)
    Sleep(100)

    def lambda_D651():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D651)
    Sleep(300)

    #C0527
    ChrTalk(
        0xD,
        "ほう……？\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xD,
        (
            "尋ねたいこととは\x01",
            "一体なんですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        (
            "#00003Fええ、それは……\x01",
            "あなたにかかっている\x01",
            "ある疑惑についてです。\x02\x03",

            "#00001Fそう……\x01",
            "詐欺を働いているという\x01",
            "疑惑のね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0530
    ChrTalk(
        0xC,
        "なっ……！？\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "い、いい加減にしてくれ！\x01",
            "ミンネスさんに失礼だろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xD,
        (
            "ふふ……まあまあ、\x01",
            "落ち着いてくださいデリックさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xC,
        "ミンネスさん……？\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xD,
        (
            "確か、特務支援課と\x01",
            "言いましたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xD,
        (
            "一体なぜ、私を\x01",
            "詐欺師と疑っているのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xD,
        (
            "もちろん、説明することが\x01",
            "可能なのでしょうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#00003F……もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xD,
        (
            "面白い……\x01",
            "ではお話をさせて頂くと\x01",
            "しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        (
            "だがその前に……\x01",
            "私が帝国人だということを\x01",
            "お忘れなきよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xD,
        (
            "もし私を詐欺師とする\x01",
            "明確な根拠がない場合……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xD,
        (
            "たとえ警察官といえど、\x01",
            "出るところに出させて\x01",
            "頂きますからご了承のほどを。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        "#00001F……いいでしょう。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0543
    ChrTalk(
        0x102,
        "#00101Fロイド……！\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x101,
        (
            "#00003F（……大丈夫だ。）\x02\x03",

            "（捜査で得た情報から、\x01",
            "  ミンネスが詐欺を働いて\x01",
            "  いることは明白……）\x02\x03",

            "#00001F（疑惑を突きつけて\x01",
            "  ミンネスの正体を暴き、\x01",
            "  デリックさんの目を覚ますんだ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xD,
        (
            "ふふ、よろしい……\x01",
            "それほどの覚悟がおありなら、\x01",
            "何なりとお答えしましょう。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0546
    ChrTalk(
        0xD,
        (
            "……では、まずはどんな話を\x01",
            "していただけるのですかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0547
    ChrTalk(
        0x101,
        (
            "#00003F──まずは、あなたの\x01",
            "クロスベルでの行動……\x02\x03",

            "#00001Fその矛盾点について\x01",
            "お聞きしたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xC,
        "矛盾、だって……？\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "……私はクロスベルに来てから、\x01",
            "ずっとデリックさんと\x01",
            "今回の計画を進めてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xD,
        (
            "アルモリカ村に我が『クインシー社』の\x01",
            "子会社を発足する……\x01",
            "『アルモリカ・ハニーカンパニー』計画。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xD,
        (
            "村の質のいい蜂蜜を使った製菓事業、\x01",
            "我が社の培ったノウハウを生かせば\x01",
            "必ずや実を結ぶでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xD,
        (
            "すでに市に正式に認可され、\x01",
            "今まさに始動しようとしている\x01",
            "この事業の……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xD,
        (
            "一体どこに矛盾があると\x01",
            "おっしゃるのですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#00003Fいいえ、あなたが今話した\x01",
            "『計画』の話……\x02\x03",

            "#00001F俺たちの持っている情報とは\x01",
            "明確に矛盾する点があります。\x02\x03",

            "#00003Fそう、その矛盾点とは……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0555
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kミンネスの『計画』について\x01",
            "矛盾する点とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "製菓のノウハウがある\x01",      # 0
            "計画が進行している\x01",        # 1
            "計画に展望がある\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3B")
    OP_2C(0x87, 0x1)

    #C0556
    ChrTalk(
        0x101,
        (
            "#00003F俺たちがＩＢＣで得た情報と\x01",
            "照らし合わせると\x01",
            "一つの矛盾点が見えてきます。\x02\x03",

            "#00001Fあなたの言う『計画』……\x02\x03",

            "実はそれは、まったくもって\x01",
            "進行していないはずなんです。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x6)
    Jump("loc_E2E9")

    label("loc_DF3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E08F")

    #C0557
    ChrTalk(
        0x101,
        (
            "#00003Fあなたの言う『計画』……\x02\x03",

            "#00001F実はそれを進行させる\x01",
            "ノウハウなんて、\x01",
            "あなたにはないはずなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xD,
        (
            "ほう……？\x01",
            "面白い意見ではありますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xD,
        (
            "しかし、それをどうやって\x01",
            "証明するつもりですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x101,
        (
            "#00011F……え、えっとそれは……\x02\x03",

            "#00006F（しまった……\x01",
            "  疑惑を突きつけるにも\x01",
            "  段取りを考えないとな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1D8")

    label("loc_E08F")


    #C0561
    ChrTalk(
        0x101,
        (
            "#00003Fあなたの言う『計画』……\x02\x03",

            "#00001F実はそれが\x01",
            "成功する見込みなんて\x01",
            "ほとんどないはずなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xD,
        (
            "ほう……？\x01",
            "面白い意見ですが、\x01",
            "いささか失礼ですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xD,
        (
            "何を持ってそういうことを\x01",
            "おっしゃるのか、\x01",
            "証明してもらいたいものですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00011F……え、えっとそれは……\x02\x03",

            "#00006F（しまった……\x01",
            "  ちょっと切り口が違ったか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1D8")


    #C0565
    ChrTalk(
        0x102,
        (
            "#00105Fあ……分かったかもしれないわ。\x02\x03",

            "#00100F私たちがＩＢＣで得た情報と\x01",
            "照らし合わせると矛盾点が\x01",
            "見えてくるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0566
    ChrTalk(
        0x101,
        (
            "#00005F……そうか……！\x02\x03",

            "#00001Fミンネスさん……\x01",
            "あなたの『計画』は……\x01",
            "実は進行していないのではないですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x7)

    label("loc_E2E9")

    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0567
    ChrTalk(
        0xD,
        "…………！\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xC,
        (
            "ＩＢＣ……？\x01",
            "ど、どういうことなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#00003F考えてみてください。\x01",
            "『クインシー社』が先ほどの\x01",
            "計画を進めるつもりなら……\x02\x03",

            "#00001F子会社の設立や工場の建造などには、\x01",
            "ＩＢＣの融資が必要になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xD,
        "……ええ、もちろんですとも。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xD,
        (
            "そのために市に会社の発足を届け出、\x01",
            "きちんと法人向けの口座を用意して……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x101,
        (
            "#00001F──用意した“だけ”。\x01",
            "そうではないですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0573
    ChrTalk(
        0xD,
        "………………\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x101,
        (
            "#00003F『ハニーカンパニー』の口座には、\x01",
            "開設に必要な最低限のミラしか\x01",
            "入ってなかったようです。\x02\x03",

            "詳しい金額は分かりませんが、\x01",
            "入金されていたのは数万ミラ程度……\x02\x03",

            "#00001F果たして、そのようなミラで\x01",
            "工場の建造などが\x01",
            "可能なのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xD,
        (
            "……ＩＢＣの口座に\x01",
            "調査の手を入れているとはね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0576
    ChrTalk(
        0xC,
        (
            "ミ、ミンネスさん……\x01",
            "まさか……！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    #C0577
    ChrTalk(
        0xD,
        (
            "ああ、誤解しないでください。\x01",
            "別に彼らの言い分を\x01",
            "認めたわけではありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xD,
        (
            "ただ、あまりにも不躾だと\x01",
            "思ってしまっただけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x109,
        (
            "#10105Fで、でも……\x01",
            "実際、口座にミラは\x01",
            "ほとんど入ってないんですよ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    #C0580
    ChrTalk(
        0xD,
        (
            "なに、会社の役員として\x01",
            "少々慎重に動かざるを得なかった\x01",
            "というだけですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xD,
        (
            "何しろ由緒正しい\x01",
            "『クインシー社』の名で\x01",
            "融資を受けるわけですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xD,
        (
            "無論、本社の許可が下り次第\x01",
            "ＩＢＣには融資の相談に\x01",
            "行こうと思っていましたがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xC,
        "ほっ……で、ですよね……\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        "#00206F（……上手くかわされましたね。）\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#00003F（いや……\x01",
            "  ミンネスも内心かなり\x01",
            "  あせっているはずだ。）\x02\x03",

            "#00001F（ここは畳み掛けるように\x01",
            "  証拠を突きつける……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xD,
        (
            "……その顔は、まだ何か\x01",
            "聞きたいことがおありのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        (
            "#00002Fええ、もちろんです。\x02\x03",

            "#00004Fなにせ、ミンネスさんの疑惑は\x01",
            "それだけではないのですから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0588
    ChrTalk(
        0xC,
        "この期に及んでまだ……！\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xD,
        "いえいえ、いいのですよ。\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xD,
        (
            "その方が\x01",
            "デリックさんにとっても\x01",
            "安心できるでしょうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x101,
        (
            "#00001F……聞きたいのは……\x01",
            "ミンネスさんの\x01",
            "プロフィールについてです。\x02\x03",

            "#00003Fミンネスさん、あなたは\x01",
            "『クインシー社』の役員を\x01",
            "名乗ってらっしゃいますが……\x02\x03",

            "#00013Fそれは確かなことでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0592
    ChrTalk(
        0xC,
        (
            "待て……\x01",
            "どういうことなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xC,
        (
            "ミンネスさんは\x01",
            "『クインシー社』の\x01",
            "人間じゃないというのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x101,
        (
            "#00003Fええ、俺たちは\x01",
            "そう睨んでいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xD,
        (
            "クク……ハハハ！\x01",
            "何をおっしゃるかと思えば……\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xD,
        (
            "何なら、名刺や社員証でも\x01",
            "お見せいたしましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x103,
        (
            "#00203F……そんなものは知識があれば\x01",
            "いくらでも偽造できるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        (
            "#00003F俺たちは、その物証を覆す\x01",
            "証拠を調べてきました。\x02\x03",

            "#00000Fそれは……他でもない、\x01",
            "クインシー社のパンフレットです。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xC,
        "クインシー社のパンフレット……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x104,
        "#00305Fお嬢の部屋にあったやつか……\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        (
            "#00102F確か、捜査手帳に\x01",
            "要点をメモしていたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#00000F本社から取り寄せられたものなので、\x01",
            "書かれている情報の信頼性は\x01",
            "保証されていると言えます。\x02\x03",

            "#00003Fそしてその資料に書かれていたこと……\x01",
            "それが、ミンネスさんの昨日の話と\x01",
            "明らかに矛盾しているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xD,
        "わ、私の話ですと……？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        (
            "#00003F昨日のミンネスさんの話が\x01",
            "“役員”の肩書きと\x01",
            "矛盾している点、それは……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0605
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K昨日のミンネスの話と\x01",
            "資料の事実が矛盾する点とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "子会社の設立計画\x01",      # 0
            "営業部の経歴\x01",          # 1
            "甘い物が苦手\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4B2")
    OP_2C(0x87, 0x1)

    #C0606
    ChrTalk(
        0x101,
        (
            "#00003F──ミンネスさん。\x01",
            "昨日、あなたはこう言いました。\x02\x03",

            "“役員の立場にはいるが\x01",
            "  実は甘い物は苦手だ”……\x02\x03",

            "#00013Fこの言葉に間違いありませんね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xC)
    OP_64(0xD)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_F0F9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F0F9)
    Sleep(50)

    def lambda_F109():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F109)
    Sleep(50)

    def lambda_F119():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F119)
    Sleep(50)

    def lambda_F129():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F129)
    Sleep(50)

    def lambda_F139():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F139)
    Sleep(300)

    #C0607
    ChrTalk(
        0x102,
        (
            "#00105Fロ、ロイド……？\x01",
            "えっと、よく意味が……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xD,
        "……確かに、私は甘い物が苦手です。\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0xD,
        (
            "フフ、しかしそれが一体\x01",
            "どうしたというのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xD,
        (
            "“甘い物が苦手な人間が\x01",
            "  製菓会社の役員なわけがない”\x01",
            "……とでも言うつもりですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#00003Fその通りです。\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xC,
        (
            "な、なんて言いがかりだ……！\x01",
            "あんた、警察として恥ずかしくは──\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        (
            "#00001F──クインシー社のパンフレットには、\x01",
            "こう書かれていました。\x02\x03",

            "#00003F『クインシー社では、\x01",
            "  役員自らが開発中の商品を試食し、\x01",
            "  販売していいかを厳正に審査する』……\x02\x03",

            "#00013Fかいつまんで言えば、そういう内容です。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F372():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F372)
    Sleep(50)

    def lambda_F382():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F382)
    Sleep(50)

    def lambda_F392():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F392)
    Sleep(50)

    def lambda_F3A2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F3A2)
    Sleep(50)

    def lambda_F3B2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F3B2)
    Sleep(300)

    #C0614
    ChrTalk(
        0xD,
        "…………………………！！\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xC,
        "それが一体どういう……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0616
    ChrTalk(
        0xC,
        "#4S……………………あっ！？\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x101,
        (
            "#00003F……クインシー社という会社が\x01",
            "『甘い物が苦手』なミンネスさんを、\x01",
            "役員にするのは不自然だ。\x02\x03",

            "#00013F……違いますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x8)
    Jump("loc_FB4D")

    label("loc_F4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F53F")

    #C0618
    ChrTalk(
        0x101,
        (
            "#00003F──ミンネスさん。\x01",
            "昨日、あなたは言いました。\x02\x03",

            "“アルモリカ村に子会社を建てる”\x01",
            "という、その計画について……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C1")

    label("loc_F53F")


    #C0619
    ChrTalk(
        0x101,
        (
            "#00003F──ミンネスさん。\x01",
            "昨日、あなたは言いました。\x02\x03",

            "“営業方面で活躍したおかげで\x01",
            "  力を認められ、\x01",
            "  今の地位についた”……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5C1")


    #C0620
    ChrTalk(
        0xD,
        (
            "……確かに言いましたが\x01",
            "それが一体なんだというのです？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0621
    ChrTalk(
        0x101,
        (
            "#00011F（し、しまった……\x01",
            "  返す言葉が全く浮かばない！\x01",
            "  考えが間違ってたのか……？）\x02\x03",

            "#00012Fえ、えっとですね。\x01",
            "今のは少し違ってて……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x105,
        (
            "#10304F──なるほどね。\x01",
            "ようやく思い出したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        "#00005Fえ。\x02",
    )

    CloseMessageWindow()

    def lambda_F6EB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6EB)
    Sleep(50)

    def lambda_F6FB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6FB)
    Sleep(50)

    def lambda_F70B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F70B)
    Sleep(50)

    def lambda_F71B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F71B)
    Sleep(50)

    def lambda_F72B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F72B)
    Sleep(300)

    #C0624
    ChrTalk(
        0x105,
        (
            "#10304F“役員の立場にはいるが\x01",
            "  実は甘い物は苦手だ”……\x02\x03",

            "#10302Fミンネスさん、\x01",
            "昨日あなたはそう言ったのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x102,
        (
            "#00105Fワ、ワジ君……？\x01",
            "えっと、よく意味が……\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xD,
        "……確かに、私は甘い物が苦手です。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0xD,
        (
            "フフ、しかしそれが一体\x01",
            "どうしたというのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xD,
        (
            "“甘い物が苦手な人間が\x01",
            "  製菓会社の役員なわけがない”\x01",
            "……とでも言うつもりですかな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F898():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F898)
    Sleep(300)

    #C0629
    ChrTalk(
        0x103,
        "#00203F……その通り、です。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)
    Sleep(300)

    #C0630
    ChrTalk(
        0x105,
        "#10309Fふふ、キミも気づいたみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xC,
        (
            "な、なんて言いがかりだ……！\x01",
            "あんたら、警察として恥ずかしくは──\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x105,
        (
            "#10304F──クインシー社のパンフレットには、\x01",
            "こう書かれていた。\x02\x03",

            "『クインシー社では、\x01",
            "  役員自らが開発中の商品を試食し、\x01",
            "  販売していいかを厳正に審査する』……\x02\x03",

            "#10302Fかいつまんで言えば、そういう内容がね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA1A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FA1A)
    Sleep(50)

    def lambda_FA2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FA2A)
    Sleep(50)

    def lambda_FA3A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FA3A)
    Sleep(50)

    def lambda_FA4A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FA4A)
    Sleep(300)

    #C0633
    ChrTalk(
        0xD,
        "…………………………！！\x02",
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xC,
        "それが一体どういう……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0635
    ChrTalk(
        0xC,
        "#4S……………………あっ！？\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x103,
        (
            "#00203F……クインシー社という会社が\x01",
            "『甘い物が苦手』なミンネスさんを、\x01",
            "役員にするのは不自然といえます。\x02\x03",

            "#00201F……違いますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x9)

    label("loc_FB4D")


    #C0637
    ChrTalk(
        0xD,
        (
            "……そっ、それは……\x01",
            "単なる記憶違いで……\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x101,
        (
            "#00003Fそれは通用しません。\x02\x03",

            "#00001F……あなたはついさっき\x01",
            "“甘い物は苦手”だと\x01",
            "ハッキリ認めたはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xD,
        "ぐうっ……！\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x101,
        (
            "#00003Fだとしたら\x01",
            "あなたはなぜ『クインシー社』の\x01",
            "役員だと偽ったのか？\x02\x03",

            "#00001Fそれは──\x01",
            "あなたが詐欺を行うために、\x01",
            "デリックさんを信用させるため。\x02\x03",

            "#00003F今までの証拠からして、\x01",
            "そうとしか考えられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        (
            "#00103Fアルモリカの蜂蜜を使った\x01",
            "製菓事業……\x02\x03",

            "#00101Fそれを信用させるためには\x01",
            "『クインシー社』という名前は\x01",
            "好都合だったというわけね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0642
    ChrTalk(
        0xC,
        (
            "ミ、ミンネスさん……\x01",
            "一体これは、\x01",
            "どういうことですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xC,
        (
            "あなたはやはり……\x01",
            "俺を騙していたのか！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    #C0644
    ChrTalk(
        0xD,
        (
            "……ク……クク……\x01",
            "デリックさん、あなたこそ\x01",
            "彼らに騙されてはいけない……\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x104,
        "#00305Fあ、あんだと？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    #C0646
    ChrTalk(
        0xD,
        "ふふ……だってそうでしょう？\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xD,
        (
            "私がアルモリカ村に来たのは、\x01",
            "『ハニーカンパニー』の計画を\x01",
            "持ち掛けるため……\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xD,
        (
            "もし、百歩譲ってそれ以外の目的があり、\x01",
            "デリックさんを騙したというなら……\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xD,
        "一体、何が目的だったというのです！？\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xD,
        (
            "それが証明できないあなた方に、\x01",
            "私を詐欺師呼ばわりする資格はないはずだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x103,
        (
            "#00200F目的の証明ですか……\x01",
            "確かにそれがありましたね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0652
    ChrTalk(
        0x101,
        (
            "#00003Fあなたの目的──\x01",
            "一つだけ、心当たりがあります。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_100D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_100D7)
    Sleep(50)

    def lambda_100E7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_100E7)
    Sleep(50)

    def lambda_100F7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_100F7)
    Sleep(50)

    def lambda_10107():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10107)
    Sleep(50)

    def lambda_10117():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10117)
    Sleep(50)

    def lambda_10127():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10127)
    Sleep(300)

    #C0653
    ChrTalk(
        0xD,
        "なっ……なんですと……！？\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        "#00105F（ロイド、大丈夫なの……！？）\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x109,
        (
            "#10106F（ぜ、全然心当たりが\x01",
            "  ありませんけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        (
            "#00003F（いや……確かにあるんだ。）\x02\x03",

            "（ここに来る直前、\x01",
            "  “あの人”が探してくれた\x01",
            "  “あの証言”……）\x02\x03",

            "（#00001Fそう、ミンネスの\x01",
            "  目的を明かす最後の手がかりが……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xD,
        (
            "何をブツブツ言っているのです！\x01",
            "……さあ、説明してみなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        (
            "#00003Fあなたがこの村で\x01",
            "詐欺を行った、真の理由。\x01",
            "それは……\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_102F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1051C")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0659
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kミンネスがアルモリカ村で\x01",
            "詐欺を働こうとした真の目的とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "土地の横取り\x01",        # 0
            "蜂蜜販売の独占\x01",      # 1
            "偽導力車の販売\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1043C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103CC")
    OP_2C(0x87, 0x1)

    label("loc_103CC")


    #C0660
    ChrTalk(
        0x101,
        (
            "#00003Fあなたの真の目的、それは……\x02\x03",

            "#00013Fこのアルモリカ村の所有する\x01",
            "“土地”そのものだったんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10517")

    label("loc_1043C")


    #C0661
    ChrTalk(
        0x101,
        (
            "#00006F（いや……違う。\x01",
            "  そんなスケールの小さい\x01",
            "  話じゃない。）\x02\x03",

            "#00001F（あれだけ手間をかけて\x01",
            "  準備を行っていたんだ……\x01",
            "  もっと大きな狙いがあるに違いない。）\x02\x03",

            "#00003F（ミンネスの本当の目的、\x01",
            "  それは……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10517")

    Jump("loc_102F3")

    label("loc_1051C")


    #C0662
    ChrTalk(
        0xD,
        "……な……あ……！！\x02",
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#00004Fハロルドさんという貿易商の方が、\x01",
            "あなたについて聞き込みをして\x01",
            "くれました。\x02\x03",

            "#00000Fミンネスさん、あなたは……\x01",
            "クロスベル入りした直後から、\x01",
            "各地の地価を調べていたようですね？\x02\x03",

            "#00003F『クインシー社』の役員が\x01",
            "新事業を持ちかけるために\x01",
            "そんな事をする必要はありません。\x02\x03",

            "だったら、何故か……？\x01",
            "考えられる可能性は一つ。\x02\x03",

            "#00013Fあなたがこの土地の横取りを\x01",
            "狙っていたからだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x109,
        (
            "#10105Fほ、本当なんですか……！？\x01",
            "な、なんだか突拍子のない\x01",
            "発想のような。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0665
    ChrTalk(
        0x101,
        (
            "#00004Fいいや、そうでもないさ。\x02\x03",

            "#00002F見てのとおり、アルモリカ村は\x01",
            "豊かな自然に囲まれ、\x01",
            "ロケーションは抜群だ。\x02\x03",

            "#00004Fたとえば、高級別荘地を管理する\x01",
            "第三者に売り渡すとしたら……\x01",
            "どれくらいの値がつくと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x102,
        (
            "#00103Fそれこそ……\x01",
            "数千万ミラかけてでも\x01",
            "落札したい人はいそうね。\x02\x03",

            "#00101F村の人たちが同意するとは\x01",
            "全く思えないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0667
    ChrTalk(
        0x101,
        (
            "#00003Fああ、だからこそ\x01",
            "これだけの手間をかけて\x01",
            "詐欺をはたらいたんだろう。\x02\x03",

            "#00001Fもし土地自体が\x01",
            "目的と仮定すれば……\x01",
            "彼の行動にも説明がつく。\x02\x03",

            "広大なレンゲ畑を含めた\x01",
            "たくさんの農場、そして\x01",
            "私有地の権利書を手に入れ……\x02\x03",

            "本社に帰るとの名目で\x01",
            "クロスベルから\x01",
            "姿を消してしまう。\x02\x03",

            "#00003Fそして、用意していた\x01",
            "販売ルートに土地の権利書を\x01",
            "売りさばき、多額のミラを得る……\x02\x03",

            "#00013Fそれこそが、ミンネスさん……\x01",
            "あなたの真の目的だったんです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A23():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10A23)
    Sleep(50)

    def lambda_10A33():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10A33)
    Sleep(50)

    def lambda_10A43():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10A43)
    Sleep(50)

    def lambda_10A53():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10A53)
    Sleep(50)

    def lambda_10A63():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A63)
    Sleep(300)

    #C0668
    ChrTalk(
        0xD,
        "……う……ぐぐ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0669
    ChrTalk(
        0xC,
        (
            "ミンネス……さん……\x01",
            "そんな……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1F, -1730, 390, 7230, 225)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    #N0670
    NpcTalk(
        0x1F,
        "男性の声",
        "──ロイドさん……！\x02",
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
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10BA0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10BA0)
    Sleep(50)

    def lambda_10BB0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10BB0)
    Sleep(50)

    def lambda_10BC0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10BC0)
    Sleep(50)

    def lambda_10BD0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10BD0)
    Sleep(50)

    def lambda_10BE0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10BE0)
    Sleep(50)

    def lambda_10BF0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10BF0)
    Sleep(50)

    def lambda_10C00():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10C00)
    Sleep(50)

    def lambda_10C10():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10C10)
    Sleep(300)

    #C0671
    ChrTalk(
        0x101,
        "#00000Fこの声は……\x02",
    )

    CloseMessageWindow()
    OP_68(2080, 1500, 14610, 3000)
    MoveCamera(288, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16200, 3000)
    SetChrPos(0x1D, -1100, 450, 5260, 45)
    SetChrPos(0x1F, -2810, 450, 5340, 45)
    SetChrPos(0x1E, -2009, 420, 6880, 45)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    OP_0D()
    BeginChrThread(0x1E, 3, 0, 49)
    BeginChrThread(0x1F, 3, 0, 48)
    Sleep(200)
    BeginChrThread(0x1D, 3, 0, 47)
    WaitChrThread(0x1E, 3)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    #C0672
    ChrTalk(
        0x1F,
        "#03600Fよかった、間に合ったようですね。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x1D,
        "デリック……\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xC,
        "親父に、ハロルドさん……！？\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#00005Fそれにキミは、\x01",
            "たしか法律事務所の……\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x1E,
        (
            "イアン先生の助手の\x01",
            "ピートといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x1E,
        (
            "本来なら先生が来るはずでしたが、\x01",
            "憲法草案の作成の関係で\x01",
            "どうしても出かける必要があったので……\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x103,
        "#00205F証拠……ですか？\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x1F,
        (
            "#03603Fええ、先ほど先生が言っていた\x01",
            "“ダメ押しの証拠”だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x1E,
        "みなさん、これを見てください。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0681
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ピートは一枚の写真を取り出し、\x01",
            "その場の皆に確認できるようにかざした。\x02\x03",

            "写真には、ミンネスと同じ顔をした\x01",
            "商人風の男が写っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0682
    ChrTalk(
        0x101,
        "#00005Fそ、その写真に写っているのは……\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xD,
        "な、なぜだ……\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xD,
        (
            "なぜお前たちが、\x01",
            "そんな写真を持っている！？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x1E,
        (
            "この写真は、イアン先生が\x01",
            "昔、帝国の知り合いの記者から\x01",
            "資料として譲り受けたものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x1E,
        (
            "ですが、写真の男の名前は……\x01",
            "“ミンネス”ではなく、\x01",
            "“リドナー”だったそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x109,
        (
            "#10100Fリドナー……？\x01",
            "その名前、最近どこかで\x01",
            "聞いたような気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x102,
        (
            "#00105F……あっ！\x01",
            "確かそれって……\x02\x03",

            "#00101Fイアン先生が話していた、\x01",
            "帝国の男爵家の土地を奪った\x01",
            "男の名前じゃ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xD,
        "ぐっ……！\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x104,
        "#00305Fおお、確かにそんな名前だったな。\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x1F,
        (
            "#03601Fええ……イアン先生にも\x01",
            "改めてお話を聞いてきましたし、\x01",
            "間違いはないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x105,
        (
            "#10304Fふむ……だとすると、\x01",
            "なかなか面白い事実が\x01",
            "見えてきそうだね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0693
    ChrTalk(
        0x105,
        (
            "#10302Fロイド、彼……ミンネスに\x01",
            "突きつけてやりなよ。\x02\x03",

            "#10304Fこの写真が持つ意味を、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        "#00003F……ああ、分かった。\x02",
    )

    CloseMessageWindow()
    OP_68(2020, 1500, 16370, 3000)

    def lambda_113DC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113DC)
    Sleep(50)

    def lambda_113EC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_113EC)
    Sleep(50)

    def lambda_113FC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_113FC)
    Sleep(50)

    def lambda_1140C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1140C)
    Sleep(50)

    def lambda_1141C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1141C)
    Sleep(50)

    def lambda_1142C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1142C)
    Sleep(50)

    def lambda_1143C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1143C)
    Sleep(50)

    def lambda_1144C():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1144C)
    Sleep(300)
    OP_6F(0x79)

    #C0695
    ChrTalk(
        0x101,
        (
            "#00001Fこの写真に写った人物“リドナー”と\x01",
            "今この場に居る“ミンネス”が\x01",
            "同じ顔をしている理由、それは……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0696
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K写真のリドナーと\x01",
            "ミンネスが同じ顔をしている理由は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "双子\x01",          # 0
            "変装\x01",          # 1
            "同一人物\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115FD")
    OP_2C(0x87, 0x1)

    #C0697
    ChrTalk(
        0x101,
        (
            "#00003Fミンネスとリドナーは同一人物……\x01",
            "そうとしか考えられない。\x02\x03",

            "#00013F詐欺の手口が酷似していたのも、\x01",
            "同一人物だったから、というわけだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11885")

    label("loc_115FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1165B")

    #C0698
    ChrTalk(
        0x101,
        (
            "#00003Fミンネスとリドナーは……双子の兄弟。\x01",
            "そうとしか考えられない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1169F")

    label("loc_1165B")


    #C0699
    ChrTalk(
        0x101,
        (
            "#00003Fミンネスは……リドナーの変装。\x01",
            "そうとしか考えられない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1169F")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xC)
    OP_64(0xD)
    OP_64(0x1D)
    OP_64(0x1F)
    OP_64(0x1E)

    #C0700
    ChrTalk(
        0x105,
        (
            "#10306F……さすがにそれは\x01",
            "深読みしすぎじゃないかな？\x02\x03",

            "#10302Fどう考えても、\x01",
            "ミンネスとリドナーは\x01",
            "同一人物だとしか思えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        (
            "#00006F（む、難しく考えすぎたか……）\x02\x03",

            "#00013Fコホン、だとすると……\x01",
            "詐欺の手口が酷似していたのも、\x01",
            "同一人物だったから、というわけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11885")


    #C0702
    ChrTalk(
        0x1D,
        "イアン先生も言っておった……\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x1D,
        (
            "おそらく、それが\x01",
            "この男が最も得意とする\x01",
            "詐欺の手口なんじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x101,
        (
            "#00003F“詐欺師”──ミンネス。\x01",
            "あなたの詐欺容疑は明白だ。\x02\x03",

            "#00013Fその上、帝国で詐欺を働いた容疑者と\x01",
            "同一人物である可能性も高い。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x104,
        (
            "#00300F叩けばいくらでも\x01",
            "ホコリがでそうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x103,
        (
            "#00203F是非、詳しく話を\x01",
            "聞かせていただきましょう。\x01",
            "……警察本部の取調室で。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0xD,
        "……クッ……\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0xD,
        (
            "お……おのれ……\x01",
            "おのれえええええええっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xD,
        (
            "私が……完璧な仕事を\x01",
            "信条とするこの私が……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0710
    ChrTalk(
        0xD,
        "#4Sこんな……青二才どもにッ！！\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xC,
        "ミ、ミンネスさん……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1194)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0xD)

    #C0712
    ChrTalk(
        0xD,
        (
            "……フン、いい気に\x01",
            "ならないでいただきましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0xD,
        (
            "悪いが、こんなことで\x01",
            "捕まってやるつもりは\x01",
            "毛頭ないのでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x101,
        "#00005Fなに……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x87, 0x1F4)
    Sleep(300)

    #C0715
    ChrTalk(
        0xD,
        "──来い、獣ども！\x02",
    )

    CloseMessageWindow()
    Sound(325, 0, 70, 0)
    WaitBGM()
    PlayBGM("ed7561", 0)
    Sleep(500)
    Fade(500)
    OP_68(10120, 700, -16210, 0)
    MoveCamera(326, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x22, 0x20)
    SetChrFlags(0x23, 0x20)
    SetChrFlags(0x24, 0x20)
    SetChrPos(0x20, 11900, 200, -14590, 180)
    SetChrPos(0x21, 11900, 200, -14590, 180)
    SetChrPos(0x22, 11900, 200, -14590, 180)
    SetChrPos(0x23, 11900, 200, -14590, 180)
    SetChrPos(0x24, 11900, 200, -14590, 180)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    OP_0D()
    OP_71(0xD, 0xF1, 0x10E, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_79(0xD)
    Sound(948, 0, 100, 0)
    Sleep(1000)
    Sleep(500)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x20, 3, 0, 52)
    Sleep(700)
    BeginChrThread(0x28, 1, 0, 63)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x21, 3, 0, 53)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x22, 3, 0, 54)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x23, 3, 0, 55)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x24, 3, 0, 56)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x28, 0x1)
    OP_68(620, 700, 17350, 0)
    MoveCamera(294, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0xC, 4960, 0, 19520, 270)
    SetChrPos(0xD, 5370, 0, 18730, 225)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x21)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x20, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x20, -6100, 0, 14940, 135)
    SetChrPos(0x21, -3890, 0, 18870, 135)
    SetChrPos(0x22, -620, 0, 21820, 180)
    SetChrPos(0x23, 3420, 0, 20140, 225)
    SetChrPos(0x24, 3620, 0, 23850, 180)
    BeginChrThread(0x20, 3, 0, 50)
    BeginChrThread(0x21, 3, 0, 50)
    BeginChrThread(0x22, 3, 0, 50)
    BeginChrThread(0x23, 3, 0, 50)
    BeginChrThread(0x24, 3, 0, 50)
    SetChrPos(0x101, 1560, 10, 17040, 0)
    SetChrPos(0x102, 2380, 0, 16239, 0)
    SetChrPos(0x103, 1370, 10, 15400, 0)
    SetChrPos(0x104, 60, 10, 17000, 315)
    SetChrPos(0x109, -290, 0, 15050, 315)
    SetChrPos(0x105, -1310, 10, 16350, 315)
    FadeToBright(1000, 0)
    OP_0D()
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0716
    ChrTalk(
        0x1E,
        "う、うわあああ！？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)

    #C0717
    ChrTalk(
        0x101,
        "#00010Fま……魔獣！？\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#00105Fしかもかなり\x01",
            "訓練されているみたい……！\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x104,
        "#00310F（こいつら、まさか……！？）\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xC, 0xB4, 0x3E8, 0x3E8, 0x0)
    Sleep(100)

    #C0720
    ChrTalk(
        0xC,
        "……う、あ……\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x1D, 0x0, 0x1F4, 0x1388, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    Sleep(300)

    #C0721
    ChrTalk(
        0x1D,
        "デ、デリック！！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x87, 0x3E8)
    Sleep(300)

    #C0722
    ChrTalk(
        0x1F,
        "#03605Fそ、村長、危ないです……！\x02",
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x109,
        (
            "#10107Fあなたは……\x01",
            "自分がなにをしているか\x01",
            "分かっているのですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xD,
        "ええ、分かっていますとも。\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0xD,
        (
            "ああ、間違っても戦おうなどと\x01",
            "考えないことですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xD,
        (
            "デリックさんや村人たちに\x01",
            "怪我をさせたくなくばね。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x101,
        "#00010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xD,
        "さあ、道を空けたまえ。\x02",
    )

    CloseMessageWindow()
    OP_68(-480, 1500, 13490, 5000)
    MoveCamera(333, 20, 0, 5000)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x0)

    def lambda_12319():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12319)

    def lambda_12326():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12326)

    def lambda_12333():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12333)

    def lambda_12340():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12340)

    def lambda_1234D():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1234D)

    def lambda_1235A():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1235A)

    def lambda_12367():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12367)

    def lambda_12374():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12374)

    def lambda_12381():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12381)
    WaitChrThread(0x105, 1)

    def lambda_12392():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12392)
    Sleep(50)

    def lambda_123AA():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_123AA)
    Sleep(50)

    def lambda_123C2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_123C2)
    Sleep(50)

    def lambda_123DA():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_123DA)
    Sleep(50)

    def lambda_123F2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123F2)
    Sleep(50)

    def lambda_1240A():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1240A)
    Sleep(50)

    def lambda_12422():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12422)
    Sleep(50)

    def lambda_1243A():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1243A)
    Sleep(50)

    def lambda_12452():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12452)
    Sleep(50)

    def lambda_1246A():
        OP_95(0xFE, -1910, 0, 11190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1246A)
    WaitChrThread(0x1F, 1)

    def lambda_12488():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12488)
    WaitChrThread(0x1D, 1)

    def lambda_12499():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12499)
    WaitChrThread(0x1E, 1)

    def lambda_124AA():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_124AA)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 1)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    Sleep(2000)
    OP_93(0x23, 0xB4, 0x0)

    def lambda_12509():

        label("loc_12509")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12509")

    QueueWorkItem2(0x101, 1, lambda_12509)
    Sleep(50)

    def lambda_1251E():

        label("loc_1251E")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1251E")

    QueueWorkItem2(0x102, 1, lambda_1251E)
    Sleep(50)

    def lambda_12533():

        label("loc_12533")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12533")

    QueueWorkItem2(0x103, 1, lambda_12533)
    Sleep(50)

    def lambda_12548():

        label("loc_12548")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12548")

    QueueWorkItem2(0x104, 1, lambda_12548)
    Sleep(50)

    def lambda_1255D():

        label("loc_1255D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1255D")

    QueueWorkItem2(0x105, 1, lambda_1255D)
    Sleep(50)

    def lambda_12572():

        label("loc_12572")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12572")

    QueueWorkItem2(0xC, 1, lambda_12572)
    Sleep(50)

    def lambda_12587():

        label("loc_12587")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12587")

    QueueWorkItem2(0x1D, 1, lambda_12587)
    Sleep(50)

    def lambda_1259C():

        label("loc_1259C")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1259C")

    QueueWorkItem2(0x1F, 1, lambda_1259C)
    Sleep(50)

    def lambda_125B1():

        label("loc_125B1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_125B1")

    QueueWorkItem2(0x1E, 1, lambda_125B1)
    Sleep(100)

    def lambda_125C6():

        label("loc_125C6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_125C6")

    QueueWorkItem2(0x109, 1, lambda_125C6)
    Sleep(50)

    def lambda_125DB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_125DB)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    def lambda_12627():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12627)
    Sleep(50)

    def lambda_1263F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1263F)
    Sleep(50)

    def lambda_12657():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12657)
    Sleep(500)

    #C0729
    ChrTalk(
        0xD,
        "ふふ、それではおさらばです。\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xD,
        "もう会うこともありますまい。\x02",
    )

    CloseMessageWindow()

    def lambda_126B3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_126B3)
    Sleep(3000)
    BeginChrThread(0x28, 1, 0, 63)
    BeginChrThread(0x20, 3, 0, 57)
    Sleep(500)
    BeginChrThread(0x21, 3, 0, 58)
    Sleep(500)
    BeginChrThread(0x22, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x23, 3, 0, 60)
    Sleep(300)
    BeginChrThread(0x24, 3, 0, 61)
    Sleep(3000)
    Fade(500)
    OP_68(1180, 1500, 16250, 0)
    MoveCamera(337, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x1D, -170, 0, 13620, 45)
    SetChrPos(0x1F, -880, 0, 12290, 45)
    SetChrPos(0x1E, -2560, 0, 13500, 45)
    SetChrPos(0x101, -2100, 0, 15860, 180)
    SetChrPos(0x102, -1230, 0, 16850, 180)
    SetChrPos(0x103, -600, 0, 18000, 180)
    SetChrPos(0x104, -3190, 0, 16370, 180)
    SetChrPos(0x109, -2640, 0, 17580, 180)
    SetChrPos(0x105, -1830, 0, 18600, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    OP_0D()
    EndChrThread(0x28, 0x1)

    #C0731
    ChrTalk(
        0x1D,
        "デ、デリック……！\x02",
    )

    CloseMessageWindow()

    def lambda_1280A():
        OP_95(0xFE, 5240, 0, 18260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1280A)
    Sleep(100)

    def lambda_12827():
        OP_95(0xFE, 3790, 0, 19250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12827)
    Sleep(100)

    def lambda_12844():
        OP_95(0xFE, 3560, 0, 17530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12844)
    WaitChrThread(0x1D, 1)

    def lambda_12862():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12862)
    WaitChrThread(0x1F, 1)

    def lambda_12873():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12873)
    WaitChrThread(0x1E, 1)

    def lambda_12884():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12884)
    WaitChrThread(0x1E, 1)

    #C0732
    ChrTalk(
        0xC,
        "うう……\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        "#00007Fくそっ、逃がすかッ……！\x02",
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x103,
        "#00201F行きましょう……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x0)

    def lambda_12917():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12917)
    Sleep(100)

    def lambda_12934():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12934)
    Sleep(100)

    def lambda_12951():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12951)
    Sleep(100)

    def lambda_1296E():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1296E)
    Sleep(100)

    def lambda_1298B():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1298B)
    Sleep(100)

    def lambda_129A8():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_129A8)
    Sleep(500)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(8750, 1500, -17760, 0)
    MoveCamera(345, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, -1860, 0, -3290, 180)
    SetChrPos(0x102, -3230, 0, -2980, 180)
    SetChrPos(0x103, -930, 0, -2320, 180)
    SetChrPos(0x104, -2380, 0, -1730, 180)
    SetChrPos(0x109, -1370, 0, -940, 180)
    SetChrPos(0x105, -3640, 0, -1220, 180)
    OP_0D()
    OP_71(0xD, 0x10F, 0x12C, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 42)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 43)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 46)
    Sleep(500)
    OP_71(0xD, 0x3C, 0x5A, 0x0, 0x0)
    Sound(494, 0, 100, 0)
    Sleep(500)
    OP_68(6900, 1500, -19750, 3000)
    MoveCamera(345, 24, 0, 3000)
    BeginChrThread(0x25, 1, 0, 62)
    OP_71(0xD, 0x79, 0xB4, 0x1, 0x20)
    Sleep(800)
    OP_6F(0x79)
    OP_68(6820, 1500, -15790, 3000)
    SetCameraDistance(15150, 3000)
    WaitChrThread(0x101, 3)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x102, 3)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x103, 3)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 3)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x109, 3)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 3)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)

    #C0735
    ChrTalk(
        0x102,
        "#00105Fああっ……！\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x103,
        (
            "#00206Fまんまと逃げられて\x01",
            "しまいましたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x109,
        (
            "#10106Fうう……悔しいです！\x01",
            "あんな卑怯な輩を\x01",
            "取り逃がしてしまうなんて……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
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
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    #C0738
    ChrTalk(
        0x101,
        (
            "#00006F……ひとまず村人たちに\x01",
            "被害がなくてよかったよ。\x02\x03",

            "#00000Fとりあえずそれだけでも\x01",
            "よしとしなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、ヤツを捕まえるのは\x01",
            "また今度のお楽しみって訳だね。\x02\x03",

            "#10300Fとりあえず、村長たちと合流して\x01",
            "事件の報告をするとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x101,
        "#00000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x104,
        "#00303F（…………………………）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_CB66 end

    def Function_35_12DA0(): pass

    label("Function_35_12DA0")

    OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 2060, 0, 16660, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_35_12DA0 end

    def Function_36_12DD4(): pass

    label("Function_36_12DD4")

    OP_97(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 1450, 0, 17650, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_36_12DD4 end

    def Function_37_12E08(): pass

    label("Function_37_12E08")

    OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2050, 0, 15310, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_37_12E08 end

    def Function_38_12E3C(): pass

    label("Function_38_12E3C")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 420, 0, 18380, 2000, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_38_12E3C end

    def Function_39_12E70(): pass

    label("Function_39_12E70")

    OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 870, 0, 16059, 2000, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)
    Return()

    # Function_39_12E70 end

    def Function_40_12EA4(): pass

    label("Function_40_12EA4")

    OP_97(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 170, 0, 17060, 2000, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_40_12EA4 end

    def Function_41_12ED8(): pass

    label("Function_41_12ED8")

    OP_97(0x101, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 7230, 0, -14950, 3500, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_41_12ED8 end

    def Function_42_12F0C(): pass

    label("Function_42_12F0C")

    OP_97(0x102, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 5740, 0, -15440, 3500, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_42_12F0C end

    def Function_43_12F40(): pass

    label("Function_43_12F40")

    OP_97(0x103, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 7140, 0, -13390, 3500, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_43_12F40 end

    def Function_44_12F74(): pass

    label("Function_44_12F74")

    OP_97(0x104, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 5860, 0, -14270, 3500, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_44_12F74 end

    def Function_45_12FA8(): pass

    label("Function_45_12FA8")

    OP_97(0x109, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 5870, 0, -12970, 3500, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_45_12FA8 end

    def Function_46_12FDC(): pass

    label("Function_46_12FDC")

    OP_97(0x105, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 4340, 0, -14470, 3500, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_46_12FDC end

    def Function_47_13010(): pass

    label("Function_47_13010")

    OP_97(0x1D, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1D, 1)
    OP_95(0x1D, -1530, 0, 11680, 2000, 0x0)
    OP_93(0x1D, 0x2D, 0x1F4)
    Return()

    # Function_47_13010 end

    def Function_48_13044(): pass

    label("Function_48_13044")

    OP_97(0x1F, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1F, 1)
    OP_95(0x1F, -2380, 0, 13280, 2000, 0x0)
    OP_93(0x1F, 0x2D, 0x1F4)
    Return()

    # Function_48_13044 end

    def Function_49_13078(): pass

    label("Function_49_13078")

    OP_97(0x1E, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1E, 1)
    OP_95(0x1E, -720, 0, 12970, 2000, 0x0)
    OP_93(0x1E, 0x2D, 0x1F4)
    Return()

    # Function_49_13078 end

    def Function_50_130AC(): pass

    label("Function_50_130AC")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_130B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130D3")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_130B7")

    label("loc_130D3")

    Return()

    # Function_50_130AC end

    def Function_51_130D4(): pass

    label("Function_51_130D4")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_130DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130F6")
    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_130DF")

    label("loc_130F6")

    Return()

    # Function_51_130D4 end

    def Function_52_130F7(): pass

    label("Function_52_130F7")


    def lambda_130FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_130FC)

    def lambda_1310D():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1310D)
    WaitChrThread(0x20, 1)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0x20, 4710, 0, -15670, 6000, 0x0)
    OP_95(0x20, -2120, 0, -1730, 6000, 0x0)
    OP_95(0x20, -2120, 0, 14270, 6000, 0x0)
    Return()

    # Function_52_130F7 end

    def Function_53_1316C(): pass

    label("Function_53_1316C")


    def lambda_13171():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_13171)

    def lambda_13182():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_13182)
    WaitChrThread(0x21, 1)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0x21, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x21, 830, 0, -10410, 7000, 0x0)
    OP_95(0x21, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x21, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_53_1316C end

    def Function_54_131F5(): pass

    label("Function_54_131F5")


    def lambda_131FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_131FA)

    def lambda_1320B():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1320B)
    WaitChrThread(0x22, 1)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0x22, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x22, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x22, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_54_131F5 end

    def Function_55_1326A(): pass

    label("Function_55_1326A")


    def lambda_1326F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1326F)

    def lambda_13280():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_13280)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0x23, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x23, 830, 0, -10410, 7000, 0x0)
    OP_95(0x23, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x23, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_55_1326A end

    def Function_56_132F3(): pass

    label("Function_56_132F3")


    def lambda_132F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_132F8)

    def lambda_13309():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_13309)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0x24, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x24, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x24, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_56_132F3 end

    def Function_57_13368(): pass

    label("Function_57_13368")

    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_57_13368 end

    def Function_58_133B3(): pass

    label("Function_58_133B3")

    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_58_133B3 end

    def Function_59_133FE(): pass

    label("Function_59_133FE")

    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_59_133FE end

    def Function_60_13449(): pass

    label("Function_60_13449")

    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_60_13449 end

    def Function_61_13494(): pass

    label("Function_61_13494")

    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_61_13494 end

    def Function_62_134DF(): pass

    label("Function_62_134DF")

    OP_9E(0xFE, 0x316, 0xFFFFE642, 0xEA60, 0x1B58, 0x4)
    Sound(487, 0, 100, 0)
    Sleep(500)
    Sleep(200)
    Sound(486, 0, 100, 0)
    OP_9F(0x0, 0x25)
    OP_9F(0x1, 12190, 0, -23580)
    OP_9F(0x1, 16760, 0, -26550)
    OP_9F(0x1, 23260, 0, -32810)
    OP_9F(0x2, 0x25, 9000, 0x6)
    Return()

    # Function_62_134DF end

    def Function_63_1353E(): pass

    label("Function_63_1353E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13557")
    Sound(845, 0, 80, 0)
    Sleep(350)
    Jump("Function_63_1353E")

    label("loc_13557")

    Return()

    # Function_63_1353E end

    def Function_64_13558(): pass

    label("Function_64_13558")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1720, 1500, -10600, 0)
    MoveCamera(344, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, 720, 0, -10290, 325)
    SetChrPos(0x102, 1980, 0, -9830, 325)
    SetChrPos(0x103, 740, 0, -11540, 325)
    SetChrPos(0x104, 2190, 0, -11320, 325)
    SetChrPos(0x109, 2210, 0, -12700, 325)
    SetChrPos(0x105, 3580, 0, -11240, 325)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_13612():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13612)
    Sleep(50)

    def lambda_1362A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1362A)
    Sleep(50)

    def lambda_13642():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13642)
    Sleep(50)

    def lambda_1365A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1365A)
    Sleep(50)

    def lambda_13672():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13672)
    Sleep(50)

    def lambda_1368A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1368A)
    OP_68(1050, 1500, -9540, 3000)
    SetCameraDistance(17450, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_136C3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_136C3)
    WaitChrThread(0x101, 1)

    def lambda_136D4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_136D4)
    WaitChrThread(0x102, 1)

    def lambda_136E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_136E5)
    WaitChrThread(0x103, 1)

    def lambda_136F6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_136F6)
    WaitChrThread(0x104, 1)

    def lambda_13707():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13707)
    WaitChrThread(0x109, 1)

    def lambda_13718():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13718)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0742
    ChrTalk(
        0x101,
        "#00000Fアルモリカ村についたか……\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x102,
        "#00105Fこの村のどこかにゲバルさんが……？\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x104,
        (
            "#00300Fとにかく、怪しい場所を\x01",
            "探してみるとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x103,
        (
            "#00200F村の人にも、話を聞いた方が\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19D, 2)
    ModifyEventFlags(0, 2, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1810, 0, -3210, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x90, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_64_13558 end

    def Function_65_1383B(): pass

    label("Function_65_1383B")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0746
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1395C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_138DA")

    #C0747
    ChrTalk(
        0x101,
        (
            "#00000F……一度、村長に相談してみよう。\x01",
            "何か知ってるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13958")

    label("loc_138DA")


    #C0748
    ChrTalk(
        0x101,
        (
            "#00003F中に人がいる気配があるけど……\x02\x03",

            "#00000Fとにかく聞き込みを続けよう。\x01",
            "村に住んでいる人なら\x01",
            "何か分かるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13958")

    TalkEnd(0xFF)
    Return()

    label("loc_1395C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396E")
    TalkEnd(0xFF)
    Jump("loc_13D11")

    label("loc_1396E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15660, 5000, 47180, 0)
    MoveCamera(313, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 15740, 3500, 47460, 0)
    SetChrPos(0x102, 15140, 3500, 46070, 0)
    SetChrPos(0x103, 16540, 3500, 46260, 0)
    SetChrPos(0x104, 15130, 3500, 44850, 0)
    SetChrPos(0x109, 16950, 3500, 45060, 0)
    SetChrPos(0x105, 16149, 3500, 43850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0749
    ChrTalk(
        0x102,
        "#00105Fロイド、ここって……\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x101,
        (
            "#00003F前に来たとき、\x01",
            "鍵なんかかかってたっけ……？\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 80, 0)
    Sleep(400)
    Sound(811, 0, 50, 0)
    Sleep(500)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0751
    ChrTalk(
        0x109,
        "#10105F今の音……\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x104,
        "#00303F……中に人がいる気配、だな。\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x103,
        "#00200Fええ、そうだと思います。\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x105,
        "#10302Fフフ、あからさまに怪しいね。\x02",
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_13C51")

    #C0755
    ChrTalk(
        0x101,
        "#00003Fもしかすると……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0756
    ChrTalk(
        0x101,
        (
            "#00001F……一度、村長に相談してみよう。\x01",
            "何か知ってるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_13CD8")

    label("loc_13C51")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0757
    ChrTalk(
        0x101,
        (
            "#00003F……とにかく、\x01",
            "ここは一旦置いておいて\x01",
            "聞き込みを続けよう。\x02\x03",

            "#00001F村に住んでいる人なら\x01",
            "何か分かるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CD8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 16100, 3500, 45380, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_13D11")

    Return()

    # Function_65_1383B end

    def Function_66_13D12(): pass

    label("Function_66_13D12")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(16250, 5000, 46160, 0)
    MoveCamera(318, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15440, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 15770, 3500, 47280, 0)
    SetChrPos(0x101, 16040, 3500, 45180, 0)
    SetChrPos(0x102, 15140, 3500, 44440, 0)
    SetChrPos(0x103, 17030, 3500, 44510, 0)
    SetChrPos(0x104, 16260, 3500, 43520, 0)
    SetChrPos(0x109, 15070, 3500, 42860, 0)
    SetChrPos(0x105, 17520, 3500, 43210, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0758
    ChrTalk(
        0x1D,
        (
            "……村長のトルタだ。\x01",
            "少しいいかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x1D,
        (
            "君と話をしたいという\x01",
            "者たちが来ておるのだが。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("中年の声")

    #A0760
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…………！\x02\x03",

            "か、帰ってくれるように\x01",
            "言ってもらえまいか。\x02\x03",

            "ご迷惑をおかけするが、\x01",
            "しばらく誰にも会いたくは\x01",
            "ないのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x1D,
        "……安心したまえ。\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x1D,
        (
            "会いにきたというのは\x01",
            "君の息子夫婦ではないのだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年の声")

    #A0763
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "な、なぜその事を……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(300)

    #C0764
    ChrTalk(
        0x101,
        (
            "#00003Fゲバルさん、聞こえますか？\x02\x03",

            "#00000Fクロスベル警察、\x01",
            "特務支援課の者です。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年の声")

    #A0765
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "け、警察だと……！？\x02\x03",

            "い、一体わしに何の用だね！\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x101,
        (
            "#00003F……突然伺ってしまってすみません。\x02\x03",

            "#00000F俺たちはアルムさんたちから\x01",
            "依頼をうけて、\x01",
            "あなたを捜索していました。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年の声")

    #A0767
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なっ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        (
            "#00000Fでも、強制的に連行するような\x01",
            "ことはしないつもりですし、\x01",
            "そんな権限もありません。\x02\x03",

            "#00004Fあなたがどうしてもというなら\x01",
            "アルムさんたちに事情を話して、\x01",
            "依頼を取り下げてもらうこともできます。\x02\x03",

            "#00000Fどうか、お話だけでも\x01",
            "聞かせていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年の声")

    #A0769
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 0, 100, 0)
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

    #C0770
    ChrTalk(
        0x102,
        "#00100F鍵を開けてくれたみたいね。\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x101,
        (
            "#00000Fああ……\x01",
            "それじゃあ、入ってみるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x5A, 0x1F4)
    OP_9B(0x1, 0x1D, 0xB4, 0x3E8, 0x7D0, 0x0)
    OP_95(0x101, 15770, 3500, 47280, 2000, 0x0)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 67)
    BeginChrThread(0x102, 3, 0, 68)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 69)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 71)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 72)
    WaitChrThread(0x105, 3)
    BeginChrThread(0x1D, 3, 0, 73)
    WaitChrThread(0x1D, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_13D12 end

    def Function_67_14347(): pass

    label("Function_67_14347")

    OP_93(0x101, 0x0, 0x0)

    def lambda_14353():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14353)

    def lambda_14368():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14368)
    Return()

    # Function_67_14347 end

    def Function_68_14375(): pass

    label("Function_68_14375")

    OP_95(0x102, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x0)

    def lambda_14395():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14395)

    def lambda_143AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_143AA)
    Return()

    # Function_68_14375 end

    def Function_69_143B7(): pass

    label("Function_69_143B7")

    OP_95(0x103, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x103, 0x0, 0x0)

    def lambda_143D7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_143D7)

    def lambda_143EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_143EC)
    Return()

    # Function_69_143B7 end

    def Function_70_143F9(): pass

    label("Function_70_143F9")

    OP_95(0x104, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_14419():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14419)

    def lambda_1442E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1442E)
    Return()

    # Function_70_143F9 end

    def Function_71_1443B(): pass

    label("Function_71_1443B")

    OP_95(0x109, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x109, 0x0, 0x0)

    def lambda_1445B():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1445B)

    def lambda_14470():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14470)
    Return()

    # Function_71_1443B end

    def Function_72_1447D(): pass

    label("Function_72_1447D")

    OP_95(0x105, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x105, 0x0, 0x0)

    def lambda_1449D():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1449D)

    def lambda_144B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_144B2)
    Return()

    # Function_72_1447D end

    def Function_73_144BF(): pass

    label("Function_73_144BF")

    OP_95(0x1D, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x0)

    def lambda_144DF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_144DF)

    def lambda_144F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_144F4)
    Return()

    # Function_73_144BF end

    def Function_74_14501(): pass

    label("Function_74_14501")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 5000, 44740, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17430, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13580, 3500, 43350, 0)
    SetChrChipByIndex(0x26, 0xA)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 3500, 46310, 135)
    SetChrChipByIndex(0x27, 0xB)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 13050, 3500, 45510, 135)
    OP_4B(0x26, 0xFF)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 15510, 3500, 44690, 315)
    SetChrPos(0x102, 14840, 3500, 43910, 315)
    SetChrPos(0x103, 16500, 3500, 44690, 315)
    SetChrPos(0x104, 15040, 3500, 42890, 315)
    SetChrPos(0x109, 15980, 3500, 42470, 315)
    SetChrPos(0x105, 16900, 3500, 43550, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(15430, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0772
    ChrTalk(
        0x26,
        "この中に、父さんがいるんだね？\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x101,
        "#00000Fええ、間違いありません。\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x102,
        (
            "#00100F今から会ってくれるという\x01",
            "約束もとりつけてます。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x26,
        "おお～、ありがとう！\x02",
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x26,
        (
            "正直、なんでこんな場所に\x01",
            "隠れていたかは知らないけど……\x01",
            "本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0777
    ChrTalk(
        0x27,
        (
            "ふふ、よかったわねアルム。\x01",
            "これでようやく\x01",
            "お義父さまに会えるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x27,
        (
            "結婚式に呼べなかった\x01",
            "お詫びも含めて、ちゃんと\x01",
            "ご挨拶しないとね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0779
    ChrTalk(
        0x26,
        (
            "ああエアリー……\x01",
            "君の心はどうしてそんなに\x01",
            "綺麗なんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x26,
        (
            "新雪のように透き通った君の心に、\x01",
            "僕の心は釘付けさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x27,
        "ああ、アルム……\x02",
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x103,
        "#00203F#4S納屋に入ってください。\x02",
    )

    CloseMessageWindow()

    def lambda_1487E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1487E)
    Sleep(50)

    def lambda_1488E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1488E)
    Sleep(300)

    #C0783
    ChrTalk(
        0x26,
        "ハッ……！？\x02",
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x27,
        "うふふ、ごめんなさいね。\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x27,
        (
            "ほぉら、アルミンも。\x01",
            "ご・め・ん・な・さ・い。\x02",
        )
    )

    CloseMessageWindow()

    #N0786
    NpcTalk(
        0x27,
        "赤ん坊",
        "ばぶぅ。\x02",
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x27,
        "よくできまちたね～。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0788
    ChrTalk(
        0x109,
        "#10106F（つ、疲れますね……）\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x1D,
        (
            "と、ともかく\x01",
            "中でゲバル殿がお待ちだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x105,
        (
            "#10302Fフフ……\x01",
            "心ゆくまでトークを\x01",
            "楽しむといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x26,
        "ああ、そうさせてもらうよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0792
    ChrTalk(
        0x26,
        "行こう、エアリー。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0793
    ChrTalk(
        0x27,
        "ええ、アルム。\x02",
    )

    CloseMessageWindow()

    def lambda_14AC2():
        OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_14AC2)
    Sleep(300)

    def lambda_14ADF():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_14ADF)

    def lambda_14AF4():

        label("loc_14AF4")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14AF4")

    QueueWorkItem2(0x101, 1, lambda_14AF4)
    Sleep(50)

    def lambda_14B09():

        label("loc_14B09")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B09")

    QueueWorkItem2(0x102, 1, lambda_14B09)
    Sleep(50)

    def lambda_14B1E():

        label("loc_14B1E")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B1E")

    QueueWorkItem2(0x103, 1, lambda_14B1E)
    Sleep(50)

    def lambda_14B33():

        label("loc_14B33")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B33")

    QueueWorkItem2(0x104, 1, lambda_14B33)
    Sleep(50)

    def lambda_14B48():

        label("loc_14B48")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B48")

    QueueWorkItem2(0x109, 1, lambda_14B48)
    Sleep(50)

    def lambda_14B5D():

        label("loc_14B5D")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B5D")

    QueueWorkItem2(0x105, 1, lambda_14B5D)
    Sleep(50)

    def lambda_14B72():

        label("loc_14B72")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B72")

    QueueWorkItem2(0x1D, 1, lambda_14B72)
    WaitChrThread(0x26, 1)
    OP_93(0x26, 0x0, 0x1F4)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)
    BeginChrThread(0x26, 3, 0, 75)
    Sleep(500)
    BeginChrThread(0x27, 3, 0, 75)
    Sleep(500)
    WaitChrThread(0x27, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_74_14501 end

    def Function_75_14C04(): pass

    label("Function_75_14C04")

    OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x0)

    def lambda_14C24():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C24)

    def lambda_14C39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C39)
    Return()

    # Function_75_14C04 end

    def Function_76_14C46(): pass

    label("Function_76_14C46")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 5000, 44740, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15430, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13580, 3500, 43350, 0)
    SetChrChipByIndex(0x26, 0xA)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 3500, 46310, 135)
    SetChrChipByIndex(0x27, 0xB)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 13050, 3500, 45510, 135)
    OP_4B(0x26, 0xFF)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 15510, 3500, 44690, 315)
    SetChrPos(0x102, 14840, 3500, 43910, 315)
    SetChrPos(0x103, 16500, 3500, 44690, 315)
    SetChrPos(0x104, 15040, 3500, 42890, 315)
    SetChrPos(0x109, 15980, 3500, 42470, 315)
    SetChrPos(0x105, 16900, 3500, 43550, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0794
    ChrTalk(
        0x26,
        "皆さん、本当にありがとう。\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x26,
        (
            "おかげで父さんにも会えて、\x01",
            "エアリーとアルミンを紹介できたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x27,
        (
            "ふふ、お義父さまったら\x01",
            "とってもうれしそうだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、力になれてよかったです。\x02\x03",

            "#00005Fえっと、ゲバルさんは……\x01",
            "まだ中にいるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x26,
        (
            "ああ、なんだか考えたいことが\x01",
            "あるから後で帰るっていうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x27,
        (
            "話してる途中で突然後ろを向いちゃって、\x01",
            "ちっともお顔を見せてくれないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x27,
        "一体どうしちゃったのかしら……\x02",
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
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0801
    ChrTalk(
        0x1D,
        "ふむ……\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x102,
        "#00105Fそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x104,
        "#00304F悪徳議員の目にも……ってやつか。\x02",
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x103,
        "#00205F驚きです。\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x105,
        (
            "#10304Fフフ……\x01",
            "ここはまあ、そっとしとくのが\x01",
            "男の務めってヤツだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0806
    ChrTalk(
        0x101,
        (
            "#00009Fはは、きっと大丈夫なので\x01",
            "心配なさらないでください。\x02\x03",

            "#00000Fお２人は、これからどうするんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x26,
        (
            "ああ、せっかく父さんと\x01",
            "再会できたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x26,
        (
            "これからは連絡を\x01",
            "取り合っていこうって\x01",
            "話になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x27,
        (
            "お義母さまのこともあるから\x01",
            "簡単にはいかないかも\x01",
            "しれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x27,
        (
            "ゆくゆくはリベール王国のほうに\x01",
            "来ていただくつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x109,
        (
            "#10102Fそうですか……\x01",
            "ふふ、うまくいくといいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x26,
        (
            "父さんも議員を\x01",
            "辞めちゃったみたいだし、\x01",
            "きっといつかそうなるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x26,
        (
            "そう……僕たちには\x01",
            "輝かしい未来が待ってる！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0814
    ChrTalk(
        0x26,
        "そうだろう、エアリー！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0815
    ChrTalk(
        0x27,
        "ええ、アルム！\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x27,
        (
            "この子を初めて抱いた時、\x01",
            "２人で誓ったものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x27,
        (
            "これからアルミンに、\x01",
            "たくさんの弟や妹を授かって……\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x26,
        (
            "……僕と君、そして\x01",
            "沢山の愛すべき子供たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x26,
        (
            "みんなで大陸一の家族を築く。\x01",
            "……そうだったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x26,
        "ああ、愛しているよエアリー！\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x27,
        "私もよ、アルム！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x27, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0822
    ChrTalk(
        0x101,
        (
            "#00006F（そこまで聞いたつもりは\x01",
            "  なかったんだけど……\x01",
            "  ま、まあいいか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x104,
        (
            "#00300Fそんじゃあ、ひとまずこれで\x01",
            "依頼は達成ってカンジだな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1557C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1557C)
    Sleep(50)

    def lambda_1558C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1558C)
    Sleep(300)

    #C0824
    ChrTalk(
        0x26,
        (
            "ああ、本当にお世話になったよ。\x01",
            "お礼をいくら言っても\x01",
            "言い足りないくらいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x27,
        (
            "私たちももう少ししたら\x01",
            "リベールに帰るわ。\x01",
            "本当にありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x103,
        "#00202Fええ、どうかお気をつけて。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0827
    ChrTalk(
        0x26,
        (
            "それじゃあエアリー、\x01",
            "せっかくだからもうしばらく\x01",
            "こっちで観光していこうよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0828
    ChrTalk(
        0x27,
        "ええアルム、そうしましょう。\x02",
    )

    CloseMessageWindow()
    OP_93(0x27, 0x87, 0x0)

    def lambda_156E4():
        OP_9B(0x1, 0xFE, 0xB4, 0x262, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_156E4)
    Sleep(100)

    def lambda_156FC():
        OP_95(0xFE, 13050, 3500, 45510, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_156FC)
    WaitChrThread(0x26, 1)
    OP_93(0x27, 0xE1, 0x1F4)
    Sleep(500)
    OP_68(12010, 5000, 41990, 4000)
    MoveCamera(340, 27, 0, 4000)
    OP_6E(600, 4000)

    def lambda_15749():
        OP_95(0xFE, 7890, 3500, 42250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15749)

    def lambda_15763():
        OP_95(0xFE, 6900, 3500, 42860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15763)

    def lambda_1577D():

        label("loc_1577D")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_1577D")

    QueueWorkItem2(0x101, 1, lambda_1577D)
    Sleep(50)

    def lambda_15792():

        label("loc_15792")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15792")

    QueueWorkItem2(0x102, 1, lambda_15792)
    Sleep(50)

    def lambda_157A7():

        label("loc_157A7")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157A7")

    QueueWorkItem2(0x103, 1, lambda_157A7)
    Sleep(50)

    def lambda_157BC():

        label("loc_157BC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157BC")

    QueueWorkItem2(0x104, 1, lambda_157BC)
    Sleep(50)

    def lambda_157D1():

        label("loc_157D1")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157D1")

    QueueWorkItem2(0x109, 1, lambda_157D1)
    Sleep(50)

    def lambda_157E6():

        label("loc_157E6")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157E6")

    QueueWorkItem2(0x105, 1, lambda_157E6)
    Sleep(50)

    def lambda_157FB():

        label("loc_157FB")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157FB")

    QueueWorkItem2(0x1D, 1, lambda_157FB)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)

    def lambda_15815():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_15815)

    def lambda_15822():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_15822)
    OP_6F(0x79)

    def lambda_15831():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15831)

    def lambda_1583E():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1583E)
    Sleep(500)

    #C0829
    ChrTalk(
        0x26,
        "あはは、エアリー㈱\x02",
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x27,
        "うふふ、あなた㈱\x02",
    )

    CloseMessageWindow()

    #N0831
    NpcTalk(
        0x27,
        "赤ん坊",
        "ばぶぶ～。\x02",
    )

    CloseMessageWindow()

    def lambda_15893():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_15893)

    def lambda_158A0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_158A0)
    Sleep(300)

    def lambda_158B0():
        OP_95(0xFE, 4830, 2000, 38020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_158B0)

    def lambda_158CA():
        OP_95(0xFE, 4470, 2000, 39100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_158CA)
    Sleep(1000)
    OP_68(15240, 5000, 43490, 5000)
    MoveCamera(5, 29, 0, 5000)
    OP_6E(600, 5000)
    WaitChrThread(0x26, 1)

    def lambda_15910():
        OP_95(0xFE, 1480, 2000, 40200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15910)
    Sleep(100)

    def lambda_1592D():
        OP_95(0xFE, 1940, 2000, 41000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1592D)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    OP_0D()
    OP_6F(0x79)

    #C0832
    ChrTalk(
        0x101,
        (
            "#00006F……最初から最後まで、\x01",
            "すごいインパクトのある\x01",
            "人たちだったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、ほんと。\x01",
            "あそこまでいくと\x01",
            "逆にうらやましいかも……\x02\x03",

            "#00104F私も両親と久しぶりに\x01",
            "会いたくなっちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x109,
        (
            "#10105Fエリィさん……\x02\x03",

            "#10109Fふふ、そうですね。\x01",
            "あたしも母さんにたくさん親孝行を\x01",
            "してあげたい気分です。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x102, 500)
    Sleep(300)

    #C0835
    ChrTalk(
        0x1D,
        (
            "さて、ついでにわしからも\x01",
            "礼を言わせてもらおうかのう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15AE6():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15AE6)
    Sleep(50)

    def lambda_15AF6():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15AF6)
    Sleep(50)

    def lambda_15B06():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15B06)
    Sleep(50)

    def lambda_15B16():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15B16)
    Sleep(50)

    def lambda_15B26():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15B26)
    Sleep(50)

    def lambda_15B36():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15B36)
    Sleep(300)

    #C0836
    ChrTalk(
        0x1D,
        (
            "ゲバル殿が落ち着いて\x01",
            "市内に戻るまで、きちんと\x01",
            "面倒はみさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x101,
        (
            "#00004Fええ、色々と協力\x01",
            "ありがとうございます。\x02\x03",

            "#00000F俺たちもそろそろ行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x105,
        "#10300Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0839
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【生き別れの父の捜索】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x90, 0x1, 0x7)
    OP_29(0x90, 0x1, 0x8)
    OP_29(0x90, 0x4, 0x10)
    SetChrFlags(0x1D, 0x80)
    OP_D7(0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x26, 0xFF)
    OP_4C(0x27, 0xFF)
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x4, 0x1)
    SetChrPos(0x0, 15390, 3500, 43000, 315)
    SetChrPos(0x26, 3170, 0, 14230, 135)
    SetChrPos(0x27, 2120, 0, 13670, 135)
    OP_69(0xFF, 0x0)
    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0x1B26, 0x1F4, 0x143C)
    OP_E3(0x7936, 0x1F4, 0xFFFFFD6C)
    EventEnd(0x5)
    Return()

    # Function_76_14C46 end

    def Function_77_15D0A(): pass

    label("Function_77_15D0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x14, 0x80)
    OP_78(0xE, 0x14)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_75(0xE, 0x1, 0x0)
    OP_71(0xE, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0xE, 0x2EE, 0x2EE, 0x2EE)
    ClearChrFlags(0x15, 0x80)
    OP_78(0xF, 0x15)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_71(0xF, 0x65, 0xA0, 0x0, 0x20)
    OP_FF(0xF, 0x307, 0x307, 0x307)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x10, 0x16)
    OP_49()
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    OP_75(0x10, 0x1, 0x0)
    OP_FF(0x10, 0x2EE, 0x2EE, 0x2EE)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x14, -46000, 16400, 90000, 260)
    OP_D5(0x14, 0x0, 0x3F7A0, 0x0, 0x0)
    SetChrPos(0x15, -46000, 16400, 90000, 260)
    OP_D5(0x15, 0x0, 0x3F7A0, 0x0, 0x0)
    SetChrPos(0x16, -46000, 0, 90000, 260)
    OP_D5(0x16, 0x0, 0x3F7A0, 0x0, 0x0)

    def lambda_15E3F():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15E3F)

    def lambda_15E59():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15E59)
    OP_82(0x32, 0x32, 0xBB8, 0x1F40)
    BeginChrThread(0x14, 0, 0, 78)
    OP_68(-26000, 5600, 70000, 0)
    MoveCamera(330, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(80000, 0)
    OP_68(-46000, 6900, 90000, 10000)
    MoveCamera(330, 30, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(70000, 10000)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, -18430, 3500, 62180, 330)
    SetChrPos(0x103, -17200, 3500, 62670, 324)
    SetChrPos(0x105, -18600, 3500, 60920, 324)
    SetChrPos(0x107, -15340, 3500, 61450, 277)
    SetChrSubChip(0x107, 0x5)
    OP_68(-24740, 5600, 71790, 0)
    MoveCamera(324, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24190, 0)
    OP_68(-18990, 5600, 64470, 5000)

    def lambda_15FB7():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15FB7)

    def lambda_15FD1():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15FD1)
    BeginChrThread(0x14, 0, 0, 80)
    BeginChrThread(0x15, 0, 0, 79)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(497, 3000, 90)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x0)
    OP_68(-17780, 5600, 62410, 0)
    MoveCamera(323, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16850, 0)
    OP_0D()
    Sleep(300)

    #C0840
    ChrTalk(
        0x105,
        (
            "#10406F#6Pさて、無事降りられたけど……\x02\x03",

            "#10408F……しかしここって、\x01",
            "村のレンゲ畑だった場所だよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x101,
        (
            "#00013F#6Pああ……\x01",
            "随分様子が変わってるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x103,
        (
            "#00206F#12P……これもキーアが覚醒した\x01",
            "影響なのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-17020, 5600, 61730, 1000)
    TurnDirection(0x103, 0x107, 400)
    OP_6F(0x79)

    #C0843
    ChrTalk(
        0x103,
        (
            "#00201F#5Pツァイト。\x01",
            "幻獣の気配はどうでしょう？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1617E():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1617E)
    Sleep(0)

    def lambda_1618E():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1618E)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0844
    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C#Nふむ、今のところ\x01",
            "出現する気配は無さそうだ。\x02\x03",

            "#01200F当面はあの法陣を\x01",
            "頼りにしても問題なかろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0845
    ChrTalk(
        0x101,
        (
            "#00003F#5P分かった。\x02\x03",

            "#00001Fとりあえずトルタ村長に\x01",
            "挨拶した方が良さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x103,
        (
            "#00202F#11Pはい。\x01",
            "行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17100, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    OP_24(0x3B6)
    SetScenarioFlags(0x22, 0)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_77_15D0A end

    def Function_78_162BE(): pass

    label("Function_78_162BE")

    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0xF, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_75(0xE, 0x2, 0x7D0)
    OP_75(0x10, 0x2, 0x7D0)
    Sleep(1000)
    OP_79(0xF)
    Return()

    # Function_78_162BE end

    def Function_79_16303(): pass

    label("Function_79_16303")

    OP_75(0xE, 0x1, 0x7D0)
    OP_75(0x10, 0x1, 0x7D0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0xF, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_79(0xF)
    OP_71(0xF, 0x65, 0xA0, 0x0, 0x20)
    Return()

    # Function_79_16303 end

    def Function_80_16351(): pass

    label("Function_80_16351")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_80_16351 end

    def Function_81_163B6(): pass

    label("Function_81_163B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 19200, 500, 21050, 200)
    SetChrPos(0x103, 19200, 500, 21050, 200)
    SetChrPos(0x105, 19200, 500, 21050, 200)
    SetChrPos(0x107, 19200, 500, 21050, 200)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(19200, 1500, 21050, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(17950, 1000, 16250, 4000)
    MoveCamera(315, 30, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_164B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_164B8)
    BeginChrThread(0x101, 1, 0, 82)
    Sleep(1000)

    def lambda_164D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_164D2)
    BeginChrThread(0x103, 1, 0, 83)
    Sleep(1000)

    def lambda_164EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_164EC)
    BeginChrThread(0x105, 1, 0, 84)
    Sleep(1000)

    def lambda_16506():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_16506)
    BeginChrThread(0x107, 1, 0, 85)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0847
    ChrTalk(
        0x105,
        (
            "#10404F#12Pさてと──\x02\x03",

            "#10400Fそれじゃあ古戦場に\x01",
            "行くってことでいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x101,
        (
            "#00006F#6Pああ、その抵抗勢力というのが\x01",
            "何者かは分からないけど。\x02\x03",

            "#00001Fひょっとしたら俺たちとも\x01",
            "連携できるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0x103,
        (
            "#00201F#5Pそうですね……\x01",
            "探ってみる価値はあるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x107,
        "#01200F#11P#3Cならば向かうとしようか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 17950, 0, 16250, 180)
    SetScenarioFlags(0x1A1, 5)
    OP_29(0xAF, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_81_163B6 end

    def Function_82_1669D(): pass

    label("Function_82_1669D")

    OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x101, 17500, 0, 14850, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_82_1669D end

    def Function_83_166C8(): pass

    label("Function_83_166C8")

    OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x103, 16900, 0, 16550, 2000, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_83_166C8 end

    def Function_84_166F3(): pass

    label("Function_84_166F3")

    OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x105, 18950, 0, 16100, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_84_166F3 end

    def Function_85_1671E(): pass

    label("Function_85_1671E")

    OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x107, 18000, 0, 17750, 2000, 0x0)
    OP_93(0x107, 0xB4, 0x1F4)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_85_1671E end

    def Function_86_1674D(): pass

    label("Function_86_1674D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    Call(0, 87)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A0E")
    Fade(500)
    OP_68(15510, 1350, -23710, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16913")
    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x105, 23130, 0, -30790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x103, 20790, 0, -30560, 315)
    SetChrPos(0x109, 22200, 0, -31420, 315)

    def lambda_1684A():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1684A)

    def lambda_16864():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16864)

    def lambda_1687E():
        OP_95(0xFE, 16930, 0, -24390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1687E)

    def lambda_16898():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16898)

    def lambda_168B2():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_168B2)

    def lambda_168CC():
        OP_95(0xFE, 15900, 0, -25220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_168CC)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    Jump("loc_16A09")

    label("loc_16913")

    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x109, 21290, 0, -30060, 315)
    SetChrPos(0x105, 22810, 0, -31000, 315)

    def lambda_1696D():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1696D)

    def lambda_16987():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16987)

    def lambda_169A1():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_169A1)

    def lambda_169BB():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_169BB)

    def lambda_169D5():
        OP_95(0xFE, 16410, 0, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_169D5)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    label("loc_16A09")

    Jump("loc_16E7F")

    label("loc_16A0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C63")
    Fade(500)
    OP_68(17090, 1500, -25640, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x8, 0x13)
    OP_49()
    SetChrPos(0x13, 27180, 0, -35450, 315)
    OP_D5(0x13, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_0D()
    OP_49()
    BeginChrThread(0x28, 1, 0, 88)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_16ABD():
        OP_95(0xFE, 15110, 0, -21470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_16ABD)
    Sleep(3500)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x13, 0x1)
    SetChrPos(0x13, 16500, 0, -18100, 135)
    OP_D5(0x13, 0x0, 0x20F58, 0x0, 0x0)
    OP_71(0x8, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x8)
    SetMapObjFlags(0x8, 0x2)
    OP_66(0x2, 0x1)
    OP_68(12290, 1200, -19990, 0)
    MoveCamera(7, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15300, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16BF5")
    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x105, 13690, 0, -20980, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x103, 11800, 0, -20300, 315)
    SetChrPos(0x109, 12760, 0, -21810, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_16C54")

    label("loc_16BF5")

    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x109, 11800, 0, -20300, 315)
    SetChrPos(0x105, 13220, 0, -21400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_16C54")

    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_16E7F")

    label("loc_16C63")

    Fade(500)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E2(0x1)
    ClearChrFlags(0x12, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x12)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x12, 13270, 0, -22560, 0)
    OP_D5(0x12, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x12, 1, 0, 5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapObjFlags(0x7, 0x4)
    OP_68(1610, 1500, -14250, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, 250, 0, -13500, 0)
    SetChrPos(0x102, 1250, 0, -13500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E16")
    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x105, 2850, 0, -14980, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x103, 960, 0, -14300, 0)
    SetChrPos(0x109, 1920, 0, -15810, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_16E75")

    label("loc_16E16")

    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x109, 960, 0, -14300, 0)
    SetChrPos(0x105, 2380, 0, -15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_16E75")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_16E7F")


    #C0851
    ChrTalk(
        0x105,
        (
            "#12P#10302Fへえ、随分景色のいい場所だね。\x02\x03",

            "#10304F確か、『アルモリカ村』だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x102,
        (
            "#00100Fええ、そうよ。\x02\x03",

            "#00104F養蜂業や農業、牧畜を\x01",
            "主産業とする村……\x02\x03",

            "#00102F《神狼》の伝説が今も残る\x01",
            "数少ない場所でもあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x101,
        (
            "#00004Fそういえば……\x01",
            "特務支援課が一番最初に\x01",
            "市外活動をした場所だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x109,
        (
            "#12P#10100Fマフィアの軍用犬の事件……\x01",
            "ふふ、懐かしいですね。\x02\x03",

            "#10103Fあの時は、あたしたちの調査を\x01",
            "支援課に委任する形に\x01",
            "なってしまったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x104,
        (
            "#00306Fまあ、それもあの無能な元司令が\x01",
            "原因だったんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、ツァイトとも\x01",
            "あの事件以来の付き合いね。\x02\x03",

            "#00104F最後の大ピンチで助けてくれて、\x01",
            "おかげで事件が解決できたのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_171AD")

    #C0857
    ChrTalk(
        0x101,
        (
            "#00009Fあの時からツァイトには\x01",
            "助けられっぱなしだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x103,
        (
            "#6P#00202Fええ、戦闘だけじゃなく\x01",
            "色々な場面でサポートして\x01",
            "もらっていますし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1722C")

    label("loc_171AD")


    #C0859
    ChrTalk(
        0x101,
        (
            "#00009Fあの時からツァイトには\x01",
            "助けられっぱなしだよな。\x02\x03",

            "#00004F戦闘だけじゃなく\x01",
            "色々な場面でサポートして\x01",
            "もらっているし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1722C")


    #C0860
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、助けられっぱなしなのは\x01",
            "ツァイトに限らない気がするけど。\x02\x03",

            "#10309Fむしろ、良い所をとられるのは\x01",
            "支援課の宿命ってヤツだよね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_172C1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_172C1)

    def lambda_172CE():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_172CE)

    def lambda_172DB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_172DB)

    def lambda_172E8():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_172E8)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17385")

    def lambda_17365():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_17365)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_17385")

    Sleep(1000)

    #C0861
    ChrTalk(
        0x109,
        "#6P#10106Fワ、ワジ君……\x02",
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x104,
        "#00306Fったく、痛い所を突きやがんなあ。\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x101,
        (
            "#00012Fま、まあ……\x01",
            "俺たちも成長してきてるはずだし、\x01",
            "それは今後の課題ってことで。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x14E, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17452")
    SetChrPos(0x0, 15500, 0, -23930, 315)
    Jump("loc_17487")

    label("loc_17452")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17476")
    SetChrPos(0x0, 11350, 0, -18420, 315)
    Jump("loc_17487")

    label("loc_17476")

    SetChrPos(0x0, 890, 0, -13080, 315)

    label("loc_17487")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_174AB")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_174AB")

    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_86_1674D end

    def Function_87_174B7(): pass

    label("Function_87_174B7")

    OP_68(-37350, 1500, 69780, 0)
    MoveCamera(338, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(53190, 0)
    OP_68(-21000, 1500, 74410, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(7400, 1500, 48380, 0)
    MoveCamera(323, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37470, 0)
    OP_68(-12130, 1500, 35080, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(-1020, 5100, 4110, 0)
    MoveCamera(338, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44250, 0)
    PlaceName2(340, 40, "c_plac14", 0x0, 3000)
    OP_68(-1020, 2800, 4110, 7000)
    OP_6F(0x1)
    Return()

    # Function_87_174B7 end

    def Function_88_17598(): pass

    label("Function_88_17598")

    Sleep(500)
    Sound(459, 0, 100, 0)
    Sleep(1200)
    Sleep(1500)
    Sound(492, 0, 90, 0)
    Return()

    # Function_88_17598 end

    def Function_89_175AE(): pass

    label("Function_89_175AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E7")
    EventBegin(0x0)
    Fade(1000)
    OP_68(16470, 1500, -26270, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x13, 12610, 0, -12660, 0)
    SetChrPos(0x101, 16690, 0, -26040, 135)
    SetChrPos(0x103, 17490, 0, -25240, 135)
    SetChrPos(0x105, 15690, 0, -25040, 135)
    SetChrPos(0x107, 16490, 0, -24240, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1769C():
        OP_93(0x107, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1769C)
    Sleep(0)

    def lambda_176AC():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_176AC)
    Sleep(0)

    def lambda_176BC():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_176BC)
    Sleep(0)

    def lambda_176CC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_176CC)
    Sleep(0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(12070, 1100, -16020, 0)
    MoveCamera(359, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, 12450, 0, -17250, 0)
    SetChrPos(0x103, 11450, 0, -17250, 0)
    SetChrPos(0x105, 12950, 0, -18450, 0)
    SetChrPos(0x107, 10950, 0, -18450, 0)
    OP_0D()

    #C0864
    ChrTalk(
        0x101,
        (
            "#12P#00000Fこの導力車は……\x01",
            "ハロルドさんの車だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x103,
        (
            "#6P#00200Fヴェルヌ社製の乗用車……\x01",
            "一度乗ったことがありますし、\x01",
            "間違いないと思います。\x02\x03",

            "#00203F村長の話では、宿の２階に\x01",
            "滞在しているとのことでしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x105,
        (
            "#12P#10403F今は一つでも情報が欲しい所だ。\x02\x03",

            "#10400F街道に出る前に\x01",
            "話を聞いておいた方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0867
    ChrTalk(
        0x101,
        "#6P#00000Fああ、行ってみるとしよう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11950, 0, -17850, 0)
    EventEnd(0x5)
    Jump("loc_1795E")

    label("loc_178E7")

    EventBegin(0x1)

    #C0868
    ChrTalk(
        0x101,
        (
            "#00000F村にハロルドさんが\x01",
            "滞在しているらしい。\x02\x03",

            "街道に出る前に、\x01",
            "宿の２階を訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)

    label("loc_1795E")

    Return()

    # Function_89_175AE end

    SaveToFile()

Try(main)
