from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c000c.bin",                # FileName
        "c000c",                    # MapName
        "c000c",                    # Location
        0x0002,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 7, 0, 8],
    )

    BuildStringList((
        "c000c",                  # 0
        "比利",                   # 1
        "利德",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "女孩",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "中央广场",               # 17
        "西街",                   # 18
        "行政区",                 # 19
        "住宅街",                 # 20
        "欢乐街",                 # 21
        "东街",                   # 22
        "旧城区",                 # 23
        "港湾区",                 # 24
        "ＩＢＣ",                 # 25
        "站前街道",               # 26
        "后巷",                   # 27
        "乌尔斯拉间道",           # 28
        "东克洛斯贝尔街道",       # 29
        "西克洛斯贝尔街道",       # 30
        "玛因兹山道",             # 31
    ))

    AddCharChip((
        "chr/ch23600.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch34300.itc",                   # 03
        "chr/ch32400.itc",                   # 04
        "chr/ch33000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch33000.itc",                   # 07
        "chr/ch32200.itc",                   # 08
        "chr/ch23900.itc",                   # 09
        "chr/ch21300.itc",                   # 0A
        "chr/ch20200.itc",                   # 0B
        "chr/ch33100.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
    ))

    DeclNpc(4000,    0,       -7000,   270,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1830,   0,       13000,   180,  257,  0x0, 0,   1,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(4420,    0,       2450,    276,  385,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(750,     0,       -7000,   0,    385,  0x0, 0,   3,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(3809,    0,       509,     136,  385,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5489,    0,       409,     267,  385,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4590,    0,       3660,    45,   385,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(6139,    0,       2970,    308,  385,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(750,     0,       3000,    0,    385,  0x0, 0,   6,   0,   0,   3,   0,   17,  255,  0)
    DeclNpc(-2970,   0,       10220,   269,  385,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(3450,    0,       -1350,   270,  385,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3450,    0,       -2150,   0,    385,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(750,     0,       -3000,   0,    385,  0x0, 0,   10,  0,   0,   4,   0,   19,  255,  0)
    DeclNpc(4800,    0,       3000,    180,  385,  0x0, 0,   11,  0,   0,   5,   0,   20,  255,  0)
    DeclNpc(3829,    0,       1169,    270,  385,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(750,     0,       1000,    180,  385,  0x0, 0,   12,  0,   0,   6,   0,   24,  255,  0)

    DeclEvent(0x0000, 0, 34,  8.5,                   -2.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.25,                 0.5,                   0.10000000149011612,   1.0])

    DeclActor(-22300,  -5000,   20700,   2000,    -22300,  -4000,   20700,   0x007C, 0,  26, 0x0000)

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

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_6A0",          # 01, 1
        "Function_2_6F3",          # 02, 2
        "Function_3_72C",          # 03, 3
        "Function_4_765",          # 04, 4
        "Function_5_79E",          # 05, 5
        "Function_6_7C9",          # 06, 6
        "Function_7_802",          # 07, 7
        "Function_8_A47",          # 08, 8
        "Function_9_B96",          # 09, 9
        "Function_10_D5B",         # 0A, 10
        "Function_11_1390",        # 0B, 11
        "Function_12_13E6",        # 0C, 12
        "Function_13_1432",        # 0D, 13
        "Function_14_148B",        # 0E, 14
        "Function_15_1528",        # 0F, 15
        "Function_16_1578",        # 10, 16
        "Function_17_15E4",        # 11, 17
        "Function_18_1634",        # 12, 18
        "Function_19_16BD",        # 13, 19
        "Function_20_16F5",        # 14, 20
        "Function_21_177E",        # 15, 21
        "Function_22_18A1",        # 16, 22
        "Function_23_1B0B",        # 17, 23
        "Function_24_1B5E",        # 18, 24
        "Function_25_1BDB",        # 19, 25
        "Function_26_1CAD",        # 1A, 26
        "Function_27_1CF8",        # 1B, 27
        "Function_28_200E",        # 1C, 28
        "Function_29_25B9",        # 1D, 29
        "Function_30_2ACB",        # 1E, 30
        "Function_31_3444",        # 1F, 31
        "Function_32_3512",        # 20, 32
        "Function_33_35AF",        # 21, 33
        "Function_34_3622",        # 22, 34
        "Function_35_3788",        # 23, 35
        "Function_36_38FC",        # 24, 36
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_628"),
        (1, "loc_634"),
        (2, "loc_640"),
        (3, "loc_64C"),
        (4, "loc_658"),
        (5, "loc_664"),
        (6, "loc_670"),
        (SWITCH_DEFAULT, "loc_67C"),
    )


    label("loc_628")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_634")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_640")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_64C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_658")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_664")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_670")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_67C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_688")

    label("loc_69F")

    Return()

    # Function_0_5E8 end

    def Function_1_6A0(): pass

    label("Function_1_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F2")
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, -9000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, 13000, 2000, 0x0)
    Sleep(300)
    Jump("Function_1_6A0")

    label("loc_6F2")

    Return()

    # Function_1_6A0 end

    def Function_2_6F3(): pass

    label("Function_2_6F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72B")
    OP_95(0xFE, 750, 0, 33000, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_2_6F3")

    label("loc_72B")

    Return()

    # Function_2_6F3 end

    def Function_3_72C(): pass

    label("Function_3_72C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_764")
    OP_95(0xFE, 750, 0, 33000, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_3_72C")

    label("loc_764")

    Return()

    # Function_3_72C end

    def Function_4_765(): pass

    label("Function_4_765")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79D")
    OP_95(0xFE, 750, 0, 33000, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_4_765")

    label("loc_79D")

    Return()

    # Function_4_765 end

    def Function_5_79E(): pass

    label("Function_5_79E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C8")
    OP_94(0xFE, 0x189C, 0xFA0, 0xCE4, 0x834, 0x3E8)
    Sleep(300)
    Jump("Function_5_79E")

    label("loc_7C8")

    Return()

    # Function_5_79E end

    def Function_6_7C9(): pass

    label("Function_6_7C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_801")
    OP_95(0xFE, 750, 0, 33000, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 750, 0, -25000, 0)
    Jump("Function_6_7C9")

    label("loc_801")

    Return()

    # Function_6_7C9 end

    def Function_7_802(): pass

    label("Function_7_802")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B1")
    SetChrPos(0x0, 0, 0, 21840, 180)
    SetChrPos(0x1, 0, 0, 21840, 180)
    SetChrPos(0x2, 0, 0, 21840, 180)
    SetChrPos(0x3, 0, 0, 21840, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_889")
    SetChrPos(0x4, 0, 0, 21840, 180)
    SetChrPos(0x5, 0, 0, 21840, 180)
    Jump("loc_8A8")

    label("loc_889")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A8")
    SetChrPos(0x4, 0, 0, 21840, 180)

    label("loc_8A8")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B1")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D0")
    Event(0, 27)
    Jump("loc_904")

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    SetMapFlags(0x10000000)
    Event(0, 28)
    Jump("loc_904")

    label("loc_8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_915")
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_924")

    label("loc_915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_924")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 31)

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_941")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_A24")

    label("loc_941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_97B")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    OP_93(0x12, 0x0, 0x0)
    SetChrPos(0x13, 2650, 0, -2050, 0)
    Jump("loc_A24")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9B5")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    OP_93(0x12, 0x0, 0x0)
    SetChrPos(0x13, 2650, 0, -2050, 0)
    SetChrFlags(0x8, 0x80)
    Jump("loc_A24")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9D7")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)
    Jump("loc_A24")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_9F9")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Jump("loc_A24")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A11")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_A24")

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A24")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_A24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A46")
    OP_C7(0x1, 0x1000)

    label("loc_A46")

    Return()

    # Function_7_802 end

    def Function_8_A47(): pass

    label("Function_8_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A6C")
    Jump("loc_A75")

    label("loc_A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_A75")

    label("loc_A75")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A91")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_A91")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACF")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE7")
    OP_1B(0x3, 0x0, 0x23)

    label("loc_AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFA")
    OP_1B(0x3, 0x0, 0x23)

    label("loc_AFA")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B12")
    OP_1B(0x0, 0x0, 0x24)

    label("loc_B12")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, 15000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_8_A47 end

    def Function_9_B96(): pass

    label("Function_9_B96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BA7")
    Jump("loc_D57")

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C1C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "明天又要去贝尔加德门\x01",
            "送货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "唉……那里的货\x01",
            "总是多到\x01",
            "需要用搬运车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "……真麻烦啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D57")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_C81")

    #C0004
    ChrTalk(
        0xFE,
        "呼，总算收到货物了。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……呃，都这么晚了吗！\x01",
            "再不快点的话，就没法准时送到了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D57")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D06")

    #C0006
    ChrTalk(
        0xFE,
        (
            "游客的确是增加了不少，\x01",
            "不过好在货物量并没有增加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "只不过，领取货物\x01",
            "所需的时间变得更长了，\x01",
            "真让人头疼啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D57")

    label("loc_D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D57")

    #C0008
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "车站里似乎很拥挤呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "这下领取货物\x01",
            "又要多花时间了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D57")

    TalkEnd(0xFE)
    Return()

    # Function_9_B96 end

    def Function_10_D5B(): pass

    label("Function_10_D5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_DD3")

    #C0010
    ChrTalk(
        0xFE,
        (
            "列车运行列数增加的时段\x01",
            "已经到了最后一天了……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "干完今天的活，\x01",
            "就到那座桥上\x01",
            "眺望列车往来吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_E84")

    #C0012
    ChrTalk(
        0xFE,
        (
            "你知道吗？\x01",
            "图书馆里有本\x01",
            "和铁道有关的书。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "其实，那本书里的某几页\x01",
            "关于铁道的专栏，是我写的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "我本来写了三百页呢，\x01",
            "结果被删减了好多。\x01",
            "实在是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F2F")

    #C0015
    ChrTalk(
        0xFE,
        (
            "像我这样，\x01",
            "觉得铁道很有浪漫感觉的人\x01",
            "一定不在少数。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "然而，在克洛斯贝尔\x01",
            "很难碰到\x01",
            "志趣相投的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "唉，哪天才能遇见\x01",
            "可以一起畅所欲言的朋友呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101C")

    #C0018
    ChrTalk(
        0xFE,
        (
            "像我这样的铁道迷，\x01",
            "对列车的感情已经近乎于爱情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "甚至想给月台上停泊的\x01",
            "每一台列车都取上女性的名字，\x01",
            "然后好好爱护它们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0200F……世界上真是\x01",
            "什么样的人都有啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0000F（好像也可以理解……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1082")

    label("loc_101C")


    #C0022
    ChrTalk(
        0xFE,
        (
            "我给驰骋在大陆铁道上的两辆列车\x01",
            "取了很好听的名字哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……哎，你们没兴趣听？\x01",
            "是吗，好可惜……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1082")

    Jump("loc_138C")

    label("loc_1087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_111A")

    #C0024
    ChrTalk(
        0xFE,
        (
            "在警备队驻扎的两座国境门那里，\x01",
            "设有专用的货运专线。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "据说，警备队员和警界相关人士\x01",
            "只要递交申请书就能乘坐呢……\x01",
            "真是羡慕啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138C")

    label("loc_111A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_124E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F3")

    #C0026
    ChrTalk(
        0xFE,
        (
            "大陆铁道公司举办过\x01",
            "『集印章拉力赛』这样的活动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "就是在比赛专用的纸板上\x01",
            "收集设置在特定车站的印章，\x01",
            "是兼具娱乐性的旅游活动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "嗯～不愧是铁道公司，\x01",
            "懂得怎么撩动爱好者的心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1249")

    label("loc_11F3")


    #C0029
    ChrTalk(
        0xFE,
        (
            "我也很想参加\x01",
            "集印章拉力赛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "一边玩游戏，一边享受旅行的乐趣，\x01",
            "真是太棒啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1249")

    Jump("loc_138C")

    label("loc_124E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_138C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1323")

    #C0031
    ChrTalk(
        0xFE,
        (
            "因为来了大批游客，\x01",
            "列车可是大显身手了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "而且，听说今年的\x01",
            "乘客数远超往年……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "在这段时期内，竟然要特别\x01",
            "增加列车运行列数哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "嗯～对铁道迷来说，\x01",
            "没有比这更开心的事了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_138C")

    label("loc_1323")


    #C0035
    ChrTalk(
        0xFE,
        (
            "增加运行列数，\x01",
            "就等于增加了观赏\x01",
            "列车驰骋英姿的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "嗯～对铁道迷来说，\x01",
            "没有比这更开心的事了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138C")

    TalkEnd(0xFE)
    Return()

    # Function_10_D5B end

    def Function_11_1390(): pass

    label("Function_11_1390")

    TalkBegin(0xFE)

    #C0037
    ChrTalk(
        0xFE,
        "呀，你们是克洛斯贝尔市的人？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "如果可以的话，\x01",
            "请推荐一些观光点给我吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1390 end

    def Function_12_13E6(): pass

    label("Function_12_13E6")

    TalkBegin(0xFE)

    #C0039
    ChrTalk(
        0xFE,
        "那边是中央广场吧。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "难得的庆典，\x01",
            "一定要去热闹的地方才行呢！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_13E6 end

    def Function_13_1432(): pass

    label("Function_13_1432")

    TalkBegin(0xFE)

    #C0041
    ChrTalk(
        0xFE,
        (
            "其实我是非常\x01",
            "不愿意步行的……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "唉～要是事先叫辆\x01",
            "负责接送的出租车就好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1432 end

    def Function_14_148B(): pass

    label("Function_14_148B")

    TalkBegin(0xFE)

    #C0043
    ChrTalk(
        0xFE,
        (
            "我太太非常任性，真是伤脑筋。\x01",
            "所谓的庆典，就是要自己步行，\x01",
            "慢慢游览才有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "不过，话说回来，\x01",
            "要是像往年一样拥挤的话，\x01",
            "车子也根本开不动。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_148B end

    def Function_15_1528(): pass

    label("Function_15_1528")

    TalkBegin(0xFE)

    #C0045
    ChrTalk(
        0xFE,
        "喂，接下来要去哪里啊？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "难得旅行一趟，\x01",
            "真想把每个角落都玩遍呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1528 end

    def Function_16_1578(): pass

    label("Function_16_1578")

    TalkBegin(0xFE)

    #C0047
    ChrTalk(
        0xFE,
        (
            "不过，话虽如此，\x01",
            "要想把纪念庆典逛全，\x01",
            "大概是很难的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "还是要选定一些\x01",
            "最想去的地方才行呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1578 end

    def Function_17_15E4(): pass

    label("Function_17_15E4")

    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0xFE,
        "今天有游行呢。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "某种意义上来说，是压轴的活动，\x01",
            "绝对不能错过哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_15E4 end

    def Function_18_1634(): pass

    label("Function_18_1634")

    TalkBegin(0xFE)

    #C0051
    ChrTalk(
        0xFE,
        (
            "在来这里旅行的期间，\x01",
            "我想去乌尔斯拉医院\x01",
            "看看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "听说那里正在研究\x01",
            "最先进的医疗技术，\x01",
            "很适合作为旅行见闻，讲给别人听吧？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1634 end

    def Function_19_16BD(): pass

    label("Function_19_16BD")

    TalkBegin(0xFE)

    #C0053
    ChrTalk(
        0xFE,
        (
            "听说游行马上就要开始了。\x01",
            "老公，你也快点呀！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_16BD end

    def Function_20_16F5(): pass

    label("Function_20_16F5")

    TalkBegin(0xFE)

    #C0054
    ChrTalk(
        0xFE,
        "嘿……玩得开心吗？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "大叔我可是\x01",
            "喝了个酩酊大醉啊。\x01",
            "哇哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "哎，反正是纪念庆典，\x01",
            "这点小事，\x01",
            "女神一定会原谅我啦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_16F5 end

    def Function_21_177E(): pass

    label("Function_21_177E")

    TalkBegin(0xFE)
    OP_4B(0x13, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1829")

    #C0057
    ChrTalk(
        0xFE,
        "女儿啊……游行还没开始吗！！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x13,
        (
            "该不会是……根本就没预定\x01",
            "通过这条路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "呜哦哦哦……\x01",
            "游行队伍在哪里啊～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1899")

    label("loc_1829")


    #C0061
    ChrTalk(
        0xFE,
        (
            "呜哦哦哦……竟然\x01",
            "没赶上游行啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "女儿啊，我太伤心了！！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x13,
        (
            "爸爸，你镇定一点！\x01",
            "只是手表不准而已啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1899")

    OP_4C(0x13, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_21_177E end

    def Function_22_18A1(): pass

    label("Function_22_18A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CF")

    #C0064
    ChrTalk(
        0x101,
        (
            "#0003F（嗯，这孩子\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0xFE,
        "嗯～不知道呢……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "我一直待在这附近，\x01",
            "好像没见到有小孩子来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢，帮大忙啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 0)
    SetScenarioFlags(0xAC, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_1A19")

    label("loc_19CF")


    #C0069
    ChrTalk(
        0xFE,
        (
            "我一直\x01",
            "待在这附近……\x01",
            "好像没见到有小孩子来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "抱歉哦，大哥哥。\x02",
    )

    CloseMessageWindow()

    label("loc_1A19")

    Jump("loc_1B07")

    label("loc_1A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1A8F")

    #C0071
    ChrTalk(
        0xFE,
        (
            "说不定……\x01",
            "刚才从那边传来的音乐，\x01",
            "就是游行队伍的音乐吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……虽然游行队伍\x01",
            "早就过去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B07")

    label("loc_1A8F")

    OP_4B(0x12, 0xFF)

    #C0073
    ChrTalk(
        0x12,
        (
            "呜哦哦哦……竟然\x01",
            "没赶上游行啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x12,
        "我太伤心了，女儿啊！！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "爸爸，你镇定一点！\x01",
            "只是手表不准而已啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)

    label("loc_1B07")

    TalkEnd(0xFE)
    Return()

    # Function_22_18A1 end

    def Function_23_1B0B(): pass

    label("Function_23_1B0B")

    TalkBegin(0xFE)

    #C0076
    ChrTalk(
        0xFE,
        "我打算早点回共和国去。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "不想因为拥挤混乱\x01",
            "而破坏了难得的\x01",
            "好心情嘛。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1B0B end

    def Function_24_1B5E(): pass

    label("Function_24_1B5E")

    TalkBegin(0xFE)

    #C0078
    ChrTalk(
        0xFE,
        (
            "听说疗养地米修拉姆那里\x01",
            "有个很好玩的\x01",
            "主题公园呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "虽然会多花点钱……\x01",
            "不过，作为旅行的纪念，\x01",
            "去看看也不错吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1B5E end

    def Function_25_1BDB(): pass

    label("Function_25_1BDB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CAC")

    #C0080
    ChrTalk(
        0x160,
        (
            "#3300F（在车站附近，\x01",
            "  已经探听得差不多了吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0003F（嗯，蔡特似乎\x01",
            "  也找过了……\x01",
            "  好像没到这一带来啊。）\x02\x03",

            "#0001F（先返回中央广场，\x01",
            "  然后去西街打听一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 6)
    OP_29(0x46, 0x1, 0x9)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_1CAC")

    Return()

    # Function_25_1BDB end

    def Function_26_1CAD(): pass

    label("Function_26_1CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC3")
    Call(0, 29)
    Jump("loc_1CF7")

    label("loc_1CC3")

    TalkBegin(0xFF)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x01",
            "现在似乎没必要打开。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_1CF7")

    Return()

    # Function_26_1CAD end

    def Function_27_1CF8(): pass

    label("Function_27_1CF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22000, -3900, 18700, 0)
    MoveCamera(32, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -22000, -5000, 22000, 180)
    SetChrPos(0x103, -22000, -5000, 22000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFC, 0xC3, 0xB6, 0x28, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetCameraDistance(19000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)

    def lambda_1DDB():
        OP_96(0xFE, 0xFFFFAA10, 0xFFFFEC78, 0x45EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DDB)

    def lambda_1DF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DF5)
    Sleep(900)

    def lambda_1E09():
        OP_96(0xFE, 0xFFFFAA10, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E09)

    def lambda_1E23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1E23)
    Sleep(1000)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    #C0083
    ChrTalk(
        0x101,
        (
            "#0005F#5P哦……都傍晚了啊。\x02\x03",

            "#0000F在下面折腾了这么久，\x01",
            "还真是耗了很长时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0204F#5P是啊……\x02\x03",

            "#0202F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x103, 500)

    #C0085
    ChrTalk(
        0x101,
        "#12P#0005F缇欧，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0086
    ChrTalk(
        0x103,
        (
            "#0201F#5P……没什么。\x02\x03",

            "#0203F赶快回约纳那里\x01",
            "收取记录结晶吧。\x02\x03",

            "#0202F而且我也很在意\x01",
            "『小猫』的真面目。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#12P#0000F是啊……\x01",
            "要是能查到些什么就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_1CF8 end

    def Function_28_200E(): pass

    label("Function_28_200E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(0, 1100, 20000, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 200, 0, 25500, 180)
    SetChrPos(0x160, -1000, 0, 25800, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_20A4():
        OP_96(0xFE, 0xC8, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20A4)
    Sleep(50)

    def lambda_20C1():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4EE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_20C1)
    SetCameraDistance(17500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    WaitChrThread(0x160, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_211C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_211C)
    Sleep(500)
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
    #Sound(1084, 255, 100, 0)    #voice#Lloyd

    def lambda_2180():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2180)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0088
    AnonymousTalk(
        0x101,
        "#0001F喂，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1267, 255, 100, 0)    #voice#Tio
    Sleep(800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("缇欧的声音")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……我是缇欧。\x02\x03",

            "现在正和蔡特一起\x01",
            "追踪柯林的气味。\x02\x03",

            "不过，也许是因为人太多了，\x01",
            "气味总是断断续续的，\x01",
            "无法完全追踪到。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0090
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F是吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("缇欧的声音")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过，他似乎没有从城市的南出口出去，\x01",
            "也没有进入过车站。\x02\x03",

            "刚才经过那里的时候，\x01",
            "蔡特是这么说的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(2054, 255, 90, 0)    #voice#Zeit
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("蔡特的声音")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗷呜！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0093
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F是吗，知道了。\x02\x03",

            "#0000F就像这样，也去其它出口看看，\x01",
            "确认一下他有没有离开市区，好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("缇欧的声音")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……明白了。\x02\x03",

            "我们就在市内按逆时针方向绕一圈吧，\x01",
            "接下来去东出口那边看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0095
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002F嗯，拜托了。\x02",
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
    WaitChrThread(0x160, 1)

    def lambda_244A():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4F4C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_244A)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    #C0096
    ChrTalk(
        0x160,
        (
            "#6P#3309F呵呵，那个时候的\x01",
            "狼先生在帮忙吧？\x02\x03",

            "#3302F不过，竟然拿人家当警犬，\x01",
            "大哥哥，你们的想法\x01",
            "还真是有趣呢。\x02",
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
    Sound(804, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x160, 500)

    #C0097
    ChrTalk(
        0x101,
        (
            "#11P#0006F不，硬要说的话，\x01",
            "其实是对方主动找上门的……\x02\x03",

            "#0005F……呃，小玲，\x01",
            "你怎么会知道这么多？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x160,
        "#6P#3304F嘻嘻……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 0, 0, 20000, 180)
    SetScenarioFlags(0xA2, 4)
    OP_29(0x46, 0x1, 0x8)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_28_200E end

    def Function_29_25B9(): pass

    label("Function_29_25B9")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-22100, -4000, 20500, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -22700, -5000, 19200, 0)
    SetChrPos(0x160, -21600, -5000, 19200, 315)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    CreatePortrait(1, 112, 64, 368, 192, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis050.itp")
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x01",
            "现在似乎没必要打开。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0100
    ChrTalk(
        0x160,
        (
            "#3305F地下空间……\x01",
            "是有魔兽徘徊的地方呢。\x02\x03",

            "#3304F没有市政厅的钥匙就进不去，\x01",
            "就先把这个地方排除吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#12P#0012F嗯，的确是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x160, 500)

    #C0102
    ChrTalk(
        0x101,
        (
            "#6P#0011F呃，等一下，你怎么\x01",
            "连这种事都知道啊！？\x02\x03",

            "#0013F不仅知道里面有魔兽，\x01",
            "而且连需要市政厅的钥匙都……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x160,
        "#3302F呵呵……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 400)
    Sleep(300)

    #C0104
    ChrTalk(
        0x160,
        (
            "#3309F#11P不要小看玲，玲可是万事通哦。\x02\x03",

            "我早就把克洛斯贝尔市\x01",
            "整个转遍了呢。\x02\x03",

            "#3302F在另一个游戏场\x01",
            "也可以查探到各种各样的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#6P#0005F另一个游戏场……\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x32, 0x12C)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x12C)

    #C0106
    ChrTalk(
        0x101,
        "#6P#0013F（………难道是……………）\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x160,
        (
            "#3304F#11P嘻嘻……\x01",
            "去调查其它地方吧？\x02\x03",

            "#3302F为了把那个可爱的孩子\x01",
            "送回到温柔父母的身边，\x01",
            "对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#6P#0001F你到底……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)

    #C0109
    ChrTalk(
        0x101,
        (
            "#6P#0003F……嗯，你说得对。\x02\x03",

            "#0001F总而言之，\x01",
            "寻找柯林才是目前的首要任务。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AAA")
    OP_93(0x101, 0xB4, 0x190)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        (
            "#0008F#5P（看样子，好像没来过\x01",
            "  这附近啊。）\x02\x03",

            "#0001F（先回中央广场，\x01",
            "  然后去西街探听一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 6)
    OP_29(0x46, 0x1, 0x9)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_2AAA")

    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -22500, -5000, 18000, 180)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xAC, 5)
    EventEnd(0x5)
    Return()

    # Function_29_25B9 end

    def Function_30_2ACB(): pass

    label("Function_30_2ACB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(0, 1000, -14200, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -600, 0, -18500, 0)
    SetChrPos(0x102, 600, 0, -18500, 0)
    SetChrPos(0x103, -600, 0, -19900, 0)
    SetChrPos(0x104, 600, 0, -19900, 0)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_2B9F():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B9F)
    Sleep(50)

    def lambda_2BBC():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BBC)
    Sleep(50)

    def lambda_2BD9():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BD9)
    Sleep(50)

    def lambda_2BF6():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BF6)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2C89():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2C89)
    Sleep(50)

    def lambda_2C99():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2C99)
    Sleep(300)

    #C0111
    ChrTalk(
        0x101,
        "#5P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#0305F喂喂，\x01",
            "又有麻烦事了？\x02",
        )
    )

    CloseMessageWindow()
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
    #Sound(1084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0113
    AnonymousTalk(
        0x101,
        "#0001F您好，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    #Sound(2083, 255, 100, 0)    #voice#Fran
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F26")
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嘿嘿，辛苦了～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0115
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊，是芙兰啊。\x02\x03",

            "#0002F昨天真是承蒙关照了，\x01",
            "谢谢你们约我去玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哪里哪里～\x01",
            "姐姐也很高兴嘛。\x02\x03",

            "呵呵，\x01",
            "我也玩得很开心哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0117
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0009F哈哈，那是我的荣幸。\x02\x03",

            "#0001F对了，怎么了？\x01",
            "难道有紧急任务？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，是的，没错。\x02\x03",

            "其实呢……\x01",
            "旧城区不是有些\x01",
            "不良团伙成员吗？\x02\x03",

            "那些人现在好像\x01",
            "正在港湾区争斗呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3016")

    label("loc_2F26")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大家辛苦了～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0120
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F啊，是芙兰啊。\x02\x03",

            "#0001F怎么了？\x01",
            "难道有紧急任务？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是的，没错。\x02\x03",

            "其实呢……\x01",
            "旧城区不是有些\x01",
            "不良团伙成员吗？\x02\x03",

            "那些人现在好像\x01",
            "正在港湾区争斗呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3016")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0122
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F真的吗？\x02\x03",

            "#0006F那些家伙，真是不知悔改……\x01",
            "也不想想有多少游客在场。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就是说嘛～……\x01",
            "所以就有人报警了。\x02\x03",

            "可是，正在巡逻的警官们都很忙，\x01",
            "腾不出手来……\x02\x03",

            "所以我就想，能不能拜托罗伊德警官你们。\x01",
            "毕竟你们和他们也算有一点交情。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0124
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F知道了，在港湾区是吧？\x02\x03",

            "我们正好刚回市里，\x01",
            "立刻就赶过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，那就拜托了。\x02",
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

    #C0126
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#0101F港湾区出了什么事吗？\x02",
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
    TurnDirection(0x101, 0x104, 500)

    #C0127
    ChrTalk(
        0x101,
        (
            "#5P#0006F嗯，是瓦吉和瓦鲁多他们。\x02\x03",

            "#0001F似乎还是死性不改，\x01",
            "又要开始打架了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x102,
        "#11P#0105F这可……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#12P#0206F真是个大麻烦呢……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#0302F哎呀呀，莫非是被庆典的\x01",
            "热闹气氛冲昏了头脑吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#5P#0001F总之，那里的人肯定很多，\x01",
            "还是赶快阻止他们为好。\x02\x03",

            "直接前往港湾区吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#11P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x104,
        (
            "#0304F好，那我们这就去\x01",
            "教育一下那帮小鬼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, 0, 0, -13500, 0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA0, 1)
    OP_29(0x44, 0x1, 0x1)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_30_2ACB end

    def Function_31_3444(): pass

    label("Function_31_3444")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-20000, -4000, 17000, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(26000, 0)
    OP_90(0x101, -10000, -3800, 17000, 270)
    OP_90(0x103, -8500, -2800, 17000, 270)
    MoveCamera(35, 25, 0, 10000)
    SetCameraDistance(17500, 10000)
    BeginChrThread(0x101, 3, 0, 32)
    BeginChrThread(0x103, 3, 0, 33)
    FadeToBright(2000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x103, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("m0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_3444 end

    def Function_32_3512(): pass

    label("Function_32_3512")


    def lambda_3517():
        OP_95(0xFE, -19000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3517)
    WaitChrThread(0xFE, 1)

    def lambda_3535():
        OP_95(0xFE, -22000, -5000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3535)
    WaitChrThread(0xFE, 1)
    OP_4B(0x103, 0xFF)
    OP_93(0xFE, 0x0, 0x1F4)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    OP_4C(0x103, 0xFF)

    def lambda_357D():
        OP_95(0xFE, -22000, -5000, 23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_357D)
    Sleep(200)

    def lambda_359A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_359A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_3512 end

    def Function_33_35AF(): pass

    label("Function_33_35AF")


    def lambda_35B4():
        OP_95(0xFE, -19000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35B4)
    WaitChrThread(0xFE, 1)

    def lambda_35D2():
        OP_95(0xFE, -22000, -5000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35D2)
    WaitChrThread(0xFE, 1)

    def lambda_35F0():
        OP_95(0xFE, -22000, -5000, 23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35F0)
    Sleep(200)

    def lambda_360D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_360D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_33_35AF end

    def Function_34_3622(): pass

    label("Function_34_3622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_369F")
    EventBegin(0x1)

    #C0134
    ChrTalk(
        0x101,
        (
            "#0000F这边是克洛斯贝尔车站。\x01",
            "似乎因为纪念庆典而十分拥挤……\x02\x03",

            "……现在不必过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_369F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_370A")
    EventBegin(0x1)

    #C0135
    ChrTalk(
        0x101,
        (
            "#0000F据蔡特说，\x01",
            "柯林好像没有去车站那边。\x02\x03",

            "这个地方可以排除了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_370A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3787")
    EventBegin(0x1)

    #C0136
    ChrTalk(
        0x101,
        (
            "#0000F这边是克洛斯贝尔车站。\x01",
            "似乎因为纪念庆典而十分拥挤……\x02\x03",

            "……现在不必过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_3787")

    Return()

    # Function_34_3622 end

    def Function_35_3788(): pass

    label("Function_35_3788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_388E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3828")

    #C0137
    ChrTalk(
        0x103,
        (
            "#0200F罗伊德前辈，约纳\x01",
            "可能会发来联络。\x02\x03",

            "走太远似乎不大好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#0000F也是……\x01",
            "做好准备之后，\x01",
            "还是尽快去地下空间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3878")

    label("loc_3828")


    #C0139
    ChrTalk(
        0x103,
        (
            "#0203F……约纳\x01",
            "可能会发来联络。\x02\x03",

            "#0200F如果准备好了，\x01",
            "就尽快去地下空间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3878")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_388E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38FB")
    EventBegin(0x1)

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000F据蔡特说，\x01",
            "柯林好像没有从南出口出去。\x02\x03",

            "这个地方可以排除了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_38FB")

    Return()

    # Function_35_3788 end

    def Function_36_38FC(): pass

    label("Function_36_38FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3989")
    EventBegin(0x1)

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F我们快点把站前街道的\x01",
            "调查工作完成吧。\x02\x03",

            "在这之后……还要赶快\x01",
            "找一找柯林有可能\x01",
            "会藏身的地方。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 21840, 180)
    EventEnd(0x4)

    label("loc_3989")

    Return()

    # Function_36_38FC end

    SaveToFile()

Try(main)
