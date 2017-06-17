from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ポリセ",                 # 1
        "タップ",                 # 2
        "テージョ",               # 3
        "客引きピム",             # 4
        "ソフィーユ",             # 5
        "ラマンダ",               # 6
        "バニーガール",           # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "ケイト巡査",             # 10
        "警官",                   # 11
        "パトカー",               # 12
        "マリー",                 # 13
        "車",                     # 14
        "黒い運搬車",             # 15
        "中央広場",               # 16
        "西通り",                 # 17
        "行政区",                 # 18
        "住宅街",                 # 19
        "歓楽街",                 # 20
        "東通り",                 # 21
        "旧市街",                 # 22
        "港湾区",                 # 23
        "ＩＢＣ",                 # 24
        "駅前通り",               # 25
        "裏通り",                 # 26
        "ウルスラ間道",           # 27
        "東クロスベル街道",       # 28
        "西クロスベル街道",       # 29
        "マインツ山道",           # 30
        "オルキスタワー",         # 31
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
    PlaceName(124.0, 0.0, 255.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_8_159F",         # 08, 8
        "Function_9_176B",         # 09, 9
        "Function_10_274B",        # 0A, 10
        "Function_11_3081",        # 0B, 11
        "Function_12_39C0",        # 0C, 12
        "Function_13_4156",        # 0D, 13
        "Function_14_4C26",        # 0E, 14
        "Function_15_5525",        # 0F, 15
        "Function_16_5FD1",        # 10, 16
        "Function_17_6062",        # 11, 17
        "Function_18_6105",        # 12, 18
        "Function_19_62F8",        # 13, 19
        "Function_20_6333",        # 14, 20
        "Function_21_6510",        # 15, 21
        "Function_22_6575",        # 16, 22
        "Function_23_69AE",        # 17, 23
        "Function_24_6A4B",        # 18, 24
        "Function_25_6A82",        # 19, 25
        "Function_26_6AAF",        # 1A, 26
        "Function_27_6AE9",        # 1B, 27
        "Function_28_6B0B",        # 1C, 28
        "Function_29_6B45",        # 1D, 29
        "Function_30_6B80",        # 1E, 30
        "Function_31_6BD7",        # 1F, 31
        "Function_32_6C7D",        # 20, 32
        "Function_33_7E3E",        # 21, 33
        "Function_34_7FD3",        # 22, 34
        "Function_35_84A4",        # 23, 35
        "Function_36_85F1",        # 24, 36
        "Function_37_9C50",        # 25, 37
        "Function_38_A937",        # 26, 38
        "Function_39_A964",        # 27, 39
        "Function_40_B4F9",        # 28, 40
        "Function_41_B8D4",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1523")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0001
    ChrTalk(
        0xFE,
        "あら、ロイド君たち……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "噂には聞いていたけど、\x01",
            "特務支援課も再始動ってわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00000Fはい、新メンバー共々\x01",
            "改めてよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00105Fそれにしても、ケイトさんが\x01",
            "歓楽街でお仕事というのも\x01",
            "珍しいですよね？\x02\x03",

            "#00100Fいつもは中央広場にいる\x01",
            "イメージでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ええ、実は最近\x01",
            "目を付けている導力車があって\x01",
            "ここで張り込みをしているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "まあそれはともかく、\x01",
            "あなたたちの活躍には\x01",
            "ますます期待しているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "今後とも、お互い\x01",
            "しゃかりきになって頑張りましょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 4)
    Jump("loc_159B")

    label("loc_1523")


    #C0009
    ChrTalk(
        0xFE,
        (
            "ふふ、噂には聞いていたけど、\x01",
            "特務支援課も再始動ってわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "今後とも、お互い\x01",
            "しゃかりきになって頑張りましょ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159B")

    TalkEnd(0xFE)
    Return()

    # Function_7_12B7 end

    def Function_8_159F(): pass

    label("Function_8_159F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1641")

    #C0011
    ChrTalk(
        0xFE,
        (
            "テロリストもそうだが、\x01",
            "『赤い星座』や『黒月』の動向も\x01",
            "不気味だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "誰がどう仕掛けて事が動くのか……\x01",
            "あらゆる動きから目を離せないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16CB")

    #C0013
    ChrTalk(
        0xFE,
        (
            "除幕式は無事に終わったが、\x01",
            "警戒はまだまだ始まったばかりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "今日から３日間、集中力を\x01",
            "切らさないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1767")

    #C0015
    ChrTalk(
        0xFE,
        (
            "通商会議の前後の間、\x01",
            "アルカンシェルは一般公演を\x01",
            "控えることになっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "おかげで、この広場の出入りも\x01",
            "若干落ち着いているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1767")

    TalkEnd(0xFE)
    Return()

    # Function_8_159F end

    def Function_9_176B(): pass

    label("Function_9_176B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17A2")
    Call(0, 39)
    Return()

    label("loc_17A2")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2747")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_180D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_180D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182D")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2742")

    label("loc_182D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1841")
    Jump("loc_2742")

    label("loc_1841")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2742")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_18BF")

    #C0017
    ChrTalk(
        0xC,
        "えへへ、喜んで頂けて嬉しいです。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        (
            "今後とも当店を\x01",
            "ごひいきにお願いしますねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1928")

    #C0019
    ChrTalk(
        0xC,
        "本当に凄い騒ぎですねー。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xC,
        (
            "何だか熱気で、アイスが\x01",
            "溶けてしまいそうな気がしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_1928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E3")

    #C0021
    ChrTalk(
        0xC,
        "イリアさん……本当に心配ですよね。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xC,
        (
            "わたしにはアイスを売るくらいしか\x01",
            "能がないですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "ここで商売を続けて、\x01",
            "イリアさんの復帰を待つつもりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A38")

    label("loc_19E3")


    #C0024
    ChrTalk(
        0xC,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "ひんやりさわやか、\x01",
            "とってもおいしいですよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A38")

    Jump("loc_2742")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEC")

    #C0026
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ～！\x01",
            "アイスはいかがですか～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        (
            "今日は待ちに待った\x01",
            "リニューアル公演の公開日で～す！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        "みんなで盛り上げて行きましょー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B84")

    label("loc_1AEC")


    #C0029
    ChrTalk(
        0xC,
        (
            "マインツなら大丈夫……\x01",
            "警備隊の人たちが\x01",
            "何とかしてくれるはずです！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xC,
        (
            "とにかく私はいつも通り、\x01",
            "アルカンシェルを応援して\x01",
            "アイスを売るだけです！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B84")

    Jump("loc_2742")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B97")
    Jump("loc_2742")

    label("loc_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CB1")

    #C0031
    ChrTalk(
        0xC,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xC,
        (
            "お客さんはお昼を食べましたかー？\x01",
            "食後のアイスは絶品ですよー。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CAC")

    #C0033
    ChrTalk(
        0x101,
        (
            "#00008F（ここでグルメガイドの取材が\x01",
            "  出来そうだけど……）\x02\x03",

            "#00003F（今はそれどころじゃない。\x01",
            "  後で忘れずに来るとしよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAC")

    Jump("loc_2742")

    label("loc_1CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D51")

    #C0034
    ChrTalk(
        0xC,
        (
            "アルカンシェルのリニューアル舞台、\x01",
            "いよいよ明後日公開ですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "またお客さんが増えちゃいますねー。\x01",
            "ふふふ、繁盛し過ぎて困りそうですー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E00")

    #C0036
    ChrTalk(
        0xC,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "どれにしようかお悩みなら、\x01",
            "ご試食もオッケーですからねー？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "こちらの特製ミニスプーンで\x01",
            "ひとくちどうぞー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E7E")

    label("loc_1E00")


    #C0039
    ChrTalk(
        0xC,
        (
            "アイスの試食サービスが好評で\x01",
            "売り上げが好調なんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "もちろん今月の屋台ＭＶＰも\x01",
            "私がいただきましたー、ビバッ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7E")

    Jump("loc_2742")

    label("loc_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F22")

    #C0041
    ChrTalk(
        0xC,
        (
            "アルカンシェル、もうすぐ\x01",
            "お休みに入っちゃうんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "う～ん、売り上げ減少の危機ですねー。\x01",
            "何とか対策を立てないとー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F96")

    label("loc_1F22")


    #C0043
    ChrTalk(
        0xC,
        (
            "う～ん、この程度の危機で\x01",
            "トップを明け渡したんじゃ\x01",
            "屋台ＭＶＰの名折れですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        "何とか対策を立てないとー。\x02",
    )

    CloseMessageWindow()

    label("loc_1F96")

    Jump("loc_2742")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_245E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2047")

    #C0045
    ChrTalk(
        0xFE,
        (
            "今さっきの赤毛のお客さんなら、\x01",
            "住宅街の方に行っちゃいましたよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "かっちりスーツ姿で決めてるのに、\x01",
            "なんだかおかしな人でしたねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_2047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22C9")

    #C0047
    ChrTalk(
        0xFE,
        (
            "今さっき、明るい赤毛のお兄さんが\x01",
            "『１０段アイスを作ってくれ』って\x01",
            "注文されちゃったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "あんな高さのアイスを注文して、\x01",
            "しかも倒さずに一気食いする\x01",
            "お客さんなんて始めてですよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "かっちりスーツ姿で決めてるのに、\x01",
            "なんだかおかしな人でしたねー。\x02",
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
            "#10106F（ロ、ロイドさん。\x01",
            "  これってやっぱりあの人じゃ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00012Fえ、えっと……\x01",
            "その男の人はどちらへ？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "アイスの冷たさに頭を抱えたまま、\x01",
            "住宅街の方に行っちゃいましたよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F（よし……\x01",
            "  このまま追いかけてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1C7, 2)
    Jump("loc_2459")

    label("loc_22C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DA")

    #C0054
    ChrTalk(
        0xC,
        "いやー、午前は凄い騒ぎでしたね～。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xC,
        (
            "この辺りはＶＩＰの皆さんが\x01",
            "通ったワケでもないので、\x01",
            "人通りはそれなりでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xC,
        (
            "除幕式が終わった後は\x01",
            "一気にどわっと人が流れて来て\x01",
            "大繁盛でしたー。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        (
            "ふふふー、これが\x01",
            "３ヶ月連続屋台ＭＶＰの実力ですー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2459")

    label("loc_23DA")


    #C0058
    ChrTalk(
        0xC,
        (
            "おかげ様で、今日は早くも\x01",
            "売り切れそうなんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "ってわけで、\x01",
            "お客さんも後悔しない内に\x01",
            "今買っちゃってくださいっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2459")

    Jump("loc_2742")

    label("loc_245E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256F")

    #C0060
    ChrTalk(
        0xC,
        (
            "ミルク系にシャーベット系、\x01",
            "お客様はどちらの\x01",
            "アイスがお好みですかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        (
            "ちなみに、イリアさんは\x01",
            "シャーベット系、プリエさんはミルク系を\x01",
            "よく買っていくんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xC,
        (
            "あと、リーシャさんも\x01",
            "イリアさんと同じく\x01",
            "シャーベット系が多いですかねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25F2")

    label("loc_256F")


    #C0063
    ChrTalk(
        0xC,
        (
            "さらに言うと、\x01",
            "ユージーンさんはミルク系、\x01",
            "テオドールさんは……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "……甘いものがキライらしくて\x01",
            "買ってくれないんですよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    Jump("loc_2742")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2605")
    Jump("loc_2742")

    label("loc_2605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B9")

    #C0065
    ChrTalk(
        0xC,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "ウチのアイスは\x01",
            "種類が豊富ですからねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "何度も通って、\x01",
            "ぜひお気に入りののフレーバーを\x01",
            "お探しくださいませー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2742")

    label("loc_26B9")


    #C0068
    ChrTalk(
        0xC,
        (
            "ちなみに要望があれば、\x01",
            "ご自由にブレンドすることも\x01",
            "できますからねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "助言を無視してマズくなっても、\x01",
            "責任は取れないですけどー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2742")

    Jump("loc_17AF")

    label("loc_2747")

    TalkEnd(0xFE)
    Return()

    # Function_9_176B end

    def Function_10_274B(): pass

    label("Function_10_274B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_27CE")

    #C0070
    ChrTalk(
        0xFE,
        (
            "いやはや……何だか\x01",
            "とんでもないことになってるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "とにかく、面倒事だけは\x01",
            "カンベンして欲しいモンだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_27CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_285A")

    #C0072
    ChrTalk(
        0xFE,
        (
            "へっへっへっ、あんたら\x01",
            "ウチの店で飲んでかないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "チャリティサービスっつうことで、\x01",
            "かなり勉強させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_285A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28F1")

    #C0074
    ChrTalk(
        0xFE,
        (
            "な～んか、最近\x01",
            "物騒なことがよく起こるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "ほ～んと、これじゃ裏通りで\x01",
            "起こってるようないさかいですら\x01",
            "可愛く見えて来ちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28FF")
    Jump("loc_307D")

    label("loc_28FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2997")

    #C0076
    ChrTalk(
        0xFE,
        (
            "あー、どこかに\x01",
            "羽振りの良さそうな\x01",
            "カモはいないもんかねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "お～っと、へっへっへっ、\x01",
            "思わず心の声が漏れちゃったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29EC")

    label("loc_2997")


    #C0078
    ChrTalk(
        0xFE,
        (
            "へっへっへっ、\x01",
            "思わず心の声が漏れちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        "気ぃゆるんでる証拠だねっと。\x02",
    )

    CloseMessageWindow()

    label("loc_29EC")

    Jump("loc_307D")

    label("loc_29F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A58")

    #C0080
    ChrTalk(
        0xFE,
        (
            "さ～て、今日もがんばって\x01",
            "お仕事しますかねっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        "夢の世界にごしょーたいってね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4F")

    #C0082
    ChrTalk(
        0xFE,
        (
            "いやー、アルカンシェルも\x01",
            "つくづく新人に恵まれてるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "今度新しい姫役でデビューする\x01",
            "シュリちゃんっつったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "あのリーシャちゃんが出てきて\x01",
            "まだ１年も経ってないってのにね。\x01",
            "ほんとウチにも分けて欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BC1")

    label("loc_2B4F")


    #C0085
    ChrTalk(
        0xFE,
        (
            "にしても、\x01",
            "アルカンシェルのアーティストは\x01",
            "カワイコちゃんばっかだよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "ほんとウチにも分けて欲しいわ。\x02",
    )

    CloseMessageWindow()

    label("loc_2BC1")

    Jump("loc_307D")

    label("loc_2BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C72")

    #C0087
    ChrTalk(
        0xFE,
        (
            "通商会議っつっても、\x01",
            "ウチらみたいなモンにとっちゃ\x01",
            "何にも面白いことがないねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "最近は豪遊してくれる\x01",
            "議員先生も少なくなったし、\x01",
            "商売上がったりだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CF2")

    #C0089
    ChrTalk(
        0xFE,
        (
            "今日は人通りが多いけど、\x01",
            "市民ばっかで観光客は少ないねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "なんていうか、\x01",
            "早くも創立記念祭が懐かしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D68")

    #C0091
    ChrTalk(
        0xFE,
        (
            "あー、警察の人たち\x01",
            "目を光らせちゃってるねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "これじゃ、あんまり\x01",
            "強引なこたぁ出来なさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D76")
    Jump("loc_307D")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_307D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3011")

    #C0093
    ChrTalk(
        0xFE,
        (
            "へっへっへっ、\x01",
            "あんたらヒマしてんなら\x01",
            "ウチの店で飲んでいかないかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "４人一緒なら団体割引で\x01",
            "サービスさせてもらうよん？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        "#10305Fへえ、それってどのくらい？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E54")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2E54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E77")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2E77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9A")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2E9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBA")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_2EBA")

    Sleep(1000)

    #C0096
    ChrTalk(
        0xFE,
        (
            "そうさねえ、いつもは\x01",
            "お１人様５００ミラの所を……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    #C0097
    ChrTalk(
        0x109,
        "#10101Fワ、ワジ君……！\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00106Fあの、私たち仕事中なので\x01",
            "そういうのはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "んん……？\x01",
            "ああ、冷やかしだったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "なら、しっしっ……\x01",
            "商売の邪魔しないでくれるかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        "#00006Fな、なんかすみません……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 2)
    Jump("loc_307D")

    label("loc_3011")


    #C0102
    ChrTalk(
        0xFE,
        (
            "あー、あんたら冷やかしなら\x01",
            "遠慮してちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "あんまりしつこいと、\x01",
            "お兄さん怒っちゃうかもよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307D")

    TalkEnd(0xFE)
    Return()

    # Function_10_274B end

    def Function_11_3081(): pass

    label("Function_11_3081")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3116")

    #C0104
    ChrTalk(
        0xFE,
        (
            "イリア様に怪我を\x01",
            "負わせたのはきっと帝国の仕業……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "だから……帝国は許せない………！\x01",
            "言いなりになってたまるものですかっ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3184")

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
            "……イリア様………\x01",
            "どうしてこんなことに………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_31C1")

    label("loc_3184")


    #C0108
    ChrTalk(
        0xFE,
        (
            "犯人のヤツラ……許せない……\x01",
            "……絶対に許せない………！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C1")

    Jump("loc_39BC")

    label("loc_31C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3265")

    #C0109
    ChrTalk(
        0xFE,
        (
            "ついに……ついに今日の夕方、\x01",
            "リニューアル公演が公開に……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "イ・リ・ア・様～～！\x01",
            "ポリセはここで舞台の成功を\x01",
            "祈っておりますわ～～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_336E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330F")

    #C0111
    ChrTalk(
        0xFE,
        (
            "明日……もう明日、\x01",
            "ついに明日、とうとう明日っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "イリア様、残念ながら\x01",
            "初日には観られませんが……\x01",
            "ポリセは今夜眠れそうにありませんっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3369")

    label("loc_330F")


    #C0113
    ChrTalk(
        0xFE,
        (
            "イリア様、残念ながら\x01",
            "初日には観られませんが……\x01",
            "ポリセは今夜眠れそうにありませんっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3369")

    Jump("loc_39BC")

    label("loc_336E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33C4")

    #C0114
    ChrTalk(
        0xFE,
        "イリア様、イリア様～っ！！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "お稽古がんばってくださいませ～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_33C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347C")

    #C0116
    ChrTalk(
        0xFE,
        (
            "明後日……\x01",
            "とうとう明後日なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "イリア様とシュリちゃんは\x01",
            "一体どう絡むのかしら……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "じゅるり……ぐふふ……\x01",
            "想像するだけでたまんないわっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34F2")

    label("loc_347C")


    #C0119
    ChrTalk(
        0xFE,
        (
            "イリア様とシュリちゃんは\x01",
            "一体どう絡むのかしら……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "じゅるり……ぐふふ……\x01",
            "想像するだけでたまんないわっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F2")

    Jump("loc_39BC")

    label("loc_34F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3565")

    #C0121
    ChrTalk(
        0xFE,
        (
            "明々後日……\x01",
            "ついに明々後日なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "リニューアル公演の公開日……\x01",
            "待ち遠しすぎるわ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3641")

    #C0123
    ChrTalk(
        0xFE,
        (
            "公演は休みでも、イリア様は\x01",
            "練習のために劇場に来るはず……！\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "つまり、逆にこれはイリア様の\x01",
            "写真を更に撮りまくるチャンス……！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "だから私は休みの間も\x01",
            "アルカンシェルに通い続けるわっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36B7")

    label("loc_3641")


    #C0126
    ChrTalk(
        0xFE,
        (
            "イリア様は練習のために\x01",
            "これからも劇場に来るはず……！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "だから私は休みの間も\x01",
            "アルカンシェルに通い続けるわっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B7")

    Jump("loc_39BC")

    label("loc_36BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3742")

    #C0128
    ChrTalk(
        0xFE,
        (
            "今日の夜、首脳たちが\x01",
            "アルカンシェルを観劇するそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "ううぅ……ずる～いっ！\x01",
            "私だって招待して欲しいのにっ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382F")

    #C0130
    ChrTalk(
        0xFE,
        "#4Sむきゃ～……っ！！#3S\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "リニューアル公演のチケット、\x01",
            "公開初日の分は流石に競争率が\x01",
            "高過ぎて手に入らなかったの！！\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "やっとの思いで手に入れたのは\x01",
            "公開１週間後のＢ席……\x01",
            "嬉しい………けど悔しいっ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E3")

    label("loc_382F")


    #C0133
    ChrTalk(
        0xFE,
        (
            "リニューアル公演のチケット、\x01",
            "公開初日の分は流石に競争率が\x01",
            "高過ぎて手に入らなかったの！！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "やっとの思いで手に入れたのは\x01",
            "公開１週間後のＢ席……\x01",
            "嬉しい………けど悔しいっ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E3")

    Jump("loc_39BC")

    label("loc_38E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_393A")

    #C0135
    ChrTalk(
        0xFE,
        "イ・リ・ア・さま～！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "ポリセは雨なんかに負けませんからー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_393A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39BC")

    #C0137
    ChrTalk(
        0xFE,
        (
            "最近よく、イリア様が\x01",
            "新人の女の子と一緒にいる\x01",
            "所を見かけるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "うう、何よあの子……\x01",
            "一体イリア様の何なわけっ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BC")

    TalkEnd(0xFE)
    Return()

    # Function_11_3081 end

    def Function_12_39C0(): pass

    label("Function_12_39C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A26")

    #C0139
    ChrTalk(
        0xFE,
        (
            "うおおっ……\x01",
            "よく言ってくれたぜ、大統領！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "俺たちは今こそ自由になるんだ！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A90")

    #C0141
    ChrTalk(
        0xFE,
        (
            "イリア様……\x01",
            "まだ目を覚まさないんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……くそっ、\x01",
            "マジでワケ分かんねえよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3B37")

    #C0143
    ChrTalk(
        0xFE,
        (
            "よ～し、今日は一日中\x01",
            "エールを送らせてもらうとするか！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "#4Sアルカンシェルの皆さ～ん！\x01",
            "俺たちファンはいつも\x01",
            "貴方たちを見守ってますからね～！！#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BCD")

    #C0145
    ChrTalk(
        0xFE,
        (
            "へへっ、きっと今頃は中で\x01",
            "リハーサルでもしてるんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "#4Sアルカンシェル、バンザ～イ！\x01",
            "リニューアル公演、バンザ～イ！！#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C55")

    #C0147
    ChrTalk(
        0xFE,
        (
            "イリア様、リーシャさん、\x01",
            "シュリちゃん、そして\x01",
            "プリエさんにセリーヌさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "#4Sみんな、みんな大好きだぁ～っ！#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C9C")

    #C0149
    ChrTalk(
        0xFE,
        (
            "おいポリセ、よだれよだれ……\x01",
            "それに表情がこえーよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D38")

    #C0150
    ChrTalk(
        0xFE,
        (
            "イリア様にリーシャさん、\x01",
            "そしてシュリちゃんが演じる\x01",
            "３人の姫、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "今回は念願のチケットも\x01",
            "手に入れたし……\x01",
            "マジで楽しみすぎるぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DEC")

    #C0152
    ChrTalk(
        0xFE,
        (
            "リニューアル公演の準備のために、\x01",
            "アルカンシェルは\x01",
            "もうすぐ休みに入るみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "その間、劇場の内部では\x01",
            "秘密の舞台稽古が……\x01",
            "死んでもいいから見てみたいぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E38")

    #C0154
    ChrTalk(
        0xFE,
        (
            "そうだよな～……\x01",
            "いくら首脳だからって\x01",
            "優遇されすぎだぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EE4")

    #C0155
    ChrTalk(
        0xFE,
        (
            "ポリセの奴、\x01",
            "やっとの思いとか言って\x01",
            "チケットを融通したのは俺なんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "へへっ、まあいいか。\x01",
            "同じ志を持つ追っかけ仲間同士、\x01",
            "そこは助け合いだからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F6F")

    #C0157
    ChrTalk(
        0xFE,
        (
            "へへっ、こんな日は\x01",
            "他の追っかけに差を付ける\x01",
            "チャンスだぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "#4Sイリア様～、リーシャさ～ん！\x01",
            "大好きだぁあ～～！！#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403D")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    #C0159
    ChrTalk(
        0xFE,
        "おや、あんたは……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "前に何度か劇場に\x01",
            "出入りする所を見たけど、\x01",
            "確か警察の人だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "いいよな～、警察は。\x01",
            "仕事で劇場に入れるんだもんな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4152")

    label("loc_403D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E4")

    #C0162
    ChrTalk(
        0xFE,
        (
            "俺も警察学校を受けて、\x01",
            "警官を目指すかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "そしたらパトロールにかこつけて\x01",
            "毎日アルカンシェルに……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#00006F（いや、それはダメだろ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4152")

    label("loc_40E4")


    #C0165
    ChrTalk(
        0xFE,
        (
            "俺も警察学校を受けて、\x01",
            "警官を目指すかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "そしたらパトロールにかこつけて\x01",
            "毎日アルカンシェルに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4152")

    TalkEnd(0xFE)
    Return()

    # Function_12_39C0 end

    def Function_13_4156(): pass

    label("Function_13_4156")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4215")

    #C0167
    ChrTalk(
        0xFE,
        (
            "何となく噂はあったけど、\x01",
            "まさか２大国がそんな\x01",
            "卑劣なことをしていたなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "私は大統領の主張に心から賛成よ。\x01",
            "今立ち上がらなきゃ、\x01",
            "同じ悲劇を繰り返すだけだもの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_4215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_42B1")

    #C0169
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの舞台、\x01",
            "本当なら今日観る\x01",
            "予定だったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "あんな事が起こったんじゃ\x01",
            "仕方ないわよね……\x01",
            "イリア様、大丈夫かしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_42B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_431D")

    #C0171
    ChrTalk(
        0xFE,
        (
            "マインツの事件……\x01",
            "本当に恐ろしい話よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "早く警備隊の人たちに\x01",
            "何とかして欲しいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_431D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_432B")
    Jump("loc_4C22")

    label("loc_432B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_439B")

    #C0173
    ChrTalk(
        0xFE,
        (
            "何だか、中央広場の方が\x01",
            "騒がしいみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "よく分からないけど、\x01",
            "事故でもあったのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_439B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_44C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4469")

    #C0175
    ChrTalk(
        0xFE,
        (
            "リニューアル舞台の公開日、\x01",
            "いよいよ明後日に迫ったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "流石に公開初日のチケットは\x01",
            "手に入らなかったけど、\x01",
            "来週には私も観に行く予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        "うふふ、気持ちが昂ぶるわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_44C0")

    label("loc_4469")


    #C0178
    ChrTalk(
        0xFE,
        (
            "リニューアル舞台、\x01",
            "来週には私も観に行く予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "うふふ、気持ちが昂ぶるわ。\x02",
    )

    CloseMessageWindow()

    label("loc_44C0")

    Jump("loc_4C22")

    label("loc_44C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_462C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F5")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    #C0180
    ChrTalk(
        0xFE,
        (
            "あら、ワジ君。\x01",
            "この前はどうもありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "ふふ、おかげ様で\x01",
            "夢のような一時を過ごせたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、こちらこそ。\x01",
            "そう言ってもらえて嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003F（ワジのやつ……\x01",
            "  いつの間にか、ちゃっかり\x01",
            "  ホストの仕事をしてるんだよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4627")

    label("loc_45F5")

    TurnDirection(0xFE, 0x105, 0)

    #C0184
    ChrTalk(
        0xFE,
        (
            "ふふ、ワジ君。\x01",
            "また遊びに行くからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4627")

    Jump("loc_4C22")

    label("loc_462C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46FD")

    #C0185
    ChrTalk(
        0xFE,
        (
            "ふと思ったんだけど、\x01",
            "ハルトマン元議長って\x01",
            "今は留置場にいるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "あれだけ大物だった人物が\x01",
            "もうすっかり世間の話題にすら\x01",
            "上がらないんだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "人って結構、薄情よね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_475B")

    label("loc_46FD")


    #C0188
    ChrTalk(
        0xFE,
        (
            "ハルトマン元議長も、\x01",
            "世間の話題にすら\x01",
            "上がらないんだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        "人って結構、薄情よね。\x02",
    )

    CloseMessageWindow()

    label("loc_475B")

    Jump("loc_4C22")

    label("loc_4760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47D6")

    #C0190
    ChrTalk(
        0xFE,
        (
            "オルキスタワー……\x01",
            "ついにその姿を現したわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "ふふ、建物を見て\x01",
            "こんなに興奮したのは始めてよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_47D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4894")

    #C0192
    ChrTalk(
        0xFE,
        (
            "高級クラブ《ノイエ＝ブラン》……\x01",
            "最近、新装開店したって噂だけど\x01",
            "ぜひ一度行ってみたいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "でも、あそこって\x01",
            "確か完全会員制なのよね……\x01",
            "誰か連れて行ってくれないかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_4894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48A2")
    Jump("loc_4C22")

    label("loc_48A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8D")
    TurnDirection(0xFE, 0x105, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0194
    ChrTalk(
        0xFE,
        (
            "あら、あなた……もしかして\x01",
            "ホストのワジ君じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x105,
        "#10305Fおや、僕のことを知ってるのかい？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "この界隈に\x01",
            "素敵なホストがいるって\x01",
            "前々から聞いていたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "うふふ、噂どおりの素敵な子ね。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、それはどうも。\x02\x03",

            "#10302Fもし良かったらお店に来るといい。\x01",
            "そこでならゆっくりお話させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "うふふ、是非今度行かせてもらうわね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5E")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A84")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAA")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4AAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AD0")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4AD0")

    Sleep(1000)

    #C0200
    ChrTalk(
        0x102,
        (
            "#00106F（さ、さすがワジ君、\x01",
            "  よく顔が知れているわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00006F（っていうか、\x01",
            "  俺たちの前で堂々と営業を……）\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x109,
        (
            "#10101F（まったくもう……\x01",
            "  後で厳重注意ですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 1)
    Jump("loc_4C22")

    label("loc_4B8D")


    #C0203
    ChrTalk(
        0xFE,
        (
            "この界隈に素敵なホストがいるって\x01",
            "前々から聞いていたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "うふふ、是非今度\x01",
            "お店に行かせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x105,
        "#10302Fフフ、お待ちしてるよ。\x02",
    )

    CloseMessageWindow()

    label("loc_4C22")

    TalkEnd(0xFE)
    Return()

    # Function_13_4156 end

    def Function_14_4C26(): pass

    label("Function_14_4C26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CA7")

    #C0206
    ChrTalk(
        0xFE,
        (
            "『クロスベル独立国』か……\x01",
            "へへ、悪くない響きだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "これから俺たちは、\x01",
            "市民じゃなくて国民ってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_4CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D76")

    #C0208
    ChrTalk(
        0xFE,
        (
            "最近やっと落ち着いて来たけど、\x01",
            "あの襲撃があってから\x01",
            "何か街全体が暗い感じがするよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "でも俺は思うんだ。\x01",
            "だからこそ、いつもより余計に遊んで\x01",
            "景気を活性化させないとってな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4D9E")

    label("loc_4D76")


    #C0210
    ChrTalk(
        0xFE,
        "さて、ってなわけで今日も遊ぶぞ～。\x02",
    )

    CloseMessageWindow()

    label("loc_4D9E")

    Jump("loc_5521")

    label("loc_4DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E48")

    #C0211
    ChrTalk(
        0xFE,
        (
            "何かマインツの方が大変らしいけど、\x01",
            "俺たちが慌てたって仕方ないよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "だから俺は、いつものように\x01",
            "この歓楽街で遊び倒すつもりだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4EB6")

    label("loc_4E48")


    #C0213
    ChrTalk(
        0xFE,
        (
            "そういや、今日って\x01",
            "リニューアル舞台の公開日なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "へへっ、初日から\x01",
            "見られるヤツが羨ましいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB6")

    Jump("loc_5521")

    label("loc_4EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F3D")

    #C0215
    ChrTalk(
        0xFE,
        (
            "さ～て、今日は\x01",
            "どこぞのバーにでも入るかな～？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "へへっ、こんな日にしっぽり\x01",
            "独り酒っつうのも悪くねえよな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_4F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4FD8")

    #C0217
    ChrTalk(
        0xFE,
        "カジノでスロットをしてたんだけど……\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "はぁ～、ダメだ。\x01",
            "どうやら今日は運に見放されたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "こんな日はさっさと帰って寝るかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_4FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_505A")

    #C0220
    ChrTalk(
        0xFE,
        (
            "カジノのスロットに\x01",
            "必勝法ってないのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "なんだかよく出る台と出ない台が\x01",
            "ありそうな気がするんだよな～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_505A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_513A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DA")

    #C0222
    ChrTalk(
        0xFE,
        "さてと、今日も張り切って遊ぶか～。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "今日の手持ちは、と……\x01",
            "やべえ、そろそろ補充しねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5135")

    label("loc_50DA")


    #C0224
    ChrTalk(
        0xFE,
        "最近、負けが続いたからな～。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "しゃーない、また親に\x01",
            "ゴマすって小遣いせびるかなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5135")

    Jump("loc_5521")

    label("loc_513A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51EC")

    #C0226
    ChrTalk(
        0xFE,
        (
            "アルカンシェル、\x01",
            "次に予定されている公演を最後に\x01",
            "しばらく休みに入るんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "リニューアル舞台の準備を\x01",
            "本格的に開始するって話だけど、\x01",
            "ホント楽しみだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_51EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_52EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529B")

    #C0228
    ChrTalk(
        0xFE,
        (
            "流石に近くでは見れなかったけど、\x01",
            "一応除幕式ってのを見てきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "オルキスタワー、すげえよなー。\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "へへっ、\x01",
            "この街は本当に景気がいいぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_52EA")

    label("loc_529B")


    #C0231
    ChrTalk(
        0xFE,
        "オルキスタワー、すげえよなー。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "へへっ、\x01",
            "この街は本当に景気がいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52EA")

    Jump("loc_5521")

    label("loc_52EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C2")

    #C0233
    ChrTalk(
        0xFE,
        (
            "あー、何か至る所で\x01",
            "警官がウロウロしてんな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "確か明日から通商会議ってのが\x01",
            "始まるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "その影響ってのは分かるけど、\x01",
            "正直この辺りをうろつかれるのは\x01",
            "カンベンだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5422")

    label("loc_53C2")


    #C0236
    ChrTalk(
        0xFE,
        (
            "俺、別に悪いことは\x01",
            "していないはずなんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "警官がいると\x01",
            "何か遊びにくいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5422")

    Jump("loc_5521")

    label("loc_5427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_54AE")

    #C0238
    ChrTalk(
        0xFE,
        (
            "へへっ、雨だからって\x01",
            "家にこもってちゃ\x01",
            "真の遊び人とは言えねえよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "さてと、今日も\x01",
            "浮かれまくるとするかぁ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_54AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5521")

    #C0240
    ChrTalk(
        0xFE,
        "おっし、今日も遊び倒すぞ～。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "まずはどっかのカジノで\x01",
            "スロットでも打って\x01",
            "今日の運でも試すかなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5521")

    TalkEnd(0xFE)
    Return()

    # Function_14_4C26 end

    def Function_15_5525(): pass

    label("Function_15_5525")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_560C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B2")

    #C0242
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "カジノハウス《バルカ》は\x01",
            "今日もアゲアゲよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "みんな、遊んで行ってね～ン。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5607")

    label("loc_55B2")


    #C0245
    ChrTalk(
        0xFE,
        (
            "カジノハウス《バルカ》は\x01",
            "今日もアゲアゲよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        "みんな、遊んで行ってね～ン。\x02",
    )

    CloseMessageWindow()

    label("loc_5607")

    Jump("loc_5FCD")

    label("loc_560C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5658")

    #C0247
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        "カジノで元気注入してかな～い？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_5658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_574E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56EB")

    #C0249
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "うふふ、ついに\x01",
            "リニューアル公演の日が\x01",
            "来たわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        "みんな、元気出さなきゃヤ～よ～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5749")

    label("loc_56EB")


    #C0252
    ChrTalk(
        0xFE,
        (
            "うふふ、ついに\x01",
            "リニューアル公演の日が\x01",
            "来たわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "みんな、元気出さなきゃヤ～よ～？\x02",
    )

    CloseMessageWindow()

    label("loc_5749")

    Jump("loc_5FCD")

    label("loc_574E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_57A1")

    #C0254
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "よければ、ウチで\x01",
            "雨宿りしてかな～い？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_57A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57F6")

    #C0256
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "うふふ、チップなら\x01",
            "いつでも大歓迎よ～㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_57F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5851")

    #C0258
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "うふふ、今日もたっぷり\x01",
            "サービスしちゃうぞっ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_5851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_598F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5908")

    #C0260
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "わたしってば、いつもこんな\x01",
            "格好をしてるワケじゃないのよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "うふふ、カレシに頼まれたら\x01",
            "プライベートで着ていいけどね～㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_598A")

    label("loc_5908")


    #C0263
    ChrTalk(
        0xFE,
        (
            "わたしってば、いつもこんな\x01",
            "格好をしてるワケじゃないのよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "うふふ、カレシに頼まれたら\x01",
            "プライベートで着ていいけどね～㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_598A")

    Jump("loc_5FCD")

    label("loc_598F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A24")

    #C0265
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "今日も日差しが強いわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "これじゃまた、\x01",
            "日焼け跡が出来ちゃうわ～ん㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5A84")

    label("loc_5A24")


    #C0268
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "今日も日差しが強いわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "これじゃまた、\x01",
            "日焼け跡が出来ちゃうわ～ん㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A84")

    Jump("loc_5FCD")

    label("loc_5A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3D")

    #C0270
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "今日は首脳のみなさんが\x01",
            "アルカンシェルの舞台を\x01",
            "観に来るんだってね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "うふふ、ついでにウチに\x01",
            "寄ってくれないかしら～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5BBC")

    label("loc_5B3D")


    #C0273
    ChrTalk(
        0xFE,
        (
            "今日は首脳のみなさんが\x01",
            "アルカンシェルの舞台を\x01",
            "観に来るんだってね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "うふふ、ついでにウチに\x01",
            "寄ってくれないかしら～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BBC")

    Jump("loc_5FCD")

    label("loc_5BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DB2")

    #C0275
    ChrTalk(
        0xFE,
        (
            "あら、ランディさんじゃない。\x01",
            "長いこと顔も出さずに\x01",
            "いったい何してたのよぉ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        (
            "#00304Fああ、悪ぃ。\x01",
            "ちょっと野暮用でな。\x02\x03",

            "#00300F今度おごるから許してくれねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "うふふ、許すも何も\x01",
            "その手には乗らないんだからぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "悪いと思ってるのなら\x01",
            "ウチでミラを落として行ってね～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#00309Fはは、相変わらず商売上手だな。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x109,
        (
            "#10100F（何ていうかランディ先輩……\x01",
            "  慣れてますね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#00000F（ああ、まあここはランディにとって\x01",
            "  ホームみたいなものらしいからな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 4)
    Jump("loc_5DFC")

    label("loc_5DB2")


    #C0282
    ChrTalk(
        0xFE,
        (
            "ランディさん、\x01",
            "悪いと思ってるのなら\x01",
            "ウチでミラを落として行ってね～☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFC")

    Jump("loc_5FCD")

    label("loc_5E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E6F")

    #C0283
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "こんな日はウチで\x01",
            "パ～ッと明るく楽しく\x01",
            "過ごすのがオススメよ～ン㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_5E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F28")

    #C0285
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "え、赤毛の男の人が\x01",
            "来なかったかって？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "あなた、お友達～？\x01",
            "その人なら、ついさっき\x01",
            "お店に来たところよ～ん㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5F7D")

    label("loc_5F28")


    #C0288
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "赤毛の男の人なら、ついさっき\x01",
            "お店に来たところよ～ん㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7D")

    Jump("loc_5FCD")

    label("loc_5F82")


    #C0290
    ChrTalk(
        0xFE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "うふふ、今日も\x01",
            "う～んと楽しんで行ってね～㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FCD")

    TalkEnd(0xFE)
    Return()

    # Function_15_5525 end

    def Function_16_5FD1(): pass

    label("Function_16_5FD1")

    TalkBegin(0xFE)

    #C0292
    ChrTalk(
        0xFE,
        (
            "ここが、あの有名な\x01",
            "《アルカンシェル》……\x01",
            "ふふ、やっと来たわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "チケットも前もって\x01",
            "手に入れてあるし、\x01",
            "あとは公演を待つだけね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_5FD1 end

    def Function_17_6062(): pass

    label("Function_17_6062")

    TalkBegin(0xFE)

    #C0294
    ChrTalk(
        0xFE,
        (
            "最高傑作の呼び声高い、\x01",
            "『金の太陽、銀の月』か。\x01",
            "楽しみで仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "けど、劇が始まる直前まで\x01",
            "開場はしていないみたいだね。\x01",
            "どこで時間を潰すかな？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_6062 end

    def Function_18_6105(): pass

    label("Function_18_6105")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_627A")
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

    def lambda_6230():
        OP_96(0xFE, 0xFFFFE0D4, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6230)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 14040, 0, 11290, 90)

    def lambda_6265():
        OP_95(0xFE, 37920, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6265)

    label("loc_627A")

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

    # Function_18_6105 end

    def Function_19_62F8(): pass

    label("Function_19_62F8")

    SetChrPos(0xFE, 13050, 0, -18750, 225)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -8000, 0, -600)
    OP_9F(0x1, -24250, 0, 8350)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_19_62F8 end

    def Function_20_6333(): pass

    label("Function_20_6333")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_648E")
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

    def lambda_645E():
        OP_96(0xFE, 0x3F15, 0x0, 0xFFFFAF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_645E)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, -3100, 1760, 9570, 180)

    label("loc_648E")

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

    # Function_20_6333 end

    def Function_21_6510(): pass

    label("Function_21_6510")

    SetChrPos(0xFE, -24950, 0, 8900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -10800, 0, 1900)
    OP_9F(0x1, 4150, 0, -2750)
    OP_9F(0x1, 10500, 0, 5450)
    OP_9F(0x1, 22600, 0, 11200)
    OP_9F(0x1, 38350, 0, 11900)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_21_6510 end

    def Function_22_6575(): pass

    label("Function_22_6575")

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
        "#00007F#5Pランディ……！\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        "#00101F#6P追いかけましょう！\x02",
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
            "バーストゲージが解除されました。\x02",
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
            "※各章のストーリーが佳境を過ぎると\x01",
            "　いったんバーストが使用できなくなります。\x02\x03",

            "※ただし次の章のストーリーが佳境に\x01",
            "　差しかかった時、再び使えるようになります。\x02\x03",

            "※その場合、最初の戦闘に突入した時、\x01",
            "　戦闘画面右上にバーストゲージが\x01",
            "　再び出現するので注意してください。\x02",
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

    # Function_22_6575 end

    def Function_23_69AE(): pass

    label("Function_23_69AE")

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

    # Function_23_69AE end

    def Function_24_6A4B(): pass

    label("Function_24_6A4B")


    def lambda_6A50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A50)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_6A4B end

    def Function_25_6A82(): pass

    label("Function_25_6A82")

    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x162, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_25_6A82 end

    def Function_26_6AAF(): pass

    label("Function_26_6AAF")

    Sleep(200)

    def lambda_6AB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6AB7)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x2D, 0xABE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_6AAF end

    def Function_27_6AE9(): pass

    label("Function_27_6AE9")

    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1770, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_27_6AE9 end

    def Function_28_6B0B(): pass

    label("Function_28_6B0B")

    Sleep(800)

    def lambda_6B13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B13)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x159, 0x190, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_28_6B0B end

    def Function_29_6B45(): pass

    label("Function_29_6B45")

    Sleep(100)
    OP_93(0xFE, 0x7D, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_29_6B45 end

    def Function_30_6B80(): pass

    label("Function_30_6B80")

    Sleep(100)

    def lambda_6B88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B88)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x1E, 0x1F4, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_30_6B80 end

    def Function_31_6BD7(): pass

    label("Function_31_6BD7")

    Sleep(500)

    def lambda_6BDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BDF)
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

    # Function_31_6BD7 end

    def Function_32_6C7D(): pass

    label("Function_32_6C7D")

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
            "#12P#00101F……昨夜から今朝にかけての\x01",
            "ランディの動きが見えてきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#5P#00003Fああ、軽く整理してみよう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_6E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70FF")
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
            "#1K最初にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EC4")
    ClearScenarioFlags(0x0, 0)

    label("loc_6EC4")

    SetChrName("")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K次にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F55")
    ClearScenarioFlags(0x0, 0)

    label("loc_6F55")

    SetChrName("")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K最後にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FF1")
    ClearScenarioFlags(0x0, 0)

    label("loc_6FF1")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7083")

    #C0306
    ChrTalk(
        0x101,
        (
            "#5P#00003F（いや……\x01",
            "  この順番じゃないはずだ。）\x02\x03",

            "#00001F（もう一度整理してみよう。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_707E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_707E")

    Jump("loc_70FA")

    label("loc_7083")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7093"),
        (SWITCH_DEFAULT, "loc_70C9"),
    )


    label("loc_7093")

    OP_2C(0xAA, 0x1)

    #C0307
    ChrTalk(
        0x101,
        "#5P#00000F（間違いない、この順番だ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FA")

    label("loc_70C9")


    #C0308
    ChrTalk(
        0x101,
        "#5P#00003F（……多分、この順番だな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FA")

    label("loc_70FA")

    Jump("loc_6E10")

    label("loc_70FF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３時～４時　カジノバー《バルカ》\x01",
            "５時～６時　修理屋《ギヨーム工房》\x01",
            "６時～　　　交換屋《ナインヴァリ》\x07\x00\x02",
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
            "#5P#00006F──おそらく最初に\x01",
            "ドレイク・オーナーに預けていた\x01",
            "トランクを受け取ったんだろう。\x02\x03",

            "#00008Fそのトランクに入っていたのは\x01",
            "ランディの猟兵時代の得物……\x02\x03",

            "#00001F多分、かなりの攻撃力を誇る\x01",
            "導力ライフルじゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        (
            "#6P#00203F普通、そうしたライフルは\x01",
            "分解した状態で持ち運ぶはずです。\x02\x03",

            "#00201F２年ほど使っていなかったため、\x01",
            "ランディさんは分解されたユニットを\x01",
            "修理工房で整備してもらった……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x109,
        (
            "#10103F#11P──うん、間違いないと思う。\x02\x03",

            "#10108F武装の整備は、戦場での生死を\x01",
            "左右するものだから……\x02\x03",

            "#10101Fランディ先輩なら絶対に\x01",
            "綿密にチェックしたはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x105,
        (
            "#12P#10303F最後に、交換屋に寄って\x01",
            "色々と仕入れたみたいだけど……\x02\x03",

            "#10301F火薬の弾薬も仕入れたってことは\x01",
            "かなり特殊なライフルなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#12P#00108Fラインフォルト社の中には\x01",
            "導力式と火薬式を切り替えられる\x01",
            "ラインナップもあるそうだけど……\x02\x03",

            "#00101Fいずれにしても、相当特殊で\x01",
            "強化されたライフルでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#5P#00006Fああ、赤い星座の猟兵たちも\x01",
            "見たことのない巨大なライフルを\x01",
            "使っていたからな。\x02\x03",

            "#00013F──よし、これで大体、\x01",
            "ランディの状況は掴めたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x103,
        (
            "#6P#00206F最後にランディさんが交換屋を\x01",
            "訪れたのが今朝の６時過ぎ……\x02\x03",

            "#00208F現在、１０時くらいですから\x01",
            "４時間近くも経っていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x109,
        (
            "#10106F#11P今から先輩の足に追いつくのは\x01",
            "かなり難しそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#5P#00003F……いや、ランディだって\x01",
            "いくらタフでも限度があるはずだ。\x02\x03",

            "#00001F《赤い星座》に仕掛けるなら\x01",
            "さすがに仮眠くらいは取るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x105,
        (
            "#12P#10304Fその上で、地形の利を活かして\x01",
            "一気に仕掛けてケリを付ける……\x02\x03",

            "#10302Fま、玉砕覚悟で\x01",
            "特攻するつもりじゃなければ\x01",
            "そのあたりが妥当だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#12P#00101F……いずれにしても\x01",
            "もうそんなに余裕がないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#5P#00013Fああ、こうなったら駄目元で\x01",
            "マインツ方面に行くしか──\x02",
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

    def lambda_787C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_787C)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_78A1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_78A1)
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
        "#5P#00011Fまさか……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#6P#00205Fランディさんから……？\x02",
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
            "#00007F──はい、特務支援課、\x01",
            "ロイド・バニングスです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性の声")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やあ、ロイドさん。\x02\x03",

            "……フフ、どうやら別の誰かと\x01",
            "カン違いさせてしまったようですね。\x02",
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
            "#00005Fそ、その声は……\x02\x03",

            "#00013F……どうしてこの番号が？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性の声")

    #A0327
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、言ったでしょう。\x01",
            "ロイドさんたちのファンだと。\x02\x03",

            "──タイムズ百貨店。\x02\x03",

            "お暇でしたら是非、\x01",
            "屋上までいらしてください。\x07\x00\x02",
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
            "#6P#00201F……ロイドさん。\x01",
            "今の通信は……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        "#12P#00108Fい、一体誰だったの？\x02",
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
            "#5P#00003F……《黒月》のツァオだ。\x02\x03",

            "#00013F中央広場のデパートの\x01",
            "屋上で待っているらしい。\x02",
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
        "#10111F#11Pええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        (
            "#12P#10301Fこんな時に……\x01",
            "いったい何のつもりだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#5P#00006F……分からない。\x01",
            "ただ、あの男が意味もなく\x01",
            "連絡してくるとも思えない。\x02\x03",

            "#00001F山道に出る前に\x01",
            "寄るだけ寄ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        "#12P#00101Fわ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x103,
        "#6P#00201Fとにかく急ぎましょう。\x02",
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

    # Function_32_6C7D end

    def Function_33_7E3E(): pass

    label("Function_33_7E3E")

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

    # Function_33_7E3E end

    def Function_34_7FD3(): pass

    label("Function_34_7FD3")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_841B")

    #C0336
    ChrTalk(
        0x11,
        (
            "来てくれたわね、\x01",
            "特務支援課のみんな！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#00000Fケイト先輩、\x01",
            "お疲れさまです。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x109,
        (
            "#10105F暴走車の件について\x01",
            "あたしたちに協力してほしい\x01",
            "とのことですが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x105,
        (
            "#10300Fぜひ事情を\x01",
            "お聞かせ願いたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x11,
        (
            "ええ、じゃあさっそく\x01",
            "説明させてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x11,
        (
            "最近、危険運転をする車……\x01",
            "いわゆる『暴走車』が、市内を\x01",
            "好き勝手に走り回ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x11,
        (
            "人や物にぶつかるスレスレの\x01",
            "スリルを楽しんでる様子で、\x01",
            "各方面から苦情が来ているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#00003F確かに、さっきのは\x01",
            "かなり乱暴な運転だったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#00101F私も聞いたことがあるわ。\x02\x03",

            "クラクションなんかも\x01",
            "所構わず鳴らすものだから、\x01",
            "騒音も問題になってるらしいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        (
            "#10106Fどこの誰だか知らないですけど、\x01",
            "迷惑な人もいたものですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x11,
        (
            "うん、広域防犯課としては\x01",
            "早急に解決したい問題なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x11,
        (
            "そこで、あなたたち支援課に\x01",
            "あの暴走車を取り締まる\x01",
            "手伝いをしてもらいたくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x11,
        "どう、お願いできるかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8485")

    label("loc_841B")


    #C0349
    ChrTalk(
        0x11,
        (
            "あなたたち支援課に\x01",
            "あの暴走車を取り締まる\x01",
            "手伝いをしてもらいたいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        "どう、お願いできるかしら？\x02",
    )

    CloseMessageWindow()

    label("loc_8485")

    Call(0, 35)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11050, 0, 540, 225)
    EventEnd(0x5)
    Return()

    # Function_34_7FD3 end

    def Function_35_84A4(): pass

    label("Function_35_84A4")

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
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850F")
    Call(0, 36)
    Jump("loc_85F0")

    label("loc_850F")


    #C0351
    ChrTalk(
        0x101,
        (
            "#00006Fお手伝いしたいのは\x01",
            "やまやまなんですが……\x01",
            "今はちょっと別件がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x11,
        (
            "うーん、そっか。\x01",
            "あなたたちにも仕事があるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x11,
        (
            "話を聞いてくれてありがと。\x01",
            "とりあえず、なんとか\x01",
            "私たちだけで対処してみるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x130, 6)

    label("loc_85F0")

    Return()

    # Function_35_84A4 end

    def Function_36_85F1(): pass

    label("Function_36_85F1")


    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F分かりました、\x01",
            "俺たちに協力できることなら\x01",
            "いくらでも手伝わせてください。\x02\x03",

            "#00009Fはは、ケイト先輩には\x01",
            "警察学校時代から\x01",
            "お世話になってますしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x11,
        "ありがとう、助かるわ！\x02",
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
            "クエスト【暴走車の取り締まり】\x07\x00",
            "を開始した！\x02",
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
            "コホン、それじゃあまずは\x01",
            "犯人たちについて説明するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x11,
        (
            "暴走車を運転しているのは、\x01",
            "共和国出身と見られる若者３人組……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x11,
        (
            "ついこの間から、クロスベル市内で\x01",
            "目撃されるようになった子たちよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x11,
        (
            "彼らは港湾区の公園を拠点に\x01",
            "自治州内を走りまわっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x11,
        (
            "最近はマインツ山道なんかも\x01",
            "走行ルートに入っているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#00105F街道にまで……\x01",
            "バスの運行にも\x01",
            "影響がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        (
            "#00005Fあれ、でも……\x02\x03",

            "#00000F走行ルートが割れているなら\x01",
            "取り締まりはそこまで\x01",
            "難しくないんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x109,
        (
            "#10105F確かにそうですね。\x02\x03",

            "#10103Fパトカーを総動員すれば、\x01",
            "すぐにでも包囲網を敷くことが\x01",
            "できると思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x11,
        (
            "うーん、それが\x01",
            "そうもいかないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x11,
        (
            "下手に追い詰めたら、\x01",
            "きっと彼らも躍起になって\x01",
            "切り抜けようとするでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x11,
        (
            "無理な運転をさせて、\x01",
            "交通事故でも起こされたら\x01",
            "目も当てられないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#00003F……厄介ですね。\x02\x03",

            "#00001Fもしそんなことになったら\x01",
            "警察の責任になりそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x11,
        (
            "そこで、あなたたちには\x01",
            "知恵を貸してほしいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x11,
        (
            "市民に迷惑をかけず、\x01",
            "スマートに暴走車を捕まえる……\x01",
            "そのための知恵をね。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど……\x01",
            "一通り事情は分かりました。\x02",
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
            "#00000F重要な要素は\x01",
            "２つあると思います。\x02\x03",

            "#00003Fまず、走っている暴走車を\x01",
            "安全に止めるための『方法』……\x02\x03",

            "#00000Fそして、その方法を使っても\x01",
            "市民たちに悪影響が出ない『場所』。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#00103F確かに、どちらが欠けても\x01",
            "安全に暴走車を取り締まることは\x01",
            "出来ないでしょうね。\x02\x03",

            "#00100Fだったらまずは、\x01",
            "『方法』から考えてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x105,
        (
            "#10304Fふむ、やり方はいくつでも\x01",
            "考えられると思うけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x109,
        (
            "#10101Fやはり、最も優先すべきは\x01",
            "事故が起きる可能性が低い、\x01",
            "ということでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x11,
        (
            "ええ、もちろん。\x01",
            "市民を巻き込む確率は\x01",
            "最小限にしたいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x11,
        (
            "そう考えると、ある程度\x01",
            "『方法』は絞られると思うけど……\x01",
            "何かいい案はあるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        "#00003Fそうですね……\x02",
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
            "#1K暴走車を安全に止める方法は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "パトカーで進路を塞ぐ\x01",      # 0
            "路面に罠を仕掛ける\x01",        # 1
            "行き止まりに誘い込む\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F3D")
    OP_2C(0x69, 0x1)

    #C0380
    ChrTalk(
        0x101,
        (
            "#00000F行き止まりに誘い込む……\x01",
            "というのはどうでしょうか？\x02\x03",

            "それ以上、暴走車が\x01",
            "進行不可能な状態にしてしまえば、\x01",
            "止まらざるを得ない筈です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9230")

    label("loc_8F3D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F53"),
        (1, "loc_9057"),
        (SWITCH_DEFAULT, "loc_9162"),
    )


    label("loc_8F53")


    #C0381
    ChrTalk(
        0x101,
        (
            "#00000Fパトカーで進路を塞ぐ……\x01",
            "というのはどうでしょうか？\x02\x03",

            "車両を壁にすれば、\x01",
            "いくら暴走車でも止まらざるを……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x109,
        (
            "#10106Fう、うーん……\x01",
            "それはちょっと強引過ぎる\x01",
            "気がしますけど。\x02\x03",

            "#10101Fブレーキをかけ損ねて\x01",
            "パトカーと衝突する\x01",
            "可能性もありますし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9162")

    label("loc_9057")


    #C0383
    ChrTalk(
        0x101,
        (
            "#00000F路面に罠を仕掛ける……\x01",
            "というのはどうでしょうか？\x02\x03",

            "針のようなものでタイヤを\x01",
            "パンクさせてしまえば……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x109,
        (
            "#10106Fう、うーん……\x01",
            "そういう道具もあるとは\x01",
            "聞いたことがありますけど……\x02\x03",

            "#10101Fクロスベル市でそれをやると、\x01",
            "大事故に繋がってしまいそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9162")

    label("loc_9162")


    #C0385
    ChrTalk(
        0x101,
        "#00006Fた、確かにそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0386
    ChrTalk(
        0x101,
        (
            "#00000F……だったら、行き止まりに\x01",
            "誘い込むというのはどうでしょう？\x02\x03",

            "それ以上、暴走車が\x01",
            "進行不可能な状態にしてしまえば、\x01",
            "止まらざるを得ない筈です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9230")


    #C0387
    ChrTalk(
        0x11,
        (
            "なるほど……\x01",
            "それなら安全に暴走車を\x01",
            "止めることができそうね！\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x102,
        (
            "#00106Fでも、行き止まりねえ……\x01",
            "使えそうな場所がパッと\x01",
            "思い浮かばないけれど。\x02\x03",

            "#00100F新市庁ビルやＩＢＣの敷地なんかは\x01",
            "さすがに利用できないでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#00003Fうーん、そうか……\x01",
            "いい考えだと思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、だったら……\x01",
            "作ってしまえばいいんじゃない？\x02\x03",

            "#10300F建設現場で使われるような\x01",
            "土嚢とかで、バリケードを作ってさ。\x02",
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
        "うん、いい考えね！\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x11,
        (
            "その方法なら、どこにでも\x01",
            "行き止まりを作れると思うわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x109,
        "#10100Fふふっ、冴えてるね。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、どういたしまして。\x02\x03",

            "#10300Fとすると、次に問題になるのは\x01",
            "行き止まりを作る『場所』だね。\x02\x03",

            "一応、暴走車のルートは\x01",
            "広域防犯課の方で把握してるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x11,
        "ええ、もちろん把握しているわ。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x11,
        (
            "暴走車が使っているルートは、\x01",
            "基本的にクロスベル市内を\x01",
            "大きく一周しているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x11,
        (
            "歓楽街⇒行政区⇒港湾区⇒\x01",
            "東通り⇒中央広場⇒裏通り……\x01",
            "そして再び歓楽街っていう具合ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x102,
        (
            "#00100Fとなると、その６つの区画の\x01",
            "どこかに行き止まりを設置して、\x01",
            "そこに誘い込む形がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x11,
        (
            "比較的人通りが少なくて、\x01",
            "市民に迷惑がかかりづらい\x01",
            "場所が望ましいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x11,
        (
            "暴走車のルート上に、\x01",
            "そんな場所はなかったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#00003Fそうですね……\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98E1")
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
            "#1K暴走車を止めるのに相応しい場所は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "歓楽街\x01",        # 0
            "行政区\x01",        # 1
            "港湾区\x01",        # 2
            "東通り\x01",        # 3
            "中央広場\x01",      # 4
            "裏通り\x01",        # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9830")

    #C0403
    ChrTalk(
        0x101,
        (
            "#00000Fその条件に当てはまるのは、\x01",
            "行政区だけだと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982B")
    OP_2C(0x69, 0x1)

    label("loc_982B")

    Jump("loc_98DC")

    label("loc_9830")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0404
    ChrTalk(
        0x101,
        (
            "#00003F（……いや、その場所は\x01",
            "  やめておいた方がいいだろう。）\x02\x03",

            "（比較的人通りが少なくて、\x01",
            "  市民に迷惑がかかりづらい場所。\x01",
            "  その条件に当てはまるのは……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98DC")

    Jump("loc_9727")

    label("loc_98E1")


    #C0405
    ChrTalk(
        0x105,
        (
            "#10300F行政区……\x01",
            "市民会館や図書館、\x01",
            "警察本部がある区画だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x102,
        (
            "#00100F確かにあそこなら\x01",
            "人通りも比較的少ないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x109,
        (
            "#10100Fええ、交通事故が起きたとしても\x01",
            "被害は最小限にできそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x11,
        (
            "加えて、警察本部も近くて\x01",
            "作戦にはもってこいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x11,
        (
            "……うん、これなら\x01",
            "なんとかいけそうだわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x11,
        (
            "ふふっ、さすが特務支援課ね！\x01",
            "あっという間に作戦が決まっちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        "#00009Fはは、先輩のお役に立てて光栄ですよ。\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x11,
        (
            "あとは、暴走車を行き止まりに\x01",
            "誘い込むために、\x01",
            "何台かパトカーが要りそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x11,
        (
            "よーし、それじゃあ\x01",
            "広域防犯課のみんなに通達して、\x01",
            "さっそく作戦を開始しましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x11,
        (
            "ロイドくんたちには、\x01",
            "バリケードの準備を頼んだわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        "#00000Fええ、お手伝いさせていただきます。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x105,
        "#10309Fフフ、面白くなってきたじゃない。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        (
            "#00100Fやるからには\x01",
            "気合を入れてやりましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x109,
        (
            "#10100Fええ、絶対に暴走車を\x01",
            "捕まえてやりましょう！！\x02",
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

    # Function_36_85F1 end

    def Function_37_9C50(): pass

    label("Function_37_9C50")

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

    def lambda_9D4B():
        OP_95(0xFE, -8119, 1770, 11630, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9D4B)
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
        "#5P#00005F……いたぞ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0420
    ChrTalk(
        0x102,
        (
            "#12P#00100Fここからは、ちょっと\x01",
            "慎重になった方が良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0421
    ChrTalk(
        0x101,
        (
            "#11P#00003Fああ、これ以上他の街区に\x01",
            "行かれないよう回り込もう。\x02\x03",

            "#00000F俺とエリィは迂回して\x01",
            "行政区方面から近付くから、\x01",
            "ノエルとワジは裏通り方面を。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0422
    ChrTalk(
        0x109,
        "#6P#10100F了解です。\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x105,
        "#6P#10302F了解#4Rヤー#。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)
    Sleep(300)

    #C0424
    ChrTalk(
        0x101,
        (
            "#11P#00000Fランディと君は\x01",
            "このまま住宅街方面から頼む。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    #C0425
    ChrTalk(
        0x104,
        "#6P#00303F……わーった。\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x1A3,
        "#5P#04609Fあはは、包囲戦だね♪\x02",
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

    def lambda_A04B():
        OP_95(0xFE, 13360, 0, 10870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A04B)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(13490, 1950, 10070, 5000)
    MoveCamera(42, 30, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9450, 5000)

    def lambda_A0A0():
        OP_95(0xFE, 15810, 0, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0A0)
    Sleep(50)

    def lambda_A0BD():
        OP_95(0xFE, 15710, 0, 10230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0BD)
    WaitChrThread(0x101, 1)

    def lambda_A0DB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0DB)
    WaitChrThread(0x102, 1)

    def lambda_A0EC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0EC)
    OP_6F(0x79)

    #C0427
    ChrTalk(
        0x101,
        (
            "#00000Fさあ、マリー。\x01",
            "こっちへおいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x102,
        (
            "#00100F心配しないでいいからね。\x01",
            "私たちがお家に帰してあげるから。\x02",
        )
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    def lambda_A173():
        OP_95(0xFE, 9930, 0, 4040, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A173)
    Sleep(50)

    def lambda_A190():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A190)
    Sleep(50)

    def lambda_A1A0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1A0)
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

    def lambda_A21A():
        OP_95(0xFE, 7970, 0, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A21A)
    Sleep(50)

    def lambda_A237():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A237)
    Sleep(50)

    def lambda_A24F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A24F)
    OP_0D()
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x87, 0x1F4)
    Sleep(300)

    #C0429
    ChrTalk(
        0x109,
        "#10100Fマリーちゃん、怖がらないで。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、観念して\x01",
            "大人しくしてくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A2D0():
        OP_95(0xFE, 440, 0, -6930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A2D0)
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

    def lambda_A357():
        OP_95(0xFE, -28830, 0, 10230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A357)
    Sleep(50)

    def lambda_A374():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A374)
    Sleep(50)

    def lambda_A38C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_A38C)
    OP_0D()
    WaitChrThread(0x14, 1)

    #C0431
    ChrTalk(
        0x1A3,
        "#04602Fほらほら、何もしないよー？\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x104,
        (
            "#00303F（……ったく。\x01",
            "  こういう所は変わらねぇな。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A407():
        OP_95(0xFE, -8119, 1770, 11630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A407)
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

    def lambda_A506():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A506)
    Sleep(50)

    def lambda_A51E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A51E)
    Sleep(50)

    def lambda_A536():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A536)
    Sleep(50)

    def lambda_A54E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A54E)
    Sleep(50)

    def lambda_A566():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A566)
    Sleep(50)

    def lambda_A57E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_A57E)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_A5A8():
        OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A5A8)
    WaitChrThread(0x14, 1)
    OP_6F(0x10)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0433
    ChrTalk(
        0x8,
        "あ、猫だ！　超可愛いー㈱\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x9,
        (
            "#11Pしかも、まだ仔猫じゃん。\x01",
            "癒されるな～。\x02",
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
        "#11P#N#00011Fしまった──\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x14, 0x1)
    OP_64(0x14)

    def lambda_A6B5():

        label("loc_A6B5")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6B5")

    QueueWorkItem2(0x101, 1, lambda_A6B5)

    def lambda_A6C7():

        label("loc_A6C7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6C7")

    QueueWorkItem2(0x104, 1, lambda_A6C7)

    def lambda_A6D9():

        label("loc_A6D9")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6D9")

    QueueWorkItem2(0x102, 1, lambda_A6D9)

    def lambda_A6EB():

        label("loc_A6EB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6EB")

    QueueWorkItem2(0x109, 1, lambda_A6EB)

    def lambda_A6FD():

        label("loc_A6FD")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6FD")

    QueueWorkItem2(0x105, 1, lambda_A6FD)

    def lambda_A70F():

        label("loc_A70F")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A70F")

    QueueWorkItem2(0x1A3, 1, lambda_A70F)

    def lambda_A721():

        label("loc_A721")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A721")

    QueueWorkItem2(0x8, 1, lambda_A721)

    def lambda_A733():

        label("loc_A733")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A733")

    QueueWorkItem2(0x9, 1, lambda_A733)
    Sound(953, 0, 100, 0)

    def lambda_A74B():
        OP_95(0xFE, -2110, 2660, 36590, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A74B)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A3, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)

    def lambda_A788():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_A788)
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
        "#11P#N#00005Fあ……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0437
    ChrTalk(
        0x102,
        "#11P#00105Fアルカンシェルに……！\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x109,
        "#11P#10106Fも、物凄い勢いでしたね。\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x104,
        (
            "#12P#00306Fはあ……とにかく\x01",
            "俺たちも中に入るしかねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x1A3,
        (
            "#6P#04609Fうんうん、\x01",
            "もう袋のネズミだろうしね♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_9C50 end

    def Function_38_A937(): pass

    label("Function_38_A937")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A963")
    OP_93(0xFE, 0x0, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x10E, 0x190)
    Jump("Function_38_A937")

    label("loc_A963")

    Return()

    # Function_38_A937 end

    def Function_39_A964(): pass

    label("Function_39_A964")

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
            "いらっしゃいませー。\x01",
            "アイスはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
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
            "あ、皆さんがそうでしたかー。\x01",
            "通信社の人から話は聞いてますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xC,
        (
            "それじゃ、さっそくですけど……\x01",
            "こちらがウチのオススメメニュー、\x01",
            "『氷菓≪七彩≫』です！\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x105,
        (
            "#10305Fへえ、なかなか\x01",
            "美味しそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xC,
        (
            "多彩な味わいが魅力の\x01",
            "新作ジェラートなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xC,
        (
            "お口の中でパチパチ弾ける\x01",
            "キャンディーチップも加わって、\x01",
            "不思議な食感が楽しめますよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#00100Fそれじゃあ、早速試食させて\x01",
            "いただきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは氷菓≪七彩≫を食べた。\x07\x00\x02",
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
            "#10103Fぱくっ。\x02\x03",

            "#10109F……う～ん、\x01",
            "冷たくて美味しいです！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0452
    ChrTalk(
        0x102,
        (
            "#00102Fええ、見た目も可愛いし、\x01",
            "口の中で弾ける感じもいいわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0453
    ChrTalk(
        0x101,
        (
            "#00000Fはは、女性陣は特に\x01",
            "こういうの好きそうだよな。\x02",
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
            "#00305Fん、どうしたティオすけ。\x01",
            "腹でも冷やしたか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AE9C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AE9C)

    def lambda_AEA9():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEA9)

    def lambda_AEB6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AEB6)

    def lambda_AEC3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEC3)

    def lambda_AED0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AED0)
    Sleep(1000)
    OP_64(0x103)

    #C0455
    ChrTalk(
        0x103,
        (
            "#00204Fいえ……すみません。\x02\x03",

            "#00200Fあまりの衝撃に一瞬、\x01",
            "我を忘れてしまっていました。\x02",
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
            "#00204F弾けるキャンディーの刺激、\x01",
            "この食感の新鮮さもさることながら……\x02\x03",

            "七色の多彩な味わいが相反することなく、\x01",
            "舌の上で見事に調和しています。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0457
    ChrTalk(
        0x103,
        "#00201F#4Sこれぞまさに、ジェラート革命……！\x02",
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
            "#00206F……すみません、\x01",
            "つい興奮してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#00012Fはは……\x01",
            "随分気に入ったみたいだし、\x01",
            "ここはティオに紹介してもらうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x103,
        (
            "#00202Fはい、ここなら\x01",
            "良いコメントが書けそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xC,
        "えへへ、喜んで頂けて嬉しいです。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "今後とも当店を\x01",
            "ごひいきにお願いしますねー。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x172, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B205")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B222")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B235")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B248")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B265")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B278")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_B295")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_B2A8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_B2C5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_B2D8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_B2F5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2F5")

    OP_29(0x80, 0x1, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3F8")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0463
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3EF")

    #A0464
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B3EF")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_B3F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4C9")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0465
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0466
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_B4C9")

    OP_4C(0xC, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10150, 1760, 22970, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_A964 end

    def Function_40_B4F9(): pass

    label("Function_40_B4F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B507")
    Jump("loc_B8D3")

    label("loc_B507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B515")
    Jump("loc_B8D3")

    label("loc_B515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B523")
    Jump("loc_B8D3")

    label("loc_B523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B531")
    Jump("loc_B8D3")

    label("loc_B531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B59C")
    EventBegin(0x1)

    #C0467
    ChrTalk(
        0x101,
        (
            "#00000F今はリハーサルで\x01",
            "忙しいみたいだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B607")
    EventBegin(0x1)

    #C0468
    ChrTalk(
        0x101,
        (
            "#00000F今はリハーサルで\x01",
            "忙しいみたいだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B615")
    Jump("loc_B8D3")

    label("loc_B615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B623")
    Jump("loc_B8D3")

    label("loc_B623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B84B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B75D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B705")

    #C0469
    ChrTalk(
        0x101,
        (
            "#00000Fそういえば、今日は首脳たちが\x01",
            "観劇する予定だって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        (
            "#00100Fお邪魔すると迷惑でしょうし、\x01",
            "訪ねるのは止めておきましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x104,
        "#00300Fああ、その方がよさそうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B758")

    label("loc_B705")


    #C0472
    ChrTalk(
        0x101,
        (
            "#00000F今日は首脳たちが\x01",
            "観劇する予定だって話だったな。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B758")

    Jump("loc_B830")

    label("loc_B75D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7EE")

    #C0473
    ChrTalk(
        0x101,
        (
            "#00003F……さっき\x01",
            "迷惑を掛けたばかりだな。\x02\x03",

            "#00000Fそろそろ首脳たちを\x01",
            "出迎える準備も必要だろうし、\x01",
            "入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B830")

    label("loc_B7EE")


    #C0474
    ChrTalk(
        0x101,
        (
            "#00000Fさっき迷惑を掛けたばかりだな。\x01",
            "入るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B830")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B859")
    Jump("loc_B8D3")

    label("loc_B859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B8CA")
    EventBegin(0x1)

    #C0475
    ChrTalk(
        0x101,
        (
            "#00000Fアルカンシェルは\x01",
            "準備で忙しいみたいだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B8D3")

    label("loc_B8D3")

    Return()

    # Function_40_B4F9 end

    def Function_41_B8D4(): pass

    label("Function_41_B8D4")

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

    # Function_41_B8D4 end

    SaveToFile()

Try(main)
