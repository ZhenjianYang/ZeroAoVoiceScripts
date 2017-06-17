from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "リッド",                 # 1
        "ビリー",                 # 2
        "クラリス",               # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "男の子",                 # 10
        "女の子",                 # 11
        "警官",                   # 12
        "国防軍兵士",             # 13
        "マーシー",               # 14
        "セピア",                 # 15
        "ウーナ",                 # 16
        "車",                     # 17
        "国防軍兵士",             # 18
        "国防軍兵士",             # 19
        "警官",                   # 20
        "警官",                   # 21
        "警官",                   # 22
        "警官",                   # 23
        "警官",                   # 24
        "警官",                   # 25
        "列車",                   # 26
        "SE制御",                 # 27
        "中央広場",               # 28
        "西通り",                 # 29
        "行政区",                 # 30
        "住宅街",                 # 31
        "歓楽街",                 # 32
        "東通り",                 # 33
        "旧市街",                 # 34
        "港湾区",                 # 35
        "ＩＢＣ",                 # 36
        "駅前通り",               # 37
        "裏通り",                 # 38
        "ウルスラ間道",           # 39
        "東クロスベル街道",       # 40
        "西クロスベル街道",       # 41
        "マインツ山道",           # 42
        "オルキスタワー",         # 43
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
    PlaceName(11.0, 0.0, 286.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_6_252F",         # 06, 6
        "Function_7_2CD8",         # 07, 7
        "Function_8_2F1B",         # 08, 8
        "Function_9_3136",         # 09, 9
        "Function_10_32F6",        # 0A, 10
        "Function_11_34BB",        # 0B, 11
        "Function_12_364C",        # 0C, 12
        "Function_13_37C4",        # 0D, 13
        "Function_14_38AD",        # 0E, 14
        "Function_15_3A57",        # 0F, 15
        "Function_16_3B8B",        # 10, 16
        "Function_17_3D7C",        # 11, 17
        "Function_18_3E11",        # 12, 18
        "Function_19_3E5B",        # 13, 19
        "Function_20_3EAB",        # 14, 20
        "Function_21_3F61",        # 15, 21
        "Function_22_42B5",        # 16, 22
        "Function_23_431A",        # 17, 23
        "Function_24_435B",        # 18, 24
        "Function_25_481A",        # 19, 25
        "Function_26_4E93",        # 1A, 26
        "Function_27_4EA5",        # 1B, 27
        "Function_28_4EBA",        # 1C, 28
        "Function_29_4ECF",        # 1D, 29
        "Function_30_4EDA",        # 1E, 30
        "Function_31_4EE5",        # 1F, 31
        "Function_32_4EF7",        # 20, 32
        "Function_33_52AD",        # 21, 33
        "Function_34_533A",        # 22, 34
        "Function_35_5350",        # 23, 35
        "Function_36_5559",        # 24, 36
        "Function_37_5857",        # 25, 37
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D5")

    #C0001
    ChrTalk(
        0xFE,
        (
            "あの独立宣言の日以来、\x01",
            "大陸横断鉄道は運行が\x01",
            "止まってしまってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "それでなくても帝国では\x01",
            "内戦が始まって、共和国でも恐慌が\x01",
            "起こってるらしいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "はあ、鉄道を眺めていられる\x01",
            "平和な時代は終わってしまったのかな。\x01",
            "これほど悲しい事はないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157F")

    label("loc_14D5")


    #C0004
    ChrTalk(
        0xFE,
        (
            "あの独立宣言の日以来、\x01",
            "大陸横断鉄道は運行が\x01",
            "止まってしまってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "はあ、鉄道を眺めていられる\x01",
            "平和な時代は終わってしまったのかな。\x01",
            "これほど悲しい事はないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F")

    Jump("loc_252B")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1592")
    Jump("loc_252B")

    label("loc_1592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1652")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今日を最後に、\x01",
            "しばらく大陸横断鉄道の運行は\x01",
            "止まってしまうらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "うう、僕の生きがいが……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "さっさと何もかも解決して、\x01",
            "早々に再開してほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E3")

    label("loc_1652")


    #C0009
    ChrTalk(
        0xFE,
        (
            "うう、僕の生きがいである\x01",
            "大陸横断鉄道の運行が\x01",
            "今日で止まってしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "さっさと何もかも解決して、\x01",
            "早々に再開してほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_252B")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    #C0011
    ChrTalk(
        0xFE,
        (
            "噂じゃ、こないだの襲撃事件は\x01",
            "帝国の仕業だっていうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "もしかして、最近起こっていた\x01",
            "脱線事故やマインツの占領事件も\x01",
            "みんな帝国のせいなんじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "鉄道技術の最先端を行く国だから\x01",
            "信じたいのはやまやまだけど……\x01",
            "疑いだしたらきりがないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18AA")

    label("loc_1804")


    #C0014
    ChrTalk(
        0xFE,
        (
            "もしかして、\x01",
            "最近起こっていた事件は\x01",
            "みんな帝国のせいなんじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "鉄道技術の最先端を行く国だから\x01",
            "信じたいのはやまやまだけど……\x01",
            "疑いだしたらきりがないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AA")

    Jump("loc_252B")

    label("loc_18AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_195D")

    #C0016
    ChrTalk(
        0xFE,
        (
            "列車の脱線事故から\x01",
            "そう日も経ってないのに、\x01",
            "占領事件なんて起こるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "なんだかイヤな感じだよ。\x01",
            "事件がこんなに続くなんて、\x01",
            "本当に偶然なのかな……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_195D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A25")

    #C0018
    ChrTalk(
        0xFE,
        (
            "横断鉄道が一晩で復旧できて\x01",
            "本当に良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "おかげで今日も心ゆくまで\x01",
            "列車を感じることができる……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "徹夜で作業に当たってくれた\x01",
            "警備隊には感謝の言葉もないね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A9F")

    label("loc_1A25")


    #C0021
    ChrTalk(
        0xFE,
        (
            "おかげで今日も心ゆくまで\x01",
            "列車を感じることができる……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "徹夜で作業に当たってくれた\x01",
            "警備隊には感謝の言葉もないね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9F")

    Jump("loc_252B")

    label("loc_1AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B2A")

    #C0023
    ChrTalk(
        0xFE,
        (
            "ううっ、なんてことだ。\x01",
            "脱線事故だなんて……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "列車も無事じゃ済まないだろうな……\x01",
            "心配で胸がざわざわするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C21")

    #C0025
    ChrTalk(
        0xFE,
        (
            "何でも昨日、駅のホームから\x01",
            "列車の屋根に飛び乗るなんて\x01",
            "事件があったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "気持ちは分かるけど……\x01",
            "鉄道マニアとしては許せない行いだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "無茶な乗り方をして列車を傷つけたり、\x01",
            "乗客に迷惑をかけるのは最悪だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CBC")

    label("loc_1C21")


    #C0028
    ChrTalk(
        0xFE,
        (
            "何でも昨日、駅のホームから\x01",
            "列車の屋根に飛び乗るなんて\x01",
            "事件があったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "無茶な乗り方をして列車を傷つけたり、\x01",
            "乗客に迷惑をかけるのは最悪だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CBC")

    Jump("loc_252B")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC0")

    #C0030
    ChrTalk(
        0xFE,
        (
            "独立する事で\x01",
            "どんなメリットがあるのか、\x01",
            "具体的にはよく分からないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "なんにしろ、帝国や共和国を\x01",
            "敵に回したりするようなことは\x01",
            "勘弁してほしいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "それが原因で横断鉄道が\x01",
            "止まったりしたら、\x01",
            "僕は生きてけないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E40")

    label("loc_1DC0")


    #C0033
    ChrTalk(
        0xFE,
        (
            "帝国や共和国を\x01",
            "敵に回したりするのは\x01",
            "勘弁してほしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "独立が原因で横断鉄道が\x01",
            "止まったりしたら、\x01",
            "僕は生きてけないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E40")

    Jump("loc_252B")

    label("loc_1E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F04")

    #C0035
    ChrTalk(
        0xFE,
        (
            "僕の中での通商会議は、\x01",
            "《アイゼングラーフ号》を\x01",
            "見れただけで８割方終わったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "あとは日程が終わって\x01",
            "クロスベルを走り去る姿を\x01",
            "眺められれば、それで充分さ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F89")

    label("loc_1F04")


    #C0037
    ChrTalk(
        0xFE,
        (
            "僕の中の通商会議は、\x01",
            "《アイゼングラーフ号》を見れて\x01",
            "８割方終わってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "さて、今日は家で本でも\x01",
            "読んでるとしようかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F89")

    Jump("loc_252B")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F2")

    #C0039
    ChrTalk(
        0xFE,
        (
            "ああああ……あれが、あれこそが\x01",
            "帝国政府専用の導力列車、\x01",
            "《アイゼングラーフ号》なのかぁ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "あの、帝国の強大な力を示すかのような、\x01",
            "炎のような赤を基調とする重厚なデザイン……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "『鉄の伯爵#8Rアイゼングラーフ#』の名に恥じない\x01",
            "素晴らしい列車と言えるだろうね！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "この日のためにカメラを\x01",
            "買っておいてよかったなあ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A3")

    label("loc_20F2")


    #C0043
    ChrTalk(
        0xFE,
        (
            "あの帝国政府専用の列車は、\x01",
            "『鉄の伯爵#8Rアイゼングラーフ#』の名に恥じない\x01",
            "素晴らしい列車と言えるだろうね！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ああ、なんていい日だろう。\x01",
            "もういつ死んでもかまわないよ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A3")

    Jump("loc_252B")

    label("loc_21A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B0")

    #C0045
    ChrTalk(
        0xFE,
        (
            "西ゼムリア通商会議……\x01",
            "帝国の首脳も来ると聞いたら、\x01",
            "鉄道マニアとしては見逃せないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "なんてったって、帝国政府は\x01",
            "専用の導力列車を持ってるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "帝国の首脳ともなれば\x01",
            "絶対にそれに乗ってくるはず……\x01",
            "いやあ、今から楽しみだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2335")

    label("loc_22B0")


    #C0048
    ChrTalk(
        0xFE,
        (
            "帝国政府は専用の\x01",
            "導力列車を持ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "明日の除幕式には、きっと\x01",
            "それに乗ってくるに違いないよ。\x01",
            "いやあ、今から楽しみだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_252B")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_23B9")

    #C0050
    ChrTalk(
        0xFE,
        "鉄道マニアの活動に天気は関係ないよ。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "雨に濡れる列車もやっぱいいなぁ。\x01",
            "まさに水も滴るなんとやら、だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_23B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_252B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")

    #C0052
    ChrTalk(
        0xFE,
        (
            "今日も大陸横断鉄道は\x01",
            "好調に運行しているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "列車の豪奢なフォルム、\x01",
            "蒼穹をそのまま映したかのような\x01",
            "美しいカラーリング……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "う～ん、いつ見ても最高だ。\x01",
            "鉄道マニアやっててよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_252B")

    label("loc_249A")


    #C0055
    ChrTalk(
        0xFE,
        (
            "列車の豪奢なフォルム、\x01",
            "蒼穹をそのまま映したかのような\x01",
            "美しいカラーリング……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "う～ん、いつ見ても最高だ。\x01",
            "鉄道マニアやっててよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252B")

    TalkEnd(0xFE)
    Return()

    # Function_5_138B end

    def Function_6_252F(): pass

    label("Function_6_252F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2618")

    #C0057
    ChrTalk(
        0xFE,
        (
            "クロスベル市に余っている物資を\x01",
            "各地に分配に行くことにしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "外国からの物資が殆ど入らない今、\x01",
            "それにも限界があるだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "運送業者として、まずはできることを\x01",
            "やっていかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26AF")

    label("loc_2618")


    #C0060
    ChrTalk(
        0xFE,
        (
            "外国からの物資が殆ど入らない今、\x01",
            "各地に物資を分配するにも\x01",
            "限界があるだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "運送業者として、まずはできることを\x01",
            "やっていかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AF")

    Jump("loc_2CD4")

    label("loc_26B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26C2")
    Jump("loc_2CD4")

    label("loc_26C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_274A")

    #C0062
    ChrTalk(
        0xFE,
        (
            "おいおい、何だか\x01",
            "大変なことになっちまったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "鉄道の運行も止まっちまうらしいし、\x01",
            "外国との流通はどうなるんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_274A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2758")
    Jump("loc_2CD4")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27EB")

    #C0064
    ChrTalk(
        0xFE,
        (
            "まさかクロスベル自治州で\x01",
            "占領事件なんてものが\x01",
            "起きちまうなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "警備隊も苦戦してるみたいだし、\x01",
            "どうなってしまうやら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_27EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27F9")
    Jump("loc_2CD4")

    label("loc_27F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2807")
    Jump("loc_2CD4")

    label("loc_2807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2898")

    #C0066
    ChrTalk(
        0xFE,
        (
            "あんたたち、\x01",
            "カプア特急便の誤配荷物を\x01",
            "届けなおしてくれたんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "いや、ほっとしたよ。\x01",
            "さすが特務支援課は頼りになるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_2898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_294E")

    #C0068
    ChrTalk(
        0xFE,
        (
            "得体の知れない魔獣が出てるから、\x01",
            "街道の行き来に気をつけろって\x01",
            "通達があったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "俺たちみたいな運送業者は\x01",
            "特に行き来が多いから、\x01",
            "やっぱり魔獣には気を遣うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_294E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29B5")

    #C0070
    ChrTalk(
        0xFE,
        "さて、そろそろ配達に行くかな。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "パパッと運ばないと、\x01",
            "オヤジにどやされちまうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_29B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAC")

    #C0072
    ChrTalk(
        0xFE,
        (
            "さっさと荷物を受け取って\x01",
            "配達に行かなきゃってのに、\x01",
            "どうも遅れちまってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "貨物列車の積み荷もかなり厳重に\x01",
            "チェックされてるんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "帝国のお偉いさんが来たんだし、\x01",
            "仕方ないといえば仕方ないけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B60")

    label("loc_2AAC")


    #C0075
    ChrTalk(
        0xFE,
        (
            "さっさと荷物を受け取って\x01",
            "配達に行かなきゃってのに、\x01",
            "どうも遅れちまってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "帝国のお偉いさんが来て\x01",
            "チェックも厳しくなってんだろうし、\x01",
            "仕方ないといえば仕方ないけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B60")

    Jump("loc_2CD4")

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B73")
    Jump("loc_2CD4")

    label("loc_2B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B81")
    Jump("loc_2CD4")

    label("loc_2B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C68")

    #C0077
    ChrTalk(
        0xFE,
        (
            "うちはライムス運送って言う\x01",
            "個人経営の運送会社なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "オヤジが社長の若い会社だけど、\x01",
            "親切・丁寧・スピーディをモットーに\x01",
            "頑張らせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "ご用命の際は、\x01",
            "是非ともご連絡をよろしくな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CD4")

    label("loc_2C68")


    #C0080
    ChrTalk(
        0xFE,
        (
            "うちはライムス運送って言う\x01",
            "個人経営の運送会社なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ご用命の際は、\x01",
            "是非ともご連絡をよろしくな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD4")

    TalkEnd(0xFE)
    Return()

    # Function_6_252F end

    def Function_7_2CD8(): pass

    label("Function_7_2CD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA1")

    #C0082
    ChrTalk(
        0xFE,
        "あら、あなたたち。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        (
            "#10105Fあ……母さん。\x01",
            "これからフランの見舞いに？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "ええ、フランの着替えを\x01",
            "届けにいくところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "あの子の様子はどうだった？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#10108Fうん、まだやっぱり\x01",
            "疲れてるみたいだけど……\x01",
            "とりあえず元気みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "ふう、それはよかったわ。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "とにかくあの子が元気になるまでは\x01",
            "こまめに見舞いに行くつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "だから、こっちは任せて\x01",
            "あんたは自分の仕事を\x01",
            "がんばりなさいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        "#10100Fうん、分かってる。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 7)
    Jump("loc_2F17")

    label("loc_2EA1")


    #C0091
    ChrTalk(
        0xFE,
        (
            "ノエル、あんたの支援課の出向は\x01",
            "今日で終わりなのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "せめて、悔いの残らないように\x01",
            "しっかりと務めなさいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F17")

    TalkEnd(0xFE)
    Return()

    # Function_7_2CD8 end

    def Function_8_2F1B(): pass

    label("Function_8_2F1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FAA")

    #N0093
    NpcTalk(
        0xFE,
        "外国人",
        (
            "むうう、今日を逃すと\x01",
            "帝国に帰れんじゃと……！？\x02",
        )
    )

    CloseMessageWindow()

    #N0094
    NpcTalk(
        0xFE,
        "外国人",
        (
            "ええい、何が国防軍じゃ！\x01",
            "勝手な事ばかり抜かしおって！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3132")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3044")

    #N0095
    NpcTalk(
        0xFE,
        "市民",
        (
            "まさかクロスベル市が\x01",
            "襲撃事件などにあってしまうとはな……\x02",
        )
    )

    CloseMessageWindow()

    #N0096
    NpcTalk(
        0xFE,
        "市民",
        (
            "わしらが何をしたというのか……\x01",
            "もうこんなことはごめんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3132")

    label("loc_3044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30CB")

    #N0097
    NpcTalk(
        0xFE,
        "市民",
        (
            "国家独立か……\x01",
            "そんなことが提唱される日が\x01",
            "来ようとはのう……\x02",
        )
    )

    CloseMessageWindow()

    #N0098
    NpcTalk(
        0xFE,
        "市民",
        (
            "なんにせよ、実現して\x01",
            "ほしいものじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3132")

    label("loc_30CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3132")

    #C0099
    ChrTalk(
        0xFE,
        (
            "おお、なんと……\x01",
            "なんと立派な街並みじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ふふ、年甲斐もなく\x01",
            "ワクワクしてきたぞい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3132")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F1B end

    def Function_9_3136(): pass

    label("Function_9_3136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31B0")

    #N0101
    NpcTalk(
        0xFE,
        "外国人",
        "おじいさん、落ち着いて下さいな……\x02",
    )

    CloseMessageWindow()

    #N0102
    NpcTalk(
        0xFE,
        "外国人",
        (
            "とにかく、早くチケットを\x01",
            "買いに行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F2")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3201")

    #C0103
    ChrTalk(
        0xFE,
        (
            "救急車が沢山通っていったが……\x01",
            "い、いったい何の騒ぎなんだい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F2")

    label("loc_3201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_326F")

    #C0104
    ChrTalk(
        0xFE,
        (
            "クロスベルってのは\x01",
            "やっぱり広いねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "観光ガイドのひとつでも\x01",
            "買っておけばよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F2")

    label("loc_326F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F2")

    #C0106
    ChrTalk(
        0xFE,
        (
            "おじいさんは大層喜んでるけど、\x01",
            "あたしは何だか心配だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "だって、クロスベルって\x01",
            "“魔都”と呼ばれてるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F2")

    TalkEnd(0xFE)
    Return()

    # Function_9_3136 end

    def Function_10_32F6(): pass

    label("Function_10_32F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_33B0")

    #N0108
    NpcTalk(
        0xFE,
        "外国人",
        (
            "クロスベルでの職を失うのは痛いが、\x01",
            "故郷に帰れなくなるよりましだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0xFE,
        "外国人",
        (
            "この際、座れなくても構わん。\x01",
            "妙な事に巻き込まれる前に\x01",
            "クロスベルを離れねばな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_33B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3430")

    #C0110
    ChrTalk(
        0xFE,
        (
            "武装集団による占拠だなんて、\x01",
            "一体全体どうしてこんな事件が……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "マインツは無事なんだろうか、\x01",
            "心配だな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_3430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B7")

    #C0112
    ChrTalk(
        0xFE,
        (
            "え～っと、今日予約しといた\x01",
            "ホテルはどこかな～っと。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "奮発して歓楽街の宿にしたんだ。\x01",
            "目いっぱい旅行を楽しまないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B7")

    TalkEnd(0xFE)
    Return()

    # Function_10_32F6 end

    def Function_11_34BB(): pass

    label("Function_11_34BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3548")

    #N0114
    NpcTalk(
        0xFE,
        "外国人",
        (
            "この間、帝国の方から\x01",
            "退去通告が届いたのよ……\x02",
        )
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0xFE,
        "外国人",
        (
            "はあ、クロスベルでの生活は\x01",
            "気に入ってたんだけどな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3648")

    label("loc_3548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_35C8")

    #C0116
    ChrTalk(
        0xFE,
        (
            "あたしゃ武装集団ってヤツが\x01",
            "クロスベルに来ないかも心配だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "早く警備隊が\x01",
            "なんとかしてくれないかねえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3648")

    label("loc_35C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3648")

    #C0118
    ChrTalk(
        0xFE,
        (
            "ふふ、この子ったら\x01",
            "こんなにはしゃいじゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "でも分かる気がするわ。\x01",
            "クロスベルってすごく\x01",
            "都会なんですもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3648")

    TalkEnd(0xFE)
    Return()

    # Function_11_34BB end

    def Function_12_364C(): pass

    label("Function_12_364C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36C7")

    #C0120
    ChrTalk(
        0xFE,
        (
            "クロスベルから\x01",
            "さっさと離れるつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "もうこんな危ない場所に\x01",
            "１秒だって居たくないからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C0")

    label("loc_36C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3754")

    #C0122
    ChrTalk(
        0xFE,
        (
            "独立って言っても、\x01",
            "いまいちどういうことか\x01",
            "分からないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "住民投票の日が来る前に、\x01",
            "ちょっと調べてみようかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C0")

    label("loc_3754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37C0")

    #C0124
    ChrTalk(
        0xFE,
        "今朝の賑わいはすごいものだったよ。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "あんな豪華なリムジンでの送迎、\x01",
            "さすがＶＩＰたちだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C0")

    TalkEnd(0xFE)
    Return()

    # Function_12_364C end

    def Function_13_37C4(): pass

    label("Function_13_37C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3847")

    #N0126
    NpcTalk(
        0xFE,
        "外国人",
        (
            "どうしよう……\x01",
            "構内が混みすぎて中に入れないの。\x02",
        )
    )

    CloseMessageWindow()

    #N0127
    NpcTalk(
        0xFE,
        "外国人",
        (
            "うう、ちゃんと共和国に\x01",
            "帰れるのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A9")

    label("loc_3847")


    #C0128
    ChrTalk(
        0xFE,
        (
            "除幕式は百貨店の屋上から\x01",
            "見たのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "あ～ん、ユリア様のお顔を\x01",
            "直接拝見したかったわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A9")

    TalkEnd(0xFE)
    Return()

    # Function_13_37C4 end

    def Function_14_38AD(): pass

    label("Function_14_38AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3924")

    #C0130
    ChrTalk(
        0xFE,
        (
            "ねーねー、なんで帝国に\x01",
            "帰らなくちゃいけないのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "せっかくいっぱい友達が\x01",
            "できたのにな～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A53")

    label("loc_3924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_398D")

    #C0132
    ChrTalk(
        0xFE,
        (
            "駅で遊んでたら、駅員さんに\x01",
            "怒られてつまみ出されちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "ちぇっ、ケチだよな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A53")

    label("loc_398D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39FC")

    #C0134
    ChrTalk(
        0xFE,
        (
            "よ～し、それじゃあ今日は\x01",
            "駅の中でかくれんぼしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "へへん、最初はオイラがオニな～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A53")

    label("loc_39FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A53")

    #C0136
    ChrTalk(
        0xFE,
        "わ～っ、ここがクロスベルかぁ～！！\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "ねーねー、早く行こうよママ～！！\x02",
    )

    CloseMessageWindow()

    label("loc_3A53")

    TalkEnd(0xFE)
    Return()

    # Function_14_38AD end

    def Function_15_3A57(): pass

    label("Function_15_3A57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3AF9")

    #C0138
    ChrTalk(
        0xFE,
        (
            "んもう、お兄ちゃんったら……\x01",
            "だから止めとこうって言ったのに～。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "……でも、駅員さんたち\x01",
            "本当に忙しそうだったよね。\x01",
            "何かあったのかなあ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B4B")

    #C0140
    ChrTalk(
        0xFE,
        "え～、やめとこうよお兄ちゃん。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "駅の人に怒られちゃうよ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B87")

    #C0142
    ChrTalk(
        0xFE,
        (
            "あたちもお父さんと一緒に\x01",
            "カジノで遊びた～い。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B87")

    TalkEnd(0xFE)
    Return()

    # Function_15_3A57 end

    def Function_16_3B8B(): pass

    label("Function_16_3B8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C4C")

    #C0143
    ChrTalk(
        0xFE,
        (
            "一体、テロリストたちは\x01",
            "どういうルートでクロスベルに\x01",
            "入ろうとしているんですかね……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "死角はないはずですが……\x01",
            "とにかく、現状では今のまま\x01",
            "警戒を続けるしかありませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D78")

    label("loc_3C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CD6")

    #C0145
    ChrTalk(
        0xFE,
        (
            "ふう、除幕式も何とか終わって\x01",
            "少しだけ肩の荷が下りた感じです。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "もっとも、まだまだ\x01",
            "これからも気は抜けませんけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D78")

    label("loc_3CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D78")

    #C0147
    ChrTalk(
        0xFE,
        (
            "駅と空港の内部には、\x01",
            "二課の捜査官が相当数詰めているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "他の場所を含め、これほどまでに\x01",
            "強固な警戒体制を敷くのは\x01",
            "俺の記憶では初めてのことだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D78")

    TalkEnd(0xFE)
    Return()

    # Function_16_3B8B end

    def Function_17_3D7C(): pass

    label("Function_17_3D7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DDE")

    #C0149
    ChrTalk(
        0xFE,
        (
            "帝国に帰る妻と娘を\x01",
            "見送りに来たんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "だ、脱線事故だなんて……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E0D")

    label("loc_3DDE")


    #C0151
    ChrTalk(
        0xFE,
        (
            "も、もし妻と娘が\x01",
            "その列車に乗ってたら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0D")

    TalkEnd(0xFE)
    Return()

    # Function_17_3D7C end

    def Function_18_3E11(): pass

    label("Function_18_3E11")

    TalkBegin(0xFE)

    #C0152
    ChrTalk(
        0xFE,
        "なんてこと……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "どれだけの被害が\x01",
            "でてしまったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3E11 end

    def Function_19_3E5B(): pass

    label("Function_19_3E5B")

    TalkBegin(0xFE)

    #C0154
    ChrTalk(
        0xFE,
        "列車がとまってるの？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "それじゃあ、今日も\x01",
            "パパと一緒にいれるね！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3E5B end

    def Function_20_3EAB(): pass

    label("Function_20_3EAB")

    TalkBegin(0xFE)

    #C0156
    ChrTalk(
        0xFE,
        (
            "クロスベル駅は、本日を以って\x01",
            "運行が休止される予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "また、再開の日程は今のところ\x01",
            "未定となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "帰国を希望される外国人の方は、\x01",
            "どうかお急ぎ下さい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3EAB end

    def Function_21_3F61(): pass

    label("Function_21_3F61")

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

    def lambda_427E():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_427E)
    BeginChrThread(0x21, 0, 0, 22)
    Sleep(5000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3F61 end

    def Function_22_42B5(): pass

    label("Function_22_42B5")

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

    # Function_22_42B5 end

    def Function_23_431A(): pass

    label("Function_23_431A")

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

    # Function_23_431A end

    def Function_24_435B(): pass

    label("Function_24_435B")

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
    SetChrName("ディーター大統領")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──彼らは長年に渡り、\x01",
            "このクロスベルを自分たちの\x01",
            "“属州”として扱ってきました。\x02\x03",

            "彼らがどんな犯罪を犯しても\x01",
            "我々に追及する権利はありません。\x02\x03",

            "そして今もなお……\x01",
            "豊かな税収を掠め取られる形で\x01",
            "我々は搾取#4Rさくしゅ#され続けているのです。\x02",
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
    SetChrName("ディーター大統領")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──ですが、\x01",
            "それだけではありません！\x02\x03",

            "#4S我々は生命の危険すら\x01",
            "脅かされてきたのです……！\x02",
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

    # Function_24_435B end

    def Function_25_481A(): pass

    label("Function_25_481A")

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

    def lambda_48EE():
        OP_97(0x101, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48EE)
    Sleep(100)

    def lambda_490B():
        OP_97(0x102, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_490B)
    Sleep(100)

    def lambda_4928():
        OP_97(0x103, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4928)
    Sleep(100)

    def lambda_4945():
        OP_97(0x104, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4945)
    Sleep(100)

    def lambda_4962():
        OP_97(0x105, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4962)
    Sleep(100)

    def lambda_497F():
        OP_97(0x109, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_497F)
    Sleep(100)

    def lambda_499C():
        OP_97(0x106, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_499C)
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
            "#11P#00006F何とか課長たちと\x01",
            "連絡を取りたいけど……\x02\x03",

            "#00013Fなんだ……？\x01",
            "この青白いモヤは？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#5P#00108Fまるで僧院や塔で\x01",
            "出ていたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x109,
        (
            "#10108F#5P人通りも……\x01",
            "全然ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x105,
        (
            "#11P#10408Fまあ、街の外で\x01",
            "戦闘が起こっているから\x01",
            "避難してるんだろうけど……\x02",
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
        "#5P#00105Fティオちゃん？\x02",
    )

    CloseMessageWindow()

    def lambda_4BF7():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4BF7)
    Sleep(30)

    def lambda_4C07():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C07)
    Sleep(30)

    def lambda_4C17():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4C17)
    Sleep(30)

    def lambda_4C27():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4C27)
    Sleep(30)

    def lambda_4C37():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4C37)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0167
    ChrTalk(
        0x104,
        "#11P#00301Fなんだ、どうした？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        (
            "#12P#00203F……中央広場から\x01",
            "共鳴音が聞こえます。\x02\x03",

            "#00201Fあの大鐘です。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#5P#00007Fなに……！？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x106,
        "#12P#10701F……行ってみましょう。\x02",
    )

    CloseMessageWindow()

    def lambda_4D0E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D0E)
    Sleep(30)

    def lambda_4D1E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4D1E)
    Sleep(30)

    def lambda_4D2E():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4D2E)
    Sleep(30)

    def lambda_4D3E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4D3E)
    Sleep(30)

    def lambda_4D4E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4D4E)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(500, 1200, 7500, 3000)
    MoveCamera(37, 21, 0, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_4D97():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D97)
    Sleep(100)

    def lambda_4DB4():
        OP_97(0x102, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4DB4)
    Sleep(100)

    def lambda_4DD1():
        OP_97(0x103, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4DD1)
    Sleep(100)

    def lambda_4DEE():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4DEE)
    Sleep(100)

    def lambda_4E0B():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4E0B)
    Sleep(100)

    def lambda_4E28():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4E28)
    Sleep(100)

    def lambda_4E45():
        OP_97(0x106, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4E45)
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

    # Function_25_481A end

    def Function_26_4E93(): pass

    label("Function_26_4E93")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_26_4E93 end

    def Function_27_4EA5(): pass

    label("Function_27_4EA5")

    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_4EA5 end

    def Function_28_4EBA(): pass

    label("Function_28_4EBA")

    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_28_4EBA end

    def Function_29_4ECF(): pass

    label("Function_29_4ECF")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_4ECF end

    def Function_30_4EDA(): pass

    label("Function_30_4EDA")

    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_30_4EDA end

    def Function_31_4EE5(): pass

    label("Function_31_4EE5")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_4EE5 end

    def Function_32_4EF7(): pass

    label("Function_32_4EF7")

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
            "#00003F（……キリカさんたちの話が\x01",
            "  どれだけ掛かるか分からない。）\x02\x03",

            "#00001F（作戦前だし、用事は一通り\x01",
            "  済ませた方がよさそうだな。）\x02",
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
            "この先のイベントを進めると\x01",
            "オルキスタワーの突入作戦が始まるため\x01",
            "市内での自由行動が出来なくなります。\x07\x00\x02",
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
            "駅構内に入る\x01",            # 0
            "他の用事を済ませる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_511A"),
        (1, "loc_527A"),
        (SWITCH_DEFAULT, "loc_52AC"),
    )


    label("loc_511A")

    OP_68(8400, 1900, -1900, 1500)
    MoveCamera(90, 13, 0, 1500)

    def lambda_513B():
        OP_96(0xFE, 0x2328, 0xFA, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_513B)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    SetCameraDistance(17500, 3000)

    def lambda_517F():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_517F)
    Sleep(50)

    def lambda_519C():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_519C)
    Sleep(50)

    def lambda_51B9():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_51B9)
    Sleep(50)

    def lambda_51D6():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_51D6)
    Sleep(50)

    def lambda_51F3():
        OP_97(0xF4, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_51F3)
    Sleep(50)

    def lambda_5210():
        OP_97(0xF5, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5210)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_5237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5237)
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
    Jump("loc_52AC")

    label("loc_527A")

    SetChrPos(0x0, 6500, 0, -2000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_52AC")

    label("loc_52AC")

    Return()

    # Function_32_4EF7 end

    def Function_33_52AD(): pass

    label("Function_33_52AD")

    TalkBegin(0x8)

    #C0173
    ChrTalk(
        0x8,
        (
            "さっき、帝国製の黒い運搬車が\x01",
            "中央広場の方に走っていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "……その先どこに行ったかって？\x01",
            "悪いけど、ちょっと分からないね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_33_52AD end

    def Function_34_533A(): pass

    label("Function_34_533A")

    EventBegin(0x1)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)
    Return()

    # Function_34_533A end

    def Function_35_5350(): pass

    label("Function_35_5350")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53A2")

    #C0175
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはクロスベル駅だ。\x01",
            "……とりあえず用事はないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5545")

    label("loc_53A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5400")
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には固く鍵が掛けられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 5)
    Jump("loc_547B")

    label("loc_5400")


    #C0177
    ChrTalk(
        0x101,
        (
            "#00001F……どうやら駅は\x01",
            "封鎖されているみたいだな。\x02\x03",

            "#00003Fまあ、特に用事が\x01",
            "あるわけでもないし、\x01",
            "ここは放っておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_547B")

    SetScenarioFlags(0x1CE, 4)
    Jump("loc_5545")

    label("loc_5483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5506")

    #C0178
    ChrTalk(
        0x101,
        (
            "#00001F……構内は帰国する外国人で\x01",
            "相当混雑しているみたいだ。\x02\x03",

            "#00003F入るのは止めておいた方が\x01",
            "よさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Jump("loc_5545")

    label("loc_5506")


    #C0179
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはクロスベル駅だ。\x01",
            "……今は用はないかな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    label("loc_5545")

    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)
    Return()

    # Function_35_5350 end

    def Function_36_5559(): pass

    label("Function_36_5559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5618")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C9")

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000Fこの先は街の南口だな。\x02\x03",

            "特に用事はないし、\x01",
            "出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5605")

    label("loc_55C9")


    #C0181
    ChrTalk(
        0x101,
        (
            "#00000Fこちら方面に用事はない。\x01",
            "出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5605")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56E7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568E")

    #C0182
    ChrTalk(
        0x101,
        (
            "#00001Fこの先は街の南口だな。\x02\x03",

            "今は寄り道せずに、\x01",
            "事故関連の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56D4")

    label("loc_568E")


    #C0183
    ChrTalk(
        0x101,
        (
            "#00001Fこっち方面に用事はない。\x01",
            "今は事故関連の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D4")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_56E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_575D")
    EventBegin(0x1)

    #C0184
    ChrTalk(
        0x101,
        (
            "#00001F今はとにかく\x01",
            "ランディを追いかけないと――\x01",
            "脇道にそれてる場合じゃない。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_575D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57C2")
    EventBegin(0x1)

    #C0185
    ChrTalk(
        0x101,
        (
            "#00001F今は市外に出ている場合じゃない。\x01",
            "大人しく引き返そう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_57C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5856")
    EventBegin(0x1)

    #C0186
    ChrTalk(
        0x101,
        (
            "#00001Fここまで来て市内を\x01",
            "離れるわけにはいかない。\x02\x03",

            "オルキスタワー突入作戦――\x01",
            "何としても成功させなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5856")

    Return()

    # Function_36_5559 end

    def Function_37_5857(): pass

    label("Function_37_5857")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_37_5857 end

    SaveToFile()

Try(main)
