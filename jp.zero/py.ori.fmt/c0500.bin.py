from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "マフィア",               # 1
        "マフィア",               # 2
        "客引きビッシュ",         # 3
        "アイリス",               # 4
        "フランツ巡査",           # 5
        "ガルシア",               # 6
        "グレイス",               # 7
        "マフィア",               # 8
        "マフィア",               # 9
        "マフィア",               # 10
        "中央広場",               # 11
        "西通り",                 # 12
        "行政区",                 # 13
        "住宅街",                 # 14
        "歓楽街",                 # 15
        "東通り",                 # 16
        "旧市街",                 # 17
        "港湾区",                 # 18
        "ＩＢＣ",                 # 19
        "駅前通り",               # 20
        "裏通り",                 # 21
        "ウルスラ間道",           # 22
        "東クロスベル街道",       # 23
        "西クロスベル街道",       # 24
        "マインツ山道",           # 25
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

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央広場")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西通り")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "東通り")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧市街")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "裏通り")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "マインツ山道")
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
        "Function_5_DB2",          # 05, 5
        "Function_6_EFF",          # 06, 6
        "Function_7_104C",         # 07, 7
        "Function_8_1123",         # 08, 8
        "Function_9_11C2",         # 09, 9
        "Function_10_1FF3",        # 0A, 10
        "Function_11_21DB",        # 0B, 11
        "Function_12_328D",        # 0C, 12
        "Function_13_3489",        # 0D, 13
        "Function_14_3612",        # 0E, 14
        "Function_15_370D",        # 0F, 15
        "Function_16_3729",        # 10, 16
        "Function_17_37E3",        # 11, 17
        "Function_18_3879",        # 12, 18
        "Function_19_3932",        # 13, 19
        "Function_20_39CA",        # 14, 20
        "Function_21_3A54",        # 15, 21
        "Function_22_3DE5",        # 16, 22
        "Function_23_4CF2",        # 17, 23
        "Function_24_5F76",        # 18, 24
        "Function_25_5F9C",        # 19, 25
        "Function_26_5FE3",        # 1A, 26
        "Function_27_602A",        # 1B, 27
        "Function_28_6053",        # 1C, 28
        "Function_29_74C2",        # 1D, 29
        "Function_30_752F",        # 1E, 30
        "Function_31_755E",        # 1F, 31
        "Function_32_758A",        # 20, 32
        "Function_33_79F4",        # 21, 33
        "Function_34_828D",        # 22, 34
        "Function_35_85C1",        # 23, 35
        "Function_36_88D4",        # 24, 36
        "Function_37_8974",        # 25, 37
        "Function_38_9115",        # 26, 38
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D61")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_CEA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_D5C")

    label("loc_CEA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D5C")

    Jump("loc_DA6")

    label("loc_D61")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_DA6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C65 end

    def Function_5_DB2(): pass

    label("Function_5_DB2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAE")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_E37")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_EA9")

    label("loc_E37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EA9")

    Jump("loc_EF3")

    label("loc_EAE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EF3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_DB2 end

    def Function_6_EFF(): pass

    label("Function_6_EFF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFB")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x69, 1)"), scpexpr(EXPR_END)), "loc_F84")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_FF6")

    label("loc_F84")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FF6")

    Jump("loc_1040")

    label("loc_FFB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1040")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_EFF end

    def Function_7_104C(): pass

    label("Function_7_104C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_10BB")

    #C0010
    ChrTalk(
        0x8,
        (
            "おいお前ら……\x01",
            "もう用事はねえはずだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "クク、それとも若頭に\x01",
            "可愛がって欲しいのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111F")

    label("loc_10BB")


    #C0012
    ChrTalk(
        0x8,
        (
            "オイオイ坊主ども、\x01",
            "お帰りはあっちだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "怖い目に遭いたくなかったら\x01",
            "さっさと失せるんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111F")

    TalkEnd(0xFE)
    Return()

    # Function_7_104C end

    def Function_8_1123(): pass

    label("Function_8_1123")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1159")

    #C0014
    ChrTalk(
        0xFE,
        (
            "いつまでうろついてんだ、\x01",
            "アア？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BE")

    label("loc_1159")


    #C0015
    ChrTalk(
        0x9,
        "《ルバーチェ商会》に何か用事か？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "ハッ、若頭がお会いになった程度で\x01",
            "調子こいてんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BE")

    TalkEnd(0xFE)
    Return()

    # Function_8_1123 end

    def Function_9_11C2(): pass

    label("Function_9_11C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1259")

    #C0017
    ChrTalk(
        0xA,
        (
            "ぺろり……どこかに\x01",
            "ええお客さんおらへんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "ワテがハッピーな世界に\x01",
            "連れて行ってあげようやん。\x01",
            "うひゃひゃひゃ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E1")

    label("loc_1259")


    #C0019
    ChrTalk(
        0xA,
        (
            "なんや釈然とせんまま\x01",
            "日が暮れてきたね。\x01",
            "今日はほんまおかしな一日やわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        (
            "……まあええわ、商売始めよか。\x01",
            "時は金なりやしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12E1")

    Jump("loc_1FEF")

    label("loc_12E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1393")

    #C0021
    ChrTalk(
        0xFE,
        (
            "なんや……昨日に続いて\x01",
            "今日も通りが静かやね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "こう、いつもうごめいとった\x01",
            "この街の『黒いシミ』が\x01",
            "感じられんちゅうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "……なんや静かすぎるわー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_158A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1439")

    #C0024
    ChrTalk(
        0xA,
        (
            "（あの人な、元猟兵やったっちゅう噂や。\x01",
            "  関わったらろくな死に方でけへんで。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        (
            "（やめとき、やめとき！\x01",
            "  ……触らぬが吉や。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C5")

    label("loc_1439")


    #C0026
    ChrTalk(
        0xA,
        (
            "（さっきのごついお兄さん、\x01",
            "  ルバーチェの若頭やろ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "（あんたら何やらかしてん……\x01",
            "  あの人に睨まれたら\x01",
            "  タダやすまへんで？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14C5")

    Jump("loc_1585")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1548")

    #C0028
    ChrTalk(
        0xFE,
        (
            "なんや、今日は通りが静かやなぁ……\x01",
            "誰も通りがからへんやん。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "お客さん来んと、\x01",
            "ワテ泣いてしまうよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1585")

    label("loc_1548")


    #C0030
    ChrTalk(
        0xFE,
        (
            "なんや、今日は通りが静かやなぁ……\x01",
            "気のせいかいなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1585")

    Jump("loc_1FEF")

    label("loc_158A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1649")

    #C0031
    ChrTalk(
        0xA,
        (
            "……あ、お客さんお客さん。\x01",
            "耳寄りな情報教えてあげるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "うちの店、新サービス初めたんよ～。\x01",
            "２時間遊んで１０００ミラぽっきり！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "な、どう？\x01",
            "ちょっと覗いてみやへん？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1796")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16D5")

    #C0034
    ChrTalk(
        0xA,
        (
            "いよいよ……待ちに待った\x01",
            "自治州議会やね！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "ワテ、記念祭と\x01",
            "この時期が一ッ番好きやね。\x01",
            "うっひゃっひゃっひゃ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1791")

    label("loc_16D5")


    #C0036
    ChrTalk(
        0xA,
        (
            "いよいよ……待ちに待った\x01",
            "自治州議会やね！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xA,
        (
            "記念祭もえらい稼ぎ時やけど、\x01",
            "議会の間もいろ～んなお客さんが来るんや。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "またまた儲けさせてもらいまっせ～！\x01",
            "うっひゃっひゃっひゃ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1791")

    Jump("loc_1FEF")

    label("loc_1796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_18C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1816")

    #C0039
    ChrTalk(
        0xA,
        (
            "ワテはこう見えて\x01",
            "結構世話好きなんやで。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        (
            "今日は若い子らに\x01",
            "ぱーっとおごったるわ。\x01",
            "ひゃっはっは！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_1816")


    #C0041
    ChrTalk(
        0xA,
        (
            "今日は店の若い子ら集めて\x01",
            "新人の歓迎会やるんや。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "若い子３人も入ったし\x01",
            "店にも慣れてもらわなな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "ひゃっはっは、\x01",
            "今日はワテのおごりや。\x01",
            "ぱーっと行こうやん！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18C1")

    Jump("loc_1FEF")

    label("loc_18C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_199B")

    #C0044
    ChrTalk(
        0xFE,
        (
            "ああ……参った参った。\x01",
            "ウチの店の女の子、\x01",
            "昨日１人引き抜かれてしもてん。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "へへへ、まあいいわ。\x01",
            "女の子なら仰山おるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "それよりどう、お兄さん。\x01",
            "うちの店、今日は\x01",
            "ハッピーセールしてるで？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_199B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A23")

    #C0047
    ChrTalk(
        0xA,
        (
            "ん～、お兄さんら\x01",
            "遊びに来たんちゃうのん？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "こんな時間に\x01",
            "ウロウロしてたらアカンよ。\x01",
            "間違えてしまうわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_1A23")


    #C0049
    ChrTalk(
        0xA,
        "こんにちわ～……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        (
            "なんやなんや～、お兄さんら。\x01",
            "しょぼくれた顔してるやん。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "よし、ワテが気晴らしさせてあげよ。\x01",
            "さ、こっち行こ行こ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1AB6")

    Jump("loc_1FEF")

    label("loc_1ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B44")

    #C0052
    ChrTalk(
        0xA,
        (
            "何してるのか知らんけど、\x01",
            "犬の吼え声とか聞こえたりするしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "ヤの人たちも\x01",
            "もう少し静かにしてもらわんと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD5")

    label("loc_1B44")


    #C0054
    ChrTalk(
        0xA,
        (
            "最近ヤの人たち、\x01",
            "どたばたしてるみたいやねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "やあ、困ったわ。\x01",
            "うちの店あそこのビルに近いねん。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        "お客さんも怖がってしまうんよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BD5")

    Jump("loc_1FEF")

    label("loc_1BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C67")

    #C0057
    ChrTalk(
        0xFE,
        (
            "ほら、みてみて。\x01",
            "新しいネックレス買ったんや。\x01",
            "……きらきらのピッカピカ！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ひゃっはっは！\x01",
            "客引きはホンマええ商売やわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CAF")

    #C0059
    ChrTalk(
        0xA,
        (
            "ウチの店大損やん……\x01",
            "ほんま堪忍してや～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D50")

    label("loc_1CAF")


    #C0060
    ChrTalk(
        0xFE,
        "さっき遊撃士の人がきたんや。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "なんや理由付けて、うちの\x01",
            "若い子連れて行ってしもうたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……あの子、給料前借してんねんで！？\x01",
            "ほんま堪忍してや～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D50")

    Jump("loc_1FEF")

    label("loc_1D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E07")

    #C0063
    ChrTalk(
        0xFE,
        "うちの店は若い子多いよ。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "一日中接客すんのも大変やけど\x01",
            "お給料はメチャええからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "中にはお給料前借りしとる子もおってね。\x01",
            "ほんま、みんなガメついわぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1ED6")

    #C0066
    ChrTalk(
        0xA,
        (
            "こんにちわ～。\x01",
            "今日も観光客多いみたいやね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        (
            "みんなして店に来てくれたら\x01",
            "お客さんもハッピー。\x01",
            "ワテらもハッピー。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "ほらほら、一緒に\x01",
            "ハッピーになりましょうやん。\x01",
            "うっひゃっひゃ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 2)), scpexpr(EXPR_END)), "loc_1F51")

    #C0069
    ChrTalk(
        0xA,
        (
            "そこの路地奥\x01",
            "近寄らん方がええよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "ヤの付く兄さんたちや。\x01",
            "ワテらよりよっぽどタチ悪いで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F54")

    label("loc_1F51")

    Call(0, 10)

    label("loc_1F54")

    Jump("loc_1FEF")

    label("loc_1F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 2)), scpexpr(EXPR_END)), "loc_1FEC")

    #C0071
    ChrTalk(
        0xA,
        (
            "あんまこの近く\x01",
            "ウロウロせん方がええよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "ワテみたいなモンに捕まったら\x01",
            "ケツの毛まで抜かれてしまうさかいな。\x01",
            "ひゃっはっは！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1FEC")

    Call(0, 10)

    label("loc_1FEF")

    TalkEnd(0xFE)
    Return()

    # Function_9_11C2 end

    def Function_10_1FF3(): pass

    label("Function_10_1FF3")


    #C0073
    ChrTalk(
        0xA,
        (
            "あ、お兄さんら観光客？\x01",
            "どう、暇してるんとちゃう？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "それやったらワテに任せとき。\x01",
            "えートコ紹介してあげるさかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        "な、ほらほらこっち行こ！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x103,
        (
            "#0200F強引な客引きです……\x01",
            "営業法違反ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x103, 500)
    Sleep(500)

    #C0077
    ChrTalk(
        0xA,
        "なんやお子さん連れやったか。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "……ああ、もうええ、ええ。\x01",
            "今日のトコは見逃したるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "お嬢ちゃんもな、\x01",
            "この辺は子供の来る所やないから。\x01",
            "気ぃつけや？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        "#0201F（…………ムッ………）\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0000F（はは……\x01",
            "  子供扱いされるのは\x01",
            "  嫌なのかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 2)
    Return()

    # Function_10_1FF3 end

    def Function_11_21DB(): pass

    label("Function_11_21DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2269")

    #C0082
    ChrTalk(
        0xB,
        (
            "裏路地の方に\x01",
            "警察の人が出たり入ったりしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "警察の人、いいのかな～。\x01",
            "……けーさつだといいんだっけ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231C")

    label("loc_2269")


    #C0084
    ChrTalk(
        0xB,
        (
            "さっきからね、裏路地の方に\x01",
            "警察に人がはいってくの。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        (
            "あそこって……\x01",
            "近づいちゃダメなトコよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "警察の人、いいのかな～。\x01",
            "黒服の人たちに\x01",
            "叱られたりしちゃわない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_231C")

    Jump("loc_3289")

    label("loc_2321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23D1")

    #C0087
    ChrTalk(
        0xB,
        (
            "ライバルの子に勝つ\x01",
            "新しい客引きのセリフ考えてンの！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "う～ん、う～ん……\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "ンもう、バカン！\x01",
            "考えの邪魔しないでよう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247F")

    label("loc_23D1")


    #C0090
    ChrTalk(
        0xB,
        "ハァイ、アイリスですわよっ☆\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xB,
        (
            "お兄さんおヒマ～ン？\x01",
            "遊んだげるっ㈱\x02",
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
            "……うーん、なんだか違うかも～。\x01",
            "路線まちがえたってカンジね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_247F")

    Jump("loc_3289")

    label("loc_2484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_25C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2505")

    #C0093
    ChrTalk(
        0xB,
        (
            "はう、またライバルの子に\x01",
            "売り上げ負けちゃいそう～。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "うーんマズイわ～。\x01",
            "なンか手を考えないと～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C1")

    label("loc_2505")


    #C0095
    ChrTalk(
        0xB,
        (
            "なンかね、今日は\x01",
            "路地裏の方がコワイ感じなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        (
            "ちょっとのぞいたら\x01",
            "黒服の人にすんごい睨まれちゃった……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xB,
        (
            "うーん、どうなってンのかしら。\x01",
            "今日は客引き、やめた方がいいかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_25C1")

    Jump("loc_3289")

    label("loc_25C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2641")

    #C0098
    ChrTalk(
        0xB,
        (
            "予約でご指名なんて初めてだもん。\x01",
            "ちょー嬉しいかも～！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "よーし、予約の\x01",
            "時間まで頑張ろっと！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E1")

    label("loc_2641")


    #C0100
    ChrTalk(
        0xB,
        (
            "うふ、今日あたし\x01",
            "ご指名はいってンの。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        "いいでしょ！　うらやましい～？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "なンかね、議会やってる間は\x01",
            "接待のご予約が多いんだって。\x01",
            "ちょーラッキー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_26E1")

    Jump("loc_3289")

    label("loc_26E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2781")

    #C0103
    ChrTalk(
        0xB,
        (
            "記念祭は終わっちゃったけど、\x01",
            "なンかあたし、やる気マンマン～！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xB,
        (
            "うふふ、来月もオトナの魅力で\x01",
            "ライバルを蹴落としちゃおっと！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2823")

    label("loc_2781")


    #C0105
    ChrTalk(
        0xB,
        (
            "記念祭の間の売り上げね、\x01",
            "ライバルの子よりちょっと多かったの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    #C0106
    ChrTalk(
        0xB,
        "やった、あたしの勝ち～！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xB,
        "うれしー、勝ったの初めてだもん！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2823")

    Jump("loc_3289")

    label("loc_2828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_299A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28B5")

    #C0108
    ChrTalk(
        0xB,
        (
            "あのシスター、眉に\x01",
            "こーんなにしわが寄っていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "フン、早くしわしわのお婆ちゃんに\x01",
            "なっちゃえばいいんだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2995")

    label("loc_28B5")


    #C0110
    ChrTalk(
        0xB,
        (
            "最近肩凝りがひどいから、\x01",
            "教会に行ってお薬をお願いしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "でもホステスですって言ったら\x01",
            "シスターが渋い顔しちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        "こんこんとお説教を始めンの。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "んもう、なによムカツク～！\x01",
            "ホステスのどこが悪いのよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2995")

    Jump("loc_3289")

    label("loc_299A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A21")

    #C0114
    ChrTalk(
        0xB,
        (
            "酔った客ってタチが悪いのよね。\x01",
            "ちっとも解放してくれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "はあ、昨晩の売り上げは\x01",
            "ぱっとしないわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC3")

    label("loc_2A21")


    #C0116
    ChrTalk(
        0xB,
        (
            "ふぁ～ああ……\x01",
            "……眠い眠い……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "昨日はしつこい客に\x01",
            "捕まっちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        "ふう、ついてないわ～。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xB,
        (
            "またライバルの子に\x01",
            "差をつけられちゃったかも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AC3")

    Jump("loc_3289")

    label("loc_2AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2B4D")

    #C0120
    ChrTalk(
        0xB,
        (
            "うふっ、そろそろ\x01",
            "客が増えてくる時間よね！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        "こんにちは、アイリスで～すっ☆\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        "……よーし、今日も頑張ろっと！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3289")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2C6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BCA")

    #C0123
    ChrTalk(
        0xB,
        (
            "警察のひとがいると\x01",
            "お商売があがったりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        (
            "んもう、早くどこかに\x01",
            "行ってくんないかなぁ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C68")

    label("loc_2BCA")


    #C0125
    ChrTalk(
        0xB,
        (
            "さっき警察のひとが\x01",
            "キキコミしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "この前の、どこかのお店の\x01",
            "ボヤ騒ぎの件かなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "んもう、なんでもいいけど\x01",
            "お商売の邪魔しないでよねっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C68")

    Jump("loc_3289")

    label("loc_2C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2CD3")

    #C0128
    ChrTalk(
        0xB,
        "最近肩凝りがひどいのよね。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "教会に行ってお薬を\x01",
            "もらってこようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D71")

    label("loc_2CD3")


    #C0130
    ChrTalk(
        0xB,
        (
            "ライバルの子が\x01",
            "売り上げをあげてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xB,
        (
            "でもあたしって、仕事増やすと\x01",
            "肩凝りしちゃうのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xB,
        (
            "はあ、教会に行って\x01",
            "お薬でももらってこようかな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D71")

    Jump("loc_3289")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DDA")

    #C0133
    ChrTalk(
        0xB,
        (
            "あの人たちに\x01",
            "声掛けちゃいけないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        "ふう、今日は失敗しちゃったわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E73")

    label("loc_2DDA")


    #C0135
    ChrTalk(
        0xB,
        (
            "さっきうっかり\x01",
            "黒いサングラスの人に\x01",
            "声を掛けちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "……すんごい\x01",
            "怖い顔で睨まれちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "はうう、あの人たち\x01",
            "やっぱり怖いかも～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E73")

    Jump("loc_3289")

    label("loc_2E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2ED2")

    #C0138
    ChrTalk(
        0xB,
        (
            "でもあたし\x01",
            "頭使うの苦手なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        "ああん、どうしよう～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F3D")

    label("loc_2ED2")


    #C0140
    ChrTalk(
        0xB,
        (
            "このままじゃライバルの子に\x01",
            "売り上げで負けちゃうわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "ああん、なにか\x01",
            "いい方法を考えなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2F3D")

    Jump("loc_3289")

    label("loc_2F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_302F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F94")

    #C0142
    ChrTalk(
        0xB,
        (
            "こっちだって商売があるのよ。\x01",
            "んもう、頭にきちゃう～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302A")

    label("loc_2F94")


    #C0143
    ChrTalk(
        0xB,
        (
            "時々ね、夜中に\x01",
            "サングラスの人たちが\x01",
            "何だかバタバタしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "この前の夜なんて\x01",
            "まるで商売にならなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        "んもう、頭にきちゃう～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_302A")

    Jump("loc_3289")

    label("loc_302F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_30BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 3)), scpexpr(EXPR_END)), "loc_30B7")

    #C0146
    ChrTalk(
        0xB,
        (
            "あたしね、ライバルの子と\x01",
            "売り上げ競ってンの。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "でもね、でもね……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xB,
        "あ～ん、今月は負けちゃいそ～う！\x02",
    )

    CloseMessageWindow()
    Jump("loc_30BA")

    label("loc_30B7")

    Call(0, 12)

    label("loc_30BA")

    Jump("loc_3289")

    label("loc_30BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 3)), scpexpr(EXPR_END)), "loc_3286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3218")

    #C0149
    ChrTalk(
        0xFE,
        (
            "ランディさんの約束って\x01",
            "あんまりアテになんないのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "この前も来てくれるって言ったのに\x01",
            "すっぽかしちゃうし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0303Fああ、あの日は確か\x01",
            "バーで美人と知り合っちまってな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 0)

    #C0152
    ChrTalk(
        0xFE,
        (
            "んもう、ランディさんのばか～ん！\x01",
            "ウソツキ～！\x02",
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
    Jump("loc_3281")

    label("loc_3218")

    TurnDirection(0xFE, 0x104, 0)

    #C0153
    ChrTalk(
        0xFE,
        (
            "ランディさんのばか～ん！\x01",
            "ウソツキ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "お店に来てくんないと、\x01",
            "アイリス怒っちゃうモ～ン！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3281")

    Jump("loc_3289")

    label("loc_3286")

    Call(0, 12)

    label("loc_3289")

    TalkEnd(0xFE)
    Return()

    # Function_11_21DB end

    def Function_12_328D(): pass

    label("Function_12_328D")

    TurnDirection(0xFE, 0x104, 0)

    #C0155
    ChrTalk(
        0xFE,
        "あっ、ランディさん発見～！\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "最近遊びに来てくれなかったケド。\x01",
            "ぶ～、何してたのよぉ！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0300Fはは、悪ぃ。\x01",
            "転職の手続きやらで\x01",
            "ちょいと忙しくってな。\x02\x03",

            "アイリスちゃんの方は\x01",
            "最近どうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "ん～、いつも通りかも～。\x01",
            "頑張ってライバルの子と\x01",
            "競い合ってるトコ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "ランディさ～ん、また\x01",
            "お店に遊びに来てよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#0304Fしゃーねえなぁ、\x01",
            "んじゃあ今夜にでも……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0109Fランディさん、\x01",
            "子供の前でやめて#200Wく・だ・さ・る#20W？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0006F（ランディ、いつも\x01",
            "  こういう事をしてるのか……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 3)
    Return()

    # Function_12_328D end

    def Function_13_3489(): pass

    label("Function_13_3489")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    #C0163
    ChrTalk(
        0xFE,
        (
            "一課の人に言われてさ、市民が\x01",
            "入らないように見張ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "で、でもここって……\x01",
            "あのルバーチェ商会だよな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "や、やばいって……\x01",
            "ホントに大丈夫なのかな、オレ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0003Fすまんフランツ……\x01",
            "見張りは頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0300Fま、万が一連中が戻ってきたら\x01",
            "急いで逃げ出す事だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_360E")

    label("loc_35B9")


    #C0168
    ChrTalk(
        0xFE,
        (
            "ううっ、オレは\x01",
            "今年入ったばっかの新米なのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "ふ、不安でいっぱいだぜ……\x02",
    )

    CloseMessageWindow()

    label("loc_360E")

    TalkEnd(0xFE)
    Return()

    # Function_13_3489 end

    def Function_14_3612(): pass

    label("Function_14_3612")

    TurnDirection(0x11C, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3671")

    #C0170
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0005F（このルートじゃないみたいだ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_370C")

    label("loc_3671")


    #C0172
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x101,
        "#0005Fこ、こっちじゃないのか？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#0200Fこのルートでは\x01",
            "ないみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_370C")

    Return()

    # Function_14_3612 end

    def Function_15_370D(): pass

    label("Function_15_370D")

    EventBegin(0x1)
    Call(0, 14)
    Sleep(50)
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_15_370D end

    def Function_16_3729(): pass

    label("Function_16_3729")

    EventBegin(0x1)

    #C0175
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0003Fさすがにこの先には\x01",
            "行ってないか……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#0200Fギリギリ最低限の分別は\x01",
            "弁えていたようですね。\x02",
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

    # Function_16_3729 end

    def Function_17_37E3(): pass

    label("Function_17_37E3")

    EventBegin(0x1)

    #C0178
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0003F……こっちじゃないな。\x02\x03",

            "#0001Fアンティークショップから出てきて\x01",
            "飲み直すとすると……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5660, 790, 4890, 180)
    EventEnd(0x4)
    Return()

    # Function_17_37E3 end

    def Function_18_3879(): pass

    label("Function_18_3879")

    EventBegin(0x2)

    #C0180
    ChrTalk(
        0x11C,
        "#1200F……ウォンウォン！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0181
    ChrTalk(
        0x101,
        "#0005Fあれ、こっちじゃないのか……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        (
            "#0200F別のルートを\x01",
            "探してみましょう。\x02",
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

    # Function_18_3879 end

    def Function_19_3932(): pass

    label("Function_19_3932")

    TalkBegin(0xFF)

    #C0183
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "……ウォン！\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……この辺りを\x01",
            "通ったのは間違い無さそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        "#0200Fええ、この調子で進みましょう。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_19_3932 end

    def Function_20_39CA(): pass

    label("Function_20_39CA")

    TalkBegin(0xFF)

    #C0186
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#0003Fここは……違うみたいだな？\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#0200Fええ、特に匂いは\x01",
            "残っていないようです。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_20_39CA end

    def Function_21_3A54(): pass

    label("Function_21_3A54")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB4")

    #A0189
    AnonymousTalk(
        0x103,
        "#0205Fこの通りは……？\x02",
    )

    CloseMessageWindow()

    #A0190
    AnonymousTalk(
        0x104,
        (
            "#0303Fま、いわゆる裏通りだな。\x02\x03",

            "#0300F歓楽街の延長みたいなもんだが、\x01",
            "粋なバーからキャバレーまで\x01",
            "中々いい店が揃ってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #A0191
    AnonymousTalk(
        0x101,
        "#0000F……ランディ、妙に詳しいな？\x02",
    )

    CloseMessageWindow()

    #A0192
    AnonymousTalk(
        0x104,
        (
            "#0302Fああ、ロイドには言っただろ？\x02\x03",

            "#0309Fこの辺りに何軒か\x01",
            "色っぽい姉ちゃんたちのいる\x01",
            "店があってな……\x02",
        )
    )

    CloseMessageWindow()

    #A0193
    AnonymousTalk(
        0x102,
        "#0106F……それ以上言わなくていいわ。\x02",
    )

    CloseMessageWindow()

    #A0194
    AnonymousTalk(
        0x101,
        (
            "#0012F（はは……ランディは結構\x01",
            "  入り浸ってるみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3CB4")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "裏通りは、中央広場から続く裏路地です。\x02",
        )
    )

    CloseMessageWindow()

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ジャズバー《ガランテ》、\x01",
            "アンティークショップ《イメルダ》などの\x01",
            "店舗が存在します。\x02",
        )
    )

    CloseMessageWindow()

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "高価ですが便利なアイテムが入手できるため\x01",
            "折をみて訪ねてみると良いでしょう。\x02",
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

    # Function_21_3A54 end

    def Function_22_3DE5(): pass

    label("Function_22_3DE5")

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
        "#12P#0001F（ここが《ルバーチェ商会》……）\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#0101F（ずいぶん怪しい路地だとは\x01",
            "  思っていたけど……）\x02",
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

    def lambda_4086():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4086)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0200
    ChrTalk(
        0x9,
        "#5Pなんだ、お前ら？\x02",
    )

    CloseMessageWindow()

    def lambda_40B6():
        OP_95(0xFE, 700, 0, 37500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40B6)
    Sleep(150)

    def lambda_40D3():
        OP_95(0xFE, -700, 0, 37500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_40D3)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)

    #C0201
    ChrTalk(
        0x8,
        (
            "#5Pお前らみたいなガキどもが\x01",
            "近寄っていい場所じゃねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        "#5Pとっとと失せやが──\x02",
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
        "#5Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        "#5Pお、お前ら、あの時の！？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        "#12P#0205Fもしかして……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x104,
        (
            "#12P#0302Fハッ、どうやら\x01",
            "お知り合いだったみてぇだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    #C0207
    ChrTalk(
        0x9,
        (
            "#11Pなんだ？\x01",
            "こいつらがどうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        "#5P例の警察のガキどもだ！\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "#5P旧市街の仕込みを\x01",
            "邪魔してくれた……！\x02",
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
        "#5Pなんだと……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#12P#0003F……どうやら自己紹介を\x01",
            "する必要はなさそうですね。\x02\x03",

            "#0000F今日は捜査任務で\x01",
            "こちらに伺わせてもらいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        "#5Pなにィ……？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#0000Fこちらの会長さんに\x01",
            "取り次いでもらえませんか？\x02\x03",

            "とある事件に関して\x01",
            "話を聞かせてもらいたいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        "#5Pふ、ふざけるな……！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "#5P警察のガキが会長に話だと！？\x01",
            "よくもぬけぬけと……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        (
            "#0103F……容疑者というわけでなく\x01",
            "あくまで、参考人としてです。\x02\x03",

            "#0100Fもちろん強制ではないので\x01",
            "無理強いはしませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、取り次いでくれるくらいは\x01",
            "してもらってもいいんじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        "#5Pチッ……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "#5Pアルノーがしくじった件で\x01",
            "更に調子に乗らせたみてぇだな……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0220
    ChrTalk(
        0x9,
        "#11Pおいおい、どうする？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#11P勘違いしてるクソガキどもに\x01",
            "改めて礼儀でも教えてやるかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        "#5Pフン、そうだな……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x104,
        "#12P#0308F（……なんか駄目っぽいぜ？）\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#6P#0006F（……仕方ない。\x01",
            "  退散するしかないか……）\x02",
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
        "豪胆な声",
        "#4P──通してやれ。\x02",
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

    def lambda_4792():

        label("loc_4792")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_4792")

    QueueWorkItem2(0x8, 2, lambda_4792)

    def lambda_47A4():

        label("loc_47A4")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_47A4")

    QueueWorkItem2(0x9, 2, lambda_47A4)

    def lambda_47B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_47B6)

    def lambda_47C7():
        OP_95(0xFE, 0, 0, 37000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47C7)
    WaitChrThread(0xD, 2)
    Sleep(1500)

    def lambda_47E8():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x92E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47E8)
    Sleep(100)

    def lambda_4805():
        OP_96(0xFE, 0x514, 0x0, 0x92E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4805)

    #C0226
    ChrTalk(
        0x8,
        "#1Pわ、若頭……！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x9,
        "#2Pお、お疲れさまです！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x11)

    #N0228
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        "#5P#3104Fおう、ご苦労。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#6P#0013F（で、でかい……）\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x103,
        (
            "#0201F#6P#N（あのヴァルドさんも\x01",
            "  相当な大きさでしたけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0231
    ChrTalk(
        0x104,
        "#0301F#12P（こっちはそれ以上だな……）\x02",
    )

    CloseMessageWindow()

    #N0232
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        (
            "#5P#3100Fクク……\x01",
            "お前らが警察のガキどもか。\x02\x03",

            "話には聞いてたが\x01",
            "思った以上に若いじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#0003F……特務支援課の\x01",
            "ロイド・バニングスです。\x02\x03",

            "#0001Fあなたは……？\x02",
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
    SetChrName("スーツ姿の巨漢")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            "ガルシア・ロッシ。\x02\x03",

            "《ルバーチェ商会》の\x01",
            "営業本部長を務めている。\x02\x03",

            "ククク……まあ《若頭》と\x01",
            "呼ばれることの方が多いがなァ。\x02",
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
            "#0301F#12P（おいおい……\x01",
            "  いきなり大物くさいぜ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#6P#0101F（……ええ。\x01",
            "  恐らくナンバー２でしょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    #C0238
    ChrTalk(
        0xD,
        (
            "#5P#3103F──入れ。\x02\x03",

            "話は俺が聞いてやる。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BAA():
        OP_95(0xFE, 0, 200, 44500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4BAA)
    Sleep(2000)

    def lambda_4BC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4BC7)

    #C0239
    ChrTalk(
        0x101,
        "#6P#0005Fえ、あ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 2)
    WaitChrThread(0xD, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)

    def lambda_4C01():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4C01)
    Sleep(100)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0240
    ChrTalk(
        0x8,
        (
            "#5P……ハッ。\x01",
            "若頭がそう言うなら仕方ねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        "#5Pとっとと入りやがれ。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "#11P……くれぐれもあの人に\x01",
            "無礼を働こうと思うなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        "#11P長生きしたかったらな。\x02",
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

    # Function_22_3DE5 end

    def Function_23_4CF2(): pass

    label("Function_23_4CF2")

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

    def lambda_4E55():

        label("loc_4E55")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4E55")

    QueueWorkItem2(0x8, 2, lambda_4E55)

    def lambda_4E67():

        label("loc_4E67")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4E67")

    QueueWorkItem2(0x9, 2, lambda_4E67)

    def lambda_4E79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E79)

    def lambda_4E8A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E8A)
    Sleep(600)

    def lambda_4EA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4EA7)

    def lambda_4EB8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4EB8)
    Sleep(400)

    def lambda_4ED5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4ED5)

    def lambda_4EE6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4EE6)
    Sleep(600)

    def lambda_4F03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4F03)

    def lambda_4F14():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F14)
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
        "#6P#0008F……参ったな。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        "#6P#0206F完全に子供扱いでしたね……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x104,
        "#0301Fフン……気に喰わねぇな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        (
            "#6P#0005Fそういえば、ランディ。\x02\x03",

            "何か呼び止められてたけど\x01",
            "どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0248
    ChrTalk(
        0x104,
        (
            "#11P#0306F……さあな。\x02\x03",

            "#0301Fただまあ、あの大男、\x01",
            "ただのハッタリだけじゃねえぞ。\x02\x03",

            "まともにやり合ったら\x01",
            "今の俺たちじゃ歯が立たねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#6P#0001Fそうか……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0250
    ChrTalk(
        0x103,
        (
            "#12P#0203Fそれ以前に、まともに相手に\x01",
            "されていない感じでしたけど……\x02\x03",

            "#0201Fこちらが何をしたところで\x01",
            "痛くも痒くもないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……それは俺も感じたよ。\x02\x03",

            "#0001F議員との繋がりがあるとはいえ、\x01",
            "あの余裕は何なんだ……？\x02",
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

    def lambda_5348():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5348)
    Sleep(100)
    TurnDirection(0x104, 0x102, 500)

    #C0253
    ChrTalk(
        0x101,
        "#6P#0005Fエリィ……？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        "#2P#0305Fなんだ、どうした？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0255
    ChrTalk(
        0x102,
        (
            "#0103F#5Pあ、うん……何でもないわ。\x02\x03",

            "#0101Fそれより、これからどうするの？\x02\x03",

            "どうやらルバーチェには\x01",
            "何か心当たりがあるみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#6P#0005Fああ、脅迫状の一件か。\x02\x03",

            "#0003Fうーん、あの若頭の言葉を\x01",
            "鵜呑みにするわけじゃないけど……\x02\x03",

            "#0001F俺は、この件にルバーチェが\x01",
            "関係している可能性は低いと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_550C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_550C)
    Sleep(50)

    def lambda_551C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_551C)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0257
    ChrTalk(
        0x102,
        "#0105F#5Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x103,
        (
            "#12P#0205Fでも……脅迫状を見て\x01",
            "明らかに反応してましたよね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0259
    ChrTalk(
        0x101,
        (
            "#6P#0004Fああ、間違いなく\x01",
            "何かに気付いたんだと思う。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは脅迫状を取り出した。\x02",
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
            "新作ノ公演ヲ中止セヨ。\x01",
            "サモナクバ炎ノ舞姫ニ\x01",
            "悲劇ガ訪レルダロウ──《銀》\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0262
    AnonymousTalk(
        0x101,
        "#0000F恐らく、気付いたのは──\x02",
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
            "#1Kガルシアが気付いた何かとは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【脅迫文の筆跡】\x01",      # 0
            "【差出人の名前】\x01",      # 1
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
        (0, "loc_5778"),
        (1, "loc_58DB"),
        (SWITCH_DEFAULT, "loc_591F"),
    )


    label("loc_5778")


    #A0264
    AnonymousTalk(
        0x101,
        (
            "#0001F脅迫文の筆跡……\x01",
            "これに反応した可能性は\x01",
            "ゼロじゃないかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0265
    AnonymousTalk(
        0x103,
        (
            "#0203F確かに筆跡というのは\x01",
            "書く人によって\x01",
            "かなり違うそうですが……\x02\x03",

            "#0200Fあの若頭が声を上げたのは\x01",
            "最後の方になってからでは？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0266
    AnonymousTalk(
        0x101,
        (
            "#0006Fあ……そうか。\x01",
            "うーん、だとすると……\x02\x03",

            "#0008F手紙の最後にあったのは\x01",
            "差出人の名前……\x02\x03",

            "#0001Fこれに反応したかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_591F")

    label("loc_58DB")

    OP_2C(0x42, 0x2)

    #A0267
    AnonymousTalk(
        0x101,
        (
            "#0001F差出人の名前……\x01",
            "これに反応したんだと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_591F")

    label("loc_591F")


    #A0268
    AnonymousTalk(
        0x104,
        "#0301F《銀》……結局はこいつか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0269
    AnonymousTalk(
        0x102,
        (
            "#0101Fこの人物が、\x01",
            "ルバーチェの関係者という\x01",
            "可能性は無いのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0270
    AnonymousTalk(
        0x101,
        (
            "#0003Fいや、関係があるとしたら\x01",
            "あの若頭の態度はおかしい。\x02\x03",

            "#0001Fまるで関係が無いことを\x01",
            "最初から確信しているような……\x02\x03",

            "そんな感じじゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0271
    AnonymousTalk(
        0x102,
        "#0105Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0272
    AnonymousTalk(
        0x104,
        (
            "#0300Fなるほど……\x01",
            "確かにそんな素振りだったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0273
    AnonymousTalk(
        0x103,
        (
            "#0203Fルバーチェと無関係でありながら\x01",
            "彼らが強く意識している存在……\x02\x03",

            "#0201Fそういう人物という事ですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0274
    AnonymousTalk(
        0x101,
        "#0004Fああ、そうだと思う。\x02",
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
            "#0103F#5P……だとすると……\x02\x03",

            "#0101Fルバーチェの情報に詳しい人に\x01",
            "相談してみた方がよさそうね。\x02\x03",

            "法律事務所のイアン先生とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、そうだな。\x02\x03",

            "#0006F本当だったらグレイスさんにも\x01",
            "相談してみたいところだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#11P#0306Fま、あの姉さんに話したら\x01",
            "脅迫状のことまで\x01",
            "強引に聞き出してくるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x103,
        (
            "#12P#0200F……アルカンシェルにとっては\x01",
            "格好のスキャンダルになりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ、だから正直、\x01",
            "アテにしない方がいいだろう。\x02\x03",

            "#0000Fあとは……他にも心当たりが\x01",
            "あるなら当たってみよう。\x02\x03",

            "もしかしたら思いがけない\x01",
            "情報が入ってくるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#0104F#5Pええ、そうね……\x02\x03",

            "#0102F……ふふっ………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    #C0281
    ChrTalk(
        0x101,
        "#6P#0005Fど、どうした？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        (
            "#0104F#5Pううん、何でもない。\x02\x03",

            "#0100Fそれでは早速、\x01",
            "聞き込みを始めましょう。\x02\x03",

            "どこを回るにせよ、\x01",
            "法律事務所には行かないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        "#6P#0000Fああ、そうだな。\x02",
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

    # Function_23_4CF2 end

    def Function_24_5F76(): pass

    label("Function_24_5F76")


    def lambda_5F7B():
        OP_95(0xFE, 0, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F7B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_24_5F76 end

    def Function_25_5F9C(): pass

    label("Function_25_5F9C")

    Sleep(700)

    def lambda_5FA4():
        OP_95(0xFE, 0, 0, 4700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FA4)
    WaitChrThread(0x102, 1)

    def lambda_5FC2():
        OP_95(0xFE, -1000, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FC2)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_25_5F9C end

    def Function_26_5FE3(): pass

    label("Function_26_5FE3")

    Sleep(1300)

    def lambda_5FEB():
        OP_95(0xFE, 0, 0, 4700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FEB)
    WaitChrThread(0x103, 1)

    def lambda_6009():
        OP_95(0xFE, 1000, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6009)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_26_5FE3 end

    def Function_27_602A(): pass

    label("Function_27_602A")

    Sleep(2500)

    def lambda_6032():
        OP_95(0xFE, 0, 0, 3100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6032)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_27_602A end

    def Function_28_6053(): pass

    label("Function_28_6053")

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

    def lambda_62A3():
        OP_96(0xFE, 0x73A, 0x0, 0xAF0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62A3)
    Sleep(300)

    def lambda_62C0():
        OP_96(0xFE, 0x5AA, 0x0, 0x898, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62C0)
    Sleep(400)

    def lambda_62DD():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xE10, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62DD)
    Sleep(300)

    def lambda_62FA():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xAF0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62FA)
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
            "#6P#0101Fやっぱり普段より\x01",
            "見張りが多いみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#0301F#6Pしかも、想像以上に\x01",
            "殺気立ってる感じだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        (
            "#6P#0206F焦りと興奮、警戒と不安……\x02\x03",

            "#0201Fそんな感情が\x01",
            "ごちゃ混ぜに伝わってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#6P#0001F間違いなく《黒月》の\x01",
            "報復を警戒してるんだろう……\x02\x03",

            "#0006F……しかし参ったな。\x02\x03",

            "あの様子じゃ、ガルシアの動向を\x01",
            "確かめるなんてとても──\x02",
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
        "豪胆な声",
        "#4P──俺が何だって？\x02",
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

    def lambda_65C6():
        OP_95(0xFE, -3000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_65C6)
    Sleep(700)

    def lambda_65E3():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65E3)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0289
    ChrTalk(
        0x101,
        "#12P#0005Fガルシア・ロッシ……！\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x104,
        (
            "#0301Fチッ、デカイくせに\x01",
            "気配を消しやがって……\x02",
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
            "フン、てめぇらか。\x02\x03",

            "あんな事があったってのに\x01",
            "よくもノコノコとこの場所に\x01",
            "ツラを出せたもんだなァ？\x02",
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
            "#12P#0013Fくっ……\x02\x03",

            "#0003F……言い訳はしません。\x02\x03",

            "#0001Fあなた達との手打ちについては\x01",
            "キーアに関する事だけですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "#3104F#5Pクク、分かってんじゃねえか。\x02\x03",

            "#3102F手打ちの件を盾に、\x01",
            "勘違いして乗り込んできたら\x01",
            "叩きのめしてやる所だったぜ。\x02",
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
        "#0306Fフン、物騒なオッサンだな。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xD,
        (
            "#3103F#5P……てめえらがコソコソと\x01",
            "嗅ぎ回っている理由は判ってる。\x02\x03",

            "だが、その件について\x01",
            "俺から話すことは一切ない。\x02\x03",

            "#3101Fとっとと消えうせろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        "#12P#0013Fくっ……\x02",
    )

    CloseMessageWindow()

    def lambda_6924():

        label("loc_6924")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_6924")

    QueueWorkItem2(0x101, 2, lambda_6924)

    def lambda_6936():

        label("loc_6936")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_6936")

    QueueWorkItem2(0x102, 2, lambda_6936)

    def lambda_6948():

        label("loc_6948")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_6948")

    QueueWorkItem2(0x103, 2, lambda_6948)

    def lambda_695A():

        label("loc_695A")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_695A")

    QueueWorkItem2(0x104, 2, lambda_695A)

    def lambda_696C():
        OP_95(0xFE, 200, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_696C)
    Sleep(400)

    def lambda_6989():
        OP_96(0xFE, 0x44C, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6989)
    WaitChrThread(0xD, 1)

    def lambda_69A7():
        OP_95(0xFE, 200, 0, 6800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_69A7)
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

    def lambda_6A61():
        OP_96(0xFE, 0x0, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6A61)
    OP_0D()

    def lambda_6A7C():
        OP_96(0xFE, 0x0, 0x0, 0xE10, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A7C)
    WaitChrThread(0x101, 1)

    #C0298
    ChrTalk(
        0x101,
        (
            "#6P#0003F──１つだけ、教えてください。\x02\x03",

            "#0001Fもし、あなたが武装した\x01",
            "敵の本拠地を攻略するとしたら……\x02\x03",

            "正面から力任せで行きますか？\x02",
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
            "#5P#3104Fハッ、まともな猟兵団なら\x01",
            "そんな作戦は絶対に立てねぇな。\x02\x03",

            "可能な限り有利な状況に持ち込んで\x01",
            "最低限の被害で最大の戦果を狙う。\x02\x03",

            "#3100Fそうだろう……《闘神の息子》？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        (
            "#6P#0303Fその名で俺を呼ぶんじゃねえ。\x02\x03",

            "#0301F……だがまあ確かに\x01",
            "それが猟兵の流儀ってヤツだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそうか……\x02\x03",

            "#0004F──ありがとう。\x01",
            "答えてくれて感謝します。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "#5P#3100Fクク……おかしなガキだぜ。\x02\x03",

            "#3103Fただまあ、ここから先は\x01",
            "不用意に立ち入らねぇことだ。\x02\x03",

            "#3101Fマジで死ぬぞ、お前ら。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D1D():
        OP_96(0xFE, 0x0, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6D1D)
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
            "#0006F#5P何だか、少し様子が変だったな。\x02\x03",

            "#0001F張り詰めているようで、\x01",
            "どこか力が抜けてるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#0106F#11P……そうね。\x02\x03",

            "#0108F言ってる事は物騒だったけど\x01",
            "殺気は感じなかったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#0206F#11P少し疲れているような、\x01",
            "そんな感じもしました……\x02\x03",

            "#0201F一体、何があったんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#0308F#5Pチッ……\x01",
            "らしくねえツラしやがって。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    #N0307
    NpcTalk(
        0xE,
        "女性の声",
        (
            "#1Pうふふん。\x01",
            "その理由、知りたい～？\x02",
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

    def lambda_7029():

        label("loc_7029")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_7029")

    QueueWorkItem2(0x101, 2, lambda_7029)

    def lambda_703B():

        label("loc_703B")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_703B")

    QueueWorkItem2(0x102, 2, lambda_703B)

    def lambda_704D():

        label("loc_704D")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_704D")

    QueueWorkItem2(0x103, 2, lambda_704D)

    def lambda_705F():

        label("loc_705F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_705F")

    QueueWorkItem2(0x104, 2, lambda_705F)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x4)

    def lambda_707B():
        OP_96(0xFE, 0x0, 0x0, 0x2BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_707B)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x0, 0x1F4)
    OP_6F(0x1)

    #C0308
    ChrTalk(
        0x101,
        "#0005F#11Pグ、グレイスさん……！？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#5P#0306Fアンタもいい加減、\x01",
            "神出鬼没な姉さんだな……\x02",
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
            "フッ、それが記者魂ってモンよ。\x02\x03",

            "それじゃ、例によって例のごとく、\x01",
            "ギブ・アンド・テイクといきましょ♪\x02\x03",

            "そこのジャズバーで待ってるから㈱\x02",
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

    def lambda_7208():
        OP_95(0xFE, -10300, 0, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7208)
    WaitChrThread(0xE, 1)

    def lambda_7226():
        OP_95(0xFE, -10300, 1500, 5400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7226)
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

    def lambda_7272():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7272)
    Sleep(500)

    def lambda_728F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_728F)
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
        "#12P#0106F……どうするの？\x02",
    )

    CloseMessageWindow()

    def lambda_7357():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7357)
    Sleep(50)
    OP_93(0x104, 0x5A, 0x1F4)

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0006Fまあ、聞くだけ聞いてみよう。\x02\x03",

            "#0001F喋り過ぎないように\x01",
            "注意する必要はありそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#12P#0211Fですね……\x02",
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

    # Function_28_6053 end

    def Function_29_74C2(): pass

    label("Function_29_74C2")

    OP_93(0x8, 0xCD, 0x1F4)

    def lambda_74CE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74CE)
    WaitChrThread(0x8, 1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_93(0x8, 0x19, 0x1F4)

    def lambda_7513():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7513)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    Return()

    # Function_29_74C2 end

    def Function_30_752F(): pass

    label("Function_30_752F")

    Sleep(1500)

    label("loc_7532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_755D")
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)
    OP_64(0x9)
    Sleep(2500)
    Jump("loc_7532")

    label("loc_755D")

    Return()

    # Function_30_752F end

    def Function_31_755E(): pass

    label("Function_31_755E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7589")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)
    OP_64(0x10)
    Sleep(2500)
    Jump("Function_31_755E")

    label("loc_7589")

    Return()

    # Function_31_755E end

    def Function_32_758A(): pass

    label("Function_32_758A")

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
        "#0101F#6P見張りが一人もいないわ……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x104,
        (
            "#12P#0306Fああ、昨日見た時は\x01",
            "普段より多かったくらいだが……\x02\x03",

            "#0301Fしかし争ったような形跡はねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#0008F#6Pああ、もしかして《黒月》の報復が\x01",
            "あったのかと思ったけど……\x02",
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

    def lambda_7756():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7756)
    Sleep(50)

    def lambda_7766():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7766)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0317
    ChrTalk(
        0x101,
        "#11P#0005Fティオ……？\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x102,
        "#0105F#11Pどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x103,
        (
            "#6P#0203F……静かすぎます。\x02\x03",

            "#0201F建物の中から人の気配が\x01",
            "感じられないくらいに……\x02",
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
        "#11P#0011Fえ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0321
    ChrTalk(
        0x103,
        (
            "#6P#0206F正確には一人、\x01",
            "中にいるようですが……\x02\x03",

            "#0208Fそれ以外は全然、\x01",
            "感じられないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x104,
        (
            "#11P#0301Fおいおい……\x01",
            "どうなってやがるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0323
    ChrTalk(
        0x101,
        (
            "#0003F#6P中にいる一人というのは\x01",
            "ダドリーさんの可能性が高いな。\x02\x03",

            "#0013Fよし……\x01",
            "念のため中を確かめてみるか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7991():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7991)
    Sleep(50)

    def lambda_79A1():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79A1)
    Sleep(50)

    def lambda_79B1():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_79B1)
    WaitChrThread(0x102, 2)

    #C0324
    ChrTalk(
        0x102,
        "#0101F#6Pええ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_EE(0x0, 0xA)
    SetScenarioFlags(0xC4, 0)
    EventEnd(0x5)
    Return()

    # Function_32_758A end

    def Function_33_79F4(): pass

    label("Function_33_79F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A10")
    Call(0, 35)
    Return()

    label("loc_7A10")

    Jump("loc_7A31")

    label("loc_7A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A31")
    Call(0, 34)
    Return()

    label("loc_7A31")

    EventBegin(0x1)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x0, -500, 0, 34000, 0)
    SetChrPos(0x1, 500, 0, 33750, 0)
    SetChrPos(0x2, -500, 0, 32500, 0)
    SetChrPos(0x3, 500, 0, 32250, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AC4")
    SetChrPos(0x4, -500, 0, 31000, 0)

    label("loc_7AC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AE3")
    SetChrPos(0x5, 500, 0, 30750, 0)

    label("loc_7AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B5A")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_END)), "loc_7B4D")

    #N0325
    NpcTalk(
        0x8,
        "黒服",
        (
            "ガキども……\x01",
            "入ってくるんじゃねえ。\x02",
        )
    )

    CloseMessageWindow()

    #N0326
    NpcTalk(
        0x9,
        "黒服",
        "とっとと失せろや。\x02",
    )

    CloseMessageWindow()

    label("loc_7B4D")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_81BF")

    label("loc_7B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BE6")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_END)), "loc_7BD9")

    #C0327
    ChrTalk(
        0x8,
        (
            "警察のガキども……\x01",
            "この先に何か用事かよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x9,
        (
            "クク、とっとと失せな。\x01",
            "この先は私有地だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BD9")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_81BF")

    label("loc_7BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E65")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0B")

    #C0329
    ChrTalk(
        0x8,
        "ん？　何だガキども。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "とっとと消えな。\x01",
            "この先は私有地だぜ。\x02",
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
            "うっ……待てよ。\x01",
            "その顔、テメエらは……\x02",
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
        "チッ、そうか例の…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6D")

    #C0333
    ChrTalk(
        0x101,
        (
            "#0001F（……どうやらマフィアに\x01",
            "　関係する建物みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#0101F（行きましょう……\x01",
            "  騒ぎを起こしてもマズイわ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E03")

    label("loc_7D6D")


    #C0335
    ChrTalk(
        0x101,
        (
            "#0001F（今日もいるのか……）\x02\x03",

            "（……どうやらマフィアに\x01",
            "　関係する建物みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#0101F（行きましょう……\x01",
            "　騒ぎを起こしてもマズイわ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E03")

    SetScenarioFlags(0x88, 0)
    Jump("loc_7E58")

    label("loc_7E0B")


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
            "フン……怪我したくなかったら\x01",
            "とっとと消えな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E58")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_81BF")

    label("loc_7E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8043")
    OP_68(250, 2950, 35310, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EE6")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_7EE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EFF")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_7EFF")

    OP_68(250, 1950, 35310, 3000)
    Sleep(3200)

    #A0339
    AnonymousTalk(
        0x101,
        "#0001F（今日は物々しいな……）\x02",
    )

    CloseMessageWindow()

    #A0340
    AnonymousTalk(
        0x104,
        (
            "#0301F（ああ、しかも想像以上に\x01",
            "  殺気立ってる感じだぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #A0341
    AnonymousTalk(
        0x102,
        (
            "#0101F（黒月に仕掛けてしまった\x01",
            "  直後だものね。）\x02\x03",

            "（……その割に\x01",
            "  余裕がない気もするけど……）\x02",
        )
    )

    CloseMessageWindow()

    #A0342
    AnonymousTalk(
        0x103,
        (
            "#0200F（……この辺り一帯が\x01",
            "  ピリピリして痛い感じです。\x01",
            "  近づかない方がいいかと。）\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x2, 0x0, 0x25)
    SetScenarioFlags(0xC8, 7)
    Jump("loc_81BF")

    label("loc_8043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81BF")
    OP_68(250, 2950, 35310, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80C4")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_80C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80DD")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_80DD")

    OP_68(250, 1950, 35310, 3000)
    Sleep(3200)

    #A0343
    AnonymousTalk(
        0x101,
        (
            "#0005Fあれ？\x01",
            "見張りがいないな……\x02",
        )
    )

    CloseMessageWindow()

    #A0344
    AnonymousTalk(
        0x103,
        "#0200Fですね……\x02",
    )

    CloseMessageWindow()

    #A0345
    AnonymousTalk(
        0x104,
        (
            "#0301F奥に引っ込んでるのか？\x02\x03",

            "……なんにせよ\x01",
            "近づかない方が良さそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #A0346
    AnonymousTalk(
        0x102,
        (
            "#0101Fそうね、有用な情報が\x01",
            "得られることも無いでしょうし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 0)

    label("loc_81BF")

    OP_68(90, 1950, 4620, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 90, 0, 4620, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8211")
    Jump("loc_822C")

    label("loc_8211")

    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)

    label("loc_822C")

    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8271")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8271")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_828A")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_828A")

    EventEnd(0x4)
    Return()

    # Function_33_79F4 end

    def Function_34_828D(): pass

    label("Function_34_828D")

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

    def lambda_8322():
        OP_98(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8322)
    Sleep(50)

    def lambda_833F():
        OP_98(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_833F)
    Sleep(50)

    def lambda_835C():
        OP_98(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_835C)
    Sleep(50)

    def lambda_8379():
        OP_98(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8379)
    OP_68(0, 1950, 37000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0347
    NpcTalk(
        0x8,
        "黒服",
        "……おい、ガキども。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #N0348
    NpcTalk(
        0x8,
        "黒服",
        "この先に何か用事か？\x02",
    )

    CloseMessageWindow()

    #N0349
    NpcTalk(
        0x9,
        "黒服",
        (
            "ここから先は私有地だ。\x01",
            "入ってくるんじゃねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x101,
        "#0005F（……何者だ……？）\x02",
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
        "#0301F随分と柄の悪い連中だな。\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#0003Fああ、ヤクザ者だと思う。\x02\x03",

            "#0001F機会があれば調べたい所だけど……\x01",
            "下手に刺激しない方が良さそうだ。\x02",
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

    # Function_34_828D end

    def Function_35_85C1(): pass

    label("Function_35_85C1")

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

    def lambda_8656():
        OP_98(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8656)
    Sleep(50)

    def lambda_8673():
        OP_98(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8673)
    Sleep(50)

    def lambda_8690():
        OP_98(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8690)
    Sleep(50)

    def lambda_86AD():
        OP_98(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_86AD)
    OP_68(0, 1950, 37000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x8,
        "……おい、ガキども。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0354
    ChrTalk(
        0x8,
        "この先に何か用事か？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0355
    ChrTalk(
        0x8,
        "ん？　警察のバッジ……？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "もしかしてこいつらが\x01",
            "ファビオたちがしくじった……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        "おいおい、マジかよ！？\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        "まだガキどもじゃねえか！？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#0001F（……どうやらマフィアに\x01",
            "  関係する建物みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#0101F（行きましょう……\x01",
            "  騒ぎを起こしてもマズイわ。）\x02",
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

    # Function_35_85C1 end

    def Function_36_88D4(): pass

    label("Function_36_88D4")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    def lambda_88E3():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_88E3)
    Sleep(50)

    def lambda_88F3():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_88F3)
    WaitChrThread(0x8, 1)

    #C0361
    ChrTalk(
        0x8,
        (
            "おい、ウロチョロ\x01",
            "してんじゃねえぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x9,
        "とっとと失せな、ガキども。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrPos(0x0, -100, 0, 41020, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_36_88D4 end

    def Function_37_8974(): pass

    label("Function_37_8974")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B6B")

    #C0363
    ChrTalk(
        0x101,
        "#0001F待ってくれ、この先は……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A1E")

    #C0364
    ChrTalk(
        0x102,
        (
            "#0101Fルバーチェ商会……\x02\x03",

            "手打ちになったとはいえ、\x01",
            "顔を出すわけには行かないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AEF")

    label("loc_8A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A8A")

    #C0365
    ChrTalk(
        0x103,
        (
            "#0203Fルバーチェ商会……\x02\x03",

            "手打ちになったとはいえ、\x01",
            "顔を出すわけには行きませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AEF")

    label("loc_8A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AEF")

    #C0366
    ChrTalk(
        0x104,
        (
            "#0301Fルバーチェ商会……\x02\x03",

            "手打ちになったとはいえ、\x01",
            "顔を出すわけには行かねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AEF")


    #C0367
    ChrTalk(
        0x153,
        (
            "#1111F？？？\x01",
            "どうかしたのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        (
            "#0000Fああ、なんでもないよ。\x02\x03",

            "#0003F（……行こう。\x01",
            "  さすがに危険すぎる。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 1)
    Jump("loc_8BD4")

    label("loc_8B6B")


    #C0369
    ChrTalk(
        0x101,
        (
            "#0001F（この先はルバーチェ商会だ。）\x02\x03",

            "（……手打ちになったとはいえ\x01",
            "  乗り込むわけにはいかないな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D41")

    #C0370
    ChrTalk(
        0x104,
        (
            "#0301Fルバーチェ商会……\x01",
            "あれ以来も健在みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#0103Fキーアちゃんの一件でしばらく\x01",
            "大人しくしていたようだけれど……\x02\x03",

            "#0101F手打ちになった後は\x01",
            "通常の“営業”を再開したようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#0001F色々あったからな……\x01",
            "刺激するのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D39")

    #C0373
    ChrTalk(
        0x109,
        (
            "#0501F（噂には聞いてたけど……\x01",
            "  ロイドさんたちも大変そうね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D39")

    SetScenarioFlags(0xC9, 2)
    Jump("loc_8DA4")

    label("loc_8D41")


    #C0374
    ChrTalk(
        0x101,
        (
            "#0001F（この先はルバーチェ商会だ。）\x02\x03",

            "（下手に刺激は出来ないし\x01",
            "  立ち寄るのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DFB")

    #C0375
    ChrTalk(
        0x101,
        (
            "#0001F（予想以上に物々しいな……\x01",
            "  立ち寄るのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E6C")

    #C0376
    ChrTalk(
        0x101,
        (
            "#0001F（若頭のガルシアか。\x01",
            "  少し態度が妙だったけど……）\x02\x03",

            "（今はグレイスさんの話を聞こう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FDD")
    TurnDirection(0x13D, 0x0, 500)

    #C0377
    ChrTalk(
        0x13D,
        (
            "#2105Fあら、君たち\x01",
            "ルバーチェに乗り込むわけ？\x02\x03",

            "#2103F流石に無謀だと思うけど……\x02\x03",

            "#2109Fううん、でも君たちが\x01",
            "やるっていうなら止めないわ㈱\x01",
            "全力で密着取材してあげる……！\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x101,
        (
            "#0006Fいや……今はやめておきます。\x01",
            "（少なくともグレイスさんの\x01",
            "  前ではやりたくない……）\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x102,
        (
            "#0101Fガンツさんの方が心配だわ……\x01",
            "カジノへ急ぎましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9020")

    label("loc_8FDD")


    #C0380
    ChrTalk(
        0x101,
        (
            "#0003F（今はガンツさんの方が優先だ。\x01",
            "  ……カジノへ急ごう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_908A")

    #C0381
    ChrTalk(
        0x101,
        (
            "#0001F（今日はルバーチェも\x01",
            "  気が立っているみたいだ……\x01",
            "  立ち寄るのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9101")

    #C0382
    ChrTalk(
        0x101,
        (
            "#0001F（見張りはいないみたいだけど\x01",
            "  下手に刺激は出来ないな……）\x02\x03",

            "（近づくのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9101")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Return()

    # Function_37_8974 end

    def Function_38_9115(): pass

    label("Function_38_9115")

    EventBegin(0x1)

    #C0383
    ChrTalk(
        0x101,
        (
            "#0001Fビクセン町長の話が気になる……\x01",
            "今はカジノへ急ごう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_38_9115 end

    SaveToFile()

Try(main)
