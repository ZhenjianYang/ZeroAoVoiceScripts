from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ソフィーユ",             # 1
        "客引きピム",             # 2
        "ポリセ",                 # 3
        "タップ",                 # 4
        "ラマンダ",               # 5
        "テージョ",               # 6
        "バニーガール",           # 7
        "ライム",                 # 8
        "フェリック",             # 9
        "青年",                   # 10
        "娘",                     # 11
        "グレイス",               # 12
        "レインズ",               # 13
        "パンセ",                 # 14
        "フェイ",                 # 15
        "サミィ",                 # 16
        "シュリ",                 # 17
        "見物客",                 # 18
        "見物客",                 # 19
        "車",                     # 20
        "セシル",                 # 21
        "ノエル",                 # 22
        "フラン",                 # 23
        "フィリア",               # 24
        "ラン",                   # 25
        "エイダ",                 # 26
        "客",                     # 27
        "客",                     # 28
        "客",                     # 29
        "客",                     # 30
        "客",                     # 31
        "客",                     # 32
        "客",                     # 33
        "客",                     # 34
        "客",                     # 35
        "客",                     # 36
        "中央広場",               # 37
        "西通り",                 # 38
        "行政区",                 # 39
        "住宅街",                 # 40
        "歓楽街",                 # 41
        "東通り",                 # 42
        "旧市街",                 # 43
        "港湾区",                 # 44
        "ＩＢＣ",                 # 45
        "駅前通り",               # 46
        "裏通り",                 # 47
        "ウルスラ間道",           # 48
        "東クロスベル街道",       # 49
        "西クロスベル街道",       # 50
        "マインツ山道",           # 51
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
        "Function_0_828",          # 00, 0
        "Function_1_8E0",          # 01, 1
        "Function_2_90B",          # 02, 2
        "Function_3_A98",          # 03, 3
        "Function_4_B9F",          # 04, 4
        "Function_5_FE7",          # 05, 5
        "Function_6_1173",         # 06, 6
        "Function_7_1EE1",         # 07, 7
        "Function_8_245A",         # 08, 8
        "Function_9_272E",         # 09, 9
        "Function_10_285D",        # 0A, 10
        "Function_11_2909",        # 0B, 11
        "Function_12_2C0D",        # 0C, 12
        "Function_13_2F18",        # 0D, 13
        "Function_14_31C2",        # 0E, 14
        "Function_15_3412",        # 0F, 15
        "Function_16_3EC5",        # 10, 16
        "Function_17_41D6",        # 11, 17
        "Function_18_4442",        # 12, 18
        "Function_19_461D",        # 13, 19
        "Function_20_4755",        # 14, 20
        "Function_21_4815",        # 15, 21
        "Function_22_490C",        # 16, 22
        "Function_23_4A18",        # 17, 23
        "Function_24_4C5C",        # 18, 24
        "Function_25_4E5B",        # 19, 25
        "Function_26_528E",        # 1A, 26
        "Function_27_5347",        # 1B, 27
        "Function_28_54D0",        # 1C, 28
        "Function_29_56A8",        # 1D, 29
        "Function_30_579D",        # 1E, 30
        "Function_31_586E",        # 1F, 31
        "Function_32_5A0D",        # 20, 32
        "Function_33_5AA9",        # 21, 33
        "Function_34_5B2A",        # 22, 34
        "Function_35_5D1D",        # 23, 35
        "Function_36_8729",        # 24, 36
        "Function_37_8C4A",        # 25, 37
        "Function_38_9214",        # 26, 38
        "Function_39_923A",        # 27, 39
        "Function_40_93B6",        # 28, 40
        "Function_41_93D2",        # 29, 41
        "Function_42_93EE",        # 2A, 42
        "Function_43_940A",        # 2B, 43
        "Function_44_9594",        # 2C, 44
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FE")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ED8")

    label("loc_11FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1212")
    Jump("loc_1ED8")

    label("loc_1212")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12A8")

    #C0001
    ChrTalk(
        0x8,
        (
            "今買わないと\x01",
            "きっと売り切れちゃいますよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "はい、後悔しないように\x01",
            "今買っちゃってください！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_12A8")


    #C0003
    ChrTalk(
        0x8,
        (
            "むふふ、今日も売り上げは\x01",
            "絶好調ですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……そこのお兄さん、\x01",
            "アイスを買うなら今ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "５段重ねでも７段重ねでも、\x01",
            "好きなだけ言っちゃってください！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1350")

    Jump("loc_1ED8")

    label("loc_1355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13AC")

    #C0006
    ChrTalk(
        0x8,
        (
            "あー、おしいなー。\x01",
            "今年のパレードは\x01",
            "終わっちゃいましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1439")

    label("loc_13AC")


    #C0007
    ChrTalk(
        0x8,
        "思うんですけど……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "パレードの後ろにくっついて\x01",
            "走ったら売れそうですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "わたし、オート三輪の\x01",
            "ユルユル運転は得意ですよぉ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1439")

    Jump("loc_1ED8")

    label("loc_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_16A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_END)), "loc_14ED")

    #C0010
    ChrTalk(
        0x8,
        (
            "なにせ、パレードと一緒に\x01",
            "どばーと人が来て\x01",
            "どばーと行っちゃいましたからねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "わたしももう、\x01",
            "何がなにやら～でしたから。\x01",
            "よく覚えてませんね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169E")

    label("loc_14ED")


    #C0012
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x8,
        (
            "……何ですか～？\x01",
            "この写真をくれるんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0001Fいえ、ですから\x01",
            "この子に見覚えはないかと\x01",
            "思いまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "さあ、知りませんねー。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "なにせ、パレードと一緒に\x01",
            "どばーと人が来て\x01",
            "どばーと行っちゃいましたからねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_169E")

    Jump("loc_1ED8")

    label("loc_16A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_178C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16FA")

    #C0019
    ChrTalk(
        0x8,
        (
            "あー、おしいなー。\x01",
            "今年のパレードは\x01",
            "終わっちゃいましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_16FA")


    #C0020
    ChrTalk(
        0x8,
        "思うんですけど……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "パレードの後ろにくっついて\x01",
            "走ったら売れそうですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "わたし、オート三輪の\x01",
            "ユルユル運転は得意ですよぉ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1787")

    Jump("loc_1ED8")

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CDB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1878")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180A")

    #C0023
    ChrTalk(
        0xFE,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "ピザを買うくらいなら\x01",
            "アイスを買ってください～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1873")

    label("loc_180A")


    #C0025
    ChrTalk(
        0xFE,
        (
            "窃盗犯が捕まろうが干されようが\x01",
            "わたしのお商売には関係ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        "さあさあ、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    label("loc_1873")

    Jump("loc_1CD6")

    label("loc_1878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B37")

    #C0027
    ChrTalk(
        0x101,
        (
            "#0001Fすみません、少しお話を\x01",
            "伺ってもいいですか？\x02\x03",

            "窃盗事件について\x01",
            "捜査をしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ああ、そこのピザ屋さんが\x01",
            "やられたそうですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "くす……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "わたしはそんなヘマは\x01",
            "しませんよー。\x02",
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
            "#0106Fえっと……犯人を見かけたりは\x01",
            "なさっていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "さあ、特に見てませんが……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "わたしのカンでは、\x01",
            "もうすぐ第三の犯行が\x01",
            "行われそうな気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "犯人は今ごろ次の獲物を探して\x01",
            "うろうろしているんでしょうねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#0306Fそ、そうかい……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#0200F……ちなみにすでに\x01",
            "４件の被害が出ているので、\x01",
            "次は“第五の犯行”ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xA)
    Jump("loc_1C1F")

    label("loc_1B37")


    #C0037
    ChrTalk(
        0xFE,
        (
            "わたしのカンでは、\x01",
            "もうすぐ次の犯行が\x01",
            "行われそうな気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "何しろ連続窃盗犯ですからねー。\x01",
            "今日中にもう１軒くらいは\x01",
            "狙われるんじゃないでしょうかー。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "くす……ご心配なく。\x01",
            "わたしは盗られるような\x01",
            "ヘマはしませんよー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1F")

    Jump("loc_1CD6")

    label("loc_1C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C7C")

    #C0040
    ChrTalk(
        0x8,
        "あのピザ屋はわたしのライバルです。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "絶対に買っちゃ駄目ですよぉ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CD6")

    label("loc_1C7C")


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
            "ピザを買うくらいなら\x01",
            "アイスを買ってください～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CD6")

    Jump("loc_1ED8")

    label("loc_1CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D44")

    #C0044
    ChrTalk(
        0x8,
        (
            "こちらも歓楽街売り上げ一位の\x01",
            "プライドがありますし。\x01",
            "負けてられませんねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD7")

    label("loc_1D44")


    #C0045
    ChrTalk(
        0x8,
        (
            "あのピザ屋さん、\x01",
            "中々やりますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "『パレット・ピザ』といえば\x01",
            "出前サービスで有名な所ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "……フフ、負けてられませんねぇ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1DD7")

    Jump("loc_1ED8")

    label("loc_1DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E56")

    #C0048
    ChrTalk(
        0x8,
        (
            "なんでも港湾区の方には\x01",
            "絶品のアイスを売る店が\x01",
            "出てるそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "わたしも負けてられませんねー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ED8")

    label("loc_1E56")


    #C0050
    ChrTalk(
        0x8,
        "アイス～、アイスはいかが～？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "……そこのお兄さん、\x01",
            "記念祭といえばアイスですよぉ！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "買わなくてどうするんですかぁ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1ED8")

    Jump("loc_1180")

    label("loc_1EDD")

    TalkEnd(0xFE)
    Return()

    # Function_6_1173 end

    def Function_7_1EE1(): pass

    label("Function_7_1EE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F75")

    #C0053
    ChrTalk(
        0x9,
        (
            "祭りが今日で終わってしまう\x01",
            "なんてもったいないねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "このまま１年くらい\x01",
            "馬鹿騒ぎが続いてくれると\x01",
            "こっちも嬉しいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_1F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_1FE0")

    #C0055
    ChrTalk(
        0x9,
        "へっへ、今日は沢山引っ掛けたよ。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "みんな浮かれてるからね、\x01",
            "引っ掛けるのも簡単だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_21F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_2071")

    #C0057
    ChrTalk(
        0x9,
        (
            "悪いけど、俺は遊んでくれる\x01",
            "お客さん以外興味ないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "どこかで見たような気もするけど\x01",
            "はっきりは覚えてないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F0")

    label("loc_2071")


    #C0059
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0061
    ChrTalk(
        0x9,
        "子供だって……？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "さあ、知らないねぇ。\x01",
            "俺はお客さん以外興味ないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "それにパレードと一緒に\x01",
            "観光客がくっ付いてきて大混雑だったんだ。\x01",
            "はっきりした事は言えないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_21F0")

    Jump("loc_2456")

    label("loc_21F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2260")

    #C0065
    ChrTalk(
        0x9,
        "へっへ、今日は沢山引っ掛けたよ。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "みんな浮かれてるからね、\x01",
            "引っ掛けるのも簡単だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_2260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2323")

    #C0067
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの公演が終わるとね、\x01",
            "客がどーっと出てくるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "今日はパレードもあるし\x01",
            "すごい混雑しそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "へっへ、遊びそうな奴も居るだろ。\x01",
            "気を付けていないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_2323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2395")

    #C0070
    ChrTalk(
        0xFE,
        (
            "ああ、嬉しいねえ。\x01",
            "今日もお客さんが一杯だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "どれどれ、次は\x01",
            "どの人にしましょうか～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_2395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23D4")

    #C0072
    ChrTalk(
        0x9,
        (
            "さーて、いいお客さんを\x01",
            "物色しますよ～っと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_23D4")


    #C0073
    ChrTalk(
        0x9,
        (
            "ああ、記念祭か……\x01",
            "嬉しいねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "客引きしてるこっちも\x01",
            "ウキウキしてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "兄ちゃん兄ちゃん、\x01",
            "遊んでいかんか～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2456")

    TalkEnd(0xFE)
    Return()

    # Function_7_1EE1 end

    def Function_8_245A(): pass

    label("Function_8_245A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_24A3")

    #C0076
    ChrTalk(
        0xA,
        (
            "ストーカーなんて卑劣だわ。\x01",
            "許すまじ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A6")

    label("loc_24A3")

    Call(0, 9)

    label("loc_24A6")

    Jump("loc_272A")

    label("loc_24AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_24FD")

    #C0077
    ChrTalk(
        0xA,
        (
            "今日という今日は\x01",
            "チケット持ってる連中が妬ましいわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_259B")

    label("loc_24FD")


    #C0078
    ChrTalk(
        0xA,
        (
            "出てきた観客に聞いたの。\x01",
            "今日の公演は凄く良かったんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "イリア様のオーラも\x01",
            "いつもより素晴らしかったって……\x01",
            "くうぅ……ブルジョアジーめ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_259B")

    Jump("loc_272A")

    label("loc_25A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2603")

    #C0080
    ChrTalk(
        0xA,
        "イリア様、イリア様～っ……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "うふふふふっ……\x01",
            "今ごろお着替えの時間かしら～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272A")

    label("loc_2603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2614")
    Call(0, 10)
    Jump("loc_272A")

    label("loc_2614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_266A")

    #C0082
    ChrTalk(
        0xA,
        (
            "このイリア様のサインは\x01",
            "我が家の家宝ね。\x01",
            "子々孫々にまで伝え継ぐわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272A")

    label("loc_266A")


    #C0083
    ChrTalk(
        0xA,
        (
            "イリア様のサインを\x01",
            "ゲットしたわ～～～っっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "キャー、生サインよ！！\x01",
            "それも私の目の前で……！！\x02",
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
            "ダメ……のぼせちゃって\x01",
            "うまくご挨拶できなかったわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_272A")

    TalkEnd(0xFE)
    Return()

    # Function_8_245A end

    def Function_9_272E(): pass

    label("Function_9_272E")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0086
    ChrTalk(
        0xA,
        (
            "タップ、聞いた！？\x01",
            "イリア様にストーキングを\x01",
            "する輩がいたそうよっ！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27B3")

    #C0087
    ChrTalk(
        0xA,
        "警察が逮捕したらしいけど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D3")

    label("loc_27B3")


    #C0088
    ChrTalk(
        0xA,
        "結局捕まったそうだけど……\x02",
    )

    CloseMessageWindow()

    label("loc_27D3")


    #C0089
    ChrTalk(
        0xA,
        (
            "許せない、許せないわ。\x01",
            "私のイリア様にぃぃ……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        (
            "ああ、許しがたいな……\x01",
            "俺たちがブチのめしてやるぜ……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_272E end

    def Function_10_285D(): pass

    label("Function_10_285D")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0091
    ChrTalk(
        0xA,
        (
            "明日のチケットを\x01",
            "持ってるですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "シャ～っ、あっちへお行きなさい！\x01",
            "観光客なんて嫌いよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xB,
        "そうだぜ、さっさと立ち去れ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    Return()

    # Function_10_285D end

    def Function_11_2909(): pass

    label("Function_11_2909")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2958")

    #C0094
    ChrTalk(
        0xB,
        (
            "何モンだ……？\x01",
            "俺たちがブチのめしてやるぜ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295B")

    label("loc_2958")

    Call(0, 9)

    label("loc_295B")

    Jump("loc_2C09")

    label("loc_2960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_29E6")

    #C0095
    ChrTalk(
        0xFE,
        (
            "くそっ、俺だって\x01",
            "イリア様と出会ったあの舞台以来\x01",
            "一度も見れてないってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "連中が妬ましくて仕方ねえぜ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C09")

    label("loc_29E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A74")

    #C0097
    ChrTalk(
        0xB,
        (
            "パレード目当ての客は\x01",
            "あっちへ行った行った……！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "お前らのせいで\x01",
            "イリア様を見逃しちまったら\x01",
            "どうするんだよっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B0F")

    label("loc_2A74")


    #C0099
    ChrTalk(
        0xB,
        "パレード？　……関係ないな。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "アルカンシェル、\x01",
            "そしてイリア様の追っかけなら\x01",
            "ずっと張り付いているべきだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        "たとえそれが祭りの最中でもな！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2B0F")

    Jump("loc_2C09")

    label("loc_2B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B25")
    Call(0, 10)
    Jump("loc_2C09")

    label("loc_2B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B6A")

    #C0102
    ChrTalk(
        0xB,
        (
            "生イリア様……\x01",
            "あんなに近くで見たのは初めてだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C09")

    label("loc_2B6A")


    #C0103
    ChrTalk(
        0xB,
        (
            "昨日は新作公演の初日だったんで、\x01",
            "臨時のサイン会があったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "もちろん俺たちも\x01",
            "急いでならんでゲットしたぜ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        "……公演は見てないんだけどな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2C09")

    TalkEnd(0xFE)
    Return()

    # Function_11_2909 end

    def Function_12_2C0D(): pass

    label("Function_12_2C0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C86")

    #C0106
    ChrTalk(
        0xC,
        (
            "今日は記念祭専用の\x01",
            "遊覧飛行船に乗ってみようかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "最終日だし、夕方なら\x01",
            "席が空いてそうよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F14")

    label("loc_2C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2CD9")

    #C0108
    ChrTalk(
        0xC,
        (
            "パレードも見たし、\x01",
            "屋台も回ったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        "今年の記念祭も満足ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F14")

    label("loc_2CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D4F")

    #C0110
    ChrTalk(
        0xC,
        (
            "パレードは真っ先に\x01",
            "この歓楽街を通るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xC,
        (
            "ふふ、見逃せないわね。\x01",
            "いい場所を確保しなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F14")

    label("loc_2D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2DC8")

    #C0112
    ChrTalk(
        0xC,
        (
            "ちょっと人が\x01",
            "多すぎなんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "こんなときに事件でも起きたら\x01",
            "どうするのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3E")

    label("loc_2DC8")


    #C0114
    ChrTalk(
        0xC,
        (
            "記念祭の３日目なのに……\x01",
            "まだ続々観光客が\x01",
            "到着しているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "表通りは歩くだけで\x01",
            "息が上がっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2E3E")

    Jump("loc_2F14")

    label("loc_2E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2E84")

    #C0116
    ChrTalk(
        0xC,
        (
            "こう人が多くちゃ\x01",
            "歩きにくくて仕方ないわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F14")

    label("loc_2E84")


    #C0117
    ChrTalk(
        0xC,
        (
            "あら、ちょっと\x01",
            "退いてくださる？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "……こう人が多くちゃ\x01",
            "歩きにくいわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "これからパーティに行かなくちゃ\x01",
            "いけないっていうのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2F14")

    TalkEnd(0xFE)
    Return()

    # Function_12_2C0D end

    def Function_13_2F18(): pass

    label("Function_13_2F18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F86")

    #C0120
    ChrTalk(
        0xD,
        "クロスベル生誕ばんざーい！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "さて、形式どおり唱えたことだし\x01",
            "今日も一日遊ぶとすっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FF0")

    #C0122
    ChrTalk(
        0xD,
        (
            "純金製の装飾とか\x01",
            "信じらんねえよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xD,
        (
            "今年のパレードは\x01",
            "噂どおりドハデだったなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_2FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_30C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_305E")

    #C0124
    ChrTalk(
        0xD,
        (
            "遊撃士の人、市内を\x01",
            "見回ってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        "へへっ、おかげで安心して遊べるぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BB")

    label("loc_305E")


    #C0126
    ChrTalk(
        0xD,
        (
            "記念祭の間も\x01",
            "遊撃士の人は働いてんだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "定期的に\x01",
            "見回ってくれてるみたいだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_30BB")

    Jump("loc_31BE")

    label("loc_30C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3140")

    #C0128
    ChrTalk(
        0xD,
        (
            "どこのカジノも気前よく\x01",
            "儲けさせてくれてるらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xD,
        (
            "あんたらも遊ぶなら今だ！\x01",
            "この記念祭の間しかねえぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BE")

    label("loc_3140")


    #C0130
    ChrTalk(
        0xD,
        (
            "やっぱあちこちの店が\x01",
            "出店だしてるみたいだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xD,
        (
            "へへっ、店にとっても稼ぎ時なんだろ。\x01",
            "客としても遊んでやらねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BE")

    TalkEnd(0xFE)
    Return()

    # Function_13_2F18 end

    def Function_14_31C2(): pass

    label("Function_14_31C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_321C")

    #C0132
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xE,
        (
            "記念祭だもの、みんな\x01",
            "遊んでいってよ～ン㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_340E")

    label("loc_321C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_33C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_END)), "loc_328A")

    #C0134
    ChrTalk(
        0xE,
        (
            "うふ、アタシお客さんの\x01",
            "お財布具合しか見てないの～。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xE,
        "子供の事は判んないかも㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C0")

    label("loc_328A")


    #C0136
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0138
    ChrTalk(
        0xE,
        (
            "え～、知らな～い。\x01",
            "見てないけどぉ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xE,
        (
            "人通りも多かったから\x01",
            "気付かないうちに通ってたかも㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000Fそ、そうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_33C0")

    Jump("loc_340E")

    label("loc_33C5")


    #C0141
    ChrTalk(
        0xE,
        "ハロー、いかが～ん☆\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xE,
        (
            "記念祭だもの、みんな\x01",
            "遊んでいってよ～ン㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340E")

    TalkEnd(0xFE)
    Return()

    # Function_14_31C2 end

    def Function_15_3412(): pass

    label("Function_15_3412")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_343C")
    Call(0, 36)
    Return()

    label("loc_343C")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3449")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC1")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_34A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34C7")
    OP_AF(0x7F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EBC")

    label("loc_34C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34DB")
    Jump("loc_3EBC")

    label("loc_34DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EBC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363E")

    #C0143
    ChrTalk(
        0xFE,
        (
            "よう、話は聞いたぞ。\x01",
            "窃盗犯をとっ捕まえたんだと？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "そいつは礼をしなきゃいけねえな。\x01",
            "……ほら、持って行けよ！\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1B1, 1)

    #C0146
    ChrTalk(
        0x101,
        (
            "#0000Fありがとうございます。\x01",
            "頂いておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "おう、遠慮なく食ってくれ。\x01",
            "警察の兄ちゃんたち！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 0)
    Jump("loc_3EBC")

    label("loc_363E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_36F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3690")

    #C0148
    ChrTalk(
        0xF,
        (
            "出店で買うなら今日限り！\x01",
            "さあさあ買った買ったぁ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36ED")

    label("loc_3690")


    #C0149
    ChrTalk(
        0xF,
        (
            "ヘイそこのお兄さん、\x01",
            "ピザはいかがだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xF,
        (
            "パレット・ピザの出店は\x01",
            "今日限りだぜっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_36ED")

    Jump("loc_3EBC")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_37BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3738")

    #C0151
    ChrTalk(
        0xF,
        (
            "くそぅ、折角の\x01",
            "賑わいだったってのに……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B8")

    label("loc_3738")


    #C0152
    ChrTalk(
        0xF,
        (
            "くそっ……！\x01",
            "パレードが通るってんで\x01",
            "出店を一時撤去させられてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xF,
        (
            "いい時間帯に店を閉める\x01",
            "羽目になっちまったぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_37B8")

    Jump("loc_3EBC")

    label("loc_37BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_385F")

    #C0154
    ChrTalk(
        0xF,
        (
            "あー、パレードが通るとき\x01",
            "屋台をどけろって言われてさぁ。\x01",
            "ゴタゴタしてたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "この１時間くらいは\x01",
            "通ってないと思うんだけどさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A38")

    label("loc_385F")


    #C0156
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0158
    ChrTalk(
        0xFE,
        (
            "えっ、迷子……？\x01",
            "ってこの子はどこかで……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0005F本当ですか……！？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "あー、パレードが通るとき\x01",
            "屋台をどけろって言われてさぁ。\x01",
            "ゴタゴタしてたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "……悪い、やっぱ自信ないや。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "でもこの１時間くらいは\x01",
            "通ってないと思うぜ。\x01",
            "混雑も収まってたしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 32)

    label("loc_3A38")

    Jump("loc_3EBC")

    label("loc_3A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A83")

    #C0164
    ChrTalk(
        0xF,
        (
            "くそぅ、折角の\x01",
            "賑わいだったってのに……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B03")

    label("loc_3A83")


    #C0165
    ChrTalk(
        0xF,
        (
            "くそっ……！\x01",
            "パレードが通るってんで\x01",
            "出店を一時撤去させられてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xF,
        (
            "いい時間帯に店を閉める\x01",
            "羽目になっちまったぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3B03")

    Jump("loc_3EBC")

    label("loc_3B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D3B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B87")

    #C0167
    ChrTalk(
        0xFE,
        "これで売上金も戻ってくるだろ。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "もうじきパレードも始まるし\x01",
            "いい事尽くめじゃねえか、ははは！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D36")

    label("loc_3B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C71")

    #C0169
    ChrTalk(
        0xFE,
        (
            "お喋りな兄ちゃんが\x01",
            "トロピカルセットを頼んでな。\x01",
            "丁度渡してる所だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "俺の接客経験から言やあ\x01",
            "ありゃあ外国からの観光客だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……はあ、悪いがあの兄ちゃんの事\x01",
            "恨みたくなって来たぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D36")

    label("loc_3C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3CB6")

    #C0172
    ChrTalk(
        0xF,
        (
            "ありゃあ危ないオジサンだろ。\x01",
            "関わりたくないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D36")

    label("loc_3CB6")


    #C0173
    ChrTalk(
        0xF,
        (
            "あそこのウロウロしてる\x01",
            "オジサン、ちょっと怖ぇよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xF,
        (
            "さっきから観光客に\x01",
            "声を掛けまくってんだ……\x01",
            "大丈夫なのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3D36")

    Jump("loc_3EBC")

    label("loc_3D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3D70")

    #C0175
    ChrTalk(
        0xF,
        "お客さんも１つどうだい！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DC8")

    label("loc_3D70")


    #C0176
    ChrTalk(
        0xF,
        "さあさあ、見てけ買っていけ！\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xF,
        (
            "みんなお馴染み\x01",
            "パレット・ピザの出店だよ～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3DC8")

    Jump("loc_3EBC")

    label("loc_3DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3E37")

    #C0178
    ChrTalk(
        0xF,
        (
            "出前でお馴染みの\x01",
            "パレット・ピザだぜっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xF,
        (
            "記念祭の間は\x01",
            "出店を出しちゃってるよ～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EBC")

    label("loc_3E37")


    #C0180
    ChrTalk(
        0xF,
        (
            "らっしゃい！\x01",
            "パレット・ピザの出店でぇっす！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xF,
        "毎度お馴染みパレット・ピザ！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xF,
        (
            "記念祭の間は\x01",
            "出店を出しちゃってるよ～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3EBC")

    Jump("loc_3449")

    label("loc_3EC1")

    TalkEnd(0xFE)
    Return()

    # Function_15_3412 end

    def Function_16_3EC5(): pass

    label("Function_16_3EC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3F3E")

    #C0183
    ChrTalk(
        0x19,
        "おお……とても美味しい。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x19,
        (
            "ここのジェラートは格別ですね。\x01",
            "最後を締めくくるに\x01",
            "相応しい味ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D2")

    label("loc_3F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3FB8")

    #C0185
    ChrTalk(
        0xFE,
        (
            "クロスベルのパレードは\x01",
            "素晴らしい……！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "まさに花の都ですね。\x01",
            "これほど賑やかな催しは初めてですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D2")

    label("loc_3FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4068")
    OP_4B(0x1A, 0xFF)

    #C0187
    ChrTalk(
        0x19,
        (
            "本日は大規模な\x01",
            "パレードがあるそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x19,
        "おまえ、体の方は平気ですか？\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x1A,
        "ええ、もちろんですわ。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x1A,
        (
            "ふふっ、パレードなんて\x01",
            "楽しみですわね！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    Jump("loc_41D2")

    label("loc_4068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4109")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)

    #C0191
    ChrTalk(
        0x19,
        (
            "すみません……\x01",
            "アルカンシェルというのは\x01",
            "ここで良いのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x19,
        (
            "明日昼の公演は\x01",
            "何時からでしたでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    Jump("loc_41D2")

    label("loc_4109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4140")

    #C0193
    ChrTalk(
        0x19,
        (
            "ではゆるりと\x01",
            "回ると致しましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D2")

    label("loc_4140")


    #C0194
    ChrTalk(
        0x19,
        (
            "おお、すばらしく\x01",
            "賑わっていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x19,
        (
            "さすがは大陸有数の\x01",
            "貿易都市クロスベル……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x19,
        (
            "はるばるレミフェリアから\x01",
            "来た甲斐がありましたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_41D2")

    TalkEnd(0xFE)
    Return()

    # Function_16_3EC5 end

    def Function_17_41D6(): pass

    label("Function_17_41D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_427C")

    #C0197
    ChrTalk(
        0x1A,
        (
            "今日がちょうど\x01",
            "彼との結婚記念日なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x1A,
        (
            "ふふっ、お陰で\x01",
            "例年になく楽しめました。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x1A,
        (
            "クロスベルの創立記念祭……\x01",
            "また来たいものですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_443E")

    label("loc_427C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_42FB")

    #C0200
    ChrTalk(
        0xFE,
        (
            "ふふっ、今年はいい思い出が\x01",
            "たくさん作れました。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "やはり旅行先に\x01",
            "クロスベルを選んだのは\x01",
            "正解でしたわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_443E")

    label("loc_42FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4374")

    #C0202
    ChrTalk(
        0x1A,
        "私、実は赤ちゃんがいますのよ。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x1A,
        (
            "ふふっ、お腹の中のこの子にも\x01",
            "パレードを見せてやりたいものですわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_443E")

    label("loc_4374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43BF")

    #C0204
    ChrTalk(
        0x1A,
        (
            "市内はごちゃごちゃしていて\x01",
            "どうもよく分かりませんわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_443E")

    label("loc_43BF")


    #C0205
    ChrTalk(
        0x1A,
        (
            "私たちの結婚記念日は\x01",
            "ちょうどクロスベルの\x01",
            "創立記念祭なのだそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x1A,
        (
            "ふふっ、結婚記念の\x01",
            "旅行先にはぴったりですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443E")

    TalkEnd(0xFE)
    Return()

    # Function_17_41D6 end

    def Function_18_4442(): pass

    label("Function_18_4442")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_449B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4493")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0207
    ChrTalk(
        0x10,
        (
            "あ、わかる。\x01",
            "あの子良かったよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4496")

    label("loc_4493")

    Call(0, 19)

    label("loc_4496")

    Jump("loc_4619")

    label("loc_449B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4511")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0208
    ChrTalk(
        0x10,
        (
            "でも、俺としちゃあ\x01",
            "パレードの方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x10,
        "おい２人とも、俺の話聞いてる？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4514")

    label("loc_4511")

    Call(0, 20)

    label("loc_4514")

    Jump("loc_4619")

    label("loc_4519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_45A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_459E")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0210
    ChrTalk(
        0x10,
        (
            "うっ……そこまで\x01",
            "言うなら付き合ってやるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x10,
        (
            "夜はスージィの\x01",
            "従姉妹の家に泊まりだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_45A1")

    label("loc_459E")

    Call(0, 21)

    label("loc_45A1")

    Jump("loc_4619")

    label("loc_45A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4616")

    #C0212
    ChrTalk(
        0x10,
        (
            "へへ、やっぱお祭りは\x01",
            "ダチと楽しまなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x10,
        (
            "祭りの間は門限もないし\x01",
            "思う存分遊べるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4619")

    label("loc_4616")

    Call(0, 22)

    label("loc_4619")

    TalkEnd(0xFE)
    Return()

    # Function_18_4442 end

    def Function_19_461D(): pass

    label("Function_19_461D")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0214
    ChrTalk(
        0x11,
        (
            "フェリックが\x01",
            "チケット持ってて助かったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x11,
        "一体どこで手に入れたんだ～？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x10,
        (
            "へっへー、親父が\x01",
            "仕事の関係で貰ったらしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x10,
        "ま、Ｂ席だったけどな。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x12,
        (
            "Ｂ席でもいいよ～。\x01",
            "イリア様チョーカッコ良かったし！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x12,
        (
            "あとやっぱテオドール様だよね～。\x01",
            "あたし大ファンなんだ～㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_19_461D end

    def Function_20_4755(): pass

    label("Function_20_4755")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0220
    ChrTalk(
        0x12,
        (
            "アルカンシェルのチケット～？\x01",
            "早く言いなよ、それ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x10,
        (
            "悪い、言い忘れてた。\x01",
            "しかも今日の昼部\x01",
            "限定でさぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x11,
        (
            "とっとと行こうぜ、\x01",
            "もう公演時間じゃねえか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_20_4755 end

    def Function_21_4815(): pass

    label("Function_21_4815")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0223
    ChrTalk(
        0x10,
        "え、ミシュラム？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x10,
        (
            "ちょっとベタじゃねーの？\x01",
            "お子様っぽいっつーかさぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x12,
        "いいじゃん、行けばぁ。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x12,
        (
            "イトコの家あるよ？\x01",
            "ついでに遊びにいっとく？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x11,
        (
            "おー、いいじゃん。\x01",
            "んじゃあホラーハウスも見に行こうぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_4815 end

    def Function_22_490C(): pass

    label("Function_22_490C")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0228
    ChrTalk(
        0x11,
        "よう、今日はどこで遊ぶ？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x12,
        (
            "例の大富豪、今夜\x01",
            "パーティやるって言ってたじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x12,
        "そっち行ってみようよー。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x10,
        (
            "ダメダメ、あそこは身内だけの\x01",
            "プライベートパーティなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x10,
        (
            "社交界に出入りするなら\x01",
            "その辺りは弁えとかないとな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_22_490C end

    def Function_23_4A18(): pass

    label("Function_23_4A18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4AB6")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0233
    ChrTalk(
        0x11,
        (
            "オレがぶったまげたのは\x01",
            "あの月の舞姫役の子だよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x11,
        (
            "新人とか絶対信じられねえって。\x01",
            "マジファンになったし。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4AB9")

    label("loc_4AB6")

    Call(0, 19)

    label("loc_4AB9")

    Jump("loc_4C58")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4B26")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0235
    ChrTalk(
        0x11,
        (
            "パレードなんて子供っちいだろ。\x01",
            "ここはオトナの劇団観賞だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4B29")

    label("loc_4B26")

    Call(0, 20)

    label("loc_4B29")

    Jump("loc_4C58")

    label("loc_4B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4BE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4BDE")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0236
    ChrTalk(
        0x11,
        (
            "ははーんフェリック、\x01",
            "お前家族でテーマパークに\x01",
            "行ったんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x11,
        (
            "ちっちっ、あそこは子供向けの場所。\x01",
            "リゾートなら他にもあるんだぜ？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4BE1")

    label("loc_4BDE")

    Call(0, 21)

    label("loc_4BE1")

    Jump("loc_4C58")

    label("loc_4BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4C55")
    OP_4B(0x10, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0238
    ChrTalk(
        0x11,
        "出た、フェリックの社交界理論！\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x11,
        (
            "んでどうする？\x01",
            "カジノにでも行っとくか？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x12, 0xFF)
    Jump("loc_4C58")

    label("loc_4C55")

    Call(0, 22)

    label("loc_4C58")

    TalkEnd(0xFE)
    Return()

    # Function_23_4A18 end

    def Function_24_4C5C(): pass

    label("Function_24_4C5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4CCF")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0240
    ChrTalk(
        0x12,
        "あー、浮気モノー！\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x12,
        (
            "この前はイリア様一択って\x01",
            "言ってたくせにー！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4CD2")

    label("loc_4CCF")

    Call(0, 19)

    label("loc_4CD2")

    Jump("loc_4E57")

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4D55")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0242
    ChrTalk(
        0x12,
        "ねえ、早く行かなくちゃ。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x12,
        (
            "予約席じゃないんでしょ？\x01",
            "……いい席探さなくっちゃ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4D58")

    label("loc_4D55")

    Call(0, 20)

    label("loc_4D58")

    Jump("loc_4E57")

    label("loc_4D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4DEE")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0244
    ChrTalk(
        0x12,
        (
            "あたしのイトコ、\x01",
            "ミシュラムに別荘あんのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x12,
        (
            "ちょーリッチだよ。\x01",
            "３人くらいヨユーで泊まれるから。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4DF1")

    label("loc_4DEE")

    Call(0, 21)

    label("loc_4DF1")

    Jump("loc_4E57")

    label("loc_4DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4E54")
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0246
    ChrTalk(
        0x12,
        "あたし高級バーとか行きた～い！\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x12,
        "オトナって感じじゃん？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Jump("loc_4E57")

    label("loc_4E54")

    Call(0, 22)

    label("loc_4E57")

    TalkEnd(0xFE)
    Return()

    # Function_24_4C5C end

    def Function_25_4E5B(): pass

    label("Function_25_4E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 1)), scpexpr(EXPR_END)), "loc_4FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF0")

    #C0248
    ChrTalk(
        0x13,
        (
            "#2100Fあ、そうそう。\x01",
            "写真の方は十分撮れたら\x01",
            "通信社の受付に渡しちゃって。\x02\x03",

            "よろしく頼んだからね～♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    Jump("loc_4FE3")

    label("loc_4EF0")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0249
    ChrTalk(
        0x13,
        (
            "#2109Fさーて、アルカンシェルの\x01",
            "新作の反響をゲットするわよ～！\x02\x03",

            "#2100Fついでにイリア・プラティエと\x01",
            "リーシャ・マオへの突撃インタビューも\x01",
            "敢行しちゃうんだから！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 300)

    #C0250
    ChrTalk(
        0x13,
        "#2100Fレインズ君、行くわよ～！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x14,
        "は、はいっ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)

    label("loc_4FE3")

    Jump("loc_528A")

    label("loc_4FE8")


    #C0252
    ChrTalk(
        0x13,
        (
            "#2100Fあら、支援課の面々じゃない。\x02\x03",

            "#2109Fいや～、この前のスクープは\x01",
            "本当に有り難かったわ！\x02\x03",

            "これも全部、君たちのおかげね！\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#0000Fはあ……調子いいですね。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x103,
        (
            "#0200F別にグレイスさんのために\x01",
            "何かしたのではありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x102,
        (
            "#0100F……さすがに複雑ですけど……\x02\x03",

            "おじいさまに同情的な\x01",
            "記事だったのは安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x13,
        (
            "#2104Fま、帝国派のネタを書けないのに\x01",
            "市長だけ槍玉に上げるってのも\x01",
            "フェアじゃないしね～。\x02\x03",

            "#2100Fというか、貴方のお祖父様って\x01",
            "市民からの人気は高いし、\x01",
            "あたしも個人的に応援してるの。\x02\x03",

            "記者としては失格かもしれないけど\x01",
            "悪いことは書きたくないのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        "#0102Fグレイスさん……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        (
            "#0300Fま、記者だって人の子だし\x01",
            "そのくらい良いんじゃないッスか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB5, 1)

    label("loc_528A")

    TalkEnd(0xFE)
    Return()

    # Function_25_4E5B end

    def Function_26_528E(): pass

    label("Function_26_528E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_52D4")

    #C0259
    ChrTalk(
        0xFE,
        (
            "先輩に連れられていると\x01",
            "体力不足を痛感するな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5343")

    label("loc_52D4")


    #C0260
    ChrTalk(
        0xFE,
        (
            "ぜえ、ぜえ……\x01",
            "先輩にくっついてると\x01",
            "あちこち走り回らされるので……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "ふう、息が上がっちゃいますよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_5343")

    TalkEnd(0xFE)
    Return()

    # Function_26_528E end

    def Function_27_5347(): pass

    label("Function_27_5347")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_53ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5365")
    Call(0, 29)
    Jump("loc_53E8")

    label("loc_5365")


    #C0262
    ChrTalk(
        0xFE,
        (
            "おとーさんのバカー！\x01",
            "メカオタク～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "せっかくいいフンイキで\x01",
            "お祭り楽しんでたのに～っ！\x01",
            "食欲なくなっちゃったじゃない！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53E8")

    Jump("loc_54CC")

    label("loc_53ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5413")

    #C0264
    ChrTalk(
        0xFE,
        "すごかったわねー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_54CC")

    label("loc_5413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_54CC")

    #C0265
    ChrTalk(
        0xFE,
        (
            "誤解のないように\x01",
            "言っておくけど、\x01",
            "あたしイリアさんも大好きなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "プリエさんもセリーヌさんも\x01",
            "新人のリーシャさんも好きよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "美人なオンナの人は\x01",
            "みんな大好きだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54CC")

    TalkEnd(0xFE)
    Return()

    # Function_27_5347 end

    def Function_28_54D0(): pass

    label("Function_28_54D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_552C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54EE")
    Call(0, 29)
    Jump("loc_5527")

    label("loc_54EE")


    #C0268
    ChrTalk(
        0xFE,
        (
            "うふふ、出店の食べ歩きって\x01",
            "意外と楽しいんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5527")

    Jump("loc_56A4")

    label("loc_552C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5595")

    #C0269
    ChrTalk(
        0xFE,
        "ああ、まったく素晴らしかったよ。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "なるほど、イリアさんの\x01",
            "人気にもうなずけるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56A4")

    label("loc_5595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_56A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_565A")
    OP_4B(0x15, 0xFF)
    OP_93(0xFE, 0xA0, 0x0)

    #C0271
    ChrTalk(
        0x15,
        (
            "んもう、アルカンシェルの\x01",
            "チケットを持ってるなら\x01",
            "どうして先に言わないのよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        "はっは、悪い悪い。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "仕事の関係でいただいて\x01",
            "ずっと忘れていたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    SetScenarioFlags(0x1, 4)
    Jump("loc_56A4")

    label("loc_565A")


    #C0274
    ChrTalk(
        0xFE,
        (
            "ははは……\x01",
            "アルカンシェルに憧れるなんて\x01",
            "パンセもやっぱり女の子だね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A4")

    TalkEnd(0xFE)
    Return()

    # Function_28_54D0 end

    def Function_29_56A8(): pass

    label("Function_29_56A8")

    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    TurnDirection(0x15, 0x16, 0)
    TurnDirection(0x16, 0x15, 0)

    #C0275
    ChrTalk(
        0x15,
        (
            "あっ、そうだ！\x01",
            "あたしアイス食べたい！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x16,
        (
            "うんうん、１つ買って\x01",
            "製造方法を分析してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x16,
        (
            "どんな製造機を\x01",
            "使ってるんだろうね～㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x15,
        (
            "おとーさんのバカー！\x01",
            "変なこと言わないでよっ！！\x02",
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

    # Function_29_56A8 end

    def Function_30_579D(): pass

    label("Function_30_579D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5806")

    #C0279
    ChrTalk(
        0xFE,
        (
            "よしゃー！\x01",
            "待ちに待った最終日よ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "イリア様～、\x01",
            "いま会いに行きますわ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_586A")

    label("loc_5806")


    #C0281
    ChrTalk(
        0xFE,
        (
            "チケット、今日の\x01",
            "Ｂ席しか取れなかったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "でもいいの！\x01",
            "ついにイリア様に会えるんだもの！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_586A")

    TalkEnd(0xFE)
    Return()

    # Function_30_579D end

    def Function_31_586E(): pass

    label("Function_31_586E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5963")

    #C0283
    ChrTalk(
        0x101,
        "#0005Fあれ……何やってるんだ？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "イリアさんに\x01",
            "アイスを頼まれたんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    #C0285
    ChrTalk(
        0xFE,
        (
            "この後公演だし、\x01",
            "急いで戻って手伝わねえと……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#0100F（頑張ってるみたいね。）\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        (
            "#0200F（この子なりに\x01",
            "  道を見つけたようです。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5A09")

    label("loc_5963")


    #C0288
    ChrTalk(
        0xFE,
        (
            "イリアさんは\x01",
            "『舞台で稽古してみる？』って言うけど\x01",
            "……オレはまだ舞台には上がらない。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "しばらくは下働きだけするんだ。\x01",
            "……イリアさんの稽古も\x01",
            "見学できるしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A09")

    TalkEnd(0xFE)
    Return()

    # Function_31_586E end

    def Function_32_5A0D(): pass

    label("Function_32_5A0D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA8")
    OP_29(0x46, 0x1, 0x2)

    #C0290
    ChrTalk(
        0x101,
        (
            "#0001F（よし、歓楽街の聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "（次は裏通りだ……\x01",
            "  同じように聞き込みを進めていこう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_5AA8")

    Return()

    # Function_32_5A0D end

    def Function_33_5AA9(): pass

    label("Function_33_5AA9")

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

    # Function_33_5AA9 end

    def Function_34_5B2A(): pass

    label("Function_34_5B2A")

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

    def lambda_5B9F():
        OP_96(0xFE, 0x5208, 0x0, 0x2E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B9F)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Sleep(500)

    #C0291
    ChrTalk(
        0x101,
        (
            "#0003F#11P（さてと……俺の担当は\x01",
            "  この歓楽街と、中央広場と、\x01",
            "  駅前通りと、西通りになるか。）\x02\x03",

            "#0000F（闇雲に回っても仕方ないから\x01",
            "  １つ１つ街区を当たっていこう。）\x02\x03",

            "（屋内に関してはキリがないから\x01",
            "  受付の人を中心に聞いてみるか。）\x02",
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

    # Function_34_5B2A end

    def Function_35_5D1D(): pass

    label("Function_35_5D1D")

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

    def lambda_5FD2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_5FD2)

    def lambda_5FEC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_5FEC)

    def lambda_6006():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6006)

    def lambda_6020():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_6020)

    def lambda_603A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_603A)
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

    def lambda_626B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_626B)

    def lambda_627C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_627C)
    Sleep(500)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)

    def lambda_62A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_62A3)

    def lambda_62B4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_62B4)
    Sleep(2000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)

    def lambda_62DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62DB)

    def lambda_62EC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62EC)
    Sleep(300)

    def lambda_6309():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_6309)

    def lambda_631A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_631A)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)

    def lambda_634B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_634B)

    def lambda_635C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_635C)
    Sleep(500)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)

    def lambda_6383():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_6383)

    def lambda_6394():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_6394)
    Sleep(1500)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)

    def lambda_63BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_63BB)

    def lambda_63CC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_63CC)
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
            "#0014F#12Pはあ～……\x01",
            "ホンッットーに凄かった！！\x02\x03",

            "こりゃあ確かに\x01",
            "熱狂的なファンがいるわけだよ！\x02",
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
            "ふふっ、そうね。\x02\x03",

            "イリアも凄かったけど\x01",
            "リーシャさんも凄く良かったわ。\x02\x03",

            "うーん、あのイリアが\x01",
            "あれほど入れ込むのも判るわね。\x02",
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
            "#0002F#12Pはは、そうだね。\x02\x03",

            "プレ公演の時よりも更に\x01",
            "息がピッタリ合ってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x1C,
        (
            "#5902F#5Pそういえば……例の事件は\x01",
            "あなた達が解決したのよね？\x02\x03",

            "この前、イリアに連絡した時に\x01",
            "あなた達のことを凄く誉めていたわ。\x02\x03",

            "#5909Fいずれ事件を題材にした舞台を企画して\x01",
            "特別出演してもらいたいとか……\x02",
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
            "#0012F#12Pい、いやあ～。\x01",
            "さすがにそれは冗談なんじゃ？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x1C,
        (
            "#5906F#5Pうーん、どうかしら。\x02\x03",

            "彼女との付き合いは長いけど\x01",
            "割と本気だったりするのよねぇ。\x02\x03",

            "#5900Fま、すぐに気が変わる事も多いから\x01",
            "大丈夫だとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#0006F#12Pそう願いたいよ……\x02\x03",

            "#0000Fなんか、あの人に強引に迫られたら\x01",
            "断りきれない気がするんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x1C,
        (
            "#5904F#5Pふふっ、あれでも結構、\x01",
            "気を遣うタイプなんだけどね。\x02\x03",

            "#5900Fそう言えば──ランディ君には\x01",
            "悪いことをしてしまったかしら。\x02\x03",

            "チケットがもう１枚あったら\x01",
            "一緒に誘う所だったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#0004F#12Pはは、気を遣う必要ないって。\x02\x03",

            "#0000F俺たち、アルカンシェルからは\x01",
            "別にチケットを貰っているしさ。\x02\x03",

            "それに、今ごろランディ、\x01",
            "セシル姉の後輩の人たちと\x01",
            "楽しく遊んでるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x1C,
        (
            "#5902F#5Pふふ、そうね。\x02\x03",

            "#5904Fあの子たちも普段忙しいから\x01",
            "ゆっくり息抜きして欲しいかな。\x02\x03",

            "#5905Fそういえば、ロイドたちも\x01",
            "休暇は今日までなのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#0000F#12Pああ、記念祭中は\x01",
            "警察の仕事も相当増えるしね。\x02\x03",

            "この前の事件のご褒美に\x01",
            "初日だけ休暇を貰えたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x1C,
        (
            "#5909F#5Pふふっ、お疲れさま。\x02\x03",

            "#5902Fそうそう、今日は家で夕食を\x01",
            "食べていってくれるんでしょう？\x02\x03",

            "お母さん達、楽しみにしていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        (
            "#0002F#12Pうん、ご馳走になるよ。\x02\x03",

            "#0005Fでも……夕食まで\x01",
            "まだ時間がありそうだな。\x02\x03",

            "#0012Fえっと……\x01",
            "祭りの様子を見物しに行こうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x1C,
        (
            "#5905F#5Pあ……ゴメンね。\x02\x03",

            "#5906F私、これからちょっと\x01",
            "待ち合わせをしちゃってて……\x02",
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
            "#0011F#12Pえっ……！？\x02\x03",

            "待ち合わせって……\x01",
            "……まさかひょっとして……\x02",
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
            "#5900F#5Pあ、うん……？\x02\x03",

            "これからイリアのメゾンで\x01",
            "会う約束をしているんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0308
    ChrTalk(
        0x101,
        (
            "#0012F#12Pな、なんだ、ハハ……\x02\x01",

            "#0013F（って、焦りすぎだろ俺……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x1C,
        (
            "#5909F#5Pほら、例のリーシャさんを\x01",
            "紹介してくれるらしくって。\x02\x03",

            "#5902Fよかったらロイドも来る？\x01",
            "お互い顔見知りなんでしょうし。\x02",
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
            "#0000F#12Pい、いや、遠慮しとくよ。\x02\x03",

            "女性ばっかりの集まりに\x01",
            "野郎が邪魔するのも何だしさ。\x02\x03",

            "#0006F（というか何となくイリアさんに\x01",
            "  いじられそうな気がするんだよな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x1C,
        (
            "#5909F#5Pふふ、遠慮することないのに。\x02\x03",

            "#5902Fまあいいわ。\x01",
            "今日は付き合ってくれてありがとう。\x02\x03",

            "私も夕食には戻るつもりだから\x01",
            "ロイドもそれまでには家に来てね？\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#0002F#12Pああ、分かったよ。\x02",
    )

    CloseMessageWindow()
    OP_68(-12750, 920, 4100, 5000)

    def lambda_7023():

        label("loc_7023")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_7023")

    QueueWorkItem2(0x101, 0, lambda_7023)
    OP_92(0x1C, 0xFFFFAC04, 0x1A2C, 0x1F4)

    def lambda_7042():
        OP_95(0xFE, -21500, 0, 6700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_7042)
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
            "#0006F#11P……タイミングが悪かったな。\x02\x03",

            "#0008Fもうちょっと兄貴みたいに\x01",
            "積極的になれるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0xFF)
    WaitChrThread(0x1C, 1)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_712C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_712C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7146")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7160")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7160")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_717A")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_717A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7194")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7194")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_71AE")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_71C8")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_71E2")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_71FC")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xB, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7216")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7216")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xC, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7230")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7230")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_724A")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_724A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7264")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7264")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_727E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_727E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7298")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7298")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72B2")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72CC")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x14, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72E6")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_72E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7300")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7312")
    SetScenarioFlags(0xAA, 1)

    label("loc_7312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737F")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "※クエスト達成率が高い\x01",      # 0
            "※クエスト達成率が低い\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_736F"),
        (1, "loc_7377"),
        (SWITCH_DEFAULT, "loc_737F"),
    )


    label("loc_736F")

    SetScenarioFlags(0xAA, 1)
    Jump("loc_737F")

    label("loc_7377")

    ClearScenarioFlags(0xAA, 1)
    Jump("loc_737F")

    label("loc_737F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_7F08")
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
        "娘の声",
        "#1Pあれー、ロイドさん？\x02",
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

    def lambda_7442():
        OP_95(0xFE, -9840, 0, 660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_7442)
    Sleep(100)

    def lambda_745F():
        OP_95(0xFE, -9220, 0, 1590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_745F)
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
        "ロイドさん、こんにちは～！\x02",
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
        "どうもお疲れさまです。\x02",
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
            "#0005F#6Pあ……フランに、ノエル曹長か。\x02\x03",

            "#0000F２人とも私服だから\x01",
            "一瞬、誰だか分からなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x1D,
        (
            "#6309Fあはは……\x01",
            "まあ、たまのオフですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1E,
        (
            "#6400F#11Pふふっ、ロイドさんは\x01",
            "普段とあんまり変わりませんね？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#0004F#6Pあー、普段から行動しやすい\x01",
            "服を着ちゃってるからね。\x02\x03",

            "#0000F２人は姉妹でデートかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x1E,
        "#6409F#11Pえへへ、そうなんですー。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x1D,
        (
            "#6306Fはあ、本当だったら\x01",
            "妹なんかとじゃなくって\x01",
            "彼氏と回りたいんですけど……\x02\x03",

            "#6308Fそんなの作る暇もないしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1D, 500)

    #C0323
    ChrTalk(
        0x1E,
        (
            "#6401F#12Pお姉ちゃん、ひどいー！\x02\x03",

            "忙しくてたまにしか会えないから\x01",
            "今日くらいは付き合ってくれるって\x01",
            "言ったのにー。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x1D,
        (
            "#6302Fはいはい、分かってるって。\x02\x03",

            "#6300F……そういえば、\x01",
            "ロイドさんはここで何を？\x02\x03",

            "誰かと待ち合わせなんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)

    #C0325
    ChrTalk(
        0x101,
        (
            "#0005F#6Pあ、いや……\x02\x03",

            "#0012Fさっきまで連れがいたんだけど\x01",
            "この後、予定が入ってたらしくてさ。\x02\x03",

            "アテが外れてどうしようかって\x01",
            "思っていた所なんだ。\x02",
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
        "#6401F#12P（お姉ちゃん、これって……）\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x1D,
        (
            "#6308F#5P（うん、ひょっとして\x01",
            "  フラれちゃったのかも……）\x02\x03",

            "#6301F（さっき声をかけた時に\x01",
            "  ちょっと表情が曇ってたし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x1E,
        "#6406F#12P（や、やっぱり……）\x02",
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
            "#0000F#6Pえっと……？\x01",
            "（何か勘違いされてるような。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x101, 500)
    TurnDirection(0x1D, 0x101, 500)

    #C0330
    ChrTalk(
        0x1E,
        (
            "#6404F#11Pあの～、ロイドさん。\x02\x03",

            "#6402Fおヒマだったら、わたしたちに\x01",
            "付き合っていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#0005F#6Pへ……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x1D,
        (
            "#6302F実は、港湾区の公園で\x01",
            "ミニライブがあるらしいんです。\x02\x03",

            "あたしたち、これから、\x01",
            "そちらに行くつもりなんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#0005F#6Pああ、そうなのか。\x02\x03",

            "#0002F面白そうだけど……\x01",
            "せっかく姉妹水入らずのところを\x01",
            "邪魔じゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x1E,
        (
            "#6409F#11Pいえいえ～！\x01",
            "ロイドさんならオッケーですよ！\x02\x03",

            "他の男の人だったら\x01",
            "全力で阻止してますけどっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x1D,
        (
            "#6306Fあのね……\x02\x03",

            "#6302Fまあいいや、そういうわけで\x01",
            "折角だから付き合ってくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CD7():
        OP_95(0xFE, -10900, 0, 3030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_7CD7)

    def lambda_7CF1():
        OP_95(0xFE, -11600, 0, 1990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_7CF1)
    OP_68(-11320, 1360, 2530, 3000)
    WaitChrThread(0x1D, 0)

    def lambda_7D20():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_7D20)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x1E, 0)

    def lambda_7D37():
        OP_93(0xFE, 0x78, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_7D37)
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
            "#0011F#5Pちょ、ちょっと２人とも。\x02\x03",

            "誘ってくれるのは有難いんだけど\x01",
            "さすがにこれはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x1D,
        "#6309F#5Pまあまあ、遠慮なさらず。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x1E,
        (
            "#6400F#11Pそうそう。\x01",
            "両手に花ってやつですよー。\x02\x03",

            "#6409Fそれじゃあ、レッツ・ゴーです！\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#0012F#5Pう、うーん……\x02\x03",

            "（なんか誤解されてるみたいだけど\x01",
            "  ……まあいいか。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EAF():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7EAF)

    def lambda_7EC9():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_7EC9)

    def lambda_7EE3():
        OP_97(0xFE, 0x1C84, 0x0, 0xFFFFEF34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_7EE3)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jump("loc_864A")

    label("loc_7F08")

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
        "ランディの声",
        "#2Pおっ、ロイドじゃねえか！\x02",
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

    def lambda_8030():

        label("loc_8030")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8030")

    QueueWorkItem2(0x104, 1, lambda_8030)

    def lambda_8042():

        label("loc_8042")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8042")

    QueueWorkItem2(0x21, 1, lambda_8042)

    def lambda_8054():

        label("loc_8054")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8054")

    QueueWorkItem2(0x1F, 1, lambda_8054)

    def lambda_8066():
        OP_96(0xFE, 0xFFFFD3F0, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_8066)
    Sleep(150)

    def lambda_8083():
        OP_96(0xFE, 0xFFFFCF7C, 0x0, 0x73A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_8083)
    Sleep(150)

    def lambda_80A0():
        OP_96(0xFE, 0xFFFFCC2A, 0x0, 0xA78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_80A0)

    def lambda_80BA():
        OP_96(0xFE, 0xFFFFCDF6, 0x0, 0xF6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_80BA)
    Sleep(4000)
    WaitChrThread(0x20, 0)

    def lambda_80DB():
        TurnDirection(0x20, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_80DB)
    Sleep(800)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x21, 0xFF)

    #C0341
    ChrTalk(
        0x101,
        (
            "#0005F#12Pランディと……\x01",
            "セシル姉の後輩の。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1F, 0)

    #C0342
    ChrTalk(
        0x1F,
        "#5Pあ、弟君だ、やっほー！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x20, 0)

    #C0343
    ChrTalk(
        0x20,
        (
            "#11Pあれれ、確かセシル先輩と\x01",
            "一緒だったんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#0000F#12Pああ、何だか友だちと\x01",
            "会う約束をしてるらしくて。\x02\x03",

            "ちょうど別れた所だったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x21,
        "#5Pあら、そうだったの。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x21,
        (
            "#5Pふふっ……\x01",
            "残念だったわね、ロイド君。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0347
    ChrTalk(
        0x101,
        "#0012F#12P……な、何の事でしょう？\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#0305F#5Pおいおい、ちょっと待て！\x02\x03",

            "#0301Fまさかセシルさん……\x01",
            "どこぞの男と会ってんのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#0004F#12Pはは、イリアさんとだよ。\x02\x03",

            "#0000Fリーシャも一緒みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#0304F#5Pふう、そうか……\x02\x03",

            "#0301Fって、それはそれで\x01",
            "メチャメチャ羨ましいじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8379():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_8379)

    def lambda_8386():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8386)
    TurnDirection(0x1F, 0x104, 500)

    #C0351
    ChrTalk(
        0x1F,
        "#6Pあら、ランディさん～？\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x20,
        (
            "あたしたちより、セシル先輩や\x01",
            "イリア・プラティエの方がいいって\x01",
            "抜かすつもり？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        "#0309F#5Pいや～、滅相もないッス。\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    #C0354
    ChrTalk(
        0x21,
        (
            "#5Pふふ、何だったら\x01",
            "ロイド君も私たちに付き合う？\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x21,
        (
            "#5Pこれから港湾区の公園である\x01",
            "ミニライブに行く所なんだけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84C6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_84C6)

    def lambda_84D3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_84D3)

    def lambda_84E0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_84E0)

    #C0356
    ChrTalk(
        0x101,
        (
            "#0002F#12Pへえ、面白そうですね。\x02\x03",

            "#0000Fそれじゃ、ご一緒しようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x104,
        "#0300F#5Pおお、付き合え付き合え。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x1F,
        (
            "#5Pそれじゃ、弟君も\x01",
            "ゲットしたことだし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x20,
        "#11P港湾区に向かうとしますか！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x78, 0x258)

    def lambda_85B9():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_85B9)
    Sleep(50)

    def lambda_85D6():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_85D6)
    Sleep(100)

    def lambda_85F3():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_85F3)
    Sleep(100)

    def lambda_8610():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_8610)

    def lambda_862A():
        OP_97(0xFE, 0x2328, 0x0, 0xFFFFE7C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_862A)
    FadeToDark(3000, 0, -1)
    OP_0D()

    label("loc_864A")

    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして──\x01",
            "記念祭初日はあっという間に過ぎて行った。\x02\x03",

            "その夜、ロイドはセシルの実家で\x01",
            "夕食をご馳走になり……\x02\x03",

            "亡き兄、ガイの話などを交えながら\x01",
            "思い出話に花を咲かせるのだった。\x02\x03",

            "そして──\x02",
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

    # Function_35_5D1D end

    def Function_36_8729(): pass

    label("Function_36_8729")

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
            "#6P#0001Fピザ屋『バレット・ピザ』……\x01",
            "被害に遭った店舗だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        (
            "#12P#0100Fあの、少しいいでしょうか？\x01",
            "窃盗事件を捜査してまして……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0363
    ChrTalk(
        0xFE,
        "#5Pああ、その話か。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "#5Pやれやれだよ。\x01",
            "接客中とはいえ\x01",
            "つい油断しちまってな……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x104,
        "#11P#0305F……接客中？\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "#5Pああ、お喋りな兄ちゃんが\x01",
            "トロピカルセットを頼んでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "#5Pん～、俺の接客経験から言やあ\x01",
            "ありゃあ外国からの観光客だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "#5Pまあともかく、その兄ちゃんに\x01",
            "丁度品物を渡してる最中だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "#5P確かに背後で\x01",
            "物音がした気がしたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "#5Pいや、あれは絶対\x01",
            "レジをこじ開ける音に違いねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        "#5Pくそっ、俺とした事が……！\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#6P#0000F成る程……\x01",
            "ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C27")
    OP_68(-4460, 1950, -3230, 1200)

    def lambda_8AA2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AA2)

    def lambda_8AAF():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8AAF)

    def lambda_8ABC():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8ABC)

    def lambda_8AC9():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8AC9)
    Sleep(1200)

    #C0373
    ChrTalk(
        0x101,
        "#6P#0003F聞き込みはこんな所かな……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        (
            "#11P#0300Fだな、そろそろ戻って\x01",
            "整理してみようぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C21")

    #C0375
    ChrTalk(
        0x102,
        (
            "#12P#0100F商工会から連絡もないし、\x01",
            "まだ次の犯行は\x01",
            "行われてないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        (
            "#12P#0203Fですね。\x02\x03",

            "#0200F……念のため、\x01",
            "出店を見て回りながら戻った方が\x01",
            "いいかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C21")

    OP_29(0x20, 0x1, 0xD)

    label("loc_8C27")

    OP_5A()
    SetChrPos(0x0, -3450, 0, -1670, 0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_8729 end

    def Function_37_8C4A(): pass

    label("Function_37_8C4A")

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
            "ロイド達は目星をつけた街区へ向かい\x01",
            "張り込みを行う事にした。\x07\x00\x02",
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

            "この客じゃなさそうだな……\x02",
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

    def lambda_8E17():
        OP_95(0xFE, 2270, 1990, 18430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8E17)
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
        "#0306F来ねえな……\x02",
    )

    CloseMessageWindow()

    #A0380
    AnonymousTalk(
        0x103,
        (
            "#0211Fもう１時間以上\x01",
            "張り込んでいますが……\x02",
        )
    )

    CloseMessageWindow()

    #A0381
    AnonymousTalk(
        0x101,
        (
            "#0001Fおかしいな、もう来ても\x01",
            "いいはずなんだが……\x02",
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

    def lambda_8F65():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F65)

    def lambda_8F72():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8F72)

    def lambda_8F7F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8F7F)
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
            "#11P#0001Fはい、ロイド・バニングス──\x02\x03",

            "#0005Fえっ、窃盗犯が現れた……！？\x02",
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
            "#11P#0005Fはい、はい、中央広場ですね。\x02\x03",

            "判りました、すぐに急行します！\x02",
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
            "#0003F#11P……みんなゴメン。\x01",
            "読みが外れたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x102,
        "#12P#0101Fいいから急ぎましょう、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#0001F#11Pそ、そうだな。\x01",
            "今は現場に急ごう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_916D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_916D)

    def lambda_917A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_917A)

    def lambda_9187():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9187)

    def lambda_9194():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9194)
    Sleep(300)
    WaitChrThread(0x102, 1)

    def lambda_91A8():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_91A8)

    def lambda_91BD():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_91BD)

    def lambda_91D2():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_91D2)

    def lambda_91E7():
        OP_9B(0x0, 0xFE, 0x14, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_91E7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_8C4A end

    def Function_38_9214(): pass

    label("Function_38_9214")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9239")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_38_9214")

    label("loc_9239")

    Return()

    # Function_38_9214 end

    def Function_39_923A(): pass

    label("Function_39_923A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9292")
    SetChrName("")

    #A0387
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

    label("loc_9292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92E8")
    SetChrName("")

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アルカンシェルは準備中のようだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_92E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9349")
    SetChrName("")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公演の後で\x01",
            "観客がたくさん残っているようだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_939F")
    SetChrName("")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アルカンシェルは準備中のようだ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_939F")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Return()

    # Function_39_923A end

    def Function_40_93B6(): pass

    label("Function_40_93B6")

    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_40_93B6 end

    def Function_41_93D2(): pass

    label("Function_41_93D2")

    EventBegin(0x1)
    Call(0, 44)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_41_93D2 end

    def Function_42_93EE(): pass

    label("Function_42_93EE")

    EventBegin(0x1)
    Call(0, 43)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_42_93EE end

    def Function_43_940A(): pass

    label("Function_43_940A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_951D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94B7")

    #C0391
    ChrTalk(
        0x101,
        (
            "#0001Fコリン君の目撃情報を\x01",
            "集めてみないと。\x02\x03",

            "#0003F受付や出店をやっている人……\x01",
            "とにかく心当たりのありそうな人に\x01",
            "聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_951D")

    label("loc_94B7")


    #C0392
    ChrTalk(
        0x101,
        (
            "#0001Fコリン君の目撃情報を\x01",
            "集めてみないと。\x02\x03",

            "この辺りで知っていそうな人に\x01",
            "聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_951D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9593")

    #C0393
    ChrTalk(
        0x101,
        (
            "#0001Fこっちはエリィが\x01",
            "調べてくれているはずだ。\x02\x03",

            "予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9593")

    Return()

    # Function_43_940A end

    def Function_44_9594(): pass

    label("Function_44_9594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9641")

    #C0394
    ChrTalk(
        0x101,
        (
            "#0001Fコリン君の目撃情報を\x01",
            "集めてみないと。\x02\x03",

            "#0003F受付や出店をやっている人……\x01",
            "とにかく心当たりのありそうな人に\x01",
            "聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_96A7")

    label("loc_9641")


    #C0395
    ChrTalk(
        0x101,
        (
            "#0001Fコリン君の目撃情報を\x01",
            "集めてみないと。\x02\x03",

            "この辺りで知っていそうな人に\x01",
            "聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9760")

    #C0396
    ChrTalk(
        0x101,
        (
            "#0001F住宅街の方はハロルドさんが\x01",
            "探しているはずだ……\x02\x03",

            "もし見つかれば\x01",
            "すぐに連絡があるだろうし。\x02\x03",

            "予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_97CE")

    label("loc_9760")


    #C0397
    ChrTalk(
        0x101,
        (
            "#0001F住宅街の方はハロルドさんが\x01",
            "探しているはずだ……\x02\x03",

            "予定通り、分担した街区で\x01",
            "聞き込みを続けていこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97CE")

    Return()

    # Function_44_9594 end

    SaveToFile()

Try(main)
