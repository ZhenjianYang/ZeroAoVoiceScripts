from ScenarioHelper import *

def main():
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
        "伊莉娅",                 # 1
        "莉夏",                   # 2
        "修利",                   # 3
        "亚邦剧团长",             # 4
        "海因兹",                 # 5
        "尤金",                   # 6
        "缇奥多尔",               # 7
        "尼克鲁",                 # 8
        "普莉埃",                 # 9
        "塞利娜",                 # 10
        "卡雷利亚",               # 11
        "玛丽",                   # 12
        "艾莉",                   # 13
        "瓦吉",                   # 14
        "吊灯",                   # 15
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
        "Function_7_134F",         # 07, 7
        "Function_8_1685",         # 08, 8
        "Function_9_23ED",         # 09, 9
        "Function_10_294C",        # 0A, 10
        "Function_11_29C1",        # 0B, 11
        "Function_12_2E47",        # 0C, 12
        "Function_13_3706",        # 0D, 13
        "Function_14_37DE",        # 0E, 14
        "Function_15_3958",        # 0F, 15
        "Function_16_3B0C",        # 10, 16
        "Function_17_403A",        # 11, 17
        "Function_18_4AEE",        # 12, 18
        "Function_19_4E6C",        # 13, 19
        "Function_20_4F0E",        # 14, 20
        "Function_21_5170",        # 15, 21
        "Function_22_549B",        # 16, 22
        "Function_23_54F8",        # 17, 23
        "Function_24_56B9",        # 18, 24
        "Function_25_582A",        # 19, 25
        "Function_26_5831",        # 1A, 26
        "Function_27_5857",        # 1B, 27
        "Function_28_74C4",        # 1C, 28
        "Function_29_7955",        # 1D, 29
        "Function_30_79CE",        # 1E, 30
        "Function_31_85B6",        # 1F, 31
        "Function_32_8AAB",        # 20, 32
        "Function_33_93EC",        # 21, 33
        "Function_34_9808",        # 22, 34
        "Function_35_AAF8",        # 23, 35
        "Function_36_B3D5",        # 24, 36
        "Function_37_B873",        # 25, 37
        "Function_38_BEFA",        # 26, 38
        "Function_39_BF45",        # 27, 39
        "Function_40_BF90",        # 28, 40
        "Function_41_BFC7",        # 29, 41
        "Function_42_C012",        # 2A, 42
        "Function_43_C086",        # 2B, 43
        "Function_44_CE7C",        # 2C, 44
        "Function_45_CEAC",        # 2D, 45
        "Function_46_CEDC",        # 2E, 46
        "Function_47_CF0C",        # 2F, 47
        "Function_48_CF7B",        # 30, 48
        "Function_49_CF98",        # 31, 49
        "Function_50_D37E",        # 32, 50
        "Function_51_D3A2",        # 33, 51
        "Function_52_D3C6",        # 34, 52
        "Function_53_D3DB",        # 35, 53
        "Function_54_D3E9",        # 36, 54
        "Function_55_D408",        # 37, 55
        "Function_56_D427",        # 38, 56
        "Function_57_DF77",        # 39, 57
        "Function_58_E228",        # 3A, 58
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE0")

    #C0001
    ChrTalk(
        0xFE,
        "如何，气势十足吧？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "为了重新开始公演，\x01",
            "大家现在都在\x01",
            "全力拼搏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "听说伊莉娅\x01",
            "已经醒过来了……\x01",
            "这也是为了回应她的期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00000F（……剧团的各位\x01",
            "  还不知道莉夏\x01",
            "  现在的下落呢。）\x02\x03",

            "（我想应该让他们\x01",
            "  见上一面吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F91")

    label("loc_EE0")


    #C0005
    ChrTalk(
        0xFE,
        (
            "我们就像平时一样，\x01",
            "在这里磨练演技，\x01",
            "等待着伊莉娅和莉夏的回归。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "罗伊德，\x01",
            "莉夏就拜托\x01",
            "你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#00000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F91")

    #C0008
    ChrTalk(
        0x106,
        (
            "#10700F剧团长……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F91")

    Jump("loc_134B")

    label("loc_F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FEE")

    #C0009
    ChrTalk(
        0xFE,
        (
            "大家真是\x01",
            "很努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "伊莉娅，还有莉夏……\x01",
            "我们会等着你们回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134B")

    label("loc_FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1159")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    #C0011
    ChrTalk(
        0xB,
        "啊，是罗伊德和各位啊……\x02",
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
        "#00003F剧团长……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        "嗯……抱歉。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "考虑到如今的种种情况，\x01",
            "我实在是非常不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "尤其是伊莉娅的状况。\x01",
            "我虽然相信她一定会\x01",
            "醒来，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        "#00108F剧团长……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "呼，但是我也不能\x01",
            "一直这样愁眉不展。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "我也……必须要\x01",
            "振作些才行。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x18D, 0)
    Jump("loc_11A7")

    label("loc_1159")


    #C0020
    ChrTalk(
        0xFE,
        (
            "呼，我也必须要\x01",
            "振作些才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "如果总是这副德性，\x01",
            "伊莉娅一定会发怒呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A7")

    Jump("loc_134B")

    label("loc_11AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1214")

    #C0022
    ChrTalk(
        0xFE,
        "抱歉啊，各位。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "距离表演开始已经没有多少时间了。\x01",
            "大家希望能专心\x01",
            "准备到最后一刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134B")

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1222")
    Jump("loc_134B")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1230")
    Jump("loc_134B")

    label("loc_1230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_123E")
    Jump("loc_134B")

    label("loc_123E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_124C")
    Jump("loc_134B")

    label("loc_124C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_125A")
    Jump("loc_134B")

    label("loc_125A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1268")
    Jump("loc_134B")

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1283")
    Call(0, 8)
    Jump("loc_12CD")

    label("loc_1283")


    #C0024
    ChrTalk(
        0xFE,
        (
            "伊莉娅真是\x01",
            "太可靠了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "看这样子，\x01",
            "明天的表演一定也会大获成功的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CD")

    Jump("loc_134B")

    label("loc_12D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_12E0")
    Jump("loc_134B")

    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_134B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FB")
    Call(0, 7)
    Jump("loc_134B")

    label("loc_12FB")


    #C0026
    ChrTalk(
        0xFE,
        (
            "虽然有点强人所难，\x01",
            "但一切都拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "这也是为了实现\x01",
            "伊莉娅的构想啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134B")

    TalkEnd(0xFE)
    Return()

    # Function_6_DDB end

    def Function_7_134F(): pass

    label("Function_7_134F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157F")

    #C0028
    ChrTalk(
        0xB,
        (
            "对了，海因兹，\x01",
            "技术方面可以实现吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        (
            "这个嘛，\x01",
            "我自然会努力尝试……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1426")

    #C0030
    ChrTalk(
        0xB,
        "哦，是特别任务支援科的各位啊。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        (
            "莫非发生什么\x01",
            "事件了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A0")

    label("loc_1426")


    #C0032
    ChrTalk(
        0xB,
        "哦，你们是……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 0)

    #C0033
    ChrTalk(
        0xB,
        (
            "哦哦，这不是特别任务支援科\x01",
            "的罗伊德吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "莫非发生什么\x01",
            "事件了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A0")


    #C0035
    ChrTalk(
        0x101,
        (
            "#00000F不，我们只是在市内各处\x01",
            "巡视一圈而已。\x02\x03",

            "谨慎起见，顺便也来\x01",
            "剧团看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        (
            "唔，是这样啊。\x01",
            "有你们来巡逻，\x01",
            "真是让人放心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        (
            "如果有什么事情，\x01",
            "随时可以过来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00100F好的，谢谢了。\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x5A, 0x0)
    SetScenarioFlags(0x136, 4)
    Jump("loc_167C")

    label("loc_157F")


    #C0039
    ChrTalk(
        0xC,
        "不过，这样可以吗？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "如果提升速度，\x01",
            "配合时机的难度\x01",
            "也会变得更高……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "哦，伊莉娅已经\x01",
            "考虑过这一点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "但为了实现这次的构想，\x01",
            "提升所有场面的\x01",
            "速度是非常必要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "所以要尽到一切努力，\x01",
            "挑战最大极限。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "是吗……\x01",
            "那我就试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x1, 3)

    label("loc_167C")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_134F end

    def Function_8_1685(): pass

    label("Function_8_1685")

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
        "呀……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#06105F啊，这不是警察弟弟吗。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#12P#00000F打扰各位了。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "#06202F大家好。\x02\x03",

            "#06209F呵呵，兰迪先生\x01",
            "总算归队了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#12P#00300F哟，莉夏小姐，\x01",
            "你还记挂着我，好开心啊。\x02\x03",

            "#00309F哦哦～话说回来，伊莉娅小姐\x01",
            "和莉夏小姐的这种装扮……\x02\x03",

            "真是看多少次都看不够呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "#06102F呵呵，谢谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#06204F被这样评价，\x01",
            "总觉得有点不好意思……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)

    #C0052
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，因为兰迪的视线\x01",
            "的确有些色咪咪呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 500)
    Sleep(300)

    #C0053
    ChrTalk(
        0x104,
        (
            "#11P#00301F瓦吉，你说什么！？\x01",
            "我这只是非常纯粹的欣赏之情……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0054
    ChrTalk(
        0x102,
        (
            "#11P#00106F好了好了，我们都明白了，\x01",
            "就到此为止吧。\x02",
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

    def lambda_19E6():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19E6)
    Sleep(50)

    def lambda_19F6():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_19F6)
    Sleep(50)

    def lambda_1A06():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A06)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    #C0055
    ChrTalk(
        0x109,
        "#12P#10109F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#12P#00006F我们太吵闹了，真是抱歉。\x02\x03",

            "#00000F说起来，你们正在\x01",
            "练习吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#06100F是啊。\x01",
            "为了准备明天的晚间表演，\x01",
            "正在做调整工作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0058
    ChrTalk(
        0x9,
        (
            "#06202F呵呵，明天的\x01",
            "客人非常重要，\x01",
            "多少有些紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        (
            "嗯，真没想到各国首脑\x01",
            "要来捧场啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0060
    ChrTalk(
        0x101,
        "#12P#00005F首脑吗……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#12P#00105F说起来，在今天早上的对策会议中\x01",
            "也提到了相关议题。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，毕竟难得\x01",
            "来一次克洛斯贝尔啊。\x02\x03",

            "#10304F彩虹剧团的舞台表演\x01",
            "自然是最高级别的招待项目。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#12P#00300F嗯，这样一想，\x01",
            "的确是最合适的活动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#12P#10100F嗯，也难怪会紧张呢。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "#06203F嗯，其他团员们\x01",
            "似乎也都有些紧张……\x02\x03",

            "#06209F不过，伊莉娅小姐倒是\x01",
            "和平时没有任何区别。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0066
    ChrTalk(
        0x8,
        (
            "#06103F嗯，因为完全没有\x01",
            "在意的必要啊。\x02\x03",

            "#06100F无论观众席上坐的是什么人，\x01",
            "我们要做的都是尽到最大努力。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)

    #C0067
    ChrTalk(
        0xB,
        (
            "#11P你可真是……\x01",
            "无论何时都这么可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "#11P这次提出的新版舞剧也是一样，\x01",
            "你的热情与斗志真是让人佩服。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x101,
        "#12P#00005F新版舞剧……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#12P#00100F说起来……\x01",
            "这次好像是要把『金之太阳、银之月』\x01",
            "翻新重演吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        (
            "#12P#10300F嗯，消息都已经\x01",
            "传遍大街小巷了。\x02\x03",

            "听说要加入\x01",
            "大胆的改编？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E77)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0072
    ChrTalk(
        0x8,
        (
            "#06109F嗯，没错。\x02\x03",

            "#06104F给已经完成的作品增添新内容，\x01",
            "从某种意义上说，是一种冒险的挑战……\x02\x03",

            "#06100F但从脚本、演出的角度来看，\x01",
            "这也是为了使作品的\x01",
            "完成度进一步提高。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#06202F嗯，这次的普通演出结束之后，\x01",
            "我们准备进行为期约一个月\x01",
            "的集中特训。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_END)), "loc_2059")

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#00000F原来如此，上次见面时，\x01",
            "你们所说的『接下来可要忙了』\x01",
            "就是指这件事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "#06100F呵呵，正是。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        (
            "#12P#12P#10100F不过，长达一个月的特训……\x01",
            "虽说只是改编而已，\x01",
            "但也投入了相当的精力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A2")

    label("loc_2059")


    #C0077
    ChrTalk(
        0x109,
        (
            "#12P#10100F原来如此……\x01",
            "虽说只是改编而已，\x01",
            "但也投入了相当的精力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A2")


    #C0078
    ChrTalk(
        0x104,
        (
            "#12P#00300F『金之太阳、银之月』\x01",
            "在彩虹剧团的众多舞剧之中，\x01",
            "也算是完成度极高，评价很好的作品……\x02\x03",

            "#00304F如果还能将它进一步改良，\x01",
            "真是想象不出会变得多么惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#12P#00000F嗯，的确呢。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "#06100F呵呵，既然已经决心要生存在舞台，\x01",
            "就必须要不断追求最高的艺术。\x02\x03",

            "#06104F为了让前来观剧的客人们\x01",
            "度过一段最美好的时间，\x01",
            "我们必须要献出最完美的作品……\x02\x03",

            "#06100F那正是彩虹剧团，\x01",
            "还有我们这些演员的\x01",
            "最大使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#12P#00102F真不愧是伊莉娅小姐，\x01",
            "在舞台表演领域，\x01",
            "真是无人能比呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        (
            "#12P#10109F嗯！真是好期待\x01",
            "新版舞剧的公演！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#06100F呵呵，正式公演的时间也不远了，\x01",
            "敬请期待哦。\x02\x03",

            "就算是曾经欣赏过原版作品的人，\x01",
            "应该也可以体验到新的乐趣。\x02\x03",

            "#06104F另外，在演员阵容方面\x01",
            "也有个很大的惊喜……\x01",
            "到时一定能让各位大吃一惊的。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#00000F惊喜吗……\x01",
            "哈哈，那我就\x01",
            "尽情期待了。\x02",
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

    # Function_8_1685 end

    def Function_9_23ED(): pass

    label("Function_9_23ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23FE")
    Jump("loc_2948")

    label("loc_23FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_240C")
    Jump("loc_2948")

    label("loc_240C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_24C5")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0085
    ChrTalk(
        0x8,
        (
            "#01700F好，我们现在开始确认\x01",
            "『月之舞姬』在另两位\x01",
            "舞姬之后登场的场面。\x02\x03",

            "莉夏、修利，准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        "#01800F嗯……没问题！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        "#04200F我也准备好了！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_2948")

    label("loc_24C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24D6")
    Call(0, 10)
    Jump("loc_2948")

    label("loc_24D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24E4")
    Jump("loc_2948")

    label("loc_24E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24F2")
    Jump("loc_2948")

    label("loc_24F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_262D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250D")
    Call(0, 30)
    Jump("loc_2628")

    label("loc_250D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25C4")

    #C0088
    ChrTalk(
        0x8,
        (
            "#01709F呵呵，这情景让我想起了\x01",
            "久未想起的往事呢。\x02\x03",

            "#01700F如果大家方便，\x01",
            "到时请一定来观赏\x01",
            "新版舞剧哦。\x02\x03",

            "莉夏和修利\x01",
            "都在拼命努力，\x01",
            "到时一定能奉献一场精彩的演出。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2628")

    label("loc_25C4")


    #C0089
    ChrTalk(
        0x8,
        (
            "#01700F到时请一定来观赏\x01",
            "新版舞剧哦。\x02\x03",

            "莉夏和修利\x01",
            "都在拼命努力，\x01",
            "到时一定能奉献一场精彩的演出。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2628")

    Jump("loc_2948")

    label("loc_262D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_263B")
    Jump("loc_2948")

    label("loc_263B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2649")
    Jump("loc_2948")

    label("loc_2649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2664")
    Call(0, 8)
    Jump("loc_27CB")

    label("loc_2664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2746")

    #C0090
    ChrTalk(
        0x8,
        (
            "#06100F既然已经决心要生存在舞台，\x01",
            "就必须要不断追求最高的艺术。\x02\x03",

            "#06104F为了让前来观剧的客人们\x01",
            "度过一段最美好的时间，\x01",
            "我们必须要献出最完美的作品……\x02\x03",

            "#06102F那正是彩虹剧团，\x01",
            "还有我们这些演员的\x01",
            "最大使命。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27CB")

    label("loc_2746")


    #C0091
    ChrTalk(
        0x8,
        (
            "#06100F呵呵，近期就会正式发布\x01",
            "新版舞剧的消息了，\x01",
            "敬请期待哦。\x02\x03",

            "#06104F就算是曾经欣赏过原版作品的人，\x01",
            "应该也可以体验到新的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CB")

    Jump("loc_2948")

    label("loc_27D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_27DE")
    Jump("loc_2948")

    label("loc_27DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EC")

    #C0092
    ChrTalk(
        0x8,
        (
            "#01700F呵呵，增加了新同伴之后，\x01",
            "警察弟弟也要再次开始工作了啊。\x02\x03",

            "#01700F塞茜尔好像也很期待\x01",
            "与你们见面呢。\x02\x03",

            "#01709F哎呀～罗伊德好受欢迎⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00012F哈、哈哈……\x01",
            "请不要戏弄我啦。\x02\x03",

            "#00004F（不过，最近确实应该\x01",
            "  去和塞茜尔姐姐打个招呼呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2948")

    label("loc_28EC")


    #C0094
    ChrTalk(
        0x8,
        (
            "#01700F呵呵，敬请期待\x01",
            "我们今后的消息吧。\x02\x03",

            "#01709F虽然暂时还要保密，\x01",
            "但一定会很有趣的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2948")

    TalkEnd(0xFE)
    Return()

    # Function_9_23ED end

    def Function_10_294C(): pass

    label("Function_10_294C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0095
    ChrTalk(
        0x8,
        (
            "#06100F好了，修利，\x01",
            "离正式上台已经没有多少时间了，\x01",
            "训练会很辛苦哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        "#12201F啊……嗯……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_294C end

    def Function_11_29C1(): pass

    label("Function_11_29C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29D2")
    Jump("loc_2E43")

    label("loc_29D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_29E0")
    Jump("loc_2E43")

    label("loc_29E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4B")

    #C0097
    ChrTalk(
        0x9,
        "#01808F不好意思，我们还要做演出之前的最后准备。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00008F（莉夏………）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A6E")

    label("loc_2A4B")


    #C0099
    ChrTalk(
        0x9,
        "#01801F伊莉娅小姐……拜托了！\x02",
    )

    CloseMessageWindow()

    label("loc_2A6E")

    Jump("loc_2E43")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A81")
    Jump("loc_2E43")

    label("loc_2A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A8F")
    Jump("loc_2E43")

    label("loc_2A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A9D")
    Jump("loc_2E43")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AAB")
    Jump("loc_2E43")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AB9")
    Jump("loc_2E43")

    label("loc_2AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AC7")
    Jump("loc_2E43")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE2")
    Call(0, 8)
    Jump("loc_2CBF")

    label("loc_2AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C63")

    #C0100
    ChrTalk(
        0x9,
        (
            "#06203F通商会议……使各种各样的人\x01",
            "都来到克洛斯贝尔了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00000F看来莉夏\x01",
            "也很紧张吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "#06208F嗯，确实稍有些紧张，而且……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x102,
        "#00105F还有其它心事吗？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "#06202F啊，不不，\x01",
            "并不是什么大不了的事情，\x01",
            "请不必在意。\x02\x03",

            "#06204F总之，我现在还是要\x01",
            "集中精神，专心考虑\x01",
            "舞台表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00005F啊，嗯……\x02\x03",

            "#00003F（通商会议中……莫非有什么\x01",
            "  让莉夏在意的事情吗？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 0)
    Jump("loc_2CBF")

    label("loc_2C63")


    #C0106
    ChrTalk(
        0x9,
        (
            "#06206F我总会去想一些\x01",
            "多余的事情。\x02\x03",

            "#06201F不过现在还是要集中精神，\x01",
            "专心考虑舞台表演。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBF")

    Jump("loc_2E43")

    label("loc_2CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CD2")
    Jump("loc_2E43")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCC")

    #C0107
    ChrTalk(
        0x9,
        (
            "#01802F支援科增加了新成员，并且重新恢复工作……\x01",
            "我今后也会继续\x01",
            "支持大家的。\x02\x03",

            "如果愿意，欢迎随时\x01",
            "来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00000F嗯，彼此彼此。\x01",
            "如果你们有什么事情，请随时联系。\x02\x03",

            "我们一定会全力帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "#01809F呵呵，真可靠呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E43")

    label("loc_2DCC")


    #C0110
    ChrTalk(
        0x9,
        (
            "#01802F支援科增加了新成员，并且重新恢复工作……\x01",
            "我今后也会继续\x01",
            "支持大家的。\x02\x03",

            "#01809F如果愿意，欢迎随时\x01",
            "来这里玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E43")

    TalkEnd(0xFE)
    Return()

    # Function_11_29C1 end

    def Function_12_2E47(): pass

    label("Function_12_2E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E6D")
    Call(0, 58)
    Return()

    label("loc_2E6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_343B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8B")
    Call(0, 35)
    Jump("loc_3436")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_334C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_30FC")

    #C0111
    ChrTalk(
        0xA,
        (
            "#04200F对了，你们已经\x01",
            "去探望过\x01",
            "伊莉娅小姐了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00000F嗯，已经去过了，\x01",
            "她很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#04203F是吗……\x02\x03",

            "#04200F那个，莉夏姐呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x106,
        (
            "#10708F嗯……虽然没有\x01",
            "面对面交谈，\x01",
            "但隔着病房的门，听到了她的声音……\x02\x03",

            "#10702F该说什么好呢……\x01",
            "总之抱歉了，修利，\x01",
            "让你那么担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xA,
        (
            "#04205F哪、哪里，我并没有……\x02\x03",

            "#04204F不过……\x01",
            "总觉得松了一口气。\x02\x03",

            "#04202F总算可以确信\x01",
            "莉夏姐没有\x01",
            "离开我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x106,
        "#10702F修利……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0117
    ChrTalk(
        0xA,
        (
            "#04206F抱歉，莉夏姐，\x01",
            "我说了些孩子气的话。\x02\x03",

            "#04202F总之，我会一直在\x01",
            "这里等你的。\x02\x03",

            "#04209F要早点回来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x106,
        "#10702F呵呵……嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3344")

    label("loc_30FC")


    #C0119
    ChrTalk(
        0xA,
        (
            "#14000F对了，你们已经\x01",
            "去探望过\x01",
            "伊莉娅小姐了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#00000F嗯，已经去过了，\x01",
            "她很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "#14003F是吗……\x02\x03",

            "#14000F那个，莉夏姐呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x106,
        (
            "#10708F嗯……虽然没有\x01",
            "面对面交谈，\x01",
            "但隔着病房的门，听到了她的声音……\x02\x03",

            "#10702F该说什么好呢……\x01",
            "总之抱歉了，修利，\x01",
            "让你那么担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        (
            "#14005F哪、哪里，我并没有……\x02\x03",

            "#14004F不过……\x01",
            "总觉得松了一口气。\x02\x03",

            "#14002F总算可以确信\x01",
            "莉夏姐没有\x01",
            "离开我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x106,
        "#10702F修利……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0125
    ChrTalk(
        0xA,
        (
            "#14006F抱歉，莉夏姐，\x01",
            "我说了些任性的话。\x02\x03",

            "#14002F总之，我会一直在\x01",
            "这里等你的。\x02\x03",

            "#14009F要早点回来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x106,
        "#10702F呵呵……嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_3344")

    SetScenarioFlags(0x1CF, 7)
    Jump("loc_3436")

    label("loc_334C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_33C8")

    #C0127
    ChrTalk(
        0xA,
        (
            "#04200F虽然不知道你们要去哪里，\x01",
            "但小心一些吧。\x02\x03",

            "#04202F再过不久，就要重新开始公演了，\x01",
            "到时一定要来看哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3436")

    label("loc_33C8")


    #C0128
    ChrTalk(
        0xA,
        (
            "#14000F虽然不知道你们要去哪里，\x01",
            "但小心一些吧。\x02\x03",

            "#14002F再过不久，就要重新开始公演了，\x01",
            "到时一定要来看哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3436")

    Jump("loc_3702")

    label("loc_343B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3456")
    Call(0, 13)
    Jump("loc_3491")

    label("loc_3456")


    #C0129
    ChrTalk(
        0xA,
        (
            "#12203F……先出现音效，\x01",
            "随后从幕后跃出，\x01",
            "踏起舞步……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3491")

    Jump("loc_3702")

    label("loc_3496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34A4")
    Jump("loc_3702")

    label("loc_34A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_34DE")

    #C0130
    ChrTalk(
        0xA,
        (
            "#04201F伊莉娅小姐，\x01",
            "我随时都可以开始！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3702")

    label("loc_34DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_34EF")
    Call(0, 10)
    Jump("loc_3702")

    label("loc_34EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34FD")
    Jump("loc_3702")

    label("loc_34FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_350B")
    Jump("loc_3702")

    label("loc_350B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3519")
    Jump("loc_3702")

    label("loc_3519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3534")
    Call(0, 14)
    Jump("loc_358C")

    label("loc_3534")


    #C0131
    ChrTalk(
        0xA,
        (
            "#04203F现在心里要只想着舞台……\x01",
            "是这样吧。\x02\x03",

            "#04201F好、好！\x01",
            "摒弃杂念，开始练习吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358C")

    Jump("loc_3702")

    label("loc_3591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_359F")
    Jump("loc_3702")

    label("loc_359F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_367D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361A")

    #C0132
    ChrTalk(
        0xA,
        (
            "#04206F伊莉娅小姐和莉夏姐\x01",
            "果然厉害啊。\x02\x03",

            "#04200F希望我以后也能掌握\x01",
            "像她们一样精湛的演技……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3678")

    label("loc_361A")


    #C0133
    ChrTalk(
        0xA,
        (
            "#04205F啊，不好了，\x01",
            "必须要赶快做完扫除。\x02\x03",

            "#04203F要是再磨磨蹭蹭的，\x01",
            "就没有练习的时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3678")

    Jump("loc_3702")

    label("loc_367D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_368B")
    Jump("loc_3702")

    label("loc_368B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3702")

    #C0134
    ChrTalk(
        0xA,
        (
            "#04200F话说回来……\x01",
            "莉夏姐改善了休息情况这种事，\x01",
            "到底是怎么看出来的。\x02\x03",

            "#04204F……伊莉娅小姐果然厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3702")

    TalkEnd(0xFE)
    Return()

    # Function_12_2E47 end

    def Function_13_3706(): pass

    label("Function_13_3706")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0135
    ChrTalk(
        0x11,
        (
            "那么，尼克鲁、修利，\x01",
            "我会跟上二位的舞步的，请开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xF,
        (
            "明白了。\x01",
            "来吧，修利。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#12201F嗯，首先是舞步\x01",
            "之后的跳跃吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00000F（修利和其他演员\x01",
            "  好像都在专心练习呢。）\x02",
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

    # Function_13_3706 end

    def Function_14_37DE(): pass

    label("Function_14_37DE")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0139
    ChrTalk(
        0xA,
        (
            "#04205F对了，尼克鲁先生。\x02\x03",

            "伊莉娅小姐她们为什么不把\x01",
            "新版舞剧的详细内容\x01",
            "告诉大家呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xF,
        (
            "哦，我虽然不清楚她的真正想法，\x01",
            "不过主要还是因为还有最终公演吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xF,
        (
            "如果原版舞剧还没结束，就透露下一版的内容，\x01",
            "恐怕会使大家无法集中精神表演……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xF,
        "大概就是这个原因吧。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#04203F是、是吗……原来如此。\x01",
            "尼克鲁先生真聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xF,
        "哪里，这很普通啦……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_14_37DE end

    def Function_15_3958(): pass

    label("Function_15_3958")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0145
    ChrTalk(
        0xA,
        (
            "#04200F对了，尼克鲁先生。\x01",
            "那一幕里的那个\x01",
            "转换到旋转的动作……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xF,
        (
            "哦，那个动作要在\x01",
            "一口气之内完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xF,
        (
            "虽然时机有些难把握，\x01",
            "但还是那样比较流畅。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        "#04201F是、是吗，我试试看。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A8B")

    #C0149
    ChrTalk(
        0x101,
        (
            "#00000F（修利……似乎练习得\x01",
            "  很努力呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#00100F（嗯，能感觉到\x01",
            "  她的专注呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF3")

    label("loc_3A8B")


    #C0151
    ChrTalk(
        0x101,
        (
            "#00005F（这孩子就是彩虹剧团\x01",
            "  新招的那个女孩吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        (
            "#00100F（呵呵，似乎正在\x01",
            "  专注练习呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF3")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_15_3958 end

    def Function_16_3B0C(): pass

    label("Function_16_3B0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B35")
    Call(0, 36)
    Return()

    label("loc_3B35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B46")
    Jump("loc_4036")

    label("loc_3B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3BD8")

    #C0153
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "外出禁止令下达得太过突然，\x01",
            "让人完全摸不清头脑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "算了，不管怎么说，\x01",
            "既然留在了这里，\x01",
            "就集中精神，专心练习吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4036")

    label("loc_3BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF3")
    Call(0, 13)
    Jump("loc_3C1A")

    label("loc_3BF3")


    #C0155
    ChrTalk(
        0xFE,
        (
            "首先是配合修利的节奏，\x01",
            "然后是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1A")

    Jump("loc_4036")

    label("loc_3C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C2D")
    Jump("loc_4036")

    label("loc_3C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C48")
    Call(0, 24)
    Jump("loc_3CAD")

    label("loc_3C48")


    #C0156
    ChrTalk(
        0xFE,
        (
            "虽、虽然不明白是怎么回事，\x01",
            "但好像踩到雷区了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "算了……\x01",
            "前辈说的对，\x01",
            "必须要快点开始练习了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CAD")

    Jump("loc_4036")

    label("loc_3CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CC0")
    Jump("loc_4036")

    label("loc_3CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3CCE")
    Jump("loc_4036")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CDC")
    Jump("loc_4036")

    label("loc_3CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3CEA")
    Jump("loc_4036")

    label("loc_3CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D05")
    Call(0, 14)
    Jump("loc_3D75")

    label("loc_3D05")


    #C0158
    ChrTalk(
        0xFE,
        "该怎么说呢，修利真是很单纯呢。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "不过，正因如此，\x01",
            "她身上才有很多值得学习的地方。\x01",
            "我必须要更加努力才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D75")

    Jump("loc_4036")

    label("loc_3D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D88")
    Jump("loc_4036")

    label("loc_3D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E73")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF6")

    #C0160
    ChrTalk(
        0xFE,
        (
            "哦……\x01",
            "又要到练习时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "问诊表的事情\x01",
            "就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6E")

    label("loc_3DF6")


    #C0162
    ChrTalk(
        0xFE,
        (
            "明天的公演自然让人担心，\x01",
            "而新版舞剧的具体内容\x01",
            "也让我非常在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "算了，不能想这些\x01",
            "多余的事情。\x01",
            "现在要专心练习。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6E")

    Jump("loc_4036")

    label("loc_3E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E81")
    Jump("loc_4036")

    label("loc_3E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC3")

    #C0164
    ChrTalk(
        0xFE,
        (
            "修利还在做杂事……\x01",
            "但每次参加表演练习时，\x01",
            "做出的动作都相当敏捷漂亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "虽然我们剧团的成员大多都可以做到，\x01",
            "但这么快就能掌握得那么好，可以称得上是天才了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "话说回来，大家能有如今的实力，\x01",
            "比才能更加重要的就是长期的努力与积累。\x01",
            "这个就不是能拿来比较的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "总之，现在我也要拼命努力。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4036")

    label("loc_3FC3")


    #C0168
    ChrTalk(
        0xFE,
        (
            "我的才能也许不如大家，\x01",
            "但最近也在逐渐\x01",
            "得到认可。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "虽然有一段时期曾经陷入迷途……\x01",
            "但我现在一定要拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4036")

    TalkEnd(0xFE)
    Return()

    # Function_16_3B0C end

    def Function_17_403A(): pass

    label("Function_17_403A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A7")

    #C0170
    ChrTalk(
        0xC,
        "啊，是各位啊。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "其实……就在刚才，\x01",
            "大师直接和我们\x01",
            "联络了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "说他马上要\x01",
            "开始制作\x01",
            "自动人偶了。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F哎……\x01",
            "那可真不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "而且大师竟然还特意\x01",
            "和我们联络，\x01",
            "这真是非常少有的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        "没有比这更让人开心的了。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#00100F（大师果然\x01",
            "  很在意彩虹剧团呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x103,
        "#00200F（呵呵，希望能尽早完成啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 6)
    Jump("loc_4212")

    label("loc_41A7")


    #C0179
    ChrTalk(
        0xC,
        (
            "大师竟然会积极主动\x01",
            "地协助我们，\x01",
            "再没有比这让人高兴的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "我也必须要继续努力，\x01",
            "做好基础工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4212")

    Jump("loc_4AEA")

    label("loc_4217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_42C2")

    #C0181
    ChrTalk(
        0xFE,
        (
            "大师亲手制作的\x01",
            "舞台装置和自动人偶，\x01",
            "我实在是无法修复……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "不过，至少要努力\x01",
            "把舞台大致修整好。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "大师肯定也很担心\x01",
            "彩虹剧团的事……\x01",
            "我要继续努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEA")

    label("loc_42C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4396")

    #C0184
    ChrTalk(
        0xFE,
        (
            "舞台上的瓦砾已经撤去了，\x01",
            "大家总算可以恢复\x01",
            "正常练习了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "但负责舞台装置的我\x01",
            "要想再次整修、操纵那些装置，\x01",
            "恐怕还要等上很久的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "不过，我仍然会踏实地做好\x01",
            "现在能做的工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4411")

    label("loc_4396")


    #C0187
    ChrTalk(
        0xFE,
        (
            "负责舞台装置的我\x01",
            "要想再次整修、操纵那些装置，\x01",
            "恐怕还要等上很久的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "不过，我仍然会踏实地做好\x01",
            "现在能做的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4411")

    Jump("loc_4AEA")

    label("loc_4416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_45B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453B")

    #C0189
    ChrTalk(
        0xFE,
        (
            "依靠大师协助完成的\x01",
            "舞台装置和自动人偶\x01",
            "全部都被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "大师耗尽心血制造，\x01",
            "饱含剧团成员灵魂的\x01",
            "独一无二的作品，全部都……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "践踏如此贵重的东西，\x01",
            "实在是让人难以饶恕的暴行……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "但只要还有作品……\x01",
            "就会有东山再起的一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "可是，伊莉娅小姐却…………！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_45B3")

    label("loc_453B")


    #C0194
    ChrTalk(
        0xFE,
        (
            "……总之，无论被破坏多少次，\x01",
            "我都会重新筑建\x01",
            "彩虹剧团的舞台。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "如果被这点小挫折击垮，\x01",
            "又怎么对得起\x01",
            "伊莉娅小姐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B3")

    Jump("loc_4AEA")

    label("loc_45B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465C")

    #C0196
    ChrTalk(
        0xFE,
        (
            "好，舞台装置\x01",
            "已经设置完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "装置的运作，也已经在\x01",
            "昨天的彩排中确认过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "接下来要做的，就只剩下\x01",
            "耐心等待表演正式开始了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_46B2")

    label("loc_465C")


    #C0199
    ChrTalk(
        0xFE,
        (
            "好，舞台装置\x01",
            "已经设置完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "接下来要做的，就只剩下\x01",
            "耐心等待表演正式开始了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B2")

    Jump("loc_4AEA")

    label("loc_46B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46C5")
    Jump("loc_4AEA")

    label("loc_46C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46D3")
    Jump("loc_4AEA")

    label("loc_46D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46E1")
    Jump("loc_4AEA")

    label("loc_46E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E2")

    #C0201
    ChrTalk(
        0xFE,
        (
            "我们请一家很熟的工房帮忙制作\x01",
            "在新版舞剧中使用的舞台装置，\x01",
            "好像明天就可以完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "这次我们提了很多任性的要求，\x01",
            "给大师添了不少麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "但大师还是和以往一样，\x01",
            "在最后关头之前想办法完成了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "现在就开始期待取货了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_486D")

    label("loc_47E2")


    #C0205
    ChrTalk(
        0xFE,
        (
            "这次我们提了很多任性的要求，\x01",
            "给大师添了不少麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "但大师还是和以往一样，\x01",
            "在最后关头之前想办法完成了呢。\x01",
            "现在就开始期待取货了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486D")

    Jump("loc_4AEA")

    label("loc_4872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_49E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4973")

    #C0207
    ChrTalk(
        0xFE,
        (
            "关于新的舞台装置，\x01",
            "大体构想已经考虑完毕了，\x01",
            "接下来就是研究具体细节。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "不过，细节方面\x01",
            "还要根据新版舞剧\x01",
            "的练习情况不断调整……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "满打满算，距离公演日\x01",
            "也只有一个月时间了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "如果不全力加油，可就\x01",
            "无论如何也来不及了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_49DE")

    label("loc_4973")


    #C0211
    ChrTalk(
        0xFE,
        (
            "满打满算，距离\x01",
            "新版舞剧的公演日\x01",
            "也只有一个月时间了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "如果不全力加油，可就\x01",
            "无论如何也来不及了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49DE")

    Jump("loc_4AEA")

    label("loc_49E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49F1")
    Jump("loc_4AEA")

    label("loc_49F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A6C")

    #C0213
    ChrTalk(
        0xFE,
        (
            "为了准备明天的晚间公演，\x01",
            "明天下午三点之前\x01",
            "是大家的休息时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "难得的自由时间，\x01",
            "不如去看看揭幕式吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEA")

    label("loc_4A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4A7A")
    Jump("loc_4AEA")

    label("loc_4A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A95")
    Call(0, 7)
    Jump("loc_4AEA")

    label("loc_4A95")


    #C0215
    ChrTalk(
        0xFE,
        "话说回来，速度增加了五成吗……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "我当然会倾尽全力，\x01",
            "但这要求还真是高难度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEA")

    TalkEnd(0xFE)
    Return()

    # Function_17_403A end

    def Function_18_4AEE(): pass

    label("Function_18_4AEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B73")

    #C0217
    ChrTalk(
        0xFE,
        (
            "在这种状况下，\x01",
            "那些孩子仍然在\x01",
            "剧团前声援我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "伊莉娅小姐的鼓励\x01",
            "也是一样……再没有\x01",
            "比这更让人感激的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E68")

    label("loc_4B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4C33")

    #C0219
    ChrTalk(
        0xFE,
        (
            "舞台就是我们的生命。\x01",
            "幸运的是，如今仍然有\x01",
            "很多支持着我们的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "既然如此，我们该做的事情也就显而易见了。\x01",
            "虽然市里发生了如此状况，\x01",
            "但我们还是要像平时一样，继续磨练演技。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E68")

    label("loc_4C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4E")
    Call(0, 19)
    Jump("loc_4C75")

    label("loc_4C4E")


    #C0221
    ChrTalk(
        0xFE,
        (
            "来吧，缇奥多尔，\x01",
            "拿出干劲来……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C75")

    Jump("loc_4E68")

    label("loc_4C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C88")
    Jump("loc_4E68")

    label("loc_4C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA3")
    Call(0, 20)
    Jump("loc_4D03")

    label("loc_4CA3")


    #C0222
    ChrTalk(
        0xFE,
        (
            "哼，不管怎么说，\x01",
            "能够演好任何角色\x01",
            "正是我最大的价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "无论有什么要求，我都能完美达成。\x02",
    )

    CloseMessageWindow()

    label("loc_4D03")

    Jump("loc_4E68")

    label("loc_4D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE8")

    #C0224
    ChrTalk(
        0xFE,
        (
            "话说回来，真不愧是\x01",
            "女权王国利贝尔啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "科洛蒂娅殿下楚楚动人，\x01",
            "尤莉亚准校的容貌仪态也是那么出众，\x01",
            "做军人真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "据说她的剑术也是一流，\x01",
            "要是加入我们，马上就能\x01",
            "成为人气演员吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4E68")

    label("loc_4DE8")


    #C0227
    ChrTalk(
        0xFE,
        (
            "尤莉亚准校……\x01",
            "容貌仪态如此出众，\x01",
            "做军人真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "据说她的剑术也是一流，\x01",
            "要是加入我们，马上就能\x01",
            "成为人气演员吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E68")

    TalkEnd(0xFE)
    Return()

    # Function_18_4AEE end

    def Function_19_4E6C(): pass

    label("Function_19_4E6C")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0229
    ChrTalk(
        0xD,
        (
            "好，普莉埃小姐，\x01",
            "你可以马上开始独唱吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "明白，当我唱到高音部分之后，\x01",
            "你们两个一起出场来烘托气氛吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xE,
        "……知道了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_4E6C end

    def Function_20_4F0E(): pass

    label("Function_20_4F0E")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0232
    ChrTalk(
        0xD,
        (
            "好了，缇奥多尔，\x01",
            "接下来就要轮到我们的高潮剧情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xD,
        (
            "扮演祭坛守护骑士的你，\x01",
            "一剑将扮演浪荡王子的我给……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xD,
        "唔……越说越觉得不爽啊。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xD,
        (
            "为什么新版的作品\x01",
            "不把这里也改编掉呢？\x02",
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
            "呼……\x01",
            "现在说这些还有什么用。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xE,
        (
            "别说废话了，赶快开始吧，\x01",
            "你这白痴。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0238
    ChrTalk(
        0xD,
        (
            "你、你小子……\x01",
            "竟敢叫我白痴！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xD,
        (
            "你才是白痴呢！\x01",
            "哼，你这白痴！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xE,
        (
            "……我道歉就是了，\x01",
            "总之赶快开始吧。\x02",
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
            "#00005F（完、完全不像是\x01",
            "  正式开演之前的气氛呢。）\x02",
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

    # Function_20_4F0E end

    def Function_21_5170(): pass

    label("Function_21_5170")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_520D")

    #C0242
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "我深切感觉到，演员真是一种\x01",
            "幸福的职业啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "我们得到了无数人的恩惠……\x01",
            "为了有朝一日可以数倍报答，\x01",
            "必须要继续努力，不断进步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5497")

    label("loc_520D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_521B")
    Jump("loc_5497")

    label("loc_521B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5236")
    Call(0, 19)
    Jump("loc_525D")

    label("loc_5236")


    #C0244
    ChrTalk(
        0xFE,
        (
            "喂，尤金，\x01",
            "你才是呢，可别被落下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525D")

    Jump("loc_5497")

    label("loc_5262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5270")
    Jump("loc_5497")

    label("loc_5270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_53C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528B")
    Call(0, 20)
    Jump("loc_53C1")

    label("loc_528B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5367")

    #C0245
    ChrTalk(
        0xE,
        (
            "……尤金从以前开始就有这个毛病，\x01",
            "只要心中不安，嘴里就会喋喋不休。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        (
            "他真是太丢人了，\x01",
            "请各位多多包涵。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#00005F是、是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    #C0248
    ChrTalk(
        0xD,
        (
            "喂，缇奥多尔，\x01",
            "别说一些多余的话。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_53C1")

    label("loc_5367")


    #C0249
    ChrTalk(
        0xFE,
        (
            "总之……无论是什么表演，\x01",
            "初演都是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "趁着还有时间，\x01",
            "多练习一下表演吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C1")

    Jump("loc_5497")

    label("loc_53C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5465")

    #C0251
    ChrTalk(
        0xFE,
        "……确实啊。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "听说科洛蒂娅殿下\x01",
            "在学生时代也曾有过\x01",
            "出演戏剧的经验……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "她们两人在舞台上\x01",
            "想必也会是一副\x01",
            "仪表堂堂的姿态。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5497")

    label("loc_5465")


    #C0254
    ChrTalk(
        0xFE,
        (
            "确实……\x01",
            "真想看看她们两人\x01",
            "在舞台上的身姿啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5497")

    TalkEnd(0xFE)
    Return()

    # Function_21_5170 end

    def Function_22_549B(): pass

    label("Function_22_549B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_54F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B9")
    Call(0, 19)
    Jump("loc_54F4")

    label("loc_54B9")


    #C0255
    ChrTalk(
        0xFE,
        (
            "他们两人都是一副干劲满满的样子呢，\x01",
            "我也不能输给他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F4")

    TalkEnd(0xFE)
    Return()

    # Function_22_549B end

    def Function_23_54F8(): pass

    label("Function_23_54F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5509")
    Jump("loc_56B5")

    label("loc_5509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_55D3")

    #C0256
    ChrTalk(
        0xFE,
        (
            "有人认为，在这种特殊时期\x01",
            "还观赏舞台表演是很不严肃的行为……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "但我的看法却完全相反，\x01",
            "我认为越是在这种时期，\x01",
            "就越需要娱乐。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "人生最大的不幸，莫过于连娱乐\x01",
            "的心情都没有，不是吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B5")

    label("loc_55D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55EE")
    Call(0, 13)
    Jump("loc_561F")

    label("loc_55EE")


    #C0259
    ChrTalk(
        0xFE,
        (
            "我要让自己的表演变得\x01",
            "更加迅敏，更加优美……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561F")

    Jump("loc_56B5")

    label("loc_5624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5632")
    Jump("loc_56B5")

    label("loc_5632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_56B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564D")
    Call(0, 24)
    Jump("loc_56B5")

    label("loc_564D")


    #C0260
    ChrTalk(
        0xFE,
        (
            "真是的，尼克鲁那家伙，\x01",
            "真是完全不能对他大意啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "这就是『草食系』男子的手段吗，\x01",
            "不、不可原谅！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B5")

    TalkEnd(0xFE)
    Return()

    # Function_23_54F8 end

    def Function_24_56B9(): pass

    label("Function_24_56B9")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0262
    ChrTalk(
        0x11,
        (
            "那么……\x01",
            "配角就要有点配角的样子，\x01",
            "就让我做好这个绿叶吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xF,
        (
            "才不是什么\x01",
            "配角呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xF,
        (
            "而且，我非常喜欢\x01",
            "塞利娜前辈的表演哦。\x02",
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
            "什、什么！？\x01",
            "你突然说些什么啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x11,
        (
            "无、无聊的闲话就到此为止，\x01",
            "赶快开始练习吧！\x01",
            "白痴！\x02",
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
            "……那个，\x01",
            "我为什么会被骂呢？\x02",
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

    # Function_24_56B9 end

    def Function_25_582A(): pass

    label("Function_25_582A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_25_582A end

    def Function_26_5831(): pass

    label("Function_26_5831")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5856")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_26_5831")

    label("loc_5856")

    Return()

    # Function_26_5831 end

    def Function_27_5857(): pass

    label("Function_27_5857")

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
        "#01702F知道了吗？修利，接下来就按我说的——\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0269
    ChrTalk(
        0xA,
        (
            "#12P#04211F不、不要啦……\x01",
            "尤其是在莉夏姐面前……！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x9,
        (
            "#12P#01802F呵呵，伊莉娅小姐，\x01",
            "修利好像很困扰呢。\x02",
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
        "#12P#00000F哈哈，怎么回事，好热闹啊。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，好像正好是\x01",
            "休息时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x109,
        "#12P#10105F是、是伊莉娅·普拉提耶……！\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x105,
        "#12P#10300F旁边那两人是……\x02",
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
        "#01700F嗯……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x8,
        "#01705F……啊，这不是警察弟弟吗！！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5BB7():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5BB7)
    TurnDirection(0xA, 0x101, 500)

    #C0277
    ChrTalk(
        0x9,
        "#5P#01802F啊……是大家！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB8")
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
            "#1K◆前作的任务「调查跟踪狂的委托」——（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不变更】\x01",      # 0
            "【完成】\x01",        # 1
            "【未完成】\x01",      # 2
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
        (0, "loc_5C9F"),
        (1, "loc_5CA4"),
        (2, "loc_5CAE"),
        (SWITCH_DEFAULT, "loc_5CB8"),
    )


    label("loc_5C9F")

    Jump("loc_5CB8")

    label("loc_5CA4")

    OP_29(0x1D, 0x4, 0x10)
    Jump("loc_5CB8")

    label("loc_5CAE")

    OP_29(0x1D, 0x3, 0x10)
    Jump("loc_5CB8")

    label("loc_5CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE3")

    #C0279
    ChrTalk(
        0xA,
        "#04200F……你们好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CF8")

    label("loc_5CE3")


    #C0280
    ChrTalk(
        0xA,
        "#04200F……啧。\x02",
    )

    CloseMessageWindow()

    label("loc_5CF8")


    def lambda_5CFD():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CFD)

    def lambda_5D17():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D17)

    def lambda_5D31():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5D31)

    def lambda_5D4B():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D4B)
    OP_68(-820, 1620, 12730, 3000)
    MoveCamera(39, 26, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(13510, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    #C0281
    ChrTalk(
        0x101,
        "#12P#00000F哈哈，好久不见。\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        (
            "#12P#00100F抱歉，在你们休息的时候\x01",
            "还过来打扰……\x02",
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
            "呵呵，没有的事啦⊥\x02\x03",

            "好久没见了，\x01",
            "多待一会再走吧。\x02\x03",

            "啊，难得重逢，警察弟弟\x01",
            "要不要和我来个再会的拥抱？\x02",
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
        "#12P#00012F不、不，还是不用了。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#5P#01702F哎，是吗？\x01",
            "其实不用客气嘛。\x02\x03",

            "#01709F呵呵～还是说……\x01",
            "你想和触感更好\x01",
            "的莉夏拥抱呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    def lambda_5F9D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F9D)
    Sleep(50)

    def lambda_5FAD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5FAD)

    #C0286
    ChrTalk(
        0x101,
        "#12P#00011F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x9,
        "#12P#01806F伊、伊莉娅小姐真是的……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        "#12P#04200F喂，怪叔叔行为也要适可而止啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)

    #C0289
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵……\x01",
            "莉夏小姐好像还是\x01",
            "和以前一样辛苦呢。\x02",
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
            "啊、啊哈哈……\x01",
            "没办法，\x01",
            "这大概就是所谓的宿命吧。\x02\x03",

            "话说回来，已经好久没见了，\x01",
            "能再次看到大家真是很开心。\x02\x03",

            "呵呵，今后也请\x01",
            "多多关照哦。\x02",
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
            "#12P#10304F呵呵，莉夏小姐\x01",
            "就是在纪念庆典的公演中\x01",
            "初次登台的那个演员啊。\x02\x03",

            "#10302F你好像住在\x01",
            "旧城区的公寓吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        (
            "#5P#01802F是、是的……\x02\x03",

            "#01805F那个……你莫非就是\x01",
            "旧城区不良团伙的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#12P#10302F瓦吉·赫米斯菲亚，\x01",
            "呵呵，认识你很荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P#01705F啊，莉夏，你认识这孩子吗？\x02\x03",

            "说起来，以前好像\x01",
            "没见过这两个孩子呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，他们是\x01",
            "支援科的新成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        (
            "#12P#10100F我、我是从警备队\x01",
            "外派到支援科的\x01",
            "诺艾尔·希卡！\x02\x03",

            "#10109F那个……我和妹妹芙兰\x01",
            "一直都很喜欢\x01",
            "伊莉娅小姐！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        "#5P#01709F呵呵，谢谢☆\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#12P#00103F缇欧和兰迪\x01",
            "还没回来……\x02\x03",

            "#00100F我们暂时会以现在的\x01",
            "四人阵容展开行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#5P#01700F原来如此～\x02\x03",

            "#01709F呵呵，聚集了不少\x01",
            "与众不同的成员呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#12P#00012F哪、哪里～\x01",
            "还比不上伊莉娅\x01",
            "小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x109,
        (
            "#12P#10106F说起来，演员真是\x01",
            "比我想象中\x01",
            "平易近人得多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#12P#10302F确实，\x01",
            "而且和杂志上的照片相比，\x01",
            "真人要更加美貌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        (
            "#5P#01702F呵呵，谢谢。\x01",
            "不过，就算这样夸我，\x01",
            "也没有好处可以得哦～\x02\x03",

            "#01703F对了……\x02\x03",

            "#01709F喂，怎么从刚才开始就一直默不作声？\x01",
            "你也来打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xA,
        "#5P#04205F……知、知道啦。\x02",
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
            "我是在剧团负责杂务的\x01",
            "修利·亚特雷德。\x02\x03",

            "那个……请多指教。\x02",
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
        "#12P#10100F请多指教哦，修利小姐。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A54")

    #C0307
    ChrTalk(
        0x101,
        "#12P#00000F哈哈，修利也很有精神啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0308
    ChrTalk(
        0xA,
        (
            "#5P#04203F哼，不要嬉皮笑脸地和我搭话。\x02\x03",

            "#04201F……话说在先，我可没有\x01",
            "忘记那时的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x101,
        "#12P#00006F（还、还在记恨吗……）\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        "#12P#10105F哎，那时的事情是指……？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "#5P#01709F这个嘛，就是警察弟弟\x01",
            "从背后动手，一把就将修利的──\x02",
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
            "#12P#00011F等、等一下，不是啦……\x02\x03",

            "#00006F再怎么说，那件事的根本原因\x01",
            "还是在修利吧！？\x02",
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
            "#5P#04205F你、你说什么！？\x02\x03",

            "#04208F……虽、虽然我\x01",
            "确实也有不对……\x02\x03",

            "#04201F但你当时那么用力地抱住不放，\x01",
            "还厚颜无耻地……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_68B8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68B8)
    Sleep(50)

    def lambda_68C8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_68C8)
    Sleep(50)
    TurnDirection(0x105, 0x101, 500)

    #C0314
    ChrTalk(
        0x109,
        "#12P#10105F抱、抱住……！？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，听起来好像\x01",
            "发生过很有趣的事啊。\x02",
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
        "#12P#00011F没、没有啦，那只是……！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#5P#01709F哦哦！突然间就要开战了啊！\x01",
            "机会难得，就让我也参加吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        (
            "#5P#01806F伊、伊莉娅小姐……\x01",
            "那样可就更难收场了。\x02",
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
            "#12P#00006F（呜呜，\x01",
            "  那件事情真是\x01",
            "  越解释越麻烦啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6A54")


    #C0320
    ChrTalk(
        0x101,
        "#12P#00005F哎，修利『小姐』……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0321
    ChrTalk(
        0x101,
        (
            "#12P#00011F#4S难、难道是女孩吗！？#3S\x02\x03",

            "#00003F是、是这样啊……\x01",
            "之前来这里时倒也见过好几次，\x01",
            "但完全没察觉到呢。\x02\x03",

            "#00000F嗯，仔细一看，长得确实很可爱……\x02",
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

    def lambda_6BC6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BC6)
    Sleep(50)

    def lambda_6BD6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6BD6)
    Sleep(50)

    def lambda_6BE6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6BE6)
    Sleep(50)

    def lambda_6BF6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6BF6)
    Sleep(50)

    def lambda_6C06():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C06)
    Sleep(50)
    TurnDirection(0xA, 0x101, 500)

    #C0322
    ChrTalk(
        0xA,
        "#5P#04201F这、这个混账……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x9,
        "#5P#01806F罗、罗伊德警官……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        "#6P#00111F……这实在是有点失礼了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0325
    ChrTalk(
        0x101,
        (
            "#11P#00011F啊啊，抱歉！\x01",
            "因为她一直用男性语气，所以就……！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        "#5P#01709F哈哈，不愧是警察弟弟啊。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x105,
        (
            "#12P#10304F唔……原来还有\x01",
            "这招可以用啊，\x01",
            "真是受教了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0328
    ChrTalk(
        0x101,
        "#5P#00011F不、不是啦，你误会了……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xA,
        "#5P#04203F……哼，讨厌的家伙。\x02",
    )

    CloseMessageWindow()

    label("loc_6D90")


    #C0330
    ChrTalk(
        0x9,
        (
            "#5P#01803F呵呵，不管怎么说……\x01",
            "大家都这么精神，真是太好了。\x02\x03",

            "#01809F非常感谢支援科\x01",
            "一直以来的关照……\x01",
            "以后随时欢迎大家过来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#5P#01700F嗯嗯，我也非常欢迎。\x02\x03",

            "#01704F而且莉夏最近的练习场面\x01",
            "比以前更有观赏价值了。\x02",
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

    def lambda_6EF3():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EF3)
    Sleep(50)

    def lambda_6F03():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F03)
    Sleep(50)

    def lambda_6F13():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F13)
    Sleep(50)

    def lambda_6F23():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F23)
    Sleep(50)

    def lambda_6F33():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F33)
    Sleep(50)
    TurnDirection(0xA, 0x8, 500)

    #C0332
    ChrTalk(
        0x101,
        "#12P#00005F哎，是吗？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x105,
        (
            "#12P#10302F确实如此。\x01",
            "她在舞台上跳跃时，\x01",
            "肯定很值得一看呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x109,
        "#12P#10106F喂、喂！瓦吉。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x9,
        "#11P#01802F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "#5P#01709F哈哈，那自然也是看点之一。\x02\x03",

            "#01704F另外，她最近的日常举止\x01",
            "也让人觉得很有精神。\x02\x03",

            "#01702F怎么说呢，好像完全感觉不到她的疲态……\x01",
            "据我猜测，大概是休息情况\x01",
            "有了改善吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0337
    ChrTalk(
        0x9,
        (
            "#11P#01809F……那、那个，\x01",
            "也可以这么说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    #C0338
    ChrTalk(
        0xA,
        (
            "#6P#04205F是吗……\x01",
            "我完全都没注意到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#12P#00100F伊莉娅小姐的观察力\x01",
            "自然和一般人不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x9,
        (
            "#11P#01803F（……确实是这样，\x01",
            "  最近没有那边的『工作』，\x01",
            "  所以得到了充分的休息……）\x02\x03",

            "#01808F（不过，竟然连这都能感觉到，\x01",
            "  伊莉娅小姐果然厉害……）\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈，莉夏一向\x01",
            "是拼命型……\x02\x03",

            "今后也要注意休息，\x01",
            "不要把身体累坏啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7236():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7236)
    Sleep(50)
    TurnDirection(0xA, 0x102, 500)

    #C0342
    ChrTalk(
        0x9,
        "#5P#01802F好的，谢谢关心。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        (
            "#12P#00103F话说回来，彩虹剧团\x01",
            "一直都很忙……\x02\x03",

            "#00100F我们最好控制\x01",
            "来这里的次数，\x01",
            "尽量不要添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "#5P#01702F呵呵，只要不是在\x01",
            "排练或演出，\x01",
            "随时都欢迎你们过来。\x02\x03",

            "#01703F呼，不过接下来\x01",
            "可能会有点忙了。\x02",
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
        "#12P#10105F哎……这样啊？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x105,
        (
            "#12P#10302F莫非有什么\x01",
            "有趣的计划吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#5P#01709F呵呵，暂·时·保·密⊥\x02\x03",

            "#01700F总之就请期待\x01",
            "我们以后的消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#12P#00000F哈哈，知道了。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#12P#00100F那可要\x01",
            "密切关注了。\x02",
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

    # Function_27_5857 end

    def Function_28_74C4(): pass

    label("Function_28_74C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 6)), scpexpr(EXPR_END)), "loc_74D1")
    Call(0, 29)
    Return()

    label("loc_74D1")

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
        "#5P#00000F莉夏，还有修利……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x102,
        (
            "#11P#00100F修利穿着\x01",
            "『星之舞姬』的服装呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        "#12P#00202F……好漂亮。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x104,
        (
            "#6P#00305F不过，阿修那小鬼……\x01",
            "看起来好像有些焦躁啊。\x02",
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
            "#12206F呼、呼、呼……\x02\x03",

            "#12201F剧团长，\x01",
            "刚才的表演很完美吧？\x02\x03",

            "伊莉娅小姐应该\x01",
            "也会认可吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        (
            "#6P唔，算是基本合格吧，\x01",
            "但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        (
            "#12206F呼，又是这样吗……\x02\x03",

            "#12200F莉夏姐，\x01",
            "你觉得呢？\x02\x03",

            "#12202F我的动作\x01",
            "并没有错误吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        "#06203F嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0358
    ChrTalk(
        0x9,
        (
            "#06202F……不过，修利。\x02\x03",

            "下次表演的时候，\x01",
            "试着多带些感情吧。\x02\x03",

            "#06204F我表达得可能不是很清楚……\x01",
            "大概就是在心里想着\x01",
            "『自己想要这样表现』。\x02",
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
            "#12201F『自己想要这样表现』……\x01",
            "唔，具体应该怎么做呢？\x02",
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
        "#5P#00005F（修利……）\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x105,
        (
            "#6P#10300F（嗯，看来我们还是\x01",
            "  离开为好呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x109,
        (
            "#12P#10103F（嗯……\x01",
            "  别打扰她们了。）\x02",
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

    # Function_28_74C4 end

    def Function_29_7955(): pass

    label("Function_29_7955")

    EventBegin(0x1)

    #C0363
    ChrTalk(
        0x101,
        (
            "#00000F（莉夏和修利……\x01",
            "  似乎正在专心\x01",
            "  练习呢。）\x02\x03",

            "#00003F（现在还是不要去打扰她们了。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    EventEnd(0x4)
    Return()

    # Function_29_7955 end

    def Function_30_79CE(): pass

    label("Function_30_79CE")

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
            "#12P#00000F伊莉娅小姐……\x01",
            "你在这里啊。\x02",
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
            "#5P#01705F啊，是警察弟弟啊。\x02\x03",

            "#01709F呵呵，新版舞剧的公演已经临近，\x01",
            "你们是来鼓励我的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        (
            "#6P#00100F呵呵，正是。\x02\x03",

            "伊莉娅小姐，\x01",
            "你在这里观看\x01",
            "莉夏和修利的练习吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(300)

    #C0368
    ChrTalk(
        0x8,
        (
            "#5P#01704F嗯，因为在二层观众席\x01",
            "可以俯视到整个舞台嘛。\x02\x03",

            "#01702F哎呀呀，话说回来，\x01",
            "年轻人努力练习的\x01",
            "样子真是很棒呢～\x02\x03",

            "看着她们，让我不由得\x01",
            "想起了自己的新人时代呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#12P#00005F伊莉娅小姐的新人时代吗……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#12P#00302F哈哈，真是难以想象啊。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，如果不介意，\x01",
            "倒是很想听听你当时的事情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0372
    ChrTalk(
        0x8,
        (
            "#5P#01700F哈，这当然没问题……\x01",
            "但也并不是很有趣哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x109,
        (
            "#12P#10109F哇！请一定讲给我们听啊！！\x02\x03",

            "#10100F我记得伊莉娅小姐初次登台之后，\x01",
            "杂志以『倍受期待的超级新人』为主题，\x01",
            "进行了大篇幅的报道。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        (
            "#6P#00205F原来如此，初次亮相就大获成功啊。\x02\x03",

            "#00202F顺便一问……\x01",
            "伊莉娅小姐是因为什么契机，\x01",
            "才会决定以演员为目标呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#5P#01703F嗯，这个嘛。\x02\x03",

            "#01700F是因为\x01",
            "在童年时期观赏了\x01",
            "彩虹剧团的表演吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x104,
        (
            "#12P#00300F原来如此，从此就开始憧憬彩虹剧团──\x01",
            "大概就是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        (
            "#5P#01703F唔……稍微有些不同。\x02\x03",

            "#01700F彩虹剧团当时就拥有演技出色的演员\x01",
            "和精巧的舞台装置，\x01",
            "表演非常精彩……\x02\x03",

            "#01706F但表演结束之后，\x01",
            "我却总有点不满足的感觉，\x01",
            "总觉得缺了些什么。\x02",
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
        "#12P#00011F不、不满足的感觉……\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#5P#01700F当时，周围的观众们和\x01",
            "我的父母都赞不绝口，\x01",
            "表演显然是很优秀的……\x02\x03",

            "#01703F但是，我却一直在想\x01",
            "『如果由我来演，一定可以更加精彩的』。\x01",
            "大概就是这种感觉吧。\x02\x03",

            "#01702F呵呵，我当时只是个没有任何\x01",
            "相关知识的外行人，但却产生了那种想法，\x01",
            "其实很奇怪吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        "#12P#10105F哎，在童年时期就有那种想法……\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x105,
        (
            "#6P#10300F唔……不过，你怀着这种心态\x01",
            "成为了彩虹剧团的一员，\x01",
            "之后的冲突想必不少吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#5P#01706F嗯，一个初来乍到的底层新人，\x01",
            "却经常多嘴，\x01",
            "冲突自然免不了。\x02\x03",

            "#01700F不过，我始终怀有坚定的信念，\x01",
            "坚信可以完成更加出色\x01",
            "的表演……\x02\x03",

            "#01709F我不断用实力证明自己，\x01",
            "渐渐自然而然地得到了大家的理解，\x01",
            "之后也就没有什么冲突了。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x103,
        (
            "#6P#00202F原来如此……\x01",
            "经过那些历练，才有了\x01",
            "如今的伊莉娅小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x8,
        (
            "#5P#01704F呵呵，但至今为止，\x01",
            "几乎没有能让我完全满意的作品呢。\x02\x03",

            "#01702F不过，莉夏和修利都是\x01",
            "前途无限的好材料……\x02\x03",

            "这样下去，\x01",
            "今后说不定可以创作出\x01",
            "最完美的作品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#12P#00002F哈哈，伊莉娅小姐对艺术\x01",
            "的渴求真是永无止境啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x102,
        (
            "#6P#00104F呵呵，有句话是『努力比天赋更重要』……\x02\x03",

            "#00109F而伊莉娅小姐却是努力型的天才，\x01",
            "真可以称得上是所向无敌了。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x104,
        "#12P#00309F嗯，说得没错。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "#5P#01709F呵呵，让你们听了\x01",
            "不少很无趣的话。\x02\x03",

            "#01704F好了，如果有兴趣，\x01",
            "请大家到时一定来观看\x01",
            "新版舞剧的表演。\x02\x03",

            "#01700F莉夏和修利也一定\x01",
            "会为大家展现\x01",
            "最完美的演技。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#12P#00004F嗯，那是不用怀疑的。\x02\x03",

            "#00000F伊莉娅小姐和大家共同创作的最高之作……\x01",
            "真是让我期待万分。\x02",
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

    # Function_30_79CE end

    def Function_31_85B6(): pass

    label("Function_31_85B6")

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
        "啊，你们是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_86DF():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_86DF)

    def lambda_86EC():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_86EC)
    TurnDirection(0xA, 0x0, 500)

    def lambda_8700():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8700)

    def lambda_871A():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_871A)

    def lambda_8734():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8734)

    def lambda_874E():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_874E)

    def lambda_8768():
        OP_95(0xFE, 700, 1450, 9980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8768)
    WaitChrThread(0x101, 1)

    #C0391
    ChrTalk(
        0x8,
        "#01705F啊，这不是警察弟弟吗。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xA,
        "#04205F有、有什么事……？\x02",
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
        "#00003F莉夏……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        "#00108F莉夏小姐……\x02",
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
            "#01705F怎么了，怎么了？\x01",
            "莉夏，你和警察弟弟他们发生了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "#01803F……没什么。\x02\x03",

            "#01801F伊莉娅小姐，先别说这些了，\x01",
            "离正式表演已经没有多少时间了。\x02\x03",

            "我想再次检验一下\x01",
            "我和修利的磨合程度。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)

    #C0398
    ChrTalk(
        0xA,
        (
            "#04200F没错，伊莉娅小姐！\x02\x03",

            "我也想把握好\x01",
            "那段戏的节奏。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0399
    ChrTalk(
        0x8,
        "#01705F啊……嗯，说得也对。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0400
    ChrTalk(
        0x8,
        (
            "#01703F警察弟弟，情况如你们所见，\x01",
            "如果没有太重要的事情，\x01",
            "今天就请各位先回去吧。\x02\x03",

            "#01700F我不希望她们的注意力\x01",
            "被打断。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A12():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A12)
    TurnDirection(0x102, 0x8, 500)

    #C0401
    ChrTalk(
        0x101,
        "#00003F好、好的……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#00103F……打扰大家了，\x01",
            "真是抱歉。\x02",
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

    # Function_31_85B6 end

    def Function_32_8AAB(): pass

    label("Function_32_8AAB")

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

    def lambda_8CFB():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CFB)

    def lambda_8D15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D15)
    Sleep(100)

    def lambda_8D29():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D29)

    def lambda_8D43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D43)
    Sleep(500)

    def lambda_8D57():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D57)

    def lambda_8D71():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8D71)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_8DB3():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DB3)

    def lambda_8DCD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8DCD)
    Sleep(500)

    def lambda_8DE1():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_8DE1)

    def lambda_8DFB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_8DFB)
    Sleep(100)

    def lambda_8E0F():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_8E0F)

    def lambda_8E29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_8E29)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0403
    ChrTalk(
        0x101,
        "#12P#00002F这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EB4")

    #C0404
    ChrTalk(
        0x10A,
        (
            "#12P#00602F『金之太阳、银之月』\x01",
            "的追加场面吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EEA")

    label("loc_8EB4")


    #C0405
    ChrTalk(
        0x109,
        (
            "#12P#10102F『金之太阳、银之月』\x01",
            "的追加场面啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EEA")


    #C0406
    ChrTalk(
        0x103,
        "#12P#00202F修利好厉害……\x02",
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

    def lambda_8FDB():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FDB)

    def lambda_8FF5():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FF5)

    def lambda_900F():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_900F)

    def lambda_9029():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9029)

    def lambda_9043():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9043)

    def lambda_905D():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_905D)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    #C0407
    ChrTalk(
        0xB,
        "#5P啊，是你们……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#12P#00000F剧团长，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x102,
        (
            "#12P#00100F各位都在\x01",
            "专心致志地练习啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xB,
        (
            "#5P嗯，我们重新设计了\x01",
            "以修利为中心的表演结构，\x01",
            "如今总算是已经成型了。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xB,
        (
            "#5P为了尽早恢复演出，\x01",
            "如今必须要全力\x01",
            "加油才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xB,
        (
            "#5P听说伊莉娅已经\x01",
            "恢复了意识……\x01",
            "这也是为了回应她的期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#12P#00000F原来如此……是这样啊。\x02\x03",

            "#00008F（……对了，剧团的各位\x01",
            "  还不知道莉夏\x01",
            "  现在的下落呢。）\x02\x03",

            "#00003F（我想应该让他们\x01",
            "  见上一面吧……）\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_934C")
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
    Jump("loc_93DA")

    label("loc_934C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_93DA")
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

    label("loc_93DA")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_32_8AAB end

    def Function_33_93EC(): pass

    label("Function_33_93EC")

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

    def lambda_95F0():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95F0)

    def lambda_960A():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_960A)

    def lambda_9624():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9624)

    def lambda_963E():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_963E)

    def lambda_9658():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9658)

    def lambda_9672():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9672)
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
        "#5P是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xB,
        "#5P如何，气势十足吧？\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)

    #C0416
    ChrTalk(
        0xB,
        (
            "#11P为了重新开始公演，\x01",
            "大家现在都在\x01",
            "全力拼搏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xB,
        (
            "#11P听说伊莉娅\x01",
            "已经醒过来了……\x01",
            "这也是为了回应她的期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x101,
        (
            "#12P#00003F（……剧团的各位\x01",
            "  还不知道莉夏\x01",
            "  现在的下落呢。）\x02\x03",

            "#00008F（我想应该让他们\x01",
            "  见上一面吧……）\x02",
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

    # Function_33_93EC end

    def Function_34_9808(): pass

    label("Function_34_9808")

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

    def lambda_9A58():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A58)

    def lambda_9A72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A72)
    Sleep(100)

    def lambda_9A86():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A86)

    def lambda_9AA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9AA0)
    Sleep(500)

    def lambda_9AB4():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9AB4)

    def lambda_9ACE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9ACE)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_9B10():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9B10)

    def lambda_9B2A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9B2A)
    Sleep(500)

    def lambda_9B3E():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9B3E)

    def lambda_9B58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_9B58)
    Sleep(100)

    def lambda_9B6C():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9B6C)

    def lambda_9B86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_9B86)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CC6")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0419
    ChrTalk(
        0x101,
        "#12P#00000F这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C1B")

    #C0420
    ChrTalk(
        0x10A,
        (
            "#12P#00602F『金之太阳、银之月』\x01",
            "的追加场面吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CA2")

    label("loc_9C1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C66")

    #C0421
    ChrTalk(
        0x109,
        (
            "#12P#10102F『金之太阳、银之月』\x01",
            "的追加场面啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CA2")

    label("loc_9C66")


    #C0422
    ChrTalk(
        0x105,
        (
            "#12P#10402F呵呵，是『金之太阳、银之月』\x01",
            "的追加场面啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA2")


    #C0423
    ChrTalk(
        0x103,
        "#12P#00202F修利好厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D17")

    label("loc_9CC6")


    #C0424
    ChrTalk(
        0x101,
        (
            "#12P#00000F大家还在努力\x01",
            "练习啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x106,
        "#12P#10702F……修利，还有大家…………\x02",
    )

    CloseMessageWindow()

    label("loc_9D17")

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

    def lambda_9DE9():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DE9)

    def lambda_9E03():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E03)

    def lambda_9E1D():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E1D)

    def lambda_9E37():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E37)

    def lambda_9E51():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9E51)

    def lambda_9E6B():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9E6B)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9ECD")

    #C0426
    ChrTalk(
        0xB,
        "#5P啊，是你们……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EE6")

    label("loc_9ECD")


    #C0427
    ChrTalk(
        0xB,
        "#5P哦，是你们啊……\x02",
    )

    CloseMessageWindow()

    label("loc_9EE6")

    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0428
    ChrTalk(
        0xB,
        (
            "#5P莉夏……\x01",
            "这不是莉夏吗！\x02",
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
        "#5P#N#12211F莉夏姐……？\x02",
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

    def lambda_9FE1():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9FE1)
    Sleep(50)

    def lambda_9FF1():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9FF1)
    Sleep(50)

    def lambda_A001():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A001)
    Sleep(50)

    def lambda_A011():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A011)
    Sleep(50)

    def lambda_A021():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A021)
    Sleep(50)

    def lambda_A031():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A031)
    Sleep(50)

    def lambda_A041():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A041)
    Sleep(50)

    def lambda_A051():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A051)
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
        "#5P真的是莉夏啊！\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xD,
        "#5P哈哈，好像不是假的嘛。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xE,
        "#5P……没错，真的是莉夏。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x10,
        (
            "#5P呵呵，心中最后的一块大石\x01",
            "终于也落了地啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x106,
        (
            "#12P#10717F……各位…………\x02\x03",

            "#10703F……真是……对不起。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A327")
    SetChrPos(0x10A, 680, 500, 11260, 0)
    Jump("loc_A35E")

    label("loc_A327")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A34D")
    SetChrPos(0x109, 680, 500, 11260, 0)
    Jump("loc_A35E")

    label("loc_A34D")

    SetChrPos(0x105, 680, 500, 11260, 0)

    label("loc_A35E")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0435
    ChrTalk(
        0xB,
        (
            "#5P是吗，你现在和\x01",
            "支援科的各位一起行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x106,
        (
            "#12P#10708F是的，现在还无法\x01",
            "将所有内情交代清楚……\x02\x03",

            "#10710F不过，等我把事情做个了结之后，\x01",
            "一定会好好向大家……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x10,
        (
            "#5P呵呵，莉夏可真是的，\x01",
            "何必露出那么一副\x01",
            "焦急的表情啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0438
    ChrTalk(
        0x106,
        "#12P#10712F哎……？\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x11,
        (
            "#5P就是啊，\x01",
            "根本没有任何人\x01",
            "要逼问或责怪你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xF,
        (
            "#5P哎，真是的，\x01",
            "这么漂亮的美人，皱着眉头太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x106,
        (
            "#12P#10718F普莉埃小姐……\x01",
            "塞利娜小姐、尼克鲁先生……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xE,
        (
            "#5P总之……\x01",
            "把要做的事情做完以后，\x01",
            "一定要第一时间回来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xD,
        (
            "#5P没错，我还需要莉夏\x01",
            "陪我一起练习表演呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x106,
        "#12P#10716F缇奥多尔先生、尤金先生……\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x12,
        (
            "#5P呵呵，我会准备好服装，\x01",
            "等你回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xC,
        "#5P我也会准备好舞台装置，等着你的。\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x106,
        "#12P#10715F卡雷利亚小姐、海因兹先生……\x02",
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
        "#12208F……莉夏姐………\x02",
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0449
    ChrTalk(
        0x106,
        "#12P#10716F修利……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xA,
        (
            "#12206F这里……彩虹剧团……\x01",
            "……是莉夏姐的家。\x02\x03",

            "#12212F我虽然不知道莉夏姐\x01",
            "背负着什么……\x02\x03",

            "#12210F但这里始终都是莉夏姐……\x01",
            "还有伊莉娅小姐\x01",
            "和我的家……\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x106,
        "#12P#10718F……修利………\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xA,
        (
            "#12212F我……无论发生什么，\x01",
            "都会一直守护这里……所以………\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x106,
        (
            "#12P#10715F嗯……嗯……\x02\x03",

            "#10716F……修利的心情，\x01",
            "我完全感受到了。\x02\x03",

            "#10716F我一定会回来的……\x01",
            "……一言为定，所以不用担心。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0454
    ChrTalk(
        0xA,
        (
            "#12210F约定……真的吗？莉夏姐。\x02\x03",

            "如果说谎，要吞千针啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x106,
        "#12P#10715F嗯……我知道。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    #C0456
    ChrTalk(
        0x101,
        "#11P#00002F莉夏……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(300)

    #C0457
    ChrTalk(
        0x106,
        (
            "#6P#10715F……罗伊德警官，\x01",
            "该走了。\x02\x03",

            "#10716F大家还要继续练习……\x01",
            "我们也要赶快前往\x01",
            "目的地。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        "#00000F嗯……是啊。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AA53")
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
    Jump("loc_AAE6")

    label("loc_AA53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AAE6")
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

    label("loc_AAE6")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_34_9808 end

    def Function_35_AAF8(): pass

    label("Function_35_AAF8")

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
        "#6P#00005F怎么了？修利。\x02",
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
            "#11P#14000F啊……\x01",
            "哦，只是在祈祷而已。\x02\x03",

            "#14003F毕竟这也算个祭坛……\x01",
            "虽然只是舞台布景而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x104,
        (
            "#12P#00302F哈哈，原来如此，\x01",
            "但看起来似乎会很灵验呢。\x02\x03",

            "#00305F那你究竟在祈祷什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x102,
        (
            "#6P#00106F喂，兰迪，\x01",
            "怎么可以随便问这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xA,
        (
            "#11P#14000F啊，其实无所谓啦。\x02\x03",

            "#14003F首先自然是祈祷伊莉娅小姐尽快康复……\x02\x03",

            "然后就是为你们祈祷。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0465
    ChrTalk(
        0x101,
        "#6P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x103,
        "#6P#00205F为我们吗？\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xA,
        (
            "#11P#14003F…………………………\x02\x03",

            "#14001F……虽然不清楚详细情况，\x01",
            "不过你们是在\x01",
            "追寻琪雅吧？\x02\x03",

            "而且好像又要去\x01",
            "很危险的地方。\x02\x03",

            "#14003F………………………\x02\x03",

            "#14002F所以我祈祷你们能平安归来，\x01",
            "毕竟莉夏姐也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF22")

    #C0468
    ChrTalk(
        0x106,
        (
            "#6P#10702F修利……\x01",
            "呵呵，谢谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF9A")

    label("loc_AF22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF62")

    #C0469
    ChrTalk(
        0x109,
        (
            "#6P#10102F原来如此……\x01",
            "修利，谢谢啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF9A")

    label("loc_AF62")


    #C0470
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，原来如此……\x01",
            "这话真是让人\x01",
            "开心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF9A")


    #C0471
    ChrTalk(
        0x101,
        (
            "#6P#00002F嗯，你真是难得说出\x01",
            "这样体贴的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xA,
        (
            "#11P#14012F总、总之……\x01",
            "琪雅是我重要的朋友。\x02\x03",

            "#14001F你们一定要把她带回来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        "#6P#00000F嗯，那当然！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B377")

    #C0474
    ChrTalk(
        0xA,
        (
            "#11P#14000F对了……\x01",
            "有件东西，希望你们\x01",
            "能带走。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        (
            "#6P#00000F东西……\x01",
            "是什么呢？\x02",
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
            "修利摘下自己的帽子，交到罗伊德手中。\x07\x00\x02",
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
            "收下了。\x02",
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
        "#6P#00005F这是……\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xA,
        (
            "#11P#04203F其实我真的\x01",
            "很想和你们一起\x01",
            "去找琪雅……\x02\x03",

            "#04208F但我也明白，\x01",
            "那是不可能的。\x02\x03",

            "作为替代，希望你们能把我\x01",
            "最喜欢的帽子带走。\x02\x03",

            "#04201F……不行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x101,
        "#6P#00002F怎么会，当然可以。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#6P#00102F修利的心意，\x01",
            "我们已经感受到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x103,
        (
            "#6P#00202F嗯，我们会负起责任，\x01",
            "帮你保管的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B312")

    #C0483
    ChrTalk(
        0xA,
        (
            "#11P#04212F是、是吗……\x01",
            "那就拜托了。\x02\x03",

            "#04202F好了，\x01",
            "莉夏姐，还有大家，\x01",
            "一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x106,
        "#6P#10709F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_B377")

    label("loc_B312")


    #C0485
    ChrTalk(
        0xA,
        (
            "#11P#04212F是、是吗……\x01",
            "那就拜托了。\x02\x03",

            "#04202F好了，\x01",
            "一定要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        "#6P#00000F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_B377")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3D2")
    OP_E0(0x34, 0x0)

    label("loc_B3D2")

    EventEnd(0x5)
    Return()

    # Function_35_AAF8 end

    def Function_36_B3D5(): pass

    label("Function_36_B3D5")

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
        "哦，你们不是……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        (
            "#6P#00000F你好，尼克鲁先生。\x02\x03",

            "我们找你有点事情……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将接受教授的委托，\x01",
            "前来收取问诊表的事情做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0490
    ChrTalk(
        0xF,
        "哦，是那张问诊表啊。\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xF,
        (
            "最近练习得太开心，\x01",
            "把交表的事情\x01",
            "完全忘掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xF,
        (
            "稍等一下啊，\x01",
            "我这就拿来。\x02",
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
        "嗯，是这个吧？\x02",
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
            "收下了。\x02",
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
        "#6P#00000F是的，就是这个。\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#6P#00102F呵呵，看样子，\x01",
            "药物的影响已经\x01",
            "彻底消除了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xF,
        (
            "嗯，我接受了\x01",
            "彻底的治疗。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xF,
        (
            "……现在想想，\x01",
            "我为何会沾染\x01",
            "那种药物呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xF,
        (
            "当时觉得自己\x01",
            "缺乏才能，\x01",
            "心情非常消沉……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x105,
        (
            "#6P#10303F所以才会心生空虚，\x01",
            "让那种药物有了\x01",
            "可乘之机啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#6P#00300F哈，既然你能自力醒悟，\x01",
            "也就不需要担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xF,
        (
            "嗯……为了彩虹剧团，\x01",
            "我今后一定会多加努力，\x01",
            "让演技继续精进。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x109,
        "#6P#10100F期待你今后在舞台上的表现哦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 4)
    OP_29(0x70, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B841")

    #A0504
    AnonymousTalk(
        0x101,
        (
            "#00000F好，我们已经把所有\x01",
            "问诊表都收回来了。\x02\x03",

            "赶快给赛兰德教授\x01",
            "送去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_B841")

    OP_93(0xF, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 65000, 0, 3000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_B3D5 end

    def Function_37_B873(): pass

    label("Function_37_B873")

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
        "#11P#00000F嗯，玛丽在不在这里呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0506
    ChrTalk(
        0x101,
        "#11P#00005F啊！\x02",
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
        "#11P#04600F呵呵，这么快就找到了呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)

    #C0508
    ChrTalk(
        0x101,
        (
            "#5P#00000F好，接下来\x01",
            "就交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    #C0509
    ChrTalk(
        0x1A3,
        (
            "#11P#04605F嗯～也行。\x02\x03",

            "#04602F嘿嘿，看看你的本事吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA5E():
        OP_95(0xFE, 8590, 15200, -7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA5E)
    Sleep(50)

    def lambda_BA7B():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_BA7B)
    WaitChrThread(0x101, 1)

    #C0510
    ChrTalk(
        0x101,
        (
            "#00002F玛丽，乖。\x01",
            "别害怕，到这里来。\x02",
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
        "#00005F啊……\x02",
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

    def lambda_BC39():
        OP_95(0xFE, 13800, 15200, -8010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BC39)
    Sleep(1000)

    def lambda_BC56():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC56)
    Sleep(50)

    def lambda_BC66():

        label("loc_BC66")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_BC66")

    QueueWorkItem2(0x1A3, 1, lambda_BC66)
    Sleep(1000)

    def lambda_BC7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_BC7B)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x1)
    EndChrThread(0x1A3, 0x1)

    #C0512
    ChrTalk(
        0x1A3,
        "#04605F哇……！？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#00006F大、大意了……\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x1A3,
        (
            "#04609F哈哈哈，我也大意了。\x02\x03",

            "#04606F唔……看来还是\x01",
            "修行不足啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 1770, 15200, -7960, 90)
    SetChrPos(0x15, 1770, 15200, -9370, 90)
    OP_68(6830, 16850, -8570, 4000)
    MoveCamera(46, 28, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(16250, 4000)

    def lambda_BD62():
        OP_95(0xFE, 6590, 15200, -7960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BD62)
    Sleep(50)

    def lambda_BD7F():
        OP_95(0xFE, 6590, 15200, -9370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BD7F)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    #C0515
    ChrTalk(
        0x15,
        (
            "#6P#10300F呀，好像打扰到\x01",
            "你们了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x14,
        (
            "#6P#00106F抱歉，\x01",
            "似乎是我们坏了事……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BDF3():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDF3)
    Sleep(50)

    def lambda_BE03():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_BE03)
    Sleep(300)

    #C0517
    ChrTalk(
        0x101,
        (
            "#00004F哪里，是我太大意了。\x02\x03",

            "#00000F总之，赶快追吧。\x02\x03",

            "保险起见，艾莉和瓦吉从另一边\x01",
            "绕向入口大厅。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x14,
        "#6P#00100F嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x1A3,
        (
            "#04609F呵呵，那就赶快\x01",
            "追吧！\x02",
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

    # Function_37_B873 end

    def Function_38_BEFA(): pass

    label("Function_38_BEFA")


    def lambda_BEFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BEFF)

    def lambda_BF10():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF10)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 10260, 15200, -7100, 2000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_38_BEFA end

    def Function_39_BF45(): pass

    label("Function_39_BF45")


    def lambda_BF4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_BF4A)

    def lambda_BF5B():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_BF5B)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 10260, 15200, -9100, 2000, 0x0)
    OP_93(0x1A3, 0x10E, 0x1F4)
    Return()

    # Function_39_BF45 end

    def Function_40_BF90(): pass

    label("Function_40_BF90")


    def lambda_BF95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_BF95)

    def lambda_BFA6():
        OP_95(0xFE, -8770, 15200, -8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BFA6)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x5A, 0x1F4)
    Return()

    # Function_40_BF90 end

    def Function_41_BFC7(): pass

    label("Function_41_BFC7")


    def lambda_BFCC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_BFCC)

    def lambda_BFDD():
        OP_95(0xFE, -11190, 15200, -8100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_BFDD)
    WaitChrThread(0x15, 1)
    OP_95(0x15, -10100, 15200, -9070, 2000, 0x0)
    OP_93(0x15, 0x5A, 0x1F4)
    Return()

    # Function_41_BFC7 end

    def Function_42_C012(): pass

    label("Function_42_C012")

    EventBegin(0x1)

    #C0520
    ChrTalk(
        0x101,
        (
            "#00000F赶快去追玛丽吧，\x01",
            "它现在应该还在附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x1A3,
        (
            "#04609F呵呵，这次可不能\x01",
            "让它再逃走了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -11130, 15200, -7980, 90)
    EventEnd(0x4)
    Return()

    # Function_42_C012 end

    def Function_43_C086(): pass

    label("Function_43_C086")

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

    def lambda_C24C():
        OP_95(0xFE, 110, 1250, 20620, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C24C)
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

    def lambda_C362():
        OP_98(0xFE, 0x0, 0x2710, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C362)
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
        "#00011F#10A什么……！\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #C0523
    ChrTalk(
        0x9,
        (
            "#06205F#23A不好！舞台装置……！\x02\x03",

            "#20A但究竟是谁……！？\x02",
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
        "#11P#04611F#19A哼哼，小意思！\x02",
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
        "#12P#00005F哎……！\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x9,
        "#12P#06205F好、好厉害……！\x02",
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

    def lambda_C75F():
        OP_98(0xFE, 0x0, 0x1770, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C75F)

    #C0527
    ChrTalk(
        0x13,
        "#6P喵～喵……！\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x1A3,
        (
            "#11P#04606F好啦，不是\x01",
            "要把你抓来吃掉。\x02\x03",

            "不用害怕的。\x02\x03",

            "#04602F嘿，这样如何¤\x02",
        )
    )

    CloseMessageWindow()

    #A0529
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "谢莉挠了挠\x01",
            "玛丽的脖子。\x07\x00\x02",
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
        "#6P喵、喵～\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x1A3,
        (
            "#11P#04609F呵呵，感觉不错吧？\x02\x03",

            "#04600F那……接下来要这样⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0532
    ChrTalk(
        0x13,
        "#6P喵噢！\x02",
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
        "#6P（舒服）……喵喵⊥\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x1A3,
        "#11P#04609F啊哈哈，平静下来了吧？\x02",
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
        "#12P#00000F哈哈，干得真出色啊。\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x9,
        (
            "#12P#06204F嗯，而且她的身手轻盈得\x01",
            "让人难以相信。\x02",
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
            "#12P#06205F对了，到底是谁操作了装置，\x01",
            "必须要确认一下……\x02",
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
            "#11P#04600F好，那我们\x01",
            "要一起下去了。\x02\x03",

            "不许再闹了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x13,
        "#6P喵～¤\x02",
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
        "#11P#04605F什么，怎么突然……啊。\x02",
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

    def lambda_CBEA():
        OP_9D(0xFE, 0x212, 0x2328, 0x4268, 0x7D0, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CBEA)
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
        "#00011F不好……！\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x9,
        "#06201F……呜………！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 47)
    Sleep(500)
    OP_68(3370, 4570, 23550, 800)
    MoveCamera(48, 23, 0, 800)
    OP_6E(500, 800)
    SetCameraDistance(20670, 800)
    Sound(834, 0, 50, 0)

    def lambda_CD3D():
        OP_9D(0xFE, 0x6D6, 0x1F40, 0x4A38, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_CD3D)
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
        "#04605F哇，接得漂亮！\x02",
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
            "#00000F呼……总算是\x01",
            "有惊无险啊。\x02",
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

    # Function_43_C086 end

    def Function_44_CE7C(): pass

    label("Function_44_CE7C")


    def lambda_CE81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE81)

    def lambda_CE92():
        OP_95(0xFE, 0, 2250, 2940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE92)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_CE7C end

    def Function_45_CEAC(): pass

    label("Function_45_CEAC")


    def lambda_CEB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_CEB1)

    def lambda_CEC2():
        OP_95(0xFE, 0, 1800, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_CEC2)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_45_CEAC end

    def Function_46_CEDC(): pass

    label("Function_46_CEDC")


    def lambda_CEE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CEE1)

    def lambda_CEF2():
        OP_95(0xFE, 0, 1350, 7460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CEF2)
    WaitChrThread(0x9, 1)
    Return()

    # Function_46_CEDC end

    def Function_47_CF0C(): pass

    label("Function_47_CF0C")

    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    Sound(250, 0, 60, 0)
    OP_9D(0x9, 0x0, 0x4E2, 0x4BFA, 0xBB8, 0x1388)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x1, 4)
    Sound(637, 0, 100, 0)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x9, 0, 0, 48)

    def lambda_CF4F():
        OP_9D(0xFE, 0x1086, 0x4E2, 0x517C, 0x1388, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CF4F)
    OP_A1(0x9, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0x9, 1)
    Sound(326, 0, 50, 0)
    Return()

    # Function_47_CF0C end

    def Function_48_CF7B(): pass

    label("Function_48_CF7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_CF97")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_48_CF7B")

    label("loc_CF97")

    Return()

    # Function_48_CF7B end

    def Function_49_CF98(): pass

    label("Function_49_CF98")

    SetChrPos(0xA, 0, 1250, 25500, 270)

    label("loc_CFA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D37D")
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_CFDA():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CFDA)
    Sound(809, 0, 30, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    Sound(50, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)

    def lambda_D015():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D015)
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

    def lambda_D09B():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D09B)
    Sleep(250)

    def lambda_D0B9():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D0B9)
    Sleep(250)

    def lambda_D0D7():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D0D7)
    Sleep(250)

    def lambda_D0F5():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D0F5)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 54)
    Sleep(1000)

    def lambda_D127():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D127)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)

    def lambda_D18D():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D18D)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(50, 0, 50, 0)

    def lambda_D1CC():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D1CC)
    BeginChrThread(0xA, 1, 0, 51)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_D208():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D208)
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

    def lambda_D31E():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D31E)
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
    Jump("loc_CFA9")

    label("loc_D37D")

    Return()

    # Function_49_CF98 end

    def Function_50_D37E(): pass

    label("Function_50_D37E")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_50_D37E end

    def Function_51_D3A2(): pass

    label("Function_51_D3A2")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_51_D3A2 end

    def Function_52_D3C6(): pass

    label("Function_52_D3C6")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_D3C6 end

    def Function_53_D3DB(): pass

    label("Function_53_D3DB")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_D3DB end

    def Function_54_D3E9(): pass

    label("Function_54_D3E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D407")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_54_D3E9")

    label("loc_D407")

    Return()

    # Function_54_D3E9 end

    def Function_55_D408(): pass

    label("Function_55_D408")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D426")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_55_D408")

    label("loc_D426")

    Return()

    # Function_55_D408 end

    def Function_56_D427(): pass

    label("Function_56_D427")

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
            "#00000F看起来真是\x01",
            "相当努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        "#00100F嗯，正如经理所说。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x103,
        (
            "#00200F该怎么说呢，\x01",
            "真的好震撼。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x104,
        (
            "#00300F是在练习新增加的\x01",
            "场面吧？\x02\x03",

            "#00304F记得她要扮演一个\x01",
            "非常重要的角色……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x109,
        (
            "#10100F嗯，是『星之舞姬』。\x02\x03",

            "据说在舞剧的后半部分\x01",
            "会相当抢眼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x105,
        "#10300F呵呵，难怪会动力十足啊。\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#00003F嗯，不过要承受的压力\x01",
            "想必也很惊人……\x02\x03",

            "#00000F我们还是赶快离开，\x01",
            "不要打扰她为好。\x02",
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
        "#12205F啊……是你们！\x02",
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
        "#00005F啊……\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x103,
        "#00200F被发现了呢。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x104,
        (
            "#00300F算了，难得过来，\x01",
            "就去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D86B():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D86B)
    Sleep(50)

    def lambda_D888():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D888)
    Sleep(50)

    def lambda_D8A5():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D8A5)
    Sleep(50)

    def lambda_D8C2():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D8C2)
    Sleep(50)

    def lambda_D8DF():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D8DF)
    Sleep(50)

    def lambda_D8FC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D8FC)
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
            "#00000F哟，修利，\x01",
            "在你练习时过来，真是打扰了。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xA,
        (
            "#12203F哼、哼，也没有……\x02\x03",

            "#12200F对了，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#00100F没有，只是刚巧路过，\x01",
            "就顺便进来看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        "#00000F嗯，打断了你的练习，真是抱歉。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xA,
        (
            "#12206F没什么，我正好\x01",
            "也可以休息一下，\x01",
            "不必介意。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x103,
        (
            "#00203F说起来，我还是第一次\x01",
            "见到修利的表演……\x02\x03",

            "#00202F感觉你已经有了相当的造诣，\x01",
            "完全不像是个新人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0562
    ChrTalk(
        0xA,
        "#12205F是、是吗……？\x02",
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x102,
        (
            "#00102F嗯，真的，\x01",
            "老实说，我真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00004F是啊，该怎么说呢，\x01",
            "好像完全没有多余的动作。\x02\x03",

            "#00002F已经接近\x01",
            "完美了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xA,
        "#12205F哎……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    #C0566
    ChrTalk(
        0x109,
        (
            "#10109F嗯嗯，而且这套服装\x01",
            "也非常适合你呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0567
    ChrTalk(
        0x109,
        "#10105F……修利？\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    def lambda_DD05():

        label("loc_DD05")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_DD05")

    QueueWorkItem2(0x102, 0, lambda_DD05)

    def lambda_DD17():

        label("loc_DD17")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_DD17")

    QueueWorkItem2(0x103, 0, lambda_DD17)
    OP_99(0xA, 0x101, 0x3E8, 0x7D0, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)

    #C0568
    ChrTalk(
        0xA,
        (
            "#12203F……喂，就是你。\x02\x03",

            "#12200F如果可以，能不能\x01",
            "稍微陪我练习一下？\x02\x03",

            "#12208F而且，那个……\x01",
            "我还有点事情想问你。\x02",
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
            "#00105F让罗伊德陪修利\x01",
            "练习吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        (
            "#00005F为、为什么是我呢？\x01",
            "而且，要问的事情是……\x02\x03",

            "#00003F直说好了，\x01",
            "我可是个对表演\x01",
            "一窍不通的外行人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xA,
        (
            "#12203F并、并不是要你\x01",
            "做什么复杂的事情。\x02\x03",

            "#12208F而且我……\x01",
            "有些自己的打算。\x02\x03",

            "#12200F……如何？\x01",
            "可以陪我练习吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x101,
        "#00003F这、这个嘛……\x02",
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_56_D427 end

    def Function_57_DF77(): pass

    label("Function_57_DF77")

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
            "陪修利练习\x01",      # 0
            "放弃\x01",            # 1
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
        (0, "loc_DFD7"),
        (1, "loc_E0A8"),
        (SWITCH_DEFAULT, "loc_E227"),
    )


    label("loc_DFD7")


    #C0573
    ChrTalk(
        0x101,
        (
            "#00000F嗯，如果我可以，那当然没问题。\x02\x03",

            "不过我真的帮不上什么大忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xA,
        "#12200F嗯……我知道。\x02",
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
            "任务【秘密的演技指导】\x07\x00",
            "开始！\x02",
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
    Jump("loc_E227")

    label("loc_E0A8")


    #C0576
    ChrTalk(
        0x101,
        (
            "#00006F……抱歉，\x01",
            "现在还有其它的事情要做，\x01",
            "实在是腾不出时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xA,
        (
            "#12206F是吗，那就算了。\x01",
            "……把我刚才说的话忘掉吧。\x02\x03",

            "#12208F好了，我要继续练习了。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x101,
        "#00000F啊……嗯嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0579
    ChrTalk(
        0x102,
        (
            "#00100F（喂，罗伊德。\x01",
            "  不如想办法匀出点时间吧？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0580
    ChrTalk(
        0x101,
        (
            "#00003F（说、说得也是啊……\x01",
            "  我再考虑一下吧。）\x02",
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
    Jump("loc_E227")

    label("loc_E227")

    Return()

    # Function_57_DF77 end

    def Function_58_E228(): pass

    label("Function_58_E228")

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
            "#12205F怎么了，你们不是\x01",
            "还有事要办吗？\x02\x03",

            "#12200F莫非……\x01",
            "要陪我练习吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_58_E228 end

    SaveToFile()

Try(main)
