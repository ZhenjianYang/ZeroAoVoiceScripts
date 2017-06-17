from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c040b.bin",                # FileName
        "c040b",                    # MapName
        "c040b",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 4, 0, 5],
    )

    BuildStringList((
        "c040b",                  # 0
        "ソフィーユ",             # 1
        "客引きピム",             # 2
        "ポリセ",                 # 3
        "タップ",                 # 4
        "ラマンダ",               # 5
        "テージョ",               # 6
        "バニーガール",           # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "マクダエル市長",         # 11
        "秘書アーネスト",         # 12
        "ツァイト",               # 13
        "ダドリー捜査官",         # 14
        "セルゲイ課長",           # 15
        "イリア",                 # 16
        "リーシャ",               # 17
        "警備隊員",               # 18
        "警備隊員",               # 19
        "警備隊員",               # 20
        "警備隊員",               # 21
        "車１",                   # 22
        "車２",                   # 23
        "客",                     # 24
        "客",                     # 25
        "客",                     # 26
        "客",                     # 27
        "客",                     # 28
        "客",                     # 29
        "客",                     # 30
        "客",                     # 31
        "客",                     # 32
        "客",                     # 33
        "SE制御",                 # 34
        "中央広場",               # 35
        "西通り",                 # 36
        "行政区",                 # 37
        "住宅街",                 # 38
        "歓楽街",                 # 39
        "東通り",                 # 40
        "旧市街",                 # 41
        "港湾区",                 # 42
        "ＩＢＣ",                 # 43
        "駅前通り",               # 44
        "裏通り",                 # 45
        "ウルスラ間道",           # 46
        "東クロスベル街道",       # 47
        "西クロスベル街道",       # 48
        "マインツ山道",           # 49
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch32200.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch24400.itc",                   # 08
        "chr/ch33100.itc",                   # 09
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(230,     0,       -1830,   175,  277,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   8,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(300,     0,       -3799,   355,  277,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(1149,    0,       -4409,   310,  277,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(14829,   0,       2670,    90,   261,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclEvent(0x0000, 0, 58,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

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

    ScpFunction((
        "Function_0_814",          # 00, 0
        "Function_1_8CC",          # 01, 1
        "Function_2_A59",          # 02, 2
        "Function_3_B60",          # 03, 3
        "Function_4_B7C",          # 04, 4
        "Function_5_DF8",          # 05, 5
        "Function_6_E89",          # 06, 6
        "Function_7_FF5",          # 07, 7
        "Function_8_1090",         # 08, 8
        "Function_9_1158",         # 09, 9
        "Function_10_1192",        # 0A, 10
        "Function_11_120D",        # 0B, 11
        "Function_12_123D",        # 0C, 12
        "Function_13_128D",        # 0D, 13
        "Function_14_12E1",        # 0E, 14
        "Function_15_1333",        # 0F, 15
        "Function_16_13AE",        # 10, 16
        "Function_17_1427",        # 11, 17
        "Function_18_147C",        # 12, 18
        "Function_19_14D1",        # 13, 19
        "Function_20_153A",        # 14, 20
        "Function_21_15A3",        # 15, 21
        "Function_22_160C",        # 16, 22
        "Function_23_1675",        # 17, 23
        "Function_24_16DE",        # 18, 24
        "Function_25_1747",        # 19, 25
        "Function_26_17B0",        # 1A, 26
        "Function_27_1819",        # 1B, 27
        "Function_28_1876",        # 1C, 28
        "Function_29_18B3",        # 1D, 29
        "Function_30_18EB",        # 1E, 30
        "Function_31_1911",        # 1F, 31
        "Function_32_1937",        # 20, 32
        "Function_33_195D",        # 21, 33
        "Function_34_1983",        # 22, 34
        "Function_35_19BD",        # 23, 35
        "Function_36_19F7",        # 24, 36
        "Function_37_1F01",        # 25, 37
        "Function_38_1F40",        # 26, 38
        "Function_39_1F75",        # 27, 39
        "Function_40_2020",        # 28, 40
        "Function_41_205A",        # 29, 41
        "Function_42_20A6",        # 2A, 42
        "Function_43_2849",        # 2B, 43
        "Function_44_2C1E",        # 2C, 44
        "Function_45_3C9A",        # 2D, 45
        "Function_46_3D03",        # 2E, 46
        "Function_47_3E02",        # 2F, 47
        "Function_48_3E91",        # 30, 48
        "Function_49_3EDB",        # 31, 49
        "Function_50_3F28",        # 32, 50
        "Function_51_3F8F",        # 33, 51
        "Function_52_3FE8",        # 34, 52
        "Function_53_4138",        # 35, 53
        "Function_54_4185",        # 36, 54
        "Function_55_41DA",        # 37, 55
        "Function_56_4230",        # 38, 56
        "Function_57_4293",        # 39, 57
        "Function_58_42AD",        # 3A, 58
        "Function_59_43C6",        # 3B, 59
        "Function_60_43E2",        # 3C, 60
        "Function_61_43FE",        # 3D, 61
        "Function_62_441A",        # 3E, 62
    ))


    def Function_0_814(): pass

    label("Function_0_814")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_854"),
        (1, "loc_860"),
        (2, "loc_86C"),
        (3, "loc_878"),
        (4, "loc_884"),
        (5, "loc_890"),
        (6, "loc_89C"),
        (SWITCH_DEFAULT, "loc_8A8"),
    )


    label("loc_854")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_860")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_86C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_878")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_884")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_890")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_89C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8CB")

    Return()

    # Function_0_814 end

    def Function_1_8CC(): pass

    label("Function_1_8CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A58")
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
    Jump("Function_1_8CC")

    label("loc_A58")

    Return()

    # Function_1_8CC end

    def Function_2_A59(): pass

    label("Function_2_A59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5F")
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
    Jump("Function_2_A59")

    label("loc_B5F")

    Return()

    # Function_2_A59 end

    def Function_3_B60(): pass

    label("Function_3_B60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B7B")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_B60")

    label("loc_B7B")

    Return()

    # Function_3_B60 end

    def Function_4_B7C(): pass

    label("Function_4_B7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D93")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C47")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C23")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_C42")

    label("loc_C23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_C42")

    Jump("loc_D93")

    label("loc_C47")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CFB")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD7")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_CF6")

    label("loc_CD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF6")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_CF6")

    Jump("loc_D93")

    label("loc_CFB")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D74")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_D93")

    label("loc_D74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D93")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_D93")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAD")
    Event(0, 43)

    label("loc_DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DC1")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 36)
    Jump("loc_DE4")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DD5")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 42)
    Jump("loc_DE4")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_DE4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 44)

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DF7")
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_DF7")

    Return()

    # Function_4_B7C end

    def Function_5_DF8(): pass

    label("Function_5_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_E1E")
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    Jump("loc_E36")

    label("loc_E1E")

    SetMapObjFrame(0xFF, "ka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x0, 0x1)

    label("loc_E36")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E4E")

    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E70")
    OP_1B(0x1, 0x0, 0x3B)
    OP_1B(0x2, 0x0, 0x3C)

    label("loc_E70")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E88")
    OP_1B(0x0, 0x0, 0x3D)

    label("loc_E88")

    Return()

    # Function_5_DF8 end

    def Function_6_E89(): pass

    label("Function_6_E89")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_EF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F14")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FEC")

    label("loc_F14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F28")
    Jump("loc_FEC")

    label("loc_F28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F8A")

    #C0001
    ChrTalk(
        0x8,
        (
            "お商売人はつらいですねー。\x01",
            "さだめってやつですかねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEC")

    label("loc_F8A")


    #C0002
    ChrTalk(
        0x8,
        "夜のクロスベルはきれーですねー。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "わたしもお商売がなきゃあ\x01",
            "遊んで回る所なんですがー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FEC")

    Jump("loc_E96")

    label("loc_FF1")

    TalkEnd(0xFE)
    Return()

    # Function_6_E89 end

    def Function_7_FF5(): pass

    label("Function_7_FF5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1089")

    #C0004
    ChrTalk(
        0xFE,
        (
            "ああ、君らも遊んでいく？\x01",
            "ウチはおいしいお酒が飲めるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "へっへ、４人だったら\x01",
            "団体割引も効くしね。\x01",
            "まあ一度考えてみてよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108C")

    label("loc_1089")

    Call(0, 8)

    label("loc_108C")

    TalkEnd(0xFE)
    Return()

    # Function_7_FF5 end

    def Function_8_1090(): pass

    label("Function_8_1090")

    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0006
    ChrTalk(
        0xF,
        "ほ、本当に大丈夫なのかね？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xF,
        (
            "そのう、興味はあるが\x01",
            "少し怖いというか、なんというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "ふはははははは……！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "大丈夫だよ、僕ら\x01",
            "そんなに黒い人じゃないから。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_8_1090 end

    def Function_9_1158(): pass

    label("Function_9_1158")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xA,
        (
            "きゃっ、そろそろ公演時間ね！\x01",
            "胸が高鳴るわ～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1158 end

    def Function_10_1192(): pass

    label("Function_10_1192")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xB,
        "夜の歓楽街ってドキドキするよな……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "くそっ、チケットがあれば\x01",
            "アルカンシェルの舞台を\x01",
            "満喫する所なんだが……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1192 end

    def Function_11_120D(): pass

    label("Function_11_120D")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xC,
        (
            "うふふ、今夜は\x01",
            "どこで遊ぼうかしら。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_120D end

    def Function_12_123D(): pass

    label("Function_12_123D")

    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xD,
        "よし、今夜も遊ぶかぁ！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xD,
        (
            "まずはカジノで\x01",
            "今日の運を試してやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_123D end

    def Function_13_128D(): pass

    label("Function_13_128D")

    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xE,
        (
            "カジノハウス《バルカ》は\x01",
            "今日も絶好調よ～ン！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_128D end

    def Function_14_12E1(): pass

    label("Function_14_12E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_132C")

    #C0018
    ChrTalk(
        0xF,
        (
            "こ、こほん……\x01",
            "妻には内緒に\x01",
            "しておいてくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132F")

    label("loc_132C")

    Call(0, 8)

    label("loc_132F")

    TalkEnd(0xFE)
    Return()

    # Function_14_12E1 end

    def Function_15_1333(): pass

    label("Function_15_1333")

    TalkBegin(0xFE)
    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0019
    ChrTalk(
        0x10,
        (
            "おっ、先輩。\x01",
            "いっちゃうんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10,
        (
            "へへへ……俺もちょっと\x01",
            "興味沸いてきちゃいましたよー。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_15_1333 end

    def Function_16_13AE(): pass

    label("Function_16_13AE")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "妻と娘がショッピングに行ったっきり\x01",
            "帰ってこないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "はあ、仕方ない。\x01",
            "先にホテルに帰ってるかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_13AE end

    def Function_17_1427(): pass

    label("Function_17_1427")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -2550, 1860, 25760, 0)
    OP_95(0xFE, -2550, 2660, 35120, 1000, 0x0)

    def lambda_145B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_145B)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_17_1427 end

    def Function_18_147C(): pass

    label("Function_18_147C")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -1280, 1990, 24700, 0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_14B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14B0)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_18_147C end

    def Function_19_14D1(): pass

    label("Function_19_14D1")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 4520, 1890, 19530, 333)
    OP_95(0xFE, -1330, 2150, 30540, 1000, 0x0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_1519():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1519)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_19_14D1 end

    def Function_20_153A(): pass

    label("Function_20_153A")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 4040, 1950, 18100, 333)
    OP_95(0xFE, -2660, 2430, 31010, 1000, 0x0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_1582():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1582)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_20_153A end

    def Function_21_15A3(): pass

    label("Function_21_15A3")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -7760, 1920, 21240, 26)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_15EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15EB)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_21_15A3 end

    def Function_22_160C(): pass

    label("Function_22_160C")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -7210, 1990, 19830, 26)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1654():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1654)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_22_160C end

    def Function_23_1675(): pass

    label("Function_23_1675")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -30, 1810, 12140, 341)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_16BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16BD)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_23_1675 end

    def Function_24_16DE(): pass

    label("Function_24_16DE")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 1150, 1760, 11990, 341)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1726():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1726)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_24_16DE end

    def Function_25_1747(): pass

    label("Function_25_1747")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -5550, 1990, 15680, 26)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_178F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_178F)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_25_1747 end

    def Function_26_17B0(): pass

    label("Function_26_17B0")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -4270, 1990, 16100, 26)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_17F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17F8)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_26_17B0 end

    def Function_27_1819(): pass

    label("Function_27_1819")

    OP_95(0xFE, -8970, 330, 5920, 2000, 0x0)
    OP_93(0xFE, 0x109, 0x1F4)

    def lambda_1839():

        label("loc_1839")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_1839")

    QueueWorkItem2(0xFE, 2, lambda_1839)
    Sleep(2500)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, -7220, 1770, 9000, 1200, 0x0)
    OP_95(0xFE, -2350, 1990, 19350, 1200, 0x0)
    Return()

    # Function_27_1819 end

    def Function_28_1876(): pass

    label("Function_28_1876")

    OP_95(0xFE, -10140, 250, 6390, 1200, 0x0)
    OP_95(0xFE, -8109, 1770, 9690, 1200, 0x0)
    OP_95(0xFE, -3180, 1990, 19840, 1200, 0x0)
    Return()

    # Function_28_1876 end

    def Function_29_18B3(): pass

    label("Function_29_18B3")

    OP_9F(0x0, 0x1D)
    OP_9F(0x1, -28630, 0, 10380)
    OP_9F(0x1, -19800, 0, 9100)
    OP_9F(0x1, -11600, 0, 3800)
    OP_9F(0x2, 0x1D, 5000, 0x6)
    Return()

    # Function_29_18B3 end

    def Function_30_18EB(): pass

    label("Function_30_18EB")

    SetChrPos(0xFE, 470, 1770, 10040, 45)
    OP_95(0xFE, -3140, 1760, 29500, 1500, 0x0)
    Return()

    # Function_30_18EB end

    def Function_31_1911(): pass

    label("Function_31_1911")

    SetChrPos(0xFE, 1910, 1770, 10160, 45)
    OP_95(0xFE, -1330, 1760, 29360, 1500, 0x0)
    Return()

    # Function_31_1911 end

    def Function_32_1937(): pass

    label("Function_32_1937")

    SetChrPos(0xFE, -6160, 1590, 7540, 315)
    OP_95(0xFE, -3140, 1760, 29500, 1500, 0x0)
    Return()

    # Function_32_1937 end

    def Function_33_195D(): pass

    label("Function_33_195D")

    SetChrPos(0xFE, -5150, 1640, 7470, 314)
    OP_95(0xFE, -1330, 1760, 29360, 1500, 0x0)
    Return()

    # Function_33_195D end

    def Function_34_1983(): pass

    label("Function_34_1983")

    SetChrPos(0xFE, -7000, 690, 5700, 314)
    OP_95(0xFE, -6030, 1770, 9130, 1200, 0x0)
    OP_95(0xFE, -3140, 1760, 29500, 1200, 0x0)
    Return()

    # Function_34_1983 end

    def Function_35_19BD(): pass

    label("Function_35_19BD")

    SetChrPos(0xFE, -5600, 740, 5500, 44)
    OP_95(0xFE, -4950, 1770, 8820, 1200, 0x0)
    OP_95(0xFE, -1330, 1760, 29360, 1200, 0x0)
    Return()

    # Function_35_19BD end

    def Function_36_19F7(): pass

    label("Function_36_19F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch02700.itc", 0x20)
    LoadChrToIndex("chr/ch33000.itc", 0x28)
    LoadChrToIndex("chr/ch33300.itc", 0x29)
    LoadChrToIndex("chr/ch27700.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadChrToIndex("chr/ch33100.itc", 0x2C)
    LoadChrToIndex("chr/ch32400.itc", 0x2D)
    LoadChrToIndex("chr/ch22000.itc", 0x2E)
    LoadChrToIndex("chr/ch33200.itc", 0x2F)
    LoadChrToIndex("chr/ch27800.itc", 0x30)
    LoadChrToIndex("chr/ch27900.itc", 0x31)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrChipByIndex(0x20, 0x29)
    SetChrChipByIndex(0x21, 0x2A)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrChipByIndex(0x24, 0x2D)
    SetChrChipByIndex(0x25, 0x2E)
    SetChrChipByIndex(0x26, 0x2F)
    SetChrChipByIndex(0x27, 0x30)
    SetChrChipByIndex(0x28, 0x31)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_68(-14500, 1950, 7000, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, -3000, 1990, 20500, 180)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, -3000, 1990, 21500, 180)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x4, 0x1D)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, -28630, 0, 10380, 130)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
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
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    BeginChrThread(0x29, 0, 0, 37)
    FadeToBright(3000, 0)
    OP_68(-2580, 10570, 29050, 0)
    MoveCamera(20, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36500, 0)
    OP_68(-2580, 10570, 29050, 14000)
    MoveCamera(345, -13, 0, 14000)
    OP_6E(800, 14000)
    SetCameraDistance(36500, 14000)
    BeginChrThread(0x1F, 0, 0, 17)
    BeginChrThread(0x20, 0, 0, 18)
    BeginChrThread(0x21, 0, 0, 19)
    BeginChrThread(0x22, 0, 0, 20)
    BeginChrThread(0x23, 0, 0, 21)
    BeginChrThread(0x24, 0, 0, 22)
    BeginChrThread(0x25, 0, 0, 23)
    BeginChrThread(0x26, 0, 0, 24)
    BeginChrThread(0x27, 0, 0, 25)
    BeginChrThread(0x28, 0, 0, 26)
    Sleep(6000)
    BeginChrThread(0x1D, 0, 0, 29)
    Sleep(2000)
    Fade(500)
    Fade(500)
    Sound(459, 0, 100, 0)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x1F, 0, 0, 30)
    BeginChrThread(0x20, 0, 0, 31)
    BeginChrThread(0x21, 0, 0, 32)
    BeginChrThread(0x22, 0, 0, 33)
    BeginChrThread(0x23, 0, 0, 34)
    BeginChrThread(0x24, 0, 0, 35)
    OP_68(-10140, 2050, 6000, 0)
    MoveCamera(12, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_6E(600, 10000)
    WaitChrThread(0x1D, 0)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0xF1, 0x10E, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, -10990, 0, 4660, 208)
    SetChrPos(0x13, -10990, 0, 4660, 208)
    BeginChrThread(0x13, 0, 0, 27)
    Sleep(1500)
    BeginChrThread(0x12, 0, 0, 28)
    Sleep(1600)
    OP_71(0x4, 0x10F, 0x12C, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0x4)
    Sleep(1500)
    Fade(500)
    OP_68(10490, 2380, 14240, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17000, 0)
    OP_68(10490, 2380, 14240, 6000)
    MoveCamera(19, 19, 0, 6000)
    OP_6E(580, 6000)
    SetCameraDistance(17000, 6000)
    SetChrPos(0x104, 13520, 0, 14590, 270)

    def lambda_1E37():
        OP_95(0xFE, 8590, 1770, 14770, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E37)
    SetChrPos(0x103, 15170, 0, 14690, 270)

    def lambda_1E62():
        OP_95(0xFE, 9760, 1400, 14890, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1E62)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 15760, 0, 13260, 272)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)

    def lambda_1EA9():
        OP_95(0xFE, 9320, 1410, 13720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1EA9)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sleep(3000)
    BeginChrThread(0x29, 0, 0, 38)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x29, 1)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x323)
    SetScenarioFlags(0x5C, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_19F7 end

    def Function_37_1F01(): pass

    label("Function_37_1F01")

    Sound(803, 2, 0, 0)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x50)
    Return()

    # Function_37_1F01 end

    def Function_38_1F40(): pass

    label("Function_38_1F40")

    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_24(0x323)
    Return()

    # Function_38_1F40 end

    def Function_39_1F75(): pass

    label("Function_39_1F75")

    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)

    def lambda_1F82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F82)
    OP_95(0xFE, -2210, 2660, 31430, 5000, 0x0)
    OP_95(0xFE, -2210, 1760, 27140, 5000, 0x0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 1000, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetChrFlags(0x13, 0x20)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    OP_95(0xFE, -2360, 1940, 25100, 5000, 0x0)
    Return()

    # Function_39_1F75 end

    def Function_40_2020(): pass

    label("Function_40_2020")


    def lambda_2025():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2025)
    OP_95(0xFE, -2720, 2660, 31430, 5000, 0x0)
    OP_95(0xFE, -2720, 1760, 29040, 5000, 0x0)
    Return()

    # Function_40_2020 end

    def Function_41_205A(): pass

    label("Function_41_205A")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_206D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_206D)
    OP_95(0xFE, -1310, 2580, 31270, 5000, 0x0)
    OP_95(0xFE, -1170, 1760, 29010, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    Return()

    # Function_41_205A end

    def Function_42_20A6(): pass

    label("Function_42_20A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("apl/ch50229.itc", 0x20)
    LoadChrToIndex("apl/ch50230.itc", 0x21)
    LoadChrToIndex("apl/ch50232.itc", 0x22)
    LoadChrToIndex("apl/ch50233.itc", 0x23)
    LoadChrToIndex("chr/ch00950.itc", 0x28)
    LoadChrToIndex("chr/ch00951.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00356.itc", 0x2E)
    LoadChrToIndex("chr/ch00351.itc", 0x2F)
    LoadChrToIndex("chr/ch00250.itc", 0x30)
    LoadChrToIndex("chr/ch00251.itc", 0x31)
    LoadChrToIndex("chr/ch00252.itc", 0x32)
    LoadChrToIndex("apl/ch50231.itc", 0x33)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0xA)
    SetChrChipByIndex(0x103, 0x30)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrPos(0x101, -2160, 2660, 36390, 180)
    SetChrPos(0x15, -2160, 2660, 36390, 180)
    SetChrPos(0x13, -2160, 2660, 36390, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, -2660, 1990, 18290, 0)
    SetChrPos(0x103, 3680, 1960, 17210, 135)
    LoadEffect(0x0, "event\\ev201_00.eff")
    LoadEffect(0x1, "battle\\ms00004.eff")
    OP_68(-2160, 4600, 35160, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(21500, 0)
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
    FadeToBright(1000, 0)
    BeginChrThread(0x13, 0, 0, 39)
    OP_68(-2040, 2800, 25190, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(480, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(1000)
    Sound(1221, 255, 100, 0)    #voice#Tio
    Sleep(500)
    SetChrPos(0x1D, -2210, 1760, 25140, 0)
    PlayEffect(0x0, 0xFF, 0x103, 0x0, 0, 1600, 0, 0, 0, 0, 1000, 1000, 1000, 0x1D, 0, 1000, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(250)
    Sound(1876, 255, 100, 2)    #voice#Earnest
    Sound(251, 0, 100, 0)
    WaitChrThread(0x13, 0)
    Sleep(500)

    def lambda_2341():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2341)
    SetChrChipByIndex(0x13, 0x33)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x2)
    Sound(1320, 255, 100, 1)    #voice#Randy
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    Sound(250, 0, 100, 0)
    Sleep(100)
    SetChrChip(0x0, 0x104, 0x32, 0x12C)
    SetChrSubChip(0x104, 0x1)
    OP_99(0x104, 0x13, 0x1F4, 0x2328, 0x0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x2)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    Sound(1877, 255, 100, 2)    #voice#Earnest
    SetChrSubChip(0x104, 0x2)
    Sound(814, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sound(830, 0, 100, 0)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    OP_9D(0x104, 0xFFFFF682, 0x7C6, 0x59EC, 0x3E8, 0x7D0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    Sound(514, 0, 100, 0)
    SetChrSubChip(0x104, 0x0)
    Sound(31, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x104, 0x2F)
    ClearChrFlags(0x104, 0x20)
    OP_95(0x104, -2280, 1990, 24350, 5000, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0023
    ChrTalk(
        0x104,
        "#0301F#11Pふう……何だってんだ。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 0x30)
    OP_95(0x103, -840, 1990, 23150, 5000, 0x0)
    TurnDirection(0x103, 0x13, 500)
    Sleep(300)

    #C0024
    ChrTalk(
        0x103,
        (
            "#0201F#11Pどうやら一連の事件の\x01",
            "真犯人みたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "ランディ、ティオ！\x02",
    )

    CloseMessageWindow()
    OP_68(-2120, 2810, 27360, 3000)
    BeginChrThread(0x101, 0, 0, 40)
    Sleep(1000)
    BeginChrThread(0x15, 0, 0, 41)
    WaitChrThread(0x101, 0)
    Sleep(1500)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0026
    ChrTalk(
        0x101,
        (
            "#0002F#5Pよかった……\x01",
            "捕まえてくれたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0301F#12Pああ、拳銃を持ってたから\x01",
            "思わず気絶させちまったぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0004F#5Pああ、それでいいよ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#0205F#12Pそれで、どうしてロイドさんが\x01",
            "一課のメガネスーツさんと……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x15,
        (
            "#0607F#5Pだ、誰がメガネスーツだ！\x02\x03",

            "#0603Fお前たち……\x01",
            "これは一体どういうことだ？\x02\x03",

            "#0601Fバックアップまで用意して\x01",
            "一体、何をしていた……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0008F#5Pそれは……\x02",
    )

    CloseMessageWindow()

    def lambda_26CB():

        label("loc_26CB")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_26CB")

    QueueWorkItem2(0x101, 2, lambda_26CB)

    def lambda_26DD():

        label("loc_26DD")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_26DD")

    QueueWorkItem2(0x104, 2, lambda_26DD)

    def lambda_26EF():

        label("loc_26EF")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_26EF")

    QueueWorkItem2(0x103, 2, lambda_26EF)

    def lambda_2701():

        label("loc_2701")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_2701")

    QueueWorkItem2(0x15, 2, lambda_2701)
    Sound(1901, 255, 100, 0)    #voice#Earnest
    SetChrChipByIndex(0x13, 0x1F)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x2)
    OP_96(0x104, 0xFFFFF6AA, 0x7C6, 0x5B04, 0x1770, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    Sound(819, 0, 100, 0)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetChrChip(0x0, 0x13, 0x32, 0x12C)
    SetChrChipByIndex(0x13, 0x20)
    ClearChrFlags(0x13, 0x20)

    def lambda_2779():
        OP_95(0xFE, 8780, 1760, 24750, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2779)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x104,
        "#0307F#5Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0007F#5Pまだ動けたのか……！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_20A6 end

    def Function_43_2849(): pass

    label("Function_43_2849")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21000, 6500, 7000, 0)
    MoveCamera(45, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -26500, 300, 17500, 180)
    SetChrPos(0x102, -25800, 300, 17500, 180)
    SetChrPos(0x103, -27200, 300, 17500, 180)
    SetChrPos(0x104, -26500, 300, 17500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(-21000, 5000, 7000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_294A():
        OP_96(0xFE, 0xFFFF987C, 0x0, 0x2A94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_294A)

    def lambda_2964():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2964)
    Sleep(700)

    def lambda_2978():
        OP_96(0xFE, 0xFFFF94F8, 0x0, 0x2E7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2978)

    def lambda_2992():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2992)
    Sleep(700)

    def lambda_29A6():
        OP_96(0xFE, 0xFFFF9C00, 0x0, 0x2F44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29A6)

    def lambda_29C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29C0)
    Sleep(700)

    def lambda_29D4():
        OP_96(0xFE, 0xFFFF987C, 0x0, 0x332C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29D4)

    def lambda_29EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_29EE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-26500, 1000, 12000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0034
    ChrTalk(
        0x101,
        "#5P#0001Fもう日が暮れたか……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#0000Fとにかくガンツさんと\x01",
            "一度話をしてみないとな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AC7)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Sleep(100)

    #C0036
    ChrTalk(
        0x102,
        (
            "#5P#0104Fええ、向こうにある\x01",
            "ホテルに行ってみましょう。\x02\x03",

            "#0100Fデラックスルームは\x01",
            "確か最上階にあったはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#5P#0306Fカジノで大勝ちをして\x01",
            "優雅にホテル暮らしかよ……\x02\x03",

            "#0301Fったく、羨ましいじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0211Fランディさん。\x01",
            "そういう問題では……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -26500, 0, 12000, 180)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetScenarioFlags(0xC1, 7)
    EventEnd(0x5)
    Return()

    # Function_43_2849 end

    def Function_44_2C1E(): pass

    label("Function_44_2C1E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31250.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch05100.itc", 0x27)
    LoadChrToIndex("chr/ch05200.itc", 0x28)
    LoadChrToIndex("chr/ch00150.itc", 0x29)
    LoadChrToIndex("chr/ch00151.itc", 0x2A)
    LoadChrToIndex("chr/ch00250.itc", 0x2B)
    LoadChrToIndex("chr/ch00251.itc", 0x2C)
    LoadChrToIndex("chr/ch00950.itc", 0x2D)
    LoadChrToIndex("chr/ch00951.itc", 0x2E)
    LoadChrToIndex("chr/ch00952.itc", 0x2F)
    LoadChrToIndex("apl/ch50509.itc", 0x30)
    LoadChrToIndex("chr/ch00152.itc", 0x31)
    LoadChrToIndex("chr/ch00254.itc", 0x32)
    OP_68(6100, 1000, -6300, 0)
    MoveCamera(35, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 9000, 0, -13700, 0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8600, 0, -15200, 0)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 9800, 0, -15700, 0)
    SetChrPos(0x104, 10200, 0, -14200, 0)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 11000, 0, -13700, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 9900, 0, -15000, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 5000, 0, -14500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -22600, 500, 9200, 180)
    SetChrPos(0x1A, -22600, 500, 9200, 180)
    SetChrPos(0x1B, -22600, 500, 9200, 180)
    SetChrPos(0x1C, -22600, 500, 9200, 180)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 1600, 1770, 13000, 180)
    SetChrChipByIndex(0x18, 0x28)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_90(0x18, 600, 1770, 13400, 180)
    OP_78(0x8, 0x1D)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    OP_49()
    SetChrPos(0x1D, -22000, 0, 10000, 0)
    OP_D3(0x1D, 0x0, 0x186A0, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x0)
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
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "battle\\mgaria1.eff")
    LoadEffect(0x2, "battle\\mg030_00.eff")
    LoadEffect(0x4, "battle\\btgun00.eff")

    def lambda_2F98():
        OP_96(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F98)
    Sleep(50)

    def lambda_2FB5():
        OP_96(0xFE, 0x1068, 0x0, 0xFFFFFB50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FB5)
    Sleep(50)

    def lambda_2FD2():
        OP_96(0xFE, 0xA28, 0x0, 0xFFFFF768, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FD2)
    Sleep(50)

    def lambda_2FEF():
        OP_96(0xFE, 0xED8, 0x0, 0xFFFFF574, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FEF)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 3, 0, 3)

    def lambda_302D():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_302D)
    OP_68(3100, 1000, -1700, 3000)
    MoveCamera(45, 21, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    FadeToBright(2000, 0)
    BeginChrThread(0x29, 1, 0, 57)
    WaitChrThread(0x101, 1)

    def lambda_3088():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3088)
    WaitChrThread(0x104, 1)

    def lambda_3099():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3099)
    WaitChrThread(0x102, 1)

    def lambda_30AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30AA)
    WaitChrThread(0x103, 1)

    def lambda_30BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_30BB)
    WaitChrThread(0x14, 1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_30F2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_30F2)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)

    #C0039
    ChrTalk(
        0x101,
        "#0006F#5Pはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#0306F#5Pさすがにキツイな……\x02",
    )

    CloseMessageWindow()

    #N0041
    NpcTalk(
        0x101,
        "キーア",
        "#6P#1112Fロイド～、だいじょうぶ？\x02",
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x104,
        "シズク",
        "#6P#6001Fわ、わたし、降ります……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#0000F#5Pいや、大丈夫だ……！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0309F#5Pハハ……\x01",
            "こんくらい任せとけって。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)

    #N0045
    NpcTalk(
        0x17,
        "女性の声",
        "#4Pあら、弟君じゃない。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3295():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3295)

    def lambda_32A2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32A2)

    def lambda_32AF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_32AF)

    def lambda_32BC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_32BC)

    def lambda_32C9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_32C9)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    OP_68(3100, 1000, 200, 4000)

    def lambda_32F6():
        OP_96(0xFE, 0xE10, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_32F6)
    Sleep(100)

    def lambda_3313():
        OP_96(0xFE, 0xA28, 0xA, 0x960, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3313)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    OP_6F(0x1)

    #C0046
    ChrTalk(
        0x101,
        "#12P#0011Fイリアさん、リーシャ！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x18,
        "#1808F#5Pみ、皆さん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3456")

    #N0048
    NpcTalk(
        0x101,
        "キーア",
        (
            "#1105F#11Pあ、リーシャと\x01",
            "ぐーすか寝てたヒトだー！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x17,
        (
            "#5P#1705Fぐーすか寝てた……？\x02\x03",

            "#1702Fそれはともかく\x01",
            "可愛い子を連れてるわね。\x02\x03",

            "#1709Fおっきな犬までいるし、\x01",
            "楽しそうな組み合わせじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363B")

    label("loc_3456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34FC")

    #N0050
    NpcTalk(
        0x101,
        "キーア",
        "#1110F#11Pあ、リーシャだー！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x17,
        (
            "#5P#1705Fへえ、可愛い子を連れてるわね。\x02\x03",

            "#1709Fおっきな犬までいるし、\x01",
            "楽しそうな組み合わせじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363B")

    label("loc_34FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35D1")

    #N0052
    NpcTalk(
        0x101,
        "キーア",
        "#1105F#11Pあ、ぐーすか寝てたヒトだー！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x17,
        (
            "#5P#1705Fぐーすか寝てた……？\x02\x03",

            "#1702Fそれはともかく\x01",
            "可愛い子を連れてるわね。\x02\x03",

            "#1709Fおっきな犬までいるし、\x01",
            "楽しそうな組み合わせじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363B")

    label("loc_35D1")


    #C0054
    ChrTalk(
        0x17,
        (
            "#5P#1705Fへえ、可愛い子を連れてるわね。\x02\x03",

            "#1709Fおっきな犬までいるし、\x01",
            "楽しそうな組み合わせじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363B")


    #C0055
    ChrTalk(
        0x101,
        (
            "#12P#0007F２人とも、急いで\x01",
            "劇場内に避難してください！\x02\x03",

            "すぐに連中が──\x02",
        )
    )

    CloseMessageWindow()
    Sound(489, 0, 100, 0)
    Sleep(1000)
    Sound(495, 0, 100, 0)
    Sleep(200)
    OP_24(0x1E9)
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
    Sleep(1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_68(-22000, 1000, 10000, 2000)
    MoveCamera(345, 27, 0, 2000)
    SetCameraDistance(18500, 2000)

    def lambda_3739():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3739)
    Sleep(50)

    def lambda_3749():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3749)

    def lambda_3756():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3756)
    Sleep(50)

    def lambda_3766():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3766)

    def lambda_3773():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3773)
    Sleep(50)

    def lambda_3783():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3783)

    def lambda_3790():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3790)
    OP_6F(0x79)
    OP_71(0x8, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x8)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    BeginChrThread(0x19, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1A, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1B, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1C, 3, 0, 55)
    WaitChrThread(0x19, 3)
    Fade(500)
    OP_68(3100, 1000, 200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    ClearScenarioFlags(0x0, 2)

    def lambda_3837():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3837)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x3)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x102, 3, 0, 47)
    BeginChrThread(0x103, 3, 0, 46)
    OP_0D()
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x1B, 0xFF)
    EndChrThread(0x1C, 0xFF)

    #C0056
    ChrTalk(
        0x104,
        (
            "#0307F#11Pチッ……\x01",
            "何台持ち出してんだっつーの！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x17,
        (
            "#11P#1705Fえ、え……\x01",
            "アトラクションか何か！？\x02\x03",

            "#1709F気合いが入ってるじゃない！？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        "#12P#0107Fとにかく避難してください！\x02",
    )

    CloseMessageWindow()
    OP_68(5600, 1000, -4800, 2000)
    MoveCamera(55, 21, 0, 2000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)

    def lambda_3971():
        OP_95(0xFE, 7000, 0, -5700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3971)
    Sleep(100)

    def lambda_398E():
        OP_95(0xFE, 5900, 0, -7000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_398E)
    WaitChrThread(0x10A, 1)

    def lambda_39AC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_39AC)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)

    def lambda_39C5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_39C5)
    WaitChrThread(0x16, 2)

    def lambda_39D6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_39D6)
    OP_6F(0x41)

    #C0059
    ChrTalk(
        0x10A,
        "#11P#0607Fおい、何をしている！\x02",
    )

    CloseMessageWindow()

    def lambda_3A09():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A09)
    Sleep(50)

    def lambda_3A19():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A19)
    SetScenarioFlags(0x0, 2)

    #C0060
    ChrTalk(
        0x16,
        "#11P#1007F警察本部に急ぐぞ！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#3P#0007Fはい……！\x02",
    )

    CloseMessageWindow()
    OP_AD(0x3)
    OP_AD(0x4)
    OP_68(15500, 1000, 9700, 5000)
    MoveCamera(30, 21, 0, 5000)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x104, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 50)
    BeginChrThread(0x103, 3, 0, 51)
    BeginChrThread(0x10A, 3, 0, 53)
    BeginChrThread(0x16, 3, 0, 54)
    BeginChrThread(0x14, 3, 0, 52)
    Sleep(1000)

    def lambda_3AB3():

        label("loc_3AB3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3AB3")

    QueueWorkItem2(0x17, 2, lambda_3AB3)

    def lambda_3AC5():

        label("loc_3AC5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3AC5")

    QueueWorkItem2(0x18, 2, lambda_3AC5)
    WaitChrThread(0x16, 3)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    OP_6F(0x41)
    EndChrThread(0x29, 0x1)
    Fade(500)
    OP_68(3100, 1000, 2200, 0)
    MoveCamera(10, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    Sleep(500)

    #C0062
    ChrTalk(
        0x17,
        (
            "#5P#1709Fワオ！\x01",
            "凄いライブ感じゃないの！？\x02\x03",

            "#1702Fよーし、こうなったらあたしも……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B83():
        OP_95(0xFE, 3200, 0, 2600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B83)
    WaitChrThread(0x18, 1)
    TurnDirection(0x18, 0x17, 500)

    #C0063
    ChrTalk(
        0x18,
        (
            "#1801F#5Pイリアさんっ！\x01",
            "いいから避難しましょう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BDE():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x3A98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BDE)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3C0A():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x3A98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C0A)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 45)
    SetCameraDistance(17000, 5000)

    #C0064
    ChrTalk(
        0x17,
        (
            "#6P#1705F#28Aちょ、リーシャ！\x01",
            "引っ張らないでってば──\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetScenarioFlags(0x5C, 1)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_2C1E end

    def Function_45_3C9A(): pass

    label("Function_45_3C9A")

    SetChrPos(0x19, -7000, 0, 1500, 90)
    SetChrPos(0x1A, -7000, 0, 1500, 90)
    SetChrPos(0x1B, -7000, 0, 1500, 90)
    SetChrPos(0x1C, -7000, 0, 1500, 90)
    Sleep(500)
    BeginChrThread(0x19, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1A, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1B, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1C, 3, 0, 56)
    Return()

    # Function_45_3C9A end

    def Function_46_3D03(): pass

    label("Function_46_3D03")

    ClearScenarioFlags(0x0, 4)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x0)

    label("loc_3D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFE")
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(831, 0, 100, 0)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x3)
    Sleep(500)
    PlayEffect(0x2, 0x2, 0x103, 0x140, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x19, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x4)
    Sleep(2000)
    StopEffect(0x2, 0x2)
    Jump("loc_3D0E")

    label("loc_3DFE")

    SetScenarioFlags(0x0, 4)
    Return()

    # Function_46_3D03 end

    def Function_47_3E02(): pass

    label("Function_47_3E02")

    ClearScenarioFlags(0x0, 3)
    SetChrChipByIndex(0x102, 0x31)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)

    label("loc_3E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8D")
    Sleep(1500)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Jump("loc_3E1B")

    label("loc_3E8D")

    SetScenarioFlags(0x0, 3)
    Return()

    # Function_47_3E02 end

    def Function_48_3E91(): pass

    label("Function_48_3E91")

    OP_92(0x101, 0x34BC, 0x25E4, 0x1F4)

    def lambda_3EA3():
        OP_95(0xFE, 13500, 0, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EA3)
    WaitChrThread(0x101, 1)

    def lambda_3EC1():
        OP_97(0xFE, 0x3A98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EC1)
    WaitChrThread(0x101, 1)
    Return()

    # Function_48_3E91 end

    def Function_49_3EDB(): pass

    label("Function_49_3EDB")

    Sleep(600)
    OP_92(0x104, 0x396C, 0x21FC, 0x1F4)

    def lambda_3EF0():
        OP_95(0xFE, 14700, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EF0)
    WaitChrThread(0x104, 1)

    def lambda_3F0E():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F0E)
    WaitChrThread(0x104, 1)
    Return()

    # Function_49_3EDB end

    def Function_50_3F28(): pass

    label("Function_50_3F28")

    SetChrSubChip(0x102, 0x2)
    Sleep(400)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    OP_92(0x102, 0x34BC, 0x25E4, 0x1F4)

    def lambda_3F57():
        OP_95(0xFE, 13500, 0, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F57)
    WaitChrThread(0x102, 1)

    def lambda_3F75():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F75)
    WaitChrThread(0x102, 1)
    Return()

    # Function_50_3F28 end

    def Function_51_3F8F(): pass

    label("Function_51_3F8F")

    SetChrSubChip(0x103, 0x3)
    Sleep(1200)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    OP_92(0x103, 0x396C, 0x21FC, 0x1F4)

    def lambda_3FB0():
        OP_95(0xFE, 14700, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FB0)
    WaitChrThread(0x103, 1)

    def lambda_3FCE():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FCE)
    WaitChrThread(0x103, 1)
    Return()

    # Function_51_3F8F end

    def Function_52_3FE8(): pass

    label("Function_52_3FE8")


    def lambda_3FED():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3FED)
    WaitChrThread(0x14, 2)
    OP_92(0x14, 0x332C, 0x21FC, 0x1F4)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 3)
    BeginChrThread(0x29, 1, 0, 57)

    def lambda_4041():
        OP_96(0xFE, 0x3E8, 0x6EA, 0x25E4, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4041)
    WaitChrThread(0x14, 1)

    def lambda_405F():
        OP_96(0xFE, 0x157C, 0x6EA, 0x319C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_405F)
    WaitChrThread(0x14, 1)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x29, 0x1)

    def lambda_4085():
        OP_92(0xFE, 0x34BC, 0x319C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4085)
    SetChrSubChip(0x14, 0x2)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x14, 0x3)
    Sleep(50)
    SetChrSubChip(0x14, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_40C6():
        OP_9D(0xFE, 0x34BC, 0x0, 0x319C, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_40C6)
    Sleep(600)
    SetChrSubChip(0x14, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x2)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0x14, 0x3)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    BeginChrThread(0x14, 0, 0, 3)
    BeginChrThread(0x29, 1, 0, 57)

    def lambda_411E():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_411E)
    WaitChrThread(0x14, 1)
    Return()

    # Function_52_3FE8 end

    def Function_53_4138(): pass

    label("Function_53_4138")

    Sleep(2500)
    OP_92(0x10A, 0x4268, 0x21FC, 0x1F4)

    def lambda_414D():
        OP_95(0xFE, 17000, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_414D)
    WaitChrThread(0x10A, 1)

    def lambda_416B():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_416B)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_53_4138 end

    def Function_54_4185(): pass

    label("Function_54_4185")

    Sleep(2800)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    OP_92(0x16, 0x4268, 0x21FC, 0x1F4)

    def lambda_41A2():
        OP_95(0xFE, 17000, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_41A2)
    WaitChrThread(0x16, 1)

    def lambda_41C0():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_41C0)
    WaitChrThread(0x16, 1)
    Return()

    # Function_54_4185 end

    def Function_55_41DA(): pass

    label("Function_55_41DA")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_41E7():
        OP_95(0xFE, -22800, 0, 7200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41E7)

    def lambda_4201():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4201)
    WaitChrThread(0xFE, 1)

    def lambda_4216():
        OP_95(0xFE, -13800, 0, 3200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4216)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_41DA end

    def Function_56_4230(): pass

    label("Function_56_4230")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_423D():
        OP_95(0xFE, 3000, 0, 1500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_423D)
    WaitChrThread(0xFE, 1)

    def lambda_425B():
        OP_95(0xFE, 13000, 0, 9500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_425B)
    WaitChrThread(0xFE, 1)

    def lambda_4279():
        OP_95(0xFE, 23000, 0, 9500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4279)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_4230 end

    def Function_57_4293(): pass

    label("Function_57_4293")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42AC")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_57_4293")

    label("loc_42AC")

    Return()

    # Function_57_4293 end

    def Function_58_42AD(): pass

    label("Function_58_42AD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4365")

    #C0065
    ChrTalk(
        0x104,
        (
            "#0300Fアルカンシェルも\x01",
            "そろそろ公演時間みてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#0003Fまだ入れそうだけど……\x02\x03",

            "#0001F今はガンツさんの様子を見に行こう。\x01",
            "すぐそこのホテルだったはずだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_43AF")

    label("loc_4365")

    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今夜の公演はまだ始まっていないようだ。\x01",
            "後で立ち寄ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43AF")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Return()

    # Function_58_42AD end

    def Function_59_43C6(): pass

    label("Function_59_43C6")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_59_43C6 end

    def Function_60_43E2(): pass

    label("Function_60_43E2")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_60_43E2 end

    def Function_61_43FE(): pass

    label("Function_61_43FE")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_61_43FE end

    def Function_62_441A(): pass

    label("Function_62_441A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448E")

    #C0068
    ChrTalk(
        0x101,
        (
            "#0001Fガンツさんは\x01",
            "この辺りの高級ホテルに\x01",
            "泊まっているらしい……\x02\x03",

            "今はそっちの方を訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45AB")

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000Fもう日が暮れたな……\x02\x03",

            "キーアも待ってる事だし\x01",
            "寄り道せずに帰ろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_452D")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0100Fそうね、一通り\x01",
            "仕事も終わった事だし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45AB")

    label("loc_452D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4568")

    #C0071
    ChrTalk(
        0x103,
        "#0200Fそうですね、そうしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45AB")

    label("loc_4568")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45AB")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0300Fだな、とっとと帰って\x01",
            "キー坊の顔を拝むか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45AB")

    Return()

    # Function_62_441A end

    SaveToFile()

Try(main)
