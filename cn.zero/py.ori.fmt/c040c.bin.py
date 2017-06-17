from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c040c.bin",                # FileName
        "c040c",                    # MapName
        "c040c",                    # Location
        0x0022,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 4, 0, 5],
    )

    BuildStringList((
        "c040c",                  # 0
        "索菲尤",                 # 1
        "揽客员皮姆",             # 2
        "珀利塞",                 # 3
        "塔普",                   # 4
        "拉曼达",                 # 5
        "缇乔",                   # 6
        "兔女郎",                 # 7
        "莱姆",                   # 8
        "菲利克",                 # 9
        "青年",                   # 10
        "少女",                   # 11
        "格蕾丝",                 # 12
        "雷因兹",                 # 13
        "潘莎",                   # 14
        "菲伊",                   # 15
        "萨米",                   # 16
        "修利",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "车",                     # 20
        "塞茜尔",                 # 21
        "诺艾尔",                 # 22
        "芙兰",                   # 23
        "菲莉亚",                 # 24
        "兰",                     # 25
        "艾达",                   # 26
        "客人",                   # 27
        "客人",                   # 28
        "客人",                   # 29
        "客人",                   # 30
        "客人",                   # 31
        "客人",                   # 32
        "客人",                   # 33
        "客人",                   # 34
        "客人",                   # 35
        "客人",                   # 36
        "中央广场",               # 37
        "西街",                   # 38
        "行政区",                 # 39
        "住宅街",                 # 40
        "欢乐街",                 # 41
        "东街",                   # 42
        "旧城区",                 # 43
        "港湾区",                 # 44
        "ＩＢＣ",                 # 45
        "站前街道",               # 46
        "后巷",                   # 47
        "乌尔斯拉间道",           # 48
        "东克洛斯贝尔街道",       # 49
        "西克洛斯贝尔街道",       # 50
        "玛因兹山道",             # 51
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch24800.itc",                   # 04
        "chr/ch25900.itc",                   # 05
        "chr/ch27100.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch22000.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch32300.itc",                   # 0B
        "chr/ch06000.itc",                   # 0C
        "chr/ch28100.itc",                   # 0D
        "chr/ch22300.itc",                   # 0E
        "chr/ch32700.itc",                   # 0F
        "chr/ch25600.itc",                   # 10
        "chr/ch10100.itc",                   # 11
        "chr/ch24400.itc",                   # 12
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4360,    0,       -10960,  310,  261,  0x0, 0,   5,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   18,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3779,   0,       500,     180,  261,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1679,   1990,    20069,   225,  277,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-1970,   1990,    18229,   0,    277,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-3460,   1990,    19659,   90,   277,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-4820,   1830,    12710,   0,    389,  0x0, 0,   12,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-6369,   1759,    12850,   90,   389,  0x0, 0,   13,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(6010,    1759,    20729,   340,  389,  0x0, 0,   14,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5510,    1759,    22149,   160,  389,  0x0, 0,   15,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(2420,    1990,    22479,   326,  389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-10770,  1769,    22969,   0,    389,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(14810,   0,       2289,    270,  261,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(15250,   0,       1220,    315,  261,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-2500,   0,       2000,    265,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclEvent(0x0000, 0, 39,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

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

    ScpFunction((
        "Function_0_828",          # 00, 0
        "Function_1_8E0",          # 01, 1
        "Function_2_90B",          # 02, 2
        "Function_3_A98",          # 03, 3
        "Function_4_B9F",          # 04, 4
        "Function_5_FE7",          # 05, 5
        "Function_6_1173",         # 06, 6
        "Function_7_1C91",         # 07, 7
        "Function_8_20E8",         # 08, 8
        "Function_9_2364",         # 09, 9
        "Function_10_246F",        # 0A, 10
        "Function_11_24E5",        # 0B, 11
        "Function_12_277F",        # 0C, 12
        "Function_13_2A1C",        # 0D, 13
        "Function_14_2C8A",        # 0E, 14
        "Function_15_2E7A",        # 0F, 15
        "Function_16_3809",        # 10, 16
        "Function_17_3A9C",        # 11, 17
        "Function_18_3C94",        # 12, 18
        "Function_19_3E4D",        # 13, 19
        "Function_20_3F53",        # 14, 20
        "Function_21_3FE9",        # 15, 21
        "Function_22_40AC",        # 16, 22
        "Function_23_4184",        # 17, 23
        "Function_24_439E",        # 18, 24
        "Function_25_455B",        # 19, 25
        "Function_26_4932",        # 1A, 26
        "Function_27_49C1",        # 1B, 27
        "Function_28_4AFE",        # 1C, 28
        "Function_29_4C9C",        # 1D, 29
        "Function_30_4D69",        # 1E, 30
        "Function_31_4E26",        # 1F, 31
        "Function_32_4F95",        # 20, 32
        "Function_33_5021",        # 21, 33
        "Function_34_50A2",        # 22, 34
        "Function_35_5297",        # 23, 35
        "Function_36_7893",        # 24, 36
        "Function_37_7D5E",        # 25, 37
        "Function_38_82FA",        # 26, 38
        "Function_39_8320",        # 27, 39
        "Function_40_8474",        # 28, 40
        "Function_41_8490",        # 29, 41
        "Function_42_84AC",        # 2A, 42
        "Function_43_84C8",        # 2B, 43
        "Function_44_861A",        # 2C, 44
    ))


    def Function_0_828(): pass

    label("Function_0_828")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_868"),
        (1, "loc_874"),
        (2, "loc_880"),
        (3, "loc_88C"),
        (4, "loc_898"),
        (5, "loc_8A4"),
        (6, "loc_8B0"),
        (SWITCH_DEFAULT, "loc_8BC"),
    )


    label("loc_868")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_874")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_880")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_88C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_898")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8C8")

    label("loc_8DF")

    Return()

    # Function_0_828 end

    def Function_1_8E0(): pass

    label("Function_1_8E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90A")
    OP_94(0xFE, 0x2148, 0xFFFFEA34, 0xB36, 0xFFFFCFFE, 0x3E8)
    Sleep(300)
    Jump("Function_1_8E0")

    label("loc_90A")

    Return()

    # Function_1_8E0 end

    def Function_2_90B(): pass

    label("Function_2_90B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A97")
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
    Jump("Function_2_90B")

    label("loc_A97")

    Return()

    # Function_2_90B end

    def Function_3_A98(): pass

    label("Function_3_A98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9E")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 60, 1000, 0x0)
    OP_95(0xFE, -5460, 0, -1360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, -1360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 60, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("Function_3_A98")

    label("loc_B9E")

    Return()

    # Function_3_A98 end

    def Function_4_B9F(): pass

    label("Function_4_B9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD1")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C73")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_C65")

    label("loc_C46")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C65")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_C65")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD1")

    label("loc_C73")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D30")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D03")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_D22")

    label("loc_D03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D22")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_D22")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD1")

    label("loc_D30")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA9")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_DC8")

    label("loc_DA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC8")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_DC8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD1")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DEE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 34)
    Jump("loc_E11")

    label("loc_DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_E02")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 35)
    Jump("loc_E11")

    label("loc_E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_E11")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 33)

    label("loc_E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E88")
    SetChrPos(0x19, -6530, 1990, 19910, 0)
    SetChrPos(0x1A, -5730, 1990, 19110, 315)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_E6D")

    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E83")
    ClearChrFlags(0x18, 0x80)

    label("loc_E83")

    Jump("loc_FD4")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F2B")
    SetChrPos(0x19, -10110, 1760, 13270, 135)
    SetChrPos(0x1A, -9100, 1760, 12260, 315)
    SetChrPos(0x10, 1960, 1990, 21100, 180)
    SetChrPos(0x11, 3030, 1990, 19760, 315)
    SetChrPos(0x12, 680, 1990, 19830, 45)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, -6890, 1990, 20250, 45)
    SetChrPos(0x16, -5800, 1990, 21340, 225)
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F26")
    SetChrFlags(0x16, 0x10)

    label("loc_F26")

    Jump("loc_FD4")

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_F6F")
    SetChrPos(0x19, -10110, 1760, 13270, 135)
    SetChrPos(0x1A, -9100, 1760, 12260, 315)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_FD4")

    label("loc_F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FBC")
    SetChrPos(0x19, 1000, 1760, 26100, 0)
    SetChrPos(0x1A, 1280, 1870, 24860, 0)
    TurnDirection(0xA, 0x19, 0)
    TurnDirection(0xB, 0x19, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x19, 0x10)
    Jump("loc_FD4")

    label("loc_FBC")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_FD4")
    ClearChrFlags(0x10, 0x10)

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_FE6")
    ClearScenarioFlags(0x5C, 3)
    SetScenarioFlags(0x1, 7)
    Event(0, 37)

    label("loc_FE6")

    Return()

    # Function_4_B9F end

    def Function_5_FE7(): pass

    label("Function_5_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_FFC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 7)

    label("loc_FFC")

    OP_78(0x6, 0x1B)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1046")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_105D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1074")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1074")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A0")
    OP_1B(0x0, 0x0, 0x2A)
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B8")
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)

    label("loc_10B8")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -2500, -3000, 26000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -2500, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -25000, -4000, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_FE7 end

    def Function_6_1173(): pass

    label("Function_6_1173")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1180")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8D")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F0")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C88")

    label("loc_11F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1204")
    Jump("loc_1C88")

    label("loc_1204")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C88")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_131F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_128A")

    #C0001
    ChrTalk(
        0x8,
        (
            "现在不买的话，\x01",
            "一定会卖光的哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "来吧，现在不赶快买的话，\x01",
            "以后可会后悔的哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131A")

    label("loc_128A")


    #C0003
    ChrTalk(
        0x8,
        (
            "呵呵，今天的销售额\x01",
            "也是节节攀升呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……那边的小哥，\x01",
            "要买冰激凌的话，就趁现在了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "不管是五个球还是七个球，\x01",
            "想要几个尽管说！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_131A")

    Jump("loc_1C88")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_13E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1366")

    #C0006
    ChrTalk(
        0x8,
        (
            "啊～真可惜啊～\x01",
            "今年的游行\x01",
            "就这么结束了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E1")

    label("loc_1366")


    #C0007
    ChrTalk(
        0x8,
        "我一直在想……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "紧跟在游行队伍后面的话，\x01",
            "生意大概会很红火吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "我可是很擅长缓慢平稳地\x01",
            "驾驶自动三轮车的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13E1")

    Jump("loc_1C88")

    label("loc_13E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_15DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_END)), "loc_146F")

    #C0010
    ChrTalk(
        0x8,
        (
            "因为游行的时候，\x01",
            "唰～地一下来了一帮人，\x01",
            "又唰～地一下全走了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "我真是被给搞得\x01",
            "晕头转向的～\x01",
            "不太记得呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D6")

    label("loc_146F")


    #C0012
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x8,
        (
            "……这是什么～？\x01",
            "要给我这张照片吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0001F不，我只是想\x01",
            "请问一下，您对这个孩子\x01",
            "有没有印象……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "这个啊，没有呢～\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "因为游行的时候，\x01",
            "唰～地一下来了一帮人，\x01",
            "又唰～地一下全走了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_15D6")

    Jump("loc_1C88")

    label("loc_15DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_16A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1620")

    #C0019
    ChrTalk(
        0x8,
        (
            "啊～真可惜啊～\x01",
            "今年的游行\x01",
            "已经结束了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169B")

    label("loc_1620")


    #C0020
    ChrTalk(
        0x8,
        "我一直在想……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "紧跟在游行队伍后面的话，\x01",
            "生意大概会很红火吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "我可是很擅长缓慢平稳地\x01",
            "驾驶自动三轮车的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_169B")

    Jump("loc_1C88")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1AFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170C")

    #C0023
    ChrTalk(
        0xFE,
        "冰激凌～要不要冰激凌～？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "与其买比萨，\x01",
            "还不如买冰激凌哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1763")

    label("loc_170C")


    #C0025
    ChrTalk(
        0xFE,
        (
            "盗窃犯是被逮捕归案还是逃之夭夭，\x01",
            "都跟我的生意没关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "来来，要不要冰激凌～？\x02",
    )

    CloseMessageWindow()

    label("loc_1763")

    Jump("loc_1AF8")

    label("loc_1768")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A60")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B7")

    #C0027
    ChrTalk(
        0x101,
        (
            "#0001F打扰一下，请问\x01",
            "能向您打听一些事吗？\x02\x03",

            "我们正在对盗窃事件\x01",
            "进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "啊，那边的比萨店\x01",
            "好像遭窃了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "嘻……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "我可不会\x01",
            "那么粗心大意哦～\x02",
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

    #C0031
    ChrTalk(
        0x102,
        (
            "#0106F嗯……请问您有没有\x01",
            "看见犯人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "不，没怎么注意呢……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "但根据我的直觉，\x01",
            "应该很快就会\x01",
            "发生第三次盗窃案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "犯人现在应该正在\x01",
            "四处物色下一个猎物吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#0306F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#0200F……顺带一提，\x01",
            "已经发生了四起盗窃案，\x01",
            "所以下次就该是『第五次盗窃案』了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xA)
    Jump("loc_1A5B")

    label("loc_19B7")


    #C0037
    ChrTalk(
        0xFE,
        (
            "根据我的直觉，\x01",
            "应该很快就会\x01",
            "再次发生盗窃案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "毕竟是连环盗窃犯嘛～\x01",
            "今天之内，应该就会\x01",
            "再找一家下手吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "嘻……不必担心。\x01",
            "我可不会糊涂到\x01",
            "被人偷钱呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5B")

    Jump("loc_1AF8")

    label("loc_1A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AB0")

    #C0040
    ChrTalk(
        0x8,
        "那家比萨店是我的竞争对手。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "你们绝对不能去他家买东西哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AF8")

    label("loc_1AB0")


    #C0042
    ChrTalk(
        0x8,
        "冰激凌～要不要冰激凌～？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "与其买比萨，\x01",
            "还不如买冰激凌哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1AF8")

    Jump("loc_1C88")

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B54")

    #C0044
    ChrTalk(
        0x8,
        (
            "我也有身为欢乐街销量第一露天店\x01",
            "的自尊。\x01",
            "可不能输给他呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC7")

    label("loc_1B54")


    #C0045
    ChrTalk(
        0x8,
        (
            "那家比萨店，\x01",
            "还真行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "说到『帕雷特比萨』，\x01",
            "是以外卖服务而闻名的店……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "……呵呵，我可不能输呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BC7")

    Jump("loc_1C88")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C22")

    #C0048
    ChrTalk(
        0x8,
        (
            "听说港湾区那边\x01",
            "有家露天店推出了\x01",
            "绝品冰激凌……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "我也不能输呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C88")

    label("loc_1C22")


    #C0050
    ChrTalk(
        0x8,
        "冰激凌～要不要冰激凌～？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "……那边的小哥，\x01",
            "纪念庆典可少不了冰激凌哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "不买怎么行呢！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C88")

    Jump("loc_1180")

    label("loc_1C8D")

    TalkEnd(0xFE)
    Return()

    # Function_6_1173 end

    def Function_7_1C91(): pass

    label("Function_7_1C91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D07")

    #C0053
    ChrTalk(
        0x9,
        (
            "庆典到今天就要结束了，\x01",
            "真是意犹未尽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "要是能够持续一年，\x01",
            "一直热闹下去，\x01",
            "我可就太高兴了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_1D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_1D5A")

    #C0055
    ChrTalk(
        0x9,
        "嘿嘿，今天拉到好多客人哦。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "大家都太兴奋，\x01",
            "很容易就上钩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_1D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_1DC3")

    #C0057
    ChrTalk(
        0x9,
        (
            "抱歉，我只对能来店里玩的\x01",
            "客人有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "可能在哪里见过，\x01",
            "不过记不清楚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFA")

    label("loc_1DC3")


    #C0059
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0061
    ChrTalk(
        0x9,
        "小孩子……？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "这个嘛，不知道呢。\x01",
            "我对客人以外的人物没有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "而且，跟着游行队伍，\x01",
            "游客们全都聚在一起，人山人海的。\x01",
            "我可说不清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_1EFA")

    Jump("loc_20E4")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F52")

    #C0065
    ChrTalk(
        0x9,
        "嘿嘿，今天拉到好多客人哦。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "大家都太兴奋，\x01",
            "很容易就上钩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_1F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1FF1")

    #C0067
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的公演一结束，\x01",
            "客人就唰～地涌出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "今天还有游行活动，\x01",
            "应该会人挤人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "嘿嘿，应该会有想玩乐的家伙吧？\x01",
            "我可得擦亮眼睛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_204D")

    #C0070
    ChrTalk(
        0xFE,
        (
            "啊，好开心啊。\x01",
            "今天也有好多客人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "我看看，接下来\x01",
            "该去拉哪个人呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_204D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_207A")

    #C0072
    ChrTalk(
        0x9,
        (
            "好～来物色\x01",
            "几个好客人吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E4")

    label("loc_207A")


    #C0073
    ChrTalk(
        0x9,
        (
            "啊，纪念庆典吗……\x01",
            "真开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "连我这个揽客员\x01",
            "都喜不自禁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "小哥小哥，\x01",
            "要不要来玩啊～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20E4")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C91 end

    def Function_8_20E8(): pass

    label("Function_8_20E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_212B")

    #C0076
    ChrTalk(
        0xA,
        (
            "跟踪狂真是太无耻了！\x01",
            "不可饶恕……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212E")

    label("loc_212B")

    Call(0, 9)

    label("loc_212E")

    Jump("loc_2360")

    label("loc_2133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_21FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_217B")

    #C0077
    ChrTalk(
        0xA,
        (
            "像今天这种日子，\x01",
            "真是嫉妒那些有票的人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_217B")


    #C0078
    ChrTalk(
        0xA,
        (
            "我问了问出来的观众。\x01",
            "他们都说今天的公演棒极了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "伊莉娅大人的光环\x01",
            "比平时更加耀眼……\x01",
            "呜……可恶的有钱人们……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_21F7")

    Jump("loc_2360")

    label("loc_21FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2257")

    #C0080
    ChrTalk(
        0xA,
        "伊莉娅大人，伊莉娅大人～……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "呵呵呵……\x01",
            "现在应该是换服装的时间吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_2257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2268")
    Call(0, 10)
    Jump("loc_2360")

    label("loc_2268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22B8")

    #C0082
    ChrTalk(
        0xA,
        (
            "我要把伊莉娅大人的这个签名\x01",
            "当作传家之宝，\x01",
            "子孙代代的传下去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2360")

    label("loc_22B8")


    #C0083
    ChrTalk(
        0xA,
        (
            "我拿到伊莉娅大人\x01",
            "的签名啦～～～！！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "呀～是手写签名哦！！\x01",
            "而且还是在我面前签的……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0085
    ChrTalk(
        0xA,
        (
            "完了……我头脑发热，\x01",
            "连招呼都打不好……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2360")

    TalkEnd(0xFE)
    Return()

    # Function_8_20E8 end

    def Function_9_2364(): pass

    label("Function_9_2364")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0086
    ChrTalk(
        0xA,
        (
            "塔普，你听说了吗！？\x01",
            "竟然有跟踪狂\x01",
            "骚扰伊莉娅大人哦！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23D7")

    #C0087
    ChrTalk(
        0xA,
        "最后好像被警察逮捕了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_23F5")

    label("loc_23D7")


    #C0088
    ChrTalk(
        0xA,
        "虽然最后好像被逮捕了……\x02",
    )

    CloseMessageWindow()

    label("loc_23F5")


    #C0089
    ChrTalk(
        0xA,
        (
            "但真是不可饶恕啊！\x01",
            "竟敢对我的伊莉娅大人……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        (
            "嗯，不可原谅啊……\x01",
            "我们去揍他一顿吧……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_2364 end

    def Function_10_246F(): pass

    label("Function_10_246F")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0091
    ChrTalk(
        0xA,
        (
            "你说你有\x01",
            "明天的票？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "去～到一边去！\x01",
            "我最讨厌游客了！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xB,
        "没错，快走吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_10_246F end

    def Function_11_24E5(): pass

    label("Function_11_24E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_252E")

    #C0094
    ChrTalk(
        0xB,
        (
            "到底是什么人……？\x01",
            "我们去揍他一顿吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2531")

    label("loc_252E")

    Call(0, 9)

    label("loc_2531")

    Jump("loc_277B")

    label("loc_2536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25AA")

    #C0095
    ChrTalk(
        0xFE,
        (
            "可恶，自从与伊莉娅大人\x01",
            "在那场舞台演出邂逅之后，\x01",
            "我就没有再见过她……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "真是嫉妒死他们了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_277B")

    label("loc_25AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2630")

    #C0097
    ChrTalk(
        0xB,
        (
            "来看游行的游客\x01",
            "都给我到一边去……！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "要是因为你们而错过了\x01",
            "见到伊莉娅大人的机会，\x01",
            "你们可要怎么赔我啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AB")

    label("loc_2630")


    #C0099
    ChrTalk(
        0xB,
        "游行？……和我无关啊。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "若想追随彩虹剧团\x01",
            "和伊莉娅大人，\x01",
            "那就应该一直盯着不放呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        "即使在庆典之中也是一样！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_26AB")

    Jump("loc_277B")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_26C1")
    Call(0, 10)
    Jump("loc_277B")

    label("loc_26C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2704")

    #C0102
    ChrTalk(
        0xB,
        (
            "伊莉娅大人本人……\x01",
            "我还是第一次那么近地看到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277B")

    label("loc_2704")


    #C0103
    ChrTalk(
        0xB,
        (
            "昨天是新剧公演的首日，\x01",
            "有临时签名会。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "当然，我们也第一时间\x01",
            "把签名弄到手了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        "……虽然没有看成公演。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_277B")

    TalkEnd(0xFE)
    Return()

    # Function_11_24E5 end

    def Function_12_277F(): pass

    label("Function_12_277F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27F4")

    #C0106
    ChrTalk(
        0xC,
        (
            "今天要不要坐坐\x01",
            "纪念庆典专用的游览飞行船呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "反正是最终日了，\x01",
            "到傍晚的话，应该会有空位吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_27F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_284D")

    #C0108
    ChrTalk(
        0xC,
        (
            "游行也看了，\x01",
            "露天店也逛了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        "今年的纪念庆典，真是玩得心满意足呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_284D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_28AF")

    #C0110
    ChrTalk(
        0xC,
        (
            "游行队伍首先会\x01",
            "经过这条欢乐街哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xC,
        (
            "呵呵，可不能错过呢，\x01",
            "要占个好位置才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_28AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_297B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2912")

    #C0112
    ChrTalk(
        0xC,
        (
            "人是不是\x01",
            "太多了点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "这种时候，要是出什么事的话，\x01",
            "可该怎么办呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2976")

    label("loc_2912")


    #C0114
    ChrTalk(
        0xC,
        (
            "纪念庆典都到第三天了……\x01",
            "好像还有游客\x01",
            "陆续到达呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "光是走在大道上，\x01",
            "就要喘不过气来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2976")

    Jump("loc_2A18")

    label("loc_297B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_29AC")

    #C0116
    ChrTalk(
        0xC,
        (
            "人这么多，\x01",
            "路真的特别难走呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_29AC")


    #C0117
    ChrTalk(
        0xC,
        (
            "哎呀，能不能\x01",
            "麻烦你稍微让一下呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "……人这么多，\x01",
            "真是难走呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "我接下来\x01",
            "还要去参加宴会呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2A18")

    TalkEnd(0xFE)
    Return()

    # Function_12_277F end

    def Function_13_2A1C(): pass

    label("Function_13_2A1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A8C")

    #C0120
    ChrTalk(
        0xD,
        "克洛斯贝尔诞生万岁～！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "好啦，形式上的口号也喊过了，\x01",
            "今天也来痛痛快快地玩上一整天吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C86")

    label("loc_2A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2AF0")

    #C0122
    ChrTalk(
        0xD,
        (
            "纯金做的装饰，\x01",
            "真令人难以置信呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xD,
        (
            "今年的游行\x01",
            "果然如传闻中的一样豪华啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C86")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B50")

    #C0124
    ChrTalk(
        0xD,
        (
            "游击士似乎\x01",
            "正在市内巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        "嘿嘿，多亏有他们，才能放心游玩啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B95")

    label("loc_2B50")


    #C0126
    ChrTalk(
        0xD,
        (
            "在纪念庆典期间，\x01",
            "游击士也在工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "似乎在定期\x01",
            "巡逻呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2B95")

    Jump("loc_2C86")

    label("loc_2B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2C16")

    #C0128
    ChrTalk(
        0xD,
        (
            "每一家店似乎\x01",
            "都能让人玩个痛快呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xD,
        (
            "你们也是，要玩的话就趁现在哦！\x01",
            "只有在纪念庆典期间才可以尽情玩啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C86")

    label("loc_2C16")


    #C0130
    ChrTalk(
        0xD,
        (
            "果然，各家店铺\x01",
            "都摆出了露天店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xD,
        (
            "嘿嘿，对店里来说，这也是赚钱的好时机吧。\x01",
            "身为客人，也要尽情玩乐啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C86")

    TalkEnd(0xFE)
    Return()

    # Function_13_2A1C end

    def Function_14_2C8A(): pass

    label("Function_14_2C8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_2CDA")

    #C0132
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ～怎么样～☆\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xE,
        (
            "纪念庆典嘛，\x01",
            "大家也来玩啦～⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E76")

    label("loc_2CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_2D34")

    #C0134
    ChrTalk(
        0xE,
        (
            "呵呵，我只会观察\x01",
            "客人的钱包状态呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xE,
        "小孩子的事不清楚啦⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E32")

    label("loc_2D34")


    #C0136
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0138
    ChrTalk(
        0xE,
        (
            "哎～不知道～\x01",
            "没见过哎～\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xE,
        (
            "这里人来人往的，\x01",
            "说不定是在我没注意的时候经过的呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000F是、是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_2E32")

    Jump("loc_2E76")

    label("loc_2E37")


    #C0141
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ～怎么样～☆\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xE,
        (
            "纪念庆典嘛，\x01",
            "大家也来玩啦～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E76")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C8A end

    def Function_15_2E7A(): pass

    label("Function_15_2E7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA4")
    Call(0, 36)
    Return()

    label("loc_2EA4")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3805")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F01")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2F01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F21")
    OP_AF(0x7F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3800")

    label("loc_2F21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F35")
    Jump("loc_3800")

    label("loc_2F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3800")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3062")

    #C0143
    ChrTalk(
        0xFE,
        (
            "哟，我听说啦。\x01",
            "已经把盗窃犯抓到了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "那可真要说声谢谢才行呢。\x01",
            "……给，拿去吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '四味奶酪比萨'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('四味奶酪比萨', 1)

    #C0146
    ChrTalk(
        0x101,
        (
            "#0000F谢谢您，\x01",
            "那我就不客气地收下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "嗯，别客气，快吃吧，\x01",
            "警察小哥！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 0)
    Jump("loc_3800")

    label("loc_3062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3112")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_30B8")

    #C0148
    ChrTalk(
        0xF,
        (
            "要在露天店买的话，只限今天了哦！\x01",
            "快来买吧，快来买吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310D")

    label("loc_30B8")


    #C0149
    ChrTalk(
        0xF,
        (
            "嘿，那边的小哥，\x01",
            "要不要来份比萨啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xF,
        (
            "帕雷特比萨店的露天店\x01",
            "只限今天了哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_310D")

    Jump("loc_3800")

    label("loc_3112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_31AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3148")

    #C0151
    ChrTalk(
        0xF,
        (
            "可恶，难得\x01",
            "这么热闹……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AA")

    label("loc_3148")


    #C0152
    ChrTalk(
        0xF,
        (
            "可恶……！\x01",
            "说是有游行要经过，\x01",
            "让我暂时撤掉了露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xF,
        (
            "这么好的时间段，\x01",
            "居然要关门啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_31AA")

    Jump("loc_3800")

    label("loc_31AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3259")

    #C0154
    ChrTalk(
        0xF,
        (
            "啊～他们竟然要我在游行队伍\x01",
            "通过的时候把露天店撤掉，让出道来。\x01",
            "当时被搞得手忙脚乱的。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "不过，至少在这一个小时之内，\x01",
            "他应该没有经过这里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341E")

    label("loc_3259")


    #C0156
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0158
    ChrTalk(
        0xFE,
        (
            "哎，走失的孩子……？\x01",
            "这孩子好像有点眼熟……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0005F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "嗯～但他们要我在游行队伍\x01",
            "通过的时候把露天店撤掉，让出道来。\x01",
            "当时被搞得手忙脚乱的……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "……所以说，抱歉，我还是不太确定。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "不过，毕竟人群也逐渐散去了，\x01",
            "至少在这一个小时之内，\x01",
            "他应该没有经过这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#0000F是这样吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_341E")

    Jump("loc_3800")

    label("loc_3423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_34C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3459")

    #C0164
    ChrTalk(
        0xF,
        (
            "可恶，难得\x01",
            "这么热闹……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BF")

    label("loc_3459")


    #C0165
    ChrTalk(
        0xF,
        (
            "可恶……！\x01",
            "说是有游行队伍要经过，\x01",
            "让我暂时撤掉了露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xF,
        (
            "这么好的时间段，\x01",
            "居然要关门啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_34BF")

    Jump("loc_3800")

    label("loc_34C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_36B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3539")

    #C0167
    ChrTalk(
        0xFE,
        "这下子，销售额也能补回来了吧。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "而且游行也马上要开始了，\x01",
            "真是好事不断啊，哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AC")

    label("loc_3539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3607")

    #C0169
    ChrTalk(
        0xFE,
        (
            "有位健谈的小哥\x01",
            "点了份热带比萨套餐，\x01",
            "当时我正在把东西递给他呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "以我接待客人的经验来看，\x01",
            "那肯定是从外国来的游客。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……唉，虽然觉得不该迁怒顾客，\x01",
            "但我好像……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AC")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_364A")

    #C0172
    ChrTalk(
        0xF,
        (
            "那肯定是个危险的大叔吧，\x01",
            "真不想跟他扯上关系啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AC")

    label("loc_364A")


    #C0173
    ChrTalk(
        0xF,
        (
            "在那边转来转去的\x01",
            "大叔，有点吓人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xF,
        (
            "从刚才起，就一直\x01",
            "在跟游客搭话……\x01",
            "那样没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_36AC")

    Jump("loc_3800")

    label("loc_36B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_372F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_36DE")

    #C0175
    ChrTalk(
        0xF,
        "客人也来一个吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_372A")

    label("loc_36DE")


    #C0176
    ChrTalk(
        0xF,
        "来来，瞧一瞧、看一看！\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xF,
        (
            "大家所熟悉的\x01",
            "帕雷特比萨店的露天店哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_372A")

    Jump("loc_3800")

    label("loc_372F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3789")

    #C0178
    ChrTalk(
        0xF,
        (
            "以外卖服务著称的\x01",
            "帕雷特比萨哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xF,
        (
            "在纪念庆典期间\x01",
            "开设露天店了哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3800")

    label("loc_3789")


    #C0180
    ChrTalk(
        0xF,
        (
            "欢迎光临！\x01",
            "这里是帕雷特比萨店的露天店！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xF,
        "大家所熟悉的帕雷特比萨哦！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xF,
        (
            "在纪念庆典期间\x01",
            "开设露天店了哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3800")

    Jump("loc_2EB1")

    label("loc_3805")

    TalkEnd(0xFE)
    Return()

    # Function_15_2E7A end

    def Function_16_3809(): pass

    label("Function_16_3809")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3882")

    #C0183
    ChrTalk(
        0x19,
        "哦哦……十分美味。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x19,
        (
            "这里的手制冰激凌真是别具一格啊。\x01",
            "十分适合当做庆典结束，\x01",
            "最后压轴的甜点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A98")

    label("loc_3882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_38F2")

    #C0185
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的游行\x01",
            "真是太棒了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "正可谓是花之都呢。\x01",
            "这么热闹的活动，我还是头一次见呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A98")

    label("loc_38F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3974")
    OP_4B(0x1A, 0xFF)

    #C0187
    ChrTalk(
        0x19,
        (
            "今天好像有大规模的\x01",
            "游行活动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x19,
        "你的身体没事吗？\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x1A,
        "嗯，当然了。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x1A,
        (
            "呵呵，游行\x01",
            "好令人期待哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    Jump("loc_3A98")

    label("loc_3974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_39F3")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0191
    ChrTalk(
        0x19,
        (
            "不好意思……\x01",
            "请问彩虹剧团\x01",
            "是在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x19,
        (
            "明天白天的公演\x01",
            "是几点开始呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    Jump("loc_3A98")

    label("loc_39F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A1E")

    #C0193
    ChrTalk(
        0x19,
        (
            "那么，\x01",
            "就慢慢转转看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A98")

    label("loc_3A1E")


    #C0194
    ChrTalk(
        0x19,
        (
            "哦哦，这可真是\x01",
            "热闹非凡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x19,
        (
            "不愧是大陆首屈一指的\x01",
            "贸易都市克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x19,
        (
            "不枉我从雷米菲利亚\x01",
            "远道而来呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3A98")

    TalkEnd(0xFE)
    Return()

    # Function_16_3809 end

    def Function_17_3A9C(): pass

    label("Function_17_3A9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B28")

    #C0197
    ChrTalk(
        0x1A,
        (
            "今天刚好是\x01",
            "我们的结婚纪念日。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x1A,
        (
            "呵呵，因此\x01",
            "我比往年更加开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x1A,
        (
            "克洛斯贝尔的创立纪念庆典……\x01",
            "还想再来一次呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C90")

    label("loc_3B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3B8F")

    #C0200
    ChrTalk(
        0xFE,
        (
            "呵呵，今年留下了\x01",
            "许多美好的回忆。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "旅行的目的地\x01",
            "选在克洛斯贝尔，\x01",
            "果然是正确的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C90")

    label("loc_3B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3BE4")

    #C0202
    ChrTalk(
        0x1A,
        "其实我已经怀孕了哦。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x1A,
        (
            "呵呵，真想让肚子里的孩子\x01",
            "也看看游行呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C90")

    label("loc_3BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C1D")

    #C0204
    ChrTalk(
        0x1A,
        (
            "市内一片混乱，\x01",
            "真叫人搞不清楚状况……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C90")

    label("loc_3C1D")


    #C0205
    ChrTalk(
        0x1A,
        (
            "我们的结婚纪念日\x01",
            "好像正好是克洛斯贝尔的\x01",
            "创立纪念庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x1A,
        (
            "呵呵，这里真的很适合当做\x01",
            "结婚纪念旅行的目的地呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C90")

    TalkEnd(0xFE)
    Return()

    # Function_17_3A9C end

    def Function_18_3C94(): pass

    label("Function_18_3C94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3CE1")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0207
    ChrTalk(
        0x10,
        (
            "啊，我知道。\x01",
            "那孩子很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_3CE4")

    label("loc_3CE1")

    Call(0, 19)

    label("loc_3CE4")

    Jump("loc_3E49")

    label("loc_3CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3D5D")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0208
    ChrTalk(
        0x10,
        (
            "不过，要我说的话，\x01",
            "还是游行更加……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x10,
        "喂，你们两个，有在听我说话吗？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_3D60")

    label("loc_3D5D")

    Call(0, 20)

    label("loc_3D60")

    Jump("loc_3E49")

    label("loc_3D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3DD4")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0210
    ChrTalk(
        0x10,
        (
            "呜……都说到这份上了，\x01",
            "只好奉陪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x10,
        (
            "晚上住在\x01",
            "苏茜的表姐家吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_3DD7")

    label("loc_3DD4")

    Call(0, 21)

    label("loc_3DD7")

    Jump("loc_3E49")

    label("loc_3DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3E46")

    #C0212
    ChrTalk(
        0x10,
        (
            "嘿嘿，在庆典果然还是要\x01",
            "痛痛快快地玩才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x10,
        (
            "庆典期间又没有门禁，\x01",
            "可以尽情玩乐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E49")

    label("loc_3E46")

    Call(0, 22)

    label("loc_3E49")

    TalkEnd(0xFE)
    Return()

    # Function_18_3C94 end

    def Function_19_3E4D(): pass

    label("Function_19_3E4D")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0214
    ChrTalk(
        0x11,
        (
            "菲利克有票，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x11,
        "到底是从哪里弄到的～？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x10,
        (
            "嘿嘿～老爸说是\x01",
            "工作上有关系的人送的。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x10,
        "不过只是Ｂ席啦。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x12,
        (
            "Ｂ席就已经很棒啦～\x01",
            "伊莉娅大人可真是超级帅气啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x12,
        (
            "还有就是缇奥多尔大人呢～\x01",
            "我可是他的超级崇拜者～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_19_3E4D end

    def Function_20_3F53(): pass

    label("Function_20_3F53")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0220
    ChrTalk(
        0x12,
        (
            "彩虹剧团的票～？\x01",
            "你怎么不早说啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x10,
        (
            "抱歉，我忘说了。\x01",
            "而且仅限\x01",
            "今天的日场……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x11,
        (
            "赶快去吧，\x01",
            "都到公演时间了嘛！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_20_3F53 end

    def Function_21_3FE9(): pass

    label("Function_21_3FE9")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0223
    ChrTalk(
        0x10,
        "哎，米修拉姆？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x10,
        (
            "太老套了吧？\x01",
            "感觉好孩子气～……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x12,
        "我觉得挺好啊，去吧。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x12,
        (
            "我表姐家就在那里哦。\x01",
            "要不要顺便住下？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x11,
        (
            "哦～不错嘛。\x01",
            "那就顺便去鬼屋玩玩吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_3FE9 end

    def Function_22_40AC(): pass

    label("Function_22_40AC")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0228
    ChrTalk(
        0x11,
        "哟，今天去哪里玩？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x12,
        (
            "那个大富豪，\x01",
            "不是说今晚要开宴会吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x12,
        "去那里看看吧～\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x10,
        (
            "不行不行，那里是只有\x01",
            "熟人才能参加的私人宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x10,
        (
            "要出入社交界的话，\x01",
            "这点道理还是要明白的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_22_40AC end

    def Function_23_4184(): pass

    label("Function_23_4184")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_420E")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0233
    ChrTalk(
        0x11,
        (
            "让我大吃一惊的是那个\x01",
            "扮演月之舞姬的女孩啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x11,
        (
            "我绝对不相信她是新人，\x01",
            "真是完全迷上她了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4211")

    label("loc_420E")

    Call(0, 19)

    label("loc_4211")

    Jump("loc_439A")

    label("loc_4216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4278")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0235
    ChrTalk(
        0x11,
        (
            "游行什么的，很孩子气吧。\x01",
            "大人还是应该欣赏剧团演出啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_427B")

    label("loc_4278")

    Call(0, 20)

    label("loc_427B")

    Jump("loc_439A")

    label("loc_4280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_432C")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0236
    ChrTalk(
        0x11,
        (
            "哈哈～菲利克，\x01",
            "你们一家之前\x01",
            "一起去了主题公园吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x11,
        (
            "啧啧，那里可是给小孩子玩的地方。\x01",
            "要说疗养地的话，还有其它的地方可以逛吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_432F")

    label("loc_432C")

    Call(0, 21)

    label("loc_432F")

    Jump("loc_439A")

    label("loc_4334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4397")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0238
    ChrTalk(
        0x11,
        "出现了，菲利克的社交界理论！\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x11,
        (
            "那怎么办？\x01",
            "难道去『巴鲁卡』？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_439A")

    label("loc_4397")

    Call(0, 22)

    label("loc_439A")

    TalkEnd(0xFE)
    Return()

    # Function_23_4184 end

    def Function_24_439E(): pass

    label("Function_24_439E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_440B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4403")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0240
    ChrTalk(
        0x12,
        "啊～花心鬼～！\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x12,
        (
            "之前还说眼中\x01",
            "只有伊莉娅大人的～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4406")

    label("loc_4403")

    Call(0, 19)

    label("loc_4406")

    Jump("loc_4557")

    label("loc_440B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_447B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4473")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0242
    ChrTalk(
        0x12,
        "喂，赶快走吧。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x12,
        (
            "那票不是预约席吧？\x01",
            "……得去找个好位置！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4476")

    label("loc_4473")

    Call(0, 20)

    label("loc_4476")

    Jump("loc_4557")

    label("loc_447B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_44FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_44F4")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0244
    ChrTalk(
        0x12,
        (
            "我的表姐\x01",
            "在米修拉姆有别墅哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x12,
        (
            "超有钱的哦。\x01",
            "三个人留宿，那是绰绰有余啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_44F7")

    label("loc_44F4")

    Call(0, 21)

    label("loc_44F7")

    Jump("loc_4557")

    label("loc_44FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4554")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0246
    ChrTalk(
        0x12,
        "我想去高级酒吧之类的地方～！\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x12,
        "那里感觉很成熟吧？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4557")

    label("loc_4554")

    Call(0, 22)

    label("loc_4557")

    TalkEnd(0xFE)
    Return()

    # Function_24_439E end

    def Function_25_455B(): pass

    label("Function_25_455B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_END)), "loc_46B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45F6")

    #C0248
    ChrTalk(
        0x13,
        (
            "#2100F啊，对了对了。\x01",
            "关于那个拍照的委托，如果照片数量够了，\x01",
            "就拿到通讯社的接待处去吧。\x02\x03",

            "拜托你们了哦～¤\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    Jump("loc_46AF")

    label("loc_45F6")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0249
    ChrTalk(
        0x13,
        (
            "#2109F好了～彩虹剧团\x01",
            "新剧的反响，可不能错过哦～！\x02\x03",

            "#2100F顺便还要对伊莉娅·普拉提耶\x01",
            "和莉夏·毛进行\x01",
            "突击采访呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 300)

    #C0250
    ChrTalk(
        0x13,
        "#2100F雷因兹，上吧～！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x14,
        "是、是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)

    label("loc_46AF")

    Jump("loc_492E")

    label("loc_46B4")


    #C0252
    ChrTalk(
        0x13,
        (
            "#2100F哎呀，这不是支援科的各位嘛。\x02\x03",

            "#2109F之前的爆炸性大新闻，\x01",
            "可真是多谢你们了啊！\x02\x03",

            "全靠你们，才能写出那种引人注目的报道。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#0000F呼……还真是得意忘形啊。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x103,
        (
            "#0200F我们那么做并不是为了\x01",
            "给格蕾丝小姐提供什么新闻素材。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x102,
        (
            "#0100F……虽然心情有些复杂……\x02\x03",

            "但那篇报道的立场总算是\x01",
            "对外公表示同情，我也就安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x13,
        (
            "#2104F哈，关于帝国派的新闻都不能写，\x01",
            "如果光把矛头指向市长，\x01",
            "就未免太不公平了～\x02\x03",

            "#2100F而且，你的外公在市民中\x01",
            "也有着相当高的人气与威望，\x01",
            "就我个人而言，也很支持他呢。\x02\x03",

            "身为记者，这样做也许有些不称职，\x01",
            "但我实在是不愿意写他的坏话～\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        "#0102F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        (
            "#0300F嗯，记者也是人啊，\x01",
            "你这种做法不是很好嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB5, 1)

    label("loc_492E")

    TalkEnd(0xFE)
    Return()

    # Function_25_455B end

    def Function_26_4932(): pass

    label("Function_26_4932")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4968")

    #C0259
    ChrTalk(
        0xFE,
        (
            "跟着前辈，\x01",
            "令我深感体力不足啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BD")

    label("loc_4968")


    #C0260
    ChrTalk(
        0xFE,
        (
            "呼、呼……\x01",
            "跟着前辈做事，\x01",
            "就要到处跑来跑去……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "呼，我都上气不接下气了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_49BD")

    TalkEnd(0xFE)
    Return()

    # Function_26_4932 end

    def Function_27_49C1(): pass

    label("Function_27_49C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49DF")
    Call(0, 29)
    Jump("loc_4A3A")

    label("loc_49DF")


    #C0262
    ChrTalk(
        0xFE,
        (
            "爸爸是大笨蛋～！\x01",
            "机械痴～！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "逛庆典本来\x01",
            "应该很开心的～！\x01",
            "结果搞得我都没食欲了！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3A")

    Jump("loc_4AFA")

    label("loc_4A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4A5F")

    #C0264
    ChrTalk(
        0xFE,
        "好精彩哦～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AFA")

    label("loc_4A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4AFA")

    #C0265
    ChrTalk(
        0xFE,
        (
            "为了不引起误会，\x01",
            "我先说一句，\x01",
            "我非常喜欢伊莉娅小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "但也很喜欢普莉埃小姐、塞利娜小姐\x01",
            "和新人莉夏小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "因为所有的美女\x01",
            "我都很喜欢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFA")

    TalkEnd(0xFE)
    Return()

    # Function_27_49C1 end

    def Function_28_4AFE(): pass

    label("Function_28_4AFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1C")
    Call(0, 29)
    Jump("loc_4B51")

    label("loc_4B1C")


    #C0268
    ChrTalk(
        0xFE,
        (
            "呵呵，边走边品尝露天店小吃\x01",
            "还真是意外地开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B51")

    Jump("loc_4C98")

    label("loc_4B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4BB3")

    #C0269
    ChrTalk(
        0xFE,
        "啊啊，真是太棒了。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "原来如此，终于明白\x01",
            "伊莉娅小姐为什么这么受欢迎了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C98")

    label("loc_4BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C5A")
    OP_4B(0x15, 0xFF)
    OP_93(0xFE, 0xA0, 0x0)

    #C0271
    ChrTalk(
        0x15,
        (
            "讨厌，既然有\x01",
            "彩虹剧团的票，\x01",
            "为什么不早说啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        "哈哈，抱歉抱歉，\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "是工作上有关系的人送的，\x01",
            "我早忘得一干二净了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    SetScenarioFlags(0x1, 4)
    Jump("loc_4C98")

    label("loc_4C5A")


    #C0274
    ChrTalk(
        0xFE,
        (
            "哈哈哈……\x01",
            "竟然会憧憬彩虹剧团，\x01",
            "潘莎到底也是个女孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C98")

    TalkEnd(0xFE)
    Return()

    # Function_28_4AFE end

    def Function_29_4C9C(): pass

    label("Function_29_4C9C")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    TurnDirection(0x15, 0x16, 0)
    TurnDirection(0x16, 0x15, 0)

    #C0275
    ChrTalk(
        0x15,
        (
            "啊，对了！\x01",
            "我想吃冰激凌！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x16,
        (
            "嗯嗯，去买一个，\x01",
            "然后来分析制作方法吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x16,
        (
            "是用什么机器\x01",
            "制作的呢～⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x15,
        (
            "爸爸是大笨蛋～！\x01",
            "不要说这种奇怪的话啦！！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x2D, 0x0)
    OP_93(0x16, 0xE1, 0x0)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_29_4C9C end

    def Function_30_4D69(): pass

    label("Function_30_4D69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCC")

    #C0279
    ChrTalk(
        0xFE,
        (
            "好耶～！\x01",
            "终于到期待已久的最终日了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "伊莉娅大人～\x01",
            "我这就来见您～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_4E22")

    label("loc_4DCC")


    #C0281
    ChrTalk(
        0xFE,
        (
            "演出的票……\x01",
            "只买到了今天的Ｂ席啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "不过没关系！\x01",
            "终于能见到伊莉娅大人了嘛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E22")

    TalkEnd(0xFE)
    Return()

    # Function_30_4D69 end

    def Function_31_4E26(): pass

    label("Function_31_4E26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F01")

    #C0283
    ChrTalk(
        0x101,
        "#0005F咦……在干什么呢？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐\x01",
            "让我来买冰激凌。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    #C0285
    ChrTalk(
        0xFE,
        (
            "之后还有公演，\x01",
            "我得赶快回去帮忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#0100F（很努力的样子呢。）\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        (
            "#0200F（这个孩子似乎\x01",
            "  也找到了自己的人生道路。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4F91")

    label("loc_4F01")


    #C0288
    ChrTalk(
        0xFE,
        (
            "虽然伊莉娅小姐问我\x01",
            "『要不要上舞台练习一下？』\x01",
            "……但我还不想上舞台。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "暂时还是只做些打杂的工作吧。\x01",
            "……反正还能参观\x01",
            "伊莉娅小姐的排练。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F91")

    TalkEnd(0xFE)
    Return()

    # Function_31_4E26 end

    def Function_32_4F95(): pass

    label("Function_32_4F95")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5020")
    OP_29(0x46, 0x1, 0x2)

    #C0290
    ChrTalk(
        0x101,
        (
            "#0001F（好，在欢乐街\x01",
            "  就探听到这里吧。）\x02\x03",

            "（接下来是后巷……\x01",
            "  用同样的方法，继续探听消息吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_5020")

    Return()

    # Function_32_4F95 end

    def Function_33_5021(): pass

    label("Function_33_5021")

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
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_5021 end

    def Function_34_50A2(): pass

    label("Function_34_50A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(21000, 1000, 11800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 27000, 0, 11800, 270)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(16500, 3000)

    def lambda_5117():
        OP_96(0xFE, 0x5208, 0x0, 0x2E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5117)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Sleep(500)

    #C0291
    ChrTalk(
        0x101,
        (
            "#0003F#11P（好……我负责的部分\x01",
            "  是欢乐街、中央广场、\x01",
            "  站前街道和西街吗。）\x02\x03",

            "#0000F（四处乱转也无济于事，\x01",
            "  还是一个街区一个街区地依次探听吧。）\x02\x03",

            "（每个人都打听一遍实在是太花费时间了，\x01",
            "  在室内的话，就主要以接待人员为中心来打听吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 21000, 0, 11800, 270)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetScenarioFlags(0xA1, 6)
    OP_C7(0x0, 0x1000)
    ModifyEventFlags(0, 0, 0x80)
    ClearChrFlags(0x16, 0x10)
    OP_29(0x46, 0x4, 0x2)
    OP_29(0x46, 0x1, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x2A)
    OP_1B(0x1, 0x0, 0x28)
    OP_1B(0x2, 0x0, 0x29)
    EventEnd(0x5)
    Return()

    # Function_34_50A2 end

    def Function_35_5297(): pass

    label("Function_35_5297")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07500.itc", 0x1E)
    LoadChrToIndex("chr/ch08400.itc", 0x1F)
    LoadChrToIndex("chr/ch08500.itc", 0x20)
    LoadChrToIndex("chr/ch36300.itc", 0x21)
    LoadChrToIndex("chr/ch36400.itc", 0x22)
    LoadChrToIndex("chr/ch36500.itc", 0x23)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06300.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05900.itp")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    LoadChrToIndex("chr/ch20000.itc", 0x28)
    LoadChrToIndex("chr/ch20100.itc", 0x29)
    LoadChrToIndex("chr/ch20200.itc", 0x2A)
    LoadChrToIndex("chr/ch20300.itc", 0x2B)
    LoadChrToIndex("chr/ch20800.itc", 0x2C)
    LoadChrToIndex("chr/ch20900.itc", 0x2D)
    LoadChrToIndex("chr/ch21200.itc", 0x2E)
    LoadChrToIndex("chr/ch21300.itc", 0x2F)
    LoadChrToIndex("chr/ch21800.itc", 0x30)
    LoadChrToIndex("chr/ch21900.itc", 0x31)
    SetChrChipByIndex(0x22, 0x28)
    SetChrChipByIndex(0x23, 0x29)
    SetChrChipByIndex(0x24, 0x2A)
    SetChrChipByIndex(0x25, 0x2B)
    SetChrChipByIndex(0x26, 0x2C)
    SetChrChipByIndex(0x27, 0x2D)
    SetChrChipByIndex(0x28, 0x2E)
    SetChrChipByIndex(0x29, 0x2F)
    SetChrChipByIndex(0x2A, 0x30)
    SetChrChipByIndex(0x2B, 0x31)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    ClearChrFlags(0x29, 0x4)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
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
    SetMapObjFlags(0x5, 0x1000)
    SetChrPos(0x22, -2880, 2660, 33730, 315)
    SetChrPos(0x23, -1480, 2660, 33130, 315)
    SetChrPos(0x24, -2520, 2660, 31990, 315)
    SetChrPos(0x25, -2560, 1760, 29650, 135)
    SetChrPos(0x26, -1660, 1760, 28950, 225)

    def lambda_554C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_554C)

    def lambda_5566():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_5566)

    def lambda_5580():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_5580)

    def lambda_559A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_559A)

    def lambda_55B4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_55B4)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_68(-7600, 1950, 500, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -5200, 0, -1600, 310)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -4300, 0, -2300, 310)
    SetChrChipByIndex(0x1F, 0x23)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -10700, 0, 2600, 130)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -11800, 0, 3500, 130)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, -12900, 0, 4400, 130)
    FadeToBright(1000, 0)
    OP_68(-1960, 4040, 33450, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(18000, 3000)
    SetChrPos(0x27, -2500, 2660, 35600, 315)
    SetChrPos(0x28, -1500, 2660, 35600, 315)
    SetChrPos(0x29, -2500, 2660, 35600, 315)
    SetChrPos(0x2A, -1500, 2660, 35600, 135)
    SetChrPos(0x2B, -1500, 2660, 35600, 225)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -2500, 2660, 35600, 0)
    SetChrPos(0x1C, -1500, 2660, 35600, 0)
    Sleep(1000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)

    def lambda_57E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_57E5)

    def lambda_57F6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_57F6)
    Sleep(500)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)

    def lambda_581D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_581D)

    def lambda_582E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_582E)
    Sleep(2000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)

    def lambda_5855():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5855)

    def lambda_5866():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5866)
    Sleep(300)

    def lambda_5883():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5883)

    def lambda_5894():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_5894)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)

    def lambda_58C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_58C5)

    def lambda_58D6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_58D6)
    Sleep(500)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)

    def lambda_58FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_58FD)

    def lambda_590E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_590E)
    Sleep(1500)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)

    def lambda_5935():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_5935)

    def lambda_5946():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_5946)
    OP_0D()
    OP_68(-11650, 2120, 3280, 0)
    MoveCamera(28, 16, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(12500, 0)
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
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x1C, 0xFF)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x101, -7400, 0, -300, 220)
    SetChrPos(0x1C, -8700, 0, 800, 220)
    OP_68(-11650, 920, 3280, 4000)
    MoveCamera(41, 24, 0, 4000)
    OP_6E(740, 4000)
    SetCameraDistance(11000, 4000)
    SetChrPos(0x101, -11320, 0, 2530, 334)
    SetChrPos(0x1C, -11770, 0, 4110, 154)
    FadeToBright(3000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0292
    ChrTalk(
        0x101,
        (
            "#0014F#12P哇～……\x01",
            "真是太棒了！！\x02\x03",

            "他们的演出如此精彩，也难怪会有\x01",
            "这么多狂热的崇拜者呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0293
    AnonymousTalk(
        0x1C,
        (
            "呵呵，是呀。\x02\x03",

            "伊莉娅固然厉害，\x01",
            "莉夏小姐也十分不错呢。\x02\x03",

            "嗯～难怪那个伊莉娅\x01",
            "会如此看重她。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0294
    ChrTalk(
        0x101,
        (
            "#0002F#12P哈哈，是啊。\x02\x03",

            "似乎比预演时\x01",
            "配合得更加默契了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x1C,
        (
            "#5902F#5P如此说来……那个事件\x01",
            "是你们解决的吧？\x02\x03",

            "不久前，伊莉娅和我联络的时候，\x01",
            "极力夸奖了你们呢。\x02\x03",

            "#5909F还说，以后准备设计一场以这次事件\x01",
            "为题材的舞台剧，然后请你们特别出演……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0296
    ChrTalk(
        0x101,
        (
            "#0012F#12P不、不会吧～\x01",
            "这一定是在开玩笑吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x1C,
        (
            "#5906F#5P嗯～难说呢。\x02\x03",

            "我和她认识很久了，\x01",
            "说不定她确实是认真的呢。\x02\x03",

            "#5900F不过，她也经常会突然改变主意，\x01",
            "所以应该不用担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#0006F#12P但愿如此……\x02\x03",

            "#0000F要是真被她强拉过去的话，\x01",
            "大概想推都推不掉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x1C,
        (
            "#5904F#5P呵呵，别看她平时那样子，\x01",
            "其实也是很懂关心他人的哦。\x02\x03",

            "#5900F话说回来──是不是有点\x01",
            "对不起兰迪呢。\x02\x03",

            "要是票再多一张的话，\x01",
            "就可以约他一起来看了……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#0004F#12P哈哈，不用费心啦。\x02\x03",

            "#0000F其实彩虹剧团\x01",
            "也送给我们门票了。\x02\x03",

            "而且，兰迪现在应该\x01",
            "和塞茜尔姐姐的后辈们\x01",
            "玩得正开心吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x1C,
        (
            "#5902F#5P呵呵，是呀。\x02\x03",

            "#5904F那些孩子们平时也很忙，\x01",
            "希望她们能趁此机会好好放松一下呢。\x02\x03",

            "#5905F说起来，罗伊德，你们的\x01",
            "休假好像只到今天为止吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#0000F#12P嗯，在纪念庆典期间，\x01",
            "警察的工作也增加了很多嘛。\x02\x03",

            "作为解决之前那次事件的奖励，\x01",
            "才在第一天给我们放了假。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x1C,
        (
            "#5909F#5P呵呵，真是辛苦了。\x02\x03",

            "#5902F对了，今天来我们家\x01",
            "吃晚饭吧？\x02\x03",

            "爸爸妈妈都很期待呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        (
            "#0002F#12P嗯，那就过去叨扰一下啦。\x02\x03",

            "#0005F不过……到晚饭之前，\x01",
            "好像还有些时间呢。\x02\x03",

            "#0012F嗯……\x01",
            "要不要一起去逛逛庆典呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x1C,
        (
            "#5905F#5P啊……抱歉哦。\x02\x03",

            "#5906F我接下来\x01",
            "还约了人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0306
    ChrTalk(
        0x101,
        (
            "#0011F#12P哎……！？\x02\x03",

            "约了人……\x01",
            "……难不成，莫非是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0307
    ChrTalk(
        0x1C,
        (
            "#5900F#5P嗯……？\x02\x03",

            "已经和伊莉娅约好了，\x01",
            "一会要去她的公寓的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0308
    ChrTalk(
        0x101,
        (
            "#0012F#12P这、这样啊，哈哈……\x02\x01",

            "#0013F（呼，我又何必这么激动嘛……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x1C,
        (
            "#5909F#5P呵呵，她说要把\x01",
            "那位莉夏小姐介绍给我认识。\x02\x03",

            "#5902F不然，罗伊德也一起来吧？\x01",
            "反正你们都见过面的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0310
    ChrTalk(
        0x101,
        (
            "#0000F#12P不、不了，我还是不去了。\x02\x03",

            "女性们的聚会，\x01",
            "男人过去打扰也不好啦。\x02\x03",

            "#0006F（不如说，总觉得去了之后\x01",
            "  就会被伊莉娅小姐欺负的……）\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x1C,
        (
            "#5909F#5P呵呵，不用客气的啊。\x02\x03",

            "#5902F也罢，\x01",
            "谢谢你今天陪我哦。\x02\x03",

            "晚饭我会回家吃的，\x01",
            "到时候，罗伊德也要来我家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#0002F#12P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_68(-12750, 920, 4100, 5000)

    def lambda_63D7():

        label("loc_63D7")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_63D7")

    QueueWorkItem2(0x101, 0, lambda_63D7)
    OP_92(0x1C, 0xFFFFAC04, 0x1A2C, 0x1F4)

    def lambda_63F6():
        OP_95(0xFE, -21500, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_63F6)
    Sleep(2000)
    EndChrThread(0x101, 0xFF)
    OP_93(0x101, 0x10E, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sound(1092, 255, 100, 0)    #voice#Lloyd
    Sleep(500)

    #C0313
    ChrTalk(
        0x101,
        (
            "#0006F#11P……时机掌握得不太好啊。\x02\x03",

            "#0008F要是能像大哥那样，\x01",
            "稍微积极一点就好了……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0xFF)
    WaitChrThread(0x1C, 1)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_64CC")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_64E6")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6500")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_651A")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_651A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6534")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6534")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_654E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_654E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6568")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6568")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6582")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6582")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_659C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_659C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xB, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65B6")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65D0")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65EA")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6604")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6604")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_661E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_661E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6638")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6652")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_666C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_666C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6686")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_66A0")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_66B2")
    SetScenarioFlags(0xAA, 1)

    label("loc_66B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_670F")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "※任务完成率高\x01",      # 0
            "※任务完成率低\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66FF"),
        (1, "loc_6707"),
        (SWITCH_DEFAULT, "loc_670F"),
    )


    label("loc_66FF")

    SetScenarioFlags(0xAA, 1)
    Jump("loc_670F")

    label("loc_6707")

    ClearScenarioFlags(0xAA, 1)
    Jump("loc_670F")

    label("loc_670F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_7152")
    SetChrPos(0x1D, -2840, 0, -3110, 306)
    SetChrPos(0x1E, -3460, 0, -4040, 306)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    Sleep(300)
    #Sound(2084, 255, 100, 0)    #voice#Fran
    Sleep(150)

    #N0314
    NpcTalk(
        0x1E,
        "女孩的声音",
        "#1P咦～罗伊德警官？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x1D, 500)
    Fade(1000)
    OP_68(-7250, 1530, -700, 0)
    MoveCamera(81, 28, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(14500, 0)

    def lambda_67D2():
        OP_95(0xFE, -9840, 0, 660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_67D2)
    Sleep(100)

    def lambda_67EF():
        OP_95(0xFE, -9220, 0, 1590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_67EF)
    OP_68(-10020, 1000, 1460, 4500)
    MoveCamera(81, 28, 0, 4500)
    OP_6E(680, 4500)
    SetCameraDistance(12500, 10000)
    WaitChrThread(0x1E, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0315
    AnonymousTalk(
        0x1E,
        "罗伊德警官，你好～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    WaitChrThread(0x1D, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0316
    AnonymousTalk(
        0x1D,
        "之前工作辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0317
    ChrTalk(
        0x101,
        (
            "#0005F#6P啊……是芙兰，还有诺艾尔上士吗。\x02\x03",

            "#0000F你们俩都穿着便服，\x01",
            "我一时还真没认出来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x1D,
        (
            "#6309F啊哈哈……\x01",
            "嗯，偶尔放假，出来放松一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1E,
        (
            "#6400F#11P呵呵，罗伊德警官的\x01",
            "打扮好像和平时差不多啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯～因为我平时就\x01",
            "一直穿着便于行动的衣服嘛。\x02\x03",

            "#0000F你们两姐妹在约会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x1E,
        "#6409F#11P嘿嘿，是呀～\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x1D,
        (
            "#6306F唉，本来不应该\x01",
            "是和妹妹，而是和\x01",
            "男朋友一起逛街才对……\x02\x03",

            "#6308F可是我连交男朋友的时间都没有嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1D, 500)

    #C0323
    ChrTalk(
        0x1E,
        (
            "#6401F#12P姐姐好过分～！\x02\x03",

            "平时忙得都没空见面，\x01",
            "明明说好了今天\x01",
            "要陪我的～\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x1D,
        (
            "#6302F是是，知道啦。\x02\x03",

            "#6300F……话说回来，\x01",
            "罗伊德警官在这里做什么呢？\x02\x03",

            "是在等人吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    #C0325
    ChrTalk(
        0x101,
        (
            "#0005F#6P啊，不……\x02\x03",

            "#0012F直到刚才还有朋友在的，\x01",
            "不过人家之后好像还有活动。\x02\x03",

            "计划突然被打乱，\x01",
            "正不知道该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1E, 0x1D, 500)
    TurnDirection(0x1D, 0x1E, 500)

    #C0326
    ChrTalk(
        0x1E,
        "#6401F#12P（姐姐，这是……）\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x1D,
        (
            "#6308F#5P（嗯，搞不好\x01",
            "  是被甩了……）\x02\x03",

            "#6301F（刚才我们和他打招呼的时候，\x01",
            "  他的表情好像就有点消沉……）\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x1E,
        "#6406F#12P（果、果然是……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1E)
    OP_64(0x1D)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000F#6P哎……？\x01",
            "（她们好像产生了什么误会啊。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    TurnDirection(0x1D, 0x101, 500)

    #C0330
    ChrTalk(
        0x1E,
        (
            "#6404F#11P那个～罗伊德警官。\x02\x03",

            "#6402F你要是有空的话，\x01",
            "能不能陪陪我们呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x1D,
        (
            "#6302F其实，港湾区的公园\x01",
            "好像正在举办小型演唱会。\x02\x03",

            "我们正打算\x01",
            "去那边看看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#0005F#6P啊，是吗？\x02\x03",

            "#0002F好像很有趣……\x01",
            "可是，你们姐妹难得有点独处的时间，\x01",
            "我这外人跟去的话，不会很碍事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x1E,
        (
            "#6409F#11P不会不会～！\x01",
            "罗伊德警官的话，完全没问题啦！\x02\x03",

            "如果是其他的男人，\x01",
            "我就会全力阻止的！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x1D,
        (
            "#6306F我说你啊……\x02\x03",

            "#6302F也罢，总之就是这样，\x01",
            "机会难得，就请陪陪我们吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F63():
        OP_95(0xFE, -10900, 0, 3030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6F63)

    def lambda_6F7D():
        OP_95(0xFE, -11600, 0, 1990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_6F7D)
    OP_68(-11320, 1360, 2530, 3000)
    WaitChrThread(0x1D, 0)

    def lambda_6FAC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_6FAC)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x1E, 0)

    def lambda_6FC3():
        OP_93(0xFE, 0x78, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_6FC3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0336
    ChrTalk(
        0x101,
        (
            "#0011F#5P两、两位，请等一下。\x02\x03",

            "虽然很感谢你们邀请我，\x01",
            "不过这实在是有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x1D,
        "#6309F#5P没事没事，不要客气。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x1E,
        (
            "#6400F#11P对对，\x01",
            "这就叫左拥右抱啦～\x02\x03",

            "#6409F那么，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0012F#5P嗯、嗯～……\x02\x03",

            "（好像被她们误会了呢\x01",
            "  ……算了。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70F9():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_70F9)

    def lambda_7113():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_7113)

    def lambda_712D():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_712D)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jump("loc_77C2")

    label("loc_7152")

    SetChrPos(0x104, -23440, 0, 8980, 1)
    SetChrPos(0x1F, -24390, 0, 8530, 126)
    SetChrPos(0x20, -23360, 0, 9820, 126)
    SetChrPos(0x21, -24780, 0, 9950, 126)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    Sleep(300)
    #Sound(1369, 255, 100, 0)    #voice#Randy
    Sleep(150)

    #N0340
    NpcTalk(
        0x104,
        "兰迪的声音",
        "#2P哦，这不是罗伊德嘛！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Fade(1000)
    OP_68(-17230, 1000, 5390, 0)
    MoveCamera(349, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(-12210, 1000, 3240, 5000)
    MoveCamera(349, 31, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(13500, 5000)

    def lambda_7274():

        label("loc_7274")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7274")

    QueueWorkItem2(0x104, 1, lambda_7274)

    def lambda_7286():

        label("loc_7286")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7286")

    QueueWorkItem2(0x21, 1, lambda_7286)

    def lambda_7298():

        label("loc_7298")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7298")

    QueueWorkItem2(0x1F, 1, lambda_7298)

    def lambda_72AA():
        OP_96(0xFE, 0xFFFFD3F0, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_72AA)
    Sleep(150)

    def lambda_72C7():
        OP_96(0xFE, 0xFFFFCF7C, 0x0, 0x73A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_72C7)
    Sleep(150)

    def lambda_72E4():
        OP_96(0xFE, 0xFFFFCC2A, 0x0, 0xA78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_72E4)

    def lambda_72FE():
        OP_96(0xFE, 0xFFFFCDF6, 0x0, 0xF6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_72FE)
    Sleep(4000)
    WaitChrThread(0x20, 0)

    def lambda_731F():
        TurnDirection(0x20, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_731F)
    Sleep(800)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x21, 0xFF)

    #C0341
    ChrTalk(
        0x101,
        (
            "#0005F#12P兰迪……\x01",
            "还有塞茜尔姐姐的后辈们。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1F, 0)

    #C0342
    ChrTalk(
        0x1F,
        "#5P啊，是警察弟弟，你好啊～！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x20, 0)

    #C0343
    ChrTalk(
        0x20,
        (
            "#11P咦，你不是和塞茜尔前辈\x01",
            "在一起的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#0000F#12P嗯，但她好像和朋友\x01",
            "另外有约。\x02\x03",

            "刚刚才走掉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x21,
        "#5P哎呀，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x21,
        (
            "#5P呵呵……\x01",
            "好可惜哦，罗伊德。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0347
    ChrTalk(
        0x101,
        "#0012F#12P……什、什么可惜啊？\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#0305F#5P喂喂，等一下！\x02\x03",

            "#0301F难不成，塞茜尔小姐……\x01",
            "是要跟哪个男人见面吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#0004F#12P哈哈，是伊莉娅小姐啦。\x02\x03",

            "#0000F好像莉夏也会去。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#0304F#5P呼，是吗……\x02\x03",

            "#0301F不对，那样不是\x01",
            "更加令人羡慕嘛！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_754D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_754D)

    def lambda_755A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_755A)
    TurnDirection(0x1F, 0x104, 500)

    #C0351
    ChrTalk(
        0x1F,
        "#6P哎呀，兰迪先生～？\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x20,
        (
            "莫非你是想说，塞茜尔前辈\x01",
            "和伊莉娅·普拉提耶\x01",
            "比我们更好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        "#0309F#5P哪里～绝无此意。\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    #C0354
    ChrTalk(
        0x21,
        (
            "#5P呵呵，不然罗伊德\x01",
            "也和我们一起去玩吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x21,
        (
            "#5P我们正打算去港湾区的公园\x01",
            "看小型演唱会呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7664():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_7664)

    def lambda_7671():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_7671)

    def lambda_767E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_767E)

    #C0356
    ChrTalk(
        0x101,
        (
            "#0002F#12P哦，好像很有趣啊。\x02\x03",

            "#0000F那好，我就跟你们一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x104,
        "#0300F#5P哦哦，来吧来吧。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x1F,
        (
            "#5P好，警察弟弟\x01",
            "也被抓到啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x20,
        "#11P向港湾区进发吧！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x78, 0x258)

    def lambda_7731():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7731)
    Sleep(50)

    def lambda_774E():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_774E)
    Sleep(100)

    def lambda_776B():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_776B)
    Sleep(100)

    def lambda_7788():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_7788)

    def lambda_77A2():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_77A2)
    FadeToDark(3000, 0, -1)
    OP_0D()

    label("loc_77C2")

    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样──\x01",
            "纪念庆典的第一天很快就过去了。\x02\x03",

            "那天晚上，罗伊德来到塞茜尔的家中，\x01",
            "与塞茜尔一家人共进晚餐……\x02\x03",

            "席间，又谈起了去世的哥哥盖伊，\x01",
            "共同分享了令人难忘的回忆。\x02\x03",

            "然后──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 6)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_5297 end

    def Function_36_7893(): pass

    label("Function_36_7893")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-4770, 1950, -2080, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10500, 0)
    SetChrPos(0x101, -4210, 0, -1770, 355)
    SetChrPos(0x102, -3290, 0, -3440, 355)
    SetChrPos(0x103, -4520, 0, -3350, 355)
    SetChrPos(0x104, -3020, 0, -1890, 355)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0361
    ChrTalk(
        0x101,
        (
            "#6P#0001F比萨店『帕雷特比萨店』……\x01",
            "是遭窃的露天店啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#12P#0100F请问，能打扰一下吗？\x01",
            "我们在进行盗窃案的调查……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0363
    ChrTalk(
        0xFE,
        "#5P哦，那件事啊。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "#5P真是伤脑筋呢。\x01",
            "虽说当时正在接待客人，\x01",
            "不过还是太大意了……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x104,
        "#11P#0305F……接待客人？\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "#5P嗯，有个健谈的小哥\x01",
            "点了份热带比萨套餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "#5P嗯～以我接待客人的经验来说，\x01",
            "那应该是从外国来的游客吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "#5P总而言之，正当我\x01",
            "把餐点交给那位小哥的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "#5P我就感觉背后\x01",
            "传来了响动……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "#5P现在想想的话，那一定是\x01",
            "撬开收银盒的声音吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "#5P可恶，我竟然会犯这种错误……！\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#6P#0000F原来如此……\x01",
            "感谢您的合作。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D3B")
    OP_68(-4460, 1950, -3230, 1200)

    def lambda_7BC0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7BC0)

    def lambda_7BCD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7BCD)

    def lambda_7BDA():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7BDA)

    def lambda_7BE7():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7BE7)
    Sleep(1200)

    #C0373
    ChrTalk(
        0x101,
        "#6P#0003F询问工作就到此为止吧……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        (
            "#11P#0300F是啊，差不多也该回去\x01",
            "整理一下情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D35")

    #C0375
    ChrTalk(
        0x102,
        (
            "#12P#0100F工商协会那边也没有和我们联络，\x01",
            "看样子，似乎还没有\x01",
            "出现新的案情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        (
            "#12P#0203F是吧。\x02\x03",

            "#0200F……慎重起见，\x01",
            "在回去的路上，顺便再留意\x01",
            "一下那些露天店铺吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D35")

    OP_29(0x20, 0x1, 0xD)

    label("loc_7D3B")

    OP_5A()
    SetChrPos(0x0, -3450, 0, -1670, 0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_7893 end

    def Function_37_7D5E(): pass

    label("Function_37_7D5E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    LoadChrToIndex("chr/ch21300.itc", 0x29)
    SoundLoad(806)
    OP_68(-10760, 3710, 22590, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14300, 0)
    SetChrPos(0x101, -13630, 1340, 14190, 0)
    SetChrPos(0x102, -13510, 1240, 13230, 0)
    SetChrPos(0x103, -14640, 980, 14590, 45)
    SetChrPos(0x104, -14440, 930, 13700, 45)
    SetChrPos(0x22, -10770, 1770, 22760, 0)
    SetChrPos(0x23, -7540, 1770, 14200, 315)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x22, 0x0)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x29)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x22, 0, 0, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrName("")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人前往目标街区，\x01",
            "随后埋伏了下来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-10760, 2710, 22590, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0x8, 1, 0, 38)
    Sleep(150)
    BeginChrThread(0x22, 1, 0, 38)
    OP_0D()
    OP_6F(0x1)

    #A0378
    AnonymousTalk(
        0x101,
        (
            "#0001F………………………………\x02\x03",

            "看来不是这位客人呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x22, 0x1)
    OP_64(0x8)
    OP_64(0x22)
    Sleep(200)
    OP_95(0x22, -1540, 1990, 21840, 1500, 0x0)

    def lambda_7F15():
        OP_95(0xFE, 2270, 1990, 18430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7F15)
    Sleep(1000)
    OP_95(0x23, -10750, 1760, 22660, 2000, 0x0)
    OP_93(0x23, 0x0, 0x190)
    BeginChrThread(0x8, 1, 0, 38)
    Sleep(150)
    BeginChrThread(0x23, 1, 0, 38)
    Sleep(2500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x23, 0x1)
    OP_64(0x8)
    OP_64(0x23)
    Sleep(200)
    OP_95(0x23, -7540, 1770, 14200, 2000, 0x0)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)

    #A0379
    AnonymousTalk(
        0x104,
        "#0306F还不来啊……\x02",
    )

    CloseMessageWindow()

    #A0380
    AnonymousTalk(
        0x103,
        (
            "#0211F都已经在这里\x01",
            "埋伏了一个多小时了……\x02",
        )
    )

    CloseMessageWindow()

    #A0381
    AnonymousTalk(
        0x101,
        (
            "#0001F真奇怪啊，都这么久了，\x01",
            "也该来了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-14510, 3210, 13420, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13550, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x5A, 0x190)
    Sleep(50)

    def lambda_805B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_805B)

    def lambda_8068():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8068)

    def lambda_8075():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8075)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0382
    ChrTalk(
        0x101,
        (
            "#11P#0001F您好，我是罗伊德·班宁斯──\x02\x03",

            "#0005F哎，盗窃犯出现了……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0383
    ChrTalk(
        0x101,
        (
            "#11P#0005F好、好，是中央广场对吧。\x02\x03",

            "明白了，我们马上就过去！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)
    Sleep(200)

    #C0384
    ChrTalk(
        0x101,
        (
            "#0003F#11P……抱歉，各位。\x01",
            "看来是我计算错误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x102,
        "#12P#0101F别说这些了，赶快出发吧，罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#0001F#11P也、也是啊。\x01",
            "当务之急是赶往现场！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8253():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8253)

    def lambda_8260():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8260)

    def lambda_826D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_826D)

    def lambda_827A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_827A)
    Sleep(300)
    WaitChrThread(0x102, 1)

    def lambda_828E():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_828E)

    def lambda_82A3():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_82A3)

    def lambda_82B8():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_82B8)

    def lambda_82CD():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_82CD)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_7D5E end

    def Function_38_82FA(): pass

    label("Function_38_82FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_831F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_38_82FA")

    label("loc_831F")

    Return()

    # Function_38_82FA end

    def Function_39_8320(): pass

    label("Function_39_8320")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_836C")
    SetChrName("")

    #A0387
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彩虹剧团似乎正在演出中，\x01",
            "还是不要进去了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_836C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83BA")
    SetChrName("")

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彩虹剧团似乎正在做准备工作，\x01",
            "还是不要进去了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_83BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8411")
    SetChrName("")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公演结束后，\x01",
            "似乎有很多观众留下未走，\x01",
            "还是不要进去了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_845D")
    SetChrName("")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "彩虹剧团似乎正在进行准备，\x01",
            "还是不要进去了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_845D")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Return()

    # Function_39_8320 end

    def Function_40_8474(): pass

    label("Function_40_8474")

    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_40_8474 end

    def Function_41_8490(): pass

    label("Function_41_8490")

    EventBegin(0x1)
    Call(0, 44)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_41_8490 end

    def Function_42_84AC(): pass

    label("Function_42_84AC")

    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_42_84AC end

    def Function_43_84C8(): pass

    label("Function_43_84C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8561")

    #C0391
    ChrTalk(
        0x101,
        (
            "#0001F得赶快收集\x01",
            "柯林的目击情报才行。\x02\x03",

            "#0003F前台接待和露天店店主……\x01",
            "总之，先去找这些可能会有线索的人\x01",
            "打听看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_85B5")

    label("loc_8561")


    #C0392
    ChrTalk(
        0x101,
        (
            "#0001F得赶快收集\x01",
            "柯林的目击情报才行。\x02\x03",

            "先向这一带可能会有线索的人\x01",
            "打听看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8619")

    #C0393
    ChrTalk(
        0x101,
        (
            "#0001F这边应该由艾莉在\x01",
            "负责调查。\x02\x03",

            "还是按照原定计划，继续在\x01",
            "我负责的街区探听吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8619")

    Return()

    # Function_43_84C8 end

    def Function_44_861A(): pass

    label("Function_44_861A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B3")

    #C0394
    ChrTalk(
        0x101,
        (
            "#0001F得赶快收集\x01",
            "柯林的目击情报才行。\x02\x03",

            "#0003F前台接待和露天店店主……\x01",
            "总之，先去找这些可能会有线索的人\x01",
            "打听看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_8707")

    label("loc_86B3")


    #C0395
    ChrTalk(
        0x101,
        (
            "#0001F得赶快收集\x01",
            "柯林的目击情报才行。\x02\x03",

            "先向这一带可能会有线索的人\x01",
            "打听看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8816")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B2")

    #C0396
    ChrTalk(
        0x101,
        (
            "#0001F住宅街那边应该由\x01",
            "哈罗德先生在负责寻找……\x02\x03",

            "如果找到的话，\x01",
            "肯定会马上联络我的吧。\x02\x03",

            "还是按照原定计划，\x01",
            "继续在我负责的街区探听吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_8816")

    label("loc_87B2")


    #C0397
    ChrTalk(
        0x101,
        (
            "#0001F住宅街那边应该由\x01",
            "哈罗德先生在负责寻找……\x02\x03",

            "还是按照原定计划，\x01",
            "继续在我负责的街区探听吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8816")

    Return()

    # Function_44_861A end

    SaveToFile()

Try(main)
