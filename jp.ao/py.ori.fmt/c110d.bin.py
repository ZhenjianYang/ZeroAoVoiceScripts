from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "クロマ",                 # 1
        "オットー",               # 2
        "ハース",                 # 3
        "市民",                   # 4
        "男の子",                 # 5
        "市民",                   # 6
        "市民",                   # 7
        "警官",                   # 8
        "車",                     # 9
        "国防軍兵士",             # 10
        "国防軍兵士",             # 11
        "市民１",                 # 12
        "市民２",                 # 13
        "市民３",                 # 14
        "市民４",                 # 15
        "市民５",                 # 16
        "市民６",                 # 17
        "市民７",                 # 18
        "市民８",                 # 19
        "中央広場",               # 20
        "西通り",                 # 21
        "行政区",                 # 22
        "住宅街",                 # 23
        "歓楽街",                 # 24
        "東通り",                 # 25
        "旧市街",                 # 26
        "港湾区",                 # 27
        "ＩＢＣ",                 # 28
        "駅前通り",               # 29
        "裏通り",                 # 30
        "ウルスラ間道",           # 31
        "東クロスベル街道",       # 32
        "西クロスベル街道",       # 33
        "マインツ山道",           # 34
        "オルキスタワー",         # 35
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
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_6_D80",          # 06, 6
        "Function_7_EF6",          # 07, 7
        "Function_8_FE9",          # 08, 8
        "Function_9_1283",         # 09, 9
        "Function_10_13B4",        # 0A, 10
        "Function_11_13FC",        # 0B, 11
        "Function_12_14AF",        # 0C, 12
        "Function_13_1549",        # 0D, 13
        "Function_14_1A2F",        # 0E, 14
        "Function_15_1DAB",        # 0F, 15
        "Function_16_2279",        # 10, 16
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B87")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA7")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D77")

    label("loc_BA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBB")
    Jump("loc_D77")

    label("loc_BBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C5F")

    #C0001
    ChrTalk(
        0x8,
        (
            "そのペーストがあれば、\x01",
            "きっと素晴らしい\x01",
            "炊き出しになると思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ちょっとクセが出ちゃうのは\x01",
            "ご愛嬌ですけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D77")

    label("loc_C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")

    #C0003
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "一部の方には大人気、\x01",
            "『にがトマトソーダ』はいかがですかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "皆さんもこれを飲んで\x01",
            "元気を出していきましょう！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D77")

    label("loc_D01")


    #C0006
    ChrTalk(
        0xFE,
        (
            "一部の方には大人気、\x01",
            "『にがトマトソーダ』はいかがですかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "皆さんもこれを飲んで\x01",
            "元気を出していきましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D77")

    Jump("loc_B29")

    label("loc_D7C")

    TalkEnd(0xFE)
    Return()

    # Function_5_AF3 end

    def Function_6_D80(): pass

    label("Function_6_D80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E68")

    #C0008
    ChrTalk(
        0xFE,
        (
            "今も目に焼きついて離れん……\x01",
            "まさか、イリア様があのような形で……！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "うむむ……許すまじ武装集団っ！\x01",
            "そして許すまじ、帝国政府っっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "こうなれば、我々は断固独立して\x01",
            "徹底抗戦するしかあるまいっ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EF2")

    label("loc_E68")


    #C0011
    ChrTalk(
        0xFE,
        (
            "うむむ……許すまじ武装集団っ！\x01",
            "そして許すまじ、帝国政府っっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "こうなれば、我々は断固独立して\x01",
            "徹底抗戦するしかあるまいっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    TalkEnd(0xFE)
    Return()

    # Function_6_D80 end

    def Function_7_EF6(): pass

    label("Function_7_EF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F72")

    #C0013
    ChrTalk(
        0xFE,
        "さあさあ、風船はいかが～？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "１個でも２個でも３個でも、\x01",
            "今日はいくらでも持って行ってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_FE5")

    label("loc_F72")


    #C0015
    ChrTalk(
        0xFE,
        (
            "午後からは\x01",
            "バルーンアート教室ってのも\x01",
            "開催予定で～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "興味のある方はぜひぜひ\x01",
            "ふるってご参加くださ～い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE5")

    TalkEnd(0xFE)
    Return()

    # Function_7_EF6 end

    def Function_8_FE9(): pass

    label("Function_8_FE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1211")

    #C0017
    ChrTalk(
        0xFE,
        "おや、支援課の皆さんですね。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00000Fええ、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        "#00100F本部はまだ復旧中なんですね？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "ええ、とりあえず一通り\x01",
            "片付けた状態ではありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "とにかく、エントランスの\x01",
            "被害がひどい状況でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "受付の機能を回復させるには、\x01",
            "まだしばらく時間がかかります。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "ちなみに、受付に関する\x01",
            "事務作業は一時的に警察学校で\x01",
            "行うことになりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "レベッカさんもいるし、\x01",
            "何か仕事関連の事務処理があれば\x01",
            "そちらで対応できるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#00002Fなるほど、了解です。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x103,
        "#00200Fどうも、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_127F")

    label("loc_1211")


    #C0027
    ChrTalk(
        0xFE,
        (
            "本部が復旧するまで\x01",
            "まだしばらくかかります。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "何か事務処理があれば、\x01",
            "警察学校の方へ行くといいですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127F")

    TalkEnd(0xFE)
    Return()

    # Function_8_FE9 end

    def Function_9_1283(): pass

    label("Function_9_1283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130F")

    #C0029
    ChrTalk(
        0xFE,
        (
            "君も聞いたかい？\x01",
            "どうやらこの間の襲撃事件は\x01",
            "帝国の陰謀だったらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "僕は本当に\x01",
            "帝国という国が許せないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_13B0")

    label("loc_130F")


    #C0031
    ChrTalk(
        0xFE,
        (
            "でも今回のことでよく分かったよ。\x01",
            "例え帝国に従った所で彼らは\x01",
            "僕らを守るつもりなんて毛頭ない……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "だからこそ、僕らは独立の意志を\x01",
            "押し通すしかないってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1283 end

    def Function_10_13B4(): pass

    label("Function_10_13B4")

    TalkBegin(0xFE)

    #C0033
    ChrTalk(
        0xFE,
        (
            "みんなにひどいことをして……\x01",
            "ていこくってわるいヤツだよね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_13B4 end

    def Function_11_13FC(): pass

    label("Function_11_13FC")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "今、市民会館でやってる\x01",
            "チャリティイベントだけど、\x01",
            "ほんと色んな催しがあって楽しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "それに何より、こうやって\x01",
            "楽しむことが復興につながるって\x01",
            "発想が素晴らしいよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_13FC end

    def Function_12_14AF(): pass

    label("Function_12_14AF")

    TalkBegin(0xFE)

    #C0036
    ChrTalk(
        0xFE,
        (
            "このイベントの企画者は\x01",
            "クロスベル商工会なんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "ふふ、毎年記念祭の時にも\x01",
            "思うけど、商工会の人たちって\x01",
            "盛り上げ上手でパワフルよね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_14AF end

    def Function_13_1549(): pass

    label("Function_13_1549")

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
    AddItemNumber(0x2E7, 1)
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
            "《赤い星座》による\x01",
            "クロスベル市蹂躙#4Rじゅうりん#から１週間後──\x02\x03",

            "ＩＢＣビルが爆破されたことで\x01",
            "周辺諸国の緊張は一気に高まった。\x02\x03",

            "これに対し、マリアベル総裁代行は\x01",
            "オルキスタワーにバックアップしていた\x01",
            "顧客データなどを速やかに復活させ……\x02\x03",

            "万全の対応を見せることで\x01",
            "周辺諸国の動揺は収まりつつあった。\x02\x03",

            "──しかし猟兵が残した爪痕は深く、\x01",
            "多くの市民はいまだ呆然としていた。\x02\x03",

            "中でも大スター、イリア・プラティエが\x01",
            "瀕死の重傷を負ったというニュースは\x01",
            "国内外にも大きな衝撃を与え……\x02\x03",

            "さらに警察本部が襲われた事実と\x01",
            "《赤い星座》の行方が掴めないことが\x01",
            "市民を言い知れぬ不安に陥れていた。\x02\x03",

            "そして──《赤い星座》の背後に\x01",
            "エレボニア帝国がいたという噂が\x01",
            "市民の間でも囁かれ始めた頃……\x02\x03",

            "事件のために延期されていた\x01",
            "『国家独立』の是非を問う住民投票が\x01",
            "３日後、開催される運びとなった。\x07\x00\x02",
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

    # Function_13_1549 end

    def Function_14_1A2F(): pass

    label("Function_14_1A2F")

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
    SetChrName("ディーター大統領")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──突然の発表で\x01",
            "驚かれた方も多いでしょう。\x02\x03",

            "ですが現在、クロスベルに\x01",
            "未曾有#6Rみ　ぞ　う#の危機が迫っています。\x02\x03",

            "正義を踏みにじり、\x01",
            "我々の尊厳を奪い取ろうとする\x01",
            "邪悪な意志が迫っているのです。\x02",
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

    # Function_14_1A2F end

    def Function_15_1DAB(): pass

    label("Function_15_1DAB")

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
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "一部の方には大人気、\x01",
            "『にがトマトソーダ』はいかがですかー？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "皆さんもこれを飲んで\x01",
            "元気を出していきましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00000F（タントスさんが言っていた\x01",
            "  にがトマトの成分が\x01",
            "  凝縮されたエキス……）\x02\x03",

            "（ここなら手に入るかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "お客様、ご注文はお決まりですかー？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00002Fあの、実はちょっと\x01",
            "相談したいことがありまして……\x02",
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
            "ロイドは事情を話した。\x07\x00\x02",
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
            "なるほど、それならこちらを\x01",
            "持っていかれてはどうでしょう？\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x340),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x340, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0049
    ChrTalk(
        0x102,
        "#00105Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "ええ、ウチで使っている\x01",
            "にがトマトを煮詰めて作った\x01",
            "ペーストです。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "これを使えば滋養強壮、\x01",
            "間違いなし――\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "きっと素晴らしい\x01",
            "炊き出しになると思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00000F助かります。\x01",
            "それじゃ代金の方を……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "ああいえ、皆さんは\x01",
            "復興のお手伝いを\x01",
            "されているんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "なら遠慮なく\x01",
            "持って行って下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00002Fそうですか、すみません。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00102Fどうもありがとうございます。\x02",
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

    # Function_15_1DAB end

    def Function_16_2279(): pass

    label("Function_16_2279")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_228A")
    Jump("loc_2555")

    label("loc_228A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2555")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " チャリティイベント　　　　　　　　　　　 \x01",
            " 　『～みんなで広げよう復興の輪～』　　　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " 【プログラム概要】　　　　　　　　　　　 \x01",
            " 　・ソロピアノコンサート　　　　　　　　 \x01",
            " 　・ミス・クロスベルコンテスト　　　　　 \x01",
            " 　・大衆グルメコンテスト　　　　　　　　 \x01",
            " 　・各種アートワーク教室　　　　　　　　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  場所 ：クロスベル市民会館・多目的ホール \x01",
            " 　　　　会館前広場　　　　　　　　　　　 \x01",
            " 開催日：本日　　　　　　　　　　　　　　 \x01",
            " 主催者：クロスベル商工会／クロスベル市　 \x01",
            " 　　　　　　　　　　　　　　　　　　　　 \x01",
            " ※各種イベントの参加費用は、　　　　　　 \x01",
            " 　全て復興支援の資金に充てられます。　　 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2555")

    TalkEnd(0xFF)
    Return()

    # Function_16_2279 end

    SaveToFile()

Try(main)
