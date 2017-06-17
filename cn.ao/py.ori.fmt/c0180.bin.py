from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0180.bin",                # FileName
        "c0180",                    # MapName
        "c0180",                    # Location
        0x0005,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0180",                  # 0
        "珍妮特",                 # 1
        "尤金",                   # 2
        "缇奥多尔",               # 3
        "琪露露",                 # 4
        "柯洛娜",                 # 5
        "利玛",                   # 6
        "梅尔斯",                 # 7
        "游客",                   # 8
        "游客",                   # 9
        "市民",                   # 10
        "女孩",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "市民",                   # 14
        "市民",                   # 15
        "游客",                   # 16
        "游客",                   # 17
        "市民",                   # 18
        "市民",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "市民",                   # 22
        "男孩",                   # 23
        "游客",                   # 24
        "多诺邦警督",             # 25
        "市民",                   # 26
        "市民",                   # 27
        "市民",                   # 28
        "市民",                   # 29
        "隆",                     # 30
        "亨利",                   # 31
        "小桃",                   # 32
        "秦",                     # 33
        "黑月",                   # 34
        "小滴",                   # 35
        "琪雅",                   # 36
        "蔡特",                   # 37
        "曹",                     # 38
        "雷克特",                 # 39
        "绳索",                   # 40
        "埃尔赛尤号",             # 41
        "SE控制",                 # 42
    ))

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch28700.itc",                   # 01
        "chr/ch28800.itc",                   # 02
        "chr/ch22700.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch26200.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch33100.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch20100.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch22000.itc",                   # 0B
        "chr/ch34300.itc",                   # 0C
        "chr/ch24500.itc",                   # 0D
        "chr/ch22100.itc",                   # 0E
        "chr/ch33000.itc",                   # 0F
        "chr/ch33300.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch20000.itc",                   # 13
        "chr/ch20102.itc",                   # 14
        "chr/ch21102.itc",                   # 15
        "chr/ch21400.itc",                   # 16
        "chr/ch33202.itc",                   # 17
        "chr/ch48800.itc",                   # 18
        "chr/ch30300.itc",                   # 19
        "chr/ch21100.itc",                   # 1A
    ))

    DeclNpc(11409,   -189,    -6550,   180,  385,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-9340,   -200,    -3940,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8640,   -200,    -3970,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-13640,  -200,    6610,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5690,   -200,    3660,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6690,   -200,    3660,    0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-7690,   -200,    3660,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-14550,  -200,    -4780,   270,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-15779,  -50,     -4780,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-15779,  -50,     -4780,   90,   389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-14550,  -200,    -4780,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-6719,   -200,    5000,    0,    389,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5590,   -200,    5000,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-7000,   -200,    -4280,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-7559,   -200,    -3000,   225,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-10659,  -200,    -2779,   135,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-10979,  -200,    -3910,   90,   389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-10619,  -200,    -1070,   0,    389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-9619,   -200,    -1070,   0,    389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-6719,   -200,    5000,    0,    389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5590,   -200,    5000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-15779,  -50,     -4780,   90,   389,  0x0, 0,   26,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-14550,  -200,    -5320,   270,  385,  0x0, 0,   22,  0,   0,   1,   0,   28,  255,  0)
    DeclNpc(-5519,   -200,    3869,    15,   389,  0x0, 0,   24,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(3809,    -200,    7099,    0,    389,  0x0, 0,   25,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1664, 0)                                       # 0

    ScpFunction((
        "Function_0_680",          # 00, 0
        "Function_1_730",          # 01, 1
        "Function_2_75B",          # 02, 2
        "Function_3_777",          # 03, 3
        "Function_4_A96",          # 04, 4
        "Function_5_D9B",          # 05, 5
        "Function_6_1138",         # 06, 6
        "Function_7_1212",         # 07, 7
        "Function_8_1277",         # 08, 8
        "Function_9_12ED",         # 09, 9
        "Function_10_134E",        # 0A, 10
        "Function_11_138C",        # 0B, 11
        "Function_12_13D9",        # 0C, 12
        "Function_13_19EF",        # 0D, 13
        "Function_14_1A32",        # 0E, 14
        "Function_15_1A7A",        # 0F, 15
        "Function_16_1ADF",        # 10, 16
        "Function_17_1B1D",        # 11, 17
        "Function_18_1B61",        # 12, 18
        "Function_19_1BBE",        # 13, 19
        "Function_20_1C29",        # 14, 20
        "Function_21_1C8F",        # 15, 21
        "Function_22_1D05",        # 16, 22
        "Function_23_1D54",        # 17, 23
        "Function_24_1DBB",        # 18, 24
        "Function_25_1E26",        # 19, 25
        "Function_26_1E9B",        # 1A, 26
        "Function_27_1EE9",        # 1B, 27
        "Function_28_2282",        # 1C, 28
        "Function_29_25AA",        # 1D, 29
        "Function_30_2680",        # 1E, 30
        "Function_31_2734",        # 1F, 31
        "Function_32_2AC5",        # 20, 32
        "Function_33_2B69",        # 21, 33
        "Function_34_2C66",        # 22, 34
        "Function_35_2C9E",        # 23, 35
        "Function_36_2CCA",        # 24, 36
        "Function_37_2D07",        # 25, 37
        "Function_38_2D38",        # 26, 38
        "Function_39_3690",        # 27, 39
        "Function_40_4AE0",        # 28, 40
        "Function_41_4BB6",        # 29, 41
        "Function_42_4C0B",        # 2A, 42
        "Function_43_4C60",        # 2B, 43
        "Function_44_4CB5",        # 2C, 44
        "Function_45_4D0A",        # 2D, 45
        "Function_46_4D54",        # 2E, 46
        "Function_47_5D95",        # 2F, 47
        "Function_48_5DD9",        # 30, 48
        "Function_49_5E1D",        # 31, 49
        "Function_50_5E61",        # 32, 50
        "Function_51_5EA5",        # 33, 51
        "Function_52_6BCA",        # 34, 52
        "Function_53_6C15",        # 35, 53
        "Function_54_6C60",        # 36, 54
        "Function_55_6CAB",        # 37, 55
        "Function_56_6CF6",        # 38, 56
        "Function_57_6D41",        # 39, 57
    ))


    def Function_0_680(): pass

    label("Function_0_680")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6B8"),
        (1, "loc_6C4"),
        (2, "loc_6D0"),
        (3, "loc_6DC"),
        (4, "loc_6E8"),
        (5, "loc_6F4"),
        (6, "loc_700"),
        (SWITCH_DEFAULT, "loc_70C"),
    )


    label("loc_6B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_6F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_700")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_70C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_718")

    label("loc_72F")

    Return()

    # Function_0_680 end

    def Function_1_730(): pass

    label("Function_1_730")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75A")
    OP_94(0xFE, 0xFFFFC4AA, 0xFFFFEFCA, 0xFFFFCD24, 0xFFFFE46C, 0x3E8)
    Sleep(300)
    Jump("Function_1_730")

    label("loc_75A")

    Return()

    # Function_1_730 end

    def Function_2_75B(): pass

    label("Function_2_75B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_776")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_75B")

    label("loc_776")

    Return()

    # Function_2_75B end

    def Function_3_777(): pass

    label("Function_3_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B7")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1D, -6820, -200, -3460, 105)
    SetChrPos(0x1E, -7510, -200, -4550, 105)
    BeginChrThread(0x1E, 0, 0, 0)
    Jump("loc_9E4")

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7C5")
    Jump("loc_9E4")

    label("loc_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7EE")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_817")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_840")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_853")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9E4")

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_87C")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8A5")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8D8")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x15)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_9E4")

    label("loc_8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8FF")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_9E4")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_966")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A8")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x14)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_9E4")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9BB")
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_9E4")

    label("loc_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x17)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)

    label("loc_9E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_9F8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 30)
    Jump("loc_A2F")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A0C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 31)
    Jump("loc_A2F")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_A20")
    ClearScenarioFlags(0x22, 2)
    Event(0, 38)
    Jump("loc_A2F")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_A2F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 33)

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A40")
    Event(0, 39)

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6D")
    Event(0, 51)
    Jump("loc_A95")

    label("loc_A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A95")
    Event(0, 46)

    label("loc_A95")

    Return()

    # Function_3_777 end

    def Function_4_A96(): pass

    label("Function_4_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B89")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x168, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x168, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF8")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x46, 0x1A4, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo00a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D35")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "heiyue", 0x0, 0x1)
    Jump("loc_D64")

    label("loc_D35")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "heiyue", 0x1, 0x1)

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D86")
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    Jump("loc_D9A")

    label("loc_D86")

    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)

    label("loc_D9A")

    Return()

    # Function_4_A96 end

    def Function_5_D9B(): pass

    label("Function_5_D9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_1134")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E53")

    #C0001
    ChrTalk(
        0xFE,
        (
            "呼，那天晚上的沙扎克先生\x01",
            "真是太帅了……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "他用那么真诚的目光望着我，\x01",
            "还说『我最了解你的优点』……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "呵呵呵，真是最美好的回忆啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA9")

    label("loc_E53")


    #C0004
    ChrTalk(
        0xFE,
        (
            "而且竟然\x01",
            "还把彩虹剧团的门票\x01",
            "当作礼物送我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "呵呵呵，我可真是个幸福的人啊。\x02",
    )

    CloseMessageWindow()

    label("loc_EA9")

    Jump("loc_1134")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EBC")
    Jump("loc_1134")

    label("loc_EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF8")

    #C0006
    ChrTalk(
        0xFE,
        (
            "唉～好羡慕帕尔小姐啊，\x01",
            "我也想要个出色又可靠的男朋友～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0007
    ChrTalk(
        0xFE,
        (
            "哎呀，不能分心不能分心……\x01",
            "我得专心给花儿们浇水才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "呵呵，对不起啦，\x01",
            "我马上就喂水给你们哟～\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#00305F（说、说话方式竟如对待婴儿一样……\x01",
            "　可以加很多分数啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        "#10106F（什、什么分数呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1023")

    label("loc_FF8")


    #C0011
    ChrTalk(
        0xFE,
        (
            "呵呵，对不起，\x01",
            "我马上就喂水给你们哟～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1023")

    Jump("loc_1134")

    label("loc_1028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1036")
    Jump("loc_1134")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CC")

    #C0012
    ChrTalk(
        0xFE,
        (
            "呼，这里的视野很棒，\x01",
            "真是个好地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "啊，我并不是\x01",
            "在偷懒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "是经理让我负责\x01",
            "给这些植物浇水的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xB4, 0x0)
    SetChrFlags(0xFE, 0x10)
    Jump("loc_1134")

    label("loc_10CC")


    #C0015
    ChrTalk(
        0xFE,
        (
            "呵呵，我现在就给你们浇水，\x01",
            "多喝一些，快快长大哟～\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00006F（说、说话方式为何像对待婴儿一样？）\x02",
    )

    CloseMessageWindow()

    label("loc_1134")

    TalkEnd(0xFE)
    Return()

    # Function_5_D9B end

    def Function_6_1138(): pass

    label("Function_6_1138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B7")

    #C0017
    ChrTalk(
        0xFE,
        (
            "最近，我每次旅行归来，\x01",
            "都会发现那座大楼渐渐接近竣工……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "原来帷幕之下是这个样子啊。\x01",
            "真厉害啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_120E")

    label("loc_11B7")


    #C0019
    ChrTalk(
        0xFE,
        (
            "好了，已经看过大楼啦……\x01",
            "差不多也该去下一个地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "至于家……就下次再回吧。\x02",
    )

    CloseMessageWindow()

    label("loc_120E")

    TalkEnd(0xFE)
    Return()

    # Function_6_1138 end

    def Function_7_1212(): pass

    label("Function_7_1212")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "哎呀～我们果然散发着\x01",
            "与众不同的气场啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "抱歉，缇奥多尔，\x01",
            "这回确实是我想得不够周全。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1212 end

    def Function_8_1277(): pass

    label("Function_8_1277")

    TalkBegin(0xFE)

    #C0023
    ChrTalk(
        0xFE,
        (
            "……呜，你之前还信誓旦旦地说：\x01",
            "『只要穿上练习服装就不会暴露身份了』。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "我竟然会相信你，真是个笨蛋啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1277 end

    def Function_9_12ED(): pass

    label("Function_9_12ED")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        (
            "我老公竟然参与建造了\x01",
            "那么宏伟的建筑物……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "呵呵，再没有比这\x01",
            "更让人自豪的事情了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_12ED end

    def Function_10_134E(): pass

    label("Function_10_134E")

    TalkBegin(0xFE)

    #C0027
    ChrTalk(
        0xFE,
        "哇～真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，爸爸果然\x01",
            "很了不起啊¤\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_134E end

    def Function_11_138C(): pass

    label("Function_11_138C")

    TalkBegin(0xFE)

    #C0029
    ChrTalk(
        0xFE,
        "利玛，你看。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "那栋大楼是爸爸\x01",
            "和同伴们齐心协力\x01",
            "建造起来的哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_138C end

    def Function_12_13D9(): pass

    label("Function_12_13D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D0")

    #C0031
    ChrTalk(
        0xFE,
        "意图袭击两国首脑的恐怖分子吗……？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "虽然不能过度\x01",
            "拘泥于这条情报，\x01",
            "但这倒是让我们做好了心理准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "总之，警备方面就\x01",
            "按照达德利赶在昨天之内\x01",
            "调整好的轮班表执行……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "另外，每个人都要\x01",
            "集中精神，全力以赴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_153F")

    label("loc_14D0")


    #C0035
    ChrTalk(
        0xFE,
        (
            "总之，警备方面就\x01",
            "按照达德利赶在昨天之内\x01",
            "调整好的轮班表执行……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "另外，每个人都要\x01",
            "集中精神，全力以赴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153F")

    Jump("loc_19EB")

    label("loc_1544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1860")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B7")

    #C0037
    ChrTalk(
        0xFE,
        (
            "哟，是你们啊。\x01",
            "听说你们也参与了\x01",
            "揭幕式的警备工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "近距离观察各国首脑，有何感想呢？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00000F嗯，真是压迫力十足。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00304F是啊，\x01",
            "这次真是亲身感受到了\x01",
            "所谓的气场。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "原来如此，看来你们切实感受\x01",
            "到了大人物的不同之处啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "不过，话说回来，\x01",
            "感受对方的气场\x01",
            "固然很重要……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "但在实际接触时，\x01",
            "绝不能被对方的气势所压倒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#00100F嗯，确实如此。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        (
            "#10106F我、我实在是\x01",
            "没什么自信呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "哈哈，毕竟在这方面，\x01",
            "经验也十分重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "总之，对你们而言，\x01",
            "这应该是一次很不错的体验。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "全靠赛尔盖那家伙\x01",
            "把你们硬塞进警备队伍，\x01",
            "你们应该好好感谢他哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00000F嗯，这是当然的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 3)
    Jump("loc_185B")

    label("loc_17B7")


    #C0050
    ChrTalk(
        0xFE,
        (
            "正如你们所感觉到的一样，\x01",
            "各国首脑那各不相同的\x01",
            "独特气场都是切实存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "不过，我真正想说的是，\x01",
            "在与那种大人物接触时，你们一定\x01",
            "不能被他们的强大气势所压倒。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185B")

    Jump("loc_19EB")

    label("loc_1860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1985")

    #C0052
    ChrTalk(
        0xFE,
        (
            "哟，是你们啊。\x01",
            "有什么异常情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00000F不，\x01",
            "并没有什么异常。\x02\x03",

            "警督，您就在这里指挥这一带的警备工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "嗯，我要负责和各界联络，\x01",
            "这个地方再合适不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "话说回来，这一带\x01",
            "目前并没有什么异常情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "你们就继续自由行动吧。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00100F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19EB")

    label("loc_1985")


    #C0058
    ChrTalk(
        0xFE,
        (
            "幸好各地的人流并没有\x01",
            "纪念庆典时那么多。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "不过明天要举办揭幕式，\x01",
            "应该不会再像今天这么轻松了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EB")

    TalkEnd(0xFE)
    Return()

    # Function_12_13D9 end

    def Function_13_19EF(): pass

    label("Function_13_19EF")

    TalkBegin(0xFE)

    #C0060
    ChrTalk(
        0xFE,
        (
            "没想到百货店的楼顶\x01",
            "居然开放了一个\x01",
            "这么好的观景地点啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_19EF end

    def Function_14_1A32(): pass

    label("Function_14_1A32")

    TalkBegin(0xFE)

    #C0061
    ChrTalk(
        0xFE,
        "啊……风吹得人好舒服啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "视野也很棒，\x01",
            "真是个好地方啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1A32 end

    def Function_15_1A7A(): pass

    label("Function_15_1A7A")

    TalkBegin(0xFE)

    #C0063
    ChrTalk(
        0xFE,
        (
            "说起来，我家的孩子对市外\x01",
            "几乎还一无所知呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "呵呵，下次就带她去\x01",
            "阿尔摩利卡村看看吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1A7A end

    def Function_16_1ADF(): pass

    label("Function_16_1ADF")

    TalkBegin(0xFE)

    #C0065
    ChrTalk(
        0xFE,
        (
            "哇，远方一片\x01",
            "绿色呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "那里也是克洛斯贝尔吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1ADF end

    def Function_17_1B1D(): pass

    label("Function_17_1B1D")

    TalkBegin(0xFE)

    #C0067
    ChrTalk(
        0xFE,
        (
            "幕布下面的大楼\x01",
            "到底是什么样的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        "真期待揭幕式啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1B1D end

    def Function_18_1B61(): pass

    label("Function_18_1B61")

    TalkBegin(0xFE)

    #C0069
    ChrTalk(
        0xFE,
        (
            "话说回来，要如何揭下\x01",
            "那么大的帷幕呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "总不可能让大家在楼底\x01",
            "把它扯下来吧……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1B61 end

    def Function_19_1BBE(): pass

    label("Function_19_1BBE")

    TalkBegin(0xFE)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0071
    ChrTalk(
        0xFE,
        "#4S呀！#3S\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "没想到竟然能在\x01",
            "这种地方遇到二位！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "请、请给我签名好吗！！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1BBE end

    def Function_20_1C29(): pass

    label("Function_20_1C29")

    TalkBegin(0xFE)
    TurnDirection(0x16, 0x15, 0)

    #C0074
    ChrTalk(
        0xFE,
        (
            "等、等一下啦，\x01",
            "你那么吵闹，\x01",
            "太给人家添麻烦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "而且是我先\x01",
            "索要签名的！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_1C29 end

    def Function_21_1C8F(): pass

    label("Function_21_1C8F")

    TalkBegin(0xFE)

    #C0076
    ChrTalk(
        0xFE,
        (
            "唔，这两个人比舞台上的形象\x01",
            "更加风度翩翩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "虽然有些不甘心，\x01",
            "但我总算明白妻子\x01",
            "为何会那么迷恋他们了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1C8F end

    def Function_22_1D05(): pass

    label("Function_22_1D05")

    TalkBegin(0xFE)

    #C0078
    ChrTalk(
        0xFE,
        (
            "啊啊，缇奥多尔先生\x01",
            "和尤金先生就在我的眼前……\x01",
            "我激动得快要昏倒了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1D05 end

    def Function_23_1D54(): pass

    label("Function_23_1D54")

    TalkBegin(0xFE)

    #C0079
    ChrTalk(
        0xFE,
        (
            "听说接下来才是\x01",
            "会议的重头戏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "我不大明白这些深奥的事情，\x01",
            "但希望市长他们能多多加油。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1D54 end

    def Function_24_1DBB(): pass

    label("Function_24_1DBB")

    TalkBegin(0xFE)

    #C0081
    ChrTalk(
        0xFE,
        (
            "如果在这里呐喊声援，\x01",
            "声音能否传到市长他们的耳中呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "加油加油！市长加油！\x01",
            "……我开玩笑的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1DBB end

    def Function_25_1E26(): pass

    label("Function_25_1E26")

    TalkBegin(0xFE)

    #C0083
    ChrTalk(
        0xFE,
        (
            "呼，无论看多少次，\x01",
            "我都忍不住为这大楼惊叹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "大家将它称为克洛斯贝尔的\x01",
            "新标志性建筑，真是恰如其分。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_1E26 end

    def Function_26_1E9B(): pass

    label("Function_26_1E9B")

    TalkBegin(0xFE)

    #C0085
    ChrTalk(
        0xFE,
        (
            "呵呵，如果能站在那座大楼的楼顶眺望，\x01",
            "一定能看到无比美丽的风景吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_1E9B end

    def Function_27_1EE9(): pass

    label("Function_27_1EE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F37")

    #C0086
    ChrTalk(
        0xFE,
        (
            "那棵巨大的树……\x01",
            "闪烁着蓝白的光芒，有种梦幻般的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_1F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F45")
    Jump("loc_227E")

    label("loc_1F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FE6")

    #C0087
    ChrTalk(
        0xFE,
        (
            "迪塔总统和亚里欧斯长官……\x01",
            "我们可以放心地把克洛斯贝尔\x01",
            "交给他们两人来管理。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "虽然也许会进入漫长的战争岁月，\x01",
            "但我们一定要努力争取独立成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2063")

    #C0089
    ChrTalk(
        0xFE,
        (
            "听说亚里欧斯先生\x01",
            "为了守卫兰花塔，\x01",
            "表现相当活跃。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "这座城市果然不能没有他，\x01",
            "我如今再次体会到了这一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_2063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_20E9")

    #C0091
    ChrTalk(
        0xFE,
        (
            "听说突然出现了武装集团……\x01",
            "为什么不能\x01",
            "防患于未然呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "如果警察和警备队\x01",
            "再不加把劲，\x01",
            "我们晚上就不能安心入睡了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_20E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20F7")
    Jump("loc_227E")

    label("loc_20F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2153")

    #C0093
    ChrTalk(
        0xFE,
        (
            "听说郊外发生了什么事故，\x01",
            "真让人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "已经出动了很多辆\x01",
            "急救车……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21DA")

    #C0095
    ChrTalk(
        0xFE,
        (
            "自从这里被开辟成休息区，\x01",
            "我总会不知不觉地\x01",
            "在百货店里待上很久。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "只要在这里吹吹风，\x01",
            "购物的疲劳就都会随之消散呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227E")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_227E")

    #C0097
    ChrTalk(
        0xFE,
        (
            "呵呵，我好像已经完全习惯\x01",
            "这种可以眺望到兰花塔的景色了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "再过十年、二十年，\x01",
            "街道的格局也许会有不少改变……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "但那座大楼的存在感\x01",
            "肯定是不变的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227E")

    TalkEnd(0xFE)
    Return()

    # Function_27_1EE9 end

    def Function_28_2282(): pass

    label("Function_28_2282")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22DD")

    #C0100
    ChrTalk(
        0xFE,
        (
            "那么巨大的树，\x01",
            "为何会飘浮在空中？\x01",
            "世上的确有很多难以解释的神秘现象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A6")

    label("loc_22DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22EB")
    Jump("loc_25A6")

    label("loc_22EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2359")

    #C0101
    ChrTalk(
        0xFE,
        (
            "听说亚里欧斯先生\x01",
            "从游击士变成了国防长官？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "虽然不是很明白，\x01",
            "但他应该已经天下无敌了吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A6")

    label("loc_2359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23B0")

    #C0103
    ChrTalk(
        0xFE,
        (
            "我是亚里欧斯·马克莱因……\x01",
            "是一名游击士！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "看招！砰砰砰砰砰砰！\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A6")

    label("loc_23B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_240D")

    #C0105
    ChrTalk(
        0xFE,
        (
            "据说现在玛因兹那边\x01",
            "的情况十分不妙。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "难道不能快点把那些坏蛋抓起来吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A6")

    label("loc_240D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_241B")
    Jump("loc_25A6")

    label("loc_241B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AB")

    #C0107
    ChrTalk(
        0xFE,
        (
            "急救车通过\x01",
            "的时候，\x01",
            "警笛声好像有些奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "原本应该是嘀嘟嘀嘟，\x01",
            "这次却是噼嘟噼嘟。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "那到底是怎么回事呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24F3")

    label("loc_24AB")


    #C0110
    ChrTalk(
        0xFE,
        (
            "急救车通过\x01",
            "的时候，\x01",
            "警笛声好像有些奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "那到底是怎么回事呢？\x02",
    )

    CloseMessageWindow()

    label("loc_24F3")

    Jump("loc_25A6")

    label("loc_24F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2568")

    #C0112
    ChrTalk(
        0xFE,
        (
            "我虽然很喜欢屋顶，\x01",
            "但这里什么都没有，未免也太空荡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "就不能设置几个\x01",
            "卖小吃的摊子吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A6")

    label("loc_2568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25A6")

    #C0114
    ChrTalk(
        0xFE,
        (
            "嘿嘿，今天的天气也很不错啊。\x01",
            "屋顶的空气真新鲜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A6")

    TalkEnd(0xFE)
    Return()

    # Function_28_2282 end

    def Function_29_25AA(): pass

    label("Function_29_25AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2609")

    #N0115
    NpcTalk(
        0xFE,
        "女孩",
        "今天的雨好像要到下午才能停。\x02",
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0xFE,
        "女孩",
        "呵呵，到时也许能看到彩虹呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_2609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_267C")

    #N0117
    NpcTalk(
        0xFE,
        "市民",
        (
            "呵呵，下雨时的城市为何能\x01",
            "如此触动我的心？\x02",
        )
    )

    CloseMessageWindow()

    #N0118
    NpcTalk(
        0xFE,
        "市民",
        (
            "这带有淡淡哀愁的感觉，\x01",
            "真是让人情不自已呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_267C")

    TalkEnd(0xFE)
    Return()

    # Function_29_25AA end

    def Function_30_2680(): pass

    label("Function_30_2680")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(9900, 2800, 25300, 0)
    MoveCamera(30, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23750, 0)
    OP_68(5550, 4800, 33000, 10000)
    MoveCamera(10, -5, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(21000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_2680 end

    def Function_31_2734(): pass

    label("Function_31_2734")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch20600.itc", 0x21)
    LoadChrToIndex("chr/ch22200.itc", 0x22)
    LoadChrToIndex("chr/ch45000.itc", 0x23)
    LoadChrToIndex("chr/ch47600.itc", 0x24)
    SoundLoad(835)
    SoundLoad(821)
    SetChrChipByIndex(0x2B, 0x1E)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2C, 0x20)
    SetChrSubChip(0x2C, 0x5)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x22)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x24)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrChipByIndex(0x23, 0x7)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x21, 0x8)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x24, 0xB)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0x19, 0xFF)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    BeginChrThread(0x2C, 3, 0, 0)
    SetChrPos(0x2B, -12800, -200, 6900, 225)
    SetChrPos(0x2A, -14000, -200, 6500, 135)
    SetChrPos(0x2C, -13000, -200, 4800, 0)
    SetChrPos(0x25, -10700, -200, 7100, 135)
    SetChrPos(0x26, -9500, -200, 7100, 225)
    SetChrPos(0x27, -10200, -200, 5900, 0)
    SetChrPos(0x28, -11900, -200, 4900, 135)
    SetChrPos(0x29, -11200, -200, 4100, 315)
    SetChrPos(0x23, -7200, -200, 4800, 0)
    SetChrPos(0x21, -5100, -200, 5600, 0)
    SetChrPos(0x24, -5000, -200, 4100, 0)
    SetChrPos(0x22, -3200, -200, 5000, 0)
    SetChrPos(0x8, -1800, -200, 4500, 0)
    SetChrPos(0xB, -5400, -200, 6800, 0)
    SetChrPos(0x19, -3000, -200, 6900, 0)
    SetChrPos(0x11, -8400, -200, 4900, 0)
    OP_68(-8000, 4800, 5500, 0)
    MoveCamera(12, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12500, 0)
    OP_68(-8000, 2500, 5500, 10000)
    MoveCamera(12, 5, 0, 10000)
    SetCameraDistance(12000, 10000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x2B, 3, 0, 32)
    BeginChrThread(0x2A, 3, 0, 32)
    BeginChrThread(0x25, 3, 0, 32)
    BeginChrThread(0x26, 3, 0, 32)
    BeginChrThread(0x27, 3, 0, 32)
    BeginChrThread(0x28, 3, 0, 32)
    BeginChrThread(0x23, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0x21, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x24, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0x22, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x8, 3, 0, 35)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 35)
    Sleep(8000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_2734 end

    def Function_32_2AC5(): pass

    label("Function_32_2AC5")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2AFD"),
        (1, "loc_2B05"),
        (2, "loc_2B0D"),
        (3, "loc_2B15"),
        (4, "loc_2B1D"),
        (5, "loc_2B25"),
        (6, "loc_2B2D"),
        (SWITCH_DEFAULT, "loc_2B35"),
    )


    label("loc_2AFD")

    Sleep(200)
    Jump("loc_2B3D")

    label("loc_2B05")

    Sleep(400)
    Jump("loc_2B3D")

    label("loc_2B0D")

    Sleep(600)
    Jump("loc_2B3D")

    label("loc_2B15")

    Sleep(800)
    Jump("loc_2B3D")

    label("loc_2B1D")

    Sleep(1000)
    Jump("loc_2B3D")

    label("loc_2B25")

    Sleep(1200)
    Jump("loc_2B3D")

    label("loc_2B2D")

    Sleep(1400)
    Jump("loc_2B3D")

    label("loc_2B35")

    Sleep(1600)
    Jump("loc_2B3D")

    label("loc_2B3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B68")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("loc_2B3D")

    label("loc_2B68")

    Return()

    # Function_32_2AC5 end

    def Function_33_2B69(): pass

    label("Function_33_2B69")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(496)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x2, 0x30)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    OP_FF(0x2, 0x15E, 0x15E, 0x15E)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x30, -30000, 10000, 50000, 135)
    OP_D5(0x30, 0x0, 0x20F58, 0x0, 0x0)
    BeginChrThread(0x30, 1, 0, 34)
    BeginChrThread(0x31, 1, 0, 37)
    OP_68(7750, 5200, 37650, 0)
    MoveCamera(30, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(45, -10, 0, 8000)
    SetCameraDistance(42500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    StopSound(496, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_2B69 end

    def Function_34_2C66(): pass

    label("Function_34_2C66")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -30000, 10000, 60000)
    OP_9F(0x1, 5000, 10000, 50000)
    OP_9F(0x1, 20000, 12000, 0)
    OP_9F(0x2, 0xFE, 14000, 0x7)
    Return()

    # Function_34_2C66 end

    def Function_35_2C9E(): pass

    label("Function_35_2C9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CC9")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(1000)
    Jump("Function_35_2C9E")

    label("loc_2CC9")

    Return()

    # Function_35_2C9E end

    def Function_36_2CCA(): pass

    label("Function_36_2CCA")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Return()

    # Function_36_2CCA end

    def Function_37_2D07(): pass

    label("Function_37_2D07")

    Sound(496, 2, 20, 0)
    Sleep(300)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F0, 0x32)
    Sleep(300)
    OP_25(0x1F0, 0x3C)
    Sleep(300)
    OP_25(0x1F0, 0x46)
    Sleep(300)
    OP_25(0x1F0, 0x50)
    Return()

    # Function_37_2D07 end

    def Function_38_2D38(): pass

    label("Function_38_2D38")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch20600.itc", 0x21)
    LoadChrToIndex("chr/ch22200.itc", 0x22)
    LoadChrToIndex("chr/ch45000.itc", 0x23)
    LoadChrToIndex("chr/ch47600.itc", 0x24)
    SoundLoad(851)
    SoundLoad(3603)
    SoundLoad(3604)
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2B, 0x1E)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -12800, -200, 6900, 0)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -14000, -200, 6500, 0)
    SetChrChipByIndex(0x2C, 0x20)
    SetChrSubChip(0x2C, 0x5)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -13000, -200, 4800, 0)
    BeginChrThread(0x2C, 3, 0, 0)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10700, -200, 7100, 0)
    SetChrChipByIndex(0x26, 0x22)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -9700, -200, 7100, 0)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -9900, -200, 5900, 0)
    SetChrChipByIndex(0x28, 0x23)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -11400, -200, 4900, 0)
    SetChrChipByIndex(0x29, 0x24)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -10900, -200, 4100, 0)
    SetChrChipByIndex(0x23, 0x7)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7200, -200, 4800, 0)
    SetChrChipByIndex(0x21, 0x8)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -5100, -200, 5600, 0)
    SetChrChipByIndex(0x24, 0xB)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -4800, -200, 4100, 0)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -3200, -200, 5000, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -1800, -200, 4500, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6400, -200, 6800, 0)
    OP_4B(0x19, 0xFF)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -3000, -200, 6900, 0)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -8900, -200, 4900, 0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x20, 0x80)
    VolumeBGM(0x5A, 0x3E8)
    OP_68(-7000, 4100, 10500, 0)
    MoveCamera(37, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    Sound(851, 2, 100, 0)
    OP_68(-7000, 1100, 10500, 5000)
    MoveCamera(37, 11, 0, 5000)
    FadeToBright(2000, 0)
    BeginChrThread(0x23, 3, 0, 35)
    BeginChrThread(0xB, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x21, 3, 0, 35)
    BeginChrThread(0x19, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x24, 3, 0, 35)
    BeginChrThread(0x22, 3, 0, 35)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 35)
    BeginChrThread(0x11, 3, 0, 35)
    OP_0D()
    OP_6F(0x79)

    #C0119
    ChrTalk(
        0x21,
        "#11P好、好厉害啊……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x23,
        (
            "#11P听说多亏有ＩＢＣ的支援，\x01",
            "那栋大楼才能顺利落成！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x22,
        (
            "#11P竟然能建起\x01",
            "那么漂亮的大楼……！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x24,
        (
            "#11P迪塔市长一出手，\x01",
            "果然不同凡响啊！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-10000, 700, 7000, 0)
    MoveCamera(37, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    OP_6F(0x79)
    BeginChrThread(0x25, 3, 0, 36)
    OP_63(0x25, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0123
    ChrTalk(
        0x25,
        "#11P#4S好、好棒啊！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x25, 3)
    TurnDirection(0x25, 0x26, 500)

    #C0124
    ChrTalk(
        0x25,
        (
            "#6P亨利！\x01",
            "我们去那里探险吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x25, 500)

    #C0125
    ChrTalk(
        0x26,
        "#11P肯、肯定又会挨骂的呀～！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x26,
        (
            "#11P呼……\x01",
            "不过我也理解你的心情。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_323A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_323A)
    Sleep(50)

    def lambda_324A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_324A)

    #C0127
    ChrTalk(
        0x27,
        "#11P……好、好棒啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3300")

    #C0128
    ChrTalk(
        0x28,
        (
            "#12P确、确实是座很惊人的大楼啊……\x01",
            "在卡尔瓦德是完全无法想象的！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x28,
        (
            "#12P唔，总算明白我们\x01",
            "为何会对这座城市如此执著了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3388")

    label("loc_3300")


    #N0130
    NpcTalk(
        0x28,
        "男孩",
        (
            "#12P确、确实是座很惊人的大楼啊……\x01",
            "在卡尔瓦德是完全无法想象的！\x02",
        )
    )

    CloseMessageWindow()

    #N0131
    NpcTalk(
        0x28,
        "男孩",
        (
            "#12P唔，总算明白我们\x01",
            "为何会对这座城市如此执著了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3388")

    OP_68(-13300, 700, 7000, 2000)
    OP_6F(0x79)

    #C0132
    ChrTalk(
        0x2A,
        (
            "#12P#06000F呵呵……\x01",
            "大家都好兴奋啊。\x02\x03",

            "#06002F琪雅，\x01",
            "那座大楼真有那么大吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x2B,
        "#11P#01105F#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(150)

    #C0134
    ChrTalk(
        0x2A,
        (
            "#5P#06005F琪雅……？\x01",
            "你在那里吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x2B, 0x2A, 500)

    #C0135
    ChrTalk(
        0x2B,
        (
            "#11P#01109F啊──抱歉哦，小滴。\x02\x03",

            "#01110F那个……真的非常大哦！\x02\x03",

            "颜色是蓝白相间的，很漂亮，\x01",
            "笔直笔直地高耸入云，超级帅气！\x02\x03",

            "#01108F#30W……可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x2A,
        "#5P#06008F嗯？你怎么了？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x2B,
        (
            "#11P#01102F啊……\x01",
            "不，没什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10460, 6100, 24340, 4000)
    MoveCamera(17, -5, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(15820, 4000)
    OP_93(0x2B, 0x0, 0x12C)
    OP_6F(0x79)
    SetChrFlags(0x2B, 0x4)
    SetChrPos(0x2B, -15500, 1200, -2900, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0138
    ChrTalk(
        0x2B,
        (
            "#01106F#3603V#40W#12P#N（这是为什么呢……\x01",
            "  明明是第一次见到……）\x02\x03",

            "#01112F#3604V#30W（可我却觉得……\x01",
            "  好像曾在什么地方见过那座大楼。）\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE14)
    OP_C9(0x1, 0x80000000)
    StopSound(851, 2000, 100)
    SetCameraDistance(15320, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0x64)
    Sleep(100)
    OP_24(0x353)
    Sleep(1000)
    SetScenarioFlags(0x22, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_2D38 end

    def Function_39_3690(): pass

    label("Function_39_3690")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("apl/ch50237.itc", 0x1F)
    SetChrPos(0x101, 12000, 0, 1000, 180)
    SetChrPos(0x102, 12000, 0, 1000, 180)
    SetChrPos(0x103, 12000, 0, 1000, 180)
    SetChrPos(0x109, 12000, 0, 1000, 180)
    SetChrPos(0x105, 12000, 0, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2D, 0x1E)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, -12000, -200, 6900, 0)
    OP_68(11250, 1000, -2300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    SetCameraDistance(14500, 4000)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 43)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 44)
    WaitChrThread(0x105, 3)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(-12000, 1000, 6900, 3000)
    MoveCamera(33, 16, 0, 3000)
    SetCameraDistance(12500, 3000)
    OP_6F(0x79)
    Sleep(300)

    #C0139
    ChrTalk(
        0x2D,
        (
            "#03204F#11P呵呵……\x01",
            "各位能这么快赶来，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-12000, 900, 5400, 3000)
    MoveCamera(37, 19, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(14000, 3000)
    SetChrPos(0x101, -4000, -200, -1000, 270)
    SetChrPos(0x102, -4000, -200, -1000, 270)
    SetChrPos(0x103, -4000, -200, -1500, 270)
    SetChrPos(0x109, -4000, -200, -1000, 270)
    SetChrPos(0x105, -4000, -200, -1500, 270)

    def lambda_391A():
        OP_95(0xFE, -12600, -200, 3900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_391A)
    Sleep(300)

    def lambda_3937():
        OP_95(0xFE, -12200, -200, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3937)
    Sleep(600)

    def lambda_3954():
        OP_95(0xFE, -11500, -200, 3700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3954)
    Sleep(600)

    def lambda_3971():
        OP_95(0xFE, -10200, -200, 3800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3971)
    Sleep(300)

    def lambda_398E():
        OP_95(0xFE, -10200, -200, 2800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_398E)
    WaitChrThread(0x101, 1)

    def lambda_39AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39AC)
    WaitChrThread(0x103, 1)

    def lambda_39BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_39BD)
    WaitChrThread(0x102, 1)

    def lambda_39CE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_39CE)
    WaitChrThread(0x109, 1)

    def lambda_39DF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_39DF)
    WaitChrThread(0x105, 1)

    def lambda_39F0():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_39F0)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0140
    ChrTalk(
        0x101,
        (
            "#12P#00001F曹先生……\x01",
            "您独自一人不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#00105F#12P平时一直待在您身边的那位护卫……\x01",
            "记得是刘先生吧？他怎么不在呢？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    OP_93(0x2D, 0xB4, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0142
    AnonymousTalk(
        0x2D,
        (
            "呵呵，最近稍微有些忙，\x01",
            "我给他安排了很多任务。\x02\x03",

            "而且，那些危险的家伙\x01",
            "已经离开这座城市了。\x02\x03",

            "所以我也可以无所顾忌地\x01",
            "走在蓝天之下了。\x02",
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

    #C0143
    ChrTalk(
        0x103,
        (
            "#12P#00211F……还是和以前一样\x01",
            "阴阳怪气。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#12P#10302F『黑月』的年轻精英干部\x01",
            "和蓝天实在是很不相称啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x2D,
        (
            "#5P#03209F哈哈，这倒也是。\x02\x03",

            "#03200F好了，我们双方都没有多余的时间，\x01",
            "还是赶快进入正题吧。\x02\x03",

            "#03206F其实，我昨晚突然\x01",
            "接到了『银』大人的联络。\x02\x03",

            "说是要中断与黑月\x01",
            "签订的长期契约。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0x109,
        "#10108F啊……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#00108F#12P这……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x2D,
        (
            "#5P#03201F哎，我实在是大吃一惊呢。\x02\x03",

            "本想设法让『银』大人回心转意，\x01",
            "但其似乎相当坚决……\x02\x03",

            "#03206F实在让我一筹莫展。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#12P#00003F……是吗……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#12P#00200F那和我们\x01",
            "有什么关系呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x2D,
        (
            "#5P#03202F昨天在艾鲁姆湖的南岸，\x01",
            "究竟发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x109,
        "#10101F莫非……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#12P#10301F你已经掌握到我们\x01",
            "当时在一起的消息了？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x2D,
        (
            "#5P#03204F嗯，而且还了解到\x01",
            "游击士协会的成员\x01",
            "和『蛇』的人也出现了。\x02\x03",

            "#03201F『银』大人当时\x01",
            "到底经历了什么事情呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#00103F#12P……我认为并没有\x01",
            "义务告诉您……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x2D,
        (
            "#5P#03202F也就是说，银小姐\x01",
            "果然遇到了某些问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        "#00110F#12P……唔！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0159
    ChrTalk(
        0x101,
        (
            "#6P#00006F……别和他说太多，艾莉，\x01",
            "对手绝非寻常之辈。\x02\x03",

            "#00011F如果口无遮拦，会把情报——啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x105,
        (
            "#12P#10306F哎呀呀，\x01",
            "你还真阴险呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x2D,
        (
            "#5P#03209F呵呵，『银』大人\x01",
            "果然是女性啊。\x02\x03",

            "#03210F她恐怕是用超强的内功\x01",
            "使语调和体型\x01",
            "发生了变化吧？\x02\x03",

            "#03204F拥有如此惊人的身体能力，\x01",
            "难怪可以在舞台上活跃表现啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2D, 500)

    #C0162
    ChrTalk(
        0x101,
        "#12P#00010F唔……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        "#12P#00201F……………………………\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x2D,
        (
            "#5P#03204F我一直都很在意这个问题，\x01",
            "因此调查了彩虹剧团\x01",
            "成员的行程安排表。\x02\x03",

            "#03210F结果发现『银』大人\x01",
            "拒绝任务的时机与\x01",
            "公演等活动的日期完全一致。\x02\x03",

            "哎呀呀，多亏各位的协助，\x01",
            "总算是彻底证实了这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#12P#00006F……………………………\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#00101F#12P……您想对她\x01",
            "做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x2D,
        (
            "#5P#03205F暂时并没有什么想法。\x02\x03",

            "#03209F呼，如果知道她真实身份的人\x01",
            "只有我，倒是可以采取\x01",
            "威胁之类的手段……\x02\x03",

            "#03202F但既然连协会的人也牵扯在其中，\x01",
            "终究不能在这里\x01",
            "将你们灭口。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0168
    ChrTalk(
        0x109,
        "#10110F……！\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        "#12P#10306F这玩笑可真不好笑……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#12P#00003F……我们的时间很紧张，如果您要\x01",
            "说的只有这些，我们就先失陪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x2D,
        (
            "#5P#03204F哈哈，别这么说嘛。\x02\x03",

            "#03210F作为接受刚才那条情报的回礼，\x01",
            "我便告诉你们一个值得一听的情报吧。\x02\x03",

            "大约在三个小时之前……\x01",
            "兰迪先生曾出现在\x01",
            "玛因兹山道的某个地点。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0172
    ChrTalk(
        0x101,
        "#12P#00011F#4S！？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#12P#00205F真、真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x2D,
        (
            "#5P#03204F我们有专门负责监视\x01",
            "『赤色星座』动向的监视班。\x02\x03",

            "#03200F那条消息正是他们发来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x105,
        "#12P#10301F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        "#00107F#12P那……具体地点是哪里呢？\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x2D,
        (
            "#5P#03203F山道的瀑布前，克洛斯贝尔警备队\x01",
            "已经在附近架起了防线……\x02\x03",

            "#03201F据说兰迪先生由附近的高台\x01",
            "顺着绳索前往崖底了。\x02\x03",

            "不过继续追下去的话很有可能会被发现，\x01",
            "我们的人就放弃了跟踪。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0178
    ChrTalk(
        0x102,
        "#00101F#11P罗伊德……！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#12P#00004F嗯，再没有比这更好的情报了。\x02\x03",

            "#00000F曹先生，\x01",
            "感谢您提供情报……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4767():
        TurnDirection(0xFE, 0x2D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4767)

    #C0180
    ChrTalk(
        0x2D,
        (
            "#5P#03200F呵呵，你们尽量努力，\x01",
            "对我们是有利无害的。\x02\x03",

            "#03204F总之就多加小心吧，\x01",
            "你们和兰迪先生都不要死哦。\x02\x03",

            "#03210F『他们』可是很强的。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#12P#00003F……明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x258)
    Sleep(150)

    #C0182
    ChrTalk(
        0x101,
        (
            "#5P#00007F好，用艾尼格玛与科长联络，\x01",
            "然后立刻前往玛因兹山道！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_486A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_486A)
    Sleep(50)

    def lambda_487A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_487A)
    Sleep(50)

    def lambda_488A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_488A)
    Sleep(50)

    def lambda_489A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_489A)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0183
    ChrTalk(
        0x103,
        "#12P#00201F是……！\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x109,
        "#10107F明白！\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#00107F#11P无论如何也要追到他……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_4914():

        label("loc_4914")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4914")

    QueueWorkItem2(0x2D, 2, lambda_4914)
    OP_68(-7000, 900, 3400, 4000)
    SetCameraDistance(15500, 4000)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 45)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 45)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 45)
    Sleep(4000)
    EndChrThread(0x2D, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(-12000, 1000, 6900, 0)
    MoveCamera(33, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_63(0x2D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x2D)
    OP_93(0x2D, 0xB4, 0x1F4)
    Sleep(150)
    SetChrChipByIndex(0x2D, 0x1F)
    SetChrSubChip(0x2D, 0x0)
    Sleep(90)
    SetChrSubChip(0x2D, 0x1)
    Sleep(90)
    SetChrSubChip(0x2D, 0x2)
    Sleep(90)
    Sound(318, 0, 60, 0)
    SetChrSubChip(0x2D, 0x3)
    Sleep(200)

    #C0186
    ChrTalk(
        0x2D,
        (
            "#03204F#5P哈哈……热血冲动的年轻人\x01",
            "有时也挺让人喜欢呢。\x02\x03",

            "#03200F好……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2D, 0x2)
    Sleep(90)
    SetChrSubChip(0x2D, 0x1)
    Sleep(90)
    SetChrSubChip(0x2D, 0x0)
    Sleep(90)
    SetChrChipByIndex(0x2D, 0x1E)
    SetChrSubChip(0x2D, 0x0)
    Sleep(200)
    SetCameraDistance(12000, 1000)
    OP_93(0x2D, 0x0, 0x15E)
    OP_6F(0x79)

    #C0187
    ChrTalk(
        0x2D,
        (
            "#03203F#11P接下来才是重头戏。\x02\x03",

            "#03202F看来我们也有必要\x01",
            "拿出全力了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x166, 2)
    OP_29(0xAA, 0x1, 0x5)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    NewScene("c0100", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_39_3690 end

    def Function_40_4AE0(): pass

    label("Function_40_4AE0")


    def lambda_4AE5():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AE5)

    def lambda_4AFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AFF)
    WaitChrThread(0xFE, 1)

    def lambda_4B14():
        OP_95(0xFE, 10500, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B14)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(100)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Return()

    # Function_40_4AE0 end

    def Function_41_4BB6(): pass

    label("Function_41_4BB6")


    def lambda_4BBB():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BBB)

    def lambda_4BD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BD5)
    WaitChrThread(0xFE, 1)

    def lambda_4BEA():
        OP_95(0xFE, 12000, -200, -3400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BEA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_41_4BB6 end

    def Function_42_4C0B(): pass

    label("Function_42_4C0B")


    def lambda_4C10():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C10)

    def lambda_4C2A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C2A)
    WaitChrThread(0xFE, 1)

    def lambda_4C3F():
        OP_95(0xFE, 10500, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C3F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_4C0B end

    def Function_43_4C60(): pass

    label("Function_43_4C60")


    def lambda_4C65():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C65)

    def lambda_4C7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C7F)
    WaitChrThread(0xFE, 1)

    def lambda_4C94():
        OP_95(0xFE, 12000, -200, -2300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C94)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_43_4C60 end

    def Function_44_4CB5(): pass

    label("Function_44_4CB5")


    def lambda_4CBA():
        OP_95(0xFE, 12000, -200, -500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CBA)

    def lambda_4CD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4CD4)
    WaitChrThread(0xFE, 1)

    def lambda_4CE9():
        OP_95(0xFE, 11800, -200, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CE9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_44_4CB5 end

    def Function_45_4D0A(): pass

    label("Function_45_4D0A")

    OP_92(0xFE, 0x1388, 0xFFFFF830, 0x1F4)

    def lambda_4D1C():
        OP_95(0xFE, 5000, -200, -2000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D1C)
    WaitChrThread(0xFE, 1)

    def lambda_4D3A():
        OP_95(0xFE, 10000, -200, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D3A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_4D0A end

    def Function_46_4D54(): pass

    label("Function_46_4D54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03500.itp")
    SetChrChipByIndex(0x2E, 0x1E)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -2960, -200, 7150, 15)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0x2F)
    SetChrPos(0x2F, -17280, -200, 6420, 90)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    Fade(1000)
    OP_68(-2900, 780, 7160, 0)
    MoveCamera(57, 18, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(8260, 0)
    SetCameraDistance(10260, 3000)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(1000)
    OP_68(5540, 2800, -6730, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7220, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 49)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x105, 3)

    def lambda_4F54():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F54)
    Sleep(50)

    def lambda_4F64():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F64)
    Sleep(50)

    def lambda_4F74():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F74)
    Sleep(50)

    def lambda_4F84():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F84)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x101,
        "#11P#00005F啊……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x102,
        "#12P#00101F在那里……\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    Fade(1000)
    OP_68(-19590, 20100, 22530, 0)
    MoveCamera(27, 2, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(1530, 0)
    OP_0D()
    OP_68(-13810, 9200, 12250, 9000)
    MoveCamera(27, 2, 0, 9000)
    OP_6E(780, 9000)
    SetCameraDistance(37930, 9000)
    OP_6F(0x1)
    Sleep(800)
    OP_68(1610, 2500, 790, 5000)
    MoveCamera(350, -3, 0, 5000)
    OP_6E(780, 5000)
    SetCameraDistance(5910, 5000)
    OP_6F(0x1)
    Sleep(1000)

    #C0190
    ChrTalk(
        0x2E,
        (
            "#03506F呼～\x02\x03",

            "#03510F……话说回来，克洛斯贝尔\x01",
            "这个地方真是让人搞不懂啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-1640, 1400, 4800, 0)
    MoveCamera(7, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12380, 0)
    SetCameraDistance(10380, 3000)
    SetChrPos(0x101, -3960, -200, 1110, 15)
    SetChrPos(0x102, -2460, -200, 1110, 15)
    SetChrPos(0x109, -3460, -200, 110, 15)
    SetChrPos(0x105, -1960, -200, 110, 15)

    def lambda_51A7():
        OP_98(0x101, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51A7)
    Sleep(50)

    def lambda_51C4():
        OP_98(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51C4)
    Sleep(50)

    def lambda_51E1():
        OP_98(0x109, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51E1)
    Sleep(50)

    def lambda_51FE():
        OP_98(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51FE)
    Sleep(50)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0191
    ChrTalk(
        0x101,
        (
            "#6P#00001F……我明白\x01",
            "你想说什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        (
            "#12P#00103F那座建筑是『兰花塔』。\x02\x03",

            "高度为２５０亚矩，共四十层，\x01",
            "是目前整个大陆最高的超高层摩天大楼。\x02\x03",

            "#00100F大楼内除了新市政厅之外，\x01",
            "还有出租给企业的楼层及国际会议场等。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x109,
        (
            "#6P#10103F的确让人震撼呢……\x02\x03",

            "#10100F在这么远的距离下遥望，\x01",
            "却仍然显得如此巨大。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，现在还盖着帷幕，\x01",
            "不知具体外观如何……\x02\x03",

            "#10302F不过应该已经完全竣工了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，半数市政府的职员\x01",
            "都已经搬到那里了。\x02\x03",

            "#00004F不过好像要到通商会议开始时，\x01",
            "才会将大楼正式公开……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x2E,
        (
            "#6P#03500F看来是想让参加会议的\x01",
            "首脑们大吃一惊吧。\x02\x03",

            "#03506F哎呀呀，\x01",
            "迪塔·库罗伊斯真是个\x01",
            "比想象中更加厉害的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#6P#00003F………………………………\x02\x03",

            "#00001F我们要站在克洛斯贝尔警察局·\x01",
            "特别任务支援科的立场上问你几个问题。\x02\x03",

            "雷克特·亚兰德尔先生，\x01",
            "我们希望确认你的身份，还请多加配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x2E,
        (
            "#6P#03504F唔唔……\x02\x03",

            "#03500F好严肃啊，\x01",
            "如果我拒绝呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#12P#00103F……克洛斯贝尔的法律\x01",
            "对帝国、共和国的政府人员\x01",
            "的确没有约束力。\x02\x03",

            "#00101F不过，前提是对方已经\x01",
            "表明了自己的身份。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#12P#10303F原来如此，如果对方\x01",
            "没有表明自己的身份，我们就可以像\x01",
            "对待普通外国人一样行使调查权……\x02\x03",

            "#10300F就是这个意思吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x2E,
        "#6P#03504F唔，来这招吗。\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0xB4, 0x1F4)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0202
    AnonymousTalk(
        0x2E,
        (
            "……没办法，\x01",
            "那我也只好乖乖就范了。\x02\x03",

            "听好哦，我的身份就是──\x02",
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
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x2E, 0x2D, 0x1F4)

    #C0203
    ChrTalk(
        0x2E,
        "#6P#03505F嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_579C():
        OP_93(0x101, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_579C)
    Sleep(50)

    def lambda_57AC():
        OP_93(0x102, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57AC)
    Sleep(50)

    def lambda_57BC():
        OP_93(0x109, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57BC)
    Sleep(50)

    def lambda_57CC():
        OP_93(0x105, 0x2D, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57CC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5510, 2800, 17730, 0)
    MoveCamera(32, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)

    #C0204
    ChrTalk(
        0x101,
        "#N#00005F怎么了？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0205
    ChrTalk(
        0x2E,
        (
            "#N#03505F哦，对面那座建筑上……\x02\x03",

            "#03506F……好像有个黑色的人影\x01",
            "从屋顶一掠而过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0x101,
        "#N#00011F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0207
    ChrTalk(
        0x102,
        "#N#11P#00105F难、难道是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0208
    ChrTalk(
        0x105,
        (
            "#N#11P#10305F嘿，莫非是那个\x01",
            "叫做『银』的人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0209
    ChrTalk(
        0x109,
        (
            "#N#11P#10105F可、可是……\x01",
            "现在可是大白天啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrFlags(0x2E, 0x80)
    OP_0D()
    SetChrPos(0x101, 0, -200, 5110, 30)
    SetChrPos(0x102, 2000, -200, 5110, 30)
    SetChrPos(0x109, 1000, -200, 4110, 30)
    SetChrPos(0x105, 2500, -200, 4110, 30)
    Fade(500)
    OP_68(-5750, 2800, 3270, 0)
    MoveCamera(53, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5280, 0)
    OP_0D()
    OP_93(0x109, 0x10E, 0x3E8)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0210
    ChrTalk(
        0x109,
        "#10111F啊啊！？\x02",
    )

    CloseMessageWindow()

    def lambda_5A3D():
        OP_93(0x101, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A3D)
    Sleep(50)

    def lambda_5A4D():
        OP_93(0x102, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A4D)
    Sleep(50)

    def lambda_5A5D():
        OP_93(0x105, 0x10E, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A5D)

    #C0211
    ChrTalk(
        0x101,
        "#00011F不、不好！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5A9C():
        OP_95(0x101, -16360, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A9C)
    Sleep(100)

    def lambda_5AB9():
        OP_95(0x102, -16360, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5AB9)
    Sleep(50)

    def lambda_5AD6():
        OP_95(0x109, -15060, -200, 4810, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5AD6)
    Sleep(50)

    def lambda_5AF3():
        OP_95(0x105, -15060, -200, 6110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AF3)
    Sleep(50)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(500)
    OP_68(-20920, 2800, 4200, 0)
    MoveCamera(54, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5220, 0)
    SetChrPos(0x101, -11360, -200, 4810, 270)
    SetChrPos(0x102, -11360, -200, 6110, 270)
    SetChrPos(0x109, -10060, -200, 4810, 270)
    SetChrPos(0x105, -10060, -200, 6110, 270)

    def lambda_5B98():
        OP_95(0x101, -16180, -200, 5770, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B98)
    Sleep(100)

    def lambda_5BB5():
        OP_95(0x102, -16149, -200, 6900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5BB5)
    Sleep(50)

    def lambda_5BD2():
        OP_95(0x109, -14800, -200, 5880, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5BD2)
    Sleep(50)

    def lambda_5BEF():
        OP_95(0x105, -15150, -200, 6830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BEF)
    WaitChrThread(0x102, 1)

    def lambda_5C0D():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C0D)
    WaitChrThread(0x105, 1)

    def lambda_5C1E():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C1E)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x102,
        (
            "#5P#00105F难、难道顺着\x01",
            "这条绳索下去了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x109,
        "#10106F这、这怎么可能……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x105,
        (
            "#10309F啊哈哈！\x01",
            "他的行动真让人难以置信！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00006F唔……竟然会有如此\x01",
            "不能以常理度之的对手……\x02\x03",

            "#00007F这下面是后巷！\x01",
            "我们赶快从楼梯下去！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("c0500", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_46_4D54 end

    def Function_47_5D95(): pass

    label("Function_47_5D95")


    def lambda_5D9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D9A)

    def lambda_5DAB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DAB)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 6830, -200, -3780, 2000, 0x0)
    Return()

    # Function_47_5D95 end

    def Function_48_5DD9(): pass

    label("Function_48_5DD9")


    def lambda_5DDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DDE)

    def lambda_5DEF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DEF)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 8000, -200, -4990, 2000, 0x0)
    Return()

    # Function_48_5DD9 end

    def Function_49_5E1D(): pass

    label("Function_49_5E1D")


    def lambda_5E22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5E22)

    def lambda_5E33():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E33)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 8850, -200, -3200, 2000, 0x0)
    Return()

    # Function_49_5E1D end

    def Function_50_5E61(): pass

    label("Function_50_5E61")


    def lambda_5E66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5E66)

    def lambda_5E77():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E77)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 9880, -200, -4810, 2000, 0x0)
    Return()

    # Function_50_5E61 end

    def Function_51_5EA5(): pass

    label("Function_51_5EA5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_68(11860, 1800, -3520, 0)
    MoveCamera(53, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10770, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5F71")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x104, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6068")

    label("loc_5F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5FEF")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x109, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6068")

    label("loc_5FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_6068")
    SetChrPos(0x1A2, 11990, -20, 570, 180)
    SetChrPos(0x102, 11990, -20, 570, 180)
    SetChrPos(0x101, 11990, -20, 570, 180)
    SetChrPos(0x105, 11990, -20, 570, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6068")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_60D3")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 55)
    Jump("loc_614E")

    label("loc_60D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6113")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 56)
    Jump("loc_614E")

    label("loc_6113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_614E")
    BeginChrThread(0x1A2, 3, 0, 52)
    Sleep(700)
    OP_68(15100, 1700, -6410, 5000)
    BeginChrThread(0x102, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 57)

    label("loc_614E")

    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    OP_6F(0x1)

    #C0216
    ChrTalk(
        0x1A2,
        (
            "#6P这里就是百货店的楼顶啊……\x01",
            "嘿，视野很不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，很棒吧？\x01",
            "在这里可以俯瞰到整个城市哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0218
    ChrTalk(
        0x1A2,
        "#5P嗯，比我想象中的还要好！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x10E, 0x1F4)
    Sleep(300)

    #C0219
    ChrTalk(
        0x1A2,
        "#11P对了，兰花塔……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6279")

    def lambda_6243():

        label("loc_6243")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6243")

    QueueWorkItem2(0x101, 1, lambda_6243)

    def lambda_6255():

        label("loc_6255")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6255")

    QueueWorkItem2(0x102, 1, lambda_6255)

    def lambda_6267():

        label("loc_6267")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6267")

    QueueWorkItem2(0x104, 1, lambda_6267)
    Jump("loc_62FC")

    label("loc_6279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_62BD")

    def lambda_6287():

        label("loc_6287")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6287")

    QueueWorkItem2(0x101, 1, lambda_6287)

    def lambda_6299():

        label("loc_6299")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_6299")

    QueueWorkItem2(0x102, 1, lambda_6299)

    def lambda_62AB():

        label("loc_62AB")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_62AB")

    QueueWorkItem2(0x109, 1, lambda_62AB)
    Jump("loc_62FC")

    label("loc_62BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_62FC")

    def lambda_62CB():

        label("loc_62CB")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_62CB")

    QueueWorkItem2(0x101, 1, lambda_62CB)

    def lambda_62DD():

        label("loc_62DD")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_62DD")

    QueueWorkItem2(0x102, 1, lambda_62DD)

    def lambda_62EF():

        label("loc_62EF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_62EF")

    QueueWorkItem2(0x105, 1, lambda_62EF)

    label("loc_62FC")


    def lambda_6301():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6301)
    Sleep(500)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6333")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    Jump("loc_636A")

    label("loc_6333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6351")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    Jump("loc_636A")

    label("loc_6351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_636A")
    EndChrThread(0x1A2, 0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x105, 0x1)

    label("loc_636A")

    Fade(500)
    OP_68(-8320, 2600, 1920, 0)
    MoveCamera(26, -1, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7370, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6460")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x104, -1960, -200, 110, 0)

    def lambda_63EF():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_63EF)
    Sleep(50)

    def lambda_640C():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_640C)
    Sleep(50)

    def lambda_6429():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6429)
    Sleep(50)

    def lambda_6446():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6446)
    Jump("loc_65E1")

    label("loc_6460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6523")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x109, -1960, -200, 110, 0)

    def lambda_64B2():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_64B2)
    Sleep(50)

    def lambda_64CF():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_64CF)
    Sleep(50)

    def lambda_64EC():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64EC)
    Sleep(50)

    def lambda_6509():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6509)
    Jump("loc_65E1")

    label("loc_6523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_65E1")
    SetChrPos(0x1A2, -3060, -200, 2110, 0)
    SetChrPos(0x102, -2460, -200, 1110, 0)
    SetChrPos(0x101, -3960, -200, 110, 0)
    SetChrPos(0x105, -1960, -200, 110, 0)

    def lambda_6575():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6575)
    Sleep(50)

    def lambda_6592():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6592)
    Sleep(50)

    def lambda_65AF():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65AF)
    Sleep(50)

    def lambda_65CC():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65CC)

    label("loc_65E1")

    OP_0D()
    WaitChrThread(0x101, 1)

    #C0220
    ChrTalk(
        0x1A2,
        "就是那个吗……！？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x1A2,
        (
            "虽然还被帷幕盖着，\x01",
            "但存在感真是相当强啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0222
    ChrTalk(
        0x1A2,
        (
            "#5P艾莉姐，再往前站一站，\x01",
            "到我旁边来吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        "#00109F呵呵，知道啦。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00006F呼，小心些，\x01",
            "别掉下去哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1620, -2300, 8900, 0)
    MoveCamera(48, 26, 2, 0)
    OP_6E(700, 0)
    SetCameraDistance(20270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_6731")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x104, -1960, -200, 3110, 0)
    Jump("loc_67D0")

    label("loc_6731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_6783")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x109, -1960, -200, 3110, 0)
    Jump("loc_67D0")

    label("loc_6783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_67D0")
    SetChrPos(0x1A2, -3160, -200, 6110, 180)
    SetChrPos(0x102, -2460, -200, 6110, 180)
    SetChrPos(0x101, -3960, -200, 3110, 0)
    SetChrPos(0x105, -1960, -200, 3110, 0)

    label("loc_67D0")

    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0225
    ChrTalk(
        0x101,
        (
            "#12P#00000F如何？在楼顶看到的风景\x01",
            "还让你满意吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x1A2,
        "嗯，十分满意呢。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1A2,
        (
            "你们的向导工作\x01",
            "也做得相当不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x1A2,
        (
            "该怎么说呢……\x01",
            "总之给我留下了很好的回忆。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#12P#00009F是吗，能让你满意，\x01",
            "真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0230
    ChrTalk(
        0x1A2,
        (
            "我预计在后天早上\x01",
            "返回卡尔瓦德。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x1A2,
        (
            "回去之后，\x01",
            "又要被那些大人整天围着，\x01",
            "日复一日地不停学习了。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x1A2,
        (
            "不过，这也是我这种\x01",
            "人上人的宿命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        "#11P#00105F秦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_69AB")

    #C0234
    ChrTalk(
        0x104,
        "#00303F……原来如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69F8")

    label("loc_69AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_69D4")

    #C0235
    ChrTalk(
        0x109,
        "#10103F……原来如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69F8")

    label("loc_69D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_69F8")

    #C0236
    ChrTalk(
        0x105,
        "#10303F……原来如此。\x02",
    )

    CloseMessageWindow()

    label("loc_69F8")


    #C0237
    ChrTalk(
        0x101,
        (
            "#12P#00000F顺便一问，\x01",
            "你会去主日学校上课吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    #C0238
    ChrTalk(
        0x1A2,
        (
            "嗯，为了增加见闻，\x01",
            "也会去那里学习的。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x1A2,
        (
            "不过大家都很害怕\x01",
            "我周围的那些大人，\x01",
            "从来不敢接近我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_6B1C")

    #C0240
    ChrTalk(
        0x1A2,
        (
            "那两个孩子是叫\x01",
            "琪雅和滴吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x1A2,
        (
            "能和那样的小孩子聊天，\x01",
            "对我来说真是新鲜又愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        "#12P#00000F哈哈，是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B33")

    label("loc_6B1C")


    #C0243
    ChrTalk(
        0x101,
        "#12P#00008F秦……\x02",
    )

    CloseMessageWindow()

    label("loc_6B33")


    #C0244
    ChrTalk(
        0x1A2,
        (
            "……嗯，好像说了些\x01",
            "无聊的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1A2,
        "总之，向导工作就到此为止。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1A2,
        "稍后送我回事务所吧。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#12P#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 4)
    SetScenarioFlags(0x22, 5)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_5EA5 end

    def Function_52_6BCA(): pass

    label("Function_52_6BCA")


    def lambda_6BCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_6BCF)

    def lambda_6BE0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_6BE0)
    WaitChrThread(0x1A2, 1)
    OP_95(0x1A2, 14590, -200, -3020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_52_6BCA end

    def Function_53_6C15(): pass

    label("Function_53_6C15")


    def lambda_6C1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C1A)

    def lambda_6C2B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C2B)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 13970, -200, -4930, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_53_6C15 end

    def Function_54_6C60(): pass

    label("Function_54_6C60")


    def lambda_6C65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C65)

    def lambda_6C76():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C76)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13740, -200, -1810, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_54_6C60 end

    def Function_55_6CAB(): pass

    label("Function_55_6CAB")


    def lambda_6CB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CB0)

    def lambda_6CC1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6CC1)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_55_6CAB end

    def Function_56_6CF6(): pass

    label("Function_56_6CF6")


    def lambda_6CFB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6CFB)

    def lambda_6D0C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D0C)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_56_6CF6 end

    def Function_57_6D41(): pass

    label("Function_57_6D41")


    def lambda_6D46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6D46)

    def lambda_6D57():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6D57)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 12230, -200, -1920, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_57_6D41 end

    SaveToFile()

Try(main)
