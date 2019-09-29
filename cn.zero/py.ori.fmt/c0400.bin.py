from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0400.bin",                # FileName
        "c0400",                    # MapName
        "c0400",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0400",                  # 0
        "索菲尤",                 # 1
        "揽客员皮姆",             # 2
        "珀利塞",                 # 3
        "塔普",                   # 4
        "拉曼达",                 # 5
        "缇乔",                   # 6
        "兔女郎",                 # 7
        "凯特巡警",               # 8
        "罗伯兹主任",             # 9
        "艾丝蒂尔",               # 10
        "约修亚",                 # 11
        "滴",                     # 12
        "艾莉",                   # 13
        "麦克道尔市长",           # 14
        "阿奈斯特秘书",           # 15
        "市长车",                 # 16
        "莉夏",                   # 17
        "伊莉娅",                 # 18
        "银",                     # 19
        "导游",                   # 20
        "游客",                   # 21
        "游客",                   # 22
        "游客",                   # 23
        "中央广场",               # 24
        "西街",                   # 25
        "行政区",                 # 26
        "住宅街",                 # 27
        "欢乐街",                 # 28
        "东街",                   # 29
        "旧城区",                 # 30
        "港湾区",                 # 31
        "ＩＢＣ",                 # 32
        "站前街道",               # 33
        "后巷",                   # 34
        "乌尔斯拉间道",           # 35
        "东克洛斯贝尔街道",       # 36
        "西克洛斯贝尔街道",       # 37
        "玛因兹山道",             # 38
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch30600.itc",                   # 08
        "chr/ch29300.itc",                   # 09
        "chr/ch00600.itc",                   # 0A
        "chr/ch00700.itc",                   # 0B
        "chr/ch08700.itc",                   # 0C
        "chr/ch00102.itc",                   # 0D
        "chr/ch24400.itc",                   # 0E
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4360,    0,       -10960,  310,  261,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   14,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   2,   0,   16,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   3,   0,   17,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2380,   1990,    18079,   225,  389,  0x0, 0,   8,   0,   0,   4,   0,   19,  255,  0)
    DeclNpc(-9439,   1759,    22709,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-9149,   1759,    24250,   90,   405,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-7849,   1799,    23100,   315,  405,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-7650,   1759,    24250,   270,  405,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-12699,  1899,    26899,   180,  405,  0x0, 0,   13,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 44,  -2.0,                  19.0,                  1.0,                   2626.5625,             [0.04878048598766327,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.09756097197532654,   -3.799999952316284,    -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 46,  -2.0,                  19.0,                  1.0,                   2626.5625,             [0.04878048598766327,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.09756097197532654,   -3.799999952316284,    -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 60,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])
    DeclEvent(0x0000, 0, 61,  -26.5,                 16.739999771118164,    -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   8.833333969116211,     -8.369999885559082,    0.10000000894069672,   1.0])
    DeclEvent(0x0000, 0, 22,  -8.279999732971191,    24.030000686645508,    1.7599999904632568,    1640.25,               [0.07856739312410355,  0.07856745272874832,   -0.0,                  0.0,                   -0.07856745272874832,  0.07856739312410355,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.5385138988494873,    -1.237436056137085,    -0.35199999809265137,  1.0])
    DeclEvent(0x0000, 0, 44,  7.0,                   22.0,                  1.0,                   612.5625,              [0.222222238779068,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.09090909361839294,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.5555557012557983,   -2.0,                  -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 46,  7.0,                   22.0,                  1.0,                   612.5625,              [0.222222238779068,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.09090909361839294,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.5555557012557983,   -2.0,                  -0.20000000298023224,  1.0])

    DeclActor(-8160,   1770,    13680,   4000,    -8160,   2270,    13680,   0x007C, 0,  29, 0x0000)
    DeclActor(9850,    1760,    27000,   3500,    9850,    3260,    27000,   0x007C, 0,  30, 0x0000)
    DeclActor(16850,   0,       3030,    3500,    16850,   1500,    3030,    0x007C, 0,  31, 0x0000)
    DeclActor(-7810,   1760,    24750,   2500,    -7810,   3260,    24750,   0x007C, 0,  32, 0x0000)
    DeclActor(-4370,   0,       2950,    3500,    -4370,   500,     2950,    0x007C, 0,  33, 0x0000)

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "中央广场")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "西街")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "行政区")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "住宅街")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "欢乐街")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "东街")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "旧城区")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "站前街道")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "后巷")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(53.86000061035156, 0.0, -135.27000427246094, 0x0000, 0x0051, "")
    PlaceName(143.6199951171875, 0.0, -91.8499984741211, 0x0000, 0x0054, "")
    PlaceName(94.7699966430664, 0.0, -148.6300048828125, 0x0000, 0x0057, "")
    PlaceName(52.61000061035156, 0.0, -86.83999633789062, 0x0000, 0x0053, "")
    PlaceName(86.83999633789062, 0.0, -46.7599983215332, 0x0000, 0x0053, "")
    PlaceName(2.0899999141693115, 0.0, -95.19000244140625, 0x0000, 0x0053, "")
    PlaceName(-14.199999809265137, 0.0, -60.119998931884766, 0x0000, 0x0053, "")
    PlaceName(25.889999389648438, 0.0, -6.679999828338623, 0x0000, 0x0052, "")
    PlaceName(33.81999969482422, 0.0, -28.389999389648438, 0x0000, 0x0053, "")
    PlaceName(48.43000030517578, 0.0, -42.59000015258789, 0x0000, 0x0053, "")
    PlaceName(96.02999877929688, 0.0, 75.98999786376953, 0x0000, 0x0051, "")
    PlaceName(283.07000732421875, 0.0, -150.3000030517578, 0x0000, 0x0052, "")
    PlaceName(254.67999267578125, 0.0, -301.44000244140625, 0x0000, 0x0053, "")
    PlaceName(232.97000122070312, 0.0, -270.5400085449219, 0x0000, 0x0053, "")
    PlaceName(109.38999938964844, 0.0, -131.92999267578125, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_A04",          # 00, 0
        "Function_1_ABC",          # 01, 1
        "Function_2_AE7",          # 02, 2
        "Function_3_C74",          # 03, 3
        "Function_4_DFB",          # 04, 4
        "Function_5_E26",          # 05, 5
        "Function_6_E70",          # 06, 6
        "Function_7_13BE",         # 07, 7
        "Function_8_178F",         # 08, 8
        "Function_9_24FB",         # 09, 9
        "Function_10_253D",        # 0A, 10
        "Function_11_25B3",        # 0B, 11
        "Function_12_26AC",        # 0C, 12
        "Function_13_3620",        # 0D, 13
        "Function_14_4221",        # 0E, 14
        "Function_15_435A",        # 0F, 15
        "Function_16_4EA9",        # 10, 16
        "Function_17_59FB",        # 11, 17
        "Function_18_662F",        # 12, 18
        "Function_19_6812",        # 13, 19
        "Function_20_69B4",        # 14, 20
        "Function_21_6C8E",        # 15, 21
        "Function_22_6DA5",        # 16, 22
        "Function_23_71AB",        # 17, 23
        "Function_24_7970",        # 18, 24
        "Function_25_79F1",        # 19, 25
        "Function_26_7DD8",        # 1A, 26
        "Function_27_8712",        # 1B, 27
        "Function_28_8782",        # 1C, 28
        "Function_29_879D",        # 1D, 29
        "Function_30_8826",        # 1E, 30
        "Function_31_88A7",        # 1F, 31
        "Function_32_891B",        # 20, 32
        "Function_33_898F",        # 21, 33
        "Function_34_8A03",        # 22, 34
        "Function_35_8ACA",        # 23, 35
        "Function_36_8AE6",        # 24, 36
        "Function_37_8B02",        # 25, 37
        "Function_38_8B1E",        # 26, 38
        "Function_39_8B3A",        # 27, 39
        "Function_40_8B56",        # 28, 40
        "Function_41_8B72",        # 29, 41
        "Function_42_8BCA",        # 2A, 42
        "Function_43_8E21",        # 2B, 43
        "Function_44_967C",        # 2C, 44
        "Function_45_99AB",        # 2D, 45
        "Function_46_A333",        # 2E, 46
        "Function_47_B7C2",        # 2F, 47
        "Function_48_B808",        # 30, 48
        "Function_49_C121",        # 31, 49
        "Function_50_CEB5",        # 32, 50
        "Function_51_CF47",        # 33, 51
        "Function_52_CF84",        # 34, 52
        "Function_53_CFE1",        # 35, 53
        "Function_54_CFF7",        # 36, 54
        "Function_55_D212",        # 37, 55
        "Function_56_D24F",        # 38, 56
        "Function_57_D28C",        # 39, 57
        "Function_58_D2C9",        # 3A, 58
        "Function_59_D306",        # 3B, 59
        "Function_60_DE70",        # 3C, 60
        "Function_61_E249",        # 3D, 61
        "Function_62_E430",        # 3E, 62
        "Function_63_E44C",        # 3F, 63
        "Function_64_E468",        # 40, 64
    ))


    def Function_0_A04(): pass

    label("Function_0_A04")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A44"),
        (1, "loc_A50"),
        (2, "loc_A5C"),
        (3, "loc_A68"),
        (4, "loc_A74"),
        (5, "loc_A80"),
        (6, "loc_A8C"),
        (SWITCH_DEFAULT, "loc_A98"),
    )


    label("loc_A44")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A50")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A5C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A68")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A74")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A80")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A8C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_A98")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_AA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AA4")

    label("loc_ABB")

    Return()

    # Function_0_A04 end

    def Function_1_ABC(): pass

    label("Function_1_ABC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE6")
    OP_94(0xFE, 0xED8, 0xFFFFEC96, 0x1AE0, 0xFFFFDE22, 0x3E8)
    Sleep(300)
    Jump("Function_1_ABC")

    label("loc_AE6")

    Return()

    # Function_1_ABC end

    def Function_2_AE7(): pass

    label("Function_2_AE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C73")
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -18740, 10, 10280, 1500, 0x0)
    OP_95(0xFE, -2040, 1770, 9880, 1500, 0x0)
    OP_95(0xFE, 30970, 0, 12150, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 30210, 0, 8600, 270)
    OP_95(0xFE, 17210, 0, 8600, 1500, 0x0)
    OP_95(0xFE, 15010, 0, 6790, 1500, 0x0)
    OP_95(0xFE, 10210, 0, -960, 1500, 0x0)
    OP_95(0xFE, 8450, 0, -7690, 1500, 0x0)
    OP_95(0xFE, 10100, 0, -11960, 1500, 0x0)
    OP_95(0xFE, 28170, 0, -38880, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    Jump("Function_2_AE7")

    label("loc_C73")

    Return()

    # Function_2_AE7 end

    def Function_3_C74(): pass

    label("Function_3_C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF4")

    label("loc_C82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEF")
    OP_95(0xFE, 4650, 0, 3100, 1000, 0x0)
    OP_95(0xFE, -450, 0, 800, 1000, 0x0)
    OP_93(0xFE, 0x119, 0x0)
    Sleep(1500)
    OP_95(0xFE, 4150, 0, 3130, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("loc_C82")

    label("loc_CEF")

    Jump("loc_DFA")

    label("loc_CF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DFA")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("loc_CF4")

    label("loc_DFA")

    Return()

    # Function_3_C74 end

    def Function_4_DFB(): pass

    label("Function_4_DFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E25")
    OP_94(0xFE, 0xFFFFEA7A, 0x4E98, 0x118, 0x4682, 0x3E8)
    Sleep(300)
    Jump("Function_4_DFB")

    label("loc_E25")

    Return()

    # Function_4_DFB end

    def Function_5_E26(): pass

    label("Function_5_E26")

    ClearChrFlags(0x17, 0x80)
    OP_78(0x4, 0x17)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -5300, 0, 1800, 100)
    OP_D3(0x17, 0x0, 0x186A0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_70(0x4, 0x0)
    Return()

    # Function_5_E26 end

    def Function_6_E70(): pass

    label("Function_6_E70")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F44")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F17")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_F36")

    label("loc_F17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F36")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_F36")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A2")

    label("loc_F44")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1001")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD4")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_FF3")

    label("loc_FD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF3")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_FF3")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A2")

    label("loc_1001")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107A")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_1099")

    label("loc_107A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1099")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_1099")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A2")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C1")
    Event(0, 45)
    Jump("loc_10DA")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DA")
    Event(0, 59)

    label("loc_10DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_10EE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 48)
    Jump("loc_114D")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1102")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 49)
    Jump("loc_114D")

    label("loc_1102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1116")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 54)
    Jump("loc_114D")

    label("loc_1116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_112A")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 23)
    Jump("loc_114D")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_113E")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 24)
    Jump("loc_114D")

    label("loc_113E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_114D")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 26)

    label("loc_114D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1160")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_134B")

    label("loc_1160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")
    SetChrFlags(0xA, 0x10)

    label("loc_1178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1191")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_1191")

    Jump("loc_134B")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_11B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11AD")
    SetChrFlags(0xA, 0x10)

    label("loc_11AD")

    Jump("loc_134B")

    label("loc_11B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11C0")
    Jump("loc_134B")

    label("loc_11C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_11F1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_134B")

    label("loc_11F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1212")
    ClearChrFlags(0xF, 0x80)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    Jump("loc_134B")

    label("loc_1212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1220")
    Jump("loc_134B")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1251")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jump("loc_134B")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12B2")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127C")
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    label("loc_127C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A8")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_12AD")

    label("loc_12A8")

    ClearChrFlags(0x10, 0x80)

    label("loc_12AD")

    Jump("loc_134B")

    label("loc_12B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1302")
    SetChrPos(0x8, -9610, 1770, 24250, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12DD")
    Jump("loc_12FD")

    label("loc_12DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_12EB")
    Jump("loc_12FD")

    label("loc_12EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_12FD")
    ClearChrFlags(0x14, 0x80)

    label("loc_12FD")

    Jump("loc_134B")

    label("loc_1302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1315")
    SetChrFlags(0xA, 0x10)
    Jump("loc_134B")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1323")
    Jump("loc_134B")

    label("loc_1323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_133D")
    TurnDirection(0xB, 0xA, 0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_134B")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_134B")
    Jump("loc_134B")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1362")
    SetMapFlags(0x10000000)
    Event(0, 43)

    label("loc_1362")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BD")
    SetChrPos(0x0, -9950, 0, 3770, 220)
    SetChrPos(0x1, -9950, 0, 3770, 220)
    SetChrPos(0x2, -9950, 0, 3770, 220)
    SetChrPos(0x3, -9950, 0, 3770, 220)

    label("loc_13BD")

    Return()

    # Function_6_E70 end

    def Function_7_13BE(): pass

    label("Function_7_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_13DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_13F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1412")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_1412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_142E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_1445")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_145A")

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_145A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_145A")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148B")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A3")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 6, 0x80)

    label("loc_14A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F4")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_1565")

    label("loc_14F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1540")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_1565")

    label("loc_1540")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_1565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_158B")
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    Jump("loc_15A3")

    label("loc_158B")

    SetMapObjFrame(0xFF, "ka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x0, 0x1)

    label("loc_15A3")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BF")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D6")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15ED")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1600")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1617")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1629")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1629")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1641")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1641")

    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1663")
    OP_1B(0x1, 0x0, 0x3E)
    OP_1B(0x2, 0x0, 0x3F)

    label("loc_1663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_167B")
    OP_1B(0x1, 0x0, 0x3E)
    OP_1B(0x2, 0x0, 0x3F)

    label("loc_167B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_168F")
    BeginChrThread(0x17, 0, 0, 5)

    label("loc_168F")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_16B1")
    Jump("loc_176D")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_176D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16CB")
    Jump("loc_176D")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_16D9")
    Jump("loc_176D")

    label("loc_16D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_1713")
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Jump("loc_176D")

    label("loc_1713")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_176D")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x0, 0x0, 0x23)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176D")
    Event(0, 42)

    label("loc_176D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1789")
    Jump("loc_178E")

    label("loc_1789")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_178E")

    Return()

    # Function_7_13BE end

    def Function_8_178F(): pass

    label("Function_8_178F")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_179C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17EC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_17EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180C")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F2")

    label("loc_180C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1820")
    Jump("loc_24F2")

    label("loc_1820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_192C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1893")

    #C0001
    ChrTalk(
        0x8,
        "我们店的冰激凌都是纯手工制作的哦。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "绝对值得您\x01",
            "购买品尝～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_1893")


    #C0003
    ChrTalk(
        0x8,
        (
            "我们店的冰激凌\x01",
            "都是纯手工制作的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……啊，你现在是不是正在想\x01",
            "『看上去似乎很好吃』呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "想吃就要立刻行动哦。\x01",
            "来，买一个回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1927")

    Jump("loc_24F2")

    label("loc_192C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A48")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1980")

    #C0006
    ChrTalk(
        0x8,
        (
            "最近这段时间，暴躁易怒的人\x01",
            "越来越多了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D2")

    label("loc_1980")


    #C0007
    ChrTalk(
        0x8,
        (
            "那边的小哥……不，大叔。\x01",
            "来个冰激凌吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x10A,
        "#0603F我才只有二十七岁……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19D2")

    Jump("loc_1A43")

    label("loc_19D7")


    #C0009
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "这位小哥，\x01",
            "你也买一个吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "我们店也有适合成年人的\x01",
            "白兰地味冰激凌哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    Jump("loc_24F2")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A86")

    #C0012
    ChrTalk(
        0x8,
        (
            "肚子痛的时候，\x01",
            "可不能吃冰激凌哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFE")

    label("loc_1A86")


    #C0013
    ChrTalk(
        0x8,
        (
            "我从彩虹剧团的人\x01",
            "那里听说了……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "他们那里的一名成员\x01",
            "最近的样子好像很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "是怎么了呢？\x01",
            "吃坏肚子了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1AFE")

    Jump("loc_24F2")

    label("loc_1B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B37")

    #C0016
    ChrTalk(
        0x8,
        (
            "冰激凌～\x01",
            "来个冰激凌吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAA")

    label("loc_1B37")


    #C0017
    ChrTalk(
        0x8,
        (
            "纪念庆典结束了，\x01",
            "可游客的人数并没有减少呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "这可真是件值得高兴的事啊。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "各位，请尽情\x01",
            "把钱花掉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BAA")

    Jump("loc_24F2")

    label("loc_1BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C70")

    #C0020
    ChrTalk(
        0x8,
        (
            "我听说在纪念庆典期间，\x01",
            "港湾区那边新开了一家好吃的冰激凌店，\x01",
            "本来还有些提心吊胆，不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "我这个月仍旧\x01",
            "获得了露天店的ＭＶＰ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "呵呵，这也是\x01",
            "托了各位的福啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D11")

    label("loc_1C70")


    #C0023
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "……纪念庆典的营业额\x01",
            "真是节节攀升呢～\x01",
            "大约是平时的二十倍左右吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "必须保持这个势头，\x01",
            "死守住露天店销售额\x01",
            "第一的宝座呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D11")

    Jump("loc_24F2")

    label("loc_1D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1F40")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DA0")

    #C0026
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x11C, 500)

    #C0027
    ChrTalk(
        0x8,
        (
            "……小狗狗要不要\x01",
            "也来个冰激凌啊～？\x01",
            "很好吃的哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3F")

    label("loc_1DA0")


    #C0028
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11C, 500)

    #C0029
    ChrTalk(
        0x8,
        (
            "……小狗狗要不要\x01",
            "也来个冰激凌啊～？\x01",
            "很好吃的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x11C,
        "#1200F呜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#0200F（它在说\x01",
            "  『我不喜欢甜食』。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E3F")

    TalkEnd(0x8)
    Return()

    label("loc_1E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EB3")

    #C0032
    ChrTalk(
        0x8,
        (
            "我们店的冰激凌，\x01",
            "在剧团团员中很受欢迎哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "干脆打着剧团指定冰激凌的旗号，\x01",
            "趁势多卖点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F3B")

    label("loc_1EB3")


    #C0034
    ChrTalk(
        0x8,
        (
            "其实剧团的人\x01",
            "也经常来买我们店的冰激凌哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "伊莉娅小姐和普莉埃小姐\x01",
            "都是我们店的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "干脆打着\x01",
            "剧团指定冰激凌的旗号吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F3B")

    Jump("loc_24F2")

    label("loc_1F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F84")

    #C0037
    ChrTalk(
        0x8,
        (
            "顾客就是神明～\x01",
            "有什么要求请尽管提出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCC")

    label("loc_1F84")


    #C0038
    ChrTalk(
        0x8,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "现在还在做开店准备，不过\x01",
            "你们要买冰激凌吗～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FCC")

    Jump("loc_24F2")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_20BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_203C")

    #C0040
    ChrTalk(
        0x8,
        (
            "剧团成员喜欢吃的口味，\x01",
            "都快要卖光了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "想吃的话要快点买啊，\x01",
            "别留下遗憾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B6")

    label("loc_203C")


    #C0042
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "彩虹剧团成员\x01",
            "喜欢吃的口味，\x01",
            "都快要卖光了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "想吃的话要快点买啊，\x01",
            "别留下遗憾。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20B6")

    Jump("loc_24F2")

    label("loc_20BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_212A")

    #C0045
    ChrTalk(
        0x8,
        (
            "剧团的崇拜者都会来买\x01",
            "这些口味的冰激凌哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "你们也要跟上潮流啊，\x01",
            "来一个怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2193")

    label("loc_212A")


    #C0047
    ChrTalk(
        0x8,
        (
            "小哥，你们也是\x01",
            "彩虹剧团的崇拜者吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "那就一定要买\x01",
            "我这里的冰激凌了～\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "来来，买一个吃吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2193")

    Jump("loc_24F2")

    label("loc_2198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21F0")

    #C0050
    ChrTalk(
        0x8,
        (
            "我这个月也\x01",
            "获得了露天店的ＭＶＰ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "这都是托了各位的福～\x02",
    )

    CloseMessageWindow()
    Jump("loc_226E")

    label("loc_21F0")


    #C0052
    ChrTalk(
        0x8,
        "太好了～销售额第一！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "承蒙各位的惠顾，\x01",
            "我们店这个月的销售额\x01",
            "获得了第一名哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "这都是托了大家的福，\x01",
            "谢谢你们～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_226E")

    Jump("loc_24F2")

    label("loc_2273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_231C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22AB")

    #C0055
    ChrTalk(
        0x8,
        (
            "我最喜欢\x01",
            "剧团的崇拜者们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2317")

    label("loc_22AB")


    #C0056
    ChrTalk(
        0x8,
        (
            "各位崇拜者\x01",
            "每天早上都会\x01",
            "很早就来。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "然后买我这里的冰激凌\x01",
            "当零食哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "哎呀～真是值得高兴啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2317")

    Jump("loc_24F2")

    label("loc_231C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_23BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2368")

    #C0059
    ChrTalk(
        0x8,
        (
            "怎么没有卖饮料的啊，\x01",
            "我还想用冰激凌换饮料喝呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B8")

    label("loc_2368")


    #C0060
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "啊，口好渴啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "哪里有\x01",
            "卖饮料的呢～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_23B8")

    Jump("loc_24F2")

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2416")

    #C0063
    ChrTalk(
        0x8,
        (
            "我建议您趁现在\x01",
            "买个冰激凌吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "下午说不定\x01",
            "就会卖光了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2491")

    label("loc_2416")


    #C0065
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "……这位小哥，\x01",
            "来个冰激凌吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "今天天气会很热哦～！\x01",
            "等下你要是后悔我可不管哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2491")

    Jump("loc_24F2")

    label("loc_2496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_24CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_24C3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BB")
    Call(0, 11)
    Jump("loc_24BE")

    label("loc_24BB")

    Call(0, 9)

    label("loc_24BE")

    Jump("loc_24C6")

    label("loc_24C3")

    Call(0, 9)

    label("loc_24C6")

    Jump("loc_24F2")

    label("loc_24CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_24EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E7")
    Call(0, 11)
    Jump("loc_24EA")

    label("loc_24E7")

    Call(0, 10)

    label("loc_24EA")

    Jump("loc_24F2")

    label("loc_24EF")

    Call(0, 10)

    label("loc_24F2")

    Jump("loc_179C")

    label("loc_24F7")

    TalkEnd(0xFE)
    Return()

    # Function_8_178F end

    def Function_9_24FB(): pass

    label("Function_9_24FB")


    #C0068
    ChrTalk(
        0x8,
        (
            "今天傍晚\x01",
            "彩虹剧团\x01",
            "有场公演呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "销售额肯定\x01",
            "能上涨许多～\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_9_24FB end

    def Function_10_253D(): pass

    label("Function_10_253D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_256E")

    #C0070
    ChrTalk(
        0x8,
        (
            "我们店的冰激凌\x01",
            "超级好吃的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B2")

    label("loc_256E")


    #C0071
    ChrTalk(
        0x8,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "……这位小哥，\x01",
            "来个冰激凌吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_25B2")

    Return()

    # Function_10_253D end

    def Function_11_25B3(): pass

    label("Function_11_25B3")


    #C0073
    ChrTalk(
        0xFE,
        "冰激凌～来个冰激凌吧～？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "对了，这位小哥，\x01",
            "今天有特别大赠送哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "我们将教您\x01",
            "奶油拿铁的制作方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "很好喝哦，\x01",
            "请务必试一试～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x15)
    Return()

    # Function_11_25B3 end

    def Function_12_26AC(): pass

    label("Function_12_26AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276E")

    #C0079
    ChrTalk(
        0xFE,
        (
            "哎呀……欢迎光临。\x01",
            "小哥，你们有时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "要不要来喝杯酒啊？\x01",
            "我们店有很多不错的女孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "嘿嘿，就连警备队司令\x01",
            "也经常来光顾哦。\x01",
            "绝对会让你们不虚此行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27CC")

    label("loc_276E")


    #C0082
    ChrTalk(
        0xFE,
        (
            "嘿嘿，就连警备队司令\x01",
            "也经常来光顾哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "怎么样，进来玩一玩吧，\x01",
            "绝对会让你们不虚此行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CC")

    Jump("loc_361C")

    label("loc_27D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2837")

    #C0084
    ChrTalk(
        0x9,
        (
            "好像从昨天开始，警察就\x01",
            "一直出入那间酒店。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        "哎呀呀，简直是妨碍营业嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28B9")

    label("loc_2837")


    #C0086
    ChrTalk(
        0x9,
        (
            "听说从昨天开始，警察就\x01",
            "一直出入那间酒店。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "哎呀呀，到底发生了什么事呢？\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "这样会让客人担心受怕，真希望他们别来啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_28B9")

    Jump("loc_361C")

    label("loc_28BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_297E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2903")

    #C0089
    ChrTalk(
        0x9,
        "今天的气氛很奇怪，\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        "我都不敢拉客了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2979")

    label("loc_2903")


    #C0091
    ChrTalk(
        0x9,
        (
            "总觉得今天\x01",
            "欢乐街的气氛很奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "警察好像随时\x01",
            "都有可能强行进行搜查。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "今天还是应该\x01",
            "早点收手为好吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2979")

    Jump("loc_361C")

    label("loc_297E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A0A")

    #C0094
    ChrTalk(
        0x9,
        (
            "自纪念庆典之后一直留在\x01",
            "这里的游客好像有很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "真是让人高兴啊，小哥，\x01",
            "我要拉大家一起去\x01",
            "玩玩特别娱乐项目。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA7")

    label("loc_2A0A")


    #C0096
    ChrTalk(
        0x9,
        (
            "纪念庆典都已经过去一个月了，\x01",
            "还有很多人不回家，\x01",
            "在这里闲逛。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "真让人高兴啊，小哥，\x01",
            "我真的很感动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "他们简直就像是在说：\x01",
            "『快来拉我们吧』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AA7")

    Jump("loc_361C")

    label("loc_2AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B29")

    #C0099
    ChrTalk(
        0x9,
        (
            "每年议会期间，我们都会\x01",
            "争抢接待工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "嘿嘿……工作了工作了，\x01",
            "今年也必须得争取多一些预约啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B96")

    label("loc_2B29")


    #C0101
    ChrTalk(
        0x9,
        "预算会议快要开始了。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "嘿嘿……\x01",
            "我们店对接待方面很有信心，\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "绝对不会输给\x01",
            "那些乱七八糟的店哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B96")

    Jump("loc_361C")

    label("loc_2B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2DCF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C18")
    TurnDirection(0x9, 0x11C, 0)

    #C0104
    ChrTalk(
        0x9,
        "哇，好威风的狗啊。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "这是你们养的吗？\x01",
            "真好啊，太让人羡慕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB8")

    label("loc_2C18")

    TurnDirection(0x9, 0x11C, 0)

    #C0106
    ChrTalk(
        0x9,
        "哇，好威风的狗啊。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "这是你们养的吗？\x01",
            "真好啊，太让人羡慕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11C,
        "#1203F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0203F（它在说：\x01",
            "  『我对你这种小角色没兴趣』。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2CB8")

    TalkEnd(0x9)
    Return()

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D31")

    #C0110
    ChrTalk(
        0x9,
        (
            "如果做违法生意，\x01",
            "游击士协会的人就会找上门来。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "哎呀呀，真是很吓人啊，\x01",
            "我可不是\x01",
            "那么坏的人哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCA")

    label("loc_2D31")


    #C0112
    ChrTalk(
        0x9,
        (
            "刚才有游击士来店里了，\x01",
            "我当时吓了一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "还好，那些人只是因为任务，\x01",
            "来询问一些事情的。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "真是很吓人啊，\x01",
            "我们店也没有\x01",
            "做什么违法生意啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2DCA")

    Jump("loc_361C")

    label("loc_2DCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E31")

    #C0115
    ChrTalk(
        0x9,
        "呵呵，今天早上睡醒后心情不错，\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "挫了挫对方的锐气，\x01",
            "心情真是好啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EAB")

    label("loc_2E31")


    #C0117
    ChrTalk(
        0x9,
        (
            "我从比修的店里\x01",
            "拉来了一个女孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "嘿嘿，不过这只是\x01",
            "小竞争而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "但能挫一挫对方的锐气，\x01",
            "心情真是好啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2EAB")

    Jump("loc_361C")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F06")

    #C0120
    ChrTalk(
        0x9,
        (
            "嘿嘿，客人们都\x01",
            "快来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "现在必须打起精神努力加油啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F6C")

    label("loc_2F06")


    #C0122
    ChrTalk(
        0x9,
        (
            "小哥小哥，\x01",
            "来得正好啊，\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "要不要\x01",
            "来玩一玩啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "肯定让您开心呢～\x01",
            "疲惫也会一扫而光的哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F6C")

    Jump("loc_361C")

    label("loc_2F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_304A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2FB6")

    #C0125
    ChrTalk(
        0x9,
        (
            "可不能跟\x01",
            "鲁巴彻商会那种\x01",
            "组织扯上关系啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3045")

    label("loc_2FB6")


    #C0126
    ChrTalk(
        0x9,
        (
            "最近黑月那帮家伙\x01",
            "好像在扩大势力范围。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "不过，克洛斯贝尔黑道势力\x01",
            "的龙头老大\x01",
            "还是鲁巴彻商会哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "在这条街上可不能\x01",
            "忤逆那些家伙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3045")

    Jump("loc_361C")

    label("loc_304A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30CD")

    #C0129
    ChrTalk(
        0x9,
        (
            "随着议会的临近，\x01",
            "要接待的客人也会增多哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "等那些手掌大权的议员来光顾时，\x01",
            "我们会给他们特别优待的～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_314B")

    label("loc_30CD")


    #C0131
    ChrTalk(
        0x9,
        (
            "小哥、小哥，\x01",
            "要不要来玩玩啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "……最近，要接待的\x01",
            "大客户增多了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "啊，真开心啊。\x01",
            "肯定是因为议会召开临近了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_314B")

    Jump("loc_361C")

    label("loc_3150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3251")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F6")

    #C0134
    ChrTalk(
        0xFE,
        (
            "昨天警察好像\x01",
            "在进行什么案件的查访。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "两个刑警一组，\x01",
            "四处打听消息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "哎呀呀，我可什么都不知道哦，\x01",
            "我只是个善良的揽客员而已～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_324C")

    label("loc_31F6")


    #C0137
    ChrTalk(
        0xFE,
        (
            "欢乐街经常有事件发生，\x01",
            "所以时不时就有警察来。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "我可什么都不知道哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_324C")

    Jump("loc_361C")

    label("loc_3251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_333D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32AF")

    #C0139
    ChrTalk(
        0x9,
        (
            "冰激凌店的那位小姐，真是可爱啊。\x01",
            "如果她失业了，就由我们来收留吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3338")

    label("loc_32AF")


    #C0140
    ChrTalk(
        0x9,
        "（舔舔）……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "我去前面那个\x01",
            "冰激凌店采购冰激凌回来了，\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "冰激凌店的那位小姐，真是可爱啊～\x01",
            "如果她失业了，就由我们来收留吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3338")

    Jump("loc_361C")

    label("loc_333D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3400")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3390")

    #C0143
    ChrTalk(
        0x9,
        (
            "比修说的话，\x01",
            "你们可不能听啊。\x01",
            "想要玩的话就来我们店吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FB")

    label("loc_3390")


    #C0144
    ChrTalk(
        0x9,
        (
            "那边的后巷里，\x01",
            "有个叫比修的男人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "他是我的竞争对手。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "那个男人说的话，\x01",
            "你们可不能听啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_33FB")

    Jump("loc_361C")

    label("loc_3400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_34B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3430")

    #C0147
    ChrTalk(
        0x9,
        (
            "哪里有\x01",
            "好客人啊～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34AC")

    label("loc_3430")


    #C0148
    ChrTalk(
        0x9,
        (
            "啊，都中午了。\x01",
            "客人们差不多快来了，\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "路过这里的客人，\x01",
            "可是很多的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "嘿嘿，真是期待啊。\x01",
            "今天要拉哪个人呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_34AC")

    Jump("loc_361C")

    label("loc_34B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3504")

    #C0151
    ChrTalk(
        0x9,
        "我们店就在这附近哦。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "嘿嘿，怎样，小哥？\x01",
            "今天会给你优惠哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361C")

    label("loc_3504")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3582")

    #C0153
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，\x01",
            "小哥你们来得正是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "怎么样，来我们店喝杯美酒吧，\x01",
            "还有很多很棒的女孩子哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EE")

    label("loc_3582")


    #C0155
    ChrTalk(
        0x9,
        (
            "啊……我可没\x01",
            "叫小孩子哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 750)

    #C0156
    ChrTalk(
        0xFE,
        (
            "怎么样，那位小哥，\x01",
            "来我们店喝杯美酒吧，\x01",
            "还有很多很棒的女孩子哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EE")


    #C0157
    ChrTalk(
        0x9,
        (
            "一小时才一千米拉哦。\x01",
            "嘿嘿，来玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_361C")

    TalkEnd(0xFE)
    Return()

    # Function_12_26AC end

    def Function_13_3620(): pass

    label("Function_13_3620")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_369E")

    #C0158
    ChrTalk(
        0xA,
        (
            "剧团爱好者的眼睛是雪亮的！\x01",
            "一定发生了什么事！\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "虽然我去问过接待处的人，\x01",
            "但也没问出什么……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373B")

    label("loc_369E")


    #C0160
    ChrTalk(
        0xA,
        "从早上开始，剧团的气氛就很奇怪。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "我虽然去问了接待处的人，\x01",
            "但是也问不出什么详细情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "今天白天的公演推迟了很久呢，\x01",
            "到底发生了什么事呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_373B")

    Jump("loc_421D")

    label("loc_3740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_37BA")

    #C0163
    ChrTalk(
        0xA,
        (
            "我听不到伊莉娅小姐心中的声音了，\x01",
            "那个声音平时只有我才能听到的……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        "到底发生了什么事呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3810")

    label("loc_37BA")


    #C0165
    ChrTalk(
        0xA,
        "#4S伊莉娅小姐～！伊莉娅小姐～！\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "……好奇怪……\x01",
            "总觉得今天好安静啊～\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3810")

    Jump("loc_421D")

    label("loc_3815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_38C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_384F")

    #C0167
    ChrTalk(
        0xA,
        (
            "伊莉娅小姐～\x01",
            "公演请加油哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BD")

    label("loc_384F")


    #C0168
    ChrTalk(
        0xA,
        "今天的公演开始了呢……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "虽然没有门票，但也没关系，\x01",
            "我仍然会站在远处为伊莉娅小姐加油！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_38BD")

    Jump("loc_421D")

    label("loc_38C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_38F9")

    #C0170
    ChrTalk(
        0xA,
        (
            "伊莉娅小姐～请出来\x01",
            "向我们挥挥手吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_38F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3958")

    #C0171
    ChrTalk(
        0xA,
        (
            "今天要发售『金之太阳、银之月』\x01",
            "的写真集哦！\x01",
            "这可一定不能错过……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A06")

    label("loc_3958")


    #C0172
    ChrTalk(
        0xA,
        (
            "喂，你们听说了吗？\x01",
            "今天要发售『金之太阳、银之月』\x01",
            "的写真集哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "里面网罗了\x01",
            "公演的精彩看点\x01",
            "和所有情节的照片哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "绝、绝对不能错过……\x01",
            "我得马上去百货店一趟……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3A06")

    Jump("loc_421D")

    label("loc_3A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3AB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3A4F")

    #C0175
    ChrTalk(
        0xA,
        (
            "啊，伊莉娅小姐……\x01",
            "她现在在做什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAC")

    label("loc_3A4F")


    #C0176
    ChrTalk(
        0xA,
        (
            "彩虹剧团\x01",
            "今天休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "虽然有几位团员主动来练习了……\x01",
            "但伊莉娅小姐好像并没有来……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3AAC")

    Jump("loc_421D")

    label("loc_3AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3AEE")

    #C0178
    ChrTalk(
        0xA,
        (
            "#4S伊莉娅小姐～\x01",
            "练习要加油哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF1")

    label("loc_3AEE")

    Call(0, 14)

    label("loc_3AF1")

    Jump("loc_421D")

    label("loc_3AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B53")

    #C0179
    ChrTalk(
        0xA,
        "伊莉娅小姐今天好像睡懒觉了。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "真是少见啊，\x01",
            "把这个写进今天的日记里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_3B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3B84")

    #C0181
    ChrTalk(
        0xA,
        (
            "伊莉娅小姐，\x01",
            "练习要加油哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_3B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3C91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3BDC")

    #C0182
    ChrTalk(
        0xA,
        "咦～……真的吗？\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "如果有人偷跑进去，\x01",
            "我可不会放过他哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C8C")

    label("loc_3BDC")


    #C0184
    ChrTalk(
        0xA,
        (
            "你们……\x01",
            "在彩虹剧团做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "很可疑啊。\x01",
            "你们不是剧团的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#0100F那个，我们并不是什么可疑的人。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#0012F我们有朋友在这里工作。\x01",
            "（这应该不算说谎吧……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3C8C")

    Jump("loc_421D")

    label("loc_3C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D02")

    #C0188
    ChrTalk(
        0xA,
        (
            "呜呜呜，我还以为\x01",
            "能再一次见到伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "为了这一天，\x01",
            "我都忍耐那么久了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC5")

    label("loc_3D02")


    #C0190
    ChrTalk(
        0xA,
        "#4S呜哇～！！\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        (
            "在新剧门票发售的日子，\x01",
            "我竟然起晚了……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "虽然我急急忙忙地跑去买，\x01",
            "但排到我时，门票刚好卖光了……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "呜呜呜……我这个笨蛋～……\x01",
            "这样一来，就见不到伊莉娅小姐了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3DC5")

    Jump("loc_421D")

    label("loc_3DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3E2C")

    #C0194
    ChrTalk(
        0xA,
        (
            "新剧的门票\x01",
            "好像从下星期开始出售。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "好想要啊……呵呵……\x01",
            "我一定要买到手……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_3E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3EBC")

    #C0196
    ChrTalk(
        0xA,
        (
            "好想拍伊莉娅小姐穿练习装的样子……\x01",
            "……还、还有她穿新剧演出服的\x01",
            "各种姿势⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "呵呵，不知道有没有\x01",
            "机会可以拍到～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F66")

    label("loc_3EBC")


    #C0198
    ChrTalk(
        0xA,
        "伊莉娅小姐，伊莉娅小姐……！\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        (
            "我拍到了她穿便装、\x01",
            "舞台服装还有在休息室穿睡袍的照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "剩下的还有她穿练习装的样子……\x01",
            "呵呵，不知道有没有\x01",
            "机会可以拍到呢～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3F66")

    Jump("loc_421D")

    label("loc_3F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3FD4")

    #C0201
    ChrTalk(
        0xA,
        (
            "伊莉娅小姐要出演\x01",
            "这次的新剧哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        (
            "啊啊，终于能在现场\x01",
            "一睹她的英姿了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4072")

    label("loc_3FD4")

    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0203
    ChrTalk(
        0xA,
        (
            "喂，你们听说了吗！？\x01",
            "这可是劲爆消息哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "彩虹剧团新剧的\x01",
            "公演快要开始了！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "听说门票也\x01",
            "要开始出售了。\x01",
            "这可一定不能错过～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4072")

    Jump("loc_421D")

    label("loc_4077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_417B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_40F0")
    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0206
    ChrTalk(
        0xA,
        "伊莉娅小姐，请快点出来吧！\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "还是说，\x01",
            "她已经从后门离开了呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4176")

    label("loc_40F0")


    #C0208
    ChrTalk(
        0xA,
        (
            "伊莉娅小姐\x01",
            "还没出来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        (
            "我的梦想是能拍到\x01",
            "伊莉娅小姐刚练习完的照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        (
            "为此我还特别花了两万米拉\x01",
            "买了一台导力相机呢～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4176")

    Jump("loc_421D")

    label("loc_417B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_41DD")

    #C0211
    ChrTalk(
        0xA,
        (
            "啊，是你们啊！\x01",
            "你们在里面看到伊莉娅小姐了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "真狡猾～！\x01",
            "我也想看呢～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_41DD")

    OP_93(0xFE, 0x13B, 0x0)

    #C0213
    ChrTalk(
        0xA,
        (
            "不知道有没有机会看到\x01",
            "伊莉娅小姐穿练习装的样子～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421D")

    TalkEnd(0xFE)
    Return()

    # Function_13_3620 end

    def Function_14_4221(): pass

    label("Function_14_4221")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0214
    ChrTalk(
        0xA,
        (
            "塔普，你买到\x01",
            "门票了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "没有买到呢……\x01",
            "我去拜托认识的人，\x01",
            "但没有一个愿意把票让给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        "那么，纪念庆典期间要做的事情就只有一件啦。\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        "嗯嗯，只有那一件了。\x02",
    )

    CloseMessageWindow()

    def lambda_42D7():
        OP_93(0xA, 0x13B, 0x2EE)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_42D7)

    def lambda_42E4():
        OP_93(0xB, 0x13B, 0x2EE)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_42E4)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0218
    ChrTalk(
        0xA,
        (
            "#4S那就是一直\x01",
            "默默守护着伊莉娅小姐～！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "#4S伊莉娅小姐，\x01",
            "我会用心一直守护您的～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_4221 end

    def Function_15_435A(): pass

    label("Function_15_435A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_43E6")

    #C0220
    ChrTalk(
        0xB,
        (
            "今天白天的公演推迟了，\x01",
            "到四点左右才开始呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xB,
        (
            "听说剧团长和经理\x01",
            "一直慌慌张张地跑进跑出……\x01",
            "不会真的发生了什么事吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EA5")

    label("loc_43E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_443D")

    #C0222
    ChrTalk(
        0xB,
        (
            "今天白天的公演\x01",
            "不知道为什么好像推迟了……\x01",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_448D")

    label("loc_443D")


    #C0223
    ChrTalk(
        0xB,
        "剧团里安静得有些可疑……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xB,
        (
            "公演差不多要开始了吧？\x01",
            "他们都在干什么啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_448D")

    Jump("loc_4EA5")

    label("loc_4492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_458B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4519")

    #C0225
    ChrTalk(
        0xB,
        (
            "今天早上我在等伊莉娅小姐的时候，\x01",
            "那个孩子一直瞪着我。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "……剧团为什么要雇\x01",
            "一个那么没有亲和力的家伙呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4586")

    label("loc_4519")


    #C0227
    ChrTalk(
        0xB,
        (
            "最近彩虹剧团好像\x01",
            "新招了一个打杂的孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        (
            "那孩子时不时就会瞪我……\x01",
            "真是一个没有亲和力的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4586")

    Jump("loc_4EA5")

    label("loc_458B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_45EC")

    #C0229
    ChrTalk(
        0xB,
        (
            "希望莉夏小姐的写真集\x01",
            "可以早点发售啊……\x01",
            "大概还要等很久，真是没办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4674")

    label("loc_45EC")


    #C0230
    ChrTalk(
        0xB,
        (
            "伊莉娅小姐当然毋庸置疑，\x01",
            "不过新人莉夏小姐也很厉害哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "如果莉夏小姐\x01",
            "出个人写真集的话，\x01",
            "绝对会大卖的。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xB,
        "还不发售吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4674")

    Jump("loc_4EA5")

    label("loc_4679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_47B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_46E5")

    #C0233
    ChrTalk(
        0xFE,
        (
            "听说莉夏·毛\x01",
            "和伊莉娅小姐的对手戏\x01",
            "非常精彩。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "呜呜……我也想\x01",
            "在现场观看啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47AE")

    label("loc_46E5")


    #C0235
    ChrTalk(
        0xFE,
        (
            "有一个凭借与伊莉娅小姐共同演出\x01",
            "而出道的女孩子叫莉夏·毛吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "大家都评论说她的演技很厉害。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "她和伊莉娅小姐的风格不同，\x01",
            "舞姿楚楚可人，\x01",
            "却也有着凛然风骨。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "呜呜……\x01",
            "我也想在现场看啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_47AE")

    Jump("loc_4EA5")

    label("loc_47B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_480A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4802")

    #C0239
    ChrTalk(
        0xB,
        (
            "#4S伊莉娅小姐～\x01",
            "我们这些崇拜者都会紧紧跟随您的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4805")

    label("loc_4802")

    Call(0, 14)

    label("loc_4805")

    Jump("loc_4EA5")

    label("loc_480A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_48BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4854")

    #C0240
    ChrTalk(
        0xB,
        (
            "那人是谁啊……？\x01",
            "难道是伊莉娅小姐的新崇拜者？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B9")

    label("loc_4854")


    #C0241
    ChrTalk(
        0xB,
        (
            "今天早上，有一群\x01",
            "穿着西服的人进了剧团……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        (
            "虽然好像是剧团的相关人员，\x01",
            "但眼神都很锐利……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_48B9")

    Jump("loc_4EA5")

    label("loc_48BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_49C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_493A")

    #C0243
    ChrTalk(
        0xB,
        (
            "不过，就算有演出，\x01",
            "我这个穷学生\x01",
            "也是看不了的……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "没关系，能看到夜晚中的剧院\x01",
            "我也就满足了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BC")

    label("loc_493A")


    #C0245
    ChrTalk(
        0xB,
        (
            "彩虹剧团最近正在为\x01",
            "新剧公演进行排练。\x01",
            "所以今天晚上没有演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xB,
        (
            "不过，能看到夜晚中的剧院\x01",
            "就已经让人兴奋不已了，不是吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_49BC")

    Jump("loc_4EA5")

    label("loc_49C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A24")

    #C0247
    ChrTalk(
        0xB,
        (
            "今天早上，那个新人莉夏小姐\x01",
            "出入了剧院好几次……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        "是有什么东西忘在家里了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EA5")

    label("loc_4A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACA")

    #C0249
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的门票，\x01",
            "就算是Ｂ席也很昂贵……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "……虽然很遗憾，但我这次\x01",
            "只能放弃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "像我这种穷学生，\x01",
            "果然是没办法看这种表演的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B18")

    label("loc_4ACA")


    #C0252
    ChrTalk(
        0xFE,
        (
            "气死我了，虽然我\x01",
            "去求了父母……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "但他们说学生不应该\x01",
            "看太多这种表演。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B18")

    Jump("loc_4EA5")

    label("loc_4B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4B4D")

    #C0254
    ChrTalk(
        0xB,
        "喂，珀利塞，口水流出来了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EA5")

    label("loc_4B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B9F")

    #C0255
    ChrTalk(
        0xB,
        (
            "可恶，我都\x01",
            "没有导力相机……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "那对学生来说\x01",
            "也实在太贵了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EA5")

    label("loc_4B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4C4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4BFB")

    #C0257
    ChrTalk(
        0xFE,
        "我每天早上都会来这里。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "真想直接在这广场\x01",
            "搭个帐篷住下算了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C47")

    label("loc_4BFB")


    #C0259
    ChrTalk(
        0xB,
        (
            "你们也是来欣赏\x01",
            "伊莉娅小姐早上的身姿的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        "追星也要适可而止啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4C47")

    Jump("loc_4EA5")

    label("loc_4C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4CE2")

    #C0261
    ChrTalk(
        0xFE,
        (
            "其实珀利塞那家伙\x01",
            "是跟我一起追随彩虹剧团的伙伴。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "哼……我们偶然在\x01",
            "同一天看到伊莉娅小姐的舞姿，\x01",
            "然后同时被她所俘虏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DBF")

    label("loc_4CE2")


    #C0263
    ChrTalk(
        0xB,
        (
            "『彩虹剧团』在国际上\x01",
            "也是享誉盛名的剧团哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        (
            "剧团里的艺人\x01",
            "也都是顶级的名演员。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        (
            "但伊莉娅小姐在其中仍是与众不同的！\x01",
            "绝世舞姬，堪称天才的伊莉娅·普拉提耶……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "我十分理解珀利塞那家伙\x01",
            "为她如痴如狂的心情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4DBF")

    Jump("loc_4EA5")

    label("loc_4DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4E16")

    #C0267
    ChrTalk(
        0xB,
        (
            "『彩虹剧团』平时都是\x01",
            "禁止观众进入的哦～\x01",
            "所以只能站在外面看呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EA5")

    label("loc_4E16")


    #C0268
    ChrTalk(
        0xB,
        (
            "哦，你们\x01",
            "也是来看\x01",
            "『彩虹剧团』的情况的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        (
            "虽然里面禁止观众进入，\x01",
            "但只从外面看的话可是免费的哦。\x01",
            "嗯，我们同为崇拜者，请多关照哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4EA5")

    TalkEnd(0xFE)
    Return()

    # Function_15_435A end

    def Function_16_4EA9(): pass

    label("Function_16_4EA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4F06")

    #C0270
    ChrTalk(
        0xC,
        (
            "今天晚上我们准备\x01",
            "全家一起去吃晚餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xC,
        (
            "呵呵，差不多\x01",
            "该去做些准备了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_4F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4F55")

    #C0272
    ChrTalk(
        0xC,
        "今天大街上有点安静啊……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xC,
        (
            "导力车的数量\x01",
            "好像也比平时少。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_506C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4FC2")

    #C0274
    ChrTalk(
        0xC,
        (
            "坎贝尔议员勉强算是\x01",
            "哈尔特曼议长的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "不过，应该没有人能胜过\x01",
            "那个议长吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5067")

    label("loc_4FC2")


    #C0276
    ChrTalk(
        0xC,
        (
            "哈尔特曼议长就是\x01",
            "那个狂妄自大的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "听说他和鲁巴彻\x01",
            "有关系，好像一直对\x01",
            "鲁巴彻颐指气使……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xC,
        (
            "呵呵，真是可怕的人啊。\x01",
            "要是与他为敌的话，应该会很惨吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5067")

    Jump("loc_59F7")

    label("loc_506C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_51A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5103")

    #C0279
    ChrTalk(
        0xC,
        (
            "有段时间，一个中性风格打扮的男公关\x01",
            "成了街头巷尾议论的话题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        (
            "不过遗憾的是，纪念庆典之后\x01",
            "就没再听过关于他的消息了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519B")

    label("loc_5103")


    #C0281
    ChrTalk(
        0xC,
        (
            "那个男公关……\x01",
            "最近都没听过关于他的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        (
            "从容不迫的眼神，\x01",
            "再加上中性风格的打扮，\x01",
            "有段时间让他受到了一致好评。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        "呼……真是令人遗憾啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_519B")

    Jump("loc_59F7")

    label("loc_51A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5246")

    #C0284
    ChrTalk(
        0xC,
        (
            "纪念庆典短短五天时间里，\x01",
            "好像无论哪家店都\x01",
            "都赚得盆满钵满。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xC,
        (
            "呵呵，这些都是\x01",
            "游客扔在这里的钱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔又从\x01",
            "世界各地收集了一大笔财富。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_5246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_52D4")

    #C0287
    ChrTalk(
        0xFE,
        (
            "参加各种聚会，去剧场看表演，\x01",
            "还要到米修拉姆的主题公园玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "呵呵呵，纪念庆典期间大概也会很忙呢，\x01",
            "必须合理安排计划呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_52D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_534B")

    #C0289
    ChrTalk(
        0xC,
        (
            "有很多游客预料到\x01",
            "纪念庆典会很拥挤，\x01",
            "所以提前来到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        (
            "这附近的酒店\x01",
            "应该会持续爆满吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_534B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_53A8")

    #C0291
    ChrTalk(
        0xC,
        (
            "呵呵，我收到了一个\x01",
            "今晚举办的社交宴会的邀请。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        "必须抓紧时间好好打扮。\x02",
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_53A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_545D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_53F9")

    #C0293
    ChrTalk(
        0xC,
        (
            "虽然很少听见相关传闻，\x01",
            "但最近好像发生了\x01",
            "很多事件呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5458")

    label("loc_53F9")


    #C0294
    ChrTalk(
        0xC,
        (
            "最近经常有警察\x01",
            "来进行案情询问。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        "哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        (
            "是不是哪里又\x01",
            "发生什么事件了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5458")

    Jump("loc_59F7")

    label("loc_545D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_551E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_54C4")

    #C0297
    ChrTalk(
        0xC,
        (
            "彩虹剧团粉丝的热情\x01",
            "丝毫未减，仍然很高涨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "竟然连我\x01",
            "都没能买到门票。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5519")

    label("loc_54C4")


    #C0299
    ChrTalk(
        0xC,
        (
            "门票发售当天\x01",
            "实在太多人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xC,
        (
            "所以我也没能买到门票。\x01",
            "唉～真是令人遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5519")

    Jump("loc_59F7")

    label("loc_551E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5588")

    #C0301
    ChrTalk(
        0xC,
        "那么，今天要去哪里玩呢？\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xC,
        (
            "呵呵，在欢乐街，\x01",
            "争吵纠纷是常有的事。\x01",
            "不需要去一一关心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_5588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_56D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5610")

    #C0303
    ChrTalk(
        0xC,
        (
            "虽然和阿尔摩利卡村及玛因兹\x01",
            "一样位于市外，\x01",
            "但乌尔斯拉医院可不一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xC,
        (
            "那是市民\x01",
            "常去的一家大学附属医院哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56CF")

    label("loc_5610")


    #C0305
    ChrTalk(
        0xC,
        (
            "乌尔斯拉医院位于\x01",
            "克洛斯贝尔市南部，\x01",
            "有最新的医疗设施哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "呵呵，它和阿尔摩利卡村\x01",
            "以及玛因兹不同，\x01",
            "是市民常去的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xC,
        (
            "在克洛斯贝尔，\x01",
            "如果受了伤，马上就会被\x01",
            "送到乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_56CF")

    Jump("loc_59F7")

    label("loc_56D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_57CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_573C")

    #C0308
    ChrTalk(
        0xC,
        "你们要注意那群拉客的男人。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "如果上了他们的当，\x01",
            "全部财产都会被骗光的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57C5")

    label("loc_573C")


    #C0310
    ChrTalk(
        0xC,
        (
            "那边的后巷里，\x01",
            "有好几个拉客的可疑男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xC,
        "你们不熟悉这里，可一定要注意啊。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xC,
        (
            "要是放松警惕的话，\x01",
            "就会被他们的花言巧语蒙骗。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_57C5")

    Jump("loc_59F7")

    label("loc_57CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_58DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_583F")

    #C0313
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔的欢乐街\x01",
            "即使在周边各国也是非常有名的社交场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xC,
        (
            "前来游玩的游客\x01",
            "络绎不绝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D8")

    label("loc_583F")


    #C0315
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔的欢乐街\x01",
            "是有名的社交场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "从面向平民的『巴鲁卡』到上流阶层\x01",
            "专用的会所都聚集于此……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        (
            "呵呵，从外国\x01",
            "前来游玩的游客\x01",
            "络绎不绝。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_58D8")

    Jump("loc_59F7")

    label("loc_58DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_593F")

    #C0318
    ChrTalk(
        0xC,
        (
            "这附近有不少家\x01",
            "酒店和餐厅哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        (
            "如果来克洛斯贝尔游玩，\x01",
            "就一定要来这里逛逛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F7")

    label("loc_593F")


    #C0320
    ChrTalk(
        0xC,
        (
            "啊，好陌生的脸孔啊，\x01",
            "你们是游客吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "呵呵，如果想玩玩，我推荐你们去『巴鲁卡』，\x01",
            "要是观光，那就一定得去『彩虹剧团』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xC,
        (
            "这附近有很多很棒的店哦。\x01",
            "你们可以自己探索一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_59F7")

    TalkEnd(0xFE)
    Return()

    # Function_16_4EA9 end

    def Function_17_59FB(): pass

    label("Function_17_59FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A3A")

    #C0323
    ChrTalk(
        0xD,
        "好，天黑了！\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xD,
        "今天也要好好玩个痛快！\x02",
    )

    CloseMessageWindow()
    Jump("loc_662B")

    label("loc_5A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5A6B")

    #C0325
    ChrTalk(
        0xD,
        "先回去睡一觉再来吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AB1")

    label("loc_5A6B")


    #C0326
    ChrTalk(
        0xD,
        (
            "昨天已经在老虎机前\x01",
            "玩了一个通宵了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xD,
        "呜～肚子饿得受不了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5AB1")

    Jump("loc_662B")

    label("loc_5AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5AED")

    #C0328
    ChrTalk(
        0xD,
        "真希望我也有那么好的运气。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B81")

    label("loc_5AED")


    #C0329
    ChrTalk(
        0xD,
        (
            "在『巴鲁卡』赚了很多米拉的那家伙，\x01",
            "现在好像被一群女公关围着，\x01",
            "过得超级奢靡。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xD,
        "呜呜呜，真是令人羡慕啊。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xD,
        (
            "那种家伙\x01",
            "也算是成功者了吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5B81")

    Jump("loc_662B")

    label("loc_5B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5C80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5BFF")

    #C0332
    ChrTalk(
        0xD,
        (
            "像他那样在『巴鲁卡』连续取胜，\x01",
            "可不是谁都能做到的。\x01",
            "虽然不知道到底是谁，不过他可真厉害啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C7B")

    label("loc_5BFF")


    #C0333
    ChrTalk(
        0xD,
        (
            "……你们听说了吗？\x01",
            "最近好像有一个家伙\x01",
            "在『巴鲁卡』连续赢了很多米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xD,
        (
            "虽然不知道到底是谁，\x01",
            "不过他可真厉害啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5C7B")

    Jump("loc_662B")

    label("loc_5C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5CCE")

    #C0335
    ChrTalk(
        0xD,
        (
            "今天虽然想玩老虎机，\x01",
            "但不知道哪里有比较好的店……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D4D")

    label("loc_5CCE")


    #C0336
    ChrTalk(
        0xD,
        "这是一片充斥着金钱与欲望的土地……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xD,
        (
            "就算纪念庆典结束了，\x01",
            "欢乐街还是欢乐街呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "来这里要做的事\x01",
            "可以说只有一件。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5D4D")

    Jump("loc_662B")

    label("loc_5D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5DC9")

    #C0339
    ChrTalk(
        0xD,
        (
            "彩虹剧团的\x01",
            "赞助商里，\x01",
            "有很多有权有势的人和外国的富豪。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xD,
        "他们每个人都有很豪华的导力车。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E4B")

    label("loc_5DC9")


    #C0341
    ChrTalk(
        0xD,
        (
            "彩虹剧团的预演\x01",
            "也临近了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        (
            "所以时不时就会有\x01",
            "赞助商来露个面……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "他们每个人都有很豪华的导力车，\x01",
            "真是让人羡慕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5E4B")

    Jump("loc_662B")

    label("loc_5E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5EBE")

    #C0344
    ChrTalk(
        0xD,
        "那个叫莉夏的女孩子，很可爱吧～\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xD,
        (
            "虽然她才刚入团不久，\x01",
            "但给人感觉总是非常努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F41")

    label("loc_5EBE")


    #C0346
    ChrTalk(
        0xD,
        (
            "彩虹剧团的新团员里\x01",
            "有一个叫莉夏的女孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xD,
        "她真是可爱啊～\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xD,
        (
            "我经常看到她上班，\x01",
            "她给人一种对排练非常努力的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_5F41")

    Jump("loc_662B")

    label("loc_5F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5FC8")

    #C0349
    ChrTalk(
        0xD,
        (
            "每天一到这个时间，\x01",
            "大圣堂的钟就会敲响。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xD,
        (
            "钟声非常庄严肃穆。\x01",
            "这对游客来说，也体现了自治州风情，很受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_662B")

    label("loc_5FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_61B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_609B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_605B")

    #C0351
    ChrTalk(
        0xFE,
        (
            "刚才那辆高级轿车，每到这个时候，\x01",
            "总会准时停在\x01",
            "彩虹剧团的前面。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "上星期我也看到了，\x01",
            "不过马上就开走了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6096")

    label("loc_605B")


    #C0353
    ChrTalk(
        0xFE,
        (
            "那么豪华的车，肯定很昂贵吧～\x01",
            "到底是哪个资产家的车呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6096")

    Jump("loc_61AE")

    label("loc_609B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_END)), "loc_6101")

    #C0354
    ChrTalk(
        0xFE,
        (
            "啊，好像停着\x01",
            "一辆很豪华的车啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "黑色的高级轿车，\x01",
            "这肯定是哪个资产家的车吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61AE")

    label("loc_6101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6160")

    #C0356
    ChrTalk(
        0xD,
        (
            "你们要是想订酒店房间，\x01",
            "就得快一点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        "不过我想要订今年的已经来不及了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_61AE")

    label("loc_6160")


    #C0358
    ChrTalk(
        0xD,
        (
            "最近无论哪间酒店，\x01",
            "好像都预约满了。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        "果然是因为纪念庆典的临近啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_61AE")

    Jump("loc_662B")

    label("loc_61B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6213")

    #C0360
    ChrTalk(
        0xD,
        "我虽然也想买张门票……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "但实在没有勇气\x01",
            "挤进那么疯狂的崇拜者中。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_628D")

    label("loc_6213")


    #C0362
    ChrTalk(
        0xD,
        (
            "彩虹剧团的新剧目\x01",
            "好像叫做『金之太阳、银之月』。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xD,
        (
            "在公布新剧信息时，\x01",
            "这里聚集了许多疯狂的崇拜者，\x01",
            "非常喧闹呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_628D")

    Jump("loc_662B")

    label("loc_6292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_62C0")

    #C0364
    ChrTalk(
        0xD,
        "那么，今天要去哪里玩呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_662B")

    label("loc_62C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_63EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6340")

    #C0365
    ChrTalk(
        0xD,
        (
            "『千禧酒店』好像\x01",
            "因为换了新经理，\x01",
            "装潢变得更为奢华了。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xD,
        (
            "等我赚够了钱，\x01",
            "一定要去住一晚享受享受。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E7")

    label("loc_6340")


    #C0367
    ChrTalk(
        0xD,
        (
            "……你们知道吗？\x01",
            "『千禧酒店』好像在前年\x01",
            "更换了经理。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xD,
        (
            "因为换了新经理，\x01",
            "本来就已经很高级的酒店变得更为奢华了。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xD,
        (
            "等我赚够了钱，\x01",
            "一定要去住一晚享受享受。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_63E7")

    Jump("loc_662B")

    label("loc_63EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_64D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_643C")

    #C0370
    ChrTalk(
        0xD,
        (
            "『巴鲁卡』的服务很周到，\x01",
            "虽然老板是个粗犷的大叔啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D3")

    label("loc_643C")


    #C0371
    ChrTalk(
        0xD,
        (
            "那边有一家叫\x01",
            "『巴鲁卡』的店，你们知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xD,
        (
            "那里的服务很周到哦。\x01",
            "要是输掉了米拉，\x01",
            "老板就会请我喝一杯。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xD,
        (
            "有兴趣的话，\x01",
            "你们可以去看看哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_64D3")

    Jump("loc_662B")

    label("loc_64D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6526")

    #C0374
    ChrTalk(
        0xD,
        (
            "去后巷的酒吧里看看好了，\x01",
            "大街上没有吃饭的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6560")

    label("loc_6526")


    #C0375
    ChrTalk(
        0xD,
        "唔～话说肚子好饿啊。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xD,
        (
            "玩着玩着\x01",
            "都忘记吃饭了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6560")

    Jump("loc_662B")

    label("loc_6565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_65BF")

    #C0377
    ChrTalk(
        0xD,
        (
            "只要在克洛斯贝尔，\x01",
            "就不愁没有地方玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        (
            "即使玩一辈子\x01",
            "也不会腻啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_662B")

    label("loc_65BF")


    #C0379
    ChrTalk(
        0xD,
        "好～今天也要玩个痛快！\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xD,
        (
            "是要去『巴鲁卡』玩玩呢，\x01",
            "还是叫个女孩去酒吧喝酒呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        "要怎么玩啊？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_662B")

    TalkEnd(0xFE)
    Return()

    # Function_17_59FB end

    def Function_18_662F(): pass

    label("Function_18_662F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6695")

    #C0382
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ，你们好吗☆\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xE,
        (
            "那位矿工客人，\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xE,
        "今天都没来呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_680E")

    label("loc_6695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_66EA")

    #C0385
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ，你们好吗☆\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xE,
        (
            "『巴鲁卡』今天的\x01",
            "生意也非常红火哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680E")

    label("loc_66EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6749")

    #C0387
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ，你们好吗☆\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "哎呀……你们还带着小孩子啊？\x01",
            "呵呵，非常欢迎哦⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680E")

    label("loc_6749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_678B")

    #C0389
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ，你们好吗☆\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        "今天有优惠活动哦⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_680E")

    label("loc_678B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_67D2")

    #C0391
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ，你们好吗☆\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        (
            "请多关照\x01",
            "『巴鲁卡』哦⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680E")

    label("loc_67D2")


    #C0393
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ，你们好吗☆\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xE,
        "呵呵，希望各位玩得尽兴哦⊥\x02",
    )

    CloseMessageWindow()

    label("loc_680E")

    TalkEnd(0xFE)
    Return()

    # Function_18_662F end

    def Function_19_6812(): pass

    label("Function_19_6812")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_694C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68F9")

    #C0395
    ChrTalk(
        0xFE,
        (
            "今天我值夜班哦，\x01",
            "必须先回总部小睡一会。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        "罗伊德，你们现在要去调查吗？\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#0000F嗯，是的。\x01",
            "准备去乌尔斯拉医院看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "支援科也很辛苦啊……\x01",
            "嗯，一起加油吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#0000F哈哈……说得没错呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6947")

    label("loc_68F9")


    #C0400
    ChrTalk(
        0xFE,
        (
            "今天我值夜班哦，\x01",
            "所以必须先回总部一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "回来的路上\x01",
            "得买点宵夜来吃。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6947")

    Jump("loc_69B0")

    label("loc_694C")


    #C0402
    ChrTalk(
        0xFE,
        (
            "最近这段时间，发生在欢乐街\x01",
            "的纠纷也开始增多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "是因为经济太景气了吗……\x01",
            "必须加强巡逻啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B0")

    TalkEnd(0xFE)
    Return()

    # Function_19_6812 end

    def Function_20_69B4(): pass

    label("Function_20_69B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C05")
    TurnDirection(0xFE, 0x103, 0)

    #C0404
    ChrTalk(
        0xFE,
        "你好啊，缇欧～\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "听说这里的手工冰激凌\x01",
            "很好吃，不知道是真是假。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0406
    ChrTalk(
        0x101,
        (
            "#0005F（缇欧……这位先生好像是\x01",
            "  爱普斯泰恩财团的人吧。）\x02\x03",

            "（约纳的事，\x01",
            "  不说好吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x103,
        (
            "#0203F（嗯，暂时\x01",
            "  先别说。）\x02\x03",

            "#0200F（……因为这会成为\x01",
            "  威胁约纳的有力手段。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0408
    ChrTalk(
        0x104,
        (
            "#0303F（如果他拒绝的话，就向财团告密吗……\x01",
            "  这种做法真是太有阿缇的风格了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#0100F（爱普斯泰恩财团的孩子们\x01",
            "  好像都很有心计呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 7)
    Jump("loc_6C8A")

    label("loc_6C05")


    #C0410
    ChrTalk(
        0xFE,
        (
            "我正在验证这里的\x01",
            "手工冰激凌是否真的好吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "不过可惜，\x01",
            "没有桃子味的……\x01",
            "我只喜欢吃桃子味的……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        "#0211F主任，好像很闲啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6C8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_69B4 end

    def Function_21_6C8E(): pass

    label("Function_21_6C8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CAC")
    Call(0, 22)
    Jump("loc_6DA1")

    label("loc_6CAC")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0413
    ChrTalk(
        0x13,
        "#6002F啊，真好吃……！\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x11,
        (
            "#0809F对吧！？\x01",
            "这是我很喜欢吃的哦。\x02\x03",

            "#0806F听说在纪念庆典期间，\x01",
            "好像还另开了一家很美味的店呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x12,
        (
            "#0900F真想让小滴\x01",
            "也吃吃看。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D92")

    #C0416
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈……\x01",
            "  看上去好像很开心呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D92")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    label("loc_6DA1")

    TalkEnd(0xFE)
    Return()

    # Function_21_6C8E end

    def Function_22_6DA5(): pass

    label("Function_22_6DA5")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_68(-9790, 3700, 23610, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17250, 0)
    SetChrPos(0x101, -5470, 1990, 19030, 315)
    SetChrPos(0x102, -4390, 1990, 19310, 315)
    SetChrPos(0x103, -4670, 1990, 17970, 315)
    SetChrPos(0x104, -3730, 1990, 18070, 315)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    TurnDirection(0x8, 0x11, 0)
    OP_0D()

    #C0417
    ChrTalk(
        0x11,
        (
            "#0800F小滴，\x01",
            "你喜欢哪种口味啊？\x02\x03",

            "我请客，\x01",
            "喜欢吃什么你随便点哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x13,
        (
            "#6010F这、这怎么行……多不好意思。\x02\x03",

            "姐姐都已经抽时间代替爸爸\x01",
            "来陪我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x11,
        (
            "#0809F啊哈哈，没关系没关系！\x01",
            "能和小滴在一起，\x01",
            "反倒是我占便宜了！\x02\x03",

            "#0800F那就点\x01",
            "我推荐的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x8, 500)

    #C0420
    ChrTalk(
        0x11,
        (
            "#0809F姐姐！\x02\x03",

            "请给我来一份巧克力布朗宁、\x01",
            "草莓奶酪蛋糕、\x01",
            "朗姆葡萄干的三合一冰激凌！\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "好的，让你们久等了，\x01",
            "请尽情享用哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x13, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 350)

    #C0422
    ChrTalk(
        0x12,
        (
            "#0906F……抱歉哦，\x01",
            "艾丝蒂尔总是这么自作主张。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0423
    ChrTalk(
        0x13,
        (
            "#6000F没、没有的事……\x01",
            "我很开心……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-7590, 3940, 20060, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19390, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_93(0x11, 0x5A, 0x0)
    OP_93(0x13, 0x10E, 0x0)
    OP_93(0x12, 0x13B, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    #C0424
    ChrTalk(
        0x101,
        (
            "#0005F（小滴……\x01",
            "  和艾丝蒂尔他们在一起吗。）\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x102,
        "#0100F（好像不应该去打扰呢……）\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x103,
        (
            "#0200F（不过，亚里欧斯先生\x01",
            "  去哪里了呢……？）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -4470, 1990, 19030, 315)
    ModifyEventFlags(0, 4, 0x80)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xD0, 0)
    EventEnd(0x5)
    Return()

    # Function_22_6DA5 end

    def Function_23_71AB(): pass

    label("Function_23_71AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    OP_68(-2100, 4610, 34300, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -2000, 2660, 37550, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -1510, 2660, 36550, 180)
    SetChrPos(0x102, -2710, 2660, 36550, 180)
    SetChrPos(0x103, -1310, 2660, 37550, 180)
    SetChrPos(0x104, -2910, 2660, 37550, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(-2100, 4610, 31380, 4000)
    MoveCamera(34, 29, 0, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_7312():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7312)

    def lambda_732C():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_732C)
    Sleep(50)

    def lambda_7340():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7340)

    def lambda_735A():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_735A)
    Sleep(50)

    def lambda_736E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFED72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_736E)

    def lambda_7388():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7388)
    Sleep(50)

    def lambda_739C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFED72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_739C)

    def lambda_73B6():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_73B6)
    WaitChrThread(0x101, 1)

    def lambda_73CB():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73CB)
    WaitChrThread(0x102, 1)

    def lambda_73DC():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_73DC)
    WaitChrThread(0x103, 1)

    def lambda_73ED():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_73ED)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_6F(0x79)

    #C0427
    ChrTalk(
        0x101,
        (
            "#0006F#12P……呼，失败失败，\x01",
            "还以为可以随便进入呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x103,
        (
            "#0200F#5P那个……\x01",
            "伊莉娅·普拉提耶是谁啊？\x02\x03",

            "真是很美丽的人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0429
    ChrTalk(
        0x104,
        (
            "#0305F#5P什么！？\x01",
            "你竟然不知道伊莉娅！？\x02\x03",

            "#0309F哎呀呀，太落伍了吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x103,
        "#0211F#5P（不爽）……\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        (
            "#0102F#6P啊哈哈……\x01",
            "她在克洛斯贝尔很有名哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0432
    NpcTalk(
        0x18,
        "女孩的声音",
        "#2S#11P那么，我就先告辞了。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_7592():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF15A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7592)

    def lambda_75AC():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_75AC)
    WaitChrThread(0x18, 1)

    def lambda_75C1():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75C1)

    def lambda_75CE():
        TurnDirection(0x102, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75CE)

    def lambda_75DB():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75DB)

    def lambda_75E8():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75E8)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("紫发的女孩")

    #A0433
    AnonymousTalk(
        0xFF,
        "呃，抱歉借过一下……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0434
    ChrTalk(
        0x101,
        (
            "#0002F#12P啊，不好意思，\x01",
            "我们挡了你的路呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_76C1():
        OP_98(0x101, 0xFA, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76C1)

    def lambda_76DB():
        OP_98(0x102, 0xFFFFFF06, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76DB)

    def lambda_76F5():
        OP_98(0x103, 0xFA, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_76F5)

    def lambda_770F():
        OP_98(0x104, 0xFFFFFF06, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_770F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #N0435
    NpcTalk(
        0x18,
        "紫发的女孩",
        "#1804F#5P………………（低头行礼）\x02",
    )

    CloseMessageWindow()

    def lambda_776B():

        label("loc_776B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_776B")

    QueueWorkItem2(0x0, 1, lambda_776B)

    def lambda_777D():

        label("loc_777D")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_777D")

    QueueWorkItem2(0x1, 1, lambda_777D)

    def lambda_778F():

        label("loc_778F")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_778F")

    QueueWorkItem2(0x2, 1, lambda_778F)

    def lambda_77A1():

        label("loc_77A1")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_77A1")

    QueueWorkItem2(0x3, 1, lambda_77A1)
    OP_95(0x18, -2110, 1760, 28460, 3000, 0x0)
    Fade(500)
    OP_68(430, 4610, 28350, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(28910, 0)
    OP_95(0x18, -1750, 1990, 23060, 3000, 0x0)
    OP_95(0x18, 7100, 1770, 15210, 3000, 0x0)
    Fade(800)
    OP_68(-2100, 4610, 31380, 0)
    MoveCamera(34, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    OP_0D()
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)

    #C0436
    ChrTalk(
        0x104,
        "#0300F#5P好像是剧团的女孩子啊。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#0100F#5P不过从没见过呢……\x01",
            "是最近加入的新人吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x1000)
    OP_68(-2110, 4610, 31550, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2110, 2660, 31550, 180)
    SetChrPos(0x1, -2110, 2660, 31550, 180)
    SetChrPos(0x2, -2110, 2660, 31550, 180)
    SetChrPos(0x3, -2110, 2660, 31550, 180)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x46, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_71AB end

    def Function_24_7970(): pass

    label("Function_24_7970")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2110, 4610, 31550, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2110, 2660, 31550, 180)
    SetChrPos(0x1, -2110, 2660, 31550, 180)
    SetChrPos(0x2, -2110, 2660, 31550, 180)
    SetChrPos(0x3, -2110, 2660, 31550, 180)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_24_7970 end

    def Function_25_79F1(): pass

    label("Function_25_79F1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A85")
    Jump("loc_7ACF")

    label("loc_7A85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7AA5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7ACF")

    label("loc_7AA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7ACF")

    label("loc_7AC5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7ACF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7BAB")

    #C0438
    ChrTalk(
        0x14,
        (
            "#0106F虽然总是被副局长挖苦，\x01",
            "没有一点好的回忆……\x02\x03",

            "#0100F但他很怕老婆，又喝得酩酊大醉，\x01",
            "好像也有很多苦衷啊。\x02\x03",

            "#0105F……你们两个还不累吗？\x01",
            "暂时回去休息下也没事哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C89")

    label("loc_7BAB")


    #C0439
    ChrTalk(
        0x14,
        "#0100F怎么样，调查还顺利吗？\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#0000F哈哈，还算顺利……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x103,
        (
            "#0203F虽然蔡特的嗅觉很灵敏，\x01",
            "但副局长的行动路线\x01",
            "很难确定，所以比较麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x14,
        (
            "#0106F果然很花时间啊。\x02\x03",

            "#0100F如果累了，暂时回去\x01",
            "休息一下也没事哦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_7C89")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【继续调查】\x01",      # 0
            "【中断调查】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA1")

    #C0443
    ChrTalk(
        0x101,
        (
            "#0006F嗯……的确累了，\x01",
            "暂时回去休息下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        (
            "#0203F说得也是呢。\x02\x03",

            "#0200F想要重新开始\x01",
            "调查时，\x01",
            "再拜托蔡特一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x14,
        (
            "#0100F那先把兰迪拉上，\x01",
            "一起回去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x95, 7)
    OP_29(0x15, 0x1, 0x2)
    SetScenarioFlags(0x5E, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_7DD0")

    label("loc_7DA1")


    #C0446
    ChrTalk(
        0x14,
        (
            "#0100F是吗，虽然要加油，\x01",
            "但也不要勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_79F1 end

    def Function_26_7DD8(): pass

    label("Function_26_7DD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-26820, 1750, 11890, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17650, 0)
    SetChrPos(0x103, -26000, 0, 12000, 180)
    SetChrPos(0x11C, -25000, 0, 11000, 180)
    SetChrPos(0x101, -27000, 0, 12250, 180)
    SetChrPos(0x102, -26000, 0, 13500, 180)
    SetChrPos(0x104, -27000, 0, 13750, 180)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_8065")

    def lambda_7E91():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E91)

    def lambda_7E9E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E9E)

    def lambda_7EAB():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7EAB)

    def lambda_7EB8():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7EB8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0447
    ChrTalk(
        0x101,
        (
            "#6P#0000F好，那就重新\x01",
            "开始调查吧。\x02\x03",

            "艾莉和兰迪……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x104,
        "#0309F交给我吧，随时待命！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 1, 0, 27)

    def lambda_7F33():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F33)

    def lambda_7F40():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F40)

    def lambda_7F4D():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F4D)

    def lambda_7F5A():
        OP_93(0x11C, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_7F5A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)
    WaitChrThread(0x104, 1)
    Sleep(400)

    def lambda_7F7E():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F7E)

    def lambda_7F8B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F8B)

    def lambda_7F98():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F98)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0449
    ChrTalk(
        0x102,
        (
            "#0100F我在那边的\x01",
            "露天店旁待命。\x02\x03",

            "罗伊德、缇欧，\x01",
            "你们加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_801E")
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    Jump("loc_805D")

    label("loc_801E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_805D")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x0, 0x0, 0x23)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)

    label("loc_805D")

    ClearScenarioFlags(0x95, 7)
    Jump("loc_8640")

    label("loc_8065")


    #C0450
    ChrTalk(
        0x101,
        (
            "#6P#0001F那么……副局长\x01",
            "当时是往哪个方向去了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x11C,
        "#11P#1200F………（嗅嗅）…………\x02",
    )

    CloseMessageWindow()
    OP_93(0x11C, 0x5A, 0x1F4)

    #C0452
    ChrTalk(
        0x11C,
        "#11P#1200F呜噜噜噜………\x02",
    )

    CloseMessageWindow()

    def lambda_80EB():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80EB)
    Sleep(50)

    def lambda_80FB():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80FB)
    Sleep(50)

    def lambda_810B():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_810B)
    Sleep(50)

    def lambda_811B():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_811B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0453
    ChrTalk(
        0x103,
        "#11P#0200F好像是……往东去了。\x02",
    )

    CloseMessageWindow()

    def lambda_815C():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_815C)

    def lambda_8169():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8169)

    def lambda_8176():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8176)

    def lambda_8183():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8183)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0454
    ChrTalk(
        0x101,
        (
            "#12P#0004F那好，接下来就\x01",
            "借助蔡特的嗅觉\x01",
            "来查明副局长的行动路线吧。\x02\x03",

            "#0000F在行走过程中，也必须注意\x01",
            "路上有没有掉落什么东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x102,
        (
            "#11P#0105F不过，罗伊德，\x01",
            "全员都参加调查的话，人数有点太多了吧？\x02\x03",

            "#0100F而且调查范围只限欢乐街，\x01",
            "减少一些人数比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#12P#0003F也是……确实是多了。\x02\x03",

            "#0000F艾莉、兰迪，\x01",
            "能不能请你们暂时待命呢？\x02\x03",

            "等我们把范围缩小点后，\x01",
            "再请你们帮忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x0, 0x1F4)

    #C0457
    ChrTalk(
        0x104,
        (
            "#5P#0304F收到，我随时待命。\x02\x03",

            "#0309F嗯～今天要玩些什么呢……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 1, 0, 27)

    def lambda_8363():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8363)

    def lambda_8370():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8370)

    def lambda_837D():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_837D)

    def lambda_838A():
        OP_93(0x11C, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_838A)

    #C0458
    ChrTalk(
        0x101,
        "#12P#0005F啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)
    WaitChrThread(0x104, 1)

    #C0459
    ChrTalk(
        0x103,
        "#11P#0211F完全来不及阻止他。\x02",
    )

    CloseMessageWindow()

    def lambda_83E3():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_83E3)

    def lambda_83F0():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_83F0)

    def lambda_83FD():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_83FD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0460
    ChrTalk(
        0x102,
        (
            "#11P#0106F他总是那个样子……\x02\x03",

            "#0100F好吧，到时候\x01",
            "再叫他就好。\x02\x03",

            "罗伊德，我就在那边的\x01",
            "露天店旁待命。\x01",
            "需要帮助时就叫我。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        (
            "#6P#0000F知道了，\x01",
            "我会的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0462
    ChrTalk(
        0x102,
        (
            "#5P#0100F缇欧、蔡特，\x01",
            "一会见啦。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 28)
    BeginChrThread(0x103, 1, 0, 28)
    BeginChrThread(0x11C, 1, 0, 28)
    OP_97(0x102, 0x7D0, 0x0, 0x0, 0x7D0, 0x1)
    OP_97(0x102, 0x7D0, 0x0, 0xFFFFF830, 0x7D0, 0x1)
    OP_97(0x102, 0xBB8, 0x0, 0x0, 0x7D0, 0x1)
    OP_97(0x102, 0x1F40, 0x0, 0x1770, 0x7D0, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x11C, 0x1)

    def lambda_854C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_854C)

    def lambda_8559():
        OP_93(0x11C, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_8559)
    Sleep(50)

    def lambda_8569():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8569)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)

    #C0463
    ChrTalk(
        0x103,
        "#11P#0200F那么，我们开始吧。\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，开始吧。\x02\x03",

            "我们走前面……\x01",
            "蔡特，如果我们走错路了，\x01",
            "你要提醒一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x11C,
        "#11P#1200F呜～\x02",
    )

    CloseMessageWindow()
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x0, 0x0, 0x23)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    OP_29(0x15, 0x1, 0x1)

    label("loc_8640")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    OP_49()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    OP_68(-26500, 1950, 12000, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -26500, 0, 12000, 180)
    SetChrPos(0x103, -26500, 0, 12000, 180)
    SetChrPos(0x11C, -26500, 0, 12000, 180)
    ClearChrFlags(0x14, 0x80)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x80)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_26_7DD8 end

    def Function_27_8712(): pass

    label("Function_27_8712")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)

    def lambda_8746():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8746)
    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_27_8712 end

    def Function_28_8782(): pass

    label("Function_28_8782")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_879C")
    TurnDirection(0xFE, 0x102, 500)
    Sleep(100)
    Jump("Function_28_8782")

    label("loc_879C")

    Return()

    # Function_28_8782 end

    def Function_29_879D(): pass

    label("Function_29_879D")

    TalkBegin(0xFF)

    #C0466
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "……呜～\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        (
            "#0005F哦……\x01",
            "这应该对了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        (
            "#0200F嗯，应该就是\x01",
            "这条路没错了。\x02\x03",

            "就这样前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x3)
    TalkEnd(0xFF)
    Return()

    # Function_29_879D end

    def Function_30_8826(): pass

    label("Function_30_8826")

    TalkBegin(0xFF)

    #C0469
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "……呜～\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        (
            "#0005F哦……\x01",
            "这里残留有气味吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x103,
        (
            "#0200F看来副局长\x01",
            "在这里休息过一阵子。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_30_8826 end

    def Function_31_88A7(): pass

    label("Function_31_88A7")

    TalkBegin(0xFF)

    #C0472
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "呜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        "#0003F这条路……好像错了啊？\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x103,
        (
            "#0200F是的，好像没有\x01",
            "什么气味。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_31_88A7 end

    def Function_32_891B(): pass

    label("Function_32_891B")

    TalkBegin(0xFF)

    #C0475
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "呜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x101,
        "#0003F这条路……好像错了啊？\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x103,
        (
            "#0200F是的，好像没有\x01",
            "什么气味。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_32_891B end

    def Function_33_898F(): pass

    label("Function_33_898F")

    TalkBegin(0xFF)

    #C0478
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "呜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        "#0003F这条路……好像错了啊？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x103,
        (
            "#0200F是的，好像没有\x01",
            "什么气味。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_33_898F end

    def Function_34_8A03(): pass

    label("Function_34_8A03")

    TurnDirection(0x11C, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8A4E")

    #C0481
    ChrTalk(
        0x11C,
        "#1200F……呜～！\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        "#0005F（好像不是这条路。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AC9")

    label("loc_8A4E")


    #C0483
    ChrTalk(
        0x11C,
        "#1200F……呜～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0484
    ChrTalk(
        0x101,
        "#0005F不、不是这边吗？\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x103,
        (
            "#0200F好像不是\x01",
            "这条路……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_8AC9")

    Return()

    # Function_34_8A03 end

    def Function_35_8ACA(): pass

    label("Function_35_8ACA")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_35_8ACA end

    def Function_36_8AE6(): pass

    label("Function_36_8AE6")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_36_8AE6 end

    def Function_37_8B02(): pass

    label("Function_37_8B02")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_37_8B02 end

    def Function_38_8B1E(): pass

    label("Function_38_8B1E")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, -2110, 2660, 34550, 180)
    EventEnd(0x4)
    Return()

    # Function_38_8B1E end

    def Function_39_8B3A(): pass

    label("Function_39_8B3A")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 17100, 2060, 23000, 270)
    EventEnd(0x4)
    Return()

    # Function_39_8B3A end

    def Function_40_8B56(): pass

    label("Function_40_8B56")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 13690, 90, -6130, 270)
    EventEnd(0x4)
    Return()

    # Function_40_8B56 end

    def Function_41_8B72(): pass

    label("Function_41_8B72")

    EventBegin(0x1)

    #C0486
    ChrTalk(
        0x101,
        (
            "#0003F没有必要调查『巴鲁卡』。\x01",
            "……去其它地方调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -26470, 300, 16370, 180)
    EventEnd(0x4)
    Return()

    # Function_41_8B72 end

    def Function_42_8BCA(): pass

    label("Function_42_8BCA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(12420, 1000, -5920, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x11C, 11520, 0, -5920, 270)
    SetChrPos(0x103, 12100, 0, -5140, 270)
    SetChrPos(0x101, 12680, 0, -6570, 270)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    #C0487
    ChrTalk(
        0x101,
        (
            "#11P#0005F副局长……\x01",
            "喝醉后穿过了酒店吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x103,
        (
            "#5P#0206F典型的\x01",
            "醉汉行为啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0489
    ChrTalk(
        0x101,
        (
            "#11P#0000F是啊，不过他好像\x01",
            "没在酒店落下什么东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11C, 0xB4, 0x1F4)

    #C0490
    ChrTalk(
        0x11C,
        "#6P#1200F呜噜噜噜噜……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x103, 0xB4, 0x2EE)
    Sleep(750)

    #C0491
    ChrTalk(
        0x103,
        (
            "#5P#0200F……接下来\x01",
            "好像往南边去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x2EE)

    #C0492
    ChrTalk(
        0x101,
        "#11P#0000F那好，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    SetChrPos(0x0, 11520, 0, -5920, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_29(0x15, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_42_8BCA end

    def Function_43_8E21(): pass

    label("Function_43_8E21")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    LoadChrToIndex("chr/ch34600.itc", 0x1E)
    LoadChrToIndex("chr/ch32400.itc", 0x1F)
    LoadChrToIndex("chr/ch34300.itc", 0x20)
    LoadChrToIndex("chr/ch32200.itc", 0x21)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    SetChrPos(0x1B, -1900, 1990, 20550, 180)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, -1900, 1990, 17860, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -3280, 1990, 18520, 45)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -590, 1990, 18520, 315)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-26220, 4050, 12750, 0)
    MoveCamera(32, 14, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15680, 0)
    FadeToBright(1000, 0)
    OP_68(13510, 1950, -6620, 7000)
    MoveCamera(56, 21, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(16000, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-1890, 8610, 32520, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25500, 0)
    OP_68(-2990, 3940, 18300, 8000)
    MoveCamera(41, 29, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(39500, 8000)
    PlaceName2(340, 200, "c_plac07", 0x0, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_942E")

    #A0493
    AnonymousTalk(
        0x101,
        "#0005F嗯？那是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(15000, 0)
    OP_0D()

    #C0494
    ChrTalk(
        0x1C,
        "#12P……哇，好棒啊！\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x1D,
        (
            "#6P这就是那个世界第一的\x01",
            "著名剧团『彩虹』吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x1E,
        (
            "#11P嗯，听说这个剧团的\x01",
            "门票很贵……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x1B,
        (
            "#5P各位，你们还尽兴吗？\x01",
            "那么，就出发去下一个地方吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x5A, 0x1F4)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_9108():
        OP_95(0xFE, -160, 1990, 19900, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9108)
    Sleep(500)

    #C0498
    ChrTalk(
        0x1D,
        (
            "#6P咦咦～不去观看\x01",
            "彩虹剧团的公演吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 1)
    OP_93(0x1B, 0xE1, 0x1F4)

    #C0499
    ChrTalk(
        0x1B,
        (
            "#11P呵呵，其实今天的公演\x01",
            "只有夜间场。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x1B,
        (
            "#11P晚上是自由活动时间，\x01",
            "请各位剧团爱好者\x01",
            "一定要来捧场。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x1B,
        (
            "#11P……接下来，\x01",
            "我将带各位去……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_91EA)

    def lambda_91F7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_91F7)

    def lambda_9204():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9204)

    def lambda_9211():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9211)
    WaitChrThread(0x1B, 1)

    def lambda_9222():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9222)
    Sleep(1000)
    WaitChrThread(0x1E, 1)

    def lambda_9243():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9243)
    Sleep(500)
    WaitChrThread(0x1C, 1)

    def lambda_9264():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9264)
    Sleep(300)
    WaitChrThread(0x1D, 1)

    def lambda_9285():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_9285)
    WaitChrThread(0x1B, 1)

    def lambda_92A3():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_92A3)
    WaitChrThread(0x1E, 1)

    def lambda_92C1():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_92C1)
    WaitChrThread(0x1C, 1)

    def lambda_92DF():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_92DF)
    WaitChrThread(0x1D, 1)

    def lambda_92FD():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_92FD)

    #A0502
    AnonymousTalk(
        0x104,
        (
            "#0300F我平时总来这附近玩……\x01",
            "经常能看见很多游客呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0503
    AnonymousTalk(
        0x101,
        (
            "#0000F嗯，最近有很多外国人\x01",
            "乘坐导力巴士来这里观光。\x02",
        )
    )

    CloseMessageWindow()

    #A0504
    AnonymousTalk(
        0x102,
        (
            "#0104F这条欢乐街\x01",
            "好像是游客必来的地方。\x02\x03",

            "#0100F如果外国人发生了什么事，\x01",
            "就可能会演变为国际问题……\x01",
            "所以我们警察的工作很重要呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0505
    AnonymousTalk(
        0x103,
        "#0200F原来如此，确实有道理。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_942E")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0506
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢乐街是位于城市北侧的商业区。\x02",
        )
    )

    CloseMessageWindow()

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "酒店、有名的剧院等设施鳞次栉比，\x01",
            "并有许多游客前来游玩。\x02",
        )
    )

    CloseMessageWindow()

    #A0508
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一些设施在前期并不会开放，\x01",
            "但随着故事的展开，\x01",
            "可以前去拜访一番。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearMapObjFlags(0x5, 0x1000)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrPos(0xC, -50000, 10, 12070, 220)
    BeginChrThread(0xC, 0, 0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F9")
    OP_68(21040, 1950, 11840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    Jump("loc_9676")

    label("loc_95F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963A")
    OP_68(13270, 1950, -19100, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_9676")

    label("loc_963A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9676")
    OP_68(-39280, 1950, 12420, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)

    label("loc_9676")

    SetScenarioFlags(0x45, 0)
    EventEnd(0x5)
    Return()

    # Function_43_8E21 end

    def Function_44_967C(): pass

    label("Function_44_967C")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-13000, 7940, 33500, 0)
    MoveCamera(40, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -2700, 1990, 21500, 0)
    SetChrPos(0x104, -1300, 1990, 21500, 0)
    SetChrPos(0x103, -2700, 1990, 20300, 0)
    SetChrPos(0x102, -1300, 1990, 20300, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_68(4000, 7940, 33500, 6000)
    MoveCamera(40, 13, 0, 6000)
    SetCameraDistance(30000, 6000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(-2000, 11940, 34000, 0)
    MoveCamera(31, -13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(28000, 0)
    MoveCamera(21, -13, 0, 9000)
    SetCameraDistance(37000, 9000)
    PlaceName2(340, 200, "c_plac11", 0x0, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(-2000, 2740, 24500, 0)
    MoveCamera(32, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(19950, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_0D()

    #C0509
    ChrTalk(
        0x103,
        (
            "#4P#0202F仔细一看……\x01",
            "还真是一座很气派的建筑物啊。\x02\x03",

            "而且看起来好像还比较新。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x102,
        (
            "#0104F大概建有二十年了吧。\x02\x03",

            "#0100F与市政厅那些建筑相比，\x01",
            "这里并不算很老。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x101,
        (
            "#6P#0003F（彩虹剧团吗……）\x02\x03",

            "#0008F（小时候，\x01",
            "  大哥和塞茜尔姐姐带我\x01",
            "  来过几次……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    #C0512
    ChrTalk(
        0x104,
        "#0305F#11P怎么啦？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#6P#0004F不……没什么。\x02\x03",

            "#0000F我们快点进去调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -2000, 1990, 19500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetScenarioFlags(0x80, 3)
    EventEnd(0x5)
    Return()

    # Function_44_967C end

    def Function_45_99AB(): pass

    label("Function_45_99AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2000, 3760, 35000, 0)
    MoveCamera(25, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -2700, 2660, 35500, 180)
    SetChrPos(0x102, -1300, 2660, 35500, 180)
    SetChrPos(0x103, -2700, 2660, 36900, 180)
    SetChrPos(0x104, -1300, 2660, 36900, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_68(-2000, 2860, 27500, 5000)
    MoveCamera(45, 27, 0, 5000)
    SetCameraDistance(18000, 5000)

    def lambda_9AC0():
        OP_96(0xFE, 0xFFFFF574, 0x6E0, 0x68B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AC0)

    def lambda_9ADA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9ADA)
    Sleep(250)

    def lambda_9AEE():
        OP_96(0xFE, 0xFFFFFAEC, 0x6E0, 0x68B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9AEE)

    def lambda_9B08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9B08)
    Sleep(100)

    def lambda_9B1C():
        OP_96(0xFE, 0xFFFFF574, 0x6E0, 0x6E28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9B1C)

    def lambda_9B36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B36)
    Sleep(250)

    def lambda_9B4A():
        OP_96(0xFE, 0xFFFFFAEC, 0x6E0, 0x6E28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B4A)

    def lambda_9B64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9B64)
    Sleep(1000)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x101, 1)

    def lambda_9B97():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B97)
    WaitChrThread(0x102, 1)

    def lambda_9BA8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9BA8)
    WaitChrThread(0x103, 1)

    def lambda_9BB9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9BB9)
    WaitChrThread(0x104, 1)

    def lambda_9BCA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BCA)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0514
    ChrTalk(
        0x104,
        (
            "#5P#0303F那么……要怎么做呢？\x02\x03",

            "#0301F眼下，线索\x01",
            "只有『鲁巴彻』这一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x103,
        (
            "#0200F『银』这个名字\x01",
            "也勉强可以算是一条线索……\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        "#6P#0008F……是啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0517
    ChrTalk(
        0x101,
        (
            "#6P#0003F──各位。\x02\x03",

            "#0013F我们去拜访\x01",
            "一下『鲁巴彻商会』吧？\x02",
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
    Sleep(1000)

    def lambda_9D23():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9D23)
    Sleep(50)

    def lambda_9D33():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9D33)
    Sleep(50)

    def lambda_9D43():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9D43)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    #C0518
    ChrTalk(
        0x102,
        "#0105F#11P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x104,
        "#5P#0301F真的假的……！？\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        (
            "#6P#0000F只是作为警察对案件的调查，\x01",
            "去进行一下普通的案情询问而已。\x02\x03",

            "#0003F虽然还不确定恐吓信\x01",
            "是不是鲁巴彻的会长\x01",
            "寄出的……\x02\x03",

            "#0001F但我觉得如果一直避开麻烦，\x01",
            "是没办法找出真相的。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x104,
        "#5P#0303F嗯……\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        "#0201F#5P……确实有一定的道理。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        (
            "#6P#0006F而且，我觉得这也是一个好机会。\x02\x03",

            "#0008F做了那种事还能在市里\x01",
            "大摇大摆，四处横行的家伙……\x02\x03",

            "#0013F我们或许可以借此机会，\x01",
            "对他们的真实情况一探究竟。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x104,
        "#5P#0302F嗯……原来如此啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9F94():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F94)
    Sleep(50)

    def lambda_9FA4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9FA4)
    Sleep(50)

    def lambda_9FB4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9FB4)
    Sleep(300)
    OP_64(0x102)

    #C0525
    ChrTalk(
        0x101,
        (
            "#6P#0005F那个，你还是担心吗？\x02\x03",

            "#0000F如果是的话，\x01",
            "就由我和兰迪两个人……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0526
    ChrTalk(
        0x103,
        "#0211F#5P罗伊德前辈……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0527
    ChrTalk(
        0x101,
        (
            "#6P#0011F不、不是！\x01",
            "我并没有那个意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x102,
        (
            "#0104F#11P不……\x01",
            "我们并没有担心。\x02\x03",

            "#0108F嗯，我觉得只是前去拜访的话\x01",
            "并不会那么危险。\x02\x03",

            "这个城市中的黑手党\x01",
            "到底是何种存在……\x02\x03",

            "#0102F这也是个了解他们的好机会吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A121():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A121)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    #C0529
    ChrTalk(
        0x101,
        "#6P#0005F啊，是啊……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x104,
        (
            "#5P#0305F什么啊，大小姐。\x01",
            "你是不是话里有话啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x102,
        (
            "#0104F#11P呵呵，那是你的错觉吧。\x02\x03",

            "#0100F而关于恐吓信，\x01",
            "也有可能会发现一些\x01",
            "预料之外的真相呢。\x02\x03",

            "我们快点去拜访一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        "#6P#0000F是啊……！\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x103,
        (
            "#0203F#5P根据数据库的情报……\x02\x03",

            "#0201F『鲁巴彻商会』的大楼\x01",
            "在后巷中间的\x01",
            "一条小巷的最深处。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x104,
        (
            "#5P#0304F哎，在那么奇怪偏僻的角落啊。\x02\x03",

            "#0300F怪不得经常能在后巷看到那些家伙，\x01",
            "原来那里就是黑手党的据点啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18150, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2000, 1760, 26500, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x5, 0x1000)
    SetScenarioFlags(0x80, 6)
    OP_29(0x42, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_45_99AB end

    def Function_46_A333(): pass

    label("Function_46_A333")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02500.itp")
    OP_68(-2000, 3000, 20500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -1500, 1990, 16500, 0)
    SetChrPos(0x102, -2700, 1990, 16500, 0)
    SetChrPos(0x103, -2700, 1990, 15300, 0)
    SetChrPos(0x104, -1500, 1990, 15300, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -2000, 2660, 36000, 180)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, -2600, 2660, 36000, 180)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x4, 0x17)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -5300, 0, 1800, 100)
    OP_D3(0x17, 0x0, 0x186A0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_70(0x4, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    SetMapObjFlags(0x5, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)

    def lambda_A4FA():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x5014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4FA)
    Sleep(50)

    def lambda_A517():
        OP_96(0xFE, 0xFFFFFA24, 0x7C6, 0x5014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A517)
    Sleep(50)

    def lambda_A534():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x4B64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A534)
    Sleep(50)

    def lambda_A551():
        OP_96(0xFE, 0xFFFFFA24, 0x7C6, 0x4B64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A551)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0535
    ChrTalk(
        0x101,
        "#11P#0005F咦……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(-2000, 3600, 32000, 2000)
    OP_6F(0x1)

    def lambda_A617():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_A617)

    def lambda_A628():
        OP_95(0xFE, -2000, 2660, 31800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A628)
    Sleep(500)

    def lambda_A645():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_A645)

    def lambda_A656():
        OP_95(0xFE, -2600, 2660, 32500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A656)
    Sleep(700)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)

    #C0536
    ChrTalk(
        0x102,
        "#0105F#1P啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0537
    NpcTalk(
        0x15,
        "老绅士",
        "#2505F#5P哦……！？\x02",
    )

    CloseMessageWindow()

    #N0538
    NpcTalk(
        0x16,
        "年轻男性",
        "#2605F#5P艾莉小姐……！\x02",
    )

    CloseMessageWindow()

    def lambda_A71B():
        OP_95(0xFE, -2000, 1990, 24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A71B)
    Sleep(250)

    def lambda_A738():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A738)
    Sleep(2000)
    Fade(500)
    OP_68(-2000, 3000, 22800, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x102, -2000, 1990, 21000, 0)
    SetChrPos(0x101, 100, 1990, 21200, 315)
    SetChrPos(0x103, -1500, 1990, 20200, 0)
    SetChrPos(0x104, -700, 1990, 19600, 0)
    SetCameraDistance(19000, 2000)
    OP_0D()
    Sleep(600)

    def lambda_A7D9():
        OP_95(0xFE, -2000, 1990, 21700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7D9)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x10)

    #C0539
    ChrTalk(
        0x102,
        "#0105F#12P外公……阿奈斯特先生。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#0005F（咦……）\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x103,
        "#0205F#4P（艾莉前辈的外公……？）\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("老绅士")

    #A0542
    AnonymousTalk(
        0xFF,
        (
            "呵呵，最近难得见一面，\x01",
            "你看上去好像很精神啊。\x02\x03",

            "有没有努力工作呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0543
    ChrTalk(
        0x102,
        (
            "#12P#0108F是、是的……\x02\x03",

            "#0103F……虽然我还是新人，\x01",
            "肯定会有一些不足的地方……\x02\x03",

            "#0102F但我一定会努力加油，\x01",
            "不让麦克道尔家蒙羞。\x02",
        )
    )

    CloseMessageWindow()

    #N0544
    NpcTalk(
        0x15,
        "老绅士",
        (
            "#5P#2503F哈哈……我之前就说过了，\x01",
            "你不用介意家里的事。\x02\x03",

            "#2500F那边的几位，是你的同事们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        "#12P#0100F嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        (
            "#0003F#12P──初次见面。\x02\x03",

            "#0000F我是克洛斯贝尔警察局·特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x103,
        "#12P#0204F我是缇欧·普拉托。（低头行礼）\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x104,
        (
            "#12P#0300F您好，\x01",
            "我叫兰迪·奥兰多。\x02",
        )
    )

    CloseMessageWindow()

    #N0549
    NpcTalk(
        0x15,
        "老绅士",
        (
            "#5P#2503F嗯，我的名字是\x01",
            "亨利·麦克道尔。\x02\x03",

            "#2500F我这个孙女\x01",
            "承蒙各位照顾了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#0012F#12P不，没那回事。\x02\x03",

            "#0000F受照顾的\x01",
            "反倒是我们──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    #C0551
    ChrTalk(
        0x104,
        (
            "#12P#0304F嗯，大小姐在写\x01",
            "报告书等书面文件时\x01",
            "确实帮了我们大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x103,
        (
            "#6P#0211F我觉得兰迪前辈\x01",
            "也应该帮点忙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)

    #C0553
    ChrTalk(
        0x102,
        "#12P#0109F那、那个……\x02",
    )

    CloseMessageWindow()

    #N0554
    NpcTalk(
        0x15,
        "麦克道尔老人",
        (
            "#5P#2500F呵呵……\x01",
            "工作内容充实就最好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x16,
        (
            "#2606F#5P不过，小姐……\x02\x03",

            "#2601F您也该不时\x01",
            "回趟家比较好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        (
            "#12P#0108F……很、很抱歉。\x02\x03",

            "#0106F因为总算能自己独立生活了，\x01",
            "就不想太依赖家里……\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x16,
        "#2601F#5P但是──\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x190)

    #N0558
    NpcTalk(
        0x15,
        "麦克道尔老人",
        (
            "#11P#2503F没关系，阿奈斯特。\x02\x03",

            "#2500F这正说明了\x01",
            "艾莉的决心十分坚定。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x102, 400)
    Sleep(300)

    #N0559
    NpcTalk(
        0x15,
        "麦克道尔老人",
        (
            "#5P#2500F你自己所选择的道路……\x01",
            "要走到自己满意为止啊。\x02\x03",

            "虽然不能公私不分，\x01",
            "但我也会尽力提供协助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x102,
        (
            "#12P#0104F……是。\x01",
            "谢谢您，外公。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x190)
    Sleep(300)

    #N0561
    NpcTalk(
        0x15,
        "麦克道尔老人",
        (
            "#11P#2500F──我们走吧，\x01",
            "阿奈斯特。\x02\x03",

            "接下来是跟工商协会的聚会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x16,
        "#2600F#5P是的，五点开始。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_AEBD():

        label("loc_AEBD")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_AEBD")

    QueueWorkItem2(0x101, 2, lambda_AEBD)

    def lambda_AECF():

        label("loc_AECF")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_AECF")

    QueueWorkItem2(0x102, 2, lambda_AECF)

    def lambda_AEE1():

        label("loc_AEE1")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_AEE1")

    QueueWorkItem2(0x103, 2, lambda_AEE1)

    def lambda_AEF3():

        label("loc_AEF3")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_AEF3")

    QueueWorkItem2(0x104, 2, lambda_AEF3)
    OP_92(0x15, 0xFFFFE890, 0x4650, 0x1F4)

    def lambda_AF12():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_AF12)
    Sleep(150)
    OP_92(0x16, 0xFFFFE5D4, 0x490C, 0x1F4)

    def lambda_AF3C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AF3C)
    Sleep(4000)
    Fade(500)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    SetChrPos(0x15, -4900, 1770, 9000, 180)
    SetChrPos(0x16, -4900, 1770, 10400, 180)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(-3000, 2000, 1800, 0)
    MoveCamera(328, 10, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13000, 0)

    def lambda_AFE2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_AFE2)
    Sleep(50)

    def lambda_AFFF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AFFF)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    Sound(462, 0, 100, 0)
    OP_71(0x4, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x4)

    def lambda_B036():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B036)

    def lambda_B050():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_B050)
    Sleep(150)

    def lambda_B064():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B064)
    Sleep(500)

    def lambda_B081():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_B081)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    Sound(461, 0, 100, 0)
    OP_71(0x4, 0x10F, 0x12C, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Sound(470, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 47)
    Sleep(300)
    Sound(457, 0, 100, 0)
    Sleep(1700)
    EndChrThread(0x17, 0xFF)
    Fade(500)
    OP_68(2500, 2000, -500, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x17, -5300, 0, 1800, 100)
    OP_D3(0x17, 0x0, 0x186A0, 0x0, 0x0)
    OP_68(12500, 2000, 6500, 5000)
    MoveCamera(36, 13, 0, 5000)
    OP_9F(0x0, 0x17)
    OP_9F(0x1, 7500, 0, 3500)
    OP_9F(0x1, 17500, 0, 9500)
    OP_9F(0x1, 31500, 0, 10500)
    OP_9F(0x2, 0x17, 6500, 0x6)
    SetChrFlags(0x17, 0x80)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x1000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Fade(500)
    OP_68(-700, 3000, 20800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    #C0563
    ChrTalk(
        0x104,
        (
            "#5P#0305F哇哦！\x01",
            "好豪华的车啊。\x02\x03",

            "#0302F大小姐，你家\x01",
            "果然很有钱吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x102,
        "#0109F#5P那……那个。\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(600)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0565
    ChrTalk(
        0x101,
        "#5P#0005F#4S啊啊啊啊！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B2B6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B2B6)
    Sleep(50)
    OP_93(0x103, 0x2D, 0x1F4)

    #C0566
    ChrTalk(
        0x104,
        "#12P#0305F啊……\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x103,
        "#6P#0205F罗伊德前辈……？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#5P#0007F亨利·麦克道尔……！\x02\x03",

            "那不是克洛斯贝尔市\x01",
            "市长的名字吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0569
    ChrTalk(
        0x104,
        "#12P#0301F什、什么……！？\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x103,
        (
            "#6P#0201F真、真的吗……？\x02\x03",

            "#0205F──啊，\x01",
            "数据库里\x01",
            "好像是这么记录的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0571
    ChrTalk(
        0x102,
        "#0106F#5P呼……\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x190)
    Sleep(300)

    #C0572
    ChrTalk(
        0x102,
        (
            "#0102F#5P──我倒是觉得，你们之前一直\x01",
            "都没有察觉到这点，才比较不可思议。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B471():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B471)
    Sleep(100)

    def lambda_B481():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B481)
    Sleep(50)
    OP_93(0x104, 0x13B, 0x1F4)

    #C0573
    ChrTalk(
        0x101,
        (
            "#11P#0002F也、也不是……\x01",
            "最开始听到艾莉的姓时\x01",
            "是有些在意。\x02\x03",

            "不过后来发生了那么多事，\x01",
            "也就逐渐淡忘了。\x02\x03",

            "#0006F──不过确实很丢脸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵，这没什么可介意的啊。\x02\x03",

            "不管外公是什么人，\x01",
            "都跟我没关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        "#11P#0005F咦……\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x102,
        (
            "#0106F#5P……比起那些，我们还是快点\x01",
            "去向伊莉娅小姐他们报告吧。\x02\x03",

            "#0101F虽然没面子……但也必须去把\x01",
            "案子换人接手的事说清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x101,
        "#11P#0001F啊，是啊……说得也是。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x104,
        (
            "#12P#0305F不过，大小姐的外公\x01",
            "为什么会来彩虹剧团啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x102,
        (
            "#0105F#5P啊，对哦……\x02\x03",

            "#0103F好像是因为剧团这次的新剧目，\x01",
            "要配合纪念庆典进行公演……\x02\x03",

            "#0100F所以外公才来这里\x01",
            "对相关事宜进行磋商的吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(-2000, 3940, 21500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2000, 1990, 21500, 0)
    SetChrPos(0x1, -2000, 1990, 21500, 0)
    SetChrPos(0x2, -2000, 1990, 21500, 0)
    SetChrPos(0x3, -2000, 1990, 21500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    ClearMapObjFlags(0x5, 0x1000)
    SetScenarioFlags(0x81, 4)
    EndChrThread(0xD, 0x0)
    BeginChrThread(0xD, 0, 0, 3)
    EventEnd(0x5)
    Return()

    # Function_46_A333 end

    def Function_47_B7C2(): pass

    label("Function_47_B7C2")


    def lambda_B7C7():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B7C7)
    Sleep(600)

    def lambda_B7DF():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x157C, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_B7DF)
    Sleep(600)

    def lambda_B7F7():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B7F7)
    Return()

    # Function_47_B7C2 end

    def Function_48_B808(): pass

    label("Function_48_B808")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05200.itc", 0x1E)
    OP_68(-2000, 2800, 29800, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -2600, 1850, 25800, 0)
    SetChrPos(0x102, -1400, 1850, 25800, 0)
    SetChrPos(0x103, -2600, 1990, 24400, 0)
    SetChrPos(0x104, -1400, 1990, 24400, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -2000, 1760, 27800, 180)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFlags(0x5, 0x1000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SubItemNumber(0x324, 1)
    OP_68(-2000, 2800, 26800, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(1637, 255, 100, 0)    #voice#Rixia
    Sleep(1000)

    #C0580
    ChrTalk(
        0x18,
        (
            "#1806F#5P那个……感觉总是在\x01",
            "给各位添麻烦啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x101,
        (
            "#12P#0012F没事，别介意哦。\x02\x03",

            "#0000F警察的工作本来就是要\x01",
            "脚踏实地地反复做一些无用功啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x103,
        "#12P#0202F这就是所谓的预防犯罪了。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x104,
        (
            "#0302F#12P对对，莉夏。\x02\x03",

            "#0309F你别担心我们，\x01",
            "预演要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x18,
        "#1802F#5P好的，谢谢各位。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x104, 500)

    #C0585
    ChrTalk(
        0x101,
        "#6P#0005F预演？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0586
    ChrTalk(
        0x104,
        (
            "#0305F#11P怎么，你不知道啊？\x02\x03",

            "#0300F彩虹剧团每次在\x01",
            "新剧目的正式公演之前，都会\x01",
            "举行一次预演，是吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x18,
        (
            "#1804F#5P是、是的。\x01",
            "我这次是第一次参加……\x02\x03",

            "#1802F预演时似乎会邀请国内外的\x01",
            "相关人员和各家媒体前来观看。\x02\x03",

            "赞助公演的那些\x01",
            "大人物好像也会来……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB90():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB90)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0588
    ChrTalk(
        0x101,
        "#12P#0000F这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0589
    ChrTalk(
        0x102,
        (
            "#0105F#12P难道……\x01",
            "也邀请麦克道尔市长了？\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x18,
        (
            "#1805F#5P啊，对啊，\x01",
            "市长是主要嘉宾。\x02\x03",

            "#1804F好像是因为公演配合了纪念庆典，\x01",
            "所以市长也给予了大力支持呢。\x02\x03",

            "#1802F今天市长也在百忙之中\x01",
            "抽空来这里慰问我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x102,
        "#0100F#12P这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0592
    ChrTalk(
        0x102,
        (
            "#0104F#12P──莉夏。\x01",
            "预演，请加油哦。\x02\x03",

            "#0102F莉夏的话，就算是第一次，\x01",
            "也绝对没有问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x18,
        "#1805F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x101,
        (
            "#12P#0002F对啊，看你练习的情况，\x01",
            "就完全不需要担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x104,
        "#0309F#12P哦哦，你一定会表演得很精彩！\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x103,
        "#12P#0204F……我也很期待。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x18,
        (
            "#1809F#5P谢、谢谢各位。\x01",
            "那个……我现在很有信心了。\x02\x03",

            "#1802F那么，我回去排练了。\x02\x03",

            "各位，谢谢你们。\x02",
        )
    )

    CloseMessageWindow()
    Sound(1638, 255, 100, 0)    #voice#Rixia
    Sleep(1000)
    OP_93(0x18, 0x0, 0x1F4)
    OP_68(-2000, 3800, 31800, 3500)

    def lambda_BE58():
        OP_95(0xFE, -2000, 2660, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BE58)
    WaitChrThread(0x18, 1)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_6F(0x79)

    def lambda_BE93():
        OP_95(0xFE, -2000, 2660, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BE93)
    Sleep(500)

    def lambda_BEB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_BEB0)
    WaitChrThread(0x18, 2)
    WaitChrThread(0x18, 1)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    Sleep(500)
    Fade(500)
    OP_68(-2000, 3000, 25100, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_BF7C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF7C)
    Sleep(50)

    def lambda_BF8C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BF8C)
    Sleep(50)

    def lambda_BF9C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BF9C)
    Sleep(50)

    def lambda_BFAC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BFAC)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    #C0598
    ChrTalk(
        0x101,
        (
            "#0006F#5P……呼……\x02\x03",

            "#0000F我们也回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x104,
        "#0306F#11P好……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#6P#0206F……总觉得\x01",
            "松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        "#0103F#5P……是啊…………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_D5(0x1E)
    OP_68(-2000, 3710, 26800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -2000, 1760, 26800, 180)
    SetChrPos(0x102, -2000, 1760, 26800, 180)
    SetChrPos(0x103, -2000, 1760, 26800, 180)
    SetChrPos(0x104, -2000, 1760, 26800, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x5, 0x1000)
    SetScenarioFlags(0x81, 5)
    OP_C7(0x0, 0x1000)
    OP_29(0x42, 0x1, 0x9)
    OP_1B(0x1, 0x0, 0x3E)
    OP_1B(0x2, 0x0, 0x3F)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7000")
    ReplaceBGM("ed7101", "ed7000")
    ReplaceBGM("ed7100", "ed7102")
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_48_B808 end

    def Function_49_C121(): pass

    label("Function_49_C121")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("chr/ch05200.itc", 0x1F)
    LoadChrToIndex("chr/ch05100.itc", 0x20)
    LoadChrToIndex("apl/ch50219.itc", 0x21)
    LoadChrToIndex("apl/ch50220.itc", 0x22)
    LoadChrToIndex("apl/ch50238.itc", 0x23)
    LoadChrToIndex("apl/ch50239.itc", 0x24)
    OP_68(15000, 14100, 24500, 0)
    MoveCamera(320, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, 15000, 0, 15000, 0)
    SetChrPos(0x1, 15000, 0, 15000, 0)
    SetChrPos(0x2, 15000, 0, 15000, 0)
    SetChrPos(0x3, 15000, 0, 15000, 0)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 26300, 14100, 24500, 270)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x18, 19300, 13100, 24500, 270)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
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
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01801.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01700.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis155.itp")
    LoadEffect(0x0, "event\\eva04_00.eff")
    OP_68(17000, 14100, 24500, 3000)
    SetCameraDistance(15500, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    SetChrChip(0x0, 0x1A, 0x1E, 0x12C)

    def lambda_C354():
        OP_9D(0xFE, 0x4B64, 0x332C, 0x5FB4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_C354)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x1A, 1)
    PlayEffect(0x0, 0xFF, 0x1A, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x1A, 0x1)
    Sound(42, 0, 100, 0)
    Sleep(10)
    Sound(31, 0, 100, 0)
    Sleep(500)
    SetChrChip(0x1, 0x1A, 0x0, 0x0)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    OP_0D()
    OP_6F(0x10)

    #C0602
    ChrTalk(
        0x1A,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#11P#40W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(19300, 13900, 24500, 0)
    MoveCamera(50, 31, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1A, 0x2)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x7)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    Sleep(1000)
    Sound(534, 0, 90, 0)
    StopBGM(0x1388)
    MoveCamera(40, 31, 0, 2000)
    SetCameraDistance(20500, 2000)
    BeginChrThread(0x1A, 3, 0, 53)

    def lambda_C49D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_C49D)

    def lambda_C4AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_C4AE)
    Sleep(600)
    SetChrSubChip(0x18, 0x1)
    Sleep(130)
    SetChrSubChip(0x18, 0x2)
    Sleep(130)
    SetChrSubChip(0x18, 0x3)
    Sleep(400)
    WaitChrThread(0x1A, 2)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    Sound(1640, 255, 100, 0)    #voice#Rixia
    Sleep(1600)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0603
    AnonymousTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#40W……………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    ClearChrFlags(0x18, 0x20)
    ClearChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    OP_93(0x18, 0x0, 0x190)
    Sleep(300)
    SetCameraDistance(21500, 3000)

    def lambda_C5A5():
        OP_96(0xFE, 0x4B64, 0x332C, 0x7788, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C5A5)
    WaitChrThread(0x18, 1)
    PlayEffect(0x0, 0xFF, 0x18, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x4)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C617():
        OP_9D(0xFE, 0x4B64, 0x13EC, 0x8B10, 0x514, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C617)
    Sound(814, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x18, 1)
    OP_6F(0x10)
    ClearChrFlags(0x18, 0x20)
    ClearChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    OP_68(-2000, 2700, 28500, 0)
    MoveCamera(320, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x18, 6000, 1760, 26000, 270)
    ClearChrFlags(0x19, 0x4)
    SetChrPos(0x19, -2000, 1990, 18600, 0)
    MoveCamera(330, 17, 0, 3500)
    SetCameraDistance(17000, 3500)

    def lambda_C6E7():
        OP_96(0xFE, 0xFFFFF830, 0x6E0, 0x6F54, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C6E7)
    FadeToBright(1000, 0)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x0, 0x1F4)
    OP_6F(0x50)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)

    #N0604
    NpcTalk(
        0x19,
        "女性的声音",
        "你来得很早啊，莉夏。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1635, 255, 100, 0)    #voice#Rixia
    OP_68(-2000, 2700, 27600, 3000)

    def lambda_C772():
        OP_96(0xFE, 0xFFFFF830, 0x6E0, 0x67E8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_C772)

    def lambda_C78C():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_C78C)
    WaitChrThread(0x19, 1)
    OP_6F(0x1)

    #C0605
    ChrTalk(
        0x18,
        "#1805F#11P伊莉娅小姐……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0606
    AnonymousTalk(
        0x19,
        (
            "怎么，是因为太期待\x01",
            "下午的排练吗？\x02\x03",

            "我已经是个\x01",
            "十足的舞痴了……\x02\x03",

            "没想到你也\x01",
            "很有这个潜质啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0607
    ChrTalk(
        0x18,
        (
            "#1809F#11P啊哈哈，没有啦……\x02\x03",

            "我还没有自信能达到伊莉娅小姐\x01",
            "那种痴迷的程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x19,
        (
            "#6P#1704F呵呵，嘴上这么说，\x01",
            "预演排练时却很拼命啊。\x02\x03",

            "#1702F你的演技很不错哦。\x02\x03",

            "也终于足够\x01",
            "当我的小对手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x18,
        (
            "#1802F#11P伊莉娅小姐……\x02\x03",

            "#1804F……如果真的是那样，\x01",
            "也全都是托了伊莉娅小姐的福。\x02\x03",

            "从前，我只知道那条生来便已被决定好的道路，\x01",
            "是你给我带来了崭新的光芒……\x02\x03",

            "#1802F……呵呵，还有，这次也必须\x01",
            "谢谢他们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x19,
        "#6P#1705F哎……\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x18,
        (
            "#1804F#11P呵呵，没什么。\x02\x03",

            "#1800F今天的练习，是再\x01",
            "完善第三幕的表演吧？\x02\x03",

            "我会加油的。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x19,
        (
            "#6P#1702F哦，很有干劲嘛。\x02\x03",

            "#1700F嗯，我也\x01",
            "绝对不会输的哦～\x02\x03",

            "#1709F好，到下个月的正式公演之前，\x01",
            "要练习得比现在好百倍～！\x02\x03",

            "跟我来，莉夏！\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x18,
        "#1809F#11P是，伊莉娅小姐……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 6000)
    BeginChrThread(0x101, 3, 0, 50)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    StopBGM(0x1388)
    WaitBGM()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CB75")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CB8F")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CBA9")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CBC3")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CBDD")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CBF7")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CC11")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CC2B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC4B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC86")

    label("loc_CC4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC6B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC86")

    label("loc_CC6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC86")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CC86")

    OP_29(0x41, 0x4, 0x10)
    OP_29(0x42, 0x4, 0x10)
    OP_29(0x43, 0x4, 0x10)
    OP_29(0x41, 0x4, 0x20)
    OP_29(0x43, 0x4, 0x20)
    SubItemNumber(0x325, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCC2")
    OP_29(0xE, 0x4, 0x40)
    Jump("loc_CCD4")

    label("loc_CCC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD4")
    OP_29(0xE, 0x4, 0x40)

    label("loc_CCD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCE6")
    OP_29(0x10, 0x4, 0x40)

    label("loc_CCE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD04")
    OP_29(0x11, 0x4, 0x40)
    Jump("loc_CD16")

    label("loc_CD04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD16")
    OP_29(0x11, 0x4, 0x40)

    label("loc_CD16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD34")
    OP_29(0x12, 0x4, 0x40)
    Jump("loc_CD46")

    label("loc_CD34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD46")
    OP_29(0x12, 0x4, 0x40)

    label("loc_CD46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD64")
    OP_29(0x13, 0x4, 0x40)
    Jump("loc_CD76")

    label("loc_CD64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD76")
    OP_29(0x13, 0x4, 0x40)

    label("loc_CD76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD94")
    OP_29(0x14, 0x4, 0x40)
    Jump("loc_CDA6")

    label("loc_CD94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDA6")
    OP_29(0x14, 0x4, 0x40)

    label("loc_CDA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDC4")
    OP_29(0x15, 0x4, 0x40)
    Jump("loc_CDD6")

    label("loc_CDC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDD6")
    OP_29(0x15, 0x4, 0x40)

    label("loc_CDD6")

    SubItemNumber(0x341, 1)
    SubItemNumber(0x33D, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x26, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_49_C121 end

    def Function_50_CEB5(): pass

    label("Function_50_CEB5")

    BeginChrThread(0x19, 3, 0, 51)
    Sleep(100)
    BeginChrThread(0x18, 3, 0, 52)
    WaitChrThread(0x19, 3)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    WaitChrThread(0x18, 3)

    def lambda_CEEC():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CEEC)
    Sleep(50)

    def lambda_CF09():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CF09)
    Sleep(300)

    def lambda_CF26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_CF26)
    Sleep(50)

    def lambda_CF3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_CF3A)
    Return()

    # Function_50_CEB5 end

    def Function_51_CF47(): pass

    label("Function_51_CF47")


    def lambda_CF4C():
        OP_96(0xFE, 0xFFFFF63C, 0x6E0, 0x73A0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CF4C)
    WaitChrThread(0x19, 1)

    def lambda_CF6A():
        OP_96(0xFE, 0xFFFFF63C, 0xA64, 0x8340, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_CF6A)
    WaitChrThread(0x19, 1)
    Return()

    # Function_51_CF47 end

    def Function_52_CF84(): pass

    label("Function_52_CF84")


    def lambda_CF89():

        label("loc_CF89")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_CF89")

    QueueWorkItem2(0x18, 2, lambda_CF89)

    def lambda_CF9B():
        OP_96(0xFE, 0xFFFFFA88, 0x6E0, 0x7080, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CF9B)
    WaitChrThread(0x18, 1)
    Sleep(600)
    EndChrThread(0x18, 0x2)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_CFC7():
        OP_95(0xFE, -1400, 2660, 32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CFC7)
    WaitChrThread(0x18, 1)
    Return()

    # Function_52_CF84 end

    def Function_53_CFE1(): pass

    label("Function_53_CFE1")

    OP_A1(0xFE, 0x7D0, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_53_CFE1 end

    def Function_54_CFF7(): pass

    label("Function_54_CFF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-23500, 1000, 10000, 0)
    MoveCamera(75, 27, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11000, 0)
    SetChrPos(0x101, -16000, 0, 5500, 300)
    SetChrPos(0x102, -16000, 0, 4300, 300)
    SetChrPos(0x104, -14600, 0, 4500, 300)
    SetChrPos(0x103, -14600, 0, 3300, 300)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
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
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    BeginChrThread(0x102, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 55)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 58)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 56)
    OP_68(-26500, 2500, 16000, 10000)
    MoveCamera(30, 11, 0, 10000)
    SetCameraDistance(19000, 10000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)

    def lambda_D178():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D178)
    Sleep(50)

    def lambda_D195():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D195)
    Sleep(50)

    def lambda_D1B2():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D1B2)
    Sleep(50)

    def lambda_D1CF():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D1CF)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 0)
    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_54_CFF7 end

    def Function_55_D212(): pass

    label("Function_55_D212")


    def lambda_D217():
        OP_95(0xFE, -26000, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D217)
    WaitChrThread(0xFE, 1)

    def lambda_D235():
        OP_95(0xFE, -26000, 300, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D235)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_D212 end

    def Function_56_D24F(): pass

    label("Function_56_D24F")


    def lambda_D254():
        OP_95(0xFE, -26000, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D254)
    WaitChrThread(0xFE, 1)

    def lambda_D272():
        OP_95(0xFE, -26000, 300, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D272)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_D24F end

    def Function_57_D28C(): pass

    label("Function_57_D28C")


    def lambda_D291():
        OP_95(0xFE, -27200, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D291)
    WaitChrThread(0xFE, 1)

    def lambda_D2AF():
        OP_95(0xFE, -27200, 300, 16100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2AF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_D28C end

    def Function_58_D2C9(): pass

    label("Function_58_D2C9")


    def lambda_D2CE():
        OP_95(0xFE, -27200, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2CE)
    WaitChrThread(0xFE, 1)

    def lambda_D2EC():
        OP_95(0xFE, -27200, 300, 14600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2EC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_D2C9 end

    def Function_59_D306(): pass

    label("Function_59_D306")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-2000, 2760, 27500, 0)
    MoveCamera(55, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -2700, 1760, 26800, 45)
    SetChrPos(0x102, -1300, 1760, 26800, 315)
    SetChrPos(0x103, -2700, 1760, 28200, 135)
    SetChrPos(0x104, -1300, 1760, 28200, 225)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(45, 27, 0, 3000)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0614
    ChrTalk(
        0x102,
        (
            "#0106F……没想到所有的人\x01",
            "都失踪了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x104,
        (
            "#5P#0303F不祥的预感应验了呢…… \x02\x03",

            "#0301F是自发性的离开，\x01",
            "还是被人绑架了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x103,
        (
            "#0206F现阶段的情报实在太少了，\x01",
            "两种可能性都要考虑到。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_D54A")

    #C0617
    ChrTalk(
        0x101,
        (
            "#6P#0003F……这五名失踪人员\x01",
            "说不定只是冰山一角。\x02\x03",

            "#0001F在克洛斯贝尔全市，\x01",
            "很可能已经有相当多的人\x01",
            "失踪了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5BE")

    label("loc_D54A")


    #C0618
    ChrTalk(
        0x101,
        (
            "#6P#0003F……这四名失踪人员\x01",
            "说不定只是冰山一角。\x02\x03",

            "#0001F在克洛斯贝尔全市，\x01",
            "很可能已经有相当多的人\x01",
            "失踪了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5BE")


    #C0619
    ChrTalk(
        0x102,
        (
            "#0108F嗯……\x01",
            "到底有多少人\x01",
            "下落不明了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x104,
        (
            "#5P#0301F怎么办，罗伊德？\x02\x03",

            "要一个一个找的话，\x01",
            "实在是太勉强了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……凭我们的人手，\x01",
            "确实是严重不足。\x02\x03",

            "#0008F在这种时候，一科却迫于上层的压力\x01",
            "而无法行动，真是让人头疼啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x103,
        (
            "#0202F不然去找二科的多诺邦警督，\x01",
            "问问他能不能帮忙吧？\x02\x03",

            "毕竟我们以前也帮过他的忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#6P#0003F不行……这应该也很难。\x02\x03",

            "#0001F既然连达德利搜查官都无计可施，\x01",
            "只能前来请求支援科帮忙，\x01",
            "二科想必也承受着相当的压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x103,
        "#0206F原来如此……的确呢。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x102,
        (
            "#0108F如此说来，公共安全科\x01",
            "的情况应该也是一样吧……\x02\x03",

            "#0106F如果能借助警队的人力，\x01",
            "情况就会大有改善了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D86E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D86E)
    Sleep(50)

    def lambda_D87E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D87E)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0626
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0627
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂，新人们……！\x02\x03",

            "你们没干什么\x01",
            "多余的事吧……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0628
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F哎……\x02\x03",

            "#0001F这声音……莫非是\x01",
            "达德利搜查官吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "什么莫非不莫非的！\x02\x03",

            "你们几个难道又擅自行动，\x01",
            "到鲁巴彻那边捣乱了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0630
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F没、没有……\x02\x03",

            "#0003F我们现在正在专心\x01",
            "调查药物方面的事情呢。\x02\x03",

            "#0001F……请问发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0631
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那还用问吗！\x01",
            "他们的事务所……\x02\x03",

            "……咳咳，没什么。\x02\x03",

            "既然不是你们干的，那就没事了。\x01",
            "继续调查你们的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0632
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0633
    ChrTalk(
        0x101,
        "#6P#0013F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0634
    ChrTalk(
        0x102,
        (
            "#0101F是达德利搜查官吗？\x01",
            "发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        "#6P#0006F这个……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0636
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将与达德利的谈话内容\x01",
            "转告给了艾莉等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0637
    ChrTalk(
        0x104,
        "#5P#0301F那是什么意思啊……\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x103,
        (
            "#0206F……明显很蹊跷呢。\x02\x03",

            "#0201F难道鲁巴彻商会那里\x01",
            "发生了什么情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x101,
        "#6P#0003F很有可能……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0640
    ChrTalk(
        0x104,
        (
            "#5P#0300F既然如此，我们也只能\x01",
            "过去看看情况了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        (
            "#0103F是啊……虽然已经被警告过，\x01",
            "让我们别再去管黑手党内斗的事情了……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x103,
        (
            "#0202F不过，如果失踪人员与黑手党有关，\x01",
            "我们应该就可以名正言顺地展开调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#6P#0001F嗯……\x01",
            "赶快前往鲁巴彻商会吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0x0, -2000, 1760, 26500, 180)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_59_D306 end

    def Function_60_DE70(): pass

    label("Function_60_DE70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DED2")
    EventBegin(0x1)

    #C0644
    ChrTalk(
        0x101,
        (
            "#0000F这里好像禁止\x01",
            "无关人员入内……\x01",
            "还是别进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_DED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF34")
    EventBegin(0x1)

    #C0645
    ChrTalk(
        0x101,
        (
            "#0000F这里好像禁止\x01",
            "无关人员入内……\x01",
            "还是别进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_DF34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF90")
    EventBegin(0x1)
    SetChrName("")

    #A0646
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彩虹剧团好像正在公演。\x01",
            "还是别进去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_DF90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E0D3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07C")

    #C0647
    ChrTalk(
        0x13D,
        (
            "#2105F咦，要进\x01",
            "彩虹剧团吗？\x02\x03",

            "#2109F……太好了！！\x01",
            "你们认识伊莉娅·普拉提耶，\x01",
            "所以一定可以进去！\x02\x03",

            "来，冲吧～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x101,
        "#0006F您在起什么哄啊……\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        (
            "#0101F我很在意镇长的话，\x01",
            "我们赶紧去『巴鲁卡』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_E0BD")

    label("loc_E07C")


    #C0650
    ChrTalk(
        0x101,
        (
            "#0001F比克森镇长的话很令人在意……\x01",
            "我们快点去『巴鲁卡』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0BD")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_E0D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E133")
    EventBegin(0x1)
    SetChrName("")

    #A0651
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彩虹剧团现在好像正在公演。\x01",
            "还是别进去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_E133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E248")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F4")

    #C0652
    ChrTalk(
        0x101,
        (
            "#0005F啊……彩虹剧团现在\x01",
            "正在公演。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x104,
        (
            "#0304F舞台那边交给\x01",
            "专业人员就行了。\x02\x03",

            "#0300F我们去做\x01",
            "我们该做的事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x101,
        (
            "#0000F也对，现在快点去\x01",
            "乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_E232")

    label("loc_E1F4")

    SetChrName("")

    #A0655
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彩虹剧团好像正在公演。\x01",
            "现在快点去乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E232")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_E248")

    Return()

    # Function_60_DE70 end

    def Function_61_E249(): pass

    label("Function_61_E249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E42F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E372")

    #C0656
    ChrTalk(
        0x103,
        "#0200F这里……好像就是『巴鲁卡』啊。\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x104,
        (
            "#0300F『巴鲁卡』──\x01",
            "是我常去的店哦。\x02\x03",

            "#0309F好！为庆祝上任，\x01",
            "大家来决一胜负吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x102,
        (
            "#0111F那可不行吧，\x01",
            "你有没有常识啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x104,
        "#0306F喂喂，这叫什么话！？\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x101,
        (
            "#0003F……我说，今天\x01",
            "也算是在职学习，\x01",
            "你就先忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 5)
    Jump("loc_E419")

    label("loc_E372")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3E7")

    #C0661
    ChrTalk(
        0x104,
        "#0300F……今天要坐在……\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x101,
        "#0000F兰迪，那可不行哦？\x02",
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x104,
        "#0301F嘁，真是一群死板的家伙啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E419")

    label("loc_E3E7")

    SetChrName("")

    #A0664
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是『巴鲁卡』。\x01",
            "……今天就不进去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E419")

    Sleep(50)
    SetChrPos(0x0, -26500, 300, 15360, 175)
    EventEnd(0x4)

    label("loc_E42F")

    Return()

    # Function_61_E249 end

    def Function_62_E430(): pass

    label("Function_62_E430")

    EventBegin(0x1)
    Call(0, 64)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_62_E430 end

    def Function_63_E44C(): pass

    label("Function_63_E44C")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 64)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_63_E44C end

    def Function_64_E468(): pass

    label("Function_64_E468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4E1")

    #C0665
    ChrTalk(
        0x101,
        (
            "#0006F今天太累了……直接回\x01",
            "支援科去吧，还是不要绕路了。\x02\x03",

            "#0000F从这里回去的话，走后巷\x01",
            "是最快的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E530")

    label("loc_E4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E530")

    #C0666
    ChrTalk(
        0x101,
        (
            "#0001F比克森镇长的话很令人在意……\x01",
            "我们快点去『巴鲁卡』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E530")

    Return()

    # Function_64_E468 end

    SaveToFile()

Try(main)
