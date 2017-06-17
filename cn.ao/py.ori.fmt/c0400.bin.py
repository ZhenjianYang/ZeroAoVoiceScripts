from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0400.bin",                # FileName
        "c0400",                    # MapName
        "c0400",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("c0400", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0400",                  # 0
        "珀利塞",                 # 1
        "塔普",                   # 2
        "缇乔",                   # 3
        "揽客员皮姆",             # 4
        "索菲尤",                 # 5
        "拉曼达",                 # 6
        "兔女郎",                 # 7
        "游客",                   # 8
        "游客",                   # 9
        "凯特巡警",               # 10
        "警官",                   # 11
        "警车",                   # 12
        "玛丽",                   # 13
        "车",                     # 14
        "黑色运输车",             # 15
        "中央广场",               # 16
        "西街",                   # 17
        "行政区",                 # 18
        "住宅街",                 # 19
        "欢乐街",                 # 20
        "东街",                   # 21
        "旧城区",                 # 22
        "港湾区",                 # 23
        "ＩＢＣ",                 # 24
        "站前街道",               # 25
        "后巷",                   # 26
        "乌尔斯拉间道",           # 27
        "东克洛斯贝尔街道",       # 28
        "西克洛斯贝尔街道",       # 29
        "玛因兹山道",             # 30
        "兰花塔",                 # 31
    ))

    AddCharChip((
        "chr/ch36300.itc",                   # 00
        "chr/ch24400.itc",                   # 01
        "chr/ch20400.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch34500.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch27100.itc",                   # 06
        "chr/ch33200.itc",                   # 07
        "chr/ch32300.itc",                   # 08
        "chr/ch30600.itc",                   # 09
        "chr/ch49100.itc",                   # 0A
        "chr/ch49200.itc",                   # 0B
        "chr/ch48900.itc",                   # 0C
        "chr/ch30000.itc",                   # 0D
    ))

    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   2,   0,   0,   4,   0,   14,  255,  0)
    DeclNpc(4360,    0,       -10960,  310,  261,  0x0, 0,   3,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   5,   0,   0,   2,   0,   13,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1840,   1990,    19209,   0,    385,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-3240,   1990,    19010,   0,    385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(13630,   0,       1000,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-10569,  1759,    15760,   180,  389,  0x0, 0,   13,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 40,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

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
    PlaceName(124.0, 0.0, 255.0, 0x0000, 0x0000, "兰花塔")
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

    ChipFrameInfo(1488, 0)                                       # 0

    ScpFunction((
        "Function_0_5D0",          # 00, 0
        "Function_1_680",          # 01, 1
        "Function_2_6AB",          # 02, 2
        "Function_3_838",          # 03, 3
        "Function_4_989",          # 04, 4
        "Function_5_A90",          # 05, 5
        "Function_6_F3A",          # 06, 6
        "Function_7_12B7",         # 07, 7
        "Function_8_1511",         # 08, 8
        "Function_9_1697",         # 09, 9
        "Function_10_2411",        # 0A, 10
        "Function_11_2BBD",        # 0B, 11
        "Function_12_33EE",        # 0C, 12
        "Function_13_3A56",        # 0D, 13
        "Function_14_43B4",        # 0E, 14
        "Function_15_4B3F",        # 0F, 15
        "Function_16_542E",        # 10, 16
        "Function_17_54AF",        # 11, 17
        "Function_18_5542",        # 12, 18
        "Function_19_5735",        # 13, 19
        "Function_20_5770",        # 14, 20
        "Function_21_594D",        # 15, 21
        "Function_22_59B2",        # 16, 22
        "Function_23_5D9D",        # 17, 23
        "Function_24_5E3A",        # 18, 24
        "Function_25_5E71",        # 19, 25
        "Function_26_5E9E",        # 1A, 26
        "Function_27_5ED8",        # 1B, 27
        "Function_28_5EFA",        # 1C, 28
        "Function_29_5F34",        # 1D, 29
        "Function_30_5F6F",        # 1E, 30
        "Function_31_5FC6",        # 1F, 31
        "Function_32_606C",        # 20, 32
        "Function_33_708B",        # 21, 33
        "Function_34_7220",        # 22, 34
        "Function_35_7629",        # 23, 35
        "Function_36_773A",        # 24, 36
        "Function_37_8991",        # 25, 37
        "Function_38_95D6",        # 26, 38
        "Function_39_9603",        # 27, 39
        "Function_40_A0AC",        # 28, 40
        "Function_41_A3F9",        # 29, 41
    ))


    def Function_0_5D0(): pass

    label("Function_0_5D0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_608"),
        (1, "loc_614"),
        (2, "loc_620"),
        (3, "loc_62C"),
        (4, "loc_638"),
        (5, "loc_644"),
        (6, "loc_650"),
        (SWITCH_DEFAULT, "loc_65C"),
    )


    label("loc_608")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_614")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_620")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_62C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_638")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_644")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_650")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_65C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_668")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_67F")

    Return()

    # Function_0_5D0 end

    def Function_1_680(): pass

    label("Function_1_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AA")
    OP_94(0xFE, 0xED8, 0xFFFFEC96, 0x1AE0, 0xFFFFDE22, 0x3E8)
    Sleep(300)
    Jump("Function_1_680")

    label("loc_6AA")

    Return()

    # Function_1_680 end

    def Function_2_6AB(): pass

    label("Function_2_6AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_837")
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
    Jump("Function_2_6AB")

    label("loc_837")

    Return()

    # Function_2_6AB end

    def Function_3_838(): pass

    label("Function_3_838")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_988")
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    Sleep(1500)
    Jump("Function_3_838")

    label("loc_988")

    Return()

    # Function_3_838 end

    def Function_4_989(): pass

    label("Function_4_989")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8F")
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
    Jump("Function_4_989")

    label("loc_A8F")

    Return()

    # Function_4_989 end

    def Function_5_A90(): pass

    label("Function_5_A90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6D")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_B5F")

    label("loc_B40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5F")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_B5F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCB")

    label("loc_B6D")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C2A")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFD")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_C1C")

    label("loc_BFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1C")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_C1C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCB")

    label("loc_C2A")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA3")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_CC2")

    label("loc_CA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC2")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_CC2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCB")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CE2")
    Jump("loc_E16")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CF0")
    Jump("loc_E16")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CFE")
    Jump("loc_E16")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D38")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xA, 0xC)
    SetChrPos(0xE, -25880, 160, 14850, 175)
    SetChrChipByIndex(0x8, 0xA)
    SetChrChipByIndex(0x9, 0xB)
    Jump("loc_E16")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_E16")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D60")
    TurnDirection(0x9, 0x8, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_E16")

    label("loc_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7C")
    BeginChrThread(0xD, 0, 0, 3)
    Jump("loc_E16")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D8A")
    Jump("loc_E16")

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D9D")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E16")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DB0")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E16")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DC3")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E16")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DFD")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xA, 0xC)
    SetChrPos(0xE, -25880, 160, 14850, 175)
    SetChrChipByIndex(0x8, 0xA)
    SetChrChipByIndex(0x9, 0xB)
    Jump("loc_E16")

    label("loc_DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E16")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0xD, 0, 0, 3)

    label("loc_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E47")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 13630, 0, 1000, 270)

    label("loc_E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E5B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_EBF")

    label("loc_E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E6F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 20)
    Jump("loc_EBF")

    label("loc_E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E88")
    ClearScenarioFlags(0x22, 2)
    SetChrFlags(0x11, 0x80)
    Event(0, 22)
    Jump("loc_EBF")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_E9F")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x1, 2)
    Event(0, 33)
    Jump("loc_EBF")

    label("loc_E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_EB0")
    ClearScenarioFlags(0x22, 4)
    Jump("loc_EBF")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_EBF")
    ClearScenarioFlags(0x22, 6)
    Event(0, 41)

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    Event(0, 32)

    label("loc_ED8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0E")
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F39")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_F39")

    Return()

    # Function_5_A90 end

    def Function_6_F3A(): pass

    label("Function_6_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F56")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F72")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F85")
    Jump("loc_FD4")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_FE9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 2)

    label("loc_FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FF7")
    Jump("loc_1034")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1011")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    Jump("loc_1034")

    label("loc_1011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_101F")
    Jump("loc_1034")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1034")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)

    label("loc_1034")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104D")
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_1053")

    label("loc_104D")

    SetMapObjFlags(0x6, 0x4)

    label("loc_1053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1108")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x7D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")
    OP_78(0x7, 0x13)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13630, 0, 3500, 270)
    OP_D5(0x13, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C7")
    OP_78(0x9, 0x16)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 0, 3500, 270)
    OP_D5(0x16, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_11C7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11DA")
    Jump("loc_12B6")

    label("loc_11DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11E8")
    Jump("loc_12B6")

    label("loc_11E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11F6")
    Jump("loc_12B6")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1204")
    Jump("loc_12B6")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 5)), scpexpr(EXPR_END)), "loc_121B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_121B")

    Jump("loc_12B6")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_123C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 5)), scpexpr(EXPR_END)), "loc_1237")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1237")

    Jump("loc_12B6")

    label("loc_123C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_124A")
    Jump("loc_12B6")

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1258")
    Jump("loc_12B6")

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1279")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_127E")

    label("loc_1279")

    ModifyEventFlags(1, 0, 0x80)

    label("loc_127E")

    Jump("loc_12B6")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1291")
    Jump("loc_12B6")

    label("loc_1291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_12AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 0)), scpexpr(EXPR_END)), "loc_12A8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_12A8")

    Jump("loc_12B6")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_12B6")

    label("loc_12B6")

    Return()

    # Function_6_F3A end

    def Function_7_12B7(): pass

    label("Function_7_12B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E1")
    Call(0, 34)
    Return()

    label("loc_12E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B5")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0001
    ChrTalk(
        0xFE,
        "啊，是罗伊德和各位啊……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "我听说了，特别任务支援科\x01",
            "要重新开始工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00000F是的，连同新成员一起，\x01",
            "今后还请您多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00105F话说回来，凯特巡警\x01",
            "竟然在欢乐街工作，\x01",
            "这似乎很少见啊。\x02\x03",

            "#00100F记得您一般都在\x01",
            "中央广场执勤……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "嗯，因为最近正在\x01",
            "盯防一辆导力车，\x01",
            "所以我要在这里定点监视。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "好啦，不说这些了，\x01",
            "我现在可是很期待\x01",
            "你们的活跃表现哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "让我们今后\x01",
            "一起努力加油吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 4)
    Jump("loc_150D")

    label("loc_14B5")


    #C0009
    ChrTalk(
        0xFE,
        (
            "呵呵，我听说了，特别任务支援科\x01",
            "要重新开始工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "让我们今后\x01",
            "一起努力加油吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150D")

    TalkEnd(0xFE)
    Return()

    # Function_7_12B7 end

    def Function_8_1511(): pass

    label("Function_8_1511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15A3")

    #C0011
    ChrTalk(
        0xFE,
        (
            "恐怖分子自不用说，\x01",
            "『赤色星座』和『黑月』\x01",
            "的动向也很诡异呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "不知他们会有什么图谋……\x01",
            "必须要密切关注他们的一切行动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1693")

    label("loc_15A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1617")

    #C0013
    ChrTalk(
        0xFE,
        (
            "揭幕式虽然顺利结束了，\x01",
            "但警戒工作才刚刚开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "在从今天开始的三天里，\x01",
            "一定要高度集中注意力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1693")

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1693")

    #C0015
    ChrTalk(
        0xFE,
        (
            "在通商会议的前后期间，\x01",
            "彩虹剧团会暂时停止\x01",
            "一般的对外演出。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "多亏如此，现在出入这广场的人\x01",
            "比平时有所减少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1693")

    TalkEnd(0xFE)
    Return()

    # Function_8_1511 end

    def Function_9_1697(): pass

    label("Function_9_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16CE")
    Call(0, 39)
    Return()

    label("loc_16CE")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_172B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174B")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2408")

    label("loc_174B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175F")
    Jump("loc_2408")

    label("loc_175F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2408")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_17D5")

    #C0017
    ChrTalk(
        0xC,
        "嘿嘿嘿，你们能喜欢本店的冰激凌，我很开心。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        (
            "今后也请继续\x01",
            "光顾本店哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2408")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1824")

    #C0019
    ChrTalk(
        0xC,
        "大家都好激动啊。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xC,
        (
            "热烈的气氛好像\x01",
            "要把冰激凌都融化掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2408")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_190F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CB")

    #C0021
    ChrTalk(
        0xC,
        "真担心伊莉娅小姐啊。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xC,
        (
            "虽然我除了在这里卖冰激凌之外，\x01",
            "什么忙都帮不上……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "但我一定会在这里继续做生意，\x01",
            "等待伊莉娅小姐重回剧场。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_190A")

    label("loc_18CB")


    #C0024
    ChrTalk(
        0xC,
        "冰激凌～要来个冰激凌吗～？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "冰凉又爽口，\x01",
            "非常美味哟～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190A")

    Jump("loc_2408")

    label("loc_190F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1994")

    #C0026
    ChrTalk(
        0xC,
        (
            "欢迎光临～！\x01",
            "要来个冰激凌吗～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "今天可是期待已久的\x01",
            "新版舞剧公演日～！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        "大家打起精神来吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A1E")

    label("loc_1994")


    #C0029
    ChrTalk(
        0xC,
        (
            "玛因兹那边一定不会有事的……\x01",
            "警备队的人一定能\x01",
            "想办法将事情解决！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        (
            "总之，我还会和平时一样，\x01",
            "一边贩卖冰激凌\x01",
            "一边给彩虹剧团鼓劲！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1E")

    Jump("loc_2408")

    label("loc_1A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A31")
    Jump("loc_2408")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B2F")

    #C0031
    ChrTalk(
        0xC,
        "冰激凌～要来个冰激凌吗～？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "客人，您吃过午饭了吗？\x01",
            "饭后来个冰激凌最棒了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B2A")

    #C0033
    ChrTalk(
        0x101,
        (
            "#00008F（在这里似乎可以进行\x01",
            "  美食向导的取材……）\x02\x03",

            "#00003F（但现在不是做这种事的时候，\x01",
            "  以后别忘了再过来一趟。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2A")

    Jump("loc_2408")

    label("loc_1B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BAD")

    #C0034
    ChrTalk(
        0xC,
        (
            "彩虹剧团的新版舞剧\x01",
            "终于要在后天公演了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "到时候，客人又会增加了。\x01",
            "呵呵呵，生意太好，也会手忙脚乱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2408")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C38")

    #C0036
    ChrTalk(
        0xC,
        "冰激凌～要来个冰激凌吗～？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "如果难以做出选择，\x01",
            "可以先试吃一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "请用这里的特制迷你勺\x01",
            "尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CA2")

    label("loc_1C38")


    #C0039
    ChrTalk(
        0xC,
        (
            "试吃冰激凌的服务很受好评，\x01",
            "销售额非常不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "这个月的露天店铺销售冠军\x01",
            "肯定又要归我所有了，万岁☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA2")

    Jump("loc_2408")

    label("loc_1CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D28")

    #C0041
    ChrTalk(
        0xC,
        (
            "再过不久，彩虹剧团\x01",
            "就要暂时停止演出了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "唔～面临着销售额降低的危机啊。\x01",
            "必须要想些对策了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D9E")

    label("loc_1D28")


    #C0043
    ChrTalk(
        0xC,
        (
            "唔～如果仅仅因为这种小危机\x01",
            "就将销售额第一的宝座拱手让人，\x01",
            "未免有损我首席露天店的名声啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        "必须要想些对策了。\x02",
    )

    CloseMessageWindow()

    label("loc_1D9E")

    Jump("loc_2408")

    label("loc_1DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E21")

    #C0045
    ChrTalk(
        0xFE,
        (
            "刚才那位红头发的客人\x01",
            "往住宅街那边走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "虽然他穿着很正式的西装，\x01",
            "但真是个怪人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A3")

    label("loc_1E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2043")

    #C0047
    ChrTalk(
        0xFE,
        (
            "刚才有个鲜红色头发的老兄\x01",
            "在我这里点了个\x01",
            "十层的冰激凌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "点了那么高的冰激凌，不但没有弄倒，\x01",
            "而且还能一口气吃光……\x01",
            "我还是第一次见到那样的客人呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "虽然他穿着很正式的西装，\x01",
            "但真是个怪人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0050
    ChrTalk(
        0x109,
        (
            "#10106F（罗、罗伊德警官，\x01",
            "  那个人显然就是……）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00012F请、请问……\x01",
            "那个男人去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "他大概是冰激凌吃得太猛，头有些疼，\x01",
            "抱着头向住宅街方向走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F（好……\x01",
            "  我们继续追吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1C7, 2)
    Jump("loc_21A3")

    label("loc_2043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2134")

    #C0054
    ChrTalk(
        0xC,
        "呼，上午可真是热闹啊～\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xC,
        (
            "各国首脑们并不会\x01",
            "经过这一带，\x01",
            "所以这里的人流还是和平时一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xC,
        (
            "但揭幕式结束之后，\x01",
            "马上就有一大群人围了过来，\x01",
            "生意好得不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        (
            "呵呵呵，这就是连续三个月\x01",
            "取得销售冠军的店铺的实力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21A3")

    label("loc_2134")


    #C0058
    ChrTalk(
        0xC,
        (
            "多亏大家赏光，\x01",
            "我今天大概也能提前卖光呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "所以说，\x01",
            "如果不想在卖光之后感到后悔，\x01",
            "就请趁现在赶快买吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A3")

    Jump("loc_2408")

    label("loc_21A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_22F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2281")

    #C0060
    ChrTalk(
        0xC,
        (
            "客人，您喜欢\x01",
            "牛奶冰激凌还是\x01",
            "水果冰激凌呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        (
            "顺便一提，伊莉娅小姐\x01",
            "经常来买果汁冰激凌，\x01",
            "普莉埃小姐经常买牛奶冰激凌。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xC,
        (
            "另外，莉夏小姐\x01",
            "和伊莉娅小姐一样，\x01",
            "买果汁冰激凌的时候比较多。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22F2")

    label("loc_2281")


    #C0063
    ChrTalk(
        0xC,
        (
            "至于其他人，\x01",
            "尤金先生更喜欢牛奶冰激凌，\x01",
            "缇奥多尔先生……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "……缇奥多尔先生好像讨厌甜食，\x01",
            "从来都不买呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F2")

    Jump("loc_2408")

    label("loc_22F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2305")
    Jump("loc_2408")

    label("loc_2305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2391")

    #C0065
    ChrTalk(
        0xC,
        "冰激凌～要来个冰激凌吗～？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "我这里的冰激凌\x01",
            "品种很丰富哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "多尝试几次，\x01",
            "寻找出自己最喜欢的\x01",
            "味道吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2408")

    label("loc_2391")


    #C0068
    ChrTalk(
        0xC,
        (
            "如果愿意，\x01",
            "也可以自由\x01",
            "混合多种口味的冰激凌哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "不过，如果不听取我的建议，\x01",
            "最后配得很难吃，我可是不负责任的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2408")

    Jump("loc_16DB")

    label("loc_240D")

    TalkEnd(0xFE)
    Return()

    # Function_9_1697 end

    def Function_10_2411(): pass

    label("Function_10_2411")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_247E")

    #C0070
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "情况好像变得很不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "总之，只要别让我\x01",
            "遇到什么麻烦事就谢天谢地了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_247E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24E6")

    #C0072
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，你们几个，\x01",
            "要不要到我们店里喝一杯？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "那场慈善宴会\x01",
            "让我学到了很多东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_24E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2565")

    #C0074
    ChrTalk(
        0xFE,
        (
            "不知是怎么回事～\x01",
            "最近好像总是发生危险的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "真是的～这样下去，\x01",
            "连纠纷不断的后巷\x01",
            "都让人觉得很可爱了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_2565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2573")
    Jump("loc_2BB9")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2631")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E7")

    #C0076
    ChrTalk(
        0xFE,
        (
            "呼，去哪里能找到\x01",
            "又有钱又好骗的\x01",
            "客人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "哦～嘿嘿嘿，一不小心\x01",
            "就吐露出心声了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_262C")

    label("loc_25E7")


    #C0078
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，一不小心\x01",
            "就吐露出心声了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "这也是我心情放松的证据。\x02",
    )

    CloseMessageWindow()

    label("loc_262C")

    Jump("loc_2BB9")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2680")

    #C0080
    ChrTalk(
        0xFE,
        (
            "好了～今天也要\x01",
            "加油工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "让我招待大家前往梦幻世界吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_2680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275D")

    #C0082
    ChrTalk(
        0xFE,
        (
            "哎呀呀，彩虹剧团总有\x01",
            "很棒的新人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "将在这次的公演中首次登台，\x01",
            "扮演新舞姬的那个新人是叫修利吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "距离那个叫莉夏的新人出道，\x01",
            "才刚过去不到一年呢。\x01",
            "真希望能把漂亮女孩分几个给我们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27B7")

    label("loc_275D")


    #C0085
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "彩虹剧团的演员里\x01",
            "真是有不少可爱的女孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "要是能分给我们几个就好了。\x02",
    )

    CloseMessageWindow()

    label("loc_27B7")

    Jump("loc_2BB9")

    label("loc_27BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2844")

    #C0087
    ChrTalk(
        0xFE,
        (
            "通商会议对我们\x01",
            "这样的人来说，\x01",
            "也没什么有趣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "最近这一阵子，\x01",
            "出手豪爽的议员比以前少多了，\x01",
            "我们的生意相当惨淡。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_2844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28C0")

    #C0089
    ChrTalk(
        0xFE,
        (
            "今天的行人虽然很多，\x01",
            "但全都是市民，游客很少。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "虽然刚刚过去没多久，\x01",
            "但我已经开始怀念创立纪念庆典了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_28C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2916")

    #C0091
    ChrTalk(
        0xFE,
        (
            "啊，那些警察的目光\x01",
            "好锐利啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "这样一来，可就没法\x01",
            "强行拉客了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB9")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2924")
    Jump("loc_2BB9")

    label("loc_2924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B71")

    #C0093
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，你们几位，\x01",
            "如果有空的话，\x01",
            "来我们店里喝几杯如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "如果四人一起，\x01",
            "可以打个团体折哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        "#10305F嘿，那大概要多少钱呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E2")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_29E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A05")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2A05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A28")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2A28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A48")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_2A48")

    Sleep(1000)

    #C0096
    ChrTalk(
        0xFE,
        (
            "这个嘛，我们的正常价格\x01",
            "是每位五百米拉……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0097
    ChrTalk(
        0x109,
        "#10101F瓦、瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00106F那个，我们正在工作中，\x01",
            "不方便去喝酒……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "嗯……？\x01",
            "什么啊，原来只是在耍我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "那就一边去……\x01",
            "不要妨碍我做生意。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        "#00006F真、真对不住……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 2)
    Jump("loc_2BB9")

    label("loc_2B71")


    #C0102
    ChrTalk(
        0xFE,
        (
            "啊，想耍人\x01",
            "请不要找我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "如果太过分，\x01",
            "哥哥我可是会生气的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB9")

    TalkEnd(0xFE)
    Return()

    # Function_10_2411 end

    def Function_11_2BBD(): pass

    label("Function_11_2BBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C48")

    #C0104
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐身负重伤，\x01",
            "一定是帝国做的好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "所以我……绝对不会原谅帝国………！\x01",
            "今后再也不会对他们唯命是从了！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EA")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB6")

    #C0106
    ChrTalk(
        0xFE,
        "…………………………………\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "……伊莉娅小姐………\x01",
            "为何会遭遇这种事情………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CF3")

    label("loc_2CB6")


    #C0108
    ChrTalk(
        0xFE,
        (
            "我绝对……不能原谅那些犯人……\x01",
            "……绝对不能原谅………！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF3")

    Jump("loc_33EA")

    label("loc_2CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D87")

    #C0109
    ChrTalk(
        0xFE,
        (
            "终于等到了……今天傍晚，\x01",
            "新版舞剧就要公演了……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "伊·莉·娅·小·姐～～！\x01",
            "珀利塞在此祈祷，\x01",
            "祝您表演大获成功～～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EA")

    label("loc_2D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E21")

    #C0111
    ChrTalk(
        0xFE,
        (
            "明天……明天……\x01",
            "这一天终于就快到了！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐，虽然我无法\x01",
            "在公演第一天去观赏……\x01",
            "但今天晚上一定会兴奋得无法入睡！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E75")

    label("loc_2E21")


    #C0113
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐，虽然我无法\x01",
            "在公演第一天去观赏……\x01",
            "但今天晚上一定会兴奋得无法入睡！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E75")

    Jump("loc_33EA")

    label("loc_2E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EC2")

    #C0114
    ChrTalk(
        0xFE,
        "伊莉娅小姐！伊莉娅小姐～！！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "练习请加油啊～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33EA")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F62")

    #C0116
    ChrTalk(
        0xFE,
        (
            "后天……\x01",
            "终于快等到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐和修利\x01",
            "究竟是怎么认识的呢……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "唔唔唔……嗯嗯嗯……\x01",
            "光是想象一下就很难平静了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FC8")

    label("loc_2F62")


    #C0119
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐和修利\x01",
            "究竟是怎么认识的呢……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "唔唔唔……嗯嗯嗯……\x01",
            "光是想象一下就很难平静了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC8")

    Jump("loc_33EA")

    label("loc_2FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_302D")

    #C0121
    ChrTalk(
        0xFE,
        (
            "大后天……\x01",
            "终于快要到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "新版舞剧的公演日……\x01",
            "我已经等待得太久了！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EA")

    label("loc_302D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EB")

    #C0123
    ChrTalk(
        0xFE,
        (
            "就算停止公演，伊莉娅小姐\x01",
            "应该也会来剧场练习……！\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "也就是说，这反而是拍下\x01",
            "伊莉娅小姐照片的大好机会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "所以我在剧团停止演出的期间\x01",
            "也会继续来这里！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_314F")

    label("loc_30EB")


    #C0126
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐在这段时间\x01",
            "应该也会来剧场练习……！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "所以我在剧团停止演出的期间\x01",
            "也会继续来这里！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_314F")

    Jump("loc_33EA")

    label("loc_3154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31C6")

    #C0128
    ChrTalk(
        0xFE,
        (
            "今天晚上，各国首脑\x01",
            "好像要来观赏彩虹剧团的演出呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "呜呜呜……好狡猾～！\x01",
            "我也想进去看啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EA")

    label("loc_31C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328B")

    #C0130
    ChrTalk(
        0xFE,
        "#4S耶……！！#3S\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "好不容易才勉强买到了\x01",
            "新版舞剧公演一周后的Ｂ席票……\x01",
            "虽然很兴奋………但有些不甘心呢！！\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "不过公演初日的票\x01",
            "抢得实在太凶，\x01",
            "根本就买不到啊！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_331F")

    label("loc_328B")


    #C0133
    ChrTalk(
        0xFE,
        (
            "好不容易才勉强买到了\x01",
            "新版舞剧公演一周后的Ｂ席票……\x01",
            "虽然很兴奋………但有些不甘心呢！！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "不过公演初日的票\x01",
            "抢得实在太凶，\x01",
            "根本就买不到啊！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331F")

    Jump("loc_33EA")

    label("loc_3324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3372")

    #C0135
    ChrTalk(
        0xFE,
        "伊·莉·娅·小·姐～～！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "我是不会被这区区雨水打退的！\x02",
    )

    CloseMessageWindow()
    Jump("loc_33EA")

    label("loc_3372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33EA")

    #C0137
    ChrTalk(
        0xFE,
        (
            "最近总是看到\x01",
            "伊莉娅小姐和一个\x01",
            "新来的女孩在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "呜呜，那孩子是谁啊……\x01",
            "她究竟是伊莉娅小姐的什么人？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EA")

    TalkEnd(0xFE)
    Return()

    # Function_11_2BBD end

    def Function_12_33EE(): pass

    label("Function_12_33EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3436")

    #C0139
    ChrTalk(
        0xFE,
        (
            "噢噢噢噢……\x01",
            "说得好啊！总统！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "我们自由了！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_3436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349E")

    #C0141
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐……\x01",
            "好像仍然没有苏醒。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……可恶，怎么会发生这种事，\x01",
            "真是莫名其妙啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_349E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3513")

    #C0143
    ChrTalk(
        0xFE,
        (
            "好～今天就呐喊声援\x01",
            "一整天吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "#4S彩虹剧团的各位～！\x01",
            "我们这些支持者\x01",
            "会永远关注你们的～！！#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3577")

    #C0145
    ChrTalk(
        0xFE,
        (
            "嘿嘿，大家现在一定\x01",
            "正在里面彩排。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "#4S彩虹剧团万岁～！\x01",
            "新版舞剧万岁～！！#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_3577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_35E9")

    #C0147
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐、莉夏小姐、\x01",
            "修利，还有普莉埃小姐\x01",
            "和塞利娜小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "#4S我最喜欢你们大家了～！#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_35E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3638")

    #C0149
    ChrTalk(
        0xFE,
        (
            "喂喂，珀利塞，你的口水都流出来了……\x01",
            "而且你的表情好恐怖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_3638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36B8")

    #C0150
    ChrTalk(
        0xFE,
        (
            "由伊莉娅小姐、莉夏小姐，\x01",
            "还有修利来扮演的\x01",
            "三位舞姬吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "这次终于如愿以偿地\x01",
            "买到了票……\x01",
            "真是太期待了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_36B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3748")

    #C0152
    ChrTalk(
        0xFE,
        (
            "为了准备新版舞剧的演出，\x01",
            "彩虹剧团再过不久\x01",
            "就要暂停公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "在那期间，他们将会在\x01",
            "剧场里秘密练习……\x01",
            "我真是想看得要死啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_3748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3788")

    #C0154
    ChrTalk(
        0xFE,
        (
            "是啊～\x01",
            "虽说是国家首脑，\x01",
            "但这待遇也太优厚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_3788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_381A")

    #C0155
    ChrTalk(
        0xFE,
        (
            "珀利塞那家伙，\x01",
            "说什么好不容易才买到票，\x01",
            "其实还不是我转让给她的。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "嘿嘿，算啦，\x01",
            "毕竟是志趣相投的伙伴，\x01",
            "互相帮助也是应该的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_381A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38A1")

    #C0157
    ChrTalk(
        0xFE,
        (
            "嘿嘿，在这种时候，\x01",
            "正是与其他支持者\x01",
            "显现出差距的好机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "#4S伊莉娅小姐～莉夏小姐～！\x01",
            "我最喜欢你们了～～！！#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A52")

    label("loc_38A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3951")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    #C0159
    ChrTalk(
        0xFE,
        "哦，你们是……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "我以前曾见你们出入\x01",
            "剧场很多次，\x01",
            "你们好像是警察吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "当警察可真好啊～\x01",
            "可以在工作中进入剧场～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A52")

    label("loc_3951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EC")

    #C0162
    ChrTalk(
        0xFE,
        (
            "不然我也去警察学校学习，\x01",
            "争取当个警官好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "那样就能以巡逻为借口，\x01",
            "每天都跑进彩虹剧团里……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#00006F（哎，那是不行的啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3A52")

    label("loc_39EC")


    #C0165
    ChrTalk(
        0xFE,
        (
            "不然我也去警察学校学习，\x01",
            "争取当个警官好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "那样就能以巡逻为借口，\x01",
            "每天都跑进彩虹剧团里……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A52")

    TalkEnd(0xFE)
    Return()

    # Function_12_33EE end

    def Function_13_3A56(): pass

    label("Function_13_3A56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B03")

    #C0167
    ChrTalk(
        0xFE,
        (
            "虽说只是传闻，\x01",
            "但没想到两大国竟能\x01",
            "做出如此卑劣的事情……！\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "我发自内心地赞同总统的主张。\x01",
            "如果现在不下定决心站起来，\x01",
            "同样的悲剧在今后只会不断重演！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B0")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3B83")

    #C0169
    ChrTalk(
        0xFE,
        (
            "我原本预定\x01",
            "今天去观赏\x01",
            "彩虹剧团表演的……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "但既然发生了那样的事情，\x01",
            "也没办法了……\x01",
            "伊莉娅小姐不要紧吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B0")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3BDD")

    #C0171
    ChrTalk(
        0xFE,
        (
            "玛因兹的事件……\x01",
            "真是好可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "希望警备队的人\x01",
            "能尽早将事情解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B0")

    label("loc_3BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BEB")
    Jump("loc_43B0")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C4F")

    #C0173
    ChrTalk(
        0xFE,
        (
            "总觉得中央广场那边\x01",
            "好像很吵闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "也不知道是怎么回事，\x01",
            "莫非是发生事故了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B0")

    label("loc_3C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE3")

    #C0175
    ChrTalk(
        0xFE,
        (
            "新版舞剧终于要在\x01",
            "后天公演了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "虽然买不到公演\x01",
            "第一天的门票，\x01",
            "但我准备下周去看。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "呵呵呵，心情真是激动啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3D20")

    label("loc_3CE3")


    #C0178
    ChrTalk(
        0xFE,
        (
            "我准备下周去看\x01",
            "新版舞剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "呵呵呵，心情真是激动啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3D20")

    Jump("loc_43B0")

    label("loc_3D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    #C0180
    ChrTalk(
        0xFE,
        (
            "啊，瓦吉，\x01",
            "之前真是谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "呵呵，多亏有你，\x01",
            "让我享受了一段梦幻般的时光呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，彼此彼此，\x01",
            "听你这么说，我真是很开心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003F（瓦吉这家伙……\x01",
            "  真会见缝插针，什么时候\x01",
            "  又去做了公关工作啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3E6B")

    label("loc_3E3F")

    TurnDirection(0xFE, 0x105, 0)

    #C0184
    ChrTalk(
        0xFE,
        (
            "呵呵，瓦吉，\x01",
            "下次再去找你玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6B")

    Jump("loc_43B0")

    label("loc_3E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2F")

    #C0185
    ChrTalk(
        0xFE,
        (
            "突然想起来一件事，\x01",
            "哈尔特曼前议长\x01",
            "现在还在拘留所吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "即使是那种重量级的大人物，\x01",
            "才过了这么一阵子，\x01",
            "就从大家的讨论话题中彻底消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "人可真是薄情啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3F95")

    label("loc_3F2F")


    #C0188
    ChrTalk(
        0xFE,
        (
            "即使是哈尔特曼前议长那种大人物，\x01",
            "也很快就从公众的\x01",
            "讨论话题中彻底消失了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        "人可真是薄情啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3F95")

    Jump("loc_43B0")

    label("loc_3F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4004")

    #C0190
    ChrTalk(
        0xFE,
        (
            "兰花塔……\x01",
            "终于揭开帷幕了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "呵呵，只是观赏建筑就会如此兴奋，\x01",
            "这还真是第一次呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B0")

    label("loc_4004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40A0")

    #C0192
    ChrTalk(
        0xFE,
        (
            "听说高级俱乐部『诺艾·布朗』\x01",
            "最近已经装修完毕，重新开始营业了，\x01",
            "真想去一次啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "不过，那个地方是\x01",
            "纯会员制的……\x01",
            "有没有人能带我去呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B0")

    label("loc_40A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40AE")
    Jump("loc_43B0")

    label("loc_40AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_43B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4339")
    TurnDirection(0xFE, 0x105, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0194
    ChrTalk(
        0xFE,
        (
            "啊，你……\x01",
            "莫非是男公关瓦吉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x105,
        "#10305F哦，你认识我吗？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "之前就听说这一带\x01",
            "有个非常英俊的\x01",
            "男公关。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "呵呵，果然如传闻所说，真是个漂亮的孩子呢。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，多谢夸奖。\x02\x03",

            "#10302F如果有兴趣，就去店里坐坐吧，\x01",
            "我们到时候在那里慢慢聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "呵呵，一定会去的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4216")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4216")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_423C")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_423C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4262")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4262")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4288")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4288")

    Sleep(1000)

    #C0200
    ChrTalk(
        0x102,
        (
            "#00106F（不、不愧是瓦吉，\x01",
            "  真是很出名啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00006F（呼，竟然在我们面前\x01",
            "  毫无顾忌地商定这种生意……）\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x109,
        (
            "#10101F（真是的……\x01",
            "  稍后可得严重警告他啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 1)
    Jump("loc_43B0")

    label("loc_4339")


    #C0203
    ChrTalk(
        0xFE,
        (
            "之前就听说这一带\x01",
            "有个非常英俊的男公关。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "呵呵，等下次有机会，\x01",
            "一定去店里找你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x105,
        "#10302F呵呵，我很期待。\x02",
    )

    CloseMessageWindow()

    label("loc_43B0")

    TalkEnd(0xFE)
    Return()

    # Function_13_3A56 end

    def Function_14_43B4(): pass

    label("Function_14_43B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4429")

    #C0206
    ChrTalk(
        0xFE,
        (
            "『克洛斯贝尔独立国』吗……\x01",
            "嘿嘿，听起来真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "这样的话，我们就不是市民，\x01",
            "而是国民了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3B")

    label("loc_4429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_451B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F6")

    #C0208
    ChrTalk(
        0xFE,
        (
            "虽然最近已经渐渐平复下来了，\x01",
            "但自从那起袭击事件发生之后，\x01",
            "整个城市的气氛就一直很阴沉。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "不过，我的想法是这样的。\x01",
            "正是在这种时候，才更应该\x01",
            "多出来玩，让城市经济恢复活力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4516")

    label("loc_44F6")


    #C0210
    ChrTalk(
        0xFE,
        "所以说，今天也要玩个痛快～\x02",
    )

    CloseMessageWindow()

    label("loc_4516")

    Jump("loc_4B3B")

    label("loc_451B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A4")

    #C0211
    ChrTalk(
        0xFE,
        (
            "虽说玛因兹那边发生了严重的事情，\x01",
            "但我们就算惊慌也没用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "所以我还要像往常一样，\x01",
            "在这欢乐街玩个够。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4602")

    label("loc_45A4")


    #C0213
    ChrTalk(
        0xFE,
        (
            "对了，今天是彩虹剧团\x01",
            "新版舞剧的公演日啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "嘿嘿，真羡慕那些能在\x01",
            "第一天观赏的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4602")

    Jump("loc_4B3B")

    label("loc_4607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4669")

    #C0215
    ChrTalk(
        0xFE,
        (
            "好了～今天要去\x01",
            "哪家酒吧呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "嘿嘿，在这种日子，\x01",
            "安静地独自喝酒也不坏啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3B")

    label("loc_4669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46F6")

    #C0217
    ChrTalk(
        0xFE,
        "之前在巴鲁卡玩了玩老虎机……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "呼～但手气完全不行啊。\x01",
            "看来今天的运气很差。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "在这种时候，是不是应该赶快回家睡觉呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B3B")

    label("loc_46F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_476C")

    #C0220
    ChrTalk(
        0xFE,
        (
            "巴鲁卡的老虎机\x01",
            "有没有必胜玩法呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "总觉得应该会有经常能吐出代币的机器和\x01",
            "基本就不出的机器吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3B")

    label("loc_476C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_482C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D8")

    #C0222
    ChrTalk(
        0xFE,
        "好，今天也要玩个痛快～\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "我看看今天带了多少钱……\x01",
            "不好，好像快不够了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4827")

    label("loc_47D8")


    #C0224
    ChrTalk(
        0xFE,
        "因为最近一直输钱呢～\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "没办法，看来又得说点好话\x01",
            "求求父母给点零花钱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4827")

    Jump("loc_4B3B")

    label("loc_482C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_48AC")

    #C0226
    ChrTalk(
        0xFE,
        (
            "彩虹剧团在表演完\x01",
            "下一场演出之后，\x01",
            "将会暂时停止公演。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "据说是要正式开始\x01",
            "准备新版舞剧了，\x01",
            "真是让人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3B")

    label("loc_48AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4979")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4939")

    #C0228
    ChrTalk(
        0xFE,
        (
            "虽然无法在近距离下观看，\x01",
            "但我也算是见证了揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "兰花塔真是惊人啊。\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "这个城市实在是很富裕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4974")

    label("loc_4939")


    #C0231
    ChrTalk(
        0xFE,
        "兰花塔真是惊人啊。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "这个城市实在是很富裕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4974")

    Jump("loc_4B3B")

    label("loc_4979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1C")

    #C0233
    ChrTalk(
        0xFE,
        (
            "唉，到处都有\x01",
            "警察啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "那个通商会议好像\x01",
            "要在明天开始吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "我虽然明白那场会议的重要性，\x01",
            "但真希望他们不要在\x01",
            "这一带转来转去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4A76")

    label("loc_4A1C")


    #C0236
    ChrTalk(
        0xFE,
        (
            "当然，我并没有\x01",
            "做过什么坏事哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "只不过，如果有警察在附近，\x01",
            "玩起来总是不太自在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A76")

    Jump("loc_4B3B")

    label("loc_4A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4AE4")

    #C0238
    ChrTalk(
        0xFE,
        (
            "嘿嘿，如果碰上\x01",
            "雨天就回家，\x01",
            "就不能算是真正的玩乐达人啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "好，今天也要\x01",
            "尽情狂欢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3B")

    label("loc_4AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4B3B")

    #C0240
    ChrTalk(
        0xFE,
        "好，今天也要玩个痛快～\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "首先要找家赌场\x01",
            "玩玩老虎机，\x01",
            "试试今天的运气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3B")

    TalkEnd(0xFE)
    Return()

    # Function_14_43B4 end

    def Function_15_4B3F(): pass

    label("Function_15_4B3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BAF")

    #C0242
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "『巴鲁卡』今天也\x01",
            "正常营业哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "大家快进来玩吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4BE8")

    label("loc_4BAF")


    #C0245
    ChrTalk(
        0xFE,
        (
            "『巴鲁卡』今天也\x01",
            "正常营业哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "大家快进来玩吧～\x02",
    )

    CloseMessageWindow()

    label("loc_4BE8")

    Jump("loc_542A")

    label("loc_4BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C3A")

    #C0247
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        "进去玩个痛快，给自己注入能量吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_542A")

    label("loc_4C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB4")

    #C0249
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "呵呵，终于到了\x01",
            "新版舞剧的\x01",
            "公演日啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        "大家一定要打起精神哦～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4CFA")

    label("loc_4CB4")


    #C0252
    ChrTalk(
        0xFE,
        (
            "呵呵，终于到了\x01",
            "新版舞剧的\x01",
            "公演日啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "大家一定要打起精神哦～\x02",
    )

    CloseMessageWindow()

    label("loc_4CFA")

    Jump("loc_542A")

    label("loc_4CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D4F")

    #C0254
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "如果愿意，就到我们\x01",
            "的店里避避雨吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542A")

    label("loc_4D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4DA3")

    #C0256
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "呵呵，如果想给我小费，\x01",
            "随时都欢迎哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542A")

    label("loc_4DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4DEF")

    #C0258
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "呵呵，今天也有很多\x01",
            "优惠活动哦⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542A")

    label("loc_4DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8B")

    #C0260
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "其实我在日常生活中\x01",
            "并不会一直穿着这种服装哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "呵呵，但在男朋友提出要求时，\x01",
            "我也会换上它的～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4EF3")

    label("loc_4E8B")


    #C0263
    ChrTalk(
        0xFE,
        (
            "其实我在日常生活中\x01",
            "并不会一直穿着这种服装哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "呵呵，但在男朋友提出要求时，\x01",
            "我也会换上它的～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF3")

    Jump("loc_542A")

    label("loc_4EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F76")

    #C0265
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "今天的阳光也很耀眼啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "我又要被晒黑了～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4FC0")

    label("loc_4F76")


    #C0268
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "今天的阳光也很耀眼啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "这样的话，\x01",
            "我又要被晒黑了～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC0")

    Jump("loc_542A")

    label("loc_4FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_50B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5056")

    #C0270
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "听说各国首脑今天\x01",
            "都会去彩虹剧团\x01",
            "观看表演～\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "呵呵，他们会不会\x01",
            "顺便来我们这里玩玩呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_50B3")

    label("loc_5056")


    #C0273
    ChrTalk(
        0xFE,
        (
            "听说各国首脑今天\x01",
            "都会去彩虹剧团\x01",
            "观看表演～\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "呵呵，他们会不会\x01",
            "顺便来我们这里玩玩呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50B3")

    Jump("loc_542A")

    label("loc_50B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_52B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5269")

    #C0275
    ChrTalk(
        0xFE,
        (
            "啊，这不是兰迪吗！\x01",
            "好长时间没看见你了，\x01",
            "到底去干什么了～？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#00304F哦哦，抱歉，\x01",
            "最近有点事情。\x02\x03",

            "#00300F等以后有空，我请你喝一杯，这次就原谅我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "呵呵呵，少来这套，\x01",
            "我才不会上你的当呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "如果认识到自己的错误了，\x01",
            "就去我们店里输点钱吧～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#00309F哈哈，你还是这么会做生意啊。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x109,
        (
            "#10100F（兰迪前辈……\x01",
            "  很习惯这种地方呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#00000F（嗯，对兰迪来说，\x01",
            "  这里就像是自己的家一样。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 4)
    Jump("loc_52AD")

    label("loc_5269")


    #C0282
    ChrTalk(
        0xFE,
        (
            "兰迪先生，\x01",
            "如果你认识到自己的错误了，\x01",
            "就去我们店里输点钱吧～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52AD")

    Jump("loc_542A")

    label("loc_52B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5311")

    #C0283
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "在这种日子，\x01",
            "建议大家进本店\x01",
            "痛痛快快地玩个够哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542A")

    label("loc_5311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_542A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53AD")

    #C0285
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "哎？你问有没有红头发\x01",
            "的男人来过？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "你们是他的朋友吗～？\x01",
            "那个人刚刚\x01",
            "进店哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_53EB")

    label("loc_53AD")


    #C0288
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "那个红头发的男人\x01",
            "刚刚进店哦～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53EB")

    Jump("loc_542A")

    label("loc_53F0")


    #C0290
    ChrTalk(
        0xFE,
        "Hello，欢迎光临～☆\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "呵呵，今天也要\x01",
            "玩尽兴哦～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_542A")

    TalkEnd(0xFE)
    Return()

    # Function_15_4B3F end

    def Function_16_542E(): pass

    label("Function_16_542E")

    TalkBegin(0xFE)

    #C0292
    ChrTalk(
        0xFE,
        (
            "这里就是那个\x01",
            "著名的『彩虹剧团』……\x01",
            "呵呵，终于来到这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "我之前就已经\x01",
            "买好了票，\x01",
            "接下来就只需等待演出开始了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_542E end

    def Function_17_54AF(): pass

    label("Function_17_54AF")

    TalkBegin(0xFE)

    #C0294
    ChrTalk(
        0xFE,
        (
            "被很多观众视为最高杰作的\x01",
            "『金之太阳、银之月』啊……\x01",
            "真是太期待了。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "不过，好像要到演出\x01",
            "快开始的时候才能入场，\x01",
            "到哪里打发时间好呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_54AF end

    def Function_18_5542(): pass

    label("Function_18_5542")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x5, 0x13)
    OP_49()
    SetChrPos(0x13, 13050, 0, -18750, 225)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B7")
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xB, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 9390, 0, -4600, 180)
    EndChrThread(0xD, 0xFF)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, 11820, 0, -12540, 270)

    def lambda_566D():
        OP_96(0xFE, 0xFFFFE0D4, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_566D)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 14040, 0, 11290, 90)

    def lambda_56A2():
        OP_95(0xFE, 37920, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_56A2)

    label("loc_56B7")

    FadeToBright(1000, 0)
    Sound(468, 2, 100, 0)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x13, 3, 0, 19)
    OP_68(-8900, 2000, 2110, 0)
    MoveCamera(60, 6, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(30000, 0)
    OP_68(-8900, 4000, 2110, 7500)
    OP_6F(0x79)
    OP_0D()
    StopSound(468, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_5542 end

    def Function_19_5735(): pass

    label("Function_19_5735")

    SetChrPos(0xFE, 13050, 0, -18750, 225)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -8000, 0, -600)
    OP_9F(0x1, -24250, 0, 8350)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_19_5735 end

    def Function_20_5770(): pass

    label("Function_20_5770")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x5, 0x13)
    OP_49()
    SetChrPos(0x13, -24950, 0, 8900, 0)
    OP_D5(0x13, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xBB, 0x9B, 0xB9, 0x0, 0x0)
    OP_11(0xBB, 0xA1, 0xBF, 0x54, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58CB")
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xB, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 10750, 0, -5630, 270)
    EndChrThread(0xD, 0xFF)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, 2520, 0, -5710, 90)

    def lambda_589B():
        OP_96(0xFE, 0x3F15, 0x0, 0xFFFFAF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_589B)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, -3100, 1760, 9570, 180)

    label("loc_58CB")

    FadeToBright(1000, 0)
    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x13, 3, 0, 21)
    OP_68(-8900, 8000, 2110, 0)
    MoveCamera(60, 6, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(30000, 0)
    OP_68(-8900, 4000, 2110, 10000)
    Sleep(7000)
    StopSound(468, 2000, 100)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5770 end

    def Function_21_594D(): pass

    label("Function_21_594D")

    SetChrPos(0xFE, -24950, 0, 8900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -10800, 0, 1900)
    OP_9F(0x1, 4150, 0, -2750)
    OP_9F(0x1, 10500, 0, 5450)
    OP_9F(0x1, 22600, 0, 11200)
    OP_9F(0x1, 38350, 0, 11900)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_21_594D end

    def Function_22_59B2(): pass

    label("Function_22_59B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x102, -2570, 50, -5500, 225)
    SetChrPos(0x109, -2570, 50, -5500, 225)
    SetChrPos(0x104, -2570, 50, -5500, 225)
    SetChrPos(0x101, -1120, 50, -3330, 45)
    SetChrPos(0x105, -1120, 50, -3330, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x5, 0x13)
    OP_49()
    SetChrPos(0x13, -35000, 0, 11000, 0)
    OP_D5(0x13, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x13, 3, 0, 23)
    OP_68(-18410, 3350, 8480, 0)
    MoveCamera(9, 14, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(22130, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1860, 2550, -4600, 7000)
    MoveCamera(31, 21, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(18000, 7000)
    Sleep(2500)
    Sound(459, 0, 80, 0)
    OP_6F(0x79)
    OP_68(290, 650, -5500, 0)
    MoveCamera(71, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14500, 0)
    Fade(500)
    OP_0D()
    WaitChrThread(0x13, 3)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    MoveCamera(78, 20, 0, 3000)
    SetCameraDistance(13090, 3000)
    Sleep(1000)
    BeginChrThread(0x104, 0, 0, 24)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    #C0296
    ChrTalk(
        0x104,
        "#00311F#5P………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 0, 0, 25)
    BeginChrThread(0x101, 0, 0, 26)
    BeginChrThread(0x102, 0, 0, 28)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    #C0297
    ChrTalk(
        0x101,
        "#00007F#5P兰迪……！\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        "#00101F#6P我们追！\x02",
    )

    CloseMessageWindow()
    MoveCamera(90, 10, 0, 5500)
    BeginChrThread(0x105, 0, 0, 30)
    BeginChrThread(0x109, 0, 0, 31)
    BeginChrThread(0x101, 0, 0, 27)
    BeginChrThread(0x102, 0, 0, 29)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(800)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "爆灵能源槽解除。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※当各章的高潮剧情结束之后，\x01",
            "　爆灵能源槽就会暂时无法使用。\x02\x03",

            "※但当下一章的剧情进入高潮部分时，\x01",
            "　爆灵能源槽便会重新开启。\x02\x03",

            "※爆灵能源槽开启后，在进入第一场\x01",
            "　战斗时，战斗画面右上方的爆灵能源槽\x01",
            "　就会再次出现，请注意。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x104, 0x0)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x3, 0xFF)
    SetScenarioFlags(0x12A, 4)
    OP_29(0xA2, 0x1, 0x4)
    OP_C9(0x0, 0x1000)
    EventEnd(0x5)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_59B2 end

    def Function_23_5D9D(): pass

    label("Function_23_5D9D")

    SetChrPos(0xFE, -35000, 0, 11000, 0)
    Sound(458, 0, 80, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23250, 0, 7500)
    OP_9F(0x1, -8000, 0, 0)
    OP_9F(0x1, -4500, 0, -2500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    Sound(492, 0, 60, 0)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x8)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x1)
    Return()

    # Function_23_5D9D end

    def Function_24_5E3A(): pass

    label("Function_24_5E3A")


    def lambda_5E3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E3F)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_5E3A end

    def Function_25_5E71(): pass

    label("Function_25_5E71")

    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x162, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_25_5E71 end

    def Function_26_5E9E(): pass

    label("Function_26_5E9E")

    Sleep(200)

    def lambda_5EA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5EA6)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x2D, 0xABE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_5E9E end

    def Function_27_5ED8(): pass

    label("Function_27_5ED8")

    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1770, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_27_5ED8 end

    def Function_28_5EFA(): pass

    label("Function_28_5EFA")

    Sleep(800)

    def lambda_5F02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5F02)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x159, 0x190, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_28_5EFA end

    def Function_29_5F34(): pass

    label("Function_29_5F34")

    Sleep(100)
    OP_93(0xFE, 0x7D, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_29_5F34 end

    def Function_30_5F6F(): pass

    label("Function_30_5F6F")

    Sleep(100)

    def lambda_5F77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5F77)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x1E, 0x1F4, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_30_5F6F end

    def Function_31_5FC6(): pass

    label("Function_31_5FC6")

    Sleep(500)

    def lambda_5FCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5FCE)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0x5, 0x1F, 0x3C, 0x0, 0x0)
    Sleep(600)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x19)
    Sleep(300)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x7D, 0x1F4)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_31_5FC6 end

    def Function_32_606C(): pass

    label("Function_32_606C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-27000, 1100, 12100, 0)
    MoveCamera(30, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18200, 0)
    SetChrPos(0x101, -27000, 0, 13400, 180)
    SetChrPos(0x102, -27600, 0, 11200, 0)
    SetChrPos(0x103, -28300, 0, 12100, 90)
    SetChrPos(0x109, -25700, 0, 12500, 270)
    SetChrPos(0x105, -26500, 0, 11200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xA, 0x80)
    OP_4B(0xA, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_4B(0xD, 0x0)
    MoveCamera(40, 23, 0, 3000)
    SetCameraDistance(15200, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0301
    ChrTalk(
        0x102,
        (
            "#12P#00101F……我们已经掌握到兰迪\x01",
            "从昨夜至今早的行动了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#5P#00003F嗯，简单整理一下吧。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_61ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6486")
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪最先前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_628B")
    ClearScenarioFlags(0x0, 0)

    label("loc_628B")

    SetChrName("")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪随后前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6308")
    ClearScenarioFlags(0x0, 0)

    label("loc_6308")

    SetChrName("")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪最后前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_638E")
    ClearScenarioFlags(0x0, 0)

    label("loc_638E")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6410")

    #C0306
    ChrTalk(
        0x101,
        (
            "#5P#00003F（不对……\x01",
            "  应该不是这个顺序。）\x02\x03",

            "#00001F（再整理一次吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640B")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_640B")

    Jump("loc_6481")

    label("loc_6410")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6420"),
        (SWITCH_DEFAULT, "loc_6452"),
    )


    label("loc_6420")

    OP_2C(0xAA, 0x1)

    #C0307
    ChrTalk(
        0x101,
        "#5P#00000F（不错，就是这个顺序。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6481")

    label("loc_6452")


    #C0308
    ChrTalk(
        0x101,
        "#5P#00003F（……多半是这个顺序吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6481")

    label("loc_6481")

    Jump("loc_61ED")

    label("loc_6486")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "三点～四点　『巴鲁卡』\x01",
            "五点～六点　改造店『基约姆工房』\x01",
            "六点～　　　交换店『纳因瓦利』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    #C0310
    ChrTalk(
        0x101,
        (
            "#5P#00006F兰迪应该先去了『巴鲁卡』，\x01",
            "取走了寄存在\x01",
            "多雷克老板那里的手提箱。\x02\x03",

            "#00008F而箱子中的东西则是\x01",
            "兰迪在猎兵时代所使用的武器……\x02\x03",

            "#00001F我想，多半是攻击力\x01",
            "超群的导力来复枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        (
            "#6P#00203F像那样的来复枪，\x01",
            "在平时应该会以分解的状态来携带。\x02\x03",

            "#00201F由于已经有两年左右没使用过了，\x01",
            "所以兰迪前辈便将那些分解的部件\x01",
            "拿到修理工房检修……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x109,
        (
            "#10103F#11P嗯，应该就是这样。\x02\x03",

            "#10108F在战场上，武器的检修\x01",
            "往往可以左右战士的生死……\x02\x03",

            "#10101F像兰迪前辈这种经验丰富的人，\x01",
            "一定会在事先做好精密的检查工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x105,
        (
            "#12P#10303F最后，就是前往交换店，\x01",
            "采购各种物品了……\x02\x03",

            "#10301F他还购买了火药式弹药，\x01",
            "看来那支来复枪是相当特殊的型号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#12P#00108F听说莱恩福尔特公司\x01",
            "制造过可以切换导力模式\x01",
            "与火药模式的来复枪……\x02\x03",

            "#00101F每一种都是经过特殊强化的\x01",
            "来复枪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#5P#00006F嗯，赤色星座的\x01",
            "那些猎兵所使用的也都是\x01",
            "从未见过的巨大来复枪。\x02\x03",

            "#00013F好，这样一来，\x01",
            "我们已经大体上掌握兰迪的行动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x103,
        (
            "#6P#00206F兰迪前辈最后出现在交换店的时间\x01",
            "是在今天早上六点之后……\x02\x03",

            "#00208F现在是十点左右，\x01",
            "已经过去快四个小时了。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x109,
        (
            "#10106F#11P如果现在才出发，\x01",
            "恐怕已经很难追到兰迪前辈了……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#5P#00003F……不，无论兰迪再怎么强健，\x01",
            "毕竟也是有极限的。\x02\x03",

            "#00001F如果想对『赤色星座』出手，\x01",
            "终究还是要先休息一下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x105,
        (
            "#12P#10304F在精力充沛的境况下，活用地形优势，\x01",
            "一口气将敌人歼灭……\x02\x03",

            "#10302F只要他没有抱着玉石俱焚的想法，\x01",
            "准备与对方同归于尽，\x01",
            "还是那种做法比较妥当。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#12P#00101F……即使如此，\x01",
            "我们也没有多余的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#5P#00013F嗯，现在也只能\x01",
            "先去玛因兹……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    def lambda_6B13():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B13)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6B38():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B38)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0322
    ChrTalk(
        0x101,
        "#5P#00011F难道是……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#6P#00205F兰迪前辈打来的……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0324
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F这里是特别任务支援科！\x01",
            "我是罗伊德·班宁斯！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呀，罗伊德警官。\x02\x03",

            "……呵呵，听你的口气，\x01",
            "似乎误以为是其他人打去的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0326
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F这、这声音是……\x02\x03",

            "#00013F……您为何会知道这个号码？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0327
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，以前不是说过吗？\x01",
            "我可是你们的支持者啊。\x02\x03",

            "我在『时代』百货店。\x02\x03",

            "如果有空，\x01",
            "请一定来楼顶一趟。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    Sleep(400)
    Sound(894, 2, 100, 0)
    Sleep(1200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_24(0x37E)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x103,
        (
            "#6P#00201F……罗伊德前辈，\x01",
            "刚才的通讯是……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        "#12P#00108F到、到底是谁？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0330
    ChrTalk(
        0x101,
        (
            "#5P#00003F……『黑月』的曹。\x02\x03",

            "#00013F他似乎正在中央广场\x01",
            "百货店的楼顶等我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x109,
        "#10111F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        (
            "#12P#10301F竟在这种时候……\x01",
            "他到底有什么目的？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#5P#00006F……不知道。\x01",
            "不过，我不认为那个男人\x01",
            "会无缘无故地发来联络。\x02\x03",

            "#00001F在前往山道之前，\x01",
            "还是过去见见他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        "#12P#00101F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x103,
        "#6P#00201F总之，我们赶快过去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x80)
    OP_4C(0xA, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_4C(0xD, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -27000, 0, 13400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 1)
    OP_29(0xAA, 0x1, 0x4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_24(0x323)
    OP_24(0x37E)
    EventEnd(0x5)
    Return()

    # Function_32_606C end

    def Function_33_708B(): pass

    label("Function_33_708B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(821)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetMapObjFlags(0x4, 0x1000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    OP_68(-28080, 1950, 8970, 0)
    MoveCamera(343, 18, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20060, 0)
    OP_68(16750, 2150, 8910, 10000)
    MoveCamera(37, 10, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(35660, 10000)
    Sound(821, 2, 50, 0)
    PlayBGM("ed7576", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x240), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x1E, 0x64)
    Sleep(100)
    VolumeBGM(0x3C, 0xFA0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-2580, 10570, 29050, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36500, 0)
    OP_68(-2580, 10570, 29050, 8000)
    MoveCamera(0, -10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(30500, 8000)
    Sleep(7000)
    StopSound(821, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e3600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_708B end

    def Function_34_7220(): pass

    label("Function_34_7220")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10850, 1950, -100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10250, 0)
    OP_78(0x7, 0x13)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13630, 0, 3500, 270)
    OP_D5(0x13, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x101, 11400, 0, 1350, 90)
    SetChrPos(0x102, 11400, 0, 80, 90)
    SetChrPos(0x109, 10060, 0, 1820, 90)
    SetChrPos(0x105, 10120, 0, 440, 90)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C4")

    #C0336
    ChrTalk(
        0x11,
        (
            "你们来了啊，\x01",
            "特别任务支援科的各位！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#00000F凯特前辈，\x01",
            "您辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x109,
        (
            "#10105F您刚才说，\x01",
            "有关飙车族的案件\x01",
            "需要我们来协助……？\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x105,
        (
            "#10300F请把事情的经过\x01",
            "告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x11,
        (
            "嗯，那我现在就\x01",
            "开始说明了。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x11,
        (
            "最近，有辆危险驾驶的车辆\x01",
            "在市内横冲直撞……\x01",
            "也就是所谓的『飙车族』。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x11,
        (
            "他们似乎很享受与行人或物件\x01",
            "紧擦而过所带来的刺激感，\x01",
            "各方人士纷纷前来向我们投诉。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#00003F的确，刚才看到的那种\x01",
            "驾驶方式实在是相当蛮横……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#00101F我也听说过。\x02\x03",

            "他们好像还随时随地\x01",
            "乱按喇叭，\x01",
            "造成了严重的噪音问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        (
            "#10106F虽然不知道车主是谁，\x01",
            "但真是很让人头疼的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x11,
        (
            "嗯，公共安全科很希望能\x01",
            "尽早将这个问题解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x11,
        (
            "因此想请你们\x01",
            "特别任务支援科\x01",
            "帮忙取缔飙车族。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x11,
        "如何？可以协助吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_760A")

    label("loc_75C4")


    #C0349
    ChrTalk(
        0x11,
        (
            "希望你们\x01",
            "特别任务支援科\x01",
            "帮忙取缔飙车族。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        "如何？可以协助吗？\x02",
    )

    CloseMessageWindow()

    label("loc_760A")

    Call(0, 35)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11050, 0, 540, 225)
    EventEnd(0x5)
    Return()

    # Function_34_7220 end

    def Function_35_7629(): pass

    label("Function_35_7629")

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
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768C")
    Call(0, 36)
    Jump("loc_7739")

    label("loc_768C")


    #C0351
    ChrTalk(
        0x101,
        (
            "#00006F我们虽然很愿意\x01",
            "帮忙……\x01",
            "但现在还有点别的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x11,
        (
            "唔，这样啊。\x01",
            "没办法，毕竟你们也有自己的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x11,
        (
            "谢谢各位听我说完。\x01",
            "既然如此，我们就\x01",
            "自己想办法解决吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x130, 6)

    label("loc_7739")

    Return()

    # Function_35_7629 end

    def Function_36_773A(): pass

    label("Function_36_773A")


    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F明白了，\x01",
            "如果我们能帮得上忙，\x01",
            "就请尽管吩咐吧。\x02\x03",

            "#00009F哈哈，毕竟在警察学校学习时\x01",
            "曾受到过凯特前辈的\x01",
            "很多关照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x11,
        "谢谢大家，真是帮大忙了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【取缔飙车族】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x69, 0x4, 0x2)

    #C0357
    ChrTalk(
        0x11,
        (
            "咳咳，既然如此，\x01",
            "我先来介绍一下违章者的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x11,
        (
            "飙车族是三个年轻人，\x01",
            "看起来是出身于共和国的……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x11,
        (
            "在克洛斯贝尔市内目击到\x01",
            "这几个孩子是从不久前开始的。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x11,
        (
            "他们以港湾区的公园为据点，\x01",
            "在自治州内四处飙车。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x11,
        (
            "最近似乎都开到\x01",
            "玛因兹山道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#00105F居然还开到市外……\x01",
            "这也许会影响到\x01",
            "巴士的行驶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#00005F哎，可是……\x02\x03",

            "#00000F既然都已经\x01",
            "掌握到他们的飙车路线，\x01",
            "取缔起来应该没什么困难吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x109,
        (
            "#10105F确实如此。\x02\x03",

            "#10103F只要多出动几辆警车，\x01",
            "应该马上就能\x01",
            "将他们包围住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x11,
        (
            "唔，那可\x01",
            "行不通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x11,
        (
            "如果草率追赶，\x01",
            "他们恐怕会气急败坏地\x01",
            "强行突围。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x11,
        (
            "如果这样导致他们危险驾驶，\x01",
            "从而引发惨痛的交通事故，\x01",
            "我们可就追悔莫及了。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#00003F……真是棘手啊。\x02\x03",

            "#00001F如果真的发生了那种事情，\x01",
            "警察可就要承担责任了。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x11,
        (
            "所以，现在就需要借助\x01",
            "你们的智慧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x11,
        (
            "如何才能在不影响\x01",
            "市民的前提下，\x01",
            "将飙车族拦住呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#00003F原来如此……\x01",
            "我已经明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0372
    ChrTalk(
        0x101,
        (
            "#00000F关键的要点\x01",
            "有两个。\x02\x03",

            "#00003F首先，是安全制止\x01",
            "飙车族的『方法』……\x02\x03",

            "#00000F其次，是施行这种方法也不会\x01",
            "对市民们造成恶劣影响的『场所』。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#00103F确实如此，无论缺少哪一点，\x01",
            "都无法在安全的前提下\x01",
            "取缔飙车族呢。\x02\x03",

            "#00100F既然如此，\x01",
            "我们就先从『方法』来考虑吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x105,
        (
            "#10304F嗯，其实方法\x01",
            "倒是有不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x109,
        (
            "#10101F但最重要的，\x01",
            "还是从中选择出最不容易\x01",
            "引起事故的方法吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x11,
        (
            "嗯，那当然。\x01",
            "要把将市民卷入其中的\x01",
            "危险性抑制在最低限度。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x11,
        (
            "从这个标准来考虑，\x01",
            "我们也筛选出了一些『方法』……\x01",
            "你们认为其中有没有可行方案？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        "#00003F这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K安全制止飙车族的方法是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "用警车堵其去路\x01",      # 0
            "在路面设置陷阱\x01",      # 1
            "将其引入死路\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EBA")
    OP_2C(0x69, 0x1)

    #C0380
    ChrTalk(
        0x101,
        (
            "#00000F将其引入死路……\x01",
            "这种方法如何？\x02\x03",

            "这样一来，\x01",
            "飙车族也就\x01",
            "不得不停下来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80FF")

    label("loc_7EBA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7ED0"),
        (1, "loc_7FA8"),
        (SWITCH_DEFAULT, "loc_8079"),
    )


    label("loc_7ED0")


    #C0381
    ChrTalk(
        0x101,
        (
            "#00000F用警车堵其去路……\x01",
            "这种方法如何？\x02\x03",

            "如果有车辆阻挡在前方，\x01",
            "就算是飙车族也只能停下来……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x109,
        (
            "#10106F唔、唔……\x01",
            "我觉得这种方法\x01",
            "稍微有些莽撞。\x02\x03",

            "#10101F对方来不及刹车，\x01",
            "直接撞到警车的可能性\x01",
            "也不是没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8079")

    label("loc_7FA8")


    #C0383
    ChrTalk(
        0x101,
        (
            "#00000F在路面设置陷阱……\x01",
            "这种方法如何？\x02\x03",

            "如果用钢针一类的东西\x01",
            "刺破他们的轮胎……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x109,
        (
            "#10106F唔、唔……\x01",
            "我倒也听说过\x01",
            "那样的道具……\x02\x03",

            "#10101F但如果在克洛斯贝尔市里那么干，\x01",
            "恐怕会造成很严重的事故呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8079")

    label("loc_8079")


    #C0385
    ChrTalk(
        0x101,
        "#00006F确、确实啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0386
    ChrTalk(
        0x101,
        (
            "#00000F……既然如此，\x01",
            "将其引入死路如何？\x02\x03",

            "这样一来，\x01",
            "飙车族也就\x01",
            "不得不停下来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80FF")


    #C0387
    ChrTalk(
        0x11,
        (
            "原来如此……\x01",
            "那样应该就可以将飙车族\x01",
            "安全阻止了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        (
            "#00106F不过，说到死路……\x01",
            "一时还真是想不出\x01",
            "合适的地方。\x02\x03",

            "#00100F新市政厅大楼和ＩＢＣ附近的地段\x01",
            "终究是不能选用。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#00003F唔，这样啊……\x01",
            "本以为是个好主意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，既然如此……\x01",
            "我们自己创造条件不就好了吗？\x02\x03",

            "#10300F比如说，可以用施工现场的土袋\x01",
            "等东西来制作路障。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0391
    ChrTalk(
        0x11,
        "嗯，这主意不错啊！\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x11,
        (
            "只要用这个办法，\x01",
            "在任何地方都能创造出死路！\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x109,
        "#10100F呵呵，你真是有头脑啊。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x105,
        (
            "#10304F哈，没什么。\x02\x03",

            "#10300F那么，接下来的问题\x01",
            "就是制造死路的『场所』了。\x02\x03",

            "公共安全科对飙车族的行驶路线\x01",
            "应该有一定程度的掌握吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x11,
        "嗯，自然有所掌握。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x11,
        (
            "飙车族一般都会\x01",
            "在克洛斯贝尔市内\x01",
            "绕上一大圈。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x11,
        (
            "依次经过欢乐街、行政区、港湾区、\x01",
            "东街、中央广场、后巷……\x01",
            "最后再返回欢乐街。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x102,
        (
            "#00100F也就是说，我们最好\x01",
            "在这六个区域中的某处创造死路，\x01",
            "并将他们引诱过去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x11,
        (
            "最好能选择来往行人比较少，\x01",
            "不会给市民们\x01",
            "带来麻烦的场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x11,
        (
            "在飙车族的行驶路线之中，\x01",
            "有没有那样的场所呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#00003F这个嘛……\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_851A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A0")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0402
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K适合阻止飙车族的场所是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "欢乐街\x01",        # 0
            "行政区\x01",        # 1
            "港湾区\x01",        # 2
            "东街\x01",          # 3
            "中央广场\x01",      # 4
            "后巷\x01",          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8607")

    #C0403
    ChrTalk(
        0x101,
        (
            "#00000F最符合条件的地方……\x01",
            "我认为是行政区。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8602")
    OP_2C(0x69, 0x1)

    label("loc_8602")

    Jump("loc_869B")

    label("loc_8607")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0404
    ChrTalk(
        0x101,
        (
            "#00003F（……不对，还是不要\x01",
            "  选择这个地方为好吧？）\x02\x03",

            "（说到来往行人比较少，\x01",
            "  不会给市民们造成麻烦的地方，\x01",
            "  最符合条件的还是……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_869B")

    Jump("loc_851A")

    label("loc_86A0")


    #C0405
    ChrTalk(
        0x105,
        (
            "#10300F行政区……\x01",
            "也就是市民会馆、图书馆，\x01",
            "还有警察总部所在的区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x102,
        (
            "#00100F那里的行人\x01",
            "确实很少……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x109,
        (
            "#10100F嗯，就算发生交通事故，\x01",
            "应该也能将损害抑制在最低限度。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x11,
        (
            "再加上警察总部就在附近，\x01",
            "正是再合适不过的作战场所！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x11,
        (
            "……嗯，按照这个方法来作战，\x01",
            "应该能取得成功！\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x11,
        (
            "呵呵，真不愧是特别任务支援科！\x01",
            "转瞬之间就制定好作战方法了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        "#00009F哈哈，能帮上前辈的忙，我深感荣幸。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x11,
        (
            "接下来，要想将飙车族\x01",
            "引诱至死路，\x01",
            "大概还需要几辆警车帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x11,
        (
            "好，那我现在就通知\x01",
            "公共安全科的各位，\x01",
            "立刻开始作战吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x11,
        (
            "罗伊德，设置路障的准备工作\x01",
            "就拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        "#00000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x105,
        "#10309F呵呵，越来越有趣了嘛。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        (
            "#00100F既然这样，\x01",
            "我们就拿出干劲吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x109,
        (
            "#10100F嗯，一定要\x01",
            "制止飙车族！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("c1200", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_36_773A end

    def Function_37_8991(): pass

    label("Function_37_8991")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -16970, 0, 10380, 90)
    OP_68(-16340, 1950, 10050, 0)
    MoveCamera(34, 51, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8590, 0)
    SetChrPos(0x101, -35010, 0, 11220, 90)
    SetChrPos(0x102, -36140, 0, 9520, 90)
    SetChrPos(0x1A3, -36060, 0, 12520, 90)
    SetChrPos(0x104, -37510, 0, 12020, 90)
    SetChrPos(0x109, -37260, 0, 10020, 90)
    SetChrPos(0x105, -38010, 0, 10820, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    def lambda_8A8C():
        OP_95(0xFE, -8119, 1770, 11630, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8A8C)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-12110, 1950, 11440, 4000)
    MoveCamera(34, 51, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(11450, 4000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-37440, 1950, 9730, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9160, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0419
    ChrTalk(
        0x101,
        "#5P#00005F……在这里！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#00100F接下来，我们还是\x01",
            "慎重些为好啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0421
    ChrTalk(
        0x101,
        (
            "#11P#00003F嗯，迂回接近，\x01",
            "免得它再跑到其它街区。\x02\x03",

            "#00000F我和艾莉绕过去，\x01",
            "由行政区方向接近它，\x01",
            "诺艾尔和瓦吉由后巷方向接近。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0422
    ChrTalk(
        0x109,
        "#6P#10100F知道了。\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x105,
        "#6P#10302F明白。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)
    Sleep(300)

    #C0424
    ChrTalk(
        0x101,
        (
            "#11P#00000F你和兰迪就继续\x01",
            "由住宅街方向接近吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    #C0425
    ChrTalk(
        0x104,
        "#6P#00303F……收到。\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x1A3,
        "#5P#04609F啊哈哈，包围战吗¤\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x3)
    OP_68(1290, 3710, 10770, 0)
    MoveCamera(43, 30, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9860, 0)
    SetChrPos(0x14, 2490, 1760, 11180, 90)
    SetChrPos(0x101, 15020, 0, 5200, 0)
    SetChrPos(0x102, 15000, 0, 2900, 0)

    def lambda_8D4A():
        OP_95(0xFE, 13360, 0, 10870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8D4A)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(13490, 1950, 10070, 5000)
    MoveCamera(42, 30, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9450, 5000)

    def lambda_8D9F():
        OP_95(0xFE, 15810, 0, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D9F)
    Sleep(50)

    def lambda_8DBC():
        OP_95(0xFE, 15710, 0, 10230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DBC)
    WaitChrThread(0x101, 1)

    def lambda_8DDA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DDA)
    WaitChrThread(0x102, 1)

    def lambda_8DEB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DEB)
    OP_6F(0x79)

    #C0427
    ChrTalk(
        0x101,
        (
            "#00000F玛丽，乖，\x01",
            "到这边来。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#00100F不用担心哦，\x01",
            "我们会带你回家的。\x02",
        )
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    def lambda_8E4E():
        OP_95(0xFE, 9930, 0, 4040, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8E4E)
    Sleep(50)

    def lambda_8E6B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E6B)
    Sleep(50)

    def lambda_8E7B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E7B)
    Sleep(1000)
    EndChrThread(0x14, 0x1)
    Fade(500)
    OP_68(6630, 1950, -13390, 0)
    MoveCamera(82, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7810, 0)
    SetChrPos(0x14, 7930, 0, -7640, 180)
    SetChrPos(0x109, 12080, 0, -15670, 315)
    SetChrPos(0x105, 11030, 0, -17020, 315)

    def lambda_8EF5():
        OP_95(0xFE, 7970, 0, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8EF5)
    Sleep(50)

    def lambda_8F12():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F12)
    Sleep(50)

    def lambda_8F2A():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8F2A)
    OP_0D()
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x87, 0x1F4)
    Sleep(300)

    #C0429
    ChrTalk(
        0x109,
        "#10100F玛丽，别害怕。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，放弃抵抗，\x01",
            "老老实实过来吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F97():
        OP_95(0xFE, 440, 0, -6930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8F97)
    Sleep(1000)
    EndChrThread(0x14, 0x1)
    Fade(500)
    OP_68(-34190, 1950, 7420, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7870, 0)
    SetChrPos(0x14, -22150, 0, 7980, 270)
    SetChrPos(0x104, -35990, 0, 9690, 90)
    SetChrPos(0x1A3, -35970, 0, 11380, 90)

    def lambda_901E():
        OP_95(0xFE, -28830, 0, 10230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_901E)
    Sleep(50)

    def lambda_903B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_903B)
    Sleep(50)

    def lambda_9053():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_9053)
    OP_0D()
    WaitChrThread(0x14, 1)

    #C0431
    ChrTalk(
        0x1A3,
        "#04602F好啦好啦，我们不会欺负你哦。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x104,
        (
            "#00303F（……真是的，\x01",
            "  她喜欢猫这一点还是没变啊。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_90D0():
        OP_95(0xFE, -8119, 1770, 11630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_90D0)
    Sleep(1000)
    EndChrThread(0x14, 0x1)
    Fade(500)
    SetChrPos(0x8, 380, 1770, 28050, 225)
    SetChrPos(0x9, 1830, 1770, 27900, 225)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(-4450, 3860, 22900, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x14, -1970, 1990, 23280, 180)
    SetChrPos(0x101, 4560, 1760, 24610, 270)
    SetChrPos(0x102, 2580, 1990, 21200, 315)
    SetChrPos(0x109, -1130, 1990, 19400, 0)
    SetChrPos(0x105, -2530, 1990, 19200, 0)
    SetChrPos(0x104, -6130, 1990, 20650, 45)
    SetChrPos(0x1A3, -7940, 1760, 23860, 90)
    SetCameraDistance(9520, 4000)
    OP_0D()

    def lambda_91CF():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91CF)
    Sleep(50)

    def lambda_91E7():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91E7)
    Sleep(50)

    def lambda_91FF():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91FF)
    Sleep(50)

    def lambda_9217():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9217)
    Sleep(50)

    def lambda_922F():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_922F)
    Sleep(50)

    def lambda_9247():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_9247)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_9271():
        OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9271)
    WaitChrThread(0x14, 1)
    OP_6F(0x10)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0433
    ChrTalk(
        0x8,
        "啊，是小猫！好可爱⊥\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x9,
        (
            "#11P而且还那么小，\x01",
            "真想抱抱啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x14)
    TurnDirection(0x14, 0x8, 500)
    OP_63(0x14, 0x0, 1200, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x14, 1, 0, 38)
    Sleep(1000)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(50)

    #C0435
    ChrTalk(
        0x101,
        "#11P#N#00011F糟糕！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x14, 0x1)
    OP_64(0x14)

    def lambda_9368():

        label("loc_9368")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_9368")

    QueueWorkItem2(0x101, 1, lambda_9368)

    def lambda_937A():

        label("loc_937A")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_937A")

    QueueWorkItem2(0x104, 1, lambda_937A)

    def lambda_938C():

        label("loc_938C")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_938C")

    QueueWorkItem2(0x102, 1, lambda_938C)

    def lambda_939E():

        label("loc_939E")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_939E")

    QueueWorkItem2(0x109, 1, lambda_939E)

    def lambda_93B0():

        label("loc_93B0")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_93B0")

    QueueWorkItem2(0x105, 1, lambda_93B0)

    def lambda_93C2():

        label("loc_93C2")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_93C2")

    QueueWorkItem2(0x1A3, 1, lambda_93C2)

    def lambda_93D4():

        label("loc_93D4")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_93D4")

    QueueWorkItem2(0x8, 1, lambda_93D4)

    def lambda_93E6():

        label("loc_93E6")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_93E6")

    QueueWorkItem2(0x9, 1, lambda_93E6)
    Sound(953, 0, 100, 0)

    def lambda_93FE():
        OP_95(0xFE, -2110, 2660, 36590, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_93FE)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A3, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)

    def lambda_943B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_943B)
    WaitChrThread(0x14, 1)
    SetChrFlags(0x14, 0x80)
    OP_0D()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0436
    ChrTalk(
        0x101,
        "#11P#N#00005F啊……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0437
    ChrTalk(
        0x102,
        "#11P#00105F跑进彩虹剧团了……！\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x109,
        "#11P#10106F好、好快的速度啊。\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x104,
        (
            "#12P#00306F呼……既然如此，\x01",
            "我们也只能进去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x1A3,
        (
            "#6P#04609F嗯嗯，\x01",
            "不过这下它可就走进死路了呢¤\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_8991 end

    def Function_38_95D6(): pass

    label("Function_38_95D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9602")
    OP_93(0xFE, 0x0, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x10E, 0x190)
    Jump("Function_38_95D6")

    label("loc_9602")

    Return()

    # Function_38_95D6 end

    def Function_39_9603(): pass

    label("Function_39_9603")

    EventBegin(0x0)
    Fade(500)
    OP_68(-11770, 3710, 22190, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11400, 0)
    SetChrPos(0x101, -10150, 1760, 22970, 0)
    SetChrPos(0x102, -11350, 1760, 22970, 0)
    SetChrPos(0x103, -10150, 1760, 21770, 0)
    SetChrPos(0x109, -11350, 1760, 21770, 0)
    SetChrPos(0x105, -10150, 1760, 20570, 0)
    SetChrPos(0x104, -11350, 1760, 20570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_0D()

    #C0441
    ChrTalk(
        0xC,
        (
            "欢迎光临，\x01",
            "要来个冰激凌吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0444
    ChrTalk(
        0xC,
        (
            "啊，原来你们是为那件事来的啊。\x01",
            "我之前听通讯社的人说起过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xC,
        (
            "那么，现在就请各位品尝一下吧……\x01",
            "这是本店推荐的冰激凌\x01",
            "冰凉甜点『七彩』！\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x105,
        (
            "#10305F嘿，看起来好像\x01",
            "很美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xC,
        (
            "这是新品种的冰激凌，\x01",
            "多种味道混和在一起就是它的魅力所在。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xC,
        (
            "另外，还加入了可以在口中\x01",
            "噼噼啪啪作响的糖粒，那种不可思议\x01",
            "的奇妙口感一定会让大家喜欢的。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#00100F那我们就赶快\x01",
            "尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人品尝了冰凉甜点『七彩』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0451
    ChrTalk(
        0x109,
        (
            "#10103F（张口品尝）\x02\x03",

            "#10109F……嗯～\x01",
            "冰凉又美味！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0452
    ChrTalk(
        0x102,
        (
            "#00102F嗯，外观非常可爱，\x01",
            "糖粒在口中噼噼作响的感觉也很不错。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0453
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，女生们好像\x01",
            "很喜欢这种甜品呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x103, 500)

    #C0454
    ChrTalk(
        0x104,
        (
            "#00305F嗯，怎么了，阿缇？\x01",
            "觉得太凉吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9AE1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9AE1)

    def lambda_9AEE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9AEE)

    def lambda_9AFB():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9AFB)

    def lambda_9B08():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9B08)

    def lambda_9B15():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9B15)
    Sleep(1000)
    OP_64(0x103)

    #C0455
    ChrTalk(
        0x103,
        (
            "#00204F不……抱歉。\x02\x03",

            "#00200F只是冲击感过于强烈，\x01",
            "瞬间陷入忘我状态了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x103, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1500)

    #C0456
    ChrTalk(
        0x103,
        (
            "#00204F在口中跳动的糖粒充满刺激感，\x01",
            "冰激凌的口感也十分新鲜……\x02\x03",

            "而且七种不同的味道毫无不协调的感觉，\x01",
            "在口中完美融合到了一起。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0457
    ChrTalk(
        0x103,
        "#00201F#4S这简直就是冰激凌的革命……！\x02",
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
    OP_64(0x103)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x103,
        (
            "#00206F……不好意思，\x01",
            "我太兴奋了。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#00012F哈哈……\x01",
            "看来你相当喜欢啊。\x01",
            "那就由缇欧来介绍它好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x103,
        (
            "#00202F嗯，我一定能写出\x01",
            "很不错的报道文章。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xC,
        "嘿嘿嘿，你们能喜欢本店的冰激凌，我很开心。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "今后也请继续\x01",
            "光顾本店哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x172, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_9DF4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_9E11")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_9E24")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9E37")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9E54")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_9E67")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9E84")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_9E97")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_9EB4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9EC7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_9EE4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EE4")

    OP_29(0x80, 0x1, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FB9")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FB0")

    #A0464
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9FB0")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_9FB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A07C")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0466
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_A07C")

    OP_4C(0xC, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10150, 1760, 22970, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_9603 end

    def Function_40_A0AC(): pass

    label("Function_40_A0AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A0BA")
    Jump("loc_A3F8")

    label("loc_A0BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A0C8")
    Jump("loc_A3F8")

    label("loc_A0C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A0D6")
    Jump("loc_A3F8")

    label("loc_A0D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A0E4")
    Jump("loc_A3F8")

    label("loc_A0E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A13F")
    EventBegin(0x1)

    #C0467
    ChrTalk(
        0x101,
        (
            "#00000F大家似乎正在\x01",
            "忙着彩排，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_A3F8")

    label("loc_A13F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A19A")
    EventBegin(0x1)

    #C0468
    ChrTalk(
        0x101,
        (
            "#00000F大家似乎正在\x01",
            "忙着彩排，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_A3F8")

    label("loc_A19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A1A8")
    Jump("loc_A3F8")

    label("loc_A1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A1B6")
    Jump("loc_A3F8")

    label("loc_A1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A37A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A272")

    #C0469
    ChrTalk(
        0x101,
        (
            "#00000F说起来，首脑们今天\x01",
            "将会来观赏舞剧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        (
            "#00100F我们如果进去，也许会打扰到人家，\x01",
            "还是不要在这种时候拜访了。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x104,
        "#00300F嗯，确实如此。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A2B1")

    label("loc_A272")


    #C0472
    ChrTalk(
        0x101,
        (
            "#00000F首脑们今天\x01",
            "准备来观赏舞剧呢。\x01",
            "我们还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2B1")

    Jump("loc_A35F")

    label("loc_A2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A329")

    #C0473
    ChrTalk(
        0x101,
        (
            "#00003F……刚刚都\x01",
            "打扰过人家了。\x02\x03",

            "#00000F他们还要为迎接\x01",
            "首脑们做准备，\x01",
            "我们还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A35F")

    label("loc_A329")


    #C0474
    ChrTalk(
        0x101,
        (
            "#00000F……刚刚都打扰过人家了，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A35F")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_A3F8")

    label("loc_A37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A388")
    Jump("loc_A3F8")

    label("loc_A388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A3EF")
    EventBegin(0x1)

    #C0475
    ChrTalk(
        0x101,
        (
            "#00000F彩虹剧团的人\x01",
            "似乎正在忙着准备，\x01",
            "我们还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_A3F8")

    label("loc_A3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A3F8")

    label("loc_A3F8")

    Return()

    # Function_40_A0AC end

    def Function_41_A3F9(): pass

    label("Function_41_A3F9")

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

    # Function_41_A3F9 end

    SaveToFile()

Try(main)
