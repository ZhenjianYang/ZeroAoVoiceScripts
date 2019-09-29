from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c140c.bin",                # FileName
        "c140c",                    # MapName
        "c140c",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 3, 0, 4],
    )

    BuildStringList((
        "c140c",                  # 0
        "迪诺",                   # 1
        "帕欧拉婆婆",             # 2
        "王",                     # 3
        "露茜",                   # 4
        "卡农",                   # 5
        "修伊",                   # 6
        "寇奇",                   # 7
        "琴兹",                   # 8
        "贝赛",                   # 9
        "柯洛娜",                 # 10
        "利玛",                   # 11
        "梅尔斯",                 # 12
        "游客",                   # 13
        "游客",                   # 14
        "艾丝蒂尔",               # 15
        "约修亚",                 # 16
        "瓦吉",                   # 17
        "瓦鲁多",                 # 18
        "阿巴斯",                 # 19
        "格蕾丝",                 # 20
        "摄影师",                 # 21
        "剑蛇帮成员",             # 22
        "剑蛇帮成员",             # 23
        "剑蛇帮成员",             # 24
        "剑蛇帮成员",             # 25
        "剑蛇帮成员",             # 26
        "圣书会成员",             # 27
        "圣书会成员",             # 28
        "圣书会成员",             # 29
        "圣书会成员",             # 30
        "事件用坦特斯老人",       # 31
        "事件用盖特纳",           # 32
        "事件用游客",             # 33
        "事件用游客",             # 34
        "罗伊德",                 # 35
        "兰迪",                   # 36
        "艾莉",                   # 37
        "缇欧",                   # 38
        "Objects用",              # 39
        "中央广场",               # 40
        "西街",                   # 41
        "行政区",                 # 42
        "住宅街",                 # 43
        "欢乐街",                 # 44
        "东街",                   # 45
        "旧城区",                 # 46
        "港湾区",                 # 47
        "ＩＢＣ",                 # 48
        "站前街道",               # 49
        "后巷",                   # 50
        "乌尔斯拉间道",           # 51
        "东克洛斯贝尔街道",       # 52
        "西克洛斯贝尔街道",       # 53
        "玛因兹山道",             # 54
    ))

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch23700.itc",                   # 09
        "chr/ch23600.itc",                   # 0A
        "chr/ch31800.itc",                   # 0B
        "chr/ch30900.itc",                   # 0C
        "chr/ch30800.itc",                   # 0D
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(2339,    0,       -2940,   315,  405,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(43650,   -2500,   -19120,  135,  389,  0x0, 0,   13,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-140,    0,       3740,    135,  405,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(920,     0,       2680,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(9449,    0,       3140,    0,    277,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8350,    0,       4110,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9560,    0,       4400,    225,  261,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-19489,  0,       -9409,   0,    261,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(1950,    0,       140,     180,  261,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  5,  0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  81, 0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西街")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "东街")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧城区")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "站前街道")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "后巷")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_8E4",          # 00, 0
        "Function_1_99C",          # 01, 1
        "Function_2_9C7",          # 02, 2
        "Function_3_AA0",          # 03, 3
        "Function_4_DFE",          # 04, 4
        "Function_5_E70",          # 05, 5
        "Function_6_FA6",          # 06, 6
        "Function_7_1240",         # 07, 7
        "Function_8_1514",         # 08, 8
        "Function_9_16FF",         # 09, 9
        "Function_10_179B",        # 0A, 10
        "Function_11_1835",        # 0B, 11
        "Function_12_19FF",        # 0C, 12
        "Function_13_1EE4",        # 0D, 13
        "Function_14_1EEE",        # 0E, 14
        "Function_15_204D",        # 0F, 15
        "Function_16_2154",        # 10, 16
        "Function_17_21DF",        # 11, 17
        "Function_18_22E6",        # 12, 18
        "Function_19_23C8",        # 13, 19
        "Function_20_2533",        # 14, 20
        "Function_21_26B0",        # 15, 21
        "Function_22_274B",        # 16, 22
        "Function_23_2951",        # 17, 23
        "Function_24_29E2",        # 18, 24
        "Function_25_2B6C",        # 19, 25
        "Function_26_4ECA",        # 1A, 26
        "Function_27_4F58",        # 1B, 27
        "Function_28_4FC0",        # 1C, 28
        "Function_29_5052",        # 1D, 29
        "Function_30_50BE",        # 1E, 30
        "Function_31_5161",        # 1F, 31
        "Function_32_51DE",        # 20, 32
        "Function_33_5291",        # 21, 33
        "Function_34_530B",        # 22, 34
        "Function_35_535D",        # 23, 35
        "Function_36_53AF",        # 24, 36
        "Function_37_53DC",        # 25, 37
        "Function_38_5420",        # 26, 38
        "Function_39_548A",        # 27, 39
        "Function_40_550D",        # 28, 40
        "Function_41_555B",        # 29, 41
        "Function_42_55A9",        # 2A, 42
        "Function_43_55DA",        # 2B, 43
        "Function_44_562D",        # 2C, 44
        "Function_45_5773",        # 2D, 45
        "Function_46_5836",        # 2E, 46
        "Function_47_5884",        # 2F, 47
        "Function_48_58D2",        # 30, 48
        "Function_49_5924",        # 31, 49
        "Function_50_5981",        # 32, 50
        "Function_51_5A2D",        # 33, 51
        "Function_52_5A79",        # 34, 52
        "Function_53_5AE4",        # 35, 53
        "Function_54_5B52",        # 36, 54
        "Function_55_5BAF",        # 37, 55
        "Function_56_5BCF",        # 38, 56
        "Function_57_5C29",        # 39, 57
        "Function_58_5C84",        # 3A, 58
        "Function_59_5CC1",        # 3B, 59
        "Function_60_5D4A",        # 3C, 60
        "Function_61_5DD9",        # 3D, 61
        "Function_62_5E68",        # 3E, 62
        "Function_63_5EF1",        # 3F, 63
        "Function_64_5F21",        # 40, 64
        "Function_65_5FD3",        # 41, 65
        "Function_66_61BE",        # 42, 66
        "Function_67_629E",        # 43, 67
        "Function_68_62AB",        # 44, 68
        "Function_69_62B6",        # 45, 69
        "Function_70_62C1",        # 46, 70
        "Function_71_62CB",        # 47, 71
        "Function_72_ADA2",        # 48, 72
        "Function_73_AEB1",        # 49, 73
        "Function_74_AEE4",        # 4A, 74
        "Function_75_AF17",        # 4B, 75
        "Function_76_AF33",        # 4C, 76
        "Function_77_AF4F",        # 4D, 77
        "Function_78_AF7B",        # 4E, 78
        "Function_79_AFA7",        # 4F, 79
        "Function_80_B034",        # 50, 80
        "Function_81_E1DE",        # 51, 81
    ))


    def Function_0_8E4(): pass

    label("Function_0_8E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_924"),
        (1, "loc_930"),
        (2, "loc_93C"),
        (3, "loc_948"),
        (4, "loc_954"),
        (5, "loc_960"),
        (6, "loc_96C"),
        (SWITCH_DEFAULT, "loc_978"),
    )


    label("loc_924")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_930")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_93C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_948")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_954")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_960")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_96C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_978")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_984")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_984")

    label("loc_99B")

    Return()

    # Function_0_8E4 end

    def Function_1_99C(): pass

    label("Function_1_99C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C6")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_99C")

    label("loc_9C6")

    Return()

    # Function_1_99C end

    def Function_2_9C7(): pass

    label("Function_2_9C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9F")
    OP_95(0xFE, 5840, 0, -6890, 5000, 0x0)
    OP_95(0xFE, 13450, -1420, -18510, 5000, 0x0)
    OP_95(0xFE, 21750, -2500, -24790, 5000, 0x0)
    OP_95(0xFE, 21750, -6500, -38390, 5000, 0x0)
    OP_95(0xFE, 7790, -6320, -37990, 5000, 0x0)
    OP_95(0xFE, -3730, -3830, -27600, 5000, 0x0)
    OP_95(0xFE, -12250, -3030, -23600, 5000, 0x0)
    OP_95(0xFE, -12250, 0, -12120, 5000, 0x0)
    OP_95(0xFE, -10970, 0, -11360, 5000, 0x0)
    OP_95(0xFE, -5510, 0, -7900, 5000, 0x0)
    Jump("Function_2_9C7")

    label("loc_A9F")

    Return()

    # Function_2_9C7 end

    def Function_3_AA0(): pass

    label("Function_3_AA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7D")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B27")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_B46")

    label("loc_B27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B46")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_B46")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7D")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B9A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)
    Jump("loc_BBD")

    label("loc_B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_BAE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 71)
    Jump("loc_BBD")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_BBD")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 80)

    label("loc_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C71")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, 4620, 0, -5320, 315)
    SetChrPos(0xF, 1100, 0, -1620, 135)
    SetChrPos(0x10, -310, 50, -1500, 135)
    SetChrPos(0xE, 44880, -2500, -20090, 225)
    OP_93(0x11, 0xE1, 0x0)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_DFD")

    label("loc_C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_CB5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrPos(0xA, 1810, 0, 4550, 315)
    SetChrPos(0xB, 610, 0, 5750, 135)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_DFD")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_CEF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_DFD")

    label("loc_CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_DA3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 4670, 0, -5500, 180)
    SetChrPos(0xB, 4710, 0, -7160, 0)
    SetChrPos(0x14, 43330, -2500, -20060, 90)
    SetChrPos(0x15, 42420, -2500, -19200, 135)
    OP_93(0x8, 0x10E, 0x0)
    TurnDirection(0x13, 0x12, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7C")
    SetChrFlags(0x8, 0x10)

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D8F")
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)

    label("loc_D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9E")
    SetChrFlags(0x12, 0x10)

    label("loc_D9E")

    Jump("loc_DFD")

    label("loc_DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_DC7")
    SetChrPos(0x15, -18810, 0, -10220, 315)
    SetChrFlags(0x8, 0x80)
    Jump("loc_DFD")

    label("loc_DC7")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 2740, 0, -770, 315)
    SetChrPos(0xB, 960, 0, 870, 135)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_DFD")

    Return()

    # Function_3_AA0 end

    def Function_4_DFE(): pass

    label("Function_4_DFE")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4D")
    OP_70(0x7, 0x0)
    Jump("loc_E51")

    label("loc_E4D")

    OP_70(0x7, 0x1E)

    label("loc_E51")

    OP_65(0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_E6F")

    Return()

    # Function_4_DFE end

    def Function_5_E70(): pass

    label("Function_5_E70")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5D")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_EEF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_F58")

    label("loc_EEF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F58")

    Jump("loc_F9A")

    label("loc_F5D")

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

    label("loc_F9A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E70 end

    def Function_6_FA6(): pass

    label("Function_6_FA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1023")

    #C0004
    ChrTalk(
        0x8,
        (
            "啊哇哇……竟然要在这种地方\x01",
            "和圣书会的家伙们……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "开、开战吗！？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "我、我……\x01",
            "该怎么办才好啊！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123C")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1071")

    #C0007
    ChrTalk(
        0x8,
        (
            "今天的游客\x01",
            "也是络绎不绝啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "真是的，好碍事！\x02",
    )

    CloseMessageWindow()
    Jump("loc_10AF")

    label("loc_1071")

    OP_4B(0x14, 0xFF)

    #C0009
    ChrTalk(
        0x8,
        "喂，这里没什么可参观的！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "到那边去！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x14, 0xFF)

    label("loc_10AF")

    Jump("loc_123C")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1120")

    #C0011
    ChrTalk(
        0x8,
        (
            "瓦鲁多大哥他们\x01",
            "都要出去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "呜呜～之前问他的时候，\x01",
            "还一副毫无兴趣的样子呢，结果……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123C")

    label("loc_1120")


    #C0013
    ChrTalk(
        0x8,
        (
            "瓦鲁多大哥他们\x01",
            "都要出去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "大家都沉迷于庆典之中，\x01",
            "每年都会逛那些露天店……\x02",
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

    #C0015
    ChrTalk(
        0x102,
        (
            "#0106F所、所以他们就\x01",
            "是让你来负责留守吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "这也是没办法的吧！\x01",
            "谁让我是地位最低的成员！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_123C")

    TalkEnd(0xFE)
    Return()

    # Function_6_FA6 end

    def Function_7_1240(): pass

    label("Function_7_1240")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12D4")
    Jump("loc_131E")

    label("loc_12D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131E")

    label("loc_12F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1314")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131E")

    label("loc_1314")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_131E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_136B")

    #C0017
    ChrTalk(
        0x9,
        "啊呀，又要打起来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_150C")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_13C1")

    #C0018
    ChrTalk(
        0x9,
        (
            "游行队伍好像\x01",
            "相当绚丽华美呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "那么，今天去吃点\x01",
            "什么美食好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150C")

    label("loc_13C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_143A")

    #C0020
    ChrTalk(
        0x9,
        (
            "我的腿脚不太好，\x01",
            "不能往人群里挤。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "不过我并不在意。\x01",
            "每年的游行活动，\x01",
            "光是听音乐就足够让人开心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150C")

    label("loc_143A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14A4")

    #C0022
    ChrTalk(
        0x9,
        (
            "旧城区这边也有很多\x01",
            "观光的人蜂涌而至呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "呵呵，这里似乎也热闹起来了，\x01",
            "我很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_150C")

    label("loc_14A4")


    #C0024
    ChrTalk(
        0x9,
        (
            "好漂亮的彩纸屑啊……\x01",
            "每年的纪念庆典都是这么激动人心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "光是在一边看着，\x01",
            "就已经觉得很快乐了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1240 end

    def Function_8_1514(): pass

    label("Function_8_1514")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1579")

    #C0026
    ChrTalk(
        0xA,
        (
            "我叫醒了老爸，\x01",
            "然后从他那里骗了些米拉。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "嘻嘻……今天\x01",
            "就去吃点好吃的吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FB")

    label("loc_1579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_15DF")

    #C0028
    ChrTalk(
        0xA,
        (
            "嘁，这么多人，\x01",
            "根本看不清楚啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "游行这种东西\x01",
            "果然没意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        "看了就不爽。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16FB")

    label("loc_15DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_162F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1627")

    #C0031
    ChrTalk(
        0xA,
        (
            "我老爸今天也喝得东倒西歪，\x01",
            "我们自己去吧～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162A")

    label("loc_1627")

    Call(0, 9)

    label("loc_162A")

    Jump("loc_16FB")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_168A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1682")

    #C0032
    ChrTalk(
        0xA,
        "喝呀～！放马过来吧～！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        "看我用必杀战技把你收拾掉！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_1682")

    Call(0, 10)

    label("loc_1685")

    Jump("loc_16FB")

    label("loc_168A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_16C5")

    #C0034
    ChrTalk(
        0xA,
        (
            "不良团伙的哥哥们\x01",
            "好像去别的地方了呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FB")

    label("loc_16C5")

    OP_4B(0x15, 0xFF)

    #C0035
    ChrTalk(
        0xA,
        "是游客啊～！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "喂，给点好处怎么样啊！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)

    label("loc_16FB")

    TalkEnd(0xFE)
    Return()

    # Function_8_1514 end

    def Function_9_16FF(): pass

    label("Function_9_16FF")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0037
    ChrTalk(
        0xA,
        "露茜，听说了吗？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "游行的队伍\x01",
            "快要到东街那边了呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        "油杏～？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        "那是什么啊～好吃吗～？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        "笨蛋～不是吃的东西啦～\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_16FF end

    def Function_10_179B(): pass

    label("Function_10_179B")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0042
    ChrTalk(
        0xA,
        "喝呀～！放马过来～！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "看我用必杀战技\x01",
            "来将你了结！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "嘻嘻……那么，\x01",
            "我就是游击士大姐姐哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        "要上了，奥义·太极轮……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_179B end

    def Function_11_1835(): pass

    label("Function_11_1835")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1869")

    #C0046
    ChrTalk(
        0xB,
        (
            "呀哈哈哈！\x01",
            "今天要玩个痛快啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_1869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_18B9")

    #C0047
    ChrTalk(
        0xB,
        (
            "撞到了大人身上，\x01",
            "头好疼啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "不过有些好玩呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_18B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_190F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1907")

    #C0049
    ChrTalk(
        0xB,
        "油杏是什么啊～？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "是食物吗？好吃吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_1907")

    Call(0, 9)

    label("loc_190A")

    Jump("loc_19FB")

    label("loc_190F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_197B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1973")

    #C0051
    ChrTalk(
        0xB,
        (
            "嘻嘻……那么，\x01",
            "我就是游击士的大姐姐哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        "要上了，奥义·太极轮……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1976")

    label("loc_1973")

    Call(0, 10)

    label("loc_1976")

    Jump("loc_19FB")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_19C0")

    #C0053
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "我要到了棉花糖哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        "和王平均分好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_19C0")


    #C0055
    ChrTalk(
        0xB,
        "是游客！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "不给点好处的话，\x01",
            "我可就要恶作剧了哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FB")

    TalkEnd(0xFE)
    Return()

    # Function_11_1835 end

    def Function_12_19FF(): pass

    label("Function_12_19FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A79")

    #C0057
    ChrTalk(
        0xC,
        (
            "今天早上，有只很漂亮的鸟\x01",
            "从天空的东方飞过哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xC,
        (
            "呵呵，希望这预示着\x01",
            "幸福也会去造访你们！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF1")

    label("loc_1A79")


    #C0059
    ChrTalk(
        0xC,
        (
            "今天早上，有只很漂亮的鸟\x01",
            "从天空的东方飞过哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xC,
        "呵呵，总觉得自己很有眼福呢。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        "希望今天也是美好的一天啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1AF1")

    Jump("loc_1EE0")

    label("loc_1AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B71")

    #C0062
    ChrTalk(
        0xC,
        "呼，今天也要努力做扫除啊。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        "明天早上也要早起……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "必须要在天黑之前回家，\x01",
            "香香甜甜地睡上一觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE0")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1BC9")

    #C0065
    ChrTalk(
        0xC,
        "（沙沙，沙沙……）\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "彩纸屑真是漂亮啊，\x01",
            "就像在下雪一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1BC9")


    #C0067
    ChrTalk(
        0xC,
        "（沙沙，沙沙……）\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "彩纸屑越积越多，\x01",
            "最近，扫除工作也增多了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "不过，彩纸屑很漂亮，真令人愉快呢。\x01",
            "看起来就像是在下雪一样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1C56")

    Jump("loc_1EE0")

    label("loc_1C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1CC9")

    #C0070
    ChrTalk(
        0xC,
        "噢噢，我可要赶快收拾干净了。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "真希望不要出现打架斗殴\x01",
            "那种令人难过的事情啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE1")

    label("loc_1CC9")


    #C0072
    ChrTalk(
        0xC,
        (
            "我不在的时候，\x01",
            "好像又有人在这里胡闹呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        "噢噢，我可要赶快收拾干净了。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "这一带也都被人弄得\x01",
            "乱七八糟呢……\x02",
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

    #C0075
    ChrTalk(
        0x101,
        "#0006F真、真对不起……\x02",
    )


    #C0076
    ChrTalk(
        0x104,
        "#0306F#6P真、真是抱歉……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1DE1")

    Jump("loc_1EE0")

    label("loc_1DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E56")

    #C0077
    ChrTalk(
        0xC,
        (
            "只要把这一带打扫干净，\x01",
            "游客们的心情也会变好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        (
            "在纪念庆典期间，\x01",
            "我一定要努力做好扫除！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE0")

    label("loc_1E56")


    #C0079
    ChrTalk(
        0xC,
        (
            "啊，你们也要来\x01",
            "帮我收拾垃圾吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xC,
        (
            "只要把这一带打扫干净，\x01",
            "游客们的心情也会变好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "只要大家都能玩得高兴，\x01",
            "我也会很开心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1EE0")

    TalkEnd(0xFE)
    Return()

    # Function_12_19FF end

    def Function_13_1EE4(): pass

    label("Function_13_1EE4")

    TalkBegin(0xFE)
    Call(0, 14)
    TalkEnd(0xFE)
    Return()

    # Function_13_1EE4 end

    def Function_14_1EEE(): pass

    label("Function_14_1EEE")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0082
    ChrTalk(
        0xD,
        (
            "这里从什么时候开始\x01",
            "变成你们的地盘了？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xD,
        "也太得意忘形了吧，混蛋们！！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xF,
        "是我们先从这里过的。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xF,
        "你们才是，最好搞清楚自己几斤几两啊！\x02",
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

    #C0086
    ChrTalk(
        0x102,
        "#0106F又开始争吵了，真是不知悔改……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0003F好了好了，忍耐一下。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_14_1EEE end

    def Function_15_204D(): pass

    label("Function_15_204D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20AA")

    #C0088
    ChrTalk(
        0xE,
        "看守的工作就由我来负责。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xE,
        (
            "只要迪诺今天能\x01",
            "玩得开心就好啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E8")

    label("loc_20AA")


    #C0090
    ChrTalk(
        0xE,
        (
            "今天要代替\x01",
            "迪诺看大门。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xE,
        "嘿，这也是前辈的责任啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20E8")

    Jump("loc_2150")

    label("loc_20ED")

    OP_4B(0xE, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0092
    ChrTalk(
        0xE,
        "我差不多也该走了。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xE,
        (
            "迪诺，加油啊！\x01",
            "不要觉得太寂寞哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        "知、知道了！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_2150")

    TalkEnd(0xFE)
    Return()

    # Function_15_204D end

    def Function_16_2154(): pass

    label("Function_16_2154")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2168")
    Call(0, 14)
    Jump("loc_21DB")

    label("loc_2168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_21D8")

    #C0095
    ChrTalk(
        0xF,
        (
            "我家里有剧团的门票呢，\x01",
            "最终日就出去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xF,
        (
            "哼……途中最好不要遇到\x01",
            "剑蛇帮的那些家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DB")

    label("loc_21D8")

    Call(0, 17)

    label("loc_21DB")

    TalkEnd(0xFE)
    Return()

    # Function_16_2154 end

    def Function_17_21DF(): pass

    label("Function_17_21DF")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0097
    ChrTalk(
        0x10,
        (
            "竟、竟然有彩虹剧团的票，\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xF,
        (
            "遗憾的是，并不是今天的票，\x01",
            "而是纪念庆典最终日的。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xF,
        (
            "……而且，这还是老爸\x01",
            "丢给我的，总有点不爽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x10,
        (
            "不、不要那么说啊，\x01",
            "我可是很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "那，最终日的时候\x01",
            "咱们两人一起去看吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_17_21DF end

    def Function_18_22E6(): pass

    label("Function_18_22E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2341")

    #C0102
    ChrTalk(
        0x10,
        (
            "剑、剑蛇帮的那些家伙\x01",
            "来找麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x10,
        (
            "这、这时候就、就要\x01",
            "迎头而上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C4")

    label("loc_2341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_23C1")

    #C0104
    ChrTalk(
        0x10,
        "琴兹的家里很有钱。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x10,
        (
            "他、他的父亲是\x01",
            "乌尔斯拉医院的有名医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x10,
        (
            "……总、总之交了个\x01",
            "好朋友，真是走运啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C4")

    label("loc_23C1")

    Call(0, 17)

    label("loc_23C4")

    TalkEnd(0xFE)
    Return()

    # Function_18_22E6 end

    def Function_19_23C8(): pass

    label("Function_19_23C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2424")

    #C0107
    ChrTalk(
        0x11,
        "啊呀，真让人头痛……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        (
            "不过，现在大概还是不要\x01",
            "勉强过去比较好吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252F")

    label("loc_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2477")

    #C0109
    ChrTalk(
        0x11,
        "呵呵，女儿也很开心的。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x11,
        (
            "今年能和家人一起逛庆典\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252F")

    label("loc_2477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_24C4")
    OP_4B(0x12, 0xFF)

    #C0111
    ChrTalk(
        0x11,
        (
            "利玛，握紧我的手啊。\x01",
            "一定不能从我们的身边离开哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_252F")

    label("loc_24C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_250D")
    OP_4B(0x13, 0xFF)

    #C0112
    ChrTalk(
        0x11,
        (
            "老公，今天就\x01",
            "少走一点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x11,
        "利玛还很小呢。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    Jump("loc_252F")

    label("loc_250D")

    OP_4B(0x13, 0xFF)

    #C0114
    ChrTalk(
        0x11,
        "老公，要去哪里玩呢？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_252F")

    TalkEnd(0xFE)
    Return()

    # Function_19_23C8 end

    def Function_20_2533(): pass

    label("Function_20_2533")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2572")
    OP_4B(0x13, 0xFF)

    #C0115
    ChrTalk(
        0x12,
        "爸爸，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x12,
        "快点走吧～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    Jump("loc_26AC")

    label("loc_2572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25B9")

    #C0117
    ChrTalk(
        0x12,
        (
            "很多闪闪发光的车子～\x01",
            "慢慢开过去了！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x12,
        "真棒啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_26AC")

    label("loc_25B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_260E")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0119
    ChrTalk(
        0x12,
        (
            "那个那个，为什么从天上\x01",
            "飘下花瓣来了呢～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Jump("loc_26AC")

    label("loc_260E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_266B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2663")

    #C0120
    ChrTalk(
        0x12,
        "利玛去哪里都可以哦～\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x12,
        "只要和爸爸在一起，去哪里都好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2666")

    label("loc_2663")

    Call(0, 21)

    label("loc_2666")

    Jump("loc_26AC")

    label("loc_266B")


    #C0122
    ChrTalk(
        0x12,
        (
            "今天和爸爸妈妈\x01",
            "一起玩！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)

    #C0123
    ChrTalk(
        0x12,
        "哇～！\x02",
    )

    CloseMessageWindow()

    label("loc_26AC")

    TalkEnd(0xFE)
    Return()

    # Function_20_2533 end

    def Function_21_26B0(): pass

    label("Function_21_26B0")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0124
    ChrTalk(
        0x13,
        (
            "利玛，今天想去\x01",
            "哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)

    #C0125
    ChrTalk(
        0x12,
        "这个嘛～那里！\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0126
    ChrTalk(
        0x13,
        "那里是……郊外的方向啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_21_26B0 end

    def Function_22_274B(): pass

    label("Function_22_274B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27A5")

    #C0127
    ChrTalk(
        0x13,
        (
            "我们正要出门呢，\x01",
            "就看到那些不良少年在争吵……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x13,
        "真令人头疼啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_27A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_27FC")

    #C0129
    ChrTalk(
        0x13,
        "游行是可以免费观看的……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x13,
        (
            "真是为全家出游量身定做的\x01",
            "精彩活动啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_27FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2878")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0131
    ChrTalk(
        0x13,
        (
            "没关系，游行队伍会从\x01",
            "大街巡回而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x13,
        (
            "东街是最后一站，\x01",
            "所以还有得是时间啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Jump("loc_294D")

    label("loc_2878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28D4")
    OP_4B(0x12, 0xFF)

    #C0133
    ChrTalk(
        0x13,
        (
            "利玛，今天去\x01",
            "东街逛逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x13,
        "露天市场一定很有趣呢～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_28D7")

    label("loc_28D4")

    Call(0, 21)

    label("loc_28D7")

    Jump("loc_294D")

    label("loc_28DC")


    #C0135
    ChrTalk(
        0x13,
        (
            "平时一天到晚都在工作……\x01",
            "总是让女儿\x01",
            "感到很孤单呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x13,
        (
            "好，今天就一起玩个够吧。\x01",
            "把以前的份全都补玩回来～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294D")

    TalkEnd(0xFE)
    Return()

    # Function_22_274B end

    def Function_23_2951(): pass

    label("Function_23_2951")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_299A")
    OP_4B(0x8, 0xFF)

    #C0137
    ChrTalk(
        0x14,
        "哎，这里是什么地方～\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x14,
        "我在做什么呢～？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_29DE")

    label("loc_299A")


    #C0139
    ChrTalk(
        0x14,
        (
            "本来想来这里\x01",
            "的酒吧看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x14,
        (
            "但今天居然临时休业，\x01",
            "好无聊啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29DE")

    TalkEnd(0xFE)
    Return()

    # Function_23_2951 end

    def Function_24_29E2(): pass

    label("Function_24_29E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A3C")
    OP_4B(0x14, 0xFF)

    #C0141
    ChrTalk(
        0x15,
        "喂喂，这里很危险吧？\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x15,
        (
            "和旧城区的家伙\x01",
            "扯上关系可没好事。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_2B68")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_2AA7")

    #C0143
    ChrTalk(
        0x15,
        (
            "我早就说过，\x01",
            "旧城区这种地方\x01",
            "根本就不用来……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x15,
        (
            "想享受庆典的话，\x01",
            "在繁华区玩就可以啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B68")

    label("loc_2AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2B05")

    #C0145
    ChrTalk(
        0x15,
        (
            "你有没有在这附近\x01",
            "看到我的女人啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x15,
        (
            "那家伙竟然一个人\x01",
            "跑进旧城区了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B68")

    label("loc_2B05")


    #C0147
    ChrTalk(
        0x15,
        (
            "哇啊……被一些奇怪的小鬼们\x01",
            "纠缠住了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x15,
        (
            "可恶，而且还和她走丢了……\x01",
            "今天真是倒霉日啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2B68")

    TalkEnd(0xFE)
    Return()

    # Function_24_29E2 end

    def Function_25_2B6C(): pass

    label("Function_25_2B6C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00000.itc", 0x2D)
    LoadChrToIndex("chr/ch00100.itc", 0x2E)
    LoadChrToIndex("chr/ch00200.itc", 0x2F)
    LoadChrToIndex("chr/ch00300.itc", 0x30)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch21000.itc", 0x24)
    LoadChrToIndex("chr/ch24500.itc", 0x25)
    LoadChrToIndex("chr/ch21300.itc", 0x26)
    ClearMapObjFlags(0x8, 0x20)
    ClearMapObjFlags(0x8, 0x4)
    OP_70(0x8, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xA, 9150, 0, -7800, 275)
    SetChrPos(0xB, 9350, 0, -8700, 275)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x14, 8000, 0, -12000, 310)
    SetChrPos(0x15, 8600, 0, -11200, 310)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x26, 12000, 0, -5900, 270)
    SetChrPos(0x27, 11700, 0, -4750, 270)
    SetChrChipByIndex(0x28, 0x25)
    SetChrSubChip(0x28, 0x0)
    SetChrChipByIndex(0x29, 0x26)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x28, 7500, 0, 400, 230)
    SetChrPos(0x29, 8050, 0, -400, 230)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x2D)
    SetChrChipByIndex(0x2B, 0x30)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrChipByIndex(0x2D, 0x2F)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrPos(0x2B, 1820, 0, -7540, 359)
    SetChrPos(0x2A, 480, 0, -6970, 116)
    SetChrPos(0x2C, 4750, 0, -8590, 291)
    SetChrPos(0x2D, 4320, 0, -9580, 309)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 3500, 0, -4840, 214)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 4070, 0, -5920, 235)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 350, 0, -4510, 162)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 1980, 0, -2970, 183)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, -1100, 0, -4400, 125)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, 3900, 0, -1750, 225)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrPos(0x1E, 2100, 0, -1550, 170)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0x5)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 5000, 0, -2900, 250)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0xD)
    SetChrPos(0x20, 1400, 0, -650, 170)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, 4400, 0, -200, 225)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -2100, 0, -5550, 80)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -2100, 0, -3250, 125)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -3250, 0, -3000, 125)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -3000, 0, -4600, 85)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    OP_68(1850, 1000, -5600, 0)
    MoveCamera(70, 31, 0, 0)
    OP_6E(670, 0)
    SetCameraDistance(17310, 0)
    FadeToBright(5000, 0)
    MoveCamera(110, 31, 0, 60000)
    SetCameraDistance(12810, 30000)
    OP_0D()

    #C0149
    ChrTalk(
        0x18,
        (
            "#6P#0404F呵呵……原来如此啊。\x02\x03",

            "利用旧城区的\x01",
            "地形而进行追逐竞赛吗……\x02\x03",

            "#0402F听起来好像相当有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x19,
        (
            "#5P#1602F哈，不错嘛！\x02\x03",

            "总之就是那种可以妨碍别人，\x01",
            "也可以随意胡闹的乱斗竞赛吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x17,
        (
            "#5P#0903F#N速度、力量、技巧，\x01",
            "还有策略性……\x02\x03",

            "#0900F似乎会考验到各方面的能力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x16,
        "#5P#0802F#N嘿～好像很有趣呢！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0153
    ChrTalk(
        0x2B,
        "#11P#0309F哈哈，是吧？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x2A,
        (
            "#6P#0006F什么『是吧』啊……\x01",
            "兰迪，我说你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x2C,
        (
            "#5P#0106F#N阻止了斗殴自然是好……\x02\x03",

            "#0101F但最后不还是一样要给\x01",
            "周围的人们添很多麻烦吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x2D,
        (
            "#11P#0202F#N不过，也有很多人\x01",
            "主动围过来看热闹啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x18,
        (
            "#6P#0404F算了，这样不是也挺好的吗？\x01",
            "很有节日庆典的感觉啊。\x02\x03",

            "#0400F另外……\x01",
            "你们真的也要参加吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x18, 500)

    #C0158
    ChrTalk(
        0x2A,
        (
            "#11P#0003F……没办法啊。\x02\x03",

            "#0001F既然都干预到这个地步了，\x01",
            "总不能在这种时候置身事外吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x2B,
        "#11P#0302F哎呀呀，真是刻板又认真啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 800)
    TurnDirection(0x17, 0x2A, 500)

    #C0160
    ChrTalk(
        0x2A,
        (
            "#6P#0011F这明明是兰迪的提议吧！？\x02\x03",

            "#0003F不过，要完全以比赛的形式来分胜负，\x01",
            "一定不能做出违背规则的行为！\x02\x03",

            "#0013F决出胜负之后，不可怨恨赢家，\x01",
            "并引起进一步的争斗！\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x16,
        (
            "#5P#0806F#N嗯～我们当然是没有异议啦，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_351E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_351E)
    Sleep(50)

    def lambda_352E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_352E)
    Sleep(50)

    def lambda_353E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_353E)
    Sleep(50)

    def lambda_354E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_354E)
    Sleep(50)

    def lambda_355E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_355E)
    Sleep(300)

    #C0162
    ChrTalk(
        0x19,
        (
            "#6P#1604F哈，我也没意见啊。\x02\x03",

            "#1602F这样一来，游击士和警察\x01",
            "全都可以成为对手了……\x02\x03",

            "#1607F就来证明一下谁才是最强的吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x19, 500)
    Sleep(150)

    #C0163
    ChrTalk(
        0x16,
        (
            "#11P#0802F啊哈哈，那么，\x01",
            "我们就来堂堂正正地战斗吧。\x02\x03",

            "#0806F还有，我刚才的\x01",
            "态度可能也有点不好。\x02\x03",

            "#0800F那个，抱歉啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x19,
        "#1605F#6P哈……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x16, 800)
    TurnDirection(0x2C, 0x16, 800)
    TurnDirection(0x2D, 0x16, 800)
    OP_63(0x2A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x2A,
        "#12P#0012F（又、又来了……）\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x2B,
        "#12P#0302F（真是的，还是老样子……）\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x18,
        (
            "#6P#0409F啊哈哈！这位小姐真是有趣！\x02\x03",

            "#0402F在这种时候道歉的话，\x01",
            "比赛不就没有意义了吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x18, 500)

    #C0168
    ChrTalk(
        0x16,
        (
            "#5P#0805F不过，在决定以比赛形式决胜负时，\x01",
            "就已经有种无所谓恩怨的感觉了吧……\x02\x03",

            "#0809F只要彼此拿出全部实力，\x01",
            "尽情享受比赛，不就足够了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x17,
        "#11P#0906F#N呼，你还真是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x2B, 500)

    #C0170
    ChrTalk(
        0x19,
        (
            "#5P#1603F……哼，奇怪的女人。\x02\x03",

            "#1601F算啦。\x01",
            "红毛，说明一下规则吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x2B,
        "#11P#0301F谁、谁是红毛啊！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_3901():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_3901)

    def lambda_390E():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_390E)

    def lambda_391B():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_391B)

    def lambda_3928():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3928)

    def lambda_3935():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3935)

    def lambda_3942():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3942)
    Fade(500)
    OP_68(1830, 1100, -6450, 0)
    MoveCamera(179, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17810, 0)
    SetChrPos(0x2A, 260, 0, -6350, 128)
    SetChrPos(0x2C, 3370, 0, -9330, 319)
    SetChrPos(0x2D, 2520, 0, -9890, 1)
    SetChrPos(0x19, 1190, 0, -3490, 172)
    TurnDirection(0x2B, 0x19, 0)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x2B,
        (
            "#5P#0300F──就像刚才所说的，\x01",
            "比赛的基本形式就是『追逐』。\x02\x03",

            "#0304F瓦吉＆瓦鲁多是旧城区队。\x02\x03",

            "艾丝蒂尔＆约修亚是游击士队。\x02\x03",

            "#0300F还有罗伊德和我组成支援科队。\x02\x03",

            "这三组队伍将要环绕着旧城区跑三圈，\x01",
            "最先到达终点的队伍就算赢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-21270, 1380, -10450, 0)
    MoveCamera(313, 42, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21500, 0)
    MoveCamera(313, 29, 0, 10000)
    OP_6E(340, 10000)
    Sleep(500)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0173
    AnonymousTalk(
        0x2B,
        (
            "#0301F──不过，各队伍在每一圈的途中\x01",
            "都要通过三处确认点。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(44450, -1060, -22490, 0)
    MoveCamera(53, 26, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(24500, 0)
    MoveCamera(53, 14, 0, 10000)
    OP_6E(460, 10000)
    SetCameraDistance(16000, 10000)
    Sleep(300)

    #A0174
    AnonymousTalk(
        0x2B,
        (
            "#0303F确认点在几条巷子的最里面，\x01",
            "上面都安装了受到冲击就会亮起灯的装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(36420, -5060, -38470, 0)
    MoveCamera(28, 26, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(24500, 0)
    MoveCamera(53, 26, 0, 10000)
    OP_6E(300, 10000)
    Sleep(300)

    #A0175
    AnonymousTalk(
        0x2B,
        (
            "#0302F如果不把这三处确认点的灯都打亮，\x01",
            "就无法被认定为跑完了一圈。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1820, 1100, -6000, 0)
    MoveCamera(180, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17810, 0)
    MoveCamera(160, 21, 0, 30000)
    Sleep(1000)

    #C0176
    ChrTalk(
        0x2B,
        (
            "#5P#0303F在这样的地形条件下，\x01",
            "单方面逃跑是不可能的。\x02\x03",

            "#0300F在比赛的途中也可以阻碍对手……\x02\x03",

            "也就是说，除非遥遥领先，\x01",
            "否则难免会遭到对手的阻碍。\x02\x03",

            "#0304F在受到妨碍时，是迎击还是躲闪，\x01",
            "就全凭各自来做出战术判断了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x18,
        (
            "#12P#0405F呵～……\x01",
            "这规则很详细周密嘛。\x02\x03",

            "#0400F顺便一问，能不能设置机关陷阱之类的东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x2B,
        (
            "#5P#0303F嗯，就算是可以吧。\x02\x03",

            "#0300F并不仅限正面比拼，\x01",
            "也可以灵活利用地形来\x01",
            "妨碍对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x2A,
        "#12P#0001F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x17,
        "#6P#0905F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x17, 500)

    #C0181
    ChrTalk(
        0x16,
        "#6P#0805F约修亚，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x17,
        (
            "#6P#0903F没什么……\x01",
            "规则基本明白了。\x02\x03",

            "#0900F那起跑顺序怎么决定呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x2B, 500)

    #C0183
    ChrTalk(
        0x2B,
        (
            "#5P#0300F抛硬币就可以了吧。\x02\x03",

            "罗伊德、瓦鲁多、艾丝蒂尔，\x01",
            "请你们每人拿出一米拉硬币来。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x2A,
        "#12P#0005F好的……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x19,
        "#6P#1602F哈……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x16,
        "#6P#0804F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x2B,
        (
            "#5P#0304F各自将硬币弹起，然后按到手背上。\x02\x03",

            "#0300F不管是正面还是反面，和其他\x01",
            "两个人不一样的人就第一个跑吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x2A,
        "#0000F#12P原来如此。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x16,
        "#0800F#6P那么，我就抛啦。\x02",
    )

    CloseMessageWindow()

    def lambda_4067():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_4067)

    def lambda_4080():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4080)

    def lambda_4099():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4099)
    Sound(860, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德、艾丝蒂尔和瓦鲁多\x01",
            "分别抛出了硬币。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_6E(470, 5000)
    Sleep(1800)

    #C0191
    ChrTalk(
        0x2A,
        "#0001F#12P正面。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x16,
        "#0800F#6P正面哦。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x19,
        (
            "#6P#1604F反面──\x01",
            "哈，我们是第一个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x2A,
        "#0001F#12P唔……\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x16,
        "#0801F#6P嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x2B,
        (
            "#5P#0300F好，那么，接下来\x01",
            "就让瓦吉来抛硬币吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x18,
        "#12P#0404F了解。\x02",
    )

    CloseMessageWindow()

    def lambda_41E1():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_41E1)
    Sound(860, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "瓦吉抛出了硬币。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x2B, 0x16, 500)
    Sleep(300)

    #C0199
    ChrTalk(
        0x2B,
        (
            "#11P#0300F罗伊德、艾丝蒂尔。\x02\x03",

            "请选择正面或反面。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x2A, 500)

    #C0200
    ChrTalk(
        0x16,
        "#0805F#5P那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x16, 500)

    #C0201
    ChrTalk(
        0x2A,
        "#0002F#11P没关系，你先选吧。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x16,
        (
            "#0809F#5P啊哈哈……\x01",
            "那么，就正面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x2A,
        "#0000F#11P那我选反面。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "瓦吉摊开了手掌。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(1000)

    #C0205
    ChrTalk(
        0x18,
        "#12P#0404F反面──第二个出发的是罗伊德他们哦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x16, 0x17, 500)

    #C0206
    ChrTalk(
        0x16,
        (
            "#0806F#6P呜呜……\x01",
            "对不起啊，约修亚。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)

    #C0207
    ChrTalk(
        0x17,
        (
            "#0904F#5P哈哈，没关系啦。\x02\x03",

            "#0900F按照这次的规则，\x01",
            "最初的起跑顺序并不重要。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2C, 3540, 0, -7660, 2000, 0x0)
    TurnDirection(0x2C, 0x18, 500)

    #C0208
    ChrTalk(
        0x2C,
        (
            "#0100F#5P──嗯，这样一来，\x01",
            "顺序就已经决定好了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x2B,
        "#0304F#11P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x19, 500)

    def lambda_4480():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4480)
    Sleep(50)

    def lambda_4490():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4490)
    Sleep(50)

    def lambda_44A0():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_44A0)
    Sleep(500)

    #C0210
    ChrTalk(
        0x2B,
        (
            "#0300F#5P那么，在比赛开始之前，\x01",
            "各队伍都先开个作战会议吧。\x02\x03",

            "等比赛开始以后，\x01",
            "可就没有这种时间了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x16,
        "#0809F#6P啊哈哈，也是呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 500)

    #C0212
    ChrTalk(
        0x18,
        (
            "#0409F#11P呵呵，那么，瓦鲁多，\x01",
            "我们就来友好地商量对策吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)

    #C0213
    ChrTalk(
        0x19,
        "#1601F#5P哼……真肉麻。\x02",
    )

    CloseMessageWindow()

    def lambda_45A2():
        OP_95(0xFE, 9480, 0, -3490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_45A2)
    Sleep(50)

    def lambda_45BF():
        OP_95(0xFE, 2900, 0, -8940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_45BF)
    Sleep(50)

    def lambda_45DC():

        label("loc_45DC")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_45DC")

    QueueWorkItem2(0x1D, 2, lambda_45DC)

    def lambda_45EE():

        label("loc_45EE")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_45EE")

    QueueWorkItem2(0x1E, 2, lambda_45EE)

    def lambda_4600():

        label("loc_4600")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4600")

    QueueWorkItem2(0x1F, 2, lambda_4600)

    def lambda_4612():

        label("loc_4612")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4612")

    QueueWorkItem2(0x20, 2, lambda_4612)

    def lambda_4624():

        label("loc_4624")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4624")

    QueueWorkItem2(0x21, 2, lambda_4624)

    def lambda_4636():
        OP_95(0xFE, -800, 0, 1900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4636)
    Sleep(100)

    def lambda_4653():
        OP_95(0xFE, 9180, 50, -2440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4653)
    Sleep(50)

    def lambda_4670():

        label("loc_4670")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4670")

    QueueWorkItem2(0x22, 2, lambda_4670)

    def lambda_4682():

        label("loc_4682")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4682")

    QueueWorkItem2(0x23, 2, lambda_4682)

    def lambda_4694():

        label("loc_4694")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4694")

    QueueWorkItem2(0x24, 2, lambda_4694)

    def lambda_46A6():

        label("loc_46A6")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_46A6")

    QueueWorkItem2(0x25, 2, lambda_46A6)

    def lambda_46B8():

        label("loc_46B8")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_46B8")

    QueueWorkItem2(0x1A, 2, lambda_46B8)

    def lambda_46CA():
        OP_95(0xFE, -1540, 0, 790, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_46CA)
    Sleep(50)

    def lambda_46E7():
        OP_95(0xFE, -4280, 0, -10520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_46E7)
    Sleep(50)

    def lambda_4704():
        OP_95(0xFE, -3260, 0, -10950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_4704)
    Sleep(1000)
    Fade(500)
    OP_68(-4510, 3150, -11210, 0)
    MoveCamera(57, 21, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(29500, 0)
    OP_68(-4510, 1750, -11210, 3000)
    MoveCamera(74, 29, 0, 3000)
    OP_6E(280, 3000)
    SetCameraDistance(29500, 3000)
    Sleep(3000)

    #C0214
    ChrTalk(
        0x2B,
        (
            "#11P#0303F那么……罗伊德。\x02\x03",

            "#0301F我想你或许也注意到了，\x01",
            "这场比赛，我们应该是最不利的一队。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x2A,
        (
            "#0006F#5P是啊……\x02\x03",

            "#0013F瓦吉和瓦鲁多\x01",
            "对旧城区的地形了如指掌。\x02\x03",

            "而艾丝蒂尔和约修亚他们\x01",
            "所暗藏的实力也不可小觑。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x2B,
        (
            "#11P#0306F正是如此。\x02\x03",

            "#0301F如果我们要想取得胜利的话，就只能依靠\x01",
            "运气，任务分工，以及准确的状况判断了……\x02\x03",

            "#0300F我在后方担任后卫，\x01",
            "你就专心向前冲吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(150)

    #C0217
    ChrTalk(
        0x2A,
        (
            "#0005F#6P可以是可以……\x01",
            "但速度方面，不是兰迪比较快吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)

    #C0218
    ChrTalk(
        0x2B,
        (
            "#11P#0304F在这种配合竞技中，\x01",
            "让速度快的在后面负责援护，会更加有利于配合。\x02\x03",

            "#0300F而且，说到防御，\x01",
            "你的旋棍也相当合适。\x02\x03",

            "这样一来，无论是迎击还是躲避，\x01",
            "我们都能做出准确的判断。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x2A,
        (
            "#0003F#6P嗯～……\x01",
            "明白了，我试试看。\x02\x03",

            "#0000F虽然每一队都很强……\x01",
            "但既然参加了，就一定要全力取胜！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x2B,
        "#0309F#11P哈哈，要的就是这股干劲。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x2B,
        (
            "#11P#0305F……对了。\x02\x03",

            "#0300F机会难得，\x01",
            "要不要在这里试一试\x01",
            "组合战技呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0222
    ChrTalk(
        0x2A,
        "#0005F#6P咦……这么突然，没问题吗？\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x2B,
        (
            "#11P#0304F没事的，我们都已经很熟悉\x01",
            "对方的行动特点了吧。\x02\x03",

            "#0300F就直接动真格好了──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 4)), scpexpr(EXPR_END)), "loc_4CBE")
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和兰迪习得了组合战技\x01\x07\x02",

            "『燃烧之怒Ⅱ』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※另外，此次追逐竞技中，在同敌方\x01",
            "　队伍交战时，可将此战技选为我方的行动策略。\x01",
            "　（这种情况下并不会消耗ＣＰ，不需担心。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_4DD7")

    label("loc_4CBE")

    AddCraft(0x0, 0x14C)
    AddCraft(0x3, 0x14C)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和兰迪习得了组合战技\x01\x07\x02",

            "『燃烧之怒』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0229
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※另外，此次追逐竞技中，在同敌方\x01",
            "　队伍交战时，可将此战技选为我方的行动策略。\x01",
            "　（这种情况下并不会消耗ＣＰ，不需担心。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_4DD7")

    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x1E, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x21, 0xFF)
    EndChrThread(0x22, 0xFF)
    EndChrThread(0x23, 0xFF)
    EndChrThread(0x24, 0xFF)
    EndChrThread(0x25, 0xFF)
    EndChrThread(0x1A, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    Call(0, 71)
    Return()

    # Function_25_2B6C end

    def Function_26_4ECA(): pass

    label("Function_26_4ECA")

    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_26_4ECA end

    def Function_27_4F58(): pass

    label("Function_27_4F58")

    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_27_4F58 end

    def Function_28_4FC0(): pass

    label("Function_28_4FC0")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -14710, 0, -11410, 7000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_28_4FC0 end

    def Function_29_5052(): pass

    label("Function_29_5052")

    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_29_5052 end

    def Function_30_50BE(): pass

    label("Function_30_50BE")

    SetChrPos(0xFE, -980, 0, -8050, 272)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_30_50BE end

    def Function_31_5161(): pass

    label("Function_31_5161")

    SetChrPos(0xFE, -1210, 0, -9240, 256)
    SetChrChipByIndex(0xFE, 0x2D)
    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_31_5161 end

    def Function_32_51DE(): pass

    label("Function_32_51DE")

    SetChrPos(0xFE, -980, 0, -8050, 272)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -8980, 0, -10190, 6000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_32_51DE end

    def Function_33_5291(): pass

    label("Function_33_5291")

    SetChrPos(0xFE, -1210, 0, -9240, 256)
    SetChrChipByIndex(0xFE, 0x2D)
    OP_95(0xFE, -8740, 0, -11240, 5000, 0x0)
    OP_95(0xFE, -18490, 0, -11470, 4000, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_33_5291 end

    def Function_34_530B(): pass

    label("Function_34_530B")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrPos(0xFE, -9470, -3280, -24010, 7000)
    OP_95(0xFE, -3020, -3880, -27130, 7000, 0x0)
    OP_95(0xFE, 8500, -6390, -35860, 6000, 0x0)
    OP_95(0xFE, 26760, -6490, -37430, 6000, 0x0)
    Return()

    # Function_34_530B end

    def Function_35_535D(): pass

    label("Function_35_535D")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrPos(0xFE, -11390, -3080, -24680, 6000)
    OP_95(0xFE, -4560, -3800, -27110, 6000, 0x0)
    OP_95(0xFE, 5280, -5590, -36320, 6000, 0x0)
    OP_95(0xFE, 26700, -6490, -39330, 6000, 0x0)
    Return()

    # Function_35_535D end

    def Function_36_53AF(): pass

    label("Function_36_53AF")

    SetChrChipByIndex(0xFE, 0x27)
    OP_95(0xFE, 22720, -6500, -37590, 7000, 0x0)
    OP_95(0xFE, 21220, -2500, -25410, 7000, 0x0)
    Return()

    # Function_36_53AF end

    def Function_37_53DC(): pass

    label("Function_37_53DC")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 30470, -6500, -37950, 6000, 0x0)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 22440, -2550, -25860, 6000, 0x0)
    Return()

    # Function_37_53DC end

    def Function_38_5420(): pass

    label("Function_38_5420")

    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 32280, -6500, -38450, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 22440, -2550, -25860, 6000, 0x0)
    Return()

    # Function_38_5420 end

    def Function_39_548A(): pass

    label("Function_39_548A")

    Sound(532, 0, 100, 0)
    OP_71(0xF, 0xA, 0x28, 0x0, 0x20)
    OP_9D(0x2E, 0x66BC, 0xFFFFE890, 0xFFFF6A96, 0x3E8, 0xFA0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(826, 0, 100, 0)
    OP_9D(0x2E, 0x61A8, 0xFFFFE890, 0xFFFF6A96, 0x190, 0xFA0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_95(0x2E, 8840, -6430, -36090, 6000, 0x0)
    SetMapObjFlags(0xF, 0x4)
    Return()

    # Function_39_548A end

    def Function_40_550D(): pass

    label("Function_40_550D")

    SetChrPos(0xFE, 21840, -6500, -37170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_40_550D end

    def Function_41_555B(): pass

    label("Function_41_555B")

    SetChrPos(0xFE, 21840, -6500, -40170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_41_555B end

    def Function_42_55A9(): pass

    label("Function_42_55A9")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrPos(0xFE, 25590, -2500, -24700, 340)
    OP_95(0xFE, 41840, -2500, -24090, 7000, 0x0)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_42_55A9 end

    def Function_43_55DA(): pass

    label("Function_43_55DA")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrPos(0xFE, 27000, -2500, -23420, 0)
    OP_95(0xFE, 43180, -2500, -22300, 5000, 0x0)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x29)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_43_55DA end

    def Function_44_562D(): pass

    label("Function_44_562D")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 43240, -2500, -22630, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 37240, -2500, -22750, 7000, 0x0)
    OP_95(0xFE, 19890, -2500, -22930, 7000, 0x0)
    OP_95(0xFE, 8740, 0, -11540, 6000, 0x0)
    OP_95(0xFE, 4170, -10, -8870, 7000, 0x0)
    OP_95(0xFE, -4930, -10, -8640, 7000, 0x0)
    OP_95(0xFE, -10890, -10, -11230, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -18070, 0, -10380, 6000, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_44_562D end

    def Function_45_5773(): pass

    label("Function_45_5773")

    Sleep(500)
    OP_95(0xFE, 34760, -2500, -23810, 5000, 0x0)
    OP_95(0xFE, 19890, -2500, -22930, 6000, 0x0)
    OP_95(0xFE, 8740, 0, -11540, 7000, 0x0)
    OP_95(0xFE, 4170, -10, -8870, 7000, 0x0)
    OP_95(0xFE, -4930, -10, -8640, 7000, 0x0)
    OP_95(0xFE, -10890, -10, -11230, 6000, 0x0)
    OP_95(0xFE, -18320, 0, -11470, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_45_5773 end

    def Function_46_5836(): pass

    label("Function_46_5836")

    SetChrPos(0xFE, 21840, -6500, -37170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_46_5836 end

    def Function_47_5884(): pass

    label("Function_47_5884")

    SetChrPos(0xFE, 21840, -6500, -40170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_47_5884 end

    def Function_48_58D2(): pass

    label("Function_48_58D2")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrPos(0xFE, -9470, -3280, -24010, 9000)
    OP_95(0xFE, -3020, -3880, -27130, 9000, 0x0)
    OP_95(0xFE, 8500, -6390, -35860, 9000, 0x0)
    OP_95(0xFE, 35200, -6490, -38160, 9000, 0x0)
    Return()

    # Function_48_58D2 end

    def Function_49_5924(): pass

    label("Function_49_5924")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrPos(0xFE, -11390, -3080, -24680, 9000)
    OP_95(0xFE, -4560, -3800, -27110, 9000, 0x0)
    OP_95(0xFE, 5280, -5590, -36320, 9000, 0x0)
    OP_95(0xFE, 33860, -6490, -39150, 9000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_49_5924 end

    def Function_50_5981(): pass

    label("Function_50_5981")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrPos(0xFE, 23260, -6490, -37200, 99)
    OP_95(0xFE, 32750, -6490, -37340, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)

    def lambda_59B3():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59B3)
    SetChrFlags(0xFE, 0x4)
    Sound(854, 0, 100, 0)
    OP_9D(0xFE, 0x8EB2, 0xFFFFEC78, 0xFFFF69C4, 0x7D0, 0xFA0)
    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_9D(0xFE, 0x7FEE, 0xFFFFE6A6, 0xFFFF6E24, 0x1F4, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    Sound(326, 0, 100, 0)
    Sleep(300)
    OP_95(0xFE, 22640, -6490, -36980, 7000, 0x0)
    Return()

    # Function_50_5981 end

    def Function_51_5A2D(): pass

    label("Function_51_5A2D")

    SetChrPos(0xFE, 22340, -6490, -38660, 94)
    Sleep(500)
    OP_95(0xFE, 31530, -6490, -39340, 7000, 0x0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Sleep(1300)
    SetChrChipByIndex(0x17, 0x30)
    OP_95(0xFE, 22640, -6490, -36980, 7000, 0x0)
    Return()

    # Function_51_5A2D end

    def Function_52_5A79(): pass

    label("Function_52_5A79")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 21840, -6500, -37170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -24500, 6000, 0x0)
    OP_95(0xFE, 31620, -2500, -22500, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x31)

    def lambda_5AD6():

        label("loc_5AD6")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_5AD6")

    QueueWorkItem2(0xFE, 2, lambda_5AD6)
    Return()

    # Function_52_5A79 end

    def Function_53_5AE4(): pass

    label("Function_53_5AE4")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 21840, -6500, -38170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 7000, 0x0)
    OP_95(0xFE, 30970, -2500, -24000, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)

    def lambda_5B44():

        label("loc_5B44")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_5B44")

    QueueWorkItem2(0xFE, 2, lambda_5B44)
    Return()

    # Function_53_5AE4 end

    def Function_54_5B52(): pass

    label("Function_54_5B52")

    SetChrChipByIndex(0xFE, 0x27)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, 42800, -2500, -23020, 7000, 0x0)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    Sound(532, 0, 100, 0)
    OP_A1(0xFE, 0xFA0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x27)
    OP_95(0xFE, 23080, -2500, -23890, 7000, 0x0)
    Return()

    # Function_54_5B52 end

    def Function_55_5BAF(): pass

    label("Function_55_5BAF")

    Sleep(2400)
    SetChrChipByIndex(0xFE, 0x2A)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, 23080, -2500, -23890, 7000, 0x0)
    Return()

    # Function_55_5BAF end

    def Function_56_5BCF(): pass

    label("Function_56_5BCF")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrFlags(0xFE, 0x4)
    Sound(814, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFCB8A, 0x10CC, 0xFFFFE049, 0x3E8, 0xFA0)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_5BFE():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BFE)
    Sound(854, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFB438, 0x7D0, 0xFFFFD7A6, 0x7D0, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_56_5BCF end

    def Function_57_5C29(): pass

    label("Function_57_5C29")

    OP_93(0xFE, 0x10E, 0x320)
    SetChrChipByIndex(0xFE, 0x29)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    OP_95(0xFE, -14710, 0, -11410, 7000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    Return()

    # Function_57_5C29 end

    def Function_58_5C84(): pass

    label("Function_58_5C84")

    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_58_5C84 end

    def Function_59_5CC1(): pass

    label("Function_59_5CC1")

    SetChrPos(0xFE, 30590, -6500, -36930, 45)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 5000, 0x0)
    OP_95(0xFE, 22800, -2510, -24000, 6000, 0x0)
    OP_95(0xFE, 33880, -2500, -23450, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x38)
    BeginChrThread(0xFE, 2, 0, 70)
    OP_9C(0xFE, 0x3E8, 0x0, 0x0, 0x64, 0xBB8)
    Sound(514, 0, 100, 0)
    Return()

    # Function_59_5CC1 end

    def Function_60_5D4A(): pass

    label("Function_60_5D4A")

    SetChrPos(0xFE, 32990, -6500, -39280, 315)
    OP_95(0xFE, 21840, -6500, -38170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 6000, 0x0)
    OP_95(0xFE, 33550, -2500, -25230, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x37)
    BeginChrThread(0xFE, 2, 0, 70)
    Sound(590, 0, 100, 0)
    OP_9C(0xFE, 0x960, 0x0, 0x0, 0x64, 0xFA0)
    Sound(819, 0, 100, 0)
    Return()

    # Function_60_5D4A end

    def Function_61_5DD9(): pass

    label("Function_61_5DD9")

    SetChrPos(0xFE, 27350, -6500, -39590, 210)
    OP_95(0xFE, 21840, -6500, -37170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 5000, 0x0)
    OP_95(0xFE, 22800, -2510, -24500, 6000, 0x0)
    OP_95(0xFE, 33770, -2500, -22910, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x39)
    BeginChrThread(0xFE, 2, 0, 70)
    Sound(590, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x64, 0xBB8)
    Sound(819, 0, 100, 0)
    Return()

    # Function_61_5DD9 end

    def Function_62_5E68(): pass

    label("Function_62_5E68")

    SetChrPos(0xFE, 29850, -6500, -40680, 135)
    OP_95(0xFE, 21840, -6500, -38170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 6000, 0x0)
    OP_95(0xFE, 33350, -2500, -24540, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    BeginChrThread(0xFE, 2, 0, 70)
    OP_9C(0xFE, 0x4E2, 0x0, 0x0, 0x64, 0xFA0)
    Sound(514, 0, 100, 0)
    Return()

    # Function_62_5E68 end

    def Function_63_5EF1(): pass

    label("Function_63_5EF1")

    OP_95(0xFE, 30930, 2390, -21190, 6000, 0x0)
    OP_95(0xFE, 34310, 2450, -21190, 6000, 0x0)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_63_5EF1 end

    def Function_64_5F21(): pass

    label("Function_64_5F21")

    OP_95(0x2A, 40240, -1000, -27180, 7000, 0x0)
    Sound(814, 0, 100, 0)
    OP_9D(0x2A, 0xA028, 0xFFFFF63C, 0xFFFFA07E, 0x3E8, 0xFA0)
    Sound(42, 0, 100, 0)
    Sound(31, 0, 100, 0)
    OP_95(0x2A, 43620, -2500, -22910, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x33)
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(150)
    OP_95(0x2A, 41240, -2490, -22980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x31)

    def lambda_5FC5():

        label("loc_5FC5")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_5FC5")

    QueueWorkItem2(0xFE, 2, lambda_5FC5)
    Return()

    # Function_64_5F21 end

    def Function_65_5FD3(): pass

    label("Function_65_5FD3")

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
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    OP_D5(0x0)
    OP_D5(0x1)
    OP_D5(0x2)
    OP_D5(0x3)
    OP_D5(0x4)
    OP_D5(0x6)
    OP_D5(0x7)
    OP_D5(0x8)
    OP_D5(0x9)
    OP_D5(0xA)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("apl/ch50378.itc", 0x24)
    LoadChrToIndex("chr/ch02150.itc", 0x25)
    LoadChrToIndex("chr/ch02152.itc", 0x26)
    LoadChrToIndex("chr/ch02151.itc", 0x27)
    LoadChrToIndex("chr/ch00450.itc", 0x28)
    LoadChrToIndex("chr/ch00452.itc", 0x29)
    LoadChrToIndex("chr/ch00451.itc", 0x2A)
    LoadChrToIndex("chr/ch00650.itc", 0x2B)
    LoadChrToIndex("chr/ch00652.itc", 0x2C)
    LoadChrToIndex("chr/ch00651.itc", 0x2D)
    LoadChrToIndex("chr/ch00750.itc", 0x2E)
    LoadChrToIndex("chr/ch00752.itc", 0x2F)
    LoadChrToIndex("chr/ch00751.itc", 0x30)
    LoadChrToIndex("chr/ch00050.itc", 0x31)
    LoadChrToIndex("chr/ch00052.itc", 0x32)
    LoadChrToIndex("chr/ch00051.itc", 0x33)
    LoadChrToIndex("chr/ch00350.itc", 0x34)
    LoadChrToIndex("chr/ch00352.itc", 0x35)
    LoadChrToIndex("chr/ch00351.itc", 0x36)
    LoadChrToIndex("chr/ch02153.itc", 0x37)
    LoadChrToIndex("chr/ch00453.itc", 0x38)
    LoadChrToIndex("chr/ch00653.itc", 0x39)
    LoadChrToIndex("chr/ch00753.itc", 0x3A)
    LoadChrToIndex("chr/ch00053.itc", 0x3B)
    LoadChrToIndex("chr/ch00353.itc", 0x3C)
    LoadChrToIndex("chr/ch00357.itc", 0x3D)
    LoadChrToIndex("apl/ch50311.itc", 0x3E)
    LoadChrToIndex("apl/ch50314.itc", 0x3F)
    LoadChrToIndex("chr/ch00155.itc", 0x40)
    LoadChrToIndex("apl/ch50312.itc", 0x41)
    ClearMapObjFlags(0x8, 0x20)
    ClearMapObjFlags(0x8, 0x4)
    OP_70(0x8, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_65_5FD3 end

    def Function_66_61BE(): pass

    label("Function_66_61BE")

    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    OP_D5(0x32)
    OP_D5(0x33)
    OP_D5(0x34)
    OP_D5(0x35)
    OP_D5(0x36)
    OP_D5(0x37)
    OP_D5(0x38)
    OP_D5(0x39)
    OP_D5(0x3A)
    OP_D5(0x3B)
    OP_D5(0x3C)
    OP_D5(0x3D)
    OP_D5(0x3E)
    OP_D5(0x3F)
    OP_D5(0x40)
    OP_D5(0x41)
    Return()

    # Function_66_61BE end

    def Function_67_629E(): pass

    label("Function_67_629E")

    OP_A1(0xFE, 0x6A4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Return()

    # Function_67_629E end

    def Function_68_62AB(): pass

    label("Function_68_62AB")

    OP_A1(0xFE, 0x6A4, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_68_62AB end

    def Function_69_62B6(): pass

    label("Function_69_62B6")

    OP_A1(0xFE, 0x6A4, 0x4, 0x3, 0x2, 0x1, 0x0)
    Return()

    # Function_69_62B6 end

    def Function_70_62C1(): pass

    label("Function_70_62C1")

    OP_A1(0xFE, 0x6A4, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_70_62C1 end

    def Function_71_62CB(): pass

    label("Function_71_62CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    OP_49()
    Call(0, 65)
    LoadChrToIndex("chr/ch00000.itc", 0x37)
    LoadChrToIndex("chr/ch00100.itc", 0x38)
    LoadChrToIndex("chr/ch00200.itc", 0x39)
    LoadChrToIndex("chr/ch00300.itc", 0x3A)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrChipByIndex(0x2D, 0x39)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x2C, -5340, 0, -6550, 122)
    SetChrPos(0x2D, -4410, 0, -5830, 122)
    SetChrPos(0x18, -3140, 0, -8130, 302)
    SetChrPos(0x19, -3080, 0, -9580, 302)
    SetChrPos(0x2A, -980, 0, -8050, 302)
    SetChrPos(0x2B, -1210, 0, -9240, 302)
    SetChrPos(0x16, 1080, 0, -9140, 302)
    SetChrPos(0x17, 1580, 0, -7990, 302)
    SetChrPos(0x1A, -3500, 0, -4500, 170)
    SetChrPos(0x1C, 2240, 0, 6890, 180)
    SetChrPos(0x1B, 1050, 0, 7050, 180)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, 1950, 0, -4050, 240)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrPos(0x1E, 3400, 0, -5700, 275)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0x5)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 3600, 0, -3700, 240)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0xD)
    SetChrPos(0x20, 2850, 0, -2050, 220)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, 4850, 0, -4050, 240)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -4350, 0, -1800, 160)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -4900, 0, -3800, 140)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -2700, 0, -3200, 160)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -6000, 0, -2600, 140)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    FadeToBright(4000, 0)
    OP_68(1350, 2000, -8800, 0)
    MoveCamera(358, 31, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16000, 0)
    OP_68(-2710, 1320, -6940, 5000)
    MoveCamera(348, 30, 0, 5000)
    OP_6E(540, 5000)
    SetCameraDistance(15740, 5000)
    Sleep(5000)

    #C0230
    ChrTalk(
        0x2C,
        (
            "#5P#0104F──那么，就由我\x01",
            "来发令了哦。\x02\x03",

            "#0100F第一发空枪后，第一组队伍起跑。\x02\x03",

            "五秒之后会发第二枪，此时第二组队伍起跑。\x02\x03",

            "再过五秒，\x01",
            "会发最后一枪，第三组队伍起跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x2D,
        (
            "#5P#0204F……倒计时就\x01",
            "由我来负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x1A,
        (
            "#5P那么，我们来注意观看比赛的人，\x01",
            "避免他们被卷进来。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0233
    ChrTalk(
        0x18,
        "#5P#0404F呵呵，舞台似乎已经准备好了呢。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("女性的声音")

    #A0234
    AnonymousTalk(
        0xFF,
        "不，主角还没到齐呢！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6943():

        label("loc_6943")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6943")

    QueueWorkItem2(0x2A, 0, lambda_6943)
    Sleep(50)

    def lambda_6958():

        label("loc_6958")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6958")

    QueueWorkItem2(0x2D, 0, lambda_6958)
    Sleep(50)

    def lambda_696D():

        label("loc_696D")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_696D")

    QueueWorkItem2(0x19, 0, lambda_696D)

    def lambda_697F():

        label("loc_697F")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_697F")

    QueueWorkItem2(0x16, 0, lambda_697F)
    Sleep(50)

    def lambda_6994():

        label("loc_6994")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6994")

    QueueWorkItem2(0x17, 0, lambda_6994)
    Sleep(50)

    def lambda_69A9():

        label("loc_69A9")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_69A9")

    QueueWorkItem2(0x1A, 0, lambda_69A9)
    Sleep(50)

    def lambda_69BE():

        label("loc_69BE")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_69BE")

    QueueWorkItem2(0x2C, 0, lambda_69BE)
    Sleep(50)

    def lambda_69D3():

        label("loc_69D3")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_69D3")

    QueueWorkItem2(0x2B, 0, lambda_69D3)

    def lambda_69E5():

        label("loc_69E5")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_69E5")

    QueueWorkItem2(0x18, 0, lambda_69E5)
    Sleep(50)

    def lambda_69FA():

        label("loc_69FA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_69FA")

    QueueWorkItem2(0x1D, 2, lambda_69FA)

    def lambda_6A0C():

        label("loc_6A0C")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A0C")

    QueueWorkItem2(0x1E, 2, lambda_6A0C)

    def lambda_6A1E():

        label("loc_6A1E")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A1E")

    QueueWorkItem2(0x1F, 2, lambda_6A1E)

    def lambda_6A30():

        label("loc_6A30")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A30")

    QueueWorkItem2(0x20, 2, lambda_6A30)

    def lambda_6A42():

        label("loc_6A42")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A42")

    QueueWorkItem2(0x21, 2, lambda_6A42)

    def lambda_6A54():

        label("loc_6A54")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A54")

    QueueWorkItem2(0x22, 2, lambda_6A54)

    def lambda_6A66():

        label("loc_6A66")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A66")

    QueueWorkItem2(0x23, 2, lambda_6A66)

    def lambda_6A78():

        label("loc_6A78")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A78")

    QueueWorkItem2(0x24, 2, lambda_6A78)

    def lambda_6A8A():

        label("loc_6A8A")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_6A8A")

    QueueWorkItem2(0x25, 2, lambda_6A8A)

    def lambda_6A9C():
        OP_95(0xFE, -1220, 0, -4550, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6A9C)

    def lambda_6AB6():
        OP_95(0xFE, -50, 0, -4300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6AB6)
    Sleep(500)
    Fade(500)
    OP_68(130, 620, -370, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12500, 0)
    OP_68(-1140, 1860, -7560, 5000)
    MoveCamera(0, 31, 0, 5000)
    OP_6E(620, 5000)
    SetCameraDistance(12500, 5000)
    Sleep(5000)

    #C0235
    ChrTalk(
        0x2A,
        "#6P#0005F格、格蕾丝小姐！？\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x17,
        "#12P#0905F是克洛斯贝尔时代周刊的……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x1B,
        (
            "#5P#2109F呀哈～ＢＯＹＳ＆ＧＩＲＬＳ！\x02\x03",

            "#2102F你们似乎正要做些\x01",
            "很有趣的事吧？\x02\x03",

            "让姐姐我也掺一脚如何啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x2A,
        "#6P#0011F掺、掺一脚……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x19,
        "#6P#1600F#N哈，你想干什么？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0240
    ChrTalk(
        0x1B,
        "#5P#2101F答案就是──这个哦！\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0xC8)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xF)
    OP_68(-1210, 2000, -6530, 500)
    OP_6E(580, 500)
    SetCameraDistance(10500, 500)
    OP_93(0x1B, 0xA, 0x2BC)
    OP_93(0x1B, 0xB4, 0x2BC)
    Sound(534, 0, 100, 0)
    Sound(882, 0, 100, 0)
    CancelBlur(100)
    Sound(896, 0, 100, 0)
    SetChrChipByIndex(0x1B, 0x3E)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x3F)
    SetChrSubChip(0x1C, 0x0)
    Sleep(1600)
    VolumeBGM(0x64, 0xC8)

    #C0241
    ChrTalk(
        0x1B,
        (
            "#5P#2110F既然是竞赛，自然要有实况解说员！\x02\x03",

            "#2109F摄影师我也一起带来了，\x01",
            "你们就尽情闹个够吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x1C, -6880, 1800, -14620, 45)
    SetChrPos(0x1B, -5740, 1800, -14060, 45)
    OP_68(-3900, 2000, -10810, 0)
    MoveCamera(87, 29, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x2A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-4080, 2000, -8980, 5000)
    MoveCamera(65, 29, 0, 5000)
    SetCameraDistance(16000, 5000)
    Sleep(1000)
    EndChrThread(0x2A, 0x0)
    EndChrThread(0x2C, 0x0)
    EndChrThread(0x2D, 0x0)
    EndChrThread(0x2B, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)

    #C0242
    ChrTalk(
        0x2D,
        (
            "#5P#0211F好像还真的开始有了\x01",
            "庆典狂欢的感觉呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x16,
        (
            "#11P#0809F#N啊哈哈，这不是很好吗，\x01",
            "总比斗殴快乐好几倍吧¤\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2C, 500)
    Sleep(300)

    #C0244
    ChrTalk(
        0x2B,
        (
            "#11P#0304F哎呀呀……\x01",
            "那就好好期待一下吧。\x02\x03",

            "#0300F那么，差不多就要正式开始了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F80():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_6F80)

    def lambda_6F8D():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_6F8D)
    Sleep(100)

    def lambda_6F9D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_6F9D)

    def lambda_6FAA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6FAA)
    Sleep(100)

    def lambda_6FBA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_6FBA)

    def lambda_6FC7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_6FC7)
    Sleep(100)

    def lambda_6FD7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_6FD7)

    def lambda_6FE4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_6FE4)

    def lambda_6FF1():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_6FF1)

    def lambda_6FFE():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_6FFE)

    def lambda_700B():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_700B)

    def lambda_7018():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_7018)

    def lambda_7025():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7025)

    def lambda_7032():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_7032)

    def lambda_703F():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_703F)

    def lambda_704C():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_704C)

    def lambda_7059():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_7059)

    #C0245
    ChrTalk(
        0x18,
        (
            "#0404F#5P呵呵，是呀。\x02\x03",

            "#0402F瓦鲁多，准备得如何了？\x02",
        )
    )

    CloseMessageWindow()
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x25)
    OP_A0(0x19, 2000, 0x0, 0xFB)

    #C0246
    ChrTalk(
        0x19,
        "#1602F#11P哈，随时奉陪。\x02",
    )

    CloseMessageWindow()
    OP_68(-5100, 1610, -9070, 3000)
    MoveCamera(72, 29, 0, 3000)
    OP_6E(540, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x18, 0x2A)

    def lambda_7100():

        label("loc_7100")

        TurnDirection(0xFE, 0x18, 400)
        Yield()
        Jump("loc_7100")

    QueueWorkItem2(0x2D, 2, lambda_7100)

    def lambda_7112():
        OP_95(0xFE, -5130, 0, -8590, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7112)
    Sleep(100)
    SetChrChipByIndex(0x19, 0x27)
    OP_95(0x19, -5050, 0, -9830, 2000, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_714B():

        label("loc_714B")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_714B")

    QueueWorkItem2(0x19, 2, lambda_714B)
    Sleep(1000)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_7164():

        label("loc_7164")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_7164")

    QueueWorkItem2(0x18, 2, lambda_7164)
    Sleep(1000)

    def lambda_7179():
        OP_96(0xFE, 0xFFFFEB60, 0x0, 0xFFFFE8D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_7179)
    WaitChrThread(0x2C, 1)
    SetChrChipByIndex(0x2C, 0x40)
    SetChrSubChip(0x2C, 0x0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x2C, 0x2)
    OP_A0(0x2C, 1500, 0x6, 0x0)
    Fade(250)
    ClearChrFlags(0x2C, 0x2)
    SetChrChipByIndex(0x2C, 0x41)
    SetChrSubChip(0x2C, 0x0)
    Sound(804, 0, 100, 0)
    EndChrThread(0x2D, 0x2)
    OP_0D()

    #C0247
    ChrTalk(
        0x2D,
        (
            "#0202F#5P……那么，\x01",
            "开始倒计时。\x02",
        )
    )

    CloseMessageWindow()
    OP_E5()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6E(1060, 6000)
    SetCameraDistance(7000, 6000)
    Sound(844, 0, 100, 0)

    #C0248
    ChrTalk(
        0x2D,
        "#0203F#10A『３』\x02",
    )
    #Auto

    Sleep(1000)
    Sound(844, 0, 100, 0)

    #C0249
    ChrTalk(
        0x2D,
        "#0203F#10A『２』\x02",
    )
    #Auto

    Sleep(1000)
    Sound(844, 0, 100, 0)

    #C0250
    ChrTalk(
        0x2D,
        "#0203F#10A『１』\x02",
    )
    #Auto

    Sleep(1000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(500, 16777215)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7507", 0)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 26)
    BeginChrThread(0x19, 3, 0, 27)
    Fade(500)
    OP_67(0x1)
    OP_68(-6020, 2000, -9720, 0)
    MoveCamera(74, 9, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27150, 0)
    Sound(845, 0, 100, 0)
    Sound(901, 0, 100, 0)

    #N0251
    NpcTalk(
        0x2D,
        "缇欧",
        "#0207F#5A#N──『０』！\x02",
    )
    #Auto

    Sleep(1000)
    OP_5A()
    SetMessageWindowPos(14, -10, -1, 3)

    #A0252
    AnonymousTalk(
        0x1B,
        "#4A#30W#2110F好，比赛开始！\x02",
    )
    #Auto

    Sleep(1000)
    EndChrThread(0x18, 0x3)
    Sleep(400)
    EndChrThread(0x19, 0x3)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_93(0x1B, 0x12C, 0x0)
    OP_93(0x1C, 0x12C, 0x0)
    SetChrPos(0x18, -3140, 0, -8130, 302)
    SetChrPos(0x19, -3080, 0, -9580, 302)
    SetChrChipByIndex(0x19, 0x27)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 26)
    BeginChrThread(0x19, 3, 0, 27)
    OP_67(0x1)
    OP_68(-17450, 2000, -12010, 2500)
    MoveCamera(296, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(27150, 0)

    #A0253
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2110F第一组，瓦吉＆瓦鲁多的队伍，\x01",
            "以相当漂亮的起跑开始了比赛！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    #A0254
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2110F现在已经通过了第一个确认点，\x01",
            "正在向第二个确认点进发！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x2)
    Sound(845, 0, 100, 0)
    Fade(500)
    BeginChrThread(0x2A, 3, 0, 28)
    BeginChrThread(0x2B, 3, 0, 29)
    OP_67(0x1)
    OP_68(-4540, 2000, -9070, 0)
    MoveCamera(83, 10, -1, 0)
    OP_6E(320, 0)
    SetCameraDistance(27150, 0)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0255
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100F第二组，罗伊德＆兰迪的队伍，\x01",
            "已经起跑了！\x02",
        )
    )
    #Auto

    Sleep(2400)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    Sleep(800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x2A, -980, 0, -8050, 302)
    SetChrPos(0x2B, -1210, 0, -9240, 302)
    BeginChrThread(0x2A, 3, 0, 28)
    BeginChrThread(0x2B, 3, 0, 29)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(-20730, 2000, -11460, 0)
    MoveCamera(59, 32, 0, 2500)
    OP_6E(340, 0)
    SetCameraDistance(25650, 0)

    #A0256
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100F兰迪选手脚下生风！\x01",
            "罗伊德选手的速度也相当快！\x02",
        )
    )
    #Auto

    Sleep(4000)
    OP_57(0x0)
    OP_5A()

    #A0257
    AnonymousTalk(
        0x1B,
        "#8A#30W#2100F现在已经通过了第一个确认点！\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()
    Sound(845, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 30)
    BeginChrThread(0x16, 3, 0, 31)
    BeginChrThread(0x2A, 3, 0, 34)
    BeginChrThread(0x2B, 3, 0, 35)
    SetChrPos(0x18, 33790, -6490, -39680, 270)
    SetChrPos(0x19, 32409, -6490, -38140, 270)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(-4720, 2000, -6290, 0)
    MoveCamera(211, 26, -1, 0)
    OP_6E(340, 0)
    SetCameraDistance(25650, 0)
    SetMessageWindowPos(290, 145, -1, -1)

    #A0258
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2104F第三组，艾丝蒂尔＆约修亚的队伍，\x01",
            "起跑！\x02",
        )
    )
    #Auto

    Sleep(200)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    Sleep(2200)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    Sleep(800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x16, 1080, 0, -9140, 302)
    SetChrPos(0x17, 1580, 0, -7990, 302)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 30)
    BeginChrThread(0x16, 3, 0, 31)
    OP_67(0x1)
    OP_68(-10660, 2000, -12350, 0)
    MoveCamera(53, 36, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12970, 0)
    OP_68(-10660, 2000, -12350, 0)
    MoveCamera(316, 36, 0, 3500)
    OP_6E(620, 0)
    SetCameraDistance(12970, 0)

    #A0259
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100F配合的默契程度近乎完美！\x01",
            "而他们身为游击士的实力也是Ａ级的！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    #A0260
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100F现在已经通过了第一个确认点！\x01",
            "开始追击先出发的队伍了！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()
    Fade(1500)
    OP_6B(0x2A)
    BeginChrThread(0x2A, 3, 0, 34)
    BeginChrThread(0x2B, 3, 0, 35)
    OP_67(0x1)
    OP_68(-9470, -3280, -24010, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(11000, 0)
    MoveCamera(65, 18, 0, 4000)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_785F():

        label("loc_785F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_785F")

    QueueWorkItem2(0x18, 2, lambda_785F)
    SetChrPos(0x18, 33790, -6490, -39680, 270)
    SetChrPos(0x19, 32409, -6490, -38140, 270)
    SetChrPos(0x16, 1080, 0, -9140, 272)
    SetChrPos(0x17, 1580, 0, -7990, 267)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    OP_93(0x1D, 0xB4, 0x0)
    OP_93(0x1E, 0xB4, 0x0)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    SetChrPos(0x2E, 32409, -4800, -38140, 180)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x2E)
    OP_D3(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_49()
    OP_74(0xF, 0xF)
    OP_70(0xF, 0xA)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x1)
    Sleep(3500)
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6B(0xFF)
    Fade(1000)
    OP_68(33490, -4540, -38270, 1000)
    MoveCamera(70, 18, 0, 1000)
    OP_6E(360, 1000)
    SetCameraDistance(22500, 1000)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0261
    AnonymousTalk(
        0x1B,
        (
            "#7A#30W#2105F噢噢～！\x01",
            "瓦鲁多选手突然施展绝技！\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()

    #A0262
    AnonymousTalk(
        0x1B,
        "#8A#30W#2101F好，罗伊德队将如何应对呢！？\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x2A, 13000, -6490, -37180, 78)

    def lambda_7A79():
        OP_95(0x2A, 23760, -6490, -37430, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 3, lambda_7A79)
    SetChrPos(0x2B, 12600, -6490, -39220, 315)

    def lambda_7AA4():
        OP_95(0x2B, 23700, -6490, -39330, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_7AA4)
    OP_68(21660, -5040, -38440, 0)
    MoveCamera(80, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_68(29470, -5040, -38330, 2500)
    MoveCamera(83, 10, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(21000, 2500)

    #C0263
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0001F（唔……）\x02",
    )
    #Auto

    Sleep(1000)

    #C0264
    ChrTalk(
        0x2B,
        "#11P#12A#30W#0301F（交给你来判断……！）\x02",
    )
    #Auto

    Sleep(1800)
    OP_E6()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【设法躲闪】\x01",      # 0
            "【直接突击】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BC6"),
        (1, "loc_7D73"),
        (SWITCH_DEFAULT, "loc_802F"),
    )


    label("loc_7BC6")


    #C0265
    ChrTalk(
        0x19,
        "#6A#30W#1607F#4S#5P#N看招啊啊！！\x02",
    )
    #Auto

    BeginChrThread(0x2E, 3, 0, 39)
    SetChrChipByIndex(0x19, 0x26)
    BeginChrThread(0x19, 3, 0, 67)
    Sleep(400)

    def lambda_7C04():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_7C04)

    def lambda_7C11():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_7C11)

    def lambda_7C1E():
        OP_9D(0xFE, 0x6428, 0xFFFFE69C, 0xFFFF728E, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7C1E)

    def lambda_7C3B():
        OP_9D(0xFE, 0x6554, 0xFFFFE69C, 0xFFFF60DC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7C3B)
    Sound(814, 0, 100, 0)
    Sleep(600)

    #C0266
    ChrTalk(
        0x18,
        "#9A#30W#0402F#5P先走一步喽～！\x02",
    )
    #Auto

    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    OP_9D(0x18, 0x76CA, 0xFFFFE69C, 0xFFFF6AB4, 0x320, 0x1770)
    Sound(814, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 36)
    OP_95(0x18, 22720, -6500, -37590, 7000, 0x0)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0267
    AnonymousTalk(
        0x1B,
        (
            "#4A#30W#2103F罗伊德＆兰迪选手\x01",
            "堪堪避开了铁桶！\x02",
        )
    )
    #Auto

    BeginChrThread(0x2A, 3, 0, 37)
    BeginChrThread(0x2B, 3, 0, 38)
    OP_95(0x18, 21220, -2500, -25410, 7000, 0x0)
    Sleep(1400)
    OP_57(0x0)
    OP_5A()

    #A0268
    AnonymousTalk(
        0x1B,
        (
            "#4A#30W#2101F但是，动作和节奏已经被破坏，\x01",
            "看来将会损失一些时间了吧！？\x02",
        )
    )
    #Auto

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    Jump("loc_802F")

    label("loc_7D73")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0269
    ChrTalk(
        0x19,
        "#6A#30W#1607F#4S#5P#N看招啊啊！！\x02",
    )
    #Auto

    BeginChrThread(0x2E, 3, 0, 39)
    SetChrChipByIndex(0x19, 0x26)
    BeginChrThread(0x19, 3, 0, 67)
    Sleep(300)
    SetChrChip(0x0, 0x2A, 0x64, 0x1F4)
    SetChrChip(0x0, 0x2B, 0x64, 0x1F4)

    def lambda_7DD4():
        OP_9D(0xFE, 0x6978, 0xFFFFE69C, 0xFFFF6C58, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7DD4)

    def lambda_7DF1():
        OP_9D(0xFE, 0x6978, 0xFFFFE69C, 0xFFFF66E0, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7DF1)
    Sound(250, 0, 100, 0)
    Sleep(100)
    EndChrThread(0x18, 0x2)

    def lambda_7E1B():
        OP_9D(0xFE, 0x76CA, 0xFFFFE69C, 0xFFFF6AB4, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7E1B)
    Sound(814, 0, 100, 0)
    OP_68(31000, -5040, -38330, 1500)
    MoveCamera(59, 6, 0, 1500)
    OP_6E(420, 1500)
    SetCameraDistance(21000, 1500)
    Sleep(600)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_7E73():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_7E73)
    Sleep(600)
    SetChrChipByIndex(0x18, 0x29)

    def lambda_7E87():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_7E87)
    Sleep(200)
    SetChrChip(0x0, 0x18, 0x64, 0x1F4)

    def lambda_7E9F():
        OP_9D(0xFE, 0x6860, 0xFFFFE69C, 0xFFFF6D2A, 0x64, 0x2BC)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7E9F)
    Sound(250, 0, 100, 0)
    Sound(541, 0, 100, 0)

    def lambda_7EC8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_7EC8)

    def lambda_7ED5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_7ED5)

    def lambda_7EE2():
        OP_9D(0xFE, 0x7530, 0xFFFFE69C, 0xFFFF7040, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7EE2)

    def lambda_7EFF():
        OP_9D(0xFE, 0x7530, 0xFFFFE69C, 0xFFFF62F8, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7EFF)
    Sound(814, 0, 100, 0)
    Sleep(200)
    TurnDirection(0x18, 0x2A, 500)
    SetChrChip(0x1, 0x18, 0x0, 0x0)
    SetChrChip(0x1, 0x2A, 0x0, 0x0)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    BeginChrThread(0x19, 3, 0, 36)

    #C0270
    ChrTalk(
        0x18,
        "#5A#30W#0402F#5P哈哈，干得不错嘛！\x02",
    )
    #Auto

    SetChrChipByIndex(0x18, 0x2A)
    Sleep(700)
    SetChrChip(0x1, 0x2A, 0x0, 0x0)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    BeginChrThread(0x2A, 3, 0, 37)
    BeginChrThread(0x2B, 3, 0, 38)
    OP_95(0x18, 21220, -2500, -25410, 7000, 0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, -10, -1, 3)

    #A0271
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2104F罗伊德＆兰迪选手\x01",
            "大胆地避开了铁桶！\x02",
        )
    )
    #Auto

    Sleep(4000)
    OP_57(0x0)
    OP_5A()
    
    #A0272
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2100F又躲过了瓦吉选手的攻击，\x01",
            "通过了第二确认点！\x02",
        )
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Jump("loc_802F")

    label("loc_802F")

    Fade(500)
    BeginChrThread(0x2A, 3, 0, 40)
    BeginChrThread(0x2B, 3, 0, 41)
    SetChrPos(0x19, 43020, -2500, -21880, 135)
    SetChrPos(0x18, 42830, -2500, -23790, 45)
    OP_6B(0x2A)
    OP_68(21840, -4500, -37170, 0)
    MoveCamera(1, 20, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(67, 12, 0, 5000)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 42)
    BeginChrThread(0x18, 3, 0, 43)
    Sleep(1500)
    Sleep(500)

    #C0273
    ChrTalk(
        0x2B,
        "#5P#6A#30W#0301F（怎么办……！？）\x02",
    )
    #Auto

    Sleep(800)

    #C0274
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0007F（……上吧……！）\x02",
    )
    #Auto

    Sleep(1200)
    EndChrThread(0x2B, 0x3)
    EndChrThread(0x2A, 0x3)
    OP_6B(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【各个击破】\x01",      # 0
            "【组合战技】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8166"),
        (1, "loc_83C2"),
        (SWITCH_DEFAULT, "loc_861D"),
    )


    label("loc_8166")

    OP_68(42290, -500, -23200, 700)

    def lambda_817C():
        OP_95(0xFE, 42100, -2500, -22410, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_817C)

    def lambda_8196():
        OP_9D(0xFE, 0xA154, 0xFFFFFE0C, 0xFFFFA20E, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8196)
    Sound(854, 0, 100, 0)
    Sleep(700)
    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    Call(0, 65)
    LoadEffect(0x3, "event\\ev301_00.eff")
    EventBegin(0x0)
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_822C():

        label("loc_822C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_822C")

    QueueWorkItem2(0x2A, 2, lambda_822C)

    def lambda_823E():

        label("loc_823E")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_823E")

    QueueWorkItem2(0x2B, 2, lambda_823E)
    SetChrPos(0x2A, 40970, -2500, -22390, 21)
    SetChrPos(0x2B, 41410, -2500, -24040, 135)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    SetChrChipByIndex(0x18, 0x28)
    SetChrChipByIndex(0x19, 0x37)

    def lambda_829C():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_829C)
    BeginChrThread(0x19, 3, 0, 68)
    Sound(514, 0, 100, 0)
    SetChrPos(0x18, 42120, -2500, -20350, 180)
    SetChrPos(0x19, 43290, -2500, -24680, 331)
    OP_6B(0x2A)
    OP_68(41050, -500, -22430, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    OP_E5()
    FadeToBright(500, 0)
    OP_0D()

    #C0275
    ChrTalk(
        0x19,
        "#11P#8A#30W#1607F唔……！？\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x18,
        "#5P#12A#30W#0404F哈哈，这下中招了呢。\x02",
    )
    #Auto

    Sleep(2000)
    OP_57(0x0)
    OP_5A()

    #C0277
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0000F先走一步了！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x2A, 3, 0, 44)

    #C0278
    ChrTalk(
        0x2B,
        "#5P#8A#30W#0309F哈哈，别往心里去啊～！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x36)
    BeginChrThread(0x2B, 3, 0, 45)
    Jump("loc_861D")

    label("loc_83C2")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(42290, -500, -23200, 700)

    def lambda_83EB():
        OP_95(0xFE, 42100, -2500, -22410, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_83EB)

    def lambda_8405():
        OP_9D(0xFE, 0xA154, 0xFFFFFE0C, 0xFFFFA20E, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8405)
    Sound(854, 0, 100, 0)
    Sleep(700)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x3, "event\\ev301_00.eff")
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_849B():

        label("loc_849B")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_849B")

    QueueWorkItem2(0x2A, 2, lambda_849B)

    def lambda_84AD():

        label("loc_84AD")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_84AD")

    QueueWorkItem2(0x2B, 2, lambda_84AD)
    SetChrPos(0x2A, 40970, -2500, -22390, 21)
    SetChrPos(0x2B, 41410, -2500, -24040, 135)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    SetChrChipByIndex(0x18, 0x38)
    SetChrChipByIndex(0x19, 0x37)
    BeginChrThread(0x18, 3, 0, 68)
    BeginChrThread(0x19, 3, 0, 68)
    SetChrPos(0x18, 42120, -2500, -20350, 180)
    SetChrPos(0x19, 43290, -2500, -24680, 331)
    OP_6B(0x2A)
    OP_68(41050, -500, -22430, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    OP_E5()
    Sound(514, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0279
    ChrTalk(
        0x19,
        "#8A#30W#1605F#11P什么……！？\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x18,
        "#8A#30W#0410F#5P嘿，不错嘛……\x02",
    )
    #Auto

    Sleep(2500)
    OP_57(0x0)
    OP_5A()

    #C0281
    ChrTalk(
        0x2A,
        "#8A#30W#0001F#5P不好意思……！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x2A, 3, 0, 44)

    #C0282
    ChrTalk(
        0x2B,
        "#8A#30W#0300F#5P先走一步啦！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x36)
    BeginChrThread(0x2B, 3, 0, 45)
    Jump("loc_861D")

    label("loc_861D")

    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 47)
    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    Sleep(3000)
    Fade(1000)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(9060, 1990, -12040, 0)
    MoveCamera(44, 31, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22150, 0)
    OP_67(0x0)
    OP_6B(0x2A)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0283
    AnonymousTalk(
        0x1B,
        "#18A#30W#2100F好！第二圈了！\x02",
    )
    #Auto

    Sleep(1000)
    OP_57(0x0)
    OP_5A()

    #A0284
    AnonymousTalk(
        0x1B,
        (
            "#20A#50W#2100F罗伊德＆兰迪选手\x01",
            "目前保持领先……\x02",
        )
    )
    #Auto

    Sleep(2400)
    OP_57(0x0)
    OP_5A()

    #A0285
    AnonymousTalk(
        0x1B,
        "#6A#20W#2109F通过第一确认点！\x02",
    )
    #Auto

    SetChrPos(0x16, 1080, 0, -9140, 272)
    SetChrPos(0x17, 1580, 0, -7990, 267)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 32)
    BeginChrThread(0x16, 3, 0, 33)
    Sleep(2200)
    OP_57(0x0)
    OP_5A()

    OP_6B(0xFF)
    OP_67(0x1)

    #A0286
    AnonymousTalk(
        0x1B,
        (
            "#15A#20W#2105F噢噢！\x01",
            "艾丝蒂尔＆约修亚选手\x01",
            "以非常惊人的速度追上来了！\x02",
        )
    )
    #Auto

    Sleep(4000)
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-4680, -1840, -26700, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    BeginChrThread(0x2A, 3, 0, 48)
    BeginChrThread(0x2B, 3, 0, 49)
    OP_6B(0x2A)
    MoveCamera(359, 18, 0, 5000)
    Sleep(1000)

    #C0287
    ChrTalk(
        0x2A,
        "#6A#30W#0008F#5P唔……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x2B,
        "#8A#30W#0301F#5P嘁，追上来了啊……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(2300)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x2A, 0x3)
    OP_95(0x2A, 35200, -6490, -38160, 7000, 0x0)

    #C0289
    ChrTalk(
        0x2B,
        "#6A#30W#0307F#5P喂，罗伊德！\x02",
    )
    #Auto

    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0x2A, 0x32)
    OP_A1(0x2A, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_889F():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_889F)
    Sleep(300)

    #C0290
    ChrTalk(
        0x2A,
        "#6A#30W#0005F#5P哎……？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6B(0xFF)
    OP_68(36410, -4540, -38600, 5000)
    MoveCamera(339, 31, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(22500, 5000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x40, 34000, -7000, -36000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x8)
    FadeToDark(300, 16777215, 100)
    Sleep(500)

    #C0291
    ChrTalk(
        0x2A,
        "#8A#30W#0007F#5P什么……！？\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x2B,
        "#8A#30W#0310F石灰吗……！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetMessageWindowPos(14, -10, -1, 3)

    #A0293
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2105F噢噢！？\x01",
            "什么什么！这白烟是～！？\x02",
        )
    )
    #Auto

    Sleep(2800)
    OP_57(0x0)
    OP_5A()

    #A0294
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2110F莫非是艾丝蒂尔队\x01",
            "设下的机关吗～！？\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x16, 3, 0, 50)
    BeginChrThread(0x17, 3, 0, 51)

    #C0295
    ChrTalk(
        0x16,
        "#6A#30W#0802F#5P#N抱歉啦～！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1500)

    #C0296
    ChrTalk(
        0x17,
        "#6A#30W#0900F#5P先走一步！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x2A,
        "#9A#30W#0013F#5P唔……\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x2B,
        "#9A#30W#0307F快追上去……！\x02",
    )
    #Auto

    CloseMessageWindow()
    FadeToBright(1300, 16777215)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_8AAA():

        label("loc_8AAA")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8AAA")

    QueueWorkItem2(0x16, 2, lambda_8AAA)
    SetChrChipByIndex(0x17, 0x2E)

    def lambda_8AC0():

        label("loc_8AC0")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8AC0")

    QueueWorkItem2(0x17, 2, lambda_8AC0)
    SetChrPos(0x17, 37300, -2500, -22500, 270)
    SetChrPos(0x16, 37800, -2500, -24000, 270)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x19, 28020, -2500, -23450, 308)
    SetChrPos(0x18, 28260, -2500, -24990, 128)
    BeginChrThread(0x2A, 3, 0, 52)
    BeginChrThread(0x2B, 3, 0, 53)
    Sleep(1500)
    OP_68(23210, -4540, -36350, 0)
    MoveCamera(48, 16, 0, 0)
    OP_6E(960, 0)
    SetCameraDistance(10000, 0)
    Sleep(2400)
    OP_68(22810, -500, -24060, 0)
    MoveCamera(120, 35, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(26000, 0)
    Sleep(1500)
    OP_68(34300, 50, -22710, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(840, 0)
    SetCameraDistance(11000, 0)
    Sleep(50)
    OP_E6()

    #C0299
    ChrTalk(
        0x16,
        "#0800F#11P来了呢……！\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x17,
        "#0901F#11P要突围了哦……！\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x2A,
        "#0013F#5P（唔……！）\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x2D)
    SetChrChipByIndex(0x17, 0x30)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChipByIndex(0x2A, 0x33)

    def lambda_8C34():
        OP_99(0xFE, 0x2B, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8C34)

    def lambda_8C48():
        OP_99(0xFE, 0x2A, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8C48)

    def lambda_8C5C():
        OP_99(0xFE, 0x16, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8C5C)

    def lambda_8C70():
        OP_99(0xFE, 0x17, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8C70)
    Sleep(150)
    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x2B, 0x2)
    EndChrThread(0x2A, 0x2)
    EndChrThread(0x16, 0x2)
    EndChrThread(0x17, 0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【各个击破】\x01",      # 0
            "【组合战技】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_8CE5():
        OP_99(0xFE, 0x2B, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8CE5)

    def lambda_8CF9():
        OP_99(0xFE, 0x2A, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8CF9)

    def lambda_8D0D():
        OP_99(0xFE, 0x16, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8D0D)

    def lambda_8D21():
        OP_99(0xFE, 0x17, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8D21)
    Sleep(150)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8D49"),
        (1, "loc_9295"),
        (SWITCH_DEFAULT, "loc_9685"),
    )


    label("loc_8D49")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "event\\ev302_01.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    OP_68(35610, -500, -24250, 0)
    MoveCamera(38, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_8E3A():

        label("loc_8E3A")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E3A")

    QueueWorkItem2(0x2A, 2, lambda_8E3A)

    def lambda_8E4C():

        label("loc_8E4C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E4C")

    QueueWorkItem2(0x2B, 2, lambda_8E4C)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_8E66():

        label("loc_8E66")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E66")

    QueueWorkItem2(0x17, 2, lambda_8E66)

    def lambda_8E78():

        label("loc_8E78")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E78")

    QueueWorkItem2(0x16, 2, lambda_8E78)
    SetChrPos(0x17, 34690, -2500, -22950, 89)
    SetChrPos(0x16, 33910, -2500, -24380, 89)
    SetChrPos(0x2A, 36880, -2500, -23410, 270)
    SetChrPos(0x2B, 37460, -2500, -24500, 270)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    FadeToBright(500, 0)
    OP_0D()

    #C0302
    ChrTalk(
        0x16,
        "#1P#30W#0809F打得漂亮！\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        "#5P#30W#0902F先走一步了！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x2D)

    def lambda_8F3A():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8F3A)
    Sleep(300)
    SetChrChipByIndex(0x17, 0x30)

    def lambda_8F5B():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8F5B)

    #C0304
    ChrTalk(
        0x2A,
        "#30W#0013F#11P唔……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x2B, 0x5A, 0x1F4)
    OP_68(36790, -500, -24050, 1000)

    #C0305
    ChrTalk(
        0x2B,
        (
            "#30W#0307F#5P赶快按下确认按钮，\x01",
            "然后追上去吧──\x02",
        )
    )

    Sleep(500)
    OP_93(0x2A, 0x5A, 0x1F4)
    CloseMessageWindow()
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    Sound(1431, 255, 100, 0)
    Sleep(1500)

    #C0306
    ChrTalk(
        0x18,
        "#8A#30W#0402F#2P东张西望可是大忌哦……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_93(0x2B, 0x10E, 0x320)
    Sleep(500)
    EndChrThread(0x2B, 0x2)
    MoveCamera(320, 27, 0, 2000)
    OP_93(0x2A, 0x10E, 0x320)
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x19, 0x27)

    def lambda_9090():
        OP_99(0xFE, 0x2B, 0xFFFFFC18, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9090)

    def lambda_90A4():
        OP_99(0xFE, 0x2A, 0xFFFFFC18, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_90A4)
    Sound(1791, 255, 100, 2)
    Sleep(1050)
    OP_49()
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(834, 0, 100, 0)
    OP_68(38120, -500, -23640, 500)
    MoveCamera(358, 27, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(24500, 500)
    OP_49()
    Sleep(30)
    SetChrChipByIndex(0x2A, 0x3B)
    BeginChrThread(0x2A, 3, 0, 68)
    Sound(514, 0, 100, 0)

    def lambda_911B():
        OP_9D(0xFE, 0x9CC2, 0xFFFFF63C, 0xFFFFA9D4, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_911B)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_913C():

        label("loc_913C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_913C")

    QueueWorkItem2(0x18, 2, lambda_913C)
    SetChrChipByIndex(0x2B, 0x3C)
    BeginChrThread(0x2B, 3, 0, 68)

    def lambda_9158():
        OP_9D(0xFE, 0x9D4E, 0xFFFFF63C, 0xFFFFA04C, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9158)
    Sound(1318, 255, 100, 1)

    #C0307
    ChrTalk(
        0x2A,
        "#11P#6A#30W#0010F呜啊……\x02",
    )
    #Auto


    #C0308
    ChrTalk(
        0x2B,
        "#12P#6A#30W#0310F啊啊……\x02",
    )
    #Auto

    Sleep(200)
    BeginChrThread(0x19, 3, 0, 54)
    Sleep(200)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_91C7():

        label("loc_91C7")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_91C7")

    QueueWorkItem2(0x18, 2, lambda_91C7)
    BeginChrThread(0x18, 3, 0, 55)
    Sleep(1000)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0309
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2105F怎么回事，怎么回事！\x01",
            "从后面追上来的瓦吉＆瓦鲁多选手\x01",
            "成功向罗伊德队发动了奇袭！\x02",
        )
    )
    #Auto

    Sleep(5200)
    OP_57(0x0)
    OP_5A()

    #A0310
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2110F而且通过了第三确认点，\x01",
            "转而追击艾丝蒂尔队了！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Jump("loc_9685")

    label("loc_9295")

    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "event\\ev302_01.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    OP_68(35610, -500, -24250, 0)
    MoveCamera(38, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x2A, 0x3B)
    SetChrChipByIndex(0x2B, 0x3C)
    BeginChrThread(0x2A, 3, 0, 68)
    BeginChrThread(0x2B, 3, 0, 68)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x19, 0x27)
    SetChrPos(0x17, 34690, -2500, -22950, 89)
    SetChrPos(0x16, 33910, -2500, -24380, 89)
    SetChrPos(0x2A, 40130, -2500, -22060, 270)
    SetChrPos(0x2B, 40270, -2500, -24500, 270)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    Sound(514, 0, 100, 0)
    OP_68(36790, -500, -24050, 1500)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)

    #C0311
    ChrTalk(
        0x16,
        "#0800F#1P告辞啦～！\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x17,
        "#0901F#5P先走了！\x02",
    )

    CloseMessageWindow()

    def lambda_9441():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9441)
    Sleep(300)

    def lambda_945E():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_945E)

    #C0313
    ChrTalk(
        0x2A,
        "#0010F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x2B,
        "#0310F#11P嘁，输了一招……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    Sound(1431, 255, 100, 0)
    Sleep(1500)

    #C0315
    ChrTalk(
        0x18,
        "#0409F#2P战况愈发白热化了呢！\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_951E():
        OP_99(0xFE, 0x2B, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_951E)
    OP_68(38120, -500, -23640, 3500)
    MoveCamera(358, 27, 0, 3500)
    OP_6E(400, 3500)
    SetCameraDistance(24500, 3500)
    ClearChrFlags(0x2A, 0x1000)
    ClearChrFlags(0x2B, 0x1000)
    OP_99(0x19, 0x2A, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_957C():

        label("loc_957C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_957C")

    QueueWorkItem2(0x19, 2, lambda_957C)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9592():

        label("loc_9592")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9592")

    QueueWorkItem2(0x18, 2, lambda_9592)

    #C0316
    ChrTalk(
        0x19,
        "#1602F哼哼……真是丢脸啊！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x18,
        "#5P#0402F好，现在就来报仇吧！\x02",
    )

    CloseMessageWindow()
    Sound(1809, 255, 100, 1)
    BeginChrThread(0x19, 3, 0, 54)
    Sleep(200)
    BeginChrThread(0x18, 3, 0, 55)
    Sleep(500)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0318
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2100F瓦吉＆瓦鲁多选手\x01",
            "越过了倒地的罗伊德队，\x01",
            "通过了第三确认点！\x02",
        )
    )
    #Auto

    Sleep(5200)
    OP_57(0x0)
    OP_5A()

    #A0319
    AnonymousTalk(
        0x1B,
        "#8A#30W#2100F转而追击艾丝蒂尔队了！\x02",
    )
    #Auto

    Sleep(2400)
    OP_57(0x0)
    OP_5A()
    Jump("loc_9685")

    label("loc_9685")

    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_969D():

        label("loc_969D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_969D")

    QueueWorkItem2(0x2A, 2, lambda_969D)
    Sound(804, 0, 100, 0)
    OP_A1(0x2B, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_96C2():

        label("loc_96C2")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_96C2")

    QueueWorkItem2(0x2B, 2, lambda_96C2)

    #C0320
    ChrTalk(
        0x2A,
        (
            "#0010F#11P呜……\x02\x03",

            "#0008F可恶，这样下去的话……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_970A():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_970A)
    Sleep(300)
    Sound(1370, 255, 100, 0)
    Sleep(150)
    EndChrThread(0x2B, 0x2)
    Sleep(1500)
    #Sound(1371, 255, 100, 0)
    Sleep(100)

    #C0321
    ChrTalk(
        0x2B,
        "#0312F#11P#60W#12A……哈哈哈哈哈哈哈哈哈……！\x02",
    )
    #Auto

    Sleep(1000)

    def lambda_9775():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9775)
    Sleep(2000)
    Sound(1310, 255, 100, 0)
    SetChrChipByIndex(0x2B, 0x3D)
    OP_A1(0x2B, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x0)

    def lambda_9799():
        OP_A6(0xFE, 0x64, 0x0, 0x320, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9799)
    CloseMessageWindow()
    PlayEffect(0x0, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    OP_68(40200, -500, -24500, 1500)
    MoveCamera(45, 27, 0, 1500)
    OP_6E(240, 1500)
    SetCameraDistance(24500, 1500)
    Sleep(1500)
    OP_6E(350, 0)
    PlayEffect(0x1, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_A1(0x2B, 0x7D0, 0x1, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(800)

    #C0322
    ChrTalk(
        0x2A,
        "#0011F#5P兰、兰迪？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_98B0():

        label("loc_98B0")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_98B0")

    QueueWorkItem2(0x2B, 2, lambda_98B0)
    Sleep(500)

    #C0323
    ChrTalk(
        0x2B,
        (
            "#0312F#11P很好嘛！越来越令人兴奋了！\x02\x03",

            "既然如此，\x01",
            "就让我好好开心一下吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrChipByIndex(0x16, 0x2B)
    BeginChrThread(0x17, 3, 0, 32)
    BeginChrThread(0x16, 3, 0, 33)
    OP_68(-7310, 2000, -9830, 0)
    MoveCamera(317, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_68(-19630, 2000, -10660, 4000)
    MoveCamera(297, 27, 0, 4000)
    OP_6E(400, 4000)
    SetCameraDistance(23270, 4000)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0324
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2103F好！艾丝蒂尔队通过广场，\x01",
            "进入第三圈！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    #A0325
    AnonymousTalk(
        0x1B,
        (
            "#20A#30W#2101F如果他们像这样一马当先地跑下去，\x01",
            "胜利应该就唾手可得了吧……\x02",
        )
    )
    #Auto

    Sleep(400)
    EndChrThread(0x16, 0x3)
    OP_93(0x16, 0x5A, 0x1F4)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_9A40():

        label("loc_9A40")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A40")

    QueueWorkItem2(0x16, 2, lambda_9A40)
    Sleep(300)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x2E)

    def lambda_9A5D():

        label("loc_9A5D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A5D")

    QueueWorkItem2(0x17, 2, lambda_9A5D)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2500)
    OP_57(0x0)
    OP_5A()

    SetChrChipByIndex(0x19, 0x25)

    def lambda_9A7D():

        label("loc_9A7D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A7D")

    QueueWorkItem2(0x19, 2, lambda_9A7D)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9A93():

        label("loc_9A93")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A93")

    QueueWorkItem2(0x18, 2, lambda_9A93)
    SetChrPos(0x19, -13190, 0, -10450, 270)
    SetChrPos(0x18, -10130, 4300, -7240, 270)
    OP_68(-15530, 2000, -10670, 700)
    OP_6E(380, 700)
    SetCameraDistance(23500, 700)

    #A0326
    AnonymousTalk(
        0x1B,
        (
            "#20A#30W#2105F噢～要取胜果然\x01",
            "没那么简单啊！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    #C0327
    ChrTalk(
        0x16,
        "#0801F#5P来了吗──嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(700)

    #C0328
    ChrTalk(
        0x16,
        "#0805F#5P哎，为什么只有一个人……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0329
    ChrTalk(
        0x17,
        "#0907F#5P#N难道……！？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13540, 3200, -8170, 0)
    MoveCamera(312, 32, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    Sleep(500)

    #C0330
    ChrTalk(
        0x18,
        "#0402F#16A──猜对了。\x02",
    )
    #Auto

    Sleep(1500)
    OP_68(-19160, 1990, -9840, 2000)
    MoveCamera(312, 55, 0, 2000)
    OP_6E(1080, 2000)
    SetCameraDistance(9000, 2000)
    EndChrThread(0x18, 0x2)
    BeginChrThread(0x18, 3, 0, 56)
    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x19, 0x27)

    def lambda_9C37():
        OP_99(0xFE, 0x17, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9C37)
    Sleep(1400)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x18, 0xFF)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200002, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x4, "event\\ev303_00.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    LoadEffect(0x5, "event\\ev311_00.eff")
    LoadEffect(0x6, "event\\eva01_00.eff")
    EventBegin(0x0)
    Call(0, 65)
    OP_68(-18550, 1810, -10400, 0)
    MoveCamera(37, 33, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_9D2F():

        label("loc_9D2F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9D2F")

    QueueWorkItem2(0x19, 2, lambda_9D2F)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9D45():

        label("loc_9D45")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9D45")

    QueueWorkItem2(0x18, 2, lambda_9D45)
    SetChrPos(0x16, -16760, 0, -9580, 270)
    SetChrPos(0x17, -16400, 0, -11240, 270)
    SetChrPos(0x19, -19960, 0, -11410, 90)
    SetChrPos(0x18, -20100, 0, -9630, 90)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    FadeToBright(500, 0)
    OP_0D()

    #C0331
    ChrTalk(
        0x16,
        "#0802F#11P干得不错嘛！\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x19,
        "#1602F#6P#N哈，彼此彼此！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0333
    ChrTalk(
        0x18,
        (
            "#0402F#5P呵呵……\x01",
            "相当厉害嘛，小兄弟。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x17,
        (
            "#0904F#11P你也一样……\x02\x03",

            "#0901F──艾丝蒂尔，走了！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x16,
        "#0801F#5P嗯！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x16, 0x2D)

    def lambda_9E82():
        OP_95(0xFE, -11620, 0, -14190, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9E82)
    Sleep(400)
    EndChrThread(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x30)

    def lambda_9EA7():
        OP_95(0xFE, -11250, -540, -15070, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9EA7)

    #C0336
    ChrTalk(
        0x18,
        "#0407F#5P瓦鲁多，追击！\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x19,
        "#1607F#6P#N用不着你说啊！\x02",
    )

    CloseMessageWindow()
    OP_E5()
    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 57)
    Sleep(100)
    EndChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    BeginChrThread(0x19, 3, 0, 58)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0338
    AnonymousTalk(
        0x1B,
        "#8A#30W#2100F两队正在进行着不分伯仲的激烈比拼！\x02",
    )
    #Auto

    Sleep(2400)
    OP_57(0x0)
    OP_5A()

    #A0339
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2100F按现在的局势来看，最终获胜者\x01",
            "大概将会从这两组队伍之中产生吧──\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChipByIndex(0x2A, 0x33)
    SetChrPos(0x2B, -6110, 0, -10730, 127)
    SetChrPos(0x2A, -6110, 0, -10730, 5)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0340
    ChrTalk(
        0x2B,
        "#12A#30W#0307F#4S噢噢噢噢噢噢……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_95(0x2B, -16000, 0, -10700, 11000, 0x0)
    Sound(1295, 255, 100, 0)

    def lambda_A036():
        OP_95(0xFE, -15720, 0, -10810, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A036)
    SetChrChipByIndex(0x2B, 0x35)
    SetChrFlags(0x2B, 0x1000)

    def lambda_A059():
        OP_A0(0xFE, 4000, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A059)
    Sound(532, 0, 100, 0)
    OP_96(0x2B, 0xFFFFADF8, 0x0, 0xFFFFD544, 0x4E20, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -21800, 1200, -10600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -21300, 1200, -10600, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_71(0xB, 0x10, 0x19, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    Sound(899, 0, 100, 0)
    SetChrChipByIndex(0x2B, 0x36)
    OP_96(0x2B, 0xFFFFB5C8, 0x0, 0xFFFFD634, 0x2EE0, 0x0)

    def lambda_A12F():
        OP_95(0xFE, -11250, -540, -15070, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A12F)
    Sleep(700)

    def lambda_A14C():
        OP_95(0xFE, -11620, 0, -14190, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A14C)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0341
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2105F厉、厉害……！\x01",
            "兰迪选手的爆发力好惊人啊！\x02",
        )
    )
    #Auto

    Sleep(4200)
    OP_57(0x0)
    OP_5A()

    #A0342
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2106F不过，那个装置……\x01",
            "好像完全被毁掉了吧？\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearMapObjFlags(0xC, 0x4)
    OP_68(30200, -4540, -39130, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_6B(0x17)
    MoveCamera(60, 27, 0, 5000)
    BeginChrThread(0x18, 3, 0, 59)
    BeginChrThread(0x19, 3, 0, 60)
    BeginChrThread(0x16, 3, 0, 61)
    BeginChrThread(0x17, 3, 0, 62)
    Sleep(5000)
    OP_6B(0xFF)
    OP_68(33400, -500, -24080, 0)
    MoveCamera(91, 25, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(14000, 3000)
    MoveCamera(91, 25, 5, 3000)
    Sleep(1000)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x2A, 25000, -1000, -27210, 90)

    #C0343
    ChrTalk(
        0x19,
        "#8A#30W#1605F#11P怎、怎么回事！？\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #C0344
    ChrTalk(
        0x17,
        "#8A#30W#0901F#12P是绳索机关……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0007F──上钩了啊！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(41380, -500, -22950, 3000)
    MoveCamera(80, 16, 5, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(16000, 3000)
    BeginChrThread(0x2A, 3, 0, 64)
    Sleep(4000)
    OP_68(37090, -500, -23670, 3000)
    MoveCamera(72, 30, 5, 7000)

    #C0346
    ChrTalk(
        0x16,
        "#10A#30W#0801F#6P#N呜……！\x02",
    )
    #Auto

    OP_A1(0x16, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x2D)
    OP_95(0x16, 38410, -2490, -22860, 6000, 0x0)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_A3C1():

        label("loc_A3C1")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A3C1")

    QueueWorkItem2(0x16, 2, lambda_A3C1)
    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x19,
        "#8A#1607F#12P#N休想过去啊，看招！！\x02",
    )
    #Auto

    OP_A1(0x19, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x27)
    OP_95(0x19, 38260, -2490, -24380, 6000, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_A427():

        label("loc_A427")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A427")

    QueueWorkItem2(0x19, 2, lambda_A427)
    CloseMessageWindow()
    OP_E6()
    Sound(804, 0, 100, 0)
    OP_A1(0x17, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x17, 0x2E)

    #C0348
    ChrTalk(
        0x17,
        "#0907F#11P等一下……！\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x18, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x18, 0x28)

    #C0349
    ChrTalk(
        0x18,
        "#0410F#5P另外一个人呢──！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1373, 255, 100, 0)
    Sleep(1000)

    def lambda_A4AC():

        label("loc_A4AC")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4AC")

    QueueWorkItem2(0x19, 0, lambda_A4AC)
    Sleep(50)

    def lambda_A4C1():

        label("loc_A4C1")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4C1")

    QueueWorkItem2(0x16, 0, lambda_A4C1)
    Sleep(100)

    def lambda_A4D6():

        label("loc_A4D6")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4D6")

    QueueWorkItem2(0x17, 0, lambda_A4D6)
    Sleep(50)

    def lambda_A4EB():

        label("loc_A4EB")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4EB")

    QueueWorkItem2(0x18, 0, lambda_A4EB)
    OP_68(33430, -500, -22930, 4000)
    MoveCamera(56, 30, 5, 4000)
    SetChrPos(0x2B, 24970, -2400, -21190, 0)

    #C0350
    ChrTalk(
        0x2B,
        "#14A#30W#0312F#5P#N掉以轻心可是大忌！！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x2B, 3, 0, 63)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    Fade(500)
    OP_68(34310, 4450, -21190, 0)
    MoveCamera(39, 10, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sleep(700)
    OP_6B(0x2B)
    SetChrChip(0x0, 0x2B, 0x64, 0x3E8)
    SetChrChipByIndex(0x2B, 0x35)

    def lambda_A5D8():
        OP_A0(0xFE, 500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A5D8)
    SetChrFlags(0x2B, 0x4)
    MoveCamera(317, 48, 5, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(16000, 1000)
    Sound(1297, 255, 100, 0)
    Sound(854, 0, 100, 0)
    OP_9D(0x2B, 0x8E94, 0xFFFFF63C, 0xFFFFA236, 0xFA0, 0xFA0)
    Sound(808, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetMapObjFlags(0xC, 0x4)
    PlayEffect(0x4, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(834, 0, 100, 0)
    Sound(813, 0, 100, 0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    TurnDirection(0x17, 0x2B, 0)
    TurnDirection(0x18, 0x2B, 0)
    TurnDirection(0x16, 0x2B, 0)
    TurnDirection(0x19, 0x2B, 0)
    SetChrChipByIndex(0x17, 0x3A)
    SetChrChipByIndex(0x18, 0x38)
    SetChrChipByIndex(0x16, 0x39)
    SetChrChipByIndex(0x19, 0x37)
    Sound(514, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 68)
    BeginChrThread(0x18, 3, 0, 68)
    BeginChrThread(0x16, 3, 0, 68)
    BeginChrThread(0x19, 3, 0, 68)
    Sound(1741, 255, 100, 1)

    def lambda_A6EA():
        OP_9D(0xFE, 0x8340, 0xFFFFF63C, 0xFFFF9EBC, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A6EA)
    Sound(1404, 255, 100, 2)

    def lambda_A70D():
        OP_9D(0xFE, 0x8322, 0xFFFFF63C, 0xFFFFA6D2, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_A70D)
    Sound(1669, 255, 100, 3)

    def lambda_A730():
        OP_9D(0xFE, 0x9970, 0xFFFFF63C, 0xFFFFA93E, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_A730)
    Sound(1800, 255, 100, 4)

    def lambda_A753():
        OP_9D(0xFE, 0x9A6A, 0xFFFFF63C, 0xFFFF9F52, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_A753)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(100)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    Sleep(500)
    CancelBlur(1000)
    Sleep(1500)
    OP_6B(0xFF)
    OP_6E(500, 3000)
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x2A, 0x33)
    OP_95(0x2A, 38500, -2500, -23850, 5000, 0x0)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_A7C8():

        label("loc_A7C8")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A7C8")

    QueueWorkItem2(0x2A, 2, lambda_A7C8)

    #C0351
    ChrTalk(
        0x2A,
        "#0000F干得漂亮！兰迪！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_A7FA():

        label("loc_A7FA")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A7FA")

    QueueWorkItem2(0x2B, 2, lambda_A7FA)
    TurnDirection(0x2B, 0x2A, 500)

    #C0352
    ChrTalk(
        0x2B,
        (
            "#0307F#5P噢噢！\x01",
            "就这样一直冲到终点吧！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x2B, 0x2)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2B, 0x36)

    def lambda_A851():
        OP_95(0xFE, 21840, -2500, -24140, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A851)
    Sleep(300)
    SetChrChipByIndex(0x2A, 0x33)

    def lambda_A872():
        OP_95(0xFE, 21840, -2500, -24140, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A872)
    Sleep(1500)
    Fade(500)
    OP_68(8660, 1940, -13150, 0)
    MoveCamera(51, 27, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7500, 0)
    SetChrPos(0x1D, 11600, -10, -9000, 135)
    SetChrPos(0x1E, 12950, -10, -8500, 135)
    SetChrPos(0x1F, 12350, -10, -7600, 135)
    SetChrPos(0x20, 11800, -10, -6250, 135)
    SetChrPos(0x21, 11200, -10, -7700, 135)
    SetChrPos(0x22, 7900, -10, -6300, 135)
    SetChrPos(0x23, 8700, -10, -6800, 135)
    SetChrPos(0x24, 10250, -10, -6200, 135)
    SetChrPos(0x25, 9500, -10, -5100, 135)
    SetChrPos(0x1A, 8700, -10, -8100, 135)
    SetChrPos(0x102, 10750, 0, -11000, 135)
    SetChrPos(0x103, 10100, 0, -10600, 135)

    def lambda_A98E():

        label("loc_A98E")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A98E")

    QueueWorkItem2(0x1D, 2, lambda_A98E)

    def lambda_A9A0():

        label("loc_A9A0")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9A0")

    QueueWorkItem2(0x1E, 2, lambda_A9A0)

    def lambda_A9B2():

        label("loc_A9B2")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9B2")

    QueueWorkItem2(0x1F, 2, lambda_A9B2)

    def lambda_A9C4():

        label("loc_A9C4")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9C4")

    QueueWorkItem2(0x20, 2, lambda_A9C4)

    def lambda_A9D6():

        label("loc_A9D6")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9D6")

    QueueWorkItem2(0x21, 2, lambda_A9D6)

    def lambda_A9E8():

        label("loc_A9E8")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A9E8")

    QueueWorkItem2(0x22, 2, lambda_A9E8)

    def lambda_A9FA():

        label("loc_A9FA")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A9FA")

    QueueWorkItem2(0x23, 2, lambda_A9FA)

    def lambda_AA0C():

        label("loc_AA0C")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA0C")

    QueueWorkItem2(0x24, 2, lambda_AA0C)

    def lambda_AA1E():

        label("loc_AA1E")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA1E")

    QueueWorkItem2(0x25, 2, lambda_AA1E)

    def lambda_AA30():

        label("loc_AA30")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA30")

    QueueWorkItem2(0x1A, 2, lambda_AA30)

    def lambda_AA42():

        label("loc_AA42")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA42")

    QueueWorkItem2(0x102, 2, lambda_AA42)

    def lambda_AA54():

        label("loc_AA54")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA54")

    QueueWorkItem2(0x103, 2, lambda_AA54)
    SetChrChipByIndex(0x17, 0x30)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrChipByIndex(0x19, 0x27)
    ClearMapObjFlags(0xD, 0x4)
    SetChrPos(0x1B, 4500, 1800, -14300, 90)
    SetChrPos(0x1C, 4059, 1800, -13820, 90)
    SetChrPos(0x2A, 16940, -2170, -20310, 0)

    def lambda_AAAF():
        OP_95(0xFE, 4080, 0, -5300, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_AAAF)
    SetChrPos(0x2B, 16290, -2310, -21940, 0)

    def lambda_AADA():
        OP_95(0xFE, 2660, 0, -6540, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_AADA)
    BeginChrThread(0x101, 3, 0, 72)
    Sleep(1500)
    Sound(874, 0, 100, 0)
    Sound(881, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0353
    AnonymousTalk(
        0x1B,
        "#12A#30W#2110F#4S到达终点！！#3S\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #A0354
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2102F一番激烈的比赛之后，\x01",
            "最终获胜的是罗伊德＆兰迪队！\x02",
        )
    )
    #Auto

    Sleep(3800)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x16, 0x4)
    SetChrPos(0x18, 16940, -2170, -20310, 0)

    def lambda_ABAD():
        OP_95(0xFE, 4080, 0, -5300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_ABAD)
    Sleep(200)
    SetChrPos(0x17, 16290, -2310, -21940, 0)

    def lambda_ABDB():
        OP_95(0xFE, 2660, 0, -6540, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_ABDB)
    Sleep(200)
    SetChrPos(0x19, 16620, -2270, -21350, 0)

    def lambda_AC09():
        OP_95(0xFE, 3270, 0, -5970, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_AC09)
    SetChrPos(0x16, 16290, -2310, -21940, 0)

    def lambda_AC34():
        OP_95(0xFE, 2660, 0, -6540, 6800, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_AC34)
    OP_57(0x0)
    OP_5A()
    Sound(876, 0, 100, 0)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0355
    AnonymousTalk(
        0x1B,
        "#16A#30W#2100F紧随其后，另外两支队伍也冲过了终点！\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()

    #A0356
    AnonymousTalk(
        0x1B,
        "#16A#30W#2105F啊呀，到底是哪队先到的呢……？\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()

    #A0357
    AnonymousTalk(
        0x1B,
        (
            "#2109F算了，不管了！\x01",
            "#16A#30W总之，大家都辛苦啦～！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    #A0358
    AnonymousTalk(
        0x1B,
        "#24A#30W#2109F各位观众，请不要吝啬你们的掌声啊～！\x02",
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Sound(900, 0, 100, 0)
    Sound(874, 0, 100, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x1A, 0x2)
    Call(0, 66)
    Call(0, 80)
    Return()

    # Function_71_62CB end

    def Function_72_ADA2(): pass

    label("Function_72_ADA2")

    Sleep(1800)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x1A, 0x2)
    Sleep(4200)

    def lambda_ADDD():

        label("loc_ADDD")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_ADDD")

    QueueWorkItem2(0x1D, 2, lambda_ADDD)

    def lambda_ADEF():

        label("loc_ADEF")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_ADEF")

    QueueWorkItem2(0x1E, 2, lambda_ADEF)

    def lambda_AE01():

        label("loc_AE01")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE01")

    QueueWorkItem2(0x1F, 2, lambda_AE01)

    def lambda_AE13():

        label("loc_AE13")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE13")

    QueueWorkItem2(0x20, 2, lambda_AE13)

    def lambda_AE25():

        label("loc_AE25")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE25")

    QueueWorkItem2(0x21, 2, lambda_AE25)

    def lambda_AE37():

        label("loc_AE37")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE37")

    QueueWorkItem2(0x22, 2, lambda_AE37)

    def lambda_AE49():

        label("loc_AE49")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE49")

    QueueWorkItem2(0x23, 2, lambda_AE49)

    def lambda_AE5B():

        label("loc_AE5B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE5B")

    QueueWorkItem2(0x24, 2, lambda_AE5B)

    def lambda_AE6D():

        label("loc_AE6D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE6D")

    QueueWorkItem2(0x25, 2, lambda_AE6D)

    def lambda_AE7F():

        label("loc_AE7F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE7F")

    QueueWorkItem2(0x1A, 2, lambda_AE7F)

    def lambda_AE91():

        label("loc_AE91")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AE91")

    QueueWorkItem2(0x102, 2, lambda_AE91)

    def lambda_AEA3():

        label("loc_AEA3")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_AEA3")

    QueueWorkItem2(0x103, 2, lambda_AEA3)
    Return()

    # Function_72_ADA2 end

    def Function_73_AEB1(): pass

    label("Function_73_AEB1")

    OP_95(0xFE, 1490, 0, 7480, 2000, 0x0)
    OP_95(0xFE, 1490, 0, 30000, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_73_AEB1 end

    def Function_74_AEE4(): pass

    label("Function_74_AEE4")

    OP_95(0xFE, 2460, 0, 6790, 2000, 0x0)
    OP_95(0xFE, 2460, 0, 30000, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_74_AEE4 end

    def Function_75_AF17(): pass

    label("Function_75_AF17")

    OP_95(0xFE, 7050, 0, 3670, 2000, 0x0)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_75_AF17 end

    def Function_76_AF33(): pass

    label("Function_76_AF33")

    OP_95(0xFE, 7380, 0, 2610, 2000, 0x0)
    TurnDirection(0xFE, 0x2B, 500)
    Return()

    # Function_76_AF33 end

    def Function_77_AF4F(): pass

    label("Function_77_AF4F")

    OP_92(0xFE, 0x251C, 0xFFFFC392, 0x1F4)
    OP_95(0xFE, 9500, -300, -15470, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_77_AF4F end

    def Function_78_AF7B(): pass

    label("Function_78_AF7B")

    OP_92(0xFE, 0xFFFFF038, 0xC10CA3D7, 0x1F4)
    OP_95(0xFE, -4040, 0, -8790, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_78_AF7B end

    def Function_79_AFA7(): pass

    label("Function_79_AFA7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B033")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFE3")
    Sleep(50)
    Jump("loc_B02B")

    label("loc_AFE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AFFA")
    Sleep(150)
    Jump("loc_B02B")

    label("loc_AFFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B011")
    Sleep(200)
    Jump("loc_B02B")

    label("loc_B011")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B028")
    Sleep(300)
    Jump("loc_B02B")

    label("loc_B028")

    Sleep(400)

    label("loc_B02B")

    Sleep(50)
    Jump("Function_79_AFA7")

    label("loc_B033")

    Return()

    # Function_79_AFA7 end

    def Function_80_B034(): pass

    label("Function_80_B034")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
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
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    LoadChrToIndex("chr/ch00000.itc", 0x37)
    LoadChrToIndex("chr/ch00100.itc", 0x38)
    LoadChrToIndex("chr/ch00200.itc", 0x39)
    LoadChrToIndex("chr/ch00300.itc", 0x3A)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("apl/ch50317.itc", 0x23)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrChipByIndex(0x2D, 0x39)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x2A, 8400, 0, 3900, 0)
    SetChrChipByIndex(0x2A, 0x23)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x2)
    SetChrPos(0x2B, 9170, 0, 3280, 224)
    SetChrFlags(0x2B, 0x8)
    SetChrPos(0x2D, 8600, 0, 6160, 185)
    SetChrPos(0x2C, 7740, 0, 6270, 161)
    SetChrPos(0x18, 8610, 0, -7590, 68)
    SetChrPos(0x19, 7270, 0, -9110, 178)
    SetChrPos(0x16, -4080, 0, -8100, 195)
    SetChrPos(0x17, -3180, 0, -9070, 287)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_68(8800, 2000, 4470, 0)
    MoveCamera(79, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(24500, 0)
    Sleep(1000)
    Sleep(1000)
    PlayBGM("ed7514", 0)
    OP_6E(400, 10000)
    BeginChrThread(0x2A, 2, 0, 79)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x101, 8400, -700, 4570, 0)
    SetChrPos(0x104, 8890, -700, 3750, 0)

    #C0359
    ChrTalk(
        0x101,
        "#0006F#5P#50W呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        "#0303F#11P#50W呼、呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x2C,
        (
            "#0102F呵呵，\x01",
            "两位都辛苦啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x2D,
        (
            "#0202F#5P……很精彩的比赛，\x01",
            "恭喜你们获胜。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#0002F#5P#40W不……全部都是……靠兰迪的作战，\x01",
            "才能取胜啊……呼、呼……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#0302F#11P#40W不……如果没有你配合的话……\x01",
            "最后那一击……是不会成功的……\x02\x03",

            "#0306F……呜啊……\x01",
            "好、好像确实是玩得有点过火了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0365
    ChrTalk(
        0x2C,
        "#0106F呼，所以说男生真是……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x2D,
        (
            "#0203F#5P该说是思考单纯呢，还是争强好胜呢……\x02\x03",

            "#0202F不过，其中也有一位女孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x2C,
        (
            "#0109F呵呵，也是啊。\x02\x03",

            "#0102F对了……\x01",
            "我去买点冷饮来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2D, 0x2C, 500)

    #C0368
    ChrTalk(
        0x2D,
        (
            "#0202F#11P啊，我也一起去。\x02\x03",

            "在东街的露天店就能买到吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x2C,
        (
            "#0104F嗯，是的。\x02\x03",

            "#0100F两位，稍等一下哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2C, 0xE1, 0x1F4)
    BeginChrThread(0x2C, 3, 0, 73)
    Sleep(400)
    BeginChrThread(0x2D, 3, 0, 74)
    Sleep(3000)
    Fade(500)
    OP_68(8660, 2000, 3480, 0)
    MoveCamera(104, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Sleep(500)
    OP_68(8660, 2000, 3480, 40000)
    MoveCamera(88, 10, 0, 40000)
    OP_6E(520, 40000)
    SetCameraDistance(15500, 40000)
    EndChrThread(0x2A, 0xFF)
    SetChrSubChip(0x2A, 0x8)
    Sleep(1500)

    #C0370
    ChrTalk(
        0x101,
        (
            "#0006F#30W啊～……呼～……\x02\x03",

            "#0008F说起来……我们是为了什么\x01",
            "才会参加这种比赛来着……？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x104,
        (
            "#0304F#30W哈哈……\x01",
            "理由什么的，都已经无所谓啦……\x02\x03",

            "#0308F#40W…………………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    OP_A0(0x2A, 1200, 0x8, 0xA)
    OP_63(0x2B, 0xFFFFFE3E, 1000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2B)
    OP_63(0x2A, 0xFFFFFDA8, 1100, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    OP_A1(0x2A, 0x4B0, 0x3, 0xA, 0xD, 0xE)

    #C0372
    ChrTalk(
        0x101,
        "#0005F#30W……兰迪……？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x104,
        (
            "#0303F#30W──说实话，你吃了一惊吧……\x02\x03",

            "看到我那种头脑充血的样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        (
            "#0005F#30W啊……\x02\x03",

            "#0001F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)

    #C0375
    ChrTalk(
        0x104,
        (
            "#0308F#30W连我自己都……不是很明白啊。\x02\x03",

            "平时那个总是态度轻浮，嘿嘿傻笑\x01",
            "的我，究竟是不是『如今』真正的自己……\x02\x03",

            "#0308F还是说，刚才那种状态\x01",
            "才是我真正的本质……\x02\x03",

            "#0303F在这两年间……\x01",
            "我已经完全搞不懂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        "#0001F#30W兰迪……\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0xFFFFFDA8, 1100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2A)

    #C0377
    ChrTalk(
        0x101,
        (
            "#0008F……那个，在加入警备队之前，\x01",
            "你都在哪里呢？\x02\x03",

            "听你说过自己不是出身于\x01",
            "克洛斯贝尔的……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#0304F#30W呵呵……在什么地方吗？\x02\x03",

            "#0312F我所在的……是像炼狱一样炽热……\x01",
            "又如冥府一般寒冷的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        "#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x104,
        (
            "#0311F#30W鲜血与灵魂都会沸腾……\x01",
            "然后冻结的世界……\x02\x03",

            "一切生命的光辉……\x01",
            "都与粪便一样的污泥\x01",
            "混杂交织的地方……\x02\x03",

            "#0303F……那就是我曾经所在的场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#0001F兰迪……\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#0300F──开玩笑啦～\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x3, 0xE, 0xF, 0x10)
    Sleep(1000)
    Sound(820, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x5, 0x11, 0x12, 0x13, 0x14, 0x15)
    Sleep(1000)
    SetChrPos(0x101, 8240, -400, 3940, 0)
    SetChrPos(0x104, 8490, -300, 3110, 0)

    #C0383
    ChrTalk(
        0x104,
        (
            "#0309F#5P哈哈，我看上去是不是很有那种感觉啊？\x02\x03",

            "#0302F……其实，我过去的经历之类的，\x01",
            "并不值得一提。\x02\x03",

            "现在的我，只是个喜欢夜生活，\x01",
            "冷酷又帅气的好男人啦。\x02\x03",

            "#0304F仅此而已。\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x3, 0x15, 0x16, 0x17)
    OP_A1(0x2A, 0x5DC, 0x2, 0x19, 0x1A)
    Sleep(500)

    #C0384
    ChrTalk(
        0x101,
        (
            "#0008F#5P…………………………………\x02\x03",

            "#0006F那个，兰迪。\x02\x03",

            "#0002F以前也和你说过吧……\x01",
            "我曾经有一个大哥。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x5DC, 0x2, 0x1A, 0x19)
    OP_A1(0x2A, 0x5DC, 0x5, 0x19, 0x1B, 0x1C, 0x1D, 0x1E)

    #C0385
    ChrTalk(
        0x104,
        "#0305F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#0004F#5P盖伊·班宁斯……\x01",
            "曾是隶属于搜查一科的搜查官。\x02\x03",

            "他的特立独行超乎所有人的想象，\x01",
            "无论遇到任何情况都会积极向前……\x02\x03",

            "在双亲因事故去世之后，\x01",
            "是他一个人把我抚养长大的……\x02\x03",

            "即使我一直憧憬的女性被他夺走，\x01",
            "也无法对他燃起一丝嫉妒之火……\x02\x03",

            "#0000F总之，他就是个『非常厉害的男人』。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x104,
        "#0300F#11P是吗……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_A1(0x2A, 0x4B0, 0x5, 0x17, 0x18, 0x19, 0x18, 0x17)
    Sleep(500)

    #C0388
    ChrTalk(
        0x104,
        (
            "#0304F#5P哈哈，你也很有压力嘛。\x02\x03",

            "所以，望着如此强大的兄长的背影，\x01",
            "才想不断追赶上去，是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#0012F#5P……算是吧。\x02\x03",

            "#0008F不过呢，稍微坦白一下……\x02\x03",

            "#0002F兰迪你……\x01",
            "稍微有点像我的大哥呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x96, 1600, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A1(0x2A, 0x708, 0x5, 0x19, 0x1B, 0x1C, 0x1D, 0x1E)

    #C0390
    ChrTalk(
        0x104,
        "#0305F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#0004F#5P当然啦，长相上\x01",
            "肯定是一点也不像啦……\x02\x03",

            "但你总是若无其事地默默\x01",
            "帮助我、艾莉还有缇欧吧？\x02\x03",

            "#0002F就是这一点和大哥有点像呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x104,
        (
            "#0305F#11P喂喂，那个……\x01",
            "别说这种让人难为情的话啦。\x02\x03",

            "#0309F哥哥我的脸都红了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#0009F#5P哈哈，那种掩饰害羞\x01",
            "的方式好像也有点像啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x104,
        "#0301F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#0004F#5P所以呢，我是有些\x01",
            "尊敬兰迪的。\x02\x03",

            "尊敬你那种能够正视，进而了解『自己』，\x01",
            "同时也能很好地照顾到他人的地方……\x02\x03",

            "#0000F与其说是作为同事，不如说，我敬佩的是\x01",
            "可以独当一面，作为一个『男人』的你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x104,
        "#0305F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#0008F#5P……老实说，我还十分不成熟。\x02\x03",

            "所以我想，即使兰迪告诉我你的过去，\x01",
            "我也只能说出一些\x01",
            "像刚才那种幼稚的蠢话。\x02\x03",

            "#0004F──所以呢。\x02\x03",

            "#0000F等到有朝一日，我能与\x01",
            "大哥，还有兰迪并肩而立了……\x02\x03",

            "你再把那些事情说给我听吧，好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        "#0302F#11P……罗伊德………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x4B0, 0x3, 0x1E, 0x1F, 0x20)
    OP_63(0x2B, 0x96, 1600, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x2B)
    Sleep(300)
    Sound(1374, 255, 85, 0)
    Sleep(1200)
    OP_A1(0x2A, 0x4B0, 0x5, 0x20, 0x21, 0x22, 0x23, 0x24)
    Sound(820, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x5, 0x24, 0x25, 0x26, 0x25, 0x24)

    #C0399
    ChrTalk(
        0x101,
        "#0011F#5P兰、兰迪……？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x104,
        (
            "#0304F#11P哎呀～真是败给你了！\x02\x03",

            "#0300F虽然大小姐早就这么说过了，\x01",
            "不过你好像还真是天生就会讨女人欢心啊。\x02\x03",

            "#0305F噢噢，不对，这种时候，\x01",
            "好像应该说会讨哥哥欢心才对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        (
            "#0011F#5P什、什么啊……\x02\x03",

            "#0013F那个，虽然我确实还是个半吊子，\x01",
            "但至少也不要把我当小孩子看待啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1376, 255, 100, 0)
    Sleep(150)
    OP_82(0x64, 0x0, 0x7D0, 0x12C)

    #C0402
    ChrTalk(
        0x104,
        (
            "#0309F#11P呵呵……\x01",
            "#4S哈哈哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x5DC, 0x4, 0x24, 0x25, 0x26, 0x25)
    OP_A1(0x2A, 0x5DC, 0x4, 0x24, 0x25, 0x26, 0x25)
    OP_A1(0x2A, 0x5DC, 0x5, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrPos(0x2C, 2300, 0, 7050, 194)
    SetChrPos(0x2D, 1700, 0, 5650, 135)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)

    #N0403
    NpcTalk(
        0x2C,
        "艾莉的声音",
        "哈……在做什么呢？\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x64, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(8240, 1500, 2820, 0)
    MoveCamera(22, 27, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    BeginChrThread(0x2C, 3, 0, 75)
    Sleep(600)
    BeginChrThread(0x2D, 3, 0, 76)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x2A, 0x2)
    SetChrPos(0x2A, 8440, 0, 4040, 240)
    SetChrPos(0x2B, 9170, 0, 3280, 240)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    Sound(804, 0, 100, 0)
    ClearChrFlags(0x2B, 0x8)
    Sleep(1500)

    #C0404
    ChrTalk(
        0x2C,
        "#0106F#6P请用吧，冰凉的饮料哦。\x02",
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x2C, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(100)
    OP_96(0x2C, 0x1B8A, 0x0, 0xE56, 0x4B0, 0x0)
    WaitChrThread(0x2D, 3)

    #C0405
    ChrTalk(
        0x2D,
        (
            "#0202F#6P那边正好有个露天店卖柠檬汽水，\x01",
            "我们就买来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x2D, 0x0, 0x44C, 0x5DC, 0x0)
    Sleep(100)
    OP_96(0x2D, 0x1CD4, 0x0, 0xA32, 0x4B0, 0x0)

    #C0406
    ChrTalk(
        0x2B,
        "#0302F#11P噢，真是谢啦。\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x2A,
        "#0002F#5P嗯，我们渴得快要虚脱了，真是得救了。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0408
    ChrTalk(
        0x2A,
        "#0003F#11P#10A#70W（咕噜、咕噜、咕噜……）\x02",
    )
    #Auto


    #C0409
    ChrTalk(
        0x2B,
        "#0303F#12P#10A#70W（咕噜、咕噜、咕噜……）\x02",
    )
    #Auto

    Sound(887, 0, 100, 0)
    Sleep(800)
    Sound(887, 0, 100, 0)
    Sleep(800)
    Sound(887, 0, 100, 0)
    Sleep(900)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0410
    ChrTalk(
        0x2A,
        "#0014F#11P#1K#4S呼啊——————！\x02",
    )


    #C0411
    ChrTalk(
        0x2B,
        "#0309F#12P#1K#4S呼啊——————！\x02",
    )

    OP_57(0x1)
    OP_5A()
    Sleep(500)

    #C0412
    ChrTalk(
        0x2C,
        (
            "#0113F#6P你们这些男生可真是……\x02\x03",

            "#0111F刚刚消耗了那么多体力，\x01",
            "就别再那么胡闹了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2D, 0x2C, 500)

    #C0413
    ChrTalk(
        0x2D,
        "#0202F#12P艾莉前辈，你是在嫉妒吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)
    TurnDirection(0x2C, 0x2D, 800)
    OP_63(0x2C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0x2C, 0x1AC2, 0x0, 0x100E, 0xBB8, 0x0)
    Sleep(500)

    #C0414
    ChrTalk(
        0x2C,
        (
            "#0112F#5P怎、怎么会…\x01",
            "我怎么可能会嫉妒啊！？\x02\x03",

            "而且，那个……\x01",
            "两个人还都是男的……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x2D,
        (
            "#0204F#12P我听说过，\x01",
            "好像也有那种兴趣比较特殊的人呢……\x02\x03",

            "#0202F照这种情况看，说不定\x01",
            "已经有什么种子发芽了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x2C,
        "#0112F#5P有、有那种事吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2C, 500)

    #C0417
    ChrTalk(
        0x2B,
        (
            "#0302F#11P哼，不好意思啦，大小姐……！\x02\x03",

            "#0309F这个世界的规则就是弱肉强食！\x01",
            "要么掠食，要么被吃，这就是一切！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2C, 0x2B, 500)

    #C0418
    ChrTalk(
        0x2C,
        "#0111F#5P我、我说你啊……\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x2A,
        (
            "#0006F#11P呼……\x01",
            "你们都在说些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0420
    NpcTalk(
        0x18,
        "少年的声音",
        "──呵呵，好热闹啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CA6C():

        label("loc_CA6C")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_CA6C")

    QueueWorkItem2(0x2A, 0, lambda_CA6C)

    def lambda_CA7E():

        label("loc_CA7E")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_CA7E")

    QueueWorkItem2(0x2C, 0, lambda_CA7E)

    def lambda_CA90():

        label("loc_CA90")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_CA90")

    QueueWorkItem2(0x2D, 0, lambda_CA90)

    def lambda_CAA2():

        label("loc_CAA2")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_CAA2")

    QueueWorkItem2(0x2B, 0, lambda_CAA2)
    Fade(500)
    SetChrPos(0x2D, 6090, 0, 3190, 230)
    OP_68(7880, 1710, 1510, 0)
    MoveCamera(127, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x18, 7000, 0, -5000, 0)
    SetChrPos(0x1A, 6200, 0, -6000, 0)
    SetChrPos(0x22, 7000, 0, -7000, 0)
    SetChrPos(0x23, 7600, 0, -6000, 0)
    SetChrPos(0x24, 6700, 0, -8350, 0)
    SetChrPos(0x25, 5200, 0, -6900, 0)

    def lambda_CBF4():
        OP_95(0xFE, 7000, 0, -180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_CBF4)

    def lambda_CC0E():
        OP_95(0xFE, 6200, 0, -1180, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_CC0E)

    def lambda_CC28():
        OP_95(0xFE, 7000, 0, -2180, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_CC28)

    def lambda_CC42():
        OP_95(0xFE, 7600, 0, -1180, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_CC42)

    def lambda_CC5C():
        OP_95(0xFE, 6700, 0, -3350, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_CC5C)

    def lambda_CC76():
        OP_95(0xFE, 5200, 0, -1900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_CC76)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0xD)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x5)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x19, 9500, 0, -5300, 0)
    SetChrPos(0x1D, 8700, 0, -6300, 0)
    SetChrPos(0x1E, 10300, 0, -6300, 0)
    SetChrPos(0x1F, 10300, 0, -7900, 0)
    SetChrPos(0x20, 8700, 0, -7900, 0)
    SetChrPos(0x21, 11400, 0, -7800, 0)

    def lambda_CD8C():
        OP_95(0xFE, 9500, 0, -500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_CD8C)

    def lambda_CDA6():
        OP_95(0xFE, 8700, 0, -1500, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_CDA6)

    def lambda_CDC0():
        OP_95(0xFE, 10300, 0, -1500, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_CDC0)

    def lambda_CDDA():
        OP_95(0xFE, 10300, 0, -3100, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_CDDA)

    def lambda_CDF4():
        OP_95(0xFE, 8700, 0, -3100, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_CDF4)

    def lambda_CE0E():
        OP_95(0xFE, 11400, 0, -3000, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_CE0E)
    Sleep(1500)

    #C0421
    ChrTalk(
        0x2A,
        (
            "#0000F#6P哎呀……\x01",
            "你们已经恢复体力了吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 3)

    #C0422
    ChrTalk(
        0x18,
        (
            "#0404F#11P呵呵，算是吧。\x02\x03",

            "#0402F今天我们就暂且\x01",
            "老老实实地认输好了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x19, 3)
    TurnDirection(0x19, 0x2B, 500)

    #C0423
    ChrTalk(
        0x19,
        (
            "#1603F#11P哼……这个结果真让人不爽。\x02\x03",

            "#1601F──喂，红毛，\x01",
            "下次咱们单挑分个胜负如何……？\x02\x03",

            "从最后的那股爆发力来看……\x01",
            "你这小子莫非一直都在隐藏实力吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x2B,
        (
            "#0306F#6P啊～……\x01",
            "并不是那样的啊。\x02\x03",

            "#0300F像那样一口气使出全部力量，爆发力是会很强。\x01",
            "然而相对地，所消耗的体力也会十分剧烈啊。\x02\x03",

            "所以这是我留到最后的救命绝招，\x01",
            "平时可不想轻易使用～仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x19,
        (
            "#1600F#11P嘁，还有那个黑发小子也是……\x02\x03",

            "#1604F算了，今天毕竟已经很累了。\x02\x03",

            "你们几个，跟着我撤了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(260, 20, -1, -1)
    SetChrName("剑蛇帮众成员")

    #A0426
    AnonymousTalk(
        0xFF,
        "#4S收到～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_D0BD():

        label("loc_D0BD")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D0BD")

    QueueWorkItem2(0x1D, 2, lambda_D0BD)

    def lambda_D0CF():

        label("loc_D0CF")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D0CF")

    QueueWorkItem2(0x1E, 2, lambda_D0CF)

    def lambda_D0E1():

        label("loc_D0E1")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D0E1")

    QueueWorkItem2(0x1F, 2, lambda_D0E1)

    def lambda_D0F3():

        label("loc_D0F3")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D0F3")

    QueueWorkItem2(0x20, 2, lambda_D0F3)

    def lambda_D105():

        label("loc_D105")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D105")

    QueueWorkItem2(0x21, 2, lambda_D105)
    BeginChrThread(0x19, 3, 0, 77)
    Sleep(1500)
    EndChrThread(0x1F, 0x2)
    BeginChrThread(0x1F, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x20, 0x2)
    BeginChrThread(0x20, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x1D, 0x2)
    BeginChrThread(0x1D, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x21, 0x2)
    BeginChrThread(0x21, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x1E, 0x2)
    BeginChrThread(0x1E, 3, 0, 77)

    #C0427
    ChrTalk(
        0x18,
        (
            "#0402F#11P呵呵，那么\x01",
            "我们也先行告辞吧。\x02\x03",

            "#0409F再会，\x01",
            "今天玩得很开心哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0428
    ChrTalk(
        0x1A,
        "#11P──撤退。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(320, 60, -1, -1)
    SetChrName("圣书会众成员")

    #A0429
    AnonymousTalk(
        0xFF,
        "#4S了解！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x24, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x25, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x22, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x1A, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x23, 3, 0, 78)
    Sleep(500)
    BeginChrThread(0x18, 3, 0, 78)
    Sleep(1000)

    #N0430
    NpcTalk(
        0x16,
        "女孩的声音",
        (
            "哈～……\x01",
            "比起『渡鸦帮』的那伙人，\x01",
            "组织性真的要强很多啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_D2D0():

        label("loc_D2D0")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D2D0")

    QueueWorkItem2(0x2A, 0, lambda_D2D0)

    def lambda_D2E2():

        label("loc_D2E2")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D2E2")

    QueueWorkItem2(0x2C, 0, lambda_D2E2)

    def lambda_D2F4():

        label("loc_D2F4")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D2F4")

    QueueWorkItem2(0x2D, 0, lambda_D2F4)

    def lambda_D306():

        label("loc_D306")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D306")

    QueueWorkItem2(0x2B, 0, lambda_D306)
    Sleep(1000)
    Fade(500)
    OP_68(3990, 1500, 2440, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x16, 3140, 0, 1400, 225)
    SetChrPos(0x17, 1830, 0, 1460, 90)

    def lambda_D384():
        OP_95(0xFE, 8300, 0, 1510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_D384)

    def lambda_D39E():
        OP_95(0xFE, 6790, 0, 1680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_D39E)
    OP_68(7460, 1500, 2790, 2000)
    Sleep(2000)

    def lambda_D3CC():

        label("loc_D3CC")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_D3CC")

    QueueWorkItem2(0x16, 0, lambda_D3CC)

    def lambda_D3DE():

        label("loc_D3DE")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_D3DE")

    QueueWorkItem2(0x17, 0, lambda_D3DE)

    #C0431
    ChrTalk(
        0x16,
        "#0809F#12P嘿嘿嘿，辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x2A,
        (
            "#0002F#5P哈哈……\x01",
            "你们也辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x2B,
        "#0300F#5P怎么，这就要回去了吗？\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x17,
        (
            "#0902F#6P是啊，本来就是为了\x01",
            "工作才来这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x2D,
        (
            "#0203F#5P这么说来，\x01",
            "我们也是一样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x2C,
        (
            "#0106F#5P唉……\x01",
            "都已经黄昏了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x16,
        (
            "#0809F#12P啊哈哈，\x01",
            "反正也玩得很开心，就不要在意了。\x02\x03",

            "#0802F毕竟是难得的庆典，\x01",
            "总要稍微闹一闹嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x2A,
        "#0012F#5P真、真有精力啊……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x17,
        (
            "#0909F#6P哈哈，那正是\x01",
            "艾丝蒂尔的长处呢。\x02\x03",

            "#0908F──不过，兰迪先生。\x02\x03",

            "#0901F你的身体没关系吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0440
    ChrTalk(
        0x2A,
        "#0005F#5P咦……\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x2B,
        (
            "#0305F#5P嘿……\x02\x03",

            "#0300F……虽然感觉不到同样的味道，\x01",
            "不过你也与那边有瓜葛吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x17,
        (
            "#0903F#6P不，正确地说并没有。\x02\x03",

            "#0901F不过多少了解一些那方面的知识……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x2B,
        (
            "#0300F#5P是吗……\x02\x03",

            "#0304F哈，反正我从还是个小鬼的时候\x01",
            "就已经习惯了。\x02\x03",

            "并不会留下什么后遗症的。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x17,
        (
            "#0904F#6P是吗……\x02\x03",

            "#0900F抱歉，我好像多管闲事了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x2B,
        "#0302F#5P哪里，别介意啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0446
    ChrTalk(
        0x2A,
        "#0001F#5P兰迪……？\x02",
    )

    CloseMessageWindow()

    def lambda_D7CF():

        label("loc_D7CF")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_D7CF")

    QueueWorkItem2(0x16, 0, lambda_D7CF)
    Sleep(300)

    #C0447
    ChrTalk(
        0x16,
        (
            "#0801F#11P等一下等一下，\x01",
            "怎么感觉你们两个人好像很了解对方一样啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D82B():

        label("loc_D82B")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D82B")

    QueueWorkItem2(0x17, 0, lambda_D82B)
    Sleep(200)

    #C0448
    ChrTalk(
        0x17,
        (
            "#0904F#6P哈哈，没什么，不必在意。\x02\x03",

            "#0900F艾丝蒂尔，我们差不多也该回去了，\x01",
            "亚里欧斯先生应该也已经回协会了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x16,
        "#0805F#11P啊，好的……\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x16,
        (
            "#0801F#11P说起来……\x01",
            "约修亚，那件事！\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x17,
        (
            "#0905F#6P啊……对了。\x02\x03",

            "#0901F难得相遇，就问问看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_D9AA():

        label("loc_D9AA")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_D9AA")

    QueueWorkItem2(0x17, 0, lambda_D9AA)

    def lambda_D9BC():

        label("loc_D9BC")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_D9BC")

    QueueWorkItem2(0x16, 0, lambda_D9BC)
    Fade(1000)
    OP_68(7700, 1730, 3080, 0)
    MoveCamera(102, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_68(7280, 1730, 3440, 30000)
    MoveCamera(125, 32, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(16000, 30000)
    Sleep(1000)

    #C0452
    ChrTalk(
        0x2A,
        "#0005F#5P那件事……？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x2B,
        "#0305F#5P怎么了，有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x16,
        (
            "#0806F#11P嗯……那个。\x02\x03",

            "#0801F你们知道『黑之竞拍会』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0455
    ChrTalk(
        0x2C,
        "#0105F#6P黑之……\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x2D,
        "#0205F#6P#N竞拍会……吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0457
    ChrTalk(
        0x16,
        (
            "#0806F#11P似乎是一场在克洛斯贝尔\x01",
            "的某处召开的竞拍会。\x02\x03",

            "而且听说每年都会在纪念庆典\x01",
            "期间召开……\x02\x03",

            "#0801F──而且，更关键的是，\x01",
            "听说竞拍品全都是盗窃来的赃物哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x2C,
        "#0101F#6P盗、盗窃来的赃物……！？\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x2A,
        "#0013F#6P真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x17,
        (
            "#0903F#11P不确定，毕竟也只是传闻而已。\x02\x03",

            "#0908F总之，听说都是一些难以估价，\x01",
            "却不能拿出来公然示人\x01",
            "的珍品……\x02\x03",

            "#0901F──不过，看你们的样子，\x01",
            "好像并没有听说过吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x2A,
        "#0006F#6P嗯……确实是第一次听到呢。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x2D,
        (
            "#0201F#6P#N……在警察的数据库中\x01",
            "也没看到过相关资料。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0463
    ChrTalk(
        0x2B,
        (
            "#0303F#5P『黑之竞拍会』吗……\x01",
            "真是个故弄玄虚的名字呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x2C,
        "#0108F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x16,
        (
            "#0806F#11P是吗～……本来还以为，\x01",
            "你们可能会知道些什么呢。\x02\x03",

            "#0800F果然只是传闻而已吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x17,
        (
            "#0903F#11P嗯～也许吧……\x02\x03",

            "#0908F但提供这个情报的人是奈尔先生，\x01",
            "所以我一直都以为准确无误……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x2A,
        "#0001F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0468
    ChrTalk(
        0x16,
        (
            "#0809F#11P啊哈哈……\x01",
            "抱歉啊，问了一些奇怪的事。\x02\x03",

            "#0802F今天真是很开心呢！\x01",
            "虽然输了比赛，总有些不甘心。\x02\x03",

            "如果下次还有机会处理同一个事件，\x01",
            "希望可以互相合作呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x2A,
        "#0002F#6P哈哈……十分赞同。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x17,
        (
            "#0904F#11P那么，我们这就告辞了。\x02\x03",

            "#0900F各位，辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x2B,
        "#0302F#5P噢，你们也辛苦啦。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0472
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样……\x01",
            "纪念庆典的第二日也顺利度过了。\x02\x03",

            "回到支援科的罗伊德等人\x01",
            "整理完报告书，一起吃过晚饭之后，\x01",
            "为了翌日的工作做准备，都早早休息了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E196")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D1")

    label("loc_E196")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1B6")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D1")

    label("loc_E1B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1D1")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1D1")

    SetScenarioFlags(0x5C, 0)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_80_B034 end

    def Function_81_E1DE(): pass

    label("Function_81_E1DE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0473
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公寓『伊梅尔达馆』\x01\x01",
            "～ 目前停止经营 ～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E285")

    #C0474
    ChrTalk(
        0x101,
        (
            "#0000F陈旧得发黑呢……\x01",
            "看来已经有很长时间都没人居住过了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_E285")

    TalkEnd(0xFF)
    Return()

    # Function_81_E1DE end

    SaveToFile()

Try(main)
