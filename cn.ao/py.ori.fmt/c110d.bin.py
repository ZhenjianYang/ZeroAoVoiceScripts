from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c110d.bin",                # FileName
        "c110d",                    # MapName
        "c110d",                    # Location
        0x0016,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c110d",                  # 0
        "库罗玛",                 # 1
        "奥特",                   # 2
        "哈斯",                   # 3
        "市民",                   # 4
        "男孩",                   # 5
        "市民",                   # 6
        "市民",                   # 7
        "警官",                   # 8
        "车",                     # 9
        "国防军士兵",             # 10
        "国防军士兵",             # 11
        "市民１",                 # 12
        "市民２",                 # 13
        "市民３",                 # 14
        "市民４",                 # 15
        "市民５",                 # 16
        "市民６",                 # 17
        "市民７",                 # 18
        "市民８",                 # 19
        "中央广场",               # 20
        "西街",                   # 21
        "行政区",                 # 22
        "住宅街",                 # 23
        "欢乐街",                 # 24
        "东街",                   # 25
        "旧城区",                 # 26
        "港湾区",                 # 27
        "ＩＢＣ",                 # 28
        "站前街道",               # 29
        "后巷",                   # 30
        "乌尔斯拉间道",           # 31
        "东克洛斯贝尔街道",       # 32
        "西克洛斯贝尔街道",       # 33
        "玛因兹山道",             # 34
        "兰花塔",                 # 35
    ))

    AddCharChip((
        "chr/ch24900.itc",                   # 00
        "chr/ch20800.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch30000.itc",                   # 03
        "chr/ch21000.itc",                   # 04
        "chr/ch23800.itc",                   # 05
        "chr/ch20400.itc",                   # 06
        "chr/ch21300.itc",                   # 07
    ))

    DeclNpc(6929,    2490,    -6650,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(8369,    2390,    -14850,  90,   257,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(-8390,   2390,    9329,    225,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-16959,  2500,    -129,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-18559,  2500,    -219,    45,   385,  0x0, 0,   5,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(7389,    2500,    -8180,   135,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(8489,    2390,    -8680,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-15050,  2500,    27399,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclActor(16550,   2410,    10660,   1200,    16550,   3910,    10660,   0x007C, 0,  16, 0x0000)

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
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "兰花塔")
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

    ChipFrameInfo(1416, 0)                                       # 0

    ScpFunction((
        "Function_0_588",          # 00, 0
        "Function_1_638",          # 01, 1
        "Function_2_711",          # 02, 2
        "Function_3_73C",          # 03, 3
        "Function_4_A9B",          # 04, 4
        "Function_5_AF3",          # 05, 5
        "Function_6_D10",          # 06, 6
        "Function_7_E66",          # 07, 7
        "Function_8_F27",          # 08, 8
        "Function_9_113B",         # 09, 9
        "Function_10_122E",        # 0A, 10
        "Function_11_126A",        # 0B, 11
        "Function_12_1305",        # 0C, 12
        "Function_13_139D",        # 0D, 13
        "Function_14_1821",        # 0E, 14
        "Function_15_1B6B",        # 0F, 15
        "Function_16_1F97",        # 10, 16
    ))


    def Function_0_588(): pass

    label("Function_0_588")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
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

    # Function_0_588 end

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
    OP_94(0xFE, 0xFFFFB2BC, 0x8CA, 0xFFFFBAC8, 0xFFFFF204, 0x3E8)
    Sleep(300)
    Jump("Function_2_711")

    label("loc_73B")

    Return()

    # Function_2_711 end

    def Function_3_73C(): pass

    label("Function_3_73C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A22")
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
    Jump("loc_A22")

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
    Jump("loc_A22")

    label("loc_8CD")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_981")
    SetChrPos(0x0, -5400, 2500, 35000, 180)
    SetChrPos(0x1, -5400, 2500, 35000, 180)
    SetChrPos(0x2, -5400, 2500, 35000, 180)
    SetChrPos(0x3, -5400, 2500, 35000, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_954")
    SetChrPos(0x4, -5400, 2500, 35000, 180)
    SetChrPos(0x5, -5400, 2500, 35000, 180)
    Jump("loc_973")

    label("loc_954")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_973")
    SetChrPos(0x4, -5400, 2500, 35000, 180)

    label("loc_973")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A22")

    label("loc_981")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FA")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_A19")

    label("loc_9FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A19")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_A19")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A22")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, -11910, 2490, 8950, 45)
    SetChrPos(0xC, -12830, 2500, 9870, 45)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A8B")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Event(0, 13)
    Jump("loc_A9A")

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A9A")
    ClearScenarioFlags(0x22, 1)
    Event(0, 14)

    label("loc_A9A")

    Return()

    # Function_3_73C end

    def Function_4_A9B(): pass

    label("Function_4_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AB0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_AC4")
    OP_24(0x7B)
    ClearScenarioFlags(0x0, 5)
    Jump("loc_AE0")

    label("loc_AC4")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_AE0")

    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x5, 0x4)
    Return()

    # Function_4_A9B end

    def Function_5_AF3(): pass

    label("Function_5_AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1C")
    Call(0, 15)
    Return()

    label("loc_B1C")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B79")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B99")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D07")

    label("loc_B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAD")
    Jump("loc_D07")

    label("loc_BAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D07")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C35")

    #C0001
    ChrTalk(
        0x8,
        (
            "只要放入那种苦西红柿酱，\x01",
            "一定可以煮出\x01",
            "很棒的赈济餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "习惯它的味道之后，\x01",
            "一定会上瘾的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D07")

    label("loc_C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAF")

    #C0003
    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "要不要尝尝部分人士\x01",
            "很喜欢的『苦西红柿苏打』？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "喝了这个之后，\x01",
            "肯定会精神百倍！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D07")

    label("loc_CAF")


    #C0006
    ChrTalk(
        0xFE,
        (
            "要不要尝尝部分人士\x01",
            "很喜欢的『苦西红柿苏打』？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "喝了这个之后，\x01",
            "肯定会精神百倍！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D07")

    Jump("loc_B29")

    label("loc_D0C")

    TalkEnd(0xFE)
    Return()

    # Function_5_AF3 end

    def Function_6_D10(): pass

    label("Function_6_D10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")

    #C0008
    ChrTalk(
        0xFE,
        (
            "当时的惨状，直到如今依然历历在目……\x01",
            "伊莉娅小姐竟然会……！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "可恶……武装集团真是不可饶恕！\x01",
            "帝国政府也同样不可饶恕！！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "事已至此，我们也只有坚决独立，\x01",
            "抗战到底这一条出路了……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E62")

    label("loc_DE4")


    #C0011
    ChrTalk(
        0xFE,
        (
            "可恶……武装集团真是不可饶恕！\x01",
            "帝国政府也同样不可饶恕！！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "事已至此，我们也只有坚决独立，\x01",
            "抗战到底这一条出路了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E62")

    TalkEnd(0xFE)
    Return()

    # Function_6_D10 end

    def Function_7_E66(): pass

    label("Function_7_E66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECA")

    #C0013
    ChrTalk(
        0xFE,
        "你好，要来个气球吗～？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "想要两个或三个也可以，\x01",
            "今天想拿几个就拿几个。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F23")

    label("loc_ECA")


    #C0015
    ChrTalk(
        0xFE,
        (
            "今天下午的活动\x01",
            "还包括把气球\x01",
            "做成各种样子的教学哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "如果有兴趣，\x01",
            "请一定要参加～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F23")

    TalkEnd(0xFE)
    Return()

    # Function_7_E66 end

    def Function_8_F27(): pass

    label("Function_8_F27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D9")

    #C0017
    ChrTalk(
        0xFE,
        "哦，是支援科的各位啊。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00000F嗯，你辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        "#00100F总部还没有修整完毕吧？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "嗯，已经大致收拾过一遍了，\x01",
            "但还没有完全恢复……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "入口大厅的受损状况\x01",
            "非常严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "要想恢复接待处的职能，\x01",
            "恐怕还需要一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "顺便一说，接待方面的\x01",
            "事务暂时转移到\x01",
            "警察学校了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "瑞贝卡小姐也在那边，\x01",
            "如果各位在工作中有什么事务\x01",
            "需要处理，可以过去找她。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00002F原来如此，知道了。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#00200F多谢告知。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_1137")

    label("loc_10D9")


    #C0027
    ChrTalk(
        0xFE,
        (
            "总部还要再过一段时间\x01",
            "才能修整完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "如果各位有什么事务需要处理，\x01",
            "可以去警察学校哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1137")

    TalkEnd(0xFE)
    Return()

    # Function_8_F27 end

    def Function_9_113B(): pass

    label("Function_9_113B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A7")

    #C0029
    ChrTalk(
        0xFE,
        (
            "你也听说了吧？\x01",
            "之前那起袭击事件\x01",
            "好像是帝国策动的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "我绝对不会\x01",
            "原谅帝国。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_122A")

    label("loc_11A7")


    #C0031
    ChrTalk(
        0xFE,
        (
            "通过这次的事情，我终于明白了。\x01",
            "就算我们对帝国唯命是从，\x01",
            "他们也丝毫没想过要保护我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "所以我们只能将独立之路\x01",
            "贯彻到底。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122A")

    TalkEnd(0xFE)
    Return()

    # Function_9_113B end

    def Function_10_122E(): pass

    label("Function_10_122E")

    TalkBegin(0xFE)

    #C0033
    ChrTalk(
        0xFE,
        (
            "对大家做出这么过分的事情……\x01",
            "帝国真是太可恶了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_122E end

    def Function_11_126A(): pass

    label("Function_11_126A")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "市民会馆内正在\x01",
            "举行慈善宴会，\x01",
            "宴会中有很多有趣的活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "最重要的是，\x01",
            "这种通过娱乐活动使大家重振精神，\x01",
            "从而使城市复兴的创意真是太高明了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_126A end

    def Function_12_1305(): pass

    label("Function_12_1305")

    TalkBegin(0xFE)

    #C0036
    ChrTalk(
        0xFE,
        (
            "这项活动好像是由\x01",
            "克洛斯贝尔市工商协会策划的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "呵呵，工商协会的各位\x01",
            "真是很懂得如何激发大家的热情呢，\x01",
            "在每年创立纪念庆典的时候也是如此。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1305 end

    def Function_13_139D(): pass

    label("Function_13_139D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xB, -11910, 2490, 8950, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -12830, 2500, 9870, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    UseItem(0x2E7, 0xFF)
    AddItemNumber('克洛斯贝尔时代周刊⑦', 1)
    Sleep(500)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "克洛斯贝尔市惨遭『赤色星座』\x01",
            "蹂躏的一周之后──\x02\x03",

            "ＩＢＣ大楼遭到爆破一事\x01",
            "使周边诸国的气氛一下子紧张起来。\x02\x03",

            "为了应对这种局面，\x01",
            "玛丽亚贝尔代理总裁在兰花塔利用\x01",
            "备份数据，迅速恢复了顾客资料……\x02\x03",

            "万全的应对措施使周边诸国的\x01",
            "慌乱情绪渐渐平复。\x02\x03",

            "但猎兵给克洛斯贝尔造成了极深的创伤，\x01",
            "很多市民直到如今还茫然失措。\x02\x03",

            "大明星伊莉娅·普拉提耶\x01",
            "身受重伤而生命垂危的消息\x01",
            "更是对国内外造成了极大的冲击……\x02\x03",

            "此外，警察总部遭受袭击的事件，\x01",
            "以及始终没能掌握『赤色星座』行踪的情况\x01",
            "令众多市民身处在一股难以名状的不安之中。\x02\x03",

            "正当『雇佣赤色星座的幕后黑手\x01",
            "为埃雷波尼亚帝国』这个传闻\x01",
            "开始在市民间广为流传之时……\x02\x03",

            "以调查大家的独立意向为目的，\x01",
            "但却因袭击事件而延期的居民投票活动\x01",
            "定于三日之后举行。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7563", 0)
    OP_68(-17800, 5250, 30550, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    MoveCamera(30, 20, 0, 6000)
    SetCameraDistance(17500, 6000)
    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(6500, 5000, -11300, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    OP_68(-12000, 5000, 6650, 8000)
    MoveCamera(40, 15, 0, 8000)
    SetCameraDistance(14000, 0)
    Sleep(7000)
    StopSound(123, 1000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ReplaceBGM("ed7150", "ed7563")
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7117", "ed7563")
    ReplaceBGM("ed7111", "ed7563")
    SetScenarioFlags(0x22, 0)
    NewScene("c120D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_139D end

    def Function_14_1821(): pass

    label("Function_14_1821")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch24900.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch28100.itc", 0x22)
    LoadChrToIndex("chr/ch28000.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadChrToIndex("chr/ch20400.itc", 0x25)
    LoadChrToIndex("chr/ch21300.itc", 0x26)
    LoadChrToIndex("chr/ch20000.itc", 0x27)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x10, 0x80)
    OP_78(0x4, 0x10)
    OP_49()
    SetChrPos(0x10, 6200, 2500, 12300, 315)
    OP_D5(0x10, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_74(0x4, 0x1E)
    OP_70(0x4, 0x2)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 3850, 2500, 11750, 225)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7250, 2500, 8350, 225)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 4200, 2500, 6700, 45)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3000, 2500, 6900, 45)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 3000, 2500, 8500, 45)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 2400, 2500, 9200, 45)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2800, 2500, 4600, 0)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 4500, 2500, 4700, 0)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -200, 2500, 8000, 90)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 900, 2500, 6700, 45)
    OP_68(6700, 4000, 11200, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(5700, 3500, 10200, 10000)
    MoveCamera(45, 17, 0, 10000)
    SetCameraDistance(18000, 10000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("迪塔总统")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "突然发表这样的演说，\x01",
            "想必会使不少居民震惊。\x02\x03",

            "但一场前所未有的严重危机\x01",
            "正在威胁着克洛斯贝尔。\x02\x03",

            "而威胁我们的，\x01",
            "正是那践踏正义、\x01",
            "剥夺我们尊严的邪恶意志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1821 end

    def Function_15_1B6B(): pass

    label("Function_15_1B6B")

    EventBegin(0x0)
    EventBegin(0x0)
    Fade(500)
    OP_68(4610, 4500, -7760, 0)
    MoveCamera(88, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11540, 0)
    SetChrPos(0x101, 6140, 2500, -8020, 45)
    SetChrPos(0x102, 5350, 2500, -7210, 45)
    SetChrPos(0x103, 5330, 2500, -8820, 45)
    SetChrPos(0x109, 4540, 2500, -8000, 45)
    SetChrPos(0x105, 4520, 2500, -9610, 45)
    SetChrPos(0x104, 3740, 2500, -8790, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0040
    ChrTalk(
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "要不要尝尝部分人士\x01",
            "很喜欢的『苦西红柿苏打』？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "喝了这个之后，\x01",
            "肯定会精神百倍！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00000F（坦特斯老先生\x01",
            "  所说的那种富含苦西红柿\x01",
            "  成分的浓缩物……）\x02\x03",

            "（能否在这里买到呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "客人，您想好要点什么了吗？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00002F那个……其实有件事情\x01",
            "想问问您……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向对方说明了事由。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    #C0047
    ChrTalk(
        0x8,
        (
            "原来如此，那就把\x01",
            "这个拿去如何？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿酱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('苦西红柿酱', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0049
    ChrTalk(
        0x102,
        "#00105F这是……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "哦，这是本店使用的酱料，\x01",
            "用苦西红柿熬制\x01",
            "而成的浓缩品。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "它有营养滋补、\x01",
            "强身健体的功效。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "加上这种苦西红柿酱，\x01",
            "一定可以煮出很棒的赈济餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00000F真是太好了，\x01",
            "请问价钱是……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "哦，不用付钱了。\x01",
            "各位正在为\x01",
            "重建工作帮忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "既然如此，请不必客气，\x01",
            "直接拿去就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00002F那可真是太不好意思了。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00102F非常感谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 5)
    SetScenarioFlags(0x0, 6)
    OP_29(0x8E, 0x1, 0x4)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5330, 2500, -8020, 56)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_15_1B6B end

    def Function_16_1F97(): pass

    label("Function_16_1F97")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FA8")
    Jump("loc_220B")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_220B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 慈善宴会　　　　　　　　　　　 \x01",
            " 　『～同心协力，共建复兴之轮～』　　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【活动概要】　　　　　　　　　　 \x01",
            " 　·钢琴独奏表演　　　　　　　　 \x01",
            " 　·克洛斯贝尔职业女性竞选活动\x01",
            " 　·大众美食竞赛\x01",
            " 　·各种才艺教学\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " 举办场所：克洛斯贝尔市民会馆·多功能大厅\x01",
            " 　　　　　会馆前的广场　　　　　　　　　　　 \x01",
            " 举办日期：今日　　　　　　　　　　　　　　 \x01",
            " 举办方 ：克洛斯贝尔工商协会／克洛斯贝尔市政府\x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " ※参加各种活动的费用\x01",
            " 　将全部以援助资金的形式投入复兴计划。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_220B")

    TalkEnd(0xFF)
    Return()

    # Function_16_1F97 end

    SaveToFile()

Try(main)
