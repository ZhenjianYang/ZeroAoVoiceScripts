from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1100.bin",                # FileName
        "c1100",                    # MapName
        "c1100",                    # Location
        0x0016,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 4210, 2500, 8930, 0, 0, 1, 22, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1100",                  # 0
        "库罗玛",                 # 1
        "奥特",                   # 2
        "塔基库",                 # 3
        "弗兰茨巡警",             # 4
        "达德利搜查官",           # 5
        "艾玛搜查官",             # 6
        "夏娜",                   # 7
        "亚比",                   # 8
        "多诺邦警督",             # 9
        "雷蒙德搜查官",           # 10
        "银",                     # 11
        "中央广场",               # 12
        "西街",                   # 13
        "行政区",                 # 14
        "住宅街",                 # 15
        "欢乐街",                 # 16
        "东街",                   # 17
        "旧城区",                 # 18
        "港湾区",                 # 19
        "ＩＢＣ",                 # 20
        "站前街道",               # 21
        "后巷",                   # 22
        "乌尔斯拉间道",           # 23
        "东克洛斯贝尔街道",       # 24
        "西克洛斯贝尔街道",       # 25
        "玛因兹山道",             # 26
    ))

    AddCharChip((
        "chr/ch24900.itc",                   # 00
        "chr/ch20800.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch00900.itc",                   # 03
        "chr/ch30500.itc",                   # 04
        "chr/ch20300.itc",                   # 05
        "chr/ch34200.itc",                   # 06
        "chr/ch30000.itc",                   # 07
        "chr/ch30300.itc",                   # 08
        "chr/ch30200.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(6929,    2490,    -6650,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(8369,    2390,    -14850,  90,   261,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(-8739,   2500,    6070,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-15050,  2500,    27399,   180,  261,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-22500,  2500,    24280,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-23659,  2500,    24280,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(6530,    2500,    -8260,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6969,    2500,    -9149,   45,   389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-21790,  2500,    27280,   180,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-21100,  2500,    26180,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  8.539999961853027,     -5.630000114440918,    2.450000047683716,     68.0625,               [0.12856481969356537,  0.23570233583450317,   -0.0,                  0.0,                   -0.12856490910053253,  0.23570217192173004,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.8217639923095703,   -0.6858946681022644,   -0.4899999797344208,   1.0])

    DeclActor(-5890,   2500,    31840,   1200,    -5890,   4000,    31840,   0x007C, 0,  24, 0x0000)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西街")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "东街")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧城区")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "站前街道")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "后巷")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-16.899999618530273, 0.0, -123.5, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_580",          # 00, 0
        "Function_1_638",          # 01, 1
        "Function_2_711",          # 02, 2
        "Function_3_73C",          # 03, 3
        "Function_4_B06",          # 04, 4
        "Function_5_C7C",          # 05, 5
        "Function_6_177D",         # 06, 6
        "Function_7_1868",         # 07, 7
        "Function_8_2459",         # 08, 8
        "Function_9_3409",         # 09, 9
        "Function_10_45BD",        # 0A, 10
        "Function_11_4613",        # 0B, 11
        "Function_12_46B4",        # 0C, 12
        "Function_13_47CC",        # 0D, 13
        "Function_14_4801",        # 0E, 14
        "Function_15_482F",        # 0F, 15
        "Function_16_4C2D",        # 10, 16
        "Function_17_4CFC",        # 11, 17
        "Function_18_5052",        # 12, 18
        "Function_19_5077",        # 13, 19
        "Function_20_509C",        # 14, 20
        "Function_21_553B",        # 15, 21
        "Function_22_5699",        # 16, 22
        "Function_23_5721",        # 17, 23
        "Function_24_5B2F",        # 18, 24
    ))


    def Function_0_580(): pass

    label("Function_0_580")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C0"),
        (1, "loc_5CC"),
        (2, "loc_5D8"),
        (3, "loc_5E4"),
        (4, "loc_5F0"),
        (5, "loc_5FC"),
        (6, "loc_608"),
        (SWITCH_DEFAULT, "loc_614"),
    )


    label("loc_5C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_608")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_614")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_637")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_637")

    Return()

    # Function_0_580 end

    def Function_1_638(): pass

    label("Function_1_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_710")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -18240, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -18430, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -7420, 2500, -14630, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_1_638")

    label("loc_710")

    Return()

    # Function_1_638 end

    def Function_2_711(): pass

    label("Function_2_711")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73B")
    OP_94(0xFE, 0x1F72, 0xFFFFEAD4, 0x109A, 0xFFFFD8AA, 0x7D0)
    Sleep(200)
    Jump("Function_2_711")

    label("loc_73B")

    Return()

    # Function_2_711 end

    def Function_3_73C(): pass

    label("Function_3_73C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96E")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_807")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_7F9")

    label("loc_7DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F9")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_7F9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96E")

    label("loc_807")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CD")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A0")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_8BF")

    label("loc_8A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BF")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_8BF")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_96E")

    label("loc_8CD")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_946")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_965")

    label("loc_946")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_965")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_965")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96E")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_991")
    OP_93(0x8, 0x2D, 0x0)
    SetChrFlags(0xB, 0x80)
    Jump("loc_AAD")

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_99F")
    Jump("loc_AAD")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9B2")
    SetChrFlags(0xB, 0x80)
    Jump("loc_AAD")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9C0")
    Jump("loc_AAD")

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9DA")
    SetChrFlags(0x8, 0x80)

    label("loc_9DA")

    Jump("loc_AAD")

    label("loc_9DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A08")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -22770, 2500, 26320, 90)
    Jump("loc_AAD")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A25")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_AAD")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_A33")
    Jump("loc_AAD")

    label("loc_A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A41")
    Jump("loc_AAD")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A4F")
    Jump("loc_AAD")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A5D")
    Jump("loc_AAD")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A6B")
    Jump("loc_AAD")

    label("loc_A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A7E")
    SetChrFlags(0xB, 0x80)
    Jump("loc_AAD")

    label("loc_A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_A96")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AAD")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AA4")
    Jump("loc_AAD")

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_AAD")

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_AC4")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x1, 1)
    Event(0, 21)
    Jump("loc_AEA")

    label("loc_AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_ADB")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x1, 1)
    Event(0, 22)
    Jump("loc_AEA")

    label("loc_ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_AEA")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 23)

    label("loc_AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B05")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_B05")

    Return()

    # Function_3_73C end

    def Function_4_B06(): pass

    label("Function_4_B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1D")

    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B31")
    Jump("loc_B40")

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_B40")
    ClearMapObjFlags(0x6, 0x4)

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B81")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BE2")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BBD")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BE2")

    label("loc_BBD")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_BF3")
    OP_24(0x7B)
    Jump("loc_C0F")

    label("loc_BF3")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_C0F")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C22")
    Jump("loc_C5A")

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C5A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C43")
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_C5A")

    label("loc_C43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_C5A")
    ModifyEventFlags(1, 0, 0x80)
    SetMapObjFlags(0x4, 0x4)

    label("loc_C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C76")
    Jump("loc_C7B")

    label("loc_C76")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_C7B")

    Return()

    # Function_4_B06 end

    def Function_5_C7C(): pass

    label("Function_5_C7C")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1779")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF9")
    OP_AF(0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1774")

    label("loc_CF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0D")
    Jump("loc_1774")

    label("loc_D0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1774")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA1")

    #C0001
    ChrTalk(
        0xFE,
        (
            "啊……差不多\x01",
            "也该打烊了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "要买饮料的话，就抓紧最后的机会吧。\x01",
            "想喝什么，请随便吩咐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE0")

    label("loc_DA1")


    #C0003
    ChrTalk(
        0xFE,
        (
            "要买饮料的话，就抓紧最后的机会吧。\x01",
            "想喝什么，请随便吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE0")

    Jump("loc_1774")

    label("loc_DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E3C")

    #C0004
    ChrTalk(
        0xFE,
        (
            "今天早上好像有很多\x01",
            "警察在转来转去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "难道是发生了什么事吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_EE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAE")

    #C0006
    ChrTalk(
        0xFE,
        "啊呀，今天是个大晴天呢……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "一下雨就没法做生意了，\x01",
            "好天气真是帮了我的大忙呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EDF")

    label("loc_EAE")


    #C0008
    ChrTalk(
        0xFE,
        (
            "今天天气好像会很热呢，\x01",
            "生意应该会很红火吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDF")

    Jump("loc_1774")

    label("loc_EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F65")

    #C0009
    ChrTalk(
        0xFE,
        (
            "因为要召开议会，\x01",
            "这一带从早到晚都很热闹。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "可是……议员和媒体人士\x01",
            "都不常来我这里买东西呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FA6")

    label("loc_F65")


    #C0011
    ChrTalk(
        0xFE,
        "我还是比较喜欢纪念庆典。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "议会之类的，\x01",
            "实在是搞不懂……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA6")

    Jump("loc_1774")

    label("loc_FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_101E")

    #C0013
    ChrTalk(
        0xFE,
        (
            "嗯～差不多也该\x01",
            "换个地方了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "必须要把握住那些在纪念庆典\x01",
            "之后准备回国的客人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A6")

    label("loc_101E")


    #C0015
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "要不要来一杯新鲜果汁～？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "……在市内观光时要是累了的话，\x01",
            "就来和姐姐我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "我可以卖给你们\x01",
            "美味的果汁哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10A6")

    Jump("loc_1774")

    label("loc_10AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_11B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1147")

    #C0018
    ChrTalk(
        0xFE,
        (
            "为了应对纪念庆典，\x01",
            "我准备多订购一些\x01",
            "制作果汁用的水果。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……说起来，\x01",
            "妈妈好像也说过类似的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "嗯～我也不能输啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11AF")

    label("loc_1147")


    #C0021
    ChrTalk(
        0xFE,
        (
            "我妈妈在百货店\x01",
            "负责食材专柜。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "她对进货流程非常熟悉……\x01",
            "我也应该多向她学习一些这方面的窍门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AF")

    Jump("loc_1774")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_11E9")

    #C0023
    ChrTalk(
        0xFE,
        (
            "欢迎光临。\x01",
            "客人，您想点些什么吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B7")

    #C0024
    ChrTalk(
        0xFE,
        (
            "我妈妈在百货店里\x01",
            "负责食材专柜。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "她从以前开始就一直从事着进口食材的工作，\x01",
            "曾经开过一家很有名气的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "呵呵，我之所以会走上经商的道路，\x01",
            "说不定也是受了母亲的影响呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1311")

    label("loc_12B7")


    #C0027
    ChrTalk(
        0xFE,
        (
            "我妈妈在百货店\x01",
            "负责食材专柜。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "在经营进口食材方面，也算是\x01",
            "有着一定的信誉与好评。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1311")

    Jump("loc_1774")

    label("loc_1316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BB")

    #C0029
    ChrTalk(
        0xFE,
        (
            "我也想自己试着做些生意，\x01",
            "于是就开始经营这家店了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "不过……为了购买这架三轮货车，\x01",
            "我还贷款了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "……必须要努力赚钱才行哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1462")

    label("loc_13BB")


    #C0032
    ChrTalk(
        0xFE,
        (
            "因为我想尝试着靠自己的力量来创业，\x01",
            "所以没有求助于母亲，而是选择了贷款。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "只有把生意做好，顺利还清贷款，\x01",
            "才能算是真正意义上的经商。\x01",
            "……必须要更加努力才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1462")

    Jump("loc_1774")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_152A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1483")
    Call(0, 6)
    Jump("loc_1525")

    label("loc_1483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1508")

    #C0034
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "要不要来点果汁呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……刚才有位游击士\x01",
            "来和我搭话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "而、而且还是个\x01",
            "挺帅气的人哦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1525")

    label("loc_1508")


    #C0037
    ChrTalk(
        0xFE,
        (
            "游、游击士果然\x01",
            "很帅呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1525")

    Jump("loc_1774")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_15C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1546")
    Call(0, 6)
    Jump("loc_15C4")

    label("loc_1546")


    #C0038
    ChrTalk(
        0xFE,
        (
            "我这家店很受\x01",
            "游客们的欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "呵呵，走累了的时候，大家\x01",
            "肯定都想喝上一杯果汁吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "选择经营果汁店，真是太正确了。\x02",
    )

    CloseMessageWindow()

    label("loc_15C4")

    Jump("loc_1774")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_168D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E5")
    Call(0, 6)
    Jump("loc_1688")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163C")

    #C0041
    ChrTalk(
        0xFE,
        "嗯～今天也是个好天气呢。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "我感觉清凉的果汁\x01",
            "应该会卖得很好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1688")

    label("loc_163C")


    #C0043
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "要不要来一杯橙汁呀～！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "非常冰凉爽口\x01",
            "的美味橙汁哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1688")

    Jump("loc_1774")

    label("loc_168D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1713")

    #C0045
    ChrTalk(
        0xFE,
        "新鲜的果汁哦～！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "在市内四处奔波的疲惫客人，\x01",
            "怎么样，要不要来杯果汁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "我这里有非常清凉的\x01",
            "新鲜果汁哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1774")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1774")

    #C0048
    ChrTalk(
        0xFE,
        (
            "欢迎光临～！\x01",
            "要不要来一杯新鲜的果汁～？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "香橙、蜜瓜……\x01",
            "各种果汁一应俱全哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1774")

    Jump("loc_C89")

    label("loc_1779")

    TalkEnd(0xFE)
    Return()

    # Function_5_C7C end

    def Function_6_177D(): pass

    label("Function_6_177D")


    #C0050
    ChrTalk(
        0xFE,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "对了，今天就把\x01",
            "美味果汁的制作方法\x01",
            "教给各位吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "在长途跋涉或剧烈运动之后，\x01",
            "补充水份可是很重要的哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '铃铛草莓果汁'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '铃铛草莓果汁'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x16)
    Return()

    # Function_6_177D end

    def Function_7_1868(): pass

    label("Function_7_1868")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191C")

    #C0055
    ChrTalk(
        0xFE,
        (
            "今日的夕阳…\x01",
            "总觉得带有一股哀愁的色彩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "惆怅的晚霞，冰冷的微风，\x01",
            "还有那重归于寂静的傍晚钟声……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "简直就是克洛斯贝尔的一道独特风景啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1968")

    label("loc_191C")


    #C0058
    ChrTalk(
        0xFE,
        (
            "你们差不多\x01",
            "也该早点回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "夜晚的欢乐街\x01",
            "可是个相当危险的场所呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1968")

    Jump("loc_2455")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0D")

    #C0060
    ChrTalk(
        0xFE,
        (
            "今天的议会，似乎又像往日一样，\x01",
            "继续着没完没了的争论呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "嗯，到底要到什么时候才能结束啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "今天都已经是延期的第三天了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A48")

    label("loc_1A0D")


    #C0063
    ChrTalk(
        0xFE,
        (
            "还是一点都没变，自治州的议会\x01",
            "每次都只会不断延长会期！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A48")

    Jump("loc_2455")

    label("loc_1A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B13")

    #C0064
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊的最新一期\x01",
            "好像因故而临时休刊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "据说有人想去商店里购买，\x01",
            "结果也都发现没有到货。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "……究竟是怎么回事呢？\x01",
            "我要求他们做出能让人信服的说明！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B58")

    label("loc_1B13")


    #C0067
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊的最新一期\x01",
            "竟然会延迟出版……怎么会有这种事！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B58")

    Jump("loc_2455")

    label("loc_1B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BCA")

    #C0068
    ChrTalk(
        0xFE,
        "嗯……莫非是发生什么事件了吗？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "总觉得最近这段时间有些不太平呢，\x01",
            "大概只是我的错觉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2455")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1C33")

    #C0070
    ChrTalk(
        0xFE,
        (
            "纪念庆典已经过去了，\x01",
            "街上也恢复了往日的平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "嗯，果然还是平和宁静的感觉最好啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2455")

    label("loc_1C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1C7D")

    #C0072
    ChrTalk(
        0xFE,
        "#4S伊莉娅大人～！！#3S\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "嗯，今天的天气也不错啊！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2455")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D07")

    #C0074
    ChrTalk(
        0xFE,
        (
            "我听说，彩虹剧团\x01",
            "好像要进行一次\x01",
            "对内公开的预演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "……真狡猾！！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "我们普通市民\x01",
            "明明也很期待的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D6A")

    label("loc_1D07")


    #C0077
    ChrTalk(
        0xFE,
        (
            "据说彩虹剧团准备在公演前\x01",
            "面向赞助商等群体\x01",
            "进行一次预演呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……真狡猾！\x01",
            "我也很想看啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6A")

    Jump("loc_2455")

    label("loc_1D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1D")

    #C0079
    ChrTalk(
        0xFE,
        (
            "市政厅那里差不多\x01",
            "也该开始讨论预算草案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "议员们唇枪舌剑的交锋，\x01",
            "似乎会很难收场吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "嗯，为了克洛斯贝尔的将来，\x01",
            "希望大家能努力啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E46")

    label("loc_1E1D")


    #C0082
    ChrTalk(
        0xFE,
        (
            "市长和市政府职员们\x01",
            "也必须要努力呀！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E46")

    Jump("loc_2455")

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECE")

    #C0083
    ChrTalk(
        0xFE,
        (
            "你们很期待彩虹剧团\x01",
            "的最新剧目吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "我也很期待的。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "我弄到了Ｂ席的票，\x01",
            "就去好好欣赏一下吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F17")

    label("loc_1ECE")


    #C0086
    ChrTalk(
        0xFE,
        "伊莉娅大人～！！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯，身为死忠支持者，\x01",
            "必须要每天叫一次才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_2455")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC2")

    #C0088
    ChrTalk(
        0xFE,
        (
            "警察局的那个副局长，\x01",
            "我见过好几次了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "就是那个一脸狡猾之相，\x01",
            "身材矮小的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "我看见他在午休时间里\x01",
            "急急忙忙地跑出去了呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_202C")

    label("loc_1FC2")


    #C0091
    ChrTalk(
        0xFE,
        (
            "警察局的那个副局长\x01",
            "长着一张很好记的脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "虽然不是什么令人喜爱的类型，\x01",
            "但离得很远时就能认出来了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202C")

    Jump("loc_2455")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F8")

    #C0093
    ChrTalk(
        0xFE,
        (
            "如今的市政厅，是一座\x01",
            "在五十年前建造的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "出自一位名叫Ｊ·金德尔\x01",
            "的著名建筑师之手！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "威风凛凛，而且潇洒气派。\x01",
            "真是个非常适合用来代表\x01",
            "克洛斯贝尔的建筑啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_215E")

    label("loc_20F8")


    #C0096
    ChrTalk(
        0xFE,
        (
            "市政厅的建筑物，是由一位\x01",
            "非常著名的建筑师设计的。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "它也很受游客的欢迎，\x01",
            "算是一大观光景点呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215E")

    Jump("loc_2455")

    label("loc_2163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_21D5")

    #C0098
    ChrTalk(
        0xFE,
        (
            "市长虽然已经上了年纪，\x01",
            "但还是经常出差，并参加各种活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "嗯，希望他也能\x01",
            "保重自己的身体啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2455")

    label("loc_21D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227D")

    #C0100
    ChrTalk(
        0xFE,
        (
            "你知道克洛斯贝尔\x01",
            "市政厅的宣传语吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "『让政务对市民开放』……\x01",
            "他们是这么宣扬的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "希望他们能多加努力，\x01",
            "让这句话早日成为现实啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2300")

    label("loc_227D")


    #C0103
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市政厅有着\x01",
            "『让政务对市民开放』\x01",
            "这一口号。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "……但实际上，真正会来这里的市民\x01",
            "其实很少，平时可以说是门可罗雀呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2300")

    Jump("loc_2455")

    label("loc_2305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E7")

    #C0105
    ChrTalk(
        0xFE,
        "早上好……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "嗯，你们几个好像是\x01",
            "克洛斯贝尔的市民啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "我本来还在想，如果是游客的话，\x01",
            "可以对这一带给你们做个详细的介绍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "本地市民的话，那就没必要了！\x01",
            "应该也不用再特意介绍什么了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2455")

    label("loc_23E7")


    #C0109
    ChrTalk(
        0xFE,
        (
            "这一带是行政机关集中的一个街区，\x01",
            "所以市民比较稀少。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "咳咳，我只是出来散散步，\x01",
            "无意中转到这附近而已！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2455")

    TalkEnd(0xFE)
    Return()

    # Function_7_1868 end

    def Function_8_2459(): pass

    label("Function_8_2459")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2555")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2504")

    #C0111
    ChrTalk(
        0xFE,
        (
            "听我说啊！\x01",
            "预算会议终于结束了！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "呼，心中的一块大石头总算是\x01",
            "落了地，可以安心回家啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "不管怎么说，预算毕竟是件\x01",
            "很重要的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2550")

    label("loc_2504")


    #C0114
    ChrTalk(
        0xFE,
        (
            "虽然总算是可以安心工作了……\x01",
            "但作为财务科的一员，\x01",
            "果然还是十分在意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2550")

    Jump("loc_3405")

    label("loc_2555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_264F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FC")

    #C0115
    ChrTalk(
        0xFE,
        (
            "刚才有个媒体界的人士\x01",
            "纠缠不休地向我发问。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "嘿，问什么议会的动向之类，\x01",
            "那种事情，我怎么可能知道～\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "不如说我才比较想知道答案啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_264A")

    label("loc_25FC")


    #C0118
    ChrTalk(
        0xFE,
        (
            "预算会议还在继续进行啊。\x01",
            "身为起草预算案的财务科一员，\x01",
            "实在是非常在意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264A")

    Jump("loc_3405")

    label("loc_264F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_27A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2712")

    #C0119
    ChrTalk(
        0xFE,
        (
            "议事堂那里，今天也是\x01",
            "从早上就开始召开预算会议呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "……表面上说是什么会议，\x01",
            "其实根本就是帝国派与共和国派\x01",
            "在对骂而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "麦克道尔市长也真是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27A2")

    label("loc_2712")


    #C0122
    ChrTalk(
        0xFE,
        (
            "帝国派和共和国派的人\x01",
            "今天也在议事堂那里\x01",
            "互相对骂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "本应起到调解引导作用的\x01",
            "哈尔特曼议长却是个帝国派……\x01",
            "麦克道尔市长也真是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27A2")

    Jump("loc_3405")

    label("loc_27A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2804")

    #C0124
    ChrTalk(
        0xFE,
        "啊～真闲啊……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "虽然很担心预算会议的结果，\x01",
            "但我终究是什么都做不了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3405")

    label("loc_2804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2891")

    #C0126
    ChrTalk(
        0xFE,
        (
            "啊，果汁店的车子\x01",
            "跑到站前街道那边了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……不知为何，我也感觉有些口渴了。\x01",
            "稍后就去那边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A43")

    label("loc_2891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_293F")

    #C0128
    ChrTalk(
        0xFE,
        (
            "嘿，你问果汁店的车子\x01",
            "去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "说起来，我刚才倒是看见\x01",
            "店主把车子推向南出口那边了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "为了提高店铺的知名度，\x01",
            "时不时也要去其它\x01",
            "地方卖一阵啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A43")

    label("loc_293F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29CF")

    #C0131
    ChrTalk(
        0xFE,
        "从明天开始，预算会议总算要正式召开了。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "提交预算草案之后，\x01",
            "也就没有我们这些政府职员什么事了……\x01",
            "嗯～但还是很在意啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A43")

    label("loc_29CF")


    #C0133
    ChrTalk(
        0xFE,
        "从明天开始，预算会议总算要正式召开了。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "……就算我现在也久经世故了，\x01",
            "但那毕竟是自己的工作。\x01",
            "果然很在意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A43")

    Jump("loc_3405")

    label("loc_2A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF4")

    #C0135
    ChrTalk(
        0xFE,
        (
            "在刚才的审议中，\x01",
            "我看见了哈尔特曼议长呢，\x01",
            "虽然只是瞥到了一眼。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "……呜呜，\x01",
            "那个人确实是与众不同呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "散发着一种难以形容的威严气势。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B60")

    label("loc_2AF4")


    #C0138
    ChrTalk(
        0xFE,
        (
            "哈尔特曼议长基本\x01",
            "不会直接参与什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "但却仍然有着非同寻常的威信，\x01",
            "真不愧是重量级的大政治家啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B60")

    Jump("loc_3405")

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF9")

    #C0140
    ChrTalk(
        0xFE,
        "呼，累死了，累死了……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "今天的会议，不如就偷懒不去了吧～\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "反正即使我出席，\x01",
            "也只会被议员先生们横加干涉而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C1D")

    label("loc_2BF9")


    #C0143
    ChrTalk(
        0xFE,
        "这种时期，财务科真是很辛苦呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2C1D")

    Jump("loc_3405")

    label("loc_2C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D25")

    #C0144
    ChrTalk(
        0xFE,
        (
            "在自治州议会上，\x01",
            "帝国派所占的席位超过半数。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "但再怎么说，也没有达到三分之二的人数，\x01",
            "仍然无法随心所欲地强行定夺。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "所以每次都争斗得很激烈呢。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "帝国派与共和国派争斗不休，\x01",
            "受此牵连而不幸告吹的\x01",
            "预算草案实在是数不胜数。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DF5")

    label("loc_2D25")


    #C0148
    ChrTalk(
        0xFE,
        (
            "比如说……那个正在\x01",
            "建设中的新市政厅大楼。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "虽然已经投入了预算，\x01",
            "但因为无法决定由哪边来掌握主导权，\x01",
            "所以直到如今也在争执不休。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "施工进行到一半，就这么搁置下来了。\x01",
            "……要到什么时候才能重新开工呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    Jump("loc_3405")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE5")

    #C0151
    ChrTalk(
        0xFE,
        (
            "在市政厅的会议室，\x01",
            "正在对预算草案进行争论呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "为了应对下个月的预算会议，\x01",
            "要先商讨出一个基本大纲。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "本来那只是我们这些\x01",
            "财政科职员的会议……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "……但不知为何，连那些\x01",
            "议员先生也都前来参与了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F33")

    label("loc_2EE5")


    #C0155
    ChrTalk(
        0xFE,
        (
            "呼，下午的会议\x01",
            "也必须要去参加啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "希望议员先生\x01",
            "能稍微退避一下啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F33")

    Jump("loc_3405")

    label("loc_2F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC1")

    #C0157
    ChrTalk(
        0xFE,
        (
            "警察啊……这个星期好像是\x01",
            "你们的防犯强化周吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "难怪感觉最近总是能看到很多警官，\x01",
            "大概就是因为这个吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3002")

    label("loc_2FC1")


    #C0159
    ChrTalk(
        0xFE,
        (
            "警察也真是的，有这种活动的话，\x01",
            "直接发个正式通知不就行了嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3002")

    Jump("loc_3405")

    label("loc_3007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3090")

    #C0160
    ChrTalk(
        0xFE,
        (
            "差不多也该继续\x01",
            "研讨下一个预算草案了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……又要承受那些\x01",
            "大人物施加的压力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "啊啊，头好疼……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3114")

    label("loc_3090")


    #C0163
    ChrTalk(
        0xFE,
        (
            "我刚到市政厅就任的时候，\x01",
            "也是一个满怀希望的有志青年……！\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "但经过这两三年的磨练，我才算是明白了。\x01",
            "什么才是现实中的政治……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3114")

    Jump("loc_3405")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D5")

    #C0165
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔自治州行驶的巴士\x01",
            "都由交通科来进行管理。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "这个部门是在五年前设立的，\x01",
            "好像一直都非常忙碌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "呵呵，多亏了那些家伙，\x01",
            "巴士才能正常运行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3223")

    label("loc_31D5")


    #C0168
    ChrTalk(
        0xFE,
        (
            "交通科的人真是很辛苦呢～\x01",
            "而我们却老是这么拖拖拉拉的，\x01",
            "实在是很难为情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3223")

    Jump("loc_3405")

    label("loc_3228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_330F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D1")

    #C0169
    ChrTalk(
        0xFE,
        (
            "我的上司就爱\x01",
            "没事乱找碴。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "经常下达一些莫名其妙的无聊命令……\x01",
            "总是这样的话，根本就不能集中精神工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "啊～真不想回去工作啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_330A")

    label("loc_32D1")


    #C0172
    ChrTalk(
        0xFE,
        (
            "市职员的薪酬虽然还不错，\x01",
            "但工作环境实在是太糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330A")

    Jump("loc_3405")

    label("loc_330F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337C")

    #C0173
    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "像我所在的财务科，\x01",
            "总是要承受来自各界的压力。\x01",
            "实在是受够了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3405")

    label("loc_337C")


    #C0175
    ChrTalk(
        0xFE,
        (
            "因为财务科是管钱的～\x01",
            "所以不管是议员还是高官，\x01",
            "都会给我们施加很大的压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "呼，休息一下吧。\x01",
            "偶尔也要出来透透气，不然都要窒息了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3405")

    TalkEnd(0xFE)
    Return()

    # Function_8_2459 end

    def Function_9_3409(): pass

    label("Function_9_3409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_362E")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x101,
        (
            "#0005F弗兰茨？\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "噢噢……这不是罗伊德嘛！\x01",
            "从警察学校毕业之后，\x01",
            "都已经过去一个月了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "对了，说起来，罗伊德，\x01",
            "你好像取得了搜查官资格吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "他们把你分配到哪里了？\x01",
            "肯定是\x01",
            "某个搜查科吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#0006F哎？那个……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0182
    ChrTalk(
        0xFE,
        "什么嘛，怎么吞吞吐吐的……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "算啦，反正我也打算\x01",
            "考取搜查官资格呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "要是在文化课学习中遇到什么不明白的地方，\x01",
            "就麻烦你多多指教吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#0000F啊，好的，这个当然没问题。\x01",
            "（……有空时也要向弗兰茨\x01",
            "  好好说明一下呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_362A")
    SetScenarioFlags(0x1, 2)

    label("loc_362A")

    TalkEnd(0xFE)
    Return()

    label("loc_362E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_363C")
    Jump("loc_45B9")

    label("loc_363C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36CD")

    #C0186
    ChrTalk(
        0xFE,
        (
            "空港那边好像发生了什么事呢。\x01",
            "市内的制服警察也要多加注意，\x01",
            "……收到了这样的指示。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "不过，到底要注意些什么啊？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_370E")

    label("loc_36CD")


    #C0188
    ChrTalk(
        0xFE,
        (
            "今天的指示怎么这么含糊不清，\x01",
            "……这真的是科长下达的指示吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370E")

    Jump("loc_45B9")

    label("loc_3713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3721")
    Jump("loc_45B9")

    label("loc_3721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AF")

    #C0189
    ChrTalk(
        0xFE,
        "哎呀，是罗伊德啊。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "其实……这次的搜查官考试，\x01",
            "我准备去参加了。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0000F噢，弗兰茨……\x01",
            "你终于决定了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "哈哈……虽然觉得自己所学还远远不够。\x01",
            "实践暂且不说，我实在是很怕文化课。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "可我觉得，只要去尝试一次，\x01",
            "就总能慢慢找到感觉的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0194
    ChrTalk(
        0xFE,
        (
            "问题是……最近强化了巡逻工作，\x01",
            "实在是挤不出学习的时间呢。\x01",
            "这段时间，突发事件实在是太多了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3913")

    label("loc_38AF")


    #C0195
    ChrTalk(
        0xFE,
        (
            "科长最近下达了指示，\x01",
            "要对市内巡逻工作进行强化。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "呵呵……实在是越来越难腾出\x01",
            "时间来学习了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3913")

    Jump("loc_45B9")

    label("loc_3918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3AAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A42")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0197
    ChrTalk(
        0xFE,
        "罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "这不是罗伊德嘛！\x01",
            "你没事吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "听说你被鲁巴彻的人给盯上了，\x01",
            "我还在想，你这次又惹了什么麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……消息\x01",
            "果然都已经传开了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        "本来只是署内的秘密呢。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "哈，听说你们已经达成了和解协议，\x01",
            "我总算能放下心啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 6)
    Jump("loc_3AA5")

    label("loc_3A42")


    #C0203
    ChrTalk(
        0xFE,
        "署内流传着各种各样的传闻呢。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "算了，听说你们已经达成了和解协议，\x01",
            "我也可以暂时把心放下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA5")

    Jump("loc_45B9")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3BE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B84")
    OP_93(0xFE, 0xB4, 0x0)

    #C0205
    ChrTalk(
        0xFE,
        (
            "嗯嗯，搜查官的七种道具\x01",
            "的使用方法是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0206
    ChrTalk(
        0xFE,
        (
            "啊，不好意思，\x01",
            "我正在背搜查官考试的题目呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        "#0000F弗兰茨，你也很努力啊。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "哈哈，你们正在调查案件吗？\x01",
            "执行任务辛苦啦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3BE0")

    label("loc_3B84")


    #C0209
    ChrTalk(
        0xFE,
        (
            "听说搜查科的人\x01",
            "最近好像很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……我也要继续努力，\x01",
            "希望能早日取得搜查官的资格。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE0")

    Jump("loc_45B9")

    label("loc_3BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CA3")

    #C0211
    ChrTalk(
        0xFE,
        (
            "达德利警官可是\x01",
            "搜查一科的希望之星呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "不仅在年轻警官之中出类拔萃，\x01",
            "连资深搜查官们也都对他青睐有加。\x01",
            "真是很令人憧憬呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "……虽然是个有些难接近的人。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D0F")

    label("loc_3CA3")


    #C0214
    ChrTalk(
        0xFE,
        (
            "达德利警官虽然很能干，\x01",
            "但却稍微有些难以亲近。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "只是和他走个形式地寒暄一下，\x01",
            "对我来说就已经很累了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0F")

    Jump("loc_45B9")

    label("loc_3D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF3")

    #C0216
    ChrTalk(
        0xFE,
        (
            "当了警官之后，最难承受的\x01",
            "就是市民们的投诉与抱怨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "即使认真尽责地努力工作，\x01",
            "也难免会有犯罪现象发生……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "虽然很想好好保护市民，\x01",
            "但总会遇到很多让人束手无策的情况啊。\x01",
            "呼，真是伤心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3E57")

    label("loc_3DF3")


    #C0219
    ChrTalk(
        0xFE,
        (
            "即使是警官，也会受到\x01",
            "多种制约呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "有很多事情，仅凭正义感根本就\x01",
            "无法解决，真是让人痛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E57")

    Jump("loc_45B9")

    label("loc_3E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_411F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FDB")

    #C0221
    ChrTalk(
        0xFE,
        (
            "哎呀，这不是罗伊德和大家嘛。\x01",
            "工作辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0000F弗兰茨，最近怎么样啊？\x01",
            "你之前说过，很难挤出\x01",
            "时间来学习吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "哈哈，是说搜查官考试吗？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "如你所见，现在还是要以\x01",
            "平时的值勤任务为重。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "当然了，考取搜查官资格\x01",
            "这个目标我也不会放弃的。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#0003F那实在是很辛苦呢……\x01",
            "可不要太过勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "放心好啦。\x01",
            "……罗伊德，倒是你，\x01",
            "可要好好努力啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 1)
    Jump("loc_411A")

    label("loc_3FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4095")

    #C0228
    ChrTalk(
        0xFE,
        (
            "对了，罗伊德……\x01",
            "你们好像经常和那位接待员聊天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "好像是位叫……瑞贝卡的小姐……\x01",
            "真是个大美人呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0230
    ChrTalk(
        0xFE,
        (
            "啊，别误会啦，\x01",
            "我没有其它意思！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_411A")

    label("loc_4095")


    #C0231
    ChrTalk(
        0xFE,
        (
            "接待员瑞贝卡小姐…\x01",
            "真是个大美人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "芙兰小姐虽然也很可爱，\x01",
            "但我果然还是只对瑞贝卡小姐……\x01",
            "……唔，不说这些奇怪的话题啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_411A")

    Jump("loc_45B9")

    label("loc_411F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_41F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418E")

    #C0233
    ChrTalk(
        0xFE,
        "大家执行任务辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "就在刚才，搜查一科的人\x01",
            "出门了呢。\x01",
            "呼，好紧张啊～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_41F1")

    label("loc_418E")


    #C0235
    ChrTalk(
        0xFE,
        (
            "搜查一科的人\x01",
            "果然很帅啊。\x01",
            "个个都是出类拔萃的搜查官。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "……我也想早日考取到\x01",
            "搜查官资格啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F1")

    Jump("loc_45B9")

    label("loc_41F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4345")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D6")

    #C0237
    ChrTalk(
        0xFE,
        (
            "在市内的巡逻任务中，我选择\x01",
            "在这个地方进行警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "虽然看起来只是很不起眼的工作，\x01",
            "但这里也有很多搜查官来来往往呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "我的目标就是成为一名搜查官……\x01",
            "在这里工作的话，能得到很多参考信息吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4340")

    label("loc_42D6")


    #C0240
    ChrTalk(
        0xFE,
        (
            "只要待在这个地方，就可以看到\x01",
            "那些搜查官是如何处理工作的。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "嗯～我实在是很憧憬\x01",
            "搜查官这个职业呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4340")

    Jump("loc_45B9")

    label("loc_4345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4353")
    Jump("loc_45B9")

    label("loc_4353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_43FB")

    #C0242
    ChrTalk(
        0xFE,
        (
            "（话说回来……那两个人\x01",
            "  好像是搜查一科的人啊！）\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "（仅、仅从外表上看，\x01",
            "  就有种非常优秀的感觉呢。\x01",
            "  光是靠近他们就觉得很紧张呢～……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_454D")

    label("loc_43FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_4494")

    #C0244
    ChrTalk(
        0xFE,
        (
            "（……那两个人…\x01",
            "  好像是搜查一科的人啊！）\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "（仅、仅从外表上看，\x01",
            "  就有种非常优秀的感觉呢。\x01",
            "  光是靠近他们就觉得很紧张呢～……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_454D")

    label("loc_4494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44ED")

    #C0246
    ChrTalk(
        0xFE,
        "大家执行任务辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "……今天是我第一次工作。\x01",
            "呼，好紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_454D")

    label("loc_44ED")


    #C0248
    ChrTalk(
        0xFE,
        (
            "不管怎么说，这也是为了\x01",
            "以后能成为一名搜查官……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "不管是什么样的工作，\x01",
            "都不能马虎大意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_454D")

    Jump("loc_45B9")

    label("loc_4552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_45B9")

    #C0250
    ChrTalk(
        0xFE,
        (
            "我的目标是加入搜查一科，\x01",
            "所以打算考取搜查官资格。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "搜查一科果然是\x01",
            "大家憧憬的对象啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B9")

    TalkEnd(0xFE)
    Return()

    # Function_9_3409 end

    def Function_10_45BD(): pass

    label("Function_10_45BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D2")
    Call(0, 11)
    Jump("loc_460F")

    label("loc_45D2")


    #C0252
    ChrTalk(
        0xFE,
        (
            "#0603F哼……\x01",
            "和你们没有关系。\x02\x03",

            "#0600F赶快从我眼前消失。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460F")

    TalkEnd(0xFE)
    Return()

    # Function_10_45BD end

    def Function_11_4613(): pass

    label("Function_11_4613")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0xD, 0x5A, 0x0)

    #C0253
    ChrTalk(
        0xC,
        (
            "#0603F嗯，我接下来就会询问\x01",
            "共和国那边的人。\x02\x03",

            "#0603F艾玛，那方面的调查就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xD,
        (
            "嗯，我马上就会\x01",
            "同Ｋ监视班会合。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_11_4613 end

    def Function_12_46B4(): pass

    label("Function_12_46B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C9")
    Call(0, 11)
    Jump("loc_47C8")

    label("loc_46C9")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0255
    ChrTalk(
        0xFE,
        "特别任务支援科……\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "……请不要妨碍我们的调查工作。\x01",
            "因为你们只不过是没用的累赘而已。\x02",
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

    #C0257
    ChrTalk(
        0x101,
        "#0006F（好像被他说得相当不堪呢……）\x02",
    )

    CloseMessageWindow()

    label("loc_47C8")

    TalkEnd(0xFE)
    Return()

    # Function_12_46B4 end

    def Function_13_47CC(): pass

    label("Function_13_47CC")

    TalkBegin(0xFE)

    #C0258
    ChrTalk(
        0xFE,
        "啊，早上好啊。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "今天的天气也不错呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_47CC end

    def Function_14_4801(): pass

    label("Function_14_4801")

    TalkBegin(0xFE)

    #C0260
    ChrTalk(
        0xFE,
        (
            "我今天也要和妈妈\x01",
            "一起去图书馆～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_4801 end

    def Function_15_482F(): pass

    label("Function_15_482F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_48CE")

    #C0261
    ChrTalk(
        0xFE,
        (
            "今天要处理暴力事件和肇事逃逸犯，\x01",
            "然后就是交易诈骗那边的调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "要是不赶快搞定，\x01",
            "太阳都该下山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        "#0000F搜查二科好像也很忙呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C29")

    label("loc_48CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ADE")

    #C0264
    ChrTalk(
        0xFE,
        (
            "……（啪啪）…………\x01",
            "你们的案子好像被一科给强行接管了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "……算了，这也没办法啊。\x02",
    )


    #C0266
    ChrTalk(
        0xFE,
        (
            "能在一科的管理范围内\x01",
            "掺上一脚，就已经\x01",
            "很不错了，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……果然是\x01",
            "那个道理吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "嗯，该说真不愧是\x01",
            "赛尔盖的部下吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        "算了，总之，尽量不要被人盯上啊。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "如果你们的行为太过惹眼，\x01",
            "可就要做好心理准备，随时遭受\x01",
            "副局长那类人的刁难了。\x02",
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

    #C0271
    ChrTalk(
        0x103,
        "#0200F那个……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        "#0306F唉，饶了我吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4C29")

    label("loc_4ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA8")

    #C0273
    ChrTalk(
        0xFE,
        (
            "竟然能在一科的地盘中\x01",
            "掺上一脚……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "赛尔盖的部下吗……\x01",
            "呵呵，说不定你们也算是\x01",
            "继承了那家伙的某些特点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#0005F……？\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "算了，总之，一定注意不要\x01",
            "显眼到被副局长盯上了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4C29")

    label("loc_4BA8")


    #C0277
    ChrTalk(
        0xFE,
        (
            "……（啪啪）…………\x01",
            "话说回来，雷蒙德那家伙\x01",
            "怎么磨磨蹭蹭的？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "再这么磨蹭下去，去询问案情之前，\x01",
            "我都已经要把香烟抽完了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C29")

    TalkEnd(0xFE)
    Return()

    # Function_15_482F end

    def Function_16_4C2D(): pass

    label("Function_16_4C2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBE")

    #C0279
    ChrTalk(
        0xFE,
        (
            "真想在纪念庆典的时候\x01",
            "和恋人一起出去玩啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "比如说，到米修拉姆\x01",
            "度过一个愉快的假期～\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        "……算了，根本就不可能的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4CF8")

    label("loc_4CBE")


    #C0282
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "我们搜查官，在纪念庆典时期\x01",
            "是不可能放假的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CF8")

    TalkEnd(0xFE)
    Return()

    # Function_16_4C2D end

    def Function_17_4CFC(): pass

    label("Function_17_4CFC")

    EventBegin(0x0)
    Fade(500)
    OP_68(7330, 3500, -6700, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17970, 0)
    SetChrPos(0x101, 6820, 2390, -5850, 270)
    SetChrPos(0x153, 8100, 2390, -5930, 225)
    BeginChrThread(0x101, 1, 0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D8C")
    SetChrPos(0x102, 8160, 2390, -7190, 180)
    BeginChrThread(0x102, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x102, 0x1)
    Jump("loc_4DED")

    label("loc_4D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DBF")
    SetChrPos(0x103, 8160, 2390, -7190, 180)
    BeginChrThread(0x103, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x103, 0x1)
    Jump("loc_4DED")

    label("loc_4DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DED")
    SetChrPos(0x104, 8160, 2390, -7190, 180)
    BeginChrThread(0x104, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x104, 0x1)

    label("loc_4DED")

    EndChrThread(0x101, 0x1)
    OP_0D()

    #C0283
    ChrTalk(
        0x101,
        (
            "#5P#0005F哎……好奇怪啊。\x02\x03",

            "喷泉广场的果汁店，\x01",
            "应该就在这一带吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E9B")
    TurnDirection(0x102, 0x101, 500)

    #C0284
    ChrTalk(
        0x102,
        (
            "#12P#0105F嗯，我觉得也是……\x02\x03",

            "#0103F不过，莫非是\x01",
            "搬到别处去了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F76")

    label("loc_4E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EFE")
    TurnDirection(0x103, 0x101, 500)

    #C0285
    ChrTalk(
        0x103,
        (
            "#12P#0203F嗯，我记得也是如此。\x02\x03",

            "#0200F很可能是搬到\x01",
            "其它地方了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F76")

    label("loc_4EFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F76")
    TurnDirection(0x104, 0x101, 500)

    #C0286
    ChrTalk(
        0x104,
        (
            "#12P#0303F是啊，我之前约会时来过那家店，\x01",
            "不会有错的。\x02\x03",

            "#0301F大概已经搬到其它什么地方了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F76")

    TurnDirection(0x153, 0x101, 500)

    #C0287
    ChrTalk(
        0x153,
        (
            "#11P#1112F哎～那么，\x01",
            "我们就不能给老爷爷\x01",
            "买慰问品了吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    #C0288
    ChrTalk(
        0x101,
        (
            "#5P#0003F不，应该还没有\x01",
            "搬到市外……\x02\x03",

            "#0000F既然都已经接下了委托，\x01",
            "就在市内好好找找吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x153,
        "#11P#1100F嗯！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 8100, 2390, -5930, 225)
    OP_29(0x26, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_17_4CFC end

    def Function_18_5052(): pass

    label("Function_18_5052")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5076")
    OP_93(0xFE, 0x0, 0x226)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x226)
    Sleep(500)
    Jump("Function_18_5052")

    label("loc_5076")

    Return()

    # Function_18_5052 end

    def Function_19_5077(): pass

    label("Function_19_5077")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_509B")
    OP_93(0xFE, 0xB4, 0x258)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x258)
    Sleep(500)
    Jump("Function_19_5077")

    label("loc_509B")

    Return()

    # Function_19_5077 end

    def Function_20_509C(): pass

    label("Function_20_509C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-18580, 4730, 27420, 0)
    MoveCamera(46, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    OP_68(9150, 6030, 14130, 5000)
    MoveCamera(46, 11, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(20160, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(24420, 6330, -12770, 0)
    MoveCamera(71, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16379, 0)
    SetChrFlags(0x8, 0x8000)
    OP_68(-12250, 5080, -8260, 7000)
    MoveCamera(45, 4, 0, 7000)
    OP_6E(700, 7000)
    SetCameraDistance(19000, 7000)
    PlaceName2(340, 40, "c_plac05", 0x0, 6000)
    OP_6F(0x79)
    Sleep(3000)

    #A0290
    AnonymousTalk(
        0x102,
        (
            "#0103F克洛斯贝尔市政厅，\x01",
            "还有警察局总部、市立图书馆……\x02\x03",

            "#0100F真不愧是市政机构\x01",
            "集中的政务区啊。\x02",
        )
    )

    CloseMessageWindow()

    #A0291
    AnonymousTalk(
        0x103,
        (
            "#0202F真是个安静闲适的地方呢。\x01",
            "连喷泉和长椅都有。\x02",
        )
    )

    CloseMessageWindow()

    #A0292
    AnonymousTalk(
        0x102,
        (
            "#0104F在整个城市里，这里也算是黄金地段了……\x01",
            "平时的氛围倒是一直十分宁静。\x02",
        )
    )

    CloseMessageWindow()

    #A0293
    AnonymousTalk(
        0x101,
        (
            "#0000F嗯，警察局总部就在这里，\x01",
            "我想，今后大概也会多次来访吧。\x02\x03",

            "从支援科到这里的具体路线，\x01",
            "一定要仔细记清楚。\x02",
        )
    )

    CloseMessageWindow()

    #A0294
    AnonymousTalk(
        0x104,
        (
            "#0304F了解，队长。\x02\x03",

            "#0300F总部不是还向我们发了个\x01",
            "『支援请求』，呼叫我们过去吗？\x01",
            "就顺路去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "行政区是位于城市北侧的政务机关集中区域。\x02",
        )
    )

    CloseMessageWindow()

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一些重要的设施与警察局总部都在此地，\x01",
            "今后应该有机会多次来访吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0297
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除了克洛斯贝尔市政厅之外，\x01",
            "市立图书馆也坐落在此区域，在馆内可阅览\x01",
            "介绍了游戏世界观的用语辞典。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0x8, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F9")
    OP_68(19940, 2240, -37920, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    Jump("loc_5535")

    label("loc_54F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5535")
    OP_68(-40390, 2240, 24150, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)

    label("loc_5535")

    SetScenarioFlags(0x45, 3)
    EventEnd(0x5)
    Return()

    # Function_20_509C end

    def Function_21_553B(): pass

    label("Function_21_553B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-7500, 3600, 25000, 0)
    MoveCamera(65, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -5500, 2500, 25000, 270)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x8)
    ClearMapObjFlags(0x1, 0x10)

    def lambda_55A1():
        OP_95(0xFE, -18500, 2500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55A1)
    OP_68(-18500, 3600, 25000, 7000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_68(-18500, 4300, 27000, 2500)
    MoveCamera(44, 3, 0, 2500)
    OP_6F(0x41)
    Sleep(1000)

    def lambda_5604():
        OP_95(0xFE, -18500, 2500, 28400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5604)
    WaitChrThread(0x101, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_5637():
        OP_95(0xFE, -18500, 3100, 31400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5637)
    Sleep(500)

    def lambda_5654():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5654)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_553B end

    def Function_22_5699(): pass

    label("Function_22_5699")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-18000, 5000, 30500, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27500, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetMapObjFlags(0x6, 0x4)
    MoveCamera(0, 10, 0, 7000)
    SetCameraDistance(17500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_5699 end

    def Function_23_5721(): pass

    label("Function_23_5721")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00501.itc", 0x1E)
    LoadChrToIndex("apl/ch50220.itc", 0x1F)
    LoadEffect(0x0, "event\\eva04_00.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 33000, 12200, 6000, 270)
    SetChrPos(0x12, 33000, 12200, 6000, 270)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(15000, 11200, 20000, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    MoveCamera(35, 0, 0, 7500)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x12, 0x1E, 0x12C)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)

    def lambda_5806():
        OP_9D(0xFE, 0x61A8, 0x3B60, 0x1770, 0xFA0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5806)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)

    def lambda_583C():
        OP_95(0xFE, 25000, 15200, 19900, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_583C)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    OP_93(0x12, 0x13B, 0x0)
    SetChrSubChip(0x12, 0x0)

    def lambda_5870():
        OP_9D(0xFE, 0x4E20, 0x4074, 0x6144, 0x8FC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5870)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_58A2():
        OP_9D(0xFE, 0x3A98, 0x3B60, 0x74CC, 0x514, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_58A2)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)

    def lambda_58D8():
        OP_95(0xFE, 2500, 15200, 29900, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_58D8)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    ClearChrFlags(0x12, 0x1)
    SetChrSubChip(0x12, 0x0)

    def lambda_590A():
        OP_9D(0xFE, 0xFFFFFE0C, 0x4268, 0x74CC, 0x8FC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_590A)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)

    def lambda_5931():
        OP_9D(0xFE, 0xFFFFD6FC, 0x4268, 0x74CC, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5931)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    Fade(500)
    OP_68(-25800, 14500, 37000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    OP_68(-40700, 10500, 37000, 2000)
    MoveCamera(50, 20, 0, 2000)
    SetChrPos(0x12, -15800, 15500, 37000, 270)
    SetChrFlags(0x12, 0x1)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x12, 0x0)

    def lambda_59CC():
        OP_9D(0xFE, 0xFFFF9B38, 0x34BC, 0x9088, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_59CC)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x12, 1)
    PlayEffect(0x0, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x12, 0x1)
    Sound(31, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_5A3B():
        OP_9D(0xFE, 0xFFFF7EB4, 0x251C, 0x9088, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A3B)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x12, 1)
    PlayEffect(0x0, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    Sound(31, 0, 100, 0)
    Sound(42, 0, 100, 0)

    def lambda_5AB4():
        OP_95(0xFE, -41700, 9500, 37000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5AB4)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_5AE1():
        OP_9D(0xFE, 0xFFFF360C, 0x251C, 0x9088, 0x76C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5AE1)
    Sound(854, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x12, 1)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_5721 end

    def Function_24_5B2F(): pass

    label("Function_24_5B2F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　※　新市政厅大楼建设中　※\x01",
            "除工程相关人员之外，一律禁止入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_5B2F end

    SaveToFile()

Try(main)
