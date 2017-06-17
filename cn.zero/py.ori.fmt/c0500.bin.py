from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0500.bin",                # FileName
        "c0500",                    # MapName
        "c0500",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0500",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "揽客员比修",             # 3
        "爱丽斯",                 # 4
        "弗兰茨巡警",             # 5
        "加尔西亚",               # 6
        "格蕾丝",                 # 7
        "黑手党",                 # 8
        "黑手党",                 # 9
        "黑手党",                 # 10
        "中央广场",               # 11
        "西街",                   # 12
        "行政区",                 # 13
        "住宅街",                 # 14
        "欢乐街",                 # 15
        "东街",                   # 16
        "旧城区",                 # 17
        "港湾区",                 # 18
        "ＩＢＣ",                 # 19
        "站前街道",               # 20
        "后巷",                   # 21
        "乌尔斯拉间道",           # 22
        "东克洛斯贝尔街道",       # 23
        "西克洛斯贝尔街道",       # 24
        "玛因兹山道",             # 25
    ))

    AddCharChip((
        "chr/ch26700.itc",                   # 00
        "chr/ch26900.itc",                   # 01
        "chr/ch31000.itc",                   # 02
        "chr/ch31100.itc",                   # 03
        "chr/ch31900.itc",                   # 04
        "chr/ch30000.itc",                   # 05
    ))

    DeclNpc(-2000,   0,       41700,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2000,    0,       41700,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-7590,   0,       2980,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   1,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(1090,    0,       41770,   180,  389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -0.10000000149011612,  43.849998474121094,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.05000000074505806,   -21.924999237060547,   0.10000000149011612,   1.0])

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  4,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  5,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  6,  0x0000)
    DeclActor(-11950,  0,       3000,    3500,    -11940,  1500,    3060,    0x007C, 0,  19, 0x0000)
    DeclActor(19100,   0,       4000,    3500,    19100,   1500,    4000,    0x007C, 0,  20, 0x0000)

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央广场")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西街")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "东街")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧城区")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "站前街道")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "后巷")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")
    PlaceName(106.0, 0.0, -10.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_5CC",          # 00, 0
        "Function_1_684",          # 01, 1
        "Function_2_6EB",          # 02, 2
        "Function_3_A09",          # 03, 3
        "Function_4_C65",          # 04, 4
        "Function_5_D9B",          # 05, 5
        "Function_6_ED1",          # 06, 6
        "Function_7_1007",         # 07, 7
        "Function_8_10E0",         # 08, 8
        "Function_9_1169",         # 09, 9
        "Function_10_1DF8",        # 0A, 10
        "Function_11_1FCA",        # 0B, 11
        "Function_12_2E78",        # 0C, 12
        "Function_13_3036",        # 0D, 13
        "Function_14_319D",        # 0E, 14
        "Function_15_3276",        # 0F, 15
        "Function_16_3292",        # 10, 16
        "Function_17_3346",        # 11, 17
        "Function_18_33CE",        # 12, 18
        "Function_19_3473",        # 13, 19
        "Function_20_34F5",        # 14, 20
        "Function_21_356D",        # 15, 21
        "Function_22_38B8",        # 16, 22
        "Function_23_4719",        # 17, 23
        "Function_24_585F",        # 18, 24
        "Function_25_5885",        # 19, 25
        "Function_26_58CC",        # 1A, 26
        "Function_27_5913",        # 1B, 27
        "Function_28_593C",        # 1C, 28
        "Function_29_6CDF",        # 1D, 29
        "Function_30_6D4C",        # 1E, 30
        "Function_31_6D7B",        # 1F, 31
        "Function_32_6DA7",        # 20, 32
        "Function_33_71D9",        # 21, 33
        "Function_34_79E4",        # 22, 34
        "Function_35_7D18",        # 23, 35
        "Function_36_8007",        # 24, 36
        "Function_37_8097",        # 25, 37
        "Function_38_87EE",        # 26, 38
    ))


    def Function_0_5CC(): pass

    label("Function_0_5CC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_60C"),
        (1, "loc_618"),
        (2, "loc_624"),
        (3, "loc_630"),
        (4, "loc_63C"),
        (5, "loc_648"),
        (6, "loc_654"),
        (SWITCH_DEFAULT, "loc_660"),
    )


    label("loc_60C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_618")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_624")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_630")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_63C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_648")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_654")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_660")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_66C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_683")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_683")

    Return()

    # Function_0_5CC end

    def Function_1_684(): pass

    label("Function_1_684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EA")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_684")

    label("loc_6EA")

    Return()

    # Function_1_684 end

    def Function_2_6EB(): pass

    label("Function_2_6EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87B")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AD")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_7CC")

    label("loc_7AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CC")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_7CC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87B")

    label("loc_7DA")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_853")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_872")

    label("loc_853")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_872")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_872")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87B")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    Event(0, 22)
    Jump("loc_942")

    label("loc_8A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C2")
    Event(0, 28)
    Jump("loc_942")

    label("loc_8C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E1")
    Event(0, 32)
    Jump("loc_942")

    label("loc_8E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_905")
    Event(0, 33)
    Jump("loc_942")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91B")
    Event(0, 33)
    Jump("loc_942")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_931")
    Event(0, 33)
    Jump("loc_942")

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942")
    Event(0, 33)

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_951")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 23)

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_95F")
    ClearChrFlags(0xC, 0x80)

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_977")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_9D9")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9D9")
    SetChrPos(0xB, 3630, 0, 2500, 180)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -1100, 0, 37580, 135)
    SetChrPos(0x10, 880, 0, 37580, 270)
    SetChrPos(0x11, 320, 0, 36160, 315)

    label("loc_9D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F1")
    OP_C7(0x1, 0x1000)

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A08")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_A08")

    Return()

    # Function_2_6EB end

    def Function_3_A09(): pass

    label("Function_3_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A25")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A41")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A79")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_A8B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E")
    OP_70(0x4, 0x0)
    Jump("loc_AA2")

    label("loc_A9E")

    OP_70(0x4, 0x1E)

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5")
    OP_70(0x5, 0x0)
    Jump("loc_AB9")

    label("loc_AB5")

    OP_70(0x5, 0x1E)

    label("loc_AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")
    OP_70(0x6, 0x0)
    Jump("loc_AD0")

    label("loc_ACC")

    OP_70(0x6, 0x1E)

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEC")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jump("loc_AFE")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AFE")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_AFE")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B16")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_B16")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2E")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B41")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7E")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B91")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA8")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_BA8")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC0")
    OP_1B(0x1, 0x0, 0x26)

    label("loc_BC0")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BD6")
    Jump("loc_C43")

    label("loc_BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BF0")
    Jump("loc_C43")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_BFE")
    Jump("loc_C43")

    label("loc_BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_C1F")
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x5, 0x0, 0x11)
    Jump("loc_C43")

    label("loc_C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_C43")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x6, 0x0, 0x12)

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5F")
    Jump("loc_C64")

    label("loc_C5F")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_C64")

    Return()

    # Function_3_A09 end

    def Function_4_C65(): pass

    label("Function_4_C65")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D52")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_CE4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_D4D")

    label("loc_CE4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D4D")

    Jump("loc_D8F")

    label("loc_D52")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_D8F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C65 end

    def Function_5_D9B(): pass

    label("Function_5_D9B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E88")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_E1A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_E83")

    label("loc_E1A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E83")

    Jump("loc_EC5")

    label("loc_E88")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EC5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_D9B end

    def Function_6_ED1(): pass

    label("Function_6_ED1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBE")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ２', 1)"), scpexpr(EXPR_END)), "loc_F50")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_FB9")

    label("loc_F50")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FB9")

    Jump("loc_FFB")

    label("loc_FBE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_FFB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_ED1 end

    def Function_7_1007(): pass

    label("Function_7_1007")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_107C")

    #C0010
    ChrTalk(
        0x8,
        (
            "喂，你们几个……\x01",
            "事情应该已经办完了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "哼哼，还是说，想让我们的副头目\x01",
            "好好陪你们玩玩呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC")

    label("loc_107C")


    #C0012
    ChrTalk(
        0x8,
        (
            "喂喂，小鬼头们，\x01",
            "回去的路在那边呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "要是不想遭遇到什么可怕的事情，\x01",
            "还是乖乖消失为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DC")

    TalkEnd(0xFE)
    Return()

    # Function_7_1007 end

    def Function_8_10E0(): pass

    label("Function_8_10E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1116")

    #C0014
    ChrTalk(
        0xFE,
        (
            "你们想闲晃到什么时候啊，\x01",
            "嗯？！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1165")

    label("loc_1116")


    #C0015
    ChrTalk(
        0x9,
        "来『鲁巴彻商会』有什么事情吗？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "哈，别以为见过副头目\x01",
            "就有资本嚣张了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1165")

    TalkEnd(0xFE)
    Return()

    # Function_8_10E0 end

    def Function_9_1169(): pass

    label("Function_9_1169")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_126D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11E2")

    #C0017
    ChrTalk(
        0xA,
        (
            "（吐舌头）……哪里有\x01",
            "好客人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "让我带你去一个\x01",
            "快乐美好的世界玩玩吧。\x01",
            "嘿嘿嘿嘿……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1268")

    label("loc_11E2")


    #C0019
    ChrTalk(
        0xA,
        (
            "搞什么啊，还莫名其妙的呢，\x01",
            "太阳就都下山了。\x01",
            "今天真是奇怪的一天啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        (
            "……算啦，不想了，开始做生意好了。\x01",
            "时间就是金钱啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1268")

    Jump("loc_1DF4")

    label("loc_126D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_131C")

    #C0021
    ChrTalk(
        0xFE,
        (
            "怎么搞的……今天跟昨天一样，\x01",
            "街上还是这么安静。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，好像感觉不到\x01",
            "这座城市中一直蠢蠢欲动的\x01",
            "『黑色暗潮』了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "……怎么回事，也太安静了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1503")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_END)), "loc_1453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13C0")

    #C0024
    ChrTalk(
        0xA,
        (
            "（据说那个人原来是猎兵呢。要是跟他\x01",
            "  扯上关系的话，恐怕都不知道是怎么死的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        (
            "（别管他，别管他了！\x01",
            "  ……离他越远越好。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144E")

    label("loc_13C0")


    #C0026
    ChrTalk(
        0xA,
        (
            "（刚才那个大块头的老兄，\x01",
            "  好像就是鲁巴彻的副头目吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "（你们到底做了什么啊……\x01",
            "  要是被那个人盯上，\x01",
            "  可不会有什么好下场啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_144E")

    Jump("loc_14FE")

    label("loc_1453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C5")

    #C0028
    ChrTalk(
        0xFE,
        (
            "怎么回事，这条街今天也太安静了……\x01",
            "都没人从这里经过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "要是客人不过来，\x01",
            "我会哭的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14FE")

    label("loc_14C5")


    #C0030
    ChrTalk(
        0xFE,
        (
            "怎么回事，这条街今天也太安静了……\x01",
            "是我的错觉吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FE")

    Jump("loc_1DF4")

    label("loc_1503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1598")

    #C0031
    ChrTalk(
        0xA,
        (
            "……啊，这位客人。\x01",
            "告诉你一个好消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "本店正在开展新服务哦～\x01",
            "玩两个小时，只需一千米拉！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "怎么样，不错吧？\x01",
            "进来看看吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_1598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_16AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_160C")

    #C0034
    ChrTalk(
        0xA,
        (
            "马上就到了啊……众所期待的\x01",
            "自治州议会！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "我最喜欢纪念庆典和\x01",
            "这个时期了。\x01",
            "嘿嘿嘿嘿！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A8")

    label("loc_160C")


    #C0036
    ChrTalk(
        0xA,
        (
            "马上就到了啊……众所期待的\x01",
            "自治州议会！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            "纪念庆典的时候也赚了不少。\x01",
            "不过，议会期间也会有各～类客人前来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "我要努力多赚钱啊～！\x01",
            "嘿嘿嘿嘿！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16A8")

    Jump("loc_1DF4")

    label("loc_16AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_17C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_171D")

    #C0039
    ChrTalk(
        0xA,
        (
            "别看我长这样，\x01",
            "其实我可会照顾人啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        (
            "今天还请几个\x01",
            "年轻人吃了一顿呢。\x01",
            "呀哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BC")

    label("loc_171D")


    #C0041
    ChrTalk(
        0xA,
        (
            "今天召集了店里的年轻姑娘，\x01",
            "开了场新人欢迎会。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "因为新来了三个女孩嘛，\x01",
            "正好让她们习惯一下店里的环境。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "哇哈哈哈哈！\x01",
            "今天我请客。\x01",
            "尽情欢闹吧！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17BC")

    Jump("loc_1DF4")

    label("loc_17C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1872")

    #C0044
    ChrTalk(
        0xFE,
        (
            "啊啊……真是服了。\x01",
            "昨天我们店里有\x01",
            "一个女孩跑掉不干了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，算啦，\x01",
            "世界上漂亮女孩有得是嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "话说回来，小兄弟，\x01",
            "我们店今天在搞\x01",
            "快乐大促销活动哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_1872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18EC")

    #C0047
    ChrTalk(
        0xA,
        (
            "嗯～几位小兄弟，\x01",
            "不进来玩玩吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "这种时间，\x01",
            "在我们这里闲晃可是不行的哦！\x01",
            "会让人误会的嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196F")

    label("loc_18EC")


    #C0049
    ChrTalk(
        0xA,
        "您好～……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "怎么啦，怎么啦～几位小兄弟。\x01",
            "怎么一副无精打采的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "好，就让我来帮你们打起精神吧。\x01",
            "来，走吧走吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_196F")

    Jump("loc_1DF4")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19E9")

    #C0052
    ChrTalk(
        0xA,
        (
            "不知道到底发生了什么，\x01",
            "但是听到了狗叫的声音呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "希望那些黑道的人\x01",
            "能稍微安分一些啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A68")

    label("loc_19E9")


    #C0054
    ChrTalk(
        0xA,
        (
            "最近，那些黑道的人\x01",
            "好像慌慌忙忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "哎呀，真让人困扰啊，\x01",
            "我们的店离那栋大楼挺近的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        "客人们也会觉得很害怕啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A68")

    Jump("loc_1DF4")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1ADA")

    #C0057
    ChrTalk(
        0xFE,
        (
            "来，看呀看呀，\x01",
            "我买了新的项链，\x01",
            "……闪闪发亮哦！！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "呀哈哈哈哈！\x01",
            "揽客真是个好买卖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_1ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B26")

    #C0059
    ChrTalk(
        0xA,
        (
            "我们的店亏了好多钱……\x01",
            "真是让人难以忍受啊～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBD")

    label("loc_1B26")


    #C0060
    ChrTalk(
        0xFE,
        "刚才来了一个游击士。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "随便扯了个理由，\x01",
            "就强行带走了我们这里的一个年轻姑娘。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……那孩子可是提前预支了薪水的啊！\x01",
            "真是让人难以忍受啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BBD")

    Jump("loc_1DF4")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1C5C")

    #C0063
    ChrTalk(
        0xFE,
        "我们店里有很多年轻的姑娘哦。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "虽然整天接待客人十分辛苦，\x01",
            "但薪水可是相当高的。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "还有人提前预支工资呢。\x01",
            "真是的，大家都这么精明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_1C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1D03")

    #C0066
    ChrTalk(
        0xA,
        (
            "您好啊～\x01",
            "今天的游客也很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "要是客人肯一起来店里玩的话，\x01",
            "一定会很开心的，\x01",
            "我们也会很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "来呀来呀，\x01",
            "一起开心地玩嘛。\x01",
            "啊哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1D7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 2)), scpexpr(EXPR_END)), "loc_1D76")

    #C0069
    ChrTalk(
        0xA,
        (
            "还是别靠近\x01",
            "那条小路为好哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "那里可都是黑道上的兄弟们呢。\x01",
            "他们比我们可恶劣太多啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D79")

    label("loc_1D76")

    Call(0, 10)

    label("loc_1D79")

    Jump("loc_1DF4")

    label("loc_1D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 2)), scpexpr(EXPR_END)), "loc_1DF1")

    #C0071
    ChrTalk(
        0xA,
        (
            "最好不要在这附近\x01",
            "闲晃啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "因为如果被我这种人抓住，\x01",
            "口袋恐怕会被掏个一干二净哦！\x01",
            "呀哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF4")

    label("loc_1DF1")

    Call(0, 10)

    label("loc_1DF4")

    TalkEnd(0xFE)
    Return()

    # Function_9_1169 end

    def Function_10_1DF8(): pass

    label("Function_10_1DF8")


    #C0073
    ChrTalk(
        0xA,
        (
            "啊，几位小兄弟是游客吗？\x01",
            "怎么样啊，是不是挺闲的？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "既然如此，那就交给我吧。\x01",
            "我会给你们介绍一个很棒的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        "怎么样？来来，到这里来！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x103,
        (
            "#0200F这属于强行拉客……\x01",
            "违反经营法呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x103, 500)
    Sleep(500)

    #C0077
    ChrTalk(
        0xA,
        "什么，你们还带着小孩子啊。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "……好吧，算了，算了。\x01",
            "今天就放过你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "小姑娘，\x01",
            "这附近可不是你这种小孩子能来的地方哦。\x01",
            "以后可要注意点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        "#0201F（…………怒………）\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈……\x01",
            "  她很不喜欢被别人\x01",
            "  当成小孩子吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 2)
    Return()

    # Function_10_1DF8 end

    def Function_11_1FCA(): pass

    label("Function_11_1FCA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_20DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_204A")

    #C0082
    ChrTalk(
        0xB,
        (
            "那条小巷里\x01",
            "有警察在出出进进的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "那些警察不要紧吗～\x01",
            "……还是说，因为是警察，所以没问题呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D7")

    label("loc_204A")


    #C0084
    ChrTalk(
        0xB,
        (
            "从刚才开始，就一直有警察\x01",
            "进入那条小巷。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        (
            "那种地方……\x01",
            "可不能随便接近啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "那些警察没事吧～\x01",
            "不会被那些穿着\x01",
            "黑衣服的人斥骂吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20D7")

    Jump("loc_2E74")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2178")

    #C0087
    ChrTalk(
        0xB,
        (
            "我正在思考战胜其他女孩，\x01",
            "顺利拉来客人的台词呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "嗯～嗯～……\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "真是的，笨蛋！\x01",
            "别妨碍我思考啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_221C")

    label("loc_2178")


    #C0090
    ChrTalk(
        0xB,
        "你好，我是爱丽斯哦☆\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "几位哥哥，现在有空吗～？\x01",
            "我来陪你们玩玩吧⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0092
    ChrTalk(
        0xB,
        (
            "……嗯，感觉还是有点不对劲～\x01",
            "好像不太符合我的风格呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_221C")

    Jump("loc_2E74")

    label("loc_2221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_233B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_228C")

    #C0093
    ChrTalk(
        0xB,
        (
            "呜呜，营业额又要被\x01",
            "其他女孩超过了～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "嗯，这可不妙～\x01",
            "必须得想出个对策才行～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_228C")


    #C0095
    ChrTalk(
        0xB,
        (
            "不知为何，今天总感觉\x01",
            "小巷那边的气氛很可怕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        (
            "我偷偷去看了一下，\x01",
            "结果就被那里的黑衣人狠狠瞪了一眼……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xB,
        (
            "嗯，到底发生了什么事呢？\x01",
            "不然今天就不要揽客了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2336")

    Jump("loc_2E74")

    label("loc_233B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2443")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23B2")

    #C0098
    ChrTalk(
        0xB,
        (
            "这还是第一次有人指名预约我呢，\x01",
            "微稍有点开心啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "好啦，要努力工作到\x01",
            "预约开始的时间！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243E")

    label("loc_23B2")


    #C0100
    ChrTalk(
        0xB,
        (
            "嘿嘿，今天有人\x01",
            "指名预约我啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        "很棒吧！羡慕吧～？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "不知道为什么，在召开议会的期间，\x01",
            "接待工作的预约会变得很多。\x01",
            "超级幸运啦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_243E")

    Jump("loc_2E74")

    label("loc_2443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_256D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24D8")

    #C0103
    ChrTalk(
        0xB,
        (
            "虽然纪念庆典已经结束了，\x01",
            "但我不知是怎么回事，干劲十足啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "呵呵，下个月也要好好展现大人的魅力，\x01",
            "把对手都打压下去！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2568")

    label("loc_24D8")


    #C0105
    ChrTalk(
        0xB,
        (
            "要说纪念庆典期间的营业额啊，\x01",
            "我比其他女孩稍多一点呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0106
    ChrTalk(
        0xB,
        "太好了，我赢了～！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xB,
        "好开心，这是我第一次赢哦！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2568")

    Jump("loc_2E74")

    label("loc_256D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_26BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25E2")

    #C0108
    ChrTalk(
        0xB,
        (
            "那个修女，老是皱着眉头，\x01",
            "都出现了很多皱纹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "哼，赶快变成满脸皱纹的\x01",
            "老太婆才好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BA")

    label("loc_25E2")


    #C0110
    ChrTalk(
        0xB,
        (
            "我最近肩膀酸痛得厉害，\x01",
            "所以跑去教会，想要一点药。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "但我表明自己是女公关之后，\x01",
            "修女的表情马上就变得好严肃。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        "然后就开始长篇大论地对我说教。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "真是的，搞什么啊，让人火大～！\x01",
            "做这行有什么不好的啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_26BA")

    Jump("loc_2E74")

    label("loc_26BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2724")

    #C0114
    ChrTalk(
        0xB,
        (
            "喝醉的客人最难应付了，\x01",
            "总是死缠着人不放。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "唉，昨天的业绩\x01",
            "超级差啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B2")

    label("loc_2724")


    #C0116
    ChrTalk(
        0xB,
        (
            "呼啊～啊啊……\x01",
            "……好困好困……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "昨天被一个死皮赖脸的客人\x01",
            "缠上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        "呼，真是不幸啊～\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xB,
        (
            "这下也许又会被\x01",
            "其他女孩抛在后面了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_27B2")

    Jump("loc_2E74")

    label("loc_27B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2824")

    #C0120
    ChrTalk(
        0xB,
        (
            "嘿嘿，马上就要到\x01",
            "客人增多的时间啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        "您好，我是爱丽斯～☆\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        "……好，今天也要加油！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E74")

    label("loc_2824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_291E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_288F")

    #C0123
    ChrTalk(
        0xB,
        (
            "要是警察来了的话，\x01",
            "我就做不成生意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        (
            "真是的，就不能赶快\x01",
            "去别的地方吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2919")

    label("loc_288F")


    #C0125
    ChrTalk(
        0xB,
        (
            "刚才有警察过来\x01",
            "调查取证了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "是为了不久前某家店\x01",
            "发生骚乱的那件事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "真的是，随便怎样都好啦，\x01",
            "但是不要妨碍我们做生意啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2919")

    Jump("loc_2E74")

    label("loc_291E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_29ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2970")

    #C0128
    ChrTalk(
        0xB,
        "最近肩膀酸痛得很厉害呢。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "要不要去教堂\x01",
            "要点药呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29E8")

    label("loc_2970")


    #C0130
    ChrTalk(
        0xB,
        (
            "我的对手也都在\x01",
            "努力提升业绩。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "可是，工作一多起来，\x01",
            "我的肩膀就会很痛。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xB,
        (
            "唉，要不要去教堂\x01",
            "拿点药回来呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29E8")

    Jump("loc_2E74")

    label("loc_29ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A39")

    #C0133
    ChrTalk(
        0xB,
        (
            "不能向那些人\x01",
            "搭话哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        "呼，今天犯了个错误。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ABA")

    label("loc_2A39")


    #C0135
    ChrTalk(
        0xB,
        (
            "刚才一不小心，\x01",
            "跟那些戴着墨镜的人\x01",
            "搭话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "……结果他们用超级可怕\x01",
            "的眼神瞪着我。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "呜呜呜，那些人\x01",
            "果然很可怕啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2ABA")

    Jump("loc_2E74")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B13")

    #C0138
    ChrTalk(
        0xB,
        (
            "我这个人很不擅长\x01",
            "动脑子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        "啊啊，怎么办才好呢～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B68")

    label("loc_2B13")


    #C0140
    ChrTalk(
        0xB,
        (
            "再这么下去，业绩就会输给\x01",
            "其他女孩了～\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "啊啊，一定要想出\x01",
            "什么好办法才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B68")

    Jump("loc_2E74")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2C60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BB3")

    #C0142
    ChrTalk(
        0xB,
        (
            "我们也是要做生意的。\x01",
            "真是的，好烦人啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5B")

    label("loc_2BB3")


    #C0143
    ChrTalk(
        0xB,
        (
            "有时候啊，那些戴着墨镜的人\x01",
            "会在大半夜折腾个没完，\x01",
            "到处跑来跑去，不知道在搞什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "之前有一天晚上，\x01",
            "简直吵得我们都做不了生意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        "真的是，让人火大啊～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C5B")

    Jump("loc_2E74")

    label("loc_2C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 3)), scpexpr(EXPR_END)), "loc_2CDC")

    #C0146
    ChrTalk(
        0xB,
        (
            "我正在跟其他女孩比赛，\x01",
            "看谁的业绩更高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "可是、可是……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        "啊啊～这个月恐怕要输了呢～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDF")

    label("loc_2CDC")

    Call(0, 12)

    label("loc_2CDF")

    Jump("loc_2E74")

    label("loc_2CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 3)), scpexpr(EXPR_END)), "loc_2E71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0F")

    #C0149
    ChrTalk(
        0xFE,
        (
            "兰迪先生许下的诺言，\x01",
            "一般都兑现不了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "之前还信誓旦旦地说会来呢，\x01",
            "结果也没有来～\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0303F啊，那天我好像是在\x01",
            "酒吧里结识了一位美女。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 0)

    #C0152
    ChrTalk(
        0xFE,
        (
            "真是的，兰迪先生是大笨蛋～！\x01",
            "大骗子～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E6C")

    label("loc_2E0F")

    TurnDirection(0xFE, 0x104, 0)

    #C0153
    ChrTalk(
        0xFE,
        (
            "兰迪先生是大笨蛋～！\x01",
            "大骗子～！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "要是不来店里玩的话，\x01",
            "爱丽斯可是会生气哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6C")

    Jump("loc_2E74")

    label("loc_2E71")

    Call(0, 12)

    label("loc_2E74")

    TalkEnd(0xFE)
    Return()

    # Function_11_1FCA end

    def Function_12_2E78(): pass

    label("Function_12_2E78")

    TurnDirection(0xFE, 0x104, 0)

    #C0155
    ChrTalk(
        0xFE,
        "啊，发现兰迪先生啦～！\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "最近怎么都没有来店里玩啊。\x01",
            "哼～都在哪里鬼混啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，抱歉。\x01",
            "最近在忙着办理转职手续什么的，\x01",
            "稍微有点忙啊。\x02\x03",

            "爱丽斯最近\x01",
            "怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "嗯～应该和以前一样吧～\x01",
            "正在努力战胜\x01",
            "竞争对手呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "兰迪先生～有空时再来\x01",
            "店里玩吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#0304F真没办法啊。\x01",
            "那么，不然今天晚上就……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0109F兰迪，\x01",
            "请不要当着小孩子的面做这种事，#200W可·以·吗#20W？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0006F（难道兰迪平时\x01",
            "  总来这种地方玩吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 3)
    Return()

    # Function_12_2E78 end

    def Function_13_3036(): pass

    label("Function_13_3036")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3150")

    #C0163
    ChrTalk(
        0xFE,
        (
            "一科的人派我在这里看守，\x01",
            "说是不要让市民进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "可、可是，这里……\x01",
            "不就是那个鲁巴彻商会的地盘吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "好、好危险啊……\x01",
            "我、我真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0003F不好意思，弗兰茨……\x01",
            "这里就拜托你看守了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0300F不要紧，万一那些家伙回来了，\x01",
            "你就赶快逃跑吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3199")

    label("loc_3150")


    #C0168
    ChrTalk(
        0xFE,
        (
            "呜呜，我明明是今年\x01",
            "才刚刚进来的新人……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "真、真是超级不安啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3199")

    TalkEnd(0xFE)
    Return()

    # Function_13_3036 end

    def Function_14_319D(): pass

    label("Function_14_319D")

    TurnDirection(0x11C, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_31EE")

    #C0170
    ChrTalk(
        0x11C,
        "#1200F……嗷呜嗷呜～！\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0005F（看来不是这条路。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_31EE")


    #C0172
    ChrTalk(
        0x11C,
        "#1200F……嗷呜嗷呜～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x101,
        "#0005F不、不是这边吗？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#0200F看起来并不是\x01",
            "这条路呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3275")

    Return()

    # Function_14_319D end

    def Function_15_3276(): pass

    label("Function_15_3276")

    EventBegin(0x1)
    Call(0, 14)
    Sleep(50)
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_15_3276 end

    def Function_16_3292(): pass

    label("Function_16_3292")

    EventBegin(0x1)

    #C0175
    ChrTalk(
        0x11C,
        "#1200F……嗷呜嗷呜～！\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0003F怎么也不应该\x01",
            "走到这边吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#0200F看来就算喝醉了，他还是保有\x01",
            "最低限度的分辨能力啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 4620, 180)
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)
    EventEnd(0x4)
    Return()

    # Function_16_3292 end

    def Function_17_3346(): pass

    label("Function_17_3346")

    EventBegin(0x1)

    #C0178
    ChrTalk(
        0x11C,
        "#1200F……嗷呜嗷呜～！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0003F……不是这边啊。\x02\x03",

            "#0001F要是从古董店里出来，\x01",
            "再去重新找家店喝酒的话……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5660, 790, 4890, 180)
    EventEnd(0x4)
    Return()

    # Function_17_3346 end

    def Function_18_33CE(): pass

    label("Function_18_33CE")

    EventBegin(0x2)

    #C0180
    ChrTalk(
        0x11C,
        "#1200F……嗷呜嗷呜～！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0181
    ChrTalk(
        0x101,
        "#0005F什么，也不是这边吗……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        (
            "#0200F再去找找\x01",
            "别的路吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Fade(500)
    SetChrPos(0x0, -10220, 1950, 5940, 180)
    OP_31(0x1)
    OP_0D()
    EventEnd(0x3)
    Return()

    # Function_18_33CE end

    def Function_19_3473(): pass

    label("Function_19_3473")

    TalkBegin(0xFF)

    #C0183
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "……嗷呜～！\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#0005F哦……看来副局长\x01",
            "确实曾从这里经过啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        "#0200F嗯，就这样继续前进吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_19_3473 end

    def Function_20_34F5(): pass

    label("Function_20_34F5")

    TalkBegin(0xFF)

    #C0186
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "呜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#0003F这里……应该不对吧？\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#0200F是啊，似乎没有\x01",
            "留下什么气味。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_20_34F5 end

    def Function_21_356D(): pass

    label("Function_21_356D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-10190, 1950, 2170, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_68(5680, 1950, 2170, 6000)
    MoveCamera(0, 10, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(16500, 6000)
    PlaceName2(340, 200, "c_plac08", 0x0, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A9")

    #A0189
    AnonymousTalk(
        0x103,
        "#0205F这条街是……？\x02",
    )

    CloseMessageWindow()

    #A0190
    AnonymousTalk(
        0x104,
        (
            "#0303F哈，也就是所谓的后巷了。\x02\x03",

            "#0300F虽说只能算是欢乐街的延长线，\x01",
            "但从普通酒吧到夜店，可谓是一应俱全，\x01",
            "其中也有很不错的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0191
    AnonymousTalk(
        0x101,
        "#0000F……兰迪，你好像挺熟悉这里的啊？\x02",
    )

    CloseMessageWindow()

    #A0192
    AnonymousTalk(
        0x104,
        (
            "#0302F对啊，不是和罗伊德说过吗？\x02\x03",

            "#0309F这附近的几家店里，\x01",
            "有很漂亮的\x01",
            "姐姐……\x02",
        )
    )

    CloseMessageWindow()

    #A0193
    AnonymousTalk(
        0x102,
        "#0106F……不用再说下去了。\x02",
    )

    CloseMessageWindow()

    #A0194
    AnonymousTalk(
        0x101,
        (
            "#0012F（哈哈……兰迪好像\x01",
            "  很沉迷于这类场所啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_37A9")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "所谓后巷，就是从中央广场延伸出来的小路。\x02",
        )
    )

    CloseMessageWindow()

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "爵士酒吧『加兰特』、\x01",
            "古董店『伊梅尔达』等\x01",
            "店铺在此经营。\x02",
        )
    )

    CloseMessageWindow()

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然价格比较高，但是能买到一些方便的道具，\x01",
            "有机会时可以过来看看。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0x47, 3)
    EventEnd(0x5)
    Return()

    # Function_21_356D end

    def Function_22_38B8(): pass

    label("Function_22_38B8")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    OP_68(0, 1000, 45000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -600, 0, 34200, 0)
    SetChrPos(0x102, 600, 0, 34200, 0)
    SetChrPos(0x103, -1200, 0, 33000, 0)
    SetChrPos(0x104, 1200, 0, 33000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -800, -100, 40500, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 800, -100, 40500, 270)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 0, 200, 44500, 180)
    ClearMapObjFlags(0x2, 0x10)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    OP_68(0, 3000, 43000, 6000)
    MoveCamera(0, -5, 0, 6000)
    SetCameraDistance(19000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac12", 0x0, 0)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 900, 35500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(18000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x8, -800, 0, 40500, 90)
    SetChrPos(0x9, 800, 0, 40500, 270)
    OP_0D()

    #C0198
    ChrTalk(
        0x101,
        "#12P#0001F（这里就是『鲁巴彻商会』……）\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#0101F（之前就感觉这条小路\x01",
            "  很可疑了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    Sleep(150)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3B4B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3B4B)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0200
    ChrTalk(
        0x9,
        "#5P你们几个是谁啊？\x02",
    )

    CloseMessageWindow()

    def lambda_3B7B():
        OP_95(0xFE, 700, 0, 37500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B7B)
    Sleep(150)

    def lambda_3B98():
        OP_95(0xFE, -700, 0, 37500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3B98)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)

    #C0201
    ChrTalk(
        0x8,
        (
            "#5P这里可不是你们这种小鬼头\x01",
            "能来的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        "#5P赶快给我消──\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0203
    ChrTalk(
        0x8,
        "#5P嗯……！？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        "#5P你、你们是——那个时候的……！？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        "#12P#0205F难道说……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        (
            "#12P#0302F哈，看样子\x01",
            "好像是老熟人嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    #C0207
    ChrTalk(
        0x9,
        (
            "#11P怎么了？\x01",
            "这些家伙是什么人啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        "#5P就是我之前说的那些警察小鬼！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "#5P阻碍我们在旧城区\x01",
            "实施行动的人……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0210
    ChrTalk(
        0x9,
        "#5P什么……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#12P#0003F……看起来，不需要\x01",
            "再做自我介绍了呢。\x02\x03",

            "#0000F我们今天是为了调查任务\x01",
            "而过来拜访的。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        "#5P什么……？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#0000F能帮忙向会长先生\x01",
            "通报一下吗？\x02\x03",

            "我们想向他询问一下\x01",
            "关于某个事件的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        "#5P开、开什么玩笑……！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "#5P警察局的臭小鬼想与会长面谈！？\x01",
            "这种蠢话，你还真敢说出口……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        (
            "#0103F……并不是把他当成嫌疑人，\x01",
            "只是想进行一般询问，以作为参考罢了。\x02\x03",

            "#0100F当然了，这不是强制行为，\x01",
            "我们也不会勉强的……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        (
            "#12P#0300F不过，只是通报一下的话，\x01",
            "应该还是可以的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        "#5P嘁……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "#5P自从那次行动失败了以后，\x01",
            "他们好像就更加嚣张了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0220
    ChrTalk(
        0x9,
        "#11P喂喂，怎么办？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#11P要不要教训教训这几个不知天高地厚\x01",
            "的臭小鬼，让他们学会最基本的礼貌？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        "#5P哼，说得是啊……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x104,
        "#12P#0308F（……看样子，似乎行不通啊？）\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#6P#0006F（……没办法。\x01",
            "  只能先回去了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    StopBGM(0xBB8)
    Sleep(500)

    #N0225
    NpcTalk(
        0xD,
        "豪气的声音",
        "#4P──让他们进来。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    Fade(500)
    OP_68(0, 1000, 42000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_EE(0x0, 0x5)
    OP_68(0, 1000, 36000, 4000)
    SetCameraDistance(20000, 4000)
    PlayBGM("ed7302", 0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_41EF():

        label("loc_41EF")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_41EF")

    QueueWorkItem2(0x8, 2, lambda_41EF)

    def lambda_4201():

        label("loc_4201")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4201")

    QueueWorkItem2(0x9, 2, lambda_4201)

    def lambda_4213():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4213)

    def lambda_4224():
        OP_95(0xFE, 0, 0, 37000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4224)
    WaitChrThread(0xD, 2)
    Sleep(1500)

    def lambda_4245():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x92E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4245)
    Sleep(100)

    def lambda_4262():
        OP_96(0xFE, 0x514, 0x0, 0x92E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4262)

    #C0226
    ChrTalk(
        0x8,
        "#1P副头目……！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x9,
        "#2P您、您辛苦了！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x11)

    #N0228
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        "#5P#3104F嗯，你们也辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#6P#0013F（好、好高大……）\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x103,
        (
            "#0201F#6P#N（那个瓦鲁多\x01",
            "  就已经很高大了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0231
    ChrTalk(
        0x104,
        "#0301F#12P（但和他一比就……）\x02",
    )

    CloseMessageWindow()

    #N0232
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        (
            "#5P#3100F哼哼……\x01",
            "你们就是那些警察小鬼吗？\x02\x03",

            "关于你们的事情，我有所耳闻。\x01",
            "你们比我想象中的还要年轻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#0003F……我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02\x03",

            "#0001F您是……？\x02",
        )
    )

    CloseMessageWindow()
    Sound(1854, 255, 90, 0)    #voice#Garcia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("穿西装的巨汉")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            "加尔西亚·罗西。\x02\x03",

            "『鲁巴彻商会』的\x01",
            "营业总部部长。\x02\x03",

            "哼哼哼……不过，还是被人称为『副头目』\x01",
            "的时候比较多吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0235
    ChrTalk(
        0x101,
        "#6P#0001F………………………………\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x104,
        (
            "#0301F#12P（喂喂……\x01",
            "  突然就跳出个大人物啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#6P#0101F（……是啊，\x01",
            "  恐怕是组织内的二号人物吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    #C0238
    ChrTalk(
        0xD,
        (
            "#5P#3103F──进来。\x02\x03",

            "有话就和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45D3():
        OP_95(0xFE, 0, 200, 44500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_45D3)
    Sleep(2000)

    def lambda_45F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_45F0)

    #C0239
    ChrTalk(
        0x101,
        "#6P#0005F哎，啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 2)
    WaitChrThread(0xD, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)

    def lambda_462A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_462A)
    Sleep(100)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0240
    ChrTalk(
        0x8,
        (
            "#5P……哼。\x01",
            "既然副头目都这么说了，那就没办法啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        "#5P赶快进去吧。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "#11P……可不要对那位大人\x01",
            "做出什么无礼的举动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        "#11P如果你们还想活久一点的话。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_EE(0x0, 0xA)
    ModifyEventFlags(0, 0, 0x80)
    OP_CA(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_38B8 end

    def Function_23_4719(): pass

    label("Function_23_4719")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 42000, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 0, 300, 45000, 180)
    SetChrPos(0x102, -400, 300, 45000, 180)
    SetChrPos(0x103, 400, 300, 45000, 180)
    SetChrPos(0x104, 0, 300, 45000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 0, 41700, 45)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 0, 41700, 315)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x2, 0x10)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    SetCameraDistance(19000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_487C():

        label("loc_487C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_487C")

    QueueWorkItem2(0x8, 2, lambda_487C)

    def lambda_488E():

        label("loc_488E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_488E")

    QueueWorkItem2(0x9, 2, lambda_488E)

    def lambda_48A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48A0)

    def lambda_48B1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48B1)
    Sleep(600)

    def lambda_48CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_48CE)

    def lambda_48DF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48DF)
    Sleep(400)

    def lambda_48FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_48FC)

    def lambda_490D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_490D)
    Sleep(600)

    def lambda_492A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_492A)

    def lambda_493B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_493B)
    Sleep(600)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    Sleep(4500)
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_68(0, 1100, 6500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 0, 0, 9000, 180)
    SetChrPos(0x102, 0, 0, 9000, 180)
    SetChrPos(0x103, 0, 0, 9000, 180)
    SetChrPos(0x104, 0, 0, 9000, 180)
    BeginChrThread(0x101, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x104, 3, 0, 27)
    OP_68(0, 1100, 3500, 5000)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)
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
        0x101,
        "#6P#0008F……真是败了啊。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        "#6P#0206F完全就像打发小孩子一样呢……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x104,
        "#0301F哼……真让人不爽啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        (
            "#6P#0005F对了，兰迪。\x02\x03",

            "他刚才为什么\x01",
            "要叫住你呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0248
    ChrTalk(
        0x104,
        (
            "#11P#0306F……谁知道呢。\x02\x03",

            "#0301F只不过，那个魁梧的男人，\x01",
            "可并不是单靠气势来唬人的。\x02\x03",

            "如果真要正面开战的话，\x01",
            "现在的我们恐怕不是他的对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#6P#0001F是吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0250
    ChrTalk(
        0x103,
        (
            "#12P#0203F在刚才的谈话中也能感觉到，\x01",
            "他根本就没把我们放在眼里……\x02\x03",

            "#0201F就好像不管我们做什么，\x01",
            "对他来说都是不痛不痒的……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……我也有这种感觉。\x02\x03",

            "#0001F虽说他背后有议员当靠山，\x01",
            "也不至于从容到这种地步吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#0108F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4D49():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D49)
    Sleep(100)
    TurnDirection(0x104, 0x102, 500)

    #C0253
    ChrTalk(
        0x101,
        "#6P#0005F艾莉……？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        "#2P#0305F怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0255
    ChrTalk(
        0x102,
        (
            "#0103F#5P啊……没什么。\x02\x03",

            "#0101F话说回来，我们接下来要怎么办？\x02\x03",

            "看样子，鲁巴彻这边的人\x01",
            "似乎知道相关线索呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊，你是说恐吓信的事吗？\x02\x03",

            "#0003F嗯，我本来也没打算\x01",
            "全盘相信那个副头目的话……\x02\x03",

            "#0001F但我认为，这件事跟鲁巴彻\x01",
            "可能确实没有关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4ECF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4ECF)
    Sleep(50)

    def lambda_4EDF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4EDF)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0257
    ChrTalk(
        0x102,
        "#0105F#5P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x103,
        (
            "#12P#0205F但是……他看到恐吓信之后，\x01",
            "明显有所反应啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0259
    ChrTalk(
        0x101,
        (
            "#6P#0004F嗯，没错，我想他应该是\x01",
            "注意到了什么。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德取出了恐吓信。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0261
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "立即中止新剧公演。\x01",
            "否则炎之舞姬\x01",
            "将会迎来悲剧──『银』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0262
    AnonymousTalk(
        0x101,
        "#0000F恐怕，他注意到的是──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFF9B9B9B, 0x1F4, 0x0)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0263
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K加尔西亚注意到了什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【恐吓信的笔迹】\x01",      # 0
            "【寄信人的名字】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_510B"),
        (1, "loc_526A"),
        (SWITCH_DEFAULT, "loc_52AA"),
    )


    label("loc_510B")


    #A0264
    AnonymousTalk(
        0x101,
        (
            "#0001F恐吓信的笔迹……\x01",
            "他因为笔迹而出现反应\x01",
            "的可能性，或许不能完全否定吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0265
    AnonymousTalk(
        0x103,
        (
            "#0203F的确，笔迹这种东西，\x01",
            "根据写信人的不同，\x01",
            "会有相当大的差异……\x02\x03",

            "#0200F但我记得，那位副头目好像是\x01",
            "看到最后才发出惊讶的声音的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0266
    AnonymousTalk(
        0x101,
        (
            "#0006F啊……是吗。\x01",
            "嗯，如此说来……\x02\x03",

            "#0008F写在那封信最后的……\x01",
            "是寄信人的名字……\x02\x03",

            "#0001F也许他是对这个产生了反应。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_52AA")

    label("loc_526A")

    OP_2C(0x42, 0x2)

    #A0267
    AnonymousTalk(
        0x101,
        (
            "#0001F寄信人的名字……\x01",
            "他应该是注意到了这个。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_52AA")

    label("loc_52AA")


    #A0268
    AnonymousTalk(
        0x104,
        "#0301F『银』……结果可疑的还是这家伙吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0269
    AnonymousTalk(
        0x102,
        (
            "#0101F莫非这个人物\x01",
            "与鲁巴彻之间\x01",
            "存在着某种关系？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0270
    AnonymousTalk(
        0x101,
        (
            "#0003F不，如果有关系的话，\x01",
            "那个副头目的反应就很奇怪了。\x02\x03",

            "#0001F他好像从一开始就确信\x01",
            "此事与他们没有任何关系……\x02\x03",

            "你们应该也有这种感觉吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0271
    AnonymousTalk(
        0x102,
        "#0105F啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0272
    AnonymousTalk(
        0x104,
        (
            "#0300F原来如此……\x01",
            "从他的表现看来，的确是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0273
    AnonymousTalk(
        0x103,
        (
            "#0203F跟鲁巴彻没有关系，\x01",
            "却能得到他们的强烈重视……\x02\x03",

            "#0201F大概就是这样一个人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0274
    AnonymousTalk(
        0x101,
        "#0004F嗯，我也是这么想的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)

    #C0275
    ChrTalk(
        0x102,
        (
            "#0103F#5P……如此说来……\x02\x03",

            "#0101F我们去找熟悉鲁巴彻\x01",
            "的人咨询一下比较好。\x02\x03",

            "比如法律事务所的伊安律师。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，是啊。\x02\x03",

            "#0006F其实，本来也想和\x01",
            "格蕾丝小姐谈谈的……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#11P#0306F哈，但要是告诉那位姐姐的话，\x01",
            "她恐怕会强迫我们把\x01",
            "恐吓信的事都透露出来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x103,
        (
            "#12P#0200F……正好可以当作\x01",
            "彩虹剧团的重大丑闻来报道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#6P#0003F是啊，所以说，\x01",
            "最好还是不要将她当做情报源了。\x02\x03",

            "#0000F还有就是……如果还想到什么\x01",
            "线索的话，就去调查看看吧。\x02\x03",

            "也许会在意想不到的地方\x01",
            "得到情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#0104F#5P嗯，有道理……\x02\x03",

            "#0102F……呵呵………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    #C0281
    ChrTalk(
        0x101,
        "#6P#0005F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        (
            "#0104F#5P不，没什么。\x02\x03",

            "#0100F那我们就快点\x01",
            "开始调查取证吧。\x02\x03",

            "不管中途去哪里，\x01",
            "记得最后一定要去法律事务所哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        "#6P#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_CA(0x1, 0xFF, 0x0)
    SetMapObjFlags(0x2, 0x10)
    OP_68(0, 1950, 2600, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 0, 0, 2600, 180)
    SetChrPos(0x1, 0, 0, 2600, 180)
    SetChrPos(0x2, 0, 0, 2600, 180)
    SetChrPos(0x3, 0, 0, 2600, 180)
    SetChrPos(0x8, -2000, 0, 41700, 1800)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x9, 2000, 0, 41700, 180)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0x80, 7)
    OP_29(0x42, 0x1, 0x4)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    EventEnd(0x5)
    Return()

    # Function_23_4719 end

    def Function_24_585F(): pass

    label("Function_24_585F")


    def lambda_5864():
        OP_95(0xFE, 0, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5864)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_24_585F end

    def Function_25_5885(): pass

    label("Function_25_5885")

    Sleep(700)

    def lambda_588D():
        OP_95(0xFE, 0, 0, 4700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_588D)
    WaitChrThread(0x102, 1)

    def lambda_58AB():
        OP_95(0xFE, -1000, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58AB)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_25_5885 end

    def Function_26_58CC(): pass

    label("Function_26_58CC")

    Sleep(1300)

    def lambda_58D4():
        OP_95(0xFE, 0, 0, 4700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58D4)
    WaitChrThread(0x103, 1)

    def lambda_58F2():
        OP_95(0xFE, 1000, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58F2)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_26_58CC end

    def Function_27_5913(): pass

    label("Function_27_5913")

    Sleep(2500)

    def lambda_591B():
        OP_95(0xFE, 0, 0, 3100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_591B)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_27_5913 end

    def Function_28_593C(): pass

    label("Function_28_593C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    OP_68(0, 1000, 42000, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -900, 0, 3600, 0)
    SetChrPos(0x102, 2150, 0, 2800, 0)
    SetChrPos(0x103, 2650, 0, 2200, 0)
    SetChrPos(0x104, -1100, 0, 2800, 0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, -8000, 0, 1000, 90)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 5000, 0, -300, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -2700, 0, 41000, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 2000, 0, 39000, 45)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -750, 0, 42000, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 3000, 0, 40000, 225)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 750, 0, 42000, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0x8, 3, 0, 29)
    BeginChrThread(0x9, 3, 0, 30)
    BeginChrThread(0x10, 3, 0, 31)
    SetCameraDistance(19000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(1000)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x10, 0x3)
    OP_68(0, 1100, 6500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(15500, 0)
    OP_68(0, 1100, 4500, 4000)
    Sleep(2000)

    def lambda_5B8C():
        OP_96(0xFE, 0x73A, 0x0, 0xAF0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B8C)
    Sleep(300)

    def lambda_5BA9():
        OP_96(0xFE, 0x5AA, 0x0, 0x898, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BA9)
    Sleep(400)

    def lambda_5BC6():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xE10, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BC6)
    Sleep(300)

    def lambda_5BE3():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xAF0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BE3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_64(0x9)
    OP_64(0x10)

    #C0284
    ChrTalk(
        0x102,
        (
            "#6P#0101F守卫人员果然\x01",
            "比平时要多呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#0301F#6P而且，能感觉到\x01",
            "超乎想象的强烈杀气呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        (
            "#6P#0206F焦躁与兴奋，警戒与不安……\x02\x03",

            "#0201F这些感情混杂在一起，\x01",
            "并传达了出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#6P#0001F肯定是在提防着\x01",
            "『黑月』的报复吧……\x02\x03",

            "#0006F……不过，真是糟糕啊。\x02\x03",

            "在如今这种状况下，很难确认\x01",
            "加尔西亚的动向──\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    StopBGM(0x7D0)

    #N0288
    NpcTalk(
        0xD,
        "豪气的声音",
        "#4P──要确认我什么啊？\x02",
    )

    CloseMessageWindow()
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
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    Fade(500)
    OP_68(-4400, 1000, 1400, 0)
    MoveCamera(301, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 800, 0, 2800, 270)
    SetChrPos(0x102, 1800, 0, 2700, 270)
    SetChrPos(0x103, 2100, 0, 1700, 270)
    SetChrPos(0x104, -600, 0, 3200, 225)
    ClearChrFlags(0xD, 0x8)
    OP_68(-1400, 1000, 1400, 3000)

    def lambda_5E87():
        OP_95(0xFE, -3000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5E87)
    Sleep(700)

    def lambda_5EA4():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EA4)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0289
    ChrTalk(
        0x101,
        "#12P#0005F加尔西亚·罗西……！\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        (
            "#0301F可恶，身体那么魁梧，\x01",
            "却如此善于隐藏气息……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1852, 255, 100, 0)    #voice#Garcia
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0291
    AnonymousTalk(
        0xD,
        (
            "哼，原来是你们啊。\x02\x03",

            "都发生过那种事情了，\x01",
            "居然还敢大摇大摆地\x01",
            "找上门来？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0292
    ChrTalk(
        0x101,
        (
            "#12P#0013F呃……\x02\x03",

            "#0003F……我们不会找借口的。\x02\x03",

            "#0001F与你们达成的和解，\x01",
            "仅限于琪雅那件事而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "#3104F#5P哼哼，知道就好。\x02\x03",

            "#3102F要是你们不知所谓，妄想用之前的和解\x01",
            "来当挡箭牌，趁机混进来的话，\x01",
            "我会当场把你们打扁的。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        "#12P#0001F………………………………\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x104,
        "#0306F哼，真是个危险的大叔啊。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xD,
        (
            "#3103F#5P……我知道你们为什么要\x01",
            "偷偷摸摸地四处打探。\x02\x03",

            "但是关于这件事情，\x01",
            "我连一个字都不会透露的。\x02\x03",

            "#3101F赶快消失吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        "#12P#0013F呃……\x02",
    )

    CloseMessageWindow()

    def lambda_619B():

        label("loc_619B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_619B")

    QueueWorkItem2(0x101, 2, lambda_619B)

    def lambda_61AD():

        label("loc_61AD")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_61AD")

    QueueWorkItem2(0x102, 2, lambda_61AD)

    def lambda_61BF():

        label("loc_61BF")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_61BF")

    QueueWorkItem2(0x103, 2, lambda_61BF)

    def lambda_61D1():

        label("loc_61D1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_61D1")

    QueueWorkItem2(0x104, 2, lambda_61D1)

    def lambda_61E3():
        OP_95(0xFE, 200, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_61E3)
    Sleep(400)

    def lambda_6200():
        OP_96(0xFE, 0x44C, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6200)
    WaitChrThread(0xD, 1)

    def lambda_621E():
        OP_95(0xFE, 200, 0, 6800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_621E)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    Fade(1000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_68(0, 500, 11500, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 400, 0, 1800, 0)
    SetChrPos(0x102, 1300, 0, 2700, 0)
    SetChrPos(0x103, 1600, 0, 1700, 0)
    SetChrPos(0x104, -1000, 0, 2900, 0)
    SetChrPos(0xD, 0, 0, 6000, 0)

    def lambda_62D8():
        OP_96(0xFE, 0x0, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_62D8)
    OP_0D()

    def lambda_62F3():
        OP_96(0xFE, 0x0, 0x0, 0xE10, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62F3)
    WaitChrThread(0x101, 1)

    #C0298
    ChrTalk(
        0x101,
        (
            "#6P#0003F──只有一件事，请务必告诉我。\x02\x03",

            "#0001F如果您准备向全副武装的\x01",
            "敌人总根据地发动进攻……\x02\x03",

            "会从正面直接突入，发起强行攻击吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0299
    ChrTalk(
        0xD,
        (
            "#5P#3104F哈，正规的猎兵团绝对\x01",
            "不会采用这种愚蠢的作战方案。\x02\x03",

            "一定要尽可能利用一切对自己有利的条件，\x01",
            "争取以最低的损失，换取最大的战果。\x02\x03",

            "#3100F对吧……『斗神之子』？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        (
            "#6P#0303F不要用那个名字叫我。\x02\x03",

            "#0301F……不过，你刚才说的这些，\x01",
            "的确是猎兵的基本作风。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#6P#0000F是吗……\x02\x03",

            "#0004F──谢谢，\x01",
            "感谢您能做出回答。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "#5P#3100F哼哼……真是个奇怪的小鬼。\x02\x03",

            "#3103F不过，这里面可不是\x01",
            "你们可以随随便便进来的地方。\x02\x03",

            "#3101F要是敢乱来的话，真的会送命呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_657C():
        OP_96(0xFE, 0x0, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_657C)
    Sleep(1000)
    OP_68(0, 500, 6100, 3000)
    MoveCamera(0, 16, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20470, 3000)
    Sleep(2000)
    StopBGM(0xFA0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)

    #C0303
    ChrTalk(
        0x101,
        (
            "#0006F#5P总觉得，他的样子有点奇怪啊。\x02\x03",

            "#0001F虽然看起来很紧张，但似乎\x01",
            "又有点心不在焉的泄气感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#0106F#11P……是啊。\x02\x03",

            "#0108F说的话虽然挺恐怖，\x01",
            "但却完全感觉不到他的杀气……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#0206F#11P看上去好像有点累了，\x01",
            "大概就是这种感觉吧……\x02\x03",

            "#0201F到底发生了什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#0308F#5P嘁……\x01",
            "真不像那大叔的作风啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    #N0307
    NpcTalk(
        0xE,
        "女性的声音",
        (
            "#1P嗯哼哼哼，\x01",
            "想知道原因吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1100, 2100, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 0, 0, 3600, 90)
    SetChrPos(0x102, 1800, 0, 2700, 90)
    SetChrPos(0x103, 2100, 0, 1700, 90)
    SetChrPos(0x104, -1000, 0, 2900, 90)

    def lambda_686C():

        label("loc_686C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_686C")

    QueueWorkItem2(0x101, 2, lambda_686C)

    def lambda_687E():

        label("loc_687E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_687E")

    QueueWorkItem2(0x102, 2, lambda_687E)

    def lambda_6890():

        label("loc_6890")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_6890")

    QueueWorkItem2(0x103, 2, lambda_6890)

    def lambda_68A2():

        label("loc_68A2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_68A2")

    QueueWorkItem2(0x104, 2, lambda_68A2)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x4)

    def lambda_68BE():
        OP_96(0xFE, 0x0, 0x0, 0x2BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_68BE)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x0, 0x1F4)
    OP_6F(0x1)

    #C0308
    ChrTalk(
        0x101,
        "#0005F#11P格、格蕾丝小姐……！？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#5P#0306F不要老是吓人啊，\x01",
            "真是个神出鬼没的姐姐……\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0310
    AnonymousTalk(
        0xE,
        (
            "哼，这才是所谓的记者之魂啊。\x02\x03",

            "那么，就按照老规矩，\x01",
            "我们来互相帮助——交换情报吧¤\x02\x03",

            "我就在那边的爵士酒吧里等你们哟⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    OP_93(0xE, 0x10E, 0x1F4)
    OP_68(-2790, 1100, 3330, 3000)

    def lambda_6A35():
        OP_95(0xFE, -10300, 0, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6A35)
    WaitChrThread(0xE, 1)

    def lambda_6A53():
        OP_95(0xFE, -10300, 1500, 5400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6A53)
    Sleep(500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0xE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_6A9F():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6A9F)
    Sleep(500)

    def lambda_6ABC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_6ABC)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xE, 2)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_68(-30, 1100, 3120, 2500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)

    #C0311
    ChrTalk(
        0x102,
        "#12P#0106F……要怎么办？\x02",
    )

    CloseMessageWindow()

    def lambda_6B82():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B82)
    Sleep(50)
    OP_93(0x104, 0x5A, 0x1F4)

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯，总之先去听听她想说什么吧。\x02\x03",

            "#0001F不过有必要注意，\x01",
            "一定不要说得太多。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#12P#0211F是啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 1950, 2600, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 0, 0, 2600, 180)
    SetChrPos(0x1, 0, 0, 2600, 180)
    SetChrPos(0x2, 0, 0, 2600, 180)
    SetChrPos(0x3, 0, 0, 2600, 180)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0xC2, 5)
    OP_29(0x4B, 0x1, 0x3)
    OP_1B(0x2, 0x0, 0x25)
    EventEnd(0x5)
    Return()

    # Function_28_593C end

    def Function_29_6CDF(): pass

    label("Function_29_6CDF")

    OP_93(0x8, 0xCD, 0x1F4)

    def lambda_6CEB():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6CEB)
    WaitChrThread(0x8, 1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_93(0x8, 0x19, 0x1F4)

    def lambda_6D30():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6D30)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    Return()

    # Function_29_6CDF end

    def Function_30_6D4C(): pass

    label("Function_30_6D4C")

    Sleep(1500)

    label("loc_6D4F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D7A")
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)
    OP_64(0x9)
    Sleep(2500)
    Jump("loc_6D4F")

    label("loc_6D7A")

    Return()

    # Function_30_6D4C end

    def Function_31_6D7B(): pass

    label("Function_31_6D7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DA6")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)
    OP_64(0x10)
    Sleep(2500)
    Jump("Function_31_6D7B")

    label("loc_6DA6")

    Return()

    # Function_31_6D7B end

    def Function_32_6DA7(): pass

    label("Function_32_6DA7")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 900, 40500, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_EE(0x0, 0x5)
    SetChrPos(0x101, -600, 0, 34200, 0)
    SetChrPos(0x102, 600, 0, 34200, 0)
    SetChrPos(0x103, -1200, 0, 33000, 0)
    SetChrPos(0x104, 1200, 0, 33000, 0)
    OP_68(0, 900, 35500, 4000)
    SetCameraDistance(20000, 4000)
    OP_0D()
    OP_6F(0x1)

    #C0314
    ChrTalk(
        0x102,
        "#0101F#6P连一个看守人员都没有……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x104,
        (
            "#12P#0306F是啊，昨天来看的时候，\x01",
            "守卫人员比平时还要多呢……\x02\x03",

            "#0301F可是，也没有发现争斗的迹象啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#0008F#6P是啊，本来还以为是\x01",
            "『黑月』进行了报复呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6F5F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F5F)
    Sleep(50)

    def lambda_6F6F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F6F)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0317
    ChrTalk(
        0x101,
        "#11P#0005F缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x102,
        "#0105F#11P怎么了？\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x103,
        (
            "#6P#0203F……太过安静了。\x02\x03",

            "#0201F完全感觉不到建筑物中\x01",
            "有人的气息呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0320
    ChrTalk(
        0x101,
        "#11P#0011F哎……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0321
    ChrTalk(
        0x103,
        (
            "#6P#0206F严格地说，\x01",
            "里面应该有一个人……\x02\x03",

            "#0208F但是，除了那人之外，\x01",
            "完全感觉不到其他人的气息……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x104,
        (
            "#11P#0301F喂喂……\x01",
            "到底是怎么一回事啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0323
    ChrTalk(
        0x101,
        (
            "#0003F#6P里面的那个人，\x01",
            "很有可能就是达德利警官吧。\x02\x03",

            "#0013F好……\x01",
            "谨慎起见，还是进去确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7178():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7178)
    Sleep(50)

    def lambda_7188():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7188)
    Sleep(50)

    def lambda_7198():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7198)
    WaitChrThread(0x102, 2)

    #C0324
    ChrTalk(
        0x102,
        "#0101F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_EE(0x0, 0xA)
    SetScenarioFlags(0xC4, 0)
    EventEnd(0x5)
    Return()

    # Function_32_6DA7 end

    def Function_33_71D9(): pass

    label("Function_33_71D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F5")
    Call(0, 35)
    Return()

    label("loc_71F5")

    Jump("loc_7216")

    label("loc_71FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7216")
    Call(0, 34)
    Return()

    label("loc_7216")

    EventBegin(0x1)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x0, -500, 0, 34000, 0)
    SetChrPos(0x1, 500, 0, 33750, 0)
    SetChrPos(0x2, -500, 0, 32500, 0)
    SetChrPos(0x3, 500, 0, 32250, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72A9")
    SetChrPos(0x4, -500, 0, 31000, 0)

    label("loc_72A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72C8")
    SetChrPos(0x5, 500, 0, 30750, 0)

    label("loc_72C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7331")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_END)), "loc_7324")

    #N0325
    NpcTalk(
        0x8,
        "黑衣人",
        (
            "臭小鬼……\x01",
            "不许进来。\x02",
        )
    )

    CloseMessageWindow()

    #N0326
    NpcTalk(
        0x9,
        "黑衣人",
        "赶快给我消失。\x02",
    )

    CloseMessageWindow()

    label("loc_7324")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_7916")

    label("loc_7331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73B3")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_END)), "loc_73A6")

    #C0327
    ChrTalk(
        0x8,
        (
            "警察局的臭小鬼……\x01",
            "来这里有什么事啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x9,
        (
            "哼哼，赶快消失吧。\x01",
            "这里是私人所有地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73A6")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_7916")

    label("loc_73B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75F0")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A0")

    #C0329
    ChrTalk(
        0x8,
        "嗯？干什么，臭小鬼。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "快点滚开。\x01",
            "这里是私人所有地。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x9,
        (
            "嗯……等一下。\x01",
            "那张脸，你们是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 400)
    Sleep(300)

    #C0332
    ChrTalk(
        0x8,
        "嘁，原来是之前那些…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_751A")

    #C0333
    ChrTalk(
        0x101,
        (
            "#0001F（……看起来，这栋建筑\x01",
            "  好像和黑手党有关啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#0101F（走吧……\x01",
            "  引起骚乱可就不妙了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7598")

    label("loc_751A")


    #C0335
    ChrTalk(
        0x101,
        (
            "#0001F（今天也在啊……）\x02\x03",

            "（……看起来，这栋建筑\x01",
            "　好像和黑手党有关啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#0101F（走吧……\x01",
            "  引起骚乱可就不妙了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7598")

    SetScenarioFlags(0x88, 0)
    Jump("loc_75E3")

    label("loc_75A0")


    #C0337
    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "哼……不想受伤的话，\x01",
            "就快点滚开吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75E3")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_7916")

    label("loc_75F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77AC")
    OP_68(250, 2950, 35310, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7671")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_7671")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_768A")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_768A")

    OP_68(250, 1950, 35310, 3000)
    Sleep(3200)

    #A0339
    AnonymousTalk(
        0x101,
        "#0001F（今天的气氛可真严肃啊……）\x02",
    )

    CloseMessageWindow()

    #A0340
    AnonymousTalk(
        0x104,
        (
            "#0301F（是啊，而且杀气比想象中\x01",
            "  的还要强烈呢。）\x02",
        )
    )

    CloseMessageWindow()

    #A0341
    AnonymousTalk(
        0x102,
        (
            "#0101F（是因为刚去袭击过\x01",
            "  黑月吧。）\x02\x03",

            "（……而且，\x01",
            "  好像也有点神经紧绷的感觉……）\x02",
        )
    )

    CloseMessageWindow()

    #A0342
    AnonymousTalk(
        0x103,
        (
            "#0200F（……这附近的气氛\x01",
            "  有如刺痛般紧张，\x01",
            "  还是不要靠近为好。）\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x2, 0x0, 0x25)
    SetScenarioFlags(0xC8, 7)
    Jump("loc_7916")

    label("loc_77AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7916")
    OP_68(250, 2950, 35310, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_782D")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_782D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7846")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_7846")

    OP_68(250, 1950, 35310, 3000)
    Sleep(3200)

    #A0343
    AnonymousTalk(
        0x101,
        (
            "#0005F哎？\x01",
            "没有看守人员呢……\x02",
        )
    )

    CloseMessageWindow()

    #A0344
    AnonymousTalk(
        0x103,
        "#0200F是啊……\x02",
    )

    CloseMessageWindow()

    #A0345
    AnonymousTalk(
        0x104,
        (
            "#0301F都进里面去了吗？\x02\x03",

            "……不管怎么说，\x01",
            "还是不要接近这里为好。\x02",
        )
    )

    CloseMessageWindow()

    #A0346
    AnonymousTalk(
        0x102,
        (
            "#0101F是啊，看起来，在这里\x01",
            "应该也找不到什么有用的情报。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 0)

    label("loc_7916")

    OP_68(90, 1950, 4620, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 90, 0, 4620, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7968")
    Jump("loc_7983")

    label("loc_7968")

    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)

    label("loc_7983")

    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79C8")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_79C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79E1")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_79E1")

    EventEnd(0x4)
    Return()

    # Function_33_71D9 end

    def Function_34_79E4(): pass

    label("Function_34_79E4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x101, -500, 0, 31000, 0)
    SetChrPos(0x102, 500, 0, 30750, 0)
    SetChrPos(0x103, -500, 0, 29500, 0)
    SetChrPos(0x104, 500, 0, 29250, 0)

    def lambda_7A79():
        OP_98(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A79)
    Sleep(50)

    def lambda_7A96():
        OP_98(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A96)
    Sleep(50)

    def lambda_7AB3():
        OP_98(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7AB3)
    Sleep(50)

    def lambda_7AD0():
        OP_98(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7AD0)
    OP_68(0, 1950, 37000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0347
    NpcTalk(
        0x8,
        "黑衣人",
        "……喂，小鬼们。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #N0348
    NpcTalk(
        0x8,
        "黑衣人",
        "来这里有事吗？\x02",
    )

    CloseMessageWindow()

    #N0349
    NpcTalk(
        0x9,
        "黑衣人",
        (
            "前方就是私人所有地了，\x01",
            "不要随便进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        "#0005F（……他们是谁啊……？）\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(0, 1500, 1000, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 0, 0, 2340, 180)
    SetChrPos(0x102, -1000, 0, 1750, 135)
    SetChrPos(0x103, 1000, 0, 1750, 225)
    SetChrPos(0x104, 0, 0, 0, 0)
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -24330, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)
    OP_4B(0xB, 0xFF)
    OP_0D()

    #C0351
    ChrTalk(
        0x104,
        "#0301F看来好像并非善类啊。\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#0003F嗯，应该是黑道的人吧。\x02\x03",

            "#0001F以后有机会的话，很想进去调查一下呢……\x01",
            "不过目前来看，还是不要贸然刺激他们为好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 2340, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x46, 6)
    EventEnd(0x5)
    Return()

    # Function_34_79E4 end

    def Function_35_7D18(): pass

    label("Function_35_7D18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x101, -500, 0, 31000, 0)
    SetChrPos(0x102, 500, 0, 30750, 0)
    SetChrPos(0x103, -500, 0, 29500, 0)
    SetChrPos(0x104, 500, 0, 29250, 0)

    def lambda_7DAD():
        OP_98(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DAD)
    Sleep(50)

    def lambda_7DCA():
        OP_98(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DCA)
    Sleep(50)

    def lambda_7DE7():
        OP_98(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7DE7)
    Sleep(50)

    def lambda_7E04():
        OP_98(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E04)
    OP_68(0, 1950, 37000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x8,
        "……喂，小鬼们。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0354
    ChrTalk(
        0x8,
        "来这里有事吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0355
    ChrTalk(
        0x8,
        "嗯？警察徽章……？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "难道说，这些家伙就是\x01",
            "让法比奥他们行动失败的……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        "喂喂，真的假的！？\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        "他们不只是一群小鬼头吗！？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#0001F（……看样子，这栋\x01",
            "  建筑物好像和黑手党有关啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#0101F（还是走吧……\x01",
            "  引起骚乱可就不妙了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1950, 2340, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 0, 0, 2340, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)
    SetScenarioFlags(0x68, 0)
    EventEnd(0x5)
    Return()

    # Function_35_7D18 end

    def Function_36_8007(): pass

    label("Function_36_8007")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    def lambda_8016():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8016)
    Sleep(50)

    def lambda_8026():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8026)
    WaitChrThread(0x8, 1)

    #C0361
    ChrTalk(
        0x8,
        (
            "喂，别在这里\x01",
            "四处乱转……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x9,
        "快点给我滚吧，小鬼们。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrPos(0x0, -100, 0, 41020, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_36_8007 end

    def Function_37_8097(): pass

    label("Function_37_8097")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_826C")

    #C0363
    ChrTalk(
        0x101,
        "#0001F等等，这前面是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8133")

    #C0364
    ChrTalk(
        0x102,
        (
            "#0101F鲁巴彻商会……\x02\x03",

            "虽然我们已经达成了和解，\x01",
            "但最好还是不要随便露面吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F4")

    label("loc_8133")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8191")

    #C0365
    ChrTalk(
        0x103,
        (
            "#0203F鲁巴彻商会……\x02\x03",

            "虽说已经达成了和解，\x01",
            "但还是不应该随便露面吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F4")

    label("loc_8191")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81F4")

    #C0366
    ChrTalk(
        0x104,
        (
            "#0301F鲁巴彻商会……\x02\x03",

            "虽然和他们已经达成了和解，\x01",
            "但也不应该随随便便地露面吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F4")


    #C0367
    ChrTalk(
        0x153,
        (
            "#1111F？？？\x01",
            "怎么了吗——？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#0000F不，没什么。\x02\x03",

            "#0003F（……走吧。\x01",
            "  去那种地方，毕竟还是太危险了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 1)
    Jump("loc_82CB")

    label("loc_826C")


    #C0369
    ChrTalk(
        0x101,
        (
            "#0001F（这前面就是鲁巴彻商会了。）\x02\x03",

            "（……虽然我们达成了和解，\x01",
            "  但还是不能随便进去啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8440")

    #C0370
    ChrTalk(
        0x104,
        (
            "#0301F鲁巴彻商会……\x01",
            "那件事发生之后，似乎仍然在正常运营啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#0103F虽然因为小琪雅的那件事，\x01",
            "暂时安分了一段时间……\x02\x03",

            "#0101F但自从达成和解之后，\x01",
            "他们似乎又重新开始『营业』了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#0001F之前发生了很多事情啊……\x01",
            "还是别去刺激他们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8438")

    #C0373
    ChrTalk(
        0x109,
        (
            "#0501F（虽然我听说了传闻……不过看起来，\x01",
            "  罗伊德警官和大家好像都很辛苦呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8438")

    SetScenarioFlags(0xC9, 2)
    Jump("loc_8499")

    label("loc_8440")


    #C0374
    ChrTalk(
        0x101,
        (
            "#0001F（这前面就是鲁巴彻商会了。）\x02\x03",

            "（最好不要贸然刺激他们，\x01",
            "  还是别随便靠近了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84F2")

    #C0375
    ChrTalk(
        0x101,
        (
            "#0001F（看起来，戒备比想象中的还要森严……\x01",
            "  还是别随便靠近了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8579")

    #C0376
    ChrTalk(
        0x101,
        (
            "#0001F（副头目加尔西亚。\x01",
            "  虽然他的态度稍微有些奇怪，令人在意……）\x02\x03",

            "（但现在还是先去听听格蕾丝小姐会说些什么吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86CE")
    TurnDirection(0x13D, 0x0, 500)

    #C0377
    ChrTalk(
        0x13D,
        (
            "#2105F哎呀，你们难道要\x01",
            "进入鲁巴彻内部吗？\x02\x03",

            "#2103F这实在是太鲁莽了啊……\x02\x03",

            "#2109F嗯，不过，如果你们非要进去，\x01",
            "我也阻止不了⊥\x01",
            "只能全力随行，进行秘密报道啦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            "#0006F不……现在还是不用了。\x01",
            "（至少不想当着格蕾丝小姐\x01",
            "  的面进去调查啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x102,
        (
            "#0101F很担心冈兹先生呢……\x01",
            "还是赶快去『巴鲁卡』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8717")

    label("loc_86CE")


    #C0380
    ChrTalk(
        0x101,
        (
            "#0003F（现在得优先解决冈兹先生的事情。\x01",
            "  ……赶快去『巴鲁卡』吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_876F")

    #C0381
    ChrTalk(
        0x101,
        (
            "#0001F（鲁巴彻的人今天好像\x01",
            "  也情绪激昂呢……\x01",
            "  还是别随便靠近了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_876F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87DA")

    #C0382
    ChrTalk(
        0x101,
        (
            "#0001F（虽然好像没人看守，\x01",
            "  但还是不要贸然刺激他们吧……）\x02\x03",

            "（别随便接近这里了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87DA")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Return()

    # Function_37_8097 end

    def Function_38_87EE(): pass

    label("Function_38_87EE")

    EventBegin(0x1)

    #C0383
    ChrTalk(
        0x101,
        (
            "#0001F比克森镇长说的话很令人在意啊……\x01",
            "现在还是赶快去『巴鲁卡』看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_38_87EE end

    SaveToFile()

Try(main)
