from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レイズ老人",             # 1
        "ペントス",               # 2
        "シンディ",               # 3
        "クレイユ",               # 4
        "ジョアンナ",             # 5
        "レクター",               # 6
        "サニータ",               # 7
        "マリー",                 # 8
        "ヘルマー",               # 9
        "リュウ",                 # 10
        "アンリ",                 # 11
        "モモ",                   # 12
        "中央広場",               # 13
        "西通り",                 # 14
        "行政区",                 # 15
        "住宅街",                 # 16
        "歓楽街",                 # 17
        "東通り",                 # 18
        "旧市街",                 # 19
        "港湾区",                 # 20
        "ＩＢＣ",                 # 21
        "駅前通り",               # 22
        "裏通り",                 # 23
        "ウルスラ間道",           # 24
        "東クロスベル街道",       # 25
        "西クロスベル街道",       # 26
        "マインツ山道",           # 27
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

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "中央広場")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "西通り")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "住宅街")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "歓楽街")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "東通り")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "旧市街")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "駅前通り")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "裏通り")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "マインツ山道")
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
        "Function_7_1D6C",         # 07, 7
        "Function_8_2C2C",         # 08, 8
        "Function_9_2EFE",         # 09, 9
        "Function_10_3616",        # 0A, 10
        "Function_11_375A",        # 0B, 11
        "Function_12_3F99",        # 0C, 12
        "Function_13_40DA",        # 0D, 13
        "Function_14_48A2",        # 0E, 14
        "Function_15_48F7",        # 0F, 15
        "Function_16_494C",        # 10, 16
        "Function_17_49A1",        # 11, 17
        "Function_18_49D8",        # 12, 18
        "Function_19_4DF2",        # 13, 19
        "Function_20_4F6C",        # 14, 20
        "Function_21_5B8C",        # 15, 21
        "Function_22_5FC3",        # 16, 22
        "Function_23_666B",        # 17, 23
        "Function_24_669B",        # 18, 24
        "Function_25_6B74",        # 19, 25
        "Function_26_754C",        # 1A, 26
        "Function_27_758B",        # 1B, 27
        "Function_28_75C8",        # 1C, 28
        "Function_29_78E6",        # 1D, 29
        "Function_30_7CBF",        # 1E, 30
        "Function_31_7D54",        # 1F, 31
        "Function_32_7FC1",        # 20, 32
        "Function_33_7FC2",        # 21, 33
        "Function_34_801A",        # 22, 34
        "Function_35_8229",        # 23, 35
        "Function_36_8E04",        # 24, 36
        "Function_37_8E23",        # 25, 37
        "Function_38_8E53",        # 26, 38
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F57")

    #C0001
    ChrTalk(
        0x8,
        (
            "お前さんらも早く帰ることじゃ。\x01",
            "クロスベルの夜は少々冷えるでな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9E")

    label("loc_F57")


    #C0002
    ChrTalk(
        0x8,
        "おっといかん、日暮れじゃ……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "そろそろ家路につかんとのう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F9E")

    Jump("loc_1D64")

    label("loc_FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_100C")

    #C0004
    ChrTalk(
        0x8,
        (
            "はて、ボンド君といえば\x01",
            "気のいい青年だったはずじゃが。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "彼がどうかしたのかのう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D64")

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_10DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1045")

    #C0006
    ChrTalk(
        0x8,
        "これでは議会も纏まるまいて。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DA")

    label("loc_1045")


    #C0007
    ChrTalk(
        0x8,
        (
            "帝国派は帝国の利権を反映し、\x01",
            "共和国派は共和国のための政策を推す。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "……まるでクロスベルで両大国が\x01",
            "おしくらマンジュウをしとるようじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10DA")

    Jump("loc_1D64")

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_118D")

    #C0009
    ChrTalk(
        0xFE,
        (
            "そこの屋敷に、証券マンをしておる\x01",
            "ボンド君という男がいるんじゃが。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "記念祭の後でなにやら\x01",
            "失敗をしてしもうたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "一時期酷くしょげておったよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D64")

    label("loc_118D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1202")

    #C0012
    ChrTalk(
        0x8,
        "ふぉふぉ、今日も良い天気じゃのう。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "どうかな、お嬢ちゃんも\x01",
            "わしといっしょに日向ぼっこせんか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D64")

    label("loc_1202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1294")

    #C0014
    ChrTalk(
        0x8,
        (
            "クロスベルの政治は\x01",
            "正義感だけで\x01",
            "どうこうできるものではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "良くも悪くも狡猾な連中に\x01",
            "任せておくべきじゃろうて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1394")

    label("loc_1294")


    #C0016
    ChrTalk(
        0x8,
        (
            "自治州議会に集う議員たちは\x01",
            "みな狡猾といってよい連中ばかりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "なにせクロスベルの政治は\x01",
            "帝国や共和国の思惑もあって\x01",
            "複雑じゃからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "まれに正義感の強い若者が\x01",
            "議員に当選してしもうたりも\x01",
            "するのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "まあ上手くは行かぬものじゃ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1394")

    Jump("loc_1D64")

    label("loc_1399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_14EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1426")

    #C0020
    ChrTalk(
        0x8,
        (
            "ここでのんびりしておると\x01",
            "よくピザの配達人を見かけるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "近頃はハイカラなものが\x01",
            "はやっとるようじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E5")

    label("loc_1426")


    #C0022
    ChrTalk(
        0x8,
        (
            "ふむ、近頃は\x01",
            "出前サービスを取るのが\x01",
            "はやりらしいのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "ここでのんびりしておると\x01",
            "よくピザの配達人を見かけるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "わしらの若い頃に較べると\x01",
            "随分ハイカラになったものじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14E5")

    Jump("loc_1D64")

    label("loc_14EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15C9")

    #C0025
    ChrTalk(
        0x8,
        (
            "ほう、お主らは\x01",
            "あの子を知っておるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "わしはてっきり\x01",
            "寝ぼけておるのかと思ったが……\x01",
            "どうやら夢ではなかったようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "なにやら不思議な子じゃったが\x01",
            "一体どこから来たのかのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1712")

    label("loc_15C9")


    #C0028
    ChrTalk(
        0x8,
        (
            "先日不思議な\x01",
            "女の子に会ったんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "綺麗なドレスを着た、\x01",
            "可愛らしいスミレ髪の娘でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "いつの間にか\x01",
            "目の前に立っておったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "じゃが、わしに一言挨拶しては\x01",
            "ふらりと消えてしもうたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0005Fそれって……\x01",
            "あの人形工房で見かけた子かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#0200Fレンちゃん、でしたか。\x01",
            "時折街にも来ているようですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1712")

    Jump("loc_1D64")

    label("loc_1717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1787")

    #C0034
    ChrTalk(
        0x8,
        "自治州議会も近い時期……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ふぉふぉ、政治家や議員が\x01",
            "忙しそうにする季節じゃのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1851")

    label("loc_1787")


    #C0036
    ChrTalk(
        0x8,
        "ほうほう、今日も良い天気じゃな。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "先ほどキャンベル議員が\x01",
            "車で出勤するところを見かけたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "ふぉふぉ、そういえば\x01",
            "自治州議会も近いのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "政治家や議員にとっても\x01",
            "忙しい時期じゃて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1851")

    Jump("loc_1D64")

    label("loc_1856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_198D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18C6")

    #C0040
    ChrTalk(
        0xFE,
        "あの事故は酷かったのう……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "確か小さい娘さんが\x01",
            "目をやられたという話じゃったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1988")

    label("loc_18C6")


    #C0042
    ChrTalk(
        0xFE,
        "４～５年ほど前じゃったか……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "表通りで運搬車が\x01",
            "大事故を起こしたことがあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "あれは酷かった……\x01",
            "爆発までしおってなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "近くに居た市民まで\x01",
            "巻き込まれてしもうたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1988")

    Jump("loc_1D64")

    label("loc_198D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19E7")

    #C0046
    ChrTalk(
        0x8,
        (
            "子供だけでお出掛けは危険じゃ。\x01",
            "大人が気をつけてやらんとのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9C")

    label("loc_19E7")


    #C0047
    ChrTalk(
        0x8,
        (
            "ふむ、近頃\x01",
            "そこのおうちの小さい娘さんが\x01",
            "よくお出掛けしておるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "とことこと遠くまで\x01",
            "行っておるようじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "子供だけで遠出は危険じゃぞ。\x01",
            "気をつけんとのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A9C")

    Jump("loc_1D64")

    label("loc_1AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AE7")

    #C0050
    ChrTalk(
        0x8,
        (
            "ふぉふぉ、平和じゃのう。\x01",
            "結構な事じゃて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B80")

    label("loc_1AE7")


    #C0051
    ChrTalk(
        0x8,
        "お若いの、朝の散歩かね。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "ふぉふぉ、早朝に気が向けば\x01",
            "ＩＢＣのビルを訪れてみると良い。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "朝霧の中に佇むＩＢＣビルは\x01",
            "なかなか趣きがあるぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B80")

    Jump("loc_1D64")

    label("loc_1B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BF0")

    #C0054
    ChrTalk(
        0x8,
        (
            "この住宅街はクロスベル市でも\x01",
            "一番治安が良いんじゃ。\x01",
            "安心して昼寝ができるわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9C")

    label("loc_1BF0")


    #C0055
    ChrTalk(
        0x8,
        (
            "この住宅街はクロスベル市でも\x01",
            "一番治安が良いんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "なにせ政治家や財界人も\x01",
            "多く住んでおるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "警察もわしら住人に気を遣って\x01",
            "おるのかのう、ふぉふぉ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C9C")

    Jump("loc_1D64")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D0A")

    #C0058
    ChrTalk(
        0x8,
        "お若いの、散歩かね。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "この辺りは静かな住宅街じゃ。\x01",
            "散歩にはもってこいじゃろうて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D64")

    label("loc_1D0A")


    #C0060
    ChrTalk(
        0x8,
        "ふぁ～ああ……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "おお、今日も日差しが心地よいのう。\x01",
            "日向ぼっこには丁度よいて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D64")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_DF8 end

    def Function_7_1D6C(): pass

    label("Function_7_1D6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DD7")

    #C0062
    ChrTalk(
        0x9,
        "４ヵ月後には市長選もある……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "バラマキが横行するのも\x01",
            "無理はなかろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E95")

    label("loc_1DD7")


    #C0064
    ChrTalk(
        0x9,
        (
            "本年度予算もかなり\x01",
            "色が付いたものになったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "見てくれのいい案件を優先し、\x01",
            "議員に都合のいい組合に予算を回す……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "一言で言えば人気取り、\x01",
            "いわゆるバラマキというわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1E95")

    Jump("loc_2C28")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1EFD")

    #C0067
    ChrTalk(
        0x9,
        "今日はあまり警官を見かけないな。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "皆してどこかに\x01",
            "行ってしまったのだろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_1EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1FE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F7C")

    #C0069
    ChrTalk(
        0x9,
        (
            "キャンベル議員も色々と\x01",
            "画策されたようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "相手があのハルトマン議長では\x01",
            "旗色も悪かろうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FDC")

    label("loc_1F7C")


    #C0071
    ChrTalk(
        0x9,
        (
            "ふむ、キャンベル議員が\x01",
            "苦戦しておられると聞く……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        "やはり帝国派の優位は揺るがぬか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1FDC")

    Jump("loc_2C28")

    label("loc_1FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_20E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2043")

    #C0073
    ChrTalk(
        0x9,
        "今年は市長選の年だな。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "マクダエル市長は\x01",
            "出馬なされるのだろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E1")

    label("loc_2043")


    #C0075
    ChrTalk(
        0x9,
        (
            "今年は５年に一度の\x01",
            "市長選の年に当たっているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "今後５年間の自治州代表を\x01",
            "決める選挙……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "予算議会が流れたりして\x01",
            "ケチが付かなければ良いが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20E1")

    Jump("loc_2C28")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_216D")

    #C0078
    ChrTalk(
        0x9,
        (
            "逮捕された例の市長秘書は\x01",
            "拘置所の方に収監されたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "……まったくあれは\x01",
            "とんでもない事件だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220C")

    label("loc_216D")


    #C0080
    ChrTalk(
        0x9,
        "そういえば……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "逮捕された例の市長秘書、\x01",
            "拘置所の方に収監されたそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "だがいまだに黙秘を続けているという。\x01",
            "まったくとんでもない男だな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_220C")

    Jump("loc_2C28")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_22B8")

    #C0083
    ChrTalk(
        0x9,
        "うおっほん、君たち……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "先ほどジオフロントに\x01",
            "入っていなかったかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "いかんよ、あそこは\x01",
            "子供の遊び場ではない。\x01",
            "危険だからやめておきなさい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_22B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2382")

    #C0086
    ChrTalk(
        0x9,
        (
            "私はＩＢＣの運営している\x01",
            "《ミシュラム》にも\x01",
            "投資しているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "うおっほん……\x01",
            "スポンサー優待として沢山の\x01",
            "《みっしぃ》グッズを持っているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        "#0200F（……うらやましい………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_2382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2414")

    #C0089
    ChrTalk(
        0x9,
        (
            "市長は最近、各方面の要人と\x01",
            "会談を重ねられているらしい……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "もうお年だというのに\x01",
            "衰えをみせようとしない、尊敬すべき方だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_25A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24AC")

    #C0091
    ChrTalk(
        0x9,
        (
            "劇団アルカンシェルの\x01",
            "チケットには３種類あるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "Ｓ席のチケットなど、\x01",
            "競売で２００倍の値が付くほど\x01",
            "超々人気なのだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A2")

    label("loc_24AC")


    #C0093
    ChrTalk(
        0x9,
        (
            "劇団アルカンシェルのチケットは\x01",
            "高価なことで有名だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "チケットにはＢ席、\x01",
            "Ａ席、Ｓ席の３種類があるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "ちなみに劇場には\x01",
            "特別な貴賓席も用意されている\x01",
            "そうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "ここは劇団のスポンサーや\x01",
            "特別な賓客しか使用できないのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_25A2")

    Jump("loc_2C28")

    label("loc_25A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2668")

    #C0097
    ChrTalk(
        0x9,
        "近頃よくピザ屋の出前を見かけるな。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "そこの通りを走っていってな、\x01",
            "住宅地の端の、誰もいない路上に\x01",
            "立っていたりするのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "ふうむ……一体誰が\x01",
            "受け取っているのだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_2668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_27A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26F5")

    #C0100
    ChrTalk(
        0x9,
        (
            "クロスベル大聖堂や\x01",
            "鉱山町マインツ方面へ向かうなら\x01",
            "この住宅街を抜けるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "ま、市民なら覚えておく事だな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_279C")

    label("loc_26F5")


    #C0102
    ChrTalk(
        0x9,
        (
            "この住宅街は\x01",
            "街の一番北西に位置している。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "そこの通りを抜ければ\x01",
            "街の北口に出られるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "クロスベル大聖堂や\x01",
            "鉱山町マインツ方面へ向かう\x01",
            "山道があるのだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_279C")

    Jump("loc_2C28")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2843")

    #C0105
    ChrTalk(
        0x9,
        (
            "地上４０階となると\x01",
            "度肝を抜かれる高さなのだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "ふふ、クロスベルにまた１つ\x01",
            "観光スポットが生まれるわけだ。\x01",
            "完成が楽しみだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2981")

    label("loc_2843")


    #C0107
    ChrTalk(
        0x9,
        (
            "いまクロスベルで建設されている\x01",
            "新市庁舎ビルは\x01",
            "世界最高の近代ビルディングだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "完成すると、なんと\x01",
            "地上４０階の建物になるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "市庁の機能は全て入るほか、\x01",
            "レストランやテナントスペースも\x01",
            "設けられる予定となっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "ふふ……私も事業家として\x01",
            "一部の事業に参加していてな。\x01",
            "完成を楽しみにしているのだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2981")

    Jump("loc_2C28")

    label("loc_2986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A14")

    #C0111
    ChrTalk(
        0x9,
        (
            "キャンベル先生は\x01",
            "共和国派の議員を纏める\x01",
            "大物政治家なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "あのハルトマン議長の\x01",
            "ライバル、という事になるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEF")

    label("loc_2A14")


    #C0113
    ChrTalk(
        0x9,
        (
            "うおっほん……そこの角地にある\x01",
            "大きな邸宅を知っているかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "共和国派議員筆頭、\x01",
            "キャンベル先生のお宅だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "朝はたまに\x01",
            "立派な導力車が止まっていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "事務所に出勤なさる\x01",
            "様子を見ることができるのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AEF")

    Jump("loc_2C28")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B60")

    #C0117
    ChrTalk(
        0x9,
        (
            "この辺りに暮らしているのは\x01",
            "上流階級の者ばかりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "ま、かくいう私も\x01",
            "その一人だがね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C28")

    label("loc_2B60")


    #C0119
    ChrTalk(
        0x9,
        (
            "うおっほん……この辺りは\x01",
            "高級な住宅が並んでいるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "クロスベルは地価が高いからな、\x01",
            "邸宅は中々ミラが掛かってしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "この辺りに暮らしているのは\x01",
            "上流階級の者ばかりと言えるだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C28")

    TalkEnd(0xFE)
    Return()

    # Function_7_1D6C end

    def Function_8_2C2C(): pass

    label("Function_8_2C2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2CD5")

    #C0122
    ChrTalk(
        0xA,
        (
            "クレイユさんの所のご主人、\x01",
            "行方不明になっちゃったってホント？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0123
    ChrTalk(
        0xA,
        (
            "な、なんだか心配よね。\x01",
            "あたしも様子を見に行こうかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xA)
    Jump("loc_2EFA")

    label("loc_2CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2D57")

    #C0124
    ChrTalk(
        0xA,
        (
            "掃除はテキパキすませて\x01",
            "お茶にしよっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "今日はパパが家にいるんだもん。\x01",
            "たまにはのんびり団欒したいよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFA")

    label("loc_2D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2DC9")

    #C0126
    ChrTalk(
        0xA,
        (
            "そういえばアンリは\x01",
            "どこ行っちゃったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "パパには絶対外出するなって\x01",
            "言われてたのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFA")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2E6A")

    #C0128
    ChrTalk(
        0xA,
        (
            "そういえば、最新の\x01",
            "クロスベルタイムズ見た？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        "うちの弟が載ってたの。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "それを見て、パパもうカンカン！\x01",
            "アンリも馬鹿な事したわよね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EFA")

    label("loc_2E6A")


    #C0131
    ChrTalk(
        0xA,
        (
            "お婆ちゃんに\x01",
            "朝の掃除を命じられちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "ふぁああ～、眠いけど\x01",
            "しょうがないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "どぉれ、ちゃちゃっと\x01",
            "済ましちゃおうかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2EFA")

    TalkEnd(0xFE)
    Return()

    # Function_8_2C2C end

    def Function_9_2EFE(): pass

    label("Function_9_2EFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_303F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F84")

    #C0134
    ChrTalk(
        0xB,
        (
            "ソフィアさんの旦那さんは\x01",
            "とても働き者な方ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        (
            "今朝も早くから\x01",
            "お出掛けになったみたいでしたの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303A")

    label("loc_2F84")


    #C0136
    ChrTalk(
        0xB,
        (
            "しゃわわ……\x01",
            "今日もいい天気ですわねえ……㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0137
    ChrTalk(
        0xB,
        (
            "そういえば、ハロルドさんは\x01",
            "今朝早くに導力車で\x01",
            "お出掛けになったみたいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        "なんだかお急ぎみたいでしたの。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_303A")

    Jump("loc_3612")

    label("loc_303F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_337D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_31BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3169")

    #C0139
    ChrTalk(
        0xFE,
        (
            "あら、さっきサニータと\x01",
            "うちにいらしていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "主人のお知り合いですの？\x01",
            "ふふ、中でお茶でもいかが？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0005Fあ、どうぞお構いなく。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0100Fマリーちゃんを\x01",
            "大事にしてあげてくださいね。\x02",
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
            "マリー……？\x01",
            "どなたかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 3)
    Jump("loc_31BA")

    label("loc_3169")


    #C0144
    ChrTalk(
        0xFE,
        (
            "うちにマリーなんて子は\x01",
            "いなかったと思いますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "……どなたかしら……？\x02",
    )

    CloseMessageWindow()

    label("loc_31BA")

    Jump("loc_3378")

    label("loc_31BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_3243")

    #C0146
    ChrTalk(
        0xFE,
        (
            "あら……サニータが\x01",
            "出て行ったみたいですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "最近よくどこかに出かけていきますの。\x01",
            "何をしているのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3378")

    label("loc_3243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_32B1")

    #C0148
    ChrTalk(
        0xB,
        (
            "今では私も\x01",
            "一通りの家事ができますのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "ふふ、これでも頑張って\x01",
            "お勉強したんですもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3378")

    label("loc_32B1")


    #C0150
    ChrTalk(
        0xB,
        "私、実家は大きなお屋敷でしたの。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "メイドや使用人がたくさんいて\x01",
            "家事なんてした事なかったんですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "結婚してからは\x01",
            "戸惑う事ばかりでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        "今の生活も中々楽しいものですの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3378")

    Jump("loc_3612")

    label("loc_337D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_34BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_33E9")

    #C0154
    ChrTalk(
        0xB,
        (
            "上の通りのソフィアさんは\x01",
            "とってもステキな方ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        "私、憧れちゃいますわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_33E9")


    #C0156
    ChrTalk(
        0xB,
        (
            "上の通りのソフィアさんは\x01",
            "とても料理がお上手なんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "そのうえご主人のお仕事を\x01",
            "手伝ってらっしゃるそうですのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        "すごいですわねぇ……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "私、主人の仕事なんて\x01",
            "さっぱり分かりませんもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_34B7")

    Jump("loc_3612")

    label("loc_34BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3527")

    #C0160
    ChrTalk(
        0xB,
        (
            "花は愛情を込めると\x01",
            "立派に咲くといいますものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        "うふふ、たーんと大きくなれですの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3612")

    label("loc_3527")


    #C0162
    ChrTalk(
        0xB,
        (
            "しゃわわ……\x01",
            "お花に水をやりませんと。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0163
    ChrTalk(
        0xB,
        (
            "うふふ、こちらの花壇は\x01",
            "去年の春にいただいた物ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xB,
        (
            "ほら見てくださる？\x01",
            "とても綺麗にお花を付けましたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "私、もしかしてお水やりの\x01",
            "才能があるのかもしれませんわ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_3612")

    TalkEnd(0xFE)
    Return()

    # Function_9_2EFE end

    def Function_10_3616(): pass

    label("Function_10_3616")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_365E")

    #C0166
    ChrTalk(
        0xC,
        (
            "…………………………\x01",
            "後で問い合わせてみないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3756")

    label("loc_365E")


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
            "#0105Fジョアンナ？\x01",
            "どうかしたの……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 750)

    #C0170
    ChrTalk(
        0xC,
        (
            "いえ……今日は\x01",
            "クロスベルタイムズの発刊日なのに\x01",
            "届いていないもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "………………………………\x01",
            "後で問い合わせてみます。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x13B, 0x2EE)
    SetChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3756")

    TalkEnd(0xFE)
    Return()

    # Function_10_3616 end

    def Function_11_375A(): pass

    label("Function_11_375A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE4")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3803")
    SetChrPos(0x102, -5250, -6000, -39000, 180)
    Jump("loc_384A")

    label("loc_3803")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3829")
    SetChrPos(0x103, -5250, -6000, -39000, 180)
    Jump("loc_384A")

    label("loc_3829")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_384A")
    SetChrPos(0x104, -5250, -6000, -39000, 180)

    label("loc_384A")

    FadeToBright(500, 0)
    OP_0D()

    #C0172
    ChrTalk(
        0x153,
        (
            "#1110F#5Pあー、あのトキの\x01",
            "ヘンなヒト！\x02",
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
            "#3509Fよう、ちびっ子じゃんか。\x01",
            "また会ったなァ～♪\x02\x03",

            "#3502Fうりうり、元気してたか？\x02",
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
            "レクターはキーアの頭をがしがしとなでた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0175
    ChrTalk(
        0x153,
        "#1105F#5Pおー、くすぐったーい。\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0011Fレクターさん……\x01",
            "まだクロスベルにいたんですね。\x02\x03",

            "#0006Fしかもまた釣りをしてるし……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A29")

    #C0177
    ChrTalk(
        0x102,
        (
            "#0111F#5Pというか……貴方は本当に\x01",
            "何者なんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC0")

    label("loc_3A29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A80")

    #C0178
    ChrTalk(
        0x103,
        (
            "#0211F#5Pというか、本当に何者なのか\x01",
            "気になっているのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC0")

    label("loc_3A80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3AC0")

    #C0179
    ChrTalk(
        0x104,
        (
            "#0301F#5Pつーかアンタ、\x01",
            "本当に何者なんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC0")


    #C0180
    ChrTalk(
        0xD,
        (
            "#3510Fうむ、それはアレだな！\x01",
            "帝国の───以下省略！！\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#0006F（なんて誤魔化し方だ……）\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x153,
        (
            "#1109F#5Pあははは！\x01",
            "やっぱりヘンなヒトー！\x02\x03",

            "#1110F……でもよかったー。\x01",
            "キーア、ぜんぜん\x01",
            "おぼえてるヒトいないんだもん。\x02\x03",

            "#1108Fロイドと初めてあったトキ？\x01",
            "……がユメみたいで、さいきん\x01",
            "分かんなくなってきちゃったー。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xD,
        (
            "#3505Fなるほどなぁ………\x02\x03",

            "#3504F……そいつは多分\x01",
            "『幸せ』って名前をしてるんだ。\x02\x03",

            "#3500F覚えとくといいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x153,
        (
            "#1105F#5Pシアワセ……？\x02\x03",

            "#1104Fんー……なんかよくわかんないケド\x01",
            "キーアたのしーし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0185
    ChrTalk(
        0x153,
        (
            "#1109F#5Pん、わかんないケド\x01",
            "わかったー！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        "#3509Fナハハ、なんじゃそりゃ～♪\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#0012F（何だか２人だけで\x01",
            "  話がまとまっている……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DC5")

    #C0188
    ChrTalk(
        0x102,
        (
            "#0109F#5P（ま、まあ、キーアちゃんも\x01",
            "  納得してるみたいだし……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E26")

    #C0189
    ChrTalk(
        0x103,
        (
            "#0202F#5P（まあ、キーアが納得しているなら\x01",
            "  それでもいいのでは……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7C")

    label("loc_3E26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E7C")

    #C0190
    ChrTalk(
        0x104,
        (
            "#0302F#5P（ま、キー坊が納得してるなら\x01",
            "  それでもいいんじゃね？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E7C")

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
    Jump("loc_3F95")

    label("loc_3EE4")


    #C0191
    ChrTalk(
        0xD,
        (
            "#3510Fしかしこの辺りは\x01",
            "のどかでいい住宅街だなァ。\x02\x03",

            "#3507Fここはやっぱミミズか？\x01",
            "それともアカムシの方が釣れんのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#0006F知りませんよ……\x01",
            "自分で試してみてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F95")

    TalkEnd(0xFE)
    Return()

    # Function_11_375A end

    def Function_12_3F99(): pass

    label("Function_12_3F99")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x322, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FE7")
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には固く鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_40D7")

    label("loc_3FE7")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02\x03",

            "ジオフロントＢ区画の鍵で\x01",
            "扉を開くことができそうだ。\x07\x00\x02",
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
            "鍵を使用する\x01",      # 0
            "使用しない\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_409B"),
        (1, "loc_40D2"),
        (SWITCH_DEFAULT, "loc_40D7"),
    )


    label("loc_409B")

    Sound(809, 0, 100, 0)
    SetChrName("")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉の鍵が外れた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x86, 1)
    Jump("loc_40D7")

    label("loc_40D2")

    Jump("loc_40D7")

    label("loc_40D7")

    EventEnd(0x3)
    Return()

    # Function_12_3F99 end

    def Function_13_40DA(): pass

    label("Function_13_40DA")

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
            "#6P#0003Fしかし、まさかこんな場所で\x01",
            "暮らしているなんて……\x02\x03",

            "#0001Fちょっと放っておけないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        (
            "#6P#0106Fええ、まだ日曜学校に\x01",
            "行ってそうな歳みたいだし……\x02\x03",

            "#0101Fティオちゃん、彼は幾つなの？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4312():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4312)
    Sleep(50)

    def lambda_4322():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4322)
    Sleep(300)

    #C0198
    ChrTalk(
        0x103,
        (
            "#11P#0200F確か１３だったはずです。\x02\x03",

            "わたしの１つ年下ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#12P#0001Fうーん、何とか財団の方で\x01",
            "引き取ってもらった方が……\x02\x03",

            "#0008Fでも、大損害とか言ってたし、\x01",
            "逆に知らせない方がいいのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        (
            "#0306F#5Pハッ、放っておけって。\x02\x03",

            "#0300Fしたたかそうなガキだったし、\x01",
            "あの様子じゃ行動力もあんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        (
            "#11P#0203Fまあ、天才的な頭脳を\x01",
            "持っているのは確かですね。\x02\x03",

            "#0202Fちょっと抜けた所があるので\x01",
            "専門外のわたしにも\x01",
            "付け込む隙がありますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#12P#0006Fうーん……\x02",
    )

    CloseMessageWindow()

    def lambda_450D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_450D)
    Sleep(50)

    def lambda_451D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_451D)
    Sleep(300)

    #C0203
    ChrTalk(
        0x102,
        (
            "#6P#0104Fふふ、あなたも苦労性ね。\x02\x03",

            "#0100Fとりあえず、彼のことは\x01",
            "気にかけておきましょう。\x02\x03",

            "定期的に訪ねてみるのも\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ……そうするか。\x02\x03",

            "#0003F──まあいい。\x01",
            "それはともかく《銀#2Rイン#》か。\x02\x03",

            "#0001Fどうやら《星見の塔》で\x01",
            "待っているみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_472F")

    #C0205
    ChrTalk(
        0x103,
        (
            "#0201F#5P以前、手前まで行った時は\x01",
            "警備隊のフェンスによって\x01",
            "封鎖されていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        (
            "#0304F#5Pま、あの程度のフェンスなら\x01",
            "簡単に乗り越えられるだろ。\x02\x03",

            "#0300F必要ならソーニャ副司令に\x01",
            "連絡して許可を貰えばいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47E3")

    label("loc_472F")


    #C0207
    ChrTalk(
        0x103,
        (
            "#0201F#5Pたしかウルスラ間道の\x01",
            "途中から見えた塔ですね？\x02\x03",

            "どうやって行くんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#0300F#5P確か街道の途中に\x01",
            "森に入る脇道があったはずだ。\x02\x03",

            "そっちの先にあるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E3")


    #C0209
    ChrTalk(
        0x102,
        (
            "#6P#0103Fそうね……\x02\x03",

            "#0101Fいずれにせよ、準備を整えて\x01",
            "向かった方がいいでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#12P#0001Fああ……\x01",
            "罠の可能性だってある。\x02\x03",

            "万全の準備をして出発しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -4800, -6000, -36700, 0)
    SetScenarioFlags(0x83, 7)
    EventEnd(0x5)
    Return()

    # Function_13_40DA end

    def Function_14_48A2(): pass

    label("Function_14_48A2")


    def lambda_48A7():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48A7)

    def lambda_48C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48C1)
    WaitChrThread(0xFE, 1)

    def lambda_48D6():
        OP_95(0xFE, -4800, -6000, -35400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_48D6)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_14_48A2 end

    def Function_15_48F7(): pass

    label("Function_15_48F7")


    def lambda_48FC():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48FC)

    def lambda_4916():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4916)
    WaitChrThread(0xFE, 1)

    def lambda_492B():
        OP_95(0xFE, -5600, -6000, -36700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_492B)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_15_48F7 end

    def Function_16_494C(): pass

    label("Function_16_494C")


    def lambda_4951():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4951)

    def lambda_496B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_496B)
    WaitChrThread(0xFE, 1)

    def lambda_4980():
        OP_95(0xFE, -4100, -6000, -36700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4980)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_16_494C end

    def Function_17_49A1(): pass

    label("Function_17_49A1")


    def lambda_49A6():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49A6)

    def lambda_49C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49C0)
    WaitChrThread(0xFE, 1)
    OP_93(0x101, 0x59, 0x1F4)
    Return()

    # Function_17_49A1 end

    def Function_18_49D8(): pass

    label("Function_18_49D8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C3E")
    Sleep(500)

    #A0211
    AnonymousTalk(
        0x101,
        (
            "#0004Fクロスベル市北西エリア……\x02\x03",

            "#0000Fこの辺りは昔から高級住宅地なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #A0212
    AnonymousTalk(
        0x104,
        "#0305Fなるほど、大きなお屋敷ばっかだな。\x02",
    )

    CloseMessageWindow()

    #A0213
    AnonymousTalk(
        0x102,
        "#0109F……そ、そうねぇ。\x02",
    )

    CloseMessageWindow()

    #A0214
    AnonymousTalk(
        0x103,
        (
            "#0205F……………………？\x01",
            "（エリィさんの様子がおかしい気が。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4C3E")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "住宅街は、街の北西にある静かな街区です。\x02",
        )
    )

    CloseMessageWindow()

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特に施設などはありませんが、\x01",
            "大きな邸宅が多く、\x01",
            "それぞれに住民たちが生活しています。\x02",
        )
    )

    CloseMessageWindow()

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "市内の見回りを兼ねて\x01",
            "一度話しかけてみると良いでしょう。\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DB0")
    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_4DEC")

    label("loc_4DB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DEC")
    OP_68(230, 1250, -38720, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)

    label("loc_4DEC")

    SetScenarioFlags(0x44, 7)
    EventEnd(0x5)
    Return()

    # Function_18_49D8 end

    def Function_19_4DF2(): pass

    label("Function_19_4DF2")

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

    def lambda_4EC7():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4EC7)

    def lambda_4EE1():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4EE1)
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

    # Function_19_4DF2 end

    def Function_20_4F6C(): pass

    label("Function_20_4F6C")

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
            "#0106F……まさか全員、\x01",
            "行方不明になってるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x104,
        (
            "#0303F嫌な予感、的中だな……\x02\x03",

            "#0301F自発的に消えちまったのか、\x01",
            "それとも拉致されちまったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        (
            "#6P#0206F現時点では情報が少なすぎて\x01",
            "どちらの可能性も考えられますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_51DC")

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#0003F……失踪した５人については\x01",
            "氷山の一角かもしれない。\x02\x03",

            "#0001Fクロスベル市全体では\x01",
            "かなりの人数が失踪している\x01",
            "可能性が高そうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526D")

    label("loc_51DC")


    #C0222
    ChrTalk(
        0x101,
        (
            "#12P#0003F……失踪した４人については\x01",
            "氷山の一角かもしれない。\x02\x03",

            "#0001Fクロスベル市全体では\x01",
            "かなりの人数が失踪している\x01",
            "可能性が高そうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_526D")


    #C0223
    ChrTalk(
        0x102,
        (
            "#0108Fええ……\x01",
            "一体どれだけの人たちが\x01",
            "消えてしまったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        (
            "#0301Fどうする、ロイド。\x02\x03",

            "一人一人を捜すってのは\x01",
            "さすがに難しそうだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#12P#0006Fああ……こちらの手が\x01",
            "圧倒的に不足している。\x02\x03",

            "#0008Fこうなると上からの圧力で\x01",
            "一課が動けないのが痛いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x103,
        (
            "#6P#0202Fでしたら二課のドノバン警部に\x01",
            "相談してみてはどうでしょう？\x02\x03",

            "以前、手伝った貸しもありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#12P#0003Fいや……難しいと思う。\x02\x03",

            "#0001Fダドリー捜査官がわざわざ、\x01",
            "支援課を頼ってきている以上、\x01",
            "二課にも圧力が掛かっているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x103,
        "#6P#0206Fなるほど……確かに。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        (
            "#0108Fとなると広域防犯課も\x01",
            "状況は同じでしょうね……\x02\x03",

            "#0106F警官隊のマンパワーが使えれば\x01",
            "すごく助かるのだけど……\x02",
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

    def lambda_5558():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5558)
    Sleep(50)

    def lambda_5568():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5568)
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
            "#0001Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おい、新米ども……！\x02\x03",

            "まさか何かしでかしたんじゃ\x01",
            "ないだろうな……！？\x02",
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
            "#0011Fへ……\x02\x03",

            "#0001Fもしかしてその声は\x01",
            "ダドリー捜査官ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もしかしても何もない！\x02\x03",

            "お前たち、ルバーチェに何か\x01",
            "ちょっかいをかけなかったか！？\x02",
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
            "#0005Fい、いえ別に……\x02\x03",

            "#0003F現在は薬物捜査の方に\x01",
            "専念していますから。\x02\x03",

            "#0001F……何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あったも何も！\x01",
            "連中の事務所が……\x02\x03",

            "……ゴホン、何でもない。\x02\x03",

            "何もしてないなら構わん。\x01",
            "そのまま捜査を続けていろ。\x02",
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
            "#0005Fあ……\x02",
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
            "#0101Fダドリー捜査官から？\x01",
            "何かあったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#12P#0006Fいや……\x02",
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
            "ロイドはエリィたちに\x01",
            "ダドリーとのやり取りを伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0241
    ChrTalk(
        0x104,
        "#0301Fなんだそりゃ……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#6P#0206F……露骨に怪しいですね。\x02\x03",

            "#0201Fルバーチェ商会で\x01",
            "何かあったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        "#12P#0003F可能性は高そうだな……\x02",
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
            "#0300Fこりゃ、行ってみるしか\x01",
            "ねえんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x102,
        (
            "#0103Fそうね……抗争には関わるなって\x01",
            "釘は刺されているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        (
            "#6P#0202F失踪者にマフィアが絡んでいるなら\x01",
            "大義名分は立つのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0001Fああ……\x01",
            "ルバーチェ商会に急ごう！\x02",
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

    # Function_20_4F6C end

    def Function_21_5B8C(): pass

    label("Function_21_5B8C")

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
            "#5P#0000F住宅街の空家……\x01",
            "住所はここみたいだな。\x02",
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
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0250
    ChrTalk(
        0x101,
        (
            "#5P#0003Fとりあえず\x01",
            "留守みたいだけど……\x02",
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
            "#5P#0300Fつーかどこを\x01",
            "どう見ても空家だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x103,
        "#5P#0200Fええ、人の気配もありませんし。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#5P#0100Fたしかここは１０年以上\x01",
            "廃屋になっているはずよ。\x02\x03",

            "小さい頃にオバケ屋敷だって\x01",
            "流行った事があるもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#5P#0005Fへえ、そうなんだ。\x02\x01",

            "#0003F（俺は知らなかったな。\x01",
            "  エリィとは同い年の筈だけど……）\x02",
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
            "#5P#0000Fとりあえず、住宅街の空家は\x01",
            "確認ＯＫってことで良さそうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F49")

    #C0256
    ChrTalk(
        0x104,
        (
            "#0300Fおお、これで確認は\x01",
            "全部終わったみてえだし……\x02\x03",

            "受付のねーちゃんに\x01",
            "報告に戻るとするか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_5F6F")

    label("loc_5F49")


    #C0257
    ChrTalk(
        0x104,
        "#0300Fおお、次に行くとしようぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_5F6F")

    Sleep(200)
    SetChrPos(0x0, 17510, 0, -2090, 180)
    SetChrPos(0x1, 17510, 0, -2090, 180)
    SetChrPos(0x2, 17510, 0, -2090, 180)
    SetChrPos(0x3, 17510, 0, -2090, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_21_5B8C end

    def Function_22_5FC3(): pass

    label("Function_22_5FC3")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609D")

    #C0258
    ChrTalk(
        0x102,
        "#11P#0105F（あっと……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_60BD")

    label("loc_609D")


    #C0259
    ChrTalk(
        0x102,
        "#11P#0103F……うーん………\x02",
    )

    CloseMessageWindow()

    label("loc_60BD")

    TurnDirection(0x102, 0x101, 500)

    #C0260
    ChrTalk(
        0x102,
        (
            "#0100Fねえロイド、この家に\x01",
            "お邪魔するつもりなの？\x02",
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
            "#5P#0000Fああ、仔猫の飼い主が\x01",
            "いるかもしれないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        (
            "#5P#0200F年頃のお子さんが\x01",
            "いる可能性もあるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#0103Fいないと思うけど……\x01",
            "そ、そうねえ……\x02",
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
            "#0100Fお留守かもしれないから、\x01",
            "まずは呼び鈴を\x01",
            "鳴らしてみてはどうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#5P#0005Fあ、ああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        (
            "#11P#0300Fなんだお嬢、\x01",
            "変なことを言うなぁ……\x02",
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
            "#0005F#11P（あれ、導力ブザーが付いてる……\x01",
            "  やっぱり裕福な家みたいだな。）\x02",
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
            "#0000F#11Pすみません、警察の者ですが……\x02\x03",

            "少しお話を伺って\x01",
            "よろしいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #N0269
    NpcTalk(
        0x10,
        "男性の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1P#N#2Sハイハイ、ただいま……\x02",
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
            "#5P当家の執事の\x01",
            "ヘルマーと申します。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x10,
        "#5Pええと、警察の方でしたかな？\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#0000F#12Pええ、大したお話では\x01",
            "ないんですが……\x02\x03",

            "こちらのお宅で\x01",
            "猫を飼ったりはしていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x10,
        "#5P猫……でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x10,
        (
            "#5Pいいえ、当家では\x01",
            "飼っておりませんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x10,
        (
            "#5Pちなみにわたくしは猫派なのですが、\x01",
            "旦那様とお嬢様はやや犬派でして……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        "#0012F#12Pは、はあ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        "#0306F#12P空振りみてえだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-24190, -3400, -32159, 3000)
    Sleep(3000)
    WaitChrThread(0x102, 1)

    #C0278
    ChrTalk(
        0x102,
        (
            "#0106F#11P（ふう……\x01",
            "  何だか気を遣うわね。）\x02",
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

    # Function_22_5FC3 end

    def Function_23_666B(): pass

    label("Function_23_666B")

    OP_96(0x102, 0xFFFFA772, 0xFFFFE890, 0xFFFF7AB8, 0x7D0, 0x0)
    OP_95(0x102, -21500, -6000, -33240, 3000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_23_666B end

    def Function_24_669B(): pass

    label("Function_24_669B")

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

    def lambda_6752():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6752)

    def lambda_6767():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6767)

    def lambda_677C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_677C)

    def lambda_6791():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_6791)
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
        "#0200F#11P？　あれは……\x02",
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

    def lambda_684B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_684B)

    def lambda_6858():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6858)
    Sleep(10)

    def lambda_6868():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6868)
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
            "マリー……\x01",
            "……マリー～っ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x12C)
    Sleep(200)

    #C0281
    ChrTalk(
        0xE,
        (
            "ううっ、どこに\x01",
            "いっちゃったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(200)

    #C0282
    ChrTalk(
        0xE,
        "マリー、でてきなさいな～っ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-6190, -3520, -17670, 2500)
    MoveCamera(20, 22, 0, 1000)
    OP_95(0xE, -7080, -6000, -21580, 4000, 0x0)

    def lambda_69E4():
        OP_95(0xFE, -6360, -2410, -12820, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_69E4)
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
        "#11P#0300Fふむ、さっき話を聞いた子だな。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#11P#0105Fあんな小さい子が\x01",
            "１人でお出掛けかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#12P#0003Fうーん、それにしては\x01",
            "様子がおかしかったけど……\x02",
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

    # Function_24_669B end

    def Function_25_6B74(): pass

    label("Function_25_6B74")

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
            "#5Pあの子ったら……\x01",
            "ほんとにどこに……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#12P#0005Fきみ、何かを探してるのか？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x0)
    OP_93(0xE, 0xB4, 0x1F4)

    #C0288
    ChrTalk(
        0xE,
        "#5Pえっ……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#12P#0100Fもしかして、仔猫を\x01",
            "探してるんじゃないかしら。\x02",
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
            "ロイドはジャケットから\x01",
            "仔猫の姿を出してみせた。\x02",
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
        "#5P#4Sマリー！\x02",
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
        "#5Pよかった、ぶじだったのね！\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xE,
        "#5Pどこにいってたのよ、もう……！\x02",
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
            "#12P#0000Fなんだ……やっぱり\x01",
            "君が飼っていたんじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    OP_63(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    def lambda_6E71():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6E71)
    OP_96(0xF, 0xFFFFC040, 0x0, 0x1040, 0x1770, 0x0)

    def lambda_6E92():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6E92)
    OP_96(0xF, 0xFFFFC180, 0x0, 0x12D4, 0x1770, 0x0)

    def lambda_6EB3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6EB3)
    OP_96(0xF, 0xFFFFC40A, 0x0, 0x14FA, 0x1770, 0x0)

    def lambda_6ED4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6ED4)
    Sleep(300)
    OP_93(0xE, 0xB4, 0x1F4)
    TurnDirection(0xF, 0xE, 300)

    #C0295
    ChrTalk(
        0xE,
        "#5Pち、ちがうわ。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xE,
        (
            "#5Pだって……マリーはまだ\x01",
            "のら猫なんですもの！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x103,
        (
            "#11P#0200F野良ですか？\x01",
            "でも首輪を付けていたのでは……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xE,
        (
            "#5Pマリーはのら猫だけど\x01",
            "わたしのものだもの。\x01",
            "だからくびわをつけておいたの。\x02",
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
        "#11P#0306Fややこしい事をすんなぁ……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xE,
        "#5Pほ、ほんとは……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xE1, 0x12C)
    Sleep(300)

    #C0301
    ChrTalk(
        0xE,
        (
            "#5Pおうちでかいたかったけれど、\x01",
            "きっとお父さまがゆるちてくれないもの。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0302
    ChrTalk(
        0xE,
        "#5Pだってマリーは……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x0, 0x12C, 0xBB8, 0x320)

    #C0303
    ChrTalk(
        0xE,
        (
            "#5P#4Sお父さまのだいじなしょるいを\x01",
            "だめにしたハンニンなんだもの！！\x02",
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
            "#5Pううっ、ひっく……\x01",
            "サニータはみてしまったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xE,
        (
            "#5Pマリーがまどからはいってきて、\x01",
            "お父さまのしょさいで昼ねしてるのを……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        (
            "#5Pそのあとしょるいを\x01",
            "ばりばりやぶってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xE,
        (
            "#5Pひっく、ひっく……\x01",
            "ごめんなさい、お父さまぁ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#12P#0003F…………………………\x02\x03",

            "それでお父さんに\x01",
            "事情を打ち明けようと\x01",
            "思ったけど……\x02\x03",

            "#0000Fそんな時に、仔猫がどこかに\x01",
            "行っちゃったんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "#5Pひっく、ひっく……\x01",
            "………コクリ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれで君は心配して\x01",
            "探してたわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        "#5Pスン、スン………コクリ。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#12P#0104Fふう、大体の謎は解けたわね。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#0200Fロイドさん、見事な推理です。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x104,
        (
            "#0300Fでもま、仔猫ってのは\x01",
            "イタズラ好きなもんだ。\x02\x03",

            "行儀よくしてろってのは\x01",
            "無理だと思うぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそうだな、君の家で\x01",
            "飼うのは難しいかもしれない……\x02\x03",

            "#0000Fでもさ、そんなにマリーが好きなら\x01",
            "まずは事情を話してみたらどうかな。\x02",
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
            "#12P#0100Fそうね、私たちも\x01",
            "付き添ってあげるから……\x02\x03",

            "ね、一緒にお話してみましょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xE,
        "#5P……………コクリ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0350", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_6B74 end

    def Function_26_754C(): pass

    label("Function_26_754C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_758A")
    OP_95(0xE, -16110, 0, 4800, 1000, 0x0)
    Sleep(500)
    OP_95(0xE, -13570, 0, 4800, 1000, 0x0)
    Sleep(500)
    Jump("Function_26_754C")

    label("loc_758A")

    Return()

    # Function_26_754C end

    def Function_27_758B(): pass

    label("Function_27_758B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75C7")
    OP_A6(0xE, 0x0, 0xF, 0x3E8, 0xBB8)
    Sleep(1200)
    OP_A6(0xE, 0x0, 0xF, 0x3E8, 0xBB8)
    Sleep(2200)
    Jump("Function_27_758B")

    label("loc_75C7")

    Return()

    # Function_27_758B end

    def Function_28_75C8(): pass

    label("Function_28_75C8")

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
            "#6P#0100Fここが依頼にあった\x01",
            "キャンベル議員のお宅ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#11P#0000F『要人の捜索依頼』、だっけ。\x01",
            "急に依頼が入ってて驚いたけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)
    Sleep(300)

    #C0320
    ChrTalk(
        0x104,
        (
            "#12P#0305Fそういやお嬢も\x01",
            "実家はこの辺りなんだよな。\x02\x03",

            "#0300Fキャンベルって奴の事は\x01",
            "知ってるのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7755():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7755)

    def lambda_7762():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7762)

    def lambda_776F():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_776F)
    Sleep(300)

    #C0321
    ChrTalk(
        0x102,
        (
            "#5P#0103F多少ご近所付きあいが\x01",
            "ある程度かしら……\x02\x03",

            "#0100Fキャンベル議員は野心的な方で、\x01",
            "ご自分の政治活動一色な人だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#12P#0203Fなるほど、\x01",
            "何となく想像が付きます。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_782F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_782F)
    Sleep(100)

    def lambda_783F():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_783F)

    def lambda_784C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_784C)

    def lambda_7859():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7859)
    Sleep(400)

    #C0323
    ChrTalk(
        0x101,
        (
            "#11P#0000Fまあ依頼があったんだ。\x01",
            "一度お邪魔して話を聞いてみるか。\x02",
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

    # Function_28_75C8 end

    def Function_29_78E6(): pass

    label("Function_29_78E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_797A")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0324
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……\x02\x03",

            "仔猫をつれたままだしな。\x01",
            "遠くへ行くのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)
    Return()

    label("loc_797A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A34")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79F3")

    #C0325
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の北口だな。\x02\x03",

            "今は外に出る必要はない……\x01",
            "市内の仕事に専念しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7A1E")

    label("loc_79F3")

    SetChrName("")

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街の外に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7A1E")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB1")
    EventBegin(0x1)

    #C0327
    ChrTalk(
        0x101,
        (
            "#0000Fアルモリカ村に行くには\x01",
            "街の東口から出ないとな。\x02\x03",

            "東通りの方へ回ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B3D")
    EventBegin(0x1)

    #C0328
    ChrTalk(
        0x101,
        (
            "#0000Fウルスラ病院に行くには\x01",
            "街の南口から出ないとな。\x02\x03",

            "中央広場から駅前通りの方へ\x01",
            "回ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C04")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC3")

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000Fっと、こっちは北口だ。\x02\x03",

            "キーアを危険な目に\x01",
            "遭わせたくないし、\x01",
            "外に出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7BEE")

    label("loc_7BC3")

    SetChrName("")

    #A0330
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街の外に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7BEE")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CBE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C7F")

    #C0331
    ChrTalk(
        0x101,
        (
            "#0003Fこっちは街の北口だな。\x02\x03",

            "黒月のこともある……\x01",
            "……今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7CA8")

    label("loc_7C7F")

    SetChrName("")

    #A0332
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7CA8")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_7CBE")

    Return()

    # Function_29_78E6 end

    def Function_30_7CBF(): pass

    label("Function_30_7CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D53")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0333
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……\x02\x03",

            "仔猫をつれたままだしな。\x01",
            "遠くへ行くのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 20930, 0, -3610, 270)
    EventEnd(0x4)
    Return()

    label("loc_7D53")

    Return()

    # Function_30_7CBF end

    def Function_31_7D54(): pass

    label("Function_31_7D54")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E5A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D95")
    Call(0, 22)
    SetScenarioFlags(0x46, 2)
    Jump("loc_7E56")

    label("loc_7D95")


    #C0334
    ChrTalk(
        0x102,
        (
            "#0109Fねえロイド……\x01",
            "さっきの人に聞いたから、\x01",
            "このお宅はいいんじゃない？\x02\x03",

            "用事が無いなら\x01",
            "止めておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#0005Fああ、そうだな……\x01",
            "（まあ聞いてみたし\x01",
            "  お邪魔する必要はないか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E56")

    TalkEnd(0xFF)
    Return()

    label("loc_7E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F8E")

    #C0336
    ChrTalk(
        0x101,
        (
            "#0005Fここは……？\x01",
            "随分と立派なお屋敷だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        (
            "#0105F門は閉じているみたいね。\x02\x03",

            "#0109Fね、ねえロイド……\x01",
            "特に用事がないのなら\x01",
            "お邪魔する事はないんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……\x01",
            "格式のある家みたいだし。\x02\x03",

            "無闇に訪ねるのはやめておくか。\x02",
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
    Jump("loc_7FBD")

    label("loc_7F8E")

    SetChrName("")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この屋敷を訪ねる必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7FBD")

    TalkEnd(0xFF)
    Return()

    # Function_31_7D54 end

    def Function_32_7FC1(): pass

    label("Function_32_7FC1")

    Return()

    # Function_32_7FC1 end

    def Function_33_7FC2(): pass

    label("Function_33_7FC2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FEB")
    Call(0, 21)
    Jump("loc_8016")

    label("loc_7FEB")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8016")

    TalkEnd(0xFF)
    Return()

    # Function_33_7FC2 end

    def Function_34_801A(): pass

    label("Function_34_801A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_803B")
    Call(0, 28)
    Return()

    label("loc_803B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81DF")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_815A")

    #C0342
    ChrTalk(
        0x102,
        (
            "#0105Fここは……\x01",
            "キャンベル議員のお宅ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#0005Fキャンベル議員？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#0103F共和国派の筆頭議員よ。\x01",
            "政界でもかなりの実力者ね。\x02\x03",

            "#0100F用事が無いなら\x01",
            "お邪魔しない方が\x01",
            "いいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……特に用もないし\x01",
            "止めておこうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81D7")

    label("loc_815A")


    #C0346
    ChrTalk(
        0x101,
        (
            "#0005Fここは……\x01",
            "前にエリィから聞いた事があるな。\x02\x03",

            "#0001F確かキャンベルっていう\x01",
            "共和国派の筆頭議員の\x01",
            "邸宅らしいけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81D7")

    SetScenarioFlags(0x46, 3)
    Jump("loc_8225")

    label("loc_81DF")

    SetChrName("")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "共和国派・キャンベル議員の邸宅だ。\x01",
            "特に訪ねる用事はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8225")

    TalkEnd(0xFF)
    Return()

    # Function_34_801A end

    def Function_35_8229(): pass

    label("Function_35_8229")

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
        "#1105F#5Pあっ、誰か来るよ～！\x02",
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

    def lambda_83D0():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_83D0)
    Sleep(50)

    def lambda_83E0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_83E0)
    Sleep(50)

    def lambda_83F0():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_83F0)

    #C0349
    ChrTalk(
        0x101,
        "#0000F#5Pなんだ、リュウたちじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        "#11Pよっ、兄ちゃんたち。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x12,
        "#11Pこんにちは～。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84C0")

    #C0352
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、こんにちは。\x02\x03",

            "#0102F子供たちだけで\x01",
            "どこかへお出かけかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8570")

    label("loc_84C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_851F")

    #C0353
    ChrTalk(
        0x103,
        (
            "#0202F#5Pこんにちは。\x02\x03",

            "#0205F……子供だけで\x01",
            "街道に出るつもりですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8570")

    label("loc_851F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8570")

    #C0354
    ChrTalk(
        0x104,
        (
            "#0309F#5P元気そうじゃねぇか。\x02\x03",

            "#0300F今からどこに行くんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8570")


    #C0355
    ChrTalk(
        0x13,
        (
            "#11Pえっとね、今から大聖堂で\x01",
            "日曜学校があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#0004F#5Pああ、なるほどね。\x01",
            "それなら危なくはないか。\x02\x03",

            "#0002Fそれにしても、\x01",
            "日曜学校まで同じ日だなんて\x01",
            "仲がいいんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x12,
        "#11Pあはは……\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x12,
        (
            "#11Pリュウと一緒にツァイトと遊んでて\x01",
            "うっかりサボっちゃったことも\x01",
            "ありますけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)

    #C0359
    ChrTalk(
        0x11,
        (
            "#5Pいや、あれは仕方ないって。\x01",
            "ツァイトが遊んでくれって\x01",
            "うるさかったんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x153,
        "#1110F#5Pツァイト、かわいいよね～。\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x153, 500)

    #C0361
    ChrTalk(
        0x11,
        (
            "#11P……そういえば\x01",
            "見かけないやつだなぁ。\x01",
            "おまえ、なんていう名前？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x153,
        "#1101F#5Pオマエじゃなくてキーアだよ～！\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x12,
        "#11Pへぇ、キーアちゃんか。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x12,
        (
            "#11P僕の名前はアンリ。\x01",
            "そっちの元気なのがリュウで、\x01",
            "こっちの控えめなのがモモだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x13,
        (
            "#11Pえ、えと……\x01",
            "よろしくキーアちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x153,
        "#1109F#5Pウン、よろしくー！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)

    #C0367
    ChrTalk(
        0x11,
        (
            "#5P……って、おいおい、\x01",
            "こんなことしてる場合じゃないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x11,
        (
            "#5P早く行かないとシスターに\x01",
            "怒られちゃうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x12,
        (
            "#11Pあっ、そうだった！\x01",
            "ごめんなさい、ロイドさん。\x01",
            "僕たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        (
            "#0000F#5Pああ、気にしないでいいよ。\x01",
            "遅れないようにな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 500)

    #C0371
    ChrTalk(
        0x11,
        "#11Pそんじゃな～！\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x13,
        "#11Pさようなら～。\x02",
    )

    CloseMessageWindow()
    OP_68(-18980, 2300, 8820, 3000)
    BeginChrThread(0x11, 3, 0, 38)
    Sleep(100)
    BeginChrThread(0x12, 3, 0, 38)
    Sleep(150)
    BeginChrThread(0x13, 3, 0, 38)
    Sleep(2000)

    def lambda_89C8():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_89C8)

    def lambda_89D5():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_89D5)

    def lambda_89E2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_89E2)
    OP_6F(0x79)
    Sleep(2000)

    #C0373
    ChrTalk(
        0x101,
        (
            "#0000F#11Pそうか、マーブル先生……\x01",
            "今から授業なんだな。\x02\x03",

            "#0005Fあれ、でも住宅街と西通りって\x01",
            "同じ授業日だったっけ？\x02\x03",

            "それなら俺とエリィも小さい頃に\x01",
            "知り合ってるはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B6B")

    #C0374
    ChrTalk(
        0x102,
        (
            "#0104F#5P確か、私たちの頃から\x01",
            "学区の構成が変わっているはずよ。\x02\x03",

            "#0100Fここ数年で都市人口が急増したから\x01",
            "割り振り方も変わったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#0000F#11Pそうだったのか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CE2")

    label("loc_8B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C2E")

    #C0376
    ChrTalk(
        0x103,
        (
            "#0204F#5Pよく分かりませんが\x01",
            "ここ数年で、学区の構成が\x01",
            "変わったのかもしれませんね。\x02\x03",

            "#0202F人口が急増している都市には\x01",
            "よく見られるケースかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        "#0000F#11Pなるほど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CE2")

    label("loc_8C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CE2")

    #C0378
    ChrTalk(
        0x104,
        (
            "#0300F#5Pよく分からねぇが\x01",
            "授業日の割り振りが\x01",
            "変わったんじゃねえのか？\x02\x03",

            "この街、何かやたらと\x01",
            "人が増えてるみてぇだからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        "#0000F#11Pそうかもしれないな……\x02",
    )

    CloseMessageWindow()

    label("loc_8CE2")


    #C0380
    ChrTalk(
        0x153,
        "#1100F#12P……ねー、バスの所に行かないの？\x02",
    )

    CloseMessageWindow()

    def lambda_8D17():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8D17)
    Sleep(50)

    def lambda_8D27():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8D27)
    Sleep(300)

    #C0381
    ChrTalk(
        0x101,
        (
            "#0012F#5Pおっと、そうだな。\x01",
            "そろそろ行くとするか。\x02",
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

    # Function_35_8229 end

    def Function_36_8E04(): pass

    label("Function_36_8E04")


    def lambda_8E09():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E09)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_8E04 end

    def Function_37_8E23(): pass

    label("Function_37_8E23")


    def lambda_8E28():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E28)
    WaitChrThread(0xFE, 1)

    def lambda_8E46():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E46)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_8E23 end

    def Function_38_8E53(): pass

    label("Function_38_8E53")


    def lambda_8E58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E58)
    WaitChrThread(0xFE, 1)

    def lambda_8E69():
        OP_98(0xFE, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E69)
    Sleep(6000)

    def lambda_8E86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8E86)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_8E53 end

    SaveToFile()

Try(main)
