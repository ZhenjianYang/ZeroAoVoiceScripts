from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "クロマ",                 # 1
        "オットー",               # 2
        "タジク",                 # 3
        "フランツ巡査",           # 4
        "ダドリー捜査官",         # 5
        "エマ捜査官",             # 6
        "シャーナ",               # 7
        "アビー",                 # 8
        "ドノバン警部",           # 9
        "レイモンド捜査官",       # 10
        "銀",                     # 11
        "中央広場",               # 12
        "西通り",                 # 13
        "行政区",                 # 14
        "住宅街",                 # 15
        "歓楽街",                 # 16
        "東通り",                 # 17
        "旧市街",                 # 18
        "港湾区",                 # 19
        "ＩＢＣ",                 # 20
        "駅前通り",               # 21
        "裏通り",                 # 22
        "ウルスラ間道",           # 23
        "東クロスベル街道",       # 24
        "西クロスベル街道",       # 25
        "マインツ山道",           # 26
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

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西通り")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "歓楽街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "東通り")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧市街")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "駅前通り")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "裏通り")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "マインツ山道")
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
        "Function_6_1913",         # 06, 6
        "Function_7_1A26",         # 07, 7
        "Function_8_26AF",         # 08, 8
        "Function_9_3705",         # 09, 9
        "Function_10_4973",        # 0A, 10
        "Function_11_49D9",        # 0B, 11
        "Function_12_4A8A",        # 0C, 12
        "Function_13_4B9E",        # 0D, 13
        "Function_14_4BE3",        # 0E, 14
        "Function_15_4C15",        # 0F, 15
        "Function_16_5021",        # 10, 16
        "Function_17_50F6",        # 11, 17
        "Function_18_549E",        # 12, 18
        "Function_19_54C3",        # 13, 19
        "Function_20_54E8",        # 14, 20
        "Function_21_5991",        # 15, 21
        "Function_22_5AEF",        # 16, 22
        "Function_23_5B77",        # 17, 23
        "Function_24_5F85",        # 18, 24
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D07")
    OP_AF(0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_190A")

    label("loc_D07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D1B")
    Jump("loc_190A")

    label("loc_D1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBD")

    #C0001
    ChrTalk(
        0xFE,
        (
            "あ……そろそろ\x01",
            "お店閉めちゃいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "ご注文ならラストオーダーです。\x01",
            "ビシッと言っちゃって下さいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E02")

    label("loc_DBD")


    #C0003
    ChrTalk(
        0xFE,
        (
            "ご注文ならラストオーダーですよ。\x01",
            "ビシッと言っちゃって下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E02")

    Jump("loc_190A")

    label("loc_E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E68")

    #C0004
    ChrTalk(
        0xFE,
        (
            "今朝は警察の人たちが\x01",
            "バタバタしていたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "何かあったのかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDE")

    #C0006
    ChrTalk(
        0xFE,
        "あら、今日は快晴ですね……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "雨だとお商売できないので\x01",
            "天気がいいのは助かりますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F17")

    label("loc_EDE")


    #C0008
    ChrTalk(
        0xFE,
        (
            "今日は暑くなりそうだし\x01",
            "売り上げも期待できそうです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F17")

    Jump("loc_190A")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_100F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC1")

    #C0009
    ChrTalk(
        0xFE,
        (
            "議会が開かれているとかで、\x01",
            "朝夕はこの辺りも賑やかなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "でも……議員の人もマスコミの人も\x01",
            "あまり買ってくれないんですよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100A")

    label("loc_FC1")


    #C0011
    ChrTalk(
        0xFE,
        "私は記念祭の方がいいです。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "議会なんて\x01",
            "よく分からないですし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100A")

    Jump("loc_190A")

    label("loc_100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1086")

    #C0013
    ChrTalk(
        0xFE,
        (
            "うーん、そろそろ場所を\x01",
            "変えようかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "記念祭から帰国する\x01",
            "お客さんを狙わないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112C")

    label("loc_1086")


    #C0015
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "新鮮なジュースはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "……市内観光に疲れたら\x01",
            "お姉さんに言ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "おいしいジュースを\x01",
            "販売しちゃいますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_112C")

    Jump("loc_190A")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_126C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F1")

    #C0018
    ChrTalk(
        0xFE,
        (
            "記念祭に向けて、\x01",
            "ジュース用の果物の仕入れを\x01",
            "増やす予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……そういえば母も\x01",
            "似たような事を言ってましたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "うーん、私も負けてられませんね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1267")

    label("loc_11F1")


    #C0021
    ChrTalk(
        0xFE,
        (
            "母は百貨店の食材コーナーを\x01",
            "任されているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "仕入れが大得意なので……\x01",
            "こっそりコツを教えてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1267")

    Jump("loc_190A")

    label("loc_126C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12AF")

    #C0023
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ。\x01",
            "お客様も何か注文なさいます？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_140A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391")

    #C0024
    ChrTalk(
        0xFE,
        (
            "私の母は百貨店で\x01",
            "食材コーナーを任されているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "昔から輸入食材を扱う仕事をしていて、\x01",
            "結構有名なお店を開いていたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ふふっ、私がお商売を始めたのは\x01",
            "母の影響かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1405")

    label("loc_1391")


    #C0027
    ChrTalk(
        0xFE,
        (
            "母は百貨店で\x01",
            "食材コーナーを任されているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "輸入食材の取り扱いにかけては\x01",
            "ちょっと定評があるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1405")

    Jump("loc_190A")

    label("loc_140A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BF")

    #C0029
    ChrTalk(
        0xFE,
        (
            "私、自分で商売をやってみたくて\x01",
            "出店を始めたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "でも……このオート三輪を\x01",
            "買うのに借金してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "……がんばって稼がなくっちゃ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1554")

    label("loc_14BF")


    #C0032
    ChrTalk(
        0xFE,
        (
            "自分の力を試したかったので、\x01",
            "母には頼らず借金をしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "出店を成功させて、借金を\x01",
            "返してこそ真のお商売ですよね。\x01",
            "……がんばらなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1554")

    Jump("loc_190A")

    label("loc_1559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_165C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1575")
    Call(0, 6)
    Jump("loc_1657")

    label("loc_1575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1622")

    #C0034
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "ジュースはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……さっき遊撃士の方が\x01",
            "声を掛けてくださったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "ちょ、ちょっと\x01",
            "カッコいい人だったな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1657")

    label("loc_1622")


    #C0037
    ChrTalk(
        0xFE,
        (
            "ゆ、遊撃士の方って\x01",
            "やっぱりカッコいいですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657")

    Jump("loc_190A")

    label("loc_165C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1709")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1678")
    Call(0, 6)
    Jump("loc_1704")

    label("loc_1678")


    #C0038
    ChrTalk(
        0xFE,
        (
            "ウチのお店って\x01",
            "観光客の人に人気なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ふふ、やっぱり\x01",
            "歩き疲れたときはジュースですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "ジュース屋を始めてよかったなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_1704")

    Jump("loc_190A")

    label("loc_1709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_17FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1725")
    Call(0, 6)
    Jump("loc_17F6")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E")

    #C0041
    ChrTalk(
        0xFE,
        "うーん、今日もいいお天気ですね。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "冷えたジュースが\x01",
            "よく売れそうな気がします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17F6")

    label("loc_178E")


    #C0043
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "オレンジジュースはいかがですか～！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "よく冷えた\x01",
            "オレンジジュースですよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F6")

    Jump("loc_190A")

    label("loc_17FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_188D")

    #C0045
    ChrTalk(
        0xFE,
        "新鮮なジュースですよ～！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "市内を歩き回って\x01",
            "お疲れのお客さん、いかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "とっても冷えた\x01",
            "フルーツジュースですよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190A")

    label("loc_188D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_190A")

    #C0048
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませー！\x01",
            "新鮮なジュースはいかがですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "オレンジ、メロン、\x01",
            "各種フルーツを扱っていますよー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190A")

    Jump("loc_C89")

    label("loc_190F")

    TalkEnd(0xFE)
    Return()

    # Function_5_C7C end

    def Function_6_1913(): pass

    label("Function_6_1913")


    #C0050
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "そうだ、今日は皆さんに\x01",
            "おいしいジュースの作り方を\x01",
            "教えちゃいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "歩き回ったり運動した後は\x01",
            "水分補給が重要なんですよ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x16)
    Return()

    # Function_6_1913 end

    def Function_7_1A26(): pass

    label("Function_7_1A26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD6")

    #C0055
    ChrTalk(
        0xFE,
        (
            "今日の夕日は\x01",
            "どことなく哀愁を帯びているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "物悲しい夕焼け、冷たいそよ風、\x01",
            "そして静かになる晩鐘……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "まさにクロスベルの風物詩だな！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B2E")

    label("loc_1AD6")


    #C0058
    ChrTalk(
        0xFE,
        (
            "君たちも\x01",
            "そろそろ家に帰りなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "夜の歓楽街などは、\x01",
            "中々危険な場所だからな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2E")

    Jump("loc_26AB")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD7")

    #C0060
    ChrTalk(
        0xFE,
        (
            "今日もまた、議会では\x01",
            "議論が繰り広げられているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "ふむ、いつになったら終わるのか。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "今日で延長３日目だったと思うが。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C0E")

    label("loc_1BD7")


    #C0063
    ChrTalk(
        0xFE,
        (
            "相変わらず自治州議会は\x01",
            "会期を延ばしてばかりだな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0E")

    Jump("loc_26AB")

    label("loc_1C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD3")

    #C0064
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズの最新刊が\x01",
            "何故だか臨時休刊しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "販売店に行っても\x01",
            "置いていないという。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "……どういうことかな？\x01",
            "納得の行く説明を要求する！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D0E")

    label("loc_1CD3")


    #C0067
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズの\x01",
            "最新刊が遅れるなど……ありえん！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0E")

    Jump("loc_26AB")

    label("loc_1D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D7C")

    #C0068
    ChrTalk(
        0xFE,
        "む……何か事件があったのか？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "近頃物騒になった気がするな。\x01",
            "私の気のせいだろうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AB")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1DD5")

    #C0070
    ChrTalk(
        0xFE,
        (
            "記念祭も過ぎ去り、\x01",
            "街も落ち着いたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "うむ、やはり平和が一番だ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_26AB")

    label("loc_1DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1E25")

    #C0072
    ChrTalk(
        0xFE,
        "#4Sイリア様～……っ！！#3S\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "ふむ、今日もいい天気だな！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_26AB")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED7")

    #C0074
    ChrTalk(
        0xFE,
        (
            "聞いたところによると、\x01",
            "アルカンシェルには\x01",
            "プレ公演というものがあるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "……ずるい！！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "私たち市民も、\x01",
            "楽しみにしているというのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F48")

    label("loc_1ED7")


    #C0077
    ChrTalk(
        0xFE,
        (
            "アルカンシェルは、\x01",
            "事前にスポンサー向けに\x01",
            "プレ公演をやるというが……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……ずるい！\x01",
            "私だって見たいのに！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F48")

    Jump("loc_26AB")

    label("loc_1F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_203F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200D")

    #C0079
    ChrTalk(
        0xFE,
        (
            "そろそろ市庁舎では\x01",
            "予算原案が話し合われる時期だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "議員の横槍が入って\x01",
            "何かとやりにくかろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ふむ、クロスベルのために\x01",
            "みんな頑張ってくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_203A")

    label("loc_200D")


    #C0082
    ChrTalk(
        0xFE,
        (
            "市長や市職員には\x01",
            "頑張ってもらわねばな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203A")

    Jump("loc_26AB")

    label("loc_203F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_212E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DC")

    #C0083
    ChrTalk(
        0xFE,
        (
            "アルカンシェル、\x01",
            "楽しみにしているかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "私も楽しみだ。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "Ｂ席のチケットが手に入ったから\x01",
            "観に行くとしようじゃないか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2129")

    label("loc_20DC")


    #C0086
    ChrTalk(
        0xFE,
        "イリア様～……っ！！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "うむ、ファンたるもの\x01",
            "一日一度は叫ばないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2129")

    Jump("loc_26AB")

    label("loc_212E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F0")

    #C0088
    ChrTalk(
        0xFE,
        (
            "警察の副局長どのなら\x01",
            "何度か見かけたことがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "あのキツネのような顔をした\x01",
            "小柄な人物だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "お昼休みなど、せかせかと\x01",
            "歩いて出て行くのを見かけるぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_225C")

    label("loc_21F0")


    #C0091
    ChrTalk(
        0xFE,
        (
            "警察の副局長どのは\x01",
            "分かりやすい顔をしているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "とても好人物とは言えんが、\x01",
            "遠目でも良く分かるぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225C")

    Jump("loc_26AB")

    label("loc_2261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_23B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233A")

    #C0093
    ChrTalk(
        0xFE,
        (
            "今の市庁舎の建物は\x01",
            "５０年前に造られたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "Ｊ・キンドールという\x01",
            "有名な建築家の手によるものだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "威風堂々、そして瀟洒#4Rしょうしゃ#。\x01",
            "クロスベルを代表するに\x01",
            "相応しい建物だな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23AE")

    label("loc_233A")


    #C0096
    ChrTalk(
        0xFE,
        (
            "市庁舎の建物は、さる有名な\x01",
            "建築家の手がけたものなのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "観光客にもすべからく人気な\x01",
            "観光スポットなのだよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AE")

    Jump("loc_26AB")

    label("loc_23B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2425")

    #C0098
    ChrTalk(
        0xFE,
        (
            "市長はご高齢にも関わらず\x01",
            "会合や出張の多い方だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "ふむ、体には\x01",
            "気をつけて頂きたいものだな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AB")

    label("loc_2425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E9")

    #C0100
    ChrTalk(
        0xFE,
        (
            "クロスベル市庁舎の\x01",
            "合言葉を知っておるかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "『市民に開かれた行政』……\x01",
            "そんな言葉を掲げておるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "真に開かれた行政となるよう\x01",
            "頑張って欲しいものだな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2572")

    label("loc_24E9")


    #C0103
    ChrTalk(
        0xFE,
        (
            "クロスベル市庁舎は\x01",
            "『市民に開かれた行政』という\x01",
            "合言葉を掲げている。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "……実際は利用者も少なく、\x01",
            "閑古鳥が鳴いているそうだがな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2572")

    Jump("loc_26AB")

    label("loc_2577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263F")

    #C0105
    ChrTalk(
        0xFE,
        "おはよう……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "フム、君たちは\x01",
            "クロスベル市民のようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "観光客ならばこの辺りを\x01",
            "詳しく案内してやるんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "市民なら、結構、結構！\x01",
            "特に案内もいらんだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26AB")

    label("loc_263F")


    #C0109
    ChrTalk(
        0xFE,
        (
            "この辺りは官公庁街でね。\x01",
            "市民の人影は極めて少ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "おっほん、つまり\x01",
            "散歩にはうってつけなのだよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AB")

    TalkEnd(0xFE)
    Return()

    # Function_7_1A26 end

    def Function_8_26AF(): pass

    label("Function_8_26AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_27C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276A")

    #C0111
    ChrTalk(
        0xFE,
        (
            "聞いてくれ！\x01",
            "ようやく予算議会が終わったんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "ふう、これで心置きなく\x01",
            "家に帰れるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "やっぱ何だかんだ言っても\x01",
            "予算ってのは大事だからな、うん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27C4")

    label("loc_276A")


    #C0114
    ChrTalk(
        0xFE,
        (
            "ついマジメに仕事しちまったが……\x01",
            "やっぱ財務課としちゃあ\x01",
            "すげー気になってたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C4")

    Jump("loc_3701")

    label("loc_27C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2874")

    #C0115
    ChrTalk(
        0xFE,
        (
            "さっきマスコミの人間が\x01",
            "しつこく質問していったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "へっ、議会の行方なんて\x01",
            "俺が知るかっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "むしろこっちが聞きたいくらいだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28D6")

    label("loc_2874")


    #C0118
    ChrTalk(
        0xFE,
        (
            "予算議会、まだやってるんだよなぁ。\x01",
            "予算案を纏めた財務課としては\x01",
            "何だかんだいって気になるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D6")

    Jump("loc_3701")

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A2")

    #C0119
    ChrTalk(
        0xFE,
        (
            "議事堂じゃ、今日も\x01",
            "朝から予算議会をやってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "……議会なんて名前ばかりで\x01",
            "もはや帝国派と共和国派の\x01",
            "罵り合いだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "ふう……\x01",
            "マクダエル市長も大変だよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A34")

    label("loc_29A2")


    #C0122
    ChrTalk(
        0xFE,
        (
            "議事堂じゃ、今日も\x01",
            "帝国派と共和国派が\x01",
            "罵り合いをやっているぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "纏め役のはずの\x01",
            "ハルトマン議長は帝国派だし……\x01",
            "マクダエル市長も大変だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A34")

    Jump("loc_3701")

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A9E")

    #C0124
    ChrTalk(
        0xFE,
        "あー、暇だなぁ……\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "予算議会の行方は心配だが、\x01",
            "どうすることも出来ねえしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3701")

    label("loc_2A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2D08")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B37")

    #C0126
    ChrTalk(
        0xFE,
        (
            "ああ、ジューススタンドは\x01",
            "駅前通りに行ってたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "……なんだか俺も喉が渇いてきたぜ。\x01",
            "後で行ってみるかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D03")

    label("loc_2B37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2C09")

    #C0128
    ChrTalk(
        0xFE,
        (
            "へ、ジューススタンドが\x01",
            "どこに行ったかって？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "そういえばさっき、屋台ごと\x01",
            "南口の方に向かっているのを見たな。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "店の知名度を上げるために、\x01",
            "ときどき別の場所に行くことが\x01",
            "あるんだとさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D03")

    label("loc_2C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9F")

    #C0131
    ChrTalk(
        0xFE,
        "明日からいよいよ予算議会だぜ。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "予算案は提出してあるから\x01",
            "俺たち役人の出番じゃないんだが……\x01",
            "うーん、やっぱ気になるよな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D03")

    label("loc_2C9F")


    #C0133
    ChrTalk(
        0xFE,
        "明日からいよいよ予算議会だ。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "……いくら俺がすれてたって\x01",
            "自分の仕事だ。\x01",
            "やっぱ気になるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D03")

    Jump("loc_3701")

    label("loc_2D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB8")

    #C0135
    ChrTalk(
        0xFE,
        (
            "さっきの審議中に、\x01",
            "ちらっとだけハルトマン議長が\x01",
            "顔を見せたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "……ううっ、\x01",
            "やっぱりあの人は別格だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "なんつーか威厳があるんだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E26")

    label("loc_2DB8")


    #C0138
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長は\x01",
            "口出したりはしないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "異様に貫禄があるんだよな。\x01",
            "さすがは大物政治家だぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E26")

    Jump("loc_3701")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC3")

    #C0140
    ChrTalk(
        0xFE,
        "はあ、だるいだるい……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "今日の会議はサボっちまおうかな～。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "どうせ出たって\x01",
            "議員先生の横槍に耐えるだけだもんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EE3")

    label("loc_2EC3")


    #C0143
    ChrTalk(
        0xFE,
        "この時期、財務課は辛いぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_2EE3")

    Jump("loc_3701")

    label("loc_2EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_30BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE9")

    #C0144
    ChrTalk(
        0xFE,
        (
            "自治州議会は\x01",
            "帝国派が過半数を牛耳ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "かといって強行採決できる\x01",
            "３分の２には届かないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "だからいつもすごい荒れるんだよな。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "帝国派と共和国派、\x01",
            "そのいざこざに巻き込まれて\x01",
            "お流れになった予算も数知れずだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30B5")

    label("loc_2FE9")


    #C0148
    ChrTalk(
        0xFE,
        (
            "たとえば……例の\x01",
            "建設中の新しい市庁舎ビルだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "あれは一度予算が付いたのに\x01",
            "どっちが主導権を握るかで\x01",
            "いまだ揉めていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "工事途中で凍結されちまったんだよ。\x01",
            "……いつになったら再開するのやら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B5")

    Jump("loc_3701")

    label("loc_30BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AD")

    #C0151
    ChrTalk(
        0xFE,
        (
            "市庁舎の会議室では\x01",
            "予算原案を打ち合わせてる所だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "来月の予算議会に向けて\x01",
            "大綱を纏めてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "当然、俺たち財務課役人だけの\x01",
            "会議なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "……なぜか議員先生も\x01",
            "首を突っ込んで来るんだよなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3211")

    label("loc_31AD")


    #C0155
    ChrTalk(
        0xFE,
        (
            "ふう、また午後の部には\x01",
            "顔を出さねえと。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "議員先生も少しは\x01",
            "顔を引っ込めてくんねえかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3211")

    Jump("loc_3701")

    label("loc_3216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_32D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3291")

    #C0157
    ChrTalk(
        0xFE,
        (
            "警察って……今週は\x01",
            "防犯強化週間だったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "警官が多い気がするのは\x01",
            "そのせいかー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32D0")

    label("loc_3291")


    #C0159
    ChrTalk(
        0xFE,
        (
            "警察もそういう事するなら、\x01",
            "ちゃんと通知すればいいのにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D0")

    Jump("loc_3701")

    label("loc_32D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_33E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3362")

    #C0160
    ChrTalk(
        0xFE,
        (
            "そろそろ次の\x01",
            "予算原案を纏めねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……また色んな\x01",
            "先生方から圧力が来るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "ああ、頭が痛いぜ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33DC")

    label("loc_3362")


    #C0163
    ChrTalk(
        0xFE,
        (
            "オレも市庁に就職したときは\x01",
            "希望に溢れる若者だった……！\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "でも２、３年すれば分かるぜ。\x01",
            "政治の現実って奴がさぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DC")

    Jump("loc_3701")

    label("loc_33E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_350A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B1")

    #C0165
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州を走るバスは\x01",
            "交通課って所が管理してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "５年ほど前にできた部署でさ、\x01",
            "いつも忙しそうにしてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "ま、連中のお陰で\x01",
            "バスが運行されてるんだもんなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3505")

    label("loc_34B1")


    #C0168
    ChrTalk(
        0xFE,
        (
            "交通課の人は大変なんだよなー。\x01",
            "ダラダラしてるこっちが\x01",
            "恥ずかしくなっちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3505")

    Jump("loc_3701")

    label("loc_350A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_35EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    #C0169
    ChrTalk(
        0xFE,
        (
            "ウチの上司は\x01",
            "小言が多いんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "下らない注文もつけてくるし……\x01",
            "あれじゃ仕事に集中できないっての。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "あー、職場に戻りたくねえなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35E6")

    label("loc_35B9")


    #C0172
    ChrTalk(
        0xFE,
        (
            "市職員は給料は良いが、\x01",
            "職場は最悪だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E6")

    Jump("loc_3701")

    label("loc_35EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_366E")

    #C0173
    ChrTalk(
        0xFE,
        "ふう……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "オレが勤めてる財務課って\x01",
            "あちこちから圧力が掛かるんだよな。\x01",
            "いい加減イヤになるぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3701")

    label("loc_366E")


    #C0175
    ChrTalk(
        0xFE,
        (
            "財務課はミラを預かってるからなー。\x01",
            "議員だの高官だのから\x01",
            "圧力が掛かってくるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "ふう、休憩休憩。\x01",
            "たまには外に出なくちゃ息が詰まるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3701")

    TalkEnd(0xFE)
    Return()

    # Function_8_26AF end

    def Function_9_3705(): pass

    label("Function_9_3705")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_396A")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x101,
        (
            "#0005Fフランツ？\x01",
            "久し振りだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "おお……ロイドじゃんか！\x01",
            "警察学校を卒業してからだから\x01",
            "１ヶ月ぶりくらいかぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "そういやロイドって\x01",
            "捜査官資格まで取っちまったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "配属はどうだったんだ？\x01",
            "やっぱしょっぱな\x01",
            "どこかの捜査課だったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#0006Fえ？　ええとその……\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0182
    ChrTalk(
        0xFE,
        "何だよ、煮え切らないなぁ……\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "まあいいや、俺もそのうち\x01",
            "捜査官資格を取るつもりだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "座学で分からない所があったら\x01",
            "教えてくれよな！\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#0000Fあ、ああ、全然構わないけど。\x01",
            "（……フランツにもちゃんと\x01",
            "  説明しておかないとなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_3966")
    SetScenarioFlags(0x1, 2)

    label("loc_3966")

    TalkEnd(0xFE)
    Return()

    label("loc_396A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3978")
    Jump("loc_496F")

    label("loc_3978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0F")

    #C0186
    ChrTalk(
        0xFE,
        (
            "空港の方で何かあったらしいな。\x01",
            "市内の制服組も注意するように\x01",
            "……とか指示が来たよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "でも、どう注意すりゃいいんだ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3A50")

    label("loc_3A0F")


    #C0188
    ChrTalk(
        0xFE,
        (
            "何だか今日の指示は曖昧だよ。\x01",
            "……本当に課長の指示なのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A50")

    Jump("loc_496F")

    label("loc_3A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A63")
    Jump("loc_496F")

    label("loc_3A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFB")

    #C0189
    ChrTalk(
        0xFE,
        "やあロイドか。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "実は……今度の捜査官試験、\x01",
            "受けてみようと思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0000Fお、フランツ……\x01",
            "ついに決めたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "はは……まだまだ勉強不足だけどな。\x01",
            "実技はともかく座学は苦手だし。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "でも一度受けてみれば\x01",
            "雰囲気とかもつかめると思ってさ。\x02",
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
            "問題は……最近巡回が強化されて\x01",
            "勉強する時間が取れない事だよ。\x01",
            "近頃はやたら事件も多いしさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3C5F")

    label("loc_3BFB")


    #C0195
    ChrTalk(
        0xFE,
        (
            "最近課長の指示で\x01",
            "市内巡回が強化されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "とほほ……ますます\x01",
            "勉強する時間が取れないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5F")

    Jump("loc_496F")

    label("loc_3C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3E0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAC")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0197
    ChrTalk(
        0xFE,
        "ロイド……？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "ロイドじゃないか！\x01",
            "無事だったのか！\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "ルバーチェに狙われてるとか聞いたから\x01",
            "今度は何をやらかしたのかと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0000Fはは……やっぱり\x01",
            "噂になってたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        "署内だけの話だけどな。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "まあ手打ちになったとも聞いたし\x01",
            "ようやく一安心ってところか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 6)
    Jump("loc_3E05")

    label("loc_3DAC")


    #C0203
    ChrTalk(
        0xFE,
        "署内でも色々噂になってたよ。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "まあ手打ちになったとも聞いたし\x01",
            "オレも一安心だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E05")

    Jump("loc_496F")

    label("loc_3E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE2")
    OP_93(0xFE, 0xB4, 0x0)

    #C0205
    ChrTalk(
        0xFE,
        (
            "ええと、捜査官の\x01",
            "七つ道具の使い方は……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0206
    ChrTalk(
        0xFE,
        (
            "おっとスマン、\x01",
            "捜査官試験の暗誦をな。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        "#0000Fフランツも頑張ってるなぁ。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "はは、ロイド達は捜査中かい？\x01",
            "任務ご苦労様！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F46")

    label("loc_3EE2")


    #C0209
    ChrTalk(
        0xFE,
        (
            "最近捜査課の人たち、\x01",
            "忙しそうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……俺も頑張って\x01",
            "早く捜査官資格を取りたいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F46")

    Jump("loc_496F")

    label("loc_3F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400B")

    #C0211
    ChrTalk(
        0xFE,
        (
            "ダドリーさんは\x01",
            "捜査一課のホープなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "若手の中じゃ一番で、年配の\x01",
            "捜査官も一目置いてるんだってさ。\x01",
            "憧れるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "……ちょっと近づきがたい人だけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_407F")

    label("loc_400B")


    #C0214
    ChrTalk(
        0xFE,
        (
            "ダドリーさんって凄いと思うけど、\x01",
            "ちょっと近づきがたい人だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "俺も形式どおりに\x01",
            "挨拶するのが精一杯だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_407F")

    Jump("loc_496F")

    label("loc_4084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_41C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4157")

    #C0216
    ChrTalk(
        0xFE,
        (
            "警察官になって一番辛いのは\x01",
            "市民からの苦情だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "真面目に勤務していても\x01",
            "犯罪は起こるものだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "市民を守りたくても\x01",
            "どうしようもない事も多いんだよな。\x01",
            "ふう、心苦しいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_41BB")

    label("loc_4157")


    #C0219
    ChrTalk(
        0xFE,
        (
            "警察官ってのも\x01",
            "結構制約が多いんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "正義感だけじゃ務まらない事が\x01",
            "多くて、心苦しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41BB")

    Jump("loc_496F")

    label("loc_41C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_449D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4347")

    #C0221
    ChrTalk(
        0xFE,
        (
            "やあロイドたちか。\x01",
            "お仕事ご苦労様！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0000Fフランツ、最近調子はどうなんだ？\x01",
            "勉強の時間が取れないって\x01",
            "言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "はは、捜査官試験のことか？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "ご覧の通り、今は\x01",
            "通常勤務優先でやってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "もちろん捜査官になることも\x01",
            "諦めちゃいないけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#0003F大変そうだな……\x01",
            "あんま無理すんなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "任せとけ。\x01",
            "……ロイド、そっちこそ\x01",
            "しっかりな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x91, 1)
    Jump("loc_4498")

    label("loc_4347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4409")

    #C0228
    ChrTalk(
        0xFE,
        (
            "そういやロイド達って……\x01",
            "時々受付の人と話してるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "レベッカさん、だっけ……\x01",
            "すげー美人だよな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0230
    ChrTalk(
        0xFE,
        (
            "ああ、いや、\x01",
            "別に他意はないんだけどさ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4498")

    label("loc_4409")


    #C0231
    ChrTalk(
        0xFE,
        (
            "受付のレベッカさんって\x01",
            "すげー美人だよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "フランさんも可愛いけど\x01",
            "オレはやっぱレベッカさんが……\x01",
            "……って、変なこと言わせるなよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4498")

    Jump("loc_496F")

    label("loc_449D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451A")

    #C0233
    ChrTalk(
        0xFE,
        "任務ご苦労様であります！\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "さっき捜査一課の人が\x01",
            "出かけて行ったよ。\x01",
            "ふう、緊張するな～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4591")

    label("loc_451A")


    #C0235
    ChrTalk(
        0xFE,
        (
            "やっぱ捜査一課の人は\x01",
            "かっこいいよな。\x01",
            "ぴしっとした捜査官ばかりでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "……オレも早く\x01",
            "捜査官資格を取りたいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4591")

    Jump("loc_496F")

    label("loc_4596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_46D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4670")

    #C0237
    ChrTalk(
        0xFE,
        (
            "市内の巡回担当、オレはここの\x01",
            "警備を選ぶことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "地味な仕事に見えるけど\x01",
            "結構捜査官の人も行き来するからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "オレ捜査官資格目指してるし……\x01",
            "ほら、色々参考になりそうだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_46D4")

    label("loc_4670")


    #C0240
    ChrTalk(
        0xFE,
        (
            "ここにいると、捜査官の人の\x01",
            "仕事振りとかも見れるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "うーん、やっぱ\x01",
            "捜査官には憧れるぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D4")

    Jump("loc_496F")

    label("loc_46D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_46E7")
    Jump("loc_496F")

    label("loc_46E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_48EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_478D")

    #C0242
    ChrTalk(
        0xFE,
        (
            "（ところで……あの２人、\x01",
            "  捜査一課の人らしいぜ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "（な、何か見るからに\x01",
            "  優秀って感じだよな。\x01",
            "  近くにいるだけで緊張するぅ～……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E7")

    label("loc_478D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_4828")

    #C0244
    ChrTalk(
        0xFE,
        (
            "（……あの２人ってさ、\x01",
            "  捜査一課の人らしいぜ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "（な、何か見るからに\x01",
            "  優秀って感じだよな。\x01",
            "  近くにいるだけで緊張するぅ～……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E7")

    label("loc_4828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488F")

    #C0246
    ChrTalk(
        0xFE,
        "任務ご苦労様であります！\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "……オレも今日が初仕事なんだ。\x01",
            "ふう、緊張するぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_48E7")

    label("loc_488F")


    #C0248
    ChrTalk(
        0xFE,
        (
            "なんの、これも\x01",
            "捜査官になるため……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "どんな仕事でも\x01",
            "手を抜いちゃいけないよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E7")

    Jump("loc_496F")

    label("loc_48EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_496F")

    #C0250
    ChrTalk(
        0xFE,
        (
            "オレの目標は捜査一課だからな。\x01",
            "その内捜査官資格を取るつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "やっぱり捜査一課は\x01",
            "みんなの憧れだもんな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496F")

    TalkEnd(0xFE)
    Return()

    # Function_9_3705 end

    def Function_10_4973(): pass

    label("Function_10_4973")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4988")
    Call(0, 11)
    Jump("loc_49D5")

    label("loc_4988")


    #C0252
    ChrTalk(
        0xFE,
        (
            "#0603Fフン……\x01",
            "お前達には関係のない話だ。\x02\x03",

            "#0600Fさっさと消えるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D5")

    TalkEnd(0xFE)
    Return()

    # Function_10_4973 end

    def Function_11_49D9(): pass

    label("Function_11_49D9")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0xD, 0x5A, 0x0)

    #C0253
    ChrTalk(
        0xC,
        (
            "#0603Fああ、私はこれから\x01",
            "共和国方面に問い合わせてみる。\x02\x03",

            "#0603Fエマ君、そちらの調査は頼むぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xD,
        (
            "ええ、すぐに\x01",
            "Ｋ監視班と合流します。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_11_49D9 end

    def Function_12_4A8A(): pass

    label("Function_12_4A8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9F")
    Call(0, 11)
    Jump("loc_4B9A")

    label("loc_4A9F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0255
    ChrTalk(
        0xFE,
        "特務支援課……\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "……捜査の邪魔をしないで下さい。\x01",
            "あなた方はただのお荷物ですから。\x02",
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
        "#0006F（何か酷い言われようだ……）\x02",
    )

    CloseMessageWindow()

    label("loc_4B9A")

    TalkEnd(0xFE)
    Return()

    # Function_12_4A8A end

    def Function_13_4B9E(): pass

    label("Function_13_4B9E")

    TalkBegin(0xFE)

    #C0258
    ChrTalk(
        0xFE,
        "あら、おはようございます。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        "今日もいいお天気ですね。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_4B9E end

    def Function_14_4BE3(): pass

    label("Function_14_4BE3")

    TalkBegin(0xFE)

    #C0260
    ChrTalk(
        0xFE,
        (
            "今日もママと\x01",
            "としょかんに行くんだ～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_4BE3 end

    def Function_15_4C15(): pass

    label("Function_15_4C15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4CBE")

    #C0261
    ChrTalk(
        0xFE,
        (
            "今日は暴行事件と当て逃げ犯、\x01",
            "あとボッタクリの捜査があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "とっとと片付けねえと\x01",
            "日が暮れちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        "#0000F捜査二課もお忙しそうですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_501D")

    label("loc_4CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_501D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECE")

    #C0264
    ChrTalk(
        0xFE,
        (
            "……すぱー…………\x01",
            "一課に事件を取られたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        "……ま、仕方ねえだろ。\x02",
    )


    #C0266
    ChrTalk(
        0xFE,
        (
            "一課の領分に\x01",
            "ちょっかいが出せただけ\x01",
            "良かったんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#0012Fはは……やっぱり\x01",
            "そんなものですかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "ああ、さすが\x01",
            "セルゲイの申し子っつーか……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        "ま、睨まれねえ程度にな。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "あまり目立つと、また\x01",
            "副局長辺りがお小言の準備を\x01",
            "してそうな気がするぜ。\x02",
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
        "#0200Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        "#0306Fぞっとしねえなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_501D")

    label("loc_4ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F90")

    #C0273
    ChrTalk(
        0xFE,
        (
            "一課の領分に\x01",
            "ちょっかいを出すなんざ……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "セルゲイの申し子っつーか、\x01",
            "ま、お前の場合は\x01",
            "あいつ譲りかもなぁ。\x02",
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
            "まあ、副局長殿に\x01",
            "睨まれねえ程度にな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_501D")

    label("loc_4F90")


    #C0277
    ChrTalk(
        0xFE,
        (
            "……すぱー…………\x01",
            "にしても、レイモンドの奴は\x01",
            "何をぐずぐずしてやがるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "聞き込みに行く前にタバコを\x01",
            "吸い尽くしちまうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501D")

    TalkEnd(0xFE)
    Return()

    # Function_15_4C15 end

    def Function_16_5021(): pass

    label("Function_16_5021")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B0")

    #C0279
    ChrTalk(
        0xFE,
        (
            "記念祭はカノジョと\x01",
            "遊びに行きたいよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "ミシュラムでバカンスを\x01",
            "楽しんだりしてさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        "……まあ無理だけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_50F2")

    label("loc_50B0")


    #C0282
    ChrTalk(
        0xFE,
        (
            "とほほ……\x01",
            "捜査官に記念祭中の休みなんて\x01",
            "あるわけないよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50F2")

    TalkEnd(0xFE)
    Return()

    # Function_16_5021 end

    def Function_17_50F6(): pass

    label("Function_17_50F6")

    EventBegin(0x0)
    Fade(500)
    OP_68(7330, 3500, -6700, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17970, 0)
    SetChrPos(0x101, 6820, 2390, -5850, 270)
    SetChrPos(0x153, 8100, 2390, -5930, 225)
    BeginChrThread(0x101, 1, 0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5186")
    SetChrPos(0x102, 8160, 2390, -7190, 180)
    BeginChrThread(0x102, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x102, 0x1)
    Jump("loc_51E7")

    label("loc_5186")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51B9")
    SetChrPos(0x103, 8160, 2390, -7190, 180)
    BeginChrThread(0x103, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x103, 0x1)
    Jump("loc_51E7")

    label("loc_51B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51E7")
    SetChrPos(0x104, 8160, 2390, -7190, 180)
    BeginChrThread(0x104, 1, 0, 19)
    Sleep(2000)
    EndChrThread(0x104, 0x1)

    label("loc_51E7")

    EndChrThread(0x101, 0x1)
    OP_0D()

    #C0283
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあれ……おかしいな。\x02\x03",

            "噴水広場のジューススタンドって\x01",
            "このあたりだったよな？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52BD")
    TurnDirection(0x102, 0x101, 500)

    #C0284
    ChrTalk(
        0x102,
        (
            "#12P#0105Fええ、そうだと思ったけど……\x02\x03",

            "#0103Fひょっとして\x01",
            "どこかに移動したのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AA")

    label("loc_52BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5332")
    TurnDirection(0x103, 0x101, 500)

    #C0285
    ChrTalk(
        0x103,
        (
            "#12P#0203Fええ、そう記憶しています。\x02\x03",

            "#0200Fどこかに移動した\x01",
            "可能性が高そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53AA")

    label("loc_5332")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53AA")
    TurnDirection(0x104, 0x101, 500)

    #C0286
    ChrTalk(
        0x104,
        (
            "#12P#0303Fおお、前にデートで\x01",
            "立ち寄ったから間違いねぇ。\x02\x03",

            "#0301Fどこかに移動しちまったのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53AA")

    TurnDirection(0x153, 0x101, 500)

    #C0287
    ChrTalk(
        0x153,
        (
            "#11P#1112Fえー、それじゃあ\x01",
            "おじいちゃんにさしいれ\x01",
            "できないのー？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    #C0288
    ChrTalk(
        0x101,
        (
            "#5P#0003Fいや、たぶん街の外には\x01",
            "移動してないだろうし……\x02\x03",

            "#0000Fせっかくだから\x01",
            "市内を探してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x153,
        "#11P#1100Fうんっ！\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 8100, 2390, -5930, 225)
    OP_29(0x26, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_17_50F6 end

    def Function_18_549E(): pass

    label("Function_18_549E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54C2")
    OP_93(0xFE, 0x0, 0x226)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x226)
    Sleep(500)
    Jump("Function_18_549E")

    label("loc_54C2")

    Return()

    # Function_18_549E end

    def Function_19_54C3(): pass

    label("Function_19_54C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54E7")
    OP_93(0xFE, 0xB4, 0x258)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x258)
    Sleep(500)
    Jump("Function_19_54C3")

    label("loc_54E7")

    Return()

    # Function_19_54C3 end

    def Function_20_54E8(): pass

    label("Function_20_54E8")

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
            "#0103Fクロスベル市庁舎に\x01",
            "警察本部、市立図書館……\x02\x03",

            "#0100Fお役所の建物が\x01",
            "集まっている官公庁街ね。\x02",
        )
    )

    CloseMessageWindow()

    #A0291
    AnonymousTalk(
        0x103,
        (
            "#0202Fのどかな所ですね。\x01",
            "噴水にベンチまでありますし。\x02",
        )
    )

    CloseMessageWindow()

    #A0292
    AnonymousTalk(
        0x102,
        (
            "#0104F市内でも一等地なんだけど……\x01",
            "日中はいつもこんな感じなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #A0293
    AnonymousTalk(
        0x101,
        (
            "#0000Fまあ警察本部があるし、\x01",
            "これから何度も訪れると思う。\x02\x03",

            "支援課からの道順は\x01",
            "しっかり覚えておこう。\x02",
        )
    )

    CloseMessageWindow()

    #A0294
    AnonymousTalk(
        0x104,
        (
            "#0304F了解、リーダー。\x02\x03",

            "#0300F本部には『支援要請』とやらでも\x01",
            "呼び出されてたんだったか。\x01",
            "ついでに顔を出してもいいかもな。\x02",
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
            "行政区は、街の北側にある官公庁街です。\x02",
        )
    )

    CloseMessageWindow()

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "重要な施設である警察本部が存在し、\x01",
            "訪れる機会も多いでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #A0297
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル市庁舎があるほか、\x01",
            "市立図書館では、世界観を紹介した\x01",
            "用語辞典を閲覧する事ができます。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594F")
    OP_68(19940, 2240, -37920, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    Jump("loc_598B")

    label("loc_594F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_598B")
    OP_68(-40390, 2240, 24150, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)

    label("loc_598B")

    SetScenarioFlags(0x45, 3)
    EventEnd(0x5)
    Return()

    # Function_20_54E8 end

    def Function_21_5991(): pass

    label("Function_21_5991")

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

    def lambda_59F7():
        OP_95(0xFE, -18500, 2500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59F7)
    OP_68(-18500, 3600, 25000, 7000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_68(-18500, 4300, 27000, 2500)
    MoveCamera(44, 3, 0, 2500)
    OP_6F(0x41)
    Sleep(1000)

    def lambda_5A5A():
        OP_95(0xFE, -18500, 2500, 28400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A5A)
    WaitChrThread(0x101, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_5A8D():
        OP_95(0xFE, -18500, 3100, 31400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A8D)
    Sleep(500)

    def lambda_5AAA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AAA)
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

    # Function_21_5991 end

    def Function_22_5AEF(): pass

    label("Function_22_5AEF")

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

    # Function_22_5AEF end

    def Function_23_5B77(): pass

    label("Function_23_5B77")

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

    def lambda_5C5C():
        OP_9D(0xFE, 0x61A8, 0x3B60, 0x1770, 0xFA0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C5C)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)

    def lambda_5C92():
        OP_95(0xFE, 25000, 15200, 19900, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5C92)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    OP_93(0x12, 0x13B, 0x0)
    SetChrSubChip(0x12, 0x0)

    def lambda_5CC6():
        OP_9D(0xFE, 0x4E20, 0x4074, 0x6144, 0x8FC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5CC6)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_5CF8():
        OP_9D(0xFE, 0x3A98, 0x3B60, 0x74CC, 0x514, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5CF8)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)

    def lambda_5D2E():
        OP_95(0xFE, 2500, 15200, 29900, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D2E)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    ClearChrFlags(0x12, 0x1)
    SetChrSubChip(0x12, 0x0)

    def lambda_5D60():
        OP_9D(0xFE, 0xFFFFFE0C, 0x4268, 0x74CC, 0x8FC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D60)
    Sound(814, 0, 70, 0)
    WaitChrThread(0x12, 1)

    def lambda_5D87():
        OP_9D(0xFE, 0xFFFFD6FC, 0x4268, 0x74CC, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D87)
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

    def lambda_5E22():
        OP_9D(0xFE, 0xFFFF9B38, 0x34BC, 0x9088, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E22)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x12, 1)
    PlayEffect(0x0, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x12, 0x1)
    Sound(31, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_5E91():
        OP_9D(0xFE, 0xFFFF7EB4, 0x251C, 0x9088, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5E91)
    Sound(854, 0, 100, 0)
    WaitChrThread(0x12, 1)
    PlayEffect(0x0, 0xFF, 0x12, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    Sound(31, 0, 100, 0)
    Sound(42, 0, 100, 0)

    def lambda_5F0A():
        OP_95(0xFE, -41700, 9500, 37000, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F0A)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_5F37():
        OP_9D(0xFE, 0xFFFF360C, 0x251C, 0x9088, 0x76C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F37)
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

    # Function_23_5B77 end

    def Function_24_5F85(): pass

    label("Function_24_5F85")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　※　新市庁舎ビル建設中　※\x01",
            "工事関係者以外、立ち入りを禁ずる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_5F85 end

    SaveToFile()

Try(main)
