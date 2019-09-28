from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c100c.bin",                # FileName
        "c100c",                    # MapName
        "c100c",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 5, 0, 6],
    )

    BuildStringList((
        "c100c",                  # 0
        "库隆克",                 # 1
        "迪因兹",                 # 2
        "莉莉",                   # 3
        "玛尔缇",                 # 4
        "安奈",                   # 5
        "卢诺爷爷",               # 6
        "洛依",                   # 7
        "梅琳",                   # 8
        "斯赞",                   # 9
        "库塔",                   # 10
        "莎丽娜",                 # 11
        "尤格特",                 # 12
        "亚泽尔",                 # 13
        "游客",                   # 14
        "游客",                   # 15
        "阿蕾莎",                 # 16
        "史蒂芬",                 # 17
        "瓦鲁多",                 # 18
        "诺加诺夫",               # 19
        "杰德",                   # 20
        "寇奇",                   # 21
        "黑发女性",               # 22
        "假货商",                 # 23
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
        "chr/ch22800.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch24900.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch21400.itc",                   # 09
        "chr/ch20500.itc",                   # 0A
        "apl/ch50375.itc",                   # 0B
        "chr/ch23300.itc",                   # 0C
        "chr/ch23800.itc",                   # 0D
        "chr/ch20600.itc",                   # 0E
        "chr/ch02100.itc",                   # 0F
        "chr/ch30800.itc",                   # 10
        "chr/ch31700.itc",                   # 11
        "chr/ch22700.itc",                   # 12
        "chr/ch34200.itc",                   # 13
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   2,   0,   0,   4,   0,   9,   255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   3,   0,   15,  255,  0)
    DeclNpc(-11560,  -300,    6820,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-12609,  -300,    7650,    135,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   9,   0,   0,   2,   0,   19,  255,  0)
    DeclNpc(-15810,  -300,    16629,   180,  261,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-14960,  -300,    15649,   315,  261,  0x0, 0,   19,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-17389,  -300,    16750,   90,   261,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-19219,  -319,    17000,   135,  261,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-17950,  -300,    17200,   225,  261,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5630,    -300,    3789,    135,  389,  0x0, 0,   18,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(7050,    -300,    3259,    225,  389,  0x0, 0,   14,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5429,    -3000,   -13149,  315,  389,  0x0, 0,   15,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5199,    -3000,   -11279,  180,  405,  0x0, 0,   16,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(4239,    -3000,   -12840,  90,   389,  0x0, 0,   17,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(3789,    -3000,   -11079,  135,  389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  46, 0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "西街")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "行政区")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "住宅街")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "东街")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "旧城区")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "港湾区")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "站前街道")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "后巷")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_694",          # 00, 0
        "Function_1_74C",          # 01, 1
        "Function_2_7E5",          # 02, 2
        "Function_3_85A",          # 03, 3
        "Function_4_91B",          # 04, 4
        "Function_5_968",          # 05, 5
        "Function_6_D65",          # 06, 6
        "Function_7_E2A",          # 07, 7
        "Function_8_11D9",         # 08, 8
        "Function_9_159E",         # 09, 9
        "Function_10_1A8D",        # 0A, 10
        "Function_11_35E2",        # 0B, 11
        "Function_12_38E5",        # 0C, 12
        "Function_13_3A28",        # 0D, 13
        "Function_14_3BF1",        # 0E, 14
        "Function_15_3E70",        # 0F, 15
        "Function_16_4160",        # 10, 16
        "Function_17_4202",        # 11, 17
        "Function_18_424B",        # 12, 18
        "Function_19_4591",        # 13, 19
        "Function_20_47D6",        # 14, 20
        "Function_21_4953",        # 15, 21
        "Function_22_4AEA",        # 16, 22
        "Function_23_4BEC",        # 17, 23
        "Function_24_4E69",        # 18, 24
        "Function_25_4F62",        # 19, 25
        "Function_26_5038",        # 1A, 26
        "Function_27_5119",        # 1B, 27
        "Function_28_541F",        # 1C, 28
        "Function_29_5472",        # 1D, 29
        "Function_30_54BD",        # 1E, 30
        "Function_31_5561",        # 1F, 31
        "Function_32_571F",        # 20, 32
        "Function_33_59E0",        # 21, 33
        "Function_34_5ACB",        # 22, 34
        "Function_35_6160",        # 23, 35
        "Function_36_725C",        # 24, 36
        "Function_37_728C",        # 25, 37
        "Function_38_72C3",        # 26, 38
        "Function_39_72E2",        # 27, 39
        "Function_40_7308",        # 28, 40
        "Function_41_732E",        # 29, 41
        "Function_42_7354",        # 2A, 42
        "Function_43_7391",        # 2B, 43
        "Function_44_73B0",        # 2C, 44
        "Function_45_73CF",        # 2D, 45
        "Function_46_7462",        # 2E, 46
        "Function_47_8E6A",        # 2F, 47
        "Function_48_90CD",        # 30, 48
    ))


    def Function_0_694(): pass

    label("Function_0_694")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6D4"),
        (1, "loc_6E0"),
        (2, "loc_6EC"),
        (3, "loc_6F8"),
        (4, "loc_704"),
        (5, "loc_710"),
        (6, "loc_71C"),
        (SWITCH_DEFAULT, "loc_728"),
    )


    label("loc_6D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_704")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_710")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_71C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_728")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_74B")

    Return()

    # Function_0_694 end

    def Function_1_74C(): pass

    label("Function_1_74C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E4")
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -40270, -300, 12170, 2000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, 26200, -300, -1050, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_74C")

    label("loc_7E4")

    Return()

    # Function_1_74C end

    def Function_2_7E5(): pass

    label("Function_2_7E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_859")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_2_7E5")

    label("loc_859")

    Return()

    # Function_2_7E5 end

    def Function_3_85A(): pass

    label("Function_3_85A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91A")
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, 26030, -300, 2230, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -40490, -300, 15850, 2000, 0x0)
    Sleep(2400)
    Jump("Function_3_85A")

    label("loc_91A")

    Return()

    # Function_3_85A end

    def Function_4_91B(): pass

    label("Function_4_91B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_4_91B")

    label("loc_967")

    Return()

    # Function_4_91B end

    def Function_5_968(): pass

    label("Function_5_968")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A06")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_A25")

    label("loc_A06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A25")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_A25")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_A33")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABA")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_AD9")

    label("loc_ABA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_AD9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_AE7")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B60")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_B7F")

    label("loc_B60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7F")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_B7F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B88")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BF2")
    SetChrPos(0x12, -14960, -300, 15650, 315)
    SetChrPos(0x13, -15810, -300, 16630, 270)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x15, -11870, -300, 6120, 315)
    SetChrPos(0x16, -12270, -300, 7480, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_D28")

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C58")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x12, -14960, -300, 15650, 315)
    SetChrPos(0x13, -15810, -300, 16630, 180)
    SetChrPos(0x15, -12120, -310, 6540, 0)
    SetChrPos(0x16, -10940, -300, 6040, 315)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_D28")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C9B")
    OP_93(0x12, 0x10E, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x15, -13300, -3000, -2410, 0)
    SetChrPos(0x16, -12550, -3000, -3260, 315)
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_D28")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CFC")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x15, -24030, -3000, 3630, 315)
    SetChrPos(0x16, -21730, -3000, 5420, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_CF7")
    SetChrFlags(0x1C, 0x10)

    label("loc_CF7")

    Jump("loc_D28")

    label("loc_CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D28")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D3C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 31)
    Jump("loc_D4B")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D4B")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 33)

    label("loc_D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D64")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_D64")

    Return()

    # Function_5_968 end

    def Function_6_D65(): pass

    label("Function_6_D65")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x1E)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -4300, 14000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10000, -4300, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -6000, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_D65 end

    def Function_7_E2A(): pass

    label("Function_7_E2A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E87")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA7")
    OP_AF(0x39)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D0")

    label("loc_EA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBB")
    Jump("loc_11D0")

    label("loc_EBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7E")

    #C0001
    ChrTalk(
        0xFE,
        "……呼，真抱歉。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "七十周年纪念的收藏品\x01",
            "已经全部卖完啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0003
    ChrTalk(
        0xFE,
        (
            "呀，全部卖完了呢～！\x01",
            "如此大卖还是头一次呢～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FDA")

    label("loc_F7E")


    #C0004
    ChrTalk(
        0xFE,
        (
            "……呼，真抱歉。\x01",
            "纪念收藏品已经全部卖完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "呵呵，辛苦制作的汗水\x01",
            "终于有了回报呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDA")

    Jump("loc_11D0")

    label("loc_FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_103C")

    #C0006
    ChrTalk(
        0xFE,
        (
            "孩子们买了\x01",
            "很多风车。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "小孩子嘛，就是喜欢\x01",
            "这种东西。\x01",
            "我也算是了解啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D0")

    label("loc_103C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1089")

    #C0008
    ChrTalk(
        0xFE,
        (
            "不知为何，\x01",
            "聚集了很多人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "这可是绝好的销售机会啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_11D0")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10E7")

    #C0010
    ChrTalk(
        0xFE,
        (
            "……哎呀，\x01",
            "纪念庆典来了很多人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "纪念品就像不要钱一样，\x01",
            "卖得飞快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D0")

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A9")

    #C0012
    ChrTalk(
        0xFE,
        "#4S嘿，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "来看看吗，\x01",
            "这里有七十周年纪念\x01",
            "的收藏品哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "雨伞架，桌上钟表，\x01",
            "连烟盒都有哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市政厅的模型\x01",
            "仅此一套，先到先得哟！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11D0")

    label("loc_11A9")


    #C0016
    ChrTalk(
        0xFE,
        (
            "要不要买点七十周年\x01",
            "的纪念品呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D0")

    Jump("loc_E37")

    label("loc_11D5")

    TalkEnd(0xFE)
    Return()

    # Function_7_E2A end

    def Function_8_11D9(): pass

    label("Function_8_11D9")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1236")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1256")
    OP_AF(0x38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1595")

    label("loc_1256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_126A")
    Jump("loc_1595")

    label("loc_126A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1595")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1301")

    #C0017
    ChrTalk(
        0xFE,
        (
            "欢迎，欢迎光临～！\x01",
            "承蒙您对迪因兹食材店的惠顾！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "今天是打折销售的最终日！\x01",
            "请尽情购买，不要留下遗憾啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1595")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_134D")

    #C0019
    ChrTalk(
        0xFE,
        "噢噢，今天卖得可真好，\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "连爱德丝女神也要大吃一惊吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1595")

    label("loc_134D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13B7")

    #C0021
    ChrTalk(
        0xFE,
        "嘿，那边的客人！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "过来看看嘛！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "露天市场名店——\x01",
            "迪因兹食材店\x01",
            "廉价大甩卖了哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1595")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_14AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1460")

    #C0024
    ChrTalk(
        0xFE,
        (
            "昨天晚上被叫去参加\x01",
            "工商协会的聚会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "还和老爷子们\x01",
            "干了一杯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "嘿嘿……\x01",
            "在庆典之夜和从商的同伴们一起喝酒，\x01",
            "还真是别有情致啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14A5")

    label("loc_1460")


    #C0027
    ChrTalk(
        0xFE,
        (
            "昨天晚上在工商协会\x01",
            "的聚会上喝了些酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "呀哈哈，真是好酒呢¤\x02",
    )

    CloseMessageWindow()

    label("loc_14A5")

    Jump("loc_1595")

    label("loc_14AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")

    #C0029
    ChrTalk(
        0xFE,
        "嘿，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "本来和莉莉说过，\x01",
            "让她至少今天去玩玩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "但她好像没有兴趣。\x01",
            "哎呀呀，真是个正经沉闷的家伙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1595")

    label("loc_153F")


    #C0032
    ChrTalk(
        0xFE,
        (
            "莉莉那家伙，从以前开始\x01",
            "就一直是一本正经的。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "哎呀呀，就算她后悔\x01",
            "我也不管哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1595")

    Jump("loc_11E6")

    label("loc_159A")

    TalkEnd(0xFE)
    Return()

    # Function_8_11D9 end

    def Function_9_159E(): pass

    label("Function_9_159E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_167B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1611")

    #C0034
    ChrTalk(
        0xFE,
        (
            "啊，欢迎光临～！\x01",
            "要买点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "找零的钱已经\x01",
            "没有了，\x01",
            "不便之处还请包涵啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1676")

    label("loc_1611")


    #C0036
    ChrTalk(
        0xFE,
        (
            "找零的钱已经\x01",
            "没有了啊。\x01",
            "还偏偏赶在这么忙的时候……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "只能找玛尔缇或库隆克\x01",
            "来帮忙换一点了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1676")

    Jump("loc_1A89")

    label("loc_167B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_16BB")

    #C0038
    ChrTalk(
        0xFE,
        "哇～好多的人啊……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "这下警察可有得忙了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A89")

    label("loc_16BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_173A")

    #C0040
    ChrTalk(
        0xFE,
        (
            "旁边那个库隆克的店，\x01",
            "东西好像卖得相当火啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "今年的露天市场ＭＶＰ\x01",
            "大概会被库隆克\x01",
            "夺得吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_173A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1845")

    #C0042
    ChrTalk(
        0xFE,
        (
            "听说市内有很多处露天店铺\x01",
            "都遭窃了？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "刚才工商协会的会长还亲自\x01",
            "前来提醒我这一点了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "算了，反正我们也早就对\x01",
            "扒手、小偷什么的见怪不怪了，\x01",
            "至少不会那么容易就让他们得逞……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "但一般的露天店铺或许就会被他们当做目标吧。\x01",
            "确实有些可怜呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18D2")

    label("loc_1845")


    #C0046
    ChrTalk(
        0xFE,
        (
            "东街的露天店铺之间\x01",
            "都会互相照应，\x01",
            "我们对抓捕扒手什么的已经习以为常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "但一般的露天店铺或许就会被他们当做目标吧。\x01",
            "确实有些可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D2")

    Jump("loc_1A89")

    label("loc_18D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1949")

    #C0048
    ChrTalk(
        0xFE,
        "迪因兹……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "和工商协会的会长在一起，\x01",
            "真的只是喝了些酒吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "真没办法啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1970")

    label("loc_1949")


    #C0051
    ChrTalk(
        0xFE,
        (
            "真是一个毫无心机\x01",
            "的单纯家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1970")

    Jump("loc_1A89")

    label("loc_1975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A58")

    #C0052
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "我们店也参加了印章收集之旅活动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "记得在买东西的时候跟我说一声哦，\x01",
            "会给你们盖上纪念印章的。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "另外，礼品的兑换地是在港湾公园哦。\x01",
            "工商协会已经搭起了帐篷，\x01",
            "应该很容易找到的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A89")

    label("loc_1A58")


    #C0055
    ChrTalk(
        0xFE,
        (
            "呼，给游客做印章收集的向导介绍\x01",
            "也很辛苦啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A89")

    TalkEnd(0xFE)
    Return()

    # Function_9_159E end

    def Function_10_1A8D(): pass

    label("Function_10_1A8D")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 6)
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1B98")

    #C0056
    ChrTalk(
        0xFE,
        (
            "啊呀，你们几个。\x01",
            "似乎带着很新鲜的鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "是自己钓的吗？\x01",
            "鱼身上也没有任何伤痕……可以就这样\x01",
            "直接摆在店里卖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "呵呵，怎么样，\x01",
            "把那些鱼卖给\x01",
            "我们店吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔产的鱼可是畅销商品哦。\x01",
            "我也会给你们些回礼的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x51, 7)
    SetScenarioFlags(0x1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_1B98")

    Call(0, 11)
    Jump("loc_35DE")

    label("loc_1BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_35DB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D6")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "对话")
    MenuCmd(1, 1, "将鱼售出")
    MenuCmd(1, 1, "放弃")
    ClearScenarioFlags(0x1, 6)
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFF")
    MenuCmd(3, 1, 0x1)

    label("loc_1BFF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C31")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1C31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3592")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CBD")
    MenuCmd(1, 1, "雪花蟹　　　　　　　地　×　10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB3")
    Call(0, 13)

    label("loc_1CB3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1CBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D14")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼　　　水　×　10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0A")
    Call(0, 13)

    label("loc_1D0A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D6B")
    MenuCmd(1, 1, "橙河鱼　　　　　　　火　×　10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D61")
    Call(0, 13)

    label("loc_1D61")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DC2")
    MenuCmd(1, 1, "岩穴鱼　　　　　　　风　×　10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB8")
    Call(0, 13)

    label("loc_1DB8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E19")
    MenuCmd(1, 1, "鲤鱼　　　　　　　　时　×　10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0F")
    Call(0, 13)

    label("loc_1E0F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E70")
    MenuCmd(1, 1, "冷水鱼　　　　　　　幻　×　10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E66")
    Call(0, 13)

    label("loc_1E66")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EC7")
    MenuCmd(1, 1, "蓝带神仙鱼　　　　　地　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EBD")
    Call(0, 13)

    label("loc_1EBD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F1E")
    MenuCmd(1, 1, "银伞鱼　　　　　　　水　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F14")
    Call(0, 13)

    label("loc_1F14")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F75")
    MenuCmd(1, 1, "虹鳟鱼　　　　　　　火　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F6B")
    Call(0, 13)

    label("loc_1F6B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FCC")
    MenuCmd(1, 1, "黑鲑　　　　　　　　风　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC2")
    Call(0, 13)

    label("loc_1FC2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1FCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2023")
    MenuCmd(1, 1, "鲑鱼　　　　　　　　时　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2019")
    Call(0, 13)

    label("loc_2019")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_207A")
    MenuCmd(1, 1, "鳗鲡　　　　　　　　幻　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2070")
    Call(0, 13)

    label("loc_2070")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_207A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20D1")
    MenuCmd(1, 1, "珍珠草　　　　　　　空　×　20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C7")
    Call(0, 13)

    label("loc_20C7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_20D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2128")
    MenuCmd(1, 1, "大口鲈鱼　　　　　　地　×　40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211E")
    Call(0, 13)

    label("loc_211E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_217F")
    MenuCmd(1, 1, "云斑蛇头　　　　　　水　×　40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2175")
    Call(0, 13)

    label("loc_2175")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_217F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21D6")
    MenuCmd(1, 1, "暗纹蛇鱼　　　　　　火　×　40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21CC")
    Call(0, 13)

    label("loc_21CC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_21D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_222D")
    MenuCmd(1, 1, "巨鲶　　　　　　　　风　×　40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2223")
    Call(0, 13)

    label("loc_2223")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_222D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2284")
    MenuCmd(1, 1, "巨血蟹　　　　　　　时　×　50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227A")
    Call(0, 13)

    label("loc_227A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2284")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22DB")
    MenuCmd(1, 1, "电鳗　　　　　　　　幻　×　50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D1")
    Call(0, 13)

    label("loc_22D1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2332")
    MenuCmd(1, 1, "魔鬼巨鲶　　　　　　时　×　50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2328")
    Call(0, 13)

    label("loc_2328")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2332")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2389")
    MenuCmd(1, 1, "弧光蟹　　　　　　　空　×　50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237F")
    Call(0, 13)

    label("loc_237F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2389")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23E1")
    MenuCmd(1, 1, "金鲑　　　　　　　　时　×　100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D7")
    Call(0, 13)

    label("loc_23D7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2439")
    MenuCmd(1, 1, "锦鲤　　　　　　　　空　×　100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_242F")
    Call(0, 13)

    label("loc_242F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2439")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2491")
    MenuCmd(1, 1, "霸王蛇鱼　　　　　　幻　×　100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2487")
    Call(0, 13)

    label("loc_2487")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2491")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24D0")
    Jump("loc_358D")

    label("loc_24D0")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2557")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0060
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I地之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_254D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2557")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25C1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I水之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_25B7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_25C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_262B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2621")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I火之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2621")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_262B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2697")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0063
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I风之之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_268D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2697")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2701")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0064
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_26F7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2701")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_276B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2761")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2761")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_276B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27D5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27CB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0066
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I地之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_27CB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_27D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_283F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2835")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0067
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I水之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2835")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_283F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28A9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0068
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I火之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_289F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_28A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2913")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2909")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0069
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I风之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2909")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2913")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_297D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2973")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0070
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2973")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_297D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29E7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29DD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0071
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_29DD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A51")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A47")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0072
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I空之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2A47")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2ABB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0073
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I地之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2AB1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B25")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0074
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I水之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2B1B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B8F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B85")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0075
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I火之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2B85")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BF9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BEF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0076
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I风之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2BEF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C63")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C59")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0077
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2C59")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CCD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0078
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2CC3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D37")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0079
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2D2D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DA1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D97")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0080
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I空之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2D97")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E0C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E02")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0081
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片100个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2E02")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E77")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0082
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I空之耀晶片100个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2E6D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EE2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0083
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片100个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_2ED8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EE2")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交换\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_358D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2FD2")

    #C0084
    ChrTalk(
        0xFE,
        (
            "这是条特别珍贵的鱼，\x01",
            "而且或许再也钓不到了……\x01",
            "真的可以卖给我吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3583")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3099"),
        (1, "loc_30CC"),
        (2, "loc_30FF"),
        (3, "loc_3132"),
        (4, "loc_3165"),
        (5, "loc_3198"),
        (6, "loc_31CB"),
        (7, "loc_31FE"),
        (8, "loc_3231"),
        (9, "loc_3264"),
        (10, "loc_3297"),
        (11, "loc_32CA"),
        (12, "loc_32FD"),
        (13, "loc_3330"),
        (14, "loc_3363"),
        (15, "loc_3396"),
        (16, "loc_33C9"),
        (17, "loc_33FC"),
        (18, "loc_342F"),
        (19, "loc_3462"),
        (20, "loc_3495"),
        (21, "loc_34C8"),
        (22, "loc_34FD"),
        (23, "loc_3532"),
        (SWITCH_DEFAULT, "loc_3567"),
    )


    label("loc_3099")


    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 10)
    SubItemNumber('斗鱼', 1)
    Jump("loc_3567")

    label("loc_30CC")


    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber('雪花蟹', 1)
    Jump("loc_3567")

    label("loc_30FF")


    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x2, 10)
    SubItemNumber('蓝带神仙鱼', 1)
    Jump("loc_3567")

    label("loc_3132")


    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I风之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber('银伞鱼', 1)
    Jump("loc_3567")

    label("loc_3165")


    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 10)
    SubItemNumber('阿尔摩利卡鲫鱼', 1)
    Jump("loc_3567")

    label("loc_3198")


    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片×１０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x6, 10)
    SubItemNumber('乌龟', 1)
    Jump("loc_3567")

    label("loc_31CB")


    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 20)
    SubItemNumber('橙河鱼', 1)
    Jump("loc_3567")

    label("loc_31FE")


    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x1, 20)
    SubItemNumber('岩穴鱼', 1)
    Jump("loc_3567")

    label("loc_3231")


    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x2, 20)
    SubItemNumber('虹鳟鱼', 1)
    Jump("loc_3567")

    label("loc_3264")


    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I风之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x3, 20)
    SubItemNumber('食人鱼', 1)
    Jump("loc_3567")

    label("loc_3297")


    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 20)
    SubItemNumber('鲤鱼', 1)
    Jump("loc_3567")

    label("loc_32CA")


    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber('大口鲈鱼', 1)
    Jump("loc_3567")

    label("loc_32FD")


    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空之耀晶片×２０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x5, 20)
    SubItemNumber('黑鲑', 1)
    Jump("loc_3567")

    label("loc_3330")


    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×４０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x0, 40)
    SubItemNumber('角斗鱼', 1)
    Jump("loc_3567")

    label("loc_3363")


    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水之耀晶片×４０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x1, 40)
    SubItemNumber('冷水鱼', 1)
    Jump("loc_3567")

    label("loc_3396")


    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火之耀晶片×４０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x2, 40)
    SubItemNumber('小鲵', 1)
    Jump("loc_3567")

    label("loc_33C9")


    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I风之耀晶片×４０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x3, 40)
    SubItemNumber('鲑鱼', 1)
    Jump("loc_3567")

    label("loc_33FC")


    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×５０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 50)
    SubItemNumber('金龙鱼', 1)
    Jump("loc_3567")

    label("loc_342F")


    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片×５０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x6, 50)
    SubItemNumber('鳗鲡', 1)
    Jump("loc_3567")

    label("loc_3462")


    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×５０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 50)
    SubItemNumber('钢壳龟', 1)
    Jump("loc_3567")

    label("loc_3495")


    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空之耀晶片×５０\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber('巨血蟹', 1)
    Jump("loc_3567")

    label("loc_34C8")


    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I时之耀晶片×１００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x4, 100)
    SubItemNumber('珍珠龙鱼', 1)
    Jump("loc_3567")

    label("loc_34FD")


    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空之耀晶片×１００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x5, 100)
    SubItemNumber('巨鲶', 1)
    Jump("loc_3567")

    label("loc_3532")


    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻之耀晶片×１００\x07\x00",
            "获得了。\x02",
        )
    )

    AddSepith(0x6, 100)
    SubItemNumber('金鲑', 1)
    Jump("loc_3567")

    label("loc_3567")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_358D")

    label("loc_3583")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_358D")

    Jump("loc_1C4A")

    label("loc_3592")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35D1")

    label("loc_35A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35B5")
    Jump("loc_35D1")

    label("loc_35B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_35D1")

    Jump("loc_1BB3")

    label("loc_35D6")

    Jump("loc_35DE")

    label("loc_35DB")

    Call(0, 11)

    label("loc_35DE")

    TalkEnd(0xB)
    Return()

    # Function_10_1A8D end

    def Function_11_35E2(): pass

    label("Function_11_35E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3684")

    #C0109
    ChrTalk(
        0xB,
        (
            "虽然克洛斯贝尔产的鱼很好卖，\x01",
            "但很少有货。\x01",
            "总是脱销。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "你们的鱼\x01",
            "看起来都不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "如果愿意的话，能卖给我们店吗？\x01",
            "我也会给你们些回礼的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_36CF")

    #C0112
    ChrTalk(
        0xB,
        (
            "今天的进货量可是\x01",
            "平时的五倍啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        "但还是全部卖光了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_36CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_371D")

    #C0114
    ChrTalk(
        0xB,
        "今年的销售额实在很惊人啊。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        "到时也能向老公夸耀一番了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_371D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3791")

    #C0116
    ChrTalk(
        0xB,
        "您好，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "纪念庆典的看点\x01",
            "并不是只有游行。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "也请多多关注\x01",
            "露天市场的这些店啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3809")

    #C0119
    ChrTalk(
        0xB,
        (
            "啊，欢迎光临～！\x01",
            "早上刚到的鱼，很新鲜哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "配上米饭，再滴上些酱油，\x01",
            "便是一份美味的极品料理啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_38E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388B")

    #C0121
    ChrTalk(
        0xB,
        "啊，欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        "要不要买点我们的鱼？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "带到那边的龙老饭店里，\x01",
            "马上就能做成可口的生鱼片！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E4")

    label("loc_388B")


    #C0124
    ChrTalk(
        0xB,
        (
            "东街的饭店，无论哪家都\x01",
            "允许自带食材。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        "走到哪吃到哪，可是这里饭店独有的方法哦。\x02",
    )

    CloseMessageWindow()

    label("loc_38E4")

    Return()

    # Function_11_35E2 end

    def Function_12_38E5(): pass

    label("Function_12_38E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_38F3")
    SetScenarioFlags(0x1, 6)

    label("loc_38F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_3901")
    SetScenarioFlags(0x1, 6)

    label("loc_3901")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_390F")
    SetScenarioFlags(0x1, 6)

    label("loc_390F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_391D")
    SetScenarioFlags(0x1, 6)

    label("loc_391D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_392B")
    SetScenarioFlags(0x1, 6)

    label("loc_392B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_3939")
    SetScenarioFlags(0x1, 6)

    label("loc_3939")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_3947")
    SetScenarioFlags(0x1, 6)

    label("loc_3947")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_3955")
    SetScenarioFlags(0x1, 6)

    label("loc_3955")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_3963")
    SetScenarioFlags(0x1, 6)

    label("loc_3963")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_3971")
    SetScenarioFlags(0x1, 6)

    label("loc_3971")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_397F")
    SetScenarioFlags(0x1, 6)

    label("loc_397F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_398D")
    SetScenarioFlags(0x1, 6)

    label("loc_398D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_399B")
    SetScenarioFlags(0x1, 6)

    label("loc_399B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_39A9")
    SetScenarioFlags(0x1, 6)

    label("loc_39A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_39B7")
    SetScenarioFlags(0x1, 6)

    label("loc_39B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_39C5")
    SetScenarioFlags(0x1, 6)

    label("loc_39C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_39D3")
    SetScenarioFlags(0x1, 6)

    label("loc_39D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_39E1")
    SetScenarioFlags(0x1, 6)

    label("loc_39E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_39EF")
    SetScenarioFlags(0x1, 6)

    label("loc_39EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_39FD")
    SetScenarioFlags(0x1, 6)

    label("loc_39FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_3A0B")
    SetScenarioFlags(0x1, 6)

    label("loc_3A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_3A19")
    SetScenarioFlags(0x1, 6)

    label("loc_3A19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_3A27")
    SetScenarioFlags(0x1, 6)

    label("loc_3A27")

    Return()

    # Function_12_38E5 end

    def Function_13_3A28(): pass

    label("Function_13_3A28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3B")
    MenuCmd(3, 1, 0x0)

    label("loc_3A3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4E")
    MenuCmd(3, 1, 0x1)

    label("loc_3A4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A61")
    MenuCmd(3, 1, 0x2)

    label("loc_3A61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A74")
    MenuCmd(3, 1, 0x3)

    label("loc_3A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A87")
    MenuCmd(3, 1, 0x4)

    label("loc_3A87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9A")
    MenuCmd(3, 1, 0x5)

    label("loc_3A9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AAD")
    MenuCmd(3, 1, 0x6)

    label("loc_3AAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC0")
    MenuCmd(3, 1, 0x7)

    label("loc_3AC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD3")
    MenuCmd(3, 1, 0x8)

    label("loc_3AD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE6")
    MenuCmd(3, 1, 0x9)

    label("loc_3AE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF9")
    MenuCmd(3, 1, 0xA)

    label("loc_3AF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0C")
    MenuCmd(3, 1, 0xB)

    label("loc_3B0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1F")
    MenuCmd(3, 1, 0xC)

    label("loc_3B1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B32")
    MenuCmd(3, 1, 0xD)

    label("loc_3B32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B45")
    MenuCmd(3, 1, 0xE)

    label("loc_3B45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B58")
    MenuCmd(3, 1, 0xF)

    label("loc_3B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6B")
    MenuCmd(3, 1, 0x10)

    label("loc_3B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7E")
    MenuCmd(3, 1, 0x11)

    label("loc_3B7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B91")
    MenuCmd(3, 1, 0x12)

    label("loc_3B91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA4")
    MenuCmd(3, 1, 0x13)

    label("loc_3BA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB7")
    MenuCmd(3, 1, 0x14)

    label("loc_3BB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BCA")
    MenuCmd(3, 1, 0x15)

    label("loc_3BCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BDD")
    MenuCmd(3, 1, 0x16)

    label("loc_3BDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF0")
    MenuCmd(3, 1, 0x17)

    label("loc_3BF0")

    Return()

    # Function_13_3A28 end

    def Function_14_3BF1(): pass

    label("Function_14_3BF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3C5C")

    #C0126
    ChrTalk(
        0xFE,
        (
            "啊，不好了，印章收集之旅\x01",
            "的礼品兑换，好像就截止到今天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "必须赶快去\x01",
            "兑换礼品。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6C")

    label("loc_3C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CAD")

    #C0128
    ChrTalk(
        0xFE,
        "今年的游行真的很壮观啊～\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "挥手致意的孩子们\x01",
            "也都很可爱啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6C")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D11")

    #C0130
    ChrTalk(
        0xFE,
        (
            "出来购物，忍不住\x01",
            "就逛了很多家店。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "呼……这可不太好啊，\x01",
            "对家人们还是保密吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6C")

    label("loc_3D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9A")

    #C0132
    ChrTalk(
        0xFE,
        (
            "今年好像也有人去了\x01",
            "阿尔摩利卡村。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "那里确实是个很漂亮的地方……\x01",
            "最重要的是还能吃到无比美味的料理呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E08")

    label("loc_3D9A")


    #C0134
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村是个很漂亮的地方，\x01",
            "而且在那里还能吃到无比美味的料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "游客们会前往那里\x01",
            "也是可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E08")

    Jump("loc_3E6C")

    label("loc_3E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E6C")

    #C0136
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间也不能休息\x01",
            "的人就是家庭主妇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "烹制晚餐的食材\x01",
            "总不能不去买。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6C")

    TalkEnd(0xFE)
    Return()

    # Function_14_3BF1 end

    def Function_15_3E70(): pass

    label("Function_15_3E70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F07")

    #C0138
    ChrTalk(
        0xFE,
        (
            "港湾区的舞台上\x01",
            "似乎每天都有娱乐表演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "嗯～我错过了第三天\x01",
            "的节目呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "至少得注意不要再错过\x01",
            "今天的表演呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F3B")

    label("loc_3F07")


    #C0141
    ChrTalk(
        0xFE,
        (
            "港湾区今日应该\x01",
            "也有文娱活动的，\x01",
            "可不能错过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F3B")

    Jump("loc_415C")

    label("loc_3F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3FBC")

    #C0142
    ChrTalk(
        0xFE,
        (
            "呵呵呵，游行时的第四辆车子\x01",
            "是克洛斯贝尔工商协会的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "因为是东方风格的设计式样，\x01",
            "我一眼就认出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_415C")

    label("loc_3FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3FFD")

    #C0144
    ChrTalk(
        0xFE,
        "呵呵，今天有游行啊。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "我也是\x01",
            "很期待的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_415C")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_406A")

    #C0146
    ChrTalk(
        0xFE,
        (
            "哦哦，又有一群游客\x01",
            "围上来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "其实没必要那么急躁，\x01",
            "今年的纪念庆典\x01",
            "可是长达五天呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_415C")

    label("loc_406A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_415C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F0")

    #C0148
    ChrTalk(
        0xFE,
        "过个开心的周年庆典吧！\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "克洛斯贝尔今年都已经七十岁了啊。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "我们这些老家伙也要\x01",
            "好好庆祝一番啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_415C")

    label("loc_40F0")


    #C0151
    ChrTalk(
        0xFE,
        (
            "顺便一提，克洛斯贝尔\x01",
            "和老夫一比，还要稍微年轻一点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "老夫今年都七十二岁了，\x01",
            "和麦克道尔市长同龄。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_415C")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E70 end

    def Function_16_4160(): pass

    label("Function_16_4160")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_41FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41DB")

    #C0153
    ChrTalk(
        0xFE,
        (
            "带妹妹来参观纪念庆典的苦差事\x01",
            "也落在我的肩上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "呼，结果就变成这样了～\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x0)
    SetChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_41FE")

    label("loc_41DB")


    #C0155
    ChrTalk(
        0xFE,
        (
            "梅琳，接下来\x01",
            "想去哪里玩呀～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FE")

    TalkEnd(0xFE)
    Return()

    # Function_16_4160 end

    def Function_17_4202(): pass

    label("Function_17_4202")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4247")

    #C0156
    ChrTalk(
        0xFE,
        "参加庆典～好开心呀～！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "梅琳想去那些\x01",
            "店里看看！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4247")

    TalkEnd(0xFE)
    Return()

    # Function_17_4202 end

    def Function_18_424B(): pass

    label("Function_18_424B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_433E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_430A")

    #C0158
    ChrTalk(
        0xFE,
        (
            "今天是庆典最终日，\x01",
            "很多公司都休息了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "我家的男人们\x01",
            "也全都出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "家务事就全都扔给我了……\x01",
            "他们也真好意思啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4339")

    label("loc_430A")


    #C0162
    ChrTalk(
        0xFE,
        (
            "我家的这些男人啊……\x01",
            "全都这么没责任心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4339")

    Jump("loc_458D")

    label("loc_433E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_43A7")

    #C0163
    ChrTalk(
        0xFE,
        (
            "呼～都已经很多年没有这么\x01",
            "近距离地观看过游行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        "这种兴奋的感觉也真是久违了啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_43A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_43F6")

    #C0165
    ChrTalk(
        0xFE,
        "那个，鲑鱼、鲑鱼……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "距离游行开始好像\x01",
            "还有一点时间呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_43F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_44B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4483")

    #C0167
    ChrTalk(
        0xFE,
        (
            "呼，我要是偷懒不做家务，\x01",
            "家里的男人们就又要开始喋喋不休了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "真是的……自己吃的饭\x01",
            "难道就不能自己做做吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_44B2")

    label("loc_4483")


    #C0169
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典，\x01",
            "家庭主妇也想休息一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B2")

    Jump("loc_458D")

    label("loc_44B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_458D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4554")

    #C0170
    ChrTalk(
        0xFE,
        "嗯～庆典真不错啊～\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "各大店铺都在打折甩卖，\x01",
            "而且也可以稍稍奢侈一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "……嘿嘿嘿，要使用私房钱的话，\x01",
            "现在正是时候啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_458D")

    label("loc_4554")


    #C0173
    ChrTalk(
        0xFE,
        (
            "稍后不如也去百货店里看看吧，\x01",
            "正好有我想要的东西呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458D")

    TalkEnd(0xFE)
    Return()

    # Function_18_424B end

    def Function_19_4591(): pass

    label("Function_19_4591")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_45EF")

    #C0174
    ChrTalk(
        0xFE,
        "……纪念庆典·最终日打折大甩卖！\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "嗯嗯，必须要抓住机会\x01",
            "多买一点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D2")

    label("loc_45EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4664")
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0176
    ChrTalk(
        0xFE,
        (
            "游行吗……\x01",
            "实在是太过华丽了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "花费那么多的钱，\x01",
            "真的没关系吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D2")

    label("loc_4664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_46DD")

    #C0178
    ChrTalk(
        0xFE,
        (
            "这个时间的话，\x01",
            "买完东西以后\x01",
            "应该还来得及看游行吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "……好像在那边能看得更清楚，\x01",
            "稍微再走几步吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D2")

    label("loc_46DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4753")

    #C0180
    ChrTalk(
        0xFE,
        (
            "嗯嗯，\x01",
            "那边有纪念庆典的打折甩卖……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "呀，等一下，这个价格的话，\x01",
            "好像还是那边的店更加便宜呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D2")

    label("loc_4753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_47D2")
    OP_63(0xFE, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0182
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间，到处都在打折甩卖，\x01",
            "这也很让人犹豫啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "究竟哪里才是最便宜的呢……\x02",
    )

    CloseMessageWindow()

    label("loc_47D2")

    TalkEnd(0xFE)
    Return()

    # Function_19_4591 end

    def Function_20_47D6(): pass

    label("Function_20_47D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4857")

    #C0184
    ChrTalk(
        0xFE,
        (
            "亚泽尔准备用他平时打工赚的钱\x01",
            "来请我们吃晚饭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "在外面用餐好像有些奢侈……\x01",
            "算啦，偶尔吃一次也无所谓。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494F")

    label("loc_4857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_48C9")

    #C0186
    ChrTalk(
        0xFE,
        (
            "呵呵，实在是玩得太兴奋了，\x01",
            "现在感到疲惫不堪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "尤格特，我来背你吧。\x01",
            "差不多也该回家了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_494F")

    label("loc_48C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_494F")
    OP_4B(0x14, 0xFF)

    #C0188
    ChrTalk(
        0xFE,
        "嗯，这里应该就可以了。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "呵呵，童年时期，我们姐弟\x01",
            "两人总是在一起玩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x14,
        "那、那么久以前的事，我早就忘啦。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)

    label("loc_494F")

    TalkEnd(0xFE)
    Return()

    # Function_20_47D6 end

    def Function_21_4953(): pass

    label("Function_21_4953")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A7A")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A13")

    #C0191
    ChrTalk(
        0xFE,
        "哥哥，接下来要玩什么？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "最近流行的游戏果然还是\x01",
            "扮演游击士啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x14,
        "啊，那就玩那个吧。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x14,
        (
            "不管做什么，哥哥今天\x01",
            "都奉陪到底。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "真的吗！？哇～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4A71")

    label("loc_4A13")


    #C0196
    ChrTalk(
        0xFE,
        (
            "那，哥哥就扮演\x01",
            "邪恶的黑手党吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x14,
        (
            "（这、这又让我想起了\x01",
            "　被偷袭受伤时的回忆……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A71")

    OP_4C(0x14, 0xFF)
    Jump("loc_4AE6")

    label("loc_4A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4ABE")

    #C0198
    ChrTalk(
        0xFE,
        "嗯～……游行真有趣啊。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "嗯嗯，都有点困了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4AE6")

    #C0200
    ChrTalk(
        0xFE,
        (
            "喂，游行队伍\x01",
            "还没有来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE6")

    TalkEnd(0xFE)
    Return()

    # Function_21_4953 end

    def Function_22_4AEA(): pass

    label("Function_22_4AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4B53")

    #C0201
    ChrTalk(
        0xFE,
        (
            "今日是计划三个人\x01",
            "一起去吃饭的。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "要去哪里呢……\x01",
            "果然还是中央广场一带比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE8")

    label("loc_4B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4B89")

    #C0203
    ChrTalk(
        0xFE,
        "尤格特，没事吧？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "你还小呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BE8")

    label("loc_4B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4BE8")

    #C0205
    ChrTalk(
        0xFE,
        (
            "我打算和家人\x01",
            "一起去看游行……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "这条街应该能看到吧，\x01",
            "好像对面那条街也可以呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE8")

    TalkEnd(0xFE)
    Return()

    # Function_22_4AEA end

    def Function_23_4BEC(): pass

    label("Function_23_4BEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C6D")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0207
    ChrTalk(
        0x15,
        (
            "那么，今天就去港湾区\x01",
            "的公园看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x15,
        (
            "那边好像也有\x01",
            "很多露天店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x16,
        "哇～好期待呀～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_4E65")

    label("loc_4C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D2B")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0210
    ChrTalk(
        0x16,
        (
            "追着看游行队伍，\x01",
            "找不到回去的路了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x15,
        "嗯，不用担心。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x15,
        (
            "前面挂着\x01",
            "游击士协会\x01",
            "的招牌呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0213
    ChrTalk(
        0x16,
        (
            "啊，真的！\x01",
            "太好了！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 3)
    Jump("loc_4D64")

    label("loc_4D2B")


    #C0214
    ChrTalk(
        0xFE,
        "不远处就是游击士协会。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "过去稍微问一下\x01",
            "路好啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D64")

    Jump("loc_4E65")

    label("loc_4D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4DAA")

    #C0216
    ChrTalk(
        0xFE,
        (
            "嗯……本来是来观光的，\x01",
            "结果有点想买东西了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E65")

    label("loc_4DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4DFD")

    #C0217
    ChrTalk(
        0xFE,
        (
            "买这些东西当作礼物的话\x01",
            "好像很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "孙儿应该也会喜欢的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E65")

    label("loc_4DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E65")

    #C0219
    ChrTalk(
        0xFE,
        "这就是克洛斯贝尔的庆典啊。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "虽然来过好几次了，但感觉每年\x01",
            "都会变得比以前更加繁华热闹。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E65")

    TalkEnd(0xFE)
    Return()

    # Function_23_4BEC end

    def Function_24_4E69(): pass

    label("Function_24_4E69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4E7D")
    Call(0, 23)
    Jump("loc_4F5E")

    label("loc_4E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E98")
    Call(0, 23)
    Jump("loc_4EBD")

    label("loc_4E98")


    #C0221
    ChrTalk(
        0xFE,
        (
            "真想顺便去见见\x01",
            "那些游击士呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBD")

    Jump("loc_4F5E")

    label("loc_4EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4EFB")

    #C0222
    ChrTalk(
        0xFE,
        (
            "奶奶，别光顾着蔬菜，\x01",
            "快去看游行啦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F5E")

    label("loc_4EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F41")

    #C0223
    ChrTalk(
        0xFE,
        "有很多有趣的东西呢～！\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "哇～好像玩具一样呢～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F5E")

    label("loc_4F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F5E")

    #C0225
    ChrTalk(
        0xFE,
        "好棒啊～奶奶！\x02",
    )

    CloseMessageWindow()

    label("loc_4F5E")

    TalkEnd(0xFE)
    Return()

    # Function_24_4E69 end

    def Function_25_4F62(): pass

    label("Function_25_4F62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5034")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FFA")

    #C0226
    ChrTalk(
        0xFE,
        (
            "因为知道肯定会拥挤不堪，\x01",
            "所以特意到第二天才来……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "嗯～但不愧是纪念庆典啊，\x01",
            "客流量和第一天好像根本没有任何不同。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5034")

    label("loc_4FFA")


    #C0228
    ChrTalk(
        0xFE,
        (
            "不愧是纪念庆典啊……\x01",
            "和昨天一样，\x01",
            "今天也有这么多人～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5034")

    TalkEnd(0xFE)
    Return()

    # Function_25_4F62 end

    def Function_26_5038(): pass

    label("Function_26_5038")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B7")

    #C0229
    ChrTalk(
        0xFE,
        (
            "终于回到了克洛斯贝尔，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "虽说是纪念庆典，\x01",
            "但克洛斯贝尔原来是\x01",
            "如此混乱不堪的吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5115")

    label("loc_50B7")


    #C0231
    ChrTalk(
        0xFE,
        (
            "但克洛斯贝尔原来是\x01",
            "如此混乱不堪的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "或许是我已经习惯了\x01",
            "阿尔摩利卡村的宁静了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5115")

    TalkEnd(0xFE)
    Return()

    # Function_26_5038 end

    def Function_27_5119(): pass

    label("Function_27_5119")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 7)), scpexpr(EXPR_END)), "loc_51AF")
    TurnDirection(0x19, 0x104, 0)

    #C0233
    ChrTalk(
        0x19,
        (
            "#1604F哼哼，那个黑头发的小子也不赖，\x01",
            "让本大爷玩得很开心嘛。\x02\x03",

            "#1602F正好，连同瓦吉一起，\x01",
            "本大爷迟早会把他们统统都干掉的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_541B")

    label("loc_51AF")


    #C0234
    ChrTalk(
        0x19,
        (
            "#1600F哟，是你们几个吗。\x02\x03",

            "#1602F呵呵……\x01",
            "怎么一副累惨了的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#0003F你看起来倒是很有精神啊。\x02\x03",

            "#0001F而且，好像又要去\x01",
            "什么地方胡闹了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x19,
        (
            "#1602F哼哼，有什么不满吗？\x02\x03",

            "庆典要怎么过\x01",
            "可是我们的自由。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        "#0106F（呼，该怎么说呢……）\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        "#0203F（真是很难沟通啊。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x19, 0x104, 750)
    Sleep(750)

    #C0239
    ChrTalk(
        0x19,
        (
            "#1601F话说回来，红毛……\x01",
            "下次咱们可要单挑分个胜负啊。\x02\x03",

            "#1602F既然让我见识到了那种绝技，\x01",
            "就更没理由轻易放过你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#0306F别了……你还是饶了我吧。\x02\x03",

            "#0301F昨天我只是一时兴奋，\x01",
            "稍微有些得意忘形了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x19,
        (
            "#1604F……越来越有意思了，\x01",
            "好想和拿出真本事的你\x01",
            "斗一斗啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        (
            "#0306F唉……\x01",
            "那招用得真是很失败啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 7)

    label("loc_541B")

    TalkEnd(0xFE)
    Return()

    # Function_27_5119 end

    def Function_28_541F(): pass

    label("Function_28_541F")

    TalkBegin(0xFE)

    #C0243
    ChrTalk(
        0x1A,
        "瓦鲁多大哥～今天要去哪里啊？\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x1A,
        (
            "OH YEAH～！！\x01",
            "我有点想去中央广场哦～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_541F end

    def Function_29_5472(): pass

    label("Function_29_5472")

    TalkBegin(0xFE)

    #C0245
    ChrTalk(
        0x1B,
        (
            "我们也有参加\x01",
            "庆典的权利。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1B,
        (
            "就算是警察也没有\x01",
            "理由干涉我们。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_5472 end

    def Function_30_54BD(): pass

    label("Function_30_54BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_54EF")

    #C0247
    ChrTalk(
        0x1C,
        (
            "瓦鲁多大哥，\x01",
            "我买来果汁啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555D")

    label("loc_54EF")


    #C0248
    ChrTalk(
        0x1C,
        (
            "对于我们不良团伙来说，\x01",
            "同伴果然是比家人更重要的存在啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x1C,
        "所以庆典就要和兄弟们一起过！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x19, 0)
    SetChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x1, 4)

    label("loc_555D")

    TalkEnd(0xFE)
    Return()

    # Function_30_54BD end

    def Function_31_5561(): pass

    label("Function_31_5561")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 7970, -300, 790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -3800, -3000, -5130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -12310, -3000, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x0, -7080, -3000, 1450, 135)
    SetChrPos(0x1, -7080, -3000, 1450, 135)
    SetChrPos(0x2, -7080, -3000, 1450, 135)
    SetChrPos(0x3, -7080, -3000, 1450, 135)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(2040, -1400, -8500, 0)
    MoveCamera(89, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_68(-16140, -1400, 1060, 10000)
    MoveCamera(37, 30, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(25000, 10000)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5561 end

    def Function_32_571F(): pass

    label("Function_32_571F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(25400, 700, 500, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 29700, -300, -100, 270)
    SetChrPos(0x102, 29700, -300, 1100, 270)
    SetChrPos(0x103, 31100, -300, -100, 270)
    SetChrPos(0x104, 31100, -300, 1100, 270)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_57BE():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57BE)
    Sleep(50)

    def lambda_57DB():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57DB)
    Sleep(50)

    def lambda_57F8():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57F8)
    Sleep(50)

    def lambda_5815():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5815)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    #C0250
    ChrTalk(
        0x104,
        (
            "#11P#0305F说起来，已经过了正午吗。\x02\x03",

            "#0306F看来游行都已经\x01",
            "结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x103,
        (
            "#0208F……真遗憾。\x01",
            "（听说还有坐着咪西\x01",
            "  的车子呢……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0252
    ChrTalk(
        0x101,
        (
            "#6P#0006F古战场的调查比想象中\x01",
            "的还要费力……\x02\x03",

            "#0000F总之，我们就先回支援科，\x01",
            "稍微喘口气吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5941():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5941)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0253
    ChrTalk(
        0x102,
        "#0102F嗯，就那么办吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 24700, -300, 500, 270)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xAA, 2)
    OP_29(0x44, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59CB")
    OP_29(0x20, 0x4, 0x40)
    Jump("loc_59DD")

    label("loc_59CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59DD")
    OP_29(0x20, 0x4, 0x40)

    label("loc_59DD")

    EventEnd(0x5)
    Return()

    # Function_32_571F end

    def Function_33_59E0(): pass

    label("Function_33_59E0")

    EventBegin(0x0)
    OP_EE(0x0, 0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07300.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("apl/ch50388.itc", 0x20)
    LoadChrToIndex("apl/ch50389.itc", 0x21)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x13)"), scpexpr(EXPR_END)), "loc_5A77")
    Call(0, 34)
    Jump("loc_5A87")

    label("loc_5A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_5A87")
    Call(0, 35)

    label("loc_5A87")

    OP_EE(0x0, 0xA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("c115C", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_33_59E0 end

    def Function_34_5ACB(): pass

    label("Function_34_5ACB")

    OP_68(10180, 1450, 550, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11550, 0)
    SetChrPos(0x1D, -4130, -300, 4860, 315)
    SetChrPos(0x1E, 24040, -300, 870, 270)
    SetChrPos(0x101, 24000, -300, 0, 270)
    SetChrPos(0x102, 25000, -300, 1500, 270)
    SetChrPos(0x103, 26000, -300, 0, 270)
    SetChrPos(0x104, 27000, -300, 1500, 270)

    def lambda_5B64():
        OP_95(0xFE, -60, -300, 660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5B64)
    OP_68(-5970, 1450, 2950, 8500)
    BeginChrThread(0x1E, 3, 0, 42)
    FadeToBright(1000, 0)
    OP_0D()

    #C0254
    ChrTalk(
        0x1E,
        "#5P#10A呼啊、呼啊。\x02",
    )
    #Auto

    OP_5A()

    #C0255
    ChrTalk(
        0x1E,
        (
            "#5P#10A别看不起我啊，\x01",
            "你们这群可恶的小鬼……\x02",
        )
    )
    #Auto

    OP_5A()

    #C0256
    ChrTalk(
        0x1E,
        (
            "#5P#10A看着吧，我这副年轻时\x01",
            "靠登山锻炼出来的身子骨，\x01",
            "肯定能把你们彻底甩开……\x02",
        )
    )
    #Auto

    OP_5A()
    Sleep(1200)

    def lambda_5C40():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5C40)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x1D, 0x1)
    WaitChrThread(0x1E, 3)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x2)

    def lambda_5C74():
        OP_95(0xFE, -6500, -300, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5C74)
    Sound(814, 0, 100, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)
    SetChrSubChip(0x1E, 0x1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0257
    ChrTalk(
        0x1E,
        "#6P#5S哇呀！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x1E)
    OP_93(0x1D, 0x10E, 0x12C)

    #C0258
    ChrTalk(
        0x1D,
        (
            "#11P#3400F啊呀……无意中\x01",
            "伸了一下脚。\x02\x03",

            "老婆婆，您不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1E,
        (
            "#6P你……你这混蛋……\x01",
            "干的什么好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1D,
        (
            "#11P#3404F……呵呵，\x01",
            "真是精神矍铄呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(11280, 1450, -20, 0)
    MoveCamera(45, 21, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x101, 3, 0, 36)
    BeginChrThread(0x102, 3, 0, 36)
    BeginChrThread(0x103, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 36)
    OP_68(-2430, 1450, -2420, 7000)
    OP_0D()

    #C0261
    ChrTalk(
        0x101,
        (
            "#0001F#6P#10A可恶，那么快的速度，\x01",
            "已经把我们抛下很远了……\x02",
        )
    )
    #Auto

    OP_5A()

    #C0262
    ChrTalk(
        0x102,
        "#0105F#6P#10A罗伊德，看啊，那里！\x02",
    )
    #Auto

    OP_5A()

    #C0263
    ChrTalk(
        0x101,
        "#0005F#6P#10A哎……\x02",
    )
    #Auto

    OP_5A()
    Fade(1000)
    OP_68(-4840, 1650, 1400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12680, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0264
    ChrTalk(
        0x101,
        (
            "#12P#0005F怎……\x01",
            "怎么会倒在这种地方！？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x104,
        (
            "#11P#0305F噢噢，这不是那位\x01",
            "黑头发的姐姐吗！\x02\x03",

            "#0301F难道说……\x01",
            "这是姐姐您做的！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x87, 0xE1)

    #C0266
    ChrTalk(
        0x1D,
        (
            "#5P#3403F……有话以后再说，\x01",
            "当务之急是先办正事。\x02\x03",

            "#3400F这位老婆婆似乎十分\x01",
            "有精神呢，如果不快点采取行动，\x01",
            "她大概很快就会爬起来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x1E,
        "#6P可、可恶～……！\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#12P#0001F……看来是这样的呢。\x01",
            "艾莉，来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        "#5P#0105F嗯。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(2000)
    BeginChrThread(0x1D, 3, 0, 41)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x1D, 3)

    #C0270
    ChrTalk(
        0x103,
        (
            "#12P#0200F很抱歉，能否请您\x01",
            "也与我们同行呢？\x02\x03",

            "#0203F毕竟您在逮捕行动中\x01",
            "提供了协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x1D,
        (
            "#5P#3403F……明白了。\x02\x03",

            "#3400F本来是不想太过张扬的，\x01",
            "但这也算是某种机缘巧合，没办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#11P#0303F放心吧！\x02\x03",

            "#0309F我会全力以赴地护送好\x01",
            "姐姐您的！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_34_5ACB end

    def Function_35_6160(): pass

    label("Function_35_6160")

    OP_68(19130, 1850, -1230, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14450, 0)
    SetChrPos(0x1E, 24040, -300, 870, 270)
    SetChrPos(0x101, 30000, -300, 0, 270)
    SetChrPos(0x102, 31000, -300, 1500, 270)
    SetChrPos(0x103, 32000, -300, 0, 270)
    SetChrPos(0x104, 33000, -300, 1500, 270)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_61F3():
        OP_95(0xFE, 20000, -300, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_61F3)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1E, 1)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x1E)

    #N0273
    NpcTalk(
        0x1E,
        "老婆婆",
        (
            "#5P……哼哼……\x01",
            "终于到克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #N0274
    NpcTalk(
        0x1E,
        "老婆婆",
        (
            "#5P接下来就只剩下与车站\x01",
            "和空港的那些孩子们会合，\x01",
            "然后找合适的地方开店了。\x02",
        )
    )

    CloseMessageWindow()

    #N0275
    NpcTalk(
        0x1E,
        "老婆婆",
        (
            "#5P每年都能大赚一笔……\x01",
            "克洛斯贝尔还真是个\x01",
            "赚钱的好地方呀。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(400, 20, -1, -1)
    SetChrName("罗伊德")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            "#0001F……请、请您\x01",
            "稍等一下！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #N0277
    NpcTalk(
        0x1E,
        "老婆婆",
        "#5P……？\x02",
    )

    CloseMessageWindow()
    OP_68(21470, 1850, -490, 3000)
    OP_93(0x1E, 0x5A, 0x1F4)

    def lambda_636D():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_636D)

    def lambda_6387():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6387)

    def lambda_63A1():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63A1)

    def lambda_63BB():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_63BB)

    def lambda_63D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63D5)

    def lambda_63E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_63E6)

    def lambda_63F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_63F7)

    def lambda_6408():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6408)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0003F#11P我们是克洛斯贝警察局·特别\x01",
            "任务支援科的成员。\x02\x03",

            "#0001F老婆婆……很不好意思，\x01",
            "能否和您稍微说几句话呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0279
    NpcTalk(
        0x1E,
        "老婆婆",
        "#6P……警……警察？\x02",
    )

    CloseMessageWindow()

    #N0280
    NpcTalk(
        0x1E,
        "老婆婆",
        (
            "#6P警、警察为什么要找我呢，\x01",
            "究竟有什么事啊？\x02",
        )
    )

    CloseMessageWindow()

    #N0281
    NpcTalk(
        0x1E,
        "老婆婆",
        (
            "#6P我现在马上就要去\x01",
            "找孙儿了，所、所以……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#11P#0001F……已经不用再演戏了。\x01",
            "如果没猜错，恐怕你就是\x01",
            "假货贩子团伙的头目吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0283
    NpcTalk(
        0x1E,
        "老婆婆",
        "#6P……！！\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#11P#0101F如果愿意配合，现在跟我们回去，\x01",
            "也就可以省去不必要的麻烦了。\x02\x03",

            "#0103F怎么样，就请老老实实地……\x02",
        )
    )

    CloseMessageWindow()

    #N0285
    NpcTalk(
        0x1E,
        "老婆婆",
        "#6P……………………别……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0286
    ChrTalk(
        0x1E,
        (
            "#6P#5S……别看不起人了！\x01",
            "你们这群可恨的小鬼啊啊啊啊啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#11P#0011F……哎！！？\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        "#11P#0105F呀！！\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        "#11P#0305F怎、怎么回事……！？\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        "#12P#0201F……原形毕露了呢。\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0291
    ChrTalk(
        0x1E,
        (
            "#6P#5S想抓我？\x01",
            "有那么简单吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0292
    ChrTalk(
        0x1E,
        (
            "#6P#5S这样的话，我就一直逃，一直逃，\x01",
            "直到跑到天涯海角也可以！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x1E,
        (
            "#6P#5S要是你有本事\x01",
            "抓到我的话……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_67C3():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_67C3)
    Sleep(1000)

    def lambda_67E0():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_67E0)
    Sleep(1000)

    def lambda_67FD():
        OP_95(0xFE, 15000, -300, 1030, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_67FD)
    Sound(250, 0, 80, 0)
    PlayBGM("ed7401", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-50, 200, -1, -1)
    SetChrName("假货商")

    #A0294
    AnonymousTalk(
        0x1E,
        "#5S就来抓抓看吧！！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x101,
        "#11P#0011F……不、不好，被她逃掉了！！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        (
            "#11P#0306F哼，刚才那副\x01",
            "高雅老夫人的假面具，\x01",
            "现在给丢到哪里去了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x103,
        "#12P#0205F……速度真是惊人。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#11P#0106F够、够了！现在是吃惊的时候吗！？\x02\x03",

            "#0101F再不赶快追上去……\x01",
            "就真要被她逃掉了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#11P#0001F说、说得对啊……\x01",
            "赶快追吧，各位！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69F0():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69F0)

    def lambda_6A0A():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A0A)

    def lambda_6A24():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A24)

    def lambda_6A3E():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A3E)
    Sleep(1500)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x1E, 11450, -300, 1000, 270)
    SetChrPos(0x101, 24000, -300, 0, 270)
    SetChrPos(0x102, 25000, -300, 1500, 270)
    SetChrPos(0x103, 26000, -300, 0, 270)
    SetChrPos(0x104, 27000, -300, 1500, 270)
    SetChrPos(0x1D, 8000, -300, 190, 270)
    OP_68(9270, 1450, -1540, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11550, 0)
    OP_68(-5970, 1450, 2950, 5000)
    BeginChrThread(0x1E, 3, 0, 42)
    BeginChrThread(0x101, 3, 0, 36)
    BeginChrThread(0x102, 3, 0, 36)
    BeginChrThread(0x103, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 36)
    FadeToBright(500, 0)
    OP_0D()

    #C0300
    ChrTalk(
        0x1E,
        (
            "#5P#10A别看不起人了，\x01",
            "你们这群可恶的小鬼！\x02",
        )
    )
    #Auto

    OP_5A()

    #C0301
    ChrTalk(
        0x1E,
        (
            "#5P#10A凭我这副年轻时靠登山锻炼出来的身子骨，\x01",
            "要是以为自己能追上就尽管放马过来啊……\x02",
        )
    )
    #Auto

    OP_5A()
    WaitChrThread(0x1E, 3)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x2)

    def lambda_6BCB():
        OP_95(0xFE, -6500, -300, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6BCB)
    Sound(814, 0, 100, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)
    SetChrSubChip(0x1E, 0x1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0302
    ChrTalk(
        0x1E,
        "#6P#5S哇呀！！\x02",
    )

    OP_5A()
    OP_68(-4030, 1450, 1640, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(12760, 2000)
    OP_6F(0x1)

    #C0303
    ChrTalk(
        0x102,
        "#11P#0105F……老、老婆婆！？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x104,
        "#11P#0305F呜啊……脸部先着地呢，没事吧。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#12P#0206F好像很疼。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#0003F似乎有些可怜……\x01",
            "但还是要马上制服才行！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5970, 1450, 2950, 2000)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 43)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(2000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0307
    ChrTalk(
        0x104,
        (
            "#11P#0306F嘿～早知如此的话，\x01",
            "不要逃跑反而会比较好吧。\x02\x03",

            "#0300F上了年纪就不要勉强嘛，老婆婆。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x1E,
        (
            "#6P呜呜呜……！\x01",
            "谁是老婆婆啊！你这个呆头呆脑的蠢货……！\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        (
            "#12P#0203F这样的话……\x01",
            "总算是逮捕完毕了呢。\x02\x03",

            "#0200F但是，这都是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("女性的声音")
    SetMessageWindowPos(350, 0, -1, -1)

    #C0310
    ChrTalk(
        0x1D,
        "……干得漂亮。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6E97():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E97)

    def lambda_6EA4():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EA4)

    def lambda_6EB1():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6EB1)

    def lambda_6EBE():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6EBE)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x1D, 3, 0, 45)
    OP_68(-3950, 1450, 1920, 2000)
    WaitChrThread(0x1D, 3)

    #C0311
    ChrTalk(
        0x1D,
        (
            "#3404F呵呵……\x01",
            "有生以来，好像还是第一次\x01",
            "看到警察抓人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x02\x03",

            "#0004F十分感谢您的助言。\x01",
            "只差一步就要被她逃掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        (
            "#0309F呀～真是千钧一发啊。\x01",
            "多亏了姐姐你的帮忙！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        (
            "#12P#0200F还好老婆婆被绊倒了，\x01",
            "我们实在是很走运。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#0104F嗯，好像是被路边的石头\x01",
            "给绊倒了呢。\x02\x03",

            "#0100F虽然是脸先着地的，\x01",
            "但看来只是轻伤哦。\x02\x03",

            "#0103F该怎么说……\x01",
            "感觉重重偶然连续发生了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x1D,
        (
            "#3403F万物都会回归至\x01",
            "它们所应在的地方。\x02\x03",

            "老婆婆的跌倒也并非偶然，\x01",
            "而是必然……\x02\x03",

            "#3400F……真遗憾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x1E,
        "#6P可、可恶～……！\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#0001F……赶快把她\x01",
            "带回总部吧。\x02\x03",

            "#0006F要是再被她逃掉可就不好办了。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        "#0100F嗯，说的对呢。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        (
            "#12P#0200F很不好意思，能否请您\x01",
            "也与我们同行呢？\x02\x03",

            "承蒙您协助进行逮捕，\x01",
            "就算只是走个形式，也希望您\x01",
            "去做个简单的笔录……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x1D,
        (
            "#3404F……明白了。\x02\x03",

            "#3400F本来是不想太过张扬的，\x01",
            "但这也算是某种机缘巧合，没办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x104,
        (
            "#0304F放心吧！\x02\x03",

            "#0309F我会全力以赴地护送好\x01",
            "姐姐您的！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_35_6160 end

    def Function_36_725C(): pass

    label("Function_36_725C")


    def lambda_7261():
        OP_98(0xFE, 0xFFFF9A70, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7261)
    WaitChrThread(0xFE, 1)

    def lambda_727F():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_727F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_725C end

    def Function_37_728C(): pass

    label("Function_37_728C")

    OP_68(-5580, 1450, 2490, 3000)

    def lambda_72A2():
        OP_95(0xFE, -7010, -300, 4430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72A2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x12C)
    Return()

    # Function_37_728C end

    def Function_38_72C3(): pass

    label("Function_38_72C3")


    def lambda_72C8():
        OP_95(0xFE, -5410, -300, 4430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72C8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_72C3 end

    def Function_39_72E2(): pass

    label("Function_39_72E2")


    def lambda_72E7():
        OP_95(0xFE, -4750, -300, 2009, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72E7)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1D, 300)
    Return()

    # Function_39_72E2 end

    def Function_40_7308(): pass

    label("Function_40_7308")


    def lambda_730D():
        OP_95(0xFE, -3190, -300, 2410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_730D)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1D, 300)
    Return()

    # Function_40_7308 end

    def Function_41_732E(): pass

    label("Function_41_732E")


    def lambda_7333():
        OP_95(0xFE, -3800, -300, 3830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7333)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_41_732E end

    def Function_42_7354(): pass

    label("Function_42_7354")


    def lambda_7359():
        OP_95(0xFE, -60, -300, 660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7359)
    WaitChrThread(0x1E, 1)

    def lambda_7377():
        OP_95(0xFE, -5000, -300, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7377)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_42_7354 end

    def Function_43_7391(): pass

    label("Function_43_7391")


    def lambda_7396():
        OP_95(0xFE, -4750, -300, 2009, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7396)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_7391 end

    def Function_44_73B0(): pass

    label("Function_44_73B0")


    def lambda_73B5():
        OP_95(0xFE, -4190, -300, 4030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73B5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_73B0 end

    def Function_45_73CF(): pass

    label("Function_45_73CF")


    def lambda_73D4():
        OP_98(0xFE, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73D4)
    WaitChrThread(0xFE, 1)

    def lambda_73F2():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73F2)

    def lambda_73FF():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_73FF)

    def lambda_740C():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_740C)

    def lambda_7419():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7419)

    def lambda_7426():
        OP_95(0xFE, -2870, -300, 2070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7426)
    OP_68(-5360, 1450, 2770, 2000)
    WaitChrThread(0xFE, 1)

    def lambda_7455():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7455)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_73CF end

    def Function_46_7462(): pass

    label("Function_46_7462")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_END)), "loc_7496")
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "供奉着东方的地藏菩萨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8E66")

    label("loc_7496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7638")
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "供奉着东方的地藏菩萨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0325
    ChrTalk(
        0x104,
        (
            "#0305F哎～虽然知道这条街\x01",
            "是东方风格的，\x01",
            "但没想到竟然还供奉着地藏菩萨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        (
            "#0200F我好像是第一次见到地藏菩萨。\x01",
            "……好大的脸呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x103,
        "#0205F地藏菩萨面前的台座是……？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#0100F一定是\x01",
            "摆放供品的台座吧。\x02\x03",

            "如果下次做出了大成功的料理，\x01",
            "就拿点来供奉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000F对了，支援科基本都是自己煮饭。\x02\x03",

            "如果下次做了成功的料理，\x01",
            "就拿到这里来好啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 0)
    Jump("loc_8E66")

    label("loc_7638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7669")
    SetChrName("")

    #A0330
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "供奉着东方的地藏菩萨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8E66")

    label("loc_7669")

    Call(0, 47)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76DF")
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "供奉着东方的地藏菩萨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0332
    ChrTalk(
        0x101,
        (
            "#0000F现在好像没有\x01",
            "适合供奉的料理哦。\x02\x03",

            "下次再拿过来吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_76DF")

    Call(0, 48)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78CE")
    SetChrName("")

    #A0333
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在闪闪发光的回路旁边\x01",
            "有一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一直诚心供奉着地藏菩萨的朋友们，\x01",
            "虽然我们并不相识，\x01",
            "但还是谢谢各位的热心。\x01",
            "虽然只留下这样一封信确实很失礼，\x01",
            "但各位的热心行为\x01",
            "使我深受感动，\x01",
            "因此我真心觉得\x01",
            "自己必须做点什么。\x02",
        )
    )

    CloseMessageWindow()

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果说是代替地藏菩萨感谢各位，未免有些僭越之嫌，\x01",
            "但我还是准备了谢礼。\x01",
            "希望能为各位所用。\x01",
            "请务必接受我的这份谢意。\x01\x01",
            "　　　　　～一名素不相识的邻人\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('明王铃', 1)
    SetScenarioFlags(0x98, 7)
    Jump("loc_8E66")

    label("loc_78CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A9F")
    SetChrName("")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旁边\x01",
            "有一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这样一个清爽闲适，\x01",
            "晴朗无云的早晨，\x01",
            "我与往常一样参拜地藏菩萨时，\x01",
            "看到了各位所\x01",
            "供奉的精美食物。\x01",
            "总来供奉料理的朋友，你使我感到了发自内心\x01",
            "的欣喜，于是我就执笔写下了这封信。\x01",
            "各位的热心一直感动着我，\x01",
            "在这里，我要向各位说声谢谢。\x02",
        )
    )

    CloseMessageWindow()

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是我对各位的一点回礼，\x01",
            "虽然不是什么贵重的东西，\x01",
            "但请务必接受我的这份谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('回复药', 1)
    SetScenarioFlags(0x98, 6)
    Jump("loc_8E66")

    label("loc_7A9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C5F")
    SetChrName("")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旁边\x01",
            "有一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "用各种上等料理供奉着地藏菩萨的\x01",
            "应该一直都是各位吧。\x01",
            "每次我经过这里，\x01",
            "都会被各位的热心所触动，\x01",
            "进而让我得以度过愉悦的一天。\x01",
            "虽然克洛斯贝尔近日骚乱不断，\x01",
            "但只要有像各位一样热心的朋友在，\x01",
            "这个社会必定能迎来光明的未来。\x02",
        )
    )

    CloseMessageWindow()

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "行文冗长，实在是失礼了。\x01",
            "虽然只是一点薄礼，\x01",
            "但请务必接受我的这份谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('回复药', 1)
    SetScenarioFlags(0x98, 5)
    Jump("loc_8E66")

    label("loc_7C5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB3")
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旁边\x01",
            "有一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我每天清晨都会\x01",
            "来参拜地藏菩萨。\x01",
            "当得知还有其他朋友\x01",
            "也会来参拜地藏菩萨时，\x01",
            "实在是万分欣喜。\x02",
        )
    )

    CloseMessageWindow()

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然未曾直接会面，\x01",
            "也并不了解各位，\x01",
            "但各位一定经常来参拜吧。\x01",
            "还请务必接受我的这份谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('回复药', 1)
    SetScenarioFlags(0x98, 4)
    Jump("loc_8E66")

    label("loc_7DB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EE0")
    SetChrName("")

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旁边\x01",
            "有一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一直供奉着地藏菩萨的\x01",
            "各位朋友，谢谢你们。\x01",
            "能有这么热心的朋友们来参拜，\x01",
            "我想地藏菩萨一定\x01",
            "也十分高兴。\x01",
            "这是我的一点谢意，虽然只是薄礼\x01",
            "但请务必收下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('回复药', 1)
    SetScenarioFlags(0x98, 3)
    Jump("loc_8E66")

    label("loc_7EE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FD7")
    SetChrName("")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旁边\x01",
            "有一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然我与各位素不相识，\x01",
            "但真的非常感谢\x01",
            "你们能经常来供奉地藏菩萨。\x01",
            "还请务必接受\x01",
            "我的这份谢意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('回复药', 1)
    SetScenarioFlags(0x98, 2)
    Jump("loc_8E66")

    label("loc_7FD7")

    SetChrName("")

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "供奉着东方的地藏菩萨。\x02\x03",

            "要供奉制作大成功的料理吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8020")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E66")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_806B")
    MenuCmd(1, 1, "霸王面")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_8061")
    Call(0, 13)

    label("loc_8061")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_806B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80A4")
    MenuCmd(1, 1, "药膳麻婆『黄龙』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_809A")
    Call(0, 13)

    label("loc_809A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80D5")
    MenuCmd(1, 1, "白虎炒饭")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_80CB")
    Call(0, 13)

    label("loc_80CB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_810C")
    MenuCmd(1, 1, "极品牛排『雅』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_8102")
    Call(0, 13)

    label("loc_8102")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_810C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8143")
    MenuCmd(1, 1, "极品炖菜『薰』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_8139")
    Call(0, 13)

    label("loc_8139")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_817A")
    MenuCmd(1, 1, "铁人锅『绚烂』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_8170")
    Call(0, 13)

    label("loc_8170")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_817A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81B1")
    MenuCmd(1, 1, "贤人锅『缭乱』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_81A7")
    Call(0, 13)

    label("loc_81A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81E8")
    MenuCmd(1, 1, "起死回生炸鱼排")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_81DE")
    Call(0, 13)

    label("loc_81DE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_821F")
    MenuCmd(1, 1, "黄金蛋饭『辉』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_8215")
    Call(0, 13)

    label("loc_8215")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_821F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8256")
    MenuCmd(1, 1, "黄金蛋面『煌』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_824C")
    Call(0, 13)

    label("loc_824C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8287")
    MenuCmd(1, 1, "汉堡之王")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_827D")
    Call(0, 13)

    label("loc_827D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82B8")
    MenuCmd(1, 1, "女王比萨")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_82AE")
    Call(0, 13)

    label("loc_82AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82F3")
    MenuCmd(1, 1, "行乐三明治『搭档』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_82E9")
    Call(0, 13)

    label("loc_82E9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8330")
    MenuCmd(1, 1, "爱心凝缩盒饭『母亲』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_8326")
    Call(0, 13)

    label("loc_8326")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_835F")
    MenuCmd(1, 1, "满月汤")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_8355")
    Call(0, 13)

    label("loc_8355")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_835F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_838E")
    MenuCmd(1, 1, "新月汤")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_8384")
    Call(0, 13)

    label("loc_8384")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_838E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83C9")
    MenuCmd(1, 1, "绝品甜点『白无垢』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_83BF")
    Call(0, 13)

    label("loc_83BF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8402")
    MenuCmd(1, 1, "绝品甜点『黄熟』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_83F8")
    Call(0, 13)

    label("loc_83F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_843B")
    MenuCmd(1, 1, "绝品甜点『粉雪』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_8431")
    Call(0, 13)

    label("loc_8431")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_843B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8474")
    MenuCmd(1, 1, "绝品甜点『浮云』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_846A")
    Call(0, 13)

    label("loc_846A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84A5")
    MenuCmd(1, 1, "极品拿铁")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_849B")
    Call(0, 13)

    label("loc_849B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84DA")
    MenuCmd(1, 1, "终极混合果汁")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_84D0")
    Call(0, 13)

    label("loc_84D0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_850B")
    MenuCmd(1, 1, "梦魇杀手")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_8501")
    Call(0, 13)

    label("loc_8501")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_850B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8542")
    MenuCmd(1, 1, "秘水『月光蝶』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_8538")
    Call(0, 13)

    label("loc_8538")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8542")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8581")
    Jump("loc_8E61")

    label("loc_8581")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上面『日轮』', 1)
    SetScenarioFlags(0x99, 0)

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_85E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8638")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('神仙麻婆『麒麟』', 1)
    SetScenarioFlags(0x99, 1)

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_862E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8684")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_867A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天下一品炒饭', 1)
    SetScenarioFlags(0x99, 2)

    #A0358
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_867A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86D0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('极品牛排『刚』', 1)
    SetScenarioFlags(0x99, 3)

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_86C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_871C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8712")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('三日久煮炖菜', 1)
    SetScenarioFlags(0x99, 4)

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8712")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_871C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8768")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大地锅『烂漫』', 1)
    SetScenarioFlags(0x99, 5)

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_875E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_87B4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87AA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天河锅『瑞云』', 1)
    SetScenarioFlags(0x99, 6)

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_87AA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8800")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('特快炸鱼『疾』', 1)
    SetScenarioFlags(0x99, 7)

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_87F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_884C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8842")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('丰盛蛋包饭', 1)
    SetScenarioFlags(0x9A, 0)

    #A0364
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8842")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_884C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8898")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_888E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠玉面『治愈』', 1)
    SetScenarioFlags(0x9A, 1)

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_888E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88E4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('双层汉堡', 1)
    SetScenarioFlags(0x9A, 2)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_88DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8930")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8926")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('四味奶酪比萨', 1)
    SetScenarioFlags(0x9A, 3)

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8926")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_897C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8972")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('强效三明治', 1)
    SetScenarioFlags(0x9A, 4)

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8972")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_897C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89BE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('真心盒饭『诚』', 1)
    SetScenarioFlags(0x9A, 5)

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_89BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A14")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('辉煌汤', 1)
    SetScenarioFlags(0x9A, 6)

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8A0A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A60")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('奇幻糖果', 1)
    SetScenarioFlags(0x9A, 7)

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8A56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AAC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AA2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上甜点『夜月』', 1)
    SetScenarioFlags(0x9B, 0)

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8AA2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AF8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AEE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('宝物甜点『白雪』', 1)
    SetScenarioFlags(0x9B, 1)

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8AEE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B44")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B3A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冰凉甜点『七彩』', 1)
    SetScenarioFlags(0x9B, 2)

    #A0374
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8B3A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B90")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B86")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('绝品甜点『瞬动』', 1)
    SetScenarioFlags(0x9B, 3)

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8B86")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BDC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('玉露『绿风』', 1)
    SetScenarioFlags(0x9B, 4)

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8BD2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C28")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C1E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('甘露『紫绀』', 1)
    SetScenarioFlags(0x9B, 5)

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8C1E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C74")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C6A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑茶『梦魇杀手』', 1)
    SetScenarioFlags(0x9B, 6)

    #A0378
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8C6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CC0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('秘水『桃源乡』', 1)
    SetScenarioFlags(0x9B, 7)

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_8CB6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CC0")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E5E")

    #C0380
    ChrTalk(
        0x101,
        (
            "#0000F这样就行了。\x01",
            "……下次有机会再拿料理来供奉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D7C")

    #C0381
    ChrTalk(
        0x102,
        (
            "#0100F总拿同样的料理来\x01",
            "未免有些失礼，\x01",
            "最好每次都供奉不同的种类呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E3F")

    label("loc_8D7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DDF")

    #C0382
    ChrTalk(
        0x103,
        (
            "#0200F如果每次都供奉同一种\x01",
            "料理好像会很失礼。\x01",
            "最好每次都供奉不同的种类。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E3F")

    label("loc_8DDF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E3F")

    #C0383
    ChrTalk(
        0x104,
        (
            "#0300F老是供奉同一种\x01",
            "料理的话好像会很失礼吧？\x01",
            "最好每次都供奉不同的种类哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E3F")


    #C0384
    ChrTalk(
        0x101,
        "#0000F嗯，就这么做吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 1)

    label("loc_8E5E")

    SetScenarioFlags(0x1, 7)

    label("loc_8E61")

    Jump("loc_8020")

    label("loc_8E66")

    TalkEnd(0xFF)
    Return()

    # Function_46_7462 end

    def Function_47_8E6A(): pass

    label("Function_47_8E6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E8D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EA6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EBF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8ED8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EF1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F0A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F23")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F3C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F55")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F6E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F87")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FA0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FB9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FD2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FEB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9004")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_901D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_901D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9036")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_904F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_904F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9068")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9081")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_909A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_909A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90B3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90CC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90CC")

    Return()

    # Function_47_8E6A end

    def Function_48_90CD(): pass

    label("Function_48_90CD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_90EA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_90FD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_9110")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_9123")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_9136")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_9149")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_915C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_915C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_916F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_916F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_9182")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_9195")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_91A8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_91BB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_91CE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_91E1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_91F4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_9207")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_921A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_921A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_922D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_922D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_9240")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_9253")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_9266")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_9279")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_928C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_928C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_929F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_929F")

    Return()

    # Function_48_90CD end

    SaveToFile()

Try(main)
