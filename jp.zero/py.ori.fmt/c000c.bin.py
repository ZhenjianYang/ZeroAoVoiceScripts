from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ビリー",                 # 1
        "リッド",                 # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "女の子",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "中央広場",               # 17
        "西通り",                 # 18
        "行政区",                 # 19
        "住宅街",                 # 20
        "歓楽街",                 # 21
        "東通り",                 # 22
        "旧市街",                 # 23
        "港湾区",                 # 24
        "ＩＢＣ",                 # 25
        "駅前通り",               # 26
        "裏通り",                 # 27
        "ウルスラ間道",           # 28
        "東クロスベル街道",       # 29
        "西クロスベル街道",       # 30
        "マインツ山道",           # 31
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

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "中央広場")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "西通り")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "行政区")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "東通り")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "旧市街")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "港湾区")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "裏通り")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "マインツ山道")
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
        "Function_10_DD5",         # 0A, 10
        "Function_11_1544",        # 0B, 11
        "Function_12_15A8",        # 0C, 12
        "Function_13_1606",        # 0D, 13
        "Function_14_167F",        # 0E, 14
        "Function_15_1722",        # 0F, 15
        "Function_16_1784",        # 10, 16
        "Function_17_17FE",        # 11, 17
        "Function_18_185A",        # 12, 18
        "Function_19_18FF",        # 13, 19
        "Function_20_1949",        # 14, 20
        "Function_21_19F2",        # 15, 21
        "Function_22_1B35",        # 16, 22
        "Function_23_1E1F",        # 17, 23
        "Function_24_1E9A",        # 18, 24
        "Function_25_1F41",        # 19, 25
        "Function_26_2031",        # 1A, 26
        "Function_27_2094",        # 1B, 27
        "Function_28_23E8",        # 1C, 28
        "Function_29_2A0F",        # 1D, 29
        "Function_30_2FA1",        # 1E, 30
        "Function_31_3A4C",        # 1F, 31
        "Function_32_3B1A",        # 20, 32
        "Function_33_3BB7",        # 21, 33
        "Function_34_3C2A",        # 22, 34
        "Function_35_3DB4",        # 23, 35
        "Function_36_3F7E",        # 24, 36
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
    Jump("loc_DD1")

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C58")

    #C0001
    ChrTalk(
        0xFE,
        (
            "明日はまたベルガード門に\x01",
            "荷物の運び入れがあるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "はぁ……あそこはいつも\x01",
            "運搬車が必要になるほど\x01",
            "荷物が多いんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "……かったるいなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD1")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_CCF")

    #C0004
    ChrTalk(
        0xFE,
        "ふぅ、ようやく荷物が受け取れたよ。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "……ってもうこんな時間か！\x01",
            "急がないと時間内に間に合わねぇ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD1")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D60")

    #C0006
    ChrTalk(
        0xFE,
        (
            "観光客は確かに増えてるけど、\x01",
            "貨物量が増えてないのは救いだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ただ、受け取るまでに\x01",
            "時間がかかっちまうのには\x01",
            "参るなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD1")

    label("loc_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_DD1")

    #C0008
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "駅の中、大分混んでるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "こりゃ、荷物を受け取るのにも\x01",
            "時間が掛かりそうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD1")

    TalkEnd(0xFE)
    Return()

    # Function_9_B96 end

    def Function_10_DD5(): pass

    label("Function_10_DD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E5D")

    #C0010
    ChrTalk(
        0xFE,
        (
            "鉄道の運行本数増加期間の\x01",
            "最後の日だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "今日の用事が済んだら、\x01",
            "そこの橋から鉄道の発着を\x01",
            "眺めていようかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1540")

    label("loc_E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_F3E")

    #C0012
    ChrTalk(
        0xFE,
        (
            "図書館に\x01",
            "鉄道関係の本があるのを\x01",
            "知っているかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "実は僕、あの本に数ページ、\x01",
            "鉄道に関するコラムを書いたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "本当は３００ページあったんだけど\x01",
            "かなり省略されちゃったんだよね。\x01",
            "残念でならないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1540")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1013")

    #C0015
    ChrTalk(
        0xFE,
        (
            "僕のように、\x01",
            "鉄道にロマンを感じる人間は\x01",
            "決して少なくない。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "だがこのクロスベルでは\x01",
            "なかなか趣味の合う人に\x01",
            "巡り会えないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ああ、いつか語り合える友を\x01",
            "得られる日がくるだろうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1540")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111C")

    #C0018
    ChrTalk(
        0xFE,
        (
            "僕くらいの鉄道マニアになると、\x01",
            "列車に沸く感情は愛情に近いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ホームに停まっている列車の\x01",
            "一台一台に女性の名前をつけて\x01",
            "愛でてあげたいくらいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#0200F……世の中には色んな人が\x01",
            "いるんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0000F（何か納得してる……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_118E")

    label("loc_111C")


    #C0022
    ChrTalk(
        0xFE,
        (
            "大陸鉄道を駆ける２台の列車には、\x01",
            "個人的に名前をつけてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……え、知りたくない？\x01",
            "そうか、残念……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118E")

    Jump("loc_1540")

    label("loc_1193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1232")

    #C0024
    ChrTalk(
        0xFE,
        (
            "警備隊の詰めてる２つの国境門へは\x01",
            "専用の貨物路線が通ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "警備隊員や警察関係者は\x01",
            "申請書があれば乗れるらしいね……\x01",
            "うらやましい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1540")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133F")

    #C0026
    ChrTalk(
        0xFE,
        (
            "大陸鉄道公社が催しているイベントに\x01",
            "“スタンプラリー”というものがあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "特定の駅に設置されたスタンプを\x01",
            "専用の台紙に集めていくという、\x01",
            "ゲームを兼ねたツアーイベントなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "うーん、さすがは鉄道公社。\x01",
            "マニア心をくすぐるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13A9")

    label("loc_133F")


    #C0029
    ChrTalk(
        0xFE,
        (
            "スタンプラリーには\x01",
            "いつか参加してみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "ゲームしながら旅行が楽しめるなんて\x01",
            "最高じゃないか！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    Jump("loc_1540")

    label("loc_13AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B5")

    #C0031
    ChrTalk(
        0xFE,
        (
            "観光客が沢山来るおかげで\x01",
            "列車が大活躍してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "しかも、しかもだよ？\x01",
            "今年は例年より乗客が多いらしくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "なんと、期間中は特別に\x01",
            "運行本数を増やすそうなんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "うーん、鉄道マニアとして\x01",
            "これほどうれしいことはないね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1540")

    label("loc_14B5")


    #C0035
    ChrTalk(
        0xFE,
        (
            "運行本数が増えれば、\x01",
            "それだけ列車の走る勇姿を\x01",
            "見る機会が増える事になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "うーん、鉄道マニアとして\x01",
            "これほどうれしいことはないね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1540")

    TalkEnd(0xFE)
    Return()

    # Function_10_DD5 end

    def Function_11_1544(): pass

    label("Function_11_1544")

    TalkBegin(0xFE)

    #C0037
    ChrTalk(
        0xFE,
        "やあ、きみたちはクロスベル市の人？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "もしよかったら、\x01",
            "おすすめの観光地とか教えてよ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1544 end

    def Function_12_15A8(): pass

    label("Function_12_15A8")

    TalkBegin(0xFE)

    #C0039
    ChrTalk(
        0xFE,
        "あっちの方が中央広場ね。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "せっかくの祭りなんだし\x01",
            "賑やかな場所に行かないとね！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_15A8 end

    def Function_13_1606(): pass

    label("Function_13_1606")

    TalkBegin(0xFE)

    #C0041
    ChrTalk(
        0xFE,
        (
            "わたくし、極力自分の足で\x01",
            "歩きたくないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "あーあ、送迎用のハイヤーでも\x01",
            "呼んでおけばよかったわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1606 end

    def Function_14_167F(): pass

    label("Function_14_167F")

    TalkBegin(0xFE)

    #C0043
    ChrTalk(
        0xFE,
        (
            "妻はワガママで困る。\x01",
            "祭りというのは自分で歩くんだから\x01",
            "面白いんじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "まぁどちらにしろ、\x01",
            "例年通りの混みようなら\x01",
            "車になど乗っていられんがね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_167F end

    def Function_15_1722(): pass

    label("Function_15_1722")

    TalkBegin(0xFE)

    #C0045
    ChrTalk(
        0xFE,
        "なぁおい、次はどこに行くよ？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "せっかくの旅行なんだ、\x01",
            "隅々まで遊びつくしたいよな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1722 end

    def Function_16_1784(): pass

    label("Function_16_1784")

    TalkBegin(0xFE)

    #C0047
    ChrTalk(
        0xFE,
        (
            "そんなこと言ったって、\x01",
            "記念祭をすべて見て回るのは\x01",
            "難しいだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "行きたい場所はちゃんと\x01",
            "絞っておかないと。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1784 end

    def Function_17_17FE(): pass

    label("Function_17_17FE")

    TalkBegin(0xFE)

    #C0049
    ChrTalk(
        0xFE,
        "今日はパレードだ。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "ある意味締めくくりのイベントだから\x01",
            "絶対に見逃せないぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_17FE end

    def Function_18_185A(): pass

    label("Function_18_185A")

    TalkBegin(0xFE)

    #C0051
    ChrTalk(
        0xFE,
        (
            "旅行で来ている間に、\x01",
            "聖ウルスラ病院に行ってみようと\x01",
            "思っていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "最新鋭の医療技術を\x01",
            "研究しているという話だし、\x01",
            "土産話にはもってこいじゃないかね？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_185A end

    def Function_19_18FF(): pass

    label("Function_19_18FF")

    TalkBegin(0xFE)

    #C0053
    ChrTalk(
        0xFE,
        (
            "もうすぐパレードが始まるんですって。\x01",
            "あなたも急ぎましょうよ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_18FF end

    def Function_20_1949(): pass

    label("Function_20_1949")

    TalkBegin(0xFE)

    #C0054
    ChrTalk(
        0xFE,
        "ウーイ……楽しんでるかぁ？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "おじさんはすっかり\x01",
            "酔っ払ってしまったよ。\x01",
            "ワハハハ……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "まぁ、記念祭なんだから\x01",
            "これくらいは女神も\x01",
            "許してくれるだろうよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_1949 end

    def Function_21_19F2(): pass

    label("Function_21_19F2")

    TalkBegin(0xFE)
    OP_4B(0x13, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1AA9")

    #C0057
    ChrTalk(
        0xFE,
        "娘よ……パレードはまだかあ！！\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x13,
        (
            "もしかして……ここは\x01",
            "通らないんじゃないかしら。\x02",
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
            "うおおお……\x01",
            "パレードはどこだあ～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B2D")

    label("loc_1AA9")


    #C0061
    ChrTalk(
        0xFE,
        (
            "うおおお……パレードに\x01",
            "乗り遅れてしまった～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "悲しいぞ、娘よ！！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x13,
        (
            "父さん、落ち着いて！\x01",
            "腕時計が狂っちゃってるだけよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2D")

    OP_4C(0x13, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_21_19F2 end

    def Function_22_1B35(): pass

    label("Function_22_1B35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C93")

    #C0064
    ChrTalk(
        0x101,
        (
            "#0003F（うん、この子なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0xFE,
        "う～ん、知らないかも……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "ずっとこの辺りにいたけど\x01",
            "子供は来なかったと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0000Fそうか……\x01",
            "ありがとう、助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 0)
    SetScenarioFlags(0xAC, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_1CF5")

    label("loc_1C93")


    #C0069
    ChrTalk(
        0xFE,
        (
            "あたしずっと\x01",
            "この辺りにいたけど……\x01",
            "子供は来なかったと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "ごめんなさい、お兄さん。\x02",
    )

    CloseMessageWindow()

    label("loc_1CF5")

    Jump("loc_1E1B")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1D8F")

    #C0071
    ChrTalk(
        0xFE,
        (
            "もしかして……\x01",
            "さっき向こうから聞こえてきた音楽が\x01",
            "パレードだったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "……もうとっくに\x01",
            "通り過ぎちゃったけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1D8F")

    OP_4B(0x12, 0xFF)

    #C0073
    ChrTalk(
        0x12,
        (
            "うおおお……パレードに\x01",
            "乗り遅れてしまった～！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x12,
        "悲しいぞ、娘よ！！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "父さん、落ち着いて！\x01",
            "腕時計が狂っちゃってるだけよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)

    label("loc_1E1B")

    TalkEnd(0xFE)
    Return()

    # Function_22_1B35 end

    def Function_23_1E1F(): pass

    label("Function_23_1E1F")

    TalkBegin(0xFE)

    #C0076
    ChrTalk(
        0xFE,
        "早めに共和国のほうに帰る予定なんだ。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "混雑に巻き込まれて\x01",
            "せっかくの楽しい気分を\x01",
            "台無しにしたくないからね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1E1F end

    def Function_24_1E9A(): pass

    label("Function_24_1E9A")

    TalkBegin(0xFE)

    #C0078
    ChrTalk(
        0xFE,
        (
            "ミシュラム保養地という場所には\x01",
            "楽しいテーマパークが\x01",
            "あるという話じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "多少ミラはかさんでしまうが……\x01",
            "旅行に来た記念に\x01",
            "行ってみてもいいかもな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1E9A end

    def Function_25_1F41(): pass

    label("Function_25_1F41")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2030")

    #C0080
    ChrTalk(
        0x160,
        (
            "#3300F（駅前の辺りは\x01",
            "  こんな所かしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0003F（ああ、ツァイトも\x01",
            "  探してくれたようだけど……\x01",
            "  この辺りには来てないみたいだ。）\x02\x03",

            "#0001F（一度中央広場に戻って\x01",
            "  西通りの聞き込みに移ろう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 6)
    OP_29(0x46, 0x1, 0x9)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_2030")

    Return()

    # Function_25_1F41 end

    def Function_26_2031(): pass

    label("Function_26_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2047")
    Call(0, 29)
    Jump("loc_2093")

    label("loc_2047")

    TalkBegin(0xFF)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゲートはロックされている。\x01",
            "今は開ける必要は無さそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2093")

    Return()

    # Function_26_2031 end

    def Function_27_2094(): pass

    label("Function_27_2094")

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

    def lambda_2177():
        OP_96(0xFE, 0xFFFFAA10, 0xFFFFEC78, 0x45EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2177)

    def lambda_2191():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2191)
    Sleep(900)

    def lambda_21A5():
        OP_96(0xFE, 0xFFFFAA10, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21A5)

    def lambda_21BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_21BF)
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
            "#0005F#5Pおっと……もう夕方か。\x02\x03",

            "#0000F何だかんだいって、\x01",
            "結構長く潜っていたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0204F#5Pそうですね……\x02\x03",

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
        "#12P#0005Fティオ、どうしたんだ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    #C0086
    ChrTalk(
        0x103,
        (
            "#0201F#5P……何でもないです。\x02\x03",

            "#0203F早くヨナのところに戻って\x01",
            "記録結晶を受け取りましょう。\x02\x03",

            "#0202Fそれに《仔猫》の正体も\x01",
            "気になりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうだな……\x01",
            "何か掴めてるといいんだが。\x02",
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

    # Function_27_2094 end

    def Function_28_23E8(): pass

    label("Function_28_23E8")

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

    def lambda_247E():
        OP_96(0xFE, 0xC8, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_247E)
    Sleep(50)

    def lambda_249B():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4EE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_249B)
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

    def lambda_24F6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_24F6)
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

    def lambda_255A():
        OP_9A(0xFE, 0x101, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_255A)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0088
    AnonymousTalk(
        0x101,
        "#0001Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1267, 255, 100, 0)    #voice#Tio
    Sleep(800)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ティオの声")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……ティオです。\x02\x03",

            "ツァイトと一緒に\x01",
            "コリン君の匂いを辿っています。\x02\x03",

            "ですが、人が多すぎるらしく\x01",
            "匂いも途切れることが多くて\x01",
            "完全には追跡できていません。\x02",
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
            "#0006Fそうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ティオの声")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ただ、街の南口から出たり\x01",
            "駅に入ったりはしていないそうです。\x02\x03",

            "先ほどそちらを回った時に\x01",
            "ツァイトが言っていました。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(2054, 255, 90, 0)    #voice#Zeit
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ツァイトの声")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウォン！\x02",
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
            "#0003Fそうか、わかった。\x02\x03",

            "#0000Fその調子で、街の外に出てないか\x01",
            "他の出口も確かめてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ティオの声")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……了解しました。\x02\x03",

            "街を反時計回りに回りつつ\x01",
            "次は東口方面に行ってみます。\x02",
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
            "#0002Fああ、よろしく。\x02",
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

    def lambda_2868():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4F4C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2868)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    WaitChrThread(0x160, 1)
    Sleep(300)

    #C0096
    ChrTalk(
        0x160,
        (
            "#6P#3309Fうふふ、あの時の\x01",
            "オオカミさんが一緒なのね？\x02\x03",

            "#3302Fでも、警察犬にしちゃうなんて\x01",
            "お兄さんたちもなかなか\x01",
            "楽しいことを考えるのね。\x02",
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
            "#11P#0006Fいや、どちらかというと\x01",
            "押しかけられた方なんだけど……\x02\x03",

            "#0005F……って、レンちゃん。\x01",
            "何でそこまで知ってるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x160,
        "#6P#3304Fクスクス……\x02",
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

    # Function_28_23E8 end

    def Function_29_2A0F(): pass

    label("Function_29_2A0F")

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
            "ゲートはロックされている。\x01",
            "今は開ける必要は無さそうだ。\x07\x00\x02",
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
            "#3305Fジオフロント……\x01",
            "魔獣がうろついている場所ね。\x02\x03",

            "#3304F市庁舎の鍵がないと入れないし、\x01",
            "除外してもよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#12P#0012Fああ、たしかに……\x02",
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
            "#6P#0011Fって、だからどうして\x01",
            "そんな事まで知ってるんだ！？\x02\x03",

            "#0013F魔獣の事もそうだけど、\x01",
            "市庁舎の鍵が必要なことまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x160,
        "#3302Fうふふ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 400)
    Sleep(300)

    #C0104
    ChrTalk(
        0x160,
        (
            "#3309F#11Pこれでもレン、物知りなのよ？\x02\x03",

            "クロスベル市なら\x01",
            "一通り回っちゃっているし。\x02\x03",

            "#3302Fもう一つの遊び場でも\x01",
            "色々なものが覗けるんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#6P#0005Fもう一つの遊び場……\x02",
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
        "#6P#0013F（………まさか……………）\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x160,
        (
            "#3304F#11Pクスクス……\x01",
            "他の場所を調べましょう？\x02\x03",

            "#3302F可愛いあの子を\x01",
            "優しいパパとママの所に\x01",
            "帰してあげるためにも、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#6P#0001F君は……\x02",
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
            "#6P#0003F……ああ、そうだな。\x02\x03",

            "#0001F今はとにかく、\x01",
            "コリン君を捜すのが先決だ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F80")
    OP_93(0x101, 0xB4, 0x190)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        (
            "#0008F#5P（どうやらこの周辺には\x01",
            "  来ていないみたいだな。）\x02\x03",

            "#0001F（一度、中央広場に戻って\x01",
            "  西通りの聞き込みに移ろう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 6)
    OP_29(0x46, 0x1, 0x9)
    OP_1B(0x0, 0xFF, 0xFFFF)

    label("loc_2F80")

    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -22500, -5000, 18000, 180)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xAC, 5)
    EventEnd(0x5)
    Return()

    # Function_29_2A0F end

    def Function_30_2FA1(): pass

    label("Function_30_2FA1")

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

    def lambda_3075():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3075)
    Sleep(50)

    def lambda_3092():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3092)
    Sleep(50)

    def lambda_30AF():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30AF)
    Sleep(50)

    def lambda_30CC():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30CC)
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

    def lambda_315F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_315F)
    Sleep(50)

    def lambda_316F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_316F)
    Sleep(300)

    #C0111
    ChrTalk(
        0x101,
        "#5P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#0305Fおいおい。\x01",
            "また厄介ごとかよ？\x02",
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
        "#0001Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    #Sound(2083, 255, 100, 0)    #voice#Fran
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3468")
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "えへへ、お疲れさまです～。\x02",
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
            "#0005Fああ、フランか。\x02\x03",

            "#0002F昨日はどうも。\x01",
            "誘ってくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いえいえ～。\x01",
            "お姉ちゃんも喜んでましたし。\x02\x03",

            "ふふっ。\x01",
            "わたしも楽しかったですよー。\x02",
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
            "#0009Fはは、そりゃ光栄だな。\x02\x03",

            "#0001Fそれで、どうした？\x01",
            "ひょっとして緊急要請か？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、はい、そうなんです。\x02\x03",

            "実はその……\x01",
            "旧市街の不良さんたちが\x01",
            "いるじゃないですか？\x02\x03",

            "ちょうど今、その人たちが\x01",
            "港湾区で喧嘩をしているみたいで。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_359E")

    label("loc_3468")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうもお疲れさまです～。\x02",
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
            "#0005Fああ、フランか。\x02\x03",

            "#0001Fどうした？\x01",
            "ひょっとして緊急要請か？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、そうなんです。\x02\x03",

            "実はその……\x01",
            "旧市街の不良さんたちが\x01",
            "いるじゃないですか？\x02\x03",

            "ちょうど今、その人たちが\x01",
            "港湾区で喧嘩をしているみたいで。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_359E")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0122
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F本当か？\x02\x03",

            "#0006Fあいつら、性懲りもなく……\x01",
            "観光客だって大勢いるだろうに。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0123
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そうなんですよー……\x01",
            "それで警察に連絡が入ってきて。\x02\x03",

            "ただ、巡回中の警官はみんな忙しくて\x01",
            "手を割けそうにないらしくて……\x02\x03",

            "それで、彼らと面識のある\x01",
            "ロイドさんたちにお願いできないかと。\x02",
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
            "#0000F分かった、港湾区だな？\x02\x03",

            "丁度、街に戻ったところだから\x01",
            "すぐに急行するよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、よろしくお願いします。\x02",
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
            "#11P#0101F港湾区で何があったの？\x02",
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
            "#5P#0006Fああ、ワジとヴァルドたちだ。\x02\x03",

            "#0001Fあの辺りで、性懲りもなく\x01",
            "喧嘩沙汰を起こしているらしい。\x02",
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
        "#11P#0105Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#12P#0206Fさすがに迷惑ですね……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#0302Fやれやれ、祭りの熱気に\x01",
            "当てられちまったってところか？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#5P#0001Fとにかく人出も多いだろうし、\x01",
            "すぐに止めた方が良さそうだ。\x02\x03",

            "このまま港湾区に向かおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#11P#0100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x104,
        (
            "#0304Fそんじゃま、\x01",
            "ガキどもを説教しに行くかね。\x02",
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

    # Function_30_2FA1 end

    def Function_31_3A4C(): pass

    label("Function_31_3A4C")

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

    # Function_31_3A4C end

    def Function_32_3B1A(): pass

    label("Function_32_3B1A")


    def lambda_3B1F():
        OP_95(0xFE, -19000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B1F)
    WaitChrThread(0xFE, 1)

    def lambda_3B3D():
        OP_95(0xFE, -22000, -5000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B3D)
    WaitChrThread(0xFE, 1)
    OP_4B(0x103, 0xFF)
    OP_93(0xFE, 0x0, 0x1F4)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x0)
    OP_4C(0x103, 0xFF)

    def lambda_3B85():
        OP_95(0xFE, -22000, -5000, 23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B85)
    Sleep(200)

    def lambda_3BA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BA2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_3B1A end

    def Function_33_3BB7(): pass

    label("Function_33_3BB7")


    def lambda_3BBC():
        OP_95(0xFE, -19000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BBC)
    WaitChrThread(0xFE, 1)

    def lambda_3BDA():
        OP_95(0xFE, -22000, -5000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BDA)
    WaitChrThread(0xFE, 1)

    def lambda_3BF8():
        OP_95(0xFE, -22000, -5000, 23000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BF8)
    Sleep(200)

    def lambda_3C15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C15)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_33_3BB7 end

    def Function_34_3C2A(): pass

    label("Function_34_3C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CAD")
    EventBegin(0x1)

    #C0134
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはクロスベル駅だ。\x01",
            "記念祭で混雑してるみたいけど……\x02\x03",

            "……今は用はないかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D30")
    EventBegin(0x1)

    #C0135
    ChrTalk(
        0x101,
        (
            "#0000Fツァイトによれば\x01",
            "駅の方には行っていないみたいだ。\x02\x03",

            "こっちは除外してよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_3D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB3")
    EventBegin(0x1)

    #C0136
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはクロスベル駅だ。\x01",
            "記念祭で混雑してるみたいけど……\x02\x03",

            "……今は用はないかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_3DB3")

    Return()

    # Function_34_3C2A end

    def Function_35_3DB4(): pass

    label("Function_35_3DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EFA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7A")

    #C0137
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさん、ヨナから\x01",
            "連絡があるかもしれません。\x02\x03",

            "あまり遠くへ行くのはどうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな……\x01",
            "支度を済ませて\x01",
            "早めにジオフロントに向かおうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EE4")

    label("loc_3E7A")


    #C0139
    ChrTalk(
        0x103,
        (
            "#0203F……ヨナから\x01",
            "連絡があるかもしれないし。\x02\x03",

            "#0200F支度を済ませたら\x01",
            "早めにジオフロントに向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE4")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_3EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7D")
    EventBegin(0x1)

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000Fツァイトによれば\x01",
            "南口の方には出ていないみたいだ。\x02\x03",

            "こっちは除外してよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_3F7D")

    Return()

    # Function_35_3DB4 end

    def Function_36_3F7E(): pass

    label("Function_36_3F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4015")
    EventBegin(0x1)

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F駅前通りの聞き込みを\x01",
            "済ませてしまおう。\x02\x03",

            "あとは……コリン君が\x01",
            "隠れていそうな場所も\x01",
            "探してみないとな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 0, 21840, 180)
    EventEnd(0x4)

    label("loc_4015")

    Return()

    # Function_36_3F7E end

    SaveToFile()

Try(main)
