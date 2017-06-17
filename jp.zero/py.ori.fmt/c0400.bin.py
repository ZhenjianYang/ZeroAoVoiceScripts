from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ソフィーユ",             # 1
        "客引きピム",             # 2
        "ポリセ",                 # 3
        "タップ",                 # 4
        "ラマンダ",               # 5
        "テージョ",               # 6
        "バニーガール",           # 7
        "ケイト巡査",             # 8
        "ロバーツ主任",           # 9
        "エステル",               # 10
        "ヨシュア",               # 11
        "シズク",                 # 12
        "エリィ",                 # 13
        "マクダエル市長",         # 14
        "秘書アーネスト",         # 15
        "市長車",                 # 16
        "リーシャ",               # 17
        "イリア",                 # 18
        "銀",                     # 19
        "ガイド",                 # 20
        "観光客",                 # 21
        "観光客",                 # 22
        "観光客",                 # 23
        "中央広場",               # 24
        "西通り",                 # 25
        "行政区",                 # 26
        "住宅街",                 # 27
        "歓楽街",                 # 28
        "東通り",                 # 29
        "旧市街",                 # 30
        "港湾区",                 # 31
        "ＩＢＣ",                 # 32
        "駅前通り",               # 33
        "裏通り",                 # 34
        "ウルスラ間道",           # 35
        "東クロスベル街道",       # 36
        "西クロスベル街道",       # 37
        "マインツ山道",           # 38
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

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "中央広場")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "西通り")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "行政区")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "住宅街")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "歓楽街")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "東通り")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "旧市街")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "駅前通り")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "裏通り")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "マインツ山道")
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
        "Function_9_2787",         # 09, 9
        "Function_10_27FB",        # 0A, 10
        "Function_11_288D",        # 0B, 11
        "Function_12_29CE",        # 0C, 12
        "Function_13_3C20",        # 0D, 13
        "Function_14_49CF",        # 0E, 14
        "Function_15_4B1C",        # 0F, 15
        "Function_16_581D",        # 10, 16
        "Function_17_6495",        # 11, 17
        "Function_18_725F",        # 12, 18
        "Function_19_7472",        # 13, 19
        "Function_20_7642",        # 14, 20
        "Function_21_7966",        # 15, 21
        "Function_22_7AA5",        # 16, 22
        "Function_23_7F51",        # 17, 23
        "Function_24_874A",        # 18, 24
        "Function_25_87CB",        # 19, 25
        "Function_26_8C0C",        # 1A, 26
        "Function_27_9628",        # 1B, 27
        "Function_28_9698",        # 1C, 28
        "Function_29_96B3",        # 1D, 29
        "Function_30_9760",        # 1E, 30
        "Function_31_97F7",        # 1F, 31
        "Function_32_9881",        # 20, 32
        "Function_33_990B",        # 21, 33
        "Function_34_9995",        # 22, 34
        "Function_35_9A90",        # 23, 35
        "Function_36_9AAC",        # 24, 36
        "Function_37_9AC8",        # 25, 37
        "Function_38_9AE4",        # 26, 38
        "Function_39_9B00",        # 27, 39
        "Function_40_9B1C",        # 28, 40
        "Function_41_9B38",        # 29, 41
        "Function_42_9B96",        # 2A, 42
        "Function_43_9E1F",        # 2B, 43
        "Function_44_A758",        # 2C, 44
        "Function_45_AACF",        # 2D, 45
        "Function_46_B525",        # 2E, 46
        "Function_47_CBA8",        # 2F, 47
        "Function_48_CBEE",        # 30, 48
        "Function_49_D64D",        # 31, 49
        "Function_50_E4A3",        # 32, 50
        "Function_51_E535",        # 33, 51
        "Function_52_E572",        # 34, 52
        "Function_53_E5CF",        # 35, 53
        "Function_54_E5E5",        # 36, 54
        "Function_55_E800",        # 37, 55
        "Function_56_E83D",        # 38, 56
        "Function_57_E87A",        # 39, 57
        "Function_58_E8B7",        # 3A, 58
        "Function_59_E8F4",        # 3B, 59
        "Function_60_F541",        # 3C, 60
        "Function_61_F9D4",        # 3D, 61
        "Function_62_FC07",        # 3E, 62
        "Function_63_FC23",        # 3F, 63
        "Function_64_FC3F",        # 40, 64
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2783")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_17FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181A")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_277E")

    label("loc_181A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_182E")
    Jump("loc_277E")

    label("loc_182E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_277E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18A9")

    #C0001
    ChrTalk(
        0x8,
        "ウチのアイスは手作りですよ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "買って食べて、\x01",
            "損はないはずです～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193F")

    label("loc_18A9")


    #C0003
    ChrTalk(
        0x8,
        (
            "ウチのアイスは\x01",
            "手作りなんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……あ、今おいしそうって\x01",
            "思いましたかぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "ほしいときが買い時です。\x01",
            "はい、買っていってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_193F")

    Jump("loc_277E")

    label("loc_1944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A86")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_199A")

    #C0006
    ChrTalk(
        0x8,
        (
            "最近はキレやすい人が\x01",
            "多くていけませんねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F4")

    label("loc_199A")


    #C0007
    ChrTalk(
        0x8,
        (
            "そこのお兄……オジサン。\x01",
            "アイスはいかがですかぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x10A,
        "#0603F私はまだ２７だ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19F4")

    Jump("loc_1A81")

    label("loc_19F9")


    #C0009
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "そこのお兄さんも\x01",
            "１つ買っていってください！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "オトナ向けのブランデー味も\x01",
            "ご用意しましたよぉ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A81")

    Jump("loc_277E")

    label("loc_1A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1ACE")

    #C0012
    ChrTalk(
        0x8,
        (
            "お腹壊してるときに\x01",
            "アイスはいけませんよ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B5E")

    label("loc_1ACE")


    #C0013
    ChrTalk(
        0x8,
        (
            "アルカンシェルの人に\x01",
            "聞いたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "最近様子のおかしい人が\x01",
            "いるそうですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "どうしたんですかねー。\x01",
            "お腹壊しましたかー？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B5E")

    Jump("loc_277E")

    label("loc_1B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BA3")

    #C0016
    ChrTalk(
        0x8,
        (
            "アイス～、アイスは\x01",
            "いかがですかぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C3E")

    label("loc_1BA3")


    #C0017
    ChrTalk(
        0x8,
        (
            "記念祭が終わっても\x01",
            "観光客の人が減りませんね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "いやー、ありがたいことです。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "皆さん、ちゃあんとミラを\x01",
            "落としていっちゃってくださいねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C3E")

    Jump("loc_277E")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1DDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D14")

    #C0020
    ChrTalk(
        0x8,
        (
            "記念祭中は港湾区に\x01",
            "美味しいアイス屋が出ていたそうで\x01",
            "一瞬ヒヤッとしましたがー……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "今月も屋台のＭＶＰは\x01",
            "わたくしがめでたく頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "むふふ、これも\x01",
            "皆さんのお陰ですね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD5")

    label("loc_1D14")


    #C0023
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "……記念祭の売り上げは\x01",
            "まずまずでしたね～。\x01",
            "普段の２０倍って所かなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "この調子で屋台の売り上げ\x01",
            "ブッチギリ一番を\x01",
            "死守しなくちゃあいけませんね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1DD5")

    Jump("loc_277E")

    label("loc_1DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_205A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E7C")

    #C0026
    ChrTalk(
        0x8,
        "アイス～、アイスはいかがですかぁ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x11C, 500)

    #C0027
    ChrTalk(
        0x8,
        (
            "……ワンちゃんもアイス、\x01",
            "食べませんか～？\x01",
            "おいしいですよ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F3D")

    label("loc_1E7C")


    #C0028
    ChrTalk(
        0x8,
        "アイス～、アイスはいかがですかぁ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11C, 500)

    #C0029
    ChrTalk(
        0x8,
        (
            "……ワンちゃんもアイス、\x01",
            "食べませんか～？\x01",
            "おいしいですよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x11C,
        "#1200Fグルルル……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#0200F（『甘い物は好かん』\x01",
            "  と言っています。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F3D")

    TalkEnd(0x8)
    Return()

    label("loc_1F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FB5")

    #C0032
    ChrTalk(
        0x8,
        (
            "ウチのアイス、\x01",
            "劇団の人にも人気なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "御用達を名乗っちゃって\x01",
            "モリモリ売り込もうかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2055")

    label("loc_1FB5")


    #C0034
    ChrTalk(
        0x8,
        (
            "実はウチのアイス、\x01",
            "劇団の人も買っていくんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "イリアさんやプリエさんは\x01",
            "ウチの常連ですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "いっそのこと\x01",
            "御用達を名乗っちゃいますかねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2055")

    Jump("loc_277E")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_210B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20B4")

    #C0037
    ChrTalk(
        0x8,
        (
            "どうぞ～、お客様は神様です。\x01",
            "ご注文しちゃって構いませんよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_20B4")


    #C0038
    ChrTalk(
        0x8,
        "あれ、おはようございますー。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "まだ準備中ですけど\x01",
            "アイス食べますか～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2106")

    Jump("loc_277E")

    label("loc_210B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2190")

    #C0040
    ChrTalk(
        0x8,
        (
            "団員お気に入りのフレーバー、\x01",
            "そろそろ売り切れ寸前で～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "後悔しないように\x01",
            "買っちゃってください～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2230")

    label("loc_2190")


    #C0042
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "アルカンシェル団員にも\x01",
            "大人気のフレーバー、\x01",
            "そろそろ売り切れですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "後悔しないように\x01",
            "買っちゃってください～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2230")

    Jump("loc_277E")

    label("loc_2235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22AE")

    #C0045
    ChrTalk(
        0x8,
        (
            "ファンの人は\x01",
            "みんな買って行くんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "流行に乗り遅れないように、\x01",
            "お一つどうですかぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233B")

    label("loc_22AE")


    #C0047
    ChrTalk(
        0x8,
        (
            "お兄さんたちも\x01",
            "アルカンシェルのファンですかぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "ならウチのアイスを\x01",
            "買わないといけませんねぇ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "さあさあ、お一つどうぞー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_233B")

    Jump("loc_277E")

    label("loc_2340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23AA")

    #C0050
    ChrTalk(
        0x8,
        (
            "今月の屋台のＭＶＰは\x01",
            "わたくしが頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        "これも皆さんのお陰ですね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2450")

    label("loc_23AA")


    #C0052
    ChrTalk(
        0x8,
        "イエ～イ、売り上げナンバーワン！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "お陰サマで、ウチの屋台は\x01",
            "今月売り上げ\x01",
            "ナンバーワンだったんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "これも皆さんのお陰ですね。\x01",
            "感謝してますよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2450")

    Jump("loc_277E")

    label("loc_2455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_253A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2495")

    #C0055
    ChrTalk(
        0x8,
        (
            "劇団のファンの方は\x01",
            "大好きですよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2535")

    label("loc_2495")


    #C0056
    ChrTalk(
        0x8,
        (
            "劇団のファンの方は\x01",
            "いつもああやって\x01",
            "朝早くからやってきて……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "おやつにうちのアイスを\x01",
            "買ってくれるんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "いや～、ありがたいことですねー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2535")

    Jump("loc_277E")

    label("loc_253A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2590")

    #C0059
    ChrTalk(
        0x8,
        (
            "ジュース屋さんがあったら\x01",
            "アイスと物々交換するんですがー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2604")

    label("loc_2590")


    #C0060
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "あー、のどが渇いたなぁ。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "どこかにジュース屋さんは\x01",
            "ないでしょうか～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2604")

    Jump("loc_277E")

    label("loc_2609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2688")

    #C0063
    ChrTalk(
        0x8,
        (
            "今、うちのアイスを\x01",
            "買っとくのがオススメです。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "午後からじゃ売り切れちゃうかも\x01",
            "しれませんので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_271D")

    label("loc_2688")


    #C0065
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "……そこのお兄さん、\x01",
            "アイスはいかがですかぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "今日はあっつくなりますよ～！\x01",
            "後悔しても知りませんよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_271D")

    Jump("loc_277E")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_274F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2747")
    Call(0, 11)
    Jump("loc_274A")

    label("loc_2747")

    Call(0, 9)

    label("loc_274A")

    Jump("loc_2752")

    label("loc_274F")

    Call(0, 9)

    label("loc_2752")

    Jump("loc_277E")

    label("loc_2757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_277B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2773")
    Call(0, 11)
    Jump("loc_2776")

    label("loc_2773")

    Call(0, 10)

    label("loc_2776")

    Jump("loc_277E")

    label("loc_277B")

    Call(0, 10)

    label("loc_277E")

    Jump("loc_179C")

    label("loc_2783")

    TalkEnd(0xFE)
    Return()

    # Function_8_178F end

    def Function_9_2787(): pass

    label("Function_9_2787")


    #C0068
    ChrTalk(
        0x8,
        (
            "今日は夕方から\x01",
            "劇団アルカンシェルの\x01",
            "公演がありますね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "売り上げもぐんと伸びる。\x01",
            "そうに違いないです～。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_9_2787 end

    def Function_10_27FB(): pass

    label("Function_10_27FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2834")

    #C0070
    ChrTalk(
        0x8,
        (
            "うちのアイスは\x01",
            "ちょー美味しいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288C")

    label("loc_2834")


    #C0071
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "……そこのお兄さん、\x01",
            "アイスはいかがですかぁ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_288C")

    Return()

    # Function_10_27FB end

    def Function_11_288D(): pass

    label("Function_11_288D")


    #C0073
    ChrTalk(
        0xFE,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "そうだそこのお兄さん、\x01",
            "今日は特別サービスですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "アイス用の材料で作った\x01",
            "クリームラテの作り方を教えちゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "おいしいので\x01",
            "一度試してみてください～。\x02",
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
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x15)
    Return()

    # Function_11_288D end

    def Function_12_29CE(): pass

    label("Function_12_29CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA6")

    #C0079
    ChrTalk(
        0xFE,
        (
            "やあ……いらっしゃい。\x01",
            "お兄さんたちヒマかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "どう、お酒飲まない？\x01",
            "ウチはいい子もそろってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "へっへっ、うちの店は\x01",
            "警備隊司令もご利用の優良店だ。\x01",
            "絶対損はさせないから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B14")

    label("loc_2AA6")


    #C0082
    ChrTalk(
        0xFE,
        (
            "へっへっ、うちの店は\x01",
            "警備隊司令もご利用の優良店だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "どう、楽しんできてよ。\x01",
            "絶対損はさせないから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B14")

    Jump("loc_3C1C")

    label("loc_2B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B8D")

    #C0084
    ChrTalk(
        0x9,
        (
            "昨日からそこのホテルに\x01",
            "警察が出入りしてるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        "やれやれ、まるで営業妨害だよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C17")

    label("loc_2B8D")


    #C0086
    ChrTalk(
        0x9,
        (
            "昨日からそこのホテルに\x01",
            "警察が出入りしてるって聞いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        "やれやれ、何の用だろうねえ。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "客がビビるからやめて欲しいんだが。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C17")

    Jump("loc_3C1C")

    label("loc_2C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C75")

    #C0089
    ChrTalk(
        0x9,
        "今日は様子が変だねえ。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        "客を引っ掛ける気にもならないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D0B")

    label("loc_2C75")


    #C0091
    ChrTalk(
        0x9,
        (
            "何だか今日は\x01",
            "歓楽街の様子が変だねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "サツのガサ入れでも\x01",
            "ありそうな雰囲気だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "今日は早めに引き上げた方が\x01",
            "いいかもしれないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D0B")

    Jump("loc_3C1C")

    label("loc_2D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DA6")

    #C0094
    ChrTalk(
        0x9,
        (
            "記念祭からずっと\x01",
            "滞在してる人、多いらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "いやお兄さん嬉しいなぁ、\x01",
            "みんな纏めてスペシャルコースに\x01",
            "誘ってあげよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2DA6")


    #C0096
    ChrTalk(
        0x9,
        (
            "記念祭から一月も経つのに\x01",
            "お家に帰らないで\x01",
            "フラフラしてる人がいるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "いやお兄さん嬉しいわ、\x01",
            "ホント感動したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "わざわざ引っ掛けて\x01",
            "下さいって言わんばかりだよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E5D")

    Jump("loc_3C1C")

    label("loc_2E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2EED")

    #C0099
    ChrTalk(
        0x9,
        (
            "議会の間の接待は\x01",
            "毎年取り合いになるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "へっへ……さあお商売お商売。\x01",
            "今年も沢山ご予約取らないとねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F72")

    label("loc_2EED")


    #C0101
    ChrTalk(
        0x9,
        "いよいよ予算議会が始まるな。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "へっへ……\x01",
            "ウチの店は接待に強いからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "他のちゃらちゃらした\x01",
            "店なんかに負けないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F72")

    Jump("loc_3C1C")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3215")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3002")
    TurnDirection(0x9, 0x11C, 0)

    #C0104
    ChrTalk(
        0x9,
        "へえ、立派な犬だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "それ君たちが飼ってるのか？\x01",
            "いいねぇ、羨ましいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B2")

    label("loc_3002")

    TurnDirection(0x9, 0x11C, 0)

    #C0106
    ChrTalk(
        0x9,
        "へえ、立派な犬だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "それ君たちが飼ってるのか？\x01",
            "いいねぇ、羨ましいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11C,
        "#1203Fグルルル……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0203F（『貴様などに興味はない』\x01",
            "  と言っています。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30B2")

    TalkEnd(0x9)
    Return()

    label("loc_30B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3153")

    #C0110
    ChrTalk(
        0x9,
        (
            "あんまりマズい商売してると\x01",
            "遊撃士の人が乗り込んで来るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "やれやれ、おっかないねぇ。\x01",
            "僕はそんなに\x01",
            "悪い人じゃありませんよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3210")

    label("loc_3153")


    #C0112
    ChrTalk(
        0x9,
        (
            "さっき遊撃士の人が店に来てね、\x01",
            "一瞬ヒヤッとしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "まあ、何かの仕事の\x01",
            "聞き込みだったみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "まったくおっかないねえ。\x01",
            "ウチもそんなにマズい事は\x01",
            "してないはずだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3210")

    Jump("loc_3C1C")

    label("loc_3215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3283")

    #C0115
    ChrTalk(
        0x9,
        "ふぅ、今朝は寝覚めがいいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "鼻を明かしてやると\x01",
            "気持ちがいいですよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3323")

    label("loc_3283")


    #C0117
    ChrTalk(
        0x9,
        (
            "ビッシュの店から一人\x01",
            "女の子を引き抜いてやったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "へっへ、まあこんなのは\x01",
            "小競り合いだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "鼻を明かしてやると\x01",
            "気持ちがいいですよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3323")

    Jump("loc_3C1C")

    label("loc_3328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_341D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3392")

    #C0120
    ChrTalk(
        0x9,
        (
            "へっへ、そろそろ\x01",
            "お客さんが集まってくる時間だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        "気合入れていかないとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3418")

    label("loc_3392")


    #C0122
    ChrTalk(
        0x9,
        (
            "兄ちゃん兄ちゃん、\x01",
            "いいトコに来たねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "これからどう。\x01",
            "少し遊んでいかんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "きっと楽しいよ～、\x01",
            "疲れも吹っ飛ぶよ～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3418")

    Jump("loc_3C1C")

    label("loc_341D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3474")

    #C0125
    ChrTalk(
        0x9,
        (
            "ルバーチェ商会なんて\x01",
            "まともに関わっちゃ\x01",
            "ダメですよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3521")

    label("loc_3474")


    #C0126
    ChrTalk(
        0x9,
        (
            "近頃黒月とかいう連中が\x01",
            "手を広げてるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "でもまだまだ、\x01",
            "クロスベル裏社会のドンは\x01",
            "ルバーチェ商会だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "この街で連中に逆らっちゃ\x01",
            "やっていけないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3521")

    Jump("loc_3C1C")

    label("loc_3526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_365E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35B1")

    #C0129
    ChrTalk(
        0x9,
        (
            "議会が近づくと\x01",
            "接待のお客さんが増えるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "羽振りのいい議員の皆さん、\x01",
            "ウチならサービスしますよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3659")

    label("loc_35B1")


    #C0131
    ChrTalk(
        0x9,
        (
            "お兄さん、お兄さん。\x01",
            "遊んでいきませんか～っと。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "……最近ね、接待でくる\x01",
            "大口のお客さんが増えてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "ああ、嬉しいねえ。\x01",
            "きっと議会が近いせいだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3659")

    Jump("loc_3C1C")

    label("loc_365E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_378B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3724")

    #C0134
    ChrTalk(
        0xFE,
        (
            "昨日から警察の人が\x01",
            "聞き込みしてるらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "２人組みの刑事に\x01",
            "あれやこれやと尋ねられたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "やれやれ、僕は何も知らないよ。\x01",
            "ただの善良な客引きですよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3786")

    label("loc_3724")


    #C0137
    ChrTalk(
        0xFE,
        (
            "歓楽街は事件多いからね。\x01",
            "時々警察の人が来るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "やれやれ、僕は\x01",
            "何も知りませんよ～っと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3786")

    Jump("loc_3C1C")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37E9")

    #C0139
    ChrTalk(
        0x9,
        (
            "アイス屋のねーちゃん、可愛いねえ。\x01",
            "失業したらウチで拾ってあげよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_387C")

    label("loc_37E9")


    #C0140
    ChrTalk(
        0x9,
        "ぺろぺろ……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        (
            "そこの先にある屋台で\x01",
            "アイスを調達して来たんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "アイス屋のねーちゃん、可愛いね～。\x01",
            "失業したらウチで拾ってあげよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_387C")

    Jump("loc_3C1C")

    label("loc_3881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_396E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38E8")

    #C0143
    ChrTalk(
        0x9,
        (
            "ビッシュの言う事なんて\x01",
            "耳かしちゃダメダメ。\x01",
            "遊ぶならウチの店にしといてよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3969")

    label("loc_38E8")


    #C0144
    ChrTalk(
        0x9,
        (
            "そこの裏通りに\x01",
            "ビッシュって男がいるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "あれ、商売敵なんだよ。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "あの男の言う事に\x01",
            "耳かしちゃダメですよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3969")

    Jump("loc_3C1C")

    label("loc_396E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_39B4")

    #C0147
    ChrTalk(
        0x9,
        (
            "どこかにいいお客さんは\x01",
            "いませんか～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_39B4")


    #C0148
    ChrTalk(
        0x9,
        (
            "ああ、お昼どきだ。\x01",
            "そろそろお客さんがくるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "ここを通りかかるお客さん、\x01",
            "結構多いんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "へっへっ、楽しみだな。\x01",
            "今日はどの人を誘おうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3A52")

    Jump("loc_3C1C")

    label("loc_3A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3AC0")

    #C0151
    ChrTalk(
        0x9,
        "ウチの店はこの近くなんだよ。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "へっへっ、どうよ兄ちゃん。\x01",
            "今日はサービスしとくよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_3AC0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B4A")

    #C0153
    ChrTalk(
        0xFE,
        (
            "へっへっへっ、\x01",
            "兄ちゃんいいトコに来たねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "どう、ウチはうまい酒が飲めるし\x01",
            "いい子もそろってるよん？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BCE")

    label("loc_3B4A")


    #C0155
    ChrTalk(
        0x9,
        (
            "ああ……お子様は\x01",
            "お呼びじゃねえんだよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 750)

    #C0156
    ChrTalk(
        0xFE,
        (
            "どう、そっちの兄ちゃん。\x01",
            "ウチはうまい酒が飲めるし\x01",
            "いい子もそろってるよん？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BCE")


    #C0157
    ChrTalk(
        0x9,
        (
            "お値打ち価格、１時間１０００ミラだよ。\x01",
            "へっへっ、まあ楽しんできてや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3C1C")

    TalkEnd(0xFE)
    Return()

    # Function_12_29CE end

    def Function_13_3C20(): pass

    label("Function_13_3C20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3D50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3CAC")

    #C0158
    ChrTalk(
        0xA,
        (
            "ファンの目はごまかせないわよっ！\x01",
            "きっと何かあったんだわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "でも受付の人に聞いても\x01",
            "分かんないのよねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D4B")

    label("loc_3CAC")


    #C0160
    ChrTalk(
        0xA,
        "朝から劇団の様子が変なのよぅ。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "受付の人に聞いても\x01",
            "詳しい事は教えてくれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "今日の昼公演は大幅に遅れたそうよ。\x01",
            "どういうことかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3D4B")

    Jump("loc_49CB")

    label("loc_3D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3DC8")

    #C0163
    ChrTalk(
        0xA,
        (
            "イリア様の心の声が聞こえないわ。\x01",
            "いつも私にだけ聞こえるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        "何かあったのかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E26")

    label("loc_3DC8")


    #C0165
    ChrTalk(
        0xA,
        "#4Sイリア様、イリア様～っ！\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "……おかしいわねぇ……\x01",
            "今日は何だか静かだわ～。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3E26")

    Jump("loc_49CB")

    label("loc_3E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3E71")

    #C0167
    ChrTalk(
        0xA,
        (
            "イリア様～、公演\x01",
            "頑張ってくださいませ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE9")

    label("loc_3E71")


    #C0168
    ChrTalk(
        0xA,
        "今日の公演が始まったわね……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "チケットは無いけど、構わないわ。\x01",
            "遠くからイリア様を応援するから！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x13B, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3EE9")

    Jump("loc_49CB")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F31")

    #C0170
    ChrTalk(
        0xA,
        (
            "イリア様～、出てきて\x01",
            "手を振ってくださいませ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CB")

    label("loc_3F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F9C")

    #C0171
    ChrTalk(
        0xA,
        (
            "今日『金の太陽、銀の月』の\x01",
            "写真集が発売なんですって！\x01",
            "これは見逃せないわ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405C")

    label("loc_3F9C")


    #C0172
    ChrTalk(
        0xA,
        (
            "ねえ聞いた？\x01",
            "今日『金の太陽、銀の月』の\x01",
            "写真集が発売なんですって！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "公演の見所や\x01",
            "あらゆるシーンの写真が\x01",
            "網羅されてるって話よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "み、見逃せないわ……\x01",
            "百貨店に走らなくっちゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_405C")

    Jump("loc_49CB")

    label("loc_4061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_40B5")

    #C0175
    ChrTalk(
        0xA,
        (
            "はあ、イリア様……今ごろ\x01",
            "何をしてらっしゃるのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4134")

    label("loc_40B5")


    #C0176
    ChrTalk(
        0xA,
        (
            "劇団アルカンシェルは\x01",
            "今日はお休みなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "何人かは自主練に来てらっしゃるけど……\x01",
            "イリア様は現れないみたいねぇ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4134")

    Jump("loc_49CB")

    label("loc_4139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_418E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4186")

    #C0178
    ChrTalk(
        0xA,
        (
            "#4Sイリア様～、お稽古\x01",
            "頑張ってくださいませ～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4189")

    label("loc_4186")

    Call(0, 14)

    label("loc_4189")

    Jump("loc_49CB")

    label("loc_418E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4203")

    #C0179
    ChrTalk(
        0xA,
        "イリア様、今日は寝坊したみたいね。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "珍しい事もあるものだわ。\x01",
            "今日の日記に記録しておきましょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CB")

    label("loc_4203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4246")

    #C0181
    ChrTalk(
        0xA,
        (
            "イリア様～、お稽古\x01",
            "頑張ってくださいませ～っ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CB")

    label("loc_4246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_42AE")

    #C0182
    ChrTalk(
        0xA,
        "じ～……本当かしら。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "もしズルして潜り込んだのなら、\x01",
            "私が許さないわよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_438C")

    label("loc_42AE")


    #C0184
    ChrTalk(
        0xA,
        (
            "あなたたち……\x01",
            "アルカンシェルで何してたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "なんだか気になるわね。\x01",
            "劇団関係の人じゃないわよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#0100Fあの、気にしないで下さい。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#0012Fその、知り合いが勤めているもので。\x01",
            "（一応嘘じゃないよな……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_438C")

    Jump("loc_49CB")

    label("loc_4391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_44EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_441C")

    #C0188
    ChrTalk(
        0xA,
        (
            "ううっっ、もう一度イリア様に\x01",
            "お会いできると思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "この日のために、\x01",
            "ずっとガマンしてたのに……ッ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E9")

    label("loc_441C")


    #C0190
    ChrTalk(
        0xA,
        "#4Sうぎゃ～……っ！！\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        (
            "新作のチケット発売の日、\x01",
            "寝坊しちゃったのよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "あわてて買いに走ったけど\x01",
            "私の１つ前の人で売り切れ……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "うううっ……私のバカ～……\x01",
            "イリア様に会えないじゃない……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_44E9")

    Jump("loc_49CB")

    label("loc_44EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4568")

    #C0194
    ChrTalk(
        0xA,
        (
            "新作公演のチケット\x01",
            "発売は来週からだそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "じゅるり……うふふ……\x01",
            "絶対手に入れてやるんだから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CB")

    label("loc_4568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_46B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_45FC")

    #C0196
    ChrTalk(
        0xA,
        (
            "イリア様の練習着姿……\x01",
            "……あ、あと新作衣装の\x01",
            "別アングルも欲しいわね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xA,
        (
            "うふふ、どこかに\x01",
            "撮影の機会は無いかしら～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46AC")

    label("loc_45FC")


    #C0198
    ChrTalk(
        0xA,
        "イリア様、イリア様……！\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        (
            "私服姿に舞台衣装、\x01",
            "控え室用のガウン姿は写真に収めたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "あとは今使われている練習着姿……\x01",
            "うふふ、どこかに\x01",
            "撮影の機会は無いかしら～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_46AC")

    Jump("loc_49CB")

    label("loc_46B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_47ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_472E")

    #C0201
    ChrTalk(
        0xA,
        (
            "今回の新作は\x01",
            "イリア様が出演なさるの！\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xA,
        (
            "ああ、イリア様の勇姿……\x01",
            "ついにナマで拝めるのね……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47E8")

    label("loc_472E")

    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0203
    ChrTalk(
        0xA,
        (
            "ねえ聞いた！？\x01",
            "ビッグニュースよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "もうすぐアルカンシェルの\x01",
            "新作公演が発表されるの！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "合わせてチケット発売も\x01",
            "始まるって噂よ。\x01",
            "これは見逃せないわ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_47E8")

    Jump("loc_49CB")

    label("loc_47ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4878")
    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0206
    ChrTalk(
        0xA,
        "イリア様、早く出てこないかしら！\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "それとももう\x01",
            "裏口から帰っちゃったのかしら～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_4878")


    #C0208
    ChrTalk(
        0xA,
        (
            "イリア様は\x01",
            "まだ出てこないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xA,
        (
            "稽古上がりのイリア様を\x01",
            "カメラに収めるのが私の夢なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xA,
        (
            "そのために２万ミラもする\x01",
            "導力カメラを買ったんだから～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_491C")

    Jump("loc_49CB")

    label("loc_4921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_498D")

    #C0211
    ChrTalk(
        0xA,
        (
            "あっ、あなた達っ！\x01",
            "中でイリア様を見なかった！？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "ずる～い！\x01",
            "私も見たかったのに～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CB")

    label("loc_498D")

    OP_93(0xFE, 0x13B, 0x0)

    #C0213
    ChrTalk(
        0xA,
        (
            "イリア様の練習着姿……\x01",
            "何とか拝めないかしら～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CB")

    TalkEnd(0xFE)
    Return()

    # Function_13_3C20 end

    def Function_14_49CF(): pass

    label("Function_14_49CF")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0214
    ChrTalk(
        0xA,
        (
            "タップ、あんたは\x01",
            "チケット手に入ったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "いや、無理だった……\x01",
            "知り合いを当たってみたんだが\x01",
            "誰も譲ってくれなくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        "じゃ、記念祭でやる事は一つね。\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        "ああ、一つしかねえ。\x02",
    )

    CloseMessageWindow()

    def lambda_4A97():
        OP_93(0xA, 0x13B, 0x2EE)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4A97)

    def lambda_4AA4():
        OP_93(0xB, 0x13B, 0x2EE)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4AA4)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0218
    ChrTalk(
        0xA,
        (
            "#4Sイリア様～、ずっと\x01",
            "見守ってますわ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "#4S心の目で見守ってるぜ、\x01",
            "イリア様～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_49CF end

    def Function_15_4B1C(): pass

    label("Function_15_4B1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4BBE")

    #C0220
    ChrTalk(
        0xB,
        (
            "今日の昼公演、遅れててさ。\x01",
            "４時くらいにやっと始まったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xB,
        (
            "劇団長や支配人が\x01",
            "慌しく出入りしてたみたいだし……\x01",
            "マジで何かあったのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5819")

    label("loc_4BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4C19")

    #C0222
    ChrTalk(
        0xB,
        (
            "今日の昼公演、\x01",
            "なんだか遅れてるみたいだな……\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C69")

    label("loc_4C19")


    #C0223
    ChrTalk(
        0xB,
        "劇団が妙に静かなんだ……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xB,
        (
            "そろそろ公演の時間だろ？\x01",
            "何やってんだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4C69")

    Jump("loc_5819")

    label("loc_4C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4D07")

    #C0225
    ChrTalk(
        0xB,
        (
            "朝のイリア様ウォッチしてると\x01",
            "あの子にジロッと睨まれるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "……劇団も何でまた\x01",
            "あんな愛想の無い奴を雇ったんだろな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D86")

    label("loc_4D07")


    #C0227
    ChrTalk(
        0xB,
        (
            "最近アルカンシェルに\x01",
            "下働きの子が入ったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        (
            "ときどきジロッと睨まれるんだが……\x01",
            "なんか、愛想の無い奴だよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4D86")

    Jump("loc_5819")

    label("loc_4D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4DF6")

    #C0229
    ChrTalk(
        0xB,
        (
            "リーシャさんの写真集、\x01",
            "早く発売されねえかな……\x01",
            "今から待ち遠しくて仕方ねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EA2")

    label("loc_4DF6")


    #C0230
    ChrTalk(
        0xB,
        (
            "イリア様は勿論のことだが、\x01",
            "新人のリーシャさんも凄いよなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "リーシャさんだったら\x01",
            "単独写真集を出しても\x01",
            "バカ売れ間違いなしだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xB,
        "発売、されねえかなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4EA2")

    Jump("loc_5819")

    label("loc_4EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F31")

    #C0233
    ChrTalk(
        0xFE,
        (
            "リーシャ・マオは\x01",
            "イリア様との共演も\x01",
            "立派にこなしてるらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "くぅぅ……俺もナマで\x01",
            "見てみたいもんだぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5012")

    label("loc_4F31")


    #C0235
    ChrTalk(
        0xFE,
        (
            "イリア様との共演でデビューした\x01",
            "リーシャ・マオって子がいるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        "評判によると凄い演技力らしいな。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "イリア様とは一味違う、\x01",
            "可憐にして凛とした舞を\x01",
            "見せてくれるらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "くぅぅ……\x01",
            "俺も見てみたいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5012")

    Jump("loc_5819")

    label("loc_5017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_506A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5062")

    #C0239
    ChrTalk(
        0xB,
        (
            "#4Sイリア様～、\x01",
            "俺たちファンが付いてるぜ～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5065")

    label("loc_5062")

    Call(0, 14)

    label("loc_5065")

    Jump("loc_5819")

    label("loc_506A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50C0")

    #C0240
    ChrTalk(
        0xB,
        (
            "ありゃあ何者なんだ……？\x01",
            "まさか、新手のイリア様ファンか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_513D")

    label("loc_50C0")


    #C0241
    ChrTalk(
        0xB,
        (
            "今朝、背広を着た人たちが\x01",
            "劇団に入っていったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        (
            "関係者の人たちみたいだけど\x01",
            "やたらと目つきが鋭そうだったぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_513D")

    Jump("loc_5819")

    label("loc_5142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_51D4")

    #C0243
    ChrTalk(
        0xB,
        (
            "ま、公演があったって\x01",
            "学生のオレには\x01",
            "手が届かないだろうがな……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "いいのさっ、夜の劇場を見るだけで\x01",
            "オレは満足だっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_525E")

    label("loc_51D4")


    #C0245
    ChrTalk(
        0xB,
        (
            "アルカンシェルは\x01",
            "新作公演の稽古期間だからな。\x01",
            "今晩も公演はナシだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xB,
        (
            "でも夜の劇場を見るだけで、\x01",
            "何だかワクワクしてこないか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_525E")

    Jump("loc_5819")

    label("loc_5263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_52D2")

    #C0247
    ChrTalk(
        0xB,
        (
            "今朝から新人のリーシャさんが\x01",
            "何度か出入りしているような……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        "家に忘れ物でもしたのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5819")

    label("loc_52D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_540D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A2")

    #C0249
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケットは\x01",
            "Ｂ席でもかなりの額がするんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "……残念ながら、俺は今回は\x01",
            "リタイアするしかなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "やっぱいち学生には\x01",
            "手の届かないシロモノだよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5408")

    label("loc_53A2")


    #C0252
    ChrTalk(
        0xFE,
        (
            "くそっ、親には\x01",
            "頼み込んでみたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "いち学生がそう何度も拝める\x01",
            "舞台じゃねえんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5408")

    Jump("loc_5819")

    label("loc_540D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_543D")

    #C0254
    ChrTalk(
        0xB,
        "おいポリセ、よだれよだれ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5819")

    label("loc_543D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_54A9")

    #C0255
    ChrTalk(
        0xB,
        (
            "くそっ、俺は\x01",
            "導力カメラを持ってないんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "あれも学生には\x01",
            "高価な代物だからなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5819")

    label("loc_54A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_557A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5525")

    #C0257
    ChrTalk(
        0xFE,
        "俺は毎朝欠かさずここに来るんだ。\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "もういっそこの広場にテント張って\x01",
            "住み着きたいくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5575")

    label("loc_5525")


    #C0259
    ChrTalk(
        0xB,
        (
            "なんだ、君たちも\x01",
            "朝のイリア様ウォッチかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xB,
        "追っかけも程ほどにな！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5575")

    Jump("loc_5819")

    label("loc_557A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_561A")

    #C0261
    ChrTalk(
        0xFE,
        (
            "ちなみにポリセの奴とは\x01",
            "アルカンシェル追っかけ仲間なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "フ……偶然にも\x01",
            "同じ日にイリア様の舞台を見て\x01",
            "虜になっちまったんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570B")

    label("loc_561A")


    #C0263
    ChrTalk(
        0xB,
        (
            "《劇団アルカンシェル》は\x01",
            "世界的にも超有名な劇団だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xB,
        (
            "アーティストたちも\x01",
            "トップクラスの名優ばかりだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        (
            "ま、その中でもイリア様は別格だな！\x01",
            "稀代の舞姫、天才イリア・プラティエ……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "ポリセの奴が\x01",
            "熱を上げるのも良く分かるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_570B")

    Jump("loc_5819")

    label("loc_5710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_577C")

    #C0267
    ChrTalk(
        0xB,
        (
            "《劇団アルカンシェル》は\x01",
            "普段はファン立ち入り禁止なんだよな～。\x01",
            "外から眺めるしかないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5819")

    label("loc_577C")


    #C0268
    ChrTalk(
        0xB,
        (
            "おっ、君らも\x01",
            "《劇団アルカンシェル》の\x01",
            "様子を見に来たのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        (
            "中はファン立ち入り禁止だけど、\x01",
            "外から見る分にはタダだぜ。\x01",
            "ま、お仲間同士ヨロシクな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5819")

    TalkEnd(0xFE)
    Return()

    # Function_15_4B1C end

    def Function_16_581D(): pass

    label("Function_16_581D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5886")

    #C0270
    ChrTalk(
        0xC,
        (
            "今夜は家族で\x01",
            "ディナーに行くつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xC,
        (
            "うふふ、そろそろ\x01",
            "支度をしなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_5886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_58E5")

    #C0272
    ChrTalk(
        0xC,
        "今日は表通りが少し静かね……\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xC,
        (
            "導力車の数も\x01",
            "いつもより少ない気がするわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_58E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_596E")

    #C0274
    ChrTalk(
        0xC,
        (
            "ハルトマン議長のライバルは\x01",
            "一応キャンベル議員のはずだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "あの議長さんに\x01",
            "勝てる人なんているのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A1B")

    label("loc_596E")


    #C0276
    ChrTalk(
        0xC,
        (
            "ハルトマン議長って\x01",
            "あのふてぶてしい人よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "ルバーチェと\x01",
            "繋がってるらしいけど、\x01",
            "あごで使っちゃってるとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xC,
        (
            "ふふ、怖いヒト。\x01",
            "敵に回したらおっかないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5A1B")

    Jump("loc_6491")

    label("loc_5A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5AA7")

    #C0279
    ChrTalk(
        0xC,
        (
            "一時期中性的なカンジのホストが\x01",
            "噂になっていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        (
            "残念な事に、記念祭の後から\x01",
            "話を聞かないわねえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_5AA7")


    #C0281
    ChrTalk(
        0xC,
        (
            "あのホストの少年……\x01",
            "最近噂を聞かないわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        (
            "涼しげな瞳に\x01",
            "中性的なカンジがいかしてるって\x01",
            "一時期評判だったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        "ふう……残念だわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5B3D")

    Jump("loc_6491")

    label("loc_5B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5C02")

    #C0284
    ChrTalk(
        0xC,
        (
            "記念祭の５日間だけで\x01",
            "どこの店も\x01",
            "とっても儲かったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xC,
        (
            "うふふ、つまり観光客が\x01",
            "ミラを落としていったってことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "またクロスベルが\x01",
            "世界からミラを集めちゃったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_5C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5CA2")

    #C0287
    ChrTalk(
        0xFE,
        (
            "各種パーティにカジノ巡り、\x01",
            "劇場鑑賞にミシュラムのテーマパーク……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "うふふ、記念祭も忙しくなりそうね。\x01",
            "みっちり予定を立てておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_5CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D29")

    #C0289
    ChrTalk(
        0xC,
        (
            "記念祭を見越して\x01",
            "早めにクロスベル入りしている\x01",
            "観光客もいるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        (
            "この辺りのホテルは\x01",
            "満室が続いてるそうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_5D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5D8C")

    #C0291
    ChrTalk(
        0xC,
        (
            "うふふ、今夜は\x01",
            "社交パーティに誘われているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        "おめかしして急がなくっちゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_5D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5DE5")

    #C0293
    ChrTalk(
        0xC,
        (
            "あまり噂は聞かないけど、\x01",
            "最近事件が\x01",
            "多かったりするのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E5C")

    label("loc_5DE5")


    #C0294
    ChrTalk(
        0xC,
        (
            "最近警察の人が\x01",
            "聞き込みに来ていたりするのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        "やれやれね……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        (
            "またどこかで\x01",
            "事件でもあったのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5E5C")

    Jump("loc_6491")

    label("loc_5E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5F4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5EE0")

    #C0297
    ChrTalk(
        0xC,
        (
            "アルカンシェルファンのパワーは\x01",
            "相変わらず凄いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "さすがの私も\x01",
            "チケット買い逃しちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F45")

    label("loc_5EE0")


    #C0299
    ChrTalk(
        0xC,
        (
            "チケットの発売当日は\x01",
            "凄い騒ぎだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xC,
        (
            "お陰で私も買い逃しちゃったわ。\x01",
            "は～あ、残念。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5F45")

    Jump("loc_6491")

    label("loc_5F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5FCC")

    #C0301
    ChrTalk(
        0xC,
        "さて、今日はどこで遊ぼうかしら。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xC,
        (
            "うふふ、歓楽街に\x01",
            "ゴタゴタは付き物だもの。\x01",
            "いちいち気にしてられないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_5FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_611C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_604A")

    #C0303
    ChrTalk(
        0xC,
        (
            "アルモリカ村やマインツは\x01",
            "田舎だけど、\x01",
            "ウルスラ病院は違うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xC,
        (
            "市民にもおなじみの\x01",
            "大学病院ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6117")

    label("loc_604A")


    #C0305
    ChrTalk(
        0xC,
        (
            "ウルスラ病院は\x01",
            "クロスベル市の南にある\x01",
            "最新の医療施設よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "うふふ、アルモリカ村や\x01",
            "マインツと違って、\x01",
            "市民にもおなじみね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xC,
        (
            "クロスベルでは、\x01",
            "怪我をしたら真っ先に\x01",
            "ウルスラ病院に行くんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6117")

    Jump("loc_6491")

    label("loc_611C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_618A")

    #C0308
    ChrTalk(
        0xC,
        "客引きの男には気をつけなさいな。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "連中に捕まったら\x01",
            "全財産ぼったくられるわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6223")

    label("loc_618A")


    #C0310
    ChrTalk(
        0xC,
        (
            "そっちの裏通りの方には\x01",
            "怪しい客引きの男が何人もいるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xC,
        "慣れていないなら気を付けることね。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xC,
        (
            "油断していると\x01",
            "言いくるめられちゃうわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6223")

    Jump("loc_6491")

    label("loc_6228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6357")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_62A9")

    #C0313
    ChrTalk(
        0xC,
        (
            "クロスベルの歓楽街って言えば\x01",
            "周辺諸国でも有名な社交場よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xC,
        (
            "遊びに来る観光客も\x01",
            "後を絶たないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6352")

    label("loc_62A9")


    #C0315
    ChrTalk(
        0xC,
        (
            "クロスベルの歓楽街って言えば\x01",
            "有名な社交場よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "庶民相手のカジノから\x01",
            "上流階級御用達のお店まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        (
            "うふふ、外国から\x01",
            "遊びに来る観光客も\x01",
            "後を絶たないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6352")

    Jump("loc_6491")

    label("loc_6357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_63D9")

    #C0318
    ChrTalk(
        0xC,
        (
            "この辺りはカジノやホテル、\x01",
            "飲食店なんかが軒を連ねているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xC,
        (
            "観光客ならあちこち\x01",
            "歩き回ってみるべきかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6491")

    label("loc_63D9")


    #C0320
    ChrTalk(
        0xC,
        (
            "あら、見ない顔ね。\x01",
            "観光客かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "ふふふ、遊ぶならカジノ、\x01",
            "観光なら《アルカンシェル》がお勧めね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xC,
        (
            "この辺りはいい店が沢山あるわよ。\x01",
            "探してみるといいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_6491")

    TalkEnd(0xFE)
    Return()

    # Function_16_581D end

    def Function_17_6495(): pass

    label("Function_17_6495")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_64E4")

    #C0323
    ChrTalk(
        0xD,
        "よぉし、日が暮れてきた！\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xD,
        "今日もはりきって遊ぶかぁ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_725B")

    label("loc_64E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_656C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_651B")

    #C0325
    ChrTalk(
        0xD,
        "一度帰って寝てくるかな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6567")

    label("loc_651B")


    #C0326
    ChrTalk(
        0xD,
        (
            "今日は朝まで\x01",
            "スロット打ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xD,
        "う～、腹へって仕方ないぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6567")

    Jump("loc_725B")

    label("loc_656C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_65A7")

    #C0328
    ChrTalk(
        0xD,
        "俺にもそんなツキがあればなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6643")

    label("loc_65A7")


    #C0329
    ChrTalk(
        0xD,
        (
            "カジノでぼろ儲けした奴、\x01",
            "今はホステスかこって\x01",
            "超リッチにやってるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xD,
        "くぅぅ、羨ましいぜ。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xD,
        (
            "そういう奴を\x01",
            "成功者って言うんだろうな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6643")

    Jump("loc_725B")

    label("loc_6648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6724")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_66AB")

    #C0332
    ChrTalk(
        0xD,
        (
            "カジノで勝ち続けるなんて\x01",
            "中々出来ないぜ。\x01",
            "誰だか知らんがやるよなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_671F")

    label("loc_66AB")


    #C0333
    ChrTalk(
        0xD,
        (
            "……聞いたか？\x01",
            "最近カジノでぼろ儲けを\x01",
            "続けてる奴がいるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xD,
        (
            "どこの誰だか\x01",
            "知らないけど、やるなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_671F")

    Jump("loc_725B")

    label("loc_6724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_677E")

    #C0335
    ChrTalk(
        0xD,
        (
            "今日はスロットをやりたい気分だが\x01",
            "……どこかいい店はねえかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6801")

    label("loc_677E")


    #C0336
    ChrTalk(
        0xD,
        "ミラと欲望の渦巻く土地……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xD,
        (
            "記念祭が終わっても\x01",
            "歓楽街は歓楽街だしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "ここに来てすることといえば\x01",
            "１つしかないぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6801")

    Jump("loc_725B")

    label("loc_6806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_688D")

    #C0339
    ChrTalk(
        0xD,
        (
            "アルカンシェルの\x01",
            "スポンサーっていやあ\x01",
            "有力者や外国の富豪も多いしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xD,
        "みんなすげえ導力車を持ってるぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6921")

    label("loc_688D")


    #C0341
    ChrTalk(
        0xD,
        (
            "アルカンシェルの\x01",
            "プレ公演が近いんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        (
            "時々スポンサーさんが\x01",
            "顔を出しに来るんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "みんなすげえ導力車だぜ。\x01",
            "羨ましいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6921")

    Jump("loc_725B")

    label("loc_6926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_69A2")

    #C0344
    ChrTalk(
        0xD,
        "リーシャって子、かわいいよな～。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xD,
        (
            "まだ入団したばっからしいけど\x01",
            "いつも一生懸命って感じだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A41")

    label("loc_69A2")


    #C0346
    ChrTalk(
        0xD,
        (
            "アルカンシェルの新人団員に\x01",
            "リーシャって子がいるだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xD,
        "あの子かわいいよな～。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xD,
        (
            "出勤する所を時々見かけるけど\x01",
            "慣れない所を一生懸命って感じだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6A41")

    Jump("loc_725B")

    label("loc_6A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6AC4")

    #C0349
    ChrTalk(
        0xD,
        (
            "毎日この時間になると\x01",
            "大聖堂の鐘が突かれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xD,
        (
            "けっこう荘厳な音色でさ。\x01",
            "観光客にも人気の風物詩だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725B")

    label("loc_6AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6CED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_6BBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B75")

    #C0351
    ChrTalk(
        0xFE,
        (
            "さっきのリムジン、そういや時々\x01",
            "アルカンシェルの前に\x01",
            "停まってる気がするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "先週も見かけたんだよな。\x01",
            "すぐに走り去っちまったけどさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BB6")

    label("loc_6B75")


    #C0353
    ChrTalk(
        0xFE,
        (
            "あんなリムジン、高いだろうな～。\x01",
            "一体どこの資産家なんだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BB6")

    Jump("loc_6CE8")

    label("loc_6BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_END)), "loc_6C2D")

    #C0354
    ChrTalk(
        0xFE,
        (
            "あれー、何だか\x01",
            "すげぇ車が停まってんなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "黒塗りのリムジンなんて\x01",
            "どこの資産家の車だろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CE8")

    label("loc_6C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6C8E")

    #C0356
    ChrTalk(
        0xD,
        (
            "あんたらもホテルを取るなら\x01",
            "早めにしとけよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        "今年はもう遅いと思うけどな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CE8")

    label("loc_6C8E")


    #C0358
    ChrTalk(
        0xD,
        (
            "最近どこのホテルへ行っても\x01",
            "予約で一杯らしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xD,
        "やっぱ記念祭が近いからなぁ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6CE8")

    Jump("loc_725B")

    label("loc_6CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6D67")

    #C0360
    ChrTalk(
        0xD,
        "オレもチケット買いたかったんだが……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "へっ、あのファンの間に\x01",
            "割って入る勇気はなかったぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DF5")

    label("loc_6D67")


    #C0362
    ChrTalk(
        0xD,
        (
            "アルカンシェルの新作は\x01",
            "『金の太陽、銀の月』っていうらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xD,
        (
            "発表されたときは\x01",
            "熱狂的なファンが集まって\x01",
            "この辺りも大騒ぎだったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6DF5")

    Jump("loc_725B")

    label("loc_6DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6E2E")

    #C0364
    ChrTalk(
        0xD,
        "さぁて、今日はどこで遊ぶかな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_725B")

    label("loc_6E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6ED0")

    #C0365
    ChrTalk(
        0xD,
        (
            "ホテル《ミレニアム》、\x01",
            "新しい支配人のお陰で\x01",
            "さらにリッチになったらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xD,
        (
            "オレもパーっと儲けたら\x01",
            "一泊くらいしてみたいもんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F9D")

    label("loc_6ED0")


    #C0367
    ChrTalk(
        0xD,
        (
            "……知ってるか？\x01",
            "ホテル《ミレニアム》の支配人って\x01",
            "おととし辺りに変わったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xD,
        (
            "お陰であの高級ホテルが\x01",
            "さらにリッチになったらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xD,
        (
            "オレもパーっと儲けたら\x01",
            "一泊くらいしてみたいもんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6F9D")

    Jump("loc_725B")

    label("loc_6FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_70BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_7002")

    #C0370
    ChrTalk(
        0xD,
        (
            "《バルカ》は結構サービスいいんだ。\x01",
            "オーナーは渋いオッサンだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70B5")

    label("loc_7002")


    #C0371
    ChrTalk(
        0xD,
        (
            "そこに《バルカ》って\x01",
            "カジノハウスあるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xD,
        (
            "あそこって結構サービスいいんだ。\x01",
            "負けたときは\x01",
            "オーナーが一杯奢ってくれたりさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xD,
        (
            "ノリ気なら\x01",
            "行ってみるといいんじゃね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_70B5")

    Jump("loc_725B")

    label("loc_70BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_717D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_711A")

    #C0374
    ChrTalk(
        0xD,
        (
            "どっか裏通りのバーにでも入るかな。\x01",
            "表通りって食事できる所ねえしさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7178")

    label("loc_711A")


    #C0375
    ChrTalk(
        0xD,
        "うーん、にしても腹がへったな。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xD,
        (
            "遊び歩いてるとついつい\x01",
            "食事すんのを忘れちまうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_7178")

    Jump("loc_725B")

    label("loc_717D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_71E1")

    #C0377
    ChrTalk(
        0xD,
        (
            "クロスベルは娯楽には\x01",
            "困らない街だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        (
            "一生遊んでも\x01",
            "飽きない気がするなぁ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_725B")

    label("loc_71E1")


    #C0379
    ChrTalk(
        0xD,
        "よぅし、今日も遊ぶぞー！\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xD,
        (
            "どっかのカジノで一勝負するか、\x01",
            "女呼んでバーで飲むか……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        "何して過ごすっかなー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_725B")

    TalkEnd(0xFE)
    Return()

    # Function_17_6495 end

    def Function_18_725F(): pass

    label("Function_18_725F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_72E3")

    #C0382
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xE,
        (
            "あの鉱員だったお客さん、\x01",
            "どうしちゃったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xE,
        "今日は来てくれないわね～ン。\x02",
    )

    CloseMessageWindow()
    Jump("loc_746E")

    label("loc_72E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_733E")

    #C0385
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xE,
        (
            "カジノハウス《バルカ》は\x01",
            "今日も絶好調よ～ン！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746E")

    label("loc_733E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7397")

    #C0387
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "あら……お子さん連れ？\x01",
            "うふふ、大歓迎よン㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746E")

    label("loc_7397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_73E1")

    #C0389
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xE,
        "今日はサービスしちゃうぞっ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_746E")

    label("loc_73E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7434")

    #C0391
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        (
            "カジノハウス\x01",
            "《バルカ》をよろしくね㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746E")

    label("loc_7434")


    #C0393
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xE,
        "うふふ、楽しんでいってね㈱\x02",
    )

    CloseMessageWindow()

    label("loc_746E")

    TalkEnd(0xFE)
    Return()

    # Function_18_725F end

    def Function_19_7472(): pass

    label("Function_19_7472")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_75DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7567")

    #C0395
    ChrTalk(
        0xFE,
        (
            "今日夜勤なのよね。\x01",
            "一度本部に戻って仮眠取らなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        "ロイド君たちはこれから捜査？\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#0000Fええ、少し\x01",
            "ウルスラ病院の方まで。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "支援課も大変ね……\x01",
            "うん、お互い頑張ろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#0000Fはは……そうですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_75D5")

    label("loc_7567")


    #C0400
    ChrTalk(
        0xFE,
        (
            "今日夜勤なのよね。\x01",
            "えーっと一度本部に戻って、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        (
            "帰りがけにどこかで\x01",
            "お夜食も買っておかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D5")

    Jump("loc_763E")

    label("loc_75DA")


    #C0402
    ChrTalk(
        0xFE,
        (
            "最近歓楽街でも\x01",
            "トラブルが増えているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "景気がいいせいかしら……\x01",
            "巡回も強化しなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_763E")

    TalkEnd(0xFE)
    Return()

    # Function_19_7472 end

    def Function_20_7642(): pass

    label("Function_20_7642")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78BB")
    TurnDirection(0xFE, 0x103, 0)

    #C0404
    ChrTalk(
        0xFE,
        "やあティオ君～。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "ここのジェラートは\x01",
            "おいしいと聞いたけど、本当かなぁ。\x02",
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
            "#0005F（ティオ……確かこの人って\x01",
            "  エプスタイン財団の人だよな。）\x02\x03",

            "（ヨナのこと、\x01",
            "  言わなくていいのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x103,
        (
            "#0203F（ええ、しばらくは\x01",
            "  伏せておこうかと。）\x02\x03",

            "#0200F（……ヨナを脅す\x01",
            "  ネタにもなりますし。）\x02",
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
            "#0303F（断ったら財団に突き出す……か。\x01",
            "  ティオすけらしいぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#0100F（エプスタイン財団の子って\x01",
            "  みんな結構逞しいわよね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 7)
    Jump("loc_7962")

    label("loc_78BB")


    #C0410
    ChrTalk(
        0xFE,
        (
            "ここのジェラートが本当に\x01",
            "おいしいかどうか、検証中なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "でも残念な事に\x01",
            "ピーチ味がないんだ……\x01",
            "僕はピーチ一択なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x103,
        "#0211F主任、ヒマそうですね。\x02",
    )

    CloseMessageWindow()

    label("loc_7962")

    TalkEnd(0xFE)
    Return()

    # Function_20_7642 end

    def Function_21_7966(): pass

    label("Function_21_7966")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7984")
    Call(0, 22)
    Jump("loc_7AA1")

    label("loc_7984")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0413
    ChrTalk(
        0x13,
        "#6002Fあ、おいしい……！\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x11,
        (
            "#0809Fでしょ！？\x01",
            "あたしのお気に入りなの。\x02\x03",

            "#0806F記念祭の時はもう一軒、\x01",
            "おいしい店が出てたんだけどね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x12,
        (
            "#0900Fシズクちゃんにも\x01",
            "食べさせてあげたかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A92")

    #C0416
    ChrTalk(
        0x101,
        (
            "#0000F（はは……\x01",
            "  盛り上がってるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A92")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    label("loc_7AA1")

    TalkEnd(0xFE)
    Return()

    # Function_21_7966 end

    def Function_22_7AA5(): pass

    label("Function_22_7AA5")

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
            "#0800Fシズクちゃん、\x01",
            "どのフレーバーがいい？\x02\x03",

            "オゴってあげるから\x01",
            "何でも好きなのを頼んでね！\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x13,
        (
            "#6010Fそ、そんな……悪いです。\x02\x03",

            "ただでさえお父さんの代わりに\x01",
            "付き合ってもらってるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x11,
        (
            "#0809Fあはは、いいのいいの！\x01",
            "シズクちゃんと一緒にいられるなんて\x01",
            "こっちとしては役得だし！\x02\x03",

            "#0800Fそれじゃ、あたしの\x01",
            "オススメを頼んじゃうわね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x8, 500)

    #C0420
    ChrTalk(
        0x11,
        (
            "#0809Fお姉さん！\x02\x03",

            "キャラメルクランチと\x01",
            "ストロベリーチーズケーキと\x01",
            "ラムレーズンをトリプルでね！\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "はい、おまちどうです。\x01",
            "どーんと食べちゃってくださいー。\x02",
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
            "#0906F……ゴメンね。\x01",
            "エステルがいつも強引でさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0423
    ChrTalk(
        0x13,
        (
            "#6000Fい、いえ、そんな……\x01",
            "すごく嬉しいですけど……\x02",
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
            "#0005F（シズクちゃん……\x01",
            "  エステルたちと一緒なのか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x102,
        "#0100F（邪魔しちゃ悪そうね……）\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x103,
        (
            "#0200F（でも、アリオスさんの方は\x01",
            "  どうしたんでしょう……？）\x02",
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

    # Function_22_7AA5 end

    def Function_23_7F51(): pass

    label("Function_23_7F51")

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

    def lambda_80B8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80B8)

    def lambda_80D2():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_80D2)
    Sleep(50)

    def lambda_80E6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_80E6)

    def lambda_8100():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8100)
    Sleep(50)

    def lambda_8114():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFED72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8114)

    def lambda_812E():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_812E)
    Sleep(50)

    def lambda_8142():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFED72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8142)

    def lambda_815C():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_815C)
    WaitChrThread(0x101, 1)

    def lambda_8171():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8171)
    WaitChrThread(0x102, 1)

    def lambda_8182():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8182)
    WaitChrThread(0x103, 1)

    def lambda_8193():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8193)
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
            "#0006F#12P……ふう、失敗失敗。\x01",
            "普通に開いてるのかと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x103,
        (
            "#0200F#5Pあの……\x01",
            "イリア・プラティエって誰ですか？\x02\x03",

            "随分と綺麗な人でしたが。\x02",
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
            "#0305F#5Pなにィ！？\x01",
            "イリアを知らねぇのかよ！？\x02\x03",

            "#0309Fやれやれ、遅れてるねぇ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x103,
        "#0211F#5Pム……\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x102,
        (
            "#0102F#6Pあはは……\x01",
            "クロスベルじゃ有名な人なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0432
    NpcTalk(
        0x18,
        "娘の声",
        "#2S#11Pそれじゃあ、お先に失礼します。\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_8362():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF15A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8362)

    def lambda_837C():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_837C)
    WaitChrThread(0x18, 1)

    def lambda_8391():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8391)

    def lambda_839E():
        TurnDirection(0x102, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_839E)

    def lambda_83AB():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_83AB)

    def lambda_83B8():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_83B8)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("紫髪の娘")

    #A0433
    AnonymousTalk(
        0xFF,
        "あっ、すみません……！\x02",
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
            "#0002F#12Pい、いや。\x01",
            "こちらこそ邪魔しちゃって。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8493():
        OP_98(0x101, 0xFA, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8493)

    def lambda_84AD():
        OP_98(0x102, 0xFFFFFF06, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_84AD)

    def lambda_84C7():
        OP_98(0x103, 0xFA, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_84C7)

    def lambda_84E1():
        OP_98(0x104, 0xFFFFFF06, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_84E1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #N0435
    NpcTalk(
        0x18,
        "紫髪の娘",
        "#1804F#5P………………（ペコリ）\x02",
    )

    CloseMessageWindow()

    def lambda_8539():

        label("loc_8539")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_8539")

    QueueWorkItem2(0x0, 1, lambda_8539)

    def lambda_854B():

        label("loc_854B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_854B")

    QueueWorkItem2(0x1, 1, lambda_854B)

    def lambda_855D():

        label("loc_855D")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_855D")

    QueueWorkItem2(0x2, 1, lambda_855D)

    def lambda_856F():

        label("loc_856F")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_856F")

    QueueWorkItem2(0x3, 1, lambda_856F)
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
        "#0300F#5P劇団の子みたいだな。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        (
            "#0100F#5P見たことのない人だけど……\x01",
            "最近入った新人なのかしら？\x02",
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

    # Function_23_7F51 end

    def Function_24_874A(): pass

    label("Function_24_874A")

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

    # Function_24_874A end

    def Function_25_87CB(): pass

    label("Function_25_87CB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_885F")
    Jump("loc_88A9")

    label("loc_885F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_887F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88A9")

    label("loc_887F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_889F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88A9")

    label("loc_889F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_88A9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_89A7")

    #C0438
    ChrTalk(
        0x14,
        (
            "#0106F副局長にはイヤミばかり言われて\x01",
            "いい思い出が無いけれど……\x02\x03",

            "#0100F恐妻家だったり泥酔したり、\x01",
            "あの人も色々あるみたいね。\x02\x03",

            "#0105F……２人とも、疲れたりしてない？\x01",
            "一旦引き上げても良いと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A97")

    label("loc_89A7")


    #C0439
    ChrTalk(
        0x14,
        "#0100Fどう、捜索の方は順調？\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x101,
        "#0000Fはは、何とか……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x103,
        (
            "#0203Fツァイトの鼻は正確ですが、\x01",
            "やはり副局長の行動が\x01",
            "不透明なのが痛いかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x14,
        (
            "#0106Fやっぱり時間が掛かりそうね。\x02\x03",

            "#0100F疲れたら一旦引き上げても\x01",
            "良いと思うけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_8A97")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【このまま続ける】\x01",      # 0
            "【捜索を中断する】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BD5")

    #C0443
    ChrTalk(
        0x101,
        (
            "#0006Fそうだな……疲れたし\x01",
            "一旦中断しようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        (
            "#0203Fそうですね。\x02\x03",

            "#0200F再開する場合は\x01",
            "またツァイトに\x01",
            "同行を求めましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x14,
        (
            "#0100Fじゃあランディを\x01",
            "引っ張って帰りましょうか。\x02",
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
    Jump("loc_8C04")

    label("loc_8BD5")


    #C0446
    ChrTalk(
        0x14,
        (
            "#0100Fそう、無理しないように\x01",
            "頑張ってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C04")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_87CB end

    def Function_26_8C0C(): pass

    label("Function_26_8C0C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_8EC5")

    def lambda_8CC5():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CC5)

    def lambda_8CD2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CD2)

    def lambda_8CDF():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CDF)

    def lambda_8CEC():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CEC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0447
    ChrTalk(
        0x101,
        (
            "#6P#0000Fよし、それじゃあ\x01",
            "捜索を再開しよう。\x02\x03",

            "エリィとランディは……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x104,
        "#0309F任しとけ、待機してるぜ！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 1, 0, 27)

    def lambda_8D7D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D7D)

    def lambda_8D8A():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D8A)

    def lambda_8D97():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D97)

    def lambda_8DA4():
        OP_93(0x11C, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_8DA4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)
    WaitChrThread(0x104, 1)
    Sleep(400)

    def lambda_8DC8():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DC8)

    def lambda_8DD5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DD5)

    def lambda_8DE2():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DE2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0449
    ChrTalk(
        0x102,
        (
            "#0100F私はそこの\x01",
            "屋台の傍で待機しているわね。\x02\x03",

            "ロイド、ティオちゃん、\x01",
            "頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_8E7E")
    OP_1B(0x1, 0x0, 0x24)
    OP_1B(0x2, 0x0, 0x25)
    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x4, 0x0, 0x27)
    OP_1B(0x5, 0x0, 0x28)
    OP_1B(0x6, 0x0, 0x29)
    Jump("loc_8EBD")

    label("loc_8E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8EBD")
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

    label("loc_8EBD")

    ClearScenarioFlags(0x95, 7)
    Jump("loc_9556")

    label("loc_8EC5")


    #C0450
    ChrTalk(
        0x101,
        (
            "#6P#0001Fさてと……ここから副局長は\x01",
            "どっちの方向へ行ったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x11C,
        "#11P#1200F………フンフン…………\x02",
    )

    CloseMessageWindow()
    OP_93(0x11C, 0x5A, 0x1F4)

    #C0452
    ChrTalk(
        0x11C,
        "#11P#1200Fグルルルル………\x02",
    )

    CloseMessageWindow()

    def lambda_8F5F():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F5F)
    Sleep(50)

    def lambda_8F6F():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F6F)
    Sleep(50)

    def lambda_8F7F():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F7F)
    Sleep(50)

    def lambda_8F8F():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F8F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0453
    ChrTalk(
        0x103,
        "#11P#0200F東の方角……のようですね。\x02",
    )

    CloseMessageWindow()

    def lambda_8FD6():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FD6)

    def lambda_8FE3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FE3)

    def lambda_8FF0():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8FF0)

    def lambda_8FFD():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8FFD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0454
    ChrTalk(
        0x101,
        (
            "#12P#0004Fよし、じゃあここからは\x01",
            "ツァイトの鼻を頼りに\x01",
            "副局長の歩いた後を辿ってみよう。\x02\x03",

            "#0000Fルート上に落とし物がないか\x01",
            "注意しながら歩かないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x102,
        (
            "#11P#0105Fでもロイド、この人数は\x01",
            "少し大げさじゃない？\x02\x03",

            "#0100F街中だし絞った方が\x01",
            "いいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうだな……流石に多いか。\x02\x03",

            "#0000Fエリィ、ランディ。\x01",
            "一旦待機していてくれるか？\x02\x03",

            "もっと範囲を絞り込んでから\x01",
            "応援を頼むと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x0, 0x1F4)

    #C0457
    ChrTalk(
        0x104,
        (
            "#5P#0304F了解、それまで待機してるぜ。\x02\x03",

            "#0309Fん～、今日のゲームは……と。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 1, 0, 27)

    def lambda_9209():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9209)

    def lambda_9216():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9216)

    def lambda_9223():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9223)

    def lambda_9230():
        OP_93(0x11C, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_9230)

    #C0458
    ChrTalk(
        0x101,
        "#12P#0005Fあ……\x02",
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
        "#11P#0211F止める間もなかったです。\x02",
    )

    CloseMessageWindow()

    def lambda_928F():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_928F)

    def lambda_929C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_929C)

    def lambda_92A9():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92A9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0460
    ChrTalk(
        0x102,
        (
            "#11P#0106Fいつもあの調子なんだから……\x02\x03",

            "#0100Fまあいいわ、後で\x01",
            "呼びつければいいんだし。\x02\x03",

            "ロイド、私はそこの\x01",
            "屋台の傍で待機しているわね。\x01",
            "何かあったら声をかけて頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        (
            "#6P#0000F分かった、\x01",
            "そうさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0462
    ChrTalk(
        0x102,
        (
            "#5P#0100Fじゃあね、\x01",
            "ティオちゃん、ツァイト。\x02",
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

    def lambda_9442():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9442)

    def lambda_944F():
        OP_93(0x11C, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_944F)
    Sleep(50)

    def lambda_945F():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_945F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)

    #C0463
    ChrTalk(
        0x103,
        "#11P#0200Fそれでは始めましょうか。\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、そうしよう。\x02\x03",

            "俺たちが先を歩くから……\x01",
            "ツァイト、ルートが間違っていたら\x01",
            "注意してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x11C,
        "#11P#1200Fウォン！\x02",
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

    label("loc_9556")

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

    # Function_26_8C0C end

    def Function_27_9628(): pass

    label("Function_27_9628")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)

    def lambda_965C():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_965C)
    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_27_9628 end

    def Function_28_9698(): pass

    label("Function_28_9698")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96B2")
    TurnDirection(0xFE, 0x102, 500)
    Sleep(100)
    Jump("Function_28_9698")

    label("loc_96B2")

    Return()

    # Function_28_9698 end

    def Function_29_96B3(): pass

    label("Function_29_96B3")

    TalkBegin(0xFF)

    #C0466
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "……ウォン！\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x01",
            "これで合ってるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        (
            "#0200Fええ、このルートで\x01",
            "間違いないようです。\x02\x03",

            "この調子で進みましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x3)
    TalkEnd(0xFF)
    Return()

    # Function_29_96B3 end

    def Function_30_9760(): pass

    label("Function_30_9760")

    TalkBegin(0xFF)

    #C0469
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "……ウォン！\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x01",
            "ここに匂いが残ってるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x103,
        (
            "#0200F副局長はここで\x01",
            "一休みしたようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_30_9760 end

    def Function_31_97F7(): pass

    label("Function_31_97F7")

    TalkBegin(0xFF)

    #C0472
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        "#0003Fここは……違うみたいだな？\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x103,
        (
            "#0200Fええ、特に匂いは\x01",
            "残っていないようです。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_31_97F7 end

    def Function_32_9881(): pass

    label("Function_32_9881")

    TalkBegin(0xFF)

    #C0475
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x101,
        "#0003Fここは……違うみたいだな？\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x103,
        (
            "#0200Fええ、特に匂いは\x01",
            "残っていないようです。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_32_9881 end

    def Function_33_990B(): pass

    label("Function_33_990B")

    TalkBegin(0xFF)

    #C0478
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        "#0003Fここは……違うみたいだな？\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x103,
        (
            "#0200Fええ、特に匂いは\x01",
            "残っていないようです。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_33_990B end

    def Function_34_9995(): pass

    label("Function_34_9995")

    TurnDirection(0x11C, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_99F4")

    #C0481
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        "#0005F（このルートじゃないみたいだ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A8F")

    label("loc_99F4")


    #C0483
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0484
    ChrTalk(
        0x101,
        "#0005Fこ、こっちじゃないのか？\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x103,
        (
            "#0200Fこのルートでは\x01",
            "ないみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_9A8F")

    Return()

    # Function_34_9995 end

    def Function_35_9A90(): pass

    label("Function_35_9A90")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_35_9A90 end

    def Function_36_9AAC(): pass

    label("Function_36_9AAC")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_36_9AAC end

    def Function_37_9AC8(): pass

    label("Function_37_9AC8")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_37_9AC8 end

    def Function_38_9AE4(): pass

    label("Function_38_9AE4")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, -2110, 2660, 34550, 180)
    EventEnd(0x4)
    Return()

    # Function_38_9AE4 end

    def Function_39_9B00(): pass

    label("Function_39_9B00")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 17100, 2060, 23000, 270)
    EventEnd(0x4)
    Return()

    # Function_39_9B00 end

    def Function_40_9B1C(): pass

    label("Function_40_9B1C")

    EventBegin(0x1)
    Call(0, 34)
    Sleep(50)
    SetChrPos(0x0, 13690, 90, -6130, 270)
    EventEnd(0x4)
    Return()

    # Function_40_9B1C end

    def Function_41_9B38(): pass

    label("Function_41_9B38")

    EventBegin(0x1)

    #C0486
    ChrTalk(
        0x101,
        (
            "#0003Fカジノを調べる必要はないな。\x01",
            "……他の場所を調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -26470, 300, 16370, 180)
    EventEnd(0x4)
    Return()

    # Function_41_9B38 end

    def Function_42_9B96(): pass

    label("Function_42_9B96")

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
            "#11P#0005F副局長……\x01",
            "酔ってホテルの中を通り抜けたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x103,
        (
            "#5P#0206F典型的な酔っ払いの\x01",
            "行動ですね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0489
    ChrTalk(
        0x101,
        (
            "#11P#0000Fああ、でも特に何も\x01",
            "落ちてなかったようだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11C, 0xB4, 0x1F4)

    #C0490
    ChrTalk(
        0x11C,
        "#6P#1200Fグルルルル……ウォン！\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x103, 0xB4, 0x2EE)
    Sleep(750)

    #C0491
    ChrTalk(
        0x103,
        (
            "#5P#0200F……次は南の方に\x01",
            "向かったそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x2EE)

    #C0492
    ChrTalk(
        0x101,
        "#11P#0000Fよし、行ってみよう。\x02",
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

    # Function_42_9B96 end

    def Function_43_9E1F(): pass

    label("Function_43_9E1F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D8")

    #A0493
    AnonymousTalk(
        0x101,
        "#0005Fん？　あれは……\x02",
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
        "#12P……まあ、素敵ですわね！\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x1D,
        (
            "#6Pこれがあの有名な\x01",
            "最高の劇団『アルカンシェル』ね！\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x1E,
        (
            "#11Pふむふむ、チケットは\x01",
            "かなりの高額と聞いたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x1B,
        (
            "#5P皆さん、ご堪能いただけましたか？\x01",
            "それでは次へ参りまーす！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x5A, 0x1F4)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_A132():
        OP_95(0xFE, -160, 1990, 19900, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A132)
    Sleep(500)

    #C0498
    ChrTalk(
        0x1D,
        (
            "#6Pええ～、アルカンシェルの公演は\x01",
            "観れないんですか～？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 1)
    OP_93(0x1B, 0xE1, 0x1F4)

    #C0499
    ChrTalk(
        0x1B,
        (
            "#11Pふふ、実は今日の公演は\x01",
            "夜の部だけなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x1B,
        (
            "#11P夜は自由時間にしますから\x01",
            "ファンの方はぜひ\x01",
            "訪れてみてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x1B,
        (
            "#11P……そして\x01",
            "次にご案内しますのは……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A242():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A242)

    def lambda_A24F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A24F)

    def lambda_A25C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A25C)

    def lambda_A269():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A269)
    WaitChrThread(0x1B, 1)

    def lambda_A27A():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A27A)
    Sleep(1000)
    WaitChrThread(0x1E, 1)

    def lambda_A29B():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A29B)
    Sleep(500)
    WaitChrThread(0x1C, 1)

    def lambda_A2BC():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A2BC)
    Sleep(300)
    WaitChrThread(0x1D, 1)

    def lambda_A2DD():
        OP_95(0xFE, 6940, 1760, 13750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A2DD)
    WaitChrThread(0x1B, 1)

    def lambda_A2FB():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A2FB)
    WaitChrThread(0x1E, 1)

    def lambda_A319():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A319)
    WaitChrThread(0x1C, 1)

    def lambda_A337():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A337)
    WaitChrThread(0x1D, 1)

    def lambda_A355():
        OP_95(0xFE, 22200, 0, 12150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A355)

    #A0502
    AnonymousTalk(
        0x104,
        (
            "#0300F俺もこのあたりは結構遊びに来てるが……\x01",
            "やたらと観光客を見かけるな。\x02",
        )
    )

    CloseMessageWindow()

    #A0503
    AnonymousTalk(
        0x101,
        (
            "#0000Fああ、最近は導力バスを使って\x01",
            "外国からツアーで来る人も多いらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #A0504
    AnonymousTalk(
        0x102,
        (
            "#0104Fこの辺りは歓楽街だから\x01",
            "観光客は必ず立ち寄るそうよ。\x02\x03",

            "#0100F外国人に何かあったら\x01",
            "国際問題にもなりかねないし……\x01",
            "警察#4Rわたしたち#の働きが重要なんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #A0505
    AnonymousTalk(
        0x103,
        "#0200Fなるほど、納得です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A4D8")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0506
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "歓楽街は、街の北側に位置する商業区です。\x02",
        )
    )

    CloseMessageWindow()

    #A0507
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カジノハウスやホテル、有名な劇場などが建ち並び\x01",
            "多くの観光客が訪れます。\x02",
        )
    )

    CloseMessageWindow()

    #A0508
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いくつかの施設は、序盤では入れませんが\x01",
            "物語の進行に合わせて\x01",
            "立ち寄ってみると良いでしょう。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6D5")
    OP_68(21040, 1950, 11840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    Jump("loc_A752")

    label("loc_A6D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A716")
    OP_68(13270, 1950, -19100, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    Jump("loc_A752")

    label("loc_A716")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A752")
    OP_68(-39280, 1950, 12420, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)

    label("loc_A752")

    SetScenarioFlags(0x45, 0)
    EventEnd(0x5)
    Return()

    # Function_43_9E1F end

    def Function_44_A758(): pass

    label("Function_44_A758")

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
            "#4P#0202F改めて見ると……\x01",
            "かなり立派な建物ですね。\x02\x03",

            "結構、新しそうな雰囲気ですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x102,
        (
            "#0104F築２０年になるかしら。\x02\x03",

            "#0100F市庁舎などに比べると\x01",
            "そんなに古い建物ではないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x101,
        (
            "#6P#0003F（アルカンシェルか……）\x02\x03",

            "#0008F（小さい頃、\x01",
            "  兄貴とセシル姉に連れられて\x01",
            "  何度か来たことはあるけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    #C0512
    ChrTalk(
        0x104,
        "#0305F#11Pなんだ、どうした？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#6P#0004Fいや……なんでもない。\x02\x03",

            "#0000F早速、お邪魔しようか。\x02",
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

    # Function_44_A758 end

    def Function_45_AACF(): pass

    label("Function_45_AACF")

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

    def lambda_ABE4():
        OP_96(0xFE, 0xFFFFF574, 0x6E0, 0x68B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABE4)

    def lambda_ABFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ABFE)
    Sleep(250)

    def lambda_AC12():
        OP_96(0xFE, 0xFFFFFAEC, 0x6E0, 0x68B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC12)

    def lambda_AC2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AC2C)
    Sleep(100)

    def lambda_AC40():
        OP_96(0xFE, 0xFFFFF574, 0x6E0, 0x6E28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC40)

    def lambda_AC5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AC5A)
    Sleep(250)

    def lambda_AC6E():
        OP_96(0xFE, 0xFFFFFAEC, 0x6E0, 0x6E28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC6E)

    def lambda_AC88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AC88)
    Sleep(1000)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x101, 1)

    def lambda_ACBB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ACBB)
    WaitChrThread(0x102, 1)

    def lambda_ACCC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ACCC)
    WaitChrThread(0x103, 1)

    def lambda_ACDD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_ACDD)
    WaitChrThread(0x104, 1)

    def lambda_ACEE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_ACEE)
    WaitChrThread(0x104, 2)
    Sleep(300)

    #C0514
    ChrTalk(
        0x104,
        (
            "#5P#0303Fさて……どうするんだ？\x02\x03",

            "#0301F今のところ手がかりは\x01",
            "《ルバーチェ》くらいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x103,
        (
            "#0200F一応《銀》という名前も\x01",
            "手がかりになりそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        "#6P#0008F……そうだな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0517
    ChrTalk(
        0x101,
        (
            "#6P#0003F──なあ、みんな。\x02\x03",

            "#0013F《ルバーチェ商会》を\x01",
            "一度、訪ねてみないか？\x02",
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

    def lambda_AE77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AE77)
    Sleep(50)

    def lambda_AE87():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AE87)
    Sleep(50)

    def lambda_AE97():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AE97)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)

    #C0518
    ChrTalk(
        0x102,
        "#0105F#11Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x104,
        "#5P#0301Fマジか……！？\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        (
            "#6P#0000F別に、警察の捜査として\x01",
            "普通の事情聴取をするだけさ。\x02\x03",

            "#0003F脅迫状を出したのが\x01",
            "ルバーチェの会長かどうかは\x01",
            "まだ分からないけれど……\x02\x03",

            "#0001F面倒を避けてるだけじゃ\x01",
            "真実には辿りつけないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x104,
        "#5P#0303Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        "#0201F#5P……一理ありますね。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそれに、いい機会だと思うんだ。\x02\x03",

            "#0008Fあれだけの事をしても捕まらず\x01",
            "大手を振って歩いている連中……\x02\x03",

            "#0013Fどんな実態なのかを掴める\x01",
            "きっかけになるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x104,
        "#5P#0302Fヘッ……なるほどな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B10C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B10C)
    Sleep(50)

    def lambda_B11C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B11C)
    Sleep(50)

    def lambda_B12C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B12C)
    Sleep(300)
    OP_64(0x102)

    #C0525
    ChrTalk(
        0x101,
        (
            "#6P#0005Fえっと、やっぱり心配か？\x02\x03",

            "#0000F何だったら\x01",
            "俺とランディだけでも……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0526
    ChrTalk(
        0x103,
        "#0211F#5Pロイドさん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0527
    ChrTalk(
        0x101,
        (
            "#6P#0011Fい、いや！\x01",
            "別にそういう意味じゃなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x102,
        (
            "#0104F#11Pううん……\x01",
            "別に心配はしていないわ。\x02\x03",

            "#0108Fそうね、訪ねるだけであれば\x01",
            "それほど危険ではないと思う。\x02\x03",

            "この街のマフィアというのが\x01",
            "本当はどういう存在なのか……\x02\x03",

            "#0102F知るにはいい機会でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B2D1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B2D1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)

    #C0529
    ChrTalk(
        0x101,
        "#6P#0005Fあ、ああ……？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x104,
        (
            "#5P#0305Fなんだよ、お嬢。\x01",
            "随分と思わせぶりだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x102,
        (
            "#0104F#11Pふふっ、気のせいよ。\x02\x03",

            "#0100F脅迫状に関しても\x01",
            "瓢箪#4Rひょうたん#から駒ということが\x01",
            "あるかもしれないし……\x02\x03",

            "早速、訪ねてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        "#6P#0000Fああ……！\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x103,
        (
            "#0203F#5Pデータベースの情報によると……\x02\x03",

            "#0201F《ルバーチェ商会》のビルは\x01",
            "そこの裏通りの途中から\x01",
            "路地の奥に入った先にありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x104,
        (
            "#5P#0304Fヘッ、あの怪しげな一角か。\x02\x03",

            "#0300F連中の姿を見かけると思ったら\x01",
            "マフィアの本拠地だったわけだな。\x02",
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

    # Function_45_AACF end

    def Function_46_B525(): pass

    label("Function_46_B525")

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

    def lambda_B6EC():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x5014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B6EC)
    Sleep(50)

    def lambda_B709():
        OP_96(0xFE, 0xFFFFFA24, 0x7C6, 0x5014, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B709)
    Sleep(50)

    def lambda_B726():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x4B64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B726)
    Sleep(50)

    def lambda_B743():
        OP_96(0xFE, 0xFFFFFA24, 0x7C6, 0x4B64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B743)
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
        "#11P#0005Fあれ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(-2000, 3600, 32000, 2000)
    OP_6F(0x1)

    def lambda_B80B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_B80B)

    def lambda_B81C():
        OP_95(0xFE, -2000, 2660, 31800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B81C)
    Sleep(500)

    def lambda_B839():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_B839)

    def lambda_B84A():
        OP_95(0xFE, -2600, 2660, 32500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B84A)
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
        "#0105F#1Pあ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0537
    NpcTalk(
        0x15,
        "老紳士",
        "#2505F#5Pおお……！？\x02",
    )

    CloseMessageWindow()

    #N0538
    NpcTalk(
        0x16,
        "若い男性",
        "#2605F#5Pエリィお嬢さん……！\x02",
    )

    CloseMessageWindow()

    def lambda_B917():
        OP_95(0xFE, -2000, 1990, 24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B917)
    Sleep(250)

    def lambda_B934():
        OP_96(0xFE, 0xFFFFF574, 0x7C6, 0x607C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B934)
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

    def lambda_B9D5():
        OP_95(0xFE, -2000, 1990, 21700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B9D5)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x10)

    #C0539
    ChrTalk(
        0x102,
        "#0105F#12Pおじいさま……アーネストさん。\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#0005F（え……）\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x103,
        "#0205F#4P（エリィさんのお祖父さん……？）\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("老紳士")

    #A0542
    AnonymousTalk(
        0xFF,
        (
            "フフ、なかなか会えないが\x01",
            "元気でやっているようだね。\x02\x03",

            "仕事の方は頑張っているのかな？\x02",
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
            "#12P#0108Fは、はい……\x02\x03",

            "#0103F……まだまだ新人なので\x01",
            "至らないところもありますが……\x02\x03",

            "#0102Fマクダエル家の名に恥じぬよう\x01",
            "精一杯、頑張らせてもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #N0544
    NpcTalk(
        0x15,
        "老紳士",
        (
            "#5P#2503Fはは……前にも言ったが\x01",
            "家のことは気にすることはない。\x02\x03",

            "#2500Fそちらの諸君は、同僚の方々かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        "#12P#0100Fは、はい。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        (
            "#0003F#12P──初めまして。\x02\x03",

            "#0000Fクロスベル警察・特務支援課、\x01",
            "ロイド・バニングスといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x103,
        "#12P#0204Fティオ・プラトーです。（ペコリ）\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x104,
        (
            "#12P#0300Fどーも。\x01",
            "ランディ・オルランドっス。\x02",
        )
    )

    CloseMessageWindow()

    #N0549
    NpcTalk(
        0x15,
        "老紳士",
        (
            "#5P#2503Fふむ、私の名前は\x01",
            "ヘンリー・マクダエルという。\x02\x03",

            "#2500Fどうやら孫娘が色々と\x01",
            "世話になっているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#0012F#12Pいえ、そんな。\x02\x03",

            "#0000F世話になっているのは\x01",
            "むしろこちらの方で──\x02",
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
            "#12P#0304Fま、確かにお嬢には\x01",
            "報告書とかの書類作りでも\x01",
            "だいぶ助けられちまってるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x103,
        (
            "#6P#0211F少しはランディさんも\x01",
            "手伝うべきかと思いますが……\x02",
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
        "#12P#0109Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #N0554
    NpcTalk(
        0x15,
        "マクダエル老人",
        (
            "#5P#2500Fフフ……\x01",
            "充実した職場で何よりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x16,
        (
            "#2606F#5Pしかし、お嬢さん……\x02\x03",

            "#2601Fたまにはご実家の方にも\x01",
            "お顔を出された方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        (
            "#12P#0108F……す、すみません。\x02\x03",

            "#0106Fその、せっかく自立したのに\x01",
            "頼るのもどうかと思いまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x16,
        "#2601F#5Pですが──\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x190)

    #N0558
    NpcTalk(
        0x15,
        "マクダエル老人",
        (
            "#11P#2503Fいいんだ、アーネスト君。\x02\x03",

            "#2500Fそれだけエリィの決意も\x01",
            "固いということだろう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x102, 400)
    Sleep(300)

    #N0559
    NpcTalk(
        0x15,
        "マクダエル老人",
        (
            "#5P#2500Fお前が選んだ道……\x01",
            "納得のいくまでやってみなさい。\x02\x03",

            "公私混同はできないが、\x01",
            "出来るだけ協力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x102,
        (
            "#12P#0104F……はい。\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x190)
    Sleep(300)

    #N0561
    NpcTalk(
        0x15,
        "マクダエル老人",
        (
            "#11P#2500F──それでは行こうか。\x01",
            "アーネスト君。\x02\x03",

            "次は商工会との会合だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x16,
        "#2600F#5Pはい、５時からになります。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_C1E3():

        label("loc_C1E3")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_C1E3")

    QueueWorkItem2(0x101, 2, lambda_C1E3)

    def lambda_C1F5():

        label("loc_C1F5")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_C1F5")

    QueueWorkItem2(0x102, 2, lambda_C1F5)

    def lambda_C207():

        label("loc_C207")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_C207")

    QueueWorkItem2(0x103, 2, lambda_C207)

    def lambda_C219():

        label("loc_C219")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_C219")

    QueueWorkItem2(0x104, 2, lambda_C219)
    OP_92(0x15, 0xFFFFE890, 0x4650, 0x1F4)

    def lambda_C238():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C238)
    Sleep(150)
    OP_92(0x16, 0xFFFFE5D4, 0x490C, 0x1F4)

    def lambda_C262():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C262)
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

    def lambda_C308():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C308)
    Sleep(50)

    def lambda_C325():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C325)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    Sound(462, 0, 100, 0)
    OP_71(0x4, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x4)

    def lambda_C35C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C35C)

    def lambda_C376():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_C376)
    Sleep(150)

    def lambda_C38A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C38A)
    Sleep(500)

    def lambda_C3A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_C3A7)
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
            "#5P#0305Fヒューッ！\x01",
            "すんげえ車だな、オイ。\x02\x03",

            "#0302Fやっぱりお嬢の実家って\x01",
            "もんのすごい金持ちなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x102,
        "#0109F#5Pえ、えーと……その。\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(600)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0565
    ChrTalk(
        0x101,
        "#5P#0005F#4Sああああっ！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C608():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C608)
    Sleep(50)
    OP_93(0x103, 0x2D, 0x1F4)

    #C0566
    ChrTalk(
        0x104,
        "#12P#0305Fうおっ……\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x103,
        "#6P#0205Fロイドさん……？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        (
            "#5P#0007Fヘンリー・マクダエル……！\x02\x03",

            "このクロスベル市の\x01",
            "市長さんの名前じゃないか！\x02",
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
        "#12P#0301Fな、なにィ……！？\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x103,
        (
            "#6P#0201Fほ、本当ですか……？\x02\x03",

            "#0205F──あ。\x01",
            "確かにデータベースでも\x01",
            "そう記録されていたような。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0571
    ChrTalk(
        0x102,
        "#0106F#5Pふう……\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x190)
    Sleep(300)

    #C0572
    ChrTalk(
        0x102,
        (
            "#0102F#5P──今まで気付かれなかったのが\x01",
            "不思議なくらいだと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C7F3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C7F3)
    Sleep(100)

    def lambda_C803():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C803)
    Sleep(50)
    OP_93(0x104, 0x13B, 0x1F4)

    #C0573
    ChrTalk(
        0x101,
        (
            "#11P#0002Fい、いや……\x01",
            "最初に苗字を聞いた時に\x01",
            "引っかかってはいたんだけど。\x02\x03",

            "何だか色々あったから\x01",
            "すっかり流してたっていうか。\x02\x03",

            "#0006Fいや──でも確かに面目ないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x102,
        (
            "#0104F#5Pまあ、別に気にする事ないわ。\x02\x03",

            "祖父が何者であろうと、\x01",
            "私には関係のないことだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        "#11P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x102,
        (
            "#0106F#5P……それより早く、\x01",
            "イリアさんたちに報告しましょう。\x02\x03",

            "#0101F面目ないけれど……\x01",
            "きちんと引継ぎのことを伝えないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x101,
        "#11P#0001Fあ、ああ……そうだな。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x104,
        (
            "#12P#0305Fところで、そのお嬢のじーさまが\x01",
            "何でアルカンシェルに来てたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x102,
        (
            "#0105F#5Pああ、そうね……\x02\x03",

            "#0103F今回の新作は、市の創立記念祭と\x01",
            "合わせて公開されるそうだから……\x02\x03",

            "#0100Fその関係の打ち合わせに\x01",
            "いらっしゃったのかもしれないわね。\x02",
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

    # Function_46_B525 end

    def Function_47_CBA8(): pass

    label("Function_47_CBA8")


    def lambda_CBAD():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_CBAD)
    Sleep(600)

    def lambda_CBC5():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x157C, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_CBC5)
    Sleep(600)

    def lambda_CBDD():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_CBDD)
    Return()

    # Function_47_CBA8 end

    def Function_48_CBEE(): pass

    label("Function_48_CBEE")

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
            "#1806F#5Pその……何だか迷惑ばかり\x01",
            "おかけしてしまったみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x101,
        (
            "#12P#0012Fいや、気にしないでよ。\x02\x03",

            "#0000F元々警察の仕事なんてのは\x01",
            "地道な無駄骨の繰り返しだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x103,
        "#12P#0202F防犯とか、そんな感じですよね。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x104,
        (
            "#0302F#12Pそうそう、リーシャちゃん。\x02\x03",

            "#0309F俺たちのことは気にしないで\x01",
            "プレ公演、頑張ってくれよな！\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x18,
        "#1802F#5Pはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x104, 500)

    #C0585
    ChrTalk(
        0x101,
        "#6P#0005Fプレ公演？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0586
    ChrTalk(
        0x104,
        (
            "#0305F#11Pなんだ、知らないのか？\x02\x03",

            "#0300Fアルカンシェルは毎回、\x01",
            "新作の本公演の前に一度だけ\x01",
            "お披露目の舞台をやるんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x18,
        (
            "#1804F#5Pは、はい。\x01",
            "私も今回が始めてですけど……\x02\x03",

            "#1802F国内外の関係者やマスコミの方々が\x01",
            "招待されるんだそうです。\x02\x03",

            "公演を後押ししてくださっている\x01",
            "偉い方々も見に来るらしくて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D00A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D00A)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0588
    ChrTalk(
        0x101,
        "#12P#0000Fそうなのか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0589
    ChrTalk(
        0x102,
        (
            "#0105F#12Pひょっとして……\x01",
            "マクダエル市長も招待を？\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x18,
        (
            "#1805F#5Pあ、はい。\x01",
            "主賓としてお迎えするそうです。\x02\x03",

            "#1804F記念祭と合わせて、今回の公演を\x01",
            "後押しして下さっているらしくて。\x02\x03",

            "#1802F今日も、お忙しい所にわざわざ\x01",
            "陣中見舞いに来て下さいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x102,
        "#0100F#12Pそうですか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0592
    ChrTalk(
        0x102,
        (
            "#0104F#12P──リーシャさん。\x01",
            "プレ公演、頑張ってください。\x02\x03",

            "#0102Fリーシャさんなら初めてでも\x01",
            "きっと大丈夫だと思いますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x18,
        "#1805F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x101,
        (
            "#12P#0002Fそうだな、練習を見るかぎり、\x01",
            "何の心配もいらなさそうだったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x104,
        "#0309F#12Pおお、絶対に良い舞台になるって！\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x103,
        "#12P#0204F……すごく楽しみです。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x18,
        (
            "#1809F#5Pあ、ありがとうございます。\x01",
            "その……とっても心強いです。\x02\x03",

            "#1802Fそれでは私、稽古に戻りますね。\x02\x03",

            "皆さん、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(1638, 255, 100, 0)    #voice#Rixia
    Sleep(1000)
    OP_93(0x18, 0x0, 0x1F4)
    OP_68(-2000, 3800, 31800, 3500)

    def lambda_D36C():
        OP_95(0xFE, -2000, 2660, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D36C)
    WaitChrThread(0x18, 1)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    OP_6F(0x79)

    def lambda_D3A7():
        OP_95(0xFE, -2000, 2660, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D3A7)
    Sleep(500)

    def lambda_D3C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_D3C4)
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

    def lambda_D490():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D490)
    Sleep(50)

    def lambda_D4A0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D4A0)
    Sleep(50)

    def lambda_D4B0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D4B0)
    Sleep(50)

    def lambda_D4C0():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D4C0)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    #C0598
    ChrTalk(
        0x101,
        (
            "#0006F#5P……はあ……\x02\x03",

            "#0000F今日はもう、帰るか。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x104,
        "#0306F#11Pだな……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#6P#0206F……何だか\x01",
            "気が抜けてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x102,
        "#0103F#5P……そうね…………\x02",
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

    # Function_48_CBEE end

    def Function_49_D64D(): pass

    label("Function_49_D64D")

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

    def lambda_D880():
        OP_9D(0xFE, 0x4B64, 0x332C, 0x5FB4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D880)
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

    def lambda_D9C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_D9C9)

    def lambda_D9DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_D9DA)
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

    def lambda_DAD1():
        OP_96(0xFE, 0x4B64, 0x332C, 0x7788, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_DAD1)
    WaitChrThread(0x18, 1)
    PlayEffect(0x0, 0xFF, 0x18, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x4)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_DB43():
        OP_9D(0xFE, 0x4B64, 0x13EC, 0x8B10, 0x514, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_DB43)
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

    def lambda_DC13():
        OP_96(0xFE, 0xFFFFF830, 0x6E0, 0x6F54, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_DC13)
    FadeToBright(1000, 0)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x0, 0x1F4)
    OP_6F(0x50)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)

    #N0604
    NpcTalk(
        0x19,
        "女性の声",
        "早いわね、リーシャ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1635, 255, 100, 0)    #voice#Rixia
    OP_68(-2000, 2700, 27600, 3000)

    def lambda_DC9C():
        OP_96(0xFE, 0xFFFFF830, 0x6E0, 0x67E8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_DC9C)

    def lambda_DCB6():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_DCB6)
    WaitChrThread(0x19, 1)
    OP_6F(0x1)

    #C0605
    ChrTalk(
        0x18,
        "#1805F#11Pイリアさん……\x02",
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
            "なに、そんなに\x01",
            "午後の稽古が楽しみだったの？\x02\x03",

            "あたしもいいかげん、\x01",
            "舞台バカではあるけれど……\x02\x03",

            "あんたも十分、\x01",
            "素質あるんじゃないかしら？\x02",
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
            "#1809F#11Pあはは、そんな……\x02\x03",

            "イリアさんの域まで\x01",
            "達する自信なんてとても……\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x19,
        (
            "#6P#1704Fふふ、そんなこと言って\x01",
            "プレ公演じゃノリノリだったくせに。\x02\x03",

            "#1702F良かったわよ、あんたの演技。\x02\x03",

            "ようやくあたしのライバルの\x01",
            "卵くらいにはなってくれたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x18,
        (
            "#1802F#11Pイリアさん……\x02\x03",

            "#1804F……もしそうだとしたら\x01",
            "全部、イリアさんのおかげです。\x02\x03",

            "受け継いだ道しか知らなかった私に\x01",
            "光を示してくれた貴女の……\x02\x03",

            "#1802F……ふふ、それと今回は\x01",
            "彼らにも感謝した方がいいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x19,
        "#6P#1705Fへ……\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x18,
        (
            "#1804F#11Pふふっ、何でもないです。\x02\x03",

            "#1800F今日の稽古は、第三幕の\x01",
            "完成度を上げていくんですよね？\x02\x03",

            "私、頑張ってお付き合いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x19,
        (
            "#6P#1702Fお、やる気満々じゃないの。\x02\x03",

            "#1700Fうーん、あたしも\x01",
            "マジで負けてられないわね～。\x02\x03",

            "#1709Fよーし、来月の本公演までに\x01",
            "今の百倍は良くしていくわよ～！\x02\x03",

            "付いてきなさい、リーシャ！\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x18,
        "#1809F#11Pはい、イリアさん……！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E163")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E163")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E17D")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E17D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E197")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E197")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E1B1")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E1CB")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E1E5")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E1FF")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E219")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E219")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E239")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E274")

    label("loc_E239")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E259")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E274")

    label("loc_E259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E274")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E274")

    OP_29(0x41, 0x4, 0x10)
    OP_29(0x42, 0x4, 0x10)
    OP_29(0x43, 0x4, 0x10)
    OP_29(0x41, 0x4, 0x20)
    OP_29(0x43, 0x4, 0x20)
    SubItemNumber(0x325, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E2B0")
    OP_29(0xE, 0x4, 0x40)
    Jump("loc_E2C2")

    label("loc_E2B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2C2")
    OP_29(0xE, 0x4, 0x40)

    label("loc_E2C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2D4")
    OP_29(0x10, 0x4, 0x40)

    label("loc_E2D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E2F2")
    OP_29(0x11, 0x4, 0x40)
    Jump("loc_E304")

    label("loc_E2F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E304")
    OP_29(0x11, 0x4, 0x40)

    label("loc_E304")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E322")
    OP_29(0x12, 0x4, 0x40)
    Jump("loc_E334")

    label("loc_E322")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E334")
    OP_29(0x12, 0x4, 0x40)

    label("loc_E334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E352")
    OP_29(0x13, 0x4, 0x40)
    Jump("loc_E364")

    label("loc_E352")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E364")
    OP_29(0x13, 0x4, 0x40)

    label("loc_E364")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E382")
    OP_29(0x14, 0x4, 0x40)
    Jump("loc_E394")

    label("loc_E382")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E394")
    OP_29(0x14, 0x4, 0x40)

    label("loc_E394")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3B2")
    OP_29(0x15, 0x4, 0x40)
    Jump("loc_E3C4")

    label("loc_E3B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3C4")
    OP_29(0x15, 0x4, 0x40)

    label("loc_E3C4")

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

    # Function_49_D64D end

    def Function_50_E4A3(): pass

    label("Function_50_E4A3")

    BeginChrThread(0x19, 3, 0, 51)
    Sleep(100)
    BeginChrThread(0x18, 3, 0, 52)
    WaitChrThread(0x19, 3)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    WaitChrThread(0x18, 3)

    def lambda_E4DA():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E4DA)
    Sleep(50)

    def lambda_E4F7():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E4F7)
    Sleep(300)

    def lambda_E514():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_E514)
    Sleep(50)

    def lambda_E528():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_E528)
    Return()

    # Function_50_E4A3 end

    def Function_51_E535(): pass

    label("Function_51_E535")


    def lambda_E53A():
        OP_96(0xFE, 0xFFFFF63C, 0x6E0, 0x73A0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E53A)
    WaitChrThread(0x19, 1)

    def lambda_E558():
        OP_96(0xFE, 0xFFFFF63C, 0xA64, 0x8340, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E558)
    WaitChrThread(0x19, 1)
    Return()

    # Function_51_E535 end

    def Function_52_E572(): pass

    label("Function_52_E572")


    def lambda_E577():

        label("loc_E577")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_E577")

    QueueWorkItem2(0x18, 2, lambda_E577)

    def lambda_E589():
        OP_96(0xFE, 0xFFFFFA88, 0x6E0, 0x7080, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E589)
    WaitChrThread(0x18, 1)
    Sleep(600)
    EndChrThread(0x18, 0x2)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_E5B5():
        OP_95(0xFE, -1400, 2660, 32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E5B5)
    WaitChrThread(0x18, 1)
    Return()

    # Function_52_E572 end

    def Function_53_E5CF(): pass

    label("Function_53_E5CF")

    OP_A1(0xFE, 0x7D0, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_53_E5CF end

    def Function_54_E5E5(): pass

    label("Function_54_E5E5")

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

    def lambda_E766():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E766)
    Sleep(50)

    def lambda_E783():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E783)
    Sleep(50)

    def lambda_E7A0():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E7A0)
    Sleep(50)

    def lambda_E7BD():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E7BD)
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

    # Function_54_E5E5 end

    def Function_55_E800(): pass

    label("Function_55_E800")


    def lambda_E805():
        OP_95(0xFE, -26000, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E805)
    WaitChrThread(0xFE, 1)

    def lambda_E823():
        OP_95(0xFE, -26000, 300, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E823)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_E800 end

    def Function_56_E83D(): pass

    label("Function_56_E83D")


    def lambda_E842():
        OP_95(0xFE, -26000, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E842)
    WaitChrThread(0xFE, 1)

    def lambda_E860():
        OP_95(0xFE, -26000, 300, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E860)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_E83D end

    def Function_57_E87A(): pass

    label("Function_57_E87A")


    def lambda_E87F():
        OP_95(0xFE, -27200, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E87F)
    WaitChrThread(0xFE, 1)

    def lambda_E89D():
        OP_95(0xFE, -27200, 300, 16100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E89D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_E87A end

    def Function_58_E8B7(): pass

    label("Function_58_E8B7")


    def lambda_E8BC():
        OP_95(0xFE, -27200, 0, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E8BC)
    WaitChrThread(0xFE, 1)

    def lambda_E8DA():
        OP_95(0xFE, -27200, 300, 14600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E8DA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_E8B7 end

    def Function_59_E8F4(): pass

    label("Function_59_E8F4")

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
            "#0106F……まさか全員、\x01",
            "行方不明になってるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x104,
        (
            "#5P#0303F嫌な予感、的中だな……\x02\x03",

            "#0301F自発的に消えちまったのか、\x01",
            "それとも拉致されちまったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x103,
        (
            "#0206F現時点では情報が少なすぎて\x01",
            "どちらの可能性も考えられますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_EB7F")

    #C0617
    ChrTalk(
        0x101,
        (
            "#6P#0003F……失踪した５人については\x01",
            "氷山の一角かもしれない。\x02\x03",

            "#0001Fクロスベル市全体では\x01",
            "かなりの人数が失踪している\x01",
            "可能性が高そうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC0F")

    label("loc_EB7F")


    #C0618
    ChrTalk(
        0x101,
        (
            "#6P#0003F……失踪した４人については\x01",
            "氷山の一角かもしれない。\x02\x03",

            "#0001Fクロスベル市全体では\x01",
            "かなりの人数が失踪している\x01",
            "可能性が高そうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC0F")


    #C0619
    ChrTalk(
        0x102,
        (
            "#0108Fええ……\x01",
            "一体どれだけの人たちが\x01",
            "消えてしまったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x104,
        (
            "#5P#0301Fどうする、ロイド。\x02\x03",

            "一人一人を捜すってのは\x01",
            "さすがに難しそうだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……こちらの手が\x01",
            "圧倒的に不足している。\x02\x03",

            "#0008Fこうなると上からの圧力で\x01",
            "一課が動けないのが痛いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x103,
        (
            "#0202Fでしたら二課のドノバン警部に\x01",
            "相談してみてはどうでしょう？\x02\x03",

            "以前、手伝った貸しもありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや……難しいと思う。\x02\x03",

            "#0001Fダドリー捜査官がわざわざ、\x01",
            "支援課を頼ってきている以上、\x01",
            "二課にも圧力が掛かっているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x103,
        "#0206Fなるほど……確かに。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x102,
        (
            "#0108Fとなると広域防犯課も\x01",
            "状況は同じでしょうね……\x02\x03",

            "#0106F警官隊のマンパワーが使えれば\x01",
            "すごく助かるのだけど……\x02",
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

    def lambda_EEF5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EEF5)
    Sleep(50)

    def lambda_EF05():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EF05)
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
            "#0001Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0627
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おい、新米ども……！\x02\x03",

            "まさか何かしでかしたんじゃ\x01",
            "ないだろうな……！？\x02",
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
            "#0011Fへ……\x02\x03",

            "#0001Fもしかしてその声は\x01",
            "ダドリー捜査官ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もしかしても何もない！\x02\x03",

            "お前たち、ルバーチェに何か\x01",
            "ちょっかいをかけなかったか！？\x02",
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
            "#0005Fい、いえ別に……\x02\x03",

            "#0003F現在は薬物捜査の方に\x01",
            "専念していますから。\x02\x03",

            "#0001F……何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0631
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あったも何も！\x01",
            "連中の事務所が……\x02\x03",

            "……ゴホン、何でもない。\x02\x03",

            "何もしてないなら構わん。\x01",
            "そのまま捜査を続けていろ。\x02",
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
            "#0005Fあ……\x02",
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
            "#0101Fダドリー捜査官から？\x01",
            "何かあったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        "#6P#0006Fいや……\x02",
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
            "ロイドはエリィたちに\x01",
            "ダドリーとのやり取りを伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0637
    ChrTalk(
        0x104,
        "#5P#0301Fなんだそりゃ……\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x103,
        (
            "#0206F……露骨に怪しいですね。\x02\x03",

            "#0201Fルバーチェ商会で\x01",
            "何かあったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x101,
        "#6P#0003F可能性は高そうだな……\x02",
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
            "#5P#0300Fこりゃ、行ってみるしか\x01",
            "ねえんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x102,
        (
            "#0103Fそうね……抗争には関わるなって\x01",
            "釘は刺されているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x103,
        (
            "#0202F失踪者にマフィアが絡んでいるなら\x01",
            "大義名分は立つのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#6P#0001Fああ……\x01",
            "ルバーチェ商会に急ごう！\x02",
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

    # Function_59_E8F4 end

    def Function_60_F541(): pass

    label("Function_60_F541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5B7")
    EventBegin(0x1)

    #C0644
    ChrTalk(
        0x101,
        (
            "#0000Fここは関係者以外\x01",
            "立ち入り禁止みたいだ……\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_F5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F62D")
    EventBegin(0x1)

    #C0645
    ChrTalk(
        0x101,
        (
            "#0000Fここは関係者以外\x01",
            "立ち入り禁止みたいだ……\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_F62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F69B")
    EventBegin(0x1)
    SetChrName("")

    #A0646
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アルカンシェルは公演中のようだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_F69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F812")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7BD")

    #C0647
    ChrTalk(
        0x13D,
        (
            "#2105Fあれ、アルカンシェルに\x01",
            "入っちゃうの？\x02\x03",

            "#2109F……いいわねソレ！！\x01",
            "イリア・プラティエと繋がりがある\x01",
            "キミ達なら行ける！\x02\x03",

            "さあ、突撃するわよ～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x101,
        "#0006F何を煽ってるんですか……\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x102,
        (
            "#0101F今はカジノに急ぎましょう。\x01",
            "町長さんの話が気になるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_F7FC")

    label("loc_F7BD")


    #C0650
    ChrTalk(
        0x101,
        (
            "#0001Fビクセン町長の話が気になる……\x01",
            "今はカジノへ急ごう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F7FC")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_F812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F880")
    EventBegin(0x1)
    SetChrName("")

    #A0651
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アルカンシェルは公演中のようだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_F880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9D3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F975")

    #C0652
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……アルカンシェルは\x01",
            "今は公演中だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x104,
        (
            "#0304F舞台の事は舞台のプロに\x01",
            "任せておけば大丈夫だろ。\x02\x03",

            "#0300F俺たちは俺たちの\x01",
            "すべき事をしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな、今は\x01",
            "ウルスラ病院へ急ごう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_F9BD")

    label("loc_F975")

    SetChrName("")

    #A0655
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アルカンシェルは公演中のようだ。\x01",
            "今はウルスラ病院へ急ごう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F9BD")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)

    label("loc_F9D3")

    Return()

    # Function_60_F541 end

    def Function_61_F9D4(): pass

    label("Function_61_F9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC06")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB35")

    #C0656
    ChrTalk(
        0x103,
        "#0200Fここは……カジノのようですね。\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x104,
        (
            "#0300Fカジノハウス《バルカ》──\x01",
            "俺の行きつけの店だぜ。\x02\x03",

            "#0309Fうっし、着任祝いに\x01",
            "みんなで一勝負してくるか！\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x102,
        (
            "#0111Fそれは駄目でしょう。\x01",
            "常識的に考えて。\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0x104,
        "#0306Fオイオイ、そりゃないぜ！？\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x101,
        (
            "#0003F……まあ　今日は\x01",
            "研修中みたいなものだし。\x01",
            "悪いけど我慢してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 5)
    Jump("loc_FBF0")

    label("loc_FB35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBB0")

    #C0661
    ChrTalk(
        0x104,
        "#0300F……今日の席は、と。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x101,
        "#0000Fえっとランディ、ダメだぞ？\x02",
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x104,
        "#0301Fチッ、お堅い連中だぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FBF0")

    label("loc_FBB0")

    SetChrName("")

    #A0664
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カジノハウスのようだ。\x01",
            "……今日は入らないでおこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FBF0")

    Sleep(50)
    SetChrPos(0x0, -26500, 300, 15360, 175)
    EventEnd(0x4)

    label("loc_FC06")

    Return()

    # Function_61_F9D4 end

    def Function_62_FC07(): pass

    label("Function_62_FC07")

    EventBegin(0x1)
    Call(0, 64)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_62_FC07 end

    def Function_63_FC23(): pass

    label("Function_63_FC23")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 64)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_63_FC23 end

    def Function_64_FC3F(): pass

    label("Function_64_FC3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FCCA")

    #C0665
    ChrTalk(
        0x101,
        (
            "#0006F今日はさすがに疲れたな……\x01",
            "寄り道せずに支援課に帰ろう。\x02\x03",

            "#0000Fここからなら裏通りを使うのが\x01",
            "一番早いはずだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD17")

    label("loc_FCCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD17")

    #C0666
    ChrTalk(
        0x101,
        (
            "#0001Fビクセン町長の話が気になる……\x01",
            "今はカジノへ急ごう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD17")

    Return()

    # Function_64_FC3F end

    SaveToFile()

Try(main)
