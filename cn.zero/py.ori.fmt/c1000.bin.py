from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1000.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1000",                  # 0
        "库隆克",                 # 1
        "迪因兹",                 # 2
        "莉莉",                   # 3
        "玛尔缇",                 # 4
        "安奈",                   # 5
        "卢诺爷爷",               # 6
        "洛依",                   # 7
        "鲁斯",                   # 8
        "梅琳",                   # 9
        "斯赞",                   # 10
        "基雷",                   # 11
        "库塔",                   # 12
        "游客",                   # 13
        "艾丝蒂尔",               # 14
        "约修亚",                 # 15
        "滴",                     # 16
        "列车",                   # 17
        "中央广场",               # 18
        "西街",                   # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "欢乐街",                 # 22
        "东街",                   # 23
        "旧城区",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "站前街道",               # 27
        "后巷",                   # 28
        "乌尔斯拉间道",           # 29
        "东克洛斯贝尔街道",       # 30
        "西克洛斯贝尔街道",       # 31
        "玛因兹山道",             # 32
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch24900.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch21400.itc",                   # 0A
        "chr/ch00600.itc",                   # 0B
        "chr/ch00700.itc",                   # 0C
        "chr/ch08700.itc",                   # 0D
        "chr/ch22800.itc",                   # 0E
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   2,   0,   0,   6,   0,   12,  255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   5,   0,   18,  255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  261,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5300,    -3000,   -13220,  270,  389,  0x0, 0,   6,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-22280,  -300,    18370,   225,  261,  0x0, 0,   7,   0,   0,   2,   0,   20,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   10,  0,   0,   3,   0,   23,  255,  0)
    DeclNpc(-4190,   -300,    -1210,   225,  389,  0x0, 0,   0,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-23690,  -3000,   3190,    270,  405,  0x0, 0,   11,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-25129,  -3000,   3630,    90,   405,  0x0, 0,   12,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-23530,  -3000,   4090,    270,  405,  0x0, 0,   13,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -7.920000076293945,    13.430000305175781,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.9600000381469727,    -6.715000152587891,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 37,  -7.789999961853027,    -7.980000019073486,    -3.0,                  25.0,                  [0.35355326533317566,  0.1414213925600052,    -0.0,                  0.0,                   -0.35355350375175476,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.06717704236507416,  2.2302145957946777,    0.5999999642372131,    1.0])
    DeclEvent(0x0000, 0, 38,  2.200000047683716,     -2.2300000190734863,   -0.30000001192092896,  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.4399999976158142,   1.1150000095367432,    0.05999999865889549,   1.0])

    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  39, 0x0000)

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
    PlaceName(-98.33000183105469, 0.0, 1.440000057220459, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6F0",          # 00, 0
        "Function_1_7A8",          # 01, 1
        "Function_2_841",          # 02, 2
        "Function_3_86C",          # 03, 3
        "Function_4_8E1",          # 04, 4
        "Function_5_92E",          # 05, 5
        "Function_6_9EF",          # 06, 6
        "Function_7_A3C",          # 07, 7
        "Function_8_AAC",          # 08, 8
        "Function_9_F19",          # 09, 9
        "Function_10_10A5",        # 0A, 10
        "Function_11_1E49",        # 0B, 11
        "Function_12_2E12",        # 0C, 12
        "Function_13_3C75",        # 0D, 13
        "Function_14_57C7",        # 0E, 14
        "Function_15_664A",        # 0F, 15
        "Function_16_678D",        # 10, 16
        "Function_17_6956",        # 11, 17
        "Function_18_752D",        # 12, 18
        "Function_19_84A4",        # 13, 19
        "Function_20_901B",        # 14, 20
        "Function_21_962C",        # 15, 21
        "Function_22_9E65",        # 16, 22
        "Function_23_9EE9",        # 17, 23
        "Function_24_A99C",        # 18, 24
        "Function_25_AB1F",        # 19, 25
        "Function_26_ABDA",        # 1A, 26
        "Function_27_AC92",        # 1B, 27
        "Function_28_AD63",        # 1C, 28
        "Function_29_B0BA",        # 1D, 29
        "Function_30_B51F",        # 1E, 30
        "Function_31_B734",        # 1F, 31
        "Function_32_C3A0",        # 20, 32
        "Function_33_C3FD",        # 21, 33
        "Function_34_CB6A",        # 22, 34
        "Function_35_CF99",        # 23, 35
        "Function_36_D2C8",        # 24, 36
        "Function_37_D536",        # 25, 37
        "Function_38_D5F4",        # 26, 38
        "Function_39_D6B2",        # 27, 39
        "Function_40_F34C",        # 28, 40
        "Function_41_F5AF",        # 29, 41
    ))


    def Function_0_6F0(): pass

    label("Function_0_6F0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_730"),
        (1, "loc_73C"),
        (2, "loc_748"),
        (3, "loc_754"),
        (4, "loc_760"),
        (5, "loc_76C"),
        (6, "loc_778"),
        (SWITCH_DEFAULT, "loc_784"),
    )


    label("loc_730")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_73C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_748")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_754")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_760")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_76C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_778")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_784")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_7A7")

    Return()

    # Function_0_6F0 end

    def Function_1_7A8(): pass

    label("Function_1_7A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_840")
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
    Jump("Function_1_7A8")

    label("loc_840")

    Return()

    # Function_1_7A8 end

    def Function_2_841(): pass

    label("Function_2_841")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86B")
    OP_94(0xFE, 0xFFFFB000, 0x4ECA, 0xFFFFA8EE, 0x3F01, 0x3E8)
    Sleep(300)
    Jump("Function_2_841")

    label("loc_86B")

    Return()

    # Function_2_841 end

    def Function_3_86C(): pass

    label("Function_3_86C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E0")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_3_86C")

    label("loc_8E0")

    Return()

    # Function_3_86C end

    def Function_4_8E1(): pass

    label("Function_4_8E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92D")
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -9950, -3000, -6670, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_4_8E1")

    label("loc_92D")

    Return()

    # Function_4_8E1 end

    def Function_5_92E(): pass

    label("Function_5_92E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
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
    Jump("Function_5_92E")

    label("loc_9EE")

    Return()

    # Function_5_92E end

    def Function_6_9EF(): pass

    label("Function_6_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3B")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_6_9EF")

    label("loc_A3B")

    Return()

    # Function_6_9EF end

    def Function_7_A3C(): pass

    label("Function_7_A3C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB")
    SetChrPos(0x18, 70000, -27500, -17600, 0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x18)
    OP_49()
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_9B(0x0, 0x18, 0x10E, 0x30D40, 0x4E20, 0x0)
    SetChrFlags(0x18, 0x80)
    SetMapObjFlags(0x0, 0x4)

    label("loc_AAB")

    Return()

    # Function_7_A3C end

    def Function_8_AAC(): pass

    label("Function_8_AAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCC")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B77")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4A")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_B69")

    label("loc_B4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B69")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_B69")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCC")

    label("loc_B77")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2B")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFE")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_C1D")

    label("loc_BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1D")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_C1D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCC")

    label("loc_C2B")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA4")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_CC3")

    label("loc_CA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC3")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_CC3")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCC")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEE")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D05")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x2, 4)
    Event(0, 30)
    Jump("loc_D14")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D14")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 31)

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D6D")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, -18200, -300, 18140, 0)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x10, 0x10)

    label("loc_D68")

    Jump("loc_F01")

    label("loc_D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_D90")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    BeginChrThread(0x13, 0, 0, 4)
    Jump("loc_F01")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D9E")
    Jump("loc_F01")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_F01")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_DE9")
    Jump("loc_F01")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DF7")
    Jump("loc_F01")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E32")
    SetChrPos(0xE, -18820, -320, 21060, 0)
    SetChrPos(0x10, -18680, -310, 19940, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E6D")
    SetChrPos(0xE, -18200, -300, 18140, 135)
    SetChrPos(0x10, -18690, -320, 19040, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_E7B")
    Jump("loc_F01")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E89")
    Jump("loc_F01")

    label("loc_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E97")
    Jump("loc_F01")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_EA5")
    Jump("loc_F01")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_EB3")
    Jump("loc_F01")

    label("loc_EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_EC6")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_F01")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_F01")
    SetChrPos(0xE, -18200, -300, 18140, 0)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x14, 0x80)

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F18")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_F18")

    Return()

    # Function_8_AAC end

    def Function_9_F19(): pass

    label("Function_9_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_F2B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_FCD")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FA8")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_FCD")

    label("loc_FA8")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_FCD")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FEF")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1002")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1015")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1028")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103B")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1049")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1049")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1061")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1061")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1083")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109F")
    Jump("loc_10A4")

    label("loc_109F")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_10A4")

    Return()

    # Function_9_F19 end

    def Function_10_10A5(): pass

    label("Function_10_10A5")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E45")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1102")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1102")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1122")
    OP_AF(0x39)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E40")

    label("loc_1122")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1136")
    Jump("loc_1E40")

    label("loc_1136")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E40")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D4")

    #C0001
    ChrTalk(
        0x101,
        (
            "#0003F（东街的市场……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_11D4")


    #C0002
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "失物啊……？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "没有，没见过。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "我每天都会打扫店前，\x01",
            "从来没见过什么失物。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        "#0106F（看来没有掉在这家店里呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_12E5")

    label("loc_1290")


    #C0007
    ChrTalk(
        0xFE,
        (
            "失物……我好像\x01",
            "没什么印象哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "你们去其它露天店\x01",
            "问问看吧？\x01",
            "大家人都很好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E5")

    Jump("loc_1E40")

    label("loc_12EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1340")

    #C0009
    ChrTalk(
        0xFE,
        (
            "刚才游击士们\x01",
            "一起出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "不知道是要去哪里呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_137A")

    label("loc_1340")


    #C0011
    ChrTalk(
        0xFE,
        (
            "他们每个人走的\x01",
            "方向都不一样……\x01",
            "不知道是要去哪里呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137A")

    Jump("loc_1E40")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_13FB")

    #C0012
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "这是库隆克工艺品店的新作品哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "手工制作的挂饰\x01",
            "最适合用来当礼物了！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "千万不要错过哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E40")

    label("loc_13FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_14C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1471")

    #C0015
    ChrTalk(
        0xFE,
        (
            "昨天晚上，港湾公园那边\x01",
            "好像发生了枪战。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔……\x01",
            "这个城市果然\x01",
            "很不安全啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14C3")

    label("loc_1471")


    #C0017
    ChrTalk(
        0xFE,
        (
            "这附近有游击士协会，\x01",
            "所以算是没问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "不过克洛斯贝尔\x01",
            "果然很不安全啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C3")

    Jump("loc_1E40")

    label("loc_14C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_15AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1570")

    #C0019
    ChrTalk(
        0xFE,
        (
            "上个星期，有一群穿黑衣服的人\x01",
            "把这附近占领了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "还威胁我们\x01",
            "交保护费。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "那就是克洛斯贝尔的黑手党吗？\x01",
            "……果然如传闻中一样可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_15A5")

    label("loc_1570")


    #C0022
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的黑手党……\x01",
            "果然如传闻中一样可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A5")

    Jump("loc_1E40")

    label("loc_15AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1663")

    #C0023
    ChrTalk(
        0xFE,
        (
            "工艺品在纪念庆典期间卖得很好，\x01",
            "所以我就开发制作了更多新种类。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "不过身上的伤因此\x01",
            "也有所增加……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "呵呵，不用担心。\x01",
            "因为克洛斯贝尔\x01",
            "有很棒的医院哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16AB")

    label("loc_1663")


    #C0026
    ChrTalk(
        0xFE,
        (
            "下午我就去\x01",
            "乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "有这么棒的医院，\x01",
            "受了伤也不用怕哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AB")

    Jump("loc_1E40")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_17B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1775")

    #C0028
    ChrTalk(
        0xFE,
        (
            "制作工艺品的乐趣……\x01",
            "那就是观察顾客看到工艺品后的反应哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "顾客看到精致的工艺品时，\x01",
            "那震惊的表情，\x01",
            "最让我高兴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "呵呵，不过作为代价，\x01",
            "我身上添了许多伤口。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_17AC")

    label("loc_1775")


    #C0031
    ChrTalk(
        0xFE,
        (
            "我想做个好作品来当\x01",
            "自治州创立七十周年的纪念品哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AC")

    Jump("loc_1E40")

    label("loc_17B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_17F4")

    #C0032
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "今天有新产品哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "请一定要看看！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E40")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_18B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1876")

    #C0034
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……我在使用工具的时候，\x01",
            "不小心把手指甲掀开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "工作的时候真的不能分神啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_18AD")

    label("loc_1876")


    #C0037
    ChrTalk(
        0xFE,
        "哎呀呀，又增加了一处伤口。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "希望能\x01",
            "早点治好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AD")

    Jump("loc_1E40")

    label("loc_18B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_196C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193A")

    #C0039
    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "下个月就是创立纪念庆典了。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "今年是自治州创立七十周年，\x01",
            "所以我想做个东西来当纪念品。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1967")

    label("loc_193A")


    #C0042
    ChrTalk(
        0xFE,
        (
            "现在就必须开始考虑\x01",
            "准备纪念庆典的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1967")

    Jump("loc_1E40")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F3")

    #C0043
    ChrTalk(
        0xFE,
        "刚才我在搬木箱的时候……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "脚撞到了\x01",
            "那边的阶梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "呵……这种痛只是小菜一碟。\x01",
            "可没法让我认输哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A43")

    label("loc_19F3")


    #C0046
    ChrTalk(
        0xFE,
        (
            "呵……工艺家这种职业\x01",
            "总是会伴随着伤痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "这点小痛\x01",
            "可没办法让我认输哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    Jump("loc_1E40")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1AAC")

    #C0048
    ChrTalk(
        0xFE,
        (
            "最近营业额\x01",
            "上涨了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "呵……真让人开心啊。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "总算不枉费\x01",
            "我的带伤劳动了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E40")

    label("loc_1AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6F")

    #C0051
    ChrTalk(
        0xFE,
        (
            "痛痛痛……\x01",
            "我的手指又受伤了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "制作工艺品时\x01",
            "经常会受伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "绝、绝对不是\x01",
            "因为我笨拙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "手艺再怎么老练的人\x01",
            "也是会受伤的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1BC0")

    label("loc_1B6F")


    #C0056
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "受伤已经是家常便饭了。\x01",
            "要是在意那些，就没法制作工艺品了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC0")

    Jump("loc_1E40")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1CA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C43")

    #C0058
    ChrTalk(
        0xFE,
        (
            "旧城区的不良少年们\x01",
            "经常来找茬。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "因为我这里卖的\x01",
            "都是些少见的物品……\x01",
            "哼，真让人火大啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C9F")

    label("loc_1C43")


    #C0060
    ChrTalk(
        0xFE,
        (
            "旧城区的不良少年们\x01",
            "时不时就会来找茬。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "每次都害得我营业额下降。\x01",
            "真是让人火大啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9F")

    Jump("loc_1E40")

    label("loc_1CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE0")

    #C0062
    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "我们这里卖的是\x01",
            "手工制作的精美工艺品哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#0005F咦，还有这种店啊……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0200F那个，这个\x01",
            "转个不停的东西是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "呵呵，您真有眼光啊，\x01",
            "让我好好来介绍一下。\x01",
            "这东西叫做『风车』。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "据说在东方被用来\x01",
            "辟邪和招运。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "怎么样，买一个吧。\x01",
            "或许会给您\x01",
            "带来幸运哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E40")

    label("loc_1DE0")


    #C0069
    ChrTalk(
        0xFE,
        (
            "除了风车，我们这里\x01",
            "还有许多其它精致的工艺品，\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "而且全都是手工制作的。\x01",
            "千万不要错过哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E40")

    Jump("loc_10B2")

    label("loc_1E45")

    TalkEnd(0xFE)
    Return()

    # Function_10_10A5 end

    def Function_11_1E49(): pass

    label("Function_11_1E49")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1EA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC6")
    OP_AF(0x38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E09")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDA")
    Jump("loc_2E09")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E09")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F78")

    #C0071
    ChrTalk(
        0x101,
        (
            "#0003F（东街的市场……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_1F78")


    #C0072
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "……什么，失物！？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "没见过哦。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "我们每天早上很早就开店，\x01",
            "要是有那种东西的话，应该会注意到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "如果是很重要的物品，\x01",
            "就去警察那里报案试试吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#0006F（我们自己就是警察啊……）\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        (
            "#0203F（克洛斯贝尔的警察果然不怎么\x01",
            "  得人心啊，知名度好低。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_210E")

    label("loc_20CB")


    #C0079
    ChrTalk(
        0xFE,
        (
            "失物吗……\x01",
            "我们这边没见过哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "不好意思啊，帮不上什么忙。\x02",
    )

    CloseMessageWindow()

    label("loc_210E")

    Jump("loc_2E09")

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_218E")

    #C0081
    ChrTalk(
        0xFE,
        (
            "尊贵的顾客，\x01",
            "别再犹豫了，\x01",
            "太阳快下山了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "抓住最后的机会买点吧！\x01",
            "这是今天最后一次吐血大甩卖了哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E09")

    label("loc_218E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2245")

    #C0083
    ChrTalk(
        0xFE,
        (
            "我真是从心底里尊敬\x01",
            "工商协会的老爷爷们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "因为他们\x01",
            "保护了这个\x01",
            "露天市场的传统。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "不过……我可搞不懂那些\x01",
            "复杂的事情！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "根本就不适合入会啦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_228B")

    label("loc_2245")


    #C0087
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "千万不要错过哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "……我果然还是适合\x01",
            "这样做生意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228B")

    Jump("loc_2E09")

    label("loc_2290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2311")

    #C0089
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "感谢惠顾迪因兹食材店！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "我们店今天也是老规矩，\x01",
            "从早上就要开始特价大甩卖了哦！\x01",
            "千万不要错过啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E09")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238A")

    #C0091
    ChrTalk(
        0xFE,
        (
            "混账，那帮\x01",
            "蛮横的家伙……！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "如果只是打我也就算了。\x01",
            "竟然还惊扰了顾客，真是不可原谅！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23B3")

    label("loc_238A")


    #C0093
    ChrTalk(
        0xFE,
        (
            "鲁巴彻的那帮家伙……\x01",
            "真是不可原谅！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B3")

    Jump("loc_2E09")

    label("loc_23B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_24D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2482")

    #C0094
    ChrTalk(
        0xFE,
        (
            "最近工商协会的老爷爷们\x01",
            "经常叫我过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "总觉得他们好像\x01",
            "挺喜欢我，\x01",
            "时不时就会叫我一起吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "嘿嘿，各位老爷爷\x01",
            "都是元老级的商人啊。\x01",
            "仅是听他们讲讲往事也很有趣哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_24CB")

    label("loc_2482")


    #C0097
    ChrTalk(
        0xFE,
        (
            "最近工商协会的老爷爷们\x01",
            "经常叫我一起吃饭哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "大家都很亲切热情。\x02",
    )

    CloseMessageWindow()

    label("loc_24CB")

    Jump("loc_2E09")

    label("loc_24D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_25D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256D")

    #C0099
    ChrTalk(
        0xFE,
        (
            "工商协会的会长\x01",
            "还表扬我\x01",
            "做生意有诚信哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "嘿嘿，真是开心啊。\x01",
            "我的生意终于被认同了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "而且他们还约我\x01",
            "下次一起去喝酒。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_25D3")

    label("loc_256D")


    #C0102
    ChrTalk(
        0xFE,
        (
            "工商协会的会长\x01",
            "表扬我做生意有诚信哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "嘿嘿，对我们这种小店来说，\x01",
            "没有什么比这更让人高兴了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D3")

    Jump("loc_2E09")

    label("loc_25D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_26F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A7")

    #C0104
    ChrTalk(
        0xFE,
        (
            "每年纪念庆典期间的进货\x01",
            "都比预想中要难得多。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "蔬菜最重要的就是新鲜，\x01",
            "进太多货可是大忌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "不过要是没货的话，\x01",
            "顾客就会感到很困扰了……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "真是苦恼啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_26F4")

    label("loc_26A7")


    #C0108
    ChrTalk(
        0xFE,
        (
            "每年纪念庆典期间的进货\x01",
            "都比预想中要难得多。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "哎呀哎呀，真是苦恼啊。\x02",
    )

    CloseMessageWindow()

    label("loc_26F4")

    Jump("loc_2E09")

    label("loc_26F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2762")

    #C0110
    ChrTalk(
        0xFE,
        "欢迎光临！欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "我们现在针对老顾客\x01",
            "有优惠活动哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "买得越多优惠就越多！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E09")

    label("loc_2762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_288E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283F")

    #C0113
    ChrTalk(
        0xFE,
        (
            "从阿尔摩利卡村购买的\x01",
            "货物是批发商用\x01",
            "导力卡车给我送过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "我刚开始做生意的时候，\x01",
            "好像还没有\x01",
            "那种方便的交通工具……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "不过多亏了那个，新鲜蔬菜\x01",
            "才能早点送到这里！\x01",
            "生活变得真方便啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2889")

    label("loc_283F")


    #C0116
    ChrTalk(
        0xFE,
        (
            "最近好像每家店\x01",
            "都在使用导力卡车哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "现在的生活变得\x01",
            "真是方便啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2889")

    Jump("loc_2E09")

    label("loc_288E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292A")

    #C0118
    ChrTalk(
        0xFE,
        (
            "早市的时候，\x01",
            "工商协会的会长跟我打招呼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "哎呀呀，真是害羞。\x01",
            "会长竟然还记得我。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "……好的，今天也要\x01",
            "努力加油吆喝！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_296F")

    label("loc_292A")


    #C0121
    ChrTalk(
        0xFE,
        "欢迎光临！欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "新鲜又便宜的蔬菜尽在\x01",
            "迪因兹食材店哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296F")

    Jump("loc_2E09")

    label("loc_2974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2C")

    #C0123
    ChrTalk(
        0xFE,
        (
            "欢迎光临！欢迎光临！\x01",
            "今天迪因兹食材店的生意\x01",
            "也十分红火哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "不是我自夸，\x01",
            "我们这店自开业以来\x01",
            "还从没休息过哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "因为尊贵的顾客们\x01",
            "需要我们的服务！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A6C")

    label("loc_2A2C")


    #C0126
    ChrTalk(
        0xFE,
        (
            "欢迎光临！欢迎光临！\x01",
            "迪因兹食材店\x01",
            "全年无休，每天都营业哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6C")

    Jump("loc_2E09")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3A")

    #C0127
    ChrTalk(
        0xFE,
        "欢迎光临！欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "今天早上有个活泼的\x01",
            "女孩子来了我们店，\x01",
            "跟我聊了很多哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "她有一头栗色的头发，梳着两个辫子，\x01",
            "不过以前都没见过呢。\x01",
            "不知道是不是最近才搬来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2BBD")

    label("loc_2B3A")


    #C0130
    ChrTalk(
        0xFE,
        (
            "今天早上有个活泼的\x01",
            "女孩子来了我们店，\x01",
            "连我也都被她那蓬勃的朝气感染了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "不过以前都没见过她。\x01",
            "不知道是不是最近才搬来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBD")

    Jump("loc_2E09")

    label("loc_2BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C30")

    #C0132
    ChrTalk(
        0xFE,
        "欢迎光临！欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "我们这的蔬菜\x01",
            "既便宜又新鲜哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        "绝对值得您购买！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C74")

    label("loc_2C30")


    #C0135
    ChrTalk(
        0xFE,
        (
            "我们店的新鲜蔬菜\x01",
            "价格非常低廉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "来来，\x01",
            "绝对值得您购买！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C74")

    Jump("loc_2E09")

    label("loc_2C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2E09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC2")

    #C0137
    ChrTalk(
        0xFE,
        (
            "欢迎光临！\x01",
            "欢迎光临！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "哦，这位小哥，以前没见过你们啊！\x01",
            "现在买的话有优惠，可以附赠一个哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0300F哇，蔬菜摆成这样\x01",
            "也好壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#0100F露天店上的商品，\x01",
            "不知道为什么，看着就想买。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "哦，这几位顾客，\x01",
            "这话说得真让人开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "这些蔬菜是从阿尔摩利卡村直接送过来的哦。\x01",
            "请随意挑选吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E09")

    label("loc_2DC2")


    #C0143
    ChrTalk(
        0xFE,
        (
            "我们店的蔬菜是从阿尔摩利卡村\x01",
            "直接送过来的哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "买点吧买点吧！\x02",
    )

    CloseMessageWindow()

    label("loc_2E09")

    Jump("loc_1E56")

    label("loc_2E0E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1E49 end

    def Function_12_2E12(): pass

    label("Function_12_2E12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9A")

    #C0145
    ChrTalk(
        0x101,
        (
            "#0003F（东街的市场……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_2E9A")


    #C0146
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "失物？\x01",
            "没有，我没见过哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "来市场的人这么多，\x01",
            "掉东西这种事很常见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "你们再去问问其他人吧，\x01",
            "说不定有人捡到了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2F9D")

    label("loc_2F56")


    #C0150
    ChrTalk(
        0xFE,
        (
            "要是想寻找失物的话，\x01",
            "就去问问其他人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "说不定有人捡到了哦。\x02",
    )

    CloseMessageWindow()

    label("loc_2F9D")

    Jump("loc_3C71")

    label("loc_2FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_30CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3055")

    #C0152
    ChrTalk(
        0xFE,
        (
            "迪因兹那家伙……\x01",
            "真不识时务啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "竟然那么干脆地\x01",
            "拒绝了工商协会的邀请。\x01",
            "然后在这里累死累活地开露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "真是死脑筋啊……\x01",
            "他也太老实了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_30C6")

    label("loc_3055")


    #C0155
    ChrTalk(
        0xFE,
        (
            "诚实、老实、死脑筋……\x01",
            "这家伙就算被坏人骗了，\x01",
            "肯定也都完全察觉不到。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "哎呀呀，果然还是得\x01",
            "由我来看好他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C6")

    Jump("loc_3C71")

    label("loc_30CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3194")

    #C0157
    ChrTalk(
        0xFE,
        (
            "工商协会的会长\x01",
            "正式给他发出了邀请。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "但迪因兹他\x01",
            "好像很苦恼的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "真是的……这还犹豫什么，\x01",
            "赶快接受不就好了。\x01",
            "对一个商人来说，这可是个可遇而不可求的好机会啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3214")

    label("loc_3194")


    #C0160
    ChrTalk(
        0xFE,
        (
            "要是进了工商协会，\x01",
            "就可以得到老爷爷们的资助。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "而且还能学到很多东西。\x01",
            "对一个商人来说，这可是个可遇而不可求的好机会啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3214")

    Jump("loc_3C71")

    label("loc_3219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_32FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329A")

    #C0162
    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "好像发生了什么事件啊，\x01",
            "不过我们店还是正常营业哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "您不用担心，\x01",
            "尽管放心买。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_32F8")

    label("loc_329A")


    #C0165
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "迪因兹还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "完全不关心那些传闻，\x01",
            "不，应该说是完全没有察觉到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F8")

    Jump("loc_3C71")

    label("loc_32FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_33B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3378")

    #C0167
    ChrTalk(
        0xFE,
        (
            "迪因兹昨天被那帮家伙\x01",
            "打得进了医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "真是，太让人火大了～\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "当然，我也\x01",
            "做不了什么。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_33AB")

    label("loc_3378")


    #C0170
    ChrTalk(
        0xFE,
        (
            "哼，如果我有能力的话，\x01",
            "一定要狠狠揍他们一顿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33AB")

    Jump("loc_3C71")

    label("loc_33B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_346D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344E")

    #C0171
    ChrTalk(
        0xFE,
        (
            "工商协会的老爷爷们\x01",
            "想邀请迪因兹入会。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "他做生意总是很诚信，\x01",
            "所以被认可了。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "不过迪因兹他太迟钝了……\x01",
            "完全没有察觉到。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3468")

    label("loc_344E")


    #C0174
    ChrTalk(
        0xFE,
        "呵呵，这样可不行啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3468")

    Jump("loc_3C71")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3575")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350E")

    #C0175
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "迪因兹那家伙太迟钝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "工商协会都在\x01",
            "邀请他入会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "能被工商协会的\x01",
            "老爷爷们认可，\x01",
            "这可是一件非常光荣的事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3570")

    label("loc_350E")


    #C0178
    ChrTalk(
        0xFE,
        (
            "能进入工商协会，\x01",
            "这可是一件非常光荣的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "不过他本人好像都没有察觉，\x01",
            "真拿他没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3570")

    Jump("loc_3C71")

    label("loc_3575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_35E9")

    #C0180
    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "到了纪念庆典时，\x01",
            "各处都会大减价哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "我们店也准备推出优惠活动，\x01",
            "敬请期待啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C71")

    label("loc_35E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_36C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3675")

    #C0183
    ChrTalk(
        0xFE,
        (
            "彩虹剧团有个新人\x01",
            "叫做莉夏，她最近很有名气。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "我时常……\x01",
            "会见到她哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "不知道她是不是\x01",
            "就住在这附近。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_36C3")

    label("loc_3675")


    #C0186
    ChrTalk(
        0xFE,
        (
            "莉夏小姐经常来\x01",
            "这个露天市场买东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "不知道她是不是\x01",
            "就住在这附近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C3")

    Jump("loc_3C71")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_37FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A3")

    #C0188
    ChrTalk(
        0xFE,
        (
            "我很想要一张\x01",
            "彩虹剧团的门票啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "嗯嗯，看完公演之后，\x01",
            "还要再去百货店扫荡一圈……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0190
    ChrTalk(
        0xFE,
        "……啊，怎么跟你们说起这个了！\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "欢、欢迎～\x01",
            "欢迎光临迪因兹食材店～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_37F7")

    label("loc_37A3")


    #C0192
    ChrTalk(
        0xFE,
        (
            "不好了不好了，\x01",
            "不知道是不是因为市里太热闹……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "我的购物欲望\x01",
            "都喷涌而出了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F7")

    Jump("loc_3C71")

    label("loc_37FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_389B")

    #C0194
    ChrTalk(
        0xFE,
        (
            "欢迎光临\x01",
            "迪因兹食材店！\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "这家店的店主虽然有些迟钝，\x01",
            "但确实是个诚实的老好人。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "要买蔬菜的话，就请来迪因兹食材店吧！\x01",
            "可以随意挑选哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C71")

    label("loc_389B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3928")

    #C0197
    ChrTalk(
        0xFE,
        (
            "迪因兹做起生意来\x01",
            "该说是老实还是什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "他会把卖剩的蔬菜\x01",
            "分给附近的人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "他这样不就是个老好人吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3992")

    label("loc_3928")


    #C0200
    ChrTalk(
        0xFE,
        (
            "迪因兹已经不能仅用诚实来形容了，\x01",
            "他已经老实到傻的地步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "……身为他从小的玩伴，\x01",
            "真替他担心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3992")

    Jump("loc_3C71")

    label("loc_3997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A94")

    #C0202
    ChrTalk(
        0xFE,
        (
            "东街有一个叫\x01",
            "『工商协会』的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "那个组织原本是为了\x01",
            "管理露天市场的商人而建立的。\x01",
            "但现在已经几乎成为地域性代表了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的\x01",
            "贸易和期货市场上\x01",
            "有很多投机商人……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "我们东街的开露天店的人\x01",
            "都不认可那些人哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3B2C")

    label("loc_3A94")


    #C0206
    ChrTalk(
        0xFE,
        (
            "工商协会的老爷爷们\x01",
            "都是靠露天店起家的商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "他们全部都不认可\x01",
            "那些为了赚钱不择手段的商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "工商协会可以说是将东街商人们团结在一起的组织。\x02",
    )

    CloseMessageWindow()

    label("loc_3B2C")

    Jump("loc_3C71")

    label("loc_3B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE6")

    #C0209
    ChrTalk(
        0xFE,
        (
            "迪因兹那家伙\x01",
            "的脑袋非常一根筋，\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "而且还太过老实，\x01",
            "都不懂对人多少要有点戒心。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "这样的他竟然\x01",
            "还说要做生意……\x01",
            "身为他从小的玩伴，真替他担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3C24")

    label("loc_3BE6")


    #C0212
    ChrTalk(
        0xFE,
        (
            "迪因兹的脑袋\x01",
            "太一根筋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "不过他很受\x01",
            "客人们的喜欢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C24")

    Jump("loc_3C71")

    label("loc_3C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3C71")

    #C0214
    ChrTalk(
        0xFE,
        "啊，欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "我们店的蔬菜非常新鲜哦！\x01",
            "买点回去吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C71")

    TalkEnd(0xFE)
    Return()

    # Function_12_2E12 end

    def Function_13_3C75(): pass

    label("Function_13_3C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CA2")
    TurnDirection(0x0, 0xB, 0)
    OP_4B(0xB, 0xFF)
    Call(0, 34)
    Return()

    label("loc_3CA2")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_3DAF")

    #C0216
    ChrTalk(
        0xFE,
        (
            "啊呀，你们几个。\x01",
            "似乎带着很新鲜的鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "是自己钓的吗？\x01",
            "鱼身上也没有任何伤痕……可以就这样\x01",
            "直接摆在这里出售呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "呵呵，怎么样，\x01",
            "把那些鱼卖给\x01",
            "我们店吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔产的鱼可是畅销商品哦。\x01",
            "我也会给你们些回礼的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x51, 7)
    SetScenarioFlags(0x2, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_3DAF")

    Call(0, 14)
    Jump("loc_57C3")

    label("loc_3DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_57C0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57BB")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "对话")
    MenuCmd(1, 1, "将鱼售出")
    MenuCmd(1, 1, "放弃")
    ClearScenarioFlags(0x2, 3)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E16")
    MenuCmd(3, 1, 0x1)

    label("loc_3E16")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E48")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3E48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5786")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5777")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ED2")
    MenuCmd(1, 1, "雪花蟹　　　        地 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC8")
    Call(0, 16)

    label("loc_3EC8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F27")
    MenuCmd(1, 1, "阿尔摩利卡鲫鱼　　　水 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1D")
    Call(0, 16)

    label("loc_3F1D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F7C")
    MenuCmd(1, 1, "橙河鱼　　　　　　  火 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F72")
    Call(0, 16)

    label("loc_3F72")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FD1")
    MenuCmd(1, 1, "岩穴鱼　　　　　　　风 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC7")
    Call(0, 16)

    label("loc_3FC7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4026")
    MenuCmd(1, 1, "鲤鱼　　　　　　　  时 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401C")
    Call(0, 16)

    label("loc_401C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4026")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_407B")
    MenuCmd(1, 1, "冷水鱼　　　　　　  幻 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4071")
    Call(0, 16)

    label("loc_4071")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_407B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40D0")
    MenuCmd(1, 1, "蓝带神仙鱼　　　　　地 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40C6")
    Call(0, 16)

    label("loc_40C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_40D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4125")
    MenuCmd(1, 1, "银伞鱼　　　　　　  水 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411B")
    Call(0, 16)

    label("loc_411B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4125")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_417A")
    MenuCmd(1, 1, "虹鳟鱼　　　　　    火 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4170")
    Call(0, 16)

    label("loc_4170")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_417A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41CF")
    MenuCmd(1, 1, "黑鲑　　　　　　    风 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C5")
    Call(0, 16)

    label("loc_41C5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_41CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4224")
    MenuCmd(1, 1, "鲑鱼　　　　　　    时 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_421A")
    Call(0, 16)

    label("loc_421A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4224")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4279")
    MenuCmd(1, 1, "鳗鲡　　　　　　    幻 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426F")
    Call(0, 16)

    label("loc_426F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42CE")
    MenuCmd(1, 1, "珍珠草　　　　      空 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C4")
    Call(0, 16)

    label("loc_42C4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_42CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4323")
    MenuCmd(1, 1, "大口鲈鱼　　　　    地 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4319")
    Call(0, 16)

    label("loc_4319")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4323")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4378")
    MenuCmd(1, 1, "云斑蛇头　　　      水 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436E")
    Call(0, 16)

    label("loc_436E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43CD")
    MenuCmd(1, 1, "暗纹蛇鱼　　　      火 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C3")
    Call(0, 16)

    label("loc_43C3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_43CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4422")
    MenuCmd(1, 1, "巨鲶　　　　　　    风 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4418")
    Call(0, 16)

    label("loc_4418")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4477")
    MenuCmd(1, 1, "巨血蟹　　　　      时 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_446D")
    Call(0, 16)

    label("loc_446D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4477")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44CC")
    MenuCmd(1, 1, "电鳗　　　　        幻 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C2")
    Call(0, 16)

    label("loc_44C2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_44CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4521")
    MenuCmd(1, 1, "魔鬼巨鲶　　　      时 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4517")
    Call(0, 16)

    label("loc_4517")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4521")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4576")
    MenuCmd(1, 1, "弧光蟹　　　        空 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_456C")
    Call(0, 16)

    label("loc_456C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4576")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45CC")
    MenuCmd(1, 1, "金鲑　　　          时 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C2")
    Call(0, 16)

    label("loc_45C2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4622")
    MenuCmd(1, 1, "锦鲤　　　          空 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4618")
    Call(0, 16)

    label("loc_4618")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4622")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4678")
    MenuCmd(1, 1, "霸王蛇鱼　　        幻 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466E")
    Call(0, 16)

    label("loc_466E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4678")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46B7")
    Jump("loc_5772")

    label("loc_46B7")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_473E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4734")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0220
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I地之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4734")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_473E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47A8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_479E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0221
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I水之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_479E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4812")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4808")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0222
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I火之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4808")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4812")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_487C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4872")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0223
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I风之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4872")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_487C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48E6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0224
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_48DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4950")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4946")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0225
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片10个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4946")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49BA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0226
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I地之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_49B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A24")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A1A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0227
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I水之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4A1A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A8E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A84")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0228
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I火之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4A84")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AF8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AEE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0229
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I风之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4AEE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4AF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B62")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B58")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0230
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4B58")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BCC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BC2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0231
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4BC2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C36")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C2C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0232
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I空之耀晶片20个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4C2C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CA0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C96")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0233
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#56I地之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4C96")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D0A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D00")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0234
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#57I水之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4D00")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D74")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0235
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#58I火之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4D6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DDE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0236
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#59I风之耀晶片40个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4DD4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4DDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E48")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E3E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0237
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4E3E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4EB2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0238
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4EA8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F1C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F12")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0239
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4F12")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F86")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0240
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I空之耀晶片50个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4F7C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4F86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FF1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0241
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#60I时之耀晶片100个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_4FE7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4FF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_505C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5052")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0242
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#61I空之耀晶片100个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_5052")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_505C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('金鲑', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50C7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50BD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0243
    ChrTalk(
        0xFE,
        (
            "这条鱼用\x07\x02",

            "#62I幻之耀晶片100个\x07\x00\x01",
            "来交换可以吗？\x02",
        )
    )


    label("loc_50BD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_50C7")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5772")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51B7")

    #C0244
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5768")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_527E"),
        (1, "loc_52B1"),
        (2, "loc_52E4"),
        (3, "loc_5317"),
        (4, "loc_534A"),
        (5, "loc_537D"),
        (6, "loc_53B0"),
        (7, "loc_53E3"),
        (8, "loc_5416"),
        (9, "loc_5449"),
        (10, "loc_547C"),
        (11, "loc_54AF"),
        (12, "loc_54E2"),
        (13, "loc_5515"),
        (14, "loc_5548"),
        (15, "loc_557B"),
        (16, "loc_55AE"),
        (17, "loc_55E1"),
        (18, "loc_5614"),
        (19, "loc_5647"),
        (20, "loc_567A"),
        (21, "loc_56AD"),
        (22, "loc_56E2"),
        (23, "loc_5717"),
        (SWITCH_DEFAULT, "loc_574C"),
    )


    label("loc_527E")


    #A0245
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
    Jump("loc_574C")

    label("loc_52B1")


    #A0246
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
    Jump("loc_574C")

    label("loc_52E4")


    #A0247
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
    Jump("loc_574C")

    label("loc_5317")


    #A0248
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
    Jump("loc_574C")

    label("loc_534A")


    #A0249
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
    Jump("loc_574C")

    label("loc_537D")


    #A0250
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
    Jump("loc_574C")

    label("loc_53B0")


    #A0251
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
    Jump("loc_574C")

    label("loc_53E3")


    #A0252
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
    Jump("loc_574C")

    label("loc_5416")


    #A0253
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
    Jump("loc_574C")

    label("loc_5449")


    #A0254
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
    Jump("loc_574C")

    label("loc_547C")


    #A0255
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
    Jump("loc_574C")

    label("loc_54AF")


    #A0256
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
    Jump("loc_574C")

    label("loc_54E2")


    #A0257
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
    Jump("loc_574C")

    label("loc_5515")


    #A0258
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
    Jump("loc_574C")

    label("loc_5548")


    #A0259
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
    Jump("loc_574C")

    label("loc_557B")


    #A0260
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
    Jump("loc_574C")

    label("loc_55AE")


    #A0261
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
    Jump("loc_574C")

    label("loc_55E1")


    #A0262
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
    Jump("loc_574C")

    label("loc_5614")


    #A0263
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
    Jump("loc_574C")

    label("loc_5647")


    #A0264
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
    Jump("loc_574C")

    label("loc_567A")


    #A0265
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
    Jump("loc_574C")

    label("loc_56AD")


    #A0266
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
    Jump("loc_574C")

    label("loc_56E2")


    #A0267
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
    Jump("loc_574C")

    label("loc_5717")


    #A0268
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
    Jump("loc_574C")

    label("loc_574C")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5772")

    label("loc_5768")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5772")

    Jump("loc_3E61")

    label("loc_5777")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B6")

    label("loc_5786")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_579A")
    Jump("loc_57B6")

    label("loc_579A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_57B6")

    Jump("loc_3DCA")

    label("loc_57BB")

    Jump("loc_57C3")

    label("loc_57C0")

    Call(0, 14)

    label("loc_57C3")

    TalkEnd(0xB)
    Return()

    # Function_13_3C75 end

    def Function_14_57C7(): pass

    label("Function_14_57C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_5869")

    #C0269
    ChrTalk(
        0xB,
        (
            "虽然克洛斯贝尔产的鱼很好卖，\x01",
            "但很少有货。\x01",
            "总是脱销。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xB,
        (
            "你们的鱼\x01",
            "看起来都不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "如果愿意的话，能卖给我们店吗？\x01",
            "我也会给你们些回礼的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6649")

    label("loc_5869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_5913")

    #C0272
    ChrTalk(
        0xB,
        (
            "警察居然会直接来领取失物，\x01",
            "这可是很少见的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xB,
        (
            "算了，就拜托你们\x01",
            "帮我把这个交给那孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#0000F嗯，请放心交给我们。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x102,
        "#0100F多谢您的协助。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6649")

    label("loc_5913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_59EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B0")

    #C0276
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔时代周刊社的人\x01",
            "从早上开始就到处转悠。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        "游击士协会的人好像也都很慌张……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xB,
        (
            "他们都在做什么呢？\x01",
            "真让人好奇啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_59E7")

    label("loc_59B0")


    #C0279
    ChrTalk(
        0xB,
        (
            "今天街上的气氛好像有点慌乱啊，\x01",
            "大家都在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E7")

    Jump("loc_6649")

    label("loc_59EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5ABD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A89")

    #C0280
    ChrTalk(
        0xB,
        (
            "今天早上，旧城区的不良少年\x01",
            "一脸担心地跑来找我，\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xB,
        "问我有没有见过他们的同伴……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "我可没见过哦……\x01",
            "不过应该是内讧了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5AB8")

    label("loc_5A89")


    #C0283
    ChrTalk(
        0xB,
        (
            "旧城区的那些不良少年，\x01",
            "好像经常会闹内讧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AB8")

    Jump("loc_6649")

    label("loc_5ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B60")

    #C0284
    ChrTalk(
        0xB,
        "我听说好像发生了什么事件……\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "但只因为这点小事，\x01",
            "可没法让我关店。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xB,
        (
            "从前的克洛斯贝尔商人，\x01",
            "就算在战争中也会照常做生意的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5BBC")

    label("loc_5B60")


    #C0287
    ChrTalk(
        0xB,
        (
            "我虽然只是个小角色，但至少也算是一名\x01",
            "克洛斯贝尔商人。不管发生什么事，\x01",
            "我都不会关店的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BBC")

    Jump("loc_6649")

    label("loc_5BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C86")

    #C0288
    ChrTalk(
        0xB,
        (
            "说起鲁巴彻的\x01",
            "那帮家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "最近，好像有个来自共和国的\x01",
            "黑手党组织到了克洛斯贝尔，\x01",
            "不过那些人看上去还算比较正派吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "但是……对于黑手党，\x01",
            "也没什么好坏之说啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5CD2")

    label("loc_5C86")


    #C0291
    ChrTalk(
        0xB,
        (
            "话说回来，最近危险的事件\x01",
            "好像增加了不少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "你们也得\x01",
            "多加注意哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CD2")

    Jump("loc_6649")

    label("loc_5CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5D68")

    #C0293
    ChrTalk(
        0xB,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xB,
        (
            "虽然纪念庆典结束了，\x01",
            "但还有很多\x01",
            "观光游客滞留在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "庆典都快过去一个星期了，\x01",
            "不过生意还是很不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6649")

    label("loc_5D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E12")

    #C0296
    ChrTalk(
        0xFE,
        (
            "通往共和国的道路\x01",
            "好像终于恢复通行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "只是一起卡车事故而已，\x01",
            "居然花了这么多时间处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "……算了，只要订购的鱼\x01",
            "能准时送到就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5E68")

    label("loc_5E12")


    #C0299
    ChrTalk(
        0xFE,
        (
            "最近好像发生了不少\x01",
            "奇怪的事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "……算了，只要订购的鱼\x01",
            "能准时送到就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E68")

    Jump("loc_6649")

    label("loc_5E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F15")

    #C0301
    ChrTalk(
        0xFE,
        "您好，欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "我只能暂时从钓公师团\x01",
            "那里买鱼了，\x01",
            "他们的鱼也算是新鲜啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "虽然送货卡车迟到很让人头痛，\x01",
            "但也一定得想办法撑住。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5F63")

    label("loc_5F15")


    #C0304
    ChrTalk(
        0xFE,
        (
            "因为上次的卡车事故，\x01",
            "货运经常会被耽搁。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "必须想个办法\x01",
            "渡过这个难关。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F63")

    Jump("loc_6649")

    label("loc_5F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5FFD")

    #C0306
    ChrTalk(
        0xFE,
        (
            "不好意思，今天\x01",
            "鱼比较少。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "好像是共和国那边出了一起卡车事故，\x01",
            "所以道路还没有恢复通行。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "送货的卡车\x01",
            "基本上也都暂时停运了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6649")

    label("loc_5FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6096")

    #C0309
    ChrTalk(
        0xFE,
        (
            "最近，共和国那边\x01",
            "好像频繁发生卡车事故啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "因此导致道路堵塞，\x01",
            "我订购的鱼也都没能准时送到。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "唉，真是让人苦恼啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6100")

    label("loc_6096")


    #C0312
    ChrTalk(
        0xFE,
        (
            "最近，共和国那边\x01",
            "的卡车事故似乎明显增加了。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "仅上个星期就连续发生了好几起。\x01",
            "……到底是怎么了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6100")

    SetScenarioFlags(0x95, 1)
    Jump("loc_6649")

    label("loc_6108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_61EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61AC")

    #C0314
    ChrTalk(
        0xB,
        (
            "老板总是忙着去进货，\x01",
            "很少能见到他……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "……啊，抱歉，\x01",
            "跟你们说了些不愉快的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "来，买条鱼吧～？\x01",
            "保证绝对条条新鲜美味～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_61E9")

    label("loc_61AC")


    #C0317
    ChrTalk(
        0xB,
        (
            "老板总是忙着去进货，\x01",
            "很少能见到他……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        "有点寂寞啊。\x02",
    )

    CloseMessageWindow()

    label("loc_61E9")

    Jump("loc_6649")

    label("loc_61EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_62E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_628F")

    #C0319
    ChrTalk(
        0xB,
        (
            "那条路上有个叫做\x01",
            "钓公师团的组织，你们知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xB,
        (
            "那里的人每次经过这里的时候，\x01",
            "总是盯着我们店的鱼看。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        "不知道他们想干什么。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62DD")

    label("loc_628F")


    #C0322
    ChrTalk(
        0xB,
        (
            "钓公师团的那些人，\x01",
            "总是一脸严肃地看着我们店的鱼。\x01",
            "真不知道他们想干什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62DD")

    Jump("loc_6649")

    label("loc_62E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_64C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6467")

    #C0323
    ChrTalk(
        0xB,
        (
            "最近都没怎么见到那些\x01",
            "穿红色衣服的不良少年们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        (
            "虽然很开心没有他们在\x01",
            "店门前吵闹……但太安静了，\x01",
            "反而开始有点担心了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xB,
        (
            "不知道他们是不是都\x01",
            "食物中毒了啊。\x02",
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
    Sleep(500)

    #C0326
    ChrTalk(
        0x104,
        (
            "#0300F（下次那帮家伙再捣乱的话，\x01",
            "  就让他们全部食物中毒吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        "#0006F（这个有点……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_64C1")

    label("loc_6467")


    #C0328
    ChrTalk(
        0xB,
        (
            "最近都没怎么见到那些\x01",
            "穿红色衣服的不良少年们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xB,
        (
            "不知道他们是不是都\x01",
            "食物中毒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C1")

    Jump("loc_6649")

    label("loc_64C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6539")

    #C0330
    ChrTalk(
        0xB,
        (
            "最近送货卡车\x01",
            "的班次增加了，\x01",
            "进货也轻松多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xB,
        (
            "来来，买条鱼吧？\x01",
            "这些都是早上刚钓起来的哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6649")

    label("loc_6539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6614")

    #C0332
    ChrTalk(
        0xB,
        (
            "买条鱼吧～！\x01",
            "新鲜的鱼哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        "#0200F……有很多鱼呢。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#0003F嗯，这些鱼全都\x01",
            "没见过啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xB,
        (
            "呵呵，那些是从共和国进的\x01",
            "盐渍海鱼哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xB,
        (
            "不管是烧还是蒸都很好吃。\x01",
            "怎么样，买一条吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6649")

    label("loc_6614")


    #C0337
    ChrTalk(
        0xB,
        "买条鱼吧～！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "刚刚送到的，\x01",
            "还都很新鲜哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6649")

    Return()

    # Function_14_57C7 end

    def Function_15_664A(): pass

    label("Function_15_664A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6658")
    SetScenarioFlags(0x2, 3)

    label("loc_6658")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('雪花蟹', 0x0)"), scpexpr(EXPR_END)), "loc_6666")
    SetScenarioFlags(0x2, 3)

    label("loc_6666")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('蓝带神仙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6674")
    SetScenarioFlags(0x2, 3)

    label("loc_6674")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('银伞鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6682")
    SetScenarioFlags(0x2, 3)

    label("loc_6682")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('阿尔摩利卡鲫鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6690")
    SetScenarioFlags(0x2, 3)

    label("loc_6690")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('乌龟', 0x0)"), scpexpr(EXPR_END)), "loc_669E")
    SetScenarioFlags(0x2, 3)

    label("loc_669E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('橙河鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66AC")
    SetScenarioFlags(0x2, 3)

    label("loc_66AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('岩穴鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66BA")
    SetScenarioFlags(0x2, 3)

    label("loc_66BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('虹鳟鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66C8")
    SetScenarioFlags(0x2, 3)

    label("loc_66C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('食人鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66D6")
    SetScenarioFlags(0x2, 3)

    label("loc_66D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲤鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66E4")
    SetScenarioFlags(0x2, 3)

    label("loc_66E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('大口鲈鱼', 0x0)"), scpexpr(EXPR_END)), "loc_66F2")
    SetScenarioFlags(0x2, 3)

    label("loc_66F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑鲑', 0x0)"), scpexpr(EXPR_END)), "loc_6700")
    SetScenarioFlags(0x2, 3)

    label("loc_6700")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('角斗鱼', 0x0)"), scpexpr(EXPR_END)), "loc_670E")
    SetScenarioFlags(0x2, 3)

    label("loc_670E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('冷水鱼', 0x0)"), scpexpr(EXPR_END)), "loc_671C")
    SetScenarioFlags(0x2, 3)

    label("loc_671C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('小鲵', 0x0)"), scpexpr(EXPR_END)), "loc_672A")
    SetScenarioFlags(0x2, 3)

    label("loc_672A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鲑鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6738")
    SetScenarioFlags(0x2, 3)

    label("loc_6738")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_6746")
    SetScenarioFlags(0x2, 3)

    label("loc_6746")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('鳗鲡', 0x0)"), scpexpr(EXPR_END)), "loc_6754")
    SetScenarioFlags(0x2, 3)

    label("loc_6754")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢壳龟', 0x0)"), scpexpr(EXPR_END)), "loc_6762")
    SetScenarioFlags(0x2, 3)

    label("loc_6762")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨血蟹', 0x0)"), scpexpr(EXPR_END)), "loc_6770")
    SetScenarioFlags(0x2, 3)

    label("loc_6770")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('珍珠龙鱼', 0x0)"), scpexpr(EXPR_END)), "loc_677E")
    SetScenarioFlags(0x2, 3)

    label("loc_677E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('巨鲶', 0x0)"), scpexpr(EXPR_END)), "loc_678C")
    SetScenarioFlags(0x2, 3)

    label("loc_678C")

    Return()

    # Function_15_664A end

    def Function_16_678D(): pass

    label("Function_16_678D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A0")
    MenuCmd(3, 1, 0x0)

    label("loc_67A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B3")
    MenuCmd(3, 1, 0x1)

    label("loc_67B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C6")
    MenuCmd(3, 1, 0x2)

    label("loc_67C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67D9")
    MenuCmd(3, 1, 0x3)

    label("loc_67D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67EC")
    MenuCmd(3, 1, 0x4)

    label("loc_67EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67FF")
    MenuCmd(3, 1, 0x5)

    label("loc_67FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6812")
    MenuCmd(3, 1, 0x6)

    label("loc_6812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6825")
    MenuCmd(3, 1, 0x7)

    label("loc_6825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6838")
    MenuCmd(3, 1, 0x8)

    label("loc_6838")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_684B")
    MenuCmd(3, 1, 0x9)

    label("loc_684B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_685E")
    MenuCmd(3, 1, 0xA)

    label("loc_685E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6871")
    MenuCmd(3, 1, 0xB)

    label("loc_6871")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6884")
    MenuCmd(3, 1, 0xC)

    label("loc_6884")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6897")
    MenuCmd(3, 1, 0xD)

    label("loc_6897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68AA")
    MenuCmd(3, 1, 0xE)

    label("loc_68AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68BD")
    MenuCmd(3, 1, 0xF)

    label("loc_68BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68D0")
    MenuCmd(3, 1, 0x10)

    label("loc_68D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68E3")
    MenuCmd(3, 1, 0x11)

    label("loc_68E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68F6")
    MenuCmd(3, 1, 0x12)

    label("loc_68F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6909")
    MenuCmd(3, 1, 0x13)

    label("loc_6909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691C")
    MenuCmd(3, 1, 0x14)

    label("loc_691C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692F")
    MenuCmd(3, 1, 0x15)

    label("loc_692F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6942")
    MenuCmd(3, 1, 0x16)

    label("loc_6942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6955")
    MenuCmd(3, 1, 0x17)

    label("loc_6955")

    Return()

    # Function_16_678D end

    def Function_17_6956(): pass

    label("Function_17_6956")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B3")

    #C0339
    ChrTalk(
        0xFE,
        "哎呀，都这个时间啦。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "必须快点买完东西，\x01",
            "赶紧回家去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6A05")

    label("loc_69B3")


    #C0341
    ChrTalk(
        0xFE,
        (
            "现在这个时间，\x01",
            "应该刚好能赶上打折甩卖。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "必须快点买完东西，\x01",
            "赶紧回家去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A05")

    Jump("loc_7529")

    label("loc_6A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6A93")

    #C0343
    ChrTalk(
        0xFE,
        (
            "今天巴士要检修，\x01",
            "所以开往阿尔摩利卡的巴士\x01",
            "从中午开始就要停止运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "如果有事要去阿尔摩利卡村，\x01",
            "还是早点比较好哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7529")

    label("loc_6A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B10")

    #C0345
    ChrTalk(
        0xFE,
        (
            "工商协会的会长，\x01",
            "好像被议会的人叫去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "加油啊～我们的代表～！\x01",
            "一定要多争取一些预算～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B70")

    label("loc_6B10")


    #C0347
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔工商协会的会长\x01",
            "算是这条东街的代表哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "现在好像在整合市内的\x01",
            "所有工商业组织。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B70")

    Jump("loc_7529")

    label("loc_6B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C22")

    #C0349
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊上报道说，\x01",
            "一年后的经济将会更加景气。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "经济要是更景气的话，\x01",
            "那我丈夫的工资也就会上涨。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "我就可以买些名牌衣服了吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6C7C")

    label("loc_6C22")


    #C0352
    ChrTalk(
        0xFE,
        (
            "没有什么事能比\x01",
            "涨工资更让人高兴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "丈夫涨工资的话，\x01",
            "我就可以买些名牌衣服了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C7C")

    Jump("loc_7529")

    label("loc_6C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6D78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D13")

    #C0354
    ChrTalk(
        0xFE,
        (
            "纪念庆典结束后，\x01",
            "街道也重新安静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "那些黑手党\x01",
            "好像也收敛了很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "最近都没有什么\x01",
            "关于他们的消息。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6D73")

    label("loc_6D13")


    #C0357
    ChrTalk(
        0xFE,
        (
            "最近都没怎么听到\x01",
            "关于鲁巴彻的消息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "他们好像收敛了很多呢，\x01",
            "总算可以让人暂时放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D73")

    Jump("loc_7529")

    label("loc_6D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6DD9")

    #C0359
    ChrTalk(
        0xFE,
        (
            "每年创立纪念庆典期间，\x01",
            "工商协会都会举行一些活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        "不知道今年是什么活动。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7529")

    label("loc_6DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6E54")

    #C0361
    ChrTalk(
        0xFE,
        "下个月终于就是创立纪念庆典了。\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "难得的庆典，果然还是想痛快地玩一场，\x01",
            "所以从现在开始必须得省点钱了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7529")

    label("loc_6E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F12")

    #C0363
    ChrTalk(
        0xFE,
        (
            "七八年前左右，\x01",
            "曾经发生过一起\x01",
            "黑手党间的斗争事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "那个时候好像有传闻，\x01",
            "说那起事件就是\x01",
            "鲁巴彻的内讧。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "哼，警察什么措施也不采取，\x01",
            "真让人感到害怕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6F6E")

    label("loc_6F12")


    #C0366
    ChrTalk(
        0xFE,
        (
            "最近在仓库街附近\x01",
            "好像也发生枪击事件了……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "是不是他们又开始内讧了呢。\x01",
            "真是可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F6E")

    Jump("loc_7529")

    label("loc_6F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_70C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7042")

    #C0368
    ChrTalk(
        0xFE,
        (
            "……你们听说了吗？\x01",
            "昨晚在仓库街那边\x01",
            "好像发生了一起枪击事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "虽然游击士急忙赶过去了，\x01",
            "但那些犯人好像早就逃走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "真是的……不管到什么时候，\x01",
            "都不能实现真正的和平啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_70C1")

    label("loc_7042")


    #C0371
    ChrTalk(
        0xFE,
        (
            "在仓库街附近\x01",
            "好像发生了一起枪击事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "不会又是那些人做的吧……\x01",
            "……这座城市不管到什么时候，\x01",
            "都不能实现真正的和平啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C1")

    SetScenarioFlags(0x95, 1)
    Jump("loc_7529")

    label("loc_70C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_71C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7186")

    #C0373
    ChrTalk(
        0xFE,
        (
            "我在克洛斯贝尔时代周刊上\x01",
            "看到了报道……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "从索妮亚这个名字上看，\x01",
            "警备队的副司令好像\x01",
            "是名女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "我经常能看见警备队的车，\x01",
            "所以对她产生了一些亲近感呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_71C4")

    label("loc_7186")


    #C0376
    ChrTalk(
        0xFE,
        (
            "警备队副司令，\x01",
            "好像是名女性。\x01",
            "我对她产生了一些亲近感呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71C4")

    Jump("loc_7529")

    label("loc_71C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_72D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7286")

    #C0377
    ChrTalk(
        0xFE,
        (
            "住在东街的话，\x01",
            "就不愁买不到东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "走几步就有很多露天店，\x01",
            "如果需要什么特别的东西，\x01",
            "去拜托熟识的商人进货就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "这一带大概是\x01",
            "生活最便利的地区了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_72D2")

    label("loc_7286")


    #C0380
    ChrTalk(
        0xFE,
        (
            "住在东街的话，\x01",
            "就不愁买不到东西哦。\x01",
            "所以这里大概是生活最便利的地区了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72D2")

    Jump("loc_7529")

    label("loc_72D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_73C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7360")

    #C0381
    ChrTalk(
        0xFE,
        "啊，你们要去阿尔摩利卡村吗？\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "只要从那边的\x01",
            "东出口出去就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "如果坐巴士的话，\x01",
            "很快就能到了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_73BC")

    label("loc_7360")


    #C0384
    ChrTalk(
        0xFE,
        (
            "穿过那边的东出口，\x01",
            "就能看到一个巴士站。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "如果坐巴士，\x01",
            "一眨眼就能到阿尔摩利卡村哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BC")

    Jump("loc_7529")

    label("loc_73C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_741D")

    #C0386
    ChrTalk(
        0xFE,
        (
            "旧城区那边\x01",
            "好像又有骚乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "那群不良少年真是……\x01",
            "警察就不能管管吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7529")

    label("loc_741D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74C7")

    #C0388
    ChrTalk(
        0xFE,
        "啊，你们是游客吗？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "要小心哦，\x01",
            "这边离旧城区很近，\x01",
            "治安不是很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "如果遇到了什么困难，就去向游击士协会求助吧。\x01",
            "肯定能得到帮助的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7529")

    label("loc_74C7")


    #C0391
    ChrTalk(
        0xFE,
        (
            "这附近\x01",
            "治安不是很好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "如果遇到了什么困难，就去向游击士协会求助吧。\x01",
            "肯定能得到帮助的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7529")

    TalkEnd(0xFE)
    Return()

    # Function_17_6956 end

    def Function_18_752D(): pass

    label("Function_18_752D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7600")

    #C0393
    ChrTalk(
        0xFE,
        (
            "鲁巴彻的会长至今为止\x01",
            "一次也没被拘捕过，\x01",
            "是个非常狡猾的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "如果要对他量刑，\x01",
            "估计最少也得判个两百年吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "他迄今为止还从没被逮捕过，\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        "这个世界真是什么事都有……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7674")

    label("loc_7600")


    #C0397
    ChrTalk(
        0xFE,
        (
            "鲁巴彻的会长要是被逮捕，\x01",
            "估计最少也得被判个两百年吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "但警察至今仍没法逮捕他……\x01",
            "这就是如今的世道啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7674")

    Jump("loc_84A0")

    label("loc_7679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76ED")

    #C0399
    ChrTalk(
        0xFE,
        (
            "从今天早上开始，国际定期飞行船\x01",
            "好像都停止运营了。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        "真是……到底发生什么事了呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7711")

    label("loc_76ED")


    #C0401
    ChrTalk(
        0xFE,
        "最近发生了好多让人不解的事件。\x02",
    )

    CloseMessageWindow()

    label("loc_7711")

    Jump("loc_84A0")

    label("loc_7716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_77FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C7")

    #C0402
    ChrTalk(
        0xFE,
        (
            "听说昨晚\x01",
            "有一辆黑色的导力车\x01",
            "冲进了港湾公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "这么一说的话，我在半夜里\x01",
            "确实听到过好几声枪响呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "哼，应该还是\x01",
            "鲁巴彻的那帮家伙干的吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_77F6")

    label("loc_77C7")


    #C0405
    ChrTalk(
        0xFE,
        (
            "又是鲁巴彻那帮家伙干的吗……\x01",
            "真是可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F6")

    Jump("loc_84A0")

    label("loc_77FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78F9")

    #C0406
    ChrTalk(
        0xFE,
        "真是，鲁巴彻的家伙们……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "前些天，那帮家伙开着一辆\x01",
            "导力搬运车闯进了露天市场。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "刚一占领那片地方，\x01",
            "他们就态度傲慢地\x01",
            "要求收取保护费。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(1000)

    #C0409
    ChrTalk(
        0xFE,
        (
            "虽然很快就被游击士赶跑了，\x01",
            "不过还是让人很气愤啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_795F")

    label("loc_78F9")


    #C0410
    ChrTalk(
        0xFE,
        (
            "鲁巴彻那帮家伙……\x01",
            "竟然这样任意践踏我们这些商人\x01",
            "世世代代守护的露天市场……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        "真是让人气愤啊。\x02",
    )

    CloseMessageWindow()

    label("loc_795F")

    Jump("loc_84A0")

    label("loc_7964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A17")

    #C0412
    ChrTalk(
        0xFE,
        (
            "纪念庆典开始之后，\x01",
            "应该会有很多观光游客\x01",
            "滞留在克洛斯贝尔吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "有很多人已经\x01",
            "瞄准了这个大好商机。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "呵呵，看来这条街上\x01",
            "又要涌现很多新商人了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7A6F")

    label("loc_7A17")


    #C0415
    ChrTalk(
        0xFE,
        (
            "商人们的聚集之处，\x01",
            "这就是东街。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "呵呵，作为他们的前辈，\x01",
            "我要亲切地欢迎他们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A6F")

    Jump("loc_84A0")

    label("loc_7A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B32")

    #C0417
    ChrTalk(
        0xFE,
        (
            "我听说库罗伊斯总裁\x01",
            "有个非常优秀的千金。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "年纪轻轻就当上了\x01",
            "ＩＢＣ集团的董事之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "呵呵，简直跟她父亲\x01",
            "年轻时一模一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        "不，或许她还要更加优秀哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7B88")

    label("loc_7B32")


    #C0421
    ChrTalk(
        0xFE,
        (
            "库罗伊斯父女\x01",
            "都非常优秀。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "虽然她现在已经很有成就了，\x01",
            "但未来更是不可限量啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B88")

    Jump("loc_84A0")

    label("loc_7B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C76")

    #C0423
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的库罗伊斯总裁\x01",
            "年轻时就历任要职，\x01",
            "是一个很有能力的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "他当时就有着\x01",
            "超群的商业嗅觉，\x01",
            "如今更是已经成为财经界的领袖人物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "而且，\x01",
            "他的成功并不令人生厌……\x01",
            "这都要归功于他高尚的品德啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7CED")

    label("loc_7C76")


    #C0426
    ChrTalk(
        0xFE,
        (
            "ＩＢＣ的库罗伊斯总裁\x01",
            "是一个很有能力的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "而且，其品德也十分高尚哦。\x01",
            "我们这些商人中，\x01",
            "有不少人都很尊敬他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CED")

    Jump("loc_84A0")

    label("loc_7CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DEA")

    #C0428
    ChrTalk(
        0xFE,
        (
            "最近，经常听到有暴力事件发生\x01",
            "之类的危险传闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "不过警察的调查\x01",
            "还是一点成果也没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "哎呀，一如既往地没用啊……\x01",
            "万一发生什么事件，\x01",
            "果然还是游击士协会最可靠。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0006F（唔唔，这话听着果然\x01",
            "  很刺耳啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7E3B")

    label("loc_7DEA")


    #C0432
    ChrTalk(
        0xFE,
        "警察的调查总是很不可靠。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "万一发生什么事件，\x01",
            "果然还是游击士协会最可靠。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E3B")

    Jump("loc_84A0")

    label("loc_7E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF2")

    #C0434
    ChrTalk(
        0xFE,
        (
            "每年创立纪念庆典期间，\x01",
            "克洛斯贝尔工商协会\x01",
            "都会举行一些活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "听说今年他们准备举办一些\x01",
            "能让市民们也一起参加的活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        "呵呵，真是期待啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7F3C")

    label("loc_7EF2")


    #C0437
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔工商协会\x01",
            "在创立纪念庆典期间会举办活动哦，\x01",
            "真是让人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3C")

    Jump("loc_84A0")

    label("loc_7F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FD7")

    #C0438
    ChrTalk(
        0xFE,
        (
            "我在东街开店\x01",
            "有很长时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "一直承蒙\x01",
            "工商协会会长的照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "呵呵，以前和他培养出的感情\x01",
            "可以说是宝贵的财富啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8044")

    label("loc_7FD7")


    #C0441
    ChrTalk(
        0xFE,
        (
            "工商协会的会长\x01",
            "直到如今也仍然会\x01",
            "时常去露天市场看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "呵呵，应该是在关心\x01",
            "那些年轻商人的生意状况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8044")

    Jump("loc_84A0")

    label("loc_8049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8175")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8116")

    #C0443
    ChrTalk(
        0xFE,
        (
            "最近三四年里，\x01",
            "导力车得到了广泛普及。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "从共和国订的货好像\x01",
            "也开始使用导力卡车运送了。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        (
            "卡车运送的确\x01",
            "比导力列车运送要更有效率。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "……你们也要\x01",
            "多关注关注导力车啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8170")

    label("loc_8116")


    #C0447
    ChrTalk(
        0xFE,
        (
            "最近使用导力卡车的\x01",
            "商人越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "这和我开始从商那时比起来，\x01",
            "真是天差地别啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8170")

    Jump("loc_84A0")

    label("loc_8175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_82C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_825D")

    #C0449
    ChrTalk(
        0xFE,
        "克洛斯贝尔从很早以前就是个贸易都市了。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "延伸东西方向的街道\x01",
            "是条重要的贸易纽带。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "国外各种各样的农作物和\x01",
            "纺织品，还有人们众口相传的各种消息……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "可以说是那些东西\x01",
            "构筑了克洛斯贝尔这个城市。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_82BB")

    label("loc_825D")


    #C0453
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔从中世纪开始\x01",
            "就是一个发达的贸易都市。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "现在还被称为\x01",
            "『文明的十字路口』哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82BB")

    Jump("loc_84A0")

    label("loc_82C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_838B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_833D")

    #C0455
    ChrTalk(
        0xFE,
        (
            "刚才，那个女记者\x01",
            "从这里经过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        "那个记者工作很努力啊……\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "常常可以\x01",
            "在这附近看到她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8386")

    label("loc_833D")


    #C0458
    ChrTalk(
        0xFE,
        (
            "那个记者\x01",
            "经常来这里采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "最近好像在\x01",
            "很热心地\x01",
            "追着游击士跑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8386")

    Jump("loc_84A0")

    label("loc_838B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_84A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8440")

    #C0460
    ChrTalk(
        0xFE,
        (
            "哦，你们看上去很面生啊。\x01",
            "是第一次来东街吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "这附近商业很繁荣，\x01",
            "也有很多国外的移民呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "呵呵，这里从很早以前开始\x01",
            "就有着热情好客\x01",
            "的好风气哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_84A0")

    label("loc_8440")


    #C0463
    ChrTalk(
        0xFE,
        (
            "虽然东街会有点嘈杂，\x01",
            "但这里的人心地都很善良。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "一开始也许会有点不习惯，\x01",
            "但也不必害怕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84A0")

    TalkEnd(0xFE)
    Return()

    # Function_18_752D end

    def Function_19_84A4(): pass

    label("Function_19_84A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_85DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859F")
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0465
    ChrTalk(
        0xE,
        (
            "我说，梅琳……\x01",
            "我到底该怎么做啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x10,
        (
            "哥哥只要像以前一样就好呀，\x01",
            "梅琳只想让哥哥陪我玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xE,
        (
            "啊哈哈哈哈……\x01",
            "这样啊，也是哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xE,
        (
            "好，今天就\x01",
            "手牵手回家吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0469
    ChrTalk(
        0x10,
        "好！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0xEE, 0)
    Jump("loc_85DA")

    label("loc_859F")


    #C0470
    ChrTalk(
        0xFE,
        "我还是去找找工作吧。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xFE,
        (
            "每天无所事事，\x01",
            "也挺无聊的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85DA")

    Jump("loc_9017")

    label("loc_85DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_869D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8667")

    #C0472
    ChrTalk(
        0xFE,
        (
            "刚才我看到亚里欧斯先生\x01",
            "从协会出去了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        (
            "其他游击士\x01",
            "好像也都很忙……\x01",
            "看来游击士这个职业也很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8698")

    label("loc_8667")


    #C0474
    ChrTalk(
        0xFE,
        (
            "啊……只有我这么\x01",
            "无所事事的……不要紧吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8698")

    Jump("loc_9017")

    label("loc_869D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8723")

    #C0475
    ChrTalk(
        0xFE,
        (
            "今天早上爷爷路过这里，\x01",
            "他嘱咐我要\x01",
            "看好梅琳。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        (
            "嗯，好像是因为又发生了什么事件呢，\x01",
            "我也得小心点了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_877D")

    label("loc_8723")


    #C0477
    ChrTalk(
        0xFE,
        (
            "爷爷好像去了\x01",
            "克洛斯贝尔议事厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        (
            "应该是受邀去参加会议吧，\x01",
            "听说那边也忙碌不堪呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_877D")

    Jump("loc_9017")

    label("loc_8782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8801")

    #C0479
    ChrTalk(
        0xFE,
        (
            "我在纪念庆典的时候\x01",
            "打工了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "我果然\x01",
            "还是找个工作比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_885D")

    label("loc_8801")


    #C0482
    ChrTalk(
        0xFE,
        (
            "现在太闲了，\x01",
            "而且工作的感觉也不坏……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "啊啊～但这样的话，\x01",
            "总觉得自己好像很没个性～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_885D")

    Jump("loc_9017")

    label("loc_8862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_891B")

    #C0484
    ChrTalk(
        0xFE,
        (
            "可恶，纪念庆典之后，\x01",
            "我被拖去帮忙收拾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        (
            "而且那些工商协会的人\x01",
            "还一直表扬我，\x01",
            "说我不愧是会长的孙子，果然很有才能……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "唉……最后还给\x01",
            "了我工钱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8942")

    label("loc_891B")


    #C0487
    ChrTalk(
        0xFE,
        (
            "唉，可我对做生意\x01",
            "一点兴趣都没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8942")

    Jump("loc_9017")

    label("loc_8947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89DA")

    #C0488
    ChrTalk(
        0xFE,
        (
            "刚、刚才老爸\x01",
            "从那条路走过去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        (
            "应该是\x01",
            "有事要去爷爷家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "危险危险……\x01",
            "如果被他发现，\x01",
            "就又会被说教了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8A24")

    label("loc_89DA")


    #C0491
    ChrTalk(
        0xFE,
        (
            "老爸总是喋喋不休地\x01",
            "叫我去工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "如果被他发现，\x01",
            "就又会被说教了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A24")

    Jump("loc_9017")

    label("loc_8A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AD0")

    #C0493
    ChrTalk(
        0xFE,
        (
            "管教梅琳的计划\x01",
            "以失败告终。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        "唉，这种娇气的孩子真让人头痛啊。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xFE,
        (
            "不过她竟然会哭成那样子……\x01",
            "果然是我做得太过分了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_8B2F")

    label("loc_8AD0")


    #C0496
    ChrTalk(
        0xFE,
        (
            "那个……是哥哥错了，\x01",
            "哥哥不该把你丢下，\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        (
            "今天你想吃什么\x01",
            "哥哥都请你，\x01",
            "所以别不开心啦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B2F")

    Jump("loc_9017")

    label("loc_8B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BD3")

    #C0498
    ChrTalk(
        0xFE,
        (
            "我想管教下\x01",
            "梅琳那家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "因为她每天都会粘着\x01",
            "我或者老妈撒娇……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        (
            "明年她就得去主日学校上学了，\x01",
            "所以必须让她\x01",
            "学着坚强点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8C4A")

    label("loc_8BD3")


    #C0501
    ChrTalk(
        0xFE,
        (
            "虽然整天无所事事的我也\x01",
            "没好到哪里去……\x01",
            "但她总是那样的话，以后会吃苦头的。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        (
            "作为哥哥，\x01",
            "我必须得管教管教她……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C4A")

    Jump("loc_9017")

    label("loc_8C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CD1")

    #C0503
    ChrTalk(
        0xFE,
        (
            "……梅琳有点\x01",
            "太娇气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xFE,
        (
            "明年她就得去主日学校上学了，\x01",
            "不让她学着坚强点的话，\x01",
            "以后会吃苦头的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8D18")

    label("loc_8CD1")


    #C0505
    ChrTalk(
        0xFE,
        "梅琳太娇气了。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "不让她学着坚强点的话，\x01",
            "她以后一定会吃苦头的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D18")

    Jump("loc_9017")

    label("loc_8D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8E14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DB7")

    #C0507
    ChrTalk(
        0xFE,
        (
            "老爸和老妈一直叫我找工作，\x01",
            "真是烦死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "好歹也\x01",
            "让我再稍微自由一段时间嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        (
            "我要是想工作的话，\x01",
            "一定会好好工作的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8E0F")

    label("loc_8DB7")


    #C0510
    ChrTalk(
        0xFE,
        (
            "老爸和老妈都太烦人了，\x01",
            "在家里简直待不下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "好歹也\x01",
            "让我再稍微自由一段时间嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0F")

    Jump("loc_9017")

    label("loc_8E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8E54")

    #C0512
    ChrTalk(
        0xFE,
        "啊～肚子好饿啊。\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xFE,
        "今天去龙老饭店吃饭吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9017")

    label("loc_8E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EEE")

    #C0514
    ChrTalk(
        0xFE,
        (
            "我们家世世代代\x01",
            "都是商人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "老爸在经营一家贸易公司，\x01",
            "爷爷是工商协会的会长。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        (
            "不过啊～我对做生意\x01",
            "一点兴趣都没有～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8F2A")

    label("loc_8EEE")


    #C0517
    ChrTalk(
        0xFE,
        "啊～真是困倦啊～……\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        "今天也去随便消磨一下时间吧～\x02",
    )

    CloseMessageWindow()

    label("loc_8F2A")

    Jump("loc_9017")

    label("loc_8F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FA0")

    #C0519
    ChrTalk(
        0xFE,
        "啊，真是好闲啊。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xFE,
        (
            "虽然讨厌\x01",
            "大人们对我指手划脚的，\x01",
            "但自己一个人也闲得发慌啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8FB2")

    label("loc_8FA0")


    #C0521
    ChrTalk(
        0xFE,
        "啊，好闲啊～\x02",
    )

    CloseMessageWindow()

    label("loc_8FB2")

    Jump("loc_9017")

    label("loc_8FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9017")

    #C0522
    ChrTalk(
        0xFE,
        (
            "老爸和老妈把照顾\x01",
            "妹妹的工作都推给我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        "真是的，就不能让我一个人待一会吗？\x02",
    )

    CloseMessageWindow()

    label("loc_9017")

    TalkEnd(0xFE)
    Return()

    # Function_19_84A4 end

    def Function_20_901B(): pass

    label("Function_20_901B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9039")
    Call(0, 19)
    Jump("loc_9054")

    label("loc_9039")


    #C0524
    ChrTalk(
        0xFE,
        (
            "哥哥终于\x01",
            "恢复精神了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9054")

    Jump("loc_9628")

    label("loc_9059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_90B4")

    #C0525
    ChrTalk(
        0xFE,
        (
            "哥哥他最近\x01",
            "一直在盯着\x01",
            "路过的人看。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "哥哥跟平时不一样……\x01",
            "怎么了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_90B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_915E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913A")

    #C0527
    ChrTalk(
        0xFE,
        (
            "今天啊，哥哥\x01",
            "叫我要跟在他身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0528
    ChrTalk(
        0xFE,
        "太好啦……！\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "梅琳要一直\x01",
            "跟哥哥在一起！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9159")

    label("loc_913A")


    #C0530
    ChrTalk(
        0xFE,
        (
            "梅琳要一直跟\x01",
            "哥哥一起玩！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9159")

    Jump("loc_9628")

    label("loc_915E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91FD")
    OP_4B(0xE, 0xFF)

    #C0531
    ChrTalk(
        0xFE,
        "哥哥，我告诉你哦！\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        (
            "今天早上，\x01",
            "我看到一只很大的狗狗哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "白色的，\x01",
            "有这么大哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xE,
        (
            "哦～这样啊～\x01",
            "不错哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_922F")

    label("loc_91FD")


    #C0535
    ChrTalk(
        0xFE,
        (
            "哥哥最近\x01",
            "总是发呆。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xFE,
        (
            "都不听\x01",
            "梅琳讲话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_922F")

    Jump("loc_9628")

    label("loc_9234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9287")

    #C0537
    ChrTalk(
        0xFE,
        "纪念庆典，玩得好开心呢！\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        (
            "梅琳和哥哥\x01",
            "两个人一起去帮了忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_9287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_92C4")

    #C0539
    ChrTalk(
        0xFE,
        "哥哥……你要去哪里？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        (
            "别丢下\x01",
            "梅琳！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_92C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_930D")

    #C0541
    ChrTalk(
        0xFE,
        "哥哥，别丢下我～！\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "妈妈叫我\x01",
            "要和哥哥待在一起！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_930D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_936C")

    #C0543
    ChrTalk(
        0xFE,
        "哒啦啦啦啦……¤\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        "今天我也要和哥哥一起玩。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xFE,
        (
            "哥哥经常\x01",
            "陪我一起玩哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_936C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_93B8")

    #C0546
    ChrTalk(
        0xFE,
        (
            "哥哥给我\x01",
            "买零食了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        (
            "（嚼嚼嚼）……\x01",
            "嗯，好好吃哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_93B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_93FF")

    #C0548
    ChrTalk(
        0xFE,
        (
            "哥哥今天又被\x01",
            "爸爸教训了。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        "……哥哥，要振作哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_93FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_944B")

    #C0550
    ChrTalk(
        0xFE,
        (
            "哥哥说他不想\x01",
            "做生意哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xFE,
        (
            "他说现在是\x01",
            "人生的充电时期。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_944B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94CC")

    #C0552
    ChrTalk(
        0xFE,
        "爸爸是个很了不起的人哦，\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "他是一家很大的\x01",
            "贸易公司的经理哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "不过……哥哥他\x01",
            "讨厌爸爸……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_9502")

    label("loc_94CC")


    #C0555
    ChrTalk(
        0xFE,
        (
            "哥哥\x01",
            "讨厌爸爸……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "呜呜呜……\x01",
            "梅琳好难过……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9502")

    Jump("loc_9628")

    label("loc_9507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9575")

    #C0557
    ChrTalk(
        0xFE,
        "哒啦哒啦……¤\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        (
            "那边的红色房子，\x01",
            "是游击士协会哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "游击士每次来\x01",
            "都会跟我打招呼哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9628")

    label("loc_9575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9603")
    OP_4B(0xE, 0xFF)

    #C0560
    ChrTalk(
        0xE,
        "梅琳，你要听好哦～\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xE,
        (
            "哥哥今天\x01",
            "想好好发一下呆。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xE,
        (
            "你可以跟着我，\x01",
            "不过不许任性哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        "好！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_9628")

    label("loc_9603")


    #C0564
    ChrTalk(
        0xFE,
        (
            "能和哥哥一起出去，\x01",
            "好开心啊～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9628")

    TalkEnd(0xFE)
    Return()

    # Function_20_901B end

    def Function_21_962C(): pass

    label("Function_21_962C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_963D")
    Jump("loc_9E61")

    label("loc_963D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_973D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96E2")

    #C0565
    ChrTalk(
        0xFE,
        (
            "昨天我特意\x01",
            "做了晚饭……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "不过我们家的男人们，\x01",
            "一个个都到半夜才回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        (
            "还找借口说什么\x01",
            "工地现场主任不在之类的。\x01",
            "那也是理由吗！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9738")

    label("loc_96E2")


    #C0568
    ChrTalk(
        0xFE,
        (
            "……我已经生气了！\x01",
            "我绝对不再做家务了！\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "从现在开始，\x01",
            "都交给他们男人来做……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9738")

    Jump("loc_9E61")

    label("loc_973D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_97BB")

    #C0570
    ChrTalk(
        0xFE,
        "我家的男人们……\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xFE,
        (
            "昨天同时回来，\x01",
            "还催着要吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "真是的，只有在那种时候，\x01",
            "他们的意见才会那么一致！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E61")

    label("loc_97BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9843")

    #C0573
    ChrTalk(
        0xFE,
        (
            "据说……\x01",
            "亚里欧斯·马克莱因\x01",
            "去长期出差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "那个人不在的话，\x01",
            "总感觉有点不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        (
            "真希望他能一直\x01",
            "待在自治州。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E61")

    label("loc_9843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_98F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98C4")

    #C0576
    ChrTalk(
        0xFE,
        (
            "我家的男人们，\x01",
            "今天都在家无所事事。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xFE,
        "说是公司放假……\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "主妇怎么就没有假期呢，\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_98F1")

    label("loc_98C4")


    #C0579
    ChrTalk(
        0xFE,
        (
            "就算公司放假，\x01",
            "也应该帮忙做点家务活啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98F1")

    Jump("loc_9E61")

    label("loc_98F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9987")

    #C0580
    ChrTalk(
        0xFE,
        (
            "啊，都到中午了啊……？\x01",
            "必须得回去\x01",
            "洗衣服了。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xFE,
        (
            "打扫、洗衣服、做饭、买东西……\x01",
            "每天都忙得要死，\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        "怎么就没人来帮帮我呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E61")

    label("loc_9987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9A3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A01")

    #C0583
    ChrTalk(
        0xFE,
        (
            "我家的男人们都\x01",
            "在建筑工地工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "最近一直\x01",
            "抱怨工作很辛苦……\x01",
            "然后在家都懒懒散散的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9A37")

    label("loc_9A01")


    #C0585
    ChrTalk(
        0xFE,
        (
            "每天都得\x01",
            "做一大堆家务活，\x01",
            "我不是比他们更辛苦吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A37")

    Jump("loc_9E61")

    label("loc_9A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9A83")

    #C0586
    ChrTalk(
        0xFE,
        (
            "啊，今天的鱼\x01",
            "品种好像很少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        "到底怎么回事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E61")

    label("loc_9A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B10")

    #C0588
    ChrTalk(
        0xFE,
        (
            "『彩虹』的门票\x01",
            "竟然都卖光了？\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "呜～我要是\x01",
            "不用做家务的话，\x01",
            "就可以去买了……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        (
            "我家的人\x01",
            "真是让人生气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9B4C")

    label("loc_9B10")


    #C0591
    ChrTalk(
        0xFE,
        (
            "我家的男人们\x01",
            "怎么就不帮我做点家务呢……\x01",
            "真是让人生气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B4C")

    Jump("loc_9E61")

    label("loc_9B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BAA")

    #C0592
    ChrTalk(
        0xFE,
        (
            "回去之后\x01",
            "还必须洗\x01",
            "一大堆衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xFE,
        "家人太多也很辛苦啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9BDD")

    label("loc_9BAA")


    #C0594
    ChrTalk(
        0xFE,
        (
            "啊，要是我家的男人们\x01",
            "能帮我做点家务就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BDD")

    Jump("loc_9E61")

    label("loc_9BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9C6F")

    #C0595
    ChrTalk(
        0xFE,
        (
            "露天店的一个好处\x01",
            "就是可以和店里的人聊天。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "这家店的阿姨会教我\x01",
            "如何快速处理活鱼哦。\x01",
            "赶时间的时候，那方法可真帮了大忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E61")

    label("loc_9C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CF3")

    #C0597
    ChrTalk(
        0xFE,
        (
            "我们家有\x01",
            "五个大男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        (
            "他们只是块头比较大而已，\x01",
            "一点忙都帮不上。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        (
            "至少也得\x01",
            "帮我做做家务吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9D43")

    label("loc_9CF3")


    #C0600
    ChrTalk(
        0xFE,
        (
            "我们家有五个\x01",
            "徒有体格，完全没用的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "真是……怎么会\x01",
            "全都是男的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D43")

    Jump("loc_9E61")

    label("loc_9D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DB7")

    #C0602
    ChrTalk(
        0xFE,
        (
            "胡萝卜八个、洋葱十二个、\x01",
            "鲑鱼十五条……\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xFE,
        (
            "嗯，还有……\x01",
            "我还要买什么来着呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_9DF9")

    label("loc_9DB7")


    #C0604
    ChrTalk(
        0xFE,
        (
            "在露天市场逛着逛着\x01",
            "就忘掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        (
            "嗯……我是来买\x01",
            "什么的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DF9")

    Jump("loc_9E61")

    label("loc_9DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9E61")

    #C0606
    ChrTalk(
        0xFE,
        "对了，要买点鱼……\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        (
            "我家的男人们\x01",
            "都很能吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        (
            "唉，只是给他们\x01",
            "做饭就很辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E61")

    TalkEnd(0xFE)
    Return()

    # Function_21_962C end

    def Function_22_9E65(): pass

    label("Function_22_9E65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ECC")

    #C0609
    ChrTalk(
        0xFE,
        (
            "我妈觉得买菜很麻烦，\x01",
            "所以我就来帮她买了。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        "我妈正在家里放松呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9EE5")

    label("loc_9ECC")


    #C0611
    ChrTalk(
        0xFE,
        (
            "我妈她\x01",
            "很怕麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE5")

    TalkEnd(0xFE)
    Return()

    # Function_22_9E65 end

    def Function_23_9EE9(): pass

    label("Function_23_9EE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F6C")

    #C0612
    ChrTalk(
        0xFE,
        (
            "我还以为自己发现了能买到\x01",
            "最物美价廉的东西的好方法，结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        "这世界上还真是充满了变数啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_9FC6")

    label("loc_9F6C")


    #C0614
    ChrTalk(
        0xFE,
        (
            "我还以为自己找到了\x01",
            "买东西的最好方法，结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        (
            "又要从头开始记\x01",
            "每家店的习惯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC6")

    Jump("loc_A998")

    label("loc_9FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A037")

    #C0616
    ChrTalk(
        0xFE,
        (
            "啊，蔬菜的价格\x01",
            "好像上涨了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        "这是为什么呢？\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xFE,
        "不应该涨价的啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A092")

    label("loc_A037")


    #C0619
    ChrTalk(
        0xFE,
        (
            "蔬菜的价格\x01",
            "好像上涨了啊……\x01",
            "而且鱼的价格也涨了……\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0xFE,
        (
            "真是奇怪，\x01",
            "不应该涨价的啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A092")

    Jump("loc_A998")

    label("loc_A097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A1DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A151")

    #C0621
    ChrTalk(
        0xFE,
        (
            "最近我终于发现了\x01",
            "能买到最价廉物美的东西的好方法……\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xFE,
        (
            "这多亏了我每天买东西的时候\x01",
            "都会去记每家店的习惯。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        (
            "呵呵……能买到最便宜的东西，\x01",
            "真是开心啊¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A1D8")

    label("loc_A151")


    #C0624
    ChrTalk(
        0xFE,
        (
            "我记住每家店的习惯，\x01",
            "然后就找到了能买到最物美价廉的东西的好方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0xFE,
        (
            "呵呵……感觉就像是\x01",
            "解开了一道很难的数学题，\x01",
            "真是很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1D8")

    Jump("loc_A998")

    label("loc_A1DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A1EB")
    Jump("loc_A998")

    label("loc_A1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A2DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A28E")

    #C0626
    ChrTalk(
        0xFE,
        (
            "纪念庆典的五天里，\x01",
            "我把做作业的事都忘光了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0627
    ChrTalk(
        0xFE,
        "必须快点把主日学校的作业做完。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        "不然会被修女骂的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A2D8")

    label("loc_A28E")


    #C0629
    ChrTalk(
        0xFE,
        (
            "纪念庆典前\x01",
            "学校布置了好多作业。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        (
            "回到家后，\x01",
            "必须赶快把作业做完。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2D8")

    Jump("loc_A998")

    label("loc_A2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A40C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3A3")

    #C0631
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔工商协会的会长\x01",
            "很了不起，他连市长也认识哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "虽然他现在贵为会长，\x01",
            "可以前也只是个普通的露天店摊贩而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        (
            "他平时也会跟我打招呼，\x01",
            "真是个亲切的老爷爷。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A407")

    label("loc_A3A3")


    #C0634
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔工商协会的会长\x01",
            "是个很亲切的老爷爷哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        (
            "刚才他路过这里的时候，\x01",
            "也跟我打了招呼哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A407")

    Jump("loc_A998")

    label("loc_A40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A4AD")

    #C0636
    ChrTalk(
        0xFE,
        (
            "今天买的东西\x01",
            "比预想中的还要便宜¤\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        (
            "……不过，要是放松神经的话，\x01",
            "不小心就会购买多余的东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        (
            "必须好好把钱节约下来\x01",
            "当做我的零花钱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A998")

    label("loc_A4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A50B")

    #C0639
    ChrTalk(
        0xFE,
        (
            "那家店的库隆克先生，\x01",
            "手上总是包着绷带。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        (
            "……没事吧，\x01",
            "让人有点担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A998")

    label("loc_A50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A5FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C1")

    #C0641
    ChrTalk(
        0xFE,
        (
            "妈妈把购物清单和买东西的钱一起给了我，\x01",
            "不过钱好像多给了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        (
            "我要是节省一点的话，\x01",
            "剩下的钱就可以当零花钱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xFE,
        (
            "……今天也要努力\x01",
            "省下点钱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A5F6")

    label("loc_A5C1")


    #C0644
    ChrTalk(
        0xFE,
        (
            "嗯，鱼的价格\x01",
            "每天都在变啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xFE,
        "真难捉摸……\x02",
    )

    CloseMessageWindow()

    label("loc_A5F6")

    Jump("loc_A998")

    label("loc_A5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A64E")

    #C0646
    ChrTalk(
        0xFE,
        "啊，今天是主日学校上课的日子。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        (
            "买完东西后\x01",
            "必须快点赶去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A998")

    label("loc_A64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6FB")

    #C0648
    ChrTalk(
        0xFE,
        (
            "这个时间的话，\x01",
            "迪因兹食材店的\x01",
            "价格应该是最便宜的。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        (
            "嗯，不过蔬菜\x01",
            "的新鲜度也很重要……\x01",
            "还是先不要急着买好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xFE,
        "去逛逛其它店再说吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A720")

    label("loc_A6FB")


    #C0651
    ChrTalk(
        0xFE,
        (
            "要买到最便宜的东西\x01",
            "也很难啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A720")

    Jump("loc_A998")

    label("loc_A725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A81B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C6")

    #C0652
    ChrTalk(
        0xFE,
        (
            "今天早上，游击士协会的人\x01",
            "来巡视露天市场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "……游击士都很忙啊。\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xFE,
        (
            "只要这条街上发生了纠纷，\x01",
            "大家都会去向游击士协会求助。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A816")

    label("loc_A7C6")


    #C0655
    ChrTalk(
        0xFE,
        (
            "今天早上，游击士们\x01",
            "看起来很悠闲的样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0xFE,
        (
            "我在迪因兹的店\x01",
            "买了蔬菜哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A816")

    Jump("loc_A998")

    label("loc_A81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A8F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8B3")

    #C0657
    ChrTalk(
        0xFE,
        (
            "那家店正在打折，\x01",
            "所以我不小心买了许多。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0658
    ChrTalk(
        0xFE,
        (
            "本来还想省点钱的，\x01",
            "……我怎么就会买了那么多呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A8F0")

    label("loc_A8B3")


    #C0659
    ChrTalk(
        0xFE,
        (
            "卖东西真是一门很深奥的学问啊。\x01",
            "买东西也不是件轻松的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8F0")

    Jump("loc_A998")

    label("loc_A8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A956")

    #C0660
    ChrTalk(
        0xFE,
        (
            "嗯，这家店的价格\x01",
            "稍微便宜一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xFE,
        (
            "不过，那家店\x01",
            "可以讲价……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A998")

    label("loc_A956")


    #C0662
    ChrTalk(
        0xFE,
        (
            "这家蔬果店到傍晚\x01",
            "就会限时打折。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xFE,
        (
            "我还是等一会\x01",
            "再来买吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A998")

    TalkEnd(0xFE)
    Return()

    # Function_23_9EE9 end

    def Function_24_A99C(): pass

    label("Function_24_A99C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A9E6")

    #C0664
    ChrTalk(
        0xFE,
        (
            "啊，铁桥的对面\x01",
            "好像很吵啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        "发生什么事了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB1B")

    label("loc_A9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_AB1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA98")

    #C0666
    ChrTalk(
        0xFE,
        (
            "在旅途中要是遇到了困难，\x01",
            "果然还是得去向游击士协会求助啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xFE,
        (
            "无论什么时候，也不管在哪个国家，\x01",
            "他们都是站在市民这边的。\x01",
            "这真是让我们安心了不少。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_AB1B")

    label("loc_AA98")


    #C0668
    ChrTalk(
        0xFE,
        (
            "在旅途中要是遇到了困难，\x01",
            "果然还是得去向游击士协会求助啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xFE,
        (
            "而且听说克洛斯贝尔\x01",
            "的游击士特别优秀，\x01",
            "这真是让我们安心了不少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB1B")

    TalkEnd(0xFE)
    Return()

    # Function_24_A99C end

    def Function_25_AB1F(): pass

    label("Function_25_AB1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_ABD6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB3E")
    Call(0, 26)
    Jump("loc_ABD6")

    label("loc_AB3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB99")

    #C0670
    ChrTalk(
        0xFE,
        "欢迎光临～……\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        (
            "拜托你们去光顾一下店里吧，\x01",
            "不然我会被老板骂的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_ABD6")

    label("loc_AB99")


    #C0672
    ChrTalk(
        0xFE,
        "这个老板很可怕啊。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xFE,
        (
            "要是当初去别的店\x01",
            "打工就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABD6")

    TalkEnd(0xFE)
    Return()

    # Function_25_AB1F end

    def Function_26_ABDA(): pass

    label("Function_26_ABDA")


    #C0674
    ChrTalk(
        0xFE,
        (
            "我在这里打工时，\x01",
            "想到了很美味的麻婆豆腐\x01",
            "的做法哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        "你们要学吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0676
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '药膳麻婆豆腐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0677
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '药膳麻婆豆腐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x2)
    Return()

    # Function_26_ABDA end

    def Function_27_AC92(): pass

    label("Function_27_AC92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_AD5F")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACBC")
    Call(0, 28)
    Jump("loc_AD53")

    label("loc_ACBC")


    #C0678
    ChrTalk(
        0x17,
        (
            "#6002F我能听到……风的声音。\x02\x03",

            "谢谢你们……！\x01",
            "艾丝蒂尔姐姐、约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x15,
        "#0809F嘿嘿……\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x16,
        "#0902F你高兴就好。\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#0004F（有点嫉妒啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_AD53")

    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)

    label("loc_AD5F")

    TalkEnd(0xFE)
    Return()

    # Function_27_AC92 end

    def Function_28_AD63(): pass

    label("Function_28_AD63")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_68(-24130, -1400, 4220, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -19520, -3000, 5040, 270)
    SetChrPos(0x102, -19520, -3000, 3780, 270)
    SetChrPos(0x103, -18270, -3000, 3780, 270)
    SetChrPos(0x104, -18270, -3000, 5040, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE0B")
    SetChrPos(0x10A, -18500, -3000, 2490, 270)

    label("loc_AE0B")

    OP_0D()
    Sleep(250)

    #C0682
    ChrTalk(
        0x17,
        (
            "#6000F呵呵……\x01",
            "风车好有趣呢。\x02\x03",

            "虽然看不见……\x01",
            "但能感到它确实在转动。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x15,
        (
            "#0800F是吗……风车可以让人听到\x01",
            "风的声音，感到风的吹拂啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x8, 500)

    #C0684
    ChrTalk(
        0x16,
        (
            "#0900F您好，\x01",
            "请给我一个粉红色的。\x02\x03",

            "因为是要送人的，\x01",
            "所以麻烦您再包装一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x8,
        "多谢惠顾！\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)

    #C0686
    ChrTalk(
        0x17,
        "#6008F约、约修亚哥哥……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x5A, 0x1F4)

    #C0687
    ChrTalk(
        0x15,
        (
            "#0800F别客气啦，\x01",
            "这没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x16,
        (
            "#0904F我们平时一直承蒙\x01",
            "亚里欧斯先生的照顾。\x02\x03",

            "#0902F当然，并不是因为这个原因才买下这个风车的。\x01",
            "总之，如果小滴能收下的话，我们会很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x17,
        "#6002F谢、谢谢两位……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-19140, -1400, 3950, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sleep(100)

    #C0690
    ChrTalk(
        0x104,
        (
            "#0300F（哈哈……\x01",
            "  好像很开心啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        (
            "#0000F（是啊……\x01",
            "  我们还是不要去打扰他们吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD0, 1)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_AD63 end

    def Function_29_B0BA(): pass

    label("Function_29_B0BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-16810, 1440, 25050, 0)
    MoveCamera(49, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26970, 0)
    OP_68(-1670, 1440, 2470, 7000)
    MoveCamera(25, 17, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(21920, 7000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(5230, -200, -13420, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(-26250, 1500, -2620, 6000)
    MoveCamera(22, 22, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14290, 6000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xB, 0x8000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-6850, 1440, -820, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31810, 0)
    SetCameraDistance(37810, 5000)
    OP_0D()
    PlaceName2(340, 40, "c_plac04", 0x0, 0)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B365")

    #A0692
    AnonymousTalk(
        0x104,
        (
            "#0305F哇，好有\x01",
            "异国风情的街道啊。\x02",
        )
    )

    CloseMessageWindow()

    #A0693
    AnonymousTalk(
        0x103,
        (
            "#0202F是东方风格的吧……\x01",
            "虽然早有耳闻，但亲眼看到还是令人惊叹啊。\x02",
        )
    )

    CloseMessageWindow()

    #A0694
    AnonymousTalk(
        0x102,
        (
            "#0102F东街的露天市场……\x01",
            "我都没怎么来过呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0695
    AnonymousTalk(
        0x104,
        (
            "#0309F哦，那我们\x01",
            "就稍微逛一逛吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0696
    AnonymousTalk(
        0x101,
        (
            "#0006F那个……\x01",
            "我们不是来购物的啊。\x02\x03",

            "#0008F（还有……东街上\x01",
            "  好像有游击士协会啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B365")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0697
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东街是位于城市东边的一条具有东方风格的街区。\x02",
        )
    )

    CloseMessageWindow()

    #A0698
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里有一个热闹的露天市场，\x01",
            "许多市民和购物者都会来往于此。\x02",
        )
    )

    CloseMessageWindow()

    #A0699
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，深受广大市民支持的\x01",
            "『游击士协会』的分部也坐落在这里。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4CC")
    OP_68(-29790, 1420, 13830, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    Jump("loc_B519")

    label("loc_B4CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B519")
    SetChrPos(0x0, -20550, -310, 29980, 180)
    OP_68(-20550, 1440, 29980, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)

    label("loc_B519")

    SetScenarioFlags(0x44, 5)
    EventEnd(0x5)
    Return()

    # Function_29_B0BA end

    def Function_30_B51F(): pass

    label("Function_30_B51F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10500, 2000, -1000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 27600, -300, -2700, 0)
    SetChrPos(0x1, 27600, -300, -2700, 0)
    SetChrPos(0x2, 27600, -300, -2700, 0)
    SetChrPos(0x3, 27600, -300, -2700, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0x10, -19900, -320, 18140, 90)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrPos(0xC, -16300, -300, 12700, 135)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrPos(0xD, -4900, -300, 4000, 315)
    SetChrFlags(0xD, 0x8000)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0700
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日，１５：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7103", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B68C():
        OP_98(0xFE, 0x32C8, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B68C)

    def lambda_B6A6():
        OP_98(0xFE, 0xFFFFCD38, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B6A6)
    OP_68(-10500, 1000, -1000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-7500, 2100, 14100, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(17500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearScenarioFlags(0x2, 4)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_B51F end

    def Function_31_B734(): pass

    label("Function_31_B734")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-7800, 1300, 13600, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, -7000, 300, 14400, 225)
    SetChrPos(0x102, -7000, 300, 14400, 225)
    SetChrPos(0x103, -7000, 300, 14400, 225)
    SetChrPos(0x104, -7000, 300, 14400, 225)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x17, -7000, 300, 14400, 225)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0x10, -19900, -320, 18140, 90)
    SetChrFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-11000, 700, 10250, 4500)

    def lambda_B889():
        OP_95(0xFE, -12000, -300, 9400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B889)

    def lambda_B8A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B8A3)
    Sleep(500)

    def lambda_B8B7():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B8B7)

    def lambda_B8D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B8D1)
    Sleep(500)

    def lambda_B8E5():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B8E5)

    def lambda_B8FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B8FF)
    Sleep(500)

    def lambda_B913():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B913)

    def lambda_B92D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B92D)
    Sleep(700)

    def lambda_B941():
        OP_95(0xFE, -9600, -300, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B941)

    def lambda_B95B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_B95B)
    WaitChrThread(0x103, 1)

    def lambda_B970():
        OP_95(0xFE, -11000, -300, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B970)

    def lambda_B98A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B98A)
    WaitChrThread(0x102, 1)

    def lambda_B99F():
        OP_95(0xFE, -11600, -300, 11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B99F)

    def lambda_B9B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B9B9)
    WaitChrThread(0x104, 1)

    def lambda_B9CE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B9CE)
    WaitChrThread(0x103, 1)

    def lambda_B9DF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B9DF)
    WaitChrThread(0x102, 1)

    def lambda_B9F0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B9F0)
    WaitChrThread(0x101, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0701
    ChrTalk(
        0x101,
        (
            "#0006F#11P啊……\x01",
            "好像被比下去了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x103,
        (
            "#6P#0204F亚里欧斯先生就不用说了，\x01",
            "连新星艾丝蒂尔他们也很厉害……\x02\x03",

            "#0202F而且其他人员\x01",
            "似乎也都拥有很强的实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        (
            "#6P#0300F他们好像全部\x01",
            "都是Ｂ级以上的游击士啊……\x02\x03",

            "这么多年轻的高手们\x01",
            "都聚集在了一个分部，\x01",
            "这不是很少见吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x102,
        (
            "#5P#0102F这说明游击士协会\x01",
            "相当重视\x01",
            "克洛斯贝尔这个地方吧。\x02\x03",

            "#0106F再说得明白一点，或许他们已经看出了\x01",
            "这里的环境令警察束手束脚……\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#0006F#11P是啊……\x01",
            "我们也必须好好努力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-10100, 700, 11300, 1200)

    def lambda_BC16():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC16)
    Sleep(150)

    def lambda_BC26():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BC26)
    Sleep(50)
    TurnDirection(0x102, 0x17, 500)
    OP_6F(0x1)

    #C0706
    ChrTalk(
        0x101,
        (
            "#6P#0012F啊，抱歉，\x01",
            "突然说了奇怪的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x17,
        (
            "#6002F#11P呵呵，请不必在意。\x02\x03",

            "#6008F爸爸以前当过警察的事情，\x01",
            "我也曾听说过……\x02\x03",

            "虽然好像有很多\x01",
            "复杂难懂的问题……\x02\x03",

            "#6000F不过，在这次的任务中，\x01",
            "他会与大家合作吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD92")

    #C0708
    ChrTalk(
        0x101,
        (
            "#6P#0004F嗯，与其说是合作，\x01",
            "不如说是我们在受他帮助。\x02\x03",

            "#0002F──那么，我带你\x01",
            "去支援科吧。\x02\x03",

            "可以牵着你的手吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C015")

    label("loc_BD92")


    #C0709
    ChrTalk(
        0x101,
        (
            "#6P#0004F嗯，与其说是合作，\x01",
            "不如说是我们在受他帮助。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0710
    ChrTalk(
        0x101,
        (
            "#6P#0000F对了，前天做的\x01",
            "那个挂件……\x02\x03",

            "你送给你爸爸了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x17,
        (
            "#6005F#11P啊……是的。\x02\x03",

            "#6000F嘿嘿……其实爸爸\x01",
            "昨晚来看我了。\x02\x03",

            "#6010F我把挂件送给他了……\x01",
            "不过，他那时的表情是什么样的呢……\x02\x03",

            "当时他沉默了一会……\x01",
            "然后稍微有些不自然地\x01",
            "对我说了谢谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x104,
        (
            "#6P#0302F哈哈……他是不是说了\x01",
            "『……那我就收下了』之类的生硬台词呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x17,
        "#6002F#11P嗯，就是那种感觉。\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x103,
        "#6P#0204F很容易想象得到啊……\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x102,
        (
            "#6P#0109F呵呵，在小滴面前，\x01",
            "亚里欧斯先生也没法像平时那样从容了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x101,
        (
            "#6P#0004F这说明他相当\x01",
            "重视小滴哦……\x02\x03",

            "#0002F──那么，我带你\x01",
            "去支援科吧。\x02\x03",

            "可以牵着你的手吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C015")


    #C0717
    ChrTalk(
        0x17,
        (
            "#6000F#11P谢、谢谢你。\x02\x03",

            "#6005F对了……\x01",
            "小琪雅也在吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#0102F嗯，她现在应该\x01",
            "和蔡特在一起吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x103,
        (
            "#6P#0202F要是她知道滴来玩，\x01",
            "肯定会高兴得跳起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x17,
        "#6002F#11P呵呵……好开心。\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x104,
        (
            "#6P#0302F好～那我们这就\x01",
            "护送小公主回去吧！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrPos(0x101, -17500, -300, 14300, 270)
    SetChrPos(0x102, -17400, -300, 13000, 270)
    SetChrPos(0x103, -16000, -300, 13200, 270)
    SetChrPos(0x104, -15800, -300, 14500, 270)
    SetChrPos(0x17, -17500, -300, 13700, 270)
    OP_68(-22000, 500, 13700, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(15500, 0)

    def lambda_C19F():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C19F)
    Sleep(15)

    def lambda_C1BC():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C1BC)
    Sleep(15)

    def lambda_C1D9():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C1D9)
    Sleep(15)

    def lambda_C1F6():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C1F6)
    Sleep(15)

    def lambda_C213():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_C213)
    BeginChrThread(0x101, 3, 0, 32)
    OP_68(-27000, 500, 13700, 10000)
    MoveCamera(54, 18, 0, 10000)
    SetCameraDistance(19500, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -40000, -340, 16000, 90)
    SetChrFlags(0xD, 0x8000)

    def lambda_C2EB():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C2EB)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_B734 end

    def Function_32_C3A0(): pass

    label("Function_32_C3A0")

    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -10000, -300, 6500, 315)
    SetChrFlags(0xC, 0x8000)

    def lambda_C3C5():
        OP_95(0xFE, -16000, -300, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C3C5)
    WaitChrThread(0xC, 1)

    def lambda_C3E3():
        OP_95(0xFE, -36000, -300, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C3E3)
    WaitChrThread(0xC, 1)
    Return()

    # Function_32_C3A0 end

    def Function_33_C3FD(): pass

    label("Function_33_C3FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
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
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_C4D1():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4D1)
    Sleep(50)

    def lambda_C4EE():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C4EE)
    Sleep(50)

    def lambda_C50B():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C50B)
    Sleep(50)

    def lambda_C528():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C528)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    Sleep(250)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C58B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C58B)
    Sleep(50)

    def lambda_C59B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C59B)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    #Sound(1084, 255, 90, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0722
    AnonymousTalk(
        0x101,
        (
            "#0001F您好，我是\x01",
            "特别任务支援科的班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    #Sound(2083, 255, 100, 0)    #voice#Fran
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0723
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官～！\x02\x03",

            "太好了，\x01",
            "终于联系上了啊～\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0724
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F芙兰吗……？\x01",
            "你很少会直接联系我啊。\x02\x03",

            "#0000F发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0725
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那个……\x02\x03",

            "其实是有人\x01",
            "想找支援科帮忙……\x02\x03",

            "我可以让那位市民直接去你们那边吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0726
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F嗯……\x01",
            "当然可以。\x02\x03",

            "不过平时不是一直\x01",
            "将委托发至这边的终端的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0727
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯……\x01",
            "因为这次的情况比较严重。\x02\x03",

            "而且那位市民指名\x01",
            "一定要找罗伊德警官你们帮忙。\x02\x03",

            "我觉得这种情况有些少见，所以就直接联系你了～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0728
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0012F这、这样啊……\x02\x03",

            "#0000F我知道了，\x01",
            "那我们回支援科去就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0729
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，我会让那位市民\x01",
            "直接去你们那里的。\x02\x03",

            "你们估计要多久才能到支援科呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0730
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F我想想啊……\x02\x03",

            "#0000F有可能会晚一点，\x01",
            "请你转告那位市民，\x01",
            "如果早到了就在里面稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0731
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，我知道了。\x02\x03",

            "那么，罗伊德警官，\x01",
            "这件事就拜托你们了哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0732
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0105F#5P有紧急任务了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x104, 500)

    #C0733
    ChrTalk(
        0x101,
        (
            "#6P#0003F是啊……\x01",
            "而且情况好像有些严重。\x02\x03",

            "#0000F暂时先放下其它支援请求，\x01",
            "回一趟支援科吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x103,
        "#0202F#11P……了解。\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x104,
        "#5P#0309F话说，委托人是个美女吗？\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        "#6P#0006F这我怎么会知道。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x0, 24700, -300, 500, 270)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x80, 1)
    OP_29(0x41, 0x1, 0x2)
    OP_24(0x326)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_C3FD end

    def Function_34_CB6A(): pass

    label("Function_34_CB6A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5890, -1400, -10830, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14300, 0)
    SetChrPos(0x101, -5200, -3000, -10840, 0)
    SetChrPos(0x102, -3950, -3000, -12150, 0)
    SetChrPos(0x103, -5040, -3000, -11950, 0)
    SetChrPos(0x104, -3970, -3000, -10800, 0)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC5D")

    #C0737
    ChrTalk(
        0x101,
        (
            "#6P#0003F（东街的市场……\x01",
            "  这里是遗失了物品的特伦特先生\x01",
            "  途中经过的地方。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_CC5D")


    #C0738
    ChrTalk(
        0x101,
        (
            "#6P#0000F不好意思，请问您在这附近\x01",
            "捡到过什么失物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xB,
        "#5P失物吗……？\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xB,
        (
            "#5P哦，说起来……\x01",
            "昨天有一个看起来挺悠闲的青年\x01",
            "掉了一个东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xB,
        (
            "#5P他看见我们的店，\x01",
            "还开了一个无聊的玩笑。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xB,
        (
            "#5P他的包上有个大洞，\x01",
            "然后从里面掉下来了一个小包裹，\x01",
            "不过他没发现，就那样走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xB,
        (
            "#5P虽然我马上追了过去，\x01",
            "但没追上。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x104,
        "#11P#0300F哈哈……好像找对地方了啊。\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xB,
        (
            "#5P嗯？你们是来取那个的\x01",
            "警察吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0xB,
        "#5P那我就直接交给你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0747
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '罗赞贝尔克人偶·Ｓ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "拿到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｓ', 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('罗赞贝尔克人偶·Ｍ', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('罗赞贝尔克人偶·Ｓ', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('波波碰！β版', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEDC")

    #C0748
    ChrTalk(
        0x101,
        (
            "#0006F呼……这样一来，总算\x01",
            "全部找到了。\x02\x03",

            "#0000F我们去跟特伦特先生报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x102,
        "#0100F嗯，去把东西还给他吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_CEDC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-4630, -1400, -10720, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, -4630, -3000, -10720, 0)
    SetChrPos(0x1, -4630, -3000, -10720, 0)
    SetChrPos(0x2, -4630, -3000, -10720, 0)
    SetChrPos(0x3, -4630, -3000, -10720, 0)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_29(0x2, 0x1, 0x2)
    SetScenarioFlags(0x2, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF93")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_CF93")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_CB6A end

    def Function_35_CF99(): pass

    label("Function_35_CF99")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D02D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D00C")

    #C0750
    ChrTalk(
        0x101,
        (
            "#0000F这里是城市的东出口。\x02\x03",

            "现在没有外出的必要……\x01",
            "专心做好市区内的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D02D")

    label("loc_D00C")

    SetChrName("")

    #A0751
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有外出的必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D02D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09D")

    #C0752
    ChrTalk(
        0x101,
        (
            "#0000F要去乌尔斯拉医院就\x01",
            "必须从城市的南出口出去。\x02\x03",

            "我们从中央广场取道去\x01",
            "站前街道那边看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D09D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0F6")

    #C0753
    ChrTalk(
        0x101,
        (
            "#0000F要去玛因兹就\x01",
            "必须从城市的北出口出去。\x02\x03",

            "我们去住宅街那边看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D189")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D168")

    #C0754
    ChrTalk(
        0x101,
        (
            "#0005F啊，这里是东出口。\x02\x03",

            "#0000F为了防止琪雅\x01",
            "遇到危险，\x01",
            "我们还是不要出去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D189")

    label("loc_D168")

    SetChrName("")

    #A0755
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有必要去市外。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D22D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D204")

    #C0756
    ChrTalk(
        0x101,
        (
            "#0003F这里是城市的东出口。\x02\x03",

            "还有黑月的事情没解决……\x01",
            "……现在集中在市区内进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D22D")

    label("loc_D204")

    SetChrName("")

    #A0757
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在集中在市区内进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D2B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D289")

    #C0758
    ChrTalk(
        0x101,
        (
            "#0000F这里是城市的东出口。\x01",
            "……现在必须得赶去乌尔斯拉医院！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D2B4")

    label("loc_D289")

    SetChrName("")

    #A0759
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没有去东克洛斯贝尔街道的必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D2B4")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_35_CF99 end

    def Function_36_D2C8(): pass

    label("Function_36_D2C8")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D45A")

    #C0760
    ChrTalk(
        0x10A,
        "#0603F………………………………\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        (
            "#0005F达德利警官，\x01",
            "您怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D34A")

    #C0762
    ChrTalk(
        0x10A,
        "#0601F哼，协会吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D36A")

    label("loc_D34A")


    #C0763
    ChrTalk(
        0x10A,
        "#0601F你们莫非……（瞪视）\x02",
    )

    CloseMessageWindow()

    label("loc_D36A")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0764
    ChrTalk(
        0x101,
        (
            "#0005F（呃，对了……\x01",
            "  达德利警官对游击士的厌恶\x01",
            "  是十分根深蒂固的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#0306F（这样的话，\x01",
            "  我们最好还是不要进去了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 6)
    Jump("loc_D51F")

    label("loc_D45A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4BC")

    #C0766
    ChrTalk(
        0x10A,
        (
            "#0603F………………………………\x02\x03",

            "#0600F没什么事要去这里，\x01",
            "……快点出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D51F")

    label("loc_D4BC")


    #C0767
    ChrTalk(
        0x10A,
        "#0600F………………………………\x02",
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        (
            "#0006F（达德利警官在瞪着我们……\x01",
            "  现在还是不要进去吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D51F")

    Sleep(50)
    SetChrPos(0x0, -9300, -300, 12060, 225)
    EventEnd(0x4)
    Return()

    # Function_36_D2C8 end

    def Function_37_D536(): pass

    label("Function_37_D536")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5AA")

    #C0769
    ChrTalk(
        0x101,
        (
            "#0005F哦……\x02\x03",

            "那个记者说的店\x01",
            "好像就在那边啊。\x02\x03",

            "#0003F现在我们需要情报，\x01",
            "总之先去问问看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D5DD")

    label("loc_D5AA")


    #C0770
    ChrTalk(
        0x101,
        (
            "#0003F现在我们需要情报……\x01",
            "总之先去问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5DD")

    Sleep(50)
    SetChrPos(0x0, -6210, -3000, -9790, 135)
    EventEnd(0x4)
    Return()

    # Function_37_D536 end

    def Function_38_D5F4(): pass

    label("Function_38_D5F4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D668")

    #C0771
    ChrTalk(
        0x101,
        (
            "#0005F哦……\x02\x03",

            "那个记者说的店\x01",
            "好像就在那边啊。\x02\x03",

            "#0003F现在我们需要情报，\x01",
            "总之先去问问看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D69B")

    label("loc_D668")


    #C0772
    ChrTalk(
        0x101,
        (
            "#0003F现在我们需要情报……\x01",
            "总之先去问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D69B")

    Sleep(50)
    SetChrPos(0x0, 2100, -1350, -5490, 180)
    EventEnd(0x4)
    Return()

    # Function_38_D5F4 end

    def Function_39_D6B2(): pass

    label("Function_39_D6B2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_END)), "loc_D6E6")
    SetChrName("")

    #A0773
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
    Jump("loc_F348")

    label("loc_D6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB0E")
    SetChrName("")

    #A0774
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D922")

    #C0775
    ChrTalk(
        0x153,
        (
            "#1110F……啊！\x01",
            "我说，这里好像有东西？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_D7A3")

    #C0776
    ChrTalk(
        0x102,
        (
            "#0105F这种地方竟然有地藏菩萨……\x01",
            "虽然路过了好几次，可都没察觉到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D82A")

    label("loc_D7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_D7E8")

    #C0777
    ChrTalk(
        0x103,
        (
            "#0205F地藏菩萨……脸好大啊。\x01",
            "这还是我第一次见到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D82A")

    label("loc_D7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D82A")

    #C0778
    ChrTalk(
        0x104,
        (
            "#0305F哎～竟然还供奉着地藏菩萨。\x01",
            "看来我们都看漏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D82A")


    #C0779
    ChrTalk(
        0x153,
        "#1111F……地藏？\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0780
    ChrTalk(
        0x153,
        (
            "#1105F那个那个，\x01",
            "这里好像有个放东西的台座哦。\x02\x03",

            "#1110F地藏菩萨肚子或许饿了，\x01",
            "我们拿点吃的给他吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#0000F这一定是摆放供品的台座。\x02\x03",

            "#0000F对了，\x01",
            "如果下次做出了大成功的料理，\x01",
            "就拿点过来供奉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB06")

    label("loc_D922")


    #C0782
    ChrTalk(
        0x104,
        (
            "#0305F哎～虽然知道这条街\x01",
            "是东方风格的，\x01",
            "但没想到竟然还供奉着地藏菩萨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x103,
        (
            "#0200F我好像是第一次见到地藏菩萨。\x01",
            "……好大的脸呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9CC")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_D9CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9EF")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_D9EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA12")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_DA12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA35")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_DA35")


    #C0784
    ChrTalk(
        0x103,
        "#0205F地藏菩萨面前的台座是……？\x02",
    )

    CloseMessageWindow()

    #C0785
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

    #C0786
    ChrTalk(
        0x101,
        (
            "#0000F对了，支援科基本都是自己煮饭。\x02\x03",

            "如果下次做了成功的料理，\x01",
            "就拿点过来供奉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB06")

    SetScenarioFlags(0x98, 0)
    Jump("loc_F348")

    label("loc_DB0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_DB3F")
    SetChrName("")

    #A0787
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
    Jump("loc_F348")

    label("loc_DB3F")

    Call(0, 40)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBB5")
    SetChrName("")

    #A0788
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

    #C0789
    ChrTalk(
        0x101,
        (
            "#0000F现在好像没有\x01",
            "适合供奉的料理啊。\x02\x03",

            "下次再拿过来吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_DBB5")

    Call(0, 41)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDAA")
    SetChrName("")

    #A0790
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

    #A0791
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

    #A0792
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果说是代替地藏菩萨感谢各位，未免有些僭越之嫌，\x01",
            "但我还是准备了感谢的礼品。\x01",
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

    #A0793
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '明王铃'),
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
    Jump("loc_F348")

    label("loc_DDAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF7D")
    SetChrName("")

    #A0794
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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

    #A0795
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
            "的欣喜，于是我不禁执笔写下了这封信。\x01",
            "各位的热心一直感动着我，\x01",
            "在这里，我要向各位说声谢谢。\x02",
        )
    )

    CloseMessageWindow()

    #A0796
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

    #A0797
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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
    Jump("loc_F348")

    label("loc_DF7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E13D")
    SetChrName("")

    #A0798
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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

    #A0799
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

    #A0800
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

    #A0801
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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
    Jump("loc_F348")

    label("loc_E13D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E291")
    SetChrName("")

    #A0802
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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

    #A0803
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

    #A0804
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

    #A0805
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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
    Jump("loc_F348")

    label("loc_E291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3C0")
    SetChrName("")

    #A0806
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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

    #A0807
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一直供奉着地藏菩萨的\x01",
            "各位朋友，谢谢你们。\x01",
            "能有这么热心的朋友们来参拜，\x01",
            "我想地藏菩萨一定\x01",
            "也十分高兴。\x01",
            "这是我的一点谢意，虽然只是薄礼，\x01",
            "但请务必收下。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0808
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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
    Jump("loc_F348")

    label("loc_E3C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4B7")
    SetChrName("")

    #A0809
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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

    #A0810
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

    #A0811
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
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
    Jump("loc_F348")

    label("loc_E4B7")

    SetChrName("")

    #A0812
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

    label("loc_E500")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F348")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E54B")
    MenuCmd(1, 1, "霸王面")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_E541")
    Call(0, 16)

    label("loc_E541")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E54B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E584")
    MenuCmd(1, 1, "药膳麻婆『黄龙』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_E57A")
    Call(0, 16)

    label("loc_E57A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E5B5")
    MenuCmd(1, 1, "白虎炒饭")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_E5AB")
    Call(0, 16)

    label("loc_E5AB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E5EC")
    MenuCmd(1, 1, "极品牛排『雅』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_E5E2")
    Call(0, 16)

    label("loc_E5E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E5EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E623")
    MenuCmd(1, 1, "极品炖菜『薰』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_E619")
    Call(0, 16)

    label("loc_E619")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E65A")
    MenuCmd(1, 1, "铁人锅『绚烂』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_E650")
    Call(0, 16)

    label("loc_E650")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E691")
    MenuCmd(1, 1, "贤人锅『缭乱』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_E687")
    Call(0, 16)

    label("loc_E687")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E6C8")
    MenuCmd(1, 1, "起死回生炸鱼排")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_E6BE")
    Call(0, 16)

    label("loc_E6BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E6C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E6FF")
    MenuCmd(1, 1, "黄金蛋饭『辉』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_E6F5")
    Call(0, 16)

    label("loc_E6F5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E736")
    MenuCmd(1, 1, "黄金蛋面『煌』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_E72C")
    Call(0, 16)

    label("loc_E72C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E767")
    MenuCmd(1, 1, "汉堡之王")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_E75D")
    Call(0, 16)

    label("loc_E75D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E798")
    MenuCmd(1, 1, "女王比萨")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_E78E")
    Call(0, 16)

    label("loc_E78E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E7D3")
    MenuCmd(1, 1, "行乐三明治『搭档』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_E7C9")
    Call(0, 16)

    label("loc_E7C9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E810")
    MenuCmd(1, 1, "爱心凝缩盒饭『母亲』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_E806")
    Call(0, 16)

    label("loc_E806")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E83F")
    MenuCmd(1, 1, "满月汤")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_E835")
    Call(0, 16)

    label("loc_E835")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E83F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E86E")
    MenuCmd(1, 1, "新月汤")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_E864")
    Call(0, 16)

    label("loc_E864")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8A9")
    MenuCmd(1, 1, "绝品甜点『白无垢』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_E89F")
    Call(0, 16)

    label("loc_E89F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8E2")
    MenuCmd(1, 1, "绝品甜点『黄熟』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_E8D8")
    Call(0, 16)

    label("loc_E8D8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E91B")
    MenuCmd(1, 1, "绝品甜点『粉雪』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_E911")
    Call(0, 16)

    label("loc_E911")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E954")
    MenuCmd(1, 1, "绝品甜点『浮云』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_E94A")
    Call(0, 16)

    label("loc_E94A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E985")
    MenuCmd(1, 1, "极品拿铁")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_E97B")
    Call(0, 16)

    label("loc_E97B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E9BA")
    MenuCmd(1, 1, "终极混合果汁")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_E9B0")
    Call(0, 16)

    label("loc_E9B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E9EB")
    MenuCmd(1, 1, "梦魇杀手")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_E9E1")
    Call(0, 16)

    label("loc_E9E1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EA22")
    MenuCmd(1, 1, "秘水『月光蝶』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_EA18")
    Call(0, 16)

    label("loc_EA18")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EA22")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EA61")
    Jump("loc_F343")

    label("loc_EA61")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EACC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAC2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上面『日轮』', 1)
    SetScenarioFlags(0x99, 0)

    #A0813
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天上面『日轮』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EAC2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB18")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB0E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('神仙麻婆『麒麟』', 1)
    SetScenarioFlags(0x99, 1)

    #A0814
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神仙麻婆『麒麟』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EB0E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EB18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB64")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB5A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天下一品炒饭', 1)
    SetScenarioFlags(0x99, 2)

    #A0815
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天下一品炒饭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EB5A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EB64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBB0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBA6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('极品牛排『刚』', 1)
    SetScenarioFlags(0x99, 3)

    #A0816
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '极品牛排『刚』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EBA6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EBB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBFC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBF2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('三日久煮炖菜', 1)
    SetScenarioFlags(0x99, 4)

    #A0817
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '三日久煮炖菜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EBF2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EBFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EC48")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC3E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('大地锅『烂漫』', 1)
    SetScenarioFlags(0x99, 5)

    #A0818
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '大地锅『烂漫』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EC3E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EC48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EC94")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC8A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天河锅『瑞云』', 1)
    SetScenarioFlags(0x99, 6)

    #A0819
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天河锅『瑞云』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EC8A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EC94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ECE0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECD6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('特快炸鱼『疾』', 1)
    SetScenarioFlags(0x99, 7)

    #A0820
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '特快炸鱼『疾』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_ECD6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ECE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ED2C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED22")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('丰盛蛋包饭', 1)
    SetScenarioFlags(0x9A, 0)

    #A0821
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '丰盛蛋包饭'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_ED22")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ED2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ED78")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED6E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('翠玉面『治愈』', 1)
    SetScenarioFlags(0x9A, 1)

    #A0822
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '翠玉面『治愈』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_ED6E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ED78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EDC4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDBA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('双层汉堡', 1)
    SetScenarioFlags(0x9A, 2)

    #A0823
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '双层汉堡'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EDBA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EDC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE10")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE06")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('四味奶酪比萨', 1)
    SetScenarioFlags(0x9A, 3)

    #A0824
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '四味奶酪比萨'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EE06")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EE10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE5C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE52")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('强效三明治', 1)
    SetScenarioFlags(0x9A, 4)

    #A0825
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '强效三明治'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EE52")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EE5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEA8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE9E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('真心盒饭『诚』', 1)
    SetScenarioFlags(0x9A, 5)

    #A0826
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '真心盒饭『诚』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EE9E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EEA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEF4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEEA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('辉煌汤', 1)
    SetScenarioFlags(0x9A, 6)

    #A0827
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '辉煌汤'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EEEA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EEF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EF40")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF36")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('奇幻糖果', 1)
    SetScenarioFlags(0x9A, 7)

    #A0828
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '奇幻糖果'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EF36")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EF40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EF8C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF82")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('天上甜点『夜月』', 1)
    SetScenarioFlags(0x9B, 0)

    #A0829
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '天上甜点『夜月』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EF82")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EF8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EFD8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFCE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('宝物甜点『白雪』', 1)
    SetScenarioFlags(0x9B, 1)

    #A0830
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '宝物甜点『白雪』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_EFCE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EFD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F024")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F01A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('冰凉甜点『七彩』', 1)
    SetScenarioFlags(0x9B, 2)

    #A0831
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '冰凉甜点『七彩』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_F01A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F070")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F066")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('绝品甜点『瞬动』', 1)
    SetScenarioFlags(0x9B, 3)

    #A0832
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝品甜点『瞬动』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_F066")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F0BC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('玉露『绿风』', 1)
    SetScenarioFlags(0x9B, 4)

    #A0833
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '玉露『绿风』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_F0B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F0BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F108")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0FE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('甘露『紫绀』', 1)
    SetScenarioFlags(0x9B, 5)

    #A0834
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '甘露『紫绀』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_F0FE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F154")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F14A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('黑茶『梦魇杀手』', 1)
    SetScenarioFlags(0x9B, 6)

    #A0835
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑茶『梦魇杀手』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_F14A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F1A0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F196")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber('秘水『桃源乡』', 1)
    SetScenarioFlags(0x9B, 7)

    #A0836
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '秘水『桃源乡』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "供奉出了。\x02",
        )
    )


    label("loc_F196")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F1A0")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F340")

    #C0837
    ChrTalk(
        0x101,
        (
            "#0000F这样就行了。\x01",
            "……下次有机会再拿料理来供奉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F25C")

    #C0838
    ChrTalk(
        0x102,
        (
            "#0100F总拿同样的料理来\x01",
            "未免有些失礼，\x01",
            "最好每次都供奉不同的品种呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F321")

    label("loc_F25C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2BF")

    #C0839
    ChrTalk(
        0x103,
        (
            "#0200F如果每次都供奉同一种\x01",
            "料理好像会很失礼。\x01",
            "最好每次都供奉不同的品种。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F321")

    label("loc_F2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F321")

    #C0840
    ChrTalk(
        0x104,
        (
            "#0300F每次都供奉同一种\x01",
            "料理的话好像会很失礼吧？\x01",
            "最好每次都供奉不同的品种哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F321")


    #C0841
    ChrTalk(
        0x101,
        "#0000F嗯，就这么做吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 1)

    label("loc_F340")

    SetScenarioFlags(0x2, 5)

    label("loc_F343")

    Jump("loc_E500")

    label("loc_F348")

    TalkEnd(0xFF)
    Return()

    # Function_39_D6B2 end

    def Function_40_F34C(): pass

    label("Function_40_F34C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上面『日轮』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F36F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('神仙麻婆『麒麟』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F388")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天下一品炒饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3A1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('极品牛排『刚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3BA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('三日久煮炖菜', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3D3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('大地锅『烂漫』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3EC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天河锅『瑞云』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F405")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特快炸鱼『疾』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F41E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('丰盛蛋包饭', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F437")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翠玉面『治愈』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F450")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('双层汉堡', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F469")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('四味奶酪比萨', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F482")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('强效三明治', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F49B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('真心盒饭『诚』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4B4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('辉煌汤', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4CD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('奇幻糖果', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4E6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天上甜点『夜月』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F4FF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('宝物甜点『白雪』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F518")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冰凉甜点『七彩』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F531")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('绝品甜点『瞬动』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F54A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('玉露『绿风』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F563")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('甘露『紫绀』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F57C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑茶『梦魇杀手』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F595")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('秘水『桃源乡』', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F5AE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F5AE")

    Return()

    # Function_40_F34C end

    def Function_41_F5AF(): pass

    label("Function_41_F5AF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_F5CC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_F5DF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F5DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_F5F2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F5F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_F605")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_F618")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_F62B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F62B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_F63E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_F651")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_F664")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_F677")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_F68A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_F69D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_F6B0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_F6C3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_F6D6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_F6E9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_F6FC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_F70F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_F722")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_F735")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_F748")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_F75B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_F76E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_F781")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F781")

    Return()

    # Function_41_F5AF end

    SaveToFile()

Try(main)
