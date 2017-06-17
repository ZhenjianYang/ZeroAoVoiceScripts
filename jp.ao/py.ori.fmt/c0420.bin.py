from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0420.bin",                # FileName
        "c0420",                    # MapName
        "c0420",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0420",                  # 0
        "イリア",                 # 1
        "リーシャ",               # 2
        "シュリ",                 # 3
        "アバン劇団長",           # 4
        "ハインツ",               # 5
        "ユージーン",             # 6
        "テオドール",             # 7
        "ニコル",                 # 8
        "プリエ",                 # 9
        "セリーヌ",               # 10
        "カレリア",               # 11
        "マリー",                 # 12
        "エリィ",                 # 13
        "ワジ",                   # 14
        "シャンデリア",           # 15
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch10000.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch27500.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch28700.itc",                   # 06
        "chr/ch28800.itc",                   # 07
        "chr/ch28900.itc",                   # 08
        "chr/ch29000.itc",                   # 09
        "chr/ch29100.itc",                   # 0A
        "chr/ch36600.itc",                   # 0B
        "chr/ch36700.itc",                   # 0C
        "chr/ch36800.itc",                   # 0D
        "chr/ch09800.itc",                   # 0E
        "chr/ch36900.itc",                   # 0F
        "chr/ch14100.itc",                   # 10
        "chr/ch37000.itc",                   # 11
        "chr/ch09700.itc",                   # 12
        "chr/ch21900.itc",                   # 13
        "chr/ch10100.itc",                   # 14
    ))

    DeclNpc(0,       0,       15550,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1000,    0,       13819,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1000,   0,       13819,   0,    261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1879,   9,       15239,   135,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-66489,  0,       7329,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2549,   1250,    19700,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  261,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(2250,    0,       14750,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-68129,  0,       2140,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-123800, 0,       -2289,   180,  261,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  0.0,                   7.079999923706055,     0.0,                   14.0625,               [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.4000000059604645,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.8320000171661377,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 28,  -60.38999938964844,    3.0,                   -1.0,                  12.25,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   30.19499969482422,     -0.8571429252624512,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 31,  0.0,                   7.079999923706055,     0.0,                   14.0625,               [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.4000000059604645,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.8320000171661377,   -0.0,                  1.0])

    ChipFrameInfo(1176, 0)                                       # 0

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_548",          # 01, 1
        "Function_2_573",          # 02, 2
        "Function_3_5C6",          # 03, 3
        "Function_4_5F1",          # 04, 4
        "Function_5_C67",          # 05, 5
        "Function_6_DDB",          # 06, 6
        "Function_7_149F",         # 07, 7
        "Function_8_18A5",         # 08, 8
        "Function_9_287B",         # 09, 9
        "Function_10_2F14",        # 0A, 10
        "Function_11_2F85",        # 0B, 11
        "Function_12_34EB",        # 0C, 12
        "Function_13_3FFA",        # 0D, 13
        "Function_14_40FE",        # 0E, 14
        "Function_15_42A8",        # 0F, 15
        "Function_16_44B6",        # 10, 16
        "Function_17_4A9E",        # 11, 17
        "Function_18_5846",        # 12, 18
        "Function_19_5C3A",        # 13, 19
        "Function_20_5CE4",        # 14, 20
        "Function_21_5F98",        # 15, 21
        "Function_22_635F",        # 16, 22
        "Function_23_63B6",        # 17, 23
        "Function_24_659B",        # 18, 24
        "Function_25_6776",        # 19, 25
        "Function_26_677D",        # 1A, 26
        "Function_27_67A3",        # 1B, 27
        "Function_28_8909",        # 1C, 28
        "Function_29_8E6A",        # 1D, 29
        "Function_30_8EF9",        # 1E, 30
        "Function_31_9C83",        # 1F, 31
        "Function_32_A1D8",        # 20, 32
        "Function_33_ABAF",        # 21, 33
        "Function_34_B029",        # 22, 34
        "Function_35_C4C5",        # 23, 35
        "Function_36_CF52",        # 24, 36
        "Function_37_D4BE",        # 25, 37
        "Function_38_DBE7",        # 26, 38
        "Function_39_DC32",        # 27, 39
        "Function_40_DC7D",        # 28, 40
        "Function_41_DCB4",        # 29, 41
        "Function_42_DCFF",        # 2A, 42
        "Function_43_DD93",        # 2B, 43
        "Function_44_EC51",        # 2C, 44
        "Function_45_EC81",        # 2D, 45
        "Function_46_ECB1",        # 2E, 46
        "Function_47_ECE1",        # 2F, 47
        "Function_48_ED50",        # 30, 48
        "Function_49_ED6D",        # 31, 49
        "Function_50_F153",        # 32, 50
        "Function_51_F177",        # 33, 51
        "Function_52_F19B",        # 34, 52
        "Function_53_F1B0",        # 35, 53
        "Function_54_F1BE",        # 36, 54
        "Function_55_F1DD",        # 37, 55
        "Function_56_F1FC",        # 38, 56
        "Function_57_FECA",        # 39, 57
        "Function_58_101BF",       # 3A, 58
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4D0"),
        (1, "loc_4DC"),
        (2, "loc_4E8"),
        (3, "loc_4F4"),
        (4, "loc_500"),
        (5, "loc_50C"),
        (6, "loc_518"),
        (SWITCH_DEFAULT, "loc_524"),
    )


    label("loc_4D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_500")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_50C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_518")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_524")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_530")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_547")

    Return()

    # Function_0_498 end

    def Function_1_548(): pass

    label("Function_1_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_572")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_548")

    label("loc_572")

    Return()

    # Function_1_548 end

    def Function_2_573(): pass

    label("Function_2_573")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C5")
    OP_95(0xFE, 61750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x2EE)
    Sleep(300)
    OP_95(0xFE, 66750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x2EE)
    Sleep(300)
    Jump("Function_2_573")

    label("loc_5C5")

    Return()

    # Function_2_573 end

    def Function_3_5C6(): pass

    label("Function_3_5C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F0")
    OP_94(0xFE, 0xFFFF9C32, 0x1C0C, 0xFFFF8F8A, 0x1108, 0x3E8)
    Sleep(300)
    Jump("Function_3_5C6")

    label("loc_5F0")

    Return()

    # Function_3_5C6 end

    def Function_4_5F1(): pass

    label("Function_4_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3520, 1250, 22730, 90)
    SetChrPos(0xE, 4800, 1250, 22730, 270)
    SetChrPos(0xA, 0, 1250, 27230, 0)
    SetChrChipByIndex(0xA, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A")
    SetChrFlags(0xA, 0x10)

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_657")
    SetChrChipByIndex(0xA, 0x2)

    label("loc_657")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B95")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6E7")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    SetChrPos(0xD, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x11, 0x11)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B95")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7C0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xA, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrChipByIndex(0xA, 0x10)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x11, 0x11)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xD, 65610, 0, 4550, 225)
    SetChrPos(0xE, 65000, 0, 3000, 270)
    SetChrPos(0x10, 63670, 0, 3590, 90)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0x10, 0xF)
    Jump("loc_B95")

    label("loc_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_813")
    SetChrPos(0xB, -62780, 0, 3150, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    SetChrFlags(0xB, 0x10)

    label("loc_7E9")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xC, -66490, 0, 7330, 0)
    Jump("loc_B95")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8BF")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, -1390, 1250, 25170, 90)
    SetChrPos(0xE, 1390, 1250, 25170, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_866")
    SetChrFlags(0xD, 0x10)

    label("loc_866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")
    SetChrFlags(0xE, 0x10)

    label("loc_875")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 64000, 0, 3000, 90)
    SetChrPos(0xF, 65000, 0, 3000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AB")
    SetChrFlags(0x11, 0x10)

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    SetChrFlags(0xF, 0x10)

    label("loc_8BA")

    Jump("loc_B95")

    label("loc_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_93D")
    SetChrChipByIndex(0xA, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F4")
    SetChrPos(0xA, -50, 0, 15980, 180)
    SetChrFlags(0x8, 0x80)
    Jump("loc_924")

    label("loc_8F4")

    SetChrChipByIndex(0x8, 0x12)
    SetChrPos(0x8, -1390, 1250, 25170, 90)
    SetChrPos(0xA, 1390, 1250, 25170, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_924")

    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B95")

    label("loc_93D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_969")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B95")

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_995")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B95")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9F4")
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xA, 1390, 1250, 26170, 270)
    SetChrPos(0x9, -1390, 1250, 26170, 90)
    SetChrPos(0xB, 80, 1250, 24110, 0)
    SetChrPos(0x8, -6130, 15200, -2810, 45)
    SetChrChipByIndex(0xA, 0x10)
    SetChrChipByIndex(0x9, 0xE)
    Jump("loc_B95")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A87")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, -1390, 1250, 25170, 90)
    SetChrPos(0xE, 1390, 1250, 25170, 270)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 64000, 0, 3000, 90)
    SetChrPos(0xF, 65000, 0, 3000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A73")
    SetChrFlags(0xA, 0x10)

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    SetChrFlags(0xF, 0x10)

    label("loc_A82")

    Jump("loc_B95")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AB3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B95")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B22")
    SetChrChipByIndex(0x8, 0x12)
    SetChrChipByIndex(0x9, 0xE)
    SetChrChipByIndex(0xF, 0xD)
    SetChrPos(0xA, 7570, 0, 17850, 315)
    SetChrPos(0xF, 67000, 0, 3000, 90)
    SetChrPos(0xB, 0, 1250, 30300, 180)
    SetChrPos(0x8, -1390, 1250, 29170, 90)
    SetChrPos(0x9, 1390, 1250, 29170, 270)
    Jump("loc_B95")

    label("loc_B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B53")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B95")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B95")
    SetChrPos(0xB, -64489, 0, 7330, 270)
    OP_93(0xC, 0x5A, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xF, 65000, 0, 3000, 180)
    BeginChrThread(0xF, 0, 0, 1)

    label("loc_B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_BA4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 43)

    label("loc_BA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C0A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")
    Event(0, 34)

    label("loc_BD8")

    Jump("loc_C05")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF4")
    Event(0, 32)
    Jump("loc_C05")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05")
    Event(0, 33)

    label("loc_C05")

    Jump("loc_C30")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C30")
    Event(0, 56)

    label("loc_C30")

    Jump("loc_C66")

    label("loc_C35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C66")
    Event(0, 37)

    label("loc_C66")

    Return()

    # Function_4_5F1 end

    def Function_5_C67(): pass

    label("Function_5_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C83")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C9A")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C9A")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CB7")
    Jump("loc_D6F")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC5")
    Jump("loc_D6F")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDD")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_CDD")

    Jump("loc_D6F")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CF0")
    Jump("loc_D6F")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CFE")
    Jump("loc_D6F")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D0C")
    Jump("loc_D6F")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D1F")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_D6F")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D2D")
    Jump("loc_D6F")

    label("loc_D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D3B")
    Jump("loc_D6F")

    label("loc_D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D49")
    Jump("loc_D6F")

    label("loc_D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D57")
    Jump("loc_D6F")

    label("loc_D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8A")
    ModifyEventFlags(1, 2, 0x80)
    OP_1B(0x2, 0x0, 0x2A)

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9E")
    ClearMapObjFlags(0x1A, 0x4)

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DDA")
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFrame(0xFF, "curtain", 0x0, 0x1)
    SetMapObjFrame(0x1B, "kesu", 0x0, 0x1)

    label("loc_DDA")

    Return()

    # Function_5_C67 end

    def Function_6_DDB(): pass

    label("Function_6_DDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3E")

    #C0001
    ChrTalk(
        0xFE,
        "どうだい、凄い気迫だろう？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "みんな今はとにかく、\x01",
            "一刻も早い公演再開のために\x01",
            "全力で頑張ってくれているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "イリア君も目を\x01",
            "覚ましてくれたと聞いたし……\x01",
            "彼女の期待に応えるためにもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00000F（……劇団の皆さんは\x01",
            "  リーシャの行方すら\x01",
            "  知らない状態なんだよな。）\x02\x03",

            "（顔だけでも\x01",
            "  見せてあげたい気もするけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1025")

    label("loc_F3E")


    #C0005
    ChrTalk(
        0xFE,
        (
            "我々はいつものように\x01",
            "ここで舞台を磨き上げながら\x01",
            "待たせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "ロイド君たち、\x01",
            "リーシャ君のことは\x01",
            "どうかよろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#00000Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1025")

    #C0008
    ChrTalk(
        0x106,
        (
            "#10700F劇団長……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1025")

    Jump("loc_149B")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10AE")

    #C0009
    ChrTalk(
        0xFE,
        (
            "みんな、本当に\x01",
            "よく頑張ってくれているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "イリア君、そしてリーシャ君……\x01",
            "私たちは君たちを待っているからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149B")

    label("loc_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1249")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    #C0011
    ChrTalk(
        0xB,
        "ああ、ロイド君か……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        "……………………………\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#00003F劇団長……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        "ああ……すまない。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "色々考えると、どうにも\x01",
            "不安になってしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "あのイリア君のことだ。\x01",
            "必ず目を覚ましてくれると\x01",
            "信じているんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        "#00108F劇団長さん……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "ふう、だがくよくよばかりも\x01",
            "していられないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "私も……もう少し、\x01",
            "しゃきっとしないと。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x18D, 0)
    Jump("loc_12B7")

    label("loc_1249")


    #C0020
    ChrTalk(
        0xFE,
        (
            "ふう、私もそろそろ\x01",
            "しゃきっとしないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "いつまでもこんな風じゃ、\x01",
            "イリア君に怒られてしまうからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B7")

    Jump("loc_149B")

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1334")

    #C0022
    ChrTalk(
        0xFE,
        "すまないね、ロイド君たち。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "本番まで時間もないからね。\x01",
            "みんなギリギリまで\x01",
            "準備していたいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149B")

    label("loc_1334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1342")
    Jump("loc_149B")

    label("loc_1342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1350")
    Jump("loc_149B")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_135E")
    Jump("loc_149B")

    label("loc_135E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_136C")
    Jump("loc_149B")

    label("loc_136C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_137A")
    Jump("loc_149B")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1388")
    Jump("loc_149B")

    label("loc_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A3")
    Call(0, 8)
    Jump("loc_140F")

    label("loc_13A3")


    #C0024
    ChrTalk(
        0xFE,
        (
            "まったく、\x01",
            "イリア君は本当に頼もしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "この様子なら、明日の舞台も\x01",
            "必ず成功させてくれるだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140F")

    Jump("loc_149B")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1422")
    Jump("loc_149B")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143D")
    Call(0, 7)
    Jump("loc_149B")

    label("loc_143D")


    #C0026
    ChrTalk(
        0xFE,
        (
            "無理を言うようだが、\x01",
            "よろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "これもイリア君の構想を\x01",
            "実現するためなのでね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149B")

    TalkEnd(0xFE)
    Return()

    # Function_6_DDB end

    def Function_7_149F(): pass

    label("Function_7_149F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175D")

    #C0028
    ChrTalk(
        0xB,
        (
            "それで、ハインツ君。\x01",
            "技術的には可能なのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "そうですね、\x01",
            "勿論やってはみますが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1596")

    #C0030
    ChrTalk(
        0xB,
        "おお、君たちは特務支援課の。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        (
            "もしかして、\x01",
            "何か事件でもあったのかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1628")

    label("loc_1596")


    #C0032
    ChrTalk(
        0xB,
        "おや、君たちは……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 0)

    #C0033
    ChrTalk(
        0xB,
        (
            "おお、君は特務支援課の\x01",
            "ロイド君じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "もしかして、\x01",
            "何か事件でもあったのかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1628")


    #C0035
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、今は市内の各所を\x01",
            "見回っている所でして。\x02\x03",

            "念のため、こちらの方にも\x01",
            "伺わせてもらった次第です。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        (
            "ふむ、そうだったのか。\x01",
            "君たちがパトロールしてくれると\x01",
            "こちらも助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "まあ、また何かあったら\x01",
            "気軽に声をかけてくれるかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00100Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x5A, 0x0)
    SetScenarioFlags(0x136, 4)
    Jump("loc_189C")

    label("loc_175D")


    #C0039
    ChrTalk(
        0xC,
        "でもいいんですか？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "速度を上げると、\x01",
            "それだけ合わせるタイミングも\x01",
            "シビアになりますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "ああ、それは\x01",
            "イリア君も承知の上だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "何でも今度の構想には\x01",
            "シーン全体のテンポアップが\x01",
            "欠かせないらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "限界ギリギリの所まで、\x01",
            "試してみたいそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "そうですか……\x01",
            "ではとにかく見てみます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x1, 3)

    label("loc_189C")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_149F end

    def Function_8_18A5(): pass

    label("Function_8_18A5")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x101, -900, 1250, 26340, 0)
    SetChrPos(0x102, 800, 1250, 26340, 0)
    SetChrPos(0x109, -1500, 1250, 25200, 0)
    SetChrPos(0x105, 0, 1250, 25400, 0)
    SetChrPos(0x104, 1500, 1250, 25200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_68(-610, 2600, 26940, 0)
    MoveCamera(27, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15740, 0)
    OP_0D()

    #C0045
    ChrTalk(
        0xB,
        "おや……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#06105Fあら、弟君たちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#12P#00000Fどうも、お邪魔しています。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "#06202F皆さん、こんにちは。\x02\x03",

            "#06209Fふふ、ランディさんも\x01",
            "ついに復帰されたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#12P#00300Fお、流石はリーシャちゃん。\x01",
            "気にかけてくれて嬉しいぜ。\x02\x03",

            "#00309Fいや～、にしてもイリアさんと\x01",
            "リーシャちゃんの衣装姿……\x02\x03",

            "マジで何度見てもイイッスね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "#06102Fふふ、どうもありがと。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#06204Fあ、改めて言われると\x01",
            "少し恥ずかしいですけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)

    #C0052
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、確かにランディの\x01",
            "視線はいやらしいからね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 500)
    Sleep(300)

    #C0053
    ChrTalk(
        0x104,
        (
            "#11P#00301F何だと、ワジ。\x01",
            "俺はいたって純粋な気持ちで――\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0054
    ChrTalk(
        0x102,
        (
            "#11P#00106Fはいはい、分かったから\x01",
            "そのくらいにしてくれるかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1C70():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C70)
    Sleep(50)

    def lambda_1C80():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1C80)
    Sleep(50)

    def lambda_1C90():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C90)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    #C0055
    ChrTalk(
        0x109,
        "#12P#10109Fあ、あはは……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#12P#00006F騒がしくてすみません。\x02\x03",

            "#00000Fところで、今って\x01",
            "練習中だったんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#06100Fまあね。\x01",
            "明日の夜の舞台に向けて\x01",
            "調整していたところよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0058
    ChrTalk(
        0x9,
        (
            "#06202Fふふ、明日は\x01",
            "お客さんがお客さんだけに\x01",
            "緊張もしますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        (
            "ああ、まさか各国首脳の方々が\x01",
            "観劇にいらしてくれるなんてね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0060
    ChrTalk(
        0x101,
        "#12P#00005F首脳が……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#12P#00105Fそういえば、今朝の対策会議でも\x01",
            "議題に挙がっていたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、何しろせっかく\x01",
            "クロスベルに招待するんだ。\x02\x03",

            "#10304Fアルカンシェルの舞台は\x01",
            "最高の持て成しだろうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#12P#00300Fま、そう考えると、\x01",
            "あって然るべき趣向ってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#12P#10100Fでも、確かにそれは緊張しますよね。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "#06203Fええ、他の団員の方たちも\x01",
            "どこかしら落ち着かなさそうで……\x02\x03",

            "#06209Fといっても、イリアさんは\x01",
            "いつもと変わらないんですけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0066
    ChrTalk(
        0x8,
        (
            "#06103Fんー、だっていちいち\x01",
            "気にしてもしょうがないじゃない。\x02\x03",

            "#06100F客席に誰が座ってようと、\x01",
            "とにかくベストを尽くすだけだし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)

    #C0067
    ChrTalk(
        0xB,
        (
            "#11Pまったく君は……\x01",
            "いつも呆れるほど頼もしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "#11P今度のリニューアル公演の発案といい、\x01",
            "その気力には毎度ながら感心するよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x101,
        "#12P#00005Fリニューアル公演……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#12P#00100Fそういえば……\x01",
            "今度『金の太陽、銀の月』を\x01",
            "リニューアルされるんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        (
            "#12P#10300Fああ、世間では既に\x01",
            "もっぱらの噂だね。\x02\x03",

            "何でも大胆なアレンジが\x01",
            "加えられるそうだけど？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21F5)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0072
    ChrTalk(
        0x8,
        (
            "#06109Fええ、そうなのよ。\x02\x03",

            "#06104F一旦完成したものに手を加えるのは\x01",
            "ある意味、挑戦だったんだけど……\x02\x03",

            "#06100F脚本、演出の観点からも\x01",
            "より完成度を高められそうな\x01",
            "目処がようやく付いてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#06202Fはい、そして今度の一般公演が\x01",
            "終わったら、約１ヶ月その特訓に\x01",
            "集中させてもらう予定なんです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_END)), "loc_2429")

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#00000Fなるほど、以前お会いした時に\x01",
            "『忙しくなりそう』と仰っていたのは\x01",
            "このことだったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "#06100Fフフ、そういうこと。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        (
            "#12P#12P#10100Fですが１ヶ月も特訓だなんて……\x01",
            "アレンジといっても相当\x01",
            "力が入っているみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247A")

    label("loc_2429")


    #C0077
    ChrTalk(
        0x109,
        (
            "#12P#10100Fなるほど……\x01",
            "アレンジといっても相当\x01",
            "力が入っているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247A")


    #C0078
    ChrTalk(
        0x104,
        (
            "#12P#00300F『金の太陽、銀の月』は、\x01",
            "アルカンシェルの舞台の中でも\x01",
            "特に完成度が高いって評判だが……\x02\x03",

            "#00304Fあれがさらに良くなるなんて、\x01",
            "どんな代物になるか想像できねえなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#12P#00000Fああ、本当だな。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "#06100Fフフ、舞台に生きていくと決めた以上は、\x01",
            "常に最高のものを求めていかないとね。\x02\x03",

            "#06104F観に来てくれるお客さんに\x01",
            "最高の時間を過ごして貰えるような、\x01",
            "素晴らしい舞台を作り上げること……\x02\x03",

            "#06100Fそれがアルカンシェルの、\x01",
            "そしてあたしたちアーティストの\x01",
            "最大の使命なんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#12P#00102F舞台にかけては\x01",
            "右に出る者がいないというか……\x01",
            "流石はイリアさんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        (
            "#12P#10109Fうーん、リニューアル公演が\x01",
            "物凄く楽しみになってきました！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#06100Fフフ、正式発表が近い内にあるから\x01",
            "待っていてちょうだい。\x02\x03",

            "以前の公演を観てくれた人でも、\x01",
            "楽しんで貰える出来になるはずよ。\x02\x03",

            "#06104Fそれに配役にちょっとした\x01",
            "サプライズもあるし……\x01",
            "きっと驚いて貰えると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#00000Fサプライズですか……\x01",
            "はは、じゃあ是非それも\x01",
            "楽しみにさせてもらいますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0x5A, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, 0, 1250, 27240, 180)
    SetScenarioFlags(0x14B, 6)
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_18A5 end

    def Function_9_287B(): pass

    label("Function_9_287B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_288C")
    Jump("loc_2F10")

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_289A")
    Jump("loc_2F10")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2971")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0085
    ChrTalk(
        0x8,
        (
            "#01700Fじゃあ今から、２人の姫の\x01",
            "後を追って《月の姫》が現れる\x01",
            "場面を確認するわよ。\x02\x03",

            "リーシャ、シュリ、準備はいい？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        "#01800Fはい……お願いします！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        "#04200Fこっちも大丈夫だ！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_2F10")

    label("loc_2971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2982")
    Call(0, 10)
    Jump("loc_2F10")

    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2990")
    Jump("loc_2F10")

    label("loc_2990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_299E")
    Jump("loc_2F10")

    label("loc_299E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B9")
    Call(0, 30)
    Jump("loc_2B38")

    label("loc_29B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA6")

    #C0088
    ChrTalk(
        0x8,
        (
            "#01709Fふふ、昔のことなんか\x01",
            "久々に思い出しちゃったわ。\x02\x03",

            "#01700Fまあ、よかったら\x01",
            "今度のリニューアル公演も\x01",
            "ぜひ観にきてちょうだい。\x02\x03",

            "あそこで頑張ってる\x01",
            "リーシャとシュリもいるし、\x01",
            "必ず素晴らしい舞台になるはずだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B38")

    label("loc_2AA6")


    #C0089
    ChrTalk(
        0x8,
        (
            "#01700F今度のリニューアル公演も\x01",
            "ぜひ観にきてちょうだい。\x02\x03",

            "あそこで頑張ってる\x01",
            "リーシャとシュリもいるし、\x01",
            "必ず素晴らしい舞台になるはずだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B38")

    Jump("loc_2F10")

    label("loc_2B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B4B")
    Jump("loc_2F10")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B59")
    Jump("loc_2F10")

    label("loc_2B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B74")
    Call(0, 8)
    Jump("loc_2D3D")

    label("loc_2B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C96")

    #C0090
    ChrTalk(
        0x8,
        (
            "#06100F舞台に生きていくと決めた以上は、\x01",
            "常に最高のものを求めていかないとね。\x02\x03",

            "#06104F観に来てくれるお客さんに\x01",
            "最高の時間を過ごして貰えるような、\x01",
            "素晴らしい舞台を創り上げること……\x02\x03",

            "#06102Fそれがアルカンシェルの、\x01",
            "そしてあたしたちアーティストの\x01",
            "最大の使命なんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D3D")

    label("loc_2C96")


    #C0091
    ChrTalk(
        0x8,
        (
            "#06100Fフフ、リニューアル公演については\x01",
            "正式発表が近い内にあるから\x01",
            "待っていてちょうだい。\x02\x03",

            "#06104F以前の公演を観てくれた人でも、\x01",
            "楽しんで貰える出来になるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3D")

    Jump("loc_2F10")

    label("loc_2D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D50")
    Jump("loc_2F10")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8C")

    #C0092
    ChrTalk(
        0x8,
        (
            "#01700Fフフ、新顔も入って弟君たちも\x01",
            "いよいよ再始動って感じね。\x02\x03",

            "#01700Fセシルも弟君たちに会えるのを\x01",
            "楽しみにしてたみたいよ。\x02\x03",

            "#01709Fいや～ニクいわね、このこの㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00012Fは、はは……\x01",
            "からかわないでくださいよ。\x02\x03",

            "#00004F（でも、セシル姉にも近い内に\x01",
            "  ちゃんと挨拶にいかないとな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F10")

    label("loc_2E8C")


    #C0094
    ChrTalk(
        0x8,
        (
            "#01700Fフフ、あたしたちの今後の展開も\x01",
            "ぜひ楽しみにしといてちょうだい。\x02\x03",

            "#01709Fまだヒミツだけど、\x01",
            "きっと面白いことになるから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F10")

    TalkEnd(0xFE)
    Return()

    # Function_9_287B end

    def Function_10_2F14(): pass

    label("Function_10_2F14")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0095
    ChrTalk(
        0x8,
        (
            "#06100Fさあ、シュリ。\x01",
            "本番まで時間もないし、\x01",
            "ビシビシ行くわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        "#12201Fお、おう……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_2F14 end

    def Function_11_2F85(): pass

    label("Function_11_2F85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F96")
    Jump("loc_34E7")

    label("loc_2F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FA4")
    Jump("loc_34E7")

    label("loc_2FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300B")

    #C0097
    ChrTalk(
        0x9,
        "#01808F――すみません、本番前ですから。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00008F（リーシャ………）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3034")

    label("loc_300B")


    #C0099
    ChrTalk(
        0x9,
        "#01801Fイリアさん……お願いします！\x02",
    )

    CloseMessageWindow()

    label("loc_3034")

    Jump("loc_34E7")

    label("loc_3039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3047")
    Jump("loc_34E7")

    label("loc_3047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3055")
    Jump("loc_34E7")

    label("loc_3055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3063")
    Jump("loc_34E7")

    label("loc_3063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3071")
    Jump("loc_34E7")

    label("loc_3071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_307F")
    Jump("loc_34E7")

    label("loc_307F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_308D")
    Jump("loc_34E7")

    label("loc_308D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A8")
    Call(0, 8)
    Jump("loc_32F1")

    label("loc_30A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3273")

    #C0100
    ChrTalk(
        0x9,
        (
            "#06203F通商会議……本当に色んな人が\x01",
            "このクロスベルに来るんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00000Fやっぱり、\x01",
            "リーシャも緊張してるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "#06208Fええ、それもありますけど……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#00105F何か他に心配事があるんですか？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "#06202Fああいえ、別に\x01",
            "大したことじゃないので\x01",
            "気にしないでください。\x02\x03",

            "#06204Fそうですよね、\x01",
            "とにかく今は舞台に\x01",
            "集中することだけ考えないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00005Fあ、ああ……\x02\x03",

            "#00003F（リーシャ、通商会議で\x01",
            "  何か気になることがあるのか？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 0)
    Jump("loc_32F1")

    label("loc_3273")


    #C0106
    ChrTalk(
        0x9,
        (
            "#06206F私って結構、余計なことを\x01",
            "考えちゃうタイプなんですよね。\x02\x03",

            "#06201Fとにかく、今は舞台に\x01",
            "集中することだけ考えないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F1")

    Jump("loc_34E7")

    label("loc_32F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3304")
    Jump("loc_34E7")

    label("loc_3304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3446")

    #C0107
    ChrTalk(
        0x9,
        (
            "#01802F新メンバーを加えての再始動……\x01",
            "これからも皆さんの\x01",
            "活躍を応援させていただきますね。\x02\x03",

            "よければ、こちらの方にも\x01",
            "またいつでも遊びに来てください。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そっちもまた何かあったら\x01",
            "いつでも相談しにきてくれ。\x02\x03",

            "必ず力を貸させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "#01809Fふふ、頼りにしていますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34E7")

    label("loc_3446")


    #C0110
    ChrTalk(
        0x9,
        (
            "#01802F新メンバーを加えての再始動……\x01",
            "これからも皆さんの\x01",
            "活躍を応援させていただきますね。\x02\x03",

            "#01809Fよければ、こちらの方にも\x01",
            "またいつでも遊びに来てください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E7")

    TalkEnd(0xFE)
    Return()

    # Function_11_2F85 end

    def Function_12_34EB(): pass

    label("Function_12_34EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3511")
    Call(0, 58)
    Return()

    label("loc_3511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352F")
    Call(0, 35)
    Jump("loc_3CA8")

    label("loc_352F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3862")

    #C0111
    ChrTalk(
        0xA,
        (
            "#04200Fそういや、アンタたちって\x01",
            "もうイリアさんの所に\x01",
            "お見舞いに行ったんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00000Fああ、元気な姿を\x01",
            "何度か拝見させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#04203Fそうか……\x02\x03",

            "#04200Fえっと、リーシャ姉は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x106,
        (
            "#10708Fうん……まだ面と向かって\x01",
            "会ってはいないけど、\x01",
            "病室の扉越しに声をかけられて……\x02\x03",

            "#10702Fなんていうか……\x01",
            "ごめんね、シュリちゃん。\x01",
            "すいぶん心配をかけちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "#04205Fそんな、オレは別に何も……\x02\x03",

            "#04204Fでも……\x01",
            "なんか安心できた気がする。\x02\x03",

            "#04202Fこれでようやく、\x01",
            "リーシャ姉はどこにもいかないって\x01",
            "確信できた気がするから。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x106,
        "#10702Fシュリちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0117
    ChrTalk(
        0xA,
        (
            "#04206Fごめん、リーシャ姉。\x01",
            "なんか生意気なこと言って。\x02\x03",

            "#04202Fとりあえず、オレは\x01",
            "ずっとここで待ってるからさ。\x02\x03",

            "#04209Fとにかく、早く帰って来てよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x106,
        "#10702Fふふ……うん、分かった。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B6E")

    label("loc_3862")


    #C0119
    ChrTalk(
        0xA,
        (
            "#14000Fそういや、アンタたちって\x01",
            "もうイリアさんの所に\x01",
            "お見舞いに行ったんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#00000Fああ、元気な姿を\x01",
            "何度か拝見させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "#14003Fそうか……\x02\x03",

            "#14000Fえっと、リーシャ姉は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x106,
        (
            "#10708Fうん……まだ面と向かって\x01",
            "会ってはいないけど、\x01",
            "病室の扉越しに声をかけられて……\x02\x03",

            "#10702Fなんていうか……\x01",
            "ごめんね、シュリちゃん。\x01",
            "すいぶん心配をかけちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        (
            "#14005Fそんな、オレは別に何も……\x02\x03",

            "#14004Fでも……\x01",
            "なんか安心できた気がする。\x02\x03",

            "#14002Fこれでようやく、\x01",
            "リーシャ姉はどこにもいかないって\x01",
            "確信できた気がするから。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x106,
        "#10702Fシュリちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0125
    ChrTalk(
        0xA,
        (
            "#14006Fごめん、リーシャ姉。\x01",
            "なんか生意気なこと言って。\x02\x03",

            "#14002Fとりあえず、オレは\x01",
            "ずっとここで待ってるからさ。\x02\x03",

            "#14009Fとにかく、早く帰って来てよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x106,
        "#10702Fふふ……うん、分かった。\x02",
    )

    CloseMessageWindow()

    label("loc_3B6E")

    SetScenarioFlags(0x1CF, 7)
    Jump("loc_3CA8")

    label("loc_3B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3C16")

    #C0127
    ChrTalk(
        0xA,
        (
            "#04200Fどこに行くかは知らないけど、\x01",
            "くれぐれも気を付けてくれよ。\x02\x03",

            "#04202Fまた近い内に公演も再開するんだ。\x01",
            "その時は絶対観に来てもらうからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA8")

    label("loc_3C16")


    #C0128
    ChrTalk(
        0xA,
        (
            "#14000Fどこに行くかは知らないけど、\x01",
            "くれぐれも気を付けてくれよ。\x02\x03",

            "#14002Fまた近い内に公演も再開するんだ。\x01",
            "その時は絶対観に来てもらうからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA8")

    Jump("loc_3FF6")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC8")
    Call(0, 13)
    Jump("loc_3D1D")

    label("loc_3CC8")


    #C0129
    ChrTalk(
        0xA,
        (
            "#12203F……まず音が来て、\x01",
            "それから舞台袖から飛び出すように\x01",
            "ステップを踏んで……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1D")

    Jump("loc_3FF6")

    label("loc_3D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D30")
    Jump("loc_3FF6")

    label("loc_3D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D72")

    #C0130
    ChrTalk(
        0xA,
        (
            "#04201Fイリアさん、\x01",
            "オレはいつでも大丈夫だぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF6")

    label("loc_3D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D83")
    Call(0, 10)
    Jump("loc_3FF6")

    label("loc_3D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D91")
    Jump("loc_3FF6")

    label("loc_3D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D9F")
    Jump("loc_3FF6")

    label("loc_3D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DAD")
    Jump("loc_3FF6")

    label("loc_3DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC8")
    Call(0, 14)
    Jump("loc_3E3E")

    label("loc_3DC8")


    #C0131
    ChrTalk(
        0xA,
        (
            "#04203F今は目の前の舞台にしろ……\x01",
            "つまり、そういうことだな。\x02\x03",

            "#04201Fよ、よし……\x01",
            "余計なこと考えずに練習するぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3E")

    Jump("loc_3FF6")

    label("loc_3E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E51")
    Jump("loc_3FF6")

    label("loc_3E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED6")

    #C0132
    ChrTalk(
        0xA,
        (
            "#04206Fやっぱ、イリアさんと\x01",
            "リーシャ姉はすげえよなぁ。\x02\x03",

            "#04200Fオレもいつかは\x01",
            "２人みたいな演技を……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F52")

    label("loc_3ED6")


    #C0133
    ChrTalk(
        0xA,
        (
            "#04205Fあっと、いけない。\x01",
            "早いトコ掃除を終わらせないと。\x02\x03",

            "#04203Fうだうだしてると、\x01",
            "稽古の時間がなくなっちゃうからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F52")

    Jump("loc_3FF6")

    label("loc_3F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F65")
    Jump("loc_3FF6")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FF6")

    #C0134
    ChrTalk(
        0xA,
        (
            "#04200Fそれにしても……\x01",
            "リーシャ姉が休息の取り方を\x01",
            "改善したとか、なんで分かるんだろ。\x02\x03",

            "#04204F……やっぱ、イリアさんはすごいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF6")

    TalkEnd(0xFE)
    Return()

    # Function_12_34EB end

    def Function_13_3FFA(): pass

    label("Function_13_3FFA")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0135
    ChrTalk(
        0x11,
        (
            "では、ニコル、シュリ。\x01",
            "付いていきますから始めて下さいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xF,
        (
            "分かりました。\x01",
            "行くぞ、シュリ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#12201Fああ、まずはステップからの\x01",
            "ジャンプだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00000F（シュリや他の皆さん……\x01",
            "  練習に専念しているみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_13_3FFA end

    def Function_14_40FE(): pass

    label("Function_14_40FE")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0139
    ChrTalk(
        0xA,
        (
            "#04205Fなあ、ニコルさん。\x02\x03",

            "イリアさんたちは何で\x01",
            "リニューアル公演の詳しい内容を\x01",
            "みんなに話してくれないんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xF,
        (
            "ああ、本当の所は分からないけど、\x01",
            "とにかくまだ最終公演が残ってるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xF,
        (
            "それも終わらない内に次の話をして\x01",
            "集中できなくなっても困るから……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xF,
        "おそらく、そんな理由じゃないかな？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#04203Fそ、そうか……なるほど。\x01",
            "ニコルさんは賢いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xF,
        "いや、別に普通だと思うけど……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_14_40FE end

    def Function_15_42A8(): pass

    label("Function_15_42A8")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0145
    ChrTalk(
        0xA,
        (
            "#04200Fなあ、ニコルさん。\x01",
            "あのシーンでやってる回転への\x01",
            "切り替わりなんだけどさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xF,
        (
            "ああ、あれは一呼吸で\x01",
            "一気につなげてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xF,
        (
            "タイミングは難しいけど、\x01",
            "その方が滑らかだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        "#04201Fそ、そうか、やってみる。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441F")

    #C0149
    ChrTalk(
        0x101,
        (
            "#00000F（シュリ……頑張って\x01",
            "  練習しているみだいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#00100F（ええ、ひたむきさが\x01",
            "  伝わってくるわね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_449D")

    label("loc_441F")


    #C0151
    ChrTalk(
        0x101,
        (
            "#00005F（この子は、アルカンシェルの\x01",
            "  新人の女の子か……）\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        (
            "#00100F（ふふ、ひたむきに\x01",
            "  練習に励んでいるみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449D")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_15_42A8 end

    def Function_16_44B6(): pass

    label("Function_16_44B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44DF")
    Call(0, 36)
    Return()

    label("loc_44DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44F0")
    Jump("loc_4A9A")

    label("loc_44F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_458C")

    #C0153
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "外出禁止令だなんて\x01",
            "突然過ぎてかなり混乱したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "ま、なにはともあれ\x01",
            "ここに残った以上は練習に\x01",
            "集中するだけだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A9A")

    label("loc_458C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A7")
    Call(0, 13)
    Jump("loc_45DE")

    label("loc_45A7")


    #C0155
    ChrTalk(
        0xFE,
        (
            "最初はシュリのタイミングに\x01",
            "合わせて、それから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DE")

    Jump("loc_4A9A")

    label("loc_45E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_45F1")
    Jump("loc_4A9A")

    label("loc_45F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460C")
    Call(0, 24)
    Jump("loc_468B")

    label("loc_460C")


    #C0156
    ChrTalk(
        0xFE,
        (
            "よ、よく分からないけど\x01",
            "何かを踏んでしまったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "まあいいや……\x01",
            "先輩も言ってることだし、\x01",
            "早く練習しないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468B")

    Jump("loc_4A9A")

    label("loc_4690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_469E")
    Jump("loc_4A9A")

    label("loc_469E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46AC")
    Jump("loc_4A9A")

    label("loc_46AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46BA")
    Jump("loc_4A9A")

    label("loc_46BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_46C8")
    Jump("loc_4A9A")

    label("loc_46C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_475E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E3")
    Call(0, 14)
    Jump("loc_4759")

    label("loc_46E3")


    #C0158
    ChrTalk(
        0xFE,
        "何ていうか、シュリは素直だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "でも、だからこそ\x01",
            "見習うべき所も多いんだよな。\x01",
            "僕ももっと頑張らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4759")

    Jump("loc_4A9A")

    label("loc_475E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_476C")
    Jump("loc_4A9A")

    label("loc_476C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4895")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47EA")

    #C0160
    ChrTalk(
        0xFE,
        (
            "よっと……\x01",
            "これからまた練習なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "問診表のことは\x01",
            "君たちに任せたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4890")

    label("loc_47EA")


    #C0162
    ChrTalk(
        0xFE,
        (
            "明日の公演も心配だけど、\x01",
            "リニューアル舞台の具体的な内容が\x01",
            "気になって仕方ないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "まあでも、余計なことを\x01",
            "考えてちゃダメだよな。\x01",
            "今はとにかく練習あるのみさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4890")

    Jump("loc_4A9A")

    label("loc_4895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48A3")
    Jump("loc_4A9A")

    label("loc_48A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F5")

    #C0164
    ChrTalk(
        0xFE,
        (
            "シュリはまだ下働きだけど……\x01",
            "演技の練習なんかに参加すると、\x01",
            "その動きのキレはハンパないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "ウチの団員は殆んどそうだけど、\x01",
            "ああいうのを天才って言うんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "といっても、みんな才能の上に\x01",
            "尋常じゃない努力だって重ねてるんだ。\x01",
            "比較するものでもないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "とにかく、僕は僕で精一杯やるだけさ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4A9A")

    label("loc_49F5")


    #C0168
    ChrTalk(
        0xFE,
        (
            "才能ではみんなに\x01",
            "劣るかもしれないけど、僕は僕で\x01",
            "最近少しずつ認められて来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "一時期は迷路にも陥っちゃったけど……\x01",
            "とにかく、僕は僕で精一杯やるだけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9A")

    TalkEnd(0xFE)
    Return()

    # Function_16_44B6 end

    def Function_17_4A9E(): pass

    label("Function_17_4A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA7")

    #C0170
    ChrTalk(
        0xC,
        "ああ、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "実はさきほど、\x01",
            "マイスターから直接こちらに\x01",
            "連絡をいただきましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "さっそく自動人形#8Rオートマタ#の製作に\x01",
            "取り掛かっていただけることに\x01",
            "なったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000Fへえ……\x01",
            "それは良かったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        "ええ、本当に。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "そもそも、マイスターの方から\x01",
            "わざわざ連絡を下さるなんて\x01",
            "滅多にないことですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        "こんなに嬉しいことはありませんよ。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#00100F（マイスター、やっぱり\x01",
            "  ずいぶん気にかけていたのね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x103,
        "#00200F（ふふ、早く完成するといいですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 6)
    Jump("loc_4D3E")

    label("loc_4CA7")


    #C0179
    ChrTalk(
        0xC,
        (
            "マイスターの方から積極的に\x01",
            "協力をいただけるなんて、\x01",
            "こんなに嬉しいことはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "私も、土台作りの方を\x01",
            "ますます頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3E")

    Jump("loc_5842")

    label("loc_4D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E4A")

    #C0181
    ChrTalk(
        0xFE,
        (
            "マイスターに手掛けて頂いた\x01",
            "舞台装置や自動人形#8Rオートマタ#の復旧は\x01",
            "流石に私では不可能ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "それでも何とか、舞台の体裁を\x01",
            "整えるまでには至りましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "マイスターも心配して\x01",
            "くれていることですし……\x01",
            "またコツコツと築いて行きますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5842")

    label("loc_4E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3A")

    #C0184
    ChrTalk(
        0xFE,
        (
            "ステージの瓦礫も撤去して、\x01",
            "ようやくまともな練習が\x01",
            "出来るようになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "舞台装置を担当する私の仕事は\x01",
            "まだまだスタート地点にすら\x01",
            "程遠いですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "それでも着実にやれることを\x01",
            "進めていきますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4FBD")

    label("loc_4F3A")


    #C0187
    ChrTalk(
        0xFE,
        (
            "舞台装置を担当する私の仕事は\x01",
            "まだまだスタート地点にすら\x01",
            "程遠いですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "それでも着実にやれることを\x01",
            "進めていきますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBD")

    Jump("loc_5842")

    label("loc_4FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5137")

    #C0189
    ChrTalk(
        0xFE,
        (
            "これまでマイスターに協力を頂いて\x01",
            "築き上げて来た舞台装置や自動人形#8Rオートマタ#は\x01",
            "ことごとく破壊されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "マイスターが命を吹き込み、\x01",
            "そして劇団メンバーがその魂を\x01",
            "育んだ無二の作品たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "これらを踏みにじったことは\x01",
            "確かに許し難い暴挙です……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "だが、作品であれば……\x01",
            "また作り直すことができる。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "でもイリアさんは…………！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_51D3")

    label("loc_5137")


    #C0194
    ChrTalk(
        0xFE,
        (
            "……とにかく、私はまた\x01",
            "何度でもアルカンシェルの舞台を\x01",
            "築いてみせますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "こんなことで挫けていたら、\x01",
            "何よりイリアさんに\x01",
            "申し訳が立ちませんからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D3")

    Jump("loc_5842")

    label("loc_51D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529E")

    #C0196
    ChrTalk(
        0xFE,
        (
            "よしっ、これで舞台装置の\x01",
            "セッティングは万全ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "動作の方も、既に昨日の\x01",
            "リハーサルで確認済みですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "あとは本番が始まるのを\x01",
            "今か今かと待つだけですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_530E")

    label("loc_529E")


    #C0199
    ChrTalk(
        0xFE,
        (
            "よしっ、これで舞台装置の\x01",
            "セッティングは万全ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "あとは本番が始まるのを\x01",
            "今か今かと待つだけですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_530E")

    Jump("loc_5842")

    label("loc_5313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5321")
    Jump("loc_5842")

    label("loc_5321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_532F")
    Jump("loc_5842")

    label("loc_532F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_533D")
    Jump("loc_5842")

    label("loc_533D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5454")

    #C0201
    ChrTalk(
        0xFE,
        (
            "知り合いの工房に頼んでいた\x01",
            "リニューアル公演用の舞台装置が\x01",
            "ついに明日完成するそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "今回は色々と無理を言って\x01",
            "困らせてしまいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "マイスターはいつも最後には\x01",
            "何とかしてくれるんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "取りに行くのが今から楽しみです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_54EB")

    label("loc_5454")


    #C0205
    ChrTalk(
        0xFE,
        (
            "今回は色々と無理を言って\x01",
            "困らせてしまいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "マイスターはいつも最後には\x01",
            "何とかしてくれるんですよね。\x01",
            "取りに行くのが今から楽しみです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54EB")

    Jump("loc_5842")

    label("loc_54F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_56FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5659")

    #C0207
    ChrTalk(
        0xFE,
        (
            "新しい舞台装置の構想が\x01",
            "大体まとまったので、これから\x01",
            "具体的な形にしていく所なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "それでも細かい所に関しては、\x01",
            "リニューアル舞台の練習に合わせて\x01",
            "詰めていく必要もあるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "公開日までは、実質あと１ヶ月と\x01",
            "ちょっとしかありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "早くも追い込みのつもりでやらないと、\x01",
            "とても間に合いそうにありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_56FA")

    label("loc_5659")


    #C0211
    ChrTalk(
        0xFE,
        (
            "リニューアル公演の公開日まで、\x01",
            "実質あと１ヶ月とちょっとしか\x01",
            "ありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "早くも追い込みのつもりでやらないと、\x01",
            "とても間に合いそうにありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FA")

    Jump("loc_5842")

    label("loc_56FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_570D")
    Jump("loc_5842")

    label("loc_570D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57BA")

    #C0213
    ChrTalk(
        0xFE,
        (
            "明日は夜の公演に備えて、\x01",
            "午後３時まで各自で休憩時間を\x01",
            "取ることになっているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "せっかくの自由時間ですからね。\x01",
            "除幕式でも見に行ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5842")

    label("loc_57BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_57C8")
    Jump("loc_5842")

    label("loc_57C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E3")
    Call(0, 7)
    Jump("loc_5842")

    label("loc_57E3")


    #C0215
    ChrTalk(
        0xFE,
        "しかし、５割増しですか……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "もちろん全力は尽くしますが、\x01",
            "またとんでもない注文ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5842")

    TalkEnd(0xFE)
    Return()

    # Function_17_4A9E end

    def Function_18_5846(): pass

    label("Function_18_5846")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5903")

    #C0217
    ChrTalk(
        0xFE,
        (
            "こんな状況にも関わらず、\x01",
            "劇団の前で声援を送ってくれる\x01",
            "ファンの子がいるみたいでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "イリアさんがくれたエールも\x01",
            "そうだけど……こんなに\x01",
            "ありがたいことってないよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C36")

    label("loc_5903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_59C9")

    #C0219
    ChrTalk(
        0xFE,
        (
            "俺たちには舞台しかない――\x01",
            "そして幸運なことに今も俺たちを\x01",
            "応援してくれる人たちがいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "ならやることは決まってるよな。\x01",
            "たとえ街がこんな状況でも\x01",
            "いつものように技を磨くだけだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C36")

    label("loc_59C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E4")
    Call(0, 19)
    Jump("loc_5A13")

    label("loc_59E4")


    #C0221
    ChrTalk(
        0xFE,
        (
            "行くぞ、テオドール。\x01",
            "気合い入れろよ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A13")

    Jump("loc_5C36")

    label("loc_5A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A26")
    Jump("loc_5C36")

    label("loc_5A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A41")
    Call(0, 20)
    Jump("loc_5AA7")

    label("loc_5A41")


    #C0222
    ChrTalk(
        0xFE,
        (
            "ま、そうは言いつつ\x01",
            "どんな役でもこなすのが\x01",
            "俺様の真骨頂だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "要求にはきっちり応えるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_5AA7")

    Jump("loc_5C36")

    label("loc_5AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA4")

    #C0224
    ChrTalk(
        0xFE,
        (
            "しかし、さすがは\x01",
            "女王国リベールというべきか……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "クローディア殿下も可憐だが、\x01",
            "ユリア准佐は軍人にしておくのは\x01",
            "勿体なさすぎだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "剣の腕前も一流らしいし、\x01",
            "ウチに入ればすぐに花形女優に\x01",
            "なれると思うんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C36")

    label("loc_5BA4")


    #C0227
    ChrTalk(
        0xFE,
        (
            "ユリア准佐……\x01",
            "あの容姿で軍人ってのは\x01",
            "勿体なさすぎだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "剣の腕前も一流らしいし、\x01",
            "ウチに入ればすぐに花形女優に\x01",
            "なれると思うんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C36")

    TalkEnd(0xFE)
    Return()

    # Function_18_5846 end

    def Function_19_5C3A(): pass

    label("Function_19_5C3A")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0229
    ChrTalk(
        0xD,
        (
            "じゃあ、プリエさん。\x01",
            "さっそく独唱をもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "了解よ、飛ばして行くから\x01",
            "２人共テンション上げてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xE,
        "……分かりました。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_5C3A end

    def Function_20_5CE4(): pass

    label("Function_20_5CE4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0232
    ChrTalk(
        0xD,
        (
            "さあ、テオドール。\x01",
            "次は俺たちのクライマックスシーンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xD,
        (
            "祭壇の守護騎士たるお前が\x01",
            "放蕩王子たる俺に剣を……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xD,
        "って、言ってて悔しくなって来たな。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xD,
        (
            "どうせなら、ここの展開も\x01",
            "リニューアルしてほしかったぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0236
    ChrTalk(
        0xE,
        (
            "はあ……\x01",
            "何を今更なことを言い出すんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xE,
        (
            "いいから黙って合わせろ、\x01",
            "このバカジーン。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0238
    ChrTalk(
        0xD,
        (
            "あ、お前。\x01",
            "今バカジーンっつったな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "ならお前はバカドールだ！\x01",
            "やい、このバカドールが！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xE,
        (
            "……悪かったから、\x01",
            "とにかく早く合わせてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0241
    ChrTalk(
        0x101,
        (
            "#00005F（ほ、本番前とは\x01",
            "  思えない雰囲気だな。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_20_5CE4 end

    def Function_21_5F98(): pass

    label("Function_21_5F98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6055")

    #C0242
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "舞台人というヤツはつくづく\x01",
            "幸せ者だと感じさせられるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "様々な人たちから受けた様々な恩……\x01",
            "いつか何倍にもして返せるよう\x01",
            "益々もって精進していかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_635B")

    label("loc_6055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6063")
    Jump("loc_635B")

    label("loc_6063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_60B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607E")
    Call(0, 19)
    Jump("loc_60B3")

    label("loc_607E")


    #C0244
    ChrTalk(
        0xFE,
        (
            "ああ、ユージーン。\x01",
            "お前こそ振り落とされるなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B3")

    Jump("loc_635B")

    label("loc_60B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_60C6")
    Jump("loc_635B")

    label("loc_60C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_624E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E1")
    Call(0, 20)
    Jump("loc_6249")

    label("loc_60E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DF")

    #C0245
    ChrTalk(
        0xE,
        (
            "……ユージーンは昔から動揺すると\x01",
            "減らず口を叩くクセがあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        (
            "見苦しいようだが、\x01",
            "どうかカンベンしてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#00005Fそ、そうなんですか……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    #C0248
    ChrTalk(
        0xD,
        (
            "おい、テオ。\x01",
            "余計なこと吹き込むんじゃねーよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6249")

    label("loc_61DF")


    #C0249
    ChrTalk(
        0xFE,
        (
            "とにかく……どんな舞台も\x01",
            "初演が特に大事だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "時間のある限り、\x01",
            "演技を見直しておくとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6249")

    Jump("loc_635B")

    label("loc_624E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_635B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631B")

    #C0251
    ChrTalk(
        0xFE,
        "……確かにな。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "クローディア殿下は学生時代に\x01",
            "演劇に参加した経験も\x01",
            "あるという話だったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "きっと、お２人とも\x01",
            "舞台上でも堂々とした姿を\x01",
            "見せ付けてくれるに違いない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_635B")

    label("loc_631B")


    #C0254
    ChrTalk(
        0xFE,
        (
            "確かに……\x01",
            "お２人が舞台に立っている所は\x01",
            "ぜひ見てみたいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_635B")

    TalkEnd(0xFE)
    Return()

    # Function_21_5F98 end

    def Function_22_635F(): pass

    label("Function_22_635F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_63B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_637D")
    Call(0, 19)
    Jump("loc_63B2")

    label("loc_637D")


    #C0255
    ChrTalk(
        0xFE,
        (
            "２人共、いい顔してるわね。\x01",
            "私も負けられないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B2")

    TalkEnd(0xFE)
    Return()

    # Function_22_635F end

    def Function_23_63B6(): pass

    label("Function_23_63B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_63C7")
    Jump("loc_6597")

    label("loc_63C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_64A5")

    #C0256
    ChrTalk(
        0xFE,
        (
            "こんな時に舞台など\x01",
            "不謹慎だという声もありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "わたくしは、\x01",
            "逆にこんな時だからこそ\x01",
            "娯楽が必要なのだと強く思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "だって人間何より不幸なことは、\x01",
            "娯楽を楽しむ余裕をなくすことでしょう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6597")

    label("loc_64A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C0")
    Call(0, 13)
    Jump("loc_64F9")

    label("loc_64C0")


    #C0259
    ChrTalk(
        0xFE,
        (
            "わたくしはわたくしの演技を\x01",
            "より疾く、より美しく……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64F9")

    Jump("loc_6597")

    label("loc_64FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_650C")
    Jump("loc_6597")

    label("loc_650C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6527")
    Call(0, 24)
    Jump("loc_6597")

    label("loc_6527")


    #C0260
    ChrTalk(
        0xFE,
        (
            "まったく、ニコルったら\x01",
            "油断も隙もありませんわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "これが草食系男子の手口ですのね、\x01",
            "ゆ、許せませんわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6597")

    TalkEnd(0xFE)
    Return()

    # Function_23_63B6 end

    def Function_24_659B(): pass

    label("Function_24_659B")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0262
    ChrTalk(
        0x11,
        (
            "さてと……\x01",
            "引き立て役は引き立て役らしく\x01",
            "頑張らさせていただきますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xF,
        (
            "引き立て役だなんて、\x01",
            "そんなことありませんって。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xF,
        (
            "それに僕、セリーヌ先輩の\x01",
            "演技すごく好きですよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    #C0265
    ChrTalk(
        0x11,
        (
            "ななな、大人しく聞いていれば、\x01",
            "突然、何を言い出しますの？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x11,
        (
            "む、無駄口はいいから\x01",
            "早く演技合わせをしますわよ、\x01",
            "このスカポンタンッ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0267
    ChrTalk(
        0xF,
        (
            "……えっと、\x01",
            "どうして罵られたんだろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_24_659B end

    def Function_25_6776(): pass

    label("Function_25_6776")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_25_6776 end

    def Function_26_677D(): pass

    label("Function_26_677D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67A2")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_26_677D")

    label("loc_67A2")

    Return()

    # Function_26_677D end

    def Function_27_67A3(): pass

    label("Function_27_67A3")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04200.itp")
    SetChrPos(0x101, 700, 1350, 7760, 0)
    SetChrPos(0x102, -700, 1350, 7760, 0)
    SetChrPos(0x109, 700, 1520, 6680, 0)
    SetChrPos(0x105, -700, 1520, 6680, 0)
    OP_68(-640, 1320, 14170, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13720, 0)
    OP_0D()

    #C0268
    ChrTalk(
        0x8,
        "#01702Fでね、それでシュリったら――\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0269
    ChrTalk(
        0xA,
        (
            "#12P#04211Fや、やめろよ……\x01",
            "よりによってリーシャ姉の前でっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x9,
        (
            "#12P#01802Fふふ、イリアさん。\x01",
            "シュリちゃんが困ってるじゃないですか。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 26)
    BeginChrThread(0x9, 0, 0, 26)
    BeginChrThread(0xA, 0, 0, 26)
    OP_68(450, 1620, 11150, 3000)
    MoveCamera(46, 24, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15050, 3000)
    OP_6F(0x79)

    #C0271
    ChrTalk(
        0x101,
        "#12P#00000Fはは、なんだか盛り上ってるな。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、今はちょうど休憩中って\x01",
            "ところみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x109,
        "#12P#10105Fほ、本物のイリア・プラティエ……！\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x105,
        "#12P#10300Fそれと、そばにいる２人は……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    OP_64(0x8)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0275
    ChrTalk(
        0x8,
        "#01700Fん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x8,
        "#01705F……あーっ、弟君じゃない！！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6B3F():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6B3F)
    TurnDirection(0xA, 0x101, 500)

    #C0277
    ChrTalk(
        0x9,
        "#5P#01802Fあ……皆さんっ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C5E")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆前編クエスト「ストーカーの捜査依頼」を？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",          # 0
            "【達成している】\x01",        # 1
            "【達成していない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C45"),
        (1, "loc_6C4A"),
        (2, "loc_6C54"),
        (SWITCH_DEFAULT, "loc_6C5E"),
    )


    label("loc_6C45")

    Jump("loc_6C5E")

    label("loc_6C4A")

    OP_29(0x1D, 0x4, 0x10)
    Jump("loc_6C5E")

    label("loc_6C54")

    OP_29(0x1D, 0x3, 0x10)
    Jump("loc_6C5E")

    label("loc_6C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C87")

    #C0279
    ChrTalk(
        0xA,
        "#04200F……ども。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CA0")

    label("loc_6C87")


    #C0280
    ChrTalk(
        0xA,
        "#04200F……ちっす。\x02",
    )

    CloseMessageWindow()

    label("loc_6CA0")


    def lambda_6CA5():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CA5)

    def lambda_6CBF():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CBF)

    def lambda_6CD9():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CD9)

    def lambda_6CF3():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CF3)
    OP_68(-820, 1620, 12730, 3000)
    MoveCamera(39, 26, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(13510, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    #C0281
    ChrTalk(
        0x101,
        "#12P#00000Fはは、お久しぶりです。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        (
            "#12P#00100Fすみません、休憩時間の\x01",
            "邪魔をしてしまったみたいで……\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0283
    AnonymousTalk(
        0x8,
        (
            "フフ、そんなことないない㈱\x02\x03",

            "久しぶりに会いに来てくれたんだし、\x01",
            "ゆっくりしてってちょうだい。\x02\x03",

            "あ、せっかくだから弟君は\x01",
            "あたしと再会のハグでもやっとく？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0284
    ChrTalk(
        0x101,
        "#12P#00012Fい、いえいえ、結構です。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#5P#01702Fえー、そう？\x01",
            "遠慮しなくてもいいのに。\x02\x03",

            "#01709Fフフ、それとも～……\x01",
            "やっぱり感触のよさそうな\x01",
            "リーシャとのハグがお望みかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    def lambda_6FBB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FBB)
    Sleep(50)

    def lambda_6FCB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6FCB)

    #C0286
    ChrTalk(
        0x101,
        "#12P#00011Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x9,
        "#12P#01806Fイ、イリアさんったら……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        "#12P#04200Fったく、オヤジもいい加減にしろよな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)

    #C0289
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ……\x01",
            "リーシャさんも相変わらず\x01",
            "苦労しているみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0290
    AnonymousTalk(
        0x9,
        (
            "あ、あはは……\x01",
            "こればっかりは宿命みたいな\x01",
            "ものなのかもしれませんけど。\x02\x03",

            "でも、久しぶりに皆さんに会えて\x01",
            "本当にうれしいです。\x02\x03",

            "ふふ、これからまた\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0291
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、リーシャさんは\x01",
            "記念祭の時の公演でデビューした\x01",
            "アーティストだったかな。\x02\x03",

            "#10302Fたしか、旧市街のアパートに\x01",
            "住んでいたんじゃなかったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        (
            "#5P#01802Fは、はい……\x02\x03",

            "#01805Fえっと、そういうあなたはもしかして、\x01",
            "旧市街の不良グループの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#12P#10302Fワジ・ヘミスフィアさ。\x01",
            "フフ、お見知り頂けて光栄だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P#01705Fあらリーシャ、知ってる子なの？\x02\x03",

            "そういえば、そっちの子たちは\x01",
            "以前はいなかったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、２人は支援課の\x01",
            "新メンバーでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        (
            "#12P#10100Fあ、あたしは警備隊から\x01",
            "支援課に出向させてもらっている\x01",
            "ノエル・シーカーと言います！\x02\x03",

            "#10109Fそのっ……イリアさんのことは\x01",
            "妹のフランともども、\x01",
            "いつも応援させていただいてます！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        "#5P#01709Fフフ、ありがと☆\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#12P#00103Fティオちゃんとランディは\x01",
            "まだ戻ってませんけど……\x02\x03",

            "#00100Fしばらくはこの４人で\x01",
            "活動する予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#5P#01700Fなるほどね～。\x02\x03",

            "#01709Fフフ、なかなかエキセントリックな\x01",
            "メンツが集まったみたいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#12P#00012Fい、いや～……\x01",
            "イリアさんには敵いそうに\x01",
            "ありませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x109,
        (
            "#12P#10106Fというか、アーティストの方って\x01",
            "想像してたのよりもずいぶんと\x01",
            "フランクなんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#12P#10302F確かに。\x01",
            "それと雑誌で見るより\x01",
            "美人度合いも格段だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#5P#01702Fフフ、ありがと。\x01",
            "でもそんなに褒めたって\x01",
            "何も出ないわよ？\x02\x03",

            "#01703Fと、それはともかく……\x02\x03",

            "#01709Fほら、さっきから黙ってないで\x01",
            "あんたも挨拶なさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xA,
        "#5P#04205F……わ、分かったよ。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0305
    AnonymousTalk(
        0xA,
        (
            "劇団で下働きをやってる\x01",
            "シュリ・アトレイドだ。\x02\x03",

            "えっと……よろしく。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0306
    ChrTalk(
        0x109,
        "#12P#10100Fふふっ、よろしくねシュリちゃん。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7CBD")

    #C0307
    ChrTalk(
        0x101,
        "#12P#00000Fはは、シュリも元気にしてたか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0308
    ChrTalk(
        0xA,
        (
            "#5P#04203Fフン、にこやかに話しかけんなっつの。\x02\x03",

            "#04201F……言っとくけど、オレはまだ\x01",
            "あの時のこと#12R㈲　㈲　㈲　㈲　㈲　㈲#を忘れてないからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x101,
        "#12P#00006F（ま、まだ根に持ってたのか……）\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        "#12P#10105Fえっと、あの時のことって……？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "#5P#01709Fえっと、確か弟君が\x01",
            "背後からシュリをガッシリと──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0312
    ChrTalk(
        0x101,
        (
            "#12P#00011Fい、いや、違っ……\x02\x03",

            "#00006Fというか、あれはそもそも\x01",
            "根本的な原因はシュリだろ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0313
    ChrTalk(
        0xA,
        (
            "#5P#04205Fな、なんだと！？\x02\x03",

            "#04208F……ま、まあ確かにオレも\x01",
            "悪かったけど……\x02\x03",

            "#04201Fあんな強く抱きついてきといて\x01",
            "よくもヌケヌケと……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7AD9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AD9)
    Sleep(50)

    def lambda_7AE9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7AE9)
    Sleep(50)
    TurnDirection(0x105, 0x101, 500)

    #C0314
    ChrTalk(
        0x109,
        "#12P#10105Fだ、抱きっ……！？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、なにやら楽しそうなことが\x01",
            "あったみたいだねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    TurnDirection(0x101, 0x102, 500)

    #C0316
    ChrTalk(
        0x101,
        "#12P#00011Fい、いやえっと、だから……！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#5P#01709Fおおっ、なんだかいきなりの修羅場ね！\x01",
            "せっかくだからあたしも参加して──\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        (
            "#5P#01806Fイ、イリアさん……\x01",
            "ややこしくなりますから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0319
    ChrTalk(
        0x101,
        (
            "#12P#00006F（うう、この件に関しては\x01",
            "  反論すればするほど\x01",
            "  泥沼にはまる気がするな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_803F")

    label("loc_7CBD")


    #C0320
    ChrTalk(
        0x101,
        "#12P#00005Fえ、シュリ『ちゃん』って……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0321
    ChrTalk(
        0x101,
        (
            "#12P#00011F#4Sお、女の子だったのか！？#3S\x02\x03",

            "#00003Fそ、そうか……\x01",
            "ここに来た時に何度か見かけてたけど、\x01",
            "ぜんぜん気づかなかったよ。\x02\x03",

            "#00000Fうん、確かによく見れば可愛い顔して……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7E4F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E4F)
    Sleep(50)

    def lambda_7E5F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E5F)
    Sleep(50)

    def lambda_7E6F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E6F)
    Sleep(50)

    def lambda_7E7F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7E7F)
    Sleep(50)

    def lambda_7E8F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7E8F)
    Sleep(50)
    TurnDirection(0xA, 0x101, 500)

    #C0322
    ChrTalk(
        0xA,
        "#5P#04201Fこ、この野郎……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x9,
        "#5P#01806Fロ、ロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        "#6P#00111F……さすがに失礼だと思うけど。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0325
    ChrTalk(
        0x101,
        (
            "#11P#00011Fいやその、ゴメン！\x01",
            "男言葉だったからつい……！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        "#5P#01709Fあははっ、さすが弟君ねえ。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x105,
        (
            "#12P#10304Fふむ、天然ジゴロ的には\x01",
            "こういうパターンもアリか。\x01",
            "なかなか勉強になるね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0328
    ChrTalk(
        0x101,
        "#5P#00011Fい、いや、違っ……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xA,
        "#5P#04203F……フン、気に入らないヤツ。\x02",
    )

    CloseMessageWindow()

    label("loc_803F")


    #C0330
    ChrTalk(
        0x9,
        (
            "#5P#01803Fふふ、それにしても……\x01",
            "皆さんお元気そうで何よりです。\x02\x03",

            "#01809F支援課の皆さんには、\x01",
            "本当によくしていただきましたし……\x01",
            "またいつでも遊びに来てくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#5P#01700Fうんうん、あたしも大歓迎よ。\x02\x03",

            "#01704Fそれに、最近のリーシャの練習風景は\x01",
            "以前にも増して見る価値があるしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_81E4():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81E4)
    Sleep(50)

    def lambda_81F4():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81F4)
    Sleep(50)

    def lambda_8204():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8204)
    Sleep(50)

    def lambda_8214():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8214)
    Sleep(50)

    def lambda_8224():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8224)
    Sleep(50)
    TurnDirection(0xA, 0x8, 500)

    #C0332
    ChrTalk(
        0x101,
        "#12P#00005Fへえ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、確かに彼女が\x01",
            "舞台で飛び跳ねていたら\x01",
            "色々#4R㈲　㈲#と見所がありそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x109,
        "#12P#10106Fこ、こらこらワジ君。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x9,
        "#11P#01802Fあ、あはは……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "#5P#01709Fフフ、もちろんそれもあるけど。\x02\x03",

            "#01704Fこの頃は日常のちょっとした所作にも\x01",
            "キレを感じるのよね。\x02\x03",

            "#01702F疲労を感じさせないっていうか……\x01",
            "察するに、休息の取り方でも\x01",
            "改善したってところかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0337
    ChrTalk(
        0x9,
        (
            "#11P#01809F……え、えっとまあ、\x01",
            "そんなところでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0338
    ChrTalk(
        0xA,
        (
            "#6P#04205Fそうなのか……\x01",
            "まったく気付かなかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、イリアさんだからこそ\x01",
            "気付けるレベルの違いみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x9,
        (
            "#11P#01803F（……確かに最近は\x01",
            "  “仕事”が休業中だから、\x01",
            "  十分に休息が取れているけど……）\x02\x03",

            "#01808F（それを肌で感じ取れるなんて、\x01",
            "  やっぱりイリアさんは凄い……）\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは、まあリーシャは\x01",
            "頑張り屋な所があるし……\x02\x03",

            "これからも十分休息をとって、\x01",
            "体を壊さないよう気をつけてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_85DD)
    Sleep(50)
    TurnDirection(0xA, 0x102, 500)

    #C0342
    ChrTalk(
        0x9,
        "#5P#01802Fはい、お気遣いありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        (
            "#12P#00103Fでも、アルカンシェルは\x01",
            "いつも忙しそうだし……\x02\x03",

            "#00100F邪魔にならない程度に\x01",
            "顔を出すくらいが\x01",
            "丁度いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "#5P#01702Fふふ、リハーサル中や\x01",
            "公演中じゃなかったら\x01",
            "いつでも大歓迎よ。\x02\x03",

            "#01703Fまあ、これからはちょっと\x01",
            "忙しくなりそうなんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0345
    ChrTalk(
        0x109,
        "#12P#10105Fえっと……そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x105,
        (
            "#12P#10302F何やら面白いことを\x01",
            "考えていそうだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#5P#01709Fフフ、まだヒ・ミ・ツ㈱\x02\x03",

            "#01700Fま、ウチの今後の展開を\x01",
            "楽しみにしといてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#12P#00000Fはは、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、しっかりと\x01",
            "チェックしていかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    OP_93(0x9, 0x0, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x137, 2)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_27_67A3 end

    def Function_28_8909(): pass

    label("Function_28_8909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 6)), scpexpr(EXPR_END)), "loc_8916")
    Call(0, 29)
    Return()

    label("loc_8916")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -60420, 0, 3700, 90)
    SetChrPos(0x102, -60920, 0, 2700, 90)
    SetChrPos(0x103, -61420, 0, 1700, 90)
    SetChrPos(0x104, -61390, 0, 3700, 90)
    SetChrPos(0x105, -62090, 0, 2700, 90)
    SetChrPos(0x109, -62390, 0, 1700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(-61380, 1500, 2260, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17600, 0)
    OP_0D()

    #C0350
    ChrTalk(
        0x101,
        "#5P#00000Fリーシャ、それにシュリ……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#11P#00100Fシュリちゃん、\x01",
            "《星の姫》の衣装を着ているのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        "#12P#00202F……キレイです。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        (
            "#6P#00305Fだが、シュリぞうの奴……\x01",
            "何か焦ってるように見えねえか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(10, 2900, 24580, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    TurnDirection(0xA, 0xB, 0)
    OP_0D()

    #C0354
    ChrTalk(
        0xA,
        (
            "#12206Fハアハアハア……\x02\x03",

            "#12201Fなあ劇団長、\x01",
            "今のは完璧だったよな？\x02\x03",

            "これなら、イリアさんも\x01",
            "認めてくれるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        (
            "#6Pふむ、もちろん\x01",
            "及第点ではあるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        (
            "#12206Fハ、またそれかよ……\x02\x03",

            "#12200Fなあリーシャ姉、\x01",
            "リーシャ姉はどう思う？\x02\x03",

            "#12202Fオレは間違った動きは\x01",
            "しちゃいなかっただろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        "#06203Fうん、そうね……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0358
    ChrTalk(
        0x9,
        (
            "#06202F……ねえ、シュリちゃん。\x02\x03",

            "次はもう少し感情みたいなものを\x01",
            "込められないかな。\x02\x03",

            "#06204F『こうありたい』って思える自分を\x01",
            "イメージするというか……\x01",
            "うまく説明はできないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0359
    ChrTalk(
        0xA,
        (
            "#12201F『こうありたい』って思える自分……\x01",
            "ぐ、具体的にどうすりゃいいんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-61380, 1500, 2260, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17600, 0)
    OP_0D()

    #C0360
    ChrTalk(
        0x101,
        "#5P#00005F（シュリ……）\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x105,
        (
            "#6P#10300F（ふむ、どうやら僕たちは\x01",
            "  退散した方がよさそうだね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x109,
        (
            "#12P#10103F（うん……\x01",
            "  邪魔は出来ないね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x16D, 6)
    EventEnd(0x5)
    Return()

    # Function_28_8909 end

    def Function_29_8E6A(): pass

    label("Function_29_8E6A")

    EventBegin(0x1)

    #C0363
    ChrTalk(
        0x101,
        (
            "#00000F（リーシャにシュリ……\x01",
            "  どうやら練習に\x01",
            "  集中しているみたいだ。）\x02\x03",

            "#00003F（今は邪魔をしないでおこう。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    EventEnd(0x4)
    Return()

    # Function_29_8E6A end

    def Function_30_8EF9(): pass

    label("Function_30_8EF9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6140, 16219, -4030, 0)
    MoveCamera(355, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17490, 0)
    SetChrPos(0x101, -5460, 15200, -4290, 315)
    SetChrPos(0x102, -6310, 15200, -5170, 0)
    SetChrPos(0x103, -7650, 15200, -4870, 45)
    SetChrPos(0x104, -4700, 15200, -5320, 315)
    SetChrPos(0x105, -8080, 15200, -6150, 45)
    SetChrPos(0x109, -3880, 15200, -6340, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0x2D, 0x0)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0364
    ChrTalk(
        0x8,
        "#5P#01703F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        (
            "#12P#00000Fイリアさん……\x01",
            "ここにいたんですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 500)

    #C0366
    ChrTalk(
        0x8,
        (
            "#5P#01705Fああ、弟君たちか。\x02\x03",

            "#01709Fフフ、リニューアル公演に向けて\x01",
            "激励に来てくれたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        (
            "#6P#00100Fふふ、そんなところです。\x02\x03",

            "イリアさんは、ここから\x01",
            "リーシャさんとシュリちゃんの\x01",
            "練習を見ていたみたいですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(300)

    #C0368
    ChrTalk(
        0x8,
        (
            "#5P#01704Fええ、２階席からだと\x01",
            "全体がよく見えるからね。\x02\x03",

            "#01702Fいやー、それにしても\x01",
            "若いコたちの頑張る姿って\x01",
            "やっぱりいいわよね～。\x02\x03",

            "なんだかこうしてると、\x01",
            "新人だった頃を思い出すわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#12P#00005Fイリアさんが新人だった頃ですか……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#12P#00302Fハハ、なんだか想像つかねえなあ。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、何だったら当時の話とかを\x01",
            "聞いてみたいものだけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0372
    ChrTalk(
        0x8,
        (
            "#5P#01700Fふふ、別にいいけど……\x01",
            "そんなに面白い話でもないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x109,
        (
            "#12P#10109Fわわっ、是非お聞きしたいです！！\x02\x03",

            "#10100F確か、デビュー当時から\x01",
            "『期待の超大型新人』だなんて\x01",
            "雑誌で大きく扱われてましたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        (
            "#6P#00205Fなるほど、デビュー当時から。\x02\x03",

            "#00202Fちなみに……\x01",
            "アーティストを目指したきっかけは\x01",
            "どういったものだったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#5P#01703Fうーん、そうねえ。\x02\x03",

            "#01700Fやっぱり、子供の頃に\x01",
            "アルカンシェルの舞台を\x01",
            "観たことがきっかけかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x104,
        (
            "#12P#00300Fなるほど、それで憧れて──\x01",
            "みたいな感じッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#5P#01703Fんー、ちょっと違うわね。\x02\x03",

            "#01700F当時から、アーティストの演技や\x01",
            "精巧な舞台装置による演出は\x01",
            "素晴らしかったんだけど……\x02\x03",

            "#01706F終わってみたら\x01",
            "何か物足りないっていうか、\x01",
            "納得が行かなかったのよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0378
    ChrTalk(
        0x101,
        "#12P#00011Fな、納得が行かなかったって……\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#5P#01700F実際、周りにいた観客や両親は\x01",
            "絶賛していたし、凄いのは\x01",
            "間違いないはずなんだけど……\x02\x03",

            "#01703Fなんていうか、あたしだったら\x01",
            "もっと良い舞台に出来るのに！って\x01",
            "感じちゃったのよね。\x02\x03",

            "#01702Fフフ、当時はまだ\x01",
            "何の知識もないド素人だったのに\x01",
            "変な話かもしれないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        "#12P#10105Fへぇ、子供の頃にそんな事を……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x105,
        (
            "#6P#10300Fふむ、だけどその流れで\x01",
            "アルカンシェルの門戸を叩いたとなると\x01",
            "衝突とかも多かったんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#5P#01706Fま、ペーペーの新米が\x01",
            "ガンガン口出しするもんだから\x01",
            "そりゃあ、そこそこはねえ。\x02\x03",

            "#01700Fでも、あたしには\x01",
            "絶対に今より良い舞台にしてやるって\x01",
            "確かな信念があったし……\x02\x03",

            "#01709Fそれを示し続けていたら、\x01",
            "自然とみんなにも理解してもらえて、\x01",
            "軋轢#4Rあつれき#もなくなっていったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x103,
        (
            "#6P#00202Fなるほど……\x01",
            "そうして、今のイリアさんが\x01",
            "あるというわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x8,
        (
            "#5P#01704Fフフ、未だに完全に納得できた\x01",
            "舞台っていうのは殆どないけどね。\x02\x03",

            "#01702Fけれど、リーシャやシュリっていう\x01",
            "将来有望な素材も入ってきたことだし……\x02\x03",

            "これからバンバン、\x01",
            "最高の舞台を創って行けるように\x01",
            "したいってところかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#12P#00002Fはは、イリアさんは本当に\x01",
            "貪欲っていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x102,
        (
            "#6P#00104Fふふ、努力に勝る天才なしというけど……\x02\x03",

            "#00109Fイリアさんは努力する天才だもの。\x01",
            "本当に敵なしという感じよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x104,
        "#12P#00309Fああ、言えてるなあ。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "#5P#01709Fふふ、つまらない話を\x01",
            "聞かせちゃったかしら。\x02\x03",

            "#01704Fまあ、よかったら\x01",
            "今度のリニューアル公演も\x01",
            "ぜひ観にきてちょうだい。\x02\x03",

            "#01700Fリーシャもシュリも……\x01",
            "必ず最高の演技を\x01",
            "披露してくれるはずだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#12P#00004Fええ、もちろんです。\x02\x03",

            "#00000Fイリアさんたちの創る最高の舞台……\x01",
            "楽しみにさせていただきますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x2D, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x17C, 3)
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5420, 15200, -4850, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_30_8EF9 end

    def Function_31_9C83(): pass

    label("Function_31_9C83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    SetChrPos(0x101, 700, 1350, 7760, 0)
    SetChrPos(0x102, -700, 1350, 7760, 0)
    SetChrPos(0x109, 700, 1520, 6680, 0)
    SetChrPos(0x105, -700, 1520, 6680, 0)
    SetChrPos(0x103, 700, 1620, 5680, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 1320, 13820, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 500)

    #C0390
    ChrTalk(
        0xB,
        "おや、君たちは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9DB0():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9DB0)

    def lambda_9DBD():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9DBD)
    TurnDirection(0xA, 0x0, 500)

    def lambda_9DD1():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DD1)

    def lambda_9DEB():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DEB)

    def lambda_9E05():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E05)

    def lambda_9E1F():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E1F)

    def lambda_9E39():
        OP_95(0xFE, 700, 1450, 9980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E39)
    WaitChrThread(0x101, 1)

    #C0391
    ChrTalk(
        0x8,
        "#01705Fあら、弟君たちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xA,
        "#04205Fな、何の用だ……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    #C0393
    ChrTalk(
        0x9,
        "#01808F……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(1000)
    TurnDirection(0x102, 0x9, 500)

    #C0394
    ChrTalk(
        0x101,
        "#00003Fリーシャ……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        "#00108Fリーシャさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x8, 0x9, 500)

    #C0396
    ChrTalk(
        0x8,
        (
            "#01705Fなになに、リーシャ。\x01",
            "弟君たちと何かあったわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "#01803F――いえ……\x02\x03",

            "#01801Fイリアさん、それよりもう\x01",
            "本番まで時間がありません。\x02\x03",

            "２人の掛け合いに入る流れを\x01",
            "改めて確認しておきたいんです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)

    #C0398
    ChrTalk(
        0xA,
        (
            "#04200Fそうだよ、イリアさん！\x02\x03",

            "オレだって、あそこの流れは\x01",
            "しっかり把握しておきたいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0399
    ChrTalk(
        0x8,
        "#01705Fあ、うん、それもそうね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0400
    ChrTalk(
        0x8,
        (
            "#01703Fというわけで弟君たち、\x01",
            "特に用事がないようだったら\x01",
            "切り上げてもらっていいかしら？\x02\x03",

            "#01700F今はちょっと集中力を\x01",
            "途切れさせたくないのよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A133():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A133)
    TurnDirection(0x102, 0x8, 500)

    #C0401
    ChrTalk(
        0x101,
        "#00003Fは、はい……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#00103F……お邪魔して\x01",
            "申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_93(0xB, 0x87, 0x0)
    SetScenarioFlags(0x16D, 7)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_31_9C83 end

    def Function_32_A1D8(): pass

    label("Function_32_A1D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3290, 3950, 17840, 0)
    MoveCamera(22, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xF)
    SetChrChipByIndex(0x11, 0x11)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0xB, 170, 450, 11640, 0)
    SetChrPos(0xD, -390, 1250, 19660, 90)
    SetChrPos(0xE, 900, 1250, 20710, 180)
    SetChrPos(0xF, 2040, 1250, 20500, 225)
    SetChrPos(0x10, 280, 1250, 18560, 45)
    SetChrPos(0x11, 1940, 1250, 18990, 315)
    SetChrPos(0xC, -3110, 1250, 19110, 60)
    SetChrPos(0x12, -1810, 1250, 19900, 240)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x101, -600, 2700, -4000, 0)
    SetChrPos(0x102, 600, 2700, -4100, 0)
    SetChrPos(0x103, -600, 2700, -4000, 0)
    SetChrPos(0x104, 600, 2700, -4100, 0)
    SetChrPos(0xF4, -600, 2700, -4000, 0)
    SetChrPos(0xF5, 600, 2700, -4100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A428():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A428)

    def lambda_A442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A442)
    Sleep(100)

    def lambda_A456():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A456)

    def lambda_A470():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A470)
    Sleep(500)

    def lambda_A484():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A484)

    def lambda_A49E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A49E)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_A4E0():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4E0)

    def lambda_A4FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A4FA)
    Sleep(500)

    def lambda_A50E():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A50E)

    def lambda_A528():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A528)
    Sleep(100)

    def lambda_A53C():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A53C)

    def lambda_A556():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A556)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0403
    ChrTalk(
        0x101,
        "#12P#00002Fこれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5EF")

    #C0404
    ChrTalk(
        0x10A,
        (
            "#12P#00602F『金の太陽、銀の月』の\x01",
            "追加シーンというやつか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A62B")

    label("loc_A5EF")


    #C0405
    ChrTalk(
        0x109,
        (
            "#12P#10102F『金の太陽、銀の月』の\x01",
            "追加シーンですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A62B")


    #C0406
    ChrTalk(
        0x103,
        "#12P#00202Fシュリさん、凄いです……\x02",
    )

    CloseMessageWindow()
    OP_68(150, 4650, 13120, 3000)
    MoveCamera(0, 10, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(10510, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(660, 820, 13410, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17510, 0)
    SetChrPos(0x101, -530, 1810, 5540, 0)
    SetChrPos(0x102, 480, 1800, 5350, 0)
    SetChrPos(0x103, -790, 2160, 4170, 0)
    SetChrPos(0x104, 730, 2240, 4050, 0)
    SetChrPos(0xF4, -400, 2240, 2900, 0)
    SetChrPos(0xF5, 680, 2240, 2900, 0)
    OP_0D()

    def lambda_A726():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A726)

    def lambda_A740():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A740)

    def lambda_A75A():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A75A)

    def lambda_A774():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A774)

    def lambda_A78E():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A78E)

    def lambda_A7A8():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A7A8)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    #C0407
    ChrTalk(
        0xB,
        "#5Pおや、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#12P#00000F劇団長、お久しぶりです。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#12P#00100F皆さん、一心不乱に練習に\x01",
            "取り組んでいるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xB,
        (
            "#5Pああ、シュリ君を中心に\x01",
            "考え直した舞台構成も\x01",
            "何とか形になりそうでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xB,
        (
            "#5P今はとにかく、\x01",
            "一刻も早い公演再開のために\x01",
            "全力で頑張ってくれているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xB,
        (
            "#5Pイリア君も目を\x01",
            "覚ましてくれたと聞いたし……\x01",
            "彼女の期待に応えるためにもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#12P#00000Fなるほど……そうでしたか。\x02\x03",

            "#00008F（そういえば、劇団の皆さんは\x01",
            "  リーシャの行方すら\x01",
            "  知らない状態なんだよな。）\x02\x03",

            "#00003F（顔だけでも\x01",
            "  見せてあげたい気もするけど……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 10, 900, 9380, 0)
    SetScenarioFlags(0x1CF, 4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AB0F")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3520, 1250, 22730, 90)
    SetChrPos(0xE, 4800, 1250, 22730, 270)
    SetChrPos(0xA, 0, 1250, 27230, 0)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0x10, 0xF)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_AB9D")

    label("loc_AB0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AB9D")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    SetChrPos(0xD, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_AB9D")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_32_A1D8 end

    def Function_33_ABAF(): pass

    label("Function_33_ABAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(610, 1520, 13160, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17510, 0)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xF)
    SetChrChipByIndex(0x11, 0x11)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0xB, 170, 450, 11640, 0)
    SetChrPos(0xD, -390, 1250, 19660, 90)
    SetChrPos(0xE, 900, 1250, 20710, 180)
    SetChrPos(0xF, 2040, 1250, 20500, 225)
    SetChrPos(0x10, 280, 1250, 18560, 45)
    SetChrPos(0x11, 1940, 1250, 18990, 315)
    SetChrPos(0xC, -3110, 1250, 19110, 60)
    SetChrPos(0x12, -1810, 1250, 19900, 240)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x101, -530, 1810, 5540, 0)
    SetChrPos(0x102, 480, 1800, 5350, 0)
    SetChrPos(0x103, -790, 2160, 4170, 0)
    SetChrPos(0x104, 730, 2240, 4050, 0)
    SetChrPos(0xF4, -400, 2240, 2900, 0)
    SetChrPos(0xF5, 680, 2240, 2900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)

    def lambda_ADB3():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADB3)

    def lambda_ADCD():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADCD)

    def lambda_ADE7():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADE7)

    def lambda_AE01():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE01)

    def lambda_AE1B():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_AE1B)

    def lambda_AE35():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_AE35)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    #C0414
    ChrTalk(
        0xB,
        "#5P君たちか……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xB,
        "#5Pどうだい、凄い気迫だろう？\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)

    #C0416
    ChrTalk(
        0xB,
        (
            "#11Pみんな今はとにかく、\x01",
            "一刻も早い公演再開のために\x01",
            "全力で頑張ってくれているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xB,
        (
            "#11Pイリア君も目を\x01",
            "覚ましてくれたと聞いたし……\x01",
            "彼女の期待に応えるためにもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#12P#00003F（……劇団の皆さんは\x01",
            "  リーシャの行方すら\x01",
            "  知らない状態なんだよな。）\x02\x03",

            "#00008F（顔だけでも\x01",
            "  見せてあげたい気もするけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_33_ABAF end

    def Function_34_B029(): pass

    label("Function_34_B029")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3290, 3950, 17840, 0)
    MoveCamera(22, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xF)
    SetChrChipByIndex(0x11, 0x11)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0xB, 170, 450, 11640, 0)
    SetChrPos(0xD, -390, 1250, 19660, 90)
    SetChrPos(0xE, 900, 1250, 20710, 180)
    SetChrPos(0xF, 2040, 1250, 20500, 225)
    SetChrPos(0x10, 280, 1250, 18560, 45)
    SetChrPos(0x11, 1940, 1250, 18990, 315)
    SetChrPos(0xC, -3110, 1250, 19110, 60)
    SetChrPos(0x12, -1810, 1250, 19900, 240)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x101, -600, 2700, -4000, 0)
    SetChrPos(0x102, 600, 2700, -4100, 0)
    SetChrPos(0x103, -600, 2700, -4000, 0)
    SetChrPos(0x104, 600, 2700, -4100, 0)
    SetChrPos(0xF4, -600, 2700, -4000, 0)
    SetChrPos(0xF5, 600, 2700, -4100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_B279():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B279)

    def lambda_B293():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B293)
    Sleep(100)

    def lambda_B2A7():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2A7)

    def lambda_B2C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B2C1)
    Sleep(500)

    def lambda_B2D5():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2D5)

    def lambda_B2EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B2EF)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_B331():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B331)

    def lambda_B34B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B34B)
    Sleep(500)

    def lambda_B35F():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B35F)

    def lambda_B379():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B379)
    Sleep(100)

    def lambda_B38D():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B38D)

    def lambda_B3A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B3A7)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B507")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0419
    ChrTalk(
        0x101,
        "#12P#00000Fこれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B44A")

    #C0420
    ChrTalk(
        0x10A,
        (
            "#12P#00602F『金の太陽、銀の月』の\x01",
            "追加シーンというやつか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D9")

    label("loc_B44A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B49B")

    #C0421
    ChrTalk(
        0x109,
        (
            "#12P#10102F『金の太陽、銀の月』の\x01",
            "追加シーンですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D9")

    label("loc_B49B")


    #C0422
    ChrTalk(
        0x105,
        (
            "#12P#10402Fフフ、『金の太陽、銀の月』の\x01",
            "追加シーンだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4D9")


    #C0423
    ChrTalk(
        0x103,
        "#12P#00202Fシュリさん、凄いです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B507")


    #C0424
    ChrTalk(
        0x101,
        (
            "#12P#00000Fみんな、まだまだ\x01",
            "練習に励んでいるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x106,
        "#12P#10702F……シュリちゃん、みんな…………\x02",
    )

    CloseMessageWindow()

    label("loc_B576")

    OP_68(150, 4650, 13120, 3000)
    MoveCamera(0, 10, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(10510, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(660, 820, 13410, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17510, 0)
    SetChrPos(0x101, -530, 1810, 5540, 0)
    SetChrPos(0x102, 480, 1800, 5350, 0)
    SetChrPos(0x103, -790, 2160, 4170, 0)
    SetChrPos(0x104, 730, 2240, 4050, 0)
    SetChrPos(0xF4, -400, 2240, 2900, 0)
    SetChrPos(0xF5, 680, 2240, 2900, 0)
    OP_0D()

    def lambda_B648():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B648)

    def lambda_B662():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B662)

    def lambda_B67C():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B67C)

    def lambda_B696():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B696)

    def lambda_B6B0():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B6B0)

    def lambda_B6CA():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B6CA)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B730")

    #C0426
    ChrTalk(
        0xB,
        "#5Pおや、君たちは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B74B")

    label("loc_B730")


    #C0427
    ChrTalk(
        0xB,
        "#5Pああ、君たちか……\x02",
    )

    CloseMessageWindow()

    label("loc_B74B")

    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0428
    ChrTalk(
        0xB,
        (
            "#5Pリーシャ君――\x01",
            "リーシャ君じゃないか！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x0, 0x0)
    Fade(500)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -50, 1250, 25080, 0)
    OP_0D()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0429
    ChrTalk(
        0xA,
        "#5P#N#12211Fリーシャ姉……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(400, 1520, 13900, 2000)
    MoveCamera(34, 16, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(17510, 2000)

    def lambda_B858():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B858)
    Sleep(50)

    def lambda_B868():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B868)
    Sleep(50)

    def lambda_B878():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B878)
    Sleep(50)

    def lambda_B888():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B888)
    Sleep(50)

    def lambda_B898():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B898)
    Sleep(50)

    def lambda_B8A8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8A8)
    Sleep(50)

    def lambda_B8B8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B8B8)
    Sleep(50)

    def lambda_B8C8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B8C8)
    Sleep(100)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0430
    ChrTalk(
        0xF,
        "#5Pほんとだ、リーシャじゃないか！\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xD,
        "#5Pはは、何かの間違いじゃないよな。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xE,
        "#5P……間違いない、確かにリーシャだ。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x10,
        (
            "#5Pふふ、これで\x01",
            "最後の気懸りがなくなったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x106,
        (
            "#12P#10717F……皆さん…………\x02\x03",

            "#10703F……あの、本当にすみませんでした。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10, 1670, 17720, 0)
    MoveCamera(46, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14860, 0)
    SetChrPos(0xB, 650, 0, 15670, 225)
    SetChrPos(0xA, -730, 0, 15940, 180)
    SetChrPos(0x12, -1810, 1250, 19920, 180)
    SetChrPos(0xC, -3020, 1250, 19410, 180)
    SetChrPos(0xD, -1000, 1250, 18840, 180)
    SetChrPos(0xE, -590, 1250, 20230, 180)
    SetChrPos(0xF, 1170, 1250, 20400, 180)
    SetChrPos(0x101, 620, 0, 14370, 315)
    SetChrPos(0x106, -630, 0, 14440, 0)
    SetChrPos(0x102, -780, 450, 12770, 0)
    SetChrPos(0x103, 700, 450, 12660, 0)
    SetChrPos(0x104, -770, 450, 11500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBD6")
    SetChrPos(0x10A, 680, 500, 11260, 0)
    Jump("loc_BC0D")

    label("loc_BBD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBFC")
    SetChrPos(0x109, 680, 500, 11260, 0)
    Jump("loc_BC0D")

    label("loc_BBFC")

    SetChrPos(0x105, 680, 500, 11260, 0)

    label("loc_BC0D")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0435
    ChrTalk(
        0xB,
        (
            "#5Pそうか、今は\x01",
            "支援課の皆さんと一緒に……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x106,
        (
            "#12P#10708Fはい、今はまだ全てを\x01",
            "お話しできませんが……\x02\x03",

            "#10710Fですが、けじめを付けたら\x01",
            "その時はちゃんと……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x10,
        (
            "#5Pふふ、リーシャったら\x01",
            "何をそんなに追い詰めたような\x01",
            "表情をしているの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0438
    ChrTalk(
        0x106,
        "#12P#10712Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x11,
        (
            "#5Pそうですわ、誰もあなたに\x01",
            "そんな顔をしてくれだなんて\x01",
            "頼んでいませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xF,
        (
            "#5Pああ、ホント。\x01",
            "せっかくの美人が台無しだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x106,
        (
            "#12P#10718Fプリエさん……\x01",
            "セリーヌさん、ニコルさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xE,
        (
            "#5Pとにかく……\x01",
            "やることをやったら\x01",
            "一刻も早く戻って来てくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xD,
        (
            "#5Pだな、俺もまだまだリーシャと\x01",
            "試してみたい演技もあることだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x106,
        "#12P#10716Fテオドールさん、ユージーンさん……\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x12,
        (
            "#5Pふふ、私も衣装を\x01",
            "準備して待っていますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xC,
        "#5P私は舞台装置を準備して、ね。\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x106,
        "#12P#10715Fカレリアさん、ハインツさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_68(-630, 1070, 15110, 2000)
    MoveCamera(56, 21, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(11060, 2000)
    OP_6F(0x79)
    OP_64(0xA)

    #C0448
    ChrTalk(
        0xA,
        "#12208F……リーシャ姉………\x02",
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0449
    ChrTalk(
        0x106,
        "#12P#10716Fシュリちゃん……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xA,
        (
            "#12206Fここは……アルカンシェルは……\x01",
            "……リーシャ姉の居場所だから。\x02\x03",

            "#12212Fリーシャ姉が何を抱えているか、\x01",
            "オレには分からないけど……\x02\x03",

            "#12210Fここはリーシャ姉の……\x01",
            "そしてイリアさんやオレの\x01",
            "帰ってくるべき場所でもあって……\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x106,
        "#12P#10718F……シュリちゃん………\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xA,
        (
            "#12212Fオレ……何があってもこの場所を\x01",
            "ずっと守ってるから……だから………\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x106,
        (
            "#12P#10715Fうん……うん……\x02\x03",

            "#10716F……シュリちゃんの気持ちは\x01",
            "十分伝わったわ。\x02\x03",

            "#10716Fちゃんと戻ってくるから……\x01",
            "……だから心配しないで、約束する。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0454
    ChrTalk(
        0xA,
        (
            "#12210F約束……本当だな、リーシャ姉。\x02\x03",

            "嘘つきは針千本なんだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x106,
        "#12P#10715Fうん……分かってる。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    #C0456
    ChrTalk(
        0x101,
        "#11P#00002Fリーシャ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(300)

    #C0457
    ChrTalk(
        0x106,
        (
            "#6P#10715F……ロイドさん。\x01",
            "そろそろ行きましょう。\x02\x03",

            "#10716Fみんなも練習があることだし……\x01",
            "私たちも急いで\x01",
            "目的の場所に向かわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        "#00000Fああ……そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13940, 0)
    SetScenarioFlags(0x1CF, 5)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C420")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3520, 1250, 22730, 90)
    SetChrPos(0xE, 4800, 1250, 22730, 270)
    SetChrPos(0xA, 0, 1250, 27230, 0)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0x10, 0xF)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_C4B3")

    label("loc_C420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C4B3")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    SetChrPos(0xD, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_C4B3")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_34_B029 end

    def Function_35_C4C5(): pass

    label("Function_35_C4C5")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_68(-40, 3900, 28500, 0)
    MoveCamera(0, 2, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20350, 0)
    SetChrPos(0x101, -750, 1250, 25380, 0)
    SetChrPos(0x102, 690, 1250, 25060, 0)
    SetChrPos(0x103, -1940, 1250, 24700, 45)
    SetChrPos(0x104, 1760, 1250, 24400, 315)
    SetChrPos(0xF4, -1200, 1250, 23190, 0)
    SetChrPos(0xF5, 1000, 1250, 23100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0x0, 0x0)
    OP_68(-40, 3200, 28500, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0459
    ChrTalk(
        0xA,
        "#12P#14003F…………………………\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        "#6P#00005Fどうしたんだ、シュリ？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(510, 2700, 24450, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16329, 0)
    Sleep(100)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(1000)

    #C0461
    ChrTalk(
        0xA,
        (
            "#11P#14000Fあ、ああ……\x01",
            "ちょっとお祈り事をな。\x02\x03",

            "#14003F一応コレ、祭壇だからさ。\x01",
            "……セットだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x104,
        (
            "#12P#00302Fはは、なるほどな。\x01",
            "だが意外とご利益がありそうだ。\x02\x03",

            "#00305Fで、一体何を祈ってたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x102,
        (
            "#6P#00106Fちょっとランディ、\x01",
            "そんなの簡単に聞くものじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xA,
        (
            "#11P#14000Fああ、別にいいけど？\x02\x03",

            "#14003F１つはもちろんイリアさんのこと……\x02\x03",

            "そしてもう１つはアンタたちのことだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0465
    ChrTalk(
        0x101,
        "#6P#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x103,
        "#6P#00205Fわたしたち、ですか？\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xA,
        (
            "#11P#14003F…………………………\x02\x03",

            "#14001F……詳しいことは分からないけど\x01",
            "アンタたちはキーアのことを\x01",
            "追ってるんだろ？\x02\x03",

            "それで、これからまた\x01",
            "危険な所に行こうとしてる。\x02\x03",

            "#14003F………………………\x02\x03",

            "#14002Fだから安全祈願ってヤツだ。\x01",
            "リーシャ姉だって一緒だしな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C96D")

    #C0468
    ChrTalk(
        0x106,
        (
            "#6P#10702Fシュリちゃん……\x01",
            "ふふ、ありがとう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA0B")

    label("loc_C96D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9B9")

    #C0469
    ChrTalk(
        0x109,
        (
            "#6P#10102Fなるほど……\x01",
            "シュリちゃん、ありがとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA0B")

    label("loc_C9B9")


    #C0470
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、なるほど……\x01",
            "これはまた嬉しいことを\x01",
            "言ってくれるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0B")


    #C0471
    ChrTalk(
        0x101,
        (
            "#6P#00002Fああ、そんな風に\x01",
            "思ってくれるなんてありがたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xA,
        (
            "#11P#14012Fと、とにかく……\x01",
            "キーアはオレの大事な友達だからな。\x02\x03",

            "#14001F絶対に取り返してきてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        "#6P#00000Fああ、もちろんだ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEF4")

    #C0474
    ChrTalk(
        0xA,
        (
            "#11P#14000Fそういや……\x01",
            "アンタたちに持って行って\x01",
            "もらいたいものがあるんだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        (
            "#6P#00000F俺たちに……\x01",
            "って、いったい何を？\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0xA, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    #A0476
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シュリは帽子を取り、ロイドに手渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0477
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1DE, 1)
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x5DC, 0x0)

    #C0478
    ChrTalk(
        0x101,
        "#6P#00005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xA,
        (
            "#11P#04203Fアンタらがキーアを\x01",
            "追いかけるんなら本当は\x01",
            "付いて行きたいけど……\x02\x03",

            "#04208Fそんなことができないってのは\x01",
            "分かってるからさ。\x02\x03",

            "代わりにオレの愛用の帽子を\x01",
            "持って行ってくれないかなって。\x02\x03",

            "#04201F……ダメか？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#6P#00002Fいや、そんなことはないよ。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#6P#00102Fシュリちゃんの気持ち、\x01",
            "確かに受け取ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x103,
        (
            "#6P#00202Fええ、これはわたしたちが\x01",
            "責任を持って預かります。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE6D")

    #C0483
    ChrTalk(
        0xA,
        (
            "#11P#04212Fそ、そうか……\x01",
            "ならよろしく頼んだからな。\x02\x03",

            "#04202Fそれじゃ、\x01",
            "リーシャ姉に他のみんなも\x01",
            "どうか気をつけてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x106,
        "#6P#10709Fうん、分かった。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_CEF4")

    label("loc_CE6D")


    #C0485
    ChrTalk(
        0xA,
        (
            "#11P#04212Fそ、そうか……\x01",
            "ならよろしく頼んだからな。\x02\x03",

            "#04202Fそれじゃ、\x01",
            "くれぐれも気をつけてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        "#6P#00000Fああ、分かった。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_CEF4")

    SetScenarioFlags(0x1DE, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 1250, 24400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF4F")
    OP_E0(0x34, 0x0)

    label("loc_CF4F")

    EventEnd(0x5)
    Return()

    # Function_35_C4C5 end

    def Function_36_CF52(): pass

    label("Function_36_CF52")

    EventBegin(0x0)
    Fade(500)
    OP_68(65370, 1500, 2140, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15840, 0)
    SetChrPos(0xF, 67000, 0, 3000, 270)
    SetChrPos(0x101, 65670, 0, 3760, 90)
    SetChrPos(0x102, 65700, 0, 2440, 90)
    SetChrPos(0x104, 64000, 0, 3200, 90)
    SetChrPos(0x109, 64590, 0, 1760, 90)
    SetChrPos(0x105, 64610, 0, 4350, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    OP_0D()

    #C0487
    ChrTalk(
        0xF,
        "おや、キミたちは……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        (
            "#6P#00000Fこんにちは、ニコルさん。\x02\x03",

            "ちょっとお尋ねしたいんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは教授の依頼で\x01",
            "問診表を回収している事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0490
    ChrTalk(
        0xF,
        "ああ、あの問診表か。\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xF,
        (
            "最近練習が楽しくて、\x01",
            "持って行くのをすっかり\x01",
            "忘れちゃってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xF,
        (
            "ちょっと待っててくれ。\x01",
            "持ってくるからさ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0493
    ChrTalk(
        0xF,
        "はい、これのことだろう？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0494
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32D, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0495
    ChrTalk(
        0x101,
        "#6P#00000Fはい、たしかに。\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#6P#00102Fふふ、その様子だと\x01",
            "薬の影響もほとんど\x01",
            "残ってないみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xF,
        (
            "ああ、ちゃんと\x01",
            "治療してもらったしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xF,
        (
            "……今思えば、\x01",
            "何であんな薬なんかに\x01",
            "手を出しちゃったんだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xF,
        (
            "確かにあの時は\x01",
            "自分の才能のなさに\x01",
            "腐ってたりしたけどさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x105,
        (
            "#6P#10303Fそういう心の隙間に\x01",
            "狡猾に付け込んでくるのが\x01",
            "クスリってやつさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#6P#00300Fま、それが自覚できたってことは\x01",
            "もう何も心配はなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xF,
        (
            "ああ……これからは\x01",
            "アルカンシェルのために\x01",
            "一層精進していくつもりさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x109,
        "#6P#10100F舞台、楽しみにしてますね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 4)
    OP_29(0x70, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D48C")

    #A0504
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで全ての問診表を\x01",
            "回収し終わったな。\x02\x03",

            "さっそくセイランド教授に\x01",
            "届けにいくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_D48C")

    OP_93(0xF, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 65000, 0, 3000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_CF52 end

    def Function_37_D4BE(): pass

    label("Function_37_D4BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    LoadChrToIndex("chr/ch00100.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 1850, 15200, -8150, 270)
    OP_68(10290, 16450, -8390, 0)
    MoveCamera(48, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16590, 0)
    SetChrPos(0x101, 13010, 15200, -8000, 270)
    SetChrPos(0x1A3, 13010, 15200, -8000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 39)
    WaitChrThread(0x1A3, 3)
    OP_0D()

    #C0505
    ChrTalk(
        0x101,
        "#11P#00000Fさて、マリーはいるかな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0506
    ChrTalk(
        0x101,
        "#11P#00005Fあ！\x02",
    )

    CloseMessageWindow()
    OP_68(2530, 16850, -8580, 3000)
    MoveCamera(48, 12, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15720, 3000)
    OP_6F(0x79)

    #C0507
    ChrTalk(
        0x1A3,
        "#11P#04600Fフフ、さっそく見つかったね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)

    #C0508
    ChrTalk(
        0x101,
        (
            "#5P#00000Fよし、それじゃあ\x01",
            "ここは俺に任せてくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    #C0509
    ChrTalk(
        0x1A3,
        (
            "#11P#04605Fええ～、まあいいけど。\x02\x03",

            "#04602Fあは、お手並み拝見だね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D6CD():
        OP_95(0xFE, 8590, 15200, -7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D6CD)
    Sleep(50)

    def lambda_D6EA():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_D6EA)
    WaitChrThread(0x101, 1)

    #C0510
    ChrTalk(
        0x101,
        (
            "#00002Fさあ、マリー。\x01",
            "安心してこっちに来るんだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 500)
    OP_63(0x13, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x13)
    OP_63(0x13, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    OP_68(5850, 16850, -7440, 3000)
    OP_9B(0x0, 0x13, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-8010, 16850, -9130, 0)
    MoveCamera(326, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15880, 0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    Sound(103, 0, 100, 0)
    SetChrPos(0x14, -13030, 15200, -8029, 90)
    SetChrPos(0x15, -13030, 15200, -8029, 90)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x14, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 41)
    WaitChrThread(0x15, 3)
    Sleep(1000)

    #C0511
    ChrTalk(
        0x101,
        "#00005Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5850, 16850, -7440, 0)
    MoveCamera(48, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    OP_63(0x13, 0x0, 1200, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(10750, 16850, -7200, 1500)
    Sound(953, 0, 100, 0)

    def lambda_D8B4():
        OP_95(0xFE, 13800, 15200, -8010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D8B4)
    Sleep(1000)

    def lambda_D8D1():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8D1)
    Sleep(50)

    def lambda_D8E1():

        label("loc_D8E1")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_D8E1")

    QueueWorkItem2(0x1A3, 1, lambda_D8E1)
    Sleep(1000)

    def lambda_D8F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D8F6)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x1)
    EndChrThread(0x1A3, 0x1)

    #C0512
    ChrTalk(
        0x1A3,
        "#04605Fわお……！？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#00006Fゆ、油断した……\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x1A3,
        (
            "#04609Fあはは、シャーリィもだよ。\x02\x03",

            "#04606Fんー、まだまだ\x01",
            "修行不足ってことかな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 1770, 15200, -7960, 90)
    SetChrPos(0x15, 1770, 15200, -9370, 90)
    OP_68(6830, 16850, -8570, 4000)
    MoveCamera(46, 28, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(16250, 4000)

    def lambda_D9F1():
        OP_95(0xFE, 6590, 15200, -7960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D9F1)
    Sleep(50)

    def lambda_DA0E():
        OP_95(0xFE, 6590, 15200, -9370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DA0E)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    #C0515
    ChrTalk(
        0x15,
        (
            "#6P#10300Fやあ、どうやら\x01",
            "邪魔をしたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x14,
        (
            "#6P#00106Fごめんなさい、\x01",
            "いい所だったみたいなのに……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DA9C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA9C)
    Sleep(50)

    def lambda_DAAC():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DAAC)
    Sleep(300)

    #C0517
    ChrTalk(
        0x101,
        (
            "#00004Fいや、俺の詰めが甘かっただけさ。\x02\x03",

            "#00000Fとにかく、すぐに後を追うよ。\x02\x03",

            "念のためエリィたちは反対側から\x01",
            "エントランスに向かってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x14,
        "#6P#00100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x1A3,
        (
            "#04609Fふふっ、それじゃあ\x01",
            "とっとと追いかけようか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x155, 6)
    OP_29(0x74, 0x1, 0x7)
    ModifyEventFlags(1, 2, 0x80)
    OP_1B(0x2, 0x0, 0x2A)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9130, 15200, -8100, 0)
    EventEnd(0x5)
    Return()

    # Function_37_D4BE end

    def Function_38_DBE7(): pass

    label("Function_38_DBE7")


    def lambda_DBEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DBEC)

    def lambda_DBFD():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBFD)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 10260, 15200, -7100, 2000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_38_DBE7 end

    def Function_39_DC32(): pass

    label("Function_39_DC32")


    def lambda_DC37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_DC37)

    def lambda_DC48():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DC48)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 10260, 15200, -9100, 2000, 0x0)
    OP_93(0x1A3, 0x10E, 0x1F4)
    Return()

    # Function_39_DC32 end

    def Function_40_DC7D(): pass

    label("Function_40_DC7D")


    def lambda_DC82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_DC82)

    def lambda_DC93():
        OP_95(0xFE, -8770, 15200, -8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DC93)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x5A, 0x1F4)
    Return()

    # Function_40_DC7D end

    def Function_41_DCB4(): pass

    label("Function_41_DCB4")


    def lambda_DCB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_DCB9)

    def lambda_DCCA():
        OP_95(0xFE, -11190, 15200, -8100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DCCA)
    WaitChrThread(0x15, 1)
    OP_95(0x15, -10100, 15200, -9070, 2000, 0x0)
    OP_93(0x15, 0x5A, 0x1F4)
    Return()

    # Function_41_DCB4 end

    def Function_42_DCFF(): pass

    label("Function_42_DCFF")

    EventBegin(0x1)

    #C0520
    ChrTalk(
        0x101,
        (
            "#00000F急いでマリーを追いかけよう。\x01",
            "今ならまだ近くにいるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x1A3,
        (
            "#04609Fふふ、今度は逃がさないように\x01",
            "しないとねー。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -11130, 15200, -7980, 90)
    EventEnd(0x4)
    Return()

    # Function_42_DCFF end

    def Function_43_DD93(): pass

    label("Function_43_DD93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    LoadChrToIndex("apl/ch50267.itc", 0x1F)
    LoadChrToIndex("apl/ch51226.itc", 0x20)
    LoadChrToIndex("apl/ch51228.itc", 0x21)
    LoadChrToIndex("apl/ch51229.itc", 0x22)
    LoadChrToIndex("chr/ch03401.itc", 0x23)
    SoundLoad(148)
    SetMapObjFrame(0xFF, "chandelier01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "chandelier02", 0x0, 0x1)
    OP_4C(0x9, 0x1)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x13, -1900, 0, -1900, 0)
    OP_78(0x19, 0x16)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_74(0x19, 0x1E)
    ClearChrFlags(0x16, 0x80)
    OP_49()
    SetChrPos(0x16, 0, 1250, 25580, 0)
    OP_D5(0x16, 0x0, 0x0, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0xE)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x4)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 0, 0, 900, 180)
    OP_68(-2680, 4650, 17690, 0)
    MoveCamera(50, 37, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(9930, 0)
    SetChrPos(0x13, 350, 1250, 18040, 0)
    SetChrPos(0x9, -140, 2700, -5190, 0)
    SetChrPos(0x1A3, -140, 2700, -5190, 0)
    SetChrPos(0x101, -140, 2700, -5190, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetCameraDistance(12670, 3000)

    def lambda_DF59():
        OP_95(0xFE, 110, 1250, 20620, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DF59)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x13, 1)
    OP_6F(0x10)
    Fade(500)
    OP_68(-2450, 4650, -2450, 0)
    MoveCamera(49, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_68(-2880, 4650, 4170, 5000)
    MoveCamera(55, 31, 0, 5000)
    BeginChrThread(0x9, 3, 0, 46)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 44)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Sleep(700)
    Fade(500)
    OP_68(-1760, 4650, 21430, 0)
    MoveCamera(50, 37, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Sound(844, 0, 50, 0)
    OP_9D(0x13, 0x15E, 0xDAC, 0x5AA0, 0xDAC, 0x1388)
    OP_D3(0x13, 0x19, "nullch")
    ClearChrFlags(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sound(143, 0, 70, 0)
    Sound(148, 2, 100, 0)

    def lambda_E06F():
        OP_98(0xFE, 0x0, 0x2710, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E06F)
    Sleep(3000)
    Fade(500)
    OP_68(-3750, 4650, 3390, 0)
    MoveCamera(33, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0522
    ChrTalk(
        0x101,
        "#00011F#10Aな……！\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #C0523
    ChrTalk(
        0x9,
        (
            "#06205F#23Aいけない、舞台装置が！\x02\x03",

            "#20Aでも、一体誰が……！？\x02",
        )
    )
    #Auto

    Sleep(1900)
    OP_57(0x0)
    OP_5A()
    OP_68(-1560, 4350, 2450, 2000)
    MoveCamera(30, 20, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(11000, 2000)
    OP_6F(0x79)

    #C0524
    ChrTalk(
        0x1A3,
        "#11P#04611F#19Aフフン、このくらい！\x02",
    )
    #Auto

    Sleep(1000)
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x1A3, 0x23)
    SetChrSubChip(0x1A3, 0x5)
    SetChrFlags(0x1A3, 0x1000)
    OP_6B(0x1A3)
    SetChrChip(0x0, 0x1A3, 0x1E, 0x12C)
    Sound(250, 0, 60, 0)
    OP_95(0x1A3, -910, 1350, 7510, 10000, 0x0)
    OP_95(0x1A3, 100, 0, 15520, 10000, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0x1A3, 0x1CC, 0x4E2, 0x49A2, 0x9C4, 0x2710)
    OP_95(0x1A3, 4610, 1250, 21370, 10000, 0x0)
    Sound(251, 0, 50, 0)
    OP_9D(0x1A3, 0x1E28, 0x9C4, 0x5910, 0x9C4, 0x2710)
    OP_93(0x1A3, 0x10E, 0x0)
    OP_9D(0x1A3, 0x0, 0xED8, 0x5A32, 0xFA0, 0x1388)
    Sound(326, 0, 50, 0)
    OP_93(0x1A3, 0x10E, 0x0)
    SetChrChip(0x1, 0x1A3, 0x0, 0x0)
    OP_D3(0x1A3, 0x19, "nullch2")
    ClearChrFlags(0x1A3, 0x1)
    OP_52(0x1A3, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6B(0xFF)
    OP_6B(0x13)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    Sound(879, 0, 70, 0)
    OP_74(0x19, 0x14)
    OP_71(0x19, 0x2B, 0x42, 0x0, 0x0)
    Sleep(1100)
    Sound(879, 0, 60, 0)
    OP_74(0x19, 0xA)
    OP_71(0x19, 0x2B, 0x3A, 0x0, 0x0)
    Sleep(1500)
    Sound(879, 0, 50, 0)
    OP_74(0x19, 0x7)
    OP_71(0x19, 0x3A, 0x32, 0x0, 0x0)
    OP_79(0x19)
    OP_74(0x19, 0x5)
    OP_71(0x19, 0x32, 0x39, 0x0, 0x0)
    OP_79(0x19)
    Sound(879, 0, 40, 0)
    OP_74(0x19, 0x2)
    OP_71(0x19, 0x39, 0x36, 0x0, 0x0)
    OP_79(0x19)
    TurnDirection(0x13, 0x1A3, 500)
    OP_6B(0xFF)
    OP_68(-400, 8390, 22760, 2000)
    MoveCamera(33, 16, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(11550, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x16, 0x1)
    Fade(500)
    OP_68(-360, 1320, 15690, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, 900, 0, 15820, 0)
    SetChrPos(0x9, -900, 0, 15820, 0)
    OP_D3(0x1A3, 0x19, "nullch")
    ClearChrFlags(0x1A3, 0x1)
    OP_52(0x1A3, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x19, 0xB, 0xB, 0x0, 0x0)
    OP_0D()

    #C0525
    ChrTalk(
        0x101,
        "#12P#00005Fえ……！\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x9,
        "#12P#06205Fす、凄い……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-790, 8810, 23640, 0)
    MoveCamera(3, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    SetChrFlags(0x13, 0x8)
    SetChrChipByIndex(0x1A3, 0x20)
    SetChrSubChip(0x1A3, 0x7)
    SetChrFlags(0x1A3, 0x2)
    SetChrPos(0x1A3, 250, 1250, 22960, 270)
    OP_0D()
    OP_6B(0x1A3)

    def lambda_E474():
        OP_98(0xFE, 0x0, 0x1770, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E474)

    #C0527
    ChrTalk(
        0x13,
        "#6Pにゃ、にゃ～ん……！\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x1A3,
        (
            "#11P#04606Fんー、何も取って食おうって\x01",
            "わけじゃないんだからさぁ。\x02\x03",

            "いいかげん安心しなよねー。\x02\x03",

            "#04602Fほーら、こいつはどうだ♪\x02",
        )
    )

    CloseMessageWindow()

    #A0529
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シャーリィはマリーの\x01",
            "喉をくすぐってやった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x1A3, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A3)
    OP_63(0x1A3, 0x0, 1200, 0x8, 0x9, 0xFA, 0x1)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Sound(953, 0, 100, 0)

    #C0530
    ChrTalk(
        0x13,
        "#6Pにゃ、にゃ～ん。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x1A3,
        (
            "#11P#04609Fふふ、悪くないって？\x02\x03",

            "#04600Fじゃあ……お次はこうだ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0532
    ChrTalk(
        0x13,
        "#6Pにゃうん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A3)
    OP_63(0x1A3, 0x0, 1200, 0xA, 0xB, 0xFA, 0x1)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0533
    ChrTalk(
        0x13,
        "#6Pごろごろごろ……うにゃん㈱\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x1A3,
        "#11P#04609Fあはは、ちょっとは落ち着いた？\x02",
    )

    CloseMessageWindow()
    OP_6B(0xFF)
    StopSound(148, 1000, 100)
    Fade(500)
    OP_68(-390, 1320, 17820, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13620, 0)
    SetChrPos(0x101, 900, 0, 15820, 0)
    SetChrPos(0x9, -900, 0, 15820, 0)
    OP_0D()

    #C0535
    ChrTalk(
        0x101,
        "#12P#00000Fはは、鮮やかな手並みだな。\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x9,
        (
            "#12P#06204Fええ、それに信じられないくらい\x01",
            "軽やかな身のこなしでした。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(300)

    #C0537
    ChrTalk(
        0x9,
        (
            "#12P#06205Fそうだ、誰が装置を\x01",
            "動かしたのか確認しないと……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x16, 0x1)
    Fade(500)
    OP_68(290, 11070, 33130, 0)
    MoveCamera(7, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x16, 0, 11250, 25580, 0)
    OP_D5(0x16, 0x0, 0x0, 0x0, 0x0)
    OP_0D()

    #C0538
    ChrTalk(
        0x1A3,
        (
            "#11P#04600Fそれじゃ、\x01",
            "これから一緒に下りるから。\x02\x03",

            "もう暴れちゃダメだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x13,
        "#6Pにゃ～ん♪\x02",
    )

    CloseMessageWindow()
    OP_68(290, 9970, 33130, 100)
    Sound(143, 0, 100, 0)
    OP_98(0x16, 0x0, 0xFFFFFA24, 0x0, 0x1F40, 0x0)
    OP_63(0x1A3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0540
    ChrTalk(
        0x1A3,
        "#11P#04605Fなにさ、いきなり……あ。\x02",
    )

    CloseMessageWindow()
    OP_68(3620, 6670, 29700, 500)
    MoveCamera(25, 17, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(28350, 500)
    Sound(879, 0, 100, 0)
    OP_74(0x19, 0x1E)
    OP_71(0x19, 0xB, 0x28, 0x0, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_98(0x16, 0x0, 0xFFFFF448, 0x0, 0x2710, 0x0)
    SetChrPos(0x13, 520, 8840, 23300, 90)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x1A3, 0x5)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x8)
    SetChrFlags(0x1A3, 0x2)
    SetChrFlags(0x13, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_E9A5():
        OP_9D(0xFE, 0x212, 0x2328, 0x4268, 0x7D0, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E9A5)
    OP_D3(0x13, 0xFF, "nullch")
    OP_93(0x1A3, 0xB4, 0x0)
    CancelBlur(500)
    Sleep(500)
    EndChrThread(0x13, 0x1)
    Fade(500)
    OP_68(-710, 1320, 19230, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 900, 0, 15820, 0)
    SetChrPos(0x9, -900, 0, 15820, 0)
    SetChrPos(0x13, 530, 10000, 22500, 90)
    OP_71(0x19, 0x28, 0x28, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0541
    ChrTalk(
        0x101,
        "#00011Fまずい……！\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x9,
        "#06201F……っ………！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 47)
    Sleep(500)
    OP_68(3370, 4570, 23550, 800)
    MoveCamera(48, 23, 0, 800)
    OP_6E(500, 800)
    SetCameraDistance(20670, 800)
    Sound(834, 0, 50, 0)

    def lambda_EAFA():
        OP_9D(0xFE, 0x6D6, 0x1F40, 0x4A38, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_EAFA)
    Sleep(700)
    EndChrThread(0x13, 0x1)
    SetChrFlags(0x13, 0x8)
    OP_6F(0x79)
    WaitChrThread(0x9, 3)
    ClearScenarioFlags(0x1, 4)
    EndChrThread(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x7)
    OP_0D()
    OP_68(4110, 4870, 24080, 1000)
    MoveCamera(48, 23, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(29060, 1000)
    SetCameraDistance(29060, 1000)
    TurnDirection(0x1A3, 0x101, 0)
    OP_0D()
    OP_6F(0x79)

    #C0543
    ChrTalk(
        0x1A3,
        "#04605Fわお、ナイスキャッチ！\x02",
    )

    CloseMessageWindow()
    OP_68(-2520, 5470, 16640, 5000)
    MoveCamera(48, 23, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(9920, 5000)
    SetChrPos(0x101, -4480, 1250, 20070, 90)
    OP_95(0x101, 1230, 1250, 20900, 2000, 0x0)
    TurnDirection(0x101, 0x9, 500)
    OP_6F(0x79)

    #C0544
    ChrTalk(
        0x101,
        (
            "#00000Fふう……どうやら\x01",
            "何とかなったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_DD93 end

    def Function_44_EC51(): pass

    label("Function_44_EC51")


    def lambda_EC56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EC56)

    def lambda_EC67():
        OP_95(0xFE, 0, 2250, 2940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC67)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_EC51 end

    def Function_45_EC81(): pass

    label("Function_45_EC81")


    def lambda_EC86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_EC86)

    def lambda_EC97():
        OP_95(0xFE, 0, 1800, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_EC97)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_45_EC81 end

    def Function_46_ECB1(): pass

    label("Function_46_ECB1")


    def lambda_ECB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_ECB6)

    def lambda_ECC7():
        OP_95(0xFE, 0, 1350, 7460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ECC7)
    WaitChrThread(0x9, 1)
    Return()

    # Function_46_ECB1 end

    def Function_47_ECE1(): pass

    label("Function_47_ECE1")

    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    Sound(250, 0, 60, 0)
    OP_9D(0x9, 0x0, 0x4E2, 0x4BFA, 0xBB8, 0x1388)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x1, 4)
    Sound(637, 0, 100, 0)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x9, 0, 0, 48)

    def lambda_ED24():
        OP_9D(0xFE, 0x1086, 0x4E2, 0x517C, 0x1388, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED24)
    OP_A1(0x9, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0x9, 1)
    Sound(326, 0, 50, 0)
    Return()

    # Function_47_ECE1 end

    def Function_48_ED50(): pass

    label("Function_48_ED50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_ED6C")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_48_ED50")

    label("loc_ED6C")

    Return()

    # Function_48_ED50 end

    def Function_49_ED6D(): pass

    label("Function_49_ED6D")

    SetChrPos(0xA, 0, 1250, 25500, 270)

    label("loc_ED7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F152")
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_EDAF():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EDAF)
    Sound(809, 0, 30, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    Sound(50, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)

    def lambda_EDEA():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EDEA)
    OP_49()
    Sound(809, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 51)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    Sound(50, 0, 70, 0)
    Sound(809, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 51)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    Sound(50, 0, 70, 0)
    EndChrThread(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)

    def lambda_EE70():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EE70)
    Sleep(250)

    def lambda_EE8E():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EE8E)
    Sleep(250)

    def lambda_EEAC():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EEAC)
    Sleep(250)

    def lambda_EECA():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EECA)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 54)
    Sleep(1000)

    def lambda_EEFC():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EEFC)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)

    def lambda_EF62():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EF62)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(50, 0, 50, 0)

    def lambda_EFA1():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EFA1)
    BeginChrThread(0xA, 1, 0, 51)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_EFDD():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EFDD)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0xAF)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0x10E, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0xBB8, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x7D0, 0x4E2, 0x61A8, 0x1194, 0x0)
    BeginChrThread(0xA, 1, 0, 50)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0x3E8, 0x4E2, 0x61A8, 0x3E8, 0xBB8)
    Sound(50, 0, 30, 0)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 55)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x61A8, 0x5DC, 0xBB8)
    Sound(50, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 54)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0xFFFFF92A, 0x4E2, 0x61A8, 0x7D0, 0xBB8)
    Sound(50, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_F0F3():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F0F3)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0xFFFFF060, 0x4E2, 0x61A8, 0xBB8, 0x578)
    Sound(50, 0, 30, 0)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0x0, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Jump("loc_ED7E")

    label("loc_F152")

    Return()

    # Function_49_ED6D end

    def Function_50_F153(): pass

    label("Function_50_F153")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_50_F153 end

    def Function_51_F177(): pass

    label("Function_51_F177")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_51_F177 end

    def Function_52_F19B(): pass

    label("Function_52_F19B")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_F19B end

    def Function_53_F1B0(): pass

    label("Function_53_F1B0")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_F1B0 end

    def Function_54_F1BE(): pass

    label("Function_54_F1BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F1DC")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_54_F1BE")

    label("loc_F1DC")

    Return()

    # Function_54_F1BE end

    def Function_55_F1DD(): pass

    label("Function_55_F1DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F1FB")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_55_F1DD")

    label("loc_F1FB")

    Return()

    # Function_55_F1DD end

    def Function_56_F1FC(): pass

    label("Function_56_F1FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 2500, 25500, 0)
    MoveCamera(32, 5, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(24000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 1250, 25500, 180)
    SetChrPos(0x101, 0, 2700, 500, 0)
    SetChrPos(0x102, 1200, 2700, 500, 0)
    SetChrPos(0x103, -1200, 2700, 500, 0)
    SetChrPos(0x104, 0, 2700, -700, 0)
    SetChrPos(0x105, 1200, 2700, -700, 0)
    SetChrPos(0x109, -1200, 2700, -700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)
    FadeToBright(1000, 0)
    OP_68(0, 4000, 25500, 10000)
    MoveCamera(14, 10, 0, 710000)
    Sleep(7000)
    Fade(500)
    OP_68(-1400, 4130, 3070, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00000Fずいぶん熱心に\x01",
            "頑張っているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        "#00100Fええ、支配人の言った通りね。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x103,
        (
            "#00200F何というか、\x01",
            "こうして見ると圧巻ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x104,
        (
            "#00300F新たに追加されるシーンの\x01",
            "練習ってわけか。\x02\x03",

            "#00304Fかなり重要な\x01",
            "役どころだって話だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x109,
        (
            "#10100Fええ、『星の姫』役ですね。\x02\x03",

            "何でも舞台の後半辺りで\x01",
            "大きな見せ場があるらしいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x105,
        "#10300Fフフ、それは気合いも入るよね。\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#00003Fああ、それだけにプレッシャーも\x01",
            "相当なものだろうし……\x02\x03",

            "#00000Fこれは、邪魔しない内に\x01",
            "退散した方が良いかもな。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x0, 0x0)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1500, 1250, 25450, 90)
    OP_68(-1500, 2500, 25500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0xA, 0xB4, 0x258)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0552
    ChrTalk(
        0xA,
        "#12205Fあ……アンタたち！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1400, 4130, 3070, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x101,
        "#00005Fおっと……\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x103,
        "#00200F気付かれてしまいましたね。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x104,
        (
            "#00300Fま、せっかくだ。\x01",
            "挨拶だけでもしておこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F6D6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6D6)
    Sleep(50)

    def lambda_F6F3():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6F3)
    Sleep(50)

    def lambda_F710():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F710)
    Sleep(50)

    def lambda_F72D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F72D)
    Sleep(50)

    def lambda_F74A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F74A)
    Sleep(50)

    def lambda_F767():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F767)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-50, 1320, 14180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, 0, 0, 14050, 0)
    SetChrPos(0x102, 1000, 0, 14150, 0)
    SetChrPos(0x103, -1000, 0, 14150, 0)
    SetChrPos(0x104, 0, 450, 12100, 0)
    SetChrPos(0x105, 1000, 450, 12000, 0)
    SetChrPos(0x109, -1000, 450, 12100, 0)
    SetChrPos(0xA, -1500, 1250, 22000, 180)
    FadeToBright(1000, 0)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x0, 0x4E2, 0x4696, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)
    Sound(809, 0, 50, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 50)
    OP_9D(0xA, 0xFFFFFFCE, 0x0, 0x3E6C, 0x3E8, 0x7D0)
    Sound(42, 0, 100, 0)
    Sound(326, 0, 20, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    #C0556
    ChrTalk(
        0x101,
        (
            "#00000Fやあ、シュリ。\x01",
            "練習中の所、邪魔したな。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xA,
        (
            "#12203Fフ、フン、別に……\x02\x03",

            "#12200Fで、何か用事でもあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#00100Fいえ、ちょっと通りがかったから\x01",
            "様子を見させてもらっただけなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        "#00000Fああ、なのに中断させて悪かったな。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xA,
        (
            "#12206Fま、丁度休憩を\x01",
            "挟もうと思ってた所だし。\x01",
            "別にいいけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x103,
        (
            "#00203Fしかしシュリさんの演技は\x01",
            "初めて見ましたけど……\x02\x03",

            "#00202Fすごく堂に入っていて\x01",
            "とても新人とは思えませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0562
    ChrTalk(
        0xA,
        "#12205Fそ、そうかな……？\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x102,
        (
            "#00102Fええ、本当に。\x01",
            "正直驚かされたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00004Fああ、それに何だろう。\x01",
            "動きに無駄がないっていうのかな。\x02\x03",

            "#00002Fもうほとんど\x01",
            "完璧に近いんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xA,
        "#12205Fえ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    #C0566
    ChrTalk(
        0x109,
        (
            "#10109Fうんうん、それにその衣装も\x01",
            "よく似合っているよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0567
    ChrTalk(
        0x109,
        "#10105F……シュリちゃん？\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    def lambda_FBE8():

        label("loc_FBE8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FBE8")

    QueueWorkItem2(0x102, 0, lambda_FBE8)

    def lambda_FBFA():

        label("loc_FBFA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FBFA")

    QueueWorkItem2(0x103, 0, lambda_FBFA)
    OP_99(0xA, 0x101, 0x3E8, 0x7D0, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)

    #C0568
    ChrTalk(
        0xA,
        (
            "#12203F……おい、アンタ。\x02\x03",

            "#12200Fよければ、少し演技の練習に\x01",
            "付き合ってくれないか？\x02\x03",

            "#12208Fそれとその……\x01",
            "ちょっと聞きたいことがあるんだ。\x02",
        )
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0569
    ChrTalk(
        0x102,
        (
            "#00105Fロイドが、シュリちゃんの\x01",
            "演技の練習に？\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        (
            "#00005Fど、どうして俺が？\x01",
            "それに聞きたいことって……\x02\x03",

            "#00003Fはっきり言っておくけど、\x01",
            "舞台のことなんて\x01",
            "何も分からないド素人だぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xA,
        (
            "#12203Fべ、別に難しいことを\x01",
            "させようってんじゃないんだ。\x02\x03",

            "#12208Fそれに、\x01",
            "ちょっと思う所があってさ。\x02\x03",

            "#12200F……で、どうなんだ。\x01",
            "付き合ってくれんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x101,
        "#00003Fそ、そうだな……\x02",
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_56_F1FC end

    def Function_57_FECA(): pass

    label("Function_57_FECA")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "シュリの練習に付き合う\x01",      # 0
            "やめておく\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_FF3C"),
        (1, "loc_1001F"),
        (SWITCH_DEFAULT, "loc_101BE"),
    )


    label("loc_FF3C")


    #C0573
    ChrTalk(
        0x101,
        (
            "#00000Fああ、俺でよければ構わないけど。\x02\x03",

            "ほんと大したことはできないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xA,
        "#12200Fああ……分かった。\x02",
    )

    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0575
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【秘密の演技指導】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x8D, 0x4, 0x2)
    SetScenarioFlags(0x22, 1)
    NewScene("e3600", 0, 0, 0)
    IdleLoop()
    Jump("loc_101BE")

    label("loc_1001F")


    #C0576
    ChrTalk(
        0x101,
        (
            "#00006F……ごめん。\x01",
            "今は他にも用事があって\x01",
            "時間を取れそうにないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xA,
        (
            "#12206Fそうか、ならいい。\x01",
            "……今言ったことは忘れてくれ。\x02\x03",

            "#12208Fじゃ、オレは練習の続きがあるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x101,
        "#00000Fあ、ああ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0579
    ChrTalk(
        0x102,
        (
            "#00100F（ねえ、ロイド。\x01",
            "  何とか時間を取れないかしら？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0580
    ChrTalk(
        0x101,
        (
            "#00003F（そ、そうだな……\x01",
            "  改めて考えてみるか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 4)
    SetChrPos(0xA, -50, 0, 15980, 180)
    OP_4C(0xA, 0xFF)
    BeginChrThread(0xA, 3, 0, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 14050, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_101BE")

    label("loc_101BE")

    Return()

    # Function_57_FECA end

    def Function_58_101BF(): pass

    label("Function_58_101BF")

    EventBegin(0x0)
    Fade(500)
    OP_68(-620, 1320, 14390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    SetChrPos(0x101, 0, 0, 14050, 0)
    SetChrPos(0x102, 1000, 0, 14150, 0)
    SetChrPos(0x103, -1000, 0, 14150, 0)
    SetChrPos(0x104, 0, 450, 12100, 0)
    SetChrPos(0x105, 1000, 450, 12000, 0)
    SetChrPos(0x109, -1000, 450, 12100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0581
    ChrTalk(
        0xA,
        (
            "#12205Fなんだ、用事が\x01",
            "あるんじゃなかったのか？\x02\x03",

            "#12200Fもしかして……\x01",
            "練習に付き合ってくれんのか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_58_101BF end

    SaveToFile()

Try(main)
