from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ビリー",                 # 1
        "リッド",                 # 2
        "フリージア",             # 3
        "レティナ",               # 4
        "マーシャ",               # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "観光客",                 # 16
        "ビジネスマン",           # 17
        "ビジネスマン",           # 18
        "観光客",                 # 19
        "観光客",                 # 20
        "観光客",                 # 21
        "観光客",                 # 22
        "観光客",                 # 23
        "観光客",                 # 24
        "観光客",                 # 25
        "観光客",                 # 26
        "観光客",                 # 27
        "セルゲイ課長",           # 28
        "老人",                   # 29
        "老婦人",                 # 30
        "グレイス",               # 31
        "アリオス",               # 32
        "列車",                   # 33
        "観光客",                 # 34
        "観光客",                 # 35
        "観光客",                 # 36
        "車00",                   # 37
        "クロマ",                 # 38
        "中央広場",               # 39
        "西通り",                 # 40
        "行政区",                 # 41
        "住宅街",                 # 42
        "歓楽街",                 # 43
        "東通り",                 # 44
        "旧市街",                 # 45
        "港湾区",                 # 46
        "ＩＢＣ",                 # 47
        "駅前通り",               # 48
        "裏通り",                 # 49
        "ウルスラ間道",           # 50
        "東クロスベル街道",       # 51
        "西クロスベル街道",       # 52
        "マインツ山道",           # 53
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
    PlaceName(2.0, 0.0, 55.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_940",          # 00, 0
        "Function_1_9F8",          # 01, 1
        "Function_2_A4B",          # 02, 2
        "Function_3_A84",          # 03, 3
        "Function_4_D88",          # 04, 4
        "Function_5_1040",         # 05, 5
        "Function_6_1A43",         # 06, 6
        "Function_7_28D6",         # 07, 7
        "Function_8_2A71",         # 08, 8
        "Function_9_2C05",         # 09, 9
        "Function_10_2D84",        # 0A, 10
        "Function_11_2F6B",        # 0B, 11
        "Function_12_2FCB",        # 0C, 12
        "Function_13_303E",        # 0D, 13
        "Function_14_309C",        # 0E, 14
        "Function_15_30FE",        # 0F, 15
        "Function_16_3180",        # 10, 16
        "Function_17_3202",        # 11, 17
        "Function_18_3279",        # 12, 18
        "Function_19_32C7",        # 13, 19
        "Function_20_3343",        # 14, 20
        "Function_21_33D4",        # 15, 21
        "Function_22_344B",        # 16, 22
        "Function_23_34AE",        # 17, 23
        "Function_24_34D3",        # 18, 24
        "Function_25_355F",        # 19, 25
        "Function_26_35AC",        # 1A, 26
        "Function_27_3601",        # 1B, 27
        "Function_28_3655",        # 1C, 28
        "Function_29_36C9",        # 1D, 29
        "Function_30_3797",        # 1E, 30
        "Function_31_3814",        # 1F, 31
        "Function_32_3880",        # 20, 32
        "Function_33_3908",        # 21, 33
        "Function_34_3B01",        # 22, 34
        "Function_35_5121",        # 23, 35
        "Function_36_535F",        # 24, 36
        "Function_37_5717",        # 25, 37
        "Function_38_5751",        # 26, 38
        "Function_39_578E",        # 27, 39
        "Function_40_57D3",        # 28, 40
        "Function_41_5814",        # 29, 41
        "Function_42_5859",        # 2A, 42
        "Function_43_589A",        # 2B, 43
        "Function_44_8FB1",        # 2C, 44
        "Function_45_A024",        # 2D, 45
        "Function_46_A11A",        # 2E, 46
        "Function_47_A210",        # 2F, 47
        "Function_48_A265",        # 30, 48
        "Function_49_A2BA",        # 31, 49
        "Function_50_A30F",        # 32, 50
        "Function_51_A370",        # 33, 51
        "Function_52_A3AD",        # 34, 52
        "Function_53_A3EA",        # 35, 53
        "Function_54_A64C",        # 36, 54
        "Function_55_A66B",        # 37, 55
        "Function_56_B209",        # 38, 56
        "Function_57_B340",        # 39, 57
        "Function_58_B670",        # 3A, 58
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_112A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DC")

    #C0001
    ChrTalk(
        0xFE,
        (
            "だぁ～！！\x01",
            "ようやく荷物を渡してもらえたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "って、もうこんな時間じゃないか！\x01",
            "急がないと今日中に配りきれないぞ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1125")

    label("loc_10DC")


    #C0003
    ChrTalk(
        0xFE,
        (
            "あれこれ考えてるヒマはないな……\x01",
            "とにかく急いで配達して回らないと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1125")

    Jump("loc_1A3F")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_11BA")

    #C0004
    ChrTalk(
        0xFE,
        "駅は今、厳戒態勢らしくてな。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "客車だけじゃなく、\x01",
            "貨物列車の臨検も遅れてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "流石に参っちまうな、\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_11BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1269")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ふ～……\x01",
            "いつもの如く、\x01",
            "列車の荷物待ちだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "ま、いい加減\x01",
            "受け取りが遅れるのも\x01",
            "馴れてきちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "この待つ時間を楽しめてこそ\x01",
            "プロってもんだよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12DE")

    #C0010
    ChrTalk(
        0xFE,
        (
            "今日は珍しく、早いうちに荷物を\x01",
            "受け取ることができたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "よーし、とっとと配達に行くとするか！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_12DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_136D")

    #C0012
    ChrTalk(
        0xFE,
        (
            "記念祭が終わっても\x01",
            "忙しいのに変わりはないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "運送業者に休みなんて\x01",
            "ないんだろうな……\x01",
            "オヤジも難儀な商売始めたもんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_136D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_137B")
    Jump("loc_1A3F")

    label("loc_137B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1389")
    Jump("loc_1A3F")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1474")

    #C0014
    ChrTalk(
        0xFE,
        (
            "ようやく\x01",
            "荷物の運び入れが終わったよ。\x01",
            "……しんどかったぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "はあ、明日はベルガード門で荷卸しか。\x01",
            "やってらんないね、こりゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "せっかく貨物列車が通ってるんだし、\x01",
            "一緒に運んでくれればいいのになぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1511")

    label("loc_1474")


    #C0017
    ChrTalk(
        0xFE,
        (
            "警備隊は詰め所暮らしだから、\x01",
            "家族からの差し入れなんかを\x01",
            "頼まれるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "せっかく貨物列車が通ってるんだし、\x01",
            "一緒に運んでくれればいいのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1511")

    Jump("loc_1A3F")

    label("loc_1516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15D1")

    #C0019
    ChrTalk(
        0xFE,
        (
            "そこに置いてるの、\x01",
            "うちの会社で使ってる\x01",
            "運搬車なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "持っていく荷物が\x01",
            "多いらしいから、\x01",
            "車を出したんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……俺一人で車に入れるわけ？\x01",
            "めんどくさ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1667")

    #C0022
    ChrTalk(
        0xFE,
        (
            "外国からの貨物は\x01",
            "到着が遅れることが多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "それで配達が遅れたら\x01",
            "俺が親父に叱られるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "あーあ、かったるいなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1785")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1709")

    #C0025
    ChrTalk(
        0xFE,
        (
            "さっき共和国からの\x01",
            "荷物が届いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "配送先は……\x01",
            "げげっ鉱山町マインツか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "はー、こいつぁ急がないと\x01",
            "日が暮れちゃうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1780")

    label("loc_1709")


    #C0028
    ChrTalk(
        0xFE,
        (
            "鉱山町マインツってことは\x01",
            "あの細い山道を登ってかなきゃ\x01",
            "なんないワケで……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "はー、急がないと\x01",
            "日が暮れちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1780")

    Jump("loc_1A3F")

    label("loc_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1836")

    #C0030
    ChrTalk(
        0xFE,
        (
            "今日は共和国からの荷物が\x01",
            "届く予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "今日は早めに来たんだけど……\x01",
            "まだ貨物は届いてないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……んー、真面目なことを\x01",
            "するんじゃなかったぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_1836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_18E1")

    #C0033
    ChrTalk(
        0xFE,
        (
            "やれやれ、\x01",
            "ようやく積荷を受け取れたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "さっさと配達先に届けないと、\x01",
            "また親父にどやされちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "まったく、文句があるなら\x01",
            "自分でやれっての。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3F")

    label("loc_18E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A8")

    #C0036
    ChrTalk(
        0xFE,
        (
            "うちは『ライムス運送』っていう\x01",
            "個人運営の運送会社でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "外国からの荷物を市民に\x01",
            "配達しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "駅に届いた貨物を\x01",
            "受け取りに来たんだけど……\x01",
            "おっそいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A3F")

    label("loc_19A8")


    #C0039
    ChrTalk(
        0xFE,
        (
            "うちは『ライムス運送』っていう\x01",
            "個人運営の運送会社でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "駅に届いた貨物を\x01",
            "受け取りに来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "こんなに遅いと\x01",
            "やってらんないよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3F")

    TalkEnd(0xFE)
    Return()

    # Function_5_1040 end

    def Function_6_1A43(): pass

    label("Function_6_1A43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1AF0")

    #C0042
    ChrTalk(
        0xFE,
        (
            "噂に聞けば、空港と駅で\x01",
            "危険物に対する警戒を敷いていた\x01",
            "そうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "一体どこのどいつなんだ！\x01",
            "俺の愛しい列車たちを\x01",
            "危険な目に合わせるなんて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7B")

    #C0044
    ChrTalk(
        0xFE,
        (
            "どうした事だ……\x01",
            "今日は列車の本数が少ない気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "……いや、全ての列車の発車が\x01",
            "遅れているのか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BB2")

    label("loc_1B7B")


    #C0046
    ChrTalk(
        0xFE,
        (
            "列車の発車がこんな頻度で\x01",
            "遅れてるなんて妙だな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")

    Jump("loc_28D2")

    label("loc_1BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA6")

    #C0047
    ChrTalk(
        0xFE,
        (
            "数々の列車を生み出した\x01",
            "帝国の文化には敬意を表したい所だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "帝国の兵器『列車砲』とやらは\x01",
            "どうしても許せないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "列車とは……人々と貨物、\x01",
            "そして僕のような列車マニアの\x01",
            "夢を運ぶ乗り物なのだから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D2F")

    label("loc_1CA6")


    #C0050
    ChrTalk(
        0xFE,
        (
            "帝国の『列車砲』とやらは\x01",
            "どうしても好きになれないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "列車とは戦う道具じゃない。\x01",
            "人と貨物、そして夢を運ぶ\x01",
            "乗り物なのだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2F")

    Jump("loc_28D2")

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E0F")

    #C0052
    ChrTalk(
        0xFE,
        (
            "僕は今、オーバルカメラが\x01",
            "無性に欲しくてたまらないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "……何故って、そりゃあ\x01",
            "列車を写真に収めるためさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ただ、やっぱり\x01",
            "庶民に簡単に手に入るほど\x01",
            "お安いものじゃないんだよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E9B")

    label("loc_1E0F")


    #C0055
    ChrTalk(
        0xFE,
        (
            "カメラマン志望で\x01",
            "クロスベル通信社の門戸を\x01",
            "叩いた事もあったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "さすがに鉄道写真を\x01",
            "撮りたいだけの僕は\x01",
            "不採用だったんだよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9B")

    Jump("loc_28D2")

    label("loc_1EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1F1C")

    #C0057
    ChrTalk(
        0xFE,
        (
            "記念祭が終わって、鉄道の運行本数は\x01",
            "いつもどおりに戻ってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "……はぁ……\x01",
            "なんだか物寂しいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1FA9")

    #C0059
    ChrTalk(
        0xFE,
        (
            "来月の記念祭では\x01",
            "列車を使って沢山の観光客が\x01",
            "訪れるんだろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "……ふふ、列車の勇姿を\x01",
            "しかと目に焼け付けないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_20F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2053")

    #C0061
    ChrTalk(
        0xFE,
        (
            "帝国人の裕福な好事家には、\x01",
            "鉄道の模型を収集している人も\x01",
            "いるそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "なんてうらやましい……！\x01",
            "僕も貴族に生まれればよかった！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20F3")

    label("loc_2053")


    #C0063
    ChrTalk(
        0xFE,
        (
            "鉄道の模型はほとんどが\x01",
            "職人による手作りだから、\x01",
            "とても高価なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "万が一にも大金持ちになれたら、\x01",
            "僕も鉄道模型を眺めながら\x01",
            "老後を過ごしたいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F3")

    Jump("loc_28D2")

    label("loc_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2197")

    #C0065
    ChrTalk(
        0xFE,
        (
            "記念祭が近づいて何が嬉しいって、\x01",
            "列車が大活躍することだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "巣から這い出る虫の大群のように\x01",
            "列車から人が出てくる光景は\x01",
            "圧巻の一言だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_2197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228D")

    #C0067
    ChrTalk(
        0xFE,
        (
            "大陸横断鉄道の線路は、\x01",
            "何年もかけてこつこつと\x01",
            "敷かれていったものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "あれだけ長い線路を\x01",
            "事故が起こらないように敷くのは\x01",
            "なかなか大変だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "まさに、先人たちの努力の賜物だ。\x01",
            "僕もかくありたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_231C")

    label("loc_228D")


    #C0070
    ChrTalk(
        0xFE,
        (
            "大陸横断鉄道の線路、\x01",
            "あれだけ長く正確なものを敷くには\x01",
            "長い年月が必要だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "まさに、先人たちの努力の賜物だ。\x01",
            "僕もかくありたいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231C")

    Jump("loc_28D2")

    label("loc_2321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_23BE")

    #C0072
    ChrTalk(
        0xFE,
        (
            "みんな何故、\x01",
            "鉄道の魅力に気づかないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "クロスベルの歴史を語るのには外せない、\x01",
            "数々の貿易を支えてきた\x01",
            "重要な乗り物だというのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_23BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2488")

    #C0074
    ChrTalk(
        0xFE,
        (
            "僕は子供の頃、\x01",
            "憧れの列車の運転手になりたかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "だけどある時気づいたんだ。\x01",
            "僕は列車を“慈しむ”ことが\x01",
            "好きだということに……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "今では僕も、立派な鉄道マニアさ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2514")

    label("loc_2488")


    #C0077
    ChrTalk(
        0xFE,
        "僕は、列車を慈しむのが好きなのさ。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "子供の頃は運転手になりたかったが……\x01",
            "今なら、どっちかっていうと\x01",
            "駅員になってみたいかな、うん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2514")

    Jump("loc_28D2")

    label("loc_2519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_262D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A2")

    #C0079
    ChrTalk(
        0xFE,
        (
            "大陸横断鉄道が開通したのは\x01",
            "約２０年前のことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "今では鉄道一本で\x01",
            "大陸東端まで行く事が出来るんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2628")

    label("loc_25A2")


    #C0081
    ChrTalk(
        0xFE,
        (
            "今では鉄道一本で\x01",
            "大陸東端まで行く事が出来るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "お金も時間もかかる長旅だけど……\x01",
            "列車好きとしてはいつか行ってみたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2628")

    Jump("loc_28D2")

    label("loc_262D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_27A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272E")

    #C0083
    ChrTalk(
        0xFE,
        "飛行船や列車や自動車……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "あんな大きなものが\x01",
            "空を自由に飛んだり、\x01",
            "陸を猛スピードで駆けたりするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "今じゃ当たり前の技術だけど、\x01",
            "考えてみればすごいことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ロマンを感じる僕の気持ち、\x01",
            "君にだって分かるだろう？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_279C")

    label("loc_272E")


    #C0087
    ChrTalk(
        0xFE,
        "飛行船や列車や自動車……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "僕の嗜好は鉄道寄りだけど、\x01",
            "乗り物にロマンを感じる人は\x01",
            "少なくないはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    Jump("loc_28D2")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_28D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284F")

    #C0089
    ChrTalk(
        0xFE,
        "もしかして駅に行くのかい？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "僕の情報網によると……\x01",
            "共和国行きの列車が\x01",
            "そろそろ到着する頃だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "今の時間帯は\x01",
            "結構混むから気をつけてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28D2")

    label("loc_284F")


    #C0092
    ChrTalk(
        0xFE,
        (
            "共和国行きの列車が\x01",
            "そろそろ到着する頃だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "うーん、急ぎの用がなきゃ\x01",
            "発着の汽笛が鳴るのを\x01",
            "聞いていたいんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D2")

    TalkEnd(0xFE)
    Return()

    # Function_6_1A43 end

    def Function_7_28D6(): pass

    label("Function_7_28D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F4")
    Call(0, 9)
    Jump("loc_295E")

    label("loc_28F4")


    #C0094
    ChrTalk(
        0xFE,
        (
            "まったく、レティナったら\x01",
            "細かい事をぐちぐち……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "……ふふ、まあいいわ。\x01",
            "屋敷に着くのが楽しみ～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295E")

    Jump("loc_2A6D")

    label("loc_2963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A09")

    #C0096
    ChrTalk(
        0xFE,
        "ふぅ、やっと一息ついたわ。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "七耀石の産地クロスベル……\x01",
            "うふふ、ワクワクしてきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "狙いは七耀石の結晶……\x01",
            "必ず手に入れて見せるわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A6D")

    label("loc_2A09")


    #C0099
    ChrTalk(
        0xFE,
        (
            "狙いは七耀石の結晶……\x01",
            "必ず手に入れて見せるわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "と、その前に……\x01",
            "まずは宿を探さないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6D")

    TalkEnd(0xFE)
    Return()

    # Function_7_28D6 end

    def Function_8_2A71(): pass

    label("Function_8_2A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8F")
    Call(0, 9)
    Jump("loc_2B0A")

    label("loc_2A8F")


    #C0101
    ChrTalk(
        0xFE,
        (
            "うう……憂鬱です。\x01",
            "お屋敷に着いたら何を言われるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ああ、女神様。\x01",
            "どうかひどいお仕置きを\x01",
            "受けませんように……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0A")

    Jump("loc_2C01")

    label("loc_2B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC1")

    #C0103
    ChrTalk(
        0xFE,
        (
            "お嬢様と、エレボニア帝国から\x01",
            "七耀石の買い付けに来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "半ば家出のような形で出てきたので\x01",
            "お屋敷では今頃大騒ぎですよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        "……気が重いです……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C01")

    label("loc_2BC1")


    #C0106
    ChrTalk(
        0xFE,
        (
            "結局こんなところまで\x01",
            "来てしまうなんて……\x01",
            "気が重いです……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C01")

    TalkEnd(0xFE)
    Return()

    # Function_8_2A71 end

    def Function_9_2C05(): pass

    label("Function_9_2C05")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    #C0107
    ChrTalk(
        0xA,
        (
            "目的の七耀石の結晶も\x01",
            "手に入れられましたし……\x01",
            "ようやく帝国に帰れますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "この大きな紅耀石#6Rカーネリア#……\x01",
            "お父様の驚く顔が目に浮かびますわ！\x01",
            "おほほほほ！\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "お屋敷から大金を持ち出して\x01",
            "出奔してから４ヶ月近く……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "いきなり帰ってきたら\x01",
            "それは驚かれると思いますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        "……うっさいわね、駄目イド！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        "あう……ひどいです……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_9_2C05 end

    def Function_10_2D84(): pass

    label("Function_10_2D84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F21")

    #C0113
    ChrTalk(
        0xFE,
        (
            "私……やはりお嬢様を\x01",
            "追いかける事にしたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "だって……やっぱり\x01",
            "放っておけないんですもの……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2E98")

    #C0115
    ChrTalk(
        0x101,
        "#0005Fあれ、このメイドさんは……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#0105F確かキャンベル議員の所の……\x02\x03",

            "#0106Fな、なんだか\x01",
            "思いつめてしまったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F16")

    label("loc_2E98")


    #C0117
    ChrTalk(
        0x101,
        "#0005Fあれ、このメイドさんは……？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#0105Fどこかの\x01",
            "お屋敷の人みたいね……\x02\x03",

            "（どこかで見た事のある\x01",
            "  方だけれど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F16")

    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0xEF, 5)
    Jump("loc_2F67")

    label("loc_2F21")


    #C0119
    ChrTalk(
        0xFE,
        (
            "旦那様、ごめんなさい……\x01",
            "でも私、お嬢様の元に\x01",
            "行ってきます……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F67")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D84 end

    def Function_11_2F6B(): pass

    label("Function_11_2F6B")

    TalkBegin(0xFE)

    #C0120
    ChrTalk(
        0xFE,
        (
            "クロスベル駅……\x01",
            "ここで間違いないな、よし。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "広い街だから少し迷ってしまったよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_2F6B end

    def Function_12_2FCB(): pass

    label("Function_12_2FCB")

    TalkBegin(0xFE)

    #C0122
    ChrTalk(
        0xFE,
        (
            "あなた、急ぎましょうよ。\x01",
            "早くしないと列車が出てしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "帰りが遅れたら\x01",
            "あなたのせいですからね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2FCB end

    def Function_13_303E(): pass

    label("Function_13_303E")

    TalkBegin(0xFE)

    #C0124
    ChrTalk(
        0xFE,
        (
            "このクロスベルには\x01",
            "珍しいものがたくさんあるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "いやはや、胸が高鳴るわい。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_303E end

    def Function_14_309C(): pass

    label("Function_14_309C")

    TalkBegin(0xFE)

    #C0126
    ChrTalk(
        0xFE,
        (
            "もう、あなたったら\x01",
            "まるで子供みたいに目を輝かせて。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "ほら、落ち着いてくださいな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_309C end

    def Function_15_30FE(): pass

    label("Function_15_30FE")

    TalkBegin(0xFE)

    #C0128
    ChrTalk(
        0xFE,
        (
            "街道に出ようとしたら、\x01",
            "道行く人に止められてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "うーん、観光には\x01",
            "大人しくバスを使った方が\x01",
            "よさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_30FE end

    def Function_16_3180(): pass

    label("Function_16_3180")

    TalkBegin(0xFE)

    #C0130
    ChrTalk(
        0xFE,
        (
            "ふらっと街道に\x01",
            "出てみたくなる気持ちは\x01",
            "すごくよくわかる。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "こんなに高い建物ばかりじゃ、\x01",
            "田舎育ちには息がつまるよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_3180 end

    def Function_17_3202(): pass

    label("Function_17_3202")

    TalkBegin(0xFE)

    #C0132
    ChrTalk(
        0xFE,
        (
            "ええっと、街の中心は……\x01",
            "あら、駅からすぐそこじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "ふぅ、やっぱり地図を買っておいて\x01",
            "よかったぁ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3202 end

    def Function_18_3279(): pass

    label("Function_18_3279")

    TalkBegin(0xFE)

    #C0134
    ChrTalk(
        0xFE,
        (
            "列車に揺られて……\x01",
            "少々気持ち悪くなってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "うえっぷ……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3279 end

    def Function_19_32C7(): pass

    label("Function_19_32C7")

    TalkBegin(0xFE)

    #C0136
    ChrTalk(
        0xFE,
        (
            "もう、あなたったら\x01",
            "すぐ乗り物酔いするんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "そんなことじゃ、\x01",
            "どこへも観光になんて\x01",
            "行けないじゃないの。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_32C7 end

    def Function_20_3343(): pass

    label("Function_20_3343")

    TalkBegin(0xFE)

    #C0138
    ChrTalk(
        0xFE,
        (
            "来月は記念祭があるだろ？\x01",
            "本当はその時来たかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "人ごみは余り好きじゃないんで、\x01",
            "空いてるうちに色々楽しみに来たのさ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3343 end

    def Function_21_33D4(): pass

    label("Function_21_33D4")

    TalkBegin(0xFE)

    #C0140
    ChrTalk(
        0xFE,
        (
            "あーあ、なんだってこんな\x01",
            "外れた時期に来ちゃったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "人ごみの賑やかな中を\x01",
            "旅行するのが楽しいのに……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_33D4 end

    def Function_22_344B(): pass

    label("Function_22_344B")

    TalkBegin(0xFE)

    #C0142
    ChrTalk(
        0xFE,
        (
            "ＩＢＣビルに\x01",
            "仕事の取り引きに来たのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "さっそく尋ねてみると\x01",
            "しようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_344B end

    def Function_23_34AE(): pass

    label("Function_23_34AE")

    TalkBegin(0xFE)

    #C0144
    ChrTalk(
        0xFE,
        "部長！　お供いたします！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_34AE end

    def Function_24_34D3(): pass

    label("Function_24_34D3")

    TalkBegin(0xFE)

    #C0145
    ChrTalk(
        0xFE,
        "記念祭が過ぎてしまったクロスベル……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "いや、過ぎてしまったからこそ、\x01",
            "商売のチャンスがある！\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        "そうは思わないかね、キミ！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_34D3 end

    def Function_25_355F(): pass

    label("Function_25_355F")

    TalkBegin(0xFE)

    #C0148
    ChrTalk(
        0xFE,
        (
            "センセイ！\x01",
            "そうと決まれば買い付ける商品を\x01",
            "品定めに行きましょう！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_355F end

    def Function_26_35AC(): pass

    label("Function_26_35AC")

    TalkBegin(0xFE)

    #C0149
    ChrTalk(
        0xFE,
        "すっかり日が暮れてしまったな。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "どこかホテルが空いていればいいが……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_35AC end

    def Function_27_3601(): pass

    label("Function_27_3601")

    TalkBegin(0xFE)

    #C0151
    ChrTalk(
        0xFE,
        (
            "なんにしろ、\x01",
            "長旅でおなかペコペコよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "どこかでご飯を食べたいわ～。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_3601 end

    def Function_28_3655(): pass

    label("Function_28_3655")

    TalkBegin(0xFE)

    #C0153
    ChrTalk(
        0xFE,
        "私達、帝国から駈け落ちしてきたの。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "ここならお父様の目も届かない。\x01",
            "きっと２人で幸せになれるわ……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_3655 end

    def Function_29_36C9(): pass

    label("Function_29_36C9")

    TalkBegin(0xFE)

    #C0155
    ChrTalk(
        0xFE,
        (
            "身分違いの恋などしなければ、\x01",
            "彼女を父上と仲違いさせる事もなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "僕はなんて罪深い男なんだ……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "けど……彼女の幸せそうな顔を見ると、\x01",
            "そんな陰鬱な気持ちも\x01",
            "どこかへ吹き飛んでしまうよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_36C9 end

    def Function_30_3797(): pass

    label("Function_30_3797")

    TalkBegin(0xFE)

    #C0158
    ChrTalk(
        0xFE,
        (
            "臨検官さんの検分が\x01",
            "とても念入りに行われていたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "危険物がどうとか言ってたな……\x01",
            "まったく物騒な話だよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_3797 end

    def Function_31_3814(): pass

    label("Function_31_3814")

    TalkBegin(0xFE)

    #C0160
    ChrTalk(
        0xFE,
        (
            "駅のホームが妙にピリピリしてて、\x01",
            "とても居心地が悪かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "何が起こっているのかしら……？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_3814 end

    def Function_32_3880(): pass

    label("Function_32_3880")

    TalkBegin(0xFE)

    #C0162
    ChrTalk(
        0xFE,
        (
            "ホームに着いてるのに、\x01",
            "１時間近くも待たされて\x01",
            "へとへとだわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "クロスベルってのは\x01",
            "こんなに警備に熱心な国だったのかね？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_3880 end

    def Function_33_3908(): pass

    label("Function_33_3908")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_39DD")

    #C0164
    ChrTalk(
        0x2D,
        (
            "特製にがトマトシェイクは\x01",
            "残念ながら普段は\x01",
            "お出しできないんですよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x2D,
        (
            "仕込みが大変な割には\x01",
            "ほとんど売れないので……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x2D,
        (
            "もっぱら市長さんのために\x01",
            "少し用意してるんですよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A6B")

    label("loc_39DD")


    #C0167
    ChrTalk(
        0x2D,
        (
            "あ、市長さんには\x01",
            "お渡しできましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#0000Fはい、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x153,
        "#1109Fどうもありがとー！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x2D,
        "いえいえ、どういたしまして。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3A6B")

    Jump("loc_3AFD")

    label("loc_3A70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x1, 0x4)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AFA")

    #C0171
    ChrTalk(
        0x2D,
        (
            "どうかそのシェイクを\x01",
            "差し入れてあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x2D,
        (
            "市長さんはお得意様ですし、\x01",
            "お世話になっていますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFD")

    label("loc_3AFA")

    Call(0, 34)

    label("loc_3AFD")

    TalkEnd(0xFE)
    Return()

    # Function_33_3908 end

    def Function_34_3B01(): pass

    label("Function_34_3B01")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B88")
    SetChrPos(0x102, -960, 0, 14520, 135)
    Jump("loc_3BCF")

    label("loc_3B88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BAE")
    SetChrPos(0x103, -960, 0, 14520, 135)
    Jump("loc_3BCF")

    label("loc_3BAE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BCF")
    SetChrPos(0x104, -960, 0, 14520, 135)

    label("loc_3BCF")

    OP_93(0x2D, 0x10E, 0x0)
    SetChrSubChip(0x2D, 0x0)
    OP_0D()

    #C0173
    ChrTalk(
        0x2D,
        "#11Pいらっしゃいませー。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x2D,
        (
            "#11P美味しい飲み物は\x01",
            "いかがでしょうか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x153,
        "#12P#1110Fあー、ジュース屋さんだー。\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#6P#0000F普段、噴水広場の方で\x01",
            "営業されている方ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x2D,
        (
            "#11Pあ、はい。\x01",
            "たまにこちらの方でも\x01",
            "営業してるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x2D,
        (
            "#11P嬉しいですねー。\x01",
            "ひょっとしてお気に入りを\x01",
            "買いに来てくれたんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D52")

    #C0179
    ChrTalk(
        0x102,
        "#6P#0102Fはい、実は……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DB5")

    label("loc_3D52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D84")

    #C0180
    ChrTalk(
        0x103,
        "#6P#0200Fいえ、実は……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DB5")

    label("loc_3D84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DB5")

    #C0181
    ChrTalk(
        0x104,
        "#6P#0300Fいや、それがさ……\x02",
    )

    CloseMessageWindow()

    label("loc_3DB5")

    SetChrName("")

    #A0182
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "市長が普段買っている飲み物を\x01",
            "買いに来た事情を説明した。\x02",
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
            "#11Pなるほど、市長さんに\x01",
            "差し入れをするんですね！\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x2D,
        (
            "#11Pそういう事ならお待ちください。\x01",
            "すぐにお作りしますから！\x02",
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
        "#11Pはい、こちらになります。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x358, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F6F")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3FC4")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F9C")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3FC4")

    label("loc_3F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FC4")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3FC4")

    Sleep(1000)

    #C0187
    ChrTalk(
        0x101,
        "#6P#0005Fこ、これって……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4037")

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#0105F確かにおじいさま、\x01",
            "苦いものが大好きだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40C6")

    label("loc_4037")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4088")

    #C0189
    ChrTalk(
        0x103,
        (
            "#6P#0206F……想像しただけで\x01",
            "口の中が苦くなりそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40C6")

    label("loc_4088")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40C6")

    #C0190
    ChrTalk(
        0x104,
        (
            "#6P#0306Fすげぇ……\x01",
            "さすが市長さんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C6")


    #C0191
    ChrTalk(
        0x2D,
        (
            "#11P疲労回復にとってもいいんですけど\x01",
            "あまりに苦すぎるので\x01",
            "隠しメニューなんですよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x2D,
        (
            "#11P……余分に作りましたけど\x01",
            "皆さんも飲んでみます？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#6P#0011Fうっ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "飲んでみる\x01",        # 0
            "遠慮しておく\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D9E")

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#0012Fそ、それじゃあ\x01",
            "ちょっとだけ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4295")

    #C0195
    ChrTalk(
        0x102,
        (
            "#6P#0106Fううっ……\x01",
            "（おじいさまの好物なら\x01",
            "  一応知っておかなくちゃ……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとエリィは\x01",
            "特製にがトマトシェイクを\x01",
            "恐る恐る飲んでみた──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_43AD")

    label("loc_4295")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4316")

    #C0197
    ChrTalk(
        0x103,
        "#6P#0206F……マジですか。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとティオは\x01",
            "特製にがトマトシェイクを\x01",
            "恐る恐る飲んでみた──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_43AD")

    label("loc_4316")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43AD")

    #C0199
    ChrTalk(
        0x104,
        (
            "#6P#0306Fったく、しゃあねえ。\x01",
            "俺も腹を括るかよ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとランディは\x01",
            "特製にがトマトシェイクを\x01",
            "恐る恐る飲んでみた──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43AD")

    Sound(887, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_442E")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_44E9")

    label("loc_442E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_448E")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_44E9")

    label("loc_448E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44E9")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_44E9")

    Sleep(1000)
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "とてつもない苦さが\x01",
            "ノドの奥を通り過ぎていく……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x0, 0x0, 0x101, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(228, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45B1")
    PlayEffect(0x0, 0x1, 0x102, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_4644")

    label("loc_45B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45FD")
    PlayEffect(0x0, 0x1, 0x103, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_4644")

    label("loc_45FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4644")
    PlayEffect(0x0, 0x1, 0x104, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_4644")

    OP_89(0x0, 0x0)
    OP_89(0x1, 0x0)
    SetChrName("")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちのＣＰが上昇した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0x0, 0x5, 0xC8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4692")
    OP_32(0x1, 0x5, 0xC8)
    Jump("loc_46C1")

    label("loc_4692")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46AC")
    OP_32(0x2, 0x5, 0xC8)
    Jump("loc_46C1")

    label("loc_46AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46C1")
    OP_32(0x3, 0x5, 0xC8)

    label("loc_46C1")


    #C0203
    ChrTalk(
        0x101,
        (
            "#6P#0010Fげほっ、げほっ……！\x02\x03",

            "#0006Fた、確かに身体には\x01",
            "いいみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4764")

    #C0204
    ChrTalk(
        0x102,
        (
            "#6P#0110Fちょ、ちょっと初心者には\x01",
            "きつすぎる苦さね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47E8")

    label("loc_4764")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47A2")

    #C0205
    ChrTalk(
        0x103,
        "#6P#0208Fあ、ありえない苦さです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E8")

    label("loc_47A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47E8")

    #C0206
    ChrTalk(
        0x104,
        (
            "#6P#0310Fさ、さすがにキツいな……\x01",
            "この苦さは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E8")


    #C0207
    ChrTalk(
        0x2D,
        "#11Pあはは、ですよねー。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x153,
        "#12P#1111Fんー……\x02",
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
            "キーアは余分に作られた\x01",
            "にがトマトシェイクを手にとって\x01",
            "ストローに口を付けた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_48B9():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48B9)

    def lambda_48C6():
        TurnDirection(0x2D, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_48C6)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4902")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x102, 0x153, 500)
    Jump("loc_4965")

    label("loc_4902")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4936")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x103, 0x153, 500)
    Jump("loc_4965")

    label("loc_4936")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4965")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0x153, 500)

    label("loc_4965")

    Sleep(1000)

    #C0210
    ChrTalk(
        0x101,
        "#6P#0011Fちょ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49B9")

    #C0211
    ChrTalk(
        0x102,
        "#6P#0105Fキ、キーアちゃん！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A1A")

    label("loc_49B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49EB")

    #C0212
    ChrTalk(
        0x103,
        "#6P#0205Fキーア……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A1A")

    label("loc_49EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A1A")

    #C0213
    ChrTalk(
        0x104,
        "#6P#0305Fおい、キー坊！？\x02",
    )

    CloseMessageWindow()

    label("loc_4A1A")


    #C0214
    ChrTalk(
        0x153,
        (
            "#12P#1103Fズズズズズズズ……\x02\x03",

            "#1100Fジュルジュルジュル……\x02\x03",

            "#1109Fぷはーっ！\x01",
            "すっごくおいしーっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AC6")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4B1B")

    label("loc_4AC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AF3")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_4B1B")

    label("loc_4AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B1B")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4B1B")

    Sleep(1000)

    #C0215
    ChrTalk(
        0x101,
        "#6P#0011Fぜ、全部飲んじゃったよ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B83")

    #C0216
    ChrTalk(
        0x102,
        "#6P#0105Fす、凄いわキーアちゃん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF9")

    label("loc_4B83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BBD")

    #C0217
    ChrTalk(
        0x103,
        "#6P#0205Fキーア、凄すぎます……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BF9")

    label("loc_4BBD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BF9")

    #C0218
    ChrTalk(
        0x104,
        (
            "#6P#0302Fキー坊……\x01",
            "すげーじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF9")

    TurnDirection(0x153, 0x101, 500)

    #C0219
    ChrTalk(
        0x153,
        (
            "#12P#1101Fほえー、なんでー？\x02\x03",

            "#1100Fちょっとニガいけど\x01",
            "とってもおいしいーよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#0006Fいや、キーアが平気なら\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x2D,
        (
            "#11Pあははっ……\x01",
            "面白いお嬢さんですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CBD():
        TurnDirection(0x101, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CBD)

    def lambda_4CCA():
        TurnDirection(0x153, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4CCA)

    def lambda_4CD7():
        TurnDirection(0x2D, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4CD7)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CFB")
    TurnDirection(0x102, 0x2D, 500)
    Jump("loc_4D2E")

    label("loc_4CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D17")
    TurnDirection(0x103, 0x2D, 500)
    Jump("loc_4D2E")

    label("loc_4D17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D2E")
    TurnDirection(0x104, 0x2D, 500)

    label("loc_4D2E")


    #C0222
    ChrTalk(
        0x101,
        (
            "#6P#0000Fと、とにかく\x01",
            "ありがとうございました。\x02\x03",

            "俺たちの分も払いますので\x01",
            "お代は幾らになります？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x26, 0x1, 0x3)
    Jump("loc_4F48")

    label("loc_4D9E")


    #C0223
    ChrTalk(
        0x101,
        (
            "#6P#0006Fいや、ちょっと\x01",
            "遠慮しておきます……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x153,
        (
            "#12P#1105Fえー、なんでー？\x02\x03",

            "#1107Fキーア、にがトマトジュース\x01",
            "飲んでみたーい！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E7F")

    #C0225
    ChrTalk(
        0x102,
        (
            "#6P#0102Fあはは……\x01",
            "キーアちゃんにはまだ\x01",
            "早いんじゃないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F12")

    label("loc_4E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EC8")

    #C0226
    ChrTalk(
        0x103,
        (
            "#6P#0200Fキーアにはまだ\x01",
            "早いのではないかと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F12")

    label("loc_4EC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F12")

    #C0227
    ChrTalk(
        0x104,
        (
            "#6P#0300Fやめとけ、キー坊。\x01",
            "口の中がニガニガするぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F12")


    #C0228
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそれで、お代は\x01",
            "幾らになりますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x26, 0x1, 0x4)

    label("loc_4F48")


    #C0229
    ChrTalk(
        0x2D,
        (
            "#11Pいえいえ、今日は特別に\x01",
            "タダにさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x2D,
        (
            "#11P市長さんはお得意様ですし、\x01",
            "お世話になっていますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x2D,
        (
            "#11Pどうかそのシェイクを\x01",
            "差し入れてあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#6P#0005Fで、でも……\x02\x03",

            "#0000F……分かりました。\x01",
            "ありがたくいただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_508E")

    #C0233
    ChrTalk(
        0x102,
        (
            "#6P#0102Fふふ……\x01",
            "市長にも伝えておきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5103")

    label("loc_508E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50CA")

    #C0234
    ChrTalk(
        0x103,
        "#6P#0202F市長にも伝えておきます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5103")

    label("loc_50CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5103")

    #C0235
    ChrTalk(
        0x104,
        "#6P#0302F市長さんにも伝えておくぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_5103")

    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x0, -700, 0, 13150, 90)
    EventEnd(0x5)
    Return()

    # Function_34_3B01 end

    def Function_35_5121(): pass

    label("Function_35_5121")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 0)), scpexpr(EXPR_END)), "loc_5263")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BD(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BD(0x3, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BD(0x2, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BD(0x1, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514A")
    Jump("loc_5263")

    label("loc_514A")


    #C0236
    ChrTalk(
        0x103,
        (
            "#0203F……まだ全員の戦術オーブメントに\x01",
            "クオーツがセットされていません。\x02\x03",

            "#0200F中に入る前に準備をしておきましょう。\x02",
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
            "パーティ全員にクオーツをセットしてください。\x02\x03",

            "キャンプメニューから［ORBMENT］を開き、\x01",
            "［QUARTZ］を選択するとクオーツのセットを行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_5263")

    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x02\x03",

            "ジオフロントＡ区画の鍵で\x01",
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
        1,
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
        (0, "loc_5317"),
        (1, "loc_5357"),
        (SWITCH_DEFAULT, "loc_535C"),
    )


    label("loc_5317")

    Sound(809, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    #A0239
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
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x46, 0)
    OP_C7(0x1, 0x80000)
    Jump("loc_535C")

    label("loc_5357")

    Jump("loc_535C")

    label("loc_535C")

    EventEnd(0x3)
    Return()

    # Function_35_5121 end

    def Function_36_535F(): pass

    label("Function_36_535F")

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

    def lambda_54F3():
        OP_95(0xFE, 900, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_54F3)

    def lambda_550D():
        OP_95(0xFE, -1100, 0, -40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_550D)
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

    def lambda_5689():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5689)

    def lambda_56A3():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_56A3)

    def lambda_56BD():
        OP_97(0xFE, 0x0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_56BD)
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

    # Function_36_535F end

    def Function_37_5717(): pass

    label("Function_37_5717")


    def lambda_571C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_571C)

    def lambda_572D():
        OP_95(0xFE, 600, 0, -1900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_572D)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x3E8)
    Return()

    # Function_37_5717 end

    def Function_38_5751(): pass

    label("Function_38_5751")


    def lambda_5756():
        OP_95(0xFE, -200, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5756)
    WaitChrThread(0x101, 1)

    def lambda_5774():
        OP_95(0xFE, -200, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5774)
    WaitChrThread(0x101, 1)
    Return()

    # Function_38_5751 end

    def Function_39_578E(): pass

    label("Function_39_578E")


    def lambda_5793():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5793)

    def lambda_57A4():
        OP_95(0xFE, 1800, 0, -2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_57A4)
    WaitChrThread(0x24, 1)
    Sleep(500)

    def lambda_57C5():

        label("loc_57C5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_57C5")

    QueueWorkItem2(0xFE, 2, lambda_57C5)
    Return()

    # Function_39_578E end

    def Function_40_57D3(): pass

    label("Function_40_57D3")

    EndChrThread(0x24, 0x2)

    def lambda_57DC():
        OP_95(0xFE, -600, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_57DC)
    WaitChrThread(0x24, 1)

    def lambda_57FA():
        OP_95(0xFE, -600, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_57FA)
    WaitChrThread(0x24, 1)
    Return()

    # Function_40_57D3 end

    def Function_41_5814(): pass

    label("Function_41_5814")


    def lambda_5819():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_5819)

    def lambda_582A():
        OP_95(0xFE, 2000, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_582A)
    WaitChrThread(0x25, 1)
    Sleep(300)

    def lambda_584B():

        label("loc_584B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_584B")

    QueueWorkItem2(0xFE, 2, lambda_584B)
    Return()

    # Function_41_5814 end

    def Function_42_5859(): pass

    label("Function_42_5859")

    EndChrThread(0x25, 0x2)

    def lambda_5862():
        OP_95(0xFE, 400, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_5862)
    WaitChrThread(0x25, 1)

    def lambda_5880():
        OP_95(0xFE, 400, 0, 40000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_5880)
    WaitChrThread(0x25, 1)
    Return()

    # Function_42_5859 end

    def Function_43_589A(): pass

    label("Function_43_589A")

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

    def lambda_5A1C():
        OP_95(0xFE, -500, 0, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5A1C)
    Sleep(500)

    def lambda_5A39():
        OP_95(0xFE, -1300, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A39)
    Sleep(50)

    def lambda_5A56():
        OP_95(0xFE, 300, 0, 18000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A56)
    Sleep(50)

    def lambda_5A73():
        OP_95(0xFE, -1300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A73)
    Sleep(50)

    def lambda_5A90():
        OP_95(0xFE, 300, 0, 19600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A90)
    OP_68(-500, 1000, 18800, 4000)
    FadeToBright(2000, 0)
    WaitChrThread(0x23, 1)

    def lambda_5AC8():
        OP_95(0xFE, -8500, -2800, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5AC8)
    WaitChrThread(0x101, 1)

    def lambda_5AE6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AE6)
    WaitChrThread(0x102, 1)

    def lambda_5AF7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5AF7)
    WaitChrThread(0x104, 1)

    def lambda_5B08():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5B08)
    WaitChrThread(0x103, 1)

    def lambda_5B19():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5B19)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)

    #C0240
    ChrTalk(
        0x101,
        "#12P#0005Fここは……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#12P#0105F駅前通りの外れ……\x01",
            "一体、何があるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        (
            "#11P#0306F後始末とか言ってたが……\x02\x03",

            "#0301Fまさか資材を片付けろとか\x01",
            "言うんじゃないだろうな？\x02",
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

    def lambda_5CBD():
        OP_95(0x23, -19500, -5000, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5CBD)
    Sleep(300)

    def lambda_5CDA():
        OP_95(0x101, -22500, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CDA)
    Sleep(50)

    def lambda_5CF7():
        OP_95(0x102, -21540, -5000, 16100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CF7)
    Sleep(50)

    def lambda_5D14():
        OP_95(0x103, -20900, -5000, 17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D14)
    Sleep(50)

    def lambda_5D31():
        OP_95(0x104, -19900, -5000, 16700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D31)
    WaitChrThread(0x23, 1)

    def lambda_5D4F():
        OP_95(0xFE, -22500, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5D4F)
    WaitChrThread(0x23, 1)
    OP_93(0x23, 0x0, 0x2BC)
    WaitChrThread(0x101, 1)

    def lambda_5D78():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D78)
    WaitChrThread(0x102, 1)

    def lambda_5D89():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D89)
    WaitChrThread(0x103, 1)

    def lambda_5D9A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D9A)
    WaitChrThread(0x104, 1)

    def lambda_5DAB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DAB)
    OP_93(0x23, 0xB4, 0x1F4)

    def lambda_5DBF():

        label("loc_5DBF")

        TurnDirection(0x101, 0x23, 500)
        Yield()
        Jump("loc_5DBF")

    QueueWorkItem2(0x101, 2, lambda_5DBF)

    def lambda_5DD1():

        label("loc_5DD1")

        TurnDirection(0x102, 0x23, 500)
        Yield()
        Jump("loc_5DD1")

    QueueWorkItem2(0x102, 2, lambda_5DD1)

    def lambda_5DE3():

        label("loc_5DE3")

        TurnDirection(0x103, 0x23, 500)
        Yield()
        Jump("loc_5DE3")

    QueueWorkItem2(0x103, 2, lambda_5DE3)

    def lambda_5DF5():

        label("loc_5DF5")

        TurnDirection(0x104, 0x23, 500)
        Yield()
        Jump("loc_5DF5")

    QueueWorkItem2(0x104, 2, lambda_5DF5)
    OP_6F(0x51)

    #C0244
    ChrTalk(
        0x23,
        (
            "#5P#1003F──ここから先は、\x01",
            "クロスベル市の地下に広がる\x01",
            "『ジオフロント区画』になる。\x02\x03",

            "#1000F今から、この中に潜ってもらう。\x02",
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
        "#12P#0005Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        "#12P#0105Fも、潜るって……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x104,
        (
            "#11P#0301Fおいおい。\x01",
            "どういうことッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x23,
        (
            "#5P#1004Fお前たちの総合能力、\x01",
            "および実戦テストのためだ。\x02\x03",

            "#1002Fジオフロント内部は\x01",
            "それほど手強くはないが\x01",
            "魔獣のたぐいが徘徊している。\x02\x03",

            "それらを掃討しながら\x01",
            "一番奥まで行ってもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        "#12P#0100Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#11P#0304F実戦テストか。\x01",
            "ま、それなら気が楽かね。\x02",
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
            "#12P#0011Fちょ、ちょっと待ってください！\x02\x03",

            "#0003Fテストはともかく……\x01",
            "どうして魔獣の徘徊する場所に\x01",
            "わざわざ入る必要があるんですか？\x02\x03",

            "#0001F警備隊じゃあるまいし……\x01",
            "捜査官の仕事じゃないですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x23,
        (
            "#5P#1004Fクク、確かに普通は\x01",
            "捜査官の仕事じゃないだろう。\x02\x03",

            "#1001F──だが、特務支援課に\x01",
            "所属するメンバーは話が別だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#12P#0011Fえ゛……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x23,
        (
            "#5P#1000F──詳しい説明は後だ。\x02\x03",

            "まずはコイツを受け取れ。\x02",
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
            "セルゲイはロイドたちに\x01",
            "携帯端末らしきものを手渡した。\x07\x00\x02",
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
        "#0005Fこれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0257
    AnonymousTalk(
        0x102,
        "#0105F新型の戦術オーブメント？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0258
    AnonymousTalk(
        0x104,
        (
            "#0305Fへえ……\x01",
            "ずいぶん洒落たデザインだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0259
    AnonymousTalk(
        0x103,
        (
            "#0203F第５世代戦術オーブメント、\x01",
            "通称『ＥＮＩＧＭＡ#12Rエ　　ニ　　グ　　マ#』……\x02\x03",

            "#0200Fようやく実戦配備ですか。\x02",
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
            "#6P#1002Fああ、財団の方から\x01",
            "先日届いたばかりの新品だ。\x02\x03",

            "お前たちの適性に合わせて\x01",
            "すでに調整もされている。\x02\x03",

            "#1004F使い方は──ティオ。\x01",
            "お前がレクチャーしてやれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#11P#0203F……面倒だけど了解です。\x02\x03",

            "#0200F新型用の結晶回路#8Rク オ ー ツ#はありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x23,
        "#6P#1002Fああ、少ないが受け取れ。\x02",
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
            "各種の結晶回路\x07\x00",
            "を手に入れた。\x02",
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
        "#5P#1000Fそれと、肝心のこいつだ。\x02",
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x321, 1)

    #C0266
    ChrTalk(
        0x23,
        (
            "#5P#1003Fそれじゃあ、一通り魔獣を\x01",
            "掃討したら本部に戻って来い。\x02\x03",

            "細かい話はその後してやろう。\x02\x03",

            "#1005Fおっと──ついでに\x01",
            "こいつも渡しておくぞ。\x02",
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
            "を手に入れた。\x02",
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
            "を手に入れた。\x02",
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
            "※『捜査手帳』について。\x02\x03",

            "※『捜査手帳』には、\x01",
            "  ゲーム中で起こった様々な出来事が\x01",
            "  自動的に記録されていきます。\x02\x03",

            "※キャンプメニューから［ITEMS］を開いて\x01",
            "  『捜査手帳』を使用するか、\x01",
            "  フィールド上で『△ボタン＋方向キー左』で\x01",
            "  内容を見ることが出来ます。 \x02\x03",

            "※マニュアルなども確認できるので、\x01",
            "  活用してください。\x07\x00\x02",
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
            "※『戦闘手帳』について。\x02\x03",

            "※『戦闘手帳』には、\x01",
            "  戦闘で戦った相手の情報が\x01",
            "  自動的に記録されていきます。\x02\x03",

            "※捜査手帳と同じく、\x01",
            "  アイテムの『戦闘手帳』を使用する、\x01",
            "  もしくは『△ボタン＋方向キー右』で\x01",
            "  内容を見ることが出来ます。 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1, 1)
    AddItemNumber(0x4, 1)
    OP_68(-19500, -3900, 17500, 3000)

    def lambda_6969():
        OP_95(0xFE, -20000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6969)
    WaitChrThread(0x23, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6999():
        OP_95(0xFE, -17500, -5000, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6999)
    #Sound(1082, 255, 100, 0)    #voice#Lloyd

    #C0271
    ChrTalk(
        0x101,
        "#6P#0011Fちょ、ちょっと課長！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 1)
    OP_6F(0x1)
    TurnDirection(0x23, 0x101, 500)

    #C0272
    ChrTalk(
        0x23,
        (
            "#11P#1002F──ああ、それとロイド。\x02\x03",

            "とりあえずお前、リーダーな。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#6P#0005Fへっ……\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x23,
        (
            "#11P#1004F今の所、捜査官としての\x01",
            "正式な資格を持っているのは\x01",
            "お前だけなんだよ。\x02\x03",

            "そんじゃあ任せたぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x5A, 0x1F4)

    def lambda_6AB9():
        OP_95(0xFE, -8500, -2800, 17500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6AB9)
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

    def lambda_6B7F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B7F)
    Sleep(50)

    def lambda_6B8F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B8F)
    Sleep(50)

    def lambda_6B9F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B9F)
    WaitChrThread(0x103, 1)
    #Sound(1362, 255, 100, 0)    #voice#Randy

    #C0275
    ChrTalk(
        0x104,
        (
            "#12P#0309Fハッハッハ。\x01",
            "押し付けられちまったなぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#12P#0104Fふふ、でも捜査官の資格を\x01",
            "持っている人がいて心強いです。\x02\x03",

            "#0102Fロイドさん。\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0277
    ChrTalk(
        0x101,
        (
            "#0000F#5Pあ……\x01",
            "いや、呼び捨てでいいよ。\x02\x03",

            "見たところ歳も近いみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそう？\x01",
            "ちなみに私は１８だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#0000F#5Pああ、それなら同い歳だ。\x02\x03",

            "#0005Fえっと、あなたたちは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#12P#0304F俺は２１だが、\x01",
            "堅苦しいからタメ口でいいぜ。\x02\x03",

            "#0300Fよろしくな、ロイド、エリィ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0281
    ChrTalk(
        0x102,
        "#6P#0102Fええ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        "#0002F#5Pああ、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#0001F……えっと……\x01",
            "それで、君の方は……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E20():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E20)
    Sleep(50)

    def lambda_6E30():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E30)
    WaitChrThread(0x102, 1)

    #C0284
    ChrTalk(
        0x103,
        "#11P#0203F──１４ですが、問題が？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0285
    ChrTalk(
        0x101,
        (
            "#6P#0012Fい、いや～。\x01",
            "別に問題があるわけじゃ……\x02",
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
        "#6P#0011Fって、#4S１４歳ッ！？#3S\x02",
    )

    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        (
            "#12P#0309Fハハ、なんだ。\x01",
            "見た通りの歳ってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        (
            "#6P#0105F驚いた……そんな若くて\x01",
            "警察に入れるものなのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#6P#0011Fいやいや！\x01",
            "どう考えてもおかしいから！\x02\x03",

            "#0006Fたしか一般の警察官でも\x01",
            "１６歳以上だったはずだし……\x02\x03",

            "#0001F日曜学校も卒業していない子が\x01",
            "どうして警察なんかに──\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        (
            "#11P#0200F……正確に言うと\x01",
            "わたしは警察官ではないです。\x02\x03",

            "エプスタイン財団から出向した\x01",
            "テスト要員ですので。\x02",
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
        "#6P#0005Fへっ……！？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        (
            "#12P#0305Fエプスタインっていやあ、\x01",
            "さっきの戦術オーブメントの……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#6P#0104Fそう……なるほどね。\x02\x03",

            "#0100Fここ数年、クロスベル市が\x01",
            "財団と協力して大規模な計画を\x01",
            "進めているのは聞いていたけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0294
    ChrTalk(
        0x103,
        (
            "#5P#0200F『導力ネットワーク計画』ですね。\x02\x03",

            "そちらにも少しは関わっていますが\x01",
            "わたしの出向目的は別にあります。\x02",
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
        "#0005Fそれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0296
    AnonymousTalk(
        0x102,
        "#0105F機械仕掛けの……杖？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0297
    AnonymousTalk(
        0x103,
        (
            "#0204F『魔導杖#6Rオーバルスタッフ#』といいます。\x02\x03",

            "この新武装の実戦テストのため\x01",
            "わたしは財団から出向しました。\x02\x03",

            "#0200F……ロイドさん。\x01",
            "ご理解いただけましたか？\x02",
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
            "#6P#0001Fちょ、ちょっと待ってくれ！\x02\x03",

            "もしかして……\x01",
            "その杖を使って君も戦うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#11P#0203F……捜査官の資格があるのに\x01",
            "ずいぶん察しが悪いんですね。\x02\x03",

            "#0211F『実戦』テストのために\x01",
            "出向したと言いましたが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#6P#0011Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        (
            "#12P#0304Fまあまあ。\x01",
            "ここでモメても仕方ないぜ。\x02\x03",

            "#0300Fこの先のジオフロントってのが\x01",
            "どれだけ危険かは知らないが……\x02\x03",

            "まずは、あのオッサンが\x01",
            "押し付けてきた任務#4Rミッション#を\x01",
            "クリアする事を考えようや。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        (
            "#6P#0103Fそうね……\x01",
            "納得できない事も多いけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#6P#0006F………分かった。\x02\x03",

            "#0000Fすまない、ティオ。\x01",
            "気分を悪くしたら謝るよ。\x02",
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
            "#11P#0203F別に……あなたの反応は\x01",
            "常識的だとは思いますから。\x02\x03",

            "#0200Fところで、わたしの武装は\x01",
            "この『魔導杖』ですが……\x02\x03",

            "皆さんの武装は何ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#6P#0005Fああ、それじゃあ──\x02\x03",

            "#0000F俺の得物は、これだよ。\x02",
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

    def lambda_7723():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7723)
    Sleep(50)

    def lambda_7733():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7733)
    Sleep(50)

    def lambda_7743():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7743)
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
        "#0105Fそれは、警棒の一種……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0307
    AnonymousTalk(
        0x104,
        (
            "#0300Fトンファーか。\x01",
            "東方で使われる武具だな。\x02\x03",

            "殺傷力よりも防御と制圧力に\x01",
            "優れているらしいが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0308
    AnonymousTalk(
        0x102,
        (
            "#0102Fなるほど。\x01",
            "警察官らしい装備ね。\x02",
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
            "#0004F#5P色々試してみたんだけど\x01",
            "これが一番しっくり来てね。\x02\x03",

            "#0000Fで、エリィとランディの得物は？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#12P#0100F私は……これね。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    OP_93(0x102, 0x0, 0x0)
    OP_0D()

    def lambda_7930():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7930)
    Sleep(50)

    def lambda_7940():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7940)
    Sleep(50)

    def lambda_7950():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7950)
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
            "#0205F導力銃……\x01",
            "少し古いタイプですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0312
    AnonymousTalk(
        0x101,
        "#0005Fずいぶん綺麗な銃だな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0313
    AnonymousTalk(
        0x102,
        (
            "#0102F競技用に特別に\x01",
            "カスタムしてもらったものよ。\x02\x03",

            "旧式だけど、狙いの正確さは\x01",
            "期待してくれてもいいと思う。\x02",
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
            "#11P#0302Fおっ、自信満々だねぇ。\x02\x03",

            "#0300Fそんじゃあ、俺はコイツだ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -19500, -5000, 17300, 270)
    OP_0D()

    def lambda_7B04():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7B04)
    Sleep(50)

    def lambda_7B14():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B14)
    Sleep(50)

    def lambda_7B24():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B24)
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
            "#0001Fそれは……\x01",
            "ずいぶん大きな武器だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0316
    AnonymousTalk(
        0x102,
        (
            "#0101F中世の騎士が使っていた\x01",
            "ハルバードみたいな形ね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0317
    AnonymousTalk(
        0x103,
        (
            "#0200F……財団の武器工房で\x01",
            "見かけたことがあります。\x02\x03",

            "導力を衝撃力に変換する\x01",
            "ユニットが付いていますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0318
    AnonymousTalk(
        0x104,
        (
            "#0304Fああ、スタンハルバードだ。\x02\x03",

            "#0300Fちょいと重くて扱いにくいが\x01",
            "一撃の威力は中々のもんだぜ。\x02",
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
            "#0003F#5Pなるほど……\x02\x03",

            "#0000Fティオの杖が、どういうものかは\x01",
            "判らないけれど……\x02\x03",

            "魔獣との戦闘になったら\x01",
            "バランスよく戦えそうだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D82():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D82)
    Sleep(50)

    def lambda_7D92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7D92)
    WaitChrThread(0x103, 1)

    #C0320
    ChrTalk(
        0x102,
        "#12P#0100F確かに……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、そのあたりも考えて\x01",
            "俺たちを集めたのかもしれんな。\x02\x03",

            "あのオッサン、とぼけた顔して\x01",
            "結構したたかそうだったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        (
            "#11P#0203F……そうですね。\x02\x03",

            "#0200Fわたしの魔導杖の性能は\x01",
            "おいおい説明するとして……\x02\x03",

            "先ほど支給された、\x01",
            "戦術オーブメントの性能を\x01",
            "説明しますか？\x02",
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
            "説明してもらう\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7F1F"),
        (1, "loc_8A0A"),
        (SWITCH_DEFAULT, "loc_8CC8"),
    )


    label("loc_7F1F")


    def lambda_7F24():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7F24)
    Sleep(50)

    def lambda_7F34():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7F34)
    Sleep(50)

    def lambda_7F44():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F44)
    Sleep(50)

    #C0323
    ChrTalk(
        0x101,
        "#0002F#5Pああ、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#11P#0203F……了解しました。\x02\x03",

            "#0200F一般的に《導力器#6Rオーブメント#》というのは、\x01",
            "導力エネルギーを利用して\x01",
            "様々な現象を起こす機械のことです。\x02\x03",

            "照明や冷暖房などの日用品から\x01",
            "車や鉄道の動力にも\x01",
            "オーブメントの力が使われていますね。\x02\x03",

            "《戦術オーブメント》とは、\x01",
            "これを個人の戦闘用に特化させた\x01",
            "小型の携帯導力器を指します。\x02\x03",

            "#0203F今回支給されたのは、\x01",
            "『エプスタイン財団』で開発された\x01",
            "その最新型です。\x02\x03",

            "従来の物と同じく、\x01",
            "『クオーツ』と呼ばれる結晶回路を\x01",
            "セットすることで作動します。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        (
            "#6P#0105F結晶回路#8Rク オ ー ツ#……\x01",
            "七耀石の欠片から作られる\x01",
            "オーブメント用の回路のことね。\x02\x03",

            "#0100Fさっき課長にいくつか\x01",
            "渡されたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        (
            "#11P#0200Fええ、それを戦術オーブメントの\x01",
            "開封されているスロットに\x01",
            "はめ込むことで、効力を発揮します。\x02\x03",

            "そして、クオーツをセットしたラインの\x01",
            "『属性値』が一定に達すると、\x01",
            "導力魔法#8Rオーバルアーツ#の使用が可能になるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#5P#0004F魔獣の種類によっては、\x01",
            "武器による直接攻撃よりも魔法#4Rアーツ#の方が\x01",
            "有効なこともあるんだ。\x02\x03",

            "#0000Fだから、魔獣との戦闘に入る前に\x01",
            "きちんと用意しておかないと\x01",
            "いけないのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#6P#0100Fなるほど……\x01",
            "魔獣と戦うための\x01",
            "とても重要な要素というわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        (
            "#12P#0304F遊撃士協会や警備隊でも\x01",
            "採用されてるくらいだしな。\x01",
            "そう思って間違いないと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x103,
        (
            "#11P#0208Fあとは……そうですね。\x02\x03",

            "#0200F戦術オーブメントは\x01",
            "個人の特性に合わせて調整されているので\x01",
            "持ち主によって構造が異なるんです。\x02\x03",

            "人によって属性限定のスロットや\x01",
            "スロットを結ぶ線#2Rライン#の形が違うはずです。\x02\x03",

            "#0203Fまあ、どこが違うのかは\x01",
            "後で見比べていただければ分かるかと。\x02\x03",

            "#0200F導力魔法#8Rア  ー  ツ#の詳しい使い方は\x01",
            "実戦で覚えたほうがいいでしょうし……\x01",
            "説明はこんな所でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#6P#0102Fおかげでよく分かったわ。\x01",
            "ありがとう、ティオちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#11P#0203F……どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        (
            "#12P#0305Fてか、新型って言っても、\x01",
            "昔のと使い方はあまり\x01",
            "変わらねぇみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x103,
        (
            "#11P#0203Fええ、旧タイプの使用経験があれば\x01",
            "今まで通りの感覚で扱えるはずです。\x02\x03",

            "#0200Fどちらかというと\x01",
            "今回のバージョンアップは\x01",
            "別機能の追加が主ですし……\x02",
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
        "#5P#0005F……別機能って？\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x103,
        (
            "#11P#0204Fまぁ、現時点では関係ないので\x01",
            "あまりお気になさらず。\x02\x03",

            "#0200Fそれよりも、今は任務の遂行を\x01",
            "優先しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#5P#0000Fあ、ああ、そうだな。\x01",
            "（……微妙に気になるけど……）\x02\x03",

            "#0004F……とりあえず、\x01",
            "ジオフロントに入る前に\x01",
            "戦術オーブメントの準備をしておこう。\x02\x03",

            "#0000F課長に渡されたクオーツをセットして、\x01",
            "それから中に入るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        "#12P#0100Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x104,
        "#12P#0300Fんじゃ、とっとと支度するとしますか。\x02",
    )

    CloseMessageWindow()
    AddItemNumber(0x64, 1)
    AddItemNumber(0x6A, 1)
    AddItemNumber(0x6D, 1)
    AddItemNumber(0x79, 1)
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
            "パーティ全員にクオーツをセットしてください。\x02\x03",

            "キャンプメニューから［ORBMENT］を開き、\x01",
            "［QUARTZ］を選択するとクオーツのセットを行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x44, 0)
    OP_C7(0x0, 0x80000)
    Jump("loc_8CC8")

    label("loc_8A0A")


    def lambda_8A0F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A0F)
    Sleep(50)

    def lambda_8A1F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8A1F)
    Sleep(50)

    def lambda_8A2F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A2F)
    Sleep(50)

    #C0341
    ChrTalk(
        0x101,
        (
            "#5P#0000Fいや……大丈夫だよ。\x02\x03",

            "見たところ、使い方は\x01",
            "従来のものとほとんど\x01",
            "変わっていないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        (
            "#11P#0203Fまぁ、そうですね。\x02\x03",

            "#0200Fどちらかというと\x01",
            "今回のバージョンアップは\x01",
            "別機能の追加が主ですし……\x02",
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
        "#5P#0005F……別機能って？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x103,
        (
            "#11P#0204Fまぁ、現時点では関係ないので\x01",
            "あまりお気になさらず。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#5P#0006F（……微妙に気になるけど……）\x02\x03",

            "#0000Fそれじゃあ……\x01",
            "とにかく中に入ってみよう。\x02\x03",

            "まずは安全に気をつけて\x01",
            "進んだ方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x102,
        "#12P#0100Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x103,
        "#11P#0200F……了解です。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        "#12P#0300Fんじゃ、行くとしますか。\x02",
    )

    CloseMessageWindow()
    OP_42(0x0, 0x6D, 0x0)
    OP_42(0x1, 0x79, 0x0)
    OP_42(0x2, 0x64, 0x0)
    OP_42(0x3, 0x6A, 0x0)
    Jump("loc_8CC8")

    label("loc_8CC8")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DE(0x0, 0x0)"), scpexpr(EXPR_END)), "loc_8FAE")
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
            "※捜査手帳を受け取ったことで、\x01",
            "  『新米捜査官』の実績を獲得しました。\x02\x03",

            "※このように、ゲームの進行中に\x01",
            "  ある一定の条件を満たすと\x01",
            "  『実績』を獲得することができます。\x02\x03",

            "※『実績』にはポイントがあり、\x01",
            "  ゲーム本編をクリアした後に\x01",
            "  それを使って様々な機能を解放できます。\x02\x03",

            "※キャンプメニューから［SYSTEM］を開き、\x01",
            "  ［RECORD］を選択すると\x01",
            "  獲得した実績を確認することができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToBright(300, 0)

    label("loc_8FAE")

    EventEnd(0x5)
    Return()

    # Function_43_589A end

    def Function_44_8FB1(): pass

    label("Function_44_8FB1")

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

    def lambda_909D():

        label("loc_909D")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_909D")

    QueueWorkItem2(0x198, 2, lambda_909D)

    def lambda_90AF():

        label("loc_90AF")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_90AF")

    QueueWorkItem2(0x197, 2, lambda_90AF)
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
        "#6P#0005Fなんだ……？\x02",
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
            "いや～、アリオスさん！\x01",
            "またしてもお手柄でしたねぇ！\x02\x03",

            "ずさんな市の施設管理の下、\x01",
            "危機に陥ってしまった少年たちを\x01",
            "鮮やかに救出した手際のよさ……！\x02\x03",

            "最新号にバッチリ\x01",
            "スクープさせてもらいますから！\x02",
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
            "#5Pすっげええ！\x01",
            "オレたち雑誌に載っちゃうの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x197,
        (
            "#1Pで、でもそれって、\x01",
            "何かうれしくないような……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x27,
        (
            "#6P#1403F……グレイス。\x01",
            "あまり騒ぎ立てないでくれ。\x02\x03",

            "#1400F確かに市の管理も問題だが\x01",
            "この子たちの行動にも問題がある。\x02\x03",

            "偏#2Rかたよ#った記事には感心しないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #N0355
    NpcTalk(
        0x26,
        "女性",
        (
            "#11P#2109Fいえいえ、あくまで読者の\x01",
            "ニーズに応えているだけですから♪\x02\x03",

            "#2102F──それに今回は\x01",
            "面白いゲストもいるみたいですし。\x02",
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

    def lambda_9588():
        OP_96(0xFE, 0xFFFFB9B0, 0xFFFFEC78, 0x3E80, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_9588)
    WaitChrThread(0x26, 1)

    def lambda_95A6():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x44C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_95A6)
    Sleep(500)

    def lambda_95C3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_95C3)
    WaitChrThread(0x26, 1)
    OP_6F(0x11)
    BeginChrThread(0x26, 3, 0, 46)

    #N0357
    NpcTalk(
        0x26,
        "女性",
        (
            "#11P#2104Fクロスベル警察の未来を背負う\x01",
            "『特務支援課』初めての出動！\x02\x03",

            "しかし力及ばず、いつもと同じように\x01",
            "遊撃士に手柄を奪われるのだった！\x02\x03",

            "#2110Fああ、未熟さを痛感した若者たちは\x01",
            "果たしてこの先に待ち受ける\x01",
            "数々の試練を乗り越えられるのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        "#6P#0011Fな、なにを……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x104,
        (
            "#6P#0301F（おいおい……\x01",
            "  一体なんだってんだ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x103,
        (
            "#6P#0200F（マスコミの人間\x01",
            "  みたいですけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x102,
        (
            "#6P#0106F（……どうやら\x01",
            "  《クロスベルタイムズ》の\x01",
            "  記者の人みたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x27,
        (
            "#11P#1403F──彼らに関しても\x01",
            "決め付けはあまり感心しない。\x02\x03",

            "一応、この子たちを\x01",
            "最初に助けたのは彼らだ。\x02\x03",

            "#1400Fまあ、ツメは甘かったようだが。\x02",
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
            "#11P#2106Fあらら、やっぱりそうなんだ。\x02\x03",

            "#2100Fま、記事で色々書くと思うけど\x01",
            "あんまり気にしないでね？\x02\x03",

            "#2109Fお姉さんからのエールだと思って\x01",
            "これからも頑張ってちょうだい。\x02",
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
            "#6P#2110F──それで、アリオスさん。\x01",
            "一度、独占インタビューをですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x27,
        (
            "#11P#1403Fそれに関しても\x01",
            "前に断っているはずだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x5A, 0x1F4)
    EndChrThread(0x198, 0x2)
    EndChrThread(0x197, 0x2)

    def lambda_99B2():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_99B2)

    def lambda_99CC():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_99CC)

    def lambda_99D9():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_99D9)
    Sleep(400)
    BeginChrThread(0x198, 3, 0, 51)
    Sleep(400)
    BeginChrThread(0x197, 3, 0, 52)
    Sleep(400)

    def lambda_99FB():
        OP_97(0xFE, 0x3A98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_99FB)
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
        "#6P#0211F……何でしょう、今の。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        (
            "#0301F#6P俺たちのことをピエロに\x01",
            "仕立てようって肚#2Rハラ#みてぇだが……\x02\x03",

            "#0306F結構好みのお姉さんだけど\x01",
            "ちょいとクセがありそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x102,
        (
            "#0106F#6Pふう……\x01",
            "そんな問題じゃないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0370
    ChrTalk(
        0x102,
        "#0101F#5Pそれでロイド、どうするの？\x02",
    )

    CloseMessageWindow()

    def lambda_9BDA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BDA)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0371
    ChrTalk(
        0x101,
        (
            "#11P#0005Fあ、ああ……\x02\x03",

            "#0006F……セルゲイ課長が出した\x01",
            "課題はクリアしたし……\x01",
            "いったん警察本部に戻ろう。\x02\x03",

            "#0008F子供たちの件についても\x01",
            "きちんと報告しないと……\x02",
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
        "#11P#0011Fこれは……\x02",
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
            "#0005F#11Pさっき貰った\x01",
            "戦術オーブメント……\x02\x03",

            "#0001Fもしかして通信が\x01",
            "入ってきているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        (
            "#0203F#6Pええ、そうみたいですね。\x02\x03",

            "#0200Fそこの赤いボタンを押せば\x01",
            "通信モードに切り替わります。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#0000F#11Pああ、これか……\x02",
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
            "#0001Fえっと……\x01",
            "ロイド・バニングスです。\x02\x03",

            "セルゲイ課長ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("娘の声")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ロイドさん！\x02\x03",

            "あの、わたしです。\x01",
            "先ほど受付でお会いした──\x02",
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
            "#0005Fあ、さっきの……\x02\x03",

            "#0000Fえっと、一体どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("受付嬢の声")

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "えっと、それがですね……\x02\x03",

            "その、急いで警察本部に\x01",
            "戻ってきていただけますか？\x02\x03",

            "何でも副局長がお呼びみたいで……\x02",
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
            "#0011Fふ、副局長……？\x02",
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

    # Function_44_8FB1 end

    def Function_45_A024(): pass

    label("Function_45_A024")

    Sleep(1000)

    label("loc_A027")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A119")
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_A03F():
        OP_96(0xFE, 0xFFFFC180, 0xFFFFEC78, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A03F)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_A0B0():
        OP_96(0xFE, 0xFFFFC180, 0xFFFFEC78, 0x44C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A0B0)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_A027")

    label("loc_A119")

    Return()

    # Function_45_A024 end

    def Function_46_A11A(): pass

    label("Function_46_A11A")

    Sleep(1000)

    label("loc_A11D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A20F")
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_A135():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x4394, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A135)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)

    def lambda_A1A6():
        OP_96(0xFE, 0xFFFFB118, 0xFFFFEC78, 0x45EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A1A6)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    Sleep(50)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x26, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_A11D")

    label("loc_A20F")

    Return()

    # Function_46_A11A end

    def Function_47_A210(): pass

    label("Function_47_A210")


    def lambda_A215():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A215)

    def lambda_A226():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A226)
    WaitChrThread(0x101, 1)

    def lambda_A244():
        OP_95(0xFE, -21700, -5000, 17100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A244)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_47_A210 end

    def Function_48_A265(): pass

    label("Function_48_A265")


    def lambda_A26A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A26A)

    def lambda_A27B():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A27B)
    WaitChrThread(0x102, 1)

    def lambda_A299():
        OP_95(0xFE, -22500, -5000, 17700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A299)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_48_A265 end

    def Function_49_A2BA(): pass

    label("Function_49_A2BA")


    def lambda_A2BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A2BF)

    def lambda_A2D0():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2D0)
    WaitChrThread(0x103, 1)

    def lambda_A2EE():
        OP_95(0xFE, -23900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2EE)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_49_A2BA end

    def Function_50_A30F(): pass

    label("Function_50_A30F")


    def lambda_A314():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A314)

    def lambda_A325():
        OP_95(0xFE, -22000, -5000, 19500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A325)
    WaitChrThread(0x104, 1)

    def lambda_A343():
        OP_95(0xFE, -22700, -5000, 19100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A343)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x5A, 0x1F4)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_50_A30F end

    def Function_51_A370(): pass

    label("Function_51_A370")


    def lambda_A375():
        OP_95(0xFE, -16000, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A375)
    WaitChrThread(0xFE, 1)

    def lambda_A393():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A393)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_51_A370 end

    def Function_52_A3AD(): pass

    label("Function_52_A3AD")


    def lambda_A3B2():
        OP_95(0xFE, -16900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3B2)
    WaitChrThread(0xFE, 1)

    def lambda_A3D0():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_A3AD end

    def Function_53_A3EA(): pass

    label("Function_53_A3EA")

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

    def lambda_A5D3():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A5D3)
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

    # Function_53_A3EA end

    def Function_54_A64C(): pass

    label("Function_54_A64C")


    def lambda_A651():
        OP_96(0xFE, 0xFFFEC780, 0xFFFFD314, 0xFFFFD314, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_A651)
    WaitChrThread(0x28, 1)
    Return()

    # Function_54_A64C end

    def Function_55_A66B(): pass

    label("Function_55_A66B")

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

    def lambda_A776():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A776)

    def lambda_A787():
        OP_96(0xFE, 0xFFFFA7B8, 0xFFFFEC78, 0x477C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A787)
    Sleep(400)

    def lambda_A7A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A7A4)

    def lambda_A7B5():
        OP_96(0xFE, 0xFFFFACCC, 0xFFFFEC78, 0x477C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7B5)
    Sleep(400)

    def lambda_A7D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A7D2)

    def lambda_A7E3():
        OP_96(0xFE, 0xFFFFA7B8, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A7E3)
    Sleep(400)

    def lambda_A800():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A800)

    def lambda_A811():
        OP_96(0xFE, 0xFFFFACCC, 0xFFFFEC78, 0x4C90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A811)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(1000)

    def lambda_A84F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A84F)
    Sleep(50)

    def lambda_A85F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A85F)
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
            "#0005Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0382
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おー、俺だ。\x02\x03",

            "調子の方はどうだ？\x02",
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
            "#0000Fセルゲイ課長。\x02\x03",

            "#0000Fえっと、ちょうど今、\x01",
            "手配されていた魔獣を倒した所です。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "順調で結構、結構。\x02\x03",

            "今、どこにいる？\x07\x00\x02",
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
            "#0005Fえっと……\x01",
            "ジオフロントを出た所ですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0386
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふむ、まあそんなに\x01",
            "遠いわけじゃないな。\x02",
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
            "#0011Fへ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──お前たちに\x01",
            "緊急の捜査任務を与える。\x02\x03",

            "支援要請は後回しでいいから\x01",
            "最優先で対応してくれ。\x02",
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
            "#0001F──了解です！\x02\x03",

            "それで……\x01",
            "一体、何を捜査すれば！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "南東エリアにある旧市街……\x01",
            "急いでそちらへ向かえ。\x02\x03",

            "住民から警察に連絡があった。\x02\x03",

            "厄介な２組の不良集団が\x01",
            "喧嘩を始めようとしてるらしい。\x07\x00\x02",
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
            "#0005Fえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0392
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "後腐れがないように止めてこい。\x01",
            "──以上だ。\x07\x00\x02",
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
            "#6P#0011Fま、待ってください！\x02\x03",

            "喧嘩を止めろって……\x01",
            "それって捜査任務じゃ──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    Sleep(200)

    #C0394
    ChrTalk(
        0x101,
        "#6P#0013F──ってもう切れてるし！\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        (
            "#0105F課長から？\x01",
            "いったい何だったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x104,
        (
            "#0302Fその調子だと\x01",
            "ロクでもない話っぽそうだな？\x02",
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
        "#6P#0006Fいや、それがさ……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0398
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルゲイから伝えられた任務内容を\x01",
            "かいつまんで説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0399
    ChrTalk(
        0x102,
        "#0101F旧市街の不良集団……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_END)), "loc_AEF7")

    #C0400
    ChrTalk(
        0x104,
        (
            "#0301Fさっき旧市街で見た\x01",
            "あの物騒なガキどもか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF61")

    label("loc_AEF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_END)), "loc_AF34")

    #C0401
    ChrTalk(
        0x104,
        (
            "#0301Fさっき旧市街で\x01",
            "そんなの見かけたか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF61")

    label("loc_AF34")


    #C0402
    ChrTalk(
        0x104,
        (
            "#0301F旧市街……\x01",
            "そんな場所があんのか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF61")


    #C0403
    ChrTalk(
        0x103,
        (
            "#0203F#5Pデータベースによると……\x02\x03",

            "#0200Fたしか『サーベルバイパー』と\x01",
            "『テスタメンツ』という２チームが\x01",
            "旧市街で徒党を組んでるらしいです。\x02\x03",

            "喧嘩などは日常茶飯事だとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#6P#0005F俺が街を離れていた間に\x01",
            "そんな連中が出てきてたのか……\x02\x03",

            "#0003F──まあいい、とにかく\x01",
            "急いで旧市街に行ってみよう。\x02\x03",

            "#0001F小競り合いが始まる前に\x01",
            "何とか止める必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        "#0101Fええ、そうね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A2")

    #C0406
    ChrTalk(
        0x104,
        (
            "#0305Fところでロイド。\x01",
            "旧市街ってのはどこにあるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、東通りに出てから\x01",
            "小さな陸橋を南に渡った先だよ。\x02\x03",

            "まずは東通りに行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x104,
        "#0300Fおう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1DB")

    label("loc_B1A2")


    #C0409
    ChrTalk(
        0x104,
        (
            "#0300Fそんじゃ、とっとと\x01",
            "旧市街に向かうとするかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1DB")

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

    # Function_55_A66B end

    def Function_56_B209(): pass

    label("Function_56_B209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B33F")
    EventBegin(0x1)

    #C0410
    ChrTalk(
        0x101,
        (
            "#0000F今回の任務は\x01",
            "一応実戦テストらしい……\x02\x03",

            "寄り道せず、とにかく\x01",
            "ジオフロントの奥まで\x01",
            "行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2BB")

    #C0411
    ChrTalk(
        0x102,
        "#0100F了解、任務に集中しましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B329")

    label("loc_B2BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2FD")

    #C0412
    ChrTalk(
        0x103,
        (
            "#0200Fそうですね。\x01",
            "任務に集中しましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B329")

    label("loc_B2FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B329")

    #C0413
    ChrTalk(
        0x104,
        "#0300Fま、そうするかね。\x02",
    )

    CloseMessageWindow()

    label("loc_B329")

    Sleep(50)
    SetChrPos(0x0, -13150, -5000, 17120, 270)
    EventEnd(0x4)

    label("loc_B33F")

    Return()

    # Function_56_B209 end

    def Function_57_B340(): pass

    label("Function_57_B340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3FA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3B9")

    #C0414
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の南口だな。\x02\x03",

            "今は外に出る必要はない……\x01",
            "市内の仕事に専念しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B3E4")

    label("loc_B3B9")

    SetChrName("")

    #A0415
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

    label("loc_B3E4")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_B3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B477")
    EventBegin(0x1)

    #C0416
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
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_B477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4F0")
    EventBegin(0x1)

    #C0417
    ChrTalk(
        0x101,
        (
            "#0000Fマインツに行くには\x01",
            "街の北口から出ないとな。\x02\x03",

            "住宅街の方に回ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_B4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5B5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B576")

    #C0418
    ChrTalk(
        0x101,
        (
            "#0000Fっと、こっちは南口だ。\x02\x03",

            "キーアを危険な目に\x01",
            "遭わせたくないし、\x01",
            "外に出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B59F")

    label("loc_B576")

    SetChrName("")

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B59F")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_B5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B66F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B630")

    #C0420
    ChrTalk(
        0x101,
        (
            "#0003Fこっちは街の南口だな。\x02\x03",

            "黒月のこともある……\x01",
            "……今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_B659")

    label("loc_B630")

    SetChrName("")

    #A0421
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

    label("loc_B659")

    Sleep(50)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_B66F")

    Return()

    # Function_57_B340 end

    def Function_58_B670(): pass

    label("Function_58_B670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6D9")
    EventBegin(0x1)

    #C0422
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはクロスベル駅だ。\x01",
            "……今は用はないかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_B6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B743")
    EventBegin(0x1)

    #C0423
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはクロスベル駅だ。\x01",
            "……今は用はないかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_B743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B79F")
    EventBegin(0x1)

    #C0424
    ChrTalk(
        0x101,
        (
            "#0000Fこっちはクロスベル駅だ。\x01",
            "……今は用はないかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)

    label("loc_B79F")

    Return()

    # Function_58_B670 end

    SaveToFile()

Try(main)
