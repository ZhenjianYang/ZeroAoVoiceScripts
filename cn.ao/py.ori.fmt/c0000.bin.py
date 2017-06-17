from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0000.bin",                # FileName
        "c0000",                    # MapName
        "c0000",                    # Location
        0x0002,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0000", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0000",                  # 0
        "利德",                   # 1
        "比利",                   # 2
        "克拉莉丝",               # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "男孩",                   # 10
        "女孩",                   # 11
        "警官",                   # 12
        "国防军士兵",             # 13
        "玛西",                   # 14
        "塞比娅",                 # 15
        "乌娜",                   # 16
        "车辆",                   # 17
        "国防军士兵",             # 18
        "国防军士兵",             # 19
        "警官",                   # 20
        "警官",                   # 21
        "警官",                   # 22
        "警官",                   # 23
        "警官",                   # 24
        "警官",                   # 25
        "列车",                   # 26
        "SE控制",                 # 27
        "中央广场",               # 28
        "西街",                   # 29
        "行政区",                 # 30
        "住宅街",                 # 31
        "欢乐街",                 # 32
        "东街",                   # 33
        "旧城区",                 # 34
        "港湾区",                 # 35
        "ＩＢＣ",                 # 36
        "站前街道",               # 37
        "后巷",                   # 38
        "乌尔斯拉间道",           # 39
        "东克洛斯贝尔街道",       # 40
        "西克洛斯贝尔街道",       # 41
        "玛因兹山道",             # 42
        "兰花塔",                 # 43
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch21600.itc",                   # 02
        "chr/ch23300.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch44000.itc",                   # 05
        "chr/ch44100.itc",                   # 06
        "chr/ch34300.itc",                   # 07
        "chr/ch34200.itc",                   # 08
        "chr/ch24700.itc",                   # 09
        "chr/ch10400.itc",                   # 0A
        "chr/ch48900.itc",                   # 0B
        "chr/ch30000.itc",                   # 0C
        "chr/ch21800.itc",                   # 0D
        "chr/ch33200.itc",                   # 0E
        "chr/ch22300.itc",                   # 0F
        "chr/ch41500.itc",                   # 10
    ))

    DeclNpc(-1830,   0,       13000,   180,  261,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(1490,    0,       -10739,  180,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3660,    29,      -56599,  90,   389,  0x0, 0,   10,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5880,    0,       2930,    35,   389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5880,    0,       2930,    35,   389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(5880,    0,       2930,    35,   389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6880,    0,       2930,    35,   389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(6880,    0,       2930,    35,   389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4000,    0,       -7000,   270,  389,  0x0, 0,   12,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6070,    0,       319,     270,  389,  0x0, 0,   16,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(5150,    0,       -1220,   90,   389,  0x0, 0,   13,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4010,    0,       -500,    90,   389,  0x0, 0,   14,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(3809,    0,       -1500,   90,   389,  0x0, 0,   15,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 35,  8.5,                   -2.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.25,                 0.5,                   0.10000000149011612,   1.0])

    DeclActor(9500,    360,     -2000,   2000,    10000,   1360,    -2000,   0x007C, 0,  32, 0x0000)
    DeclActor(-22300,  -5000,   20700,   2000,    -21950,  -4000,   21360,   0x007C, 0,  37, 0x0000)

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "中央广场")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "西街")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "行政区")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "东街")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "旧城区")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "港湾区")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "站前街道")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "后巷")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(11.0, 0.0, 286.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ChipFrameInfo(2132, 0)                                       # 0

    ScpFunction((
        "Function_0_854",          # 00, 0
        "Function_1_904",          # 01, 1
        "Function_2_957",          # 02, 2
        "Function_3_990",          # 03, 3
        "Function_4_ED7",          # 04, 4
        "Function_5_138B",         # 05, 5
        "Function_6_227D",         # 06, 6
        "Function_7_28DC",         # 07, 7
        "Function_8_2A7F",         # 08, 8
        "Function_9_2C32",         # 09, 9
        "Function_10_2D86",        # 0A, 10
        "Function_11_2F2F",        # 0B, 11
        "Function_12_3070",        # 0C, 12
        "Function_13_31A2",        # 0D, 13
        "Function_14_326D",        # 0E, 14
        "Function_15_33B9",        # 0F, 15
        "Function_16_34B5",        # 10, 16
        "Function_17_3630",        # 11, 17
        "Function_18_36C7",        # 12, 18
        "Function_19_3703",        # 13, 19
        "Function_20_3741",        # 14, 20
        "Function_21_37B9",        # 15, 21
        "Function_22_3B0D",        # 16, 22
        "Function_23_3B72",        # 17, 23
        "Function_24_3BB3",        # 18, 24
        "Function_25_4018",        # 19, 25
        "Function_26_4661",        # 1A, 26
        "Function_27_4673",        # 1B, 27
        "Function_28_4688",        # 1C, 28
        "Function_29_469D",        # 1D, 29
        "Function_30_46A8",        # 1E, 30
        "Function_31_46B3",        # 1F, 31
        "Function_32_46C5",        # 20, 32
        "Function_33_4A49",        # 21, 33
        "Function_34_4ABA",        # 22, 34
        "Function_35_4AD0",        # 23, 35
        "Function_36_4C79",        # 24, 36
        "Function_37_4F2B",        # 25, 37
    ))


    def Function_0_854(): pass

    label("Function_0_854")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_88C"),
        (1, "loc_898"),
        (2, "loc_8A4"),
        (3, "loc_8B0"),
        (4, "loc_8BC"),
        (5, "loc_8C8"),
        (6, "loc_8D4"),
        (SWITCH_DEFAULT, "loc_8E0"),
    )


    label("loc_88C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_898")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_903")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_903")

    Return()

    # Function_0_854 end

    def Function_1_904(): pass

    label("Function_1_904")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_956")
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, -9000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, 13000, 2000, 0x0)
    Sleep(300)
    Jump("Function_1_904")

    label("loc_956")

    Return()

    # Function_1_904 end

    def Function_2_957(): pass

    label("Function_2_957")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98F")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_2_957")

    label("loc_98F")

    Return()

    # Function_2_957 end

    def Function_3_990(): pass

    label("Function_3_990")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3F")
    SetChrPos(0x0, 0, 0, 21840, 180)
    SetChrPos(0x1, 0, 0, 21840, 180)
    SetChrPos(0x2, 0, 0, 21840, 180)
    SetChrPos(0x3, 0, 0, 21840, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A17")
    SetChrPos(0x4, 0, 0, 21840, 180)
    SetChrPos(0x5, 0, 0, 21840, 180)
    Jump("loc_A36")

    label("loc_A17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A36")
    SetChrPos(0x4, 0, 0, 21840, 180)

    label("loc_A36")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3F")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A56")
    Jump("loc_E55")

    label("loc_A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A6E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A86")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B5B")
    SetChrPos(0x9, 2730, 0, -9140, 45)
    SetChrPos(0x8, -3650, 0, -1670, 270)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6010, 0, -4070, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 3930, 0, 510, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3230, 0, 1580, 135)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1830, 0, -4530, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1830, 0, -6290, 360)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 170, 0, -5890, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2890, 0, -2500, 90)
    Jump("loc_E55")

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BB9")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2050, 0, 8850, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_B99")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2840, 0, -530, 270)

    label("loc_B99")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2490, 0, 2350, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BF3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4720, 0, 2440, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3740, 0, 2940, 90)
    Jump("loc_E55")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C21")
    SetChrChipByIndex(0x8, 0xB)
    SetChrPos(0x8, -3650, 0, -1670, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C85")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 2050, 0, 8850, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4720, 0, 2440, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3740, 0, 2940, 90)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_E55")

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA0")
    SetChrFlags(0x9, 0x80)

    label("loc_CA0")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 2050, 0, 8850, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4720, 0, 2440, 270)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3740, 0, 2940, 90)
    SetChrFlags(0x12, 0x10)
    Jump("loc_E55")

    label("loc_CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D2B")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2490, 0, 2350, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2050, 0, 8850, 270)
    Jump("loc_E55")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D6A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2490, 0, 2350, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1490, 0, 2550, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_E55")

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DA9")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2490, 0, 2350, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1490, 0, 2550, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_E55")

    label("loc_DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DED")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2490, 0, 2350, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1490, 0, 2550, 0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_E55")

    label("loc_DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E1B")
    SetChrChipByIndex(0x8, 0xB)
    SetChrPos(0x8, -3650, 0, -1670, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E55")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2490, 0, 2350, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1490, 0, 2550, 0)
    SetChrFlags(0x11, 0x10)

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6D")
    ClearMapFlags(0x2000)
    Jump("loc_E74")

    label("loc_E6D")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E88")
    ClearScenarioFlags(0x22, 0)
    Event(0, 21)
    Jump("loc_EAB")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E9C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 24)
    Jump("loc_EAB")

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EAB")
    ClearScenarioFlags(0x22, 3)
    Event(0, 25)

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED6")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_ED6")

    Return()

    # Function_3_990 end

    def Function_4_ED7(): pass

    label("Function_4_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F8C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102C")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_107F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x28, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_107F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C8")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    Jump("loc_10FE")

    label("loc_10C8")

    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)

    label("loc_10FE")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_111A")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_111A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1146")
    OP_1B(0x3, 0x0, 0x22)

    label("loc_1146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115E")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_116C")
    Jump("loc_11C1")

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_117F")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_118D")
    Jump("loc_11C1")

    label("loc_118D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11A0")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11B3")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11C1")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_11C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D4")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E7")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FA")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120D")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1220")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_1220")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_124D")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_124D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_125B")
    Jump("loc_1384")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1269")
    Jump("loc_1384")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1277")
    Jump("loc_1384")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_129E")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_129E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12AC")
    Jump("loc_1384")

    label("loc_12AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12D3")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1306")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1301")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)

    label("loc_1301")

    Jump("loc_1384")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_132D")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1354")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1362")
    Jump("loc_1384")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1384")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)

    label("loc_1384")

    SetMapObjFlags(0xB, 0x4)
    Return()

    # Function_4_ED7 end

    def Function_5_138B(): pass

    label("Function_5_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B9")
    Call(0, 33)
    Return()

    label("loc_13B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_153C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A5")

    #C0001
    ChrTalk(
        0xFE,
        (
            "从独立宣言正式发表之日起，\x01",
            "铁道列车就全面\x01",
            "停止了运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "此外，帝国爆发了内战，\x01",
            "共和国境内则\x01",
            "出现了经济危机……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "唉，那个可以眺望铁道列车的\x01",
            "和平时代已经结束了吗？\x01",
            "再没有比这更让人悲伤的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1537")

    label("loc_14A5")


    #C0004
    ChrTalk(
        0xFE,
        (
            "从独立宣言正式发表之日起，\x01",
            "铁道列车就全面\x01",
            "停止了运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "唉，那个可以眺望铁道列车的\x01",
            "和平时代已经结束了吗？\x01",
            "再没有比这更让人悲伤的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1537")

    Jump("loc_2279")

    label("loc_153C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_154A")
    Jump("loc_2279")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1678")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F8")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今天就是最后一天了……\x01",
            "铁道列车从明天开始\x01",
            "就要停止运营了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "呜呜，我的人生意义就这样……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "真希望这种局势早日过去，\x01",
            "让列车恢复运营啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1673")

    label("loc_15F8")


    #C0009
    ChrTalk(
        0xFE,
        (
            "呜呜，铁路就是我的人生意义，\x01",
            "但过了今天，\x01",
            "铁道列车就要停止运营了……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "真希望这种局势早日过去，\x01",
            "让列车恢复运营啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1673")

    Jump("loc_2279")

    label("loc_1678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1756")

    #C0011
    ChrTalk(
        0xFE,
        (
            "有传闻说，上次的袭击事件\x01",
            "是帝国策划的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "难道不久前发生的脱轨事件\x01",
            "与占领玛因兹事件也\x01",
            "都是帝国干的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "虽然我很想信任那个拥有\x01",
            "最尖端铁道技术的国家，\x01",
            "但如今真是不能不怀疑他们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17DE")

    label("loc_1756")


    #C0014
    ChrTalk(
        0xFE,
        (
            "难道最近发生的\x01",
            "一系列事件\x01",
            "全都是帝国干的好事……？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "虽然我很想信任那个拥有\x01",
            "最尖端铁道技术的国家，\x01",
            "但如今真是不能不怀疑他们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DE")

    Jump("loc_2279")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_186B")

    #C0016
    ChrTalk(
        0xFE,
        (
            "列车脱轨事件\x01",
            "刚过去没几天，\x01",
            "又发生了占领事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "让人心里很不舒服啊。\x01",
            "事件接连不断地发生，\x01",
            "真的只是偶然吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_199E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1929")

    #C0018
    ChrTalk(
        0xFE,
        (
            "铁路只用了一晚上就彻底修复完毕，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "多亏抢修人员的努力，我今天也可以\x01",
            "尽情感受列车的美妙了……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "真不知该如何感谢那些\x01",
            "通宵作业的警备队员啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1999")

    label("loc_1929")


    #C0021
    ChrTalk(
        0xFE,
        (
            "多亏抢修人员的努力，我今天也可以\x01",
            "尽情感受列车的美妙了……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "真不知该如何感谢那些\x01",
            "通宵作业的警备队员啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1999")

    Jump("loc_2279")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A18")

    #C0023
    ChrTalk(
        0xFE,
        (
            "呜呜，怎么会这样，\x01",
            "竟然发生了脱轨事件……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "列车肯定也不会完好无损吧……\x01",
            "我担心得都有些胸闷了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_1A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFF")

    #C0025
    ChrTalk(
        0xFE,
        (
            "听说昨天有人从月台\x01",
            "飞身跳到了\x01",
            "列车车顶上。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "虽然能理解这种急迫的心情……\x01",
            "但对铁道迷来说，这是不可原谅的行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "用如此粗暴的方式登车，会使列车受到损伤，\x01",
            "还会给乘客们造成困扰，实在是太差劲了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B84")

    label("loc_1AFF")


    #C0028
    ChrTalk(
        0xFE,
        (
            "听说昨天有人从月台\x01",
            "飞身跳到了\x01",
            "列车车顶上。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "用如此粗暴的方式登车，会使列车受到损伤，\x01",
            "还会给乘客们造成困扰，实在是太差劲了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B84")

    Jump("loc_2279")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C38")

    #C0030
    ChrTalk(
        0xFE,
        (
            "独立到底有\x01",
            "什么好处呢？\x01",
            "我真是搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "千万不要与帝国\x01",
            "和共和国为敌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "要是因为那种原因\x01",
            "使铁路停运，\x01",
            "我可就活不下去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C9C")

    label("loc_1C38")


    #C0033
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "千万不要与帝国\x01",
            "和共和国为敌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "如果因为独立\x01",
            "而使铁路停运，\x01",
            "我可就活不下去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9C")

    Jump("loc_2279")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D50")

    #C0035
    ChrTalk(
        0xFE,
        (
            "对我来说，在看过\x01",
            "『艾森古拉夫号』之后，\x01",
            "通商会议就已经结束八成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "接下来，只需等待会议结束，\x01",
            "再好好观赏它离开克洛斯贝尔的\x01",
            "身影就足够了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB7")

    label("loc_1D50")


    #C0037
    ChrTalk(
        0xFE,
        (
            "对我来说，在看过\x01",
            "『艾森古拉夫号』之后，\x01",
            "通商会议就已经结束八成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "好，今天就回家\x01",
            "看书吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB7")

    Jump("loc_2279")

    label("loc_1DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED8")

    #C0039
    ChrTalk(
        0xFE,
        (
            "啊啊啊啊……那、那就是\x01",
            "帝国政府的专用导力列车\x01",
            "『艾森古拉夫号』吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "那以火焰般的鲜红色为基调的稳重设计，\x01",
            "简直就像在昭示着帝国的强大实力一般……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "真是无愧于『铁之伯爵』这个称号的\x01",
            "美妙列车！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "幸好我为了这一天，\x01",
            "特地在事先买了相机……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F5F")

    label("loc_1ED8")


    #C0043
    ChrTalk(
        0xFE,
        (
            "帝国政府的那辆专用列车，\x01",
            "真是辆无愧于『铁之伯爵』\x01",
            "这个称号的美妙列车啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "啊啊，今天真是太棒了。\x01",
            "就算马上死掉都没有遗憾了！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5F")

    Jump("loc_2279")

    label("loc_1F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_20CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205A")

    #C0045
    ChrTalk(
        0xFE,
        (
            "西塞姆里亚通商会议……\x01",
            "听说帝国首脑也会来，\x01",
            "我身为铁道迷，自然要多加关注。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "要说原因，那当然是因为\x01",
            "帝国政府有一辆专用的导力列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "既然是帝国的首脑来访，\x01",
            "绝对会乘坐那辆列车前来……\x01",
            "哎呀，真是太让人期待了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20C9")

    label("loc_205A")


    #C0048
    ChrTalk(
        0xFE,
        (
            "帝国政府有一辆\x01",
            "专用的导力列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "他们一定会乘坐那辆列车来\x01",
            "参加明天的揭幕式。\x01",
            "哎呀，真是太让人期待了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C9")

    Jump("loc_2279")

    label("loc_20CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_213F")

    #C0050
    ChrTalk(
        0xFE,
        "对铁道迷来说，天气根本不算什么。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "被雨淋湿的列车也很棒啊，\x01",
            "那滴着水珠的样子另有一番美感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_213F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FA")

    #C0052
    ChrTalk(
        0xFE,
        (
            "铁道列车今天\x01",
            "也在通畅运行。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "列车那豪华的造型，\x01",
            "以及像是映照着整个\x01",
            "天空般的美丽涂装……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "嗯～不管什么时候看，都觉得好棒。\x01",
            "能成为铁道迷真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2279")

    label("loc_21FA")


    #C0055
    ChrTalk(
        0xFE,
        (
            "列车那豪华的造型，\x01",
            "以及像是映照着整个\x01",
            "天空般的美丽涂装……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "嗯～不管什么时候看，都觉得好棒。\x01",
            "能成为铁道迷真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2279")

    TalkEnd(0xFE)
    Return()

    # Function_5_138B end

    def Function_6_227D(): pass

    label("Function_6_227D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234E")

    #C0057
    ChrTalk(
        0xFE,
        (
            "我负责把克洛斯贝尔市内的\x01",
            "多余物资分送到各地。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "现在几乎得不到来自外国的物资了，\x01",
            "就算合理分配，恐怕也撑不了多久……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "但作为运输业人士，首先要\x01",
            "做好自己力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23D5")

    label("loc_234E")


    #C0060
    ChrTalk(
        0xFE,
        (
            "现在几乎得不到来自外国的物资了，\x01",
            "就算向各地分配物资，\x01",
            "恐怕也撑不了多久……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "但作为运输业人士，首先要\x01",
            "做好自己力所能及的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D5")

    Jump("loc_28D8")

    label("loc_23DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23E8")
    Jump("loc_28D8")

    label("loc_23E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2450")

    #C0062
    ChrTalk(
        0xFE,
        (
            "喂喂，事态好像\x01",
            "很严重了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "连铁道都停止运营了，\x01",
            "今后要如何与外国流通物资啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D8")

    label("loc_2450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_245E")
    Jump("loc_28D8")

    label("loc_245E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_24D1")

    #C0064
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州\x01",
            "竟然会发生\x01",
            "武装占领事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "据说警备队还在苦苦奋战，\x01",
            "到底将会怎样收场呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D8")

    label("loc_24D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24DF")
    Jump("loc_28D8")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24ED")
    Jump("loc_28D8")

    label("loc_24ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2564")

    #C0066
    ChrTalk(
        0xFE,
        (
            "听说你们帮\x01",
            "卡普亚特急便\x01",
            "重新派发了送错的包裹？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "哎呀，那我就放心了，\x01",
            "特别任务支援科果然可靠啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D8")

    label("loc_2564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25FC")

    #C0068
    ChrTalk(
        0xFE,
        (
            "由于出现了来历不明的魔兽，\x01",
            "我们接到了在郊外行驶时\x01",
            "要注意安全的通知。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "我们这些干运输业的人\x01",
            "总是要东奔西跑，\x01",
            "真是很担心魔兽的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D8")

    label("loc_25FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_265F")

    #C0070
    ChrTalk(
        0xFE,
        "好了，差不多也该去派件了。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "要是不快点把东西送达，\x01",
            "又会被我老爸臭骂一顿的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D8")

    label("loc_265F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_278F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2716")

    #C0072
    ChrTalk(
        0xFE,
        (
            "本想赶快收取包裹，\x01",
            "然后去派送，\x01",
            "但卸货似乎是延误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "看来货运列车上的货物\x01",
            "也要接受相当严密的检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "毕竟帝国的大人物来了，\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_278A")

    label("loc_2716")


    #C0075
    ChrTalk(
        0xFE,
        (
            "本想赶快收取包裹，\x01",
            "然后去派送，\x01",
            "但卸货似乎是延误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "毕竟帝国的大人物来了，\x01",
            "检查力度加强\x01",
            "也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278A")

    Jump("loc_28D8")

    label("loc_278F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_279D")
    Jump("loc_28D8")

    label("loc_279D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_27AB")
    Jump("loc_28D8")

    label("loc_27AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_287E")

    #C0077
    ChrTalk(
        0xFE,
        (
            "我们是个体经营的运输公司──\x01",
            "莱姆斯运输公司，我老爸就是老板。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "虽然开张还没多久，但我们\x01",
            "会以亲切、细心、迅速为原则，\x01",
            "努力为大家服务的。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "如果有什么需要，\x01",
            "请尽管联系我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28D8")

    label("loc_287E")


    #C0080
    ChrTalk(
        0xFE,
        (
            "我们是个体经营的运输公司──\x01",
            "莱姆斯运输公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "如果有什么需要，\x01",
            "请尽管联系我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D8")

    TalkEnd(0xFE)
    Return()

    # Function_6_227D end

    def Function_7_28DC(): pass

    label("Function_7_28DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A29")

    #C0082
    ChrTalk(
        0xFE,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        (
            "#10105F啊……妈妈，\x01",
            "你要去看望芙兰吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "嗯，我去给她送\x01",
            "换洗的衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "那孩子的状态怎么样？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#10108F嗯，目前还很\x01",
            "疲惫……\x01",
            "但精神还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "这样啊，那就好。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "在她恢复之前，\x01",
            "我会尽量多去看她的。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "芙兰就交给我照顾，\x01",
            "你专心做好\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        "#10100F嗯，我知道。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 7)
    Jump("loc_2A7B")

    label("loc_2A29")


    #C0091
    ChrTalk(
        0xFE,
        (
            "诺艾尔，你明天就要\x01",
            "离开支援科了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "努力工作吧，\x01",
            "别给自己留下什么遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7B")

    TalkEnd(0xFE)
    Return()

    # Function_7_28DC end

    def Function_8_2A7F(): pass

    label("Function_8_2A7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2AF4")

    #N0093
    NpcTalk(
        0xFE,
        "外国人",
        (
            "什么？过了今天就\x01",
            "没法回帝国了……！？\x02",
        )
    )

    CloseMessageWindow()

    #N0094
    NpcTalk(
        0xFE,
        "外国人",
        (
            "哼，什么国防军啊！\x01",
            "竟敢如此肆意妄为！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2E")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B5C")

    #N0095
    NpcTalk(
        0xFE,
        "市民",
        (
            "没想到克洛斯贝尔市\x01",
            "会遭到袭击……\x02",
        )
    )

    CloseMessageWindow()

    #N0096
    NpcTalk(
        0xFE,
        "市民",
        (
            "我们到底做错了什么……\x01",
            "真是受够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2E")

    label("loc_2B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BCB")

    #N0097
    NpcTalk(
        0xFE,
        "市民",
        (
            "独立吗……\x01",
            "没想到市长会提出\x01",
            "这样的提案……\x02",
        )
    )

    CloseMessageWindow()

    #N0098
    NpcTalk(
        0xFE,
        "市民",
        (
            "无论如何，我真希望\x01",
            "能顺利实现啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C2E")

    label("loc_2BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C2E")

    #C0099
    ChrTalk(
        0xFE,
        (
            "哦哦……\x01",
            "多么漂亮的街道！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然都已经这把年纪了，\x01",
            "但我还是兴奋得不得了啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C2E")

    TalkEnd(0xFE)
    Return()

    # Function_8_2A7F end

    def Function_9_2C32(): pass

    label("Function_9_2C32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C8A")

    #N0101
    NpcTalk(
        0xFE,
        "外国人",
        "老头子，你冷静些……\x02",
    )

    CloseMessageWindow()

    #N0102
    NpcTalk(
        0xFE,
        "外国人",
        (
            "总之，我们赶快\x01",
            "去买票吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D82")

    label("loc_2C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2CCF")

    #C0103
    ChrTalk(
        0xFE,
        (
            "刚才开过去很多辆急救车……\x01",
            "到、到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D82")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D1D")

    #C0104
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "果然很大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "早知如此，就买本\x01",
            "旅游指南了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D82")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D82")

    #C0106
    ChrTalk(
        0xFE,
        (
            "虽然老伴很高兴，\x01",
            "但我却有点担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "毕竟克洛斯贝尔可是个\x01",
            "有『魔都』之称的城市啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D82")

    TalkEnd(0xFE)
    Return()

    # Function_9_2C32 end

    def Function_10_2D86(): pass

    label("Function_10_2D86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E46")

    #N0108
    NpcTalk(
        0xFE,
        "外国人",
        (
            "失去这份在克洛斯贝尔的工作虽然遗憾，\x01",
            "但总比回不了故乡要好。\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0xFE,
        "外国人",
        (
            "事到如今，就算只能买到站票也无所谓了，\x01",
            "在被卷进危险的事情之前，\x01",
            "必须要赶快离开克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2B")

    label("loc_2E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2EB8")

    #C0110
    ChrTalk(
        0xFE,
        (
            "居然会被武装集团占领，\x01",
            "为什么会发生这种事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "不知玛因兹那边的情况如何，\x01",
            "真让人担心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2B")

    label("loc_2EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F2B")

    #C0112
    ChrTalk(
        0xFE,
        (
            "唔～今天预约的\x01",
            "酒店要怎么走呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "我痛下血本，在欢乐街的酒店订了房间，\x01",
            "必须要好好享受这次的旅行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2B")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D86 end

    def Function_11_2F2F(): pass

    label("Function_11_2F2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FA6")

    #N0114
    NpcTalk(
        0xFE,
        "外国人",
        (
            "不久前，我接到了帝国\x01",
            "发来的撤离通知……\x02",
        )
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0xFE,
        "外国人",
        (
            "唉，我很喜欢在\x01",
            "克洛斯贝尔的生活啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_2FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3004")

    #C0116
    ChrTalk(
        0xFE,
        (
            "真怕那个武装集团\x01",
            "来克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "警备队就不能\x01",
            "赶快解决这个问题吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_3004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_306C")

    #C0118
    ChrTalk(
        0xFE,
        (
            "呵呵，这孩子，\x01",
            "竟然高兴成这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "但我也理解他的心情，\x01",
            "毕竟克洛斯贝尔是个\x01",
            "超级大都市。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306C")

    TalkEnd(0xFE)
    Return()

    # Function_11_2F2F end

    def Function_12_3070(): pass

    label("Function_12_3070")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_30D1")

    #C0120
    ChrTalk(
        0xFE,
        (
            "我打算立刻\x01",
            "离开克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "这么危险的地方，\x01",
            "我连一秒钟都不想多待了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_319E")

    label("loc_30D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3142")

    #C0122
    ChrTalk(
        0xFE,
        (
            "一直在说独立，\x01",
            "但我直到现在都\x01",
            "搞不懂是怎么回事。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "在居民投票日之前，\x01",
            "稍微了解一下好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_319E")

    label("loc_3142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_319E")

    #C0124
    ChrTalk(
        0xFE,
        "今天早上真是太热闹了。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "竟然用那么豪华的轿车来接送，\x01",
            "真不愧是国家首脑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319E")

    TalkEnd(0xFE)
    Return()

    # Function_12_3070 end

    def Function_13_31A2(): pass

    label("Function_13_31A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3215")

    #N0126
    NpcTalk(
        0xFE,
        "外国人",
        (
            "怎么办……\x01",
            "人实在太多了，根本进不去啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0xFE,
        "外国人",
        (
            "呜呜，我还能安全\x01",
            "回到共和国吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3269")

    label("loc_3215")


    #C0128
    ChrTalk(
        0xFE,
        (
            "我在百货店的楼顶上\x01",
            "观看了揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "啊～真想近距离目睹\x01",
            "尤莉亚大人的尊容啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3269")

    TalkEnd(0xFE)
    Return()

    # Function_13_31A2 end

    def Function_14_326D(): pass

    label("Function_14_326D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32C6")

    #C0130
    ChrTalk(
        0xFE,
        (
            "喂，为什么非要\x01",
            "回帝国呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "人家好不容易才\x01",
            "认识了那么多朋友……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B5")

    label("loc_32C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_331F")

    #C0132
    ChrTalk(
        0xFE,
        (
            "我们只是在车站里玩了一会，\x01",
            "就被站员生气地赶出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "哼，真小气～\x02",
    )

    CloseMessageWindow()
    Jump("loc_33B5")

    label("loc_331F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3370")

    #C0134
    ChrTalk(
        0xFE,
        (
            "好～那今天就在\x01",
            "车站里玩捉迷藏吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "嘿嘿，先由我来扮鬼哦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_33B5")

    label("loc_3370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33B5")

    #C0136
    ChrTalk(
        0xFE,
        "哇～这里就是克洛斯贝尔吗～！！\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "快走啊，妈妈～！！\x02",
    )

    CloseMessageWindow()

    label("loc_33B5")

    TalkEnd(0xFE)
    Return()

    # Function_14_326D end

    def Function_15_33B9(): pass

    label("Function_15_33B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3439")

    #C0138
    ChrTalk(
        0xFE,
        (
            "唉，哥哥真是的……\x01",
            "所以我当时才劝你不要进去啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "……话说回来，站员们\x01",
            "好像都很忙啊。\x01",
            "发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B1")

    label("loc_3439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3487")

    #C0140
    ChrTalk(
        0xFE,
        "哎～？不要啦，哥哥。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "随便进去，会惹车站里的人生气的～\x02",
    )

    CloseMessageWindow()
    Jump("loc_34B1")

    label("loc_3487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B1")

    #C0142
    ChrTalk(
        0xFE,
        (
            "我想和爸爸一起去\x01",
            "巴鲁卡玩～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B1")

    TalkEnd(0xFE)
    Return()

    # Function_15_33B9 end

    def Function_16_34B5(): pass

    label("Function_16_34B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3546")

    #C0143
    ChrTalk(
        0xFE,
        (
            "那些恐怖分子究竟\x01",
            "想以什么方法潜入\x01",
            "克洛斯贝尔呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "明明应该没有死角了……\x01",
            "总之，现在也只能保持现状，\x01",
            "继续进行警戒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362C")

    label("loc_3546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35A4")

    #C0145
    ChrTalk(
        0xFE,
        (
            "呼，揭幕式总算结束了，\x01",
            "肩上的担子稍微轻了一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "但还是不能\x01",
            "掉以轻心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362C")

    label("loc_35A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_362C")

    #C0147
    ChrTalk(
        0xFE,
        (
            "车站和空港内部聚集了不少二科的搜查官，\x01",
            "其它地方的情况也都差不多。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "在我印象中，\x01",
            "如此严密的警戒体制\x01",
            "好像还是头一次呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362C")

    TalkEnd(0xFE)
    Return()

    # Function_16_34B5 end

    def Function_17_3630(): pass

    label("Function_17_3630")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3696")

    #C0149
    ChrTalk(
        0xFE,
        (
            "我是来为准备回帝国的\x01",
            "妻子和女儿送行的……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "但、但竟然发生了脱轨事件……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36C3")

    label("loc_3696")


    #C0151
    ChrTalk(
        0xFE,
        (
            "要、要是我妻子和女儿\x01",
            "坐上了那趟列车……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C3")

    TalkEnd(0xFE)
    Return()

    # Function_17_3630 end

    def Function_18_36C7(): pass

    label("Function_18_36C7")

    TalkBegin(0xFE)

    #C0152
    ChrTalk(
        0xFE,
        "真是太可怕了……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "不知受害情况\x01",
            "有多严重……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_36C7 end

    def Function_19_3703(): pass

    label("Function_19_3703")

    TalkBegin(0xFE)

    #C0154
    ChrTalk(
        0xFE,
        "列车停驶了？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "那我今天也可以\x01",
            "和爸爸在一起了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3703 end

    def Function_20_3741(): pass

    label("Function_20_3741")

    TalkBegin(0xFE)

    #C0156
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔车站将\x01",
            "从明日起暂停运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "重新恢复运营的时间\x01",
            "尚未确定。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "准备回国的外国乘客\x01",
            "请尽快登车。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3741 end

    def Function_21_37B9(): pass

    label("Function_21_37B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51231.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(825)
    SoundLoad(455)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x1B, 0xC)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0xC)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0xC)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0xC)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0xC)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0xC)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x13, 0x21)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1B, -3750, 0, -1250, 270)
    SetChrPos(0x1C, -3750, 0, -2750, 270)
    SetChrPos(0x1D, -2750, 0, 11000, 270)
    SetChrPos(0x1E, -2750, 0, 9500, 270)
    SetChrPos(0x1F, -2750, 0, 5500, 270)
    SetChrPos(0x20, -2750, 0, 4000, 270)
    SetChrPos(0x21, -37500, -11600, 7500, 90)
    OP_D5(0x21, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(9150, 2700, -1950, 0)
    MoveCamera(48, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27850, 0)
    OP_68(-2750, 1000, 7000, 5000)
    MoveCamera(45, 25, 0, 5000)
    SetCameraDistance(16000, 5000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetCameraDistance(15750, 200)
    OP_0D()
    Sleep(500)
    Fade(1000)
    SetChrPos(0x1B, -8000, -10300, -1000, 0)
    SetChrPos(0x1C, -9500, -10300, -1000, 0)
    SetChrPos(0x1D, -11000, -10300, -1000, 0)
    SetChrPos(0x1E, -12500, -10300, -1000, 0)
    SetChrPos(0x1F, -14000, -10300, -1000, 0)
    SetChrPos(0x20, -15500, -10300, -1000, 0)
    OP_68(-20000, -8500, 7500, 0)
    MoveCamera(325, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7000, 0)
    OP_68(0, -8500, 7500, 8000)
    MoveCamera(70, 15, 0, 8000)
    SetCameraDistance(32000, 8000)
    Sound(455, 0, 100, 0)
    BeginChrThread(0x22, 1, 0, 23)

    def lambda_3AD6():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3AD6)
    BeginChrThread(0x21, 0, 0, 22)
    Sleep(5000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_37B9 end

    def Function_22_3B0D(): pass

    label("Function_22_3B0D")

    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    Return()

    # Function_22_3B0D end

    def Function_23_3B72(): pass

    label("Function_23_3B72")

    Sound(825, 2, 10, 0)
    Sleep(100)
    OP_25(0x339, 0x14)
    Sleep(100)
    OP_25(0x339, 0x1E)
    Sleep(100)
    OP_25(0x339, 0x28)
    Sleep(100)
    OP_25(0x339, 0x32)
    Sleep(100)
    OP_25(0x339, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x46)
    Sleep(100)
    OP_25(0x339, 0x50)
    Sleep(5300)
    StopSound(825, 2000, 80)
    Return()

    # Function_23_3B72 end

    def Function_24_3BB3(): pass

    label("Function_24_3BB3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41800.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    SetChrPos(0x0, 6500, 0, 8000, 0)
    SetChrPos(0x1, 6500, 0, 8000, 0)
    SetChrPos(0x2, 6500, 0, 8000, 0)
    SetChrPos(0x3, 6500, 0, 8000, 0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x12, 0x18)
    OP_49()
    SetChrPos(0x18, 5000, 0, -1000, 0)
    OP_D5(0x18, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x3)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2500, 0, 100, 270)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 2500, 0, -4500, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 200, 0, -3500, 90)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1000, 0, -1800, 90)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1000, 0, -3000, 90)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x5)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1000, 0, 0, 135)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x6)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 100, 0, -4900, 45)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2400, 0, -2400, 90)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -1400, 0, -5400, 45)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 600, 0, 1000, 135)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(2200, 1200, -2000, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    MoveCamera(51, 23, 0, 13000)
    SetCameraDistance(16500, 13000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(150, 100, -1, -1)
    SetChrName("迪塔总统")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "长年以来，他们一直把\x01",
            "我们的克洛斯贝尔视为\x01",
            "自己的『附属州』。\x02\x03",

            "无论他们犯下什么罪行，\x01",
            "我们都没有追究的权力。\x02\x03",

            "不仅如此……\x01",
            "他们至今还在以掠夺巨额税收的形式\x01",
            "来不断榨取我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x12, 0x4)
    Sleep(300)
    SetMessageWindowPos(150, 110, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("迪塔总统")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S而且他们的所作所为\x01",
            "还远远不止这些！\x02\x03",

            "#4S他们甚至做出过很多\x01",
            "危及我们生命的行为！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c040D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3BB3 end

    def Function_25_4018(): pass

    label("Function_25_4018")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 300, 0, -24600, 0)
    SetChrPos(0x102, 1600, 0, -25000, 0)
    SetChrPos(0x103, 300, 0, -26000, 0)
    SetChrPos(0x104, 1600, 0, -26400, 0)
    SetChrPos(0x109, 900, 0, -27500, 0)
    SetChrPos(0x105, -1000, 0, -26400, 0)
    SetChrPos(0x106, -500, 0, -27500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_68(0, 1200, -15300, 0)
    MoveCamera(40, 29, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(32500, 0)

    def lambda_40EC():
        OP_97(0x101, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40EC)
    Sleep(100)

    def lambda_4109():
        OP_97(0x102, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4109)
    Sleep(100)

    def lambda_4126():
        OP_97(0x103, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4126)
    Sleep(100)

    def lambda_4143():
        OP_97(0x104, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4143)
    Sleep(100)

    def lambda_4160():
        OP_97(0x105, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4160)
    Sleep(100)

    def lambda_417D():
        OP_97(0x109, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_417D)
    Sleep(100)

    def lambda_419A():
        OP_97(0x106, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_419A)
    OP_68(0, 1200, -5300, 3000)
    MoveCamera(50, 25, 0, 3000)
    SetCameraDistance(22500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(500, 1200, -1300, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(16500, 2000)
    OP_0D()
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 3, 0, 26)
    WaitChrThread(0x102, 0)
    BeginChrThread(0x102, 3, 0, 27)
    WaitChrThread(0x104, 0)
    BeginChrThread(0x104, 3, 0, 28)
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 3, 0, 29)
    WaitChrThread(0x109, 0)
    BeginChrThread(0x109, 3, 0, 30)
    WaitChrThread(0x106, 0)
    BeginChrThread(0x106, 3, 0, 31)
    OP_6F(0x79)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x101,
        (
            "#11P#00006F必须要想办法\x01",
            "和科长他们取得联络……\x02\x03",

            "#00013F怎么回事……？\x01",
            "这蓝白色的雾气是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#5P#00108F简直就像曾在僧院和塔中\x01",
            "出现过的那种……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x109,
        (
            "#10108F#5P街上……\x01",
            "一个人影都没有呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x105,
        (
            "#11P#10408F毕竟市外\x01",
            "发生了战斗，\x01",
            "大概都去避难了……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        "#12P#00205F#30W………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x106, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 500)

    #C0166
    ChrTalk(
        0x102,
        "#5P#00105F缇欧？\x02",
    )

    CloseMessageWindow()

    def lambda_43D7():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_43D7)
    Sleep(30)

    def lambda_43E7():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_43E7)
    Sleep(30)

    def lambda_43F7():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_43F7)
    Sleep(30)

    def lambda_4407():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4407)
    Sleep(30)

    def lambda_4417():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4417)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0167
    ChrTalk(
        0x104,
        "#11P#00301F怎么了？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        (
            "#12P#00203F……从中央广场的方向\x01",
            "传来了鸣响的声音。\x02\x03",

            "#00201F是那口大钟。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#5P#00007F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x106,
        "#12P#10701F……去看看吧。\x02",
    )

    CloseMessageWindow()

    def lambda_44DC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44DC)
    Sleep(30)

    def lambda_44EC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_44EC)
    Sleep(30)

    def lambda_44FC():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_44FC)
    Sleep(30)

    def lambda_450C():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_450C)
    Sleep(30)

    def lambda_451C():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_451C)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(500, 1200, 7500, 3000)
    MoveCamera(37, 21, 0, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_4565():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4565)
    Sleep(100)

    def lambda_4582():
        OP_97(0x102, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4582)
    Sleep(100)

    def lambda_459F():
        OP_97(0x103, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_459F)
    Sleep(100)

    def lambda_45BC():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_45BC)
    Sleep(100)

    def lambda_45D9():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_45D9)
    Sleep(100)

    def lambda_45F6():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_45F6)
    Sleep(100)

    def lambda_4613():
        OP_97(0x106, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4613)
    Sleep(1900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0x106, 0xFF)
    SetScenarioFlags(0x24, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4018 end

    def Function_26_4661(): pass

    label("Function_26_4661")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_26_4661 end

    def Function_27_4673(): pass

    label("Function_27_4673")

    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_4673 end

    def Function_28_4688(): pass

    label("Function_28_4688")

    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_28_4688 end

    def Function_29_469D(): pass

    label("Function_29_469D")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_469D end

    def Function_30_46A8(): pass

    label("Function_30_46A8")

    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_30_46A8 end

    def Function_31_46B3(): pass

    label("Function_31_46B3")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_46B3 end

    def Function_32_46C5(): pass

    label("Function_32_46C5")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(6400, 1900, -1900, 0)
    MoveCamera(57, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15860, 0)
    SetChrPos(0x101, 6500, 0, -1900, 90)
    SetChrPos(0x102, 5900, 0, -1000, 90)
    SetChrPos(0x103, 5900, 0, -2800, 90)
    SetChrPos(0x104, 3900, 0, -1900, 90)
    SetChrPos(0xF4, 4300, 0, -3100, 90)
    SetChrPos(0xF5, 4300, 0, -700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(300)

    #C0171
    ChrTalk(
        0x101,
        (
            "#00003F（……不知接下来要和\x01",
            "  雾香小姐他们谈多久。）\x02\x03",

            "#00001F（作战即将开始，还是先把\x01",
            "  其它事情都处理完为好。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一旦触发接下来的剧情，\x01",
            "突击兰花塔的作战就会开始，\x01",
            "届时将无法在市内自由行动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "进入车站\x01",              # 0
            "先去处理其它事情\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_48B6"),
        (1, "loc_4A16"),
        (SWITCH_DEFAULT, "loc_4A48"),
    )


    label("loc_48B6")

    OP_68(8400, 1900, -1900, 1500)
    MoveCamera(90, 13, 0, 1500)

    def lambda_48D7():
        OP_96(0xFE, 0x2328, 0xFA, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48D7)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    SetCameraDistance(17500, 3000)

    def lambda_491B():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_491B)
    Sleep(50)

    def lambda_4938():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4938)
    Sleep(50)

    def lambda_4955():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4955)
    Sleep(50)

    def lambda_4972():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4972)
    Sleep(50)

    def lambda_498F():
        OP_97(0xF4, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_498F)
    Sleep(50)

    def lambda_49AC():
        OP_97(0xF5, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_49AC)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_49D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49D3)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0xF4, 0xFF)
    EndChrThread(0xF5, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Jump("loc_4A48")

    label("loc_4A16")

    SetChrPos(0x0, 6500, 0, -2000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_4A48")

    label("loc_4A48")

    Return()

    # Function_32_46C5 end

    def Function_33_4A49(): pass

    label("Function_33_4A49")

    TalkBegin(0x8)

    #C0173
    ChrTalk(
        0x8,
        (
            "刚才有一辆帝国制造的黑色运输车\x01",
            "开向了中央广场。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "……后来开到哪里去了？\x01",
            "对不起，那就不太清楚了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_33_4A49 end

    def Function_34_4ABA(): pass

    label("Function_34_4ABA")

    EventBegin(0x1)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)
    Return()

    # Function_34_4ABA end

    def Function_35_4AD0(): pass

    label("Function_35_4AD0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B14")

    #C0175
    ChrTalk(
        0x101,
        (
            "#00000F这里是克洛斯贝尔车站，\x01",
            "现在不需要进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C65")

    label("loc_4B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B60")
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4BBD")

    label("loc_4B60")


    #C0177
    ChrTalk(
        0x101,
        (
            "#00001F……看来车站已经\x01",
            "被封锁了啊。\x02\x03",

            "#00003F算了，也没什么\x01",
            "重要的事，\x01",
            "就先别管这里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BBD")

    SetScenarioFlags(0x1CE, 4)
    Jump("loc_4C65")

    label("loc_4BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C2E")

    #C0178
    ChrTalk(
        0x101,
        (
            "#00001F……站内都是准备回国的\x01",
            "外国人，场面相当混乱。\x02\x03",

            "#00003F我们还是\x01",
            "不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Jump("loc_4C65")

    label("loc_4C2E")


    #C0179
    ChrTalk(
        0x101,
        (
            "#00000F这里是克洛斯贝尔车站，\x01",
            "现在不需要进去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    label("loc_4C65")

    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)
    Return()

    # Function_35_4AD0 end

    def Function_36_4C79(): pass

    label("Function_36_4C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D30")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE7")

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000F前方是城市的南出口。\x02\x03",

            "现在也没有什么事要去这边，\x01",
            "还是别出去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D1D")

    label("loc_4CE7")


    #C0181
    ChrTalk(
        0x101,
        (
            "#00000F现在也没有什么事要去这边，\x01",
            "还是别出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1D")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA6")

    #C0182
    ChrTalk(
        0x101,
        (
            "#00001F前方是城市的南出口。\x02\x03",

            "现在要集中精力，专心调查\x01",
            "列车事故，别到处乱跑了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4DE0")

    label("loc_4DA6")


    #C0183
    ChrTalk(
        0x101,
        (
            "#00001F现在不需要往这边走，\x01",
            "集中精力调查列车事故吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE0")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E4D")
    EventBegin(0x1)

    #C0184
    ChrTalk(
        0x101,
        (
            "#00001F必须要尽快\x01",
            "追上兰迪，\x01",
            "现在没时间绕远路了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EA0")
    EventBegin(0x1)

    #C0185
    ChrTalk(
        0x101,
        (
            "#00001F现在不是去市外的时候，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F2A")
    EventBegin(0x1)

    #C0186
    ChrTalk(
        0x101,
        (
            "#00001F都已经走到了这一步，\x01",
            "现在没理由离开市区。\x02\x03",

            "突入兰花塔的作战行动……\x01",
            "无论如何也要取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_4F2A")

    Return()

    # Function_36_4C79 end

    def Function_37_4F2B(): pass

    label("Function_37_4F2B")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_37_4F2B end

    SaveToFile()

Try(main)
