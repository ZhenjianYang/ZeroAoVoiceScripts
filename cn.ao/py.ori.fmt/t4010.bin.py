from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t4010.bin",                # FileName
        "t4010",                    # MapName
        "t4010",                    # Location
        0x0000,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 7, 0, 8],
    )

    BuildStringList((
        "t4010",                  # 0
        "玛布尔修女",             # 1
        "艾拉尔达大主教",         # 2
        "莉丝修女",               # 3
        "基纳斯祭司",             # 4
        "伦顿祭司",               # 5
        "哈缇娜修女",             # 6
        "贸易商摩尔吉奥",         # 7
        "久久修女",               # 8
        "雷缇",                   # 9
        "琪雅",                   # 10
        "隆",                     # 11
        "亨利",                   # 12
        "小桃",                   # 13
        "潘莎",                   # 14
        "塔米尔",                 # 15
        "哈米尔",                 # 16
        "库塔",                   # 17
        "尤格特",                 # 18
        "男孩",                   # 19
        "男孩",                   # 20
        "女孩",                   # 21
        "女孩",                   # 22
        "普鲁娜",                 # 23
        "利娜莉",                 # 24
        "布利克",                 # 25
        "青年",                   # 26
        "女孩",                   # 27
        "人偶",                   # 28
    ))

    AddCharChip((
        "chr/ch25500.itc",                   # 00
        "chr/ch26500.itc",                   # 01
        "chr/ch14000.itc",                   # 02
        "chr/ch23802.itc",                   # 03
        "chr/ch25400.itc",                   # 04
        "chr/ch25300.itc",                   # 05
        "chr/ch21802.itc",                   # 06
        "chr/ch22202.itc",                   # 07
        "chr/ch20602.itc",                   # 08
        "chr/ch20702.itc",                   # 09
        "chr/ch22302.itc",                   # 0A
        "chr/ch21402.itc",                   # 0B
        "chr/ch34202.itc",                   # 0C
        "chr/ch20602.itc",                   # 0D
        "chr/ch23802.itc",                   # 0E
        "chr/ch21502.itc",                   # 0F
        "chr/ch23902.itc",                   # 10
        "chr/ch20502.itc",                   # 11
        "chr/ch22102.itc",                   # 12
        "chr/ch20402.itc",                   # 13
        "chr/ch22802.itc",                   # 14
        "chr/ch21302.itc",                   # 15
        "chr/ch08202.itc",                   # 16
        "chr/ch20500.itc",                   # 17
        "chr/ch22100.itc",                   # 18
        "chr/ch26502.itc",                   # 19
        "chr/ch21800.itc",                   # 1A
        "chr/ch10300.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(150800,  200,     17500,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-209,    379,     23229,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-2960,   250,     20010,   180,  257,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(99300,   0,       5679,    225,  257,  0x0, 0,   5,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(2950,    189,     19709,   165,  257,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-3849,   150,     6519,    0,    325,  0x0, 0,   26,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       180,  385,  0x0, 0,   0,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(1059,    0,       11659,   0,    389,  0x0, 0,   27,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   22,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(153619,  150,     12229,   0,    453,  0x0, 0,   8,   0,   255, 255, 0,   29,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   7,   0,   255, 255, 0,   30,  255,  0)
    DeclNpc(154929,  150,     9130,    0,    453,  0x0, 0,   9,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    453,  0x0, 0,   10,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(148490,  150,     12229,   45,   453,  0x0, 0,   3,   0,   255, 255, 0,   33,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    453,  0x0, 0,   3,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    453,  0x0, 0,   11,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(147139,  150,     9130,    0,    453,  0x0, 0,   12,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   13,  0,   255, 255, 0,   37,  255,  0)
    DeclNpc(153619,  150,     6150,    0,    453,  0x0, 0,   14,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   15,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(148490,  150,     6150,    0,    453,  0x0, 0,   16,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(147139,  150,     12229,   0,    453,  0x0, 0,   23,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(148490,  150,     12229,   0,    453,  0x0, 0,   24,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(154929,  150,     12229,   0,    453,  0x0, 0,   19,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(148490,  150,     9130,    0,    453,  0x0, 0,   20,  0,   255, 255, 0,   45,  255,  0)
    DeclNpc(153619,  150,     9130,    0,    453,  0x0, 0,   21,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(150910,  200,     16530,   1200,    150800,  1700,    17500,   0x007E, 0,  22, 0x0000)
    DeclActor(40,      500,     21930,   1200,    -210,    2100,    23230,   0x007E, 0,  9,  0x0000)
    DeclActor(50280,   0,       12800,   1200,    50160,   1000,    13560,   0x007C, 0,  48, 0x0000)

    ChipFrameInfo(1392, 0)                                       # 0

    ScpFunction((
        "Function_0_570",          # 00, 0
        "Function_1_620",          # 01, 1
        "Function_2_64B",          # 02, 2
        "Function_3_676",          # 03, 3
        "Function_4_6A1",          # 04, 4
        "Function_5_6CC",          # 05, 5
        "Function_6_6F7",          # 06, 6
        "Function_7_848",          # 07, 7
        "Function_8_F0D",          # 08, 8
        "Function_9_1118",         # 09, 9
        "Function_10_111C",        # 0A, 10
        "Function_11_2742",        # 0B, 11
        "Function_12_2826",        # 0C, 12
        "Function_13_2B1F",        # 0D, 13
        "Function_14_2BF7",        # 0E, 14
        "Function_15_2D49",        # 0F, 15
        "Function_16_3CAB",        # 10, 16
        "Function_17_4C33",        # 11, 17
        "Function_18_5948",        # 12, 18
        "Function_19_6C31",        # 13, 19
        "Function_20_7500",        # 14, 20
        "Function_21_7835",        # 15, 21
        "Function_22_79C6",        # 16, 22
        "Function_23_79F5",        # 17, 23
        "Function_24_91FF",        # 18, 24
        "Function_25_96DE",        # 19, 25
        "Function_26_9832",        # 1A, 26
        "Function_27_9D87",        # 1B, 27
        "Function_28_9E61",        # 1C, 28
        "Function_29_9EDE",        # 1D, 29
        "Function_30_9FC5",        # 1E, 30
        "Function_31_A094",        # 1F, 31
        "Function_32_A18A",        # 20, 32
        "Function_33_A3E3",        # 21, 33
        "Function_34_A585",        # 22, 34
        "Function_35_A6F4",        # 23, 35
        "Function_36_A7B7",        # 24, 36
        "Function_37_A828",        # 25, 37
        "Function_38_A857",        # 26, 38
        "Function_39_A8B4",        # 27, 39
        "Function_40_A9B2",        # 28, 40
        "Function_41_AA18",        # 29, 41
        "Function_42_AAC6",        # 2A, 42
        "Function_43_ABB7",        # 2B, 43
        "Function_44_AC21",        # 2C, 44
        "Function_45_ACE6",        # 2D, 45
        "Function_46_AD2C",        # 2E, 46
        "Function_47_AE2F",        # 2F, 47
        "Function_48_B112",        # 30, 48
        "Function_49_B1A1",        # 31, 49
        "Function_50_B600",        # 32, 50
        "Function_51_B885",        # 33, 51
        "Function_52_CA18",        # 34, 52
        "Function_53_D202",        # 35, 53
        "Function_54_E655",        # 36, 54
        "Function_55_E83D",        # 37, 55
        "Function_56_EAF2",        # 38, 56
        "Function_57_F4A3",        # 39, 57
    ))


    def Function_0_570(): pass

    label("Function_0_570")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5A8"),
        (1, "loc_5B4"),
        (2, "loc_5C0"),
        (3, "loc_5CC"),
        (4, "loc_5D8"),
        (5, "loc_5E4"),
        (6, "loc_5F0"),
        (SWITCH_DEFAULT, "loc_5FC"),
    )


    label("loc_5A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_61F")

    Return()

    # Function_0_570 end

    def Function_1_620(): pass

    label("Function_1_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64A")
    OP_94(0xFE, 0x17A8E, 0x125C, 0x186A0, 0x1D4C, 0x3E8)
    Sleep(450)
    Jump("Function_1_620")

    label("loc_64A")

    Return()

    # Function_1_620 end

    def Function_2_64B(): pass

    label("Function_2_64B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_675")
    OP_94(0xFE, 0xFFFFF7F4, 0x1ACC, 0x8B6, 0x3D68, 0x3E8)
    Sleep(450)
    Jump("Function_2_64B")

    label("loc_675")

    Return()

    # Function_2_64B end

    def Function_3_676(): pass

    label("Function_3_676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A0")
    OP_94(0xFE, 0xBA5E, 0x319C, 0xCD46, 0xC44, 0x3E8)
    Sleep(450)
    Jump("Function_3_676")

    label("loc_6A0")

    Return()

    # Function_3_676 end

    def Function_4_6A1(): pass

    label("Function_4_6A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CB")
    OP_94(0xFE, 0xFFFFF7F4, 0x1ACC, 0x8B6, 0x3D68, 0x3E8)
    Sleep(450)
    Jump("Function_4_6A1")

    label("loc_6CB")

    Return()

    # Function_4_6A1 end

    def Function_5_6CC(): pass

    label("Function_5_6CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F6")
    OP_94(0xFE, 0x24A7C, 0x17DE, 0x25170, 0x34F8, 0x3E8)
    Sleep(450)
    Jump("Function_5_6CC")

    label("loc_6F6")

    Return()

    # Function_5_6CC end

    def Function_6_6F7(): pass

    label("Function_6_6F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_847")
    OP_95(0xFE, 48280, 0, 9200, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 5070, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 3530, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 1560, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 3530, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 5070, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 9200, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 48280, 0, 10730, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    Jump("Function_6_6F7")

    label("loc_847")

    Return()

    # Function_6_6F7 end

    def Function_7_848(): pass

    label("Function_7_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868")
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_876")
    Jump("loc_F0C")

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8A0")
    ClearChrFlags(0xE, 0x40)
    SetChrPos(0xE, 160, 0, 10850, 0)
    BeginChrThread(0xE, 0, 0, 4)
    Jump("loc_F0C")

    label("loc_8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_F0C")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -6960, 0, 20030, 135)

    label("loc_8DF")

    SetChrPos(0x8, 8480, 0, 19550, 225)
    SetChrPos(0x16, 5350, 150, 11500, 0)
    SetChrPos(0x17, 6400, 150, 11500, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x16, 0x3)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    Jump("loc_F0C")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_956")
    Jump("loc_F0C")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9A1")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 48280, 0, 10730, 180)
    BeginChrThread(0xF, 0, 0, 6)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 151520, 0, 9530, 0)
    BeginChrThread(0xA, 0, 0, 5)
    Jump("loc_F0C")

    label("loc_9A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9CB")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xC, 95850, 0, 8119, 270)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_F0C")

    label("loc_9CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EC")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9E7")
    SetChrFlags(0xE, 0x10)

    label("loc_9E7")

    Jump("loc_F0C")

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_AD0")
    SetChrPos(0x9, 100000, 150, 10600, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xC, 160, 0, 10850, 0)
    BeginChrThread(0xC, 0, 0, 4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xF, 153000, 200, 17650, 270)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69")
    SetChrFlags(0xF, 0x10)

    label("loc_A69")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrPos(0x1E, 155440, 0, 3630, 270)
    SetChrPos(0x1F, 153430, 0, 3820, 90)
    BeginChrThread(0x1E, 0, 0, 0)
    BeginChrThread(0x1F, 0, 0, 0)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    ClearChrFlags(0x1E, 0x40)
    ClearChrFlags(0x1F, 0x40)
    Jump("loc_F0C")

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_BAB")
    SetChrPos(0x9, 97640, 0, 12650, 0)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xC, 160, 0, 10850, 0)
    BeginChrThread(0xC, 0, 0, 4)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 153790, 200, 17470, 180)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x1E, 0x11)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x12)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x14)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    SetChrFlags(0x1E, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    Jump("loc_F0C")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CA0")
    SetChrPos(0xC, 49920, 0, 9850, 359)
    BeginChrThread(0xC, 0, 0, 3)
    SetChrPos(0x9, 97640, 0, 12650, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEB")
    SetChrFlags(0x9, 0x10)

    label("loc_BEB")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 150800, 200, 17500, 180)
    SetChrPos(0x8, 153790, 200, 17470, 180)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x18, 0xB)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrChipByIndex(0x19, 0xC)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrChipByIndex(0x1A, 0xD)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x1B, 0xE)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    SetChrChipByIndex(0x1C, 0xF)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    SetChrChipByIndex(0x1D, 0x10)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jump("loc_F0C")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CEB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CE6")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xA, 153000, 200, 17650, 270)

    label("loc_CE6")

    Jump("loc_F0C")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D25")
    SetChrPos(0xD, 2330, 500, 22880, 270)
    OP_93(0x9, 0x5A, 0x0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D20")
    SetChrFlags(0xD, 0x10)

    label("loc_D20")

    Jump("loc_F0C")

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D33")
    Jump("loc_F0C")

    label("loc_D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrPos(0xD, 2330, 500, 22880, 270)
    OP_93(0x9, 0x5A, 0x0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    SetChrFlags(0xD, 0x10)

    label("loc_D68")

    SetChrPos(0xB, 160, 0, 10850, 0)
    BeginChrThread(0xB, 0, 0, 4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -1000, 0, 7830, 270)
    BeginChrThread(0xF, 0, 0, 4)
    SetChrPos(0x8, 150800, 200, 17500, 90)
    SetChrPos(0xA, 153000, 200, 17650, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD1")
    SetChrFlags(0x8, 0x10)

    label("loc_DD1")

    SetChrFlags(0xA, 0x10)
    Jump("loc_F0C")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF3")
    SetChrFlags(0x9, 0x10)

    label("loc_DF3")

    Jump("loc_F0C")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_E55")
    SetChrPos(0x9, 100000, 150, 10610, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 100000, 0, 7200, 0)
    SetChrPos(0xC, 50430, 0, 4030, 0)
    BeginChrThread(0xC, 0, 0, 3)
    Jump("loc_F0C")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F0C")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0x8)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0x13, 0x7)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x9)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xA)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrChipByIndex(0x16, 0x3)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x17, 0x3)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F07")
    SetChrFlags(0x13, 0x10)

    label("loc_F07")

    SetChrFlags(0x14, 0x10)

    label("loc_F0C")

    Return()

    # Function_7_848 end

    def Function_8_F0D(): pass

    label("Function_8_F0D")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2F")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F3D")
    Jump("loc_1036")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F4B")
    Jump("loc_1036")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F59")
    Jump("loc_1036")

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F67")
    Jump("loc_1036")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F75")
    Jump("loc_1036")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F83")
    Jump("loc_1036")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F91")
    Jump("loc_1036")

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F9F")
    Jump("loc_1036")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_FB1")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_FC3")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FD5")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FE3")
    Jump("loc_1036")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FF1")
    Jump("loc_1036")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FFF")
    Jump("loc_1036")

    label("loc_FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_100D")
    Jump("loc_1036")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_101B")
    Jump("loc_1036")

    label("loc_101B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_102D")
    OP_65(0x1, 0x1)
    Jump("loc_1036")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1036")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1048")
    OP_65(0x0, 0x1)

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1064")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_107B")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_107B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10CD")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj_18", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj_27", 0x0, 0x1)
    Sound(128, 1, 50, 0)
    Jump("loc_10DE")

    label("loc_10CD")

    SetMapObjFrame(0xFF, "cloudwind", 0x0, 0x1)

    label("loc_10DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F1")
    OP_1B(0x2, 0x0, 0x33)

    label("loc_10F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1104")
    OP_1B(0x2, 0x0, 0x34)

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1117")
    OP_1B(0x4, 0x0, 0x35)

    label("loc_1117")

    Return()

    # Function_8_F0D end

    def Function_9_1118(): pass

    label("Function_9_1118")

    Call(0, 10)
    Return()

    # Function_9_1118 end

    def Function_10_111C(): pass

    label("Function_10_111C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_114A")
    Call(0, 12)
    Jump("loc_114D")

    label("loc_114A")

    Call(0, 11)

    label("loc_114D")

    Jump("loc_1332")

    label("loc_1152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B3")

    #C0001
    ChrTalk(
        0x9,
        (
            "出现在湿地的『大树』……\x01",
            "在七耀教会的任何圣典中\x01",
            "都未有记载。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "那恐怕并非世俗之人\x01",
            "所能撼动之物。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1288")

    #C0003
    ChrTalk(
        0x105,
        (
            "#10400F总之，接下来就\x01",
            "交给我们好了。\x02\x03",

            "#10404F将事态平息之后，\x01",
            "十分希望您以后能\x01",
            "对骑士团多加协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "……只要是为了克洛斯贝尔，\x01",
            "我会积极考虑的。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        "愿女神保佑你们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12AB")

    label("loc_1288")


    #C0006
    ChrTalk(
        0x9,
        (
            "……祝愿各位得到\x01",
            "女神的保佑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AB")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1332")

    label("loc_12B3")


    #C0007
    ChrTalk(
        0x9,
        (
            "在七耀教会的任何圣典中\x01",
            "都没有记载有关那棵『大树』的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "那恐怕并非世俗之人\x01",
            "所能撼动之物。\x01",
            "祝愿各位得到女神的保佑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1332")

    Jump("loc_273E")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_14C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1362")
    Call(0, 12)
    Jump("loc_1365")

    label("loc_1362")

    Call(0, 11)

    label("loc_1365")

    Jump("loc_14BE")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1446")

    #C0009
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔之所以会发生如此事态……\x01",
            "我始终拒绝『封圣省』的介入\x01",
            "或许也是原因之一吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "如果早些接受他们的协助，\x01",
            "事态也许就不会\x01",
            "发展到如此地步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "看来我也需要一些\x01",
            "冷静头脑，\x01",
            "自我检讨的时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14BE")

    label("loc_1446")


    #C0012
    ChrTalk(
        0x9,
        (
            "如果早些接受『封圣省』的协助，\x01",
            "事态也许就不会\x01",
            "发展到如此地步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "看来我也需要一些\x01",
            "冷静头脑，\x01",
            "自我检讨的时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BE")

    Jump("loc_273E")

    label("loc_14C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_166B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D8")

    #C0014
    ChrTalk(
        0x9,
        (
            "莉丝修女已经返回\x01",
            "亚尔特利亚的教会总部了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "……看来封圣省是要正式开始行动，\x01",
            "介入克洛斯贝尔的事态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔将要\x01",
            "进入动乱时代……\x01",
            "这或许就是其预兆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "我身为克洛斯贝尔地区的教区长，\x01",
            "似乎也必须要好好思考\x01",
            "今后的行动方针了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1666")

    label("loc_15D8")


    #C0018
    ChrTalk(
        0x9,
        (
            "封圣省也要正式开始行动了，\x01",
            "克洛斯贝尔将要\x01",
            "进入动乱时代……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "我身为克洛斯贝尔地区的教区长，\x01",
            "似乎也必须要好好思考\x01",
            "今后的行动方针了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1666")

    Jump("loc_273E")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1770")

    #C0020
    ChrTalk(
        0x9,
        (
            "……就在不久前，接到了\x01",
            "典礼省那边的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "据说法王已经亲自批准了\x01",
            "封圣省介入克洛斯贝尔的事态。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "毕竟刚刚发生过严重的袭击事件，\x01",
            "在如今的状况下，恐怕也没办法了……\x02",
        )
    )


    #C0023
    ChrTalk(
        0x9,
        (
            "但即使如此……\x01",
            "我也无法认同那些\x01",
            "从事着非法活动的家伙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17F8")

    label("loc_1770")


    #C0024
    ChrTalk(
        0x9,
        (
            "之前接到了情报，\x01",
            "据说法王已经亲自批准了\x01",
            "封圣省介入克洛斯贝尔的事态……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "但即使如此……\x01",
            "我也无法认同那些\x01",
            "从事着非法活动的家伙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F8")

    Jump("loc_273E")

    label("loc_17FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")

    #C0026
    ChrTalk(
        0x9,
        (
            "玛因兹山道的大量警备队员\x01",
            "正处在极度危险的状况下。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "伟大的空之女神啊，\x01",
            "请您保佑他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        "并击退那邪恶的势力吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18DD")

    label("loc_1896")


    #C0029
    ChrTalk(
        0x9,
        (
            "伟大的空之女神啊，\x01",
            "请您保佑他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        "并击退那邪恶的势力吧……\x02",
    )

    CloseMessageWindow()

    label("loc_18DD")

    Jump("loc_273E")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1979")

    #C0031
    ChrTalk(
        0x9,
        (
            "之前有游击士来询问过消息，\x01",
            "据说艾欧莉娅她们如今下落不明。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "很遗憾，她们并没有来过大圣堂。\x01",
            "嗯，但愿她们平安无事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19EF")

    label("loc_1979")


    #C0033
    ChrTalk(
        0x9,
        (
            "艾欧莉娅她们经常帮助我们\x01",
            "采集药物的材料，给祭司担当护卫，\x01",
            "实在是受到过她们的很多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "但愿她们平安无事……\x02",
    )

    CloseMessageWindow()

    label("loc_19EF")

    Jump("loc_273E")

    label("loc_19F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A89")

    #C0035
    ChrTalk(
        0x9,
        (
            "嗯……\x01",
            "下次举办弥撒的时间必须要提前才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "自从上次的教团事件之后，就事件不断……\x01",
            "要让市民们前来参加弥撒，\x01",
            "恢复平静的心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273E")

    label("loc_1A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2D")

    #C0037
    ChrTalk(
        0x9,
        (
            "……你们还在探查\x01",
            "昨天那个蓝花的事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "在这片广阔的大陆中，\x01",
            "存在着很多不该去\x01",
            "接触的领域。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        "……你们还是不要过度深究为好。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B98")

    label("loc_1B2D")


    #C0040
    ChrTalk(
        0x9,
        (
            "在这片广阔的大陆中，\x01",
            "存在着很多不该去\x01",
            "接触的领域。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "凡事不要过度深究，\x01",
            "希望你们将这句话牢记在心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B98")

    Jump("loc_273E")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_1DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFA")

    #C0042
    ChrTalk(
        0x9,
        (
            "关于此花，我没有任何话\x01",
            "可以对你们讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "至于教会中的其他人……\x01",
            "即使是玛布尔修女，\x01",
            "应该也不知晓它的存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "好了，请你们赶快回去吧。\x01",
            "我现在很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00003F（大主教果然不愿意\x01",
            "  告诉我们内情啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00100F（莉丝小姐似乎\x01",
            "  有话要对我们说……\x01",
            "  还是先去找她吧。）\x02\x03",

            "（她就在礼拜堂门口的\x01",
            "  宿舍内等着我们。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DA5")

    label("loc_1CFA")


    #C0047
    ChrTalk(
        0x9,
        (
            "关于此花，我没有任何话\x01",
            "可以对你们讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "好了，请你们赶快回去吧。\x01",
            "我现在很忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00000F（莉丝小姐就在礼拜堂门口的\x01",
            "  宿舍内等着我们……\x01",
            "  总之，先过去找她吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA5")

    Jump("loc_273E")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E46")

    #C0050
    ChrTalk(
        0x9,
        (
            "莉丝·亚尔珍特……\x01",
            "看来确实是她的妹妹。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "哼……那些家伙，\x01",
            "究竟有何企图……？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00003F（好像正在思考什么事情呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E6D")

    label("loc_1E46")


    #C0053
    ChrTalk(
        0x9,
        (
            "……那些家伙，\x01",
            "究竟有何企图……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6D")

    Jump("loc_273E")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F53")

    #C0054
    ChrTalk(
        0x9,
        (
            "通商会议的正式会议那天……\x01",
            "莉丝修女去玛因兹地区授课时，\x01",
            "耗费了相当久的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "而在玛因茨地区内，\x01",
            "存在着那个遗迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "……原来如此。\x01",
            "虽然不知她具体做了些什么……\x01",
            "但显然是这样没错。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F98")

    label("loc_1F53")


    #C0057
    ChrTalk(
        0x9,
        "……哦，有何贵干？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "我正在研究重要的事情，\x01",
            "请不要随意进来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F98")

    Jump("loc_273E")

    label("loc_1F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2211")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD9")
    Call(0, 57)
    Return()

    label("loc_1FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C3")

    #C0059
    ChrTalk(
        0x9,
        (
            "怪盗Ｂ……竟敢在这神圣的\x01",
            "克洛斯贝尔大圣堂内藏匿赃物。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "之前就听说过有关他的传闻，\x01",
            "如今看来，似乎是个十分恶劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "身为伟大女神的仆从，\x01",
            "我绝不能容许他的肆意妄为。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "各位，无论如何也请\x01",
            "抓捕到他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2126")

    label("loc_20C3")


    #C0063
    ChrTalk(
        0x9,
        (
            "怪盗Ｂ……\x01",
            "身为伟大女神的仆从，\x01",
            "我绝不能容许他的肆意妄为。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "各位，无论如何也请\x01",
            "抓捕到他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2126")

    TalkEnd(0x9)
    Return()

    label("loc_212A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B1")

    #C0065
    ChrTalk(
        0x9,
        (
            "科洛蒂娅王太女\x01",
            "刚才来这里拜访过……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "虽然年纪轻轻，\x01",
            "但思想非常成熟。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "利贝尔王国的未来\x01",
            "想必会充满光明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_220C")

    label("loc_21B1")


    #C0068
    ChrTalk(
        0x9,
        (
            "科洛蒂娅王太女\x01",
            "虽然年纪轻轻，\x01",
            "但思想非常成熟。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "利贝尔王国的未来\x01",
            "想必会充满光明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220C")

    Jump("loc_273E")

    label("loc_2211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_22B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222C")
    Call(0, 14)
    Jump("loc_22B0")

    label("loc_222C")

    OP_4B(0xD, 0xFF)

    #C0070
    ChrTalk(
        0x9,
        (
            "去玛因兹地区授课吗……\x01",
            "虽然有些在意，但暂且不管了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "如果有什么关于她的新情况，\x01",
            "就再来向我报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        "好、好的……\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_22B0")

    Jump("loc_273E")

    label("loc_22B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_241C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2382")

    #C0073
    ChrTalk(
        0x9,
        (
            "乌尔斯拉医院的拉格教授\x01",
            "寄来了信。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "信上说，他利用以前索要的\x01",
            "那种名为羽扇豆草的药草，\x01",
            "已经在研究中取得了成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "……虽然与我完全无关，\x01",
            "但这次就赞他一句『做得好』吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2417")

    label("loc_2382")


    #C0076
    ChrTalk(
        0x9,
        (
            "乌尔斯拉医院的拉格教授寄来了信，\x01",
            "信中说他利用以前索要的\x01",
            "羽扇豆草在研究中取得了成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "……虽然与我完全无关，\x01",
            "但这次就赞他一句『做得好』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2417")

    Jump("loc_273E")

    label("loc_241C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_24A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2437")
    Call(0, 13)
    Jump("loc_24A0")

    label("loc_2437")

    OP_4B(0xD, 0xFF)

    #C0078
    ChrTalk(
        0x9,
        (
            "莉丝·亚尔珍特吗……\x01",
            "算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "哈缇娜修女，\x01",
            "将工作内容仔细\x01",
            "教导给她。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xD,
        "嗯，交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)

    label("loc_24A0")

    Jump("loc_273E")

    label("loc_24A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A0")

    #C0081
    ChrTalk(
        0x9,
        (
            "……莉丝·亚尔珍特……\x01",
            "那个女孩是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0082
    ChrTalk(
        0x153,
        "#01111F大主教，怎么啦？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x105,
        (
            "#10300F莉丝就是刚才的\x01",
            "那位修女吧？\x02\x03",

            "#10304F呵呵，莫非有什么事情令您很在意吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0084
    ChrTalk(
        0x9,
        (
            "……没有什么，\x01",
            "请不必挂怀。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_262D")

    label("loc_25A0")


    #C0085
    ChrTalk(
        0x9,
        (
            "……莉丝·亚尔珍特……\x01",
            "那女孩是……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x153,
        (
            "#01100F要是肚子疼就说出来吧，\x01",
            "琪雅会帮你把急救箱拿来的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x153, 500)

    #C0087
    ChrTalk(
        0x9,
        (
            "唔、唔唔……\x01",
            "请不必在意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262D")

    Jump("loc_273E")

    label("loc_2632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2640")
    Jump("loc_273E")

    label("loc_2640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_273E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DD")

    #C0088
    ChrTalk(
        0x9,
        (
            "欢迎来到\x01",
            "克洛斯贝尔大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "只要怀着虔诚的心情祈祷，\x01",
            "空之女神爱德丝就一定会向你伸出援手。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        "愿你们得到女神的引导……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_273E")

    label("loc_26DD")


    #C0091
    ChrTalk(
        0x9,
        (
            "只要怀着虔诚的心情祈祷，\x01",
            "空之女神爱德丝就一定会向你伸出援手。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        "愿你们得到女神的引导……\x02",
    )

    CloseMessageWindow()

    label("loc_273E")

    TalkEnd(0x9)
    Return()

    # Function_10_111C end

    def Function_11_2742(): pass

    label("Function_11_2742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D4")

    #C0093
    ChrTalk(
        0x9,
        (
            "……没想到，竟然会\x01",
            "引起这种程度的事态……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "这恐怕是始终都抗拒\x01",
            "『他们』介入的我的责任……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2825")

    label("loc_27D4")


    #C0096
    ChrTalk(
        0x9,
        (
            "这恐怕是始终都抗拒\x01",
            "『他们』介入的我的责任……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2825")

    Return()

    # Function_11_2742 end

    def Function_12_2826(): pass

    label("Function_12_2826")

    TurnDirection(0x9, 0x105, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0098
    ChrTalk(
        0x9,
        "是你们……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        (
            "#10400F您好，艾拉尔达大主教。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "……原来如此。\x01",
            "瓦吉·赫米斯菲亚，\x01",
            "你果然是……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "利用莉丝修女\x01",
            "作为掩护，彻底\x01",
            "把我给骗了过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "……确实是『封圣省』的风格。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10404F呵呵，关于此事，\x01",
            "请容我向您正式道歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "……我始终顽固不化地拒绝你们介入，\x01",
            "或许也是造成如今这种状况\x01",
            "的原因之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "你应该斥责我才对，\x01",
            "并没有道歉的必要。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#00108F大主教……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        "#00306F还是这么严于律己啊。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        (
            "#10404F算啦，站在您的立场来考虑，\x01",
            "那种做法也是可以理解的。\x02\x03",

            "#10400F不过，对于我们今后的活动，\x01",
            "希望您稍微网开一面，\x01",
            "尽量睁一只眼闭一只眼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#00011F喂、喂，瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#00211F要求得也太露骨了。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "……我无法立刻答允你，\x01",
            "但我会好好考虑一下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "我也需要一些\x01",
            "冷静头脑，\x01",
            "自我检讨的时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 1)
    Return()

    # Function_12_2826 end

    def Function_13_2B1F(): pass

    label("Function_13_2B1F")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0113
    ChrTalk(
        0x9,
        (
            "……她似乎正在帮\x01",
            "玛布尔修女做事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        "莉丝修女吗？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xD,
        (
            "嗯，她很快\x01",
            "就掌握工作了……\x01",
            "真是帮了我们的大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        "嗯，是吗……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        "（……算了，先不管了。）\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_13_2B1F end

    def Function_14_2BF7(): pass

    label("Function_14_2BF7")

    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0118
    ChrTalk(
        0x9,
        (
            "唔……\x01",
            "安排了莉丝修女\x01",
            "明天外出授课？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        (
            "是的，她之前就有过\x01",
            "主日学校的外出授课经验。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xD,
        (
            "……那个，大主教，\x01",
            "莉丝修女究竟……？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "最近您似乎非常注意她，\x01",
            "一直询问有关她的情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "……不，没什么。\x01",
            "我只是有点关心\x01",
            "她的工作情况而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "如果有什么关于她的新情况，\x01",
            "就再来向我报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        "好、好的……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_14_2BF7 end

    def Function_15_2D49(): pass

    label("Function_15_2D49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDC")

    #C0125
    ChrTalk(
        0xFE,
        (
            "虽说已经将总统拘捕了，\x01",
            "但克洛斯贝尔如今的状况\x01",
            "仍然不容乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "此地再次燃起战火的日子\x01",
            "或许已经为期不远了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E2A")

    label("loc_2DDC")


    #C0127
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "再次燃起战火的日子\x01",
            "或许已经为期不远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "向女神祈祷吧……\x02",
    )

    CloseMessageWindow()

    label("loc_2E2A")

    Jump("loc_3CA7")

    label("loc_2E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF4")

    #C0129
    ChrTalk(
        0xFE,
        (
            "大主教似乎认为\x01",
            "自己应对如今这种事态\x01",
            "担负很大责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "他一向是个\x01",
            "对自己也非常严厉的人，\x01",
            "这也难怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "但正因如此，\x01",
            "我很希望他能像以往一样，\x01",
            "继续引导我们前进。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F5A")

    label("loc_2EF4")


    #C0132
    ChrTalk(
        0xFE,
        (
            "大主教似乎认为\x01",
            "自己应对如今这种事态\x01",
            "担负很大责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "但即使如此，\x01",
            "我们也愿意\x01",
            "继续追随大主教。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5A")

    Jump("loc_3CA7")

    label("loc_2F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3024")

    #C0134
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔宣布独立，\x01",
            "一定会对周边诸国\x01",
            "造成很大影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "特别是两大国，\x01",
            "今后肯定会继续施加\x01",
            "更强的压力……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "我们克洛斯贝尔的居民们\x01",
            "又能否顺利越过\x01",
            "这个难关呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_308C")

    label("loc_3024")


    #C0137
    ChrTalk(
        0xFE,
        (
            "两大国今后\x01",
            "肯定会继续施加\x01",
            "更强的压力……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "我们克洛斯贝尔的居民们\x01",
            "又能否顺利越过\x01",
            "这个难关呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308C")

    Jump("loc_3CA7")

    label("loc_3091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315A")

    #C0139
    ChrTalk(
        0xFE,
        (
            "在上次的袭击事件中，\x01",
            "有大量警备队员\x01",
            "与普通市民不幸遇难。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "究竟要怎么做，\x01",
            "才能避免这样的灾难\x01",
            "再次发生呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的每一个\x01",
            "居民都必须要思考\x01",
            "这个问题才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_31CA")

    label("loc_315A")


    #C0142
    ChrTalk(
        0xFE,
        (
            "究竟要怎么做，\x01",
            "才能避免这样的灾难\x01",
            "再次发生呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的每一个\x01",
            "居民都必须要思考\x01",
            "这个问题才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CA")

    Jump("loc_3CA7")

    label("loc_31CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3232")

    #C0144
    ChrTalk(
        0xFE,
        (
            "玛因兹的居民们\x01",
            "为何要遭此不幸啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "这样的行径……\x01",
            "女神是绝对\x01",
            "不会原谅的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_3232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32A6")

    #C0146
    ChrTalk(
        0xFE,
        (
            "据说昨天发生在西克洛斯贝尔街道\x01",
            "的脱轨事故非常惨烈。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "没有出现死难者，\x01",
            "总算是不幸中的大幸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_32A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_335D")

    #C0148
    ChrTalk(
        0xFE,
        (
            "无论在任何时候，始终都坚持正确的道路……\x01",
            "这可不是件容易的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教不仅只对他人要求严格，\x01",
            "也是个非常严于律己的人，\x01",
            "所以对我来说，是最值得尊敬的人物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_335D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33F4")

    #C0150
    ChrTalk(
        0xFE,
        (
            "大主教一直都非常严格地\x01",
            "遵守七耀教会的戒律。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "虽然在有些人看来，他过于顽固不化，\x01",
            "但我始终认为大主教的这种\x01",
            "原则是非常值得尊敬的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_33F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_345D")

    #C0152
    ChrTalk(
        0xFE,
        (
            "哦，你们已经和\x01",
            "大主教谈过了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "这么快就谈完了，\x01",
            "莫非发生什么不愉快了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_345D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_34DB")

    #C0154
    ChrTalk(
        0xFE,
        (
            "听说最近一段时间，在克洛斯贝尔各地\x01",
            "都有人目击到神秘的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "警备队已经下达了公告，\x01",
            "提醒大家多加注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_34DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_358A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356C")

    #C0156
    ChrTalk(
        0xFE,
        (
            "大主教在\x01",
            "办公室里。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "他好像正在\x01",
            "调查莉丝修女\x01",
            "最近的行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "大主教与莉丝修女之间……\x01",
            "难道有什么隐情吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3585")

    label("loc_356C")


    #C0159
    ChrTalk(
        0xFE,
        (
            "大主教在\x01",
            "办公室里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3585")

    Jump("loc_3CA7")

    label("loc_358A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3634")

    #C0160
    ChrTalk(
        0xFE,
        (
            "据说科洛蒂娅殿下\x01",
            "还精通剑技呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "听说她的剑术是尤莉亚准校亲授的，\x01",
            "实力相当了得呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "虽然这么说有点失礼，\x01",
            "不过还真是人不可貌相啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_368C")

    label("loc_3634")


    #C0163
    ChrTalk(
        0xFE,
        (
            "据说科洛蒂娅殿下\x01",
            "还精通剑技呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "虽然这么说有点失礼，\x01",
            "不过还真是人不可貌相啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368C")

    Jump("loc_3CA7")

    label("loc_3691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3743")

    #C0165
    ChrTalk(
        0xFE,
        (
            "我也很关注\x01",
            "通商会议的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "各国的首脑\x01",
            "均为著名的\x01",
            "有识之士……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "他们究竟会探讨出怎样的成果呢？\x01",
            "身为克洛斯贝尔的居民，\x01",
            "实在是不容错过啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37B2")

    label("loc_3743")


    #C0168
    ChrTalk(
        0xFE,
        (
            "我也很关注\x01",
            "通商会议的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "他们究竟会探讨出怎样的成果呢？\x01",
            "身为克洛斯贝尔的居民，\x01",
            "实在是不容错过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B2")

    Jump("loc_3CA7")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388D")

    #C0170
    ChrTalk(
        0xFE,
        (
            "大主教与拉格教授之间\x01",
            "有着很深的芥蒂……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "但他们的关系最近似乎稍微缓和了一些，\x01",
            "至少大主教已经肯读\x01",
            "拉格教授的信了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "和看都不看就直接扔掉的时候相比，\x01",
            "关系还真是\x01",
            "改善了不少呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E5")

    label("loc_388D")


    #C0173
    ChrTalk(
        0xFE,
        (
            "拉格教授原本也是\x01",
            "在大主教手下学习的祭司……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "但愿他们之间的隔阂\x01",
            "可以尽早消除。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E5")

    Jump("loc_3CA7")

    label("loc_38EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3965")

    #C0175
    ChrTalk(
        0xFE,
        (
            "今天手头没什么事情的人\x01",
            "都要给大圣堂做扫除。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "毕竟是很古老的建筑物了……\x01",
            "不定期做扫除\x01",
            "可是不行的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA7")

    label("loc_3965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3AAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1E")

    #C0177
    ChrTalk(
        0xFE,
        (
            "高年级的课程\x01",
            "要比低年级的课程\x01",
            "困难不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "小琪雅的理解能力\x01",
            "真是很出众呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x153,
        (
            "#01109F嘿嘿嘿……\x01",
            "被表扬啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#00000F哈哈，连我都感到面上有光呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AA6")

    label("loc_3A1E")


    #C0181
    ChrTalk(
        0xFE,
        (
            "小琪雅经常可以\x01",
            "轻松解答一些连大人都要\x01",
            "努力思考良久的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "我虽然没去课堂旁听，\x01",
            "但光是听别人转述一下，\x01",
            "也能明白她有多厉害。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA6")

    Jump("loc_3CA7")

    label("loc_3AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_3BD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B69")

    #C0183
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教好像\x01",
            "正在会见那个刚刚到任的\x01",
            "名叫莉丝的修女。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "在听到她的名字时，\x01",
            "我感觉大主教显露出了\x01",
            "一丝惊讶的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "嗯，莫非她是个\x01",
            "很有名的人吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BD2")

    label("loc_3B69")


    #C0186
    ChrTalk(
        0xFE,
        (
            "莉丝修女报上自己的名字时，\x01",
            "大主教似乎显露出了\x01",
            "一丝惊讶的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "嗯，莫非她是个\x01",
            "很有名的人吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD2")

    Jump("loc_3CA7")

    label("loc_3BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5B")

    #C0188
    ChrTalk(
        0xFE,
        (
            "大圣堂会定期\x01",
            "举行弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "弥撒就是赞颂空之女神的\x01",
            "神圣仪式……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "当弥撒举办时，\x01",
            "还请踊跃参加。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CA7")

    label("loc_3C5B")


    #C0191
    ChrTalk(
        0xFE,
        (
            "弥撒就是赞颂空之女神的\x01",
            "神圣仪式……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "当弥撒举办时，\x01",
            "还请踊跃参加。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA7")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D49 end

    def Function_16_3CAB(): pass

    label("Function_16_3CAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D44")

    #C0193
    ChrTalk(
        0xFE,
        (
            "总算与市外的孩子们\x01",
            "取得联络了。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "虽然不久后还要外出讲授主日学校\x01",
            "的课程，到时也能看到他们，\x01",
            "但提前放下心当然更好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3DC7")

    label("loc_3D44")


    #C0195
    ChrTalk(
        0xFE,
        (
            "已经与市外的孩子们取得联络了，\x01",
            "总算可以把心放下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "嗯，为了准备主日学校的再次开课，\x01",
            "去和玛布尔修女讨论一下\x01",
            "授课内容吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC7")

    Jump("loc_4C2F")

    label("loc_3DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5A")

    #C0197
    ChrTalk(
        0xFE,
        (
            "在这种一直都很难\x01",
            "与市外的孩子们取得联络的时候，\x01",
            "怎么又发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊……\x01",
            "请您保佑大家吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E83")

    label("loc_3E5A")


    #C0199
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊……\x01",
            "请您保佑大家吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E83")

    Jump("loc_4C2F")

    label("loc_3E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F86")

    #C0200
    ChrTalk(
        0xFE,
        (
            "莉丝修女在几天前\x01",
            "离开克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "据说是亚尔特利亚法典国\x01",
            "下达了召回指示……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#00005F（艾莉，这莫非是……）\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#00101F（嗯，应该就是向\x01",
            "  『星杯骑士』下达的指示。）\x02\x03",

            "#00103F（至于具体内容，\x01",
            "  我就不了解了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3FDE")

    label("loc_3F86")


    #C0204
    ChrTalk(
        0xFE,
        (
            "莉丝修女在几天前\x01",
            "离开克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "据说是亚尔特利亚法典国\x01",
            "下达了召回指示……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FDE")

    Jump("loc_4C2F")

    label("loc_3FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4072")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4015")
    Call(0, 54)
    Return()

    label("loc_4015")


    #C0206
    ChrTalk(
        0xFE,
        (
            "参加这次弥撒的人\x01",
            "要比平时多很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "大家在袭击事件中遭受的创伤\x01",
            "果然很严重呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C2F")

    label("loc_4072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_419F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4129")

    #C0208
    ChrTalk(
        0xFE,
        (
            "小奇米，还有亚雷库……\x01",
            "前天还见过面，\x01",
            "如今他们却被卷进这样的事件了……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "他们现在一定很害怕吧……\x01",
            "啊啊，女神啊……\x01",
            "请您救救孩子们，救救玛因兹吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_419A")

    label("loc_4129")


    #C0210
    ChrTalk(
        0xFE,
        (
            "我为了完成\x01",
            "主日学校的外出授课，\x01",
            "前天刚刚去过玛因兹。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "啊啊，女神啊……\x01",
            "请您救救孩子们，救救玛因兹吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_419A")

    Jump("loc_4C2F")

    label("loc_419F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_41AD")
    Jump("loc_4C2F")

    label("loc_41AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41BB")
    Jump("loc_4C2F")

    label("loc_41BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41C9")
    Jump("loc_4C2F")

    label("loc_41C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_4263")

    #C0212
    ChrTalk(
        0xFE,
        (
            "高年级的授课\x01",
            "好像已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "我明天和后天分别\x01",
            "要去玛因兹和阿尔摩利卡\x01",
            "外出授课。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "稍后要去和玛布尔修女\x01",
            "讨论一下授课内容才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C2F")

    label("loc_4263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_436B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FB")

    #C0215
    ChrTalk(
        0xFE,
        "找玛布尔修女有事吗？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "她正在给高年级的学生\x01",
            "授课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "她今天还要将\x01",
            "授课方式教给久久修女，\x01",
            "也许没时间接待你们……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4366")

    label("loc_42FB")


    #C0218
    ChrTalk(
        0xFE,
        (
            "玛布尔修女正在给\x01",
            "高年级的学生授课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "她今天还要将\x01",
            "授课方式教给久久修女，\x01",
            "也许没时间接待你们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4366")

    Jump("loc_4C2F")

    label("loc_436B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4458")

    #C0220
    ChrTalk(
        0xFE,
        (
            "久久修女今天好像\x01",
            "要向玛布尔修女\x01",
            "学习授课方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "之前将玛因兹的外出授课\x01",
            "任务交给了莉丝修女，\x01",
            "对她似乎是个很好的刺激呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "孩子们很喜欢久久修女，\x01",
            "虽然她的授课方式有些笨拙，\x01",
            "但一定可以慢慢掌握技巧的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_44A0")

    label("loc_4458")


    #C0223
    ChrTalk(
        0xFE,
        (
            "久久修女很受\x01",
            "孩子们的喜欢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "相信一定可以\x01",
            "慢慢掌握授课技巧的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A0")

    Jump("loc_4C2F")

    label("loc_44A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_454C")

    #C0225
    ChrTalk(
        0xFE,
        (
            "外出授课的\x01",
            "莉丝修女\x01",
            "刚才总算回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "比预期时间晚了一些，\x01",
            "我还一直在担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "莫非她是跑到什么地方\x01",
            "去大吃大喝了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_459D")

    label("loc_454C")


    #C0228
    ChrTalk(
        0xFE,
        (
            "外出授课的\x01",
            "莉丝修女\x01",
            "刚才总算回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "现在应该去玛布尔修女\x01",
            "那里报告了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459D")

    Jump("loc_46C4")

    label("loc_45A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_466D")

    #C0230
    ChrTalk(
        0xFE,
        (
            "莉丝修女今天要去\x01",
            "玛因兹地区进行\x01",
            "主日学校的外出授课。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "她的性格虽然很文静，\x01",
            "但却很会教课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "说起来，都已经这么晚了，\x01",
            "差不多也该回来了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "莫非是坐巴士\x01",
            "坐过站了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_46C4")

    label("loc_466D")


    #C0234
    ChrTalk(
        0xFE,
        (
            "都已经这么晚了，\x01",
            "外出授课的莉丝修女\x01",
            "也该回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "莫非是坐巴士\x01",
            "坐过站了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C4")

    Jump("loc_4C2F")

    label("loc_46C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_474C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E4")
    Call(0, 14)
    Jump("loc_4747")

    label("loc_46E4")


    #C0236
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教……\x01",
            "好像一直都非常在意\x01",
            "莉丝修女。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "莫非存在着什么我们所不知\x01",
            "的隐情吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4747")

    Jump("loc_4C2F")

    label("loc_474C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_48B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4849")

    #C0238
    ChrTalk(
        0xFE,
        (
            "玛因兹和阿尔摩利卡的孩子们\x01",
            "离大圣堂太远了，所以无法到\x01",
            "主日学校来上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "而旧城区的孩子们\x01",
            "就算到了授课日\x01",
            "也经常不来教会。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "为了那些孩子们，\x01",
            "我们这些修女\x01",
            "会外出授课。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "顺便一说，\x01",
            "莉丝修女今天去\x01",
            "旧城区授课了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_48AC")

    label("loc_4849")


    #C0242
    ChrTalk(
        0xFE,
        (
            "顺便一说，\x01",
            "莉丝修女今天去\x01",
            "旧城区授课了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "那里的孩子都比较顽劣，\x01",
            "她能顺利完成授课吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AC")

    Jump("loc_4C2F")

    label("loc_48B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CC")
    Call(0, 13)
    Jump("loc_4942")

    label("loc_48CC")


    #C0244
    ChrTalk(
        0xFE,
        (
            "莉丝修女很快就将\x01",
            "工作熟练掌握了……\x01",
            "真是帮了我们的大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "艾拉尔达大主教……\x01",
            "看起来似乎有些在意\x01",
            "莉丝修女呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4942")

    Jump("loc_4C2F")

    label("loc_4947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_49C2")

    #C0246
    ChrTalk(
        0xFE,
        (
            "莉丝修女在与\x01",
            "大主教打过招呼之后，\x01",
            "好像就去墓地那边了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "从明天开始，我们要将\x01",
            "各种各样的工作教给她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C2F")

    label("loc_49C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_4BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B51")

    #C0248
    ChrTalk(
        0xFE,
        (
            "莉丝修女的身上似乎有种\x01",
            "沉着安稳的气息，\x01",
            "是个气质独特的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "而且她的身上\x01",
            "似乎还散发着很好闻的香气，\x01",
            "那究竟是……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00005F说起来……\x01",
            "莉丝小姐的身上好像\x01",
            "隐隐有一些面包的气味。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#00100F多半是来大圣堂报到之前，\x01",
            "先去面包店里买了面包吧。\x02\x03",

            "#00109F莉丝小姐身材如此苗条，\x01",
            "胃口却相当惊人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x109,
        "#10105F哎……这样吗？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，倒是真想\x01",
            "和她共餐一次呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BC0")

    label("loc_4B51")


    #C0254
    ChrTalk(
        0xFE,
        (
            "莉丝修女的身上似乎有种\x01",
            "沉着安稳的气息，\x01",
            "是个气质独特的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "对久久修女来说，\x01",
            "似乎也会是个很好的刺激。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC0")

    Jump("loc_4C2F")

    label("loc_4BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C2F")

    #C0256
    ChrTalk(
        0xFE,
        (
            "亚尔特利亚法典国\x01",
            "今天将要派遣新的修女\x01",
            "到这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "究竟会是什么样的人呢……\x01",
            "真是有点期待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C2F")

    TalkEnd(0xFE)
    Return()

    # Function_16_3CAB end

    def Function_17_4C33(): pass

    label("Function_17_4C33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CAE")

    #C0258
    ChrTalk(
        0xC,
        (
            "接下来，市民们大概会\x01",
            "接连不断地前来教会寻求救赎。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xC,
        (
            "我们必须做好充足准备，\x01",
            "以便迎接他们的到来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_4CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D05")

    #C0260
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔市似乎发生了\x01",
            "很严重的事件呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        "但愿市民们平安无事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_4D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCA")

    #C0262
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔独立吗……\x01",
            "真是让人震惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "不仅如此，竟然还要冻结各国在银行的资金……\x01",
            "身为七耀教会的一员，\x01",
            "实在是无法赞同拥护呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "我们暂且观望\x01",
            "事态的发展吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E3D")

    label("loc_4DCA")


    #C0265
    ChrTalk(
        0xC,
        (
            "竟然冻结各国在银行的资金……\x01",
            "身为七耀教会的一员，\x01",
            "实在是无法赞同拥护呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "我们暂时先观望\x01",
            "事态的发展吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3D")

    Jump("loc_5944")

    label("loc_4E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4EDE")

    #C0267
    ChrTalk(
        0xC,
        (
            "旧城区的重建工作\x01",
            "似乎是由圣书会的\x01",
            "那些孩子带头发起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "一开始我还不明白他们\x01",
            "想干什么，原来是这样……\x01",
            "看来都是些本性善良的好孩子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_4EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4F3E")

    #C0269
    ChrTalk(
        0xC,
        (
            "竟然会发生这样的事件，\x01",
            "真是让人难以置信。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "希望玛因兹的人们\x01",
            "平安无事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_4F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F9B")

    #C0271
    ChrTalk(
        0xC,
        (
            "我刚才看到\x01",
            "久久修女摔了个\x01",
            "四脚朝天。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "哎呀呀，她总是这么\x01",
            "笨手笨脚的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_4F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5001")

    #C0273
    ChrTalk(
        0xC,
        (
            "在调配药物等工作中\x01",
            "会经常使用到这个台座。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "因此要比其它地方\x01",
            "更加用心打扫才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_5001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5116")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50A0")

    #C0275
    ChrTalk(
        0xC,
        (
            "莉丝修女的圣典\x01",
            "好像从不离身呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "我经常能看到\x01",
            "她只要有点空闲，\x01",
            "就会翻开书阅读。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "哎呀，真是个勤奋的人。\x01",
            "十分让人佩服。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5111")

    label("loc_50A0")


    #C0278
    ChrTalk(
        0xC,
        (
            "莉丝修女的圣典\x01",
            "好像从不离身呢。\x01",
            "只要有点空闲，她就会翻开书阅读。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "哎呀，真是个勤奋的人。\x01",
            "十分让人佩服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5111")

    Jump("loc_5944")

    label("loc_5116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_5178")

    #C0280
    ChrTalk(
        0xC,
        (
            "莉丝修女已经\x01",
            "从市里回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        (
            "她今天是在哪里吃的东西呢……\x01",
            "稍后去问问好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_5178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_51D5")

    #C0282
    ChrTalk(
        0xC,
        "嗯，已经打扫得差不多了。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        (
            "这是大家的共用场所，\x01",
            "必须要打扫得干干净净。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_51D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5265")

    #C0284
    ChrTalk(
        0xC,
        (
            "我正在办公室做扫除，\x01",
            "大主教就进来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xC,
        (
            "他说有些事情要调查，\x01",
            "需要一个人独处。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "嗯……\x01",
            "到底要调查什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_52AF")

    label("loc_5265")


    #C0287
    ChrTalk(
        0xC,
        (
            "莉丝修女刚才\x01",
            "去市里了，\x01",
            "好像是要去吃午饭……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        "我也休息一下好了。\x02",
    )

    CloseMessageWindow()

    label("loc_52AF")

    Jump("loc_5944")

    label("loc_52B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_53D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5361")

    #C0289
    ChrTalk(
        0xC,
        (
            "我原本还在想，\x01",
            "科洛蒂娅殿下会不会因为\x01",
            "今天的正式会议而紧张……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xC,
        (
            "结果她竟然\x01",
            "无比冷静呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "不愧是利贝尔的下任女王……\x01",
            "真是镇定自若啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_53CE")

    label("loc_5361")


    #C0292
    ChrTalk(
        0xC,
        (
            "会议马上就要召开了，\x01",
            "科洛蒂娅殿下\x01",
            "却仍然可以保持平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xC,
        (
            "不愧是利贝尔的下任女王……\x01",
            "真是镇定自若啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53CE")

    Jump("loc_5944")

    label("loc_53D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549A")

    #C0294
    ChrTalk(
        0xC,
        "揭幕式真是令我也大吃一惊。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "老实说，\x01",
            "居然能盖起四十层的建筑物，\x01",
            "这实在是让人难以置信。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xC,
        (
            "哈哈，等迪塔市长\x01",
            "下次来参加礼拜的时候，\x01",
            "可要好好向他表达我的崇拜之情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5523")

    label("loc_549A")


    #C0297
    ChrTalk(
        0xC,
        (
            "揭幕式真是令我也大吃一惊。\x01",
            "居然能盖起四十层的建筑物……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "哈哈，等迪塔市长\x01",
            "下次来参加礼拜的时候，\x01",
            "可要好好向他表达我的崇拜之情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5523")

    Jump("loc_5944")

    label("loc_5528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_56A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5619")

    #C0299
    ChrTalk(
        0xC,
        (
            "艾拉尔达大主教\x01",
            "是个十分刻板的人，\x01",
            "因此在教会内也存在很多对立者。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xC,
        (
            "其中，他尤其反感那些活动内容\x01",
            "遮遮掩掩的『封圣省』成员，\x01",
            "对他们的态度十分严厉。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        (
            "拜其所赐，\x01",
            "封圣省的相关人员\x01",
            "几乎不会来克洛斯贝尔教区。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_569E")

    label("loc_5619")


    #C0302
    ChrTalk(
        0xC,
        (
            "说起封圣省，\x01",
            "据说那是教会内专门负责\x01",
            "管理女神机密的机关……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xC,
        (
            "但他们的活动内容十分隐蔽，\x01",
            "连我们这些普通的神职人员也不太了解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_569E")

    Jump("loc_5944")

    label("loc_56A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_57E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5779")

    #C0304
    ChrTalk(
        0xC,
        (
            "莉丝修女太过安静老实，\x01",
            "所以我原本还担心她是否能与大家和睦相处……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xC,
        (
            "但她首先就和昨天负责做晚饭\x01",
            "的久久修女相处融洽了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "昨天晚上她们好像一直在讨论\x01",
            "市内的美食店，聊得很热闹。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_57DB")

    label("loc_5779")


    #C0307
    ChrTalk(
        0xC,
        (
            "只要一谈到有关食物的话题，\x01",
            "莉丝修女马上就会积极响应。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "哈哈，她对食物的热情\x01",
            "可真是惊人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DB")

    Jump("loc_5944")

    label("loc_57E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_585B")

    #C0309
    ChrTalk(
        0xC,
        (
            "会面已经结束了，\x01",
            "但大主教好像还在思考着什么心事。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xC,
        (
            "莫非莉丝修女\x01",
            "有什么问题吗？\x01",
            "我是完全没看出来……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_585B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_58DA")

    #C0311
    ChrTalk(
        0xC,
        (
            "只要有新祭司或修女\x01",
            "加入，大主教就会\x01",
            "与他们一一会面。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xC,
        (
            "不适合担任神职工作者的人\x01",
            "是不能留在这所大圣堂的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5944")

    label("loc_58DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5944")

    #C0313
    ChrTalk(
        0xC,
        (
            "这里是艾拉尔达大主教\x01",
            "的办公室。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xC,
        (
            "珍奇的药草与贵重的书籍\x01",
            "都保存在这里，\x01",
            "请不要随意触碰。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5944")

    TalkEnd(0xFE)
    Return()

    # Function_17_4C33 end

    def Function_18_5948(): pass

    label("Function_18_5948")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A09")

    #C0315
    ChrTalk(
        0xFE,
        (
            "突然出现了那种东西，\x01",
            "商业伙伴们全都很吃惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "但是不必担心。\x01",
            "只要向女神祈祷，\x01",
            "就一定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "你们也来祈祷吧。\x01",
            "只要诚心祈祷，\x01",
            "不管什么事都会顺利的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A81")

    label("loc_5A09")


    #C0318
    ChrTalk(
        0xFE,
        (
            "无论发生了什么事情，\x01",
            "只要向女神祈祷，\x01",
            "就一定没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "你们也来祈祷吧。\x01",
            "只要诚心祈祷，\x01",
            "不管做什么都会顺利的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A81")

    Jump("loc_6C2D")

    label("loc_5A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1E")

    #C0320
    ChrTalk(
        0xFE,
        (
            "我、我在戒严令颁布期间\x01",
            "悄悄跑出来祈祷，\x01",
            "结果却发生了这样的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "现在已经无法回到市里了，\x01",
            "到底该怎么办才好……！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B60")

    label("loc_5B1E")


    #C0322
    ChrTalk(
        0xFE,
        (
            "总、总之，\x01",
            "现在也只能向女神祈祷，\x01",
            "希望这事态能尽快平息了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B60")

    Jump("loc_6C2D")

    label("loc_5B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C2B")

    #C0323
    ChrTalk(
        0xFE,
        (
            "如果铁路停运，\x01",
            "今后的贸易工作\x01",
            "可就十分严峻了……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "但我并不打算\x01",
            "逆潮流而动，\x01",
            "因为这一定也是女神的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "总之一定会有办法的，\x01",
            "只要保持着相信女神的诚心就好啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5C82")

    label("loc_5C2B")


    #C0326
    ChrTalk(
        0xFE,
        (
            "只要向女神祈祷，\x01",
            "无论做什么\x01",
            "都会顺利的。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "你们也来祈祷吧，\x01",
            "最重要的还是诚心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C82")

    Jump("loc_6C2D")

    label("loc_5C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D50")

    #C0328
    ChrTalk(
        0xFE,
        (
            "因为一直都向女神祈祷，最近\x01",
            "买卖做得越来越好……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "但发生了如此严重的事件，\x01",
            "实在是让人高兴不起来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "一味拼命赚钱\x01",
            "并没有意义，\x01",
            "唯有平稳的生活才是真正应该祈祷的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5DC5")

    label("loc_5D50")


    #C0331
    ChrTalk(
        0xFE,
        (
            "不管赚到多少钱，\x01",
            "看到克洛斯贝尔陷入这种状况\x01",
            "也完全高兴不起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "唯有平稳的生活，\x01",
            "才是真正应该向女神祈祷的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC5")

    Jump("loc_6C2D")

    label("loc_5DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E60")

    #C0333
    ChrTalk(
        0xFE,
        (
            "我今天本想去玛因兹\x01",
            "购入七耀石……\x01",
            "没想到竟然会发生这种事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "对、对了，要赶快向女神祈祷，\x01",
            "希望事件能快点解决……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5EC6")

    label("loc_5E60")


    #C0335
    ChrTalk(
        0xFE,
        (
            "即使抛开生意上的事不谈，\x01",
            "我也很担心玛因兹的状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "女神啊，请您引导这场事件\x01",
            "圆满解决吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC6")

    Jump("loc_6C2D")

    label("loc_5ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6E")

    #C0337
    ChrTalk(
        0xFE,
        (
            "其实我昨天一整天\x01",
            "都有种不祥的预感。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "之后一打听，\x01",
            "才知道发生了\x01",
            "脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "虽然并不影响我的商谈……\x01",
            "但还是感到毛骨悚然啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5FE5")

    label("loc_5F6E")


    #C0340
    ChrTalk(
        0xFE,
        (
            "其实我昨天一整天\x01",
            "都有种不祥的预感。\x01",
            "脱轨事故真是让人吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "虽然并不影响我的商谈……\x01",
            "但还是感到毛骨悚然啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE5")

    Jump("loc_6C2D")

    label("loc_5FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_60E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6075")

    #C0342
    ChrTalk(
        0xFE,
        (
            "我一直都充满热情地坚持向女神祈祷……\x01",
            "但鞋带却突然断掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "今天还有商谈任务……\x01",
            "为什么这么不吉利啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_60DF")

    label("loc_6075")


    #C0344
    ChrTalk(
        0xFE,
        (
            "黑猫从我面前经过，\x01",
            "鞋带又断掉……\x01",
            "从今天早上开始，不吉利的预兆就接连不断。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "但愿别发生什么事……\x02",
    )

    CloseMessageWindow()

    label("loc_60DF")

    Jump("loc_6C2D")

    label("loc_60E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A4")

    #C0346
    ChrTalk(
        0xFE,
        (
            "……今天早上，\x01",
            "有只黑猫从我面前经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "啊啊，可恶……\x01",
            "今天还有商谈任务呢，\x01",
            "这也太不吉利了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "既然如此，必须要比\x01",
            "平时更加用心地祈祷才行啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)
    Jump("loc_6202")

    label("loc_61A4")


    #C0349
    ChrTalk(
        0xFE,
        (
            "今天还有商谈任务在身，\x01",
            "一只黑猫却从我的面前经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "女神啊，请帮我将这\x01",
            "晦气消除吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6202")

    Jump("loc_6C2D")

    label("loc_6207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_6275")

    #C0351
    ChrTalk(
        0xFE,
        (
            "……嗯，已经认真祈祷过了，\x01",
            "差不多也该回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "……不，还是不够，\x01",
            "再在这里祈祷一会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C2D")

    label("loc_6275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_63CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6346")

    #C0353
    ChrTalk(
        0xFE,
        (
            "之前来的那个人\x01",
            "好像是伊安·格里姆伍德律师啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "看上去，他好像有些疲倦……\x01",
            "洋溢在礼拜堂之内的圣洁空气\x01",
            "一定能使他那疲惫的身躯恢复活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "他已经祈祷过了……\x01",
            "应该没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_63C6")

    label("loc_6346")


    #C0356
    ChrTalk(
        0xFE,
        (
            "我在经商过程中\x01",
            "经常会去找格里姆伍德\x01",
            "律师商谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "看上去，他好像有些疲倦……\x01",
            "不过他已经祈祷过了……\x01",
            "应该可以恢复活力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C6")

    Jump("loc_6C2D")

    label("loc_63CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6496")

    #C0358
    ChrTalk(
        0xFE,
        (
            "迪塔市长发表独立提案之后，\x01",
            "在境外诸国似乎也引起了很高的关注。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "外国的那些商业伙伴\x01",
            "整天也都在讨论有关\x01",
            "克洛斯贝尔独立的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "现在克洛斯贝尔受到了\x01",
            "更进一步的关注。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6524")

    label("loc_6496")


    #C0361
    ChrTalk(
        0xFE,
        (
            "调查居民意见的投票活动也即将开始。\x01",
            "至于投票结果，现在也只有\x01",
            "女神才能知道了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "哦哦，女神啊，\x01",
            "请您为克洛斯贝尔\x01",
            "指引最佳的选择吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6524")

    Jump("loc_6C2D")

    label("loc_6529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_65C0")

    #C0363
    ChrTalk(
        0xFE,
        (
            "在今天的正式会议中，\x01",
            "普通市民好像是无法旁听的。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "虽然很遗憾……但也没办法。\x01",
            "我就在这里继续向女神祈祷，\x01",
            "保佑会议顺利取得成功吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C2D")

    label("loc_65C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_66C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6660")

    #C0365
    ChrTalk(
        0xFE,
        (
            "我也看到过\x01",
            "兰花塔……\x01",
            "实在是高得惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "要是站在楼顶\x01",
            "向空之女神祈祷，\x01",
            "女神就会更容易听到吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "嗯，真想登上去\x01",
            "看看啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_66C1")

    label("loc_6660")


    #C0368
    ChrTalk(
        0xFE,
        (
            "如果在兰花塔的楼顶祈祷，\x01",
            "空之女神就更容易\x01",
            "听到我们的声音吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "嗯，我真想登上去\x01",
            "看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C1")

    Jump("loc_6C2D")

    label("loc_66C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_67CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6779")

    #C0370
    ChrTalk(
        0xFE,
        (
            "在从明天开始的通商会议中，\x01",
            "将会对经济相关方面的\x01",
            "各种问题展开讨论及定夺。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "对我这个以克洛斯贝尔\x01",
            "为据点的商人来说，\x01",
            "真是个非常值得关注的活动啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_67C5")

    label("loc_6779")


    #C0372
    ChrTalk(
        0xFE,
        (
            "身为商人，对通商会议\x01",
            "是非常关心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "总之，要向女神祈祷\x01",
            "会议成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C5")

    Jump("loc_6C2D")

    label("loc_67CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_68CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6869")

    #C0374
    ChrTalk(
        0xFE,
        (
            "不管是下暴雨还是刮台风，\x01",
            "或者是一大早就要去商谈也好，\x01",
            "我都没有忘记过每天的祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "多亏如此，\x01",
            "我的买卖越做越好。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_68C7")

    label("loc_6869")


    #C0376
    ChrTalk(
        0xFE,
        (
            "无论发生什么事情，\x01",
            "我都没有忘记过每天的祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "正所谓『坚持就是力量』啊。\x01",
            "哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C7")

    Jump("loc_6C2D")

    label("loc_68CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_6A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69F7")

    #C0378
    ChrTalk(
        0x153,
        (
            "#01105F啊，是那个每天都来\x01",
            "祈祷的叔叔。\x02\x03",

            "#01109F你好像早上就来了，\x01",
            "怎么现在还在？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "嗯，每逢休息日，\x01",
            "我会将一整天\x01",
            "都用于祈祷的。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        (
            "小姑娘，你也来祈祷吧。\x01",
            "只要诚心祈祷，\x01",
            "无论做什么都能顺利成功的。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x153,
        "#01105F……罗伊德，真的吗？\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#00006F（……问我也没用。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6A65")

    label("loc_69F7")


    #C0383
    ChrTalk(
        0xFE,
        (
            "每逢休息日，\x01",
            "我会将一整天\x01",
            "都用于祈祷的。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "你们也来祈祷吧。\x01",
            "只要诚心祈祷，\x01",
            "无论做什么都能顺利成功的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A65")

    Jump("loc_6C2D")

    label("loc_6A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_6B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AE2")

    #C0385
    ChrTalk(
        0xFE,
        (
            "全都靠女神的保佑，\x01",
            "才能有如今的我……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "必须要满怀感激的心情\x01",
            "向女神祈祷才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_6B40")

    label("loc_6AE2")


    #C0387
    ChrTalk(
        0xFE,
        (
            "啊啊，空之女神啊，\x01",
            "感谢您一直以来的保佑……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        (
            "在下一次的交易中\x01",
            "也请继续保佑我吧……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B40")

    Jump("loc_6C2D")

    label("loc_6B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB7")

    #C0389
    ChrTalk(
        0xFE,
        (
            "我是一个贸易商，\x01",
            "为了祈祷买卖顺利，\x01",
            "经常来这里祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "我建议你们也\x01",
            "多来祈祷。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6C2D")

    label("loc_6BB7")


    #C0391
    ChrTalk(
        0xFE,
        (
            "我以前向女神祈祷，希望能在经商中成功，\x01",
            "结果就真的越来越顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "不管做什么，首先要向女神祈祷。\x01",
            "这样做准没错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C2D")

    TalkEnd(0xFE)
    Return()

    # Function_18_5948 end

    def Function_19_6C31(): pass

    label("Function_19_6C31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6C42")
    Jump("loc_74FC")

    label("loc_6C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_702C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C74")
    Call(0, 56)
    Return()

    label("loc_6C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F04")

    #C0393
    ChrTalk(
        0x101,
        (
            "#00000F莉丝小姐，\x01",
            "你正在帮忙处理\x01",
            "弥撒中的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xA,
        (
            "#04400F嗯，正是。\x02\x03",

            "#04408F……前来参加\x01",
            "这次弥撒的人似乎\x01",
            "比平时多了不少。\x02\x03",

            "重要的家园被袭击、\x01",
            "破坏的那种恐惧感……\x02\x03",

            "#04403F……我都能体会得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        "#00105F莉丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x105,
        (
            "#10303F（……她以前或许也有过\x01",
            "  类似的遭遇呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0397
    ChrTalk(
        0xA,
        (
            "#04400F（这些话只在这里说……\x01",
            "  受此次事件的影响，『封圣省』目前\x01",
            "  也在犹豫下一步的行动方针。）\x02\x03",

            "#04403F（……我打算趁还能留在克洛斯贝尔的时间里，\x01",
            "  尽可能地收集情报。）\x02\x03",

            "#04400F（各位也请随时注意\x01",
            "  事态的动向。）\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x103,
        "#00200F（还能留在克洛斯贝尔的时间里吗……）\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        (
            "#00003F（……明白了，\x01",
            "  莉丝小姐也要多加小心。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)
    Jump("loc_6FC8")

    label("loc_6F04")


    #C0400
    ChrTalk(
        0xA,
        (
            "#04400F（受此次事件的影响，『封圣省』目前\x01",
            "  也在犹豫下一步的行动方针。）\x02\x03",

            "#04403F（……我打算趁还能留在克洛斯贝尔的时间里，\x01",
            "  尽可能地收集情报。）\x02\x03",

            "#04400F（各位也请随时注意\x01",
            "  事态的动向。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FC8")

    Jump("loc_7027")

    label("loc_6FCD")


    #C0401
    ChrTalk(
        0xA,
        (
            "#04400F我暂时还要继续\x01",
            "帮忙处理弥撒中的工作。\x02\x03",

            "#04404F等到活动要开始时\x01",
            "再和我联络吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7027")

    Jump("loc_74FC")

    label("loc_702C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_703A")
    Jump("loc_74FC")

    label("loc_703A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_73B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7309")

    #C0402
    ChrTalk(
        0xA,
        (
            "#04400F据说有人在昨天的\x01",
            "脱轨事故现场附近\x01",
            "目击到了巨大的怪物。\x02\x03",

            "各位，\x01",
            "你们有什么头绪吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        "#00001F嗯，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0404
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将昨日发生的事件\x01",
            "做了简要说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0405
    ChrTalk(
        0xA,
        (
            "#04405F……诺克斯森林中\x01",
            "也生长着灵智之草……\x02\x03",

            "#04408F而且『真知』再次\x01",
            "出现在了克洛斯贝尔吗……\x02\x03",

            "#04403F最重要的问题还是……\x01",
            "『是谁将真知交给他的』。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x105,
        (
            "#10301F……你们那边有什么\x01",
            "线索吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xA,
        (
            "#04400F很遗憾……\x01",
            "包含『真知』在内，教团方面的调查工作\x01",
            "仍然没有取得实质性进展。\x02\x03",

            "#04403F关于灵智之草，\x01",
            "虽然我还在继续调查，\x01",
            "但盛开原因等疑问仍然不明……\x02\x03",

            "#04400F由于可以潜入此地区的人\x01",
            "只有我，因此可能需要花费\x01",
            "比较久的时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x02\x03",

            "#00000F那么，如果以后有什么发现，\x01",
            "还请告知给我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xA,
        "#04400F嗯……明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 1)
    Jump("loc_73AB")

    label("loc_7309")


    #C0410
    ChrTalk(
        0xA,
        (
            "#04403F诺克斯森林的灵智之草……\x01",
            "还有再次出现在克洛斯贝尔\x01",
            "的『真知』……\x02\x03",

            "#04400F虽然我无法公开行动，\x01",
            "调查状况不容乐观……\x01",
            "但如果有所发现，一定会报告给大家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73AB")

    Jump("loc_74FC")

    label("loc_73B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_73BE")
    Jump("loc_74FC")

    label("loc_73BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_73CC")
    Jump("loc_74FC")

    label("loc_73CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_73DA")
    Jump("loc_74FC")

    label("loc_73DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_73E8")
    Jump("loc_74FC")

    label("loc_73E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_73F6")
    Jump("loc_74FC")

    label("loc_73F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_747C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741D")
    Call(0, 21)
    Jump("loc_7477")

    label("loc_741D")


    #C0411
    ChrTalk(
        0xA,
        (
            "#04400F……各位，今天真是\x01",
            "太感谢了。\x02\x03",

            "#04403F如果以后再有什么事情，\x01",
            "还请大家多帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7477")

    Jump("loc_74FC")

    label("loc_747C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_748A")
    Jump("loc_74FC")

    label("loc_748A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7498")
    Jump("loc_74FC")

    label("loc_7498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B3")
    Call(0, 20)
    Jump("loc_74D2")

    label("loc_74B3")


    #C0412
    ChrTalk(
        0xA,
        "#04403F（露菲娜姐姐……）\x02",
    )

    CloseMessageWindow()

    label("loc_74D2")

    Jump("loc_74FC")

    label("loc_74D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_74E5")
    Jump("loc_74FC")

    label("loc_74E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_74F3")
    Jump("loc_74FC")

    label("loc_74F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_74FC")

    label("loc_74FC")

    TalkEnd(0xFE)
    Return()

    # Function_19_6C31 end

    def Function_20_7500(): pass

    label("Function_20_7500")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0413
    ChrTalk(
        0xA,
        (
            "#04400F……原来如此，这里的教育工作\x01",
            "似乎相当超前。\x02\x03",

            "#04404F不愧是走在时代最前方的\x01",
            "现代都市啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        (
            "呵呵，虽然的确\x01",
            "稍微有些超前……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "但任何地方的小孩子\x01",
            "其实都是一样的啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xA,
        "#04402F的确……或许是这样。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x8,
        (
            "……对了，莉丝修女，\x01",
            "有件事情我\x01",
            "有点在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x8,
        (
            "你莫非是\x01",
            "露菲娜小姐的……\x01",
            "妹妹吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0419
    ChrTalk(
        0xA,
        "#04405F……您认识我姐姐吗？\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x8,
        (
            "呵呵，果然如此。\x01",
            "你们的姓氏一样，所以马上就想到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "我以前受到过她的\x01",
            "很多关照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xA,
        (
            "#04403F是吗……\x02\x03",

            "#04400F那个，玛布尔修女，\x01",
            "有件事要拜托您……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "呵呵，不用说我也知道啦。\x01",
            "你多半也是那里的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "我以前受到过露菲娜小姐的不少关照，\x01",
            "绝不会向大主教告密啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x8,
        "……不过，答应我一个要求可以吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0426
    ChrTalk(
        0x8,
        (
            "绝对不要太勉强自己。\x01",
            "就算是为了你的姐姐，也……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xA,
        (
            "#04403F……明白了，\x01",
            "谢谢您的关心。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 3)
    Return()

    # Function_20_7500 end

    def Function_21_7835(): pass

    label("Function_21_7835")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0428
    ChrTalk(
        0x8,
        (
            "莉丝修女，你回来得\x01",
            "似乎有些晚，\x01",
            "莫非发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "而且修道服上\x01",
            "也有很多污迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xA,
        (
            "#04403F抱歉，回来晚了。\x02\x03",

            "#04400F我在回来的路上\x01",
            "不小心摔了一跤。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x8,
        (
            "哎呀呀，没想到莉丝修女\x01",
            "还有笨拙的一面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x8,
        (
            "……虽然你还年轻，\x01",
            "但是以后可不能太莽撞哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xA,
        (
            "#04400F……谢谢关心，\x01",
            "我这就去换衣服。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x101,
        (
            "#00000F（玛布尔老师……\x01",
            "  似乎已经察觉到\x01",
            "  发生过一些事情呢。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x2, 0)
    Return()

    # Function_21_7835 end

    def Function_22_79C6(): pass

    label("Function_22_79C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79E9")
    Call(0, 23)
    Jump("loc_79EC")

    label("loc_79E9")

    Call(0, 25)

    label("loc_79EC")

    Jump("loc_79F4")

    label("loc_79F1")

    Call(0, 23)

    label("loc_79F4")

    Return()

    # Function_22_79C6 end

    def Function_23_79F5(): pass

    label("Function_23_79F5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B9B")

    #C0435
    ChrTalk(
        0x8,
        (
            "罗伊德，艾莉……\x01",
            "有件事想问你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        (
            "小琪雅……\x01",
            "就在那棵大树上吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0437
    ChrTalk(
        0x101,
        "#00005F老师……您已经知道了？\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x8,
        (
            "……看看你们那副\x01",
            "充满担忧的表情，\x01",
            "基本就能猜想到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x8,
        (
            "……我并不了解事情的详细情况，\x01",
            "要对你们说的话只有一句。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        (
            "你们身为小琪雅的监护人，\x01",
            "一定要亲手把她带回来。\x01",
            "……好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x102,
        "#00101F是……一定！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 3)
    Jump("loc_7C8F")

    label("loc_7B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C38")

    #C0442
    ChrTalk(
        0x8,
        (
            "无论发生了什么事情，\x01",
            "小琪雅都\x01",
            "需要你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x8,
        (
            "反过来说\x01",
            "也是一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x8,
        (
            "罗伊德，艾莉，还有各位，\x01",
            "请你们一定要亲手\x01",
            "把小琪雅带回来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7C8F")

    label("loc_7C38")


    #C0445
    ChrTalk(
        0x8,
        (
            "无论发生了什么事情，\x01",
            "小琪雅都\x01",
            "需要你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "请你们一定要亲手\x01",
            "把小琪雅带回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C8F")

    Jump("loc_91FB")

    label("loc_7C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E38")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0447
    ChrTalk(
        0x8,
        (
            "罗伊德，艾莉，\x01",
            "还有各位……！\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x101,
        (
            "#00000F玛布尔老师……\x01",
            "您平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x102,
        (
            "#00100F让您担心了，\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "哪里，不要介意。\x01",
            "大家平安无事\x01",
            "比什么都重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        (
            "话说回来……小琪雅\x01",
            "没和你们在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x103,
        "#00203F……没有。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x104,
        "#00306F虽然知道她在哪里，但是……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x8,
        "是吗……真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "……总之，现在的状况\x01",
            "十分艰难。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "你们一定要\x01",
            "多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 2)
    Jump("loc_7F34")

    label("loc_7E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF2")

    #C0457
    ChrTalk(
        0x8,
        "小琪雅……真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x8,
        (
            "自从发表独立宣言的那天之后，\x01",
            "我就再也没有见过她了，\x01",
            "真是很担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        (
            "……总之，现在的状况\x01",
            "十分艰难。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x8,
        (
            "你们一定要\x01",
            "多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7F34")

    label("loc_7EF2")


    #C0461
    ChrTalk(
        0x8,
        (
            "……总之，现在的状况\x01",
            "十分艰难。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "你们一定要\x01",
            "多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F34")

    Jump("loc_91FB")

    label("loc_7F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_815D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80DF")

    #C0463
    ChrTalk(
        0x8,
        (
            "罗伊德……\x01",
            "小琪雅还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x8,
        (
            "主日学校最近停课，一直都看不到她，\x01",
            "我有些担心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        (
            "#00008F……听您这么一说，\x01",
            "确实觉得她最近几天\x01",
            "有些奇怪呢。\x02\x03",

            "#00003F好像总是一副若有所思的表情……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#00108F的确……\x01",
            "在我们出门的时候，\x01",
            "她好像也显得非常担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x8,
        "是吗……\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        (
            "在这种状况下，心里不安\x01",
            "也是在所难免的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "罗伊德，\x01",
            "你身为小琪雅的监护人，\x01",
            "一定要看护好她哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#00000F嗯，那当然。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 4)
    Jump("loc_8158")

    label("loc_80DF")


    #C0471
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔已经陷入如此状况……\x01",
            "今后还不知道会发生什么情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x8,
        (
            "罗伊德，\x01",
            "你身为小琪雅的监护人，\x01",
            "一定要看护好她哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8158")

    Jump("loc_91FB")

    label("loc_815D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_82B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_818F")
    Call(0, 55)
    Return()

    label("loc_818F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8240")

    #C0473
    ChrTalk(
        0x8,
        (
            "总算已经确认来主日学校\x01",
            "上课的孩子们平安无事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "在如今这种状况下，\x01",
            "也只能暂时停课……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "等到再次开课的时候，\x01",
            "希望可以再看到他们那充满活力的笑脸。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_82B3")

    label("loc_8240")


    #C0476
    ChrTalk(
        0x8,
        (
            "在如今这种状况下，\x01",
            "主日学校\x01",
            "也只能暂时停课……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x8,
        (
            "等到再次开课的时候，\x01",
            "希望可以再看到他们那充满活力的笑脸。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B3")

    Jump("loc_91FB")

    label("loc_82B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_830A")

    #C0478
    ChrTalk(
        0x8,
        (
            "事态的发展似乎\x01",
            "相当严重啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x8,
        (
            "但愿玛因兹的人们\x01",
            "平安无事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91FB")

    label("loc_830A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_841A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83AB")

    #C0480
    ChrTalk(
        0x8,
        (
            "哈缇娜修女今天\x01",
            "去阿尔摩利卡村\x01",
            "进行主日学校的外出授课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔地区\x01",
            "今天似乎整体降雨……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x8,
        (
            "但愿她别被淋得\x01",
            "全身湿透。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8415")

    label("loc_83AB")


    #C0483
    ChrTalk(
        0x8,
        (
            "哈缇娜修女今天\x01",
            "去阿尔摩利卡村\x01",
            "进行主日学校的外出授课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        (
            "下起雨来了，\x01",
            "但愿她别被淋得\x01",
            "全身湿透。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8415")

    Jump("loc_91FB")

    label("loc_841A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_85E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856A")

    #C0485
    ChrTalk(
        0x8,
        (
            "莉丝修女有个\x01",
            "名叫露菲娜的姐姐，\x01",
            "她是我的知己。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x8,
        (
            "露菲娜归属于教会的『封圣省』，\x01",
            "她凭借着卓越的交涉技术，\x01",
            "曾解决过各种各样的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x8,
        (
            "不知从何时开始，她就有了『千之腕』\x01",
            "这样的绰号，在教会中也算是赫赫有名的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x8,
        (
            "……遗憾的是，在几年前，\x01",
            "她因为一场不幸的事故而殉教……\x01",
            "她的离世真是让人惋惜不已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_85E0")

    label("loc_856A")


    #C0489
    ChrTalk(
        0x8,
        (
            "露菲娜小姐\x01",
            "以前曾经多次\x01",
            "关照过我。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x8,
        (
            "原本还想再次向她表达\x01",
            "我的谢意，但如今却已……\x01",
            "她的离世真是让人惋惜不已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E0")

    Jump("loc_91FB")

    label("loc_85E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8781")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_871E")

    #C0491
    ChrTalk(
        0x8,
        (
            "对了，罗伊德……\x01",
            "你们昨天好像\x01",
            "来找过我吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x8,
        (
            "是有什么事情\x01",
            "想问我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x101,
        (
            "#00000F哦，没什么，\x01",
            "那件事情已经解决了。\x02\x03",

            "#00003F（有关『灵智之草』的事情\x01",
            "  在教会中似乎是禁忌……\x01",
            "  还是不要对老师说了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x8,
        (
            "是吗……\x01",
            "那就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x8,
        (
            "呵呵，如果以后需要帮忙，\x01",
            "请不要客气，随时来找我哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_877C")

    label("loc_871E")


    #C0496
    ChrTalk(
        0x8,
        (
            "我很愿意尽自己所能\x01",
            "来帮助你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x8,
        (
            "呵呵，如果以后需要帮忙，\x01",
            "请不要客气，随时来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_877C")

    Jump("loc_91FB")

    label("loc_8781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_8865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_879C")
    Call(0, 27)
    Jump("loc_8860")

    label("loc_879C")


    #C0498
    ChrTalk(
        0x8,
        (
            "千里之行，始于足下……\x01",
            "只要一点一滴地记住这些技巧就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#00008F（据大主教所说，\x01",
            "  老师应该也不清楚\x01",
            "  有关蓝花的事情……）\x02\x03",

            "#00003F（还是去找莉丝小姐吧，\x01",
            "  她现在就在礼拜堂前的宿舍。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8860")

    Jump("loc_91FB")

    label("loc_8865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_8974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88FA")

    #C0500
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔要将\x01",
            "自身税收的１０％\x01",
            "交给帝国和共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x8,
        (
            "这是两大宗主国\x01",
            "在自治州成立之初\x01",
            "所制定的自治州法中的一条……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_896F")

    label("loc_88FA")


    #C0502
    ChrTalk(
        0x8,
        (
            "也就是说，如果自治州能够独立，\x01",
            "克洛斯贝尔就可以\x01",
            "摆脱这种不利的束缚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x8,
        (
            "当然了，这肯定没有\x01",
            "说的这么简单……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_896F")

    Jump("loc_91FB")

    label("loc_8974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3F")

    #C0504
    ChrTalk(
        0x8,
        (
            "要将努力二字的重要性\x01",
            "教导给孩子们。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        (
            "这样的话，就算是很难的课程，\x01",
            "他们应该也会努力学习的。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x8,
        (
            "久久修女在讲课时\x01",
            "还是有些结结巴巴的，\x01",
            "但那股拼命努力的精神还是合格的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8ACD")

    label("loc_8A3F")


    #C0507
    ChrTalk(
        0x8,
        (
            "久久修女在讲课时\x01",
            "还是有些结结巴巴的，\x01",
            "但那股拼命努力的精神还是合格的。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x8,
        (
            "今后只要再熟练掌握授课时\x01",
            "的基本技巧，应该就可以\x01",
            "把课上好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ACD")

    Jump("loc_91FB")

    label("loc_8AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8D33")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AF9")
    Call(0, 21)
    Jump("loc_8B71")

    label("loc_8AF9")


    #C0509
    ChrTalk(
        0x8,
        (
            "莉丝修女的工作性质比较特殊，\x01",
            "有时难免会勉强自己……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x8,
        (
            "……罗伊德，你们也是一样。\x01",
            "虽然年轻，但不要太勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B71")

    Jump("loc_8D2E")

    label("loc_8B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CB5")

    #C0511
    ChrTalk(
        0x8,
        (
            "听说在不久之前发生在利贝尔\x01",
            "的异变事件中，科洛蒂娅殿下\x01",
            "也曾为解决事件而做出了贡献呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "就在那起严重事件的过程中，\x01",
            "她完成了王太女仪式，\x01",
            "正式成为利贝尔的下任女王。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x8,
        (
            "她究竟经历了多么激烈的思想斗争\x01",
            "才能下定这种决心，\x01",
            "身为外人自然无法得知……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x8,
        (
            "虽然年纪尚轻，但她一定是个\x01",
            "内心相当坚韧的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8D2E")

    label("loc_8CB5")


    #C0515
    ChrTalk(
        0x8,
        (
            "听说科洛蒂娅殿下在利贝尔\x01",
            "发生异变事件的期间，\x01",
            "完成了王太女仪式。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x8,
        (
            "虽然年纪尚轻，但她一定是个\x01",
            "内心相当坚韧的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D2E")

    Jump("loc_91FB")

    label("loc_8D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF1")

    #C0517
    ChrTalk(
        0x8,
        (
            "说起来，今天就是\x01",
            "揭幕式的日子了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x8,
        (
            "高达四十层的建筑物……\x01",
            "孩子们如果抬头仰视，\x01",
            "大概能感受到通往天际般的震撼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "呵呵，孩子们\x01",
            "现在应该\x01",
            "都很兴奋吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8E6B")

    label("loc_8DF1")


    #C0520
    ChrTalk(
        0x8,
        (
            "高达四十层的建筑物……\x01",
            "孩子们如果抬头仰视，\x01",
            "大概能感受到通往天际般的震撼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "呵呵，孩子们\x01",
            "现在应该\x01",
            "都很兴奋吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E6B")

    Jump("loc_91FB")

    label("loc_8E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F1C")

    #C0522
    ChrTalk(
        0x8,
        (
            "通商会议终于\x01",
            "要在明天开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x8,
        (
            "到时也许会非常繁忙……\x01",
            "你们也要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        "#00000F是，我们一定努力！\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x102,
        (
            "#00100F谢谢您，\x01",
            "玛布尔老师。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8F6A")

    label("loc_8F1C")


    #C0526
    ChrTalk(
        0x8,
        (
            "到时也许会非常繁忙……\x01",
            "你们也要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "我会一直在后方\x01",
            "支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F6A")

    Jump("loc_91FB")

    label("loc_8F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F8A")
    Call(0, 20)
    Jump("loc_8FD4")

    label("loc_8F8A")


    #C0528
    ChrTalk(
        0x8,
        (
            "啊，罗伊德，还有各位……\x01",
            "在下雨天还要出门啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        (
            "小心不要\x01",
            "感冒哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FD4")

    Jump("loc_91FB")

    label("loc_8FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_9184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_910C")
    TurnDirection(0x8, 0x153, 0)

    #C0530
    ChrTalk(
        0x8,
        (
            "呵呵，小琪雅，\x01",
            "期待你再来听\x01",
            "高年级的课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x8,
        (
            "下次我会准备更难些\x01",
            "的问题给你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x153,
        (
            "#01109F嗯，知道啦，\x01",
            "琪雅会认真预习的！\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x109,
        (
            "#10104F嗯～了不起……\x01",
            "真让人佩服啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，大概很快\x01",
            "就能超过我们了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#00006F嗯……要是那样，\x01",
            "我们就真是无地自容了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_917F")

    label("loc_910C")


    #C0536
    ChrTalk(
        0x8,
        (
            "自从小琪雅来听课之后，\x01",
            "高年级课堂的气氛\x01",
            "也更加活跃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "呵呵，对其他的孩子来说，\x01",
            "这也是个很不错的刺激吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_917F")

    Jump("loc_91FB")

    label("loc_9184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_9192")
    Jump("loc_91FB")

    label("loc_9192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_91FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91AD")
    Call(0, 24)
    Jump("loc_91FB")

    label("loc_91AD")


    #C0538
    ChrTalk(
        0x8,
        (
            "呵呵，不好意思哦，\x01",
            "我还要继续上课。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        (
            "以后要是有机会，\x01",
            "就再过来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91FB")

    TalkEnd(0x8)
    Return()

    # Function_23_79F5 end

    def Function_24_91FF(): pass

    label("Function_24_91FF")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1700, 16650, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27870, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrPos(0x101, 153000, 200, 16800, 270)
    SetChrPos(0x102, 153300, 200, 17700, 270)
    SetChrPos(0x109, 154200, 200, 17580, 270)
    SetChrPos(0x105, 153900, 200, 16580, 270)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0540
    ChrTalk(
        0x8,
        (
            "啊，罗伊德和艾莉……\x01",
            "你们来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        "#00000F好久不见了，玛布尔老师。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x102,
        (
            "#00105F好久不见……\x01",
            "哎，您好像并不是很吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x8,
        (
            "呵呵，因为小琪雅\x01",
            "刚才开心地告诉我\x01",
            "你们回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x109,
        (
            "#10100F您就是……罗伊德警官和艾莉小姐\x01",
            "在主日学校上学时的老师……？\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x8,
        (
            "嗯，是啊。\x01",
            "说起来，你们应该就是\x01",
            "支援科的新成员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x8,
        (
            "我是七耀教会的修女\x01",
            "玛布尔，\x01",
            "请多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        (
            "#00005F啊，如此说来……\x01",
            "诺艾尔当年没在\x01",
            "玛布尔老师这里上过课吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x109,
        (
            "#10100F嗯，我和芙兰当时\x01",
            "所在的东街班级\x01",
            "是由神父授课的。\x02\x03",

            "#10103F那个班级现在\x01",
            "好像已经没有了……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x105,
        (
            "#10304F嗯，教会内的祭司\x01",
            "也时常会有一些\x01",
            "调动的。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x8,
        (
            "呵呵，从这层意义上来说，\x01",
            "罗伊德和艾莉的再会\x01",
            "实在是很幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x12,
        (
            "玛布尔老师～\x01",
            "不要一直和大哥哥他们聊天了，\x01",
            "继续讲课嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x13,
        (
            "隆，你可真是的！\x01",
            "人家久别重逢，\x01",
            "你就不要捣乱啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0553
    ChrTalk(
        0x8,
        (
            "哎呀呀，对不起哦，\x01",
            "我太开心，一不小心就聊久了。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x8,
        (
            "呵呵，不好意思啦，\x01",
            "我还要继续讲课。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x8,
        (
            "以后要是有机会，\x01",
            "就再过来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x101,
        (
            "#00005F对、对不起，\x01",
            "打扰您上课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x102,
        (
            "#00100F嗯，那我们\x01",
            "就先告辞啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153260, 200, 16760, 270)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 2)
    EventEnd(0x5)
    Return()

    # Function_24_91FF end

    def Function_25_96DE(): pass

    label("Function_25_96DE")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97C2")

    #C0558
    ChrTalk(
        0xF,
        (
            "嗯，接下来要讲的是……\x01",
            "简单来说，在前一段时间\x01",
            "召开的那个通商会议……\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xF,
        (
            "主要就是商定\x01",
            "经济相关方面的……\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x18,
        (
            "老师，我有点\x01",
            "听不明白啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0561
    ChrTalk(
        0xF,
        (
            "哎，那、那我就\x01",
            "从头开始再讲一遍……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_982E")

    label("loc_97C2")


    #C0562
    ChrTalk(
        0xF,
        (
            "（呜呜，这个课题\x01",
            "  的难度是不是太高了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xF,
        (
            "（但、但这些知识很重要，\x01",
            "  一定要努力教给大家……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_982E")

    TalkEnd(0xF)
    Return()

    # Function_25_96DE end

    def Function_26_9832(): pass

    label("Function_26_9832")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9843")
    Jump("loc_9D83")

    label("loc_9843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9851")
    Jump("loc_9D83")

    label("loc_9851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_985F")
    Jump("loc_9D83")

    label("loc_985F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_992E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98CB")

    #C0564
    ChrTalk(
        0xFE,
        (
            "在下雨天，\x01",
            "地上是很滑的，\x01",
            "要小心别摔倒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        (
            "……我刚才就不小心\x01",
            "跌倒了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9929")

    label("loc_98CB")


    #C0566
    ChrTalk(
        0xFE,
        (
            "呼，还好主日学校\x01",
            "今天没课。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        (
            "当时的狼狈相要是被孩子们看到，\x01",
            "他们就会更加小看我了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9929")

    Jump("loc_9D83")

    label("loc_992E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_993C")
    Jump("loc_9D83")

    label("loc_993C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_994A")
    Jump("loc_9D83")

    label("loc_994A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_99CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9965")
    Call(0, 27)
    Jump("loc_99C5")

    label("loc_9965")


    #C0568
    ChrTalk(
        0xFE,
        (
            "玛布尔老师的教导\x01",
            "让我学会了很多东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "我希望自己有朝一日\x01",
            "也能成为像她那样出色的修女。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C5")

    Jump("loc_9D83")

    label("loc_99CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_9AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A52")

    #C0570
    ChrTalk(
        0xFE,
        (
            "玛布尔老师讲的课\x01",
            "真是让我学会了不少东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xFE,
        (
            "啊！不对不对！\x01",
            "这可不是在听课，\x01",
            "必须得多加参考才行……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9AA4")

    label("loc_9A52")


    #C0572
    ChrTalk(
        0xFE,
        (
            "我正在旁听玛布尔老师的授课，\x01",
            "学习讲课的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xFE,
        (
            "但是一不小心\x01",
            "就听入了神。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AA4")

    Jump("loc_9D83")

    label("loc_9AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B93")

    #C0574
    ChrTalk(
        0xFE,
        (
            "嗯，接下来要讲的是……\x01",
            "简单来说，在前一段时间\x01",
            "召开的那个通商会议……\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        (
            "主要就是商定\x01",
            "经济相关方面的……\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x18,
        (
            "老师，我有点\x01",
            "听不明白啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0577
    ChrTalk(
        0xFE,
        (
            "哎，那、那我就\x01",
            "从头开始再讲一遍……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9BFF")

    label("loc_9B93")


    #C0578
    ChrTalk(
        0xFE,
        (
            "（呜呜，这个课题\x01",
            "  的难度是不是太高了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        (
            "（但、但这些知识很重要，\x01",
            "  一定要努力教给大家……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BFF")

    Jump("loc_9D83")

    label("loc_9C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9C12")
    Jump("loc_9D83")

    label("loc_9C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9C20")
    Jump("loc_9D83")

    label("loc_9C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9C2E")
    Jump("loc_9D83")

    label("loc_9C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9D5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CEB")

    #C0580
    ChrTalk(
        0xFE,
        (
            "莉丝修女好像\x01",
            "在亚尔特利亚\x01",
            "做修女已经好几年了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xFE,
        (
            "虽然她的年纪和我差不多，\x01",
            "但却远比我沉稳冷静……\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "呼，我竟然还装模作样地摆前辈架子，\x01",
            "真是太丢脸了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9D59")

    label("loc_9CEB")


    #C0583
    ChrTalk(
        0xFE,
        (
            "呼，莉丝修女竟然是\x01",
            "资历比我老好几年的前辈……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "想想当时以为有了后辈感到很开心的自己，\x01",
            "真是难为情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D59")

    Jump("loc_9D83")

    label("loc_9D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_9D6C")
    Jump("loc_9D83")

    label("loc_9D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_9D7A")
    Jump("loc_9D83")

    label("loc_9D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9D83")

    label("loc_9D83")

    TalkEnd(0xFE)
    Return()

    # Function_26_9832 end

    def Function_27_9D87(): pass

    label("Function_27_9D87")

    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0585
    ChrTalk(
        0xF,
        (
            "玛布尔修女，\x01",
            "您今天让我学会了很多东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xF,
        (
            "那个……在低年级的\x01",
            "课堂上让您看到了\x01",
            "我丢脸的场面……\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x8,
        "呵呵，不必在意哦。\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x8,
        (
            "千里之行，始于足下……\x01",
            "只要一点一滴地记住这些技巧就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_27_9D87 end

    def Function_28_9E61(): pass

    label("Function_28_9E61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E76")
    Call(0, 50)
    Jump("loc_9EDA")

    label("loc_9E76")


    #C0589
    ChrTalk(
        0x11,
        (
            "#01100F琪雅最喜欢主日学校了。\x02\x03",

            "#01109F每天都能学习到各种知识，\x01",
            "还能见到隆和亨利他们，\x01",
            "好开心！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EDA")

    TalkEnd(0xFE)
    Return()

    # Function_28_9E61 end

    def Function_29_9EDE(): pass

    label("Function_29_9EDE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F9C")

    #C0590
    ChrTalk(
        0xFE,
        (
            "呜……学习果然\x01",
            "是件麻烦事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        (
            "哥哥能不能\x01",
            "替我学习一会呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#00006F那个……学习是为了自己吧？\x01",
            "还是应该自己认真做好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xFE,
        (
            "哼，说教的口气\x01",
            "就像爸爸一样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9FC1")

    label("loc_9F9C")


    #C0594
    ChrTalk(
        0xFE,
        (
            "呜……学习果然\x01",
            "是件麻烦事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC1")

    TalkEnd(0xFE)
    Return()

    # Function_29_9EDE end

    def Function_30_9FC5(): pass

    label("Function_30_9FC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A052")
    SetChrSubChip(0x13, 0x1)
    Sleep(500)
    SetChrSubChip(0x12, 0x2)
    Sleep(500)

    #C0595
    ChrTalk(
        0xFE,
        "隆，认真学习啊。\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "再这么下去，\x01",
            "你可就要被琪雅远远抛在后面了哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x12,
        "我、我知道啦！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_A090")

    label("loc_A052")


    #C0598
    ChrTalk(
        0xFE,
        (
            "我也不能\x01",
            "光说隆。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        (
            "自己也要努力学习，\x01",
            "不能输给琪雅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A090")

    TalkEnd(0xFE)
    Return()

    # Function_30_9FC5 end

    def Function_31_A094(): pass

    label("Function_31_A094")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A159")
    OP_63(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x14)

    #C0600
    ChrTalk(
        0xFE,
        "嗯，嗯嗯……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x14, 0x1)
    Sleep(500)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)

    #C0601
    ChrTalk(
        0xFE,
        (
            "那个……琪雅……\x01",
            "这里应该怎么解呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x11,
        "#01100F嗯，这道算式啊……\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈……\x01",
            "  看来相处得很不错呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A186")

    label("loc_A159")


    #C0604
    ChrTalk(
        0xFE,
        (
            "原、原来如此……\x01",
            "只要这样就能解开了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A186")

    TalkEnd(0xFE)
    Return()

    # Function_31_A094 end

    def Function_32_A18A(): pass

    label("Function_32_A18A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A38C")

    #C0605
    ChrTalk(
        0x101,
        (
            "#00000F哦，这不是潘莎吗，\x01",
            "最近还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "是温蒂姐姐的\x01",
            "朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        (
            "大哥哥，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 6)), scpexpr(EXPR_END)), "loc_A28C")

    #C0608
    ChrTalk(
        0x105,
        "#10305F说起温蒂，好像是……\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x102,
        (
            "#00100F嗯，就是刚才在导力商店见到的\x01",
            "那位技师小姐。\x02\x03",

            "#00109F呵呵，她是罗伊德的童年玩伴哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2F2")

    label("loc_A28C")


    #C0610
    ChrTalk(
        0x105,
        "#10305F温蒂是……\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x102,
        (
            "#00100F是导力商店的\x01",
            "一位技师小姐。\x02\x03",

            "#00109F呵呵，也是罗伊德的童年玩伴哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F2")


    #C0612
    ChrTalk(
        0xFE,
        (
            "嗯，那个机械痴\x01",
            "就是我姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0x109,
        "#10112F说、说的好直接啊。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xFE,
        (
            "但事实就是如此嘛，\x01",
            "大哥哥也这么觉得吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        "#00006F（……确实无法否定呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 1)
    Jump("loc_A3DF")

    label("loc_A38C")


    #C0616
    ChrTalk(
        0xFE,
        (
            "姐姐会变成\x01",
            "那样的机械痴，\x01",
            "都是因为受爸爸的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "我可绝对不要\x01",
            "变成那样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3DF")

    TalkEnd(0xFE)
    Return()

    # Function_32_A18A end

    def Function_33_A3E3(): pass

    label("Function_33_A3E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A3F4")
    Jump("loc_A581")

    label("loc_A3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A453")

    #C0618
    ChrTalk(
        0xFE,
        "今天有弥撒哦。\x02",
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "我们平时虽然会一直玩闹，\x01",
            "但在这种时候就必须要严肃些了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A581")

    label("loc_A453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A461")
    Jump("loc_A581")

    label("loc_A461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A46F")
    Jump("loc_A581")

    label("loc_A46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A47D")
    Jump("loc_A581")

    label("loc_A47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A48B")
    Jump("loc_A581")

    label("loc_A48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_A499")
    Jump("loc_A581")

    label("loc_A499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_A4A7")
    Jump("loc_A581")

    label("loc_A4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A4B5")
    Jump("loc_A581")

    label("loc_A4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A4C3")
    Jump("loc_A581")

    label("loc_A4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A4D1")
    Jump("loc_A581")

    label("loc_A4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A4DF")
    Jump("loc_A581")

    label("loc_A4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A4ED")
    Jump("loc_A581")

    label("loc_A4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_A4FB")
    Jump("loc_A581")

    label("loc_A4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_A509")
    Jump("loc_A581")

    label("loc_A509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A581")

    #C0620
    ChrTalk(
        0xFE,
        (
            "哼，哈米尔那家伙\x01",
            "为了在琪雅面前展现优点，\x01",
            "最近一直都在认真学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xFE,
        (
            "比起学习，我还是\x01",
            "更喜欢到外边玩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A581")

    TalkEnd(0xFE)
    Return()

    # Function_33_A3E3 end

    def Function_34_A585(): pass

    label("Function_34_A585")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A596")
    Jump("loc_A6F0")

    label("loc_A596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A5D4")

    #C0622
    ChrTalk(
        0xFE,
        (
            "女神啊……\x01",
            "请您让市里的人们\x01",
            "恢复精神吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6F0")

    label("loc_A5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A5E2")
    Jump("loc_A6F0")

    label("loc_A5E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A5F0")
    Jump("loc_A6F0")

    label("loc_A5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A5FE")
    Jump("loc_A6F0")

    label("loc_A5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A60C")
    Jump("loc_A6F0")

    label("loc_A60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_A61A")
    Jump("loc_A6F0")

    label("loc_A61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_A628")
    Jump("loc_A6F0")

    label("loc_A628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A636")
    Jump("loc_A6F0")

    label("loc_A636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A644")
    Jump("loc_A6F0")

    label("loc_A644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A652")
    Jump("loc_A6F0")

    label("loc_A652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A660")
    Jump("loc_A6F0")

    label("loc_A660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A66E")
    Jump("loc_A6F0")

    label("loc_A66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_A67C")
    Jump("loc_A6F0")

    label("loc_A67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_A68A")
    Jump("loc_A6F0")

    label("loc_A68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A6F0")

    #C0623
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "琪雅好可爱啊，\x01",
            "能和她一起学习真开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0xFE,
        (
            "今天也要拼命举手，\x01",
            "多回答老师的问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6F0")

    TalkEnd(0xFE)
    Return()

    # Function_34_A585 end

    def Function_35_A6F4(): pass

    label("Function_35_A6F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A780")

    #C0625
    ChrTalk(
        0xFE,
        (
            "我喜欢购物，\x01",
            "对经济方面的知识\x01",
            "一向很有兴趣……\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "但不久前关于那场通商会议方面的知识，\x01",
            "对我们来说实在是太难了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_A7B3")

    label("loc_A780")


    #C0627
    ChrTalk(
        0xFE,
        (
            "有关通商会议的知识，\x01",
            "对我们来说实在是太难了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7B3")

    TalkEnd(0xFE)
    Return()

    # Function_35_A6F4 end

    def Function_36_A7B7(): pass

    label("Function_36_A7B7")

    TalkBegin(0xFE)

    #C0628
    ChrTalk(
        0xFE,
        (
            "如果换成亚泽尔哥哥，\x01",
            "应该就能听懂课上讲的内容了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xFE,
        (
            "等哥哥下次回家的时候，\x01",
            "我就去问问他好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_A7B7 end

    def Function_37_A828(): pass

    label("Function_37_A828")

    TalkBegin(0xFE)

    #C0630
    ChrTalk(
        0xFE,
        "唉唉……\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xFE,
        "……还是听不明白啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_A828 end

    def Function_38_A857(): pass

    label("Function_38_A857")

    TalkBegin(0xFE)

    #C0632
    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "只要开始学习，就忍不住想睡。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        (
            "但修女也在努力讲课，\x01",
            "我必须要认真听才行。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_A857 end

    def Function_39_A8B4(): pass

    label("Function_39_A8B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A94A")

    #C0634
    ChrTalk(
        0xFE,
        (
            "哼、哼……\x01",
            "不就是通商会议吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        (
            "这种程度的知识只是常识而已。\x01",
            "真是简单得可笑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        (
            "……我、我没吹牛啦！\x01",
            "我真的懂哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A9AE")

    label("loc_A94A")


    #C0637
    ChrTalk(
        0xFE,
        (
            "通商会议什么的，根本就是常识而已。\x01",
            "简单～简单……\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        (
            "……真是的，别来打扰我！\x01",
            "我正在学习呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9AE")

    TalkEnd(0xFE)
    Return()

    # Function_39_A8B4 end

    def Function_40_A9B2(): pass

    label("Function_40_A9B2")

    TalkBegin(0xFE)

    #C0639
    ChrTalk(
        0xFE,
        (
            "为了自己的将来，无论多难的知识\x01",
            "也必须要努力学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        "……大哥哥，你们有没有努力学习呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_A9B2 end

    def Function_41_AA18(): pass

    label("Function_41_AA18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_AA61")

    #C0641
    ChrTalk(
        0xFE,
        "嘿，我们一会要去哪里啊？\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        "不然还是去百货店吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAC2")

    label("loc_AA61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_AAC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA7C")
    Call(0, 42)
    Jump("loc_AAC2")

    label("loc_AA7C")


    #C0643
    ChrTalk(
        0xFE,
        (
            "（利娜莉……\x01",
            "  都怪你一直在课堂上说话，\x01",
            "  连我都被老师提醒了～）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAC2")

    TalkEnd(0xFE)
    Return()

    # Function_41_AA18 end

    def Function_42_AAC6(): pass

    label("Function_42_AAC6")


    #C0644
    ChrTalk(
        0x1F,
        (
            "修女知不知道\x01",
            "一些简单的\x01",
            "减肥秘诀呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x1E,
        (
            "你可别\x01",
            "在上课时间\x01",
            "问无聊的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x1E,
        "又会惹老师生气的。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    #C0647
    ChrTalk(
        0x8,
        (
            "呵呵，那边的两名同学，\x01",
            "在上课时请保持安静哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    Sleep(1000)

    #C0648
    ChrTalk(
        0x1F,
        "是～\x02",
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x1E,
        (
            "是、是……\x01",
            "（连我也被老师批评了……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1, 7)
    Return()

    # Function_42_AAC6 end

    def Function_43_ABB7(): pass

    label("Function_43_ABB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_ABE8")

    #C0650
    ChrTalk(
        0xFE,
        "我们还真是一直都逛不腻啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC1D")

    label("loc_ABE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_AC1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC03")
    Call(0, 42)
    Jump("loc_AC1D")

    label("loc_AC03")


    #C0651
    ChrTalk(
        0xFE,
        "（对、对不起啦……）\x02",
    )

    CloseMessageWindow()

    label("loc_AC1D")

    TalkEnd(0xFE)
    Return()

    # Function_43_ABB7 end

    def Function_44_AC21(): pass

    label("Function_44_AC21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_AC96")

    #C0652
    ChrTalk(
        0xFE,
        (
            "嗯，今天能学到关于独立的知识\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        (
            "有些知识，光读克洛斯贝尔时代周刊\x01",
            "是无法了解的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACE2")

    label("loc_AC96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_ACE2")

    #C0654
    ChrTalk(
        0xFE,
        "原来如此，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        (
            "玛布尔老师讲的课\x01",
            "果然清楚易懂啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACE2")

    TalkEnd(0xFE)
    Return()

    # Function_44_AC21 end

    def Function_45_ACE6(): pass

    label("Function_45_ACE6")

    TalkBegin(0xFE)

    #C0656
    ChrTalk(
        0xFE,
        (
            "高年级的课程\x01",
            "果然很难啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        "还好我已经认真预习过了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_ACE6 end

    def Function_46_AD2C(): pass

    label("Function_46_AD2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADCC")

    #C0658
    ChrTalk(
        0xFE,
        (
            "哎，那个叫琪雅\x01",
            "的孩子今天\x01",
            "没来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        (
            "……哦，说起来，\x01",
            "她好像只参加\x01",
            "自然科学课呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xFE,
        (
            "哎，还以为今天也能\x01",
            "看到她那可爱的小背影呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_AE2B")

    label("loc_ADCC")


    #C0661
    ChrTalk(
        0xFE,
        (
            "小琪雅一般都坐在\x01",
            "我前边的座位。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0xFE,
        (
            "一边看着她那可爱的小脑袋\x01",
            "一边听课，\x01",
            "实在是很享受呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE2B")

    TalkEnd(0xFE)
    Return()

    # Function_46_AD2C end

    def Function_47_AE2F(): pass

    label("Function_47_AE2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B04D")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0663
    ChrTalk(
        0xFE,
        "啊，是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x101,
        (
            "#00005F阿姨……\x01",
            "您在这里啊。\x02\x03",

            "#00000F塞茜尔姐姐刚才\x01",
            "来支援科了。\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        (
            "啊，是吗，\x01",
            "那我稍后可要过去看看她。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "克洛斯贝尔今后\x01",
            "将会变成什么样子呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#00003F……老实说，\x01",
            "我们的心里也充满疑惑……\x02\x03",

            "#00000F但无论未来会变成什么样子，\x01",
            "我们想要守护克洛斯贝尔\x01",
            "的意志也是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x102,
        "#00104F……嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x103,
        "#00200F那当然。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x104,
        "#00300F嗯，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        (
            "……呵呵，你们可真是\x01",
            "值得信赖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0xFE,
        (
            "嗯，多亏你们，\x01",
            "我的不安已经稍有缓和了。\x01",
            "谢谢你们特意和我打招呼哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 5)
    Jump("loc_B10E")

    label("loc_B04D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0DC")

    #C0673
    ChrTalk(
        0xFE,
        (
            "我还要在这里\x01",
            "继续祈祷一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0xFE,
        (
            "虽然还不知道克洛斯贝尔\x01",
            "今后会变成什么样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        (
            "但伟大的女神\x01",
            "一定会引导我们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B10E")

    label("loc_B0DC")

    OP_93(0xFE, 0x0, 0x0)

    #C0676
    ChrTalk(
        0xFE,
        (
            "空之女神啊……\x01",
            "请您继续守护我们吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B10E")

    TalkEnd(0xFE)
    Return()

    # Function_47_AE2F end

    def Function_48_B112(): pass

    label("Function_48_B112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B124")
    Call(0, 49)
    Jump("loc_B1A0")

    label("loc_B124")

    TalkBegin(0xFF)
    SetChrName("")

    #A0677
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "莉丝修女好像正在房间里\x01",
            "与大主教会面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0678
    ChrTalk(
        0x101,
        (
            "#00000F……我们还是先去接琪雅吧，\x01",
            "她应该就在主日学校的教室。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_B1A0")

    Return()

    # Function_48_B112 end

    def Function_49_B1A1(): pass

    label("Function_49_B1A1")

    EventBegin(0x0)
    Fade(500)
    OP_68(50010, 1500, 11920, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    SetChrPos(0x101, 49000, 0, 12340, 0)
    SetChrPos(0x102, 51000, 0, 12340, 0)
    SetChrPos(0x109, 49500, 0, 11330, 0)
    SetChrPos(0x105, 50500, 0, 11330, 0)
    SetChrFlags(0xC, 0x80)
    OP_0D()

    #C0679
    ChrTalk(
        0x102,
        (
            "#12P#00100F这里好像是\x01",
            "艾拉尔达大主教的办公室吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        (
            "#6P#00005F嗯……？\x01",
            "从里面传来了谈话的声音呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xA, 0xFF)
    LoadChrToIndex("chr/ch11500.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    OP_68(100890, 1500, 8200, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0681
    ChrTalk(
        0xA,
        (
            "#6P#13800F……那么，从今天开始\x01",
            "要请您多关照了。\x02\x03",

            "#13803F我还有很多不足之处，\x01",
            "请您今后多加鞭策教导……\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x9,
        (
            "#11P……慢着。\x01",
            "你的姓氏是『亚尔珍特』……\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x9,
        (
            "#11P我的确是接到了来自亚尔特利亚法典国\x01",
            "的联络，说有个新人要来赴任，\x01",
            "难道……\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0xA,
        (
            "#6P#13803F……莫非有什么\x01",
            "问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x9,
        "#11P…………不，没什么。\x02",
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x9,
        (
            "#11P欢迎你的到来，\x01",
            "莉丝修女。\x01",
            "今后请不断努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0xA,
        (
            "#6P#13802F谢谢您。\x02\x03",

            "#13804F在女神的指引之下，\x01",
            "我今后一定会努力工作。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_4C(0xA, 0xFF)
    OP_D7(0x1E)
    OP_68(50010, 1500, 11920, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28290, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0688
    ChrTalk(
        0x109,
        (
            "#6P#10105F这声音……\x01",
            "好像就是刚才那位莉丝小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x105,
        (
            "#12P#10304F看样子，赴任之后\x01",
            "正在拜会大主教呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0690
    ChrTalk(
        0x102,
        (
            "#12P#00103F……各位，\x01",
            "站在这里偷听可不太好啊。\x02\x03",

            "#00100F我们还是\x01",
            "赶快去接琪雅吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0691
    ChrTalk(
        0x101,
        "#5P#00000F嗯，说的对。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 50430, 0, 4030, 360)
    BeginChrThread(0xC, 0, 0, 3)
    SetScenarioFlags(0x134, 7)
    SetChrPos(0x0, 50280, 0, 12000, 180)
    EventEnd(0x5)
    Return()

    # Function_49_B1A1 end

    def Function_50_B600(): pass

    label("Function_50_B600")

    EventBegin(0x0)
    Fade(500)
    OP_68(152600, 1000, 8640, 0)
    MoveCamera(15, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(24640, 0)
    SetChrPos(0x101, 151610, 0, 8490, 90)
    SetChrPos(0x102, 151620, 0, 9490, 90)
    SetChrPos(0x109, 150550, 0, 7660, 90)
    SetChrPos(0x105, 150560, 0, 8880, 90)
    SetChrPos(0x11, 153620, 150, 9130, 270)
    SetChrSubChip(0x11, 0x1)
    OP_0D()

    #C0692
    ChrTalk(
        0x11,
        (
            "#11P#01105F啊，是罗伊德和大家。\x02\x03",

            "#01100F今天是来参观授课的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        (
            "#6P#00000F啊，不不，\x01",
            "并不是的。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x109,
        (
            "#6P#10100F小琪雅，\x01",
            "你有没有努力学习呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x11,
        (
            "#11P#01110F嗯！\x02\x03",

            "#01109F每天都能学习到各种知识，\x01",
            "还能见到隆和亨利他们，\x01",
            "好开心！\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x102,
        "#5P#00102F呵呵，是吗。\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x105,
        (
            "#6P#10300F哈，看来相处得\x01",
            "非常不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x101,
        (
            "#6P#00004F嗯，一开始还很担心……\x01",
            "结果完全没有必要。\x02\x03",

            "#00000F琪雅，要努力学习哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x11,
        (
            "#11P#01109F嗯！\x01",
            "罗伊德，你们也要\x01",
            "加油工作哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x135, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 151150, 0, 8870, 90)
    SetChrPos(0x11, 153620, 150, 9130, 0)
    SetChrSubChip(0x11, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_B600 end

    def Function_51_B885(): pass

    label("Function_51_B885")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch20400.itc", 0x1E)
    SoundLoad(3598)
    OP_68(9000, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 9500, 0, 2500, 90)
    SetChrPos(0x102, 8750, 0, 2000, 90)
    SetChrPos(0x109, 8150, 0, 3200, 90)
    SetChrPos(0x105, 7350, 0, 2750, 90)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x1E, 0x11)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x12)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrChipByIndex(0x20, 0x13)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x21, 0x14)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrChipByIndex(0x22, 0x15)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x101,
        "#00005F#5P哎……？\x02",
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x102,
        "#00105F#5P怎么了？\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#00008F#5P没什么，只是看起来\x01",
            "好像还没下课。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x52, 0xFF, 0xFF)
    SetChrPos(0x153, 151000, 200, 18000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 148500, 200, 18000, 90)
    OP_4B(0x8, 0xFF)
    OP_68(151000, 1600, 10500, 0)
    MoveCamera(324, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    OP_68(151000, 1600, 15500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0703
    ChrTalk(
        0x153,
        (
            "#01105F#5P嗯……这个算式\x01",
            "应该先这样解，然后是这样……\x02\x03",

            "#01101F…………………（用力书写）\x02\x03",

            "#01109F嗯！答案是\x01",
            "５１２平方赛尔矩！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(837, 0, 100, 0)
    SetChrName("高年级的学生们")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #A0704
    AnonymousTalk(
        0xFF,
        "#4S哇哇～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0705
    ChrTalk(
        0x8,
        "#5P很好，回答正确。\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "#5P你刚才的算法是前所未闻的，\x01",
            "难道是自己想出来的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)

    #C0707
    ChrTalk(
        0x153,
        (
            "#01104F#11P嗯！嘿嘿嘿，因为总觉得\x01",
            "这样计算的感觉比较好。\x02\x03",

            "#01110F琪雅错了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x8,
        (
            "#5P没有没有，\x01",
            "实在是非常出色的解法。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    #C0709
    ChrTalk(
        0x8,
        (
            "#11P请大家记住，所谓的公式，\x01",
            "仅仅是用于求得正确答案的\x01",
            "指针之一而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x8,
        (
            "#11P偶尔也应该保持着愉快的心情，\x01",
            "尝试用各种新的方法来解答问题。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrName("高年级的学生们")
    SetMessageWindowPos(50, 150, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0711
    AnonymousTalk(
        0xFF,
        "#4S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(9000, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 9300, 0, 2200, 45)
    SetChrPos(0x102, 9100, 0, 2950, 90)
    SetChrPos(0x109, 9000, 0, 1400, 45)
    SetChrPos(0x105, 8400, 0, 2400, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0712
    ChrTalk(
        0x101,
        "#00001F#5P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x102,
        (
            "#00108F#5P是主日学校的\x01",
            "高年级课堂啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x109,
        (
            "#10105F#6P小琪雅好厉害……\x02\x03",

            "#10106F那种题目，就算让我来解答，\x01",
            "恐怕也要花费一番工夫呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x105,
        (
            "#10304F#5P毕竟是中等数学题。\x02\x03",

            "#10302F呵呵，那种解法\x01",
            "的确很不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯，真不愧是\x01",
            "我们的琪雅啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x102,
        (
            "#00109F#5P是啊，凭小琪雅的头脑，\x01",
            "就算是那种难度的题目也……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0718
    ChrTalk(
        0x101,
        "#6P#00011F#4S#1K……不对！\x02",
    )


    #C0719
    ChrTalk(
        0x102,
        "#5P#00105F#4S#1K……不对！\x02",
    )

    OP_57(0x1)
    OP_5A()

    #C0720
    ChrTalk(
        0x105,
        (
            "#10306F#5P哎呀呀，\x01",
            "稍微冷静些啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x109,
        (
            "#10112F#6P总、总之先安静\x01",
            "等待授课结束吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(151000, 1000, 13400, 0)
    MoveCamera(312, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    SetCameraDistance(30000, 6000)
    SetChrPos(0x101, 147750, 0, 3750, 45)
    SetChrPos(0x102, 146400, 0, 4000, 45)
    SetChrPos(0x109, 146750, 0, 2850, 45)
    SetChrPos(0x105, 145500, 0, 3150, 45)
    SetChrPos(0x153, 151400, 0, 13400, 270)
    SetChrPos(0x8, 150600, 0, 13400, 90)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x1E, 0x4)
    ClearChrBattleFlags(0x1F, 0x4)
    ClearChrBattleFlags(0x20, 0x4)
    SetChrChipByIndex(0x1E, 0x17)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x18)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x1E, 150000, 0, 12000, 270)
    SetChrPos(0x1F, 150550, 0, 11100, 315)
    SetChrPos(0x20, 152000, 0, 11550, 180)
    Sleep(1000)
    FadeToBright(1000, 0)

    def lambda_C0FF():
        OP_9B(0x0, 0x20, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_C0FF)
    Sleep(1000)
    TurnDirection(0x1E, 0x1F, 500)
    Sleep(300)

    def lambda_C121():
        OP_93(0x1F, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_C121)
    Sleep(50)

    def lambda_C131():
        OP_93(0x1E, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_C131)
    WaitChrThread(0x1F, 2)

    def lambda_C142():
        OP_9B(0x0, 0x1F, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C142)
    Sleep(50)
    WaitChrThread(0x1E, 2)

    def lambda_C15E():
        OP_9B(0x0, 0x1E, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_C15E)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x20, 1)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_0D()
    OP_6F(0x79)

    #C0722
    ChrTalk(
        0x101,
        "那个，琪雅……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_C1CC():
        OP_93(0x153, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_C1CC)
    Sleep(50)

    def lambda_C1DC():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C1DC)
    OP_68(149000, 1000, 7700, 2000)
    MoveCamera(317, 22, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(35000, 2000)
    OP_6F(0x79)

    #C0723
    ChrTalk(
        0x8,
        "啊，各位……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0724
    ChrTalk(
        0x153,
        (
            "#01105F#3598V#11P#30W哎哎……\x01",
            "大家怎么都来了？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0E)
    OP_C9(0x1, 0x80000000)
    OP_68(151000, 1000, 12400, 5000)
    MoveCamera(312, 25, 0, 5000)
    SetCameraDistance(30000, 5000)

    def lambda_C296():
        OP_95(0xFE, 151400, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C296)
    Sleep(100)

    def lambda_C2B3():
        OP_95(0xFE, 150600, 0, 4000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2B3)
    Sleep(500)

    def lambda_C2D0():
        OP_95(0xFE, 151400, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C2D0)
    Sleep(100)

    def lambda_C2ED():
        OP_95(0xFE, 150600, 0, 3800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C2ED)
    WaitChrThread(0x101, 1)

    def lambda_C30B():
        OP_95(0xFE, 151400, 0, 11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C30B)
    WaitChrThread(0x102, 1)

    def lambda_C329():
        OP_95(0xFE, 150600, 0, 11300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C329)
    WaitChrThread(0x109, 1)

    def lambda_C347():
        OP_95(0xFE, 151400, 0, 10000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C347)
    WaitChrThread(0x105, 1)

    def lambda_C365():
        OP_95(0xFE, 150600, 0, 9800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C365)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x79)

    #C0725
    ChrTalk(
        0x101,
        (
            "#00006F#6P这个……因为琪雅一直没回来，\x01",
            "我们就过来接你……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x153, 500)
    Sleep(300)

    #C0726
    ChrTalk(
        0x102,
        (
            "#00102F#5P不、不过，琪雅为什么\x01",
            "会在高年级的班级上课？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0727
    ChrTalk(
        0x153,
        (
            "#01112F#11P啊……\x02\x03",

            "#01108F嗯，这个……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    #C0728
    ChrTalk(
        0x8,
        (
            "#5P莫非你还没和\x01",
            "罗伊德他们说过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x153,
        "#01106F#11P……………………（点头）\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x105,
        (
            "#10303F#6P依我看，是因为她的\x01",
            "学习能力非常强吧？\x02\x03",

            "#10300F已经足以跟上\x01",
            "高年级的课程了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 350)

    #C0731
    ChrTalk(
        0x8,
        (
            "#11P嗯，遵照她本人的意愿，\x01",
            "从不久前开始，就让她参加\x01",
            "高年级的课程了。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x8,
        (
            "#11P不过也仅限于数学等\x01",
            "自然科学课程。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        "#00008F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x102,
        (
            "#00103F#5P小琪雅的头脑\x01",
            "竟然会聪明到这种程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x153,
        (
            "#01112F#11P那个……\x01",
            "一直瞒着大家，真对不起……\x02\x03",

            "#01106F琪雅还是个小孩子，\x01",
            "却非要学习数学……\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，没必要道歉吧？\x02\x03",

            "#00002F既然琪雅有兴趣，\x01",
            "我当然不会反对。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x102,
        (
            "#00104F#5P对啊……希望你能\x01",
            "继续保持这种求知欲。\x02\x03",

            "#00102F嗯，我也赞成。\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x153,
        "#01110F#11P真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x101,
        (
            "#00004F#6P不过，也要继续和隆他们\x01",
            "一起认真听低年级的课程哦。\x02\x03",

            "#00000F来主日学校上课的目的\x01",
            "并不是只有学习知识而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x153,
        (
            "#01109F#11P嗯，我知道！\x02\x03",

            "给隆和小桃讲解他们不懂的地方，\x01",
            "我也觉得很开心！\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x101,
        "#00012F#6P是、是吗～\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x109,
        (
            "#10102F#6P小琪雅……\x01",
            "真是非常聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x8,
        (
            "#11P呵呵，多亏如此，\x01",
            "我也省了不少力气。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x8,
        (
            "#11P琪雅每周会参加\x01",
            "高年级的课程一次……\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x8,
        (
            "#11P我会好好照看她的，\x01",
            "请大家放心吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)

    #C0746
    ChrTalk(
        0x101,
        "#00002F#6P嗯，当然放心。\x02",
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        "#00104F#6P拜托您了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0748
    ChrTalk(
        0x105,
        (
            "#10304F#6P呵呵……\x01",
            "能达成一致就好。\x02\x03",

            "#10302F那我们就趁着天黑之前，\x01",
            "赶快返回支援科吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，说的对。\x02\x03",

            "#00000F玛布尔老师，\x01",
            "那我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x102,
        "#00102F#6P您辛苦了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x8, 500)
    Sleep(150)

    #C0751
    ChrTalk(
        0x153,
        "#01110F#12P老师再见！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x153, 350)

    #C0752
    ChrTalk(
        0x8,
        (
            "#5P呵呵，再见，\x01",
            "路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x8, 150800, 200, 17500, 180)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 151000, 0, 11500, 0)
    SetScenarioFlags(0x128, 0)
    OP_29(0xA1, 0x1, 0xB)
    OP_1B(0x2, 0xFF, 0xFFFF)
    SetMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_51_B885 end

    def Function_52_CA18(): pass

    label("Function_52_CA18")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(150000, 1500, 10500, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(33000, 0)
    OP_68(150000, 1500, 13500, 3000)
    SetChrPos(0x101, 9300, 0, 2200, 90)
    SetChrPos(0x102, 9000, 0, 1300, 45)
    SetChrPos(0x103, 9150, 0, 3250, 135)
    SetChrPos(0x104, 8100, 0, 2700, 90)
    SetChrPos(0x109, 7250, 0, 2150, 90)
    SetChrPos(0x105, 7800, 0, 4250, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -2500, 0, 2500, 90)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8750, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30500, 0)
    SetCameraDistance(30000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0753
    ChrTalk(
        0x101,
        (
            "#00005F#5P现在是高年级学生\x01",
            "上课的时间啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x103,
        (
            "#00200F#5P琪雅今天\x01",
            "似乎没有参加……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)

    #N0755
    NpcTalk(
        0x9,
        "充满威严的声音",
        "#4P你们有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_CC63():

        label("loc_CC63")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_CC63")

    QueueWorkItem2(0x101, 2, lambda_CC63)

    def lambda_CC75():

        label("loc_CC75")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_CC75")

    QueueWorkItem2(0x102, 2, lambda_CC75)

    def lambda_CC87():

        label("loc_CC87")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_CC87")

    QueueWorkItem2(0x103, 2, lambda_CC87)

    def lambda_CC99():

        label("loc_CC99")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_CC99")

    QueueWorkItem2(0x104, 2, lambda_CC99)

    def lambda_CCAB():

        label("loc_CCAB")

        TurnDirection(0x109, 0x9, 500)
        Yield()
        Jump("loc_CCAB")

    QueueWorkItem2(0x109, 2, lambda_CCAB)

    def lambda_CCBD():

        label("loc_CCBD")

        TurnDirection(0x105, 0x9, 500)
        Yield()
        Jump("loc_CCBD")

    QueueWorkItem2(0x105, 2, lambda_CCBD)
    Sleep(500)
    OP_68(7420, 1000, 2480, 4000)

    def lambda_CCE3():
        OP_9B(0x0, 0x9, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_CCE3)

    #C0756
    ChrTalk(
        0x101,
        "#00011F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x102,
        "#00105F#12P艾拉尔达大主教……\x02",
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x109,
        "#10112F#6P您、您辛苦了！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    #C0759
    ChrTalk(
        0x9,
        (
            "#5P你们是……\x01",
            "克洛斯贝尔的警察啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x9,
        "#5P找玛布尔修女有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        (
            "#00003F#12P是、是的。\x02\x03",

            "#00000F那个……关于某种植物，\x01",
            "有些事情想和她谈谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0762
    ChrTalk(
        0x9,
        "#5P嗯，植物啊……\x02",
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x9,
        "#5P是药草之类的植物吗？\x02",
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x102,
        (
            "#00103F#12P不，\x01",
            "并不是……\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#00300F#12P似乎是种圣典中也许\x01",
            "有所记载的植物。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x9,
        "#5P哦……？\x02",
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x9,
        (
            "#5P嗯，既然如此，\x01",
            "不如就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x9,
        (
            "#5P药草也好，或是别的什么也好，\x01",
            "我对任何植物都有一定的了解。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CFE8")

    #C0769
    ChrTalk(
        0x101,
        (
            "#00002F#12P啊，说起来……\x01",
            "当时来拿取羽扇豆草的时候，\x01",
            "多亏了您的帮忙呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D007")

    label("loc_CFE8")


    #C0770
    ChrTalk(
        0x101,
        "#00005F#12P是、是这样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_D007")


    #C0771
    ChrTalk(
        0x9,
        "#5P嗯，我先回办公室了。\x02",
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x9,
        (
            "#5P你们要是方便，\x01",
            "就过来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    OP_68(-9000, 1000, 2500, 6500)
    OP_9B(0x0, 0x9, 0x0, 0x3778, 0x8FC, 0x0)
    Sleep(250)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_D094():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_D094)
    OP_9B(0x0, 0x9, 0x0, 0x7D0, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Sleep(250)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(8750, 1000, 2500, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(31000, 0)
    OP_0D()

    #C0773
    ChrTalk(
        0x101,
        "#00001F#12P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x109,
        (
            "#10106F#6P还是老样子，\x01",
            "真是个很严肃的人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x102,
        (
            "#00100F#12P不过，机会难得，\x01",
            "我们不如去和大主教谈谈吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x105,
        "#10308F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 9000, 0, 2500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 6)
    OP_29(0xA6, 0x1, 0x7)
    OP_1B(0x2, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_52_CA18 end

    def Function_53_D202(): pass

    label("Function_53_D202")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis253.itp")
    OP_68(100000, 1000, 10600, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28000, 0)
    SetCameraDistance(27000, 1500)
    SetChrPos(0x101, 100000, 0, 2500, 0)
    SetChrPos(0x102, 101200, 0, 2250, 0)
    SetChrPos(0x103, 99000, 0, 2250, 0)
    SetChrPos(0x104, 100000, 0, 500, 0)
    SetChrPos(0x109, 101000, 0, 1000, 0)
    SetChrPos(0x105, 98750, 0, 900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 100000, 100, 10600, 180)
    SetChrChipByIndex(0x9, 0x19)
    SetChrSubChip(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0777
    ChrTalk(
        0x101,
        (
            "#00000F#2P打扰了，\x01",
            "我们是特别任务支援科的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x9,
        "#11P哦，进来吧。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(100000, 1000, 8500, 3000)
    MoveCamera(315, 22, 0, 3000)
    SetCameraDistance(30000, 3000)

    def lambda_D39B():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D39B)
    Sleep(100)

    def lambda_D3B3():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D3B3)
    Sleep(100)

    def lambda_D3CB():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D3CB)
    Sleep(100)

    def lambda_D3E3():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D3E3)
    Sleep(100)

    def lambda_D3FB():
        OP_9B(0x0, 0x109, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D3FB)
    Sleep(100)

    def lambda_D413():
        OP_9B(0x0, 0x105, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D413)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0779
    ChrTalk(
        0x9,
        "#11P我们就直奔主题好了。\x02",
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x9,
        (
            "#11P你们刚才说是一种在圣典中\x01",
            "有所记载的植物？\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#00003F#6P不，现在还\x01",
            "不能确定……\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x102,
        (
            "#00101F#6P先把至今为止的\x01",
            "事情经过说给您听吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_7D(0xFF, 0xE6, 0xDC, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(600)
    OP_64(0x9)

    #C0783
    ChrTalk(
        0x9,
        (
            "#11P……时、空、幻的气息以及\x01",
            "不可思议的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x109,
        (
            "#10106F#6P那个……和以前在报告中所提及的\x01",
            "那些出现在塔与僧院的魔兽有所不同……\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x101,
        "#00005F#5P（啊，说起来……）\x02",
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x103,
        (
            "#00200F#5P（诺艾尔上士以前曾来\x01",
            "  教会探讨过有关遗迹的问题呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x9,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x9,
        (
            "#11P刚才说的那种花……\x01",
            "你们现在带在身上吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x101,
        (
            "#00000F#6P啊，是的。\x01",
            "虽然它已经不发光了……\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Fade(250)
    Sound(812, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x4)
    OP_0D()
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0790
    AnonymousTalk(
        0x9,
        (
            "#11P#4S！！！\x02\x03",

            "……这是………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0791
    AnonymousTalk(
        0x101,
        "#00001F#6P莫非……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0792
    AnonymousTalk(
        0x109,
        "#10107F您想必是有一些头绪吧！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(300)

    #C0793
    ChrTalk(
        0x9,
        (
            "#11P……不。\x02\x03",

            "很遗憾，我完全没有头绪。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0794
    ChrTalk(
        0x101,
        "#00011F#6P什么！？\x02",
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x104,
        (
            "#00301F#6P喂喂！\x01",
            "这明显不可能吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x103,
        (
            "#00211F#6P再怎么说，您刚才的反应\x01",
            "也明显是想到了什么啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x9,
        "#11P没有就是没有。\x02",
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x9,
        (
            "#11P……虽然是我主动邀请你们过来的，\x01",
            "但现在请你们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x9,
        "#11P我还有事在身，忙得很。\x02",
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x101,
        "#00006F#6P怎、怎么能这样……\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x9,
        (
            "#11P哦，对了，就算去问\x01",
            "玛布尔修女也没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0802
    ChrTalk(
        0x9,
        (
            "#11P虽说她学识渊博，\x01",
            "但也不可能听说过这种花。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x9,
        (
            "#11P不如说，如果她听说过，\x01",
            "问题恐怕就比较严重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x109,
        "#10108F#6P这、这到底……\x02",
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x105,
        (
            "#10302F#6P……您这种说法，\x01",
            "明显就是承认自己有所了解啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x9,
        (
            "#11P不管你们怎么说，\x01",
            "我的回答也不会改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x9,
        (
            "#11P就算警备队的索妮亚司令\x01",
            "亲自拜访，结果也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x101,
        "#00013F#6P唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(250)

    #C0809
    ChrTalk(
        0x102,
        (
            "#00106F#12P……罗伊德，我们走吧。\x02\x03",

            "#00108F再问下去也是徒劳无功了。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x101,
        "#00006F#5P……明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_DB7B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB7B)
    Sleep(50)

    def lambda_DB8B():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DB8B)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    Sleep(200)

    #C0811
    ChrTalk(
        0x101,
        "#00003F#6P我们告辞了，大主教。\x02",
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x9,
        "#11P嗯，不要误会，我并没有恶意。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x6, 0x4)
    OP_68(50000, 1000, 13000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, 50000, 0, 14000, 180)
    SetChrPos(0x102, 50000, 0, 14000, 180)
    SetChrPos(0x103, 50000, 0, 14000, 180)
    SetChrPos(0x104, 50000, 0, 14000, 180)
    SetChrPos(0x109, 50000, 0, 14000, 180)
    SetChrPos(0x105, 50000, 0, 14000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 60000, 0, 3000, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_DD16():
        OP_95(0x101, 50000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD16)

    def lambda_DD30():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_DD30)
    OP_68(49820, 1000, 3570, 7000)
    MoveCamera(315, 20, 0, 7000)
    OP_6E(300, 7000)
    SetCameraDistance(30000, 7000)
    Sleep(500)

    def lambda_DD72():
        OP_95(0x102, 48800, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DD72)

    def lambda_DD8C():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_DD8C)
    Sleep(500)

    def lambda_DDA0():
        OP_95(0x103, 51000, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDA0)

    def lambda_DDBA():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_DDBA)
    Sleep(500)

    def lambda_DDCE():
        OP_95(0x104, 50000, 0, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DDCE)

    def lambda_DDE8():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_DDE8)
    Sleep(500)

    def lambda_DDFC():
        OP_95(0x109, 48750, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DDFC)

    def lambda_DE16():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_DE16)
    Sleep(500)

    def lambda_DE2A():
        OP_95(0x105, 50000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DE2A)

    def lambda_DE44():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_DE44)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x0, 0x1F4)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    def lambda_DE7B():
        OP_95(0x105, 50750, 0, 4500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DE7B)
    WaitChrThread(0x101, 1)

    def lambda_DE99():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DE99)
    WaitChrThread(0x102, 1)

    def lambda_DEAA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DEAA)
    WaitChrThread(0x103, 1)

    def lambda_DEBB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DEBB)
    WaitChrThread(0x104, 1)

    def lambda_DECC():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DECC)
    WaitChrThread(0x109, 1)

    def lambda_DEDD():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DEDD)
    WaitChrThread(0x105, 1)
    TurnDirection(0x105, 0x101, 500)
    OP_0D()
    OP_6F(0x79)

    #C0813
    ChrTalk(
        0x104,
        (
            "#00303F#11P喂喂喂……\x02\x03",

            "#00301F这未免也太\x01",
            "让人不爽了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x109,
        "#10108F#5P前、前辈……\x02",
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x103,
        (
            "#00206F#12P不过，他似乎显得\x01",
            "非常坦然呢。\x02\x03",

            "#00208F给人的感觉简直就是……\x01",
            "对我们隐瞒才是正确的做法……\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x101,
        (
            "#00006F#6P……恐怕是存在着\x01",
            "某种禁忌吧。\x02\x03",

            "#00008F而且是连玛布尔老师\x01",
            "都不了解的禁忌……\x02",
        )
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x105,
        (
            "#10304F#11P唉，但他那种说话方式\x01",
            "只会让人更加好奇啊。\x02\x03",

            "#10302F既然如此，我们干脆就把\x01",
            "所有圣典都读上一遍如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x102,
        (
            "#00106F#5P可是……圣典的数量\x01",
            "是非常惊人的……\x02\x03",

            "#00108F……我以前也读过一些圣典，\x01",
            "但那只是微不足道的一小部分而已……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    Sound(103, 0, 60, 0)

    #N0819
    NpcTalk(
        0xA,
        "女孩的声音",
        (
            "#1P#2S……在普通的圣典中，\x01",
            "恐怕并没有详细记载。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E14E():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_E14E)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0820
    ChrTalk(
        0x101,
        "#00005F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_68(52730, 1000, 3870, 2000)
    MoveCamera(326, 21, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)

    def lambda_E23C():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E23C)
    Sleep(0)

    def lambda_E24C():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E24C)
    Sleep(0)

    def lambda_E25C():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E25C)
    Sleep(0)

    def lambda_E26C():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E26C)
    Sleep(0)

    def lambda_E27C():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E27C)
    Sleep(0)

    def lambda_E28C():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E28C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_E2B1():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_E2B1)
    OP_95(0xA, 56800, 0, 3000, 2000, 0x0)
    OP_6F(0x79)

    #C0821
    ChrTalk(
        0x101,
        "#00005F#5P你是……\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x102,
        "#00105F#5P莉丝小姐……？\x02",
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0xA,
        (
            "#04403F#12P（嘘，安静……）\x02\x03",

            "#04400F（……请离开礼拜堂，\x01",
            "  到宿舍来找我。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    OP_9B(0x0, 0xA, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_E375():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_E375)
    OP_9B(0x0, 0xA, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xA, 3)
    SetChrFlags(0xA, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(49820, 1000, 3570, 2000)
    MoveCamera(315, 20, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30000, 2000)
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    Sleep(300)

    def lambda_E44F():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E44F)

    def lambda_E45C():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E45C)
    Sleep(50)

    def lambda_E46C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E46C)
    Sleep(50)

    def lambda_E47C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E47C)
    Sleep(50)

    def lambda_E48C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E48C)
    Sleep(50)

    def lambda_E49C():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E49C)
    Sleep(50)

    def lambda_E4AC():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E4AC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)

    #C0824
    ChrTalk(
        0x109,
        "#10101F#5P（怎、怎么办……？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E581")

    #C0825
    ChrTalk(
        0x101,
        (
            "#00003F#6P（记得她是『星杯骑士团』\x01",
            "  的成员……）\x02\x03",

            "#00001F（总之，我们就过去找她吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x102,
        "#00101F#5P（嗯，我同意。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_E610")

    label("loc_E581")


    #C0827
    ChrTalk(
        0x102,
        (
            "#00103F#5P（……莉丝小姐是值得信任的。）\x02\x03",

            "#00101F（她似乎有话要对我们说，\x01",
            "  赶快过去找她吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    #C0828
    ChrTalk(
        0x101,
        "#00001F#6P（……嗯，知道了。）\x02",
    )

    CloseMessageWindow()

    label("loc_E610")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 50000, 0, 2500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 7)
    OP_29(0xA6, 0x1, 0x8)
    OP_1B(0x4, 0xFF, 0xFFFF)
    EventEnd(0x5)
    Return()

    # Function_53_D202 end

    def Function_54_E655(): pass

    label("Function_54_E655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7D8")

    #C0829
    ChrTalk(
        0xD,
        (
            "哦……看你们的样子，\x01",
            "好像是遇到什么麻烦了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x101,
        (
            "#00003F（要不要邀请她来担当\x01",
            "  职业女性选秀活动中的『修女』呢……？）\x02\x03",

            "#00000F那个，不好意思。\x01",
            "有点事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0831
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人邀请对方参加\x01",
            "慈善宴会中的职业女性选秀活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0832
    ChrTalk(
        0xD,
        (
            "……这、这个……\x01",
            "没想到竟然会邀请我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0xD,
        (
            "但是……很抱歉，\x01",
            "我还有些其它的工作要做。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x101,
        (
            "#00006F是吗……\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 2)
    Jump("loc_E839")

    label("loc_E7D8")


    #C0835
    ChrTalk(
        0xD,
        (
            "真抱歉，\x01",
            "我还有些其它的工作要做。\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0xD,
        (
            "而且我也有点害怕\x01",
            "选秀时的那种气氛……\x01",
            "请容我拒绝吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E839")

    TalkEnd(0xD)
    Return()

    # Function_54_E655 end

    def Function_55_E83D(): pass

    label("Function_55_E83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA69")

    #C0837
    ChrTalk(
        0x8,
        (
            "哦……\x01",
            "大家有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x101,
        (
            "#00000F（虽然玛布尔老师\x01",
            "  也是修女……）\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x102,
        (
            "#00106F（但、但终究不能\x01",
            "  邀请老师去参加\x01",
            "  那种选秀啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x8,
        "……呵呵，难道说……\x02",
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x8,
        (
            "你们想邀请我去参加\x01",
            "职业女性选秀活动吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x8,
        (
            "我倒是听说过\x01",
            "有关那个策划\x01",
            "的传闻。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0843
    ChrTalk(
        0x101,
        (
            "#00012F这、这个……\x01",
            "原来您知道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0844
    ChrTalk(
        0x8,
        (
            "呵呵，开个玩笑啦，\x01",
            "毕竟我都这个年纪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x8,
        (
            "你们还是去找其他的修女商量吧，\x01",
            "一定会有人愿意参加的。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x102,
        (
            "#00106F唉……\x01",
            "真是拿玛布尔老师\x01",
            "没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x199, 3)
    Jump("loc_EAEE")

    label("loc_EA69")


    #C0847
    ChrTalk(
        0x8,
        (
            "那个职业女性选秀活动，\x01",
            "你们就去找其他的修女参加吧，\x01",
            "一定会有人愿意帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x8,
        (
            "呵呵，要是我再年轻些的话，\x01",
            "也许倒能当个候选人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAEE")

    TalkEnd(0x8)
    Return()

    # Function_55_E83D end

    def Function_56_EAF2(): pass

    label("Function_56_EAF2")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5600, 2000, 18210, 0)
    MoveCamera(339, 30, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(31500, 0)
    SetChrPos(0x101, -5140, 0, 19480, 315)
    SetChrPos(0x102, -5930, 0, 18250, 315)
    SetChrPos(0x103, -5840, 0, 17320, 315)
    SetChrPos(0x104, -5040, 0, 18120, 315)
    SetChrPos(0x109, -4230, 0, 18930, 315)
    SetChrPos(0x105, -4420, 0, 17290, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xA, 0x87, 0x0)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 5)), scpexpr(EXPR_END)), "loc_EC7B")

    #C0849
    ChrTalk(
        0xA,
        (
            "#04405F哦，各位\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x105,
        (
            "#10300F（职业女性选秀活动中的『修女』……\x01",
            "  让她来担当应该很不错吧……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x101,
        (
            "#00003F（说的对……问问看吧。）\x02\x03",

            "#00000F那个，有件事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F01A")

    label("loc_EC7B")


    #C0852
    ChrTalk(
        0x101,
        (
            "#00000F莉丝小姐，\x01",
            "你正在帮忙处理\x01",
            "弥撒中的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0xA,
        (
            "#04400F嗯，正是。\x02\x03",

            "#04400F……前来参加\x01",
            "这次弥撒的人似乎\x01",
            "比平时多了不少。\x02\x03",

            "重要的家园被袭击、\x01",
            "破坏的那种恐惧感……\x02\x03",

            "#04403F……我都能体会得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x102,
        "#00105F莉丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x105,
        (
            "#10303F（……她以前或许也有过\x01",
            "  类似的遭遇呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0856
    ChrTalk(
        0xA,
        (
            "#04400F（这些话只在这里说……\x01",
            "  受此次事件的影响，『封圣省』目前\x01",
            "  也在犹豫下一步的行动方针。）\x02\x03",

            "#04403F（……我打算趁还能留在克洛斯贝尔的时间里，\x01",
            "  尽可能地收集情报。）\x02\x03",

            "#04400F（各位也请随时注意\x01",
            "  事态的动向。）\x02",
        )
    )

    CloseMessageWindow()

    #C0857
    ChrTalk(
        0x103,
        "#00200F（还能留在克洛斯贝尔的时间里吗……）\x02",
    )

    CloseMessageWindow()

    #C0858
    ChrTalk(
        0x101,
        (
            "#00003F（……明白了，\x01",
            "  莉丝小姐也要多加小心。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0859
    ChrTalk(
        0xA,
        (
            "#04405F说起来……\x01",
            "大家莫非有什么事找我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x101,
        "#00012F哎，这个，嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x105,
        (
            "#10300F（呵呵，差点给忘了，\x01",
            "  职业女性选秀活动中的『修女』……\x01",
            "  让她来担当应该很不错吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0862
    ChrTalk(
        0x101,
        (
            "#00003F（说的对啊……\x01",
            "  既然已经来了，就顺便问问看吧。）\x02\x03",

            "#00000F那个，有件事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 5)

    label("loc_F01A")

    SetChrName("")

    #A0863
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人邀请对方参加\x01",
            "慈善宴会中的职业女性选秀活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0864
    ChrTalk(
        0xA,
        (
            "#04405F职业女性选秀吗……\x02\x03",

            "#04402F慈善宴会这种活动，\x01",
            "我认为是很不错的……\x01",
            "但我今天实在是很忙。\x02\x03",

            "#04406F而且，身为一名神职人员，\x01",
            "去参加那种选秀活动，终究还是有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x102,
        "#00106F唔……说的也对呢……\x02",
    )

    CloseMessageWindow()

    #C0866
    ChrTalk(
        0x104,
        (
            "#00306F唉，本以为能看到莉丝小姐\x01",
            "站在台上的身姿呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0867
    ChrTalk(
        0xA,
        (
            "#04402F呵呵……\x01",
            "不过我觉得这种活动本身\x01",
            "还是很不错的。\x02\x03",

            "除了职业女性选秀之外，\x01",
            "还有其它活动吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x109,
        "#10105F唔，除了这个活动之外……\x02",
    )

    CloseMessageWindow()

    #C0869
    ChrTalk(
        0x103,
        (
            "#00200F好像还有钢琴演奏\x01",
            "和立餐宴会。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0870
    ChrTalk(
        0xA,
        (
            "#04403F…………………………\x01",
            "各位，还是让我去参加那个\x01",
            "职业女性选秀活动吧，可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0871
    ChrTalk(
        0x101,
        (
            "#00012F这、这个……那当然没问题。\x02\x03",

            "#00004F（是被立餐宴会吸引了吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0x105,
        "#10309F（啊哈哈，看来没错。）\x02",
    )

    CloseMessageWindow()

    #C0873
    ChrTalk(
        0xA,
        (
            "#04402F那么，我暂时还要继续\x01",
            "帮忙处理弥撒的工作。\x02\x03",

            "#04404F等到活动要开始时\x01",
            "再和我联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0x101,
        "#00000F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F470")

    #C0875
    ChrTalk(
        0x101,
        (
            "#00003F好，我们总算\x01",
            "把参选者找齐了。\x02\x03",

            "#00000F这就去市民会馆，\x01",
            "向洛依先生他们报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_F470")

    SetScenarioFlags(0x199, 7)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5530, 0, 18650, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_56_EAF2 end

    def Function_57_F4A3(): pass

    label("Function_57_F4A3")

    EventBegin(0x0)
    Fade(500)
    OP_68(860, 2190, 20270, 0)
    MoveCamera(319, 24, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30010, 0)
    SetChrPos(0x101, -160, 500, 20710, 0)
    SetChrPos(0x102, -1330, 500, 20570, 0)
    SetChrPos(0x103, 1040, 500, 20540, 0)
    SetChrPos(0x104, -1100, 250, 19370, 0)
    SetChrPos(0x109, 60, 250, 19350, 0)
    SetChrPos(0x105, 1230, 250, 19340, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0876
    ChrTalk(
        0x9,
        "哦……找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0877
    ChrTalk(
        0x9,
        (
            "如果想听我讲解七耀教义，\x01",
            "我就为你们腾出一些时间好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0878
    ChrTalk(
        0x101,
        (
            "#6P#00005F不、不必了，\x01",
            "我们并不是为此而来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x102,
        (
            "#6P#00103F（怪盗Ｂ留下的那张卡片上\x01",
            "  所记载的『最耀眼的女神之光』……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(570, 3200, 26250, 3000)
    MoveCamera(325, 24, 0, 3000)
    OP_6E(300, 3000)
    SetCameraDistance(31590, 3000)
    OP_6F(0x79)

    #C0880
    ChrTalk(
        0x102,
        (
            "#6P#N#00100F（我想多半就是指\x01",
            "  透过这里的彩色玻璃\x01",
            "  而照射下来的光线。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0881
    ChrTalk(
        0x103,
        (
            "#6P#N#00203F（如果所料不差，\x01",
            "  『背受女神之光』指的就是……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(860, 2190, 20270, 2000)
    MoveCamera(319, 24, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(30010, 2000)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_6F(0x79)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0882
    ChrTalk(
        0x9,
        "搞不懂你们到底想干什么……\x02",
    )

    CloseMessageWindow()

    #C0883
    ChrTalk(
        0x9,
        (
            "如果有什么话想说，\x01",
            "不如就直截了当地说出来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0884
    ChrTalk(
        0x101,
        (
            "#6P#00012F这、这个，既然如此……\x02\x03",

            "#00000F艾拉尔达大主教，\x01",
            "能否允许我们调查一下\x01",
            "这教坛的下面呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0885
    ChrTalk(
        0x9,
        "……什么？\x02",
    )

    CloseMessageWindow()

    #C0886
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，我们一定不会做\x01",
            "奇怪的事情，请放心吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0887
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人向艾拉尔达大主教\x01",
            "做了说明之后，调查了教坛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(1025, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0888
    AnonymousTalk(
        0x101,
        "#00000F有了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(470, 2000, 10610, 0)
    MoveCamera(311, 34, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28510, 0)
    SetChrPos(0x101, -1250, 0, 11150, 0)
    SetChrPos(0x102, 150, 0, 11210, 315)
    SetChrPos(0x103, -2060, 0, 10100, 0)
    SetChrPos(0x104, -670, 0, 10170, 0)
    SetChrPos(0x109, 1000, 0, 10460, 315)
    SetChrPos(0x105, -1350, 0, 9170, 0)
    SetChrPos(0x9, 120, 0, 14230, 225)
    ClearMapObjFlags(0x5, 0x4)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x1)
    SetChrPos(0x23, -1320, 150, 12580, 0)
    OP_52(0x23, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x2)
    SetChrFlags(0x23, 0x10)
    SetChrFlags(0x23, 0x20)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1024, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x5)
    Sleep(1000)
    SetChrName("")

    #A0889
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在皮箱的内侧\x01",
            "贴着一张卡片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0890
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第四个牢笼在市外。\x01",
            "请寻找『从西方卫士们\x01",
            "脚下通过的钢铁之道』。\x07\x00\x02",
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

    #C0891
    ChrTalk(
        0x102,
        (
            "#6P#00100F这应该就是贝尔非常珍爱\x01",
            "的人偶『米丝蒂尔』。\x02",
        )
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0x105,
        (
            "#6P#10302F嗯，看来的确是真货。\x01",
            "……总算是找到第三个了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0893
    ChrTalk(
        0x9,
        (
            "这种东西到底是什么时候\x01",
            "给放进来的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0x9,
        (
            "虽然我时常有事需要暂时离开教坛，\x01",
            "但时间绝对没有长到能做出这种事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x104,
        (
            "#6P#00306F老实说，这简直可以称得上是\x01",
            "神乎其技了……\x02",
        )
    )

    CloseMessageWindow()

    #C0896
    ChrTalk(
        0x101,
        (
            "#6P#00001F卡片上的提示\x01",
            "还是一样难懂啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0897
    ChrTalk(
        0x102,
        (
            "#12P#00100F『卫士』就是字面上的意思，\x01",
            "含义是『守卫者』。\x02\x03",

            "#00103F再加上『西方的』，\x01",
            "应该就代表\x01",
            "『位于克洛斯贝尔西侧的守卫人员』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0898
    ChrTalk(
        0x109,
        (
            "#12P#10105F从『卫士』的脚下\x01",
            "通过的『钢铁之道』……\x02\x03",

            "#10106F嗯……还不是很明白呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0x103,
        "#6P#00200F大概又是某种比喻吧。\x02",
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，我想多半如此。\x02\x03",

            "#00000F总之，我们就先把这个箱子保存好，\x01",
            "继续去找下一个目标吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    #C0901
    ChrTalk(
        0x9,
        (
            "#11P怪盗Ｂ吗……\x01",
            "之前就听说过有关他的传闻，\x01",
            "如今看来，似乎是个十分恶劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FED9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FED9)
    Sleep(50)

    def lambda_FEE9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FEE9)

    #C0902
    ChrTalk(
        0x9,
        (
            "#11P身为伟大女神的仆从，\x01",
            "我绝不能容许他的肆意妄为。\x02",
        )
    )

    CloseMessageWindow()

    #C0903
    ChrTalk(
        0x9,
        (
            "#11P各位，无论如何也请\x01",
            "抓捕到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0904
    ChrTalk(
        0x101,
        "#6P#00012F我、我们会努力的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0905
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16I罗赞贝尔克人偶·Ｍ\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｍ', 1)
    SetMapObjFlags(0x5, 0x4)
    SetChrFlags(0x23, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 180, 0, 10810, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, -210, 380, 23230, 180)
    OP_29(0x7A, 0x1, 0x4)
    SetScenarioFlags(0x157, 3)
    TalkEnd(0x9)
    EventEnd(0x5)
    Return()

    # Function_57_F4A3 end

    SaveToFile()

Try(main)
