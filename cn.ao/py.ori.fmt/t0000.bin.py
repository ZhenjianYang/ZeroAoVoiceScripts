from ScenarioHelper import *

def main():
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
        "卡米尤",                 # 1
        "艾尔琴",                 # 2
        "普莉",                   # 3
        "史蒂芬",                 # 4
        "迪利克",                 # 5
        "敏涅斯",                 # 6
        "阿蕾莎",                 # 7
        "索菲亚",                 # 8
        "柯林",                   # 9
        "游击士斯克特",           # 10
        "巴士",                   # 11
        "特别任务支援科车辆",     # 12
        "梅尔卡瓦九号机",         # 13
        "梅尔卡瓦光学迷彩",       # 14
        "梅尔卡瓦影子",           # 15
        "奇斯",                   # 16
        "游击士林",               # 17
        "游击士艾欧莉娅",         # 18
        "安洁",                   # 19
        "格方",                   # 20
        "席莉",                   # 21
        "特鲁塔村长",             # 22
        "皮特",                   # 23
        "哈罗德",                 # 24
        "猫型魔兽",               # 25
        "猫型魔兽",               # 26
        "猫型魔兽",               # 27
        "猫型魔兽",               # 28
        "猫型魔兽",               # 29
        "黑色运输车",             # 30
        "阿鲁姆",                 # 31
        "艾娅莉",                 # 32
        "SE控制",                 # 33
        "bt0000",                 # 34
        "bt0000",                 # 35
        "阿尔摩利卡古道",         # 36
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

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "阿尔摩利卡古道")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2404, 0)                                       # 0

    ScpFunction((
        "Function_0_964",          # 00, 0
        "Function_1_A1C",          # 01, 1
        "Function_2_12CF",         # 02, 2
        "Function_3_175B",         # 03, 3
        "Function_4_1843",         # 04, 4
        "Function_5_1956",         # 05, 5
        "Function_6_198C",         # 06, 6
        "Function_7_19DD",         # 07, 7
        "Function_8_1A71",         # 08, 8
        "Function_9_2D60",         # 09, 9
        "Function_10_3644",        # 0A, 10
        "Function_11_383C",        # 0B, 11
        "Function_12_3CC1",        # 0C, 12
        "Function_13_4331",        # 0D, 13
        "Function_14_49DD",        # 0E, 14
        "Function_15_4AD5",        # 0F, 15
        "Function_16_4B85",        # 10, 16
        "Function_17_4CD6",        # 11, 17
        "Function_18_4D86",        # 12, 18
        "Function_19_4E14",        # 13, 19
        "Function_20_5105",        # 14, 20
        "Function_21_522A",        # 15, 21
        "Function_22_52E5",        # 16, 22
        "Function_23_5612",        # 17, 23
        "Function_24_564C",        # 18, 24
        "Function_25_5714",        # 19, 25
        "Function_26_5956",        # 1A, 26
        "Function_27_6AC4",        # 1B, 27
        "Function_28_7E40",        # 1C, 28
        "Function_29_800C",        # 1D, 29
        "Function_30_A7A0",        # 1E, 30
        "Function_31_A8B4",        # 1F, 31
        "Function_32_A8D1",        # 20, 32
        "Function_33_AD11",        # 21, 33
        "Function_34_B64C",        # 22, 34
        "Function_35_10DE0",       # 23, 35
        "Function_36_10E14",       # 24, 36
        "Function_37_10E48",       # 25, 37
        "Function_38_10E7C",       # 26, 38
        "Function_39_10EB0",       # 27, 39
        "Function_40_10EE4",       # 28, 40
        "Function_41_10F18",       # 29, 41
        "Function_42_10F4C",       # 2A, 42
        "Function_43_10F80",       # 2B, 43
        "Function_44_10FB4",       # 2C, 44
        "Function_45_10FE8",       # 2D, 45
        "Function_46_1101C",       # 2E, 46
        "Function_47_11050",       # 2F, 47
        "Function_48_11084",       # 30, 48
        "Function_49_110B8",       # 31, 49
        "Function_50_110EC",       # 32, 50
        "Function_51_11114",       # 33, 51
        "Function_52_11137",       # 34, 52
        "Function_53_111AC",       # 35, 53
        "Function_54_11235",       # 36, 54
        "Function_55_112AA",       # 37, 55
        "Function_56_11333",       # 38, 56
        "Function_57_113A8",       # 39, 57
        "Function_58_113F3",       # 3A, 58
        "Function_59_1143E",       # 3B, 59
        "Function_60_11489",       # 3C, 60
        "Function_61_114D4",       # 3D, 61
        "Function_62_1151F",       # 3E, 62
        "Function_63_1157E",       # 3F, 63
        "Function_64_11598",       # 40, 64
        "Function_65_1186B",       # 41, 65
        "Function_66_11CDC",       # 42, 66
        "Function_67_12277",       # 43, 67
        "Function_68_122A5",       # 44, 68
        "Function_69_122E7",       # 45, 69
        "Function_70_12329",       # 46, 70
        "Function_71_1236B",       # 47, 71
        "Function_72_123AD",       # 48, 72
        "Function_73_123EF",       # 49, 73
        "Function_74_12431",       # 4A, 74
        "Function_75_12AC2",       # 4B, 75
        "Function_76_12B04",       # 4C, 76
        "Function_77_139DA",       # 4D, 77
        "Function_78_13F28",       # 4E, 78
        "Function_79_13F6D",       # 4F, 79
        "Function_80_13FBB",       # 50, 80
        "Function_81_14020",       # 51, 81
        "Function_82_142C3",       # 52, 82
        "Function_83_142EE",       # 53, 83
        "Function_84_14319",       # 54, 84
        "Function_85_14344",       # 55, 85
        "Function_86_14373",       # 56, 86
        "Function_87_1505D",       # 57, 87
        "Function_88_1513E",       # 58, 88
        "Function_89_15154",       # 59, 89
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
            "#1K这里是巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市东口\x01",      # 0
            "唐古拉姆门\x01",            # 1
            "停靠站（三岔路）\x01",      # 2
            "放弃\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F6")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_183B")

    label("loc_17F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181B")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_183B")

    label("loc_181B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183B")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_183B")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_3_175B end

    def Function_4_1843(): pass

    label("Function_4_1843")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1952")
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

    label("loc_1952")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_4_1843 end

    def Function_5_1956(): pass

    label("Function_5_1956")

    OP_95(0x12, 10630, 0, -20520, 4000, 0x0)
    OP_9E(0x12, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xFA0, 0x1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_5_1956 end

    def Function_6_198C(): pass

    label("Function_6_198C")

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

    # Function_6_198C end

    def Function_7_19DD(): pass

    label("Function_7_19DD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1A38")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A2D")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1A33")

    label("loc_1A2D")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1A33")

    Jump("loc_1A5C")

    label("loc_1A38")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A56")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1A5C")

    label("loc_1A56")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1A5C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_19DD end

    def Function_8_1A71(): pass

    label("Function_8_1A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B34")

    #C0002
    ChrTalk(
        0x9,
        (
            "吓、吓死人了……\x01",
            "那棵大树究竟是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "突然出现了那种东西，\x01",
            "无论怎么想也不正常啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "难道已经回不到以前那种\x01",
            "可以开心驾驶导力车的生活了吗……！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BAC")

    label("loc_1B34")


    #C0005
    ChrTalk(
        0x9,
        (
            "突然出现了那种东西，\x01",
            "克洛斯贝尔究竟会怎么样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "难道已经回不到以前那种\x01",
            "可以开心驾驶导力车的生活了吗……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAC")

    Jump("loc_2D5C")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C68")

    #C0007
    ChrTalk(
        0x9,
        (
            "独立无效宣言\x01",
            "已经发表了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "其实我还是更喜欢原来那个可以\x01",
            "驾驶导力车自由兜风的克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "我并不懂什么独立不独立，\x01",
            "只希望能恢复\x01",
            "原来的生活。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D00")

    label("loc_1C68")


    #C0010
    ChrTalk(
        0x9,
        (
            "和所谓的独立国家相比，\x01",
            "我还是更喜欢原来那个可以\x01",
            "驾驶导力车自由兜风的克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "无效宣言好像已经发表了，\x01",
            "希望克洛斯贝尔可以\x01",
            "恢复原来的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D00")

    Jump("loc_2D5C")

    label("loc_1D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1EB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E07")

    #C0012
    ChrTalk(
        0x9,
        (
            "在禁行令的限制下，\x01",
            "几乎都看不到巴士和导力车来村里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "偶尔开到村里来的国防军\x01",
            "装甲车虽然很威风……\x01",
            "但老实说，我真是已经看腻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "因为出现了什么『幻兽』，\x01",
            "现在都不能随意出去兜风了……\x01",
            "这种状态究竟要持续到什么时候啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EB3")

    label("loc_1E07")


    #C0015
    ChrTalk(
        0x9,
        (
            "在禁行令的限制下，\x01",
            "现在来村里的导力车只有\x01",
            "偶尔才来一次的国防军装甲车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "因为出现了什么『幻兽』，\x01",
            "现在都不能随意出去兜风了……\x01",
            "这种状态究竟要持续到什么时候啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB3")

    Jump("loc_2D5C")

    label("loc_1EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F28")

    #C0017
    ChrTalk(
        0xFE,
        (
            "发生了那样的袭击事件，\x01",
            "都有些不敢出村了……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "但正是在这种时候，\x01",
            "我们才更要努力保卫村子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5C")

    label("loc_1F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F36")
    Jump("loc_2D5C")

    label("loc_1F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_221A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")

    #C0019
    ChrTalk(
        0xFE,
        (
            "迪利克和敏涅斯先生的计划\x01",
            "似乎进展得相当顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "这个村子将会\x01",
            "发展成什么样子呢……\x01",
            "呵呵，真是太期待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2215")

    label("loc_1FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CA")

    #C0021
    ChrTalk(
        0xFE,
        (
            "呼，敏涅斯先生\x01",
            "竟然是个诈骗犯……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "那个……我从他那里\x01",
            "买下的这辆导力车……\x01",
            "你们觉得应该怎样处理？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x109,
        (
            "#10101F记得之前听你说过，\x01",
            "只花了五万米拉就从他手中买下了\x01",
            "市价在五十万米拉左右的导力卡车。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#00003F嗯～这个……\x01",
            "的确是个很微妙的问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#00100F我认为还是\x01",
            "先把车交给警察，\x01",
            "由他们来裁定比较好。\x02\x03",

            "#00104F因为你算是通过正规交易方式购买的，\x01",
            "应该马上就会返还给你……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        (
            "#00200F说的对呢，为了调查一下车辆本身的\x01",
            "合法性，也还是先交给警察比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "这样啊……\x01",
            "也好，那就和警察联络一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 7)
    Jump("loc_2215")

    label("loc_21CA")


    #C0028
    ChrTalk(
        0xFE,
        (
            "毕竟是从诈骗犯手中\x01",
            "买到的新型卡车……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "呼，还是和警察联络一下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2215")

    Jump("loc_2D5C")

    label("loc_221A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2415")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E3")

    #C0030
    ChrTalk(
        0xFE,
        (
            "迪利克为了和\x01",
            "敏涅斯先生会面，\x01",
            "留在市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "现在大概正在欢乐街\x01",
            "的酒店里谈话吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……嗯，先不管那些了～\x01",
            "难得买到了最新型的车，\x01",
            "必须要好好检修保养。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_231B")

    label("loc_22E3")


    #C0033
    ChrTalk(
        0xFE,
        (
            "迪利克现在应该在\x01",
            "欢乐街的酒店里\x01",
            "和敏涅斯先生谈话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231B")

    Jump("loc_2410")

    label("loc_2320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B7")

    #C0034
    ChrTalk(
        0xFE,
        (
            "敏涅斯先生真是个\x01",
            "慷慨大方的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "不愧是在大型糕点\x01",
            "公司——昆西公司\x01",
            "任职的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "我们一定要全力\x01",
            "支持他和迪利克\x01",
            "的计划。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2410")

    label("loc_23B7")


    #C0037
    ChrTalk(
        0xFE,
        (
            "敏涅斯先生真是个\x01",
            "慷慨大方的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "不愧是在大型糕点\x01",
            "公司——昆西公司\x01",
            "任职的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2410")

    Jump("loc_2D5C")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_270C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_END)), "loc_2583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CA")

    #C0039
    ChrTalk(
        0xFE,
        (
            "哎……\x01",
            "私有地的锁被打开了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "呼，是吗……\x01",
            "怎么会有这种\x01",
            "爱给人添麻烦的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "多谢你们过来告诉我。\x01",
            "稍后我会开车过去\x01",
            "把它锁上的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_257E")

    label("loc_24CA")


    #C0042
    ChrTalk(
        0xFE,
        (
            "私有地的锁……\x01",
            "稍后我会开车过去\x01",
            "把它锁上的。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "……呼，说实话，\x01",
            "卡车最近常出故障，\x01",
            "驾驶时真是很发愁。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "可是村子并没有购买新卡车\x01",
            "的预算费用……\x01",
            "也只能想办法修理一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257E")

    Jump("loc_2707")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2653")

    #C0045
    ChrTalk(
        0xFE,
        (
            "在阿尔摩利卡古道的中途，\x01",
            "有一块由村子管理的私有地。\x01",
            "我刚从那里回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "那里是保管农具\x01",
            "和材料的地方，\x01",
            "一般人不能随意入内哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "为了防止有人进去，\x01",
            "平时都会上着锁，\x01",
            "所以应该没问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2707")

    label("loc_2653")


    #C0048
    ChrTalk(
        0xFE,
        (
            "在阿尔摩利卡古道的中途，\x01",
            "有一块由村子管理的私有地。\x01",
            "我刚从那里回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "……说起来，村里来了\x01",
            "一位外国的客人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "这辆黑色的运输车是他的吧？\x01",
            "看起来好像是非常高级的车……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2707")

    Jump("loc_2D5C")

    label("loc_270C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_296F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278E")

    #C0051
    ChrTalk(
        0x9,
        (
            "我看了你们的特训，\x01",
            "刚才那招战技\x01",
            "真厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "之前的比赛也很精彩，\x01",
            "不愧是游击士啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F6")

    label("loc_278E")


    #C0053
    ChrTalk(
        0x9,
        (
            "啊～看了你们刚才的比赛，\x01",
            "我直到现在还在兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "呵呵，以后还要让我欣赏\x01",
            "你们和游击士的较量哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F6")

    Jump("loc_296A")

    label("loc_27FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291D")

    #C0055
    ChrTalk(
        0x9,
        (
            "我只要一兴奋，\x01",
            "就会不自觉地说起方言。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "说方言太土了，完全没有现代年轻人的样子，\x01",
            "所以我一直都想努力改正……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "为了这个问题，我还去和米莉亚姐姐商量过，\x01",
            "但她却说『不必在意这种事』。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "哼，其实就是事不关己罢了……\x01",
            "如果不改掉说方言的习惯，谁都能看出我是乡下人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_296A")

    label("loc_291D")


    #C0059
    ChrTalk(
        0xFE,
        (
            "米莉亚姐姐让我不要介意\x01",
            "说方言的习惯。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "哼，其实就是事不关己罢了……\x02",
    )

    CloseMessageWindow()

    label("loc_296A")

    Jump("loc_2D5C")

    label("loc_296F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D5C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B15")

    #C0061
    ChrTalk(
        0x9,
        "哦，欢迎来到阿尔摩利卡村。\x02",
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
            "嗯……？\x01",
            "那、那辆导力车是……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "既不是乌尔努公司制造的，\x01",
            "也不是莱恩福尔特公司制造的……\x01",
            "我还是第一次见到这种车呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#10104F呵呵，这辆车是蔡斯中央工房制造的。\x02\x03",

            "#10102F由于装载了新型引擎，\x01",
            "最高时速可以达到\x01",
            "１５００赛尔矩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "什么～！？\x01",
            "那可真是太棒了啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00012F（诺艾尔好像很自豪呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 5)
    Jump("loc_2C4F")

    label("loc_2B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDF")

    #C0067
    ChrTalk(
        0x9,
        (
            "最高时速１５００赛尔矩……\x01",
            "蔡斯中央工房竟然也造出了\x01",
            "这么棒的车啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "真好啊，真好啊！\x01",
            "俺也很想要辆\x01",
            "新型导力卡车呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "……咳咳。\x01",
            "哎呀，只要一激动，\x01",
            "就会忍不住说出方言。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C4F")

    label("loc_2BDF")


    #C0070
    ChrTalk(
        0x9,
        (
            "……说起来，前一阵子的\x01",
            "那些怪人究竟是做什么的……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "算了，做什么都无所谓，\x01",
            "只要别影响我的驾车生活就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4F")

    Jump("loc_2D5C")

    label("loc_2C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEC")

    #C0072
    ChrTalk(
        0x9,
        "哦，欢迎来到阿尔摩利卡村。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "我们村子主要从事养蜂业、\x01",
            "农业和畜牧业。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "这里的视野也很不错，\x01",
            "如果有兴趣，不妨多待一阵子吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D5C")

    label("loc_2CEC")


    #C0075
    ChrTalk(
        0x9,
        (
            "……说起来，前一阵子的\x01",
            "那些怪人究竟是做什么的……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "算了，做什么都无所谓，\x01",
            "只要别影响我的驾车生活就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5C")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A71 end

    def Function_9_2D60(): pass

    label("Function_9_2D60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE4")

    #C0077
    ChrTalk(
        0x8,
        (
            "虽然大人们都很惊慌……\x01",
            "不过那棵树实在是很棒啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "要是能爬上那样巨大的树，\x01",
            "一定会非常开心吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E3E")

    label("loc_2DE4")


    #C0079
    ChrTalk(
        0x8,
        (
            "要是能爬上那样巨大的树，\x01",
            "一定会非常开心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "说不定还能在上面捉到\x01",
            "超大的甲虫呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3E")

    Jump("loc_3640")

    label("loc_2E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0D")

    #C0081
    ChrTalk(
        0x8,
        (
            "好，今天就来玩\x01",
            "踢罐捉迷藏吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    #C0082
    ChrTalk(
        0x10,
        (
            "#03805F踢罐捉迷藏～？\x01",
            "那是什么～？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "哎，你连踢罐捉迷藏都不懂吗！？\x01",
            "真没办法啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "那个……基本规则\x01",
            "和捉迷藏差不多……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0x10, 0xFF)
    Jump("loc_2F8C")

    label("loc_2F0D")


    #C0085
    ChrTalk(
        0x8,
        (
            "然后呢，趁鬼不在罐子附近的时候，\x01",
            "把这个罐子……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    #C0086
    ChrTalk(
        0x10,
        (
            "#03809F我知道～踩扁之后\x01",
            "丢进垃圾箱里吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        "才、才不是～\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_2F8C")

    Jump("loc_3640")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_308E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3039")

    #C0088
    ChrTalk(
        0x8,
        (
            "不久前，哈罗德叔叔\x01",
            "带着孩子一起来村里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "唔……如果有个弟弟，\x01",
            "大概就是这种感觉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "我的年纪比柯林大，\x01",
            "一定要好好照顾他才行！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3089")

    label("loc_3039")


    #C0091
    ChrTalk(
        0x8,
        (
            "哈罗德叔叔要是\x01",
            "也搬到村里住就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "那样我就可以\x01",
            "一直和柯林一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3089")

    Jump("loc_3640")

    label("loc_308E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316B")

    #C0093
    ChrTalk(
        0x8,
        (
            "听说就在不久前，有一群可怕的家伙\x01",
            "在克洛斯贝尔市发起了暴乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "我住在这个村子，平时一直都很无聊，\x01",
            "所以总希望能发生一些\x01",
            "特别的事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "但像那样的袭击事件，\x01",
            "无论如何也不希望发生啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31CB")

    label("loc_316B")


    #C0096
    ChrTalk(
        0x8,
        (
            "我以前一直都觉得这村子\x01",
            "太和平了，简直无聊……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "现在想想，这种生活也许\x01",
            "才是最可贵的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CB")

    Jump("loc_3640")

    label("loc_31D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31DE")
    Jump("loc_3640")

    label("loc_31DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_332E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323C")

    #C0098
    ChrTalk(
        0x8,
        "啊啊，今天好无聊。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "村里就不能发生些\x01",
            "振奋人心的大事件吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3329")

    label("loc_323C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D6")

    #C0100
    ChrTalk(
        0x8,
        (
            "哇哇，刚才真是好精彩啊！\x01",
            "突然窜出了那么大的猫！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "那个叔叔莫非是\x01",
            "哪个马戏团的\x01",
            "驯兽师吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "哇，要是事先找他\x01",
            "要个签名就好了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3329")

    label("loc_32D6")


    #C0103
    ChrTalk(
        0x8,
        (
            "那个叔叔莫非是\x01",
            "哪个马戏团的\x01",
            "驯兽师吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "哇，要是事先找他\x01",
            "要个签名就好了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3329")

    Jump("loc_3640")

    label("loc_332E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D7")

    #C0105
    ChrTalk(
        0x8,
        (
            "最近经常来村里的\x01",
            "那个外国人叔叔\x01",
            "送了点心给我们吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "我做了失礼的事，\x01",
            "本来还以为他会发怒……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "嘿嘿，世界上竟然\x01",
            "还有这么亲切的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3454")

    label("loc_33D7")


    #C0108
    ChrTalk(
        0x8,
        (
            "我对那个外国人叔叔做了失礼的事，\x01",
            "可他不但没生气，\x01",
            "还给我点心吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "……不过，之后被妈妈发现了，\x01",
            "她狠狠骂了我一顿呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3454")

    Jump("loc_3640")

    label("loc_3459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3474")
    Call(0, 10)
    Jump("loc_34DA")

    label("loc_3474")


    #C0110
    ChrTalk(
        0x8,
        (
            "嗯……虽然都是捉迷藏，\x01",
            "但规则却有些细微的区别呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "那今天就玩史蒂芬的\x01",
            "克洛斯贝尔式捉迷藏吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DA")

    Jump("loc_3640")

    label("loc_34DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_353A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FA")
    Call(0, 10)
    Jump("loc_3535")

    label("loc_34FA")


    #C0112
    ChrTalk(
        0x8,
        (
            "是吗，市里还有那么\x01",
            "壮观的建筑物啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "真想去探险～\x02",
    )

    CloseMessageWindow()

    label("loc_3535")

    Jump("loc_3640")

    label("loc_353A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F1")

    #C0114
    ChrTalk(
        0x8,
        (
            "啧，这个村子实在太和平了，\x01",
            "真是无聊啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "说起最近的新闻，\x01",
            "也无非就是『牧场的牛生了小牛』\x01",
            "之类的琐碎小事。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "唉唉，怎么就不能\x01",
            "发生一些大事件呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3640")

    label("loc_35F1")


    #C0117
    ChrTalk(
        0x8,
        (
            "虽然小牛\x01",
            "确实很可爱……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "但我期待的大事件\x01",
            "可不是这种\x01",
            "温馨的小事情啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3640")

    TalkEnd(0xFE)
    Return()

    # Function_9_2D60 end

    def Function_10_3644(): pass

    label("Function_10_3644")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_372D")

    #C0119
    ChrTalk(
        0x8,
        (
            "好，那就来玩\x01",
            "捉迷藏吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "鬼绝对不能\x01",
            "爬到高处哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        "普莉当鬼就好！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "哎？不是只要\x01",
            "在三秒之内，\x01",
            "爬到高处也可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "……那是什么规则啊，\x01",
            "我还是第一次听到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "喂喂，\x01",
            "普莉当鬼就好！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jump("loc_382C")

    label("loc_372D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_382C")

    #C0125
    ChrTalk(
        0xB,
        (
            "说起来，\x01",
            "市里今天好像要举办\x01",
            "兰花塔的揭幕式呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "兰花塔？\x01",
            "那是什么，能吃吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        "是点心吗？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "不不，不是啦，\x01",
            "是个超大的建筑物哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "据说，只要站在楼顶上，\x01",
            "可以俯瞰\x01",
            "整个克洛斯贝尔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "哎，好厉害啊！\x01",
            "真想去看看。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)

    label("loc_382C")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_3644 end

    def Function_11_383C(): pass

    label("Function_11_383C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3898")

    #C0131
    ChrTalk(
        0xA,
        (
            "柯林和\x01",
            "哈罗德叔叔\x01",
            "一起回市里了～\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "他和我约定好了，\x01",
            "以后还会来玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBD")

    label("loc_3898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_39B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3953")

    #C0133
    ChrTalk(
        0xA,
        (
            "哥哥光和\x01",
            "柯林一起玩，\x01",
            "我好无聊啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "但妈妈说，\x01",
            "我是小姐姐，\x01",
            "所以要让着柯林。\x02",
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
            "我会让着柯林的。\x01",
            "……因为我是小姐姐嘛¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39AE")

    label("loc_3953")


    #C0136
    ChrTalk(
        0xA,
        (
            "我的年纪\x01",
            "比柯林稍大～\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "所以就算被哥哥冷落，\x01",
            "我也会忍耐的。\x01",
            "……因为我是小姐姐嘛¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AE")

    Jump("loc_3CBD")

    label("loc_39B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A0B")

    #C0138
    ChrTalk(
        0xA,
        (
            "哥哥最近\x01",
            "只和柯林\x01",
            "一起玩～\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "明明是我的\x01",
            "哥哥嘛……\x01",
            "柯林太狡猾了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBD")

    label("loc_3A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5D")

    #C0140
    ChrTalk(
        0xA,
        (
            "史蒂芬好像已经\x01",
            "回到村里了～\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "赶快来找我玩吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AAE")

    label("loc_3A5D")


    #C0142
    ChrTalk(
        0xA,
        (
            "最近这段时间，\x01",
            "只能和哥哥\x01",
            "两人一起玩～\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "果然还是加上史蒂芬\x01",
            "更有意思啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AAE")

    Jump("loc_3CBD")

    label("loc_3AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3AC1")
    Jump("loc_3CBD")

    label("loc_3AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AFD")

    #C0144
    ChrTalk(
        0xA,
        (
            "普莉想玩扮演\x01",
            "游击士的游戏！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B63")

    label("loc_3AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B44")

    #C0145
    ChrTalk(
        0xA,
        (
            "喵喵，\x01",
            "好大的猫咪啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        "不过并不是很可爱呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B63")

    label("loc_3B44")


    #C0147
    ChrTalk(
        0xA,
        (
            "普莉还是更喜欢\x01",
            "小的猫咪～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B63")

    Jump("loc_3CBD")

    label("loc_3B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3BCA")

    #C0148
    ChrTalk(
        0xA,
        (
            "哥哥前段时间\x01",
            "被妈妈\x01",
            "打了屁股呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "嘿嘿嘿，\x01",
            "他的屁股被打得像\x01",
            "苹果一样通红～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBD")

    label("loc_3BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE5")
    Call(0, 10)
    Jump("loc_3BFE")

    label("loc_3BE5")


    #C0150
    ChrTalk(
        0xA,
        (
            "普莉当鬼\x01",
            "可以吗！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFE")

    Jump("loc_3CBD")

    label("loc_3C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1E")
    Call(0, 10)
    Jump("loc_3C4A")

    label("loc_3C1E")


    #C0151
    ChrTalk(
        0xA,
        (
            "和骑在哥哥的\x01",
            "脖子上相比，\x01",
            "哪个更高呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4A")

    Jump("loc_3CBD")

    label("loc_3C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3CBD")

    #C0152
    ChrTalk(
        0xA,
        (
            "因为有哥哥在，\x01",
            "所以普莉从来\x01",
            "都不会觉得无聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "史蒂芬最近也开始和\x01",
            "我们一起玩了，所以很开心～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBD")

    TalkEnd(0xFE)
    Return()

    # Function_11_383C end

    def Function_12_3CC1(): pass

    label("Function_12_3CC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6F")

    #C0154
    ChrTalk(
        0xB,
        (
            "嗯……发生了这么严重\x01",
            "的大事件……\x01",
            "这么轻松真的好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "算啦，这也是他们两人\x01",
            "的优点。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "但为了应对意外情况，\x01",
            "就由我来负责保持警觉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3DEE")

    label("loc_3D6F")


    #C0157
    ChrTalk(
        0xB,
        (
            "他们两人的优点就是\x01",
            "无论到什么时候都很轻松……\x01",
            "但这次的事件真是很严重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "为了应对意外情况，\x01",
            "就由我来负责保持警觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DEE")

    Jump("loc_432D")

    label("loc_3DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E88")

    #C0159
    ChrTalk(
        0xB,
        (
            "柯林有些时候\x01",
            "还真是让人很不放心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xB,
        (
            "刚才他说觉得蓝花很漂亮，\x01",
            "直接就向村外跑去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        "我们可得仔细看好他才行。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3ECF")

    label("loc_3E88")


    #C0162
    ChrTalk(
        0xB,
        (
            "柯林有些时候\x01",
            "还真是让人很不放心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        "我们可得仔细看好他才行。\x02",
    )

    CloseMessageWindow()

    label("loc_3ECF")

    Jump("loc_432D")

    label("loc_3ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3F5D")

    #C0164
    ChrTalk(
        0xB,
        (
            "哈罗德先生他们\x01",
            "暂住在『白蜡亭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "我和妈妈刚搬到村里的时候，\x01",
            "也受到了大家的不少照顾，\x01",
            "这个村子的人真是很热情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432D")

    label("loc_3F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F6B")
    Jump("loc_432D")

    label("loc_3F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F79")
    Jump("loc_432D")

    label("loc_3F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4073")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC3")

    #C0166
    ChrTalk(
        0xB,
        (
            "真是的，扮演游击士的游戏\x01",
            "我已经玩腻了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_406E")

    label("loc_3FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4028")

    #C0167
    ChrTalk(
        0xB,
        (
            "那个叔叔果然\x01",
            "是个坏蛋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "竟然在村子里\x01",
            "放出魔兽……\x01",
            "我还以为会被吃掉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_406E")

    label("loc_4028")


    #C0169
    ChrTalk(
        0xB,
        (
            "话说回来，差点就要\x01",
            "遭到魔兽的袭击了，\x01",
            "这对兄妹却还是这么轻松……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_406E")

    Jump("loc_432D")

    label("loc_4073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40F0")

    #C0170
    ChrTalk(
        0xB,
        (
            "不知道为什么，\x01",
            "我就是不太喜欢那个叔叔。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "虽然他一直都面带微笑，\x01",
            "待人温和，但总觉得\x01",
            "他的眼睛没有笑……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432D")

    label("loc_40F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_416D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410B")
    Call(0, 10)
    Jump("loc_4168")

    label("loc_410B")


    #C0172
    ChrTalk(
        0xB,
        (
            "在克洛斯贝尔市，\x01",
            "鬼可以在三秒之内\x01",
            "爬到高处去。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "这应该算是一种\x01",
            "地方性的游戏规则吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4168")

    Jump("loc_432D")

    label("loc_416D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4188")
    Call(0, 10)
    Jump("loc_41FA")

    label("loc_4188")


    #C0174
    ChrTalk(
        0xB,
        (
            "嗯……\x01",
            "以前一直都盖着那么大的帷幕，\x01",
            "就算不知道也不奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "揭开了那样巨大的帷幕，\x01",
            "市里应该\x01",
            "非常热闹吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FA")

    Jump("loc_432D")

    label("loc_41FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_432D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D0")

    #C0176
    ChrTalk(
        0xB,
        (
            "我以前和妈妈\x01",
            "一起住在\x01",
            "克洛斯贝尔市……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "自从搬到阿尔摩利卡村之后，\x01",
            "好像每天都能遇到一些\x01",
            "新鲜事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "我一开始为什么会\x01",
            "那么讨厌这里呢，\x01",
            "真是连自己都不明白啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0x6B, 0x0)
    Jump("loc_432D")

    label("loc_42D0")


    #C0179
    ChrTalk(
        0xB,
        (
            "能亲眼看到小牛\x01",
            "的出生，\x01",
            "真是好棒啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "不过，既然住在村子里，\x01",
            "这也没什么好奇怪的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432D")

    TalkEnd(0xFE)
    Return()

    # Function_12_3CC1 end

    def Function_13_4331(): pass

    label("Function_13_4331")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4342")
    Jump("loc_49D9")

    label("loc_4342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_445E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4401")

    #C0181
    ChrTalk(
        0xC,
        (
            "独立无效宣言吗……\x01",
            "由于这个村子远离市区，\x01",
            "所以几乎没有受到影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "不过，由于事态的急剧变化，\x01",
            "也有不少村民感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "还是要一家一家地\x01",
            "去村民家拜访啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4459")

    label("loc_4401")


    #C0184
    ChrTalk(
        0xC,
        (
            "由于事态的急剧变化，\x01",
            "有不少村民都感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "还是要一家一家地\x01",
            "去村民家拜访啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4459")

    Jump("loc_49D9")

    label("loc_445E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_45CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4537")

    #C0186
    ChrTalk(
        0xC,
        (
            "那种诡异的蓝花……\x01",
            "从不久前开始，\x01",
            "就在花田里盛开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "我担心它会影响到其它花的生长，\x01",
            "就尝试着把它拔掉……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "但无论拔掉多少次，也都会再长出来。\x01",
            "可恶！事到如今，我已经束手无策了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_45CA")

    label("loc_4537")


    #C0189
    ChrTalk(
        0xC,
        (
            "对村子来说，这片花田\x01",
            "是很重要的地方，\x01",
            "所以很想把那些蓝花处理掉……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        (
            "但无论拔掉多少次，也都会再长出来。\x01",
            "可恶！事到如今，我已经束手无策了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CA")

    Jump("loc_49D9")

    label("loc_45CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A3")

    #C0191
    ChrTalk(
        0xC,
        (
            "自从市里发生了袭击事件以来，\x01",
            "我们就开始轮流在\x01",
            "村子的周边巡视了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        (
            "都已经发生了那样的事情，\x01",
            "今后无论再发生什么\x01",
            "也都不足为奇了……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xC,
        (
            "总之，为了村子的安全，\x01",
            "必须要尽力而为啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_46F3")

    label("loc_46A3")


    #C0194
    ChrTalk(
        0xC,
        (
            "我们开始轮流在\x01",
            "村子的周边巡视了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "为了村子的安全，\x01",
            "必须要尽力而为啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46F3")

    Jump("loc_49D9")

    label("loc_46F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4706")
    Jump("loc_49D9")

    label("loc_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4714")
    Jump("loc_49D9")

    label("loc_4714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4722")
    Jump("loc_49D9")

    label("loc_4722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4730")
    Jump("loc_49D9")

    label("loc_4730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_488E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480F")

    #C0196
    ChrTalk(
        0xC,
        (
            "为了阿尔摩利卡村的未来，\x01",
            "我昨天也向村长提出了\x01",
            "各种改革方案……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xC,
        (
            "但全部都被否决了。\x01",
            "最后还是像平时一样，\x01",
            "以一番争执而收场。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xC,
        (
            "我爸爸……村长他\x01",
            "难道就感觉不到\x01",
            "阿尔摩利卡村如今的危机吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4889")

    label("loc_480F")


    #C0199
    ChrTalk(
        0xC,
        (
            "我昨天提出了\x01",
            "很多改革方案……\x01",
            "但村长一个也没有采纳。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        (
            "我爸爸……村长他\x01",
            "难道就感觉不到\x01",
            "阿尔摩利卡村如今的危机吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4889")

    Jump("loc_49D9")

    label("loc_488E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_49D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4966")

    #C0201
    ChrTalk(
        0xC,
        (
            "最近这段时间，无论是农业\x01",
            "还是畜牧业，状况都不容乐观。\x01",
            "村子的财政问题很严峻。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xC,
        (
            "可是我爸爸……村长他却\x01",
            "仍然坚持着自己那套\x01",
            "保守的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "……身为下一任村长，\x01",
            "我必须做些什么才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_49D9")

    label("loc_4966")


    #C0204
    ChrTalk(
        0xC,
        (
            "为了阿尔摩利卡村的未来，\x01",
            "绝对不能安于现状，\x01",
            "被传统观念所束缚。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        (
            "……身为下一任村长，\x01",
            "我必须做些什么才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D9")

    TalkEnd(0xFE)
    Return()

    # Function_13_4331 end

    def Function_14_49DD(): pass

    label("Function_14_49DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A84")

    #N0206
    NpcTalk(
        0xD,
        "打扮讲究的男性",
        (
            "这里就是阿尔摩利卡村啊……\x01",
            "果然和我了解的一样，\x01",
            "是个很不错的村子呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0207
    NpcTalk(
        0xD,
        "打扮讲究的男性",
        (
            "呵呵，那就赶快\x01",
            "开始工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4AD1")

    label("loc_4A84")


    #N0208
    NpcTalk(
        0xD,
        "打扮讲究的男性",
        (
            "赶快开始\x01",
            "工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0209
    NpcTalk(
        0xD,
        "打扮讲究的男性",
        "嗯，村长家是在……\x02",
    )

    CloseMessageWindow()

    label("loc_4AD1")

    TalkEnd(0xFE)
    Return()

    # Function_14_49DD end

    def Function_15_4AD5(): pass

    label("Function_15_4AD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4AE6")
    Jump("loc_4B81")

    label("loc_4AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B01")
    Call(0, 16)
    Jump("loc_4B73")

    label("loc_4B01")


    #C0210
    ChrTalk(
        0xE,
        (
            "呵呵，索菲亚夫人\x01",
            "总是对柯林\x01",
            "那么牵肠挂肚。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xE,
        (
            "其实不用这么担心啦，\x01",
            "小孩子只有在跌跌撞撞中\x01",
            "才能得到成长呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B73")

    Jump("loc_4B81")

    label("loc_4B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4B81")

    label("loc_4B81")

    TalkEnd(0xFE)
    Return()

    # Function_15_4AD5 end

    def Function_16_4B85(): pass

    label("Function_16_4B85")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0212
    ChrTalk(
        0xF,
        "#03708F柯林……不要紧吧……（惊慌不安）\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xE,
        (
            "呵呵，索菲亚夫人，\x01",
            "不用那么担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        (
            "我以前也是这样，\x01",
            "觉得史蒂芬是个娇弱的都市孩子，\x01",
            "一直对他牵肠挂肚……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xE,
        (
            "但为了让孩子健康成长，\x01",
            "还是应该适当放他们\x01",
            "自由玩耍。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)

    #C0216
    ChrTalk(
        0xF,
        (
            "#03700F说、说的也是呢。\x01",
            "如果我总是过度保护，\x01",
            "柯林恐怕也不会快乐的……\x02",
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

    # Function_16_4B85 end

    def Function_17_4CD6(): pass

    label("Function_17_4CD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CE7")
    Jump("loc_4D82")

    label("loc_4CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D02")
    Call(0, 16)
    Jump("loc_4D66")

    label("loc_4D02")


    #C0217
    ChrTalk(
        0xF,
        (
            "#03700F……我原来的过度保护\x01",
            "说不定是错误的教育方式。\x02\x03",

            "#03709F看柯林现在的样子，\x01",
            "好像很快乐呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D66")

    Jump("loc_4D82")

    label("loc_4D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_4D79")
    Jump("loc_4D82")

    label("loc_4D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4D82")

    label("loc_4D82")

    TalkEnd(0xFE)
    Return()

    # Function_17_4CD6 end

    def Function_18_4D86(): pass

    label("Function_18_4D86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D97")
    Jump("loc_4E10")

    label("loc_4D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4DF9")

    #C0218
    ChrTalk(
        0x10,
        (
            "#03800F能和这么多朋友一起玩，\x01",
            "太开心了～！\x02\x03",

            "#03809F下次也带萨妮塔\x01",
            "一起来玩吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E10")

    label("loc_4DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_4E07")
    Jump("loc_4E10")

    label("loc_4E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4E10")

    label("loc_4E10")

    TalkEnd(0xFE)
    Return()

    # Function_18_4D86 end

    def Function_19_4E14(): pass

    label("Function_19_4E14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507B")

    #C0219
    ChrTalk(
        0xFE,
        (
            "我正在想办法拔除\x01",
            "这片花田中的『灵智之草』。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "拔掉之后，马上就会再长出来……\x01",
            "要是有办法能让它们根绝就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x01",
            "它是『幻兽』出现的原因，\x01",
            "确实应该当作最优先的处理事项。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "总之，我再多试几种方法好了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0223
    ChrTalk(
        0xFE,
        (
            "对了，有件事\x01",
            "一定要告诉你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "……我马上就要和未婚妻帕尔\x01",
            "举行结婚仪式了。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "如今的状况比较特殊，\x01",
            "所以暂时还要对帕尔保密……\x01",
            "不过我已经开始做各种准备工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#00102F啊……\x01",
            "呵呵，那可真是恭喜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "哈哈，正是在这种时候，\x01",
            "才更想把要保护的人\x01",
            "牢牢握在手心里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "等到婚礼的日期定下来之后，\x01",
            "一定会邀请你们的，\x01",
            "请务必赏光参加哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 1)
    Jump("loc_5101")

    label("loc_507B")


    #C0229
    ChrTalk(
        0xFE,
        (
            "都已经让帕尔等了\x01",
            "很久了……最近一定会\x01",
            "举办结婚仪式。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "我身为克洛斯贝尔的游击士，\x01",
            "就算是为了保护好她，\x01",
            "也必须要继续提高自己。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5101")

    TalkEnd(0xFE)
    Return()

    # Function_19_4E14 end

    def Function_20_5105(): pass

    label("Function_20_5105")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B8")

    #C0231
    ChrTalk(
        0x26,
        (
            "我们再在这里\x01",
            "观光一阵子，\x01",
            "就要回利贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x26,
        (
            "各位的恩情，我永生难忘，\x01",
            "用语言实在无法表达感激之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x26,
        (
            "多亏你们，我才能与父亲重逢，\x01",
            "请容我再次道谢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5226")

    label("loc_51B8")


    #C0234
    ChrTalk(
        0x26,
        (
            "各位的恩情，我永生难忘，\x01",
            "用语言实在无法表达感激之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x26,
        (
            "多亏你们，我才能与父亲重逢，\x01",
            "请容我再次道谢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5226")

    TalkEnd(0xFE)
    Return()

    # Function_20_5105 end

    def Function_21_522A(): pass

    label("Function_21_522A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A7")

    #C0236
    ChrTalk(
        0xFE,
        (
            "呵呵，能见到爷爷，\x01",
            "阿尔米好像\x01",
            "也很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "真是太好啦～\x01",
            "对吧，阿尔米⊥\x02",
        )
    )

    CloseMessageWindow()

    #N0238
    NpcTalk(
        0xFE,
        "婴儿",
        "哇——哇——\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_52E1")

    label("loc_52A7")


    #C0239
    ChrTalk(
        0xFE,
        (
            "乖哦～我们再去见\x01",
            "爷爷一面吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #N0240
    NpcTalk(
        0xFE,
        "婴儿",
        "哇——哇——\x02",
    )

    CloseMessageWindow()

    label("loc_52E1")

    TalkEnd(0xFE)
    Return()

    # Function_21_522A end

    def Function_22_52E5(): pass

    label("Function_22_52E5")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5317")
    SetScenarioFlags(0x31, 2)

    label("loc_5317")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_535D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_5357")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_534C")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_5352")

    label("loc_534C")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_5352")

    Jump("loc_535D")

    label("loc_5357")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_535D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_53CE")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_53AE"),
        (SWITCH_DEFAULT, "loc_53BF"),
    )


    label("loc_53AE")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_53C9")

    label("loc_53BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53C9")

    Jump("loc_55FF")

    label("loc_53CE")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_53FE")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_53FE")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5428"),
        (1, "loc_552C"),
        (2, "loc_55BD"),
        (SWITCH_DEFAULT, "loc_55F5"),
    )


    label("loc_5428")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5459")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_5469")

    label("loc_5459")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_5469")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54BF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54BF")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E2")
    Sound(461, 0, 100, 0)

    label("loc_54E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5502")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_5512")

    label("loc_5502")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_5512")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_535D")

    label("loc_552C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_559E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5561")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5579")

    label("loc_5561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5574")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5579")

    label("loc_5574")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5579")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55B8")

    label("loc_559E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_55AE")
    OP_AF(0xFB)
    Jump("loc_55B8")

    label("loc_55AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55B8")

    Jump("loc_55FF")

    label("loc_55BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55D6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_55F0")

    label("loc_55D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_55E6")
    OP_AF(0xFB)
    Jump("loc_55F0")

    label("loc_55E6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55F0")

    Jump("loc_55FF")

    label("loc_55F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55FF")

    Jump("loc_535D")

    label("loc_5604")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_52E5 end

    def Function_23_5612(): pass

    label("Function_23_5612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5648")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_5648")

    Call(0, 3)
    Return()

    # Function_23_5612 end

    def Function_24_564C(): pass

    label("Function_24_564C")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0242
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
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
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570F")
    OP_E2(0x2)
    MiniGame(0x6, 0x1B, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_570F")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_564C end

    def Function_25_5714(): pass

    label("Function_25_5714")

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

    # Function_25_5714 end

    def Function_26_5956(): pass

    label("Function_26_5956")

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
            "#6P#00005F话说回来……\x01",
            "观众真是不少呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B92():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B92)
    Sleep(50)

    def lambda_5BA2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5BA2)

    def lambda_5BAF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BAF)
    Sleep(50)

    def lambda_5BBF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5BBF)

    def lambda_5BCC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BCC)
    Sleep(50)

    def lambda_5BDC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BDC)
    Sleep(300)

    #C0245
    ChrTalk(
        0x18,
        (
            "#12P嗯，消息好像\x01",
            "立刻就传开了。\x02",
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
        "#5P嘿嘿，游击士是无敌的哦。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "#5P收拾区区警察，\x01",
            "根本不在话下嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0248
    ChrTalk(
        0xA,
        (
            "#11P不在话下？\x01",
            "那是什么意思？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0249
    ChrTalk(
        0xB,
        (
            "#5P嗯……就是说，\x01",
            "那些警察完全不是对手啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x96, 0x1F4)

    #C0250
    ChrTalk(
        0xB,
        (
            "#5P是这样吗，\x01",
            "但我觉得特别任务支援科\x01",
            "的哥哥姐姐们也很厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x96, 0x1F4)

    #C0251
    ChrTalk(
        0x9,
        "#5P噢噢！我开始热血沸腾了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1D, 500)

    #C0252
    ChrTalk(
        0x9,
        (
            "#11P嘿，村长觉得\x01",
            "哪边会赢啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x1D,
        (
            "#5P唔，这个嘛……\x01",
            "平时经常受到他们两方的关照，\x01",
            "不想偏袒其中一方啊。\x02",
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
        "#12P#00106F连、连村长都……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0255
    ChrTalk(
        0x19,
        (
            "#12P说起来，\x01",
            "有关比试的事情，\x01",
            "也只对村长说过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        "#6P#10302F呵呵，真不愧是乡村啊。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        "#6P#00306F嗯，小道消息的传播速度太惊人了。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x109,
        (
            "#6P#10112F啊哈哈……\x01",
            "让人感到了另一层意义上的紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x18,
        (
            "#12P呵呵，算啦，偶尔经历\x01",
            "一次这样的事情也不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0xEE, 0x1F4)
    Sleep(300)

    #C0260
    ChrTalk(
        0x18,
        (
            "#11P那么，我们马上就\x01",
            "开始比试吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F5B():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F5B)
    Sleep(50)

    def lambda_5F6B():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F6B)

    def lambda_5F78():
        OP_93(0xFE, 0xEE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5F78)
    Sleep(50)

    def lambda_5F88():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F88)
    Sleep(50)

    def lambda_5F98():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F98)
    Sleep(50)

    def lambda_5FA8():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FA8)
    Sleep(300)

    #C0261
    ChrTalk(
        0x18,
        "#11P不过，首先还是要决定比试形式。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x19,
        (
            "#11P嗯～我考虑过\x01",
            "好几种方案……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x19,
        (
            "#11P觉得还是采用两人一组，\x01",
            "也就是二对二形式的战斗比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x18,
        (
            "#5P嗯，我也赞成\x01",
            "这种形式。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x18,
        "#11P你们没有异议吧？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#6P#00004F嗯，毕竟是二位提出的委托，\x01",
            "我们当然没有问题……\x02\x03",

            "#00000F不过，参战人选\x01",
            "可以由我们来决定吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x18,
        "#11P嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x18,
        (
            "#11P不过，罗伊德，\x01",
            "我们希望你一定要参战。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#6P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x18,
        (
            "#11P哈哈，这没什么\x01",
            "好吃惊的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x18,
        (
            "#11P我们想见识的，\x01",
            "并非只有你们的\x01",
            "个人身体能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x18,
        (
            "#11P特别任务支援科以罗伊德\x01",
            "为中心的团队凝聚力……\x01",
            "才是我们最想看到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x19,
        (
            "没错没错，\x01",
            "如果身为关键人物的队长不上场，\x01",
            "比试也就没有意义了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#6P#00005F知、知道了……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        (
            "#6P#00301F可恶，罗伊德这臭小子……！\x02\x03",

            "竟然被这么漂亮的\x01",
            "姐姐如此恳求……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，原来如此，\x01",
            "这就是传说中的贵族弟弟啊。\x02",
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
            "#6P#00006F我好像听到了\x01",
            "一些不当的评价……\x01",
            "算啦，不管了。\x02\x03",

            "#00000F总之，\x01",
            "我已经明白二位的意思了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#6P#00100F那么，\x01",
            "罗伊德要选谁\x01",
            "做搭档呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        "#6P#00003F嗯，这个嘛……\x02",
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
            "和艾莉一起战斗\x01",        # 0
            "和兰迪一起战斗\x01",        # 1
            "和诺艾尔一起战斗\x01",      # 2
            "和瓦吉一起战斗\x01",        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64F7")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0280
    ChrTalk(
        0x101,
        "#5P#00000F艾莉，请你出场可以吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0281
    ChrTalk(
        0x102,
        (
            "#12P#00104F呵呵，当然。\x02\x03",

            "#00102F就让二位游击士见识一下\x01",
            "我们的组合战技吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66EF")

    label("loc_64F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659D")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x2)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0282
    ChrTalk(
        0x101,
        "#5P#00000F兰迪，请你出场可以吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x104,
        (
            "#12P#00309F哦，当然！\x02\x03",

            "#00300F就用我们的组合战技\x01",
            "把两位姐姐击败吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66EF")

    label("loc_659D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6647")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0284
    ChrTalk(
        0x101,
        "#11P#00000F诺艾尔，请你出场可以吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0285
    ChrTalk(
        0x109,
        (
            "#6P#10109F嗯，当然！\x02\x03",

            "#10100F就用我们的组合战技\x01",
            "把二位游击士打败吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66EF")

    label("loc_6647")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x4)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0286
    ChrTalk(
        0x101,
        "#11P#00000F瓦吉，可以一起战斗吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0287
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，很乐意接受你的邀请。\x02\x03",

            "#10302F施展我们的二人战技，\x01",
            "让两位姐姐大吃一惊吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66EF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFA, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6728")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6780")

    label("loc_6728")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_674C")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6780")

    label("loc_674C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6770")
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_6780")

    label("loc_6770")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_6780")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(8610, 1700, -21420, 0)
    MoveCamera(4, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12790, 0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6821")
    SetChrPos(0x104, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_6915")

    label("loc_6821")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6879")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_6915")

    label("loc_6879")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68D1")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_6915")

    label("loc_68D1")

    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x109, 13100, 0, -12850, 225)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_6915")

    FadeToBright(1000, 0)
    OP_0D()

    #C0288
    ChrTalk(
        0x19,
        "#11P已经决定好了啊！\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x18,
        "#11P二位，请准备好武器。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10960, 1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6995")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_69DB")

    label("loc_6995")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69B1")
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_69DB")

    label("loc_69B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D3")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_69DB")

    label("loc_69D3")

    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_69DB")

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
        "#4S#11P比试开始！\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A40")
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_6A95")

    label("loc_6A40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A63")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_6A95")

    label("loc_6A63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A86")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_6A95")

    label("loc_6A86")

    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)

    label("loc_6A95")

    Battle("BattleInfo_774", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x109, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    Return()

    # Function_26_5956 end

    def Function_27_6AC4(): pass

    label("Function_27_6AC4")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70F4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC9")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x3)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_6DD5")

    label("loc_6CC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D29")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_6DD5")

    label("loc_6D29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D89")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_6DD5")

    label("loc_6D89")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x3)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_6DD5")

    FadeToBright(1000, 0)
    OP_0D()

    #C0291
    ChrTalk(
        0x101,
        "#6P#00006F呼……呼……赢不了吗！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4E")

    #C0292
    ChrTalk(
        0x102,
        (
            "#6P#00106F怎么会这样……对方明明\x01",
            "没有认真……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFC")

    label("loc_6E4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E97")

    #C0293
    ChrTalk(
        0x104,
        (
            "#6P#00306F呜！而且对方根本\x01",
            "就没有拿出全力……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFC")

    label("loc_6E97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ED6")

    #C0294
    ChrTalk(
        0x109,
        (
            "#6P#10106F呜……完全\x01",
            "估计错误啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFC")

    label("loc_6ED6")


    #C0295
    ChrTalk(
        0x105,
        "#6P#10306F哎呀呀……大意了呢……\x02",
    )

    CloseMessageWindow()

    label("loc_6EFC")


    #C0296
    ChrTalk(
        0x18,
        (
            "#11P呼，没想到只有这点实力……\x01",
            "稍微有些失望啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x19,
        (
            "#11P嗯～本以为你们\x01",
            "可以做得更好些。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x18,
        (
            "#11P算啦，只能说你们的\x01",
            "联手作战经验尚浅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x18,
        (
            "#11P那么，我们接下来\x01",
            "想与你们整个队伍交手。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7073")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Jump("loc_70EF")

    label("loc_7073")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70A3")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Jump("loc_70EF")

    label("loc_70A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70D3")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Jump("loc_70EF")

    label("loc_70D3")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    label("loc_70EF")

    Jump("loc_7653")

    label("loc_70F4")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716D")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_7279")

    label("loc_716D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71CD")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_7279")

    label("loc_71CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_722D")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_7279")

    label("loc_722D")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_7279")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0300
    ChrTalk(
        0x101,
        "#6P#00000F呼……赢了吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F8")

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#00102F嗯……不过\x01",
            "对方好像\x01",
            "手下留情了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_73C1")

    label("loc_72F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7341")

    #C0302
    ChrTalk(
        0x104,
        (
            "#6P#00304F嗯，但对方\x01",
            "似乎并没有\x01",
            "拿出全力呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_73C1")

    label("loc_7341")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_738A")

    #C0303
    ChrTalk(
        0x109,
        (
            "#6P#10104F是的……但是\x01",
            "对方好像\x01",
            "手下留情了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_73C1")

    label("loc_738A")


    #C0304
    ChrTalk(
        0x105,
        (
            "#6P#10304F是啊，不过\x01",
            "那两人似乎\x01",
            "并没有认真呢。\x02",
        )
    )

    OP_57(0x0)
    OP_5A()
    CloseMessageWindow()

    label("loc_73C1")

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
            "#11P呵呵，真让人吃惊，\x01",
            "干得实在是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x19,
        (
            "#11P嗯嗯，配合得比我\x01",
            "想象中更加默契呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#6P#00012F啊哈哈……你们似乎很轻松啊。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x18,
        (
            "#11P呵呵，手下留情虽然是事实，\x01",
            "但我们也并不是很轻松。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x18,
        (
            "#11P总之，这场比试\x01",
            "让我们很有收获。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        (
            "#6P#00105F那么……训练就\x01",
            "到此结束了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x18,
        (
            "#11P呵呵，\x01",
            "不要那么着急嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x19,
        (
            "#11P这样就结束，\x01",
            "你们也会觉得意犹未尽吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#6P#00005F没、没有的事……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x18,
        "#11P哈哈，有什么可不好意思的。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x18,
        (
            "#11P好了，接下来，\x01",
            "我们两个想与特别任务支援科\x01",
            "的全体成员对决。\x02",
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

    label("loc_7653")


    def lambda_7658():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7658)
    Sleep(50)

    def lambda_7668():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7668)
    Sleep(50)

    def lambda_7678():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7678)
    Sleep(50)

    def lambda_7688():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7688)
    Sleep(300)

    #C0316
    ChrTalk(
        0x101,
        "#6P#00005F和、和我们五个人战斗吗？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        (
            "#6P#00306F就算是你们，想以二敌五\x01",
            "恐怕也很艰难吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x18,
        (
            "#11P呵呵，就是要这样\x01",
            "才能达到训练的目的啊。\x02",
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
        "#11P#4S——破！\x02",
    )

    CloseMessageWindow()
    Sound(620, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 9600, 0, -18150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    #C0320
    ChrTalk(
        0x102,
        "#6P#00105F好厉害……力量迸发而出！\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#6P#00303F是东方武术中的『气功』吗……\x02\x03",

            "#00301F……看来很棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x18,
        "#11P嘿，了解得很清楚嘛。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x18,
        "#11P——艾欧莉娅！\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x19,
        "#11P明白！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7852():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7852)
    Sleep(50)

    def lambda_7862():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7862)
    Sleep(50)

    def lambda_7872():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7872)
    Sleep(50)

    def lambda_7882():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7882)
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
        "#6P#10105F这是……\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，所有人都恢复\x01",
            "十足状态了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x18,
        "#11P这样就可以心无挂碍地战斗了吧？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x18,
        (
            "#11P好了，你们几位！\x01",
            "不要磨磨蹭蹭的，准备战斗！\x02",
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
        "#6P#00300F呼，看来也只能硬着头皮上了。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#6P#00100F罗伊德……\x01",
            "让谁来担任援护队员？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#6P#00003F哦……\x02",
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
            "让艾莉担任援护队员\x01",        # 0
            "让兰迪担任援护队员\x01",        # 1
            "让诺艾尔担任援护队员\x01",      # 2
            "让瓦吉担任援护队员\x01",        # 3
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC9")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_7B21")

    label("loc_7AC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AED")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_7B21")

    label("loc_7AED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B11")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_7B21")

    label("loc_7B11")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_7B21")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BBC")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_7CB0")

    label("loc_7BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C14")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_7CB0")

    label("loc_7C14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C6C")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_7CB0")

    label("loc_7C6C")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_7CB0")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D14")

    #C0332
    ChrTalk(
        0x101,
        "#6P#00000F艾莉，援护工作就拜托你了！\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x102,
        "#6P#00100F嗯，知道了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E06")

    label("loc_7D14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D66")

    #C0334
    ChrTalk(
        0x101,
        "#6P#00000F兰迪，援护工作交给你了！\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        "#6P#00300F收到！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E06")

    label("loc_7D66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC0")

    #C0336
    ChrTalk(
        0x101,
        "#6P#00000F诺艾尔，援护工作交给你负责！\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x109,
        "#6P#10100F是，队长！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E06")

    label("loc_7DC0")


    #C0338
    ChrTalk(
        0x101,
        "#6P#00000F瓦吉，援护工作就交给你了！\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x105,
        "#6P#10300F呵呵，明白！\x02",
    )

    CloseMessageWindow()

    label("loc_7E06")


    #C0340
    ChrTalk(
        0x18,
        "#4S#11P——要上了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_7B8", 0x30200011, 0x0, 0x100, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    Return()

    # Function_27_6AC4 end

    def Function_28_7E40(): pass

    label("Function_28_7E40")

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

    # Function_28_7E40 end

    def Function_29_800C(): pass

    label("Function_29_800C")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86F8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8226")
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
    Jump("loc_837A")

    label("loc_8226")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_829E")
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
    Jump("loc_837A")

    label("loc_829E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8316")
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
    Jump("loc_837A")

    label("loc_8316")

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

    label("loc_837A")

    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0341
    ChrTalk(
        0x101,
        "#6P#00006F呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#6P#00301F怎么会有这么强的女子……\x01",
            "全体一起上，竟然都不是她们的对手……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x109,
        "#6P#10108F我们彻底败了呢……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x18,
        (
            "#11P呼……老实说，\x01",
            "这次连我都觉得\x01",
            "恐怕要输了。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x19,
        (
            "#11P嗯，不过总算是\x01",
            "艰难取胜了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x19,
        "#11P这大概也正是经验差距的体现吧。\x02",
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
        "#6P#00002F啊……\x02",
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
            "#6P#00105F之前受的伤\x01",
            "被完全治好了……\x02\x03",

            "#00102F好厉害的回复技术啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        (
            "#6P#00301F不过，被打败之后，\x01",
            "竟然又被对方治疗伤势……\x02\x03",

            "#00306F呼，身为男人，真是太丢脸了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x19,
        (
            "#11P对不起，\x01",
            "莫非是我多事了吗？\x02",
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
            "#6P#00309F哪里哪里，没有的事！\x02\x03",

            "#00300F全身都被艾欧莉娅小姐\x01",
            "那温暖的魔法轻抚……\x01",
            "世间幸事，真是莫过于此啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x109,
        "#6P#10106F兰、兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x105,
        (
            "#6P#10300F哈哈，刚才的自尊心\x01",
            "跑到哪里去了～\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        (
            "#6P#00106F呼，真是的……\x01",
            "该说是欠缺\x01",
            "紧张感吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C9F")

    label("loc_86F8")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8789")
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
    Jump("loc_88DD")

    label("loc_8789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8801")
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
    Jump("loc_88DD")

    label("loc_8801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8879")
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
    Jump("loc_88DD")

    label("loc_8879")

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

    label("loc_88DD")

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
            "#6P#00006F呼、呼……\x01",
            "结、结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        (
            "#6P#00304F嗯，总算赢了啊。\x02\x03",

            "#00302F话说回来，以我们五个人为对手，\x01",
            "竟然还能缠斗到如此地步，\x01",
            "真是相当惊人的实力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#6P#00104F嗯，的确……\x01",
            "直到最后，我们都无法松懈半分呢。\x02",
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
            "#11P呼……\x01",
            "果然还是不行啊。\x02",
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
            "#11P本以为可以表现得\x01",
            "再好一些呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x19,
        (
            "#11P算啦，既然结果已定，\x01",
            "再说这些也没有用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x19,
        (
            "#11P你们确实很强，\x01",
            "这次是我们彻底输了。\x02",
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
        "#6P#00005F啊……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#6P#00102F好厉害……\x02\x03",

            "之前受的伤\x01",
            "被完全治好了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#6P#00309F一天之内竟然可以连续两次\x01",
            "享受到艾欧莉娅小姐的回复魔法……\x01",
            "感觉爽到要升天了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x19,
        "#11P谢谢夸奖，兰迪。\x02",
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
            "#11P如果你还想享受第三次，\x01",
            "要不要再尝尝我的攻击？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x104,
        "#6P#00306F呜！还是饶了我吧。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，要是再来一次，\x01",
            "说不定就真要升天了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x109,
        "#6P#10106F瓦、瓦吉……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0370
    ChrTalk(
        0x102,
        (
            "#6P#00106F呼，真是的……\x01",
            "该说是欠缺\x01",
            "紧张感吗……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    label("loc_8C9F")


    #C0371
    ChrTalk(
        0x18,
        (
            "#11P哈哈，你们几个真是有趣，\x01",
            "听你们聊天怎么听都不会腻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        "#11P#00012F多、多谢夸奖。\x02",
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
            "#12P好啦好啦，这次的比试\x01",
            "已经结束了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1D, 500)
    Sleep(300)

    #C0374
    ChrTalk(
        0x19,
        (
            "#12P各位，就算继续待下去，\x01",
            "也看不到什么有趣的事情了哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DC3():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DC3)
    Sleep(50)

    def lambda_8DD3():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DD3)
    Sleep(50)

    def lambda_8DE3():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DE3)
    Sleep(50)

    def lambda_8DF3():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8DF3)
    Sleep(50)

    def lambda_8E03():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8E03)
    Sleep(300)

    #C0375
    ChrTalk(
        0x1D,
        (
            "#5P唔，既然如此，\x01",
            "我们解散吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x1D,
        (
            "#5P大家也都要工作吧，\x01",
            "休息时间已经结束了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)
    Sleep(300)

    #C0377
    ChrTalk(
        0x1B,
        "#11P哈哈，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x8, 500)
    Sleep(300)

    #C0378
    ChrTalk(
        0x1A,
        "#11P好啦，大家都走吧。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x9,
        "#11P哎呀～真是场精彩的战斗啊！\x02",
    )

    CloseMessageWindow()
    OP_68(7360, 1500, -16890, 5000)
    MoveCamera(20, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16070, 5000)

    def lambda_8F03():
        OP_95(0xFE, 8600, 0, -6460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8F03)
    Sleep(50)

    def lambda_8F20():
        OP_95(0xFE, -2960, 0, -6890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8F20)
    Sleep(50)

    def lambda_8F3D():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8F3D)
    Sleep(1000)

    def lambda_8F5A():
        OP_95(0xFE, 1980, 0, -8140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8F5A)
    Sleep(50)

    def lambda_8F77():
        OP_95(0xFE, -470, 0, -11050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F77)
    Sleep(50)

    def lambda_8F94():
        OP_95(0xFE, 280, 0, -10190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8F94)
    Sleep(50)

    def lambda_8FB1():
        OP_95(0xFE, 1220, 0, -9620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8FB1)
    Sleep(1200)

    def lambda_8FCE():
        OP_95(0xFE, 3110, 0, -9910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8FCE)
    WaitChrThread(0x9, 1)

    def lambda_8FEC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8FEC)
    WaitChrThread(0x8, 1)

    def lambda_8FFD():
        OP_95(0xFE, -5810, 0, -6140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8FFD)
    WaitChrThread(0xA, 1)

    def lambda_901B():
        OP_95(0xFE, -5250, 0, -4930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_901B)
    WaitChrThread(0xB, 1)

    def lambda_9039():
        OP_95(0xFE, -4680, 0, -3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9039)
    WaitChrThread(0x1A, 1)

    def lambda_9057():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9057)
    WaitChrThread(0x1B, 1)

    def lambda_9075():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9075)
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
            "#12P哦，对了，村长先生，\x01",
            "谢谢您允许我们\x01",
            "使用场地哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x18,
        "#12P多亏您帮忙，才完成了一场很不错的训练。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x1D,
        (
            "#5P哪里哪里，\x01",
            "我应该向你们道谢才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x1D,
        (
            "#5P平时总是受到你们的关照，\x01",
            "如果以后还有什么事，随时可以和我说。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x1D,
        "#5P那我就先告辞啦。\x02",
    )

    CloseMessageWindow()

    def lambda_91AB():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_91AB)
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
            "#6P#00009F哈哈，\x01",
            "没想到大家\x01",
            "看得这么开心啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18, 500)
    Sleep(300)

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#00005F对了，林小姐……\x01",
            "训练的结果怎么样？\x01",
            "这才是最关键的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_928E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_928E)
    Sleep(50)

    def lambda_929E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_929E)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F7")

    def lambda_92BA():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92BA)
    Sleep(50)

    def lambda_92CA():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92CA)
    Sleep(50)

    def lambda_92DA():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_92DA)
    Sleep(50)

    def lambda_92EA():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_92EA)
    Jump("loc_93D6")

    label("loc_92F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9348")

    def lambda_930B():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_930B)
    Sleep(50)

    def lambda_931B():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_931B)
    Sleep(50)

    def lambda_932B():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_932B)
    Sleep(50)

    def lambda_933B():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_933B)
    Jump("loc_93D6")

    label("loc_9348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9399")

    def lambda_935C():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_935C)
    Sleep(50)

    def lambda_936C():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_936C)
    Sleep(50)

    def lambda_937C():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_937C)
    Sleep(50)

    def lambda_938C():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_938C)
    Jump("loc_93D6")

    label("loc_9399")


    def lambda_939E():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_939E)
    Sleep(50)

    def lambda_93AE():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93AE)
    Sleep(50)

    def lambda_93BE():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93BE)
    Sleep(50)

    def lambda_93CE():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_93CE)

    label("loc_93D6")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_950F")
    OP_2C(0x75, 0x2)
    OP_29(0x75, 0x1, 0x5)

    #C0387
    ChrTalk(
        0x18,
        (
            "#11P嗯，各位比我\x01",
            "想象中的还要强，\x01",
            "经过亲身体验，真是大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x18,
        "#11P训练非常有成果呢。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x19,
        (
            "#11P呵呵，不过我们可不\x01",
            "喜欢战败的滋味。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x19,
        (
            "#11P以后可要给我们\x01",
            "一雪前耻的机会哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，如果以后有机会，\x01",
            "我们一定奉陪。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        "#6P#00309F我随时都没问题哦⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_950F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95F9")
    OP_29(0x75, 0x1, 0x6)

    #C0393
    ChrTalk(
        0x18,
        (
            "#11P这个嘛，如果你们能再顽强些，\x01",
            "就能达到更好的训练效果了……\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x19,
        (
            "#11P可惜……该怎么说呢，\x01",
            "大概就是有些意犹未尽吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        "#6P#00006F真、真是惭愧。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x18,
        "#11P算啦，即使如此，也取得了一定的成果。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9698")

    label("loc_95F9")

    OP_2C(0x75, 0x1)
    OP_29(0x75, 0x1, 0x7)

    #C0397
    ChrTalk(
        0x18,
        (
            "#11P是啊，各位努力配合我们的训练\x01",
            "就已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x19,
        (
            "#11P嗯嗯，等以后有机会时，\x01",
            "还请各位再陪我们训练哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#6P#00000F嗯，到时还请多多指教。\x02",
    )

    CloseMessageWindow()

    label("loc_9698")

    OP_29(0x75, 0x1, 0x8)

    #C0400
    ChrTalk(
        0x18,
        (
            "#11P另外，能亲身感受到\x01",
            "大家各自的战斗风格，\x01",
            "也算是不小的收获。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x18,
        (
            "#11P特别是罗伊德，\x01",
            "我对你的旋棍术\x01",
            "很有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x18,
        (
            "#11P好像是在警察学校中\x01",
            "学习的压制术的一种吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#6P#00000F是的，你了解得很清楚啊。\x02\x03",

            "#00005F不过，很有兴趣是指……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x18, 500)

    #C0404
    ChrTalk(
        0x104,
        (
            "#6P#00304F说起来，旋棍这种武器\x01",
            "是从东方传来的呢。\x02\x03",

            "#00305F林小姐应该也会用吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x18,
        "#11P嗯，还算有一些研究吧。\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x18,
        (
            "#11P除此之外，还有偃月轮与三节棍，\x01",
            "这些东方兵器的技术，我在师门中\x01",
            "修行时大致都有所掌握……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x18,
        (
            "#11P在我看来，\x01",
            "罗伊德，你的那招回旋战技\x01",
            "似乎还有变化的余地。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0408
    ChrTalk(
        0x101,
        (
            "#6P#00005F变化……也就是说，\x01",
            "战技可以变得更强吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x18,
        "#11P嗯，不过也只是有可能而已。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x18,
        (
            "#11P如果你的时间方便，\x01",
            "我可以在这里稍加指点……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x18,
        "#11P要试试看吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0412
    ChrTalk(
        0x101,
        "#6P#00002F嗯！如果可以，请务必指教！\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x19,
        "#11P真不错啊～罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x19,
        (
            "#11P林很少会\x01",
            "指点别人呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x19, 500)

    #C0415
    ChrTalk(
        0x104,
        (
            "#6P#00309F我也有很多方面需要\x01",
            "艾欧莉娅小姐的指点。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x19,
        "#11P嗯～？驳回。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x104,
        "#6P#00306F呜。\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x109,
        "#6P#10106F兰迪前辈真是不知悔改啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0419
    ChrTalk(
        0x101,
        (
            "#11P#00006F各位，不好意思……\x02\x03",

            "#00000F事情就如你们所见，\x01",
            "能不能稍微等等我？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9ADA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9ADA)
    Sleep(50)

    def lambda_9AEA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9AEA)
    Sleep(50)

    def lambda_9AFA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AFA)
    Sleep(50)

    def lambda_9B0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9B0A)
    Sleep(300)

    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#00100F嗯，难得的机会，\x01",
            "好好学习一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，那我们就在\x01",
            "一旁观摩好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x109,
        "#6P#10100F加油啊，罗伊德警官。\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x104,
        "#6P#00300F噢噢！连同我的份一起加油啊！\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x101,
        "#11P#00012F啊，嗯……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x18,
        (
            "#11P哈哈，那就赶快\x01",
            "开始吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0426
    ChrTalk(
        0x101,
        "#6P#00000F请多指教！\x02",
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
            "#6P#00000F刚、刚才那一次\x01",
            "的感觉好像很不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x18,
        "#11P嗯，完全合格。\x02",
    )

    CloseMessageWindow()
    OP_68(7310, 1400, -21350, 2000)
    MoveCamera(12, 19, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14340, 2000)

    def lambda_9DBD():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9DBD)
    Sleep(50)

    def lambda_9DD5():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DD5)
    Sleep(50)

    def lambda_9DED():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9DED)

    def lambda_9E02():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E02)
    Sleep(50)

    def lambda_9E1A():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E1A)
    Sleep(50)

    def lambda_9E32():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E32)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    #C0429
    ChrTalk(
        0x18,
        (
            "#11P今后只要在实战中应用，\x01",
            "很快就可以彻底掌握了。\x02",
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
            "#6P#00000F呼，太好了……\x01",
            "真是多谢指导。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        "#6P#00100F呵呵，成功了啊。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x109,
        "#6P#10100F罗伊德警官，辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0xFA, 0x1F4)

    #C0433
    ChrTalk(
        0x101,
        (
            "#11P#00000F嗯，谢谢。\x02\x03",

            "#00003F话说回来，还真是惊人啊……\x01",
            "仅凭一种技巧，就可以使\x01",
            "力量的流动产生如此变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x18,
        (
            "#11P呵呵，刚才教给你的，\x01",
            "是俗称为『螺旋』的技术形式\x01",
            "中的一种格斗技巧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x3A, 0x1F4)

    #C0435
    ChrTalk(
        0x18,
        (
            "#11P『螺旋』可以算是武术中的基本技巧之一，\x01",
            "亚里欧斯先生所使用的『八叶一刀流』\x01",
            "也包含了这种技巧。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x18,
        (
            "#11P它是一切武术的基础，\x01",
            "可以应用在各种武术之中，\x01",
            "由其所派生出来的技术更是多如繁星……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x18,
        (
            "#11P据说，将『螺旋』修炼到极致，\x01",
            "掌握『无』之领域的人，便可达至\x01",
            "一切武术的顶点——『理』之境界。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        "#6P#00005F『螺旋』、『无』，还有『理』吗……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x18,
        (
            "#11P呼，有关这些，\x01",
            "我也不是很了解，\x01",
            "所以只能粗略讲解一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x18,
        (
            "#11P总之，所谓的『理』，\x01",
            "是常人穷其一生\x01",
            "也无法达至的达人境界啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x18,
        (
            "#11P能达到那种境界的人，\x01",
            "据说在整个大陆之中\x01",
            "也只有寥寥数人而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        "#6P#00005F整、整个大陆中只有寥寥数人……\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x104,
        (
            "#6P#00303F我也听说过相关的传闻，\x01",
            "感觉真是离自己很遥远的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x18,
        "#11P哈哈，的确呢。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x18,
        (
            "#11P以『理』之境界为目标，终究是有些勉强，\x01",
            "但今后还是要继续修炼哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        "#6P#00002F嗯，明白了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0447
    ChrTalk(
        0x18,
        (
            "#11P哦，不知不觉，都已经过了这么久，\x01",
            "该去处理下一件任务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x19,
        (
            "#11P嗯，我们都要抓紧时间，\x01",
            "不然可就麻烦了呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A376():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A376)
    Sleep(50)

    def lambda_A386():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A386)
    Sleep(300)

    #C0449
    ChrTalk(
        0x102,
        "#6P#00100F二位果然非常忙啊。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x18,
        (
            "#11P嗯，由于通商会议的缘故，\x01",
            "时间实在是特别紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x19,
        (
            "#11P幸好有米歇尔排列的\x01",
            "行程表呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x19,
        (
            "#11P如今的行程表上，\x01",
            "时间单位都已经用分钟来计算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x109,
        "#6P#10105F那、那可真是很辛苦呢。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x18,
        (
            "#11P呵呵，话虽如此，\x01",
            "但我们也会适度休息的。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x18,
        (
            "#11P那我们就先告辞了，\x01",
            "请各位不要懈怠，继续进步吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x19,
        "#11P再见啦～各位。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#00000F好的，\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16340, 3000)

    def lambda_A527():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A527)
    Sleep(50)

    def lambda_A544():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A544)

    def lambda_A55E():

        label("loc_A55E")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_A55E")

    QueueWorkItem2(0x101, 1, lambda_A55E)
    Sleep(50)

    def lambda_A573():

        label("loc_A573")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_A573")

    QueueWorkItem2(0x102, 1, lambda_A573)
    Sleep(50)

    def lambda_A588():

        label("loc_A588")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_A588")

    QueueWorkItem2(0x104, 1, lambda_A588)
    Sleep(50)

    def lambda_A59D():

        label("loc_A59D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_A59D")

    QueueWorkItem2(0x109, 1, lambda_A59D)
    Sleep(50)

    def lambda_A5B2():

        label("loc_A5B2")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_A5B2")

    QueueWorkItem2(0x105, 1, lambda_A5B2)
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
            "罗伊德习得\x01",
            "狂怒旋击。\x07\x00\x02",
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
            "罗伊德的战技『加速急袭』\x01",
            "强化为『狂怒旋击』。\x07\x00\x02",
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
            "不仅攻击力有所提升，\x01",
            "还可将敌人牵引至一处。\x07\x00\x02",
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
            "任务【参加游击士的训练】\x07\x00",
            "完成！\x02",
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

    # Function_29_800C end

    def Function_30_A7A0(): pass

    label("Function_30_A7A0")

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

    def lambda_A883():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2EE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A883)
    BeginChrThread(0x101, 0, 0, 31)
    WaitChrThread(0x101, 1)
    StopEffect(0x5, 0x2)
    ClearScenarioFlags(0x1, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_A7A0 end

    def Function_31_A8B4(): pass

    label("Function_31_A8B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A8D0")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_31_A8B4")

    label("loc_A8D0")

    Return()

    # Function_31_A8B4 end

    def Function_32_A8D1(): pass

    label("Function_32_A8D1")

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
            "#00003F已经大致探听过一圈了……\x01",
            "得到了不少情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x102,
        (
            "#00103F名字是『敏涅斯』……\x01",
            "似乎是一名\x01",
            "商业人士。\x02\x03",

            "#00101F大家对他的印象都很不错，\x01",
            "这倒有些意外呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x105,
        (
            "#10302F温和有礼，对孩子很友善……\x01",
            "大概就是这样的印象。\x02\x03",

            "#10304F呵呵，但这样反而\x01",
            "更加可疑了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x109,
        "#10106F确、确实……\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x103,
        (
            "#00200F目前还无法了解\x01",
            "他的真实目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#00303F他和村长的儿子\x01",
            "好像正在谈些什么，\x01",
            "这让人有点在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x01",
            "我们还是继续\x01",
            "探听一番为好。\x02\x03",

            "#00005F嗯……\x02",
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

    def lambda_ABDF():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABDF)

    def lambda_ABEC():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ABEC)

    def lambda_ABF9():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ABF9)

    def lambda_AC06():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AC06)

    def lambda_AC13():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC13)
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
            "#00005F那个人……好像就是\x01",
            "和迪利克先生一起\x01",
            "去市里的艾尔琴先生吧？\x02\x03",

            "#00003F他好像是刚刚\x01",
            "回来的……\x01",
            "我们去问问看吧。\x02",
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

    # Function_32_A8D1 end

    def Function_33_AD11(): pass

    label("Function_33_AD11")

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
        "呵呵呵……¤\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#00000F那个，打扰了，\x01",
            "您是艾尔琴先生吧？\x02\x03",

            "有点事情想向您\x01",
            "打听一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0472
    ChrTalk(
        0x9,
        "哦，什么事？\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x9,
        (
            "难道和我这辆\x01",
            "新型导力卡车\x01",
            "有关吗？\x02",
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
            "#00012F不、不是的……\x01",
            "想问的并不是\x01",
            "这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x9,
        "啧，原来不是啊。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x9,
        (
            "难得从敏涅斯先生\x01",
            "手中以低价买到了\x01",
            "乌尔努公司的最新型卡车……\x02",
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
            "#00105F哎……？\x02\x03",

            "#00101F敏涅斯先生，\x01",
            "不就是最近来村里\x01",
            "的那个外国人……？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x109,
        (
            "#10105F您、您刚才说是低价买到……\x01",
            "究竟是什么价格呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x9,
        "哼哼哼，听了可别吃惊……\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x9,
        (
            "他只开价五万米拉，\x01",
            "就把这辆车卖给我了！\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        "#00011F五、五万！？\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x109,
        (
            "#10106F用那么便宜的价钱\x01",
            "竟然就能买到新车……\x01",
            "真、真幸运啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#00306F喂喂，现在可不是\x01",
            "羡慕别人的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x109,
        "#10112F说、说的对啊……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x103,
        (
            "#00203F咳……那个。\x02\x03",

            "#00200F新车的价格应该在\x01",
            "五十万米拉左右，这个价格\x01",
            "实在是太便宜了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x105,
        (
            "#10302F竟然以一折的价格出售，\x01",
            "哎呀呀，真是个\x01",
            "相当慷慨的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x9,
        (
            "他为了让我们的\x01",
            "工作可以顺利进行，\x01",
            "就以超低价把这辆车让给了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x9,
        (
            "敏涅斯先生似乎正在和迪利克\x01",
            "共同推进多项计划……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x9,
        (
            "呵呵，在敏涅斯先生的面前，\x01",
            "真是抬不起头啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        "#00305F计划……？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x9,
        (
            "哦、哦哦！\x01",
            "不好，迪利克还特意叮嘱过我，\x01",
            "让我保守秘密的。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x9,
        (
            "嗯，总之……\x01",
            "我认为敏涅斯先生\x01",
            "是个值得信任的好人。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x101,
        (
            "#00003F原来如此……\x02\x03",

            "#00005F……对了，艾尔琴先生，\x01",
            "您为何独自一人在这里？\x02\x03",

            "我听村长说，您和迪利克先生\x01",
            "一起去市里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x9,
        (
            "哦，迪利克稍后坐巴士回来，\x01",
            "让我先走一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x9,
        (
            "因为他在欢乐街的酒店\x01",
            "还有点事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x9,
        (
            "好像是和敏涅斯先生\x01",
            "约好要在那里见面。\x02",
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
        "#00101F罗伊德，这……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0498
    ChrTalk(
        0x101,
        (
            "#00003F嗯，说不定可以\x01",
            "直接和当事人对话呢。\x02\x03",

            "#00001F我们有必要过去看看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0499
    ChrTalk(
        0x101,
        (
            "#00000F感谢您的协助，\x01",
            "您提供的情报很有参考价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x9,
        "哪里，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x9,
        (
            "虽然不清楚到底发生了什么事，\x01",
            "不过还是请大家加油吧。\x02",
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

    # Function_33_AD11 end

    def Function_34_B64C(): pass

    label("Function_34_B64C")

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
            "#N#1P#00010F糟糕……\x01",
            "交易已经结束了吗……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_B9A0():
        OP_95(0xFE, 3850, 0, 19250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B9A0)
    Sleep(100)

    def lambda_B9BD():
        OP_95(0xFE, 4270, 0, 18270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B9BD)
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

    def lambda_BA68():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BA68)
    Sleep(100)

    def lambda_BA78():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BA78)
    Sleep(300)

    #C0503
    ChrTalk(
        0xD,
        "哦，你们是……\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xC,
        "特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        (
            "#00001F迪利克先生，敏涅斯先生……\x01",
            "二位今天进行了什么交易，\x01",
            "可以和我们说说吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        "呼，爸爸又派你们来游说吗……\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xD,
        (
            "呵呵，这也没什么不好啊，\x01",
            "迪利克先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xD,
        (
            "反正我们的计划\x01",
            "都已经开始了……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        "#00105F这是……什么意思？\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xD,
        (
            "其实，我刚刚已经和迪利克先生\x01",
            "完成了最后的交易。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xD,
        (
            "我们决定借用各位村民的土地，\x01",
            "着手于扩大花田\x01",
            "的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xD,
        (
            "而花田的管理工作，\x01",
            "则由我们『昆西公司』\x01",
            "来全权受理。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#00011F什么……！\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x105,
        (
            "#10303F……也就是说，\x01",
            "几乎把村里的农场\x01",
            "全部转让了出去……\x02\x03",

            "#10300F迪利克先生，\x01",
            "这样做真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        "……这是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xC,
        (
            "不过就是把管理权\x01",
            "出让而已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xD,
        "嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xD,
        (
            "由我们公司来负责收获蜂蜜的工作，\x01",
            "能以更高的效率来\x01",
            "运营公司的糕点制造事业。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xD,
        (
            "因此，暂时将管理权\x01",
            "移交给敝公司，\x01",
            "会更有利于效率的提升。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x104,
        (
            "#00310F（啧……\x01",
            "  真是个能说会道的混蛋。）\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x103,
        (
            "#00206F（看来计划已经\x01",
            "  进展到了最终阶段啊。）\x02\x03",

            "#00208F（既然如此，接下来……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    #C0522
    ChrTalk(
        0xD,
        (
            "呵呵，迪利克先生，\x01",
            "我会把这份合同\x01",
            "递交到总公司。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0523
    ChrTalk(
        0xD,
        (
            "我想公司明天应该\x01",
            "就会与您联络的，\x01",
            "请您静候佳音吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xC,
        "嗯，我等着您的好消息。\x02",
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
        "#10101F（罗、罗伊德警官……！）\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        (
            "#00003F（嗯……\x01",
            "  绝不能就此放过他！）\x02\x03",

            "#00001F敏涅斯先生，在此之前……\x01",
            "我还有几个问题想请教你。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C003():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C003)
    Sleep(100)

    def lambda_C013():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C013)
    Sleep(300)

    #C0527
    ChrTalk(
        0xD,
        "哦……？\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xD,
        (
            "究竟想问什么\x01",
            "问题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        (
            "#00003F嗯，其实……\x01",
            "我们对你抱有\x01",
            "一些怀疑。\x02\x03",

            "#00001F直说好了……\x01",
            "我们认为你\x01",
            "存在欺诈的嫌疑。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0530
    ChrTalk(
        0xC,
        "什么……！？\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "不、不要太过分了！\x01",
            "怎能对敏涅斯先生如此无礼！\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xD,
        (
            "呵呵……算啦算啦，\x01",
            "请不要激动，迪利克先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xC,
        "敏涅斯先生……？\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xD,
        (
            "记得各位是特别任务\x01",
            "支援科的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xD,
        (
            "既然你们怀疑\x01",
            "我是一名诈骗犯……\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xD,
        (
            "想必可以给出一个\x01",
            "令人信服的说明吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#00003F……那当然。\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xD,
        (
            "有意思……\x01",
            "那我就洗耳\x01",
            "恭听了。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        (
            "但我话说在先……\x01",
            "你们可不要忘记\x01",
            "我是帝国人。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xD,
        (
            "如果没有明确的证据\x01",
            "能证明我是一名诈骗犯……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xD,
        (
            "就算你们是警察，\x01",
            "也请给我老老实实\x01",
            "地让路。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        "#00001F……好的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0543
    ChrTalk(
        0x102,
        "#00101F罗伊德……！\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x101,
        (
            "#00003F（……没问题。）\x02\x03",

            "（根据我们在调查过程中取得的情报，\x01",
            "  可以确定敏涅斯进行诈骗行为\x01",
            "  是毫无疑问的事实……）\x02\x03",

            "#00001F（追究我们的疑问，\x01",
            "  撕下敏涅斯的假面具，\x01",
            "  让迪利克先生彻底醒悟吧！）\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xD,
        (
            "呵呵，很好……\x01",
            "既然你们有此觉悟，\x01",
            "我一定有问必答。\x02",
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
            "……那么，首先要\x01",
            "问什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0547
    ChrTalk(
        0x101,
        (
            "#00003F首先是你在\x01",
            "克洛斯贝尔的行动……\x02\x03",

            "#00001F有关其中的矛盾点，\x01",
            "我想请教一二。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xC,
        "矛盾是指……？\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "……我自从来到克洛斯贝尔之后，\x01",
            "就一直在与迪利克先生\x01",
            "共同推进此次计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xD,
        (
            "也就是在阿尔摩利卡村设立\x01",
            "我们『昆西公司』的子公司——\x01",
            "『阿尔摩利卡·甜蜜商社』的计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xD,
        (
            "使用村中出产的优质蜂蜜，\x01",
            "再结合本公司多年积累的技术，\x01",
            "必定能在糕点制造业中取得成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xD,
        (
            "此事业已经在市里\x01",
            "获得许可，如今即将\x01",
            "正式展开……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xD,
        (
            "请问，这其中究竟\x01",
            "有何矛盾呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#00003F你刚刚所提到的\x01",
            "这项『计划』……\x02\x03",

            "#00001F与我们所掌握到的情报之间\x01",
            "存在着明显的矛盾。\x02\x03",

            "#00003F这个矛盾就是……\x02",
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
            "#1K有关敏涅斯的『计划』，\x01",
            "矛盾之处在哪里？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "糕点制造技术\x01",      # 0
            "计划正在进行\x01",      # 1
            "计划的可行性\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C775")
    OP_2C(0x87, 0x1)

    #C0556
    ChrTalk(
        0x101,
        (
            "#00003F与我们在ＩＢＣ获得\x01",
            "的情报对照之后，\x01",
            "不难发现一个矛盾之处。\x02\x03",

            "#00001F你所说的『计划』……\x02\x03",

            "其实根本就\x01",
            "没在进行。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x6)
    Jump("loc_CAA3")

    label("loc_C775")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8A1")

    #C0557
    ChrTalk(
        0x101,
        (
            "#00003F你所说的『计划』……\x02\x03",

            "#00001F根本就无法完成，\x01",
            "因为你并没有能使计划\x01",
            "顺利进行的技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xD,
        (
            "哦……？\x01",
            "这个观点真是很有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xD,
        (
            "不过，你要如何\x01",
            "证明这一点呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x101,
        (
            "#00011F……哎，这、这个嘛……\x02\x03",

            "#00006F（糟糕……\x01",
            "  在提出质疑的过程中，\x01",
            "  必须要考虑好正确的步骤才行啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9C0")

    label("loc_C8A1")


    #C0561
    ChrTalk(
        0x101,
        (
            "#00003F你所说的『计划』……\x02\x03",

            "#00001F根本就无法完成，\x01",
            "因为完全没有\x01",
            "成功的可能性。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xD,
        (
            "哦……？\x01",
            "这种观点倒是很有趣，\x01",
            "但似乎有些失礼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xD,
        (
            "你说出这样的话，\x01",
            "究竟有何根据呢，\x01",
            "希望能做出合理的证明。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00011F……哎，这、这个嘛……\x02\x03",

            "#00006F（糟糕……\x01",
            "  似乎没有选对正确的突破口。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9C0")


    #C0565
    ChrTalk(
        0x102,
        (
            "#00105F啊……我明白了。\x02\x03",

            "#00100F与我们在ＩＢＣ获得\x01",
            "的情报对照之后，\x01",
            "不是可以发现一个矛盾之处吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0566
    ChrTalk(
        0x101,
        (
            "#00005F……原来如此……！\x02\x03",

            "#00001F敏涅斯先生……\x01",
            "你所说的『计划』……\x01",
            "其实根本就没在进行吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x7)

    label("loc_CAA3")

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
            "这、这是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#00003F很简单，\x01",
            "『昆西公司』如果真的打算\x01",
            "推进之前所说的计划……\x02\x03",

            "#00001F在设立子公司、建造工厂等方面\x01",
            "都会需要ＩＢＣ的融资。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xD,
        "……嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xD,
        (
            "所以我向市里提交了设立公司的申请，\x01",
            "并且专门开通了公司专用的帐户……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x101,
        (
            "#00001F仅仅是『开通』了而已，\x01",
            "没错吧？\x02",
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
            "#00003F在『甜蜜商社』的帐户中，\x01",
            "仅仅预存了开户所需\x01",
            "的最低金额。\x02\x03",

            "虽然我并不了解具体金额，\x01",
            "但存款总数仅有数万米拉……\x02\x03",

            "#00001F就靠那点钱，\x01",
            "难道就能设立公司，\x01",
            "建造工厂吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xD,
        (
            "……你们竟然还特意调查了\x01",
            "我的ＩＢＣ帐户啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0576
    ChrTalk(
        0xC,
        (
            "敏、敏涅斯先生……\x01",
            "难道您……！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    #C0577
    ChrTalk(
        0xD,
        (
            "啊，请不要误会。\x01",
            "我并没有认同\x01",
            "他的主张。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xD,
        (
            "仅仅是觉得这种做法\x01",
            "有些冒昧欠妥而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x109,
        (
            "#10105F可、可是……\x01",
            "你的帐户里确实\x01",
            "没有存多少钱吧！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    #C0580
    ChrTalk(
        0xD,
        (
            "那又如何，身为公司的董事，\x01",
            "我的行为自然\x01",
            "应该保持慎重。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xD,
        (
            "而且由有着良好的名望与信誉的\x01",
            "『昆西公司』来出面，\x01",
            "一定能够得到ＩＢＣ的融资……\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xD,
        (
            "一旦总公司下达许可，\x01",
            "我马上就会与ＩＢＣ\x01",
            "交涉融资方面的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xC,
        "呼……说、说得也是啊……\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x103,
        "#00206F（……被他轻松推卸了呢。）\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#00003F（不……\x01",
            "  敏涅斯的心里应该\x01",
            "  已经相当慌张了。）\x02\x03",

            "#00001F（此时就要一鼓作气，\x01",
            "  把更多的证据出示给他……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xD,
        (
            "……看你这表情，似乎还有\x01",
            "其它的事情要问啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        (
            "#00002F嗯，那当然。\x02\x03",

            "#00004F因为我对你的\x01",
            "怀疑并非只有这些。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0588
    ChrTalk(
        0xC,
        "都解释得这么清楚了，为何还要……！\x02",
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xD,
        "没关系，不必介意。\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xD,
        (
            "把话说清楚，\x01",
            "也能让迪利克先生\x01",
            "更加放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x101,
        (
            "#00001F……我接下来想问的是……\x01",
            "敏涅斯先生的\x01",
            "真实身份。\x02\x03",

            "#00003F敏涅斯先生，\x01",
            "你一直自称是\x01",
            "『昆西公司』的董事……\x02\x03",

            "#00013F事实真的是这样吗？\x02",
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
            "慢着……\x01",
            "这是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xC,
        (
            "难道你觉得\x01",
            "敏涅斯先生\x01",
            "不是『昆西公司』的成员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x101,
        (
            "#00003F嗯，我们正是\x01",
            "这样认为的。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xD,
        (
            "哼哼……哈哈哈！\x01",
            "我还以为你想说什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xD,
        (
            "如果不相信，要不要看看\x01",
            "我的名片和工作证？\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x103,
        (
            "#00203F……只要有一定知识，\x01",
            "那种东西都可以轻易伪造的。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        (
            "#00003F我们找到了一件证物，\x01",
            "可以完全推翻你的说辞。\x02\x03",

            "#00000F那件证物……\x01",
            "就是昆西公司的宣传手册。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xC,
        "昆西公司的宣传手册……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x104,
        "#00305F就是在大小姐的房间里找到的那本书吗……\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        (
            "#00102F我们还把其中的要点\x01",
            "记录在了调查手册呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#00000F那本手册是向总公司索取的，\x01",
            "因此可以确保其中所记内容\x01",
            "的可信性。\x02\x03",

            "#00003F而手册中所记载的某些资料……\x01",
            "与敏涅斯先生昨天说的一些话\x01",
            "存在着明显的矛盾。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xD,
        "和、和我说的话有矛盾……？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯先生昨天所说的话，\x01",
            "与其『公司董事』的身份之间\x01",
            "存在的矛盾之处，那就是……\x02",
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
            "#1K敏涅斯昨天说的话\x01",
            "与资料中记载的事实有何矛盾？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "设立子公司的计划\x01",      # 0
            "在营业部的经历\x01",        # 1
            "讨厌甜食\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA38")
    OP_2C(0x87, 0x1)

    #C0606
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯先生，\x01",
            "你昨天曾经这样说过——\x02\x03",

            "『虽然我是公司的董事，\x01",
            "  但是很讨厌甜食』……\x02\x03",

            "#00013F你还记得这句话吧？\x02",
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

    def lambda_D6C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D6C5)
    Sleep(50)

    def lambda_D6D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D6D5)
    Sleep(50)

    def lambda_D6E5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D6E5)
    Sleep(50)

    def lambda_D6F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D6F5)
    Sleep(50)

    def lambda_D705():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D705)
    Sleep(300)

    #C0607
    ChrTalk(
        0x102,
        (
            "#00105F罗、罗伊德……？\x01",
            "这个……我不太明白你的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xD,
        "……我确实很讨厌甜食。\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0xD,
        (
            "呵呵，但这又有\x01",
            "什么问题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xD,
        (
            "『讨厌吃甜食的人不可能\x01",
            "  在糕点制造公司担任董事』\x01",
            "……难道你想这样说吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#00003F正是如此。\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xC,
        (
            "你、你在胡扯些什么……！\x01",
            "身为警察，竟然如此胡搅蛮缠……！\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x101,
        (
            "#00001F昆西公司的宣传手册中\x01",
            "有这样一段内容——\x02\x03",

            "#00003F『昆西公司有严格的审查制度，\x01",
            "  董事要亲自试吃开发中的商品，\x01",
            "  从而判断其上市销售的可行性』……\x02\x03",

            "#00013F简要来说，重点就是这段话。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D8F0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D8F0)
    Sleep(50)

    def lambda_D900():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D900)
    Sleep(50)

    def lambda_D910():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D910)
    Sleep(50)

    def lambda_D920():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D920)
    Sleep(50)

    def lambda_D930():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D930)
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
        "这是什么意思……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0616
    ChrTalk(
        0xC,
        "#4S……………………啊！？\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x101,
        (
            "#00003F……像昆西公司这样的企业，\x01",
            "会任命敏涅斯先生这种『讨厌甜食』的人\x01",
            "来担任董事，本身就是一件很难理解的事情。\x02\x03",

            "#00013F……难道不是吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x8)
    Jump("loc_E015")

    label("loc_DA38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAAB")

    #C0618
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯先生，\x01",
            "你昨天曾经这样说过——\x02\x03",

            "这次的计划是\x01",
            "『在阿尔摩利卡村设立子公司』……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB29")

    label("loc_DAAB")


    #C0619
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯先生，\x01",
            "你昨天曾经这样说过——\x02\x03",

            "『由于在营业工作中表现突出，\x01",
            "  能力得到了认可，\x01",
            "  所以才有了如今的地位』……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB29")


    #C0620
    ChrTalk(
        0xD,
        (
            "……我确实说过，\x01",
            "这有什么问题吗？\x02",
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
            "#00011F（糟、糟糕……\x01",
            "  完全不知道该怎么回答！\x01",
            "  是我的想法有误吗……？）\x02\x03",

            "#00012F这、这个嘛，\x01",
            "刚才是我搞错了……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x105,
        (
            "#10304F原来如此，\x01",
            "我终于想起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        "#00005F哎？\x02",
    )

    CloseMessageWindow()

    def lambda_DC1D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC1D)
    Sleep(50)

    def lambda_DC2D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC2D)
    Sleep(50)

    def lambda_DC3D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DC3D)
    Sleep(50)

    def lambda_DC4D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC4D)
    Sleep(50)

    def lambda_DC5D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DC5D)
    Sleep(300)

    #C0624
    ChrTalk(
        0x105,
        (
            "#10304F『虽然我是公司的董事，\x01",
            "  但是很讨厌甜食』…………\x02\x03",

            "#10302F敏涅斯先生，\x01",
            "你昨天就是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x102,
        (
            "#00105F瓦、瓦吉……？\x01",
            "那个……我不太明白你的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xD,
        "……我确实很讨厌甜食。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0xD,
        (
            "呵呵，但这又有\x01",
            "什么问题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xD,
        (
            "『讨厌吃甜食的人不可能\x01",
            "  在糕点制造公司担任董事』\x01",
            "……难道你想这样说吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DD9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DD9A)
    Sleep(300)

    #C0629
    ChrTalk(
        0x103,
        "#00203F……正是。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)
    Sleep(300)

    #C0630
    ChrTalk(
        0x105,
        "#10309F呵呵，你也察觉到了啊。\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xC,
        (
            "你、你们在胡扯些什么……！\x01",
            "身为警察，竟然如此胡搅蛮缠……！\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x105,
        (
            "#10304F昆西公司的宣传手册中\x01",
            "有这样一段内容——\x02\x03",

            "『昆西公司有严格的审查制度，\x01",
            "  董事要亲自试吃开发中的商品，\x01",
            "  从而判断其上市销售的可行性』……\x02\x03",

            "#10302F简要来说，重点就是这段话。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DEE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DEE6)
    Sleep(50)

    def lambda_DEF6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DEF6)
    Sleep(50)

    def lambda_DF06():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DF06)
    Sleep(50)

    def lambda_DF16():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF16)
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
        "这是什么意思……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0635
    ChrTalk(
        0xC,
        "#4S……………………啊！？\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x103,
        (
            "#00203F……像昆西公司这样的企业，\x01",
            "会任命敏涅斯先生这种『讨厌甜食』的人\x01",
            "来担任董事，本身就是一件很难理解的事情。\x02\x03",

            "#00201F……没错吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x9)

    label("loc_E015")


    #C0637
    ChrTalk(
        0xD,
        (
            "……这、这只是……\x01",
            "只是你们记错了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x101,
        (
            "#00003F这种说辞是行不通的。\x02\x03",

            "#00001F……你刚刚已经\x01",
            "清清楚楚地承认过\x01",
            "『自己讨厌甜食』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xD,
        "呜……！\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x101,
        (
            "#00003F既然如此，\x01",
            "你为何要冒充\x01",
            "『昆西公司』的董事？\x02\x03",

            "#00001F答案就是──\x01",
            "你想获得迪利克先生的信任，\x01",
            "使自己的诈骗行为取得成功。\x02\x03",

            "#00003F通过目前取得的种种证据来分析，\x01",
            "也只有这种可能了。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        (
            "#00103F你声称要将阿尔摩利卡村\x01",
            "出产的蜂蜜用于糕点制造业……\x02\x03",

            "#00101F为了得到对方的信任，\x01",
            "『昆西公司』的名号\x01",
            "是最适合不过的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0642
    ChrTalk(
        0xC,
        (
            "敏、敏涅斯先生……\x01",
            "这到底是\x01",
            "怎么回事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xC,
        (
            "你、你真的……\x01",
            "你真的是在欺骗我吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    #C0644
    ChrTalk(
        0xD,
        (
            "……哼……哼哼……\x01",
            "迪利克先生，\x01",
            "你可不能被他们这些家伙骗了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x104,
        "#00305F什、什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    #C0646
    ChrTalk(
        0xD,
        "呵呵……你们想想看吧。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xD,
        (
            "我来到阿尔摩利卡村，\x01",
            "是为了完成\x01",
            "『甜蜜商社』计划……\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xD,
        (
            "退一百步说，就算我真的欺骗了迪利克先生，\x01",
            "实际上另有其它目的……\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xD,
        "试问，我又能有什么目的呢！？\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xD,
        (
            "如果你们无法给出答案，\x01",
            "就没有资格说我是诈骗犯！\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x103,
        (
            "#00200F证明你的真实目的吗……\x01",
            "确实有这个必要呢。\x02",
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
            "#00003F至于你的目的，\x01",
            "我有一个猜测。\x02",
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

    def lambda_E4ED():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4ED)
    Sleep(50)

    def lambda_E4FD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E4FD)
    Sleep(50)

    def lambda_E50D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E50D)
    Sleep(50)

    def lambda_E51D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E51D)
    Sleep(50)

    def lambda_E52D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E52D)
    Sleep(50)

    def lambda_E53D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E53D)
    Sleep(300)

    #C0653
    ChrTalk(
        0xD,
        "什……什么……！？\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x102,
        "#00105F（罗、罗伊德，没问题吗……！？）\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x109,
        (
            "#10106F（我、我可是完全\x01",
            "  想不出呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        (
            "#00003F（没问题……我们的确有证据。）\x02\x03",

            "（在来到这里之前，\x01",
            "  『那个人』给我们提供了\x01",
            "  『一些证言』……）\x02\x03",

            "（#00001F那些证言，正是可以解明\x01",
            "  敏涅斯真正目的的最后线索……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xD,
        (
            "你们在嘀咕什么！\x01",
            "……好了！赶快给我说明吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        (
            "#00003F你来到这个村子\x01",
            "进行诈骗，\x01",
            "真正的目的就是……\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8C0")
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
            "#1K敏涅斯在阿尔摩利卡村\x01",
            "进行诈骗行为的真正目的是什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "骗取土地\x01",              # 0
            "独占蜂蜜的销售权\x01",      # 1
            "贩卖伪造导力车\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7B4")
    OP_2C(0x87, 0x1)

    label("loc_E7B4")


    #C0660
    ChrTalk(
        0x101,
        (
            "#00003F你的真正目的就是……\x02\x03",

            "#00013F抢占阿尔摩利卡村\x01",
            "所拥有的『土地』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8BB")

    label("loc_E806")


    #C0661
    ChrTalk(
        0x101,
        (
            "#00006F（不对……并不是这样。\x01",
            "  绝不是这种程度\x01",
            "  的小事。）\x02\x03",

            "#00001F（他费尽心机，\x01",
            "  做了如此周密的准备工作……\x01",
            "  所图者必大。）\x02\x03",

            "#00003F（敏涅斯真正的目的，\x01",
            "  那就是……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E8BB")

    Jump("loc_E6E3")

    label("loc_E8C0")


    #C0662
    ChrTalk(
        0xD,
        "……啊……啊……！！\x02",
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x101,
        (
            "#00004F有位名叫哈罗德的贸易商\x01",
            "向我们提供了一些\x01",
            "关于你的信息。\x02\x03",

            "#00000F敏涅斯先生……\x01",
            "你在来到克洛斯贝尔之后，\x01",
            "马上就去调查了各地的地价吧？\x02\x03",

            "#00003F如果是『昆西公司』\x01",
            "的董事前来开拓新事业，\x01",
            "显然没有做这种事情的必要。\x02\x03",

            "那么，你为何要如此做呢……？\x01",
            "经过我的考虑，可能性只有一个。\x02\x03",

            "#00013F你的真正目的是\x01",
            "抢占这里的土地。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x109,
        (
            "#10105F真、真的吗……！？\x01",
            "听起来似乎有点\x01",
            "不着边际的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0665
    ChrTalk(
        0x101,
        (
            "#00004F不，并非如此。\x02\x03",

            "#00002F如大家所见，阿尔摩利卡村\x01",
            "被丰饶的自然景观所环绕，\x01",
            "地理位置可谓得天独厚。\x02\x03",

            "#00004F假如把这里卖给开发\x01",
            "高级别墅区的第三方……\x01",
            "大概能卖到什么价钱呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x102,
        (
            "#00103F这……\x01",
            "就算要价几千万米拉，\x01",
            "恐怕也会有人举牌呢。\x02\x03",

            "#00101F不过这里的村民们\x01",
            "肯定不会同意的……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0667
    ChrTalk(
        0x101,
        (
            "#00003F嗯，正因如此，\x01",
            "所以他才要花费这么一番工夫，\x01",
            "企图完成自己的诈骗行动。\x02\x03",

            "#00001F假设他的目标\x01",
            "就是土地本身……\x01",
            "那他这一系列的行动也就顺理成章了。\x02\x03",

            "在取得广阔花田、\x01",
            "大面积的农场，以及私有地\x01",
            "的土地产权证之后……\x02\x03",

            "他便以返回\x01",
            "总公司为由，\x01",
            "离开克洛斯贝尔。\x02\x03",

            "#00003F随后，再通过事先协调好的\x01",
            "销售渠道将土地产权证贩卖，\x01",
            "从而赚取巨额米拉……\x02\x03",

            "#00013F敏涅斯先生……\x01",
            "这才是你的真实目的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ED15():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED15)
    Sleep(50)

    def lambda_ED25():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ED25)
    Sleep(50)

    def lambda_ED35():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ED35)
    Sleep(50)

    def lambda_ED45():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ED45)
    Sleep(50)

    def lambda_ED55():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ED55)
    Sleep(300)

    #C0668
    ChrTalk(
        0xD,
        "……唔……唔唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    #C0669
    ChrTalk(
        0xC,
        (
            "敏涅斯……先生……\x01",
            "怎么会……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1F, -1730, 390, 7230, 225)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    #N0670
    NpcTalk(
        0x1F,
        "男性的声音",
        "罗伊德警官……！\x02",
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

    def lambda_EE8E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE8E)
    Sleep(50)

    def lambda_EE9E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE9E)
    Sleep(50)

    def lambda_EEAE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EEAE)
    Sleep(50)

    def lambda_EEBE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EEBE)
    Sleep(50)

    def lambda_EECE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EECE)
    Sleep(50)

    def lambda_EEDE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EEDE)
    Sleep(50)

    def lambda_EEEE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_EEEE)
    Sleep(50)

    def lambda_EEFE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EEFE)
    Sleep(300)

    #C0671
    ChrTalk(
        0x101,
        "#00000F这声音是……\x02",
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
        "#03600F太好了，我们总算及时赶到了。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x1D,
        "迪利克……\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xC,
        "爸爸，哈罗德先生……！？\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#00005F你是法律\x01",
            "事务所的……\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x1E,
        (
            "我叫皮特，\x01",
            "是伊安律师的助手。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x1E,
        (
            "律师本来是想亲自过来的，\x01",
            "但为了制订宪法草案，\x01",
            "必须要外出去其它地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x103,
        "#00205F由你带来了证据吗……？\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x1F,
        (
            "#03603F嗯，似乎就是律师之前\x01",
            "所说的『决定性证据』。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x1E,
        "各位，请看这个。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0681
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "皮特取出一张照片并举过头顶，\x01",
            "以便在场众人都能看到。\x02\x03",

            "照片上是一个相貌与敏涅斯相同，\x01",
            "商人打扮的男子。\x07\x00\x02",
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
        "#00005F这、这张照片上的人是……\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0xD,
        "为、为什么……\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xD,
        (
            "为什么你们\x01",
            "会有那张照片！？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x1E,
        (
            "这张照片是伊安律师\x01",
            "以前从一位熟识的帝国记者\x01",
            "那里得到的资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x1E,
        (
            "可是，照片上这个男人的名字……\x01",
            "并不是『敏涅斯』，\x01",
            "而是『利德纳』。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x109,
        (
            "#10100F利德纳……？\x01",
            "最近好像曾在什么地方\x01",
            "听到过这个名字……\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x102,
        (
            "#00105F……啊！\x01",
            "想起来了……\x02\x03",

            "#00101F不就是伊安律师说起过的……\x01",
            "霸占帝国男爵家土地\x01",
            "的男人的名字吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xD,
        "呜……！\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x104,
        "#00305F哦哦，确实是这个名字。\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x1F,
        (
            "#03601F嗯……伊安律师也给\x01",
            "我们讲述了这个事件，\x01",
            "不会有错的。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x105,
        (
            "#10304F唔……如此一来，\x01",
            "似乎已经了解到了\x01",
            "一些有趣的事实呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0693
    ChrTalk(
        0x105,
        (
            "#10302F罗伊德……\x01",
            "继续向敏涅斯展开追究吧。\x02\x03",

            "#10304F说说这张照片所体现出的意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        "#00003F……嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_68(2020, 1500, 16370, 3000)

    def lambda_F5D4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5D4)
    Sleep(50)

    def lambda_F5E4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F5E4)
    Sleep(50)

    def lambda_F5F4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F5F4)
    Sleep(50)

    def lambda_F604():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F604)
    Sleep(50)

    def lambda_F614():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F614)
    Sleep(50)

    def lambda_F624():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F624)
    Sleep(50)

    def lambda_F634():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F634)
    Sleep(50)

    def lambda_F644():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F644)
    Sleep(300)
    OP_6F(0x79)

    #C0695
    ChrTalk(
        0x101,
        (
            "#00001F这张照片上的人物『利德纳』\x01",
            "与在场的『敏涅斯』相貌一样，\x01",
            "原因就是……\x02",
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
            "#1K照片中的利德纳和敏涅斯\x01",
            "相貌一样的原因是……？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "双胞胎\x01",        # 0
            "扮装\x01",          # 1
            "同一个人\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7B9")
    OP_2C(0x87, 0x1)

    #C0697
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯和利德纳是同一个人……\x01",
            "也只能这样想了。\x02\x03",

            "#00013F而且诈骗的手段非常相似，\x01",
            "也是因为二者是同一个人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9E7")

    label("loc_F7B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F80B")

    #C0698
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯与利德纳是……双胞胎兄弟。\x01",
            "也只能这样想了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F843")

    label("loc_F80B")


    #C0699
    ChrTalk(
        0x101,
        (
            "#00003F敏涅斯……扮装成了利德纳。\x01",
            "也只能这样想了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F843")

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
            "#10306F……再怎么说，\x01",
            "你也有点想多了吧？\x02\x03",

            "#10302F依我看，\x01",
            "敏涅斯与利纳德\x01",
            "就是同一个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        (
            "#00006F（是、是我想得太复杂了吗……）\x02\x03",

            "#00013F咳咳，说起来……\x01",
            "诈骗的手段非常相似，\x01",
            "也是因为二者是同一个人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9E7")


    #C0702
    ChrTalk(
        0x1D,
        "伊安律师之前也曾说起过……\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x1D,
        (
            "这恐怕正是他\x01",
            "最擅长的\x01",
            "诈骗手法。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x101,
        (
            "#00003F『诈骗犯』敏涅斯，\x01",
            "你的诈骗嫌疑已经不容否认了。\x02\x03",

            "#00013F而且你很有可能就是那个\x01",
            "在帝国从事诈骗行为的嫌疑犯。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x104,
        (
            "#00300F你的劣行已经\x01",
            "完全败露了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x103,
        (
            "#00203F至于诈骗的详细经过，\x01",
            "还是去警察总部的审讯室里\x01",
            "慢慢交代吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0xD,
        "……呜……\x02",
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0xD,
        (
            "你……你们……\x01",
            "你们这些混蛋……！\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xD,
        (
            "我……我这个以完美解决工作\x01",
            "为人生信条的完美主义者……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0710
    ChrTalk(
        0xD,
        "#4S竟……竟会被你们这些乳臭未干的毛孩子……！！\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0xC,
        "敏、敏涅斯先生……\x02",
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
            "……哼，不要得意\x01",
            "得太早。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0xD,
        (
            "不好意思，\x01",
            "我可完全没有\x01",
            "被你们逮捕的打算呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x101,
        "#00005F什么……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x87, 0x1F4)
    Sleep(300)

    #C0715
    ChrTalk(
        0xD,
        "全都过来！\x02",
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
        "呜、呜哇哇！？\x02",
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
        "#00010F魔……魔兽！？\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#00105F而且好像还是\x01",
            "训练相当有素的魔兽……！\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x104,
        "#00310F（这些家伙，难道是……！？）\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xC, 0xB4, 0x3E8, 0x3E8, 0x0)
    Sleep(100)

    #C0720
    ChrTalk(
        0xC,
        "……呜……啊……\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x1D, 0x0, 0x1F4, 0x1388, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    Sleep(300)

    #C0721
    ChrTalk(
        0x1D,
        "迪、迪利克！！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x87, 0x3E8)
    Sleep(300)

    #C0722
    ChrTalk(
        0x1F,
        "#03605F村、村长，危险……！\x02",
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x109,
        (
            "#10107F你……\x01",
            "你明白自己正在\x01",
            "做些什么吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0xD,
        "嗯，当然明白。\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0xD,
        (
            "我想你们应该\x01",
            "也不愿意在这里开战吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0xD,
        (
            "如果你们不希望迪利克先生\x01",
            "或其他村民受伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x101,
        "#00010F呜……\x02",
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xD,
        "好了，赶快给我让出一条路。\x02",
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

    def lambda_103C7():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_103C7)

    def lambda_103D4():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_103D4)

    def lambda_103E1():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_103E1)

    def lambda_103EE():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_103EE)

    def lambda_103FB():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_103FB)

    def lambda_10408():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10408)

    def lambda_10415():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10415)

    def lambda_10422():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10422)

    def lambda_1042F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1042F)
    WaitChrThread(0x105, 1)

    def lambda_10440():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10440)
    Sleep(50)

    def lambda_10458():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10458)
    Sleep(50)

    def lambda_10470():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10470)
    Sleep(50)

    def lambda_10488():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10488)
    Sleep(50)

    def lambda_104A0():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_104A0)
    Sleep(50)

    def lambda_104B8():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104B8)
    Sleep(50)

    def lambda_104D0():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_104D0)
    Sleep(50)

    def lambda_104E8():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_104E8)
    Sleep(50)

    def lambda_10500():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10500)
    Sleep(50)

    def lambda_10518():
        OP_95(0xFE, -1910, 0, 11190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10518)
    WaitChrThread(0x1F, 1)

    def lambda_10536():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10536)
    WaitChrThread(0x1D, 1)

    def lambda_10547():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10547)
    WaitChrThread(0x1E, 1)

    def lambda_10558():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10558)
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

    def lambda_105B7():

        label("loc_105B7")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_105B7")

    QueueWorkItem2(0x101, 1, lambda_105B7)
    Sleep(50)

    def lambda_105CC():

        label("loc_105CC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_105CC")

    QueueWorkItem2(0x102, 1, lambda_105CC)
    Sleep(50)

    def lambda_105E1():

        label("loc_105E1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_105E1")

    QueueWorkItem2(0x103, 1, lambda_105E1)
    Sleep(50)

    def lambda_105F6():

        label("loc_105F6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_105F6")

    QueueWorkItem2(0x104, 1, lambda_105F6)
    Sleep(50)

    def lambda_1060B():

        label("loc_1060B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1060B")

    QueueWorkItem2(0x105, 1, lambda_1060B)
    Sleep(50)

    def lambda_10620():

        label("loc_10620")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_10620")

    QueueWorkItem2(0xC, 1, lambda_10620)
    Sleep(50)

    def lambda_10635():

        label("loc_10635")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_10635")

    QueueWorkItem2(0x1D, 1, lambda_10635)
    Sleep(50)

    def lambda_1064A():

        label("loc_1064A")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1064A")

    QueueWorkItem2(0x1F, 1, lambda_1064A)
    Sleep(50)

    def lambda_1065F():

        label("loc_1065F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1065F")

    QueueWorkItem2(0x1E, 1, lambda_1065F)
    Sleep(100)

    def lambda_10674():

        label("loc_10674")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_10674")

    QueueWorkItem2(0x109, 1, lambda_10674)
    Sleep(50)

    def lambda_10689():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10689)
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

    def lambda_106D5():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_106D5)
    Sleep(50)

    def lambda_106ED():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_106ED)
    Sleep(50)

    def lambda_10705():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10705)
    Sleep(500)

    #C0729
    ChrTalk(
        0xD,
        "呵呵，那就再见吧。\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0xD,
        "不过恐怕也没机会再见了。\x02",
    )

    CloseMessageWindow()

    def lambda_10753():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10753)
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
        "迪、迪利克……！\x02",
    )

    CloseMessageWindow()

    def lambda_108A8():
        OP_95(0xFE, 5240, 0, 18260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_108A8)
    Sleep(100)

    def lambda_108C5():
        OP_95(0xFE, 3790, 0, 19250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_108C5)
    Sleep(100)

    def lambda_108E2():
        OP_95(0xFE, 3560, 0, 17530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_108E2)
    WaitChrThread(0x1D, 1)

    def lambda_10900():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10900)
    WaitChrThread(0x1F, 1)

    def lambda_10911():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10911)
    WaitChrThread(0x1E, 1)

    def lambda_10922():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10922)
    WaitChrThread(0x1E, 1)

    #C0732
    ChrTalk(
        0xC,
        "呜呜……\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        "#00007F可恶，想逃吗……！\x02",
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x103,
        "#00201F我们快追……！\x02",
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

    def lambda_109AB():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_109AB)
    Sleep(100)

    def lambda_109C8():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_109C8)
    Sleep(100)

    def lambda_109E5():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_109E5)
    Sleep(100)

    def lambda_10A02():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10A02)
    Sleep(100)

    def lambda_10A1F():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10A1F)
    Sleep(100)

    def lambda_10A3C():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A3C)
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
        "#00105F啊……！\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x103,
        (
            "#00206F让他彻底\x01",
            "逃走了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x109,
        (
            "#10106F呜呜……真不甘心！\x01",
            "竟然让那种卑鄙之徒\x01",
            "逃脱了……！\x02",
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
            "#00006F……至少村民们都没受伤，\x01",
            "也算不错了。\x02\x03",

            "#00000F能如此收场，\x01",
            "已经值得庆幸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，看来只能把逮捕他的乐趣\x01",
            "留到下次再享受了。\x02\x03",

            "#10300F总之，我们先回村长他们那里，\x01",
            "把整个事件做个报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x101,
        "#00000F嗯，说的对。\x02",
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

    # Function_34_B64C end

    def Function_35_10DE0(): pass

    label("Function_35_10DE0")

    OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 2060, 0, 16660, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_35_10DE0 end

    def Function_36_10E14(): pass

    label("Function_36_10E14")

    OP_97(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 1450, 0, 17650, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_36_10E14 end

    def Function_37_10E48(): pass

    label("Function_37_10E48")

    OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2050, 0, 15310, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_37_10E48 end

    def Function_38_10E7C(): pass

    label("Function_38_10E7C")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 420, 0, 18380, 2000, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_38_10E7C end

    def Function_39_10EB0(): pass

    label("Function_39_10EB0")

    OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 870, 0, 16059, 2000, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)
    Return()

    # Function_39_10EB0 end

    def Function_40_10EE4(): pass

    label("Function_40_10EE4")

    OP_97(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 170, 0, 17060, 2000, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_40_10EE4 end

    def Function_41_10F18(): pass

    label("Function_41_10F18")

    OP_97(0x101, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 7230, 0, -14950, 3500, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_41_10F18 end

    def Function_42_10F4C(): pass

    label("Function_42_10F4C")

    OP_97(0x102, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 5740, 0, -15440, 3500, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_42_10F4C end

    def Function_43_10F80(): pass

    label("Function_43_10F80")

    OP_97(0x103, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 7140, 0, -13390, 3500, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_43_10F80 end

    def Function_44_10FB4(): pass

    label("Function_44_10FB4")

    OP_97(0x104, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 5860, 0, -14270, 3500, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_44_10FB4 end

    def Function_45_10FE8(): pass

    label("Function_45_10FE8")

    OP_97(0x109, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 5870, 0, -12970, 3500, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_45_10FE8 end

    def Function_46_1101C(): pass

    label("Function_46_1101C")

    OP_97(0x105, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 4340, 0, -14470, 3500, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_46_1101C end

    def Function_47_11050(): pass

    label("Function_47_11050")

    OP_97(0x1D, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1D, 1)
    OP_95(0x1D, -1530, 0, 11680, 2000, 0x0)
    OP_93(0x1D, 0x2D, 0x1F4)
    Return()

    # Function_47_11050 end

    def Function_48_11084(): pass

    label("Function_48_11084")

    OP_97(0x1F, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1F, 1)
    OP_95(0x1F, -2380, 0, 13280, 2000, 0x0)
    OP_93(0x1F, 0x2D, 0x1F4)
    Return()

    # Function_48_11084 end

    def Function_49_110B8(): pass

    label("Function_49_110B8")

    OP_97(0x1E, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1E, 1)
    OP_95(0x1E, -720, 0, 12970, 2000, 0x0)
    OP_93(0x1E, 0x2D, 0x1F4)
    Return()

    # Function_49_110B8 end

    def Function_50_110EC(): pass

    label("Function_50_110EC")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_110F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11113")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_110F7")

    label("loc_11113")

    Return()

    # Function_50_110EC end

    def Function_51_11114(): pass

    label("Function_51_11114")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1111F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11136")
    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_1111F")

    label("loc_11136")

    Return()

    # Function_51_11114 end

    def Function_52_11137(): pass

    label("Function_52_11137")


    def lambda_1113C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_1113C)

    def lambda_1114D():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1114D)
    WaitChrThread(0x20, 1)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0x20, 4710, 0, -15670, 6000, 0x0)
    OP_95(0x20, -2120, 0, -1730, 6000, 0x0)
    OP_95(0x20, -2120, 0, 14270, 6000, 0x0)
    Return()

    # Function_52_11137 end

    def Function_53_111AC(): pass

    label("Function_53_111AC")


    def lambda_111B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_111B1)

    def lambda_111C2():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_111C2)
    WaitChrThread(0x21, 1)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0x21, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x21, 830, 0, -10410, 7000, 0x0)
    OP_95(0x21, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x21, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_53_111AC end

    def Function_54_11235(): pass

    label("Function_54_11235")


    def lambda_1123A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_1123A)

    def lambda_1124B():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1124B)
    WaitChrThread(0x22, 1)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0x22, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x22, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x22, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_54_11235 end

    def Function_55_112AA(): pass

    label("Function_55_112AA")


    def lambda_112AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_112AF)

    def lambda_112C0():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_112C0)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0x23, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x23, 830, 0, -10410, 7000, 0x0)
    OP_95(0x23, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x23, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_55_112AA end

    def Function_56_11333(): pass

    label("Function_56_11333")


    def lambda_11338():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_11338)

    def lambda_11349():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_11349)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0x24, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x24, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x24, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_56_11333 end

    def Function_57_113A8(): pass

    label("Function_57_113A8")

    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_57_113A8 end

    def Function_58_113F3(): pass

    label("Function_58_113F3")

    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_58_113F3 end

    def Function_59_1143E(): pass

    label("Function_59_1143E")

    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_59_1143E end

    def Function_60_11489(): pass

    label("Function_60_11489")

    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_60_11489 end

    def Function_61_114D4(): pass

    label("Function_61_114D4")

    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_61_114D4 end

    def Function_62_1151F(): pass

    label("Function_62_1151F")

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

    # Function_62_1151F end

    def Function_63_1157E(): pass

    label("Function_63_1157E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11597")
    Sound(845, 0, 80, 0)
    Sleep(350)
    Jump("Function_63_1157E")

    label("loc_11597")

    Return()

    # Function_63_1157E end

    def Function_64_11598(): pass

    label("Function_64_11598")

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

    def lambda_11652():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11652)
    Sleep(50)

    def lambda_1166A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1166A)
    Sleep(50)

    def lambda_11682():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11682)
    Sleep(50)

    def lambda_1169A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1169A)
    Sleep(50)

    def lambda_116B2():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_116B2)
    Sleep(50)

    def lambda_116CA():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_116CA)
    OP_68(1050, 1500, -9540, 3000)
    SetCameraDistance(17450, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_11703():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11703)
    WaitChrThread(0x101, 1)

    def lambda_11714():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11714)
    WaitChrThread(0x102, 1)

    def lambda_11725():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11725)
    WaitChrThread(0x103, 1)

    def lambda_11736():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11736)
    WaitChrThread(0x104, 1)

    def lambda_11747():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11747)
    WaitChrThread(0x109, 1)

    def lambda_11758():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11758)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0742
    ChrTalk(
        0x101,
        "#00000F到达阿尔摩利卡村了……\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x102,
        "#00105F盖巴尔先生究竟在什么地方呢……？\x02",
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x104,
        (
            "#00300F总之，我们先去那些\x01",
            "比较可疑的地方找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x103,
        (
            "#00200F在寻找过程中，\x01",
            "最好也向村民们打听一下。\x02",
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

    # Function_64_11598 end

    def Function_65_1186B(): pass

    label("Function_65_1186B")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0746
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1195A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_118F0")

    #C0747
    ChrTalk(
        0x101,
        (
            "#00000F……我们去找村长谈谈吧，\x01",
            "说不定他知道些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11956")

    label("loc_118F0")


    #C0748
    ChrTalk(
        0x101,
        (
            "#00003F感觉里面好像有人……\x02\x03",

            "#00000F还是继续去探听消息吧。\x01",
            "住在村子里的村民们\x01",
            "也许会知道些什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11956")

    TalkEnd(0xFF)
    Return()

    label("loc_1195A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1196C")
    TalkEnd(0xFF)
    Jump("loc_11CDB")

    label("loc_1196C")

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
        "#00105F罗伊德，这里……\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x101,
        (
            "#00003F上次来的时候，\x01",
            "这里好像并没有上锁吧……？\x02",
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
        "#10105F刚才的声音是……\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x104,
        "#00303F……感觉里面好像有人呢。\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x103,
        "#00200F嗯，我也这么想。\x02",
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x105,
        "#10302F呵呵，实在是很可疑呢。\x02",
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_11C2D")

    #C0755
    ChrTalk(
        0x101,
        "#00003F莫非是……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0756
    ChrTalk(
        0x101,
        (
            "#00001F……我们还是去找村长谈谈吧，\x01",
            "说不定他知道些什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_11CA2")

    label("loc_11C2D")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0757
    ChrTalk(
        0x101,
        (
            "#00003F……总之，\x01",
            "暂时先别管这里了，\x01",
            "继续去探听消息吧。\x02\x03",

            "#00001F住在村子里的村民们\x01",
            "也许会知道些什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CA2")

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

    label("loc_11CDB")

    Return()

    # Function_65_1186B end

    def Function_66_11CDC(): pass

    label("Function_66_11CDC")

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
            "……我是村长特鲁塔，\x01",
            "打扰一下可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x1D,
        (
            "有人特意过来，\x01",
            "好像是有些话想和你说。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("中年人的声音")

    #A0760
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…………！\x02\x03",

            "能、能不能\x01",
            "让他们回去？\x02\x03",

            "给您添麻烦了，\x01",
            "但我暂时不想见到\x01",
            "任何人。\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x1D,
        "……放心吧。\x02",
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x1D,
        (
            "来见你的人并不是\x01",
            "你的儿子和儿媳。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年人的声音")

    #A0763
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "您、您怎么会知道那种事……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(300)

    #C0764
    ChrTalk(
        0x101,
        (
            "#00003F盖巴尔先生，您能听到吗？\x02\x03",

            "#00000F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年人的声音")

    #A0765
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警、警察……！？\x02\x03",

            "找、找我到底有什么事！？\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x101,
        (
            "#00003F……突然拜访，实在不好意思。\x02\x03",

            "#00000F我们接受了阿鲁姆\x01",
            "先生的委托，\x01",
            "前来寻找您。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年人的声音")

    #A0767
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "什么……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        (
            "#00000F不过，我们并不会\x01",
            "把您强行带走的，\x01",
            "我们也没有那种权限。\x02\x03",

            "#00004F如果您无论如何也不愿意与儿子见面，\x01",
            "我们会向阿鲁姆先生说明情况，\x01",
            "并撤消他的委托。\x02\x03",

            "#00000F情况就是这样，\x01",
            "您可以和我们谈谈吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年人的声音")

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
        "#00100F好像把锁打开了呢。\x02",
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "那我们就进去吧。\x02",
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

    # Function_66_11CDC end

    def Function_67_12277(): pass

    label("Function_67_12277")

    OP_93(0x101, 0x0, 0x0)

    def lambda_12283():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12283)

    def lambda_12298():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12298)
    Return()

    # Function_67_12277 end

    def Function_68_122A5(): pass

    label("Function_68_122A5")

    OP_95(0x102, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x0)

    def lambda_122C5():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_122C5)

    def lambda_122DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_122DA)
    Return()

    # Function_68_122A5 end

    def Function_69_122E7(): pass

    label("Function_69_122E7")

    OP_95(0x103, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x103, 0x0, 0x0)

    def lambda_12307():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12307)

    def lambda_1231C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1231C)
    Return()

    # Function_69_122E7 end

    def Function_70_12329(): pass

    label("Function_70_12329")

    OP_95(0x104, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_12349():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12349)

    def lambda_1235E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1235E)
    Return()

    # Function_70_12329 end

    def Function_71_1236B(): pass

    label("Function_71_1236B")

    OP_95(0x109, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x109, 0x0, 0x0)

    def lambda_1238B():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1238B)

    def lambda_123A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_123A0)
    Return()

    # Function_71_1236B end

    def Function_72_123AD(): pass

    label("Function_72_123AD")

    OP_95(0x105, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x105, 0x0, 0x0)

    def lambda_123CD():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_123CD)

    def lambda_123E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_123E2)
    Return()

    # Function_72_123AD end

    def Function_73_123EF(): pass

    label("Function_73_123EF")

    OP_95(0x1D, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x0)

    def lambda_1240F():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1240F)

    def lambda_12424():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_12424)
    Return()

    # Function_73_123EF end

    def Function_74_12431(): pass

    label("Function_74_12431")

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
        "我爸爸就在里面吧？\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x101,
        "#00000F嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x102,
        (
            "#00100F事先已经打过了招呼，\x01",
            "他同意与你们见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x26,
        "哦哦～谢谢！\x02",
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x26,
        (
            "他为什么要躲藏\x01",
            "在这种地方呢……\x01",
            "算啦，不管怎么说，真是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0777
    ChrTalk(
        0x27,
        (
            "呵呵，太好了，阿鲁姆，\x01",
            "终于可以见到\x01",
            "公公了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x27,
        (
            "当时没能请他老人家参加我们\x01",
            "的结婚仪式，借着这次见面的机会，\x01",
            "可要好好道个歉才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0779
    ChrTalk(
        0x26,
        (
            "啊啊，艾娅莉……\x01",
            "你的心灵为何\x01",
            "如此纯洁美丽？\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x26,
        (
            "你那如同白雪般清澈的心，\x01",
            "将我的心牢牢吸引……\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x27,
        "啊啊，阿鲁姆……\x02",
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x103,
        "#00203F#4S请二位赶快进入仓库吧。\x02",
    )

    CloseMessageWindow()

    def lambda_12768():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_12768)
    Sleep(50)

    def lambda_12778():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_12778)
    Sleep(300)

    #C0783
    ChrTalk(
        0x26,
        "啊……！？\x02",
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x27,
        "呵呵呵，真不好意思哦。\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x27,
        (
            "来，阿尔米也来道个歉，\x01",
            "对·不·起·哟。\x02",
        )
    )

    CloseMessageWindow()

    #N0786
    NpcTalk(
        0x27,
        "婴儿",
        "唔唔。\x02",
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x27,
        "好有礼貌哦～\x02",
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
        "#10106F（和、和他们说话真是好累……）\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x1D,
        (
            "总、总之，\x01",
            "盖巴尔先生还在里面等你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x105,
        (
            "#10302F呵呵……\x01",
            "请尽情畅谈\x01",
            "一番吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x26,
        "嗯，那当然。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0792
    ChrTalk(
        0x26,
        "我们走吧，艾娅莉。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0793
    ChrTalk(
        0x27,
        "嗯，阿鲁姆。\x02",
    )

    CloseMessageWindow()

    def lambda_12980():
        OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_12980)
    Sleep(300)

    def lambda_1299D():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1299D)

    def lambda_129B2():

        label("loc_129B2")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_129B2")

    QueueWorkItem2(0x101, 1, lambda_129B2)
    Sleep(50)

    def lambda_129C7():

        label("loc_129C7")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_129C7")

    QueueWorkItem2(0x102, 1, lambda_129C7)
    Sleep(50)

    def lambda_129DC():

        label("loc_129DC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_129DC")

    QueueWorkItem2(0x103, 1, lambda_129DC)
    Sleep(50)

    def lambda_129F1():

        label("loc_129F1")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_129F1")

    QueueWorkItem2(0x104, 1, lambda_129F1)
    Sleep(50)

    def lambda_12A06():

        label("loc_12A06")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_12A06")

    QueueWorkItem2(0x109, 1, lambda_12A06)
    Sleep(50)

    def lambda_12A1B():

        label("loc_12A1B")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_12A1B")

    QueueWorkItem2(0x105, 1, lambda_12A1B)
    Sleep(50)

    def lambda_12A30():

        label("loc_12A30")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_12A30")

    QueueWorkItem2(0x1D, 1, lambda_12A30)
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

    # Function_74_12431 end

    def Function_75_12AC2(): pass

    label("Function_75_12AC2")

    OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x0)

    def lambda_12AE2():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12AE2)

    def lambda_12AF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12AF7)
    Return()

    # Function_75_12AC2 end

    def Function_76_12B04(): pass

    label("Function_76_12B04")

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
        "各位，真是太谢谢你们了。\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x26,
        (
            "多亏你们的帮忙，我才能见到父亲，\x01",
            "并把艾娅莉和阿尔米介绍给他。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x27,
        (
            "呵呵，公公似乎也\x01",
            "非常高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x101,
        (
            "#00000F哪里，能帮上忙就好。\x02\x03",

            "#00005F那个，盖巴尔先生他……\x01",
            "还在里面吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x26,
        (
            "嗯，他说还要在里面思考一些事情，\x01",
            "稍后再回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x27,
        (
            "在我们谈话到一半时，他突然转过了身，\x01",
            "然后就再也没让我们看到他的脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x27,
        "究竟是怎么了呢……\x02",
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
        "唔……\x02",
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x102,
        "#00105F这、这……\x02",
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x104,
        "#00304F品行恶劣的议员……原来也是有血有泪的啊。\x02",
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x103,
        "#00205F真是吃惊。\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x105,
        (
            "#10304F呵呵……\x01",
            "算啦，身为男人，\x01",
            "你就不要对这种事情刨根问底了。\x02",
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
            "#00009F哈哈，他肯定不要紧的，\x01",
            "请不必担心。\x02\x03",

            "#00000F二位今后有什么打算？\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x26,
        (
            "嗯，总算与父亲\x01",
            "重逢……\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x26,
        (
            "我们今后\x01",
            "一定会继续\x01",
            "保持联系。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x27,
        (
            "虽然公公与婆婆之间\x01",
            "曾发生过那样的事情，\x01",
            "很难轻易淡忘……\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x27,
        (
            "但我们将来一定会把他\x01",
            "接到利贝尔王国。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x109,
        (
            "#10102F是吗……\x01",
            "呵呵，但愿今后一切顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x26,
        (
            "父亲如今已经\x01",
            "卸下了议员的职位，\x01",
            "我们总有一天可以团圆。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x26,
        (
            "嗯……光明无限的未来\x01",
            "在等待着我们！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0814
    ChrTalk(
        0x26,
        "没错吧？艾娅莉！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0815
    ChrTalk(
        0x27,
        "嗯！阿鲁姆！\x02",
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x27,
        (
            "在初次怀抱这孩子的时候，\x01",
            "我们便曾相互许下过誓言。\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x27,
        (
            "今后要给阿尔米\x01",
            "生下许许多多的弟弟妹妹……\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x26,
        (
            "……说的没错，你我二人，\x01",
            "还有无数可爱的孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x26,
        (
            "大家将会共建\x01",
            "大陆第一家族。\x02",
        )
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x26,
        "啊啊，艾娅莉，我好爱你！\x02",
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x27,
        "我也爱你，阿鲁姆！！\x02",
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
            "#00006F（我根本就没想\x01",
            "  问这些啊……\x01",
            "  算、算了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x104,
        (
            "#00300F那么，这样应该\x01",
            "就算是完成委托了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1331E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1331E)
    Sleep(50)

    def lambda_1332E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1332E)
    Sleep(300)

    #C0824
    ChrTalk(
        0x26,
        (
            "嗯，承蒙各位的帮助。\x01",
            "真是不知该如何\x01",
            "感谢你们才好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x27,
        (
            "再过不久，\x01",
            "我们就要回利贝尔了，\x01",
            "真是很感谢各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x103,
        "#00202F嗯，还请一路小心啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #C0827
    ChrTalk(
        0x26,
        (
            "艾娅莉，\x01",
            "难得来此，我们不如\x01",
            "在这里稍微观光一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    #C0828
    ChrTalk(
        0x27,
        "嗯，阿鲁姆，都听你的。\x02",
    )

    CloseMessageWindow()
    OP_93(0x27, 0x87, 0x0)

    def lambda_1343E():
        OP_9B(0x1, 0xFE, 0xB4, 0x262, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1343E)
    Sleep(100)

    def lambda_13456():
        OP_95(0xFE, 13050, 3500, 45510, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_13456)
    WaitChrThread(0x26, 1)
    OP_93(0x27, 0xE1, 0x1F4)
    Sleep(500)
    OP_68(12010, 5000, 41990, 4000)
    MoveCamera(340, 27, 0, 4000)
    OP_6E(600, 4000)

    def lambda_134A3():
        OP_95(0xFE, 7890, 3500, 42250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_134A3)

    def lambda_134BD():
        OP_95(0xFE, 6900, 3500, 42860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_134BD)

    def lambda_134D7():

        label("loc_134D7")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_134D7")

    QueueWorkItem2(0x101, 1, lambda_134D7)
    Sleep(50)

    def lambda_134EC():

        label("loc_134EC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_134EC")

    QueueWorkItem2(0x102, 1, lambda_134EC)
    Sleep(50)

    def lambda_13501():

        label("loc_13501")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_13501")

    QueueWorkItem2(0x103, 1, lambda_13501)
    Sleep(50)

    def lambda_13516():

        label("loc_13516")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_13516")

    QueueWorkItem2(0x104, 1, lambda_13516)
    Sleep(50)

    def lambda_1352B():

        label("loc_1352B")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_1352B")

    QueueWorkItem2(0x109, 1, lambda_1352B)
    Sleep(50)

    def lambda_13540():

        label("loc_13540")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_13540")

    QueueWorkItem2(0x105, 1, lambda_13540)
    Sleep(50)

    def lambda_13555():

        label("loc_13555")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_13555")

    QueueWorkItem2(0x1D, 1, lambda_13555)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)

    def lambda_1356F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1356F)

    def lambda_1357C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1357C)
    OP_6F(0x79)

    def lambda_1358B():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1358B)

    def lambda_13598():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_13598)
    Sleep(500)

    #C0829
    ChrTalk(
        0x26,
        "啊哈哈，艾娅莉⊥\x02",
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x27,
        "呵呵呵，亲爱的⊥\x02",
    )

    CloseMessageWindow()

    #N0831
    NpcTalk(
        0x27,
        "婴儿",
        "唔唔～\x02",
    )

    CloseMessageWindow()

    def lambda_135E5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_135E5)

    def lambda_135F2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_135F2)
    Sleep(300)

    def lambda_13602():
        OP_95(0xFE, 4830, 2000, 38020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_13602)

    def lambda_1361C():
        OP_95(0xFE, 4470, 2000, 39100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1361C)
    Sleep(1000)
    OP_68(15240, 5000, 43490, 5000)
    MoveCamera(5, 29, 0, 5000)
    OP_6E(600, 5000)
    WaitChrThread(0x26, 1)

    def lambda_13662():
        OP_95(0xFE, 1480, 2000, 40200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_13662)
    Sleep(100)

    def lambda_1367F():
        OP_95(0xFE, 1940, 2000, 41000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1367F)
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
            "#00006F……从始至终，\x01",
            "这两个人给人的印象\x01",
            "都十分强烈啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，是啊。\x01",
            "如此旁若无人，\x01",
            "还真有点让人羡慕呢……\x02\x03",

            "#00104F连我也久违地\x01",
            "想和父母见面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x109,
        (
            "#10105F艾莉小姐……\x02\x03",

            "#10109F呵呵，说的没错呢。\x01",
            "受他们的影响，我也想\x01",
            "为妈妈多尽一些孝了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x102, 500)
    Sleep(300)

    #C0835
    ChrTalk(
        0x1D,
        (
            "嗯，我也向各位\x01",
            "道声谢吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_137E6():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_137E6)
    Sleep(50)

    def lambda_137F6():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_137F6)
    Sleep(50)

    def lambda_13806():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13806)
    Sleep(50)

    def lambda_13816():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13816)
    Sleep(50)

    def lambda_13826():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13826)
    Sleep(50)

    def lambda_13836():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13836)
    Sleep(300)

    #C0836
    ChrTalk(
        0x1D,
        (
            "在盖巴尔先生情绪平复，\x01",
            "返回市里之前，\x01",
            "我会仔细照料他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x101,
        (
            "#00004F嗯，非常感谢\x01",
            "您的帮助。\x02\x03",

            "#00000F我们差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x105,
        "#10300F呵呵，知道了。\x02",
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
            "任务【寻找自幼分离的父亲】\x07\x00",
            "完成！\x02",
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

    # Function_76_12B04 end

    def Function_77_139DA(): pass

    label("Function_77_139DA")

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

    def lambda_13B0F():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_13B0F)

    def lambda_13B29():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13B29)
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

    def lambda_13C87():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_13C87)

    def lambda_13CA1():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13CA1)
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
            "#10406F#6P嗯，已经顺利降落了……\x02\x03",

            "#10408F……这里好像是\x01",
            "村中的花田吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x101,
        (
            "#00013F#6P嗯……\x01",
            "不过变化真是很大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x103,
        (
            "#00206F#12P……说不定，这也是\x01",
            "琪雅觉醒所造成的影响。\x02",
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
            "#00201F#5P蔡特，\x01",
            "附近有没有幻兽的气息？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13E18():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13E18)
    Sleep(0)

    def lambda_13E28():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_13E28)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0844
    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C#N唔……目前来看，\x01",
            "不会有幻兽出现。\x02\x03",

            "#01200F在这里设置法阵\x01",
            "应该没有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0845
    ChrTalk(
        0x101,
        (
            "#00003F#5P明白了。\x02\x03",

            "#00001F那我们先去和\x01",
            "特鲁塔村长打声招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x103,
        (
            "#00202F#11P好的，\x01",
            "我们走吧。\x02",
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

    # Function_77_139DA end

    def Function_78_13F28(): pass

    label("Function_78_13F28")

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

    # Function_78_13F28 end

    def Function_79_13F6D(): pass

    label("Function_79_13F6D")

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

    # Function_79_13F6D end

    def Function_80_13FBB(): pass

    label("Function_80_13FBB")

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

    # Function_80_13FBB end

    def Function_81_14020(): pass

    label("Function_81_14020")

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

    def lambda_14122():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14122)
    BeginChrThread(0x101, 1, 0, 82)
    Sleep(1000)

    def lambda_1413C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_1413C)
    BeginChrThread(0x103, 1, 0, 83)
    Sleep(1000)

    def lambda_14156():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_14156)
    BeginChrThread(0x105, 1, 0, 84)
    Sleep(1000)

    def lambda_14170():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_14170)
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
            "#10404F#12P那么……\x02\x03",

            "#10400F我们这就向\x01",
            "古战场出发如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，虽然还不知道\x01",
            "那股抵抗势力是由什么人结成的。\x02\x03",

            "#00001F但我们说不定可以\x01",
            "同他们联手合作。\x02",
        )
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0x103,
        (
            "#00201F#5P是啊……\x01",
            "的确有一探的价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x107,
        "#01200F#11P#3C那就出发吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 17950, 0, 16250, 180)
    SetScenarioFlags(0x1A1, 5)
    OP_29(0xAF, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_81_14020 end

    def Function_82_142C3(): pass

    label("Function_82_142C3")

    OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x101, 17500, 0, 14850, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_82_142C3 end

    def Function_83_142EE(): pass

    label("Function_83_142EE")

    OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x103, 16900, 0, 16550, 2000, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_83_142EE end

    def Function_84_14319(): pass

    label("Function_84_14319")

    OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x105, 18950, 0, 16100, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_84_14319 end

    def Function_85_14344(): pass

    label("Function_85_14344")

    OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x107, 18000, 0, 17750, 2000, 0x0)
    OP_93(0x107, 0xB4, 0x1F4)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_85_14344 end

    def Function_86_14373(): pass

    label("Function_86_14373")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    Call(0, 87)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14634")
    Fade(500)
    OP_68(15510, 1350, -23710, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14539")
    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x105, 23130, 0, -30790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x103, 20790, 0, -30560, 315)
    SetChrPos(0x109, 22200, 0, -31420, 315)

    def lambda_14470():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14470)

    def lambda_1448A():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1448A)

    def lambda_144A4():
        OP_95(0xFE, 16930, 0, -24390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_144A4)

    def lambda_144BE():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_144BE)

    def lambda_144D8():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_144D8)

    def lambda_144F2():
        OP_95(0xFE, 15900, 0, -25220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_144F2)
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
    Jump("loc_1462F")

    label("loc_14539")

    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x109, 21290, 0, -30060, 315)
    SetChrPos(0x105, 22810, 0, -31000, 315)

    def lambda_14593():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14593)

    def lambda_145AD():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_145AD)

    def lambda_145C7():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_145C7)

    def lambda_145E1():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_145E1)

    def lambda_145FB():
        OP_95(0xFE, 16410, 0, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_145FB)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    label("loc_1462F")

    Jump("loc_14AA5")

    label("loc_14634")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14889")
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

    def lambda_146E3():
        OP_95(0xFE, 15110, 0, -21470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_146E3)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1481B")
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
    Jump("loc_1487A")

    label("loc_1481B")

    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x109, 11800, 0, -20300, 315)
    SetChrPos(0x105, 13220, 0, -21400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1487A")

    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_14AA5")

    label("loc_14889")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14A3C")
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
    Jump("loc_14A9B")

    label("loc_14A3C")

    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x109, 960, 0, -14300, 0)
    SetChrPos(0x105, 2380, 0, -15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_14A9B")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_14AA5")


    #C0851
    ChrTalk(
        0x105,
        (
            "#12P#10302F嘿，真是个风景优美的地方啊。\x02\x03",

            "#10304F好像是叫『阿尔摩利卡村』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x102,
        (
            "#00100F嗯，没错。\x02\x03",

            "#00104F养蜂业、农业和畜牧业\x01",
            "是这个村子的主要产业……\x02\x03",

            "#00102F这个村子也是至今仍然流传着\x01",
            "『神狼』传说的为数不多的地方之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x101,
        (
            "#00004F说起来……\x01",
            "也是特别任务支援科\x01",
            "初次进行市外活动的场所啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x109,
        (
            "#12P#10100F黑手党的军犬事件……\x01",
            "呵呵，真让人怀念。\x02\x03",

            "#10103F当时我们以委任的形式\x01",
            "把自己的调查工作交付给了\x01",
            "特别任务支援科呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x104,
        (
            "#00306F那也是因为\x01",
            "前司令太无能了。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，自从那次的事件之后，\x01",
            "蔡特就与我们一起行动了。\x02\x03",

            "#00104F在最为危机的关头，多亏有蔡特赶来相助，\x01",
            "我们才能顺利解决那起事件。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14D8B")

    #C0857
    ChrTalk(
        0x101,
        (
            "#00009F自那以后，\x01",
            "蔡特又帮过我们无数忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x103,
        (
            "#6P#00202F嗯，不仅是战斗，\x01",
            "蔡特在各种场合\x01",
            "都会为我们提供援助。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF4")

    label("loc_14D8B")


    #C0859
    ChrTalk(
        0x101,
        (
            "#00009F自那以后，\x01",
            "蔡特又帮过我们无数忙呢。\x02\x03",

            "#00004F不仅是战斗，\x01",
            "蔡特在各种场合\x01",
            "都会为我们提供援助。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DF4")


    #C0860
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，经常帮助你们的\x01",
            "好像并不是只有蔡特啊。\x02\x03",

            "#10309F不如说……被抢走风头\x01",
            "正是支援科的宿命。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14E65():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14E65)

    def lambda_14E72():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14E72)

    def lambda_14E7F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14E7F)

    def lambda_14E8C():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14E8C)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F29")

    def lambda_14F09():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14F09)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_14F29")

    Sleep(1000)

    #C0861
    ChrTalk(
        0x109,
        "#6P#10106F瓦、瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x104,
        "#00306F真是的，不要戳我们的痛处啊。\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x101,
        (
            "#00012F算、算了……\x01",
            "通过那些事情，我们也得到了成长，\x01",
            "至于风头什么的……还是今后再争取吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x14E, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF8")
    SetChrPos(0x0, 15500, 0, -23930, 315)
    Jump("loc_1502D")

    label("loc_14FF8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1501C")
    SetChrPos(0x0, 11350, 0, -18420, 315)
    Jump("loc_1502D")

    label("loc_1501C")

    SetChrPos(0x0, 890, 0, -13080, 315)

    label("loc_1502D")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15051")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_15051")

    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_86_14373 end

    def Function_87_1505D(): pass

    label("Function_87_1505D")

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

    # Function_87_1505D end

    def Function_88_1513E(): pass

    label("Function_88_1513E")

    Sleep(500)
    Sound(459, 0, 100, 0)
    Sleep(1200)
    Sleep(1500)
    Sound(492, 0, 90, 0)
    Return()

    # Function_88_1513E end

    def Function_89_15154(): pass

    label("Function_89_15154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15451")
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

    def lambda_15242():
        OP_93(0x107, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_15242)
    Sleep(0)

    def lambda_15252():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15252)
    Sleep(0)

    def lambda_15262():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15262)
    Sleep(0)

    def lambda_15272():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15272)
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
            "#12P#00000F这辆导力车是……\x01",
            "哈罗德先生的车啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x103,
        (
            "#6P#00200F乌尔努公司制造的小型轿车……\x01",
            "我们以前还坐过一次，\x01",
            "不会认错的。\x02\x03",

            "#00203F据村长所说，哈罗德先生\x01",
            "暂时住在旅店的二层。\x02",
        )
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x105,
        (
            "#12P#10403F我们现在需要一切情报。\x02\x03",

            "#10400F在离开村子之前，\x01",
            "最好去和他打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0867
    ChrTalk(
        0x101,
        "#6P#00000F嗯，那就走吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11950, 0, -17850, 0)
    EventEnd(0x5)
    Jump("loc_154B8")

    label("loc_15451")

    EventBegin(0x1)

    #C0868
    ChrTalk(
        0x101,
        (
            "#00000F哈罗德先生\x01",
            "暂住在村子里。\x02\x03",

            "在离开村子之前，\x01",
            "先去旅店二层拜访他吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)

    label("loc_154B8")

    Return()

    # Function_89_15154 end

    SaveToFile()

Try(main)
