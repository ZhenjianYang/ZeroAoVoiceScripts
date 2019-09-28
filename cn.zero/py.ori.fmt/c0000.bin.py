from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0000.bin",                # FileName
        "c0000",                    # MapName
        "c0000",                    # Location
        0x0002,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0000",                  # 0
        "比利",                   # 1
        "利德",                   # 2
        "弗里吉亚",               # 3
        "莱缇娜",                 # 4
        "玛夏",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "商务人士",               # 17
        "商务人士",               # 18
        "游客",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "游客",                   # 22
        "游客",                   # 23
        "游客",                   # 24
        "游客",                   # 25
        "游客",                   # 26
        "游客",                   # 27
        "赛尔盖科长",             # 28
        "老人",                   # 29
        "老妇人",                 # 30
        "格蕾丝",                 # 31
        "亚里欧斯",               # 32
        "列车",                   # 33
        "游客",                   # 34
        "游客",                   # 35
        "游客",                   # 36
        "车00",                   # 37
        "库罗玛",                 # 38
        "中央广场",               # 39
        "西街",                   # 40
        "行政区",                 # 41
        "住宅街",                 # 42
        "欢乐街",                 # 43
        "东街",                   # 44
        "旧城区",                 # 45
        "港湾区",                 # 46
        "ＩＢＣ",                 # 47
        "站前街道",               # 48
        "后巷",                   # 49
        "乌尔斯拉间道",           # 50
        "东克洛斯贝尔街道",       # 51
        "西克洛斯贝尔街道",       # 52
        "玛因兹山道",             # 53
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21700.itc",                   # 05
        "chr/ch22800.itc",                   # 06
        "chr/ch24400.itc",                   # 07
        "chr/ch21300.itc",                   # 08
        "chr/ch21800.itc",                   # 09
        "chr/ch21900.itc",                   # 0A
        "chr/ch21200.itc",                   # 0B
        "chr/ch27700.itc",                   # 0C
        "chr/ch27800.itc",                   # 0D
        "chr/ch22100.itc",                   # 0E
        "chr/ch22000.itc",                   # 0F
        "chr/ch32200.itc",                   # 10
        "chr/ch32300.itc",                   # 11
        "chr/ch20200.itc",                   # 12
        "chr/ch20300.itc",                   # 13
        "chr/ch33300.itc",                   # 14
        "chr/ch34500.itc",                   # 15
        "chr/ch24900.itc",                   # 16
    ))

    DeclNpc(4000,    0,       -7000,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1830,   0,       13000,   180,  261,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(5849,    0,       1759,    315,  389,  0x0, 0,   20,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4650,    0,       2950,    135,  389,  0x0, 0,   21,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4389,    0,       -4900,   90,   389,  0x0, 0,   21,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6039,    0,       2779,    292,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4940,    0,       3049,    111,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5920,    0,       2700,    291,  405,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4750,    0,       3109,    111,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(5909,    0,       2680,    291,  389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(5239,    0,       2819,    286,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6539,    0,       1690,    81,   389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(6320,    0,       2339,    177,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5130,    0,       2099,    290,  389,  0x0, 0,   11,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4079,    0,       2480,    110,  389,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3369,    0,       1950,    180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3480,    0,       529,     0,    389,  0x0, 0,   13,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4369,    0,       2119,    101,  389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5940,    0,       1970,    281,  389,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4539,    0,       3069,    45,   389,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5880,    0,       2589,    315,  389,  0x0, 0,   19,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5110,    0,       3750,    112,  389,  0x0, 0,   14,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(5909,    0,       3420,    292,  389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(6360,    0,       2480,    225,  389,  0x0, 0,   2,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(5239,    0,       2789,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(4579,    0,       1519,    252,  389,  0x0, 0,   4,   0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(699,     0,       13149,   270,  389,  0x0, 0,   22,  0,   0,   0,   0,   33,  255,  0)

    DeclEvent(0x0000, 0, 56,  -11.670000076293945,   17.1200008392334,      -5.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.835000038146973,     -8.5600004196167,      1.100000023841858,     1.0])
    DeclEvent(0x0000, 0, 58,  8.5,                   -2.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.25,                 0.5,                   0.10000000149011612,   1.0])

    DeclActor(-22300,  -5000,   20700,   2000,    -21950,  -4000,   21360,   0x007C, 0,  35, 0x0000)

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
    PlaceName(2.0, 0.0, 55.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_940",          # 00, 0
        "Function_1_9F8",          # 01, 1
        "Function_2_A4B",          # 02, 2
        "Function_3_A84",          # 03, 3
        "Function_4_D88",          # 04, 4
        "Function_5_1040",         # 05, 5
        "Function_6_189F",         # 06, 6
        "Function_7_2578",         # 07, 7
        "Function_8_26DD",         # 08, 8
        "Function_9_2847",         # 09, 9
        "Function_10_298A",        # 0A, 10
        "Function_11_2B19",        # 0B, 11
        "Function_12_2B69",        # 0C, 12
        "Function_13_2BC8",        # 0D, 13
        "Function_14_2C1C",        # 0E, 14
        "Function_15_2C6C",        # 0F, 15
        "Function_16_2CD4",        # 10, 16
        "Function_17_2D42",        # 11, 17
        "Function_18_2D93",        # 12, 18
        "Function_19_2DD3",        # 13, 19
        "Function_20_2E2F",        # 14, 20
        "Function_21_2EB4",        # 15, 21
        "Function_22_2F07",        # 16, 22
        "Function_23_2F4C",        # 17, 23
        "Function_24_2F69",        # 18, 24
        "Function_25_2FD5",        # 19, 25
        "Function_26_300E",        # 1A, 26
        "Function_27_3049",        # 1B, 27
        "Function_28_308D",        # 1C, 28
        "Function_29_30EF",        # 1D, 29
        "Function_30_3193",        # 1E, 30
        "Function_31_31EC",        # 1F, 31
        "Function_32_324A",        # 20, 32
        "Function_33_32B4",        # 21, 33
        "Function_34_345F",        # 22, 34
        "Function_35_48D9",        # 23, 35
        "Function_36_4AC1",        # 24, 36
        "Function_37_4E79",        # 25, 37
        "Function_38_4EB3",        # 26, 38
        "Function_39_4EF0",        # 27, 39
        "Function_40_4F35",        # 28, 40
        "Function_41_4F76",        # 29, 41
        "Function_42_4FBB",        # 2A, 42
        "Function_43_4FFC",        # 2B, 43
        "Function_44_8136",        # 2C, 44
        "Function_45_904B",        # 2D, 45
        "Function_46_9141",        # 2E, 46
        "Function_47_9237",        # 2F, 47
        "Function_48_928C",        # 30, 48
        "Function_49_92E1",        # 31, 49
        "Function_50_9336",        # 32, 50
        "Function_51_9397",        # 33, 51
        "Function_52_93D4",        # 34, 52
        "Function_53_9411",        # 35, 53
        "Function_54_9673",        # 36, 54
        "Function_55_9692",        # 37, 55
        "Function_56_A11A",        # 38, 56
        "Function_57_A239",        # 39, 57
        "Function_58_A533",        # 3A, 58
    ))


    def Function_0_940(): pass

    label("Function_0_940")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_980"),
        (1, "loc_98C"),
        (2, "loc_998"),
        (3, "loc_9A4"),
        (4, "loc_9B0"),
        (5, "loc_9BC"),
        (6, "loc_9C8"),
        (SWITCH_DEFAULT, "loc_9D4"),
    )


    label("loc_980")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_98C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_998")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E0")

    label("loc_9F7")

    Return()

    # Function_0_940 end

    def Function_1_9F8(): pass

    label("Function_1_9F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4A")
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, -9000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, 13000, 2000, 0x0)
    Sleep(300)
    Jump("Function_1_9F8")

    label("loc_A4A")

    Return()

    # Function_1_9F8 end

    def Function_2_A4B(): pass

    label("Function_2_A4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A83")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_2_A4B")

    label("loc_A83")

    Return()

    # Function_2_A4B end

    def Function_3_A84(): pass

    label("Function_3_A84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B33")
    SetChrPos(0x0, 0, 0, 21840, 180)
    SetChrPos(0x1, 0, 0, 21840, 180)
    SetChrPos(0x2, 0, 0, 21840, 180)
    SetChrPos(0x3, 0, 0, 21840, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0B")
    SetChrPos(0x4, 0, 0, 21840, 180)
    SetChrPos(0x5, 0, 0, 21840, 180)
    Jump("loc_B2A")

    label("loc_B0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2A")
    SetChrPos(0x4, 0, 0, 21840, 180)

    label("loc_B2A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B33")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B48")
    SetScenarioFlags(0x53, 7)

    label("loc_B48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5C")
    Event(0, 55)

    label("loc_B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B70")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 36)
    Jump("loc_BA7")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_B84")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 43)
    Jump("loc_BA7")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_B98")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 44)
    Jump("loc_BA7")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_BA7")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 53)

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BDE")
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x8, 3030, 0, -8220, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD9")
    ClearChrFlags(0xC, 0x80)

    label("loc_BD9")

    Jump("loc_D65")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BF6")
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_D65")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C0E")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_D65")

    label("loc_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_C26")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_D65")

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C43")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    Jump("loc_D65")

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C6D")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_C68")
    ClearChrFlags(0x2D, 0x80)

    label("loc_C68")

    Jump("loc_D65")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_C8F")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x8, 0x80)
    Jump("loc_D65")

    label("loc_C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CAC")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_D65")

    label("loc_CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_CDF")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x8, 1990, 0, -10980, 180)
    Jump("loc_D65")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CF2")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_D65")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D0A")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_D65")

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D22")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_D65")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D44")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    Jump("loc_D65")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_D52")
    Jump("loc_D65")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_D65")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_D65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D87")
    OP_C7(0x1, 0x1000)

    label("loc_D87")

    Return()

    # Function_3_A84 end

    def Function_4_D88(): pass

    label("Function_4_D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD7")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD7")

    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD7")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD7")

    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF2")
    ClearMapObjFlags(0x0, 0x10)
    Jump("loc_DF6")

    label("loc_DF2")

    OP_65(0x0, 0x1)

    label("loc_DF6")

    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E0A")
    Jump("loc_E53")

    label("loc_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_E31")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_E53")

    label("loc_E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E53")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)

    label("loc_E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E94")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_EF5")

    label("loc_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_ED0")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_EF5")

    label("loc_ED0")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_EF5")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F09")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F09")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F21")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F34")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F47")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5A")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6D")
    OP_1B(0x3, 0x0, 0x39)

    label("loc_F6D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA9")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FB7")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_FB7")

    OP_78(0xD, 0x2C)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FCF")
    Jump("loc_100F")

    label("loc_FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_100F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_100F")
    ClearMapObjFlags(0xD, 0x4)
    SetChrPos(0x2C, 2250, 0, 12500, 180)
    OP_D3(0x2C, 0x0, 0x2BF20, 0x0, 0x0)

    label("loc_100F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_101E")
    SetScenarioFlags(0xD3, 0)

    label("loc_101E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103A")
    Jump("loc_103F")

    label("loc_103A")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_103F")

    Return()

    # Function_4_D88 end

    def Function_5_1040(): pass

    label("Function_5_1040")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")

    #C0001
    ChrTalk(
        0xFE,
        (
            "啊～！！\x01",
            "总算收到货物啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "哎，都这么晚了啊！\x01",
            "再不抓紧的话，今天可就送不完了……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E9")

    label("loc_10BA")


    #C0003
    ChrTalk(
        0xFE,
        (
            "没空胡思乱想了啊……\x01",
            "总之得赶紧去送货了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E9")

    Jump("loc_189B")

    label("loc_10EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_116C")

    #C0004
    ChrTalk(
        0xFE,
        "车站现在似乎处于戒严状态啊。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "不光是客车，\x01",
            "货物列车的安检好像也推迟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "哎呀呀……\x01",
            "真是伤脑筋啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1219")

    #C0007
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "和平时一样，\x01",
            "我正在等待列车运来的货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "嗯，基本上\x01",
            "我也已经习惯\x01",
            "很晚才能拿到货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "只有学会享受这段等待的时光，\x01",
            "才称得上是职业人士啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1266")

    #C0010
    ChrTalk(
        0xFE,
        (
            "今天很难得，一早就\x01",
            "拿到货物了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "好～赶快去送货吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_1266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_12E1")

    #C0012
    ChrTalk(
        0xFE,
        (
            "虽然纪念庆典结束了，\x01",
            "可还是这么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "物流业的工作者\x01",
            "真是没有假日啊……\x01",
            "老板真是找了个辛苦的买卖。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12EF")
    Jump("loc_189B")

    label("loc_12EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12FD")
    Jump("loc_189B")

    label("loc_12FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_145C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C6")

    #C0014
    ChrTalk(
        0xFE,
        (
            "总算把货物\x01",
            "都搬进来了，\x01",
            "……真够累人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "唉，明天还要去贝尔加德门卸货啊，\x01",
            "这可真不是人干的活啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "难得开通了货物列车专线，\x01",
            "要是能把我这些货一起运过去该多好啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1457")

    label("loc_13C6")


    #C0017
    ChrTalk(
        0xFE,
        (
            "警备队员都在执勤地点住宿，\x01",
            "所以他们的家人经常会托我们\x01",
            "送些慰问品过去……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "难得开通了货物列车专线，\x01",
            "要是能把我这些货一起运过去该多好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1457")

    Jump("loc_189B")

    label("loc_145C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14FB")

    #C0019
    ChrTalk(
        0xFE,
        (
            "停在那边的，\x01",
            "是我们公司用的\x01",
            "搬运车。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "要送过去的货物\x01",
            "好像有很多，\x01",
            "所以开了车出来……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……难道要我一个人搬进车里吗？\x01",
            "麻烦死啦～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1571")

    #C0022
    ChrTalk(
        0xFE,
        (
            "从外国运来的货物\x01",
            "经常会延迟到达。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "可送货晚了的话，\x01",
            "我就会被老爸训斥。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "唉～真叫人着急啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_1571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_166D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1607")

    #C0025
    ChrTalk(
        0xFE,
        (
            "从共和国送来的\x01",
            "货物刚刚到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "收件地址是……\x01",
            "呃，是矿山镇玛因兹吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "唉～再不赶快送去的话，\x01",
            "天都要黑了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1668")

    label("loc_1607")


    #C0028
    ChrTalk(
        0xFE,
        (
            "要去矿山镇玛因兹，\x01",
            "就必须要走那条\x01",
            "狭窄的山道……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "唉～再不赶快送去的话，\x01",
            "天都要黑了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1668")

    Jump("loc_189B")

    label("loc_166D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_16EC")

    #C0030
    ChrTalk(
        0xFE,
        (
            "今天应该有从共和国\x01",
            "发来的货物。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "今天我来早了点……\x01",
            "货物好像还没运来。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……嗯～真不该\x01",
            "这么认真的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_16EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1779")

    #C0033
    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "总算收到货物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "不赶快送到收件人那里的话，\x01",
            "又要被老爸教训啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "真是的，要是不满意的话，\x01",
            "就自己去送啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189B")

    label("loc_1779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_189B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_181E")

    #C0036
    ChrTalk(
        0xFE,
        (
            "我们是私人运营的运输公司，\x01",
            "叫做『莱姆斯运输』。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "负责把外国发来的货物\x01",
            "配送给市民们。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "我来领取\x01",
            "运到车站来的货物……\x01",
            "好慢啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_189B")

    label("loc_181E")


    #C0039
    ChrTalk(
        0xFE,
        (
            "我们是私人运营的运输公司，\x01",
            "叫做『莱姆斯运输』。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "我来领取\x01",
            "运到车站来的货物……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "送得这么迟，\x01",
            "可叫人怎么干活啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189B")

    TalkEnd(0xFE)
    Return()

    # Function_5_1040 end

    def Function_6_189F(): pass

    label("Function_6_189F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_192C")

    #C0042
    ChrTalk(
        0xFE,
        (
            "听别人说，空港和车站\x01",
            "都有警备人员驻守，\x01",
            "大概在严查危险物品吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "到底是什么人啊！\x01",
            "竟敢让我心爱的列车们\x01",
            "身陷险境……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2574")

    label("loc_192C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_19E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B1")

    #C0044
    ChrTalk(
        0xFE,
        (
            "真是太过分了……\x01",
            "感觉今天经过的列车好像少了点。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "……不，好像是所有列车的发车时间\x01",
            "都推迟了……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19E2")

    label("loc_19B1")


    #C0046
    ChrTalk(
        0xFE,
        (
            "列车发车延迟的状况\x01",
            "如此频发，可真奇怪啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E2")

    Jump("loc_2574")

    label("loc_19E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACA")

    #C0047
    ChrTalk(
        0xFE,
        (
            "虽然我对开发出各种列车的\x01",
            "帝国文化表示敬意……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "但帝国的兵器，比如『列车炮』之类的东西，\x01",
            "我绝对不能接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "因为，所谓的列车……是满载着乘客和货物，\x01",
            "以及像我这种列车迷的\x01",
            "梦想的交通工具……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B4D")

    label("loc_1ACA")


    #C0050
    ChrTalk(
        0xFE,
        (
            "对于帝国的『列车炮』之类的东西，\x01",
            "我实在是没有好感啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "列车可不是战斗的工具。\x01",
            "而是满载乘客与货物，\x01",
            "以及梦想的交通工具……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B4D")

    Jump("loc_2574")

    label("loc_1B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C01")

    #C0052
    ChrTalk(
        0xFE,
        (
            "我现在非常非常想要\x01",
            "一部导力相机啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "……你问为什么，\x01",
            "当然是为了拍列车的照片啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "只不过，那终究不是\x01",
            "平民可以轻易买下的\x01",
            "廉价商品啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C7D")

    label("loc_1C01")


    #C0055
    ChrTalk(
        0xFE,
        (
            "虽然我也曾尝试过\x01",
            "去克洛斯贝尔时代周刊社\x01",
            "应聘摄影师的职位……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "不过，他们当然\x01",
            "不会录用我这种\x01",
            "只想拍铁道照片的人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7D")

    Jump("loc_2574")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1CE8")

    #C0057
    ChrTalk(
        0xFE,
        (
            "纪念庆典结束了，铁路列车的运行列数\x01",
            "也恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "……唉……\x01",
            "感觉有点寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2574")

    label("loc_1CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1D67")

    #C0059
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典时，\x01",
            "会有许多游客乘坐列车\x01",
            "来这里吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "……哈哈，我要将列车的英姿\x01",
            "一个不漏地尽收眼底。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2574")

    label("loc_1D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE7")

    #C0061
    ChrTalk(
        0xFE,
        (
            "听说帝国有些富裕的\x01",
            "收藏家，还会收集\x01",
            "铁道模型。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "真叫人羡慕啊……！\x01",
            "为什么我不是贵族出身呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E63")

    label("loc_1DE7")


    #C0063
    ChrTalk(
        0xFE,
        (
            "铁道模型几乎都是\x01",
            "职业工匠手工制作的，\x01",
            "所以价格非常高昂。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "如果以后发了大财，\x01",
            "我就想每天欣赏着铁道模型\x01",
            "安享晚年啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E63")

    Jump("loc_2574")

    label("loc_1E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1EFB")

    #C0065
    ChrTalk(
        0xFE,
        (
            "要说临近纪念庆典有什么值得高兴的事，\x01",
            "那就是列车要大显身手啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "从列车里涌出的人群\x01",
            "仿佛群虫出巢一般，\x01",
            "这景象真是震撼人心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2574")

    label("loc_1EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_206B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD5")

    #C0067
    ChrTalk(
        0xFE,
        (
            "横贯大陆的铁路轨道，\x01",
            "是耗时数年，一点一点\x01",
            "铺设而成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "那么长的铁轨，要小心铺设，\x01",
            "避免列车运行时发生事故，\x01",
            "肯定是相当困难的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "这正是前人种树后人凉。\x01",
            "我真是太崇敬各位施工者了\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2066")

    label("loc_1FD5")


    #C0070
    ChrTalk(
        0xFE,
        (
            "横贯大陆的铁路轨道，在铺设长度\x01",
            "惊人的同时还要保持施工精准，\x01",
            "这是需要花费漫长年月的。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "这正是前人种树后人凉。\x01",
            "我真是太崇敬各位施工者了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2066")

    Jump("loc_2574")

    label("loc_206B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2100")

    #C0072
    ChrTalk(
        0xFE,
        (
            "为什么大家\x01",
            "都没发觉铁道的魅力呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "那些与克洛斯贝尔的发展史密不可分的\x01",
            "贸易产业，可都是靠这种重要的\x01",
            "交通工具支撑起来的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2574")

    label("loc_2100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B6")

    #C0074
    ChrTalk(
        0xFE,
        (
            "我小时候，\x01",
            "一直憧憬着能当上列车驾驶员。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "不过有一天，我突然发现了。\x01",
            "我真正的爱好其实是\x01",
            "『疼爱』列车……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "如今，我已经是个名副其实的铁道迷了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_221C")

    label("loc_21B6")


    #C0077
    ChrTalk(
        0xFE,
        "我的爱好是疼爱列车。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "小时候虽然想当驾驶员……\x01",
            "至于现在的话，相比之下\x01",
            "倒是更想当车站站员了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221C")

    Jump("loc_2574")

    label("loc_2221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2298")

    #C0079
    ChrTalk(
        0xFE,
        (
            "横贯大陆铁道，\x01",
            "大约是在二十年前开通的。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "现在，只要坐一趟列车\x01",
            "就能抵达大陆东端了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2314")

    label("loc_2298")


    #C0081
    ChrTalk(
        0xFE,
        (
            "现在，只要坐一趟列车\x01",
            "就能抵达大陆东端了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "虽然是花钱又费时的漫长旅途……\x01",
            "但作为列车爱好者，总有一天要试试看呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2314")

    Jump("loc_2574")

    label("loc_2319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2475")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2406")

    #C0083
    ChrTalk(
        0xFE,
        "飞船、列车、导力车……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "那么庞大的东西\x01",
            "竟能在天上自由飞翔，\x01",
            "或在地上飞速驰骋。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "在如今虽是司空见惯的技术，\x01",
            "但仔细想想的话，还真是很了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "这真让人感到浪漫啊，\x01",
            "你们能够理解我的这种心情吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2470")

    label("loc_2406")


    #C0087
    ChrTalk(
        0xFE,
        "飞船、列车、导力车……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "我的嗜好虽然更偏向于铁道，\x01",
            "但觉得交通工具有浪漫感的人\x01",
            "应该也为数不少呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2470")

    Jump("loc_2574")

    label("loc_2475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250B")

    #C0089
    ChrTalk(
        0xFE,
        "你们是要去车站吗？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "根据我的情报网……\x01",
            "开往共和国的列车\x01",
            "差不多快到达了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "现在这个时间段\x01",
            "十分拥挤，要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2574")

    label("loc_250B")


    #C0092
    ChrTalk(
        0xFE,
        (
            "我想，开往共和国的列车\x01",
            "应该差不多快到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "嗯～若不是有急事的话，\x01",
            "还真想听听\x01",
            "发车时的汽笛声呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2574")

    TalkEnd(0xFE)
    Return()

    # Function_6_189F end

    def Function_7_2578(): pass

    label("Function_7_2578")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_25F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2596")
    Call(0, 9)
    Jump("loc_25EE")

    label("loc_2596")


    #C0094
    ChrTalk(
        0xFE,
        (
            "真是的，莱缇娜\x01",
            "总是对一些琐事发牢骚……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……呵呵，算了。\x01",
            "真期待快点到家啊～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25EE")

    Jump("loc_26D9")

    label("loc_25F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2683")

    #C0096
    ChrTalk(
        0xFE,
        "呼，总算能喘口气了。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "七耀石的产地克洛斯贝尔……\x01",
            "呵呵，真是激动人心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "目标是七耀石的结晶……\x01",
            "我一定要弄到手！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26D9")

    label("loc_2683")


    #C0099
    ChrTalk(
        0xFE,
        (
            "目标是七耀石的结晶……\x01",
            "我一定要弄到手！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "哦，在此之前……\x01",
            "先要找旅馆才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D9")

    TalkEnd(0xFE)
    Return()

    # Function_7_2578 end

    def Function_8_26DD(): pass

    label("Function_8_26DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_276F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FB")
    Call(0, 9)
    Jump("loc_276A")

    label("loc_26FB")


    #C0101
    ChrTalk(
        0xFE,
        (
            "呜呜……好郁闷。\x01",
            "回到家以后，不知会被骂成什么样……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊。\x01",
            "求您保佑我不要\x01",
            "受到严厉的惩罚……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_276A")

    Jump("loc_2843")

    label("loc_276F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2813")

    #C0103
    ChrTalk(
        0xFE,
        (
            "我和大小姐是从埃雷波尼亚帝国\x01",
            "来这里采购七耀石的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "不过也有一半的原因是离家出走。\x01",
            "家里现在必定已经乱成一团了……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "……心情好沉重……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2843")

    label("loc_2813")


    #C0106
    ChrTalk(
        0xFE,
        (
            "结果竟然\x01",
            "跑到这种地方来……\x01",
            "心情真沉重……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2843")

    TalkEnd(0xFE)
    Return()

    # Function_8_26DD end

    def Function_9_2847(): pass

    label("Function_9_2847")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0107
    ChrTalk(
        0xA,
        (
            "作为目标的七耀石的结晶\x01",
            "也弄到手了……\x01",
            "终于可以回帝国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "这么大的红耀石……\x01",
            "我的脑海里已经浮现出父亲那大吃一惊的表情了！\x01",
            "呵呵呵！\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "从家里拿了一大笔钱，\x01",
            "离家出走将近四个月……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "突然回去的话，\x01",
            "家里人当然会大吃一惊吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        "……你好烦呀，笨女仆！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        "呜……好过分……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_9_2847 end

    def Function_10_298A(): pass

    label("Function_10_298A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADD")

    #C0113
    ChrTalk(
        0xFE,
        (
            "我……还是追着\x01",
            "大小姐来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "因为……我还是\x01",
            "放心不下她呀……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2A68")

    #C0115
    ChrTalk(
        0x101,
        "#0005F咦，这位女仆……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#0105F记得是坎贝尔议员家的……\x02\x03",

            "#0106F感、感觉她好像\x01",
            "一副心事重重的表情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD2")

    label("loc_2A68")


    #C0117
    ChrTalk(
        0x101,
        "#0005F咦，这位女仆是……？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#0105F好像是在某座\x01",
            "大宅里工作呢……\x02\x03",

            "（好像在哪里\x01",
            "　见到过似的……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD2")

    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0xEF, 5)
    Jump("loc_2B15")

    label("loc_2ADD")


    #C0119
    ChrTalk(
        0xFE,
        (
            "老爷，对不起……\x01",
            "但是，我还是要\x01",
            "去大小姐身边……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B15")

    TalkEnd(0xFE)
    Return()

    # Function_10_298A end

    def Function_11_2B19(): pass

    label("Function_11_2B19")

    TalkBegin(0xFE)

    #C0120
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔车站……\x01",
            "是这里没错吧，好。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "城市太大，有点迷路了呢。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_2B19 end

    def Function_12_2B69(): pass

    label("Function_12_2B69")

    TalkBegin(0xFE)

    #C0122
    ChrTalk(
        0xFE,
        (
            "老公，赶快走吧。\x01",
            "再不快点，列车就要开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "回程要是耽误了，\x01",
            "那可都是你的错哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2B69 end

    def Function_13_2BC8(): pass

    label("Function_13_2BC8")

    TalkBegin(0xFE)

    #C0124
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市里，\x01",
            "稀奇的东西可真不少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "哎呀呀，真令人兴奋不已呀。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2BC8 end

    def Function_14_2C1C(): pass

    label("Function_14_2C1C")

    TalkBegin(0xFE)

    #C0126
    ChrTalk(
        0xFE,
        (
            "哎，老头子你真是的，\x01",
            "像小孩子一样两眼放光。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "好了，镇定一点吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_2C1C end

    def Function_15_2C6C(): pass

    label("Function_15_2C6C")

    TalkBegin(0xFE)

    #C0128
    ChrTalk(
        0xFE,
        (
            "我正要往市外走呢，\x01",
            "就被过路的人阻止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "嗯～要观光的话，\x01",
            "还是老老实实\x01",
            "坐巴士比较好啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2C6C end

    def Function_16_2CD4(): pass

    label("Function_16_2CD4")

    TalkBegin(0xFE)

    #C0130
    ChrTalk(
        0xFE,
        (
            "我十分能理解\x01",
            "想去市外\x01",
            "逛逛的心情。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "这里都是高层建筑，\x01",
            "对于在乡下长大的人来说，真是太压抑啦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_2CD4 end

    def Function_17_2D42(): pass

    label("Function_17_2D42")

    TalkBegin(0xFE)

    #C0132
    ChrTalk(
        0xFE,
        (
            "嗯，市中心在……\x01",
            "哎呀，不就在车站边上吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "呼，还好\x01",
            "买了地图啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2D42 end

    def Function_18_2D93(): pass

    label("Function_18_2D93")

    TalkBegin(0xFE)

    #C0134
    ChrTalk(
        0xFE,
        (
            "在列车上一路摇晃……\x01",
            "感觉有点不舒服。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "呜呕……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2D93 end

    def Function_19_2DD3(): pass

    label("Function_19_2DD3")

    TalkBegin(0xFE)

    #C0136
    ChrTalk(
        0xFE,
        (
            "唉，老公你真是的，\x01",
            "总是很容易就晕车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "你这个样子，\x01",
            "还怎么去别处\x01",
            "观光呀？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2DD3 end

    def Function_20_2E2F(): pass

    label("Function_20_2E2F")

    TalkBegin(0xFE)

    #C0138
    ChrTalk(
        0xFE,
        (
            "下个月会有纪念庆典吧？\x01",
            "我本来是想等到那时候再来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "不过，我不太喜欢拥挤的地方，\x01",
            "还是趁人少的时候好好享受一下吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2E2F end

    def Function_21_2EB4(): pass

    label("Function_21_2EB4")

    TalkBegin(0xFE)

    #C0140
    ChrTalk(
        0xFE,
        (
            "唉～为什么选在\x01",
            "这种淡季过来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "在热闹的人群中\x01",
            "旅行才有乐趣啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2EB4 end

    def Function_22_2F07(): pass

    label("Function_22_2F07")

    TalkBegin(0xFE)

    #C0142
    ChrTalk(
        0xFE,
        (
            "我是因公来ＩＢＣ大厦\x01",
            "办事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "还是先找人\x01",
            "问个路吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2F07 end

    def Function_23_2F4C(): pass

    label("Function_23_2F4C")

    TalkBegin(0xFE)

    #C0144
    ChrTalk(
        0xFE,
        "部长！我陪您去！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2F4C end

    def Function_24_2F69(): pass

    label("Function_24_2F69")

    TalkBegin(0xFE)

    #C0145
    ChrTalk(
        0xFE,
        "纪念庆典过后的克洛斯贝尔……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "正是因为庆典刚过，\x01",
            "才有做生意的机会！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "难道你不这么想吗！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2F69 end

    def Function_25_2FD5(): pass

    label("Function_25_2FD5")

    TalkBegin(0xFE)

    #C0148
    ChrTalk(
        0xFE,
        (
            "老师！\x01",
            "既然决定了，就去检查\x01",
            "要采购的商品吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_2FD5 end

    def Function_26_300E(): pass

    label("Function_26_300E")

    TalkBegin(0xFE)

    #C0149
    ChrTalk(
        0xFE,
        "天色完全暗下来了啊。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "希望旅馆还有空房……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_300E end

    def Function_27_3049(): pass

    label("Function_27_3049")

    TalkBegin(0xFE)

    #C0151
    ChrTalk(
        0xFE,
        (
            "毕竟，\x01",
            "长途旅行都把我饿坏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "真想找个地方吃饭啊～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_3049 end

    def Function_28_308D(): pass

    label("Function_28_308D")

    TalkBegin(0xFE)

    #C0153
    ChrTalk(
        0xFE,
        "我们是从帝国私奔而来的。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "在这里的话，父亲就找不到了。\x01",
            "我们两人一定能幸福的……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_308D end

    def Function_29_30EF(): pass

    label("Function_29_30EF")

    TalkBegin(0xFE)

    #C0155
    ChrTalk(
        0xFE,
        (
            "若不是爱上身份卑微的我，\x01",
            "她也就不会和父亲失和了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "我真是罪孽深重的男人啊……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "可是……只要看到她那幸福的表情，\x01",
            "这种阴郁的心情\x01",
            "也就烟消云散了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_30EF end

    def Function_30_3193(): pass

    label("Function_30_3193")

    TalkBegin(0xFE)

    #C0158
    ChrTalk(
        0xFE,
        (
            "安检官的检查\x01",
            "相当仔细呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "说是要检查危险物品什么的……\x01",
            "真是令人不安啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_3193 end

    def Function_31_31EC(): pass

    label("Function_31_31EC")

    TalkBegin(0xFE)

    #C0160
    ChrTalk(
        0xFE,
        (
            "车站月台里弥漫着一股莫名的紧张气氛，\x01",
            "搞得人心惶惶的。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "到底出了什么事呢……？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_31EC end

    def Function_32_324A(): pass

    label("Function_32_324A")

    TalkBegin(0xFE)

    #C0162
    ChrTalk(
        0xFE,
        (
            "都到了月台，\x01",
            "还让人等了将近一小时，\x01",
            "真是累死人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔这地方\x01",
            "原来这么重视警备吗？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_324A end

    def Function_33_32B4(): pass

    label("Function_33_32B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_33E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_336B")

    #C0164
    ChrTalk(
        0x2D,
        (
            "遗憾的是，\x01",
            "特制苦西红柿奶昔平时\x01",
            "一般没法出售呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x2D,
        (
            "因为原材料很难进货，\x01",
            "而且基本卖不出去……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x2D,
        (
            "现在店里的一点点原料\x01",
            "完全是为市长先生准备的哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DD")

    label("loc_336B")


    #C0167
    ChrTalk(
        0x2D,
        (
            "啊，饮料已经\x01",
            "交给市长先生了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#0000F嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x153,
        "#1109F谢谢您了～！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x2D,
        "哪里哪里，不客气。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_33DD")

    Jump("loc_345B")

    label("loc_33E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3458")

    #C0171
    ChrTalk(
        0x2D,
        (
            "请把那杯奶昔\x01",
            "送给市长先生，聊表慰问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x2D,
        (
            "市长先生是我的老主顾，\x01",
            "一直承蒙他关照呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345B")

    label("loc_3458")

    Call(0, 34)

    label("loc_345B")

    TalkEnd(0xFE)
    Return()

    # Function_33_32B4 end

    def Function_34_345F(): pass

    label("Function_34_345F")

    EventBegin(0x0)
    Fade(500)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(-530, 1300, 12810, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17490, 0)
    SetChrPos(0x101, -700, 0, 13150, 90)
    SetChrPos(0x153, -850, 0, 11920, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E6")
    SetChrPos(0x102, -960, 0, 14520, 135)
    Jump("loc_352D")

    label("loc_34E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_350C")
    SetChrPos(0x103, -960, 0, 14520, 135)
    Jump("loc_352D")

    label("loc_350C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_352D")
    SetChrPos(0x104, -960, 0, 14520, 135)

    label("loc_352D")

    OP_93(0x2D, 0x10E, 0x0)
    SetChrSubChip(0x2D, 0x0)
    OP_0D()

    #C0173
    ChrTalk(
        0x2D,
        "#11P欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x2D,
        (
            "#11P要不要喝杯\x01",
            "可口的饮料呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x153,
        "#12P#1110F啊～是卖果汁的～\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#6P#0000F您就是平时在喷泉广场附近\x01",
            "营业的那位店主吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x2D,
        (
            "#11P啊，是的。\x01",
            "但偶尔也会来这边\x01",
            "做做生意……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x2D,
        (
            "#11P真令人高兴啊～\x01",
            "莫非是特地过来买\x01",
            "喜爱的果汁吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3668")

    #C0179
    ChrTalk(
        0x102,
        "#6P#0102F是的，其实……\x02",
    )

    CloseMessageWindow()
    Jump("loc_36C7")

    label("loc_3668")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_369A")

    #C0180
    ChrTalk(
        0x103,
        "#6P#0200F不，其实是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_36C7")

    label("loc_369A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36C7")

    #C0181
    ChrTalk(
        0x104,
        "#6P#0300F不，其实呢……\x02",
    )

    CloseMessageWindow()

    label("loc_36C7")

    SetChrName("")

    #A0182
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向对方说明了来意，\x01",
            "并要求购买市长平时爱喝的饮料。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x2D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0183
    ChrTalk(
        0x2D,
        (
            "#11P原来如此，是来买给市长先生的\x01",
            "慰问品啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x2D,
        (
            "#11P这样的话，请稍等一下。\x01",
            "我马上为你们做出来！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadEffect(0x0, "battle\\it002_00.eff")
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0185
    ChrTalk(
        0x2D,
        "#11P给，就是这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0186
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('ＺＷＥＩ２企鹅', 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3859")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_38AE")

    label("loc_3859")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3886")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_38AE")

    label("loc_3886")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38AE")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_38AE")

    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#6P#0005F这、这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_390D")

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#0105F外公的确是\x01",
            "很喜欢苦的东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399C")

    label("loc_390D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3960")

    #C0189
    ChrTalk(
        0x103,
        (
            "#6P#0206F……光是想象一下，\x01",
            "就觉得嘴里有股苦味弥漫开来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399C")

    label("loc_3960")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_399C")

    #C0190
    ChrTalk(
        0x104,
        (
            "#6P#0306F真厉害……\x01",
            "不愧是市长先生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399C")


    #C0191
    ChrTalk(
        0x2D,
        (
            "#11P这种奶昔对缓解疲劳很有效果，\x01",
            "可是因为太苦了，\x01",
            "所以只能作为特别定制的饮料来卖呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x2D,
        (
            "#11P……正好我多做了一点，\x01",
            "各位要不要喝喝看呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#6P#0011F呜……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "喝喝看\x01",        # 0
            "婉言谢绝\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4596")

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#0012F那、那么，\x01",
            "就尝一点点……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B49")

    #C0195
    ChrTalk(
        0x102,
        (
            "#6P#0106F呜呜……\x01",
            "（既然是外公喜欢的饮料，\x01",
            "  总该了解一下才是……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和艾莉\x01",
            "拿起特制苦西红柿奶昔，\x01",
            "战战兢兢地喝了下去──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3C55")

    label("loc_3B49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BC4")

    #C0197
    ChrTalk(
        0x103,
        "#6P#0206F……真的要喝吗？\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和缇欧\x01",
            "拿起特制苦西红柿奶昔，\x01",
            "战战兢兢地喝了下去──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3C55")

    label("loc_3BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C55")

    #C0199
    ChrTalk(
        0x104,
        (
            "#6P#0306F唉，真是没办法。\x01",
            "我也要下定决心试一下吗……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和兰迪\x01",
            "拿起特制苦西红柿奶昔，\x01",
            "战战兢兢地喝了下去──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3C55")

    Sound(887, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CD6")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3D91")

    label("loc_3CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D36")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3D91")

    label("loc_3D36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D91")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3D91")

    Sleep(1000)
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "无与伦比的苦味饮料\x01",
            "顺着喉咙滑了下去……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x0, 0x0, 0x101, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(228, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E51")
    PlayEffect(0x0, 0x1, 0x102, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3EE4")

    label("loc_3E51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E9D")
    PlayEffect(0x0, 0x1, 0x103, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3EE4")

    label("loc_3E9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EE4")
    PlayEffect(0x0, 0x1, 0x104, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_3EE4")

    OP_89(0x0, 0x0)
    OP_89(0x1, 0x0)
    SetChrName("")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人的ＣＰ上升了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0x0, 0x5, 0xC8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2E")
    OP_32(0x1, 0x5, 0xC8)
    Jump("loc_3F5D")

    label("loc_3F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F48")
    OP_32(0x2, 0x5, 0xC8)
    Jump("loc_3F5D")

    label("loc_3F48")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F5D")
    OP_32(0x3, 0x5, 0xC8)

    label("loc_3F5D")


    #C0203
    ChrTalk(
        0x101,
        (
            "#6P#0010F咳、咳……！\x02\x03",

            "#0006F好、好像的确对身体\x01",
            "很有益处……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FFC")

    #C0204
    ChrTalk(
        0x102,
        (
            "#6P#0110F不、不过，这苦味……\x01",
            "对第一次喝的人来说，真是太强烈了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4078")

    label("loc_3FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4034")

    #C0205
    ChrTalk(
        0x103,
        "#6P#0208F苦、苦得难以形容……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4078")

    label("loc_4034")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4078")

    #C0206
    ChrTalk(
        0x104,
        (
            "#6P#0310F还、还真是够要命啊……\x01",
            "怎么这么苦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4078")


    #C0207
    ChrTalk(
        0x2D,
        "#11P啊哈哈，说得是呢～\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x153,
        "#12P#1111F嗯～……\x02",
    )

    CloseMessageWindow()
    OP_93(0x153, 0x5A, 0x1F4)
    OP_96(0x153, 0x2BC, 0x0, 0x2E90, 0x3E8, 0x0)
    Sleep(500)
    OP_93(0x153, 0x0, 0x1F4)
    SetChrName("")

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅拿起剩下的\x01",
            "苦西红柿奶昔，\x01",
            "把吸管放入口中。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4129():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4129)

    def lambda_4136():
        TurnDirection(0x2D, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4136)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4172")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_41D5")

    label("loc_4172")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41A6")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_41D5")

    label("loc_41A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41D5")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0x153, 500)

    label("loc_41D5")

    Sleep(1000)

    #C0210
    ChrTalk(
        0x101,
        "#6P#0011F等、等一下……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4229")

    #C0211
    ChrTalk(
        0x102,
        "#6P#0105F小、小琪雅！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4284")

    label("loc_4229")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4259")

    #C0212
    ChrTalk(
        0x103,
        "#6P#0205F琪雅……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4284")

    label("loc_4259")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4284")

    #C0213
    ChrTalk(
        0x104,
        "#6P#0305F喂，阿琪！？\x02",
    )

    CloseMessageWindow()

    label("loc_4284")


    #C0214
    ChrTalk(
        0x153,
        (
            "#12P#1103F（吸吸）……\x02\x03",

            "#1100F（咽下）……\x02\x03",

            "#1109F呼哇～！\x01",
            "好好喝哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4316")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_436B")

    label("loc_4316")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4343")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_436B")

    label("loc_4343")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_436B")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_436B")

    Sleep(1000)

    #C0215
    ChrTalk(
        0x101,
        "#6P#0011F全、全都喝掉了啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43C7")

    #C0216
    ChrTalk(
        0x102,
        "#6P#0105F小、小琪雅好厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4431")

    label("loc_43C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43FF")

    #C0217
    ChrTalk(
        0x103,
        "#6P#0205F琪雅，你太厉害了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4431")

    label("loc_43FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4431")

    #C0218
    ChrTalk(
        0x104,
        (
            "#6P#0302F阿琪……\x01",
            "你好强啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4431")

    TurnDirection(0x153, 0x101, 500)

    #C0219
    ChrTalk(
        0x153,
        (
            "#12P#1101F哎～为什么～？\x02\x03",

            "#1100F虽然有一点点苦，\x01",
            "但是很好喝呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#0006F呃，琪雅你觉得\x01",
            "好喝就好……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x2D,
        (
            "#11P啊哈哈……\x01",
            "好有趣的小姑娘啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44D3():
        TurnDirection(0x101, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44D3)

    def lambda_44E0():
        TurnDirection(0x153, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_44E0)

    def lambda_44ED():
        TurnDirection(0x2D, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_44ED)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4511")
    TurnDirection(0x102, 0x2D, 500)
    Jump("loc_4544")

    label("loc_4511")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_452D")
    TurnDirection(0x103, 0x2D, 500)
    Jump("loc_4544")

    label("loc_452D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4544")
    TurnDirection(0x104, 0x2D, 500)

    label("loc_4544")


    #C0222
    ChrTalk(
        0x101,
        (
            "#6P#0000F总、总之，\x01",
            "真是多谢您了。\x02\x03",

            "算上我们喝掉的，\x01",
            "总共多少钱？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x26, 0x1, 0x3)
    Jump("loc_470C")

    label("loc_4596")


    #C0223
    ChrTalk(
        0x101,
        (
            "#6P#0006F不，好意还是\x01",
            "心领了……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x153,
        (
            "#12P#1105F哎～为什么～？\x02\x03",

            "#1107F琪雅想喝\x01",
            "苦西红柿汁嘛～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_464F")

    #C0225
    ChrTalk(
        0x102,
        (
            "#6P#0102F啊哈哈……\x01",
            "小琪雅喝这种东西\x01",
            "似乎还早了一点吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E4")

    label("loc_464F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4698")

    #C0226
    ChrTalk(
        0x103,
        (
            "#6P#0200F我认为，琪雅喝这个\x01",
            "似乎还太早了点……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E4")

    label("loc_4698")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46E4")

    #C0227
    ChrTalk(
        0x104,
        (
            "#6P#0300F还是算了吧，阿琪。\x01",
            "会喝得一嘴苦味，很难受的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E4")


    #C0228
    ChrTalk(
        0x101,
        (
            "#6P#0000F对了，\x01",
            "要多少钱呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x26, 0x1, 0x4)

    label("loc_470C")


    #C0229
    ChrTalk(
        0x2D,
        (
            "#11P不用不用，今天就\x01",
            "特别算你们免费吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x2D,
        (
            "#11P市长先生是我的老主顾，\x01",
            "一直都承蒙他关照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x2D,
        (
            "#11P请把这杯奶昔\x01",
            "送给市长先生，聊表慰问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#6P#0005F但、但是……\x02\x03",

            "#0000F……明白了，\x01",
            "那我们就不客气地收下啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4834")

    #C0233
    ChrTalk(
        0x102,
        (
            "#6P#0102F呵呵……\x01",
            "我们会把您的心意也转达给市长的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48BB")

    label("loc_4834")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4878")

    #C0234
    ChrTalk(
        0x103,
        "#6P#0202F我们会把您的心意也转达给市长的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_48BB")

    label("loc_4878")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48BB")

    #C0235
    ChrTalk(
        0x104,
        "#6P#0302F我们一定会把您的心意转达给市长先生。\x02",
    )

    CloseMessageWindow()

    label("loc_48BB")

    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x0, -700, 0, 13150, 90)
    EventEnd(0x5)
    Return()

    # Function_34_345F end

    def Function_35_48D9(): pass

    label("Function_35_48D9")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 0)), scpexpr(EXPR_END)), "loc_49E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BD(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BD(0x3, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BD(0x2, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BD(0x1, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4902")
    Jump("loc_49E1")

    label("loc_4902")


    #C0236
    ChrTalk(
        0x103,
        (
            "#0203F……还没给所有人的战术导力器\x01",
            "镶嵌好结晶回路。\x02\x03",

            "#0200F进入里面之前，先准备妥当吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请为全体成员的战术导力器镶嵌结晶回路。\x02\x03",

            "在主菜单中打开［ORBMENT］项目，\x01",
            "选择［QUARTZ］，即可镶嵌结晶回路。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_49E1")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02\x03",

            "使用地下空间Ａ区域的钥匙\x01",
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
        1,
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
        (0, "loc_4A7D"),
        (1, "loc_4AB9"),
        (SWITCH_DEFAULT, "loc_4ABE"),
    )


    label("loc_4A7D")

    Sound(809, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    #A0239
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
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x46, 0)
    OP_C7(0x1, 0x80000)
    Jump("loc_4ABE")

    label("loc_4AB9")

    Jump("loc_4ABE")

    label("loc_4ABE")

    EventEnd(0x3)
    Return()

    # Function_35_48D9 end

    def Function_36_4AC1(): pass

    label("Function_36_4AC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch20900.itc", 0x1F)
    LoadChrToIndex("chr/ch21400.itc", 0x20)
    LoadChrToIndex("apl/ch50003.itc", 0x21)
    OP_68(4200, 3100, -1900, 0)
    MoveCamera(90, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 10000, 500, -1900, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x24, 10000, 500, -2800, 270)
    SetChrPos(0x25, 10000, 500, -1000, 270)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x40)
    SetChrChipByIndex(0x29, 0xF)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x8)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x20)
    SetChrSubChip(0x2B, 0x0)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x2A, 900, 0, -8000, 0)
    SetChrPos(0x29, 4600, 0, 3300, 45)
    SetChrPos(0x2B, -4100, 0, -700, 315)
    SetChrPos(0x9, -1100, 0, 11000, 180)
    OP_E5()
    FadeToBright(1000, 0)
    OP_0D()
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)

    def lambda_4C55():
        OP_95(0xFE, 900, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_4C55)

    def lambda_4C6F():
        OP_95(0xFE, -1100, 0, -40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C6F)
    OP_68(1200, 1100, -1900, 6000)
    MoveCamera(90, 12, 0, 6000)
    SetCameraDistance(22000, 6000)
    BeginChrThread(0x101, 3, 0, 37)
    Sleep(800)
    BeginChrThread(0x24, 3, 0, 39)
    Sleep(500)
    BeginChrThread(0x25, 3, 0, 41)
    Sleep(2000)
    Sound(101, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Sleep(2000)
    Fade(1000)
    OP_68(1200, 1100, -1900, 0)
    MoveCamera(48, 14, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24000, 0)
    MoveCamera(42, 14, 0, 8000)
    SetCameraDistance(30000, 8000)
    OP_0D()
    PlaceName2(100, 200, "c_plac01", 0x0, 2000)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(400)
    BeginChrThread(0x24, 3, 0, 40)
    Sleep(1100)
    BeginChrThread(0x25, 3, 0, 42)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(-700, 700, 12800, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    SetChrPos(0x101, -700, 0, 10000, 0)
    SetChrPos(0x24, -1000, 0, 7800, 0)
    SetChrPos(0x25, 0, 0, 7400, 0)

    def lambda_4DEB():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DEB)

    def lambda_4E05():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4E05)

    def lambda_4E1F():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4E1F)
    OP_68(1400, 2700, 17000, 8000)
    MoveCamera(41, 5, 0, 8000)
    SetCameraDistance(19500, 8000)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    OP_E6()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_4AC1 end

    def Function_37_4E79(): pass

    label("Function_37_4E79")


    def lambda_4E7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E7E)

    def lambda_4E8F():
        OP_95(0xFE, 600, 0, -1900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E8F)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x3E8)
    Return()

    # Function_37_4E79 end

    def Function_38_4EB3(): pass

    label("Function_38_4EB3")


    def lambda_4EB8():
        OP_95(0xFE, -200, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EB8)
    WaitChrThread(0x101, 1)

    def lambda_4ED6():
        OP_95(0xFE, -200, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4ED6)
    WaitChrThread(0x101, 1)
    Return()

    # Function_38_4EB3 end

    def Function_39_4EF0(): pass

    label("Function_39_4EF0")


    def lambda_4EF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4EF5)

    def lambda_4F06():
        OP_95(0xFE, 1800, 0, -2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4F06)
    WaitChrThread(0x24, 1)
    Sleep(500)

    def lambda_4F27():

        label("loc_4F27")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4F27")

    QueueWorkItem2(0xFE, 2, lambda_4F27)
    Return()

    # Function_39_4EF0 end

    def Function_40_4F35(): pass

    label("Function_40_4F35")

    EndChrThread(0x24, 0x2)

    def lambda_4F3E():
        OP_95(0xFE, -600, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4F3E)
    WaitChrThread(0x24, 1)

    def lambda_4F5C():
        OP_95(0xFE, -600, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4F5C)
    WaitChrThread(0x24, 1)
    Return()

    # Function_40_4F35 end

    def Function_41_4F76(): pass

    label("Function_41_4F76")


    def lambda_4F7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_4F7B)

    def lambda_4F8C():
        OP_95(0xFE, 2000, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4F8C)
    WaitChrThread(0x25, 1)
    Sleep(300)

    def lambda_4FAD():

        label("loc_4FAD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4FAD")

    QueueWorkItem2(0xFE, 2, lambda_4FAD)
    Return()

    # Function_41_4F76 end

    def Function_42_4FBB(): pass

    label("Function_42_4FBB")

    EndChrThread(0x25, 0x2)

    def lambda_4FC4():
        OP_95(0xFE, 400, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4FC4)
    WaitChrThread(0x25, 1)

    def lambda_4FE2():
        OP_95(0xFE, 400, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4FE2)
    WaitChrThread(0x25, 1)
    Return()

    # Function_42_4FBB end

    def Function_43_4FFC(): pass

    label("Function_43_4FFC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    OP_68(-500, 3000, 18800, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x23, -500, 0, 22000, 180)
    SetChrPos(0x101, -1300, 0, 25000, 180)
    SetChrPos(0x102, 300, 0, 25000, 180)
    SetChrPos(0x103, -1300, 0, 26600, 180)
    SetChrPos(0x104, 300, 0, 26600, 180)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis001.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis002.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis003.itp")
    CreatePortrait(3, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis004.itp")

    def lambda_517E():
        OP_95(0xFE, -500, 0, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_517E)
    Sleep(500)

    def lambda_519B():
        OP_95(0xFE, -1300, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_519B)
    Sleep(50)

    def lambda_51B8():
        OP_95(0xFE, 300, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51B8)
    Sleep(50)

    def lambda_51D5():
        OP_95(0xFE, -1300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_51D5)
    Sleep(50)

    def lambda_51F2():
        OP_95(0xFE, 300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_51F2)
    OP_68(-500, 1000, 18800, 4000)
    FadeToBright(2000, 0)
    WaitChrThread(0x23, 1)

    def lambda_522A():
        OP_95(0xFE, -8500, -2800, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_522A)
    WaitChrThread(0x101, 1)

    def lambda_5248():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5248)
    WaitChrThread(0x102, 1)

    def lambda_5259():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5259)
    WaitChrThread(0x104, 1)

    def lambda_526A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_526A)
    WaitChrThread(0x103, 1)

    def lambda_527B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_527B)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)

    #C0240
    ChrTalk(
        0x101,
        "#12P#0005F这里是……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#12P#0105F站前街道的角落……\x01",
            "到底有什么东西呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        (
            "#11P#0306F说是善后……\x02\x03",

            "#0301F该不会是要我们来\x01",
            "收拾建材什么的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        "#5P#0200F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x23, 1)
    Fade(1000)
    OP_68(-15500, -3900, 17500, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x23, -10500, -4000, 17500, 270)
    SetChrPos(0x101, -8500, -2300, 17000, 270)
    SetChrPos(0x102, -7540, -1800, 16100, 270)
    SetChrPos(0x103, -6900, -1500, 17800, 270)
    SetChrPos(0x104, -5900, -1300, 16700, 270)
    OP_68(-22500, -3900, 17500, 6000)
    MoveCamera(38, 16, 0, 6000)
    SetCameraDistance(17000, 6000)

    def lambda_53FF():
        OP_95(0x23, -19500, -5000, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_53FF)
    Sleep(300)

    def lambda_541C():
        OP_95(0x101, -22500, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_541C)
    Sleep(50)

    def lambda_5439():
        OP_95(0x102, -21540, -5000, 16100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5439)
    Sleep(50)

    def lambda_5456():
        OP_95(0x103, -20900, -5000, 17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5456)
    Sleep(50)

    def lambda_5473():
        OP_95(0x104, -19900, -5000, 16700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5473)
    WaitChrThread(0x23, 1)

    def lambda_5491():
        OP_95(0xFE, -22500, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5491)
    WaitChrThread(0x23, 1)
    OP_93(0x23, 0x0, 0x2BC)
    WaitChrThread(0x101, 1)

    def lambda_54BA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54BA)
    WaitChrThread(0x102, 1)

    def lambda_54CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54CB)
    WaitChrThread(0x103, 1)

    def lambda_54DC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54DC)
    WaitChrThread(0x104, 1)

    def lambda_54ED():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54ED)
    OP_93(0x23, 0xB4, 0x1F4)

    def lambda_5501():

        label("loc_5501")

        TurnDirection(0x101, 0x23, 500)
        Yield()
        Jump("loc_5501")

    QueueWorkItem2(0x101, 2, lambda_5501)

    def lambda_5513():

        label("loc_5513")

        TurnDirection(0x102, 0x23, 500)
        Yield()
        Jump("loc_5513")

    QueueWorkItem2(0x102, 2, lambda_5513)

    def lambda_5525():

        label("loc_5525")

        TurnDirection(0x103, 0x23, 500)
        Yield()
        Jump("loc_5525")

    QueueWorkItem2(0x103, 2, lambda_5525)

    def lambda_5537():

        label("loc_5537")

        TurnDirection(0x104, 0x23, 500)
        Yield()
        Jump("loc_5537")

    QueueWorkItem2(0x104, 2, lambda_5537)
    OP_6F(0x51)

    #C0244
    ChrTalk(
        0x23,
        (
            "#5P#1003F──这扇门的后面，\x01",
            "就是克洛斯贝尔市地下广阔的\x01",
            "『地下空间区域』。\x02\x03",

            "#1000F接下来，你们要潜入到里面去。\x02",
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
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0245
    ChrTalk(
        0x101,
        "#12P#0005F哎！？\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        "#12P#0105F潜、潜入……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x104,
        (
            "#11P#0301F喂喂，\x01",
            "这是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x23,
        (
            "#5P#1004F这是为了测试你们的\x01",
            "综合能力以及实战技巧。\x02\x03",

            "#1002F地下空间内部\x01",
            "徘徊着一些不算\x01",
            "太难对付的魔兽。\x02\x03",

            "你们要一路消灭掉这些魔兽，\x01",
            "前进到最深处去。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        "#12P#0100F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#11P#0304F实战测试吗……\x01",
            "哈，这样一说我反而轻松了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#0011F请、请等一下！\x02\x03",

            "#0003F测试暂且不提……\x01",
            "但为什么要特地进入\x01",
            "有魔兽徘徊的地方呢？\x02\x03",

            "#0001F我们又不是警备队……\x01",
            "这应该不是搜查官的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x23,
        (
            "#5P#1004F哼哼，这的确不是\x01",
            "普通搜查官的工作。\x02\x03",

            "#1001F──不过，如果是特别任务支援科的\x01",
            "所属成员，那就另当别论了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x23,
        (
            "#5P#1000F──详情之后再说。\x02\x03",

            "先收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x23, -22500, -5000, 18000, 2000, 0x0)
    Sleep(300)
    SetChrName("")

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔盖将类似便携式终端的东西\x01",
            "交给了罗伊德等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A0256
    AnonymousTalk(
        0x101,
        "#0005F这个是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0257
    AnonymousTalk(
        0x102,
        "#0105F新型的战术导力器？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0258
    AnonymousTalk(
        0x104,
        (
            "#0305F嘿……\x01",
            "款式还真时髦啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0259
    AnonymousTalk(
        0x103,
        (
            "#0203F第５代战术导力器，\x01",
            "通称『艾尼格玛（ＥＮＩＧＭＡ）』……\x02\x03",

            "#0200F终于用于实战配备了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    TurnDirection(0x23, 0x103, 250)
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis005.itp")

    #C0260
    ChrTalk(
        0x23,
        (
            "#6P#1002F嗯，这是财团的人在\x01",
            "前些日子刚送来的新品。\x02\x03",

            "已经根据你们各自的特性\x01",
            "而进行了调整。\x02\x03",

            "#1004F至于使用方法──缇欧，\x01",
            "由你来给他们讲解一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#11P#0203F……好吧，虽然很麻烦。\x02\x03",

            "#0200F有用于新型导力器的结晶回路吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x23,
        "#6P#1002F嗯，虽然不多……给，收下吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0263
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "各种结晶回路\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TurnDirection(0x23, 0x101, 500)

    #C0264
    ChrTalk(
        0x23,
        "#5P#1000F还有，这才是最关键的东西。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x321),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('伊梅尔达馆的钥匙', 1)

    #C0266
    ChrTalk(
        0x23,
        (
            "#5P#1003F那么，把魔兽都\x01",
            "清理完之后，就回总部来吧。\x02\x03",

            "其它细节问题到时再谈。\x02\x03",

            "#1005F对了──顺便\x01",
            "把这个也给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※关于『调查手册』。\x02\x03",

            "※『调查手册』会自动\x01",
            "  记录游戏中发生的\x01",
            "  各种事件。\x02\x03",

            "※在主菜单中打开［ITEMS］菜单\x01",
            "  在其中使用『调查手册』，\x01",
            "  或在大地图上按下『△键＋左方向键』，  \x01",
            "  即可查阅其内容。\x02\x03",

            "※各类资料与指南也可在手册中查阅，\x01",
            "  请多加运用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(828, 0, 100, 0)

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※关于『战斗手册』。\x02\x03",

            "※『战斗手册』会自动\x01",
            "  记录曾经交战过的\x01",
            "  敌人情报。\x02\x03",

            "※同调查手册一样，\x01",
            "  使用道具栏中的『战斗手册』，\x01",
            "  或直接按下『△键＋右方向键』，  \x01",
            "  即可查阅其内容。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('调查手册', 1)
    AddItemNumber('战斗手册', 1)
    OP_68(-19500, -3900, 17500, 3000)

    def lambda_5F2B():
        OP_95(0xFE, -20000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5F2B)
    WaitChrThread(0x23, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5F5B():
        OP_95(0xFE, -17500, -5000, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5F5B)
    #Sound(1082, 255, 100, 0)    #voice#Lloyd

    #C0271
    ChrTalk(
        0x101,
        "#6P#0011F请、请等等，科长！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 1)
    OP_6F(0x1)
    TurnDirection(0x23, 0x101, 500)

    #C0272
    ChrTalk(
        0x23,
        (
            "#11P#1002F──啊，对了，罗伊德。\x02\x03",

            "暂且由你来当队长吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x23,
        (
            "#11P#1004F目前拥有正式\x01",
            "搜查官资格的人\x01",
            "可只有你哦。\x02\x03",

            "所以就交给你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x5A, 0x1F4)

    def lambda_604D():
        OP_95(0xFE, -8500, -2800, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_604D)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitChrThread(0x23, 1)
    Fade(1000)
    OP_68(-21200, -3900, 17300, 0)
    MoveCamera(335, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrPos(0x101, -22500, -5000, 17300, 90)
    SetChrPos(0x102, -20900, -5000, 16000, 90)
    SetChrPos(0x103, -21500, -5000, 18600, 90)
    SetChrPos(0x104, -19900, -5000, 17300, 90)
    SetChrFlags(0x23, 0x80)
    OP_0D()

    def lambda_6113():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6113)
    Sleep(50)

    def lambda_6123():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6123)
    Sleep(50)

    def lambda_6133():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6133)
    WaitChrThread(0x103, 1)
    #Sound(1362, 255, 100, 0)    #voice#Randy

    #C0275
    ChrTalk(
        0x104,
        (
            "#12P#0309F哈哈哈，\x01",
            "你被派了个苦差事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#12P#0104F呵呵，不过，有个拥有搜查官资格的\x01",
            "人在队里，可就令人安心多了。\x02\x03",

            "#0102F罗伊德先生，\x01",
            "还请多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0277
    ChrTalk(
        0x101,
        (
            "#0000F#5P啊……\x01",
            "不用客气，直接叫我的名字就好啦。\x02\x03",

            "看起来，我们的年龄应该也很相近。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#12P#0100F是吗？\x01",
            "顺带一提，我十八岁……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#0000F#5P啊，那跟我同龄啊。\x02\x03",

            "#0005F那你们呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#12P#0304F我二十一岁，\x01",
            "但也不必对我使用死板的敬语。\x02\x03",

            "#0300F多关照啦，罗伊德、艾莉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0281
    ChrTalk(
        0x102,
        "#6P#0102F嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        "#0002F#5P嗯，请多关照了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#0001F……嗯……\x01",
            "那，你呢……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6380():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6380)
    Sleep(50)

    def lambda_6390():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6390)
    WaitChrThread(0x102, 1)

    #C0284
    ChrTalk(
        0x103,
        "#11P#0203F──十四岁，有问题吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0285
    ChrTalk(
        0x101,
        (
            "#6P#0012F没、没有啦～\x01",
            "怎么会有问题……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(1081, 255, 100, 0)    #voice#Lloyd

    #C0286
    ChrTalk(
        0x101,
        "#6P#0011F呃，#4S十四岁！？#3S\x02",
    )

    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        (
            "#12P#0309F哈哈，怎么了，\x01",
            "跟外表看起来一样小嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        (
            "#6P#0105F真令人惊讶……这么年轻\x01",
            "也能当警察啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#6P#0011F不不！\x01",
            "怎么想也都不对劲吧！\x02\x03",

            "#0006F我记得，普通警察的入职年龄\x01",
            "也被限制在十六岁以上……\x02\x03",

            "#0001F连主日学校都还没毕业的孩子，\x01",
            "怎么可能当警察──\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        (
            "#11P#0200F……确切地说，\x01",
            "我并不是警察。\x02\x03",

            "而是爱普斯泰恩财团派来的\x01",
            "测试人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x101,
        "#6P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        (
            "#12P#0305F说到爱普斯泰恩，\x01",
            "不就是刚才那个战术导力器的……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#6P#0104F是吗……原来如此。\x02\x03",

            "#0100F我听说，最近数年来，克洛斯贝尔市\x01",
            "与财团合作，正在推行某些\x01",
            "大规模的计划……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0294
    ChrTalk(
        0x103,
        (
            "#5P#0200F是指『导力网络计划』吧。\x02\x03",

            "和那个也略有一点关系，\x01",
            "但这次财团派我来是另有目的的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -21500, -5000, 18800, 180)
    OP_0D()
    Sound(1268, 255, 100, 0)    #voice#Tio
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    Sleep(1000)

    #A0295
    AnonymousTalk(
        0x101,
        "#0005F那个是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0296
    AnonymousTalk(
        0x102,
        "#0105F装设了机械装置的……手杖？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0297
    AnonymousTalk(
        0x103,
        (
            "#0204F这个叫做『魔导杖』。\x02\x03",

            "为了对这种新武器进行实战测试，\x01",
            "财团才把我派来的。\x02\x03",

            "#0200F……罗伊德前辈，\x01",
            "你可以理解了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0298
    ChrTalk(
        0x101,
        (
            "#6P#0001F等、等一下！\x02\x03",

            "难道说……\x01",
            "你要使用这把手杖参与战斗吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#11P#0203F……你明明拥有搜查官资格，\x01",
            "但理解能力却令人不敢恭维呢。\x02\x03",

            "#0211F刚才都已经说过了，我是来进行\x01",
            "『实战』测试的啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#6P#0011F呜……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        (
            "#12P#0304F好啦好啦，\x01",
            "在这里争论也无济于事啊。\x02\x03",

            "#0300F虽然还不知道这扇门后面的\x01",
            "地下空间到底有多危险……\x02\x03",

            "不过，现在还是优先考虑\x01",
            "如何才能完成那个大叔\x01",
            "硬塞给我们的任务吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        (
            "#6P#0103F是啊……\x01",
            "虽然还有很多事情没想通。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#6P#0006F………明白了。\x02\x03",

            "#0000F抱歉，缇欧。\x01",
            "如果害你不高兴的话，我在此道歉。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x103, -21500, -5000, 18600, 180)
    TurnDirection(0x103, 0x101, 0)
    OP_0D()
    Sleep(300)

    #C0304
    ChrTalk(
        0x103,
        (
            "#11P#0203F没什么……我认为\x01",
            "你的反应是正常人应有的。\x02\x03",

            "#0200F话说回来，我的武器\x01",
            "是这把『魔导杖』……\x02\x03",

            "各位的武器都是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#6P#0005F嗯，那么──\x02\x03",

            "#0000F我的武器，是这个。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -22700, -5000, 17300, 90)
    OP_0D()

    def lambda_6B91():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B91)
    Sleep(50)

    def lambda_6BA1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6BA1)
    Sleep(50)

    def lambda_6BB1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BB1)
    WaitChrThread(0x102, 1)
    Sound(1083, 255, 100, 0)    #voice#Lloyd
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(1000)

    #A0306
    AnonymousTalk(
        0x102,
        "#0105F这个，是警棍的一种……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0307
    AnonymousTalk(
        0x104,
        (
            "#0300F『旋棍』啊，\x01",
            "是东方式的武器呢。\x02\x03",

            "听说，相对于杀伤力而言，\x01",
            "防御力与压制力更为优秀……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0308
    AnonymousTalk(
        0x102,
        (
            "#0102F原来如此，\x01",
            "很有警官风格的装备呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x101, -22500, -5000, 17300, 90)
    OP_0D()
    Sleep(300)

    #C0309
    ChrTalk(
        0x101,
        (
            "#0004F#5P我也试过很多武器，\x01",
            "但还是这个最称手啊。\x02\x03",

            "#0000F那，艾莉和兰迪的武器呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#12P#0100F我的……是这个。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    OP_93(0x102, 0x0, 0x0)
    OP_0D()

    def lambda_6D8A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D8A)
    Sleep(50)

    def lambda_6D9A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6D9A)
    Sleep(50)

    def lambda_6DAA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DAA)
    WaitChrThread(0x103, 1)
    Sound(1173, 255, 100, 0)    #voice#Elie
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    Sleep(1000)

    #A0311
    AnonymousTalk(
        0x103,
        (
            "#0205F导力枪……\x01",
            "款式有点旧呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0312
    AnonymousTalk(
        0x101,
        "#0005F好漂亮的枪啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0313
    AnonymousTalk(
        0x102,
        (
            "#0102F针对竞技性而专门\x01",
            "进行过特殊调整哦。\x02\x03",

            "虽然是旧式，但瞄准的精确性\x01",
            "应该还是值得期待的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0314
    ChrTalk(
        0x104,
        (
            "#11P#0302F哦，信心十足嘛。\x02\x03",

            "#0300F那么，我的是这家伙。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -19500, -5000, 17300, 270)
    OP_0D()

    def lambda_6F32():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F32)
    Sleep(50)

    def lambda_6F42():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F42)
    Sleep(50)

    def lambda_6F52():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F52)
    WaitChrThread(0x102, 1)
    Sound(1363, 255, 100, 0)    #voice#Randy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(1000)

    #A0315
    AnonymousTalk(
        0x101,
        (
            "#0001F那个是……\x01",
            "相当巨大的武器啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0316
    AnonymousTalk(
        0x102,
        (
            "#0101F形状很像是中世纪的骑士\x01",
            "所使用的『斧枪』啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0317
    AnonymousTalk(
        0x103,
        (
            "#0200F……我在财团的武器工房中\x01",
            "见过这个。\x02\x03",

            "上面装设了可以将导力\x01",
            "转化成冲击力的元件吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0318
    AnonymousTalk(
        0x104,
        (
            "#0304F嗯，这是冲击斧枪。\x02\x03",

            "#0300F虽然重了点，导致操作不便，\x01",
            "不过攻击的威力可是非常了得哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    SetChrPos(0x104, -19900, -5000, 17300, 270)
    OP_0D()
    Sleep(300)

    #C0319
    ChrTalk(
        0x101,
        (
            "#0003F#5P原来如此……\x02\x03",

            "#0000F虽然还不清楚缇欧的魔导杖\x01",
            "具体是什么原理……\x02\x03",

            "但要和魔兽作战的话，\x01",
            "这种阵容应该还算是平衡吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7188():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7188)
    Sleep(50)

    def lambda_7198():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7198)
    WaitChrThread(0x103, 1)

    #C0320
    ChrTalk(
        0x102,
        "#12P#0100F的确……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#12P#0300F嗯，说不定正是连这一点也考虑到了，\x01",
            "所以才会把我们几个召集起来的吧。\x02\x03",

            "那位大叔看起来没精打采的，\x01",
            "其实可不是等闲之辈啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#11P#0203F……是啊。\x02\x03",

            "#0200F关于这把魔导杖的性能，\x01",
            "以后再慢慢说明……\x02\x03",

            "要先对刚才配发给我们的\x01",
            "战术导力器的性能\x01",
            "进行一下说明吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "请缇欧说明一下\x01",      # 0
            "还是算了\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7319"),
        (1, "loc_7C43"),
        (SWITCH_DEFAULT, "loc_7EA3"),
    )


    label("loc_7319")


    def lambda_731E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_731E)
    Sleep(50)

    def lambda_732E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_732E)
    Sleep(50)

    def lambda_733E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_733E)
    Sleep(50)

    #C0323
    ChrTalk(
        0x101,
        "#0002F#5P嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#11P#0203F……明白了。\x02\x03",

            "#0200F一般来说，所谓的『导力器』，\x01",
            "是指利用导力能源\x01",
            "而引发各种现象的机械。\x02\x03",

            "从照明和制冷制暖设备等日用品，\x01",
            "到车辆与铁路的动力，\x01",
            "全都使用了导力器的能量。\x02\x03",

            "而所谓的『战术导力器』，\x01",
            "则是专门针对个人战斗而进行了\x01",
            "特殊处理的小型便携式导力器。\x02\x03",

            "#0203F这次发配给我们的，\x01",
            "是由『爱普斯泰恩财团』开发的\x01",
            "最新型战术导力器。\x02\x03",

            "和以前的型号一样，\x01",
            "它需要镶嵌被通称为『回路』的\x01",
            "结晶回路来进行运作。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        (
            "#6P#0105F结晶回路……\x01",
            "就是用七耀石碎片制作而成的\x01",
            "导力器专用回路吧。\x02\x03",

            "#0100F科长刚才好像\x01",
            "给了我们几个……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        (
            "#11P#0200F嗯，只要把它嵌入\x01",
            "战术导力器中已开封过的\x01",
            "结晶孔内，就能发挥作用了。\x02\x03",

            "另外，镶嵌有结晶回路的结晶链\x01",
            "都有『属性值』，当其达到一定程度时，\x01",
            "就可以使用导力魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#5P#0004F针对魔兽的种类，\x01",
            "有时候，与其用武器直接攻击，\x01",
            "不如使用魔法更为有效。\x02\x03",

            "#0000F所以，在和魔兽进行战斗之前，\x01",
            "一定要事先\x01",
            "准备好才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#6P#0100F原来如此……\x01",
            "这么说，在与魔兽战斗中，\x01",
            "这也是十分重要的一环呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        (
            "#12P#0304F毕竟连游击士协会\x01",
            "和警备队都将其投入使用了嘛。\x01",
            "这么想肯定没错啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x103,
        (
            "#11P#0208F还有……对了。\x02\x03",

            "#0200F战术导力器依照个人的特性进行过调整，\x01",
            "因此，根据所有者的不同，\x01",
            "导力器的构造也会存在差异。\x02\x03",

            "例如，某些结晶孔会有属性限制，\x01",
            "或是连接结晶孔的结晶链形态有所不同。\x02\x03",

            "#0203F总之，至于具体的区别，\x01",
            "只要稍后自行比较一下就知道了。\x02\x03",

            "#0200F关于导力魔法的具体使用方法，\x01",
            "还是在实战中自行摸索为好……\x01",
            "说明就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#6P#0102F多亏你的解释，我已经非常明白了。\x01",
            "谢谢啦，缇欧。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#11P#0203F……不客气。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        (
            "#12P#0305F话说，虽然是新型，\x01",
            "但使用方法好像和\x01",
            "以前的没什么区别啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x103,
        (
            "#11P#0203F嗯，如果有过使用旧型号的经验，\x01",
            "只需按照之前的感觉操作即可。\x02\x03",

            "#0200F要说区别的话，\x01",
            "主要就在于这次的升级版\x01",
            "增加了其它功能……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0335
    ChrTalk(
        0x101,
        "#5P#0005F……其它功能？\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        (
            "#11P#0204F不过，目前应该还用不上，\x01",
            "所以请不必在意。\x02\x03",

            "#0200F现在还是优先\x01",
            "完成此次任务吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，也对。\x01",
            "（……稍微有些在意呢……）\x02\x03",

            "#0004F……总而言之，\x01",
            "在进入地下空间之前，\x01",
            "先调整好战术导力器吧。\x02\x03",

            "#0000F镶嵌好科长给的结晶回路，\x01",
            "然后再进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        "#12P#0100F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x104,
        "#12P#0300F那好，赶快做好准备吧。\x02",
    )

    CloseMessageWindow()
    AddItemNumber('ＨＰ１', 1)
    AddItemNumber('ＥＰ３', 1)
    AddItemNumber('攻击２', 1)
    AddItemNumber('魔防２', 1)
    FadeToDark(300, 0, 100)
    Sleep(300)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请为全体成员的战术导力器镶嵌结晶回路。\x02\x03",

            "在主菜单中打开［ORBMENT］选项，\x01",
            "再选择［QUARTZ］，即可进行结晶回路的设置。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x44, 0)
    OP_C7(0x0, 0x80000)
    Jump("loc_7EA3")

    label("loc_7C43")


    def lambda_7C48():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C48)
    Sleep(50)

    def lambda_7C58():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C58)
    Sleep(50)

    def lambda_7C68():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C68)
    Sleep(50)

    #C0341
    ChrTalk(
        0x101,
        (
            "#5P#0000F不……没问题的。\x02\x03",

            "看起来，使用方法\x01",
            "好像和以前的型号\x01",
            "没什么变化嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#11P#0203F嗯，那倒是。\x02\x03",

            "#0200F要说区别，\x01",
            "主要就在于这次的升级版\x01",
            "增加了其它功能……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0343
    ChrTalk(
        0x101,
        "#5P#0005F……其它功能？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x103,
        (
            "#11P#0204F不过，目前应该还用不上，\x01",
            "所以请不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#5P#0006F（……稍微有些在意呢……）\x02\x03",

            "#0000F那么……\x01",
            "总之，就先进去看看吧。\x02\x03",

            "首先还是要注意安全，\x01",
            "谨慎前进为好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x102,
        "#12P#0100F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x103,
        "#11P#0200F……明白了。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        "#12P#0300F那好，快进去吧。\x02",
    )

    CloseMessageWindow()
    OP_42(0x0, 0x6D, 0x0)
    OP_42(0x1, 0x79, 0x0)
    OP_42(0x2, 0x64, 0x0)
    OP_42(0x3, 0x6A, 0x0)
    Jump("loc_7EA3")

    label("loc_7EA3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0x1, 0x0, 0x3)
    RemoveCraft(0x1, 0xFFFF)
    OP_38(0x1, 0x80, 0x1)
    OP_42(0x1, 0x3FC, 0xFF)
    OP_42(0x1, 0x5DC, 0xFF)
    OP_42(0x1, 0x640, 0xFF)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xFF)
    SetChrChipPat(0x1, 0x6, 0xFF)
    OP_32(0x2, 0x0, 0x3)
    RemoveCraft(0x2, 0xFFFF)
    OP_38(0x2, 0x80, 0x1)
    OP_42(0x2, 0x410, 0xFF)
    OP_42(0x2, 0x5DC, 0xFF)
    OP_42(0x2, 0x640, 0xFF)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0x104)
    SetChrChipPat(0x2, 0x6, 0x104)
    OP_32(0x3, 0x0, 0x3)
    RemoveCraft(0x3, 0xFFFF)
    OP_38(0x3, 0x80, 0x1)
    OP_42(0x3, 0x424, 0xFF)
    OP_42(0x3, 0x5DC, 0xFF)
    OP_42(0x3, 0x640, 0xFF)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0x109)
    SetChrChipPat(0x3, 0x6, 0x109)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_68(-21000, -2800, 17500, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x0, -21000, -5000, 17500, 270)
    SetChrPos(0x1, -21000, -5000, 17500, 270)
    SetChrPos(0x2, -21000, -5000, 17500, 270)
    SetChrPos(0x3, -21000, -5000, 17500, 270)
    SetScenarioFlags(0x40, 2)
    OP_29(0x3C, 0x4, 0x2)
    OP_29(0x3C, 0x1, 0x0)
    OP_C5(0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DE(0x0, 0x0)"), scpexpr(EXPR_END)), "loc_8133")
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※由于收到了调查手册，\x01",
            "  因此获得了『新人搜查官』的成就。\x02\x03",

            "※同理，在游戏进行的过程中，\x01",
            "  只要满足了一定条件，\x01",
            "  就可以获得『成就』。\x02\x03",

            "※『成就』含有一定的点数，\x01",
            "  在游戏通关之后，\x01",
            "  可以使用这些点数来开启各种功能。\x02\x03",

            "※在主菜单中打开［SYSTEM］，\x01",
            "  选择［RECORD］，\x01",
            "  即可确认已获得的成就。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)

    label("loc_8133")

    EventEnd(0x5)
    Return()

    # Function_43_4FFC end

    def Function_44_8136(): pass

    label("Function_44_8136")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch02400.itc", 0x1F)
    LoadChrToIndex("apl/ch50010.itc", 0x20)
    LoadChrToIndex("apl/ch50011.itc", 0x21)
    SoundLoad(806)
    OP_68(-22500, -4100, 17300, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x102, -22000, -5000, 21000, 180)
    SetChrPos(0x101, -22000, -5000, 21000, 180)
    SetChrPos(0x103, -22000, -5000, 21000, 180)
    SetChrPos(0x104, -22000, -5000, 21000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x198, -17100, -5000, 19300, 135)
    SetChrPos(0x197, -18000, -5000, 19300, 135)

    def lambda_8222():

        label("loc_8222")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_8222")

    QueueWorkItem2(0x198, 2, lambda_8222)

    def lambda_8234():

        label("loc_8234")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_8234")

    QueueWorkItem2(0x197, 2, lambda_8234)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x1F)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    SetChrPos(0x26, -16000, -5000, 17300, 270)
    SetChrPos(0x27, -18000, -5000, 17300, 90)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFC, 0xC3, 0xB6, 0x28, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis001.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    CreatePortrait(2, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    LoadEffect(0x0, "event\\eva02_00.eff")
    ClearMapObjFlags(0x0, 0x10)
    BeginChrThread(0x26, 3, 0, 45)
    SetCameraDistance(19500, 2000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 49)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 50)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x10)

    #C0350
    ChrTalk(
        0x101,
        "#6P#0005F怎么……？\x02",
    )

    CloseMessageWindow()
    OP_68(-16500, -4100, 17300, 2000)
    SetCameraDistance(19000, 2000)
    OP_6F(0x1)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("女性")

    #A0351
    AnonymousTalk(
        0xFF,
        (
            "哎呀～亚里欧斯先生！\x01",
            "您又立了大功呢！\x02\x03",

            "在城市设施管理不善的情况下，\x01",
            "以高超的技艺，漂亮地\x01",
            "拯救了陷入危机的少年……！\x02\x03",

            "一定要在最新刊上\x01",
            "登一条特快消息！\x02",
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

    #C0352
    ChrTalk(
        0x198,
        (
            "#5P太棒了！\x01",
            "我们要上杂志了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x197,
        (
            "#1P但、但是，\x01",
            "这好像并不值得高兴……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x27,
        (
            "#6P#1403F……格蕾丝。\x01",
            "最好不要大肆宣传。\x02\x03",

            "#1400F虽然市内的管理确实存在问题，\x01",
            "但这两个孩子的行为也有一定责任。\x02\x03",

            "有失偏颇的报道，我可不敢苟同。\x02",
        )
    )

    CloseMessageWindow()

    #N0355
    NpcTalk(
        0x26,
        "女性",
        (
            "#11P#2109F哪里哪里，我纯粹就是在\x01",
            "迎合读者的喜好而已啦¤\x02\x03",

            "#2102F──而且，这次好像\x01",
            "还有有趣的嘉宾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#0001F#5P！？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x26, 0x3)
    OP_68(-20080, -4100, 17580, 2500)
    SetCameraDistance(19500, 2500)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_86A1():
        OP_96(0xFE, 0xFFFFB9B0, 0xFFFFEC78, 0x3E80, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_86A1)
    WaitChrThread(0x26, 1)

    def lambda_86BF():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x44C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_86BF)
    Sleep(500)

    def lambda_86DC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_86DC)
    WaitChrThread(0x26, 1)
    OP_6F(0x11)
    BeginChrThread(0x26, 3, 0, 46)

    #N0357
    NpcTalk(
        0x26,
        "女性",
        (
            "#11P#2104F肩负着克洛斯贝尔警察局未来的\x01",
            "『特别任务支援科』首次出动！\x02\x03",

            "然而，由于实力不足，\x01",
            "仍然如同往常一般，被游击士抢走了功劳！\x02\x03",

            "#2110F啊，这些年轻人们深切感受到了自己的不成熟，\x01",
            "而他们又能否通过等待在前方的\x01",
            "种种试炼呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#6P#0011F说、说什么呢……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x104,
        (
            "#6P#0301F（喂喂……\x01",
            "　到底是怎么回事？）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x103,
        (
            "#6P#0200F（好像是\x01",
            "　媒体的人……）\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        (
            "#6P#0106F（……看样子，\x01",
            "  似乎是《克洛斯贝尔时代周刊》的\x01",
            "  记者呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x27,
        (
            "#11P#1403F──我不赞成\x01",
            "过早对他们妄下定论。\x02\x03",

            "况且，最先解救了\x01",
            "两个孩子的也是他们。\x02\x03",

            "#1400F不过，似乎确实还不够成熟啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#6P#0001F！！\x02",
    )

    CloseMessageWindow()

    #N0364
    NpcTalk(
        0x26,
        "女性",
        (
            "#11P#2106F哎呀呀，果然是这么回事啊。\x02\x03",

            "#2100F好，我会在报道里好好描述一番的，\x01",
            "不过，你们不用太介意啦～\x02\x03",

            "#2109F就当做是姐姐对你们的声援，\x01",
            "今后也要多加努力哦。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x26, 0x3)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    #N0365
    NpcTalk(
        0x26,
        "女性",
        (
            "#6P#2110F──那么，亚里欧斯先生。\x01",
            "请让我做一次独家专访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x27,
        (
            "#11P#1403F关于这件事，\x01",
            "之前我已经拒绝过了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x5A, 0x1F4)
    EndChrThread(0x198, 0x2)
    EndChrThread(0x197, 0x2)

    def lambda_8A71():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8A71)

    def lambda_8A8B():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_8A8B)

    def lambda_8A98():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_8A98)
    Sleep(400)
    BeginChrThread(0x198, 3, 0, 51)
    Sleep(400)
    BeginChrThread(0x197, 3, 0, 52)
    Sleep(400)

    def lambda_8ABA():
        OP_97(0xFE, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_8ABA)
    Sleep(4000)
    OP_68(-22500, -4000, 17300, 2000)
    MoveCamera(40, 23, 0, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    OP_6F(0x1)
    WaitChrThread(0x27, 1)
    WaitChrThread(0x198, 3)
    WaitChrThread(0x197, 3)
    WaitChrThread(0x26, 1)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)

    #C0367
    ChrTalk(
        0x103,
        "#6P#0211F……刚才那算什么啊。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        (
            "#0301F#6P好像是打算\x01",
            "拿我们当小丑，让人看笑话呢……\x02\x03",

            "#0306F那位姐姐算是我喜欢的类型，\x01",
            "不过，性格好像有点奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x102,
        (
            "#0106F#6P唉……\x01",
            "问题并不在这里吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0370
    ChrTalk(
        0x102,
        "#0101F#5P那么，罗伊德，现在该怎么办？\x02",
    )

    CloseMessageWindow()

    def lambda_8C77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8C77)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0371
    ChrTalk(
        0x101,
        (
            "#11P#0005F啊……\x02\x03",

            "#0006F……赛尔盖科长交给我们的\x01",
            "课题也算是完成了……\x01",
            "先回警察局总部去吧。\x02\x03",

            "#0008F关于孩子们的事情，\x01",
            "也需要详细报告……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0372
    ChrTalk(
        0x101,
        "#11P#0011F这是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0373
    ChrTalk(
        0x101,
        (
            "#0005F#11P刚才发给我们的\x01",
            "战术导力器……\x02\x03",

            "#0001F莫非有通讯\x01",
            "联络吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        (
            "#0203F#6P嗯，看来是这样呢。\x02\x03",

            "#0200F按下那个红色按钮，\x01",
            "就能切换到通讯模式。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#0000F#11P哦，这个吗……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x2, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0376
    AnonymousTalk(
        0x101,
        (
            "#0001F喂……\x01",
            "我是罗伊德·班宁斯。\x02\x03",

            "是赛尔盖科长吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少女的声音")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官！\x02\x03",

            "那个，是我。\x01",
            "刚才在接待处见过面的──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0378
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊，是刚才的……\x02\x03",

            "#0000F嗯，请问有什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("接待小姐的声音")

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，是这样的……\x02\x03",

            "那个，能麻烦你们尽快\x01",
            "返回警察局总部吗？\x02\x03",

            "副局长好像找你们有事……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0380
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F副、副局长……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x0, 0x2, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    RemoveParty(0x96, 0x0)
    RemoveParty(0x97, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_8136 end

    def Function_45_904B(): pass

    label("Function_45_904B")

    Sleep(1000)

    label("loc_904E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9140")
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_9066():
        OP_96(0xFE, 0xFFFFC180, 0xFFFFEC78, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_9066)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_90D7():
        OP_96(0xFE, 0xFFFFC180, 0xFFFFEC78, 0x44C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_90D7)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_904E")

    label("loc_9140")

    Return()

    # Function_45_904B end

    def Function_46_9141(): pass

    label("Function_46_9141")

    Sleep(1000)

    label("loc_9144")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9236")
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_915C():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x4394, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_915C)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_91CD():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x45EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_91CD)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_9144")

    label("loc_9236")

    Return()

    # Function_46_9141 end

    def Function_47_9237(): pass

    label("Function_47_9237")


    def lambda_923C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_923C)

    def lambda_924D():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_924D)
    WaitChrThread(0x101, 1)

    def lambda_926B():
        OP_95(0xFE, -21700, -5000, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_926B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_47_9237 end

    def Function_48_928C(): pass

    label("Function_48_928C")


    def lambda_9291():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9291)

    def lambda_92A2():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92A2)
    WaitChrThread(0x102, 1)

    def lambda_92C0():
        OP_95(0xFE, -22500, -5000, 17700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92C0)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_48_928C end

    def Function_49_92E1(): pass

    label("Function_49_92E1")


    def lambda_92E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_92E6)

    def lambda_92F7():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92F7)
    WaitChrThread(0x103, 1)

    def lambda_9315():
        OP_95(0xFE, -23900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9315)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_49_92E1 end

    def Function_50_9336(): pass

    label("Function_50_9336")


    def lambda_933B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_933B)

    def lambda_934C():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_934C)
    WaitChrThread(0x104, 1)

    def lambda_936A():
        OP_95(0xFE, -22700, -5000, 19100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_936A)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_50_9336 end

    def Function_51_9397(): pass

    label("Function_51_9397")


    def lambda_939C():
        OP_95(0xFE, -16000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_939C)
    WaitChrThread(0xFE, 1)

    def lambda_93BA():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93BA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_51_9397 end

    def Function_52_93D4(): pass

    label("Function_52_93D4")


    def lambda_93D9():
        OP_95(0xFE, -16900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93D9)
    WaitChrThread(0xFE, 1)

    def lambda_93F7():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93F7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_93D4 end

    def Function_53_9411(): pass

    label("Function_53_9411")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28300.itc", 0x1E)
    LoadChrToIndex("chr/ch28400.itc", 0x1F)
    OP_68(10000, -2500, 2000, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(43000, 0)
    SetChrPos(0x101, -4500, -10300, -1900, 0)
    SetChrPos(0x102, -4500, -10300, -1900, 0)
    SetChrPos(0x103, -4500, -10300, -1900, 0)
    SetChrPos(0x104, -4500, -10300, -1900, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xB, 0x28)
    OP_49()
    SetChrPos(0x28, 40000, -11500, -11500, 0)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrPos(0x29, 5000, 0, 0, 180)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 5000, 0, -1800, 0)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2B, 0x10)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 0, 0, 22000, 180)
    SetChrFlags(0x2B, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -2400, 0, -8000, 270)
    SetChrFlags(0x9, 0x8000)
    BeginChrThread(0x9, 0, 0, 0)
    OP_11(0xF0, 0xF2, 0xFC, 0x14, 0x64, 0x0)
    OP_7D(0xC8, 0xDC, 0xE6, 0x0, 0x0)
    OP_11(0xF0, 0xF2, 0xFC, 0x1E, 0x6E, 0x1F40)
    OP_7D(0xDC, 0xF0, 0xFF, 0x0, 0x1F40)
    Sound(829, 0, 100, 0)
    OP_68(-5000, -2500, 2000, 10000)
    SetCameraDistance(48000, 10000)

    def lambda_95FA():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_95FA)
    FadeToBright(2000, 0)
    OP_0D()
    BeginChrThread(0x28, 3, 0, 54)
    Sleep(2000)
    Sound(451, 0, 100, 0)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x28, 3)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_9411 end

    def Function_54_9673(): pass

    label("Function_54_9673")


    def lambda_9678():
        OP_96(0xFE, 0xFFFEC780, 0xFFFFD314, 0xFFFFD314, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_9678)
    WaitChrThread(0x28, 1)
    Return()

    # Function_54_9673 end

    def Function_55_9692(): pass

    label("Function_55_9692")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-21900, -3900, 19000, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -21900, -5000, 22000, 180)
    SetChrPos(0x102, -21900, -5000, 22000, 180)
    SetChrPos(0x103, -21900, -5000, 22000, 180)
    SetChrPos(0x104, -21900, -5000, 22000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    SetCameraDistance(18000, 2000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_979D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_979D)

    def lambda_97AE():
        OP_96(0xFE, 0xFFFFA7B8, 0xFFFFEC78, 0x477C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97AE)
    Sleep(400)

    def lambda_97CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_97CB)

    def lambda_97DC():
        OP_96(0xFE, 0xFFFFACCC, 0xFFFFEC78, 0x477C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97DC)
    Sleep(400)

    def lambda_97F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_97F9)

    def lambda_980A():
        OP_96(0xFE, 0xFFFFA7B8, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_980A)
    Sleep(400)

    def lambda_9827():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9827)

    def lambda_9838():
        OP_96(0xFE, 0xFFFFACCC, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9838)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(1000)

    def lambda_9876():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9876)
    Sleep(50)

    def lambda_9886():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9886)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0381
    AnonymousTalk(
        0x101,
        (
            "#0005F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0382
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦～是我。\x02\x03",

            "情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0383
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F赛尔盖科长。\x02\x03",

            "#0000F嗯，刚刚打倒了\x01",
            "通缉中的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "很好，顺利就好。\x02\x03",

            "你们现在在哪里？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0385
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F嗯……\x01",
            "地下空间的出口附近。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0386
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "唔，那也不算\x01",
            "很远嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0387
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F哎……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──现在交给你们\x01",
            "一件紧急任务。\x02\x03",

            "将其它支援请求延后也没关系，\x01",
            "总之优先处理这个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0389
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F──明白！\x02\x03",

            "那么……\x01",
            "到底是什么任务！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位置是城市东南角的旧城区……\x01",
            "你们尽快赶往那边吧。\x02\x03",

            "有居民报警了。\x02\x03",

            "据说有两组危险的不良团伙\x01",
            "就要开始斗殴了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0391
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F哎……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0392
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赶快去阻止，要解决得干净利落。\x01",
            "──就这样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    Sleep(200)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0393
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0011F请、请等一下！\x02\x03",

            "阻止斗殴……\x01",
            "这也属于我们的工作吗──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sleep(200)

    #C0394
    ChrTalk(
        0x101,
        "#6P#0013F──怎么已经挂断了！\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        (
            "#0105F科长打来的？\x01",
            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x104,
        (
            "#0302F看这样子，\x01",
            "好像不是什么好事吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)

    #C0397
    ChrTalk(
        0x101,
        "#6P#0006F唉，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0398
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将赛尔盖交代的任务内容\x01",
            "简略做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0399
    ChrTalk(
        0x102,
        "#0101F旧城区的不良团伙……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_END)), "loc_9E78")

    #C0400
    ChrTalk(
        0x104,
        (
            "#0301F就是之前在旧城区见到的\x01",
            "那些危险的小鬼们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EE0")

    label("loc_9E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_END)), "loc_9EB5")

    #C0401
    ChrTalk(
        0x104,
        (
            "#0301F我们之前在旧城区\x01",
            "见到过那样的人吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EE0")

    label("loc_9EB5")


    #C0402
    ChrTalk(
        0x104,
        (
            "#0301F旧城区……\x01",
            "竟然还有那种地方吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE0")


    #C0403
    ChrTalk(
        0x103,
        (
            "#0203F#5P据数据库显示……\x02\x03",

            "#0200F的确有『剑蛇帮』和\x01",
            "『圣书会』这两个团伙\x01",
            "在旧城区拉帮结派。\x02\x03",

            "据说，斗殴之类的事情是家常便饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#6P#0005F在我离开城市这段期间，\x01",
            "竟然冒出了那种家伙吗……\x02\x03",

            "#0003F──也罢，不管怎么说，\x01",
            "我们赶快去旧城区看看吧。\x02\x03",

            "#0001F在发生小规模冲突之前，\x01",
            "必须想办法阻止他们才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        "#0101F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0C3")

    #C0406
    ChrTalk(
        0x104,
        (
            "#0305F对了，罗伊德。\x01",
            "旧城区在哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，到了东街之后往南走，\x01",
            "经过一道小桥就是了。\x02\x03",

            "总而言之，先去东街吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x104,
        "#0300F好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0EC")

    label("loc_A0C3")


    #C0409
    ChrTalk(
        0x104,
        (
            "#0300F那好，我们这就\x01",
            "前往旧城区吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0EC")

    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -21900, -5000, 18000, 180)
    SetScenarioFlags(0x41, 7)
    OP_29(0x3E, 0x4, 0x2)
    OP_29(0x3E, 0x1, 0x0)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_55_9692 end

    def Function_56_A11A(): pass

    label("Function_56_A11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A238")
    EventBegin(0x1)

    #C0410
    ChrTalk(
        0x101,
        (
            "#0000F这次的任务\x01",
            "姑且也算是实战测试……\x02\x03",

            "还是不要绕道了，\x01",
            "快点去地下空间的\x01",
            "深处看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B8")

    #C0411
    ChrTalk(
        0x102,
        "#0100F明白，专心执行任务吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A222")

    label("loc_A1B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F8")

    #C0412
    ChrTalk(
        0x103,
        (
            "#0200F说得也是。\x01",
            "集中精神来执行任务吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A222")

    label("loc_A1F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A222")

    #C0413
    ChrTalk(
        0x104,
        "#0300F嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()

    label("loc_A222")

    Sleep(50)
    SetChrPos(0x0, -13150, -5000, 17120, 270)
    EventEnd(0x4)

    label("loc_A238")

    Return()

    # Function_56_A11A end

    def Function_57_A239(): pass

    label("Function_57_A239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2DF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2A8")

    #C0414
    ChrTalk(
        0x101,
        (
            "#0000F这边是城市的南出口吧。\x02\x03",

            "现在没必要出去……\x01",
            "专心完成市内的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A2C9")

    label("loc_A2A8")

    SetChrName("")

    #A0415
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎没必要离开市区。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A2C9")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_A2DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A358")
    EventBegin(0x1)

    #C0416
    ChrTalk(
        0x101,
        (
            "#0000F要去阿尔摩利卡村的话，\x01",
            "得从城市的东出口出去才行啊。\x02\x03",

            "先绕到东街那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_A358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3CD")
    EventBegin(0x1)

    #C0417
    ChrTalk(
        0x101,
        (
            "#0000F要去玛因兹的话，\x01",
            "得从城市的北出口出去才行啊。\x02\x03",

            "先绕到住宅街那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_A3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A476")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A43F")

    #C0418
    ChrTalk(
        0x101,
        (
            "#0000F啊，这边是南出口。\x02\x03",

            "现在要避免让琪雅\x01",
            "遭遇到危险，\x01",
            "还是不要外出了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A460")

    label("loc_A43F")

    SetChrName("")

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎没有必要去市外。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A460")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_A476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A532")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4F1")

    #C0420
    ChrTalk(
        0x101,
        (
            "#0003F这边是城市的南出口啊。\x02\x03",

            "考虑到黑月的事……\x01",
            "……现在还是专心在市内进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A51C")

    label("loc_A4F1")

    SetChrName("")

    #A0421
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在还是专心在市内进行调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A51C")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_A532")

    Return()

    # Function_57_A239 end

    def Function_58_A533(): pass

    label("Function_58_A533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A59A")
    EventBegin(0x1)

    #C0422
    ChrTalk(
        0x101,
        (
            "#0000F这边是克洛斯贝尔车站。\x01",
            "……现在不必去那里吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_A59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A602")
    EventBegin(0x1)

    #C0423
    ChrTalk(
        0x101,
        (
            "#0000F这边是克洛斯贝尔车站。\x01",
            "……现在不必去那里吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_A602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A65C")
    EventBegin(0x1)

    #C0424
    ChrTalk(
        0x101,
        (
            "#0000F这边是克洛斯贝尔车站。\x01",
            "……现在不必去那里吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_A65C")

    Return()

    # Function_58_A533 end

    SaveToFile()

Try(main)
