from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0300.bin",                # FileName
        "c0300",                    # MapName
        "c0300",                    # Location
        0x002A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0300",                  # 0
        "雷兹老人",               # 1
        "本特斯",                 # 2
        "辛迪",                   # 3
        "库雷优",                 # 4
        "乔安娜",                 # 5
        "雷克特",                 # 6
        "萨妮塔",                 # 7
        "玛丽",                   # 8
        "海尔玛",                 # 9
        "隆",                     # 10
        "亨利",                   # 11
        "小桃",                   # 12
        "中央广场",               # 13
        "西街",                   # 14
        "行政区",                 # 15
        "住宅街",                 # 16
        "欢乐街",                 # 17
        "东街",                   # 18
        "旧城区",                 # 19
        "港湾区",                 # 20
        "ＩＢＣ",                 # 21
        "站前街道",               # 22
        "后巷",                   # 23
        "乌尔斯拉间道",           # 24
        "东克洛斯贝尔街道",       # 25
        "西克洛斯贝尔街道",       # 26
        "玛因兹山道",             # 27
    ))

    AddCharChip((
        "chr/ch21602.itc",                   # 00
        "chr/ch33000.itc",                   # 01
        "chr/ch22100.itc",                   # 02
        "chr/ch33300.itc",                   # 03
        "chr/ch25700.itc",                   # 04
        "chr/ch34400.itc",                   # 05
        "chr/ch39000.itc",                   # 06
        "apl/ch50392.itc",                   # 07
    ))

    DeclNpc(-12850,  -5900,   -31489,  315,  261,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(32279,   0,       -4369,   270,  257,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(2349,    0,       -30700,  45,   389,  0x0, 0,   2,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(-15039,  -6000,   -17110,  45,   389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-21469,  -6000,   -33240,  315,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5500,   -6000,   -41360,  270,  439,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-15609,  0,       4480,    315,  453,  0x0, 0,   5,   0,   0,   3,   0,   25,  255,  0)
    DeclNpc(-15859,  0,       3849,    45,   453,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-1000,   0,       610,     90,   449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(449,     0,       610,     90,   449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(5360,    3000,    17690,   0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 32,  -24.110000610351562,   -33.16999816894531,    -6.5,                  0.0,                   [1.0,                  0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0])
    DeclEvent(0x0000, 0, 24,  0.38999998569488525,   -33.59000015258789,    0.0,                   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.039000000804662704, 11.196666717529297,    -0.0,                  1.0])

    DeclActor(-2700,   -6500,   -38000,  2000,    -2700,   -5500,   -38000,  0x007C, 0,  12, 0x0000)
    DeclActor(17650,   0,       -800,    2000,    17650,   1500,    -800,    0x007C, 0,  33, 0x0000)
    DeclActor(0,       0,       -770,    2000,    0,       1500,    -770,    0x007C, 0,  34, 0x0000)
    DeclActor(-24000,  -6000,   -33500,  2000,    -24000,  -4500,   -33500,  0x007C, 0,  31, 0x0000)

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央广场")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西街")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "欢乐街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "东街")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧城区")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "站前街道")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "后巷")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")
    PlaceName(185.89999389648438, 0.0, -144.17999267578125, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_648",          # 00, 0
        "Function_1_700",          # 01, 1
        "Function_2_761",          # 02, 2
        "Function_3_78C",          # 03, 3
        "Function_4_7B7",          # 04, 4
        "Function_5_B11",          # 05, 5
        "Function_6_DF8",          # 06, 6
        "Function_7_1BC8",         # 07, 7
        "Function_8_2896",         # 08, 8
        "Function_9_2ADA",         # 09, 9
        "Function_10_30AE",        # 0A, 10
        "Function_11_31E8",        # 0B, 11
        "Function_12_399D",        # 0C, 12
        "Function_13_3AB6",        # 0D, 13
        "Function_14_41D6",        # 0E, 14
        "Function_15_422B",        # 0F, 15
        "Function_16_4280",        # 10, 16
        "Function_17_42D5",        # 11, 17
        "Function_18_430C",        # 12, 18
        "Function_19_46F8",        # 13, 19
        "Function_20_4872",        # 14, 20
        "Function_21_53B1",        # 15, 21
        "Function_22_579C",        # 16, 22
        "Function_23_5DB6",        # 17, 23
        "Function_24_5DE6",        # 18, 24
        "Function_25_628F",        # 19, 25
        "Function_26_6B65",        # 1A, 26
        "Function_27_6BA4",        # 1B, 27
        "Function_28_6BE1",        # 1C, 28
        "Function_29_6EF1",        # 1D, 29
        "Function_30_7292",        # 1E, 30
        "Function_31_7313",        # 1F, 31
        "Function_32_7552",        # 20, 32
        "Function_33_7553",        # 21, 33
        "Function_34_759F",        # 22, 34
        "Function_35_778E",        # 23, 35
        "Function_36_8259",        # 24, 36
        "Function_37_8278",        # 25, 37
        "Function_38_82A8",        # 26, 38
    ))


    def Function_0_648(): pass

    label("Function_0_648")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_688"),
        (1, "loc_694"),
        (2, "loc_6A0"),
        (3, "loc_6AC"),
        (4, "loc_6B8"),
        (5, "loc_6C4"),
        (6, "loc_6D0"),
        (SWITCH_DEFAULT, "loc_6DC"),
    )


    label("loc_688")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_694")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6FF")

    Return()

    # Function_0_648 end

    def Function_1_700(): pass

    label("Function_1_700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_760")
    OP_95(0xFE, 2630, 0, -4370, 1000, 0x0)
    OP_95(0xFE, 240, 0, -7350, 1000, 0x0)
    OP_95(0xFE, 240, -750, -48720, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 35280, 0, -4370, 45)
    Jump("Function_1_700")

    label("loc_760")

    Return()

    # Function_1_700 end

    def Function_2_761(): pass

    label("Function_2_761")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78B")
    OP_94(0xFE, 0xD20, 0xFFFF8FDA, 0x546, 0xFFFF842C, 0x3E8)
    Sleep(300)
    Jump("Function_2_761")

    label("loc_78B")

    Return()

    # Function_2_761 end

    def Function_3_78C(): pass

    label("Function_3_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_94(0xFE, 0xFFFFC7AC, 0x1658, 0xFFFFBBEA, 0x3F2, 0x3E8)
    Sleep(300)
    Jump("Function_3_78C")

    label("loc_7B6")

    Return()

    # Function_3_78C end

    def Function_4_7B7(): pass

    label("Function_4_7B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_879")
    SetChrPos(0x0, 230, -750, -38720, 0)
    SetChrPos(0x1, 230, -750, -38720, 0)
    SetChrPos(0x2, 230, -750, -38720, 0)
    SetChrPos(0x3, 230, -750, -38720, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84C")
    SetChrPos(0x4, 230, -750, -38720, 0)
    SetChrPos(0x5, 230, -750, -38720, 0)
    Jump("loc_86B")

    label("loc_84C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86B")
    SetChrPos(0x4, 230, -750, -38720, 0)

    label("loc_86B")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_948")

    label("loc_879")

    SetChrPos(0x0, 24330, 0, -4050, 270)
    SetChrPos(0x1, 24330, 0, -4050, 270)
    SetChrPos(0x2, 24330, 0, -4050, 270)
    SetChrPos(0x3, 24330, 0, -4050, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F2")
    SetChrPos(0x4, 24330, 0, -4050, 270)
    SetChrPos(0x5, 24330, 0, -4050, 270)
    Jump("loc_911")

    label("loc_8F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_911")
    SetChrPos(0x4, 24330, 0, -4050, 270)

    label("loc_911")

    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_948")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_985")

    label("loc_96C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_985")
    Event(0, 20)

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_994")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 19)

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AA")
    Event(0, 35)

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9D4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -10850, -6000, -24740, 315)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_AE1")

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9E2")
    Jump("loc_AE1")

    label("loc_9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9FA")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_AE1")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A08")
    Jump("loc_AE1")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A20")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AE1")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A38")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_AE1")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A46")
    Jump("loc_AE1")

    label("loc_A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A68")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    SetChrFlags(0xB, 0x10)

    label("loc_A63")

    Jump("loc_AE1")

    label("loc_A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A76")
    Jump("loc_AE1")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AA7")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA2")
    ClearChrFlags(0xE, 0x80)

    label("loc_AA2")

    Jump("loc_AE1")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AB5")
    Jump("loc_AE1")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AC8")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_AE1")

    label("loc_AC8")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE1")
    SetChrFlags(0xB, 0x10)

    label("loc_AE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF9")
    OP_C7(0x1, 0x1000)

    label("loc_AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B10")
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_B10")

    Return()

    # Function_4_7B7 end

    def Function_5_B11(): pass

    label("Function_5_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_B2A")

    label("loc_B26")

    OP_65(0x0, 0x1)

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BCC")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BA7")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BCC")

    label("loc_BA7")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_BCC")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BF3")
    ClearMapObjFlags(0xF, 0x4)
    Jump("loc_C37")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C01")
    Jump("loc_C37")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C15")
    ClearMapObjFlags(0xF, 0x4)
    Jump("loc_C37")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_C37")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C37")
    ClearMapObjFlags(0xF, 0x4)
    Jump("loc_C37")

    label("loc_C37")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    OP_70(0x0, 0xA)
    OP_70(0x1, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0x0)
    OP_70(0x6, 0xA)
    OP_70(0xD, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C95")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA8")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBB")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCE")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CE1")

    ModifyEventFlags(0, 0, 0x80)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D00")
    OP_70(0x1, 0x0)
    OP_66(0x3, 0x1)

    label("loc_D00")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1A")
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)

    label("loc_D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5A")
    OP_1B(0x1, 0x0, 0x1E)

    label("loc_D5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D79")
    Jump("loc_D7E")

    label("loc_D79")

    ModifyEventFlags(0, 1, 0x80)

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD6")
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -7830, -6000, -41810, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF2")
    Jump("loc_DF7")

    label("loc_DF2")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_DF7")

    Return()

    # Function_5_B11 end

    def Function_6_DF8(): pass

    label("Function_6_DF8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8C")
    Jump("loc_ED6")

    label("loc_E8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EAC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ED6")

    label("loc_EAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ED6")

    label("loc_ECC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ED6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F49")

    #C0001
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔的夜晚有点冷，\x01",
            "你们还是早些回去为好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F88")

    label("loc_F49")


    #C0002
    ChrTalk(
        0x8,
        "哎呀，糟糕，已经是黄昏了……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "差不多也该回家了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F88")

    Jump("loc_1BC0")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FDE")

    #C0004
    ChrTalk(
        0x8,
        (
            "说起本德，那可真是个\x01",
            "性格开朗的青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "他出了什么事吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_10A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_101B")

    #C0006
    ChrTalk(
        0x8,
        "这样的话，会议一时也无法结束了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A0")

    label("loc_101B")


    #C0007
    ChrTalk(
        0x8,
        (
            "帝国派的提案考虑到了帝国的权利，\x01",
            "而共和国派也努力推行有利于共和国的政策。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "……克洛斯贝尔简直就是被\x01",
            "两个大国夹在了中间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10A0")

    Jump("loc_1BC0")

    label("loc_10A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1135")

    #C0009
    ChrTalk(
        0xFE,
        (
            "那座住宅里住着一名\x01",
            "叫做本德的证券经理。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "大概是纪念庆典之后吧，\x01",
            "好像在生意上失败了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "那段时间里，他的情绪非常低落。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_118E")

    #C0012
    ChrTalk(
        0x8,
        "哦哦，今天也是个好天气呢。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "怎么样，小姑娘也\x01",
            "跟我一起晒晒太阳吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_118E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1323")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_122C")

    #C0014
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔的政治局面\x01",
            "非常复杂，只凭正义感，\x01",
            "很多事情根本就做不成。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "还是要把这些事交付给那些\x01",
            "狡猾的人才行，无论他们是善是恶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131E")

    label("loc_122C")


    #C0016
    ChrTalk(
        0x8,
        (
            "自治州议会中聚集的那些议员们，\x01",
            "都是一些狡猾的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "因为克洛斯贝尔的政治体系中，\x01",
            "涉及到了帝国和共和国的各种意图，\x01",
            "情况十分复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "就算一些正义感很强的年轻人\x01",
            "当选了议员，想要做些什么，\x01",
            "到头来……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "终究还是无法得偿所愿啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_131E")

    Jump("loc_1BC0")

    label("loc_1323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_139E")

    #C0020
    ChrTalk(
        0x8,
        (
            "我在这里悠闲放松的时候，\x01",
            "经常看到送比萨的人经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "最近，这种新潮的东西\x01",
            "开始流行起来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1441")

    label("loc_139E")


    #C0022
    ChrTalk(
        0x8,
        (
            "嗯，最近使用\x01",
            "外卖服务好像\x01",
            "成为了一种新的流行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "我在这里悠闲放松的时候，\x01",
            "经常看到送比萨的人经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "跟我年轻的时候相比，\x01",
            "时代真是越来越进步了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1441")

    Jump("loc_1BC0")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_162B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14F3")

    #C0025
    ChrTalk(
        0x8,
        (
            "哦，看来你们\x01",
            "好像认识那孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "我还以为\x01",
            "是自己睡糊涂了呢……\x01",
            "看来这真的不是梦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "总觉得是个不可思议的孩子呢，\x01",
            "到底是从哪里来的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1626")

    label("loc_14F3")


    #C0028
    ChrTalk(
        0x8,
        (
            "前几天，我遇到了一个\x01",
            "不可思议的小女孩。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "是个穿着漂亮的连衣裙，\x01",
            "有着紫色头发的可爱孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "不知什么时候，\x01",
            "就已经站在了我的面前。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "不过，跟我打过一声招呼后，\x01",
            "一下就消失不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0005F那是……\x01",
            "我们在人偶工房见到的那个孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#0200F好像是叫……小玲吧，\x01",
            "她好像不时会到市里来玩呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1626")

    Jump("loc_1BC0")

    label("loc_162B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1744")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1693")

    #C0034
    ChrTalk(
        0x8,
        "自治州议会将近的这个时期……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "唔唔，是政治家和议员们\x01",
            "开始忙碌的时节呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173F")

    label("loc_1693")


    #C0036
    ChrTalk(
        0x8,
        "呵呵，今天也是个好天气呢。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "刚才看到坎贝尔议员\x01",
            "坐车去上班了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "唔唔，说起来，\x01",
            "自治州议会快要召开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "对政治家和议员们来说，\x01",
            "这个时期会非常忙碌吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_173F")

    Jump("loc_1BC0")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_183B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_179E")

    #C0040
    ChrTalk(
        0xFE,
        "那场事故十分严重呢……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "好像有一个小姑娘的\x01",
            "眼睛被弄伤了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1836")

    label("loc_179E")


    #C0042
    ChrTalk(
        0xFE,
        "那是四五年前的事了……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "搬运车在路上\x01",
            "造成了一起大事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "真是太惨烈了……\x01",
            "而且还发生了爆炸。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "就连附近的居民\x01",
            "也被这起事故波及到了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1836")

    Jump("loc_1BC0")

    label("loc_183B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1889")

    #C0046
    ChrTalk(
        0x8,
        (
            "小孩子单独出门是很危险的。\x01",
            "大人必须要小心看护啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1910")

    label("loc_1889")


    #C0047
    ChrTalk(
        0x8,
        (
            "嗯，最近\x01",
            "那家的小姑娘\x01",
            "似乎经常出门。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "而且好像是跑去\x01",
            "很远的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "小孩子单独出远门是很危险的啊。\x01",
            "要多注意一下才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1910")

    Jump("loc_1BC0")

    label("loc_1915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_195F")

    #C0050
    ChrTalk(
        0x8,
        (
            "哦哦，真是和平的日子啊。\x01",
            "这样不是挺好的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F8")

    label("loc_195F")


    #C0051
    ChrTalk(
        0x8,
        "年轻人，早起散步吗？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "呵呵，一大早就这么有活力啊。\x01",
            "不如去ＩＢＣ的大楼拜访一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "欣赏在晨雾中矗立着的ＩＢＣ大楼，\x01",
            "真是别有一番情致啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19F8")

    Jump("loc_1BC0")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A66")

    #C0054
    ChrTalk(
        0x8,
        (
            "这条住宅街，在克洛斯贝尔市里\x01",
            "算是治安最好的街道了。\x01",
            "可以安心地在这里午睡呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AFC")

    label("loc_1A66")


    #C0055
    ChrTalk(
        0x8,
        (
            "这条住宅街，在克洛斯贝尔市中，\x01",
            "算是治安最好的街道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "因为这里住着很多\x01",
            "政治家和财经界的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "警察对我们这些住户\x01",
            "也很关照呢，呵呵……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1AFC")

    Jump("loc_1BC0")

    label("loc_1B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B5E")

    #C0058
    ChrTalk(
        0x8,
        "年轻人，在散步吗？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "这一带是宁静的住宅街。\x01",
            "要散步的话，非这里莫属啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1B5E")


    #C0060
    ChrTalk(
        0x8,
        "呼～啊啊……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "哦哦，今天的阳光也很明媚啊，照得人真舒服。\x01",
            "要晒太阳的话，真是太合适了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BC0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_DF8 end

    def Function_7_1BC8(): pass

    label("Function_7_1BC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1CF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C49")

    #C0062
    ChrTalk(
        0x9,
        "四个月之后还会有市长选举……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "到时候，拉选票的活动肯定又会泛滥成灾，\x01",
            "这也是没有办法的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_1C49")


    #C0064
    ChrTalk(
        0x9,
        (
            "本年度的预算似乎\x01",
            "也搀杂着很多复杂的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "优先通过能提高知名度的提案，\x01",
            "把预算分配在对议员有利的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "其实就是博取人气，\x01",
            "也就是所谓的拉选票呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1CEF")

    Jump("loc_2892")

    label("loc_1CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D3D")

    #C0067
    ChrTalk(
        0x9,
        "今天没怎么遇到警官呢。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "大家都到\x01",
            "别的地方去了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_1D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DBA")

    #C0069
    ChrTalk(
        0x9,
        (
            "坎贝尔议员也做了\x01",
            "各种各样的策划吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "不过，对手是那位哈尔特曼议长的话，\x01",
            "总觉得胜算不大啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_1DBA")


    #C0071
    ChrTalk(
        0x9,
        (
            "唔，听说坎贝尔议员\x01",
            "目前陷入苦战了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        "帝国派的优势果然是很难动摇啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1E0E")

    Jump("loc_2892")

    label("loc_1E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E6B")

    #C0073
    ChrTalk(
        0x9,
        "今年是市长的选举年呢。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "麦克道尔市长\x01",
            "会不会出马竞选呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F05")

    label("loc_1E6B")


    #C0075
    ChrTalk(
        0x9,
        (
            "今年正好是五年一度的\x01",
            "市长选举年。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "那是决定在今后的五年里，由谁来\x01",
            "担任自治州代表的选举……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "希望别再出现像\x01",
            "预算会议不断延期那样的状况了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F05")

    Jump("loc_2892")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2009")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F7D")

    #C0078
    ChrTalk(
        0x9,
        (
            "被逮捕的那个市长秘书，\x01",
            "据说被关押到拘留所里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "……那可真是个\x01",
            "令人震惊的案子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2004")

    label("loc_1F7D")


    #C0080
    ChrTalk(
        0x9,
        "说起来……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "被逮捕的那个市长秘书，\x01",
            "已经被关押到拘留所里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "不过，现在仍然保持着沉默。\x01",
            "真是的，好一个嘴硬的男人啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2004")

    Jump("loc_2892")

    label("loc_2009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_209E")

    #C0083
    ChrTalk(
        0x9,
        "咳咳，你们几个……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "刚才是不是进入\x01",
            "地下空间里面了？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "这可不行啊，那里\x01",
            "可不是小孩子玩耍的地方。\x01",
            "太危险了，还是不要再去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_209E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_213E")

    #C0086
    ChrTalk(
        0x9,
        (
            "我个人也投资了\x01",
            "ＩＢＣ所运营的\x01",
            "『米修拉姆』。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "咳咳……\x01",
            "作为受到优待的赞助商，我有很多\x01",
            "『咪西』的周边哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        "#0200F（……好羡慕………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_213E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_21C6")

    #C0089
    ChrTalk(
        0x9,
        (
            "市长最近好像在跟各方面的要人\x01",
            "频繁进行着一些重要会谈……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "都已经上了年纪，\x01",
            "却仍然不服老，真是一位令人尊敬的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_21C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2303")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_223E")

    #C0091
    ChrTalk(
        0x9,
        (
            "彩虹剧团的票\x01",
            "总共有三种。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "Ｓ席的票能拍卖到\x01",
            "原价两百倍的价格，\x01",
            "他们的人气就是这么夸张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22FE")

    label("loc_223E")


    #C0093
    ChrTalk(
        0x9,
        (
            "彩虹剧团的门票价格\x01",
            "是出了名的高。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "票一共分为Ｂ席、Ａ席、Ｓ席\x01",
            "三种。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "顺便一说，剧场中好像\x01",
            "也准备了特别贵宾席，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "那只是为了剧团的赞助商\x01",
            "和特别的宾客而专门准备的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_22FE")

    Jump("loc_2892")

    label("loc_2303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2396")

    #C0097
    ChrTalk(
        0x9,
        "最近常常看到比萨店送外卖的人。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "就从那条路上跑过去，\x01",
            "然后站在没有人家的\x01",
            "住宅区尽头。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "嗯……到底是谁\x01",
            "会去那里拿比萨呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_24AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_241B")

    #C0100
    ChrTalk(
        0x9,
        (
            "如果要去克洛斯贝尔大圣堂，\x01",
            "或是矿山镇玛因兹的话，\x01",
            "穿过住宅街就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "呵呵，对市民来说，这都是常识。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24AA")

    label("loc_241B")


    #C0102
    ChrTalk(
        0x9,
        (
            "这个住宅街\x01",
            "位于城市最西北的位置。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "通过这里之后，\x01",
            "就能从城市的北出口出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "外面的山道通向\x01",
            "克洛斯贝尔大圣堂\x01",
            "和矿山镇玛因兹。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24AA")

    Jump("loc_2892")

    label("loc_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2531")

    #C0105
    ChrTalk(
        0x9,
        (
            "高达四十层的大楼，\x01",
            "实在是让人震惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "呵呵，克洛斯贝尔又多了一处\x01",
            "观光胜地呢。\x01",
            "真期待它的建成啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_2531")


    #C0107
    ChrTalk(
        0x9,
        (
            "现在正在建设中的\x01",
            "克洛斯贝尔新市政厅大楼，\x01",
            "将会是世界上最高的近代建筑物。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "一旦完成的话，将会是一座\x01",
            "高达四十层的建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "不仅囊括了市政厅的全部机能，\x01",
            "还预计将餐饮、租赁空间\x01",
            "等项目也设计进去。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "呵呵……我作为一个事业家，\x01",
            "也参与了一部分事业呢。\x01",
            "真是太期待工程的完成了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_264F")

    Jump("loc_2892")

    label("loc_2654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_278E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26D0")

    #C0111
    ChrTalk(
        0x9,
        (
            "坎贝尔先生是一位\x01",
            "领导着共和国派议员的\x01",
            "大政治家。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "也就是说，是那位\x01",
            "哈尔特曼议长的竞争对手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2789")

    label("loc_26D0")


    #C0113
    ChrTalk(
        0x9,
        (
            "咳咳……你知道拐弯处的\x01",
            "那座大宅子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "那是共和国派议员的领袖，\x01",
            "坎贝尔先生的住宅。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "早上有时能看到\x01",
            "豪华的导力车停留在那里。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "还能看到他乘坐那辆车\x01",
            "前往事务所上班呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2789")

    Jump("loc_2892")

    label("loc_278E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_27F6")

    #C0117
    ChrTalk(
        0x9,
        (
            "在这一带居住的居民，\x01",
            "都是些上流社会的人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "哈，如此说来，\x01",
            "我也算其中之一了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2892")

    label("loc_27F6")


    #C0119
    ChrTalk(
        0x9,
        (
            "咳咳……矗立在这一带的\x01",
            "都是些高级住宅。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔的地价是很高的，\x01",
            "所以豪宅都是价格不菲。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "在这一带居住的居民，\x01",
            "都算得上是上流社会的人士。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2892")

    TalkEnd(0xFE)
    Return()

    # Function_7_1BC8 end

    def Function_8_2896(): pass

    label("Function_8_2896")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2915")

    #C0122
    ChrTalk(
        0xA,
        (
            "库雷优夫人的丈夫\x01",
            "真的失踪了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0123
    ChrTalk(
        0xA,
        (
            "总、总觉得很让人担心啊，\x01",
            "我也去探望一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xA)
    Jump("loc_2AD6")

    label("loc_2915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2979")

    #C0124
    ChrTalk(
        0xA,
        (
            "利落地打扫完，\x01",
            "之后去喝杯茶吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "今天爸爸也在家。\x01",
            "偶尔也能悠闲地全家团聚呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD6")

    label("loc_2979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_29CF")

    #C0126
    ChrTalk(
        0xA,
        (
            "说起来，亨利到底\x01",
            "去哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "爸爸明明说过，\x01",
            "绝对不许外出的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD6")

    label("loc_29CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A68")

    #C0128
    ChrTalk(
        0xA,
        (
            "对了，你看了最新一期的\x01",
            "克洛斯贝尔时代周刊吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        "我的弟弟被刊登在上面了。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "爸爸看了那个报道之后很生气呢！\x01",
            "亨利又做了蠢事啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AD6")

    label("loc_2A68")


    #C0131
    ChrTalk(
        0xA,
        (
            "奶奶命令我\x01",
            "早晨起来就开始打扫。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "呼啊啊～困死我了，\x01",
            "不过这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "赶紧利落地\x01",
            "收拾完吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2AD6")

    TalkEnd(0xFE)
    Return()

    # Function_8_2896 end

    def Function_9_2ADA(): pass

    label("Function_9_2ADA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2BD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2B44")

    #C0134
    ChrTalk(
        0xB,
        (
            "索菲亚女士的丈夫\x01",
            "是一位工作狂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        (
            "好像上午一大早\x01",
            "就匆匆忙忙地出门了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD0")

    label("loc_2B44")


    #C0136
    ChrTalk(
        0xB,
        (
            "啊啊啊……\x01",
            "今天的天气也不错呐……⊥\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0137
    ChrTalk(
        0xB,
        (
            "说起来，哈罗德先生\x01",
            "今天一大早\x01",
            "就开着导力车出门了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "好像有什么急事似的。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_2BD0")

    Jump("loc_30AA")

    label("loc_2BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2EA3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD9")

    #C0139
    ChrTalk(
        0xFE,
        (
            "哎呀，你们是刚才和萨妮塔\x01",
            "一起来过我家的……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "是我家先生的熟人吗？\x01",
            "呵呵，请进来喝杯茶吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0005F啊，请不用这么客气。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0100F请好好照顾\x01",
            "小玛丽哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0143
    ChrTalk(
        0xFE,
        (
            "玛丽……？\x01",
            "那是哪位啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 3)
    Jump("loc_2D18")

    label("loc_2CD9")


    #C0144
    ChrTalk(
        0xFE,
        (
            "我们家好像没有\x01",
            "叫玛丽的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "……到底是谁呢……？\x02",
    )

    CloseMessageWindow()

    label("loc_2D18")

    Jump("loc_2E9E")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_2D89")

    #C0146
    ChrTalk(
        0xFE,
        (
            "哎呀……萨妮塔\x01",
            "好像已经出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "最近好像经常出门去什么地方。\x01",
            "到底在做些什么呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9E")

    label("loc_2D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2DE5")

    #C0148
    ChrTalk(
        0xB,
        (
            "现在的我，\x01",
            "已经能应付一般家务了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "呵呵，这也是我努力\x01",
            "学习的结果啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9E")

    label("loc_2DE5")


    #C0150
    ChrTalk(
        0xB,
        "我父母的家是一座大宅子。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "有很多女仆和佣人可以使唤，\x01",
            "家务之类的事情，我从来都没做过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "结婚之后，\x01",
            "这么多的家务让我手忙脚乱……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        "不过，现在的生活却让我乐在其中呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2E9E")

    Jump("loc_30AA")

    label("loc_2EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2FAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F07")

    #C0154
    ChrTalk(
        0xB,
        (
            "住在前面那条街道的索菲亚女士，\x01",
            "是一位非常出色的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        "我非常憧憬她。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FA7")

    label("loc_2F07")


    #C0156
    ChrTalk(
        0xB,
        (
            "住在前面那条街道的索菲亚女士，\x01",
            "在烹饪方面很有一手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "而且好像还能帮丈夫\x01",
            "处理工作上的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        "真是太能干了……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "我对丈夫的工作\x01",
            "就一窍不通。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_2FA7")

    Jump("loc_30AA")

    label("loc_2FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3005")

    #C0160
    ChrTalk(
        0xB,
        (
            "都说鲜花要经过爱心的浇灌，\x01",
            "才能鲜艳盛开呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        "呵呵，渐渐长大了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30AA")

    label("loc_3005")


    #C0162
    ChrTalk(
        0xB,
        (
            "啦啦……\x01",
            "又该给花浇水了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0163
    ChrTalk(
        0xB,
        (
            "呵呵，那边的花坛\x01",
            "是去年春天建起来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "你们看！\x01",
            "有很多美丽的鲜花盛开着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "我说不定有\x01",
            "给花浇水的才能哦。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_30AA")

    TalkEnd(0xFE)
    Return()

    # Function_9_2ADA end

    def Function_10_30AE(): pass

    label("Function_10_30AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_30F4")

    #C0166
    ChrTalk(
        0xC,
        (
            "…………………………\x01",
            "稍后必须要去询问一下啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E4")

    label("loc_30F4")


    #C0167
    ChrTalk(
        0xC,
        "…………………………？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#0105F乔安娜？\x01",
            "你怎么了吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 750)

    #C0170
    ChrTalk(
        0xC,
        (
            "没什么……今天明明是\x01",
            "克洛斯贝尔时代周刊的发行日，\x01",
            "却还没有送过来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "………………………………\x01",
            "稍后得问问是怎么回事。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x13B, 0x2EE)
    SetChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_31E4")

    TalkEnd(0xFE)
    Return()

    # Function_10_30AE end

    def Function_11_31E8(): pass

    label("Function_11_31E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EE")
    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50357.itc", 0x1E)
    OP_68(-6130, -4250, -41410, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, -4900, -6000, -40150, 225)
    SetChrPos(0x153, -5500, -6000, -39860, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3291")
    SetChrPos(0x102, -5250, -6000, -39000, 180)
    Jump("loc_32D8")

    label("loc_3291")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32B7")
    SetChrPos(0x103, -5250, -6000, -39000, 180)
    Jump("loc_32D8")

    label("loc_32B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32D8")
    SetChrPos(0x104, -5250, -6000, -39000, 180)

    label("loc_32D8")

    FadeToBright(500, 0)
    OP_0D()

    #C0172
    ChrTalk(
        0x153,
        (
            "#1110F#5P啊～是那时的\x01",
            "那个奇怪的人！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Sleep(300)
    Fade(500)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x1E)
    ClearChrFlags(0xD, 0x2)
    OP_93(0xD, 0x0, 0x1F4)
    StopEffect(0x8, 0x2)
    OP_0D()

    #C0173
    ChrTalk(
        0xD,
        (
            "#3509F哟，这不是小不点吗，\x01",
            "又见面了啊～¤\x02\x03",

            "#3502F呵呵，最近还好吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雷克特摸了摸琪雅的头。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0175
    ChrTalk(
        0x153,
        "#1105F#5P啊～好痒啊。\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0011F雷克特先生……\x01",
            "你还在克洛斯贝尔啊。\x02\x03",

            "#0006F而且又在悠闲地钓鱼……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_346F")

    #C0177
    ChrTalk(
        0x102,
        (
            "#0111F#5P话说回来……你到底\x01",
            "是什么人啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34FC")

    label("loc_346F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34C2")

    #C0178
    ChrTalk(
        0x103,
        (
            "#0211F#5P话说回来，你到底是什么人啊，\x01",
            "真是很让人好奇呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34FC")

    label("loc_34C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34FC")

    #C0179
    ChrTalk(
        0x104,
        (
            "#0301F#5P我说，你到底\x01",
            "是干什么的啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FC")


    #C0180
    ChrTalk(
        0xD,
        (
            "#3510F嗯，这个嘛，就是那个啦！\x01",
            "帝国的───以下省略！！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#0006F（这种糊弄人的方式也太烂了吧……）\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x153,
        (
            "#1109F#5P啊哈哈哈！\x01",
            "果然是个奇怪的人～！\x02\x03",

            "#1110F……不过，真开心呢。\x01",
            "因为琪雅的记忆里，\x01",
            "完全都不记得任何人。\x02\x03",

            "#1108F跟罗伊德第一次见面的时候……\x01",
            "感觉就像在做梦一样，\x01",
            "最近都有点模糊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xD,
        (
            "#3505F原来如此啊………\x02\x03",

            "#3504F……看起来，你多半是浸在\x01",
            "名为『幸福』的感觉中了。\x02\x03",

            "#3500F这种感觉，可要好好记住哟。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x153,
        (
            "#1105F#5P幸福……？\x02\x03",

            "#1104F嗯……听不太明白呢，\x01",
            "反正琪雅很快乐就是了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0185
    ChrTalk(
        0x153,
        (
            "#1109F#5P算啦，虽然还是不太懂，\x01",
            "不过我记住了！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        "#3509F啊哈哈，这算什么话嘛～¤\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#0012F（好像正在进行着只有\x01",
            "  他们两人才能理解的对话啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F3")

    #C0188
    ChrTalk(
        0x102,
        (
            "#0109F#5P（呵呵，算了，这也挺好啊，\x01",
            "  至少琪雅好像能够接受……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3886")

    label("loc_37F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3844")

    #C0189
    ChrTalk(
        0x103,
        (
            "#0202F#5P（算啦，只要琪雅能接受，\x01",
            "  不就挺好的吗……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3886")

    label("loc_3844")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3886")

    #C0190
    ChrTalk(
        0x104,
        (
            "#0302F#5P（算啦，只要阿琪能接受\x01",
            "  就行了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3886")

    Sleep(150)
    SetChrPos(0x0, -4900, -6000, -40050, 225)
    SetChrChipByIndex(0xD, 0x7)
    SetChrFlags(0xD, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_93(0xD, 0x10E, 0x0)
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -7830, -6000, -41810, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    SetScenarioFlags(0xB7, 6)
    EventEnd(0x5)
    Jump("loc_3999")

    label("loc_38EE")


    #C0191
    ChrTalk(
        0xD,
        (
            "#3510F话说，住宅街这一带\x01",
            "可真是一片宁静啊。\x02\x03",

            "#3507F在这里钓鱼的话，果然要用蚯蚓吧？\x01",
            "还是说，要用红虫做鱼饵才行呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#0006F我怎么会知道啊……\x01",
            "请你自己试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3999")

    TalkEnd(0xFE)
    Return()

    # Function_11_31E8 end

    def Function_12_399D(): pass

    label("Function_12_399D")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('地下空间Ｂ区域的钥匙', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DF")
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门被牢牢地锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3AB3")

    label("loc_39DF")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02\x03",

            "使用地下空间Ｂ区域的钥匙\x01",
            "应该就可以将门打开。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "使用钥匙\x01",        # 0
            "不使用钥匙\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A7B"),
        (1, "loc_3AAE"),
        (SWITCH_DEFAULT, "loc_3AB3"),
    )


    label("loc_3A7B")

    Sound(809, 0, 100, 0)
    SetChrName("")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "打开了门锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x86, 1)
    Jump("loc_3AB3")

    label("loc_3AAE")

    Jump("loc_3AB3")

    label("loc_3AB3")

    EventEnd(0x3)
    Return()

    # Function_12_399D end

    def Function_13_3AB6(): pass

    label("Function_13_3AB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3000, -5500, -38000, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, -1000, -6500, -38000, 270)
    SetChrPos(0x102, -1000, -6500, -38000, 270)
    SetChrPos(0x103, -1000, -6500, -38000, 270)
    SetChrPos(0x104, -1000, -6500, -38000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x10000000)
    MoveCamera(55, 35, 0, 6000)
    SetCameraDistance(24000, 6000)
    FadeToBright(2000, 0)
    Sleep(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    BeginChrThread(0x104, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(1500)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x101, 3)
    Fade(500)
    OP_68(-4800, -4900, -37000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    #C0196
    ChrTalk(
        0x101,
        (
            "#6P#0003F不过，没想到他会在\x01",
            "这种地方生活啊……\x02\x03",

            "#0001F真让人有些放心不下。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        (
            "#6P#0106F是啊，看起来还是该在\x01",
            "主日学校学习的年纪……\x02\x03",

            "#0101F缇欧，他多大了呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CCC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3CCC)
    Sleep(50)

    def lambda_3CDC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CDC)
    Sleep(300)

    #C0198
    ChrTalk(
        0x103,
        (
            "#11P#0200F没记错的话，应该是十三岁。\x02\x03",

            "比我要小一岁。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯～还是让财团的人\x01",
            "来领走他比较好吧……\x02\x03",

            "#0008F不过，他毕竟给财团造成过很大的损害，\x01",
            "也许别让财团知道他的行踪比较好吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        (
            "#0306F#5P呼，还是先别管他了。\x02\x03",

            "#0300F看样子，他是个很精明的小鬼，\x01",
            "而且行动力也不差。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        (
            "#11P#0203F嗯，可以这么说吧，\x01",
            "他确实拥有着天才般的头脑。\x02\x03",

            "#0202F不过，有时也会缺根神经，\x01",
            "所以刚才就连并非专攻此道的我\x01",
            "也能找到切入的破绽。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#12P#0006F嗯～……\x02",
    )

    CloseMessageWindow()

    def lambda_3EB1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3EB1)
    Sleep(50)

    def lambda_3EC1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3EC1)
    Sleep(300)

    #C0203
    ChrTalk(
        0x102,
        (
            "#6P#0104F呵呵，你还真是爱操心啊。\x02\x03",

            "#0100F总而言之，对他还是\x01",
            "多留心一下吧。\x02\x03",

            "以后最好还是定期\x01",
            "来拜访一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯……就这么办吧。\x02\x03",

            "#0003F──这样也好。\x01",
            "另外就是关于『银』的事情。\x02\x03",

            "#0001F对方似乎在『星见之塔』\x01",
            "那里等着我们……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_4093")

    #C0205
    ChrTalk(
        0x103,
        (
            "#0201F#5P以前去塔前的时候，\x01",
            "那里是被警备队所设的防护栏\x01",
            "封锁着的……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        (
            "#0304F#5P不过，像那种高度的防护栏，\x01",
            "轻而易举就能翻越过去。\x02\x03",

            "#0300F如有必要的话，还可以联系\x01",
            "索妮亚副司令，取得她的许可。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4133")

    label("loc_4093")


    #C0207
    ChrTalk(
        0x103,
        (
            "#0201F#5P应该是那座在乌尔斯拉间道\x01",
            "途中就可以看到的塔吧？\x02\x03",

            "要怎么走才能到那里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#0300F#5P道路的途中应该\x01",
            "有一条通向森林的岔道。\x02\x03",

            "就在那条路的尽头吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4133")


    #C0209
    ChrTalk(
        0x102,
        (
            "#6P#0103F说得也是……\x02\x03",

            "#0101F总而言之，做好准备后\x01",
            "再去那里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯……\x01",
            "有可能是个陷阱。\x02\x03",

            "做好万全的准备之后再出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -4800, -6000, -36700, 0)
    SetScenarioFlags(0x83, 7)
    EventEnd(0x5)
    Return()

    # Function_13_3AB6 end

    def Function_14_41D6(): pass

    label("Function_14_41D6")


    def lambda_41DB():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41DB)

    def lambda_41F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41F5)
    WaitChrThread(0xFE, 1)

    def lambda_420A():
        OP_95(0xFE, -4800, -6000, -35400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_420A)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_14_41D6 end

    def Function_15_422B(): pass

    label("Function_15_422B")


    def lambda_4230():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4230)

    def lambda_424A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_424A)
    WaitChrThread(0xFE, 1)

    def lambda_425F():
        OP_95(0xFE, -5600, -6000, -36700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_425F)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_15_422B end

    def Function_16_4280(): pass

    label("Function_16_4280")


    def lambda_4285():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4285)

    def lambda_429F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_429F)
    WaitChrThread(0xFE, 1)

    def lambda_42B4():
        OP_95(0xFE, -4100, -6000, -36700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_42B4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_16_4280 end

    def Function_17_42D5(): pass

    label("Function_17_42D5")


    def lambda_42DA():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42DA)

    def lambda_42F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42F4)
    WaitChrThread(0xFE, 1)
    OP_93(0x101, 0x59, 0x1F4)
    Return()

    # Function_17_42D5 end

    def Function_18_430C(): pass

    label("Function_18_430C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_4B(0x9, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(90, 2000, 3870, 0)
    MoveCamera(18, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25500, 0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    FadeToBright(1000, 0)
    OP_68(11790, 2000, -24490, 7000)
    MoveCamera(67, 22, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(21000, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-16190, -3900, -16880, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    OP_68(-28000, -3400, -29760, 5000)
    MoveCamera(0, 22, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(23000, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-14640, 2000, -35510, 0)
    MoveCamera(26, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(29000, 5000)
    OP_0D()
    PlaceName2(100, 200, "c_plac09", 0x0, 0)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4560")
    Sleep(500)

    #A0211
    AnonymousTalk(
        0x101,
        (
            "#0004F克洛斯贝尔市西北区域……\x02\x03",

            "#0000F这一带从前就建有很多高级住宅呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0212
    AnonymousTalk(
        0x104,
        "#0305F原来如此，全都是大豪宅啊。\x02",
    )

    CloseMessageWindow()

    #A0213
    AnonymousTalk(
        0x102,
        "#0109F……是、是啊。\x02",
    )

    CloseMessageWindow()

    #A0214
    AnonymousTalk(
        0x103,
        (
            "#0205F……………………？\x01",
            "（感觉艾莉前辈的样子好像有些奇怪呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4560")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "住宅街是位于城市西北部的宁静街区。\x02",
        )
    )

    CloseMessageWindow()

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽说没有特别的公共设施，\x01",
            "不过却建有很多大型住宅，\x01",
            "并生活着各种各样的居民。\x02",
        )
    )

    CloseMessageWindow()

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "趁着巡视市内的机会，\x01",
            "可以去跟他们打个招呼。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x6, 0x1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46B6")
    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_46F2")

    label("loc_46B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F2")
    OP_68(230, 1250, -38720, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)

    label("loc_46F2")

    SetScenarioFlags(0x44, 7)
    EventEnd(0x5)
    Return()

    # Function_18_430C end

    def Function_19_46F8(): pass

    label("Function_19_46F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17500, -1500, -6700, 0)
    MoveCamera(30, 7, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(55000, 0)
    SetChrPos(0x0, -22900, 0, -7500, 0)
    SetChrPos(0x1, -22900, 0, -7500, 0)
    SetChrPos(0x2, -22900, 0, -7500, 0)
    SetChrPos(0x3, -22900, 0, -7500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -1000, 0, -25000, 180)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 1500, 0, -35000, 0)
    SetChrFlags(0xA, 0x8000)

    def lambda_47CD():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47CD)

    def lambda_47E7():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_47E7)
    OP_68(17500, -2500, -6700, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-29000, -3000, -28500, 0)
    MoveCamera(355, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(22000, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_46F8 end

    def Function_20_4872(): pass

    label("Function_20_4872")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-11000, -5000, -24500, 0)
    MoveCamera(15, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -11000, -6000, -25500, 0)
    SetChrPos(0x102, -10000, -6000, -24500, 270)
    SetChrPos(0x103, -12000, -6000, -24500, 90)
    SetChrPos(0x104, -11000, -6000, -23500, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(25, 25, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0218
    ChrTalk(
        0x102,
        (
            "#0106F……没想到所有的人\x01",
            "都失踪了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x104,
        (
            "#0303F不祥的预感应验了呢…… \x02\x03",

            "#0301F是自发性的离开，\x01",
            "还是被人绑架了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#6P#0206F现阶段的情报实在太少了，\x01",
            "两种可能性都要考虑到。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_4A9B")

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#0003F……这五名失踪人员\x01",
            "说不定只是冰山一角。\x02\x03",

            "#0001F在克洛斯贝尔全市，\x01",
            "很可能已经有相当多的人\x01",
            "失踪了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B10")

    label("loc_4A9B")


    #C0222
    ChrTalk(
        0x101,
        (
            "#12P#0003F……这四名失踪人员\x01",
            "说不定只是冰山一角。\x02\x03",

            "#0001F在克洛斯贝尔全市，\x01",
            "很可能已经有相当多的人\x01",
            "失踪了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B10")


    #C0223
    ChrTalk(
        0x102,
        (
            "#0108F嗯……\x01",
            "到底有多少人\x01",
            "下落不明了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        (
            "#0301F怎么办，罗伊德？\x02\x03",

            "要一个一个找的话，\x01",
            "实在是太勉强了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#12P#0006F嗯……凭我们的人手，\x01",
            "确实是严重不足。\x02\x03",

            "#0008F在这种时候，一科却迫于上层的压力\x01",
            "而无法行动，真是让人头疼啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x103,
        (
            "#6P#0202F不然去找二科的多诺邦警督，\x01",
            "问问他能不能帮忙吧？\x02\x03",

            "我们以前不是也帮过他的忙吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#12P#0003F不行……这应该也很难。\x02\x03",

            "#0001F既然连达德利搜查官都无计可施，\x01",
            "只能前来请求支援科帮忙，\x01",
            "二科想必也承受着相当的压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x103,
        "#6P#0206F原来如此……的确呢。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        (
            "#0108F如此说来，公共安全科\x01",
            "的情况应该也是一样吧……\x02\x03",

            "#0106F如果能借助警队的人力，\x01",
            "情况就会大有改善了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4DC7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4DC7)
    Sleep(50)

    def lambda_4DD7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4DD7)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0230
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "喂，新人们……！\x02\x03",

            "你们没干什么\x01",
            "多余的事吧……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0232
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F哎……\x02\x03",

            "#0001F这声音……莫非是\x01",
            "达德利搜查官吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "什么莫非不莫非的！\x02\x03",

            "你们几个难道又擅自行动，\x01",
            "到鲁巴彻那边捣乱了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0234
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F没、没有……\x02\x03",

            "#0003F我们现在正在专心\x01",
            "调查药物方面的事情呢。\x02\x03",

            "#0001F……请问发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("达德利的声音")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那还用问吗！\x01",
            "他们的事务所……\x02\x03",

            "……咳咳，没什么。\x02\x03",

            "既然不是你们干的，那就没事了。\x01",
            "继续调查你们的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0236
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0237
    ChrTalk(
        0x101,
        "#12P#0013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#0101F是达德利搜查官吗？\x01",
            "发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#12P#0006F这个……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将与达德利的谈话内容\x01",
            "转告给了艾莉等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0241
    ChrTalk(
        0x104,
        "#0301F那是什么意思啊……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#6P#0206F……明显很蹊跷呢。\x02\x03",

            "#0201F难道鲁巴彻商会那里\x01",
            "发生了什么情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        "#12P#0003F很有可能……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0244
    ChrTalk(
        0x104,
        (
            "#0300F既然如此，我们也只能\x01",
            "过去看看情况了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x102,
        (
            "#0103F是啊……虽然已经被警告过，\x01",
            "让我们别再去管黑手党内斗的事情了……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        (
            "#6P#0202F不过，如果失踪人员与黑手党有关，\x01",
            "我们应该就可以名正言顺地展开调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0001F嗯……\x01",
            "赶快前往鲁巴彻商会吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -11500, -6000, -24000, 135)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_20_4872 end

    def Function_21_53B1(): pass

    label("Function_21_53B1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17650, 2000, -2150, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17050, 0)
    SetChrPos(0x101, 17020, 0, -2660, 0)
    SetChrPos(0x102, 17020, 0, -4100, 0)
    SetChrPos(0x103, 18450, 0, -2660, 0)
    SetChrPos(0x104, 18450, 0, -4100, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0248
    ChrTalk(
        0x101,
        (
            "#5P#0000F住宅街的空房……\x01",
            "好像就是这里了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 17570, 0, -1480, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0250
    ChrTalk(
        0x101,
        (
            "#5P#0003F看样子，\x01",
            "房间里好像没人……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(22460, 2000, 7120, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(620, 3000)
    SetCameraDistance(26390, 3000)
    Sleep(3300)

    #C0251
    ChrTalk(
        0x104,
        (
            "#5P#0300F无论怎么看，\x01",
            "这都是间空房子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x103,
        "#5P#0200F没错，完全感觉不到人的气息。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#5P#0100F这间房子好像从十多年前起\x01",
            "就是废宅了。\x02\x03",

            "在我小时候，还流行着一个传闻，\x01",
            "说这里是鬼屋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#5P#0005F哦，还有这种事啊。\x02\x01",

            "#0003F（我都不知道有这回事呢。\x01",
            "  明明和艾莉是同年……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(17650, 2000, -2150, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17050, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0255
    ChrTalk(
        0x101,
        (
            "#5P#0000F总而言之，住宅街的空房，\x01",
            "这样就算确认完毕了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5726")

    #C0256
    ChrTalk(
        0x104,
        (
            "#0300F没错，这样一来，\x01",
            "确认工作就全部完成了……\x02\x03",

            "回去向接待处的\x01",
            "姐姐报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_5748")

    label("loc_5726")


    #C0257
    ChrTalk(
        0x104,
        "#0300F没错，去下一处地方吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5748")

    Sleep(200)
    SetChrPos(0x0, 17510, 0, -2090, 180)
    SetChrPos(0x1, 17510, 0, -2090, 180)
    SetChrPos(0x2, 17510, 0, -2090, 180)
    SetChrPos(0x3, 17510, 0, -2090, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_21_53B1 end

    def Function_22_579C(): pass

    label("Function_22_579C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch25800.itc", 0x1E)
    OP_68(-25370, -3900, -33010, 0)
    MoveCamera(342, 18, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(32990, 0)
    SetChrPos(0x101, -23330, -6000, -35420, 315)
    SetChrPos(0x102, -22290, -6000, -34420, 315)
    SetChrPos(0x103, -22140, -6000, -36580, 315)
    SetChrPos(0x104, -21140, -6000, -35430, 315)
    SetChrPos(0x10, -30260, -5500, -27540, 45)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5872")

    #C0258
    ChrTalk(
        0x102,
        "#11P#0105F（嗯……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5890")

    label("loc_5872")


    #C0259
    ChrTalk(
        0x102,
        "#11P#0103F……嗯～………\x02",
    )

    CloseMessageWindow()

    label("loc_5890")

    TurnDirection(0x102, 0x101, 500)

    #C0260
    ChrTalk(
        0x102,
        (
            "#0100F那个，罗伊德，你打算\x01",
            "拜访这户人家吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    TurnDirection(0x104, 0x102, 500)
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0261
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，说不定小猫的\x01",
            "饲主就在这里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        (
            "#5P#0200F这家可能会有\x01",
            "年幼的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#0103F我觉得应该不会有……\x01",
            "不过还是问问吧…………\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(800)
    TurnDirection(0x102, 0x101, 500)

    #C0264
    ChrTalk(
        0x102,
        (
            "#0100F家里可能没有人，\x01",
            "先按一下门铃，\x01",
            "看看情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#5P#0005F嗯，说得没错。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        (
            "#11P#0300F怎么了，大小姐，\x01",
            "你有点奇怪哦……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-27380, -3400, -31750, 0)
    MoveCamera(350, 39, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(26410, 0)
    SetChrPos(0x101, -27840, -6000, -30320, 315)
    SetChrPos(0x103, -26850, -6000, -31330, 315)
    SetChrPos(0x104, -26030, -6000, -30540, 315)
    SetChrPos(0x102, -25060, -6000, -31540, 315)
    OP_70(0x1, 0xA)
    ClearChrFlags(0x10, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, -28480, -5500, -29370, 1000, 0x0)
    Sleep(300)

    #C0267
    ChrTalk(
        0x101,
        (
            "#0005F#11P（哎，装有导力门铃……\x01",
            "  果然是个富裕的家庭呢。）\x02",
        )
    )

    CloseMessageWindow()
    Sound(801, 0, 100, 0)
    Sleep(1000)
    Sound(811, 0, 100, 0)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x101,
        (
            "#0000F#11P打扰了，我们是警察……\x02\x03",

            "想就某件事进行一下询问，\x01",
            "不知道您现在方便吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0269
    NpcTalk(
        0x10,
        "男性的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1P#N#2S请稍等，马上就来……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 1, 0, 23)
    OP_96(0x101, 0xFFFF9340, 0xFFFFE890, 0xFFFF8990, 0x3E8, 0x0)
    Sleep(800)
    ClearMapObjFlags(0x7, 0x10)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x7)
    OP_95(0x10, -28690, -5500, -28740, 1000, 0x0)
    Sleep(300)

    #C0270
    ChrTalk(
        0x10,
        (
            "#5P我是本宅的\x01",
            "管家海尔玛。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x10,
        "#5P那个……各位是警察吗？\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#0000F#12P是的，其实并没有\x01",
            "什么大不了的事……\x02\x03",

            "请问您府上\x01",
            "有养猫吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x10,
        "#5P您是说……猫吗？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x10,
        (
            "#5P没有，本宅\x01",
            "并没有养猫。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x10,
        (
            "#5P顺便一说，虽然我本人比较喜欢猫，\x01",
            "不过老爷和大小姐却更喜欢狗一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        "#0012F#12P是、是吗，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        "#0306F#12P好像白跑了一趟呢。\x02",
    )

    CloseMessageWindow()
    OP_68(-24190, -3400, -32159, 3000)
    Sleep(3000)
    WaitChrThread(0x102, 1)

    #C0278
    ChrTalk(
        0x102,
        (
            "#0106F#11P（呼……\x01",
            "  真是让人神经紧张啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22430, -6000, -35200, 135)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    OP_49()
    OP_D5(0x1E)
    SetChrFlags(0x10, 0x80)
    OP_70(0x1, 0x0)
    OP_70(0x7, 0x0)
    OP_29(0x8, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_579C end

    def Function_23_5DB6(): pass

    label("Function_23_5DB6")

    OP_96(0x102, 0xFFFFA772, 0xFFFFE890, 0xFFFF7AB8, 0x7D0, 0x0)
    OP_95(0x102, -21500, -6000, -33240, 3000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_23_5DB6 end

    def Function_24_5DE6(): pass

    label("Function_24_5DE6")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xE, 0xFF)
    OP_68(-240, 1200, -33240, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20370, 0)
    SetChrPos(0x101, -750, 0, -32800, 180)
    SetChrPos(0x102, 890, 0, -31800, 180)
    SetChrPos(0x103, -800, 0, -31210, 180)
    SetChrPos(0x104, 800, 0, -33280, 180)
    SetChrPos(0xE, -19170, -5600, -15790, 315)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)

    def lambda_5E9D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5E9D)

    def lambda_5EB2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5EB2)

    def lambda_5EC7():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5EC7)

    def lambda_5EDC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5EDC)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(800)
    EndChrThread(0x103, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)

    #C0279
    ChrTalk(
        0x103,
        "#0200F#11P嗯？那是……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_5F94():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F94)

    def lambda_5FA1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FA1)
    Sleep(10)

    def lambda_5FB1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FB1)
    Sleep(300)
    OP_5A()
    OP_68(-17990, -3520, -17700, 4000)
    MoveCamera(0, 22, 0, 4000)
    SetCameraDistance(18500, 4000)
    Sleep(4000)
    ClearMapObjFlags(0xB, 0x10)
    OP_71(0xB, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0xB)
    OP_95(0xE, -17970, -5610, -17000, 3000, 0x0)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_71(0xB, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0xB)
    Sleep(300)
    OP_68(-11490, -3520, -24200, 3500)
    OP_95(0xE, -11470, -6000, -23510, 3000, 0x0)
    Sleep(300)
    OP_93(0xE, 0xE1, 0x1F4)
    Sleep(200)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(200)

    #C0280
    ChrTalk(
        0xE,
        (
            "玛丽……\x01",
            "……玛丽～……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x12C)
    Sleep(200)

    #C0281
    ChrTalk(
        0xE,
        (
            "呜呜，到底\x01",
            "跑到哪里去了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(200)

    #C0282
    ChrTalk(
        0xE,
        "玛丽，快出来吧～！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-6190, -3520, -17670, 2500)
    MoveCamera(20, 22, 0, 1000)
    OP_95(0xE, -7080, -6000, -21580, 4000, 0x0)

    def lambda_6113():
        OP_95(0xFE, -6360, -2410, -12820, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6113)
    Sleep(1800)
    Fade(800)
    OP_68(-240, 1200, -33240, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20370, 0)
    OP_93(0x0, 0x13B, 0x0)
    OP_93(0x1, 0x13B, 0x0)
    OP_93(0x2, 0x13B, 0x0)
    OP_93(0x3, 0x13B, 0x0)
    OP_0D()

    #C0283
    ChrTalk(
        0x104,
        "#11P#0300F嗯，是刚才问过话的孩子呢。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#11P#0105F那么小的孩子，\x01",
            "竟然会独自一人跑出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯～而且她\x01",
            "的样子好像很奇怪呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xE, 0x1)
    SetChrPos(0x0, 190, 0, -33400, 180)
    SetChrPos(0xE, -15610, 100, 4480, 315)
    BeginChrThread(0xE, 0, 0, 3)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x4)
    OP_4C(0xE, 0xFF)
    SetMapObjFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EndChrThread(0x9, 0x0)
    SetChrPos(0x9, 35280, 0, -4370, 45)
    BeginChrThread(0x9, 0, 0, 1)
    SetScenarioFlags(0x70, 1)
    ModifyEventFlags(0, 1, 0x80)
    Sleep(800)
    EventEnd(0x5)
    Return()

    # Function_24_5DE6 end

    def Function_25_628F(): pass

    label("Function_25_628F")

    OP_4B(0xE, 0xFF)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-15490, 900, 2940, 0)
    MoveCamera(52, 28, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x101, -15850, 0, 1880, 0)
    SetChrPos(0x102, -15980, 0, 170, 0)
    SetChrPos(0x103, -14220, 0, 1940, 0)
    SetChrPos(0x104, -14350, 0, 240, 0)
    SetChrPos(0xE, -15080, 0, 4800, 270)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xE, 0, 0, 26)

    #C0286
    ChrTalk(
        0xE,
        (
            "#5P那孩子真是的……\x01",
            "到底跑到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#12P#0005F你是在找什么吗？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x0)
    OP_93(0xE, 0xB4, 0x1F4)

    #C0288
    ChrTalk(
        0xE,
        "#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#12P#0100F莫非你在寻找\x01",
            "一只小猫吗？\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从外套里\x01",
            "抱出小猫给对方看。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0291
    ChrTalk(
        0xE,
        "#5P#4S玛丽！\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xE, 0xFFFFC2E8, 0x0, 0xA14, 0x1B58, 0x0)
    Sleep(400)
    OP_96(0xE, 0xFFFFC518, 0x0, 0x12C0, 0xBB8, 0x0)
    OP_93(0xE, 0xE1, 0x1F4)
    Sleep(200)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    OP_0D()
    Sleep(300)

    #C0292
    ChrTalk(
        0xE,
        "#5P太好了！还好你没事！\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xE,
        "#5P到底跑到哪里去了啊，真是的……！\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(300)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0294
    ChrTalk(
        0x101,
        (
            "#12P#0000F这样啊……这只猫\x01",
            "原来是你养的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    OP_63(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    def lambda_654C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_654C)
    OP_96(0xF, 0xFFFFC040, 0x0, 0x1040, 0x1770, 0x0)

    def lambda_656D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_656D)
    OP_96(0xF, 0xFFFFC180, 0x0, 0x12D4, 0x1770, 0x0)

    def lambda_658E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_658E)
    OP_96(0xF, 0xFFFFC40A, 0x0, 0x14FA, 0x1770, 0x0)

    def lambda_65AF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_65AF)
    Sleep(300)
    OP_93(0xE, 0xB4, 0x1F4)
    TurnDirection(0xF, 0xE, 300)

    #C0295
    ChrTalk(
        0xE,
        "#5P不、不是的。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xE,
        (
            "#5P因为……玛丽它\x01",
            "还只算是野猫！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x103,
        (
            "#11P#0200F野猫吗？\x01",
            "可是它脖子上套着项圈啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xE,
        (
            "#5P玛丽虽然是只野猫，\x01",
            "不过它是我的朋友。\x01",
            "所以我才给它套上项圈的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0299
    ChrTalk(
        0x104,
        "#11P#0306F为什么要把事情弄得那么复杂啊……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xE,
        "#5P其、其实……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xE1, 0x12C)
    Sleep(300)

    #C0301
    ChrTalk(
        0xE,
        (
            "#5P我虽然很想抱回家养，\x01",
            "可是爸爸肯定不会同意的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0302
    ChrTalk(
        0xE,
        "#5P因为玛丽是……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x0, 0x12C, 0xBB8, 0x320)

    #C0303
    ChrTalk(
        0xE,
        (
            "#5P#4S把爸爸的重要文件\x01",
            "抓坏的犯人！！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xE, 0x13B, 0x1F4)
    BeginChrThread(0xE, 0, 0, 27)

    #C0304
    ChrTalk(
        0xE,
        (
            "#5P呜呜……\x01",
            "萨妮塔都看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xE,
        (
            "#5P玛丽从窗户钻进来，\x01",
            "然后趴在爸爸的文件上午睡……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        (
            "#5P之后就把文件\x01",
            "撕成了碎纸片……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xE,
        (
            "#5P呜呜，呜呜……\x01",
            "对不起啊，爸爸……！\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#12P#0003F…………………………\x02\x03",

            "虽然之后你想把\x01",
            "事情的经过\x01",
            "向爸爸说清楚……\x02\x03",

            "#0000F不过，小猫那时已经离开，\x01",
            "不知跑到哪里去了，对吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "#5P呜呜，呜呜……\x01",
            "………（点头）\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#12P#0000F然后你很担心它，\x01",
            "就出来找它了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        "#5P嗯、嗯………（点头）\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#12P#0104F呼，谜团基本解开了啊。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#0200F罗伊德前辈，真是精彩的推理。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#0300F不过呢，小猫的本性\x01",
            "就是喜欢恶作剧嘛。\x02\x03",

            "想让它老老实实地待着，\x01",
            "大概是不太可能的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#0003F说得也是，但这样一来，\x01",
            "想在你家饲养的话，可能就比较困难了吧……\x02\x03",

            "#0000F不过呢，既然你这么喜欢玛丽，\x01",
            "先把事情的原委向爸爸说清楚如何。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x0)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xE, 0x101, 500)
    Sleep(600)

    #C0316
    ChrTalk(
        0x102,
        (
            "#12P#0100F没错，\x01",
            "我们也会陪你一起去的……\x02\x03",

            "一起把事情解释清楚好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xE,
        "#5P……………（点头）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0350", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_628F end

    def Function_26_6B65(): pass

    label("Function_26_6B65")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BA3")
    OP_95(0xE, -16110, 0, 4800, 1000, 0x0)
    Sleep(500)
    OP_95(0xE, -13570, 0, 4800, 1000, 0x0)
    Sleep(500)
    Jump("Function_26_6B65")

    label("loc_6BA3")

    Return()

    # Function_26_6B65 end

    def Function_27_6BA4(): pass

    label("Function_27_6BA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BE0")
    OP_A6(0xE, 0x0, 0xF, 0x3E8, 0xBB8)
    Sleep(1200)
    OP_A6(0xE, 0x0, 0xF, 0x3E8, 0xBB8)
    Sleep(2200)
    Jump("Function_27_6BA4")

    label("loc_6BE0")

    Return()

    # Function_27_6BA4 end

    def Function_28_6BE1(): pass

    label("Function_28_6BE1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1400, 1700, -2500, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(12300, 0)
    SetChrPos(0x101, 0, 0, -2800, 0)
    SetChrPos(0x102, -1200, 0, -2800, 0)
    SetChrPos(0x103, -1200, 0, -4250, 0)
    SetChrPos(0x104, 0, 0, -4250, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0318
    ChrTalk(
        0x102,
        (
            "#6P#0100F这里就是委托人坎贝尔议员的\x01",
            "宅邸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#11P#0000F好像是『重要人士的搜索委托』吧。\x01",
            "突然接到这样的委托，有些吃惊呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)
    Sleep(300)

    #C0320
    ChrTalk(
        0x104,
        (
            "#12P#0305F话说回来，大小姐的家\x01",
            "好像就在这附近吧。\x02\x03",

            "#0300F坎贝尔这个人的情况，\x01",
            "你了解吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D64():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D64)

    def lambda_6D71():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D71)

    def lambda_6D7E():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6D7E)
    Sleep(300)

    #C0321
    ChrTalk(
        0x102,
        (
            "#5P#0103F因为住得不远，\x01",
            "还算有一定程度的了解……\x02\x03",

            "#0100F坎贝尔议员是个很有野心的人，\x01",
            "一心投入到自己的政治活动中。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#12P#0203F原来如此，\x01",
            "大概能想象得出来。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E32():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E32)
    Sleep(100)

    def lambda_6E42():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E42)

    def lambda_6E4F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E4F)

    def lambda_6E5C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E5C)
    Sleep(400)

    #C0323
    ChrTalk(
        0x101,
        (
            "#11P#0000F好了，总之既然接到了他的委托。\x01",
            "就去打扰一下，听听对方的请求吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -480, 0, -2810, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_29(0x2D, 0x1, 0x0)
    OP_70(0x0, 0xA)
    OP_65(0x2, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_6BE1 end

    def Function_29_6EF1(): pass

    label("Function_29_6EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F71")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0324
    ChrTalk(
        0x101,
        (
            "#0000F哎呀……\x02\x03",

            "还带着小猫呢，\x01",
            "还是不要走得太远吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)
    Return()

    label("loc_6F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7025")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FEA")

    #C0325
    ChrTalk(
        0x101,
        (
            "#0000F这里是城市的北出口。\x02\x03",

            "现在没有离开市区的必要……\x01",
            "还是专心处理市内的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_700F")

    label("loc_6FEA")

    SetChrName("")

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有离开市区的必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_700F")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_709C")
    EventBegin(0x1)

    #C0327
    ChrTalk(
        0x101,
        (
            "#0000F要去阿尔摩利卡村的话，\x01",
            "就要从城市的东出口出去。\x02\x03",

            "绕去东街那边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_709C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7128")
    EventBegin(0x1)

    #C0328
    ChrTalk(
        0x101,
        (
            "#0000F要去乌尔斯拉医院的话，\x01",
            "就要从城市的南出口出去。\x02\x03",

            "先去中央广场，然后穿过\x01",
            "站前街道就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71CD")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7192")

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000F这里是北出口。\x02\x03",

            "不能让琪雅\x01",
            "遭遇到危险，\x01",
            "还是不要离开市区了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_71B7")

    label("loc_7192")

    SetChrName("")

    #A0330
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有离开市区的必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_71B7")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_71CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7291")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_724C")

    #C0331
    ChrTalk(
        0x101,
        (
            "#0003F这里是城市的北出口。\x02\x03",

            "现在还有黑月的事要处理……\x01",
            "……先集中精力在市内进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_727B")

    label("loc_724C")

    SetChrName("")

    #A0332
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在先集中精力，在市内进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_727B")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7291")

    Return()

    # Function_29_6EF1 end

    def Function_30_7292(): pass

    label("Function_30_7292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7312")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0333
    ChrTalk(
        0x101,
        (
            "#0000F哎呀……\x02\x03",

            "还带着小猫呢，\x01",
            "还是不要走得太远吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 20930, 0, -3610, 270)
    EventEnd(0x4)
    Return()

    label("loc_7312")

    Return()

    # Function_30_7292 end

    def Function_31_7313(): pass

    label("Function_31_7313")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7415")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7354")
    Call(0, 22)
    SetScenarioFlags(0x46, 2)
    Jump("loc_7411")

    label("loc_7354")


    #C0334
    ChrTalk(
        0x102,
        (
            "#0109F那个，罗伊德……\x01",
            "都已经问过刚才那个人了，\x01",
            "没必要再来这座住宅了吧？\x02\x03",

            "要是没其它事情的话，\x01",
            "我们还是离开吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#0005F嗯，说得也是……\x01",
            "（该问的已经问完了，\x01",
            "  没必要再继续打扰。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7411")

    TalkEnd(0xFF)
    Return()

    label("loc_7415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_754E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7527")

    #C0336
    ChrTalk(
        0x101,
        (
            "#0005F这里是……？\x01",
            "真是座气派的宅邸呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        (
            "#0105F不过门好像关着呢。\x02\x03",

            "#0109F罗、罗伊德……\x01",
            "如果没什么事情的话，\x01",
            "就不用特意打扰人家了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#0000F说得也是……\x01",
            "这家人好像很有身份。\x02\x03",

            "还是不要冒昧拜访了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        "#0108F…………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 2)
    Jump("loc_754E")

    label("loc_7527")

    SetChrName("")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎没有必要拜访这座宅邸。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_754E")

    TalkEnd(0xFF)
    Return()

    # Function_31_7313 end

    def Function_32_7552(): pass

    label("Function_32_7552")

    Return()

    # Function_32_7552 end

    def Function_33_7553(): pass

    label("Function_33_7553")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_757C")
    Call(0, 21)
    Jump("loc_759B")

    label("loc_757C")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_759B")

    TalkEnd(0xFF)
    Return()

    # Function_33_7553 end

    def Function_34_759F(): pass

    label("Function_34_759F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C0")
    Call(0, 28)
    Return()

    label("loc_75C0")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7744")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76D7")

    #C0342
    ChrTalk(
        0x102,
        (
            "#0105F这里是……\x01",
            "坎贝尔议员的住宅吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#0005F坎贝尔议员？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#0103F是共和国派的首席议员哦。\x01",
            "在政界也算是有分量的人物。\x02\x03",

            "#0100F如果没什么事情的话，\x01",
            "还是不要打扰人家\x01",
            "比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#0000F说得也是……反正也没什么事，\x01",
            "就不要进去打扰了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773C")

    label("loc_76D7")


    #C0346
    ChrTalk(
        0x101,
        (
            "#0005F这里是……\x01",
            "以前好像听艾莉说起过。\x02\x03",

            "#0001F好像是位叫做坎贝尔的\x01",
            "共和国派首席议员\x01",
            "的宅邸……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_773C")

    SetScenarioFlags(0x46, 3)
    Jump("loc_778A")

    label("loc_7744")

    SetChrName("")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是共和国派的坎贝尔议员的宅邸，\x01",
            "没有什么必要前去拜访。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_778A")

    TalkEnd(0xFF)
    Return()

    # Function_34_759F end

    def Function_35_778E(): pass

    label("Function_35_778E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-18070, 2300, 9900, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13550, 0)
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch22200.itc", 0x1F)
    LoadChrToIndex("chr/ch20700.itc", 0x20)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x101, -16860, 0, 16000, 180)
    SetChrPos(0xEF, -17740, 0, 17160, 180)
    SetChrPos(0x153, -18240, 0, 15330, 180)
    SetChrPos(0x11, -15230, 0, 1710, 0)
    SetChrPos(0x12, -16050, 0, 120, 0)
    SetChrPos(0x13, -15630, 0, -920, 0)
    OP_68(-18070, 2300, 7120, 3000)
    SetCameraDistance(13550, 3000)
    BeginChrThread(0x153, 3, 0, 36)
    Sleep(100)
    BeginChrThread(0x0, 3, 0, 36)
    Sleep(100)
    BeginChrThread(0x1, 3, 0, 36)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x153, 3)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0348
    ChrTalk(
        0x153,
        "#1105F#5P啊，有人来了～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(300)
    BeginChrThread(0x13, 3, 0, 37)
    Sleep(1000)

    def lambda_7931():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7931)
    Sleep(50)

    def lambda_7941():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7941)
    Sleep(50)

    def lambda_7951():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7951)

    #C0349
    ChrTalk(
        0x101,
        "#0000F#5P哦，这不是隆嘛。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        "#11P哟，大哥哥，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x12,
        "#11P你们好啊～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A01")

    #C0352
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，你们好。\x02\x03",

            "#0102F一群小孩子，\x01",
            "要去哪里玩吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA3")

    label("loc_7A01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A58")

    #C0353
    ChrTalk(
        0x103,
        (
            "#0202F#5P你们好。\x02\x03",

            "#0205F……一群小孩子，\x01",
            "难道打算出市区吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA3")

    label("loc_7A58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AA3")

    #C0354
    ChrTalk(
        0x104,
        (
            "#0309F#5P你们真有精神啊。\x02\x03",

            "#0300F今天打算去哪里玩啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AA3")


    #C0355
    ChrTalk(
        0x13,
        (
            "#11P那个，我们正要去大圣堂\x01",
            "的主日学校上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#0004F#5P哦，原来如此，\x01",
            "那应该没什么危险吧。\x02\x03",

            "#0002F不过话说回来，\x01",
            "你们去主日学校上课都选在同一天，\x01",
            "关系还真是不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x12,
        "#11P啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x12,
        (
            "#11P我和隆有一次陪蔡特一起玩，\x01",
            "结果不小心玩过头，\x01",
            "最后翘了课呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)

    #C0359
    ChrTalk(
        0x11,
        (
            "#5P哈哈，有什么办法啊。\x01",
            "是蔡特缠着我们，\x01",
            "让我们陪它玩的。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x153,
        "#1110F#5P蔡特很可爱吧～\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x153, 500)

    #C0361
    ChrTalk(
        0x11,
        (
            "#11P……对了，\x01",
            "我们以前都没见过你啊，\x01",
            "你这家伙叫什么名字啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x153,
        "#1101F#5P我是『琪雅』，不是什么『家伙』～！\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x12,
        "#11P嘿，琪雅吗……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x12,
        (
            "#11P我的名字叫亨利。\x01",
            "那个精力过剩的小子是隆，\x01",
            "这个腼腆的家伙是小桃。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x13,
        (
            "#11P那、那个……\x01",
            "请多指教，小琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x153,
        "#1109F#5P嗯！请多指教～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)

    #C0367
    ChrTalk(
        0x11,
        (
            "#5P……喂喂，话说，\x01",
            "现在可不是聊天的时候吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x11,
        (
            "#5P再不快点走的话，\x01",
            "修女就要生气了！\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x12,
        (
            "#11P啊，说得对！\x01",
            "不好意思，罗伊德哥哥。\x01",
            "我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        (
            "#0000F#5P啊，不用在意，\x01",
            "可不要迟到哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 500)

    #C0371
    ChrTalk(
        0x11,
        "#11P那，再见啦～！\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x13,
        "#11P再见～\x02",
    )

    CloseMessageWindow()
    OP_68(-18980, 2300, 8820, 3000)
    BeginChrThread(0x11, 3, 0, 38)
    Sleep(100)
    BeginChrThread(0x12, 3, 0, 38)
    Sleep(150)
    BeginChrThread(0x13, 3, 0, 38)
    Sleep(2000)

    def lambda_7E6D():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7E6D)

    def lambda_7E7A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7E7A)

    def lambda_7E87():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7E87)
    OP_6F(0x79)
    Sleep(2000)

    #C0373
    ChrTalk(
        0x101,
        (
            "#0000F#11P是吗，玛布尔老师……\x01",
            "马上就要开始上课了吧。\x02\x03",

            "#0005F哎，不过住宅街和西街\x01",
            "的授课日是同一天吗？\x02\x03",

            "要是这样的话，我和艾莉在小时候\x01",
            "就应该认识了吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FE8")

    #C0374
    ChrTalk(
        0x102,
        (
            "#0104F#5P和我们那时相比，\x01",
            "现在的学区结构已经改变了。\x02\x03",

            "#0100F这几年来，城市的人口急剧增加，\x01",
            "分区的方法也需要随之变化呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#0000F#11P是这样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8143")

    label("loc_7FE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80A3")

    #C0376
    ChrTalk(
        0x103,
        (
            "#0204F#5P虽然我也不是很清楚，\x01",
            "不过最近几年，学区的结构\x01",
            "或许变得和以前不一样了。\x02\x03",

            "#0202F在人口不断激增的都市中，\x01",
            "这也是很正常的现象。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        "#0000F#11P原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8143")

    label("loc_80A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8143")

    #C0378
    ChrTalk(
        0x104,
        (
            "#0300F#5P我也不是很清楚，\x01",
            "不过，可能是授课日\x01",
            "的分配有了改变吧？\x02\x03",

            "毕竟这个城市的人口好像\x01",
            "增加了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        "#0000F#11P说不定就是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_8143")


    #C0380
    ChrTalk(
        0x153,
        "#1100F#12P……那个～不是要去巴士车站吗？\x02",
    )

    CloseMessageWindow()

    def lambda_8176():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8176)
    Sleep(50)

    def lambda_8186():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8186)
    Sleep(300)

    #C0381
    ChrTalk(
        0x101,
        (
            "#0012F#5P嗯，也对。\x01",
            "差不多也该去那里了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xBD, 2)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -16860, 0, 13000, 180)
    SetChrPos(0x1, -16860, 0, 13000, 180)
    SetChrPos(0x2, -16860, 0, 13000, 180)
    OP_68(-16860, 2000, 13000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_35_778E end

    def Function_36_8259(): pass

    label("Function_36_8259")


    def lambda_825E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_825E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_8259 end

    def Function_37_8278(): pass

    label("Function_37_8278")


    def lambda_827D():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_827D)
    WaitChrThread(0xFE, 1)

    def lambda_829B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_829B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_8278 end

    def Function_38_82A8(): pass

    label("Function_38_82A8")


    def lambda_82AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82AD)
    WaitChrThread(0xFE, 1)

    def lambda_82BE():
        OP_98(0xFE, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82BE)
    Sleep(6000)

    def lambda_82DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_82DB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_82A8 end

    SaveToFile()

Try(main)
