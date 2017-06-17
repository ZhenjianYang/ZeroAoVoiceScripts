from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1130.bin",                # FileName
        "c1130",                    # MapName
        "c1130",                    # Location
        0x0019,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 25, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1130",                  # 0
        "凯赛尔",                 # 1
        "诺瓦斯",                 # 2
        "夏娜",                   # 3
        "亚比",                   # 4
        "迈尔斯",                 # 5
        "尼尔森",                 # 6
        "琪雅",                   # 7
        "雷缇",                   # 8
        "凯赛尔",                 # 9
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28202.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch20300.itc",                   # 03
        "chr/ch20302.itc",                   # 04
        "chr/ch34200.itc",                   # 05
        "chr/ch34202.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch08200.itc",                   # 09
        "chr/ch45100.itc",                   # 0A
        "chr/ch20200.itc",                   # 0B
        "chr/ch29400.itc",                   # 0C
        "chr/ch45102.itc",                   # 0D
    ))

    DeclNpc(29309,   4000,    -9439,   90,   261,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(18040,   180,     -9699,   180,  261,  0x0, 0,   12,  0,   0,   0,   0,   6,   255,  0)
    DeclNpc(13199,   4000,    10529,   180,  325,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(12649,   4000,    10529,   180,  325,  0x0, 1,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7699,    150,     7980,    270,  325,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(10420,   29,      -500,    180,  389,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8699,    150,     7980,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(8699,    150,     7980,    90,   389,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(6290,    0,       8000,    1300,    7700,    1500,    7980,    0x007E, 0,  12, 0x0000)
    DeclActor(2750,    0,       11140,   1000,    2750,    1200,    11140,   0x007C, 0,  35, 0x0000)
    DeclActor(18610,   0,       -4500,   1000,    18610,   1200,    -4500,   0x007C, 0,  4,  0x0000)
    DeclActor(23750,   0,       -9500,   1000,    23750,   1200,    -9500,   0x007C, 0,  36, 0x0000)
    DeclActor(6500,    0,       -4500,   1000,    6500,    1200,    -4500,   0x007C, 0,  37, 0x0000)
    DeclActor(9300,    0,       -4500,   1000,    9300,    1200,    -4500,   0x007C, 0,  38, 0x0000)
    DeclActor(21300,   0,       -4500,   1000,    21300,   1200,    -4500,   0x007C, 0,  39, 0x0000)
    DeclActor(23750,   0,       -6600,   1000,    23750,   1200,    -6600,   0x007C, 0,  40, 0x0000)
    DeclActor(23750,   0,       -14700,  1000,    23750,   1200,    -14700,  0x007C, 0,  41, 0x0000)
    DeclActor(23750,   0,       -17600,  1000,    23750,   1200,    -17600,  0x007C, 0,  42, 0x0000)
    DeclActor(18500,   4000,    11800,   1000,    18500,   5200,    11800,   0x007C, 0,  43, 0x0000)
    DeclActor(21500,   4000,    11800,   1000,    21450,   5200,    11800,   0x007C, 0,  44, 0x0000)
    DeclActor(26400,   4000,    11800,   1000,    26400,   5200,    11800,   0x007C, 0,  45, 0x0000)
    DeclActor(29400,   4000,    11800,   1000,    29400,   5200,    11800,   0x007C, 0,  46, 0x0000)
    DeclActor(31800,   4000,    9200,    1000,    31750,   5200,    9200,    0x007C, 0,  47, 0x0000)
    DeclActor(31800,   4000,    6450,    1000,    31800,   5200,    6450,    0x007C, 0,  48, 0x0000)
    DeclActor(31800,   4000,    1440,    1000,    31800,   5200,    1440,    0x007C, 0,  49, 0x0000)
    DeclActor(31750,   4000,    -1650,   1000,    31750,   5200,    -1650,   0x007C, 0,  50, 0x0000)
    DeclActor(31750,   4000,    -6690,   1000,    31750,   5200,    -6690,   0x007C, 0,  51, 0x0000)
    DeclActor(21500,   0,       -18500,  1000,    21500,   1200,    -18500,  0x007C, 0,  52, 0x0000)
    DeclActor(18500,   0,       -18500,  1000,    18500,   1200,    -18500,  0x007C, 0,  53, 0x0000)
    DeclActor(13500,   0,       -18500,  1000,    13500,   1200,    -18500,  0x007C, 0,  54, 0x0000)
    DeclActor(10500,   0,       -18500,  1000,    10500,   1200,    -18500,  0x007C, 0,  55, 0x0000)

    ChipFrameInfo(1508, 0)                                       # 0

    ScpFunction((
        "Function_0_5E4",          # 00, 0
        "Function_1_69C",          # 01, 1
        "Function_2_725",          # 02, 2
        "Function_3_C12",          # 03, 3
        "Function_4_D0F",          # 04, 4
        "Function_5_DB8",          # 05, 5
        "Function_6_1834",         # 06, 6
        "Function_7_230C",         # 07, 7
        "Function_8_23FB",         # 08, 8
        "Function_9_25D8",         # 09, 9
        "Function_10_2DFF",        # 0A, 10
        "Function_11_2F6A",        # 0B, 11
        "Function_12_3449",        # 0C, 12
        "Function_13_34AB",        # 0D, 13
        "Function_14_3582",        # 0E, 14
        "Function_15_46CB",        # 0F, 15
        "Function_16_478A",        # 10, 16
        "Function_17_4972",        # 11, 17
        "Function_18_4AB8",        # 12, 18
        "Function_19_4B4F",        # 13, 19
        "Function_20_4CB1",        # 14, 20
        "Function_21_4F59",        # 15, 21
        "Function_22_4FF0",        # 16, 22
        "Function_23_5045",        # 17, 23
        "Function_24_5370",        # 18, 24
        "Function_25_56E0",        # 19, 25
        "Function_26_5A74",        # 1A, 26
        "Function_27_640A",        # 1B, 27
        "Function_28_6764",        # 1C, 28
        "Function_29_67B4",        # 1D, 29
        "Function_30_8DD4",        # 1E, 30
        "Function_31_9A72",        # 1F, 31
        "Function_32_9B68",        # 20, 32
        "Function_33_9DDF",        # 21, 33
        "Function_34_A428",        # 22, 34
        "Function_35_AD24",        # 23, 35
        "Function_36_B1D0",        # 24, 36
        "Function_37_B2A1",        # 25, 37
        "Function_38_B31C",        # 26, 38
        "Function_39_B39F",        # 27, 39
        "Function_40_B41A",        # 28, 40
        "Function_41_B497",        # 29, 41
        "Function_42_B53B",        # 2A, 42
        "Function_43_B5BA",        # 2B, 43
        "Function_44_B944",        # 2C, 44
        "Function_45_C154",        # 2D, 45
        "Function_46_C8D2",        # 2E, 46
        "Function_47_CBB2",        # 2F, 47
        "Function_48_D225",        # 30, 48
        "Function_49_D633",        # 31, 49
        "Function_50_DA6D",        # 32, 50
        "Function_51_DE0D",        # 33, 51
        "Function_52_E58C",        # 34, 52
        "Function_53_E636",        # 35, 53
        "Function_54_E726",        # 36, 54
        "Function_55_E816",        # 37, 55
    ))


    def Function_0_5E4(): pass

    label("Function_0_5E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_624"),
        (1, "loc_630"),
        (2, "loc_63C"),
        (3, "loc_648"),
        (4, "loc_654"),
        (5, "loc_660"),
        (6, "loc_66C"),
        (SWITCH_DEFAULT, "loc_678"),
    )


    label("loc_624")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_630")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_63C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_648")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_654")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_660")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_66C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_678")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_684")

    label("loc_69B")

    Return()

    # Function_0_5E4 end

    def Function_1_69C(): pass

    label("Function_1_69C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_724")
    OP_95(0xFE, 29310, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 9100, 1000, 0x0)
    OP_95(0xFE, 17140, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, 6840, 1000, 0x0)
    OP_95(0xFE, 27790, 4000, -9440, 1000, 0x0)
    OP_95(0xFE, 29310, 4000, -9440, 1000, 0x0)
    Jump("Function_1_69C")

    label("loc_724")

    Return()

    # Function_1_69C end

    def Function_2_725(): pass

    label("Function_2_725")

    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_774")
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C02")

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7BE")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 30720, 4000, -9860, 90)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_C02")

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7EB")
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C02")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_825")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_87B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 30720, 4000, -9860, 90)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8B9")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8F7")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_95D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 5000, 30, 8720, 90)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30740, 4000, -7340, 90)
    Jump("loc_C02")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9E6")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 19380, 20, -9760, 225)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xC, 16430, 30, -9880, 135)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0x8, 7700, 150, 7980, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A40")
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 30740, 4000, -7340, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2A")
    SetChrFlags(0xE, 0x10)

    label("loc_A2A")

    SetChrPos(0x9, 27020, 4019, -10540, 45)
    Jump("loc_C02")

    label("loc_A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A79")
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AA9")
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_B99")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_B08")
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 13560, 0, -6140, 270)
    BeginChrThread(0xD, 0, 0, 0)
    Jump("loc_B6D")

    label("loc_B08")

    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 13560, 30, -4990, 180)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 13560, 0, -6140, 0)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0x8, 7700, 150, 7980, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_B6D")

    Jump("loc_B83")

    label("loc_B72")

    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)

    label("loc_B83")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_C02")

    label("loc_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BD7")
    SetChrFlags(0xA, 0x10)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_C02")

    label("loc_BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C02")
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C11")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)

    label("loc_C11")

    Return()

    # Function_2_725 end

    def Function_3_C12(): pass

    label("Function_3_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2B")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_C31")

    label("loc_C2B")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C7A")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB9")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_CB9")

    OP_65(0x16, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CCA")
    OP_66(0x16, 0x1)

    label("loc_CCA")

    OP_65(0x15, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CDB")
    OP_66(0x15, 0x1)

    label("loc_CDB")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CEC")
    OP_66(0x2, 0x1)

    label("loc_CEC")

    OP_65(0x14, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CFD")
    OP_66(0x14, 0x1)

    label("loc_CFD")

    OP_65(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D0E")
    OP_66(0x13, 0x1)

    label("loc_D0E")

    Return()

    # Function_3_C12 end

    def Function_4_D0F(): pass

    label("Function_4_D0F")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着《一分钟烹饪·点心篇》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_DB4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『轻快爆米花』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DB4")

    TalkEnd(0xFF)
    Return()

    # Function_4_D0F end

    def Function_5_DB8(): pass

    label("Function_5_DB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E68")

    #C0003
    ChrTalk(
        0xFE,
        (
            "您好，\x01",
            "欢迎光临克洛斯贝尔图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "……唉，今天来图书馆的人\x01",
            "还是不多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "突然出现了那样的大树，\x01",
            "恐怕有很多人已经\x01",
            "连门都不愿出了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ECD")

    label("loc_E68")


    #C0006
    ChrTalk(
        0xFE,
        (
            "今天来图书馆的人\x01",
            "还是不多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "身为图书馆的管理员，\x01",
            "我会全心全意来\x01",
            "接待到此借阅图书的各位。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECD")

    Jump("loc_1830")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F50")

    #C0008
    ChrTalk(
        0xFE,
        (
            "我现在的恐惧感，\x01",
            "与猎兵袭击城市时并无二致。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "为什么会发生这样的事呢……\x01",
            "如今的心情真是充满不解和苦恼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FF2")

    #C0010
    ChrTalk(
        0xFE,
        (
            "『克洛斯贝尔独立国』……\x01",
            "走到这一步，\x01",
            "看来已经无法回头了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "在听到那种宣言之后，\x01",
            "两大国又会是什么态度呢……\x01",
            "老实说，真是太让人不安了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CC")

    #C0012
    ChrTalk(
        0xFE,
        (
            "在发生袭击的那天晚上，\x01",
            "我已经结束工作，离开了这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "听说以警察总部为中心，\x01",
            "整个行政区遭受了相当\x01",
            "恐怖的暴行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "虽然都已经过去一周了……\x01",
            "但我还是无法忘记那个\x01",
            "战火漫天的夜晚。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_113B")

    label("loc_10CC")


    #C0015
    ChrTalk(
        0xFE,
        (
            "虽然都已经过去一周了……\x01",
            "但我还是无法忘记那个\x01",
            "战火漫天的夜晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "或许这也是对\x01",
            "独立提案的一个警告吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113B")

    Jump("loc_1830")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11AA")

    #C0017
    ChrTalk(
        0xFE,
        (
            "不用说也知道……\x01",
            "警察总部现在肯定相当慌忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "但愿玛因兹那里的事件\x01",
            "能顺利解决……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_11AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1294")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1253")

    #C0019
    ChrTalk(
        0xFE,
        (
            "据说今天要在\x01",
            "市民会馆召开\x01",
            "市民讨论会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "居民投票日也已经逐渐临近了……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "有关独立的是与非……\x01",
            "大家必须要尽快\x01",
            "确定自己的意见啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_128F")

    label("loc_1253")


    #C0022
    ChrTalk(
        0xFE,
        (
            "有关独立的是与非……\x01",
            "大家必须要尽快\x01",
            "确定自己的意见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128F")

    Jump("loc_1830")

    label("loc_1294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_13A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132A")

    #C0023
    ChrTalk(
        0xFE,
        (
            "嗯，这本是学术类书籍，\x01",
            "要放到那边的书架上。这本是……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "呵呵，把书放进书柜\x01",
            "中的缝隙里，\x01",
            "竟然是一件如此开心的事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_139D")

    label("loc_132A")


    #C0025
    ChrTalk(
        0xFE,
        (
            "把书放回到书架里，\x01",
            "有点像是在做解谜游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "当把手中的书严丝合缝地\x01",
            "塞进书架里时，\x01",
            "甚至会有点感动的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139D")

    Jump("loc_1830")

    label("loc_13A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145F")

    #C0027
    ChrTalk(
        0xFE,
        (
            "您好，\x01",
            "欢迎光临克洛斯贝尔图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "如果想借阅的书籍已经\x01",
            "被其他人借出了，\x01",
            "可以来这里预约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "我和馆长都很乐于为您服务，\x01",
            "如有需要，随时可以来找我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14DA")

    label("loc_145F")


    #C0030
    ChrTalk(
        0xFE,
        (
            "如果想借阅的书籍已经\x01",
            "被其他人借出了，\x01",
            "可以来这里预约哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "我和馆长都很乐于为您服务，\x01",
            "如有需要，随时可以来找我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DA")

    Jump("loc_1830")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14ED")
    Jump("loc_1830")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1567")

    #C0032
    ChrTalk(
        0xFE,
        (
            "各国的首脑们\x01",
            "昨晚好像住在了\x01",
            "米修拉姆的迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "他们肯定在豪华的晚宴中\x01",
            "享用到了无数美食吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_1567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15E2")

    #C0034
    ChrTalk(
        0xFE,
        (
            "受通商会议的影响，\x01",
            "今天的气氛好像\x01",
            "就像庆典时期一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "呵呵，就算什么都不做，\x01",
            "心情都会变得挺愉快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_15E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1688")

    #C0036
    ChrTalk(
        0xFE,
        (
            "在听说星见之塔中\x01",
            "存有大量古文书时，\x01",
            "馆长非常高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "馆长想\x01",
            "把全部书籍\x01",
            "运到我们这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "但我们的地下书库\x01",
            "还有那么大的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E3")

    label("loc_1688")


    #C0039
    ChrTalk(
        0xFE,
        (
            "馆长似乎想把\x01",
            "所有古文书都\x01",
            "运到我们这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "但我们的地下书库\x01",
            "还有那么大的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_1830")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_175F")

    #C0041
    ChrTalk(
        0xFE,
        (
            "尼尔森先生是个自由记者，\x01",
            "听说他非常繁忙，\x01",
            "一直奔波于大陆各地。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "而这次是他时隔\x01",
            "大约三年的归乡。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_175F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_17D7")

    #C0043
    ChrTalk(
        0xFE,
        (
            "馆长因为\x01",
            "尼尔森先生今天要来，\x01",
            "高兴得一直都坐不安稳。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "他好像非常喜欢\x01",
            "和尼尔森先生聊天呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_17D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1830")

    #C0045
    ChrTalk(
        0xFE,
        (
            "您好，\x01",
            "欢迎光临克洛斯贝尔图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "如果想找什么书，\x01",
            "可以随时和我说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1830")

    TalkEnd(0xFE)
    Return()

    # Function_5_DB8 end

    def Function_6_1834(): pass

    label("Function_6_1834")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1845")
    Jump("loc_2308")

    label("loc_1845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193A")

    #C0047
    ChrTalk(
        0xFE,
        (
            "虽然有些地方还未彻底……\x01",
            "但城市的复兴工作\x01",
            "看起来已经差不多完成了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "所幸车站与空港并没有\x01",
            "遭到任何侵害，\x01",
            "我还能再来克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "袭击中把交通管道作为目标\x01",
            "是十分常见的。\x01",
            "……这样一想的话，还真是很恐怖。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19A8")

    label("loc_193A")


    #C0050
    ChrTalk(
        0xFE,
        (
            "如果想研究克洛斯贝尔的历史，\x01",
            "就必须要来这座图书馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "不过，差不多也可以\x01",
            "回列曼的研究室闭门研究了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A8")

    Jump("loc_2308")

    label("loc_19AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1AC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A49")

    #C0052
    ChrTalk(
        0xFE,
        (
            "玛因兹发生了袭击事件……\x01",
            "而且现在仍然被袭击者占领着。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "是帝国干的吗？还是共和国？\x01",
            "说心里话，我觉得\x01",
            "两边的嫌疑都很大……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AC1")

    label("loc_1A49")


    #C0054
    ChrTalk(
        0xFE,
        (
            "无论对帝国而言，还是对共和国而言，\x01",
            "玛因兹目前的状况都是最好的攻击材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "说心里话，我觉得\x01",
            "两边的嫌疑都很大……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC1")

    Jump("loc_2308")

    label("loc_1AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8E")

    #C0056
    ChrTalk(
        0xFE,
        (
            "最近这段时间，\x01",
            "克洛斯贝尔各地好像都出现了\x01",
            "与普通魔兽有所不同的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "据说那些怪物的形象\x01",
            "与教会圣典中所描述\x01",
            "的魔物十分吻合……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔究竟\x01",
            "发生了什么呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C28")

    label("loc_1B8E")


    #C0059
    ChrTalk(
        0xFE,
        (
            "如果古代塞姆里亚文明的知识\x01",
            "能流传到现在，应该就能\x01",
            "了解这些情况了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "呼，我可真是没用啊。\x01",
            "对眼前的实物视而不见，\x01",
            "却只幻想那些虚无缥缈的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C28")

    Jump("loc_2308")

    label("loc_1C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CCF")

    #C0061
    ChrTalk(
        0xFE,
        (
            "嗯，下次如果以古今东西的\x01",
            "各次独立事件为主题写一篇论文，\x01",
            "说不定会很有意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "从中发现到的共通点，\x01",
            "说不定可以解开\x01",
            "历史中存在的不少疑问呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2308")

    label("loc_1CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D86")

    #C0063
    ChrTalk(
        0xFE,
        "独立为主权国家吗……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "回顾中世纪以来\x01",
            "克洛斯贝尔的历史……\x01",
            "这样的提案也不是没有过。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "看一下近代的状况就能明白，\x01",
            "那种事当然连一次\x01",
            "都没有成功过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E26")

    label("loc_1D86")


    #C0066
    ChrTalk(
        0xFE,
        (
            "虽说如此，但在现在这个时代，\x01",
            "倒也不能断言说\x01",
            "『从前不行，现在就肯定也不行』……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "如果这个提案最终能发展为\x01",
            "震撼整个大陆的运动……\x01",
            "或许也有可能顺利进展。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E26")

    Jump("loc_2308")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E46")
    Call(0, 20)
    Jump("loc_1E49")

    label("loc_1E46")

    Call(0, 21)

    label("loc_1E49")

    Jump("loc_2308")

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF9")

    #C0068
    ChrTalk(
        0xFE,
        (
            "这孩子想找些书，\x01",
            "所以我正在帮她。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "哎呀，真是佩服啊。\x01",
            "小小年纪，\x01",
            "竟然就对历史感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "身为一名历史研究者，\x01",
            "没有比这更开心的事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F62")

    label("loc_1EF9")


    #C0071
    ChrTalk(
        0xFE,
        (
            "哎呀，真是佩服啊。\x01",
            "小小年纪，\x01",
            "竟然就对历史感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "身为一名历史研究者，\x01",
            "没有比这更开心的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F62")

    Jump("loc_2308")

    label("loc_1F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F94")
    Call(0, 7)
    Jump("loc_20C6")

    label("loc_1F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204C")

    #C0073
    ChrTalk(
        0xFE,
        "西塞姆里亚通商会议吗……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔究竟有\x01",
            "多少年没有召开过\x01",
            "如此规模的国际会议了……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "总之，这三天发生的事情\x01",
            "一定会成为大陆历史的一部分，\x01",
            "并流传至后世。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20C6")

    label("loc_204C")


    #C0076
    ChrTalk(
        0xFE,
        (
            "这三天发生的事情\x01",
            "将会成为大陆历史的一部分，\x01",
            "并流传至后世。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "可以亲身见证这种\x01",
            "重要的历史性事件，\x01",
            "实在是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C6")

    Jump("loc_2308")

    label("loc_20CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_20F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20E8")
    Call(0, 7)
    Jump("loc_20EB")

    label("loc_20E8")

    Call(0, 8)

    label("loc_20EB")

    Jump("loc_2308")

    label("loc_20F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2185")

    #C0078
    ChrTalk(
        0xFE,
        (
            "不知道是不是由于下雨的缘故，\x01",
            "研究取得了很大进展呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "也许是因为听着下雨声\x01",
            "就不会去想一些多余的事吧……\x01",
            "总之可以让我集中精神。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2308")

    label("loc_2185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227D")

    #C0080
    ChrTalk(
        0xFE,
        (
            "我是列曼自治州的\x01",
            "某所州立大学的学生，\x01",
            "专门研究历史学。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "顺便一说，我至今为止\x01",
            "已经尝试考取博士学位两次了……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "但第一次的论文不合格，彻底失败。\x01",
            "第二次又没能在期限内提交，不战而败。\x01",
            "……呼，总之就是很惨的连败。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2308")

    label("loc_227D")


    #C0083
    ChrTalk(
        0xFE,
        (
            "为了把握明年的机会，\x01",
            "我正在努力推敲论文。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "……不过，就算没有取得博士称号，\x01",
            "大学也是可以毕业的，\x01",
            "这么拼命其实可以说是有点固执了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2308")

    TalkEnd(0xFE)
    Return()

    # Function_6_1834 end

    def Function_7_230C(): pass

    label("Function_7_230C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239B")

    #C0085
    ChrTalk(
        0xFE,
        (
            "星见之塔的调查任务\x01",
            "是由你们负责的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "大量书籍突然消失不见，\x01",
            "的确让人很在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "不过，能留下一本\x01",
            "也比没有好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23FA")

    label("loc_239B")


    #C0088
    ChrTalk(
        0xFE,
        (
            "总之，能留下一本\x01",
            "也比没有好。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "我已经和迈尔斯先生说过了，\x01",
            "过一阵子准备\x01",
            "再去调查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FA")

    Return()

    # Function_7_230C end

    def Function_8_23FB(): pass

    label("Function_8_23FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2575")

    #C0090
    ChrTalk(
        0xFE,
        (
            "听说星见之塔中\x01",
            "存留着大量\x01",
            "古文书啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "书的状态\x01",
            "好像并不是很好……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "毕竟那些贵重的\x01",
            "资料一直无人管理，\x01",
            "已经放置了那么久。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "身为一名探寻历史的人，\x01",
            "对管理不力的警备队\x01",
            "真是感到十分愤怒。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x109,
        (
            "#10106F（……确实如他所说呢，\x01",
            "  真是愧疚…………）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#00303F（算啦，\x01",
            "  毕竟塔的管理工作\x01",
            "  全是由前司令负责的。）\x02\x03",

            "#00302F（我们就算有不满\x01",
            "  也没用啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25D7")

    label("loc_2575")


    #C0096
    ChrTalk(
        0xFE,
        (
            "听说星见之塔中\x01",
            "存留着大量\x01",
            "古文书啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "书的保存状态\x01",
            "好像并不是很好……\x01",
            "真希望能早点看到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D7")

    Return()

    # Function_8_23FB end

    def Function_9_25D8(): pass

    label("Function_9_25D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_266F")

    #C0098
    ChrTalk(
        0xFE,
        (
            "因为那起事件，\x01",
            "亚比感到很害怕，所以我准备\x01",
            "给他读一些开心有趣的书。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "想来想去，果然还是\x01",
            "《玛尔克与森林深处的魔女》\x01",
            "最合适啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFB")

    label("loc_266F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_267D")
    Jump("loc_2DFB")

    label("loc_267D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_280A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2765")

    #C0100
    ChrTalk(
        0xFE,
        (
            "迪塔先生的演说……\x01",
            "真是让人无比震惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "虽然也曾经隐约想过这个可能性，\x01",
            "但没想到两大国之间的暗斗\x01",
            "竟然可以如此明目张胆地展开……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "为了守护这些孩子的未来，\x01",
            "我们也只能继续坚持\x01",
            "独立主张了吧……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2805")

    label("loc_2765")


    #C0103
    ChrTalk(
        0xFE,
        (
            "虽然也曾经隐约想过这个可能性，\x01",
            "但没想到两大国之间的暗斗\x01",
            "竟然可以如此明目张胆地展开……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "为了守护这些孩子的未来，\x01",
            "我们也只能继续坚持\x01",
            "独立主张了吧……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2805")

    Jump("loc_2DFB")

    label("loc_280A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2818")
    Jump("loc_2DFB")

    label("loc_2818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_290D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B3")

    #C0105
    ChrTalk(
        0xFE,
        (
            "矿山镇那边好像发生了\x01",
            "很恐怖的事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "矿山镇里应该也有\x01",
            "很多像亚比这么大\x01",
            "的小孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "真希望大家能\x01",
            "尽早平安获救。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2908")

    label("loc_28B3")


    #C0108
    ChrTalk(
        0xFE,
        (
            "矿山镇里应该也有\x01",
            "很多像亚比这么大\x01",
            "的小孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "真希望大家能\x01",
            "尽早平安获救。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2908")

    Jump("loc_2DFB")

    label("loc_290D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_292F")

    #C0110
    ChrTalk(
        0xFE,
        "嗯，这个啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DFB")

    label("loc_292F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2978")

    #C0111
    ChrTalk(
        0xFE,
        (
            "啊，真的呢，\x01",
            "妈妈也没注意到。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "是不是去买东西了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DFB")

    label("loc_2978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29CF")

    #C0113
    ChrTalk(
        0xFE,
        (
            "小琪雅今天也在\x01",
            "认真查阅书籍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "亚比好像非常\x01",
            "羡慕她呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFB")

    label("loc_29CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7D")

    #C0115
    ChrTalk(
        0xFE,
        (
            "到了明年，我家的亚比\x01",
            "就可以去主日学校上课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "这孩子很喜欢书，\x01",
            "学习应该也会\x01",
            "很顺利吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "呵呵，在父母眼里，自己的孩子总是最出色的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2AE1")

    label("loc_2A7D")


    #C0118
    ChrTalk(
        0xFE,
        (
            "我希望能把亚比培养成\x01",
            "一个健康又正直的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "我对他并没有更多奢望，\x01",
            "只要做到这两点就够了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE1")

    Jump("loc_2DFB")

    label("loc_2AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7E")

    #C0120
    ChrTalk(
        0xFE,
        "呵呵，亚比真是聪明呢。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "好吧～那今天回家时\x01",
            "就稍微绕个远道，\x01",
            "去给你买个冰激凌吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "真的吗！？\x01",
            "太棒了！好开心！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BB3")

    label("loc_2B7E")


    #C0123
    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "要吃什么口味的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        "嗯……蜜瓜味吧！\x02",
    )

    CloseMessageWindow()

    label("loc_2BB3")

    Jump("loc_2DFB")

    label("loc_2BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C36")

    #C0125
    ChrTalk(
        0xFE,
        (
            "呵呵，亚比这孩子，\x01",
            "看揭幕式时太累了，\x01",
            "已经睡着了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "如此安祥平和的睡脸……\x01",
            "真是好可爱啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C74")

    label("loc_2C36")


    #C0127
    ChrTalk(
        0xFE,
        (
            "呵呵，亚比这孩子，\x01",
            "一副安祥平和的睡脸……\x01",
            "真是好可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C74")

    Jump("loc_2DFB")

    label("loc_2C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CE0")

    #C0128
    ChrTalk(
        0xFE,
        (
            "这个图书馆非常安静，\x01",
            "让人心情舒畅。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "而且这种古书独有的\x01",
            "味道可以让人\x01",
            "心情平静。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DFB")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6E")

    #C0130
    ChrTalk(
        0xFE,
        "随后，空之女神爱德丝流下了眼泪……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(18, 0, 70, 0)
    Sleep(300)

    #C0131
    ChrTalk(
        0xFE,
        (
            "泪水洒向大地，\x01",
            "融入世界之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "人们凝望着这副景象……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D93")

    label("loc_2D6E")


    #C0133
    ChrTalk(
        0xFE,
        (
            "人们凝望着这副景象……\x01",
            "然后……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D93")

    Jump("loc_2DFB")

    label("loc_2D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB3")
    Call(0, 10)
    Jump("loc_2DFB")

    label("loc_2DB3")


    #C0134
    ChrTalk(
        0xFE,
        (
            "我家的亚比\x01",
            "非常喜欢\x01",
            "小琪雅呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "呵呵，当然，我也很喜欢那孩子。\x02",
    )

    CloseMessageWindow()

    label("loc_2DFB")

    TalkEnd(0xFE)
    Return()

    # Function_9_25D8 end

    def Function_10_2DFF(): pass

    label("Function_10_2DFF")


    #C0136
    ChrTalk(
        0xA,
        "啊，各位是……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "啊，是琪雅姐姐的\x01",
            "哥哥和姐姐！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "哎哎，琪雅姐姐\x01",
            "今天不来吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00002F嗯，抱歉啊，\x01",
            "她今天去主日学校了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#00102F我们会帮你传话给琪雅的，\x01",
            "今天就忍耐一下好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        "嗯，知道了！\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "那就……\x01",
            "替我向琪雅姐姐\x01",
            "问声好吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#00109F呵呵，没问题。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10304F哈，她在这里\x01",
            "好像也很受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x109,
        (
            "#10102F嗯，真不愧是\x01",
            "小琪雅啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 0)
    Return()

    # Function_10_2DFF end

    def Function_11_2F6A(): pass

    label("Function_11_2F6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FA0")

    #C0146
    ChrTalk(
        0xFE,
        (
            "（兴奋）……\x01",
            "妈妈，快点讲啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2FAE")
    Jump("loc_3441")

    label("loc_2FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FF6")

    #C0147
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "大家好像都在外面说着什么，\x01",
            "到底是什么事啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_2FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3004")
    Jump("loc_3441")

    label("loc_3004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3048")

    #C0148
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "你的脸色好像不太好，\x01",
            "发生什么事了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_3048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3075")

    #C0149
    ChrTalk(
        0xFE,
        (
            "妈妈，\x01",
            "这个词是什么意思？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_3075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3102")

    #C0150
    ChrTalk(
        0xFE,
        (
            "哎，琪雅姐姐\x01",
            "是什么时候回去的？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "哎～要是早点注意到，\x01",
            "就能和她道别了……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "算、算了，反正还能再见面。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_314F")

    label("loc_3102")


    #C0153
    ChrTalk(
        0xFE,
        (
            "哎～要是早点注意到，\x01",
            "就能和她道别了……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "算、算了，反正还能再见面。\x02",
    )

    CloseMessageWindow()

    label("loc_314F")

    Jump("loc_3441")

    label("loc_3154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31B5")

    #C0155
    ChrTalk(
        0xFE,
        (
            "琪雅姐姐\x01",
            "可以一个人读懂书上的内容，\x01",
            "好厉害啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "嗯～我也要\x01",
            "努力学习才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_31B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3232")

    #C0157
    ChrTalk(
        0xFE,
        (
            "再过不久，\x01",
            "我就可以和琪雅姐姐一样，\x01",
            "去主日学校上课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "嘿嘿，要是在主日学校也能见到\x01",
            "琪雅姐姐就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_3232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3290")

    #C0159
    ChrTalk(
        0xFE,
        (
            "那个……琪雅姐姐说\x01",
            "今天要查一些资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "所以你们可不要去给\x01",
            "姐姐捣乱哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_3290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_331E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FB")

    #C0161
    ChrTalk(
        0xFE,
        "……（呼……呼……）……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "那么多人，好厉害啊……\x01",
            "……嗯嗯……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3319")

    label("loc_32FB")


    #C0163
    ChrTalk(
        0xFE,
        "……（呼……呼……）……\x02",
    )

    CloseMessageWindow()

    label("loc_3319")

    Jump("loc_3441")

    label("loc_331E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A3")

    #C0164
    ChrTalk(
        0xFE,
        (
            "妈妈说书本上\x01",
            "有一股很好闻的味道……\x01",
            "但我却闻不到。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "倒是妈妈的身上\x01",
            "一直都有很香很好闻的\x01",
            "气味呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33C6")

    label("loc_33A3")


    #C0166
    ChrTalk(
        0xFE,
        (
            "书本里真的有\x01",
            "很好闻的味道吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C6")

    Jump("loc_3441")

    label("loc_33CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33EF")

    #C0167
    ChrTalk(
        0xFE,
        "嗯嗯，然后呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3441")

    label("loc_33EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340A")
    Call(0, 10)
    Jump("loc_3441")

    label("loc_340A")


    #C0168
    ChrTalk(
        0xFE,
        (
            "帮我向琪雅姐姐\x01",
            "问好哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "我会在这里等她的。\x02",
    )

    CloseMessageWindow()

    label("loc_3441")

    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_2F6A end

    def Function_12_3449(): pass

    label("Function_12_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_345A")
    Call(0, 14)
    Jump("loc_34AA")

    label("loc_345A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_346B")
    Call(0, 13)
    Jump("loc_34AA")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_347C")
    Call(0, 14)
    Jump("loc_34AA")

    label("loc_347C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_34A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_349F")
    Call(0, 13)
    Jump("loc_34A2")

    label("loc_349F")

    Call(0, 14)

    label("loc_34A2")

    Jump("loc_34AA")

    label("loc_34A7")

    Call(0, 14)

    label("loc_34AA")

    Return()

    # Function_12_3449 end

    def Function_13_34AB(): pass

    label("Function_13_34AB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3526")

    #C0170
    ChrTalk(
        0x8,
        (
            "馆长他们今天一直在\x01",
            "调查从星见之塔内\x01",
            "发现的古文书。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "他们就像少年一样\x01",
            "兴致勃勃，\x01",
            "总觉得很可爱呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357E")

    label("loc_3526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_357E")

    #C0172
    ChrTalk(
        0x8,
        (
            "馆长真是的，\x01",
            "又和尼尔森先生\x01",
            "聊得那么投入。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "休息时间都已经\x01",
            "结束了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_357E")

    TalkEnd(0x8)
    Return()

    # Function_13_34AB end

    def Function_14_3582(): pass

    label("Function_14_3582")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 7)), scpexpr(EXPR_END)), "loc_35B5")
    Call(0, 32)
    Return()

    label("loc_35B5")

    Call(0, 30)
    Return()

    label("loc_35B9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3709")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3688")

    #C0174
    ChrTalk(
        0xC,
        (
            "城市里总算已经恢复了\x01",
            "平时的样子……\x01",
            "但还是有不少人感到不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "毕竟出现了那种诡异的大树，\x01",
            "这也是没办法的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "希望市民们暂时在家里\x01",
            "静心读读书，\x01",
            "让心情平静下来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3704")

    label("loc_3688")


    #C0177
    ChrTalk(
        0xC,
        (
            "城市里总算已经恢复了\x01",
            "平时的样子……\x01",
            "但还是有不少人感到不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "希望市民们暂时在家里\x01",
            "静心读读书，\x01",
            "让心情平静下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3704")

    Jump("loc_46C7")

    label("loc_3709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CD")
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0179
    ChrTalk(
        0xC,
        (
            "哦哦，罗伊德……\x01",
            "你没事啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00002F迈尔斯叔叔，您也是……\x01",
            "看到您平安无事，我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xC,
        "啊啊，真是的。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "当听说罗伊德被指名通缉时，\x01",
            "我非常震惊……\x01",
            "但我始终相信这里面一定有什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "迈尔斯叔叔……\x01",
            "谢谢您。\x02\x03",

            "#00001F还有很多话想和您说，\x01",
            "但现在实在是没有时间了。\x02\x03",

            "总之，在外面的情况彻底平定下来之前，\x01",
            "请您不要前往室外。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xC,
        "嗯……知道了。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "罗伊德，你们也一定\x01",
            "要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 4)
    Jump("loc_393D")

    label("loc_38CD")


    #C0186
    ChrTalk(
        0xC,
        (
            "正巧来到图书馆的\x01",
            "尼尔森先生\x01",
            "也被困在这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "真是发生了不得了的\x01",
            "状况啊……罗伊德，\x01",
            "你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_393D")

    Jump("loc_46C7")

    label("loc_3942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9D")

    #C0188
    ChrTalk(
        0xC,
        (
            "罗、罗伊德，\x01",
            "你听了吗……迪塔市长的演说……\x01",
            "还有那所谓的国防军……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00001F嗯，我们也\x01",
            "非常吃惊，\x01",
            "现在正在展开各种调查。\x02\x03",

            "总之，迈尔斯叔叔……\x01",
            "您先冷静下来，\x01",
            "继续观望情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        "啊……嗯嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xC,
        (
            "虽然很不安，\x01",
            "但首先还是要\x01",
            "冷静下来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        "罗伊德，你们也要加油。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#00002F嗯，谢谢了，迈尔斯叔叔。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B01")

    label("loc_3A9D")


    #C0194
    ChrTalk(
        0xC,
        (
            "虽然很不安，\x01",
            "但首先还是要冷静下来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "话说回来……迪塔先生为何会采取\x01",
            "如此强硬的手段呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B01")

    Jump("loc_46C7")

    label("loc_3B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B79")

    #C0196
    ChrTalk(
        0xC,
        (
            "市政厅与工商协会\x01",
            "共同举办的慈善宴会\x01",
            "似乎进展顺利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xC,
        "嗯，我稍后也要过去看看。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BC8")

    label("loc_3B79")


    #C0198
    ChrTalk(
        0xC,
        (
            "不管怎么说，对人而言，\x01",
            "互助精神是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        "嗯，我稍后也要过去看看。\x02",
    )

    CloseMessageWindow()

    label("loc_3BC8")

    Jump("loc_46C7")

    label("loc_3BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C67")

    #C0200
    ChrTalk(
        0xC,
        (
            "虽然不知道那个武装集团究竟是些什么人……\x01",
            "但真是一群愚蠢的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xC,
        (
            "竟然使用暴力来支配他人……\x01",
            "我无论如何也无法原谅这种错误的行径。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C7")

    label("loc_3C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CBF")

    #C0202
    ChrTalk(
        0xC,
        "嗯，外面下雨了啊。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "为了不让湿气进入，\x01",
            "今天就不要去\x01",
            "地下书库了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46C7")

    label("loc_3CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D1A")

    #C0204
    ChrTalk(
        0xC,
        (
            "我老婆做的盒饭\x01",
            "还是一样美味。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        "吃了之后，下午也可以继续努力工作了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_46C7")

    label("loc_3D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D35")
    Call(0, 15)
    Jump("loc_3D7B")

    label("loc_3D35")


    #C0206
    ChrTalk(
        0xC,
        (
            "哎呀呀，我竟然忘了带\x01",
            "爱妻盒饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        (
            "不过还好，\x01",
            "她帮我送过来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7B")

    Jump("loc_46C7")

    label("loc_3D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9B")
    Call(0, 20)
    Jump("loc_3D9E")

    label("loc_3D9B")

    Call(0, 21)

    label("loc_3D9E")

    Jump("loc_46C7")

    label("loc_3DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3DDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3DC9")
    Call(0, 18)
    Jump("loc_3DD5")

    label("loc_3DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_3DD5")
    Call(0, 17)

    label("loc_3DD5")

    Jump("loc_3F58")

    label("loc_3DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB2")

    #C0208
    ChrTalk(
        0xC,
        "哎呀，琪雅真是热爱学习啊。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "我们图书馆每次最多只能将\x01",
            "三册书借给一位读者，\x01",
            "真是有点不好意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xC,
        (
            "嗯，看来今后应该商讨一些新制度，\x01",
            "对借阅记录良好的爱书之人放宽限制，\x01",
            "增加他们的借阅册数。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F58")

    label("loc_3EB2")


    #C0211
    ChrTalk(
        0xC,
        (
            "我们图书馆每次最多只能将\x01",
            "三册书借给一位读者，\x01",
            "真是有点不好意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        (
            "嗯，看来今后应该商讨一些新制度，\x01",
            "对借阅记录良好的爱书之人放宽限制，\x01",
            "增加他们的借阅册数。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F58")

    Jump("loc_46C7")

    label("loc_3F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3F94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F83")
    Call(0, 18)
    Jump("loc_3F8F")

    label("loc_3F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_3F8F")
    Call(0, 17)

    label("loc_3F8F")

    Jump("loc_4122")

    label("loc_3F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4094")

    #C0213
    ChrTalk(
        0xC,
        (
            "嗯，各国的名流人士\x01",
            "果然都气度不凡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "其中，最能引起我注意的人\x01",
            "还是奥利维特皇子。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "为解决利贝尔的异变做出了贡献，\x01",
            "还乘坐『埃尔赛尤号』\x01",
            "返回帝都……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "他用与铁血宰相完全不同的\x01",
            "方式来震惊世人，\x01",
            "一举一动都能牵动别人的目光。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4122")

    label("loc_4094")


    #C0217
    ChrTalk(
        0xC,
        (
            "在各国的名流人士之中，\x01",
            "最能引起我注意的人\x01",
            "还是奥利维特皇子。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xC,
        (
            "他用与铁血宰相完全不同的\x01",
            "方式来震惊世人，\x01",
            "一举一动都能牵动别人的目光。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4122")

    Jump("loc_46C7")

    label("loc_4127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4155")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4144")
    Call(0, 18)
    Jump("loc_4150")

    label("loc_4144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4150")
    Call(0, 17)

    label("loc_4150")

    Jump("loc_46C7")

    label("loc_4155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_427F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_420B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417C")
    Call(0, 16)
    Jump("loc_4206")

    label("loc_417C")


    #C0219
    ChrTalk(
        0xC,
        (
            "自他获取菲利策奖，\x01",
            "并从而一跃成名算起，\x01",
            "都已经过去十年了……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "虽然不知道他什么时候\x01",
            "还会离开自治州，\x01",
            "但他这次回来就让我很高兴了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4206")

    Jump("loc_427A")

    label("loc_420B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_426C")

    #C0221
    ChrTalk(
        0xC,
        (
            "唔，每次尼尔森先生一来，\x01",
            "总会一不留神就聊得忘了时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        "好了，工作工作……\x02",
    )

    CloseMessageWindow()
    Jump("loc_427A")

    label("loc_426C")

    Call(0, 26)
    TalkEnd(0xC)
    OP_93(0xC, 0x10E, 0x0)
    Return()

    label("loc_427A")

    Jump("loc_46C7")

    label("loc_427F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_443D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E8")

    #C0223
    ChrTalk(
        0xC,
        (
            "今天将会有一位\x01",
            "特别的客人来访。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xC,
        "呵呵，很期待和他聊天呢。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        "#00005F特别的客人？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "嗯，是一位表现活跃\x01",
            "的国际级记者，\x01",
            "名叫尼尔森。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "看这时间，应该很快\x01",
            "就能到了……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "如果有兴趣，我可以介绍\x01",
            "给你们认识哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#00003F表现活跃的\x01",
            "国际级记者吗……\x01",
            "确实让人很感兴趣呢。\x02\x03",

            "#00002F嗯，我们要是有时间，\x01",
            "稍后还会过来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_4438")

    label("loc_43E8")


    #C0230
    ChrTalk(
        0xC,
        (
            "尼尔森先生\x01",
            "再过不久应该就到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "如果有兴趣，我可以介绍\x01",
            "给你们认识哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4438")

    Jump("loc_46C7")

    label("loc_443D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_46C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4679")

    #C0232
    ChrTalk(
        0xC,
        "哦，这不是罗伊德吗！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        (
            "和伙伴们在一起……\x01",
            "看来特别任务支援科\x01",
            "已经重新开始工作了？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#00000F嗯，托您的福，正是。\x02\x03",

            "迈尔斯叔叔以后要是有什么事，\x01",
            "欢迎随时来找\x01",
            "我们帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        "嗯，那到时候就拜托了。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "话说回来，你好像比以前\x01",
            "更加靠得住了啊。\x01",
            "我真是很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#00006F哪、哪里……\x01",
            "我还有很多不足之处呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "唔，在我看来，\x01",
            "你应该再自信一些。\x01",
            "不过，现在这样才像罗伊德啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xC,
        (
            "今后我会继续支持你们的，\x01",
            "也欢迎大家随时\x01",
            "到我家里去玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00002F嗯，\x01",
            "谢谢您，迈尔斯叔叔。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#00104F（塞茜尔小姐的父亲……\x01",
            "  真是个和蔼热情的人呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 5)
    Jump("loc_46C7")

    label("loc_4679")


    #C0242
    ChrTalk(
        0xC,
        (
            "我会一直支持你们\x01",
            "特别任务支援科的。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "也欢迎大家随时\x01",
            "到我家里去玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C7")

    TalkEnd(0xC)
    Return()

    # Function_14_3582 end

    def Function_15_46CB(): pass

    label("Function_15_46CB")


    #C0244
    ChrTalk(
        0xC,
        (
            "怎么了，老婆，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "哎呀呀，你还好意思问啊。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xF,
        (
            "呵呵，你忘带盒饭啦，\x01",
            "我给你送过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "哎！？\x01",
            "哈哈，都没注意到。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "真不好意思啊，\x01",
            "多谢你帮我送来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    Return()

    # Function_15_46CB end

    def Function_16_478A(): pass

    label("Function_16_478A")


    #C0249
    ChrTalk(
        0xC,
        (
            "嗯，罗伊德，\x01",
            "看来你们已经谈完了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        "是否聊了些有意义的事情呢？\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00004F嗯，算是吧。\x01",
            "学习到了不少东西呢。\x02\x03",

            "#00000F话说回来，\x01",
            "迈尔斯叔叔和尼尔森先生\x01",
            "早就认识了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "嗯，尼尔森先生\x01",
            "是克洛斯贝尔本地人。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "从他在克洛斯贝尔通讯社\x01",
            "工作的时候开始，\x01",
            "我们的关系就不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xC,
        (
            "顺便一说，盖伊当年\x01",
            "好像也和他来往密切呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#00002F嗯，我们已经听说了。\x02\x03",

            "#00003F（大概有点类似\x01",
            "  我们与格蕾丝小姐之间的关系吧。）\x02\x03",

            "（……当然了，尼尔森先生的性格\x01",
            "  与格蕾丝小姐却是完全不同的。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 6)
    Return()

    # Function_16_478A end

    def Function_17_4972(): pass

    label("Function_17_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A42")

    #C0256
    ChrTalk(
        0xC,
        (
            "调查位于乌尔斯拉间道尽头的\x01",
            "『星见之塔』的工作就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        (
            "那里应该存留着\x01",
            "大量古文书。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "你们帮忙确认一下，\x01",
            "将那些书籍运到图书馆\x01",
            "大概需要多少费用。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xC,
        "总之，全都拜托各位了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4AB7")

    label("loc_4A42")


    #C0260
    ChrTalk(
        0xC,
        (
            "星见之塔的位置\x01",
            "在南边的乌尔斯拉间道，\x01",
            "穿越途中的森林就可到达。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "据说塔内留存着不少古文书，\x01",
            "请你们前去调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB7")

    Return()

    # Function_17_4972 end

    def Function_18_4AB8(): pass

    label("Function_18_4AB8")


    #C0262
    ChrTalk(
        0xC,
        (
            "没能把塔内的\x01",
            "所有书籍都取回，\x01",
            "实在是万分遗憾……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "但单是这些魔导书\x01",
            "就已经十分贵重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "谢谢大家了。\x01",
            "如果以后再有什么事，还要拜托你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_4AB8 end

    def Function_19_4B4F(): pass

    label("Function_19_4B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_4B6F")
    Call(0, 28)
    Return()

    label("loc_4B6F")

    Call(0, 26)
    Return()

    label("loc_4B73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4BEF")

    #C0265
    ChrTalk(
        0xFE,
        (
            "突然下达戒严令……\x01",
            "这也算是总统已经\x01",
            "走投无路的证据吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "压制是无法长久持续的……\x01",
            "这是世间常理啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAD")

    label("loc_4BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4C8F")

    #C0267
    ChrTalk(
        0xFE,
        "………………………\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "（大陆最强的猎兵团……\x01",
            "  他们背后的势力究竟是……）\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "（如果断定为帝国在暗中操控，\x01",
            "  问题自然简单得很，可是……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAD")

    label("loc_4C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAA")
    Call(0, 20)
    Jump("loc_4CAD")

    label("loc_4CAA")

    Call(0, 21)

    label("loc_4CAD")

    TalkEnd(0xFE)
    Return()

    # Function_19_4B4F end

    def Function_20_4CB1(): pass

    label("Function_20_4CB1")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0270
    ChrTalk(
        0x9,
        (
            "嗯……这魔导书\x01",
            "果然是研究古代遗物的中世纪书籍……\x01",
            "可以这样断言。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xC,
        (
            "原来如此……\x01",
            "那关于著作者，\x01",
            "有没有比较详细的了解？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "嗯……毫无疑问，\x01",
            "肯定是曾经建造了『星见之塔』\x01",
            "的那些炼金术师留下的……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "但是，有关他们的详细信息，\x01",
            "似乎还无法了解呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x9,
        (
            "不管怎么说，\x01",
            "这些书都是很贵重的资料。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "嗯……但只剩下这几本，\x01",
            "真是让人不甘心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "说起来，那些中世纪的炼金术师\x01",
            "在当时就是极为神秘的……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xD,
        (
            "这世上未必存在能揭示\x01",
            "他们详细信息的书……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        "是的，确实如此。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "嗯～书籍一下子\x01",
            "就全部消失这件事\x01",
            "也充满谜团呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F4D")

    #C0280
    ChrTalk(
        0x101,
        (
            "#00000F（迈尔斯叔叔他们……\x01",
            "  好像正在调查\x01",
            "  我们找到的那些书啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#00100F（嗯，不过好像没有什么\x01",
            "  新的发现……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4D")

    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16B, 4)
    Return()

    # Function_20_4CB1 end

    def Function_21_4F59(): pass

    label("Function_21_4F59")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0282
    ChrTalk(
        0xC,
        (
            "唔，中世纪的炼金术师吗……\x01",
            "真是充满谜团啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xD,
        (
            "嗯，但这魔导书\x01",
            "真是很有意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        (
            "说的对，\x01",
            "应该还有解析的余地，\x01",
            "再仔细看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_21_4F59 end

    def Function_22_4FF0(): pass

    label("Function_22_4FF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500E")
    Call(0, 15)
    Jump("loc_5041")

    label("loc_500E")


    #C0285
    ChrTalk(
        0xFE,
        (
            "呵呵，我老公可真是的，\x01",
            "有时连盒饭都会忘了带。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5041")

    TalkEnd(0xFE)
    Return()

    # Function_22_4FF0 end

    def Function_23_5045(): pass

    label("Function_23_5045")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5063")
    Call(0, 25)
    Jump("loc_51B0")

    label("loc_5063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5152")

    #C0286
    ChrTalk(
        0xE,
        (
            "#01105F……啊，对了，\x01",
            "忘了去买晚饭的食材了！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，时间还很充裕呢，\x01",
            "不用那么着急啦。\x02\x03",

            "你还是慢慢挑选\x01",
            "探望小滴时\x01",
            "要带去的书吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xE,
        (
            "#01109F嗯，谢谢，罗伊德。\x02\x03",

            "#01110F不过我一定会买好东西的，\x01",
            "大家等我哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_51B0")

    label("loc_5152")


    #C0289
    ChrTalk(
        0xE,
        (
            "#01103F嗯……带什么书\x01",
            "去探望小滴好呢？\x02\x03",

            "#01109F（翻来翻去……）\x01",
            "嗯，这本好像也很有意思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B0")

    Jump("loc_536C")

    label("loc_51B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_536C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D0")
    Call(0, 24)
    Jump("loc_536C")

    label("loc_51D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52FE")

    #C0290
    ChrTalk(
        0xE,
        (
            "#01109F看啊看啊，罗伊德。\x01",
            "这本书里画着中央广场的\x01",
            "那个大钟呢。\x02\x03",

            "#01100F书上说，那个大钟原本\x01",
            "是在『太阳堡垒』的。\x02\x03",

            "#01111F嗯……那么大的钟……\x01",
            "搬运时一定会很麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，琪雅的好奇心与求知欲\x01",
            "  似乎比我们想象中的更强啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x109,
        "#10109F（呵呵，将来肯定很有前途呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_536C")

    label("loc_52FE")


    #C0293
    ChrTalk(
        0xE,
        (
            "#01100F中央广场的那个大钟，\x01",
            "原本是在『太阳堡垒』的。\x02\x03",

            "#01111F嗯……那么大的钟……\x01",
            "搬运时一定会很麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536C")

    TalkEnd(0xFE)
    Return()

    # Function_23_5045 end

    def Function_24_5370(): pass

    label("Function_24_5370")

    EventBegin(0x0)
    Fade(500)
    OP_68(29830, 4720, -6800, 0)
    MoveCamera(51, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20650, 0)
    SetChrPos(0x101, 29220, 4019, -7320, 90)
    SetChrPos(0x102, 28690, 4030, -6360, 90)
    SetChrPos(0x103, 28670, 4030, -8220, 90)
    SetChrPos(0x104, 27620, 4030, -7320, 90)
    SetChrPos(0x109, 27220, 4030, -6140, 90)
    SetChrPos(0x105, 27190, 4030, -8580, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x8, 0x0)
    OP_0D()

    #C0294
    ChrTalk(
        0xE,
        "#5P#01101F嗯嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0295
    ChrTalk(
        0xE,
        (
            "#5P#01110F啊，这个……\x01",
            "莫非……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#00002F琪雅……\x01",
            "你在查什么东西吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 500)
    Sleep(300)

    #C0297
    ChrTalk(
        0xE,
        (
            "#01109F啊，是大家。\x02\x03",

            "#01110F嗯，想找一些旧事传闻\x01",
            "方面的书籍。\x02\x03",

            "读过一册之后，\x01",
            "就越来越感兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#00102F哎，我看看……\x02\x03",

            "#00105F《克洛斯贝尔中世纪历史》，\x01",
            "《通过遗迹了解克洛斯贝尔的足迹》……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x109,
        (
            "#6P#10105F嗯，与其说是旧事传闻，\x01",
            "倒不如说是很正规的历史书籍和论文呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        "#12P#00202F琪雅好棒……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        (
            "#6P#00300F哈哈，不然你以后\x01",
            "就当个学者如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xE,
        "#01100F哎，琪雅可以吗？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x105,
        "#12P#10302F呵呵，真是疼爱孩子的家长啊。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x151, 7)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 28570, 4019, -7240, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 29310, 4000, -9440, 90)
    BeginChrThread(0x8, 0, 0, 1)
    EventEnd(0x5)
    Return()

    # Function_24_5370 end

    def Function_25_56E0(): pass

    label("Function_25_56E0")

    EventBegin(0x0)
    Fade(500)
    OP_68(29830, 4720, -6800, 0)
    MoveCamera(51, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20650, 0)
    SetChrPos(0x101, 29220, 4019, -7320, 90)
    SetChrPos(0x102, 28690, 4030, -6360, 90)
    SetChrPos(0x103, 28670, 4030, -8220, 90)
    SetChrPos(0x104, 27620, 4030, -7320, 90)
    SetChrPos(0x109, 27220, 4030, -6140, 90)
    SetChrPos(0x105, 27190, 4030, -8580, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0x10E, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x8, 0x0)
    OP_0D()

    #C0304
    ChrTalk(
        0xE,
        "#01110F啊，是大家。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#00000F琪雅，你在看书吗？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        (
            "#01109F嗯，我正在找\x01",
            "下次探望小滴时\x01",
            "要带去的书。\x02\x03",

            "#01111F选哪本好呢……\x01",
            "这一本吗？\x01",
            "好像很有意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        (
            "#00105F哎，可是……\x01",
            "那个书架上的书不是盲文书吗？\x02\x03",

            "『很有意思』，也就是说……\x01",
            "难道琪雅可以\x01",
            "读懂这些书吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xE,
        "#01105F嗯，当然啊。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#6P#00306F竟然说得\x01",
            "如此轻松……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x105,
        "#6P#10302F是在主日学校里学的吗？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        (
            "#01100F不是啦，和小滴一起玩的时候\x01",
            "就学会了。\x02\x03",

            "像《玛尔克与森林深处的魔女》\x01",
            "之类的书都有盲文版，\x01",
            "很简单的。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00005F或许是因为对普通版比较熟悉，\x01",
            "所以学起来才这么快，但还是很厉害……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        (
            "#12P#00202F呵呵，真不愧是琪雅，\x01",
            "掌握得如此迅速。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x170, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 28570, 4019, -7240, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 29310, 4000, -9440, 90)
    BeginChrThread(0x8, 0, 0, 1)
    EventEnd(0x5)
    Return()

    # Function_25_56E0 end

    def Function_26_5A74(): pass

    label("Function_26_5A74")

    EventBegin(0x0)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Fade(500)
    OP_68(12700, 1000, -5500, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 11240, 30, -5300, 90)
    SetChrPos(0x102, 11210, 20, -6440, 90)
    SetChrPos(0x109, 10000, 30, -5300, 90)
    SetChrPos(0x105, 10010, 30, -6440, 90)
    OP_0D()

    #C0314
    ChrTalk(
        0xC,
        (
            "原来如此……\x01",
            "的确是很有意思的想法呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5B3B():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5B3B)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_5C27")

    #C0315
    ChrTalk(
        0xC,
        (
            "哦哦，这不是罗伊德和大家吗。\x01",
            "你们来得正好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "这位就是我之前和你们\x01",
            "说过的尼尔森先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#00005F就是这位啊……\x02\x03",

            "#00000F您好，初次见面，\x01",
            "我是克洛斯贝尔警察局·\x01",
            "特别任务支援科的罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D49")

    label("loc_5C27")


    #C0318
    ChrTalk(
        0xC,
        "哦哦，这不是罗伊德和大家吗。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#00005F迈尔斯叔叔，这位是……？\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        "哦，他是尼尔森先生。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "是一位表现活跃的\x01",
            "国际级著名记者。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0322
    ChrTalk(
        0xC,
        (
            "尼尔森先生，\x01",
            "他们就是最近在各方面都受到好评的\x01",
            "克洛斯贝尔警察局·特别任务支援科成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00002F您好，初次见面，\x01",
            "我叫罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    label("loc_5D49")


    #C0324
    ChrTalk(
        0xD,
        (
            "哦，我听说过你们。\x01",
            "你就是队长\x01",
            "罗伊德警官……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xD,
        "呵呵，真是清澈悦耳的语声啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0326
    ChrTalk(
        0x101,
        "#00001F请容我失礼一问，莫非您的眼睛……？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xD,
        (
            "嗯，很久以前负了伤，\x01",
            "从那之后就失明了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 4570, 40, -1570, 90)
    OP_68(12490, 1000, -4720, 3000)
    MoveCamera(45, 24, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(21000, 3000)
    OP_95(0x8, 13110, 30, -2100, 2000, 0x0)
    Sleep(100)
    TurnDirection(0x8, 0xC, 500)
    OP_6F(0x79)

    #C0328
    ChrTalk(
        0x8,
        (
            "馆长，您怎么\x01",
            "还在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "休息时间已经\x01",
            "结束很久了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 500)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0330
    ChrTalk(
        0xC,
        (
            "抱歉，一不留神，\x01",
            "又聊得忘了时间。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0331
    ChrTalk(
        0xC,
        (
            "情况如你所见，不好意思，\x01",
            "我要继续工作了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    #C0332
    ChrTalk(
        0xD,
        (
            "嗯，如果有机会，\x01",
            "我们下次再交换情报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "好的，随时欢迎\x01",
            "你过来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x102, 500)

    #C0334
    ChrTalk(
        0xC,
        (
            "罗伊德，还有各位，\x01",
            "你们和尼尔森先生继续聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#00005F啊，嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_5FE2():
        OP_95(0x8, 24560, 4019, 80, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5FE2)
    OP_93(0xC, 0x0, 0x1F4)
    OP_95(0xC, 13110, 30, -2100, 2000, 0x0)

    def lambda_6017():
        OP_95(0xC, 4570, 40, -1570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_6017)
    Sleep(1000)
    OP_68(12280, 1000, -5990, 2000)
    OP_6F(0x1)

    #C0336
    ChrTalk(
        0x102,
        "#00105F那个……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xD,
        (
            "哦，我先正式做个\x01",
            "自我介绍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "初次见面，\x01",
            "我是一名自由记者，\x01",
            "名叫尼尔森。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        "#00000F您好，请多指教。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        (
            "#00108F（尼尔森先生……\x01",
            "  好像曾在哪里\x01",
            "  听到过这个名字……）\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xD,
        (
            "唔，其实我早就想与支援科\x01",
            "的各位见个面了，\x01",
            "这次相会，真是倍感荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        (
            "突然提出请求，实在失礼，\x01",
            "其实我有件事情希望得到\x01",
            "各位的协助……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        "可以稍微占用你们一点时间吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0344
    ChrTalk(
        0x101,
        "#00005F没问题，请问是什么事呢？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xD,
        (
            "其实我正在\x01",
            "对那起教团事件\x01",
            "进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xD,
        (
            "但对于部分情况\x01",
            "还有不明之处。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xD,
        (
            "各位身为解决此事件的功劳者，\x01",
            "对详情非常了解，\x01",
            "因此希望你们能接受我的采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x109,
        "#10101F有关教团事件的采访吗……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，听他的口气，\x01",
            "好像已经掌握到不少情况了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x102,
        (
            "#00101F（罗伊德，怎么办？）\x02\x03",

            "（毕竟是教团事件，\x01",
            "  可不能把一些不该说的\x01",
            "　事情说漏嘴了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00001F（唔……）\x02\x03",

            "#00003F（不过，通过配合采访，\x01",
            "  说不定能将那次的事件\x01",
            "  重新整理一下……）\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetChrChipByIndex(0x8, 0x0)
    SetChrPos(0x8, 29310, 4000, -9440, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 7700, 150, 7980, 270)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Return()

    # Function_26_5A74 end

    def Function_27_640A(): pass

    label("Function_27_640A")

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
            "接受尼尔森的采访\x01",      # 0
            "再考虑一下\x01",            # 1
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
        (0, "loc_6476"),
        (1, "loc_6697"),
        (SWITCH_DEFAULT, "loc_6763"),
    )


    label("loc_6476")


    #C0352
    ChrTalk(
        0x101,
        (
            "#00001F明白了，\x01",
            "我们愿意接受您的采访。\x02\x03",

            "只不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xD,
        (
            "嗯，我明白，各位也有自己的立场。\x01",
            "如果是不便透露的内容，\x01",
            "我自然不会硬加追问。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xD,
        (
            "另外，此次采访为非正式性质，\x01",
            "不会对外公开。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        (
            "#00002F原来如此……\x01",
            "多谢您的理解。\x02\x03",

            "#00005F不过，地点要选在哪里呢？\x01",
            "这里似乎不太方便吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xD,
        (
            "嗯，那就请大家移步到\x01",
            "二层的谈话区如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "我认为那里是很合适的场所，\x01",
            "如果有人过来，马上就能察觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#00000F的确如此，\x01",
            "那我们就赶快去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(128, 3000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【有关教团事件的协助采访】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6E, 0x4, 0x2)
    StopBGM(0xBB8)
    WaitBGM()
    Call(0, 29)
    Jump("loc_6763")

    label("loc_6697")


    #C0360
    ChrTalk(
        0x101,
        (
            "#00006F抱歉，\x01",
            "我们现在还有其它任务要处理……\x02\x03",

            "#00001F稍后再接受您的采访可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "好的，我还要在\x01",
            "这里待上一段时间，\x01",
            "并不着急。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xD,
        (
            "等你们有空的时候，\x01",
            "随时可以来找我。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_675B")
    EventEnd(0x5)

    label("loc_675B")

    SetScenarioFlags(0x133, 3)
    Jump("loc_6763")

    label("loc_6763")

    Return()

    # Function_27_640A end

    def Function_28_6764(): pass

    label("Function_28_6764")

    TalkBegin(0xD)

    #C0363
    ChrTalk(
        0xD,
        "……是罗伊德警官啊。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "有关教团事件，\x01",
            "可以接受我的采访吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Call(0, 27)
    TalkEnd(0xD)
    Return()

    # Function_28_6764 end

    def Function_29_67B4(): pass

    label("Function_29_67B4")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0xD, 0xD)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)
    OP_68(28650, 5020, -15570, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20760, 0)
    SetChrPos(0xD, 30640, 4100, -17100, 270)
    SetChrPos(0x101, 25380, 4100, -17100, 90)
    SetChrPos(0x102, 25380, 4100, -15900, 90)
    SetChrPos(0x109, 26700, 4100, -18660, 0)
    SetChrPos(0x105, 28500, 4100, -18680, 0)
    PlayBGM("ed7516", 0)
    Sound(128, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0365
    ChrTalk(
        0xD,
        (
            "#11P感谢大家配合\x01",
            "我的采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xD,
        (
            "#11P那么，我们首先来整理一下\x01",
            "事件的基本状况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xD,
        (
            "#11P所谓的Ｄ∴Ｇ教团，\x01",
            "以否定女神、\x01",
            "崇拜恶魔为教义。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xD,
        (
            "#11P自十几年前开始，\x01",
            "在大陆各地不断绑架幼童，\x01",
            "是最恶劣的犯罪集团。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xD,
        (
            "#11P这一系列的绑架事件，\x01",
            "一直持续到了六年前\x01",
            "才宣告结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xD,
        (
            "当时各方势力共同发动\x01",
            "大规模的作战行动，\x01",
            "击溃了散布于大陆各地的教团据点……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xD,
        (
            "#11P至于发动那次作战行动的势力，\x01",
            "各位应该有所了解吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        "#00003F#6P嗯，那是——\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K六年前，对Ｄ∴Ｇ教团\x01",
            "发起作战的势力是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "各国的军队与警察组织\x01",      # 0
            "各国的游击士协会\x01",          # 1
            "以上两者\x01",                  # 2
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
        (0, "loc_6B3F"),
        (1, "loc_6BBB"),
        (2, "loc_6C3D"),
        (SWITCH_DEFAULT, "loc_6C87"),
    )


    label("loc_6B3F")


    #C0374
    ChrTalk(
        0x101,
        (
            "#00000F#6P应该是各国的军队和警察组织吧？\x02\x03",

            "#00006F……不，不止如此。\x02\x03",

            "#00001F我听说各国的游击士协会\x01",
            "也参与了行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C87")

    label("loc_6BBB")


    #C0375
    ChrTalk(
        0x101,
        (
            "#00000F#6P好像是各国的游击士协会吧？\x02\x03",

            "#00006F……不，显然不止如此。\x02\x03",

            "#00001F我听说各国的军队和警察组织\x01",
            "也都参与了行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C87")

    label("loc_6C3D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0376
    ChrTalk(
        0x101,
        (
            "#00001F#6P是各国的军队和警察组织，\x01",
            "以及游击士协会吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C87")

    label("loc_6C87")


    #C0377
    ChrTalk(
        0x102,
        (
            "#00100F#6P嗯，鉴于事件的规模\x01",
            "过于庞大，专门建立了国际性\x01",
            "的搜查体制呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        "#11P不错，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xD,
        (
            "#11P而在这联合搜查体制之中，\x01",
            "由游击士卡西乌斯·布莱特\x01",
            "担任总指挥——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0380
    ChrTalk(
        0x102,
        (
            "#00105F#6P抱、抱歉，\x01",
            "可以稍微打断您一下吗？\x02\x03",

            "#00101F卡西乌斯·布莱特……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x109,
        (
            "#10111F#12P莫、莫非……\x01",
            "就是利贝尔王国军的司令\x01",
            "卡西乌斯准将吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xD,
        "#11P嗯，正是。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xD,
        (
            "#11P他当年退出王国军之后，\x01",
            "曾以游击士的身份大展身手约十年左右，\x01",
            "之后再度回归到了王国军。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x105,
        (
            "#10302F#12P呵，此人的经历\x01",
            "相当有趣嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x102,
        (
            "#00106F#6P先、先不说这个……\x02\x03",

            "#00108F我之前竟然一直都没察觉到，\x01",
            "说起『布莱特』，难道……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯，我在一科研修的过程中，\x01",
            "看到相关资料时也吃了一惊呢。\x02\x03",

            "#00001F卡西乌斯·布莱特准将\x01",
            "正是艾丝蒂尔·布莱特的父亲。\x02\x03",

            "而约修亚似乎是卡西乌斯准将的养子。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    #C0387
    ChrTalk(
        0x102,
        "#00105F#6P果、果然如此……\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x109,
        "#10105F#12P真是预料之外的联系呢……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x105,
        (
            "#10304F#11P在追逐竞赛的时候，\x01",
            "我就感觉到她不是平凡之辈了……\x02\x03",

            "#10302F但没想到竟是那种\x01",
            "超级名人的女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xD,
        (
            "#11P哦，原来各位认识卡西乌斯准将\x01",
            "的女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xD,
        (
            "#11P我身为一名记者，\x01",
            "对她的活跃表现也有一定了解……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(50)

    #C0392
    ChrTalk(
        0x101,
        "#00002F#6P嗯，有过不少来往。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#00106F#6P实在抱歉，\x01",
            "打断了您的话……\x02\x03",

            "#00100F请您继续说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xD,
        "#11P嗯，那我就继续了。\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xD,
        (
            "#11P就这样，在游击士\x01",
            "卡西乌斯·布莱特的总指挥下，\x01",
            "逮捕作战正式展开……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        (
            "#11P经过此次作战，\x01",
            "教团的势力大约\x01",
            "被毁灭了九成左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xD,
        (
            "#11P顺便一说，\x01",
            "克洛斯贝尔地区派出参加当年那场\x01",
            "行动的小组是警察局的赛尔盖班。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xD,
        (
            "#11P其中包括现在担任你们特别任务\x01",
            "支援科科长的赛尔盖先生，\x01",
            "以及两名能力出众的新人——\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        (
            "#11P也就是亚里欧斯·马克莱因，\x01",
            "还有罗伊德警官的哥哥\x01",
            "盖伊先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#00003F#6P……看来您对\x01",
            "此事件调查得\x01",
            "相当深入啊。\x02\x03",

            "#00008F而且连我和大哥的关系都……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        (
            "#00105F#6P这些情报，\x01",
            "就算在警察局内部，\x01",
            "也只有一部分人才了解……\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "#11P哦，做我们这个职业的，\x01",
            "只要做得久，在各界都会积累\x01",
            "一定的人脉关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xD,
        (
            "#11P而且我当年曾多次\x01",
            "采访过盖伊先生，\x01",
            "彼此之间的关系很亲近。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        "#00005F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        (
            "#11P……嗯，盖伊先生在世时，\x01",
            "曾给过我很多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xD,
        (
            "#11P……唔，\x01",
            "还是言归正传吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xD,
        (
            "#11P除了以上三人之外，克洛斯贝尔\x01",
            "还有一个人参与了那次行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xD,
        (
            "#11P那就是以民间顾问的身份\x01",
            "参与协助的律师\x01",
            "伊安·格里姆伍德。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "#11P伊安律师当时就\x01",
            "以对人权问题十分了解\x01",
            "而著名。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xD,
        (
            "#11P据说他曾帮忙收集各国被绑架者的情报，\x01",
            "做出了不小的贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x102,
        (
            "#00104F#6P如此说来，律师自己\x01",
            "好像也曾提到过此事呢。\x02\x03",

            "#00100F原来如此，是以那种形式参与的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xD,
        (
            "#11P另外，据说教会的人员\x01",
            "与某个神秘组织也\x01",
            "暗中介入到了此事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xD,
        (
            "#11P在他们的行动之下，\x01",
            "教团的残余势力也被彻底驱逐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#00003F#6P（教会的人员吗……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    #C0415
    ChrTalk(
        0x109,
        (
            "#10101F#12P（的确，在阿尔泰尔据点\x01",
            "  遇到的凯文神父\x01",
            "  也说曾参与过击溃教团据点呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        (
            "#00101F#6P（而那个所谓的神秘组织，\x01",
            "  应该就是指『结社』吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x105,
        (
            "#10302F#11P（呵呵，二者都是些\x01",
            "  神秘莫测的家伙啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xD,
        "#11P嗯……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(50)

    #C0419
    ChrTalk(
        0xD,
        (
            "#11P总之，\x01",
            "就这样，教团事件\x01",
            "本应得到终结。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xD,
        (
            "#11P但就在几个月之前，\x01",
            "却发现事件并没有\x01",
            "彻底结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xD,
        "#11P其理由正如各位所知……\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，因为教团的残党\x01",
            "约亚西姆·琼塔\x01",
            "的真实身份浮出了水面。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xD,
        "#11P不错，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xD,
        (
            "#11P顺便一问，他似乎对教团中的\x01",
            "种种内幕都有很详细的了解……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xD,
        (
            "#11P莫非约亚西姆·琼塔就是\x01",
            "教团的首领吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0426
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K约亚西姆·琼塔\x01",
            "是Ｄ∴Ｇ教团的首领吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "正是如此\x01",                # 0
            "是一名干部祭司\x01",          # 1
            "只是普通的教团成员\x01",      # 2
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
        (0, "loc_79E0"),
        (1, "loc_7A74"),
        (2, "loc_7ABC"),
        (SWITCH_DEFAULT, "loc_7B4D"),
    )


    label("loc_79E0")


    #C0427
    ChrTalk(
        0x101,
        (
            "#00001F#6P正是如此，他就是\x01",
            "教团的真正首领。\x02\x03",

            "#00011F（……不对吧？\x01",
            "  我在胡说些什么。）\x02\x03",

            "#00006F……并非如此，\x01",
            "他是教团中的一名干部祭司。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B4D")

    label("loc_7A74")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0428
    ChrTalk(
        0x101,
        (
            "#00001F#6P不，并非如此，\x01",
            "他是教团中的一名干部祭司。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B4D")

    label("loc_7ABC")


    #C0429
    ChrTalk(
        0x101,
        (
            "#00001F#6P不，他只是一名普通的教团成员。\x02\x03",

            "#00011F（……不对吧？\x01",
            "  我在胡说些什么。）\x02\x03",

            "#00006F……并非如此，\x01",
            "他是教团中的一名干部祭司。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B4D")

    label("loc_7B4D")


    #C0430
    ChrTalk(
        0x102,
        (
            "#00103F#6P嗯，他本人也曾\x01",
            "亲口承认过这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#00003F#6P另外，他还有研究者这一重身份，\x01",
            "兼任多项实验的负责人。\x02\x03",

            "#00001F正因如此，他才会对教团的\x01",
            "种种内情都有详尽了解。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xD,
        "#11P唔，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xD,
        (
            "#11P由于拥有如此身份，所以他能掌握到\x01",
            "在各地举行的仪式中所取得的成果，\x01",
            "并以此为基础，不断进行研究……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xD,
        (
            "#11P在六年前的逮捕行动中，\x01",
            "他成功逃脱，随后隐瞒身份，\x01",
            "暂时潜伏。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xD,
        (
            "#11P之后，他以哈尔特曼前议长\x01",
            "在『乐园』的劣行为把柄，\x01",
            "从此扎根在了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xD,
        (
            "#11P最后，他终于完成了\x01",
            "有着『真之睿智』之名\x01",
            "的药物——『真知』。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xD,
        (
            "#11P虽然细微之处尚不了解……\x01",
            "但他应该是为了完成教团的夙愿。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x102,
        (
            "#00101F#6P教团的夙愿……\x02\x03",

            "#00108F（他的确是说过\x01",
            "  要让小琪雅成为\x01",
            "  『神』之类的话……）\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        (
            "#00008F#6P（嗯，服用过红色『真知』的\x01",
            "  约亚西姆似乎还看到了\x01",
            "  一些东西……）\x02\x03",

            "#00006F（但我们直到最后\x01",
            "  也没能详细了解呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xD,
        (
            "#11P……唔，虽然仍有\x01",
            "很多不明了的地方…… \x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xD,
        (
            "#11P但通过刚才的谈话，\x01",
            "我已经将事件概要\x01",
            "基本整理完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xD,
        (
            "#11P那么，接下来就要到最后的问题了，\x01",
            "也就是有关Ｄ∴Ｇ教团的起源。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xD,
        (
            "#11P我想研究一下教团的起源，\x01",
            "可以请大家协助吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#00005F#6P教团的起源……\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xD,
        (
            "#11P是的，顺便一问，\x01",
            "罗伊德警官认为教团的历史\x01",
            "可以追溯到多少年以前？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0446
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KＤ∴Ｇ教团的历史\x01",
            "可以追溯到多少年以前？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "一千二百年前\x01",      # 0
            "五百年前\x01",          # 1
            "五十年前\x01",          # 2
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
        (0, "loc_8079"),
        (1, "loc_814A"),
        (2, "loc_8196"),
        (SWITCH_DEFAULT, "loc_824A"),
    )


    label("loc_8079")


    #C0447
    ChrTalk(
        0x101,
        (
            "#00008F#6P（一千二百年前……\x01",
            "  不对，就算事实真是如此，\x01",
            "  我们也没有任何根据。）\x02\x03",

            "#00003F（根据我们目前为止所得到的情报，\x01",
            "  可以断言的是……）\x02\x03",

            "#00001F大约可以追溯到五百年前——\x01",
            "也就是中世纪时期吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824A")

    label("loc_814A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0448
    ChrTalk(
        0x101,
        (
            "#00001F#6P大约可以追溯到五百年前——\x01",
            "也就是中世纪时期。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824A")

    label("loc_8196")


    #C0449
    ChrTalk(
        0x101,
        (
            "#00011F#6P（五十年前……\x01",
            "  不对，不可能那么近吧。）\x02\x03",

            "#00003F（根据我们目前为止所得到的情报，\x01",
            "  可以断言的是……）\x02\x03",

            "#00001F大约可以追溯到五百年前——\x01",
            "也就是中世纪时期吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824A")

    label("loc_824A")


    #C0450
    ChrTalk(
        0xD,
        "#11P唔，这个结论有何根据呢？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        (
            "#00003F#6P……其实是约亚西姆\x01",
            "亲口告诉我们的。\x02\x03",

            "#00008F五百年前，此地曾经存在着\x01",
            "一个炼金术师集团。\x02\x03",

            "#00001F据说教团自那时开始，\x01",
            "就利用了他们的技术。\x02\x03",

            "#00006F至于教团更加久远的情况，\x01",
            "目前仍然不明……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xD,
        (
            "#11P原来如此，约亚西姆·琼塔\x01",
            "还透露了这样的信息……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xD,
        (
            "#11P存在于此地的炼金术师……\x01",
            "也就是建造了『星见之塔』的\x01",
            "那些人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xD,
        (
            "#11P仅在古老传闻中才听说过的事，\x01",
            "竟然以这样的形式得到了证实……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x105,
        "#10304F#12P呵呵，的确很让人吃惊呢。\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xD,
        (
            "#11P唔，如此考虑的话，\x01",
            "罗伊德警官与各位\x01",
            "收留的那名少女……\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xD,
        (
            "#11P应该也是出生于\x01",
            "那个时代的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x101,
        "#00013F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x102,
        (
            "#00108F#6P您对这个事件\x01",
            "究竟了解到了什么程度？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xD,
        (
            "#11P抱歉，我刚才的发言\x01",
            "稍微有些不妥。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xD,
        (
            "#11P那只是我结合了自己手中的情报\x01",
            "与各位透露给我的信息之后，\x01",
            "突然涌现出来的『猜想』。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xD,
        (
            "#11P我可以向女神发誓，\x01",
            "绝不会对外散布这件事，\x01",
            "还请大家放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        "#00006F#6P言、言重了……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    #C0464
    ChrTalk(
        0xD,
        (
            "#11P……嗯，那么，\x01",
            "采访就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xD,
        (
            "#11P今天真是\x01",
            "多谢各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xD,
        (
            "#11P多亏你们，\x01",
            "我得到了很有意义的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x102,
        "#00104F#6P……哪里，彼此彼此。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)

    #C0468
    ChrTalk(
        0xD,
        (
            "#11P都已经这么晚了，\x01",
            "必须要尽快去下一个\x01",
            "采访地点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xD,
        "#11P那么，我就此告辞。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xD,
        (
            "#11P希望以后还有\x01",
            "和大家聊天的机会。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xD, 0xA)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 30000, 4030, -17070, 270)
    OP_0D()
    Sleep(500)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_87B9():
        OP_95(0xD, 28680, 4019, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_87B9)
    OP_68(27600, 5000, 300, 8600)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    OP_6F(0x1)

    def lambda_8802():
        OP_95(0xD, 9240, -490, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_8802)
    OP_68(23120, 4000, 0, 6000)
    Sleep(6500)
    Fade(500)
    SetChrFlags(0xD, 0x80)
    OP_68(28410, 4420, -15830, 0)
    MoveCamera(59, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20710, 0)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    OP_0D()

    #C0471
    ChrTalk(
        0x109,
        (
            "#10105F#12P虽说眼睛看不见，\x01",
            "但脚步非常轻快呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x105,
        "#10300F#11P嗯，的确了不起。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        (
            "#00006F#6P该怎么说呢……\x01",
            "真是个很让人吃惊的人呢。\x02\x03",

            "#00000F有关琪雅的问题，\x01",
            "应该可以相信他说的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x102,
        "#00108F#5P是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    Sleep(500)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0475
    ChrTalk(
        0x102,
        "#00105F#5P啊！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)

    #C0476
    ChrTalk(
        0x101,
        "#00005F#12P怎么了？艾莉。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        (
            "#00101F#5P我终于想起来了，\x01",
            "刚才那个人是玛鲁塞尔·尼尔森——\x02\x03",

            "在十年前左右曾得到过菲利策奖，\x01",
            "出身于克洛斯贝尔的\x01",
            "著名记者。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0478
    ChrTalk(
        0x105,
        (
            "#10305F#11P啊，虽然我了解得并不详细，\x01",
            "但菲利策奖不就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯，每年授予\x01",
            "最优秀记者的\x01",
            "国际性大奖。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x109,
        (
            "#10101F#12P原来如此……\x01",
            "怪不得他有那么强的洞察力啊。\x02\x03",

            "#10105F不过，既然出身于克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#00103F#5P嗯，他原来\x01",
            "应该在克洛斯贝尔通讯社\x01",
            "做过记者。\x02\x03",

            "#00108F之后，在当时的一次战地现场报道，\x01",
            "也就是之后让他获奖的那次报道中\x01",
            "受伤失明了。\x02\x03",

            "#00100F不过，他在那之后仍然\x01",
            "巡游于大陆各地，积极报道采访，\x01",
            "向很多杂志投稿。\x02\x03",

            "#00104F在新闻界，可以算是\x01",
            "一位人尽皆知的人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x105,
        (
            "#10302F#11P呵，如此说来，\x01",
            "还真是个了不起的大人物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#00004F#12P尼尔森先生吗……\x02\x03",

            "#00000F如果以后有机会的话，\x01",
            "不妨再和他聊聊吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0484
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【有关教团事件的协助采访】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D57")
    OP_2C(0x6E, 0x2)
    Jump("loc_8D6B")

    label("loc_8D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6B")
    OP_2C(0x6E, 0x1)

    label("loc_8D6B")

    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 27640, 4030, -13760, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x6E, 0x1, 0x0)
    OP_29(0x6E, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_29_67B4 end

    def Function_30_8DD4(): pass

    label("Function_30_8DD4")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis345.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EFC")
    SetChrPos(0x101, 5000, 30, 8000, 90)
    SetChrPos(0x102, 5000, 30, 9000, 90)
    SetChrPos(0x103, 5000, 30, 7000, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_8F5B")

    label("loc_8EFC")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_8F5B")

    FadeToBright(1000, 0)
    OP_0D()

    #C0485
    ChrTalk(
        0x101,
        "#00000F您好，迈尔斯叔叔。\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xC,
        (
            "哦，罗伊德，\x01",
            "莫非是来接受\x01",
            "委托的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        (
            "#00002F嗯，正是。\x02\x03",

            "如果现在方便，\x01",
            "可以把事情告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x102,
        (
            "#00100F好像是要回收残留在\x01",
            "星见之塔内的古文书吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xC,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xC,
        (
            "乌尔斯拉间道的尽头\x01",
            "有个名为『星见之塔』的遗迹，\x01",
            "你们应该知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xC,
        (
            "警备队以前曾下达过禁令，\x01",
            "禁止一般人进去调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        (
            "但最近已经有了变化，只要得到许可，\x01",
            "就可以进入塔内调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x109,
        (
            "#10103F嗯，确实听说过\x01",
            "此事呢。\x02\x03",

            "#10100F警备队的前任司令在未经调查的情况下\x01",
            "就将那个地方放置不理……\x02\x03",

            "不过因为\x01",
            "最近里面已经\x01",
            "没有魔兽出没了。\x02\x03",

            "所以现在哪怕是民间人士，\x01",
            "提交报告之后也可进入调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x101,
        "#00005F哎，是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92EB")

    #C0495
    ChrTalk(
        0xC,
        (
            "嗯，就在前几天，\x01",
            "尼尔森先生趁此机会\x01",
            "进去调查了一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xC,
        (
            "他在里面发现了\x01",
            "很有意思的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x101,
        (
            "#00000F那位记者先生……\x02\x03",

            "#00005F可、可是，尼尔森先生\x01",
            "的眼睛不是……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xC,
        (
            "哦，这个嘛……\x01",
            "当时有克洛斯贝尔时代周刊\x01",
            "的记者与他同行。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        "不过他的确是个行动力很强的人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9531")

    label("loc_92EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_9427")

    #C0500
    ChrTalk(
        0xC,
        (
            "嗯，就在前几天，\x01",
            "尼尔森先生趁此机会\x01",
            "进去调查了一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xC,
        (
            "他在里面发现了\x01",
            "很有意思的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x101,
        (
            "#00000F尼尔森先生……\x01",
            "就是迈尔斯叔叔之前提到过的\x01",
            "那位记者吧？\x02\x03",

            "竟然特意前往\x01",
            "那种场所调查，\x01",
            "真是个行动力很强的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        (
            "嗯，其实他的眼睛\x01",
            "已经失明了……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xC,
        (
            "当时有克洛斯贝尔时代周刊\x01",
            "的记者与他同行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9531")

    label("loc_9427")


    #C0505
    ChrTalk(
        0xC,
        (
            "嗯，前几天，我认识的一位\x01",
            "名叫尼尔森的记者就趁此机会\x01",
            "进入调查了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "他在里面发现了\x01",
            "很有意思的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000F哎，竟然特意前往\x01",
            "那种场所调查，\x01",
            "真是个行动力很强的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xC,
        (
            "嗯，其实他的眼睛\x01",
            "已经失明了……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xC,
        (
            "当时有克洛斯贝尔时代周刊\x01",
            "的记者与他同行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9531")


    #C0510
    ChrTalk(
        0x105,
        (
            "#10300F『很有意思的东西』就是\x01",
            "在委托中提到的『古文书』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x104,
        (
            "#00303F如此说来……\x01",
            "当时在追寻『银』的时候，\x01",
            "好像是见到过那种东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)

    #A0512
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300F『星见之塔』\x01",
            "的最上层与途中某层\x01",
            "都摆放着巨大的书架……\x02\x03",

            "委托中所指的就是\x01",
            "存放在那里面的古文书吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)

    #C0513
    ChrTalk(
        0xC,
        (
            "哦哦！原来你们去过啊！\x01",
            "既然如此，说起来可就简单了。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xC,
        (
            "得知如此贵重的古文书\x01",
            "一直被弃置在那种地方，\x01",
            "图书馆自然不能坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        "如何，可以拜托你们帮忙吗？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#00103F的确，保存珍贵书籍\x01",
            "也是图书馆的重要职责之一……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x109,
        (
            "#10101F不过……那么多的书，\x01",
            "如果光靠我们几个来搬运，\x01",
            "终究是不可能的吧？\x02\x03",

            "#10106F如果硬要搬运，\x01",
            "不知道要往返跑多少趟呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        "#00005F说、说的也是啊。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xC,
        (
            "哦哦，当然不会向你们\x01",
            "提出那么过分的要求啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xC,
        (
            "只是希望你们去做一番调查，\x01",
            "估算搬运那些书籍大概需要多少\x01",
            "人力和费用，也就是事前准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xC,
        (
            "至于警备队与市政厅，\x01",
            "都已经表示许可了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_993B")

    #C0522
    ChrTalk(
        0x103,
        "#00202F原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x105,
        (
            "#10300F之后会以我们的调查结果为基础，\x01",
            "制定回收书籍的计划吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_999A")

    label("loc_993B")


    #C0524
    ChrTalk(
        0x105,
        (
            "#10304F原来如此，是这样啊。\x02\x03",

            "#10300F之后会以我们的调查结果为基础，\x01",
            "制定回收书籍的计划吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_999A")


    #C0525
    ChrTalk(
        0x102,
        (
            "#00100F我们曾经登上过那座塔，\x01",
            "的确可以算是最合适\x01",
            "的人选呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xC,
        "如何，可以接受这个委托吗？\x02",
    )

    CloseMessageWindow()
    OP_29(0x71, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A16")
    Call(0, 33)

    label("loc_9A16")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A50")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_9A5A")

    label("loc_9A50")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9A5A")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_8DD4 end

    def Function_31_9A72(): pass

    label("Function_31_9A72")

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
            "接受\x01",      # 0
            "放弃\x01",      # 1
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
        (0, "loc_9ACC"),
        (1, "loc_9AD1"),
        (SWITCH_DEFAULT, "loc_9B67"),
    )


    label("loc_9ACC")

    Jump("loc_9B67")

    label("loc_9AD1")


    #C0527
    ChrTalk(
        0x101,
        (
            "#00000F抱歉，迈尔斯叔叔，\x01",
            "我们现在太忙，\x01",
            "实在无暇分身……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xC,
        (
            "嗯～是这样啊。\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xC,
        (
            "既然如此，\x01",
            "等你们有空之后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x152, 7)
    Jump("loc_9B67")

    label("loc_9B67")

    Return()

    # Function_31_9A72 end

    def Function_32_9B68(): pass

    label("Function_32_9B68")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C64")
    SetChrPos(0x101, 5000, 30, 8000, 90)
    SetChrPos(0x102, 5000, 30, 9000, 90)
    SetChrPos(0x103, 5000, 30, 7000, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_9CC3")

    label("loc_9C64")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9CC3")

    FadeToBright(1000, 0)
    OP_0D()

    #C0530
    ChrTalk(
        0xC,
        (
            "希望你们帮忙调查\x01",
            "放置在『星见之塔』\x01",
            "的古文书。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "主要任务是估算搬运书籍大约需要多少\x01",
            "人力和费用，以便让我们做好事前准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xC,
        "如何，可以接受这个委托吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D83")
    Call(0, 33)

    label("loc_9D83")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DBD")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_9DC7")

    label("loc_9DBD")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9DC7")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_9B68 end

    def Function_33_9DDF(): pass

    label("Function_33_9DDF")


    #C0533
    ChrTalk(
        0x101,
        (
            "#00002F嗯，明白了，\x01",
            "我们接受委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xC,
        "谢谢，这可帮大忙啦。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xC,
        (
            "那就请稍等一下，\x01",
            "我现在就和警备队联络，\x01",
            "让他们解除星见之塔的封锁。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x109,
        (
            "#10100F啊，这件事就\x01",
            "交给我好了。\x02\x03",

            "我直接和索妮亚司令联络\x01",
            "会更省时间。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EB9():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9EB9)
    Sleep(50)

    def lambda_9EC9():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9EC9)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EF4")

    def lambda_9EE9():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9EE9)
    Sleep(50)

    label("loc_9EF4")


    def lambda_9EF9():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9EF9)
    Sleep(50)

    def lambda_9F09():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9F09)
    Sleep(300)

    #C0537
    ChrTalk(
        0x104,
        (
            "#00300F也对，\x01",
            "还是这样更快。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xC,
        "哦，那就拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x10E, 0x1F4)
    Sleep(300)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("索妮亚的声音")

    #A0539
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──你好，\x01",
            "我是索妮亚·贝尔茨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0540
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10100F司令，您辛苦了，\x01",
            "我是诺艾尔·希卡。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("索妮亚的声音")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，诺艾尔，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0542
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10103F嗯，是这样……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0543
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "诺艾尔将接受委托，准备前往\x01",
            "星见之塔调查的事情做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("索妮亚的声音")

    #A0544
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，是那件事啊。\x02\x03",

            "他们和我也打过招呼。\x01",
            "你们的确可以算是\x01",
            "最佳人选呢。\x02\x03",

            "我马上就联络在周边地区\x01",
            "巡逻的部队，\x01",
            "让他们解除封锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0545
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10101F是，谢谢您！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("索妮亚的声音")

    #A0546
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查时要多加小心哦。\x01",
            "……就这样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x1, 0x3)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Sound(802, 0, 100, 0)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_93(0x109, 0x10E, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)

    #C0547
    ChrTalk(
        0x109,
        "#10100F……嗯，这样就行了。\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        "#00002F谢谢了，诺艾尔。\x02",
    )

    CloseMessageWindow()

    def lambda_A288():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A288)
    Sleep(50)

    def lambda_A298():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A298)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2C3")

    def lambda_A2B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2B8)
    Sleep(50)

    label("loc_A2C3")


    def lambda_A2C8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2C8)
    Sleep(50)

    def lambda_A2D8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A2D8)
    Sleep(300)

    #C0549
    ChrTalk(
        0xC,
        (
            "呼，这么顺利\x01",
            "就搞定了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xC,
        (
            "交际面如此广，\x01",
            "真不愧是特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，过奖。\x02\x03",

            "那我们这就出发，\x01",
            "前往星见之塔吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x101,
        (
            "#00004F嗯，同意。\x02\x03",

            "#00002F迈尔斯叔叔，\x01",
            "您就等我们的好消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xC,
        "嗯，要小心啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0554
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查塔内的古文书】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x71, 0x1, 0x1)
    SetScenarioFlags(0x153, 0)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_33_9DDF end

    def Function_34_A428(): pass

    label("Function_34_A428")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4F1")
    SetChrPos(0x101, 5000, 30, 8000, 90)
    SetChrPos(0x102, 5000, 30, 9000, 90)
    SetChrPos(0x103, 5000, 30, 7000, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_A550")

    label("loc_A4F1")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_A550")

    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0555
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将书架中的书\x01",
            "消失不见的情况向迈尔斯做了报告。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0556
    ChrTalk(
        0x101,
        "#00003F……情况就是这样。\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xC,
        (
            "难、难道说……\x01",
            "有人把那么多的书全部带走了吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xC,
        (
            "而且还是在神不知鬼不觉的情况下……\x01",
            "这根本不符合常识啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#00008F……很遗憾，\x01",
            "我们也完全想不通。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xC,
        "……唉，没办法了吗……\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xC,
        (
            "哪怕能知道那些书\x01",
            "究竟是什么书也好啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x104,
        (
            "#00302F哦，对了，\x01",
            "那里还剩下了几本。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x102,
        (
            "#00102F因为数量不多，\x01",
            "我们就给带回来了……\x02\x03",

            "或许能从中推测出\x01",
            "其它书籍的类别吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xC,
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#00000F不过，我们完全看不懂\x01",
            "书中的内容。\x02\x03",

            "也不知道这些书是否\x01",
            "有价值……\x01",
            "总之，先把书交给您吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0566
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把在塔中取得的书籍\x01",
            "交给了迈尔斯。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0567
    ChrTalk(
        0xC,
        "这、这是……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x105,
        (
            "#10300F看样子，\x01",
            "好像是中世纪时期的书吧？\x02\x03",

            "不过已经非常破旧了，\x01",
            "不知道还能不能\x01",
            "看清楚里面的字。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0569
    ChrTalk(
        0x109,
        "#10105F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xC,
        (
            "太、太棒了……\x01",
            "这里、这里……还有这里的图……\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xC,
        "这是中世纪的魔导书啊！\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        "#00105F魔导书……是什么？\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xC,
        (
            "这是古人写的书！\x01",
            "记载着炼金术与\x01",
            "魔导具的操作方法！\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xC,
        (
            "虽然要经过解读才能了解其中的含义，\x01",
            "但从里面的图解来看，\x01",
            "绝对没有错！\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        (
            "#00002F哎……\x01",
            "看来是很贵重的书啊。\x02\x03",

            "#00003F不过，既然会被丢弃在\x01",
            "那种地方，也就表示……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA5E")

    #C0576
    ChrTalk(
        0x103,
        (
            "#00200F对带走那些书籍的人来说，\x01",
            "这些并不是很重要的书，\x01",
            "是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x105,
        (
            "#10300F想以这些书为线索来寻找盗书者，\x01",
            "看来是相当困难了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AADE")

    label("loc_AA5E")


    #C0578
    ChrTalk(
        0x105,
        (
            "#10300F对带走那些书的人来说，\x01",
            "这几本书并不是很重要……\x01",
            "是这么一回事吧？\x02\x03",

            "想以这些书为线索来寻找盗书者，\x01",
            "看来是相当困难了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AADE")


    #C0579
    ChrTalk(
        0x101,
        "#00001F嗯……\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x102,
        "#00108F还是留下了难以索解的谜团呢……\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xC,
        (
            "哪里哪里，\x01",
            "不管怎么说，你们也帮忙\x01",
            "取回了非常贵重的书籍啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xC,
        (
            "大家做得已经很好了，\x01",
            "委托你们果然是正确的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x109,
        "#10100F啊哈哈……不敢当。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xC,
        (
            "我们会把这些书\x01",
            "慎重保管在地下书库中。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xC,
        (
            "到时要和尼尔森先生他们\x01",
            "一起好好研究研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xC,
        (
            "谢谢了，罗伊德，还有各位。\x01",
            "以后如果又有什么事，还要拜托大家帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        (
            "#00002F啊……嗯，\x01",
            "随时恭候。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0588
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查塔内的古文书】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACEE")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_ACF8")

    label("loc_ACEE")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_ACF8")

    OP_29(0x71, 0x1, 0x5)
    OP_29(0x71, 0x1, 0x6)
    OP_29(0x71, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_A428 end

    def Function_35_AD24(): pass

    label("Function_35_AD24")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AE03")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0589
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　图书馆消息　～\x01",
            "  为了响应大家的要求，\x01",
            "  增加了以下书籍。\x01",
            "  ·黑市医生格伦 第１３卷\x01",
            "  ·黑市医生格伦 第１４卷\x01",
            "※以上书籍放置在一层的书架中，\x01",
            "　有兴趣者请尽管借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B1CD")

    label("loc_AE03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AF0D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　图书馆消息　～\x01",
            "  为了响应大家的要求，\x01",
            "  增加了以下书籍。\x01",
            "  ·黑市医生格伦 第９卷\x01",
            "  ·黑市医生格伦 第１０卷\x01",
            "  ·黑市医生格伦 第１１卷\x01",
            "  ·黑市医生格伦 第１２卷\x01",
            "※以上书籍放置在一层的书架中，\x01",
            "　有兴趣者请尽管借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B1CD")

    label("loc_AF0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AFCA")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0591
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　图书馆消息　～\x01",
            "  为了响应大家的要求，\x01",
            "  增加了以下书籍。\x01",
            "  ·一分钟烹饪（点心篇）\x01",
            "※以上书籍放置在一层的书架中，\x01",
            "　有兴趣者请尽管借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B1CD")

    label("loc_AFCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B0CE")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0592
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　图书馆消息　～\x01",
            "  为了响应大家的要求，\x01",
            "  增加了以下书籍。\x01",
            "  ·黑市医生格伦 第５卷\x01",
            "  ·黑市医生格伦 第６卷\x01",
            "  ·黑市医生格伦 第７卷\x01",
            "  ·黑市医生格伦 第８卷\x01",
            "※以上书籍放置在一层的书架中，\x01",
            "　有兴趣者请尽管借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_B1CD")

    label("loc_B0CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B1CD")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0593
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　图书馆消息　～\x01",
            "  为了响应大家的要求，\x01",
            "  增加了以下书籍。\x01",
            "  ·黑市医生格伦 第１卷\x01",
            "  ·黑市医生格伦 第２卷\x01",
            "  ·黑市医生格伦 第３卷\x01",
            "  ·黑市医生格伦 第４卷\x01",
            "※以上书籍放置在一层的书架中，\x01",
            "　有兴趣者请尽管借阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_B1CD")

    EventEnd(0x3)
    Return()

    # Function_35_AD24 end

    def Function_36_B1D0(): pass

    label("Function_36_B1D0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0594
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《玛尔克与森林深处的魔女》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【阅读中卷】\x01",      # 1
            "【阅读下卷】\x01",      # 2
            "【放弃】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B275")
    UseItem(0x2D6, 0xFF)

    label("loc_B275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B289")
    UseItem(0x2DD, 0xFF)

    label("loc_B289")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B29D")
    UseItem(0x2DE, 0xFF)

    label("loc_B29D")

    TalkEnd(0xFF)
    Return()

    # Function_36_B1D0 end

    def Function_37_B2A1(): pass

    label("Function_37_B2A1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0595
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《改变大陆的美人们》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B318")
    UseItem(0x2D7, 0xFF)

    label("loc_B318")

    TalkEnd(0xFF)
    Return()

    # Function_37_B2A1 end

    def Function_38_B31C(): pass

    label("Function_38_B31C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《有效利用五分钟的零散时间》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B39B")
    UseItem(0x2D8, 0xFF)

    label("loc_B39B")

    TalkEnd(0xFF)
    Return()

    # Function_38_B31C end

    def Function_39_B39F(): pass

    label("Function_39_B39F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《铁道爱好者的推荐》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B416")
    UseItem(0x2D5, 0xFF)

    label("loc_B416")

    TalkEnd(0xFF)
    Return()

    # Function_39_B39F end

    def Function_40_B41A(): pass

    label("Function_40_B41A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0598
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《克洛斯贝尔怪谈全集》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B493")
    UseItem(0x2D9, 0xFF)

    label("loc_B493")

    TalkEnd(0xFF)
    Return()

    # Function_40_B41A end

    def Function_41_B497(): pass

    label("Function_41_B497")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《圣女与白狼》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读上卷】\x01",      # 0
            "【阅读下卷】\x01",      # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B523")
    UseItem(0x2DF, 0xFF)

    label("loc_B523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B537")
    UseItem(0x2E0, 0xFF)

    label("loc_B537")

    TalkEnd(0xFF)
    Return()

    # Function_41_B497 end

    def Function_42_B53B(): pass

    label("Function_42_B53B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0600
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《彩虹·Ｆａｎｂｏｏｋ》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5B6")
    UseItem(0x2DA, 0xFF)

    label("loc_B5B6")

    TalkEnd(0xFF)
    Return()

    # Function_42_B53B end

    def Function_43_B5BA(): pass

    label("Function_43_B5BA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B5D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B937")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 壹 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ＩＢＣ】\x01",      # 0
            "【ＺＣＦ】\x01",      # 1
            "【放弃】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7A6")
    SetChrName("")
    MenuTitle(-1, 25, 0, "ＩＢＣ（International Bank of Crossbell）")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0601
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『克洛斯贝尔国际银行』的简称。\x01",
            "这所巨大银行管理、运用着\x01",
            "从大陆全境汇集而来的庞大资产。\x01",
            "不仅限于克洛斯贝尔，ＩＢＣ也\x01",
            "常年支撑着国际金融、经济市场。\x02\x03",

            "除了投资活动和金融商品的开发，\x01",
            "其业务还涉及主题公园运营等领域，\x01",
            "并且也积极为爱普斯泰恩财团的\x01",
            "『导力网络计划』提供运作资金。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B932")
    MenuTitle(-1, 25, 0, "ＺＣＦ（Zeiss Central Factory）")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0602
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『蔡斯中央工房』的简称。\x01",
            "ＺＣＦ位于利贝尔王国的蔡斯市，\x01",
            "由导力器的发明者——爱普斯泰恩博士的\x01",
            "直系弟子Ａ·拉赛尔博士，\x01",
            "与蔡斯钟表师工会联合创办，\x01",
            "其前身为『蔡斯技术工房』。\x02\x03",

            "ＺＣＦ成功率先开发了导力飞船，\x01",
            "是大陆上首屈一指的导力器制造商，\x01",
            "近年，它更是成功制造了\x01",
            "利贝尔王国军的高速巡洋舰『埃尔赛尤』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B932")

    Jump("loc_B5D1")

    label("loc_B937")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_43_B5BA end

    def Function_44_B944(): pass

    label("Function_44_B944")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B95B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C147")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 贰 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【彩虹剧团】\x01",              # 0
            "【亚尔特利亚法典国】\x01",      # 1
            "【乌尔努公司】\x01",            # 2
            "【埃雷波尼亚帝国】\x01",        # 3
            "【爱普斯泰恩财团】\x01",        # 4
            "【放弃】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB0B")
    MenuTitle(-1, 25, 0, "彩虹剧团")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0603
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于克洛斯贝尔自治州，\x01",
            "是世界著名的剧团。\x02\x03",

            "其技巧高超的表演\x01",
            "与激情华丽的舞台，\x01",
            "让许多观众如痴如醉。\x02\x03",

            "特别是被誉为『炎之舞姬』的\x01",
            "现任招牌女演员伊莉娅·普拉提耶\x01",
            "受到了极大欢迎，\x01",
            "其狂热追随者遍布周边各国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC6A")
    MenuTitle(-1, 25, 0, "亚尔特利亚法典国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0604
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "亚尔特利亚法典国是七耀教会的总部所在地。\x01",
            "这座城国位于塞姆里亚大陆的中心地区，\x01",
            "并作为全大陆的信徒与宗教相关人员\x01",
            "齐聚的圣地而声名远扬。\x02\x03",

            "其中设有全权负责祭祀仪式相关事宜的『典礼省』，\x01",
            "据传负责管理女神圣物的『封圣省』，\x01",
            "以及负责城市保卫任务的『僧兵厅』等\x01",
            "各种各样的组织。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDCF")
    MenuTitle(-1, 25, 0, "乌尔努公司")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0605
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总部位于卡尔瓦德共和国，\x01",
            "是一家巨大的综合技术制造商。\x02\x03",

            "与埃雷波尼亚帝国的莱恩福尔特公司\x01",
            "同为武器和兵器开发领域的两大老牌公司，\x01",
            "但自从导力器出现后，\x01",
            "就开始着手研究和开发一切导力产品。\x02\x03",

            "其中在导力驱动车的领域，\x01",
            "以导力巴士为首，从家用车到特殊车辆的开发，\x01",
            "乌尔努公司都有着卓越的成绩。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFDD")
    MenuTitle(-1, 25, 0, "埃雷波尼亚帝国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0606
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于克洛斯贝尔自治州西部，\x01",
            "是一个以『黄金战马』为国徽的巨大帝国。\x01",
            "现任皇帝为尤肯特·莱泽·亚诺尔。\x02\x03",

            "该国家由大贵族支配，虽然体制陈旧，\x01",
            "但在被誉为『铁血宰相』——出身军队的\x01",
            "吉利亚斯·奥斯本宰相的推动下，\x01",
            "国土全境铺设了铁路，正逐渐向现代化发展。\x02\x03",

            "整个国家除了机械化的正规军之外，\x01",
            "还设有贵族的私人军队等，军事力量十分强大，\x01",
            "因此周边诸国都对其常年保持警戒。\x02\x03",

            "另外，皇帝之子——奥利维特皇子\x01",
            "去年帮助解决了利贝尔的异变事件，\x01",
            "这在帝国内引起了很大反响。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BFDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C142")
    MenuTitle(-1, 25, 0, "爱普斯泰恩财团")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0607
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "继承了发明导力器的天才导力学者\x01",
            "Ｃ·爱普斯泰恩博士辉煌成就的财团。\x01",
            "在研究机关与制造商的领域中也有很强实力，\x01",
            "特别擅长通讯及情报处理等领域。\x02\x03",

            "另外，此财团是能够驱动魔法的\x01",
            "『战术导力器』的唯一开发制造商，\x01",
            "近年来，还在致力于研究开发\x01",
            "通讯及情报处理技术领域的尖端工程『导力网络计划』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C142")

    Jump("loc_B95B")

    label("loc_C147")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_44_B944 end

    def Function_45_C154(): pass

    label("Function_45_C154")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C16B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8C5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 叁 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【怪盗Ｂ】\x01",                # 0
            "【卡尔瓦德共和国】\x01",        # 1
            "【克洛斯贝尔自治州】\x01",      # 2
            "【结晶回路】\x01",              # 3
            "【古代遗物】\x01",              # 4
            "【放弃】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3BC")
    MenuTitle(-1, 25, 0, "怪盗Ｂ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0608
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "活动领域覆盖大陆全境，神出鬼没的大盗。\x01",
            "小到宝石，大至导力战车，\x01",
            "无论所有者是国家还是个人，都可以成功盗走，\x01",
            "据说由于其手法华丽，甚至获得了\x01",
            "一部分狂热的崇拜者。\x02\x03",

            "他总是将别有寓意的信息送至各地，\x01",
            "虽然有人见到过他戴着面具，身披白色斗篷的样子，\x01",
            "但其真实面目一直是个谜。\x01",
            "近年来，他号称要进行『美的解放活动』，\x01",
            "在埃雷波尼亚帝国犯下了一系列\x01",
            "华丽并且无法侦破的罪行，再次引起了新话题。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C50F")
    MenuTitle(-1, 25, 0, "卡尔瓦德共和国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0609
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于克洛斯贝尔自治州东部，\x01",
            "在百年前便推行了民主化。\x01",
            "现任国家元首是洛克史密斯总统。\x02\x03",

            "该国家幅员辽阔，\x01",
            "因有着许多东方移民，\x01",
            "所以文化背景也丰富多彩。\x02\x03",

            "虽然在《互不侵犯条约》签订之后，态度便一直保持低调，\x01",
            "但在历史上，该国家与埃雷波尼亚帝国之间\x01",
            "曾发生过数次冲突。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C50F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C65F")
    MenuTitle(-1, 25, 0, "克洛斯贝尔自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0610
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于塞姆里亚大陆西部。\x01",
            "处在埃雷波尼亚帝国\x01",
            "和卡尔瓦德共和国这两大国之间，\x01",
            "曾经是激烈领土争端的对象，\x01",
            "但七十年前作为自治州成立了。\x02\x03",

            "现在，其中心克洛斯贝尔市已经发展为\x01",
            "大陆首屈一指的巨大贸易都市，\x01",
            "以及连接帝国和共和国的横贯大陆铁道\x01",
            "和国际定期飞船的中转站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C65F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C742")
    MenuTitle(-1, 25, 0, "结晶回路")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0611
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "用七耀石的碎片『耀晶片』精制加工而成，\x01",
            "拥有结晶构造的回路。\x02\x03",

            "是既能作为能量源使用，\x01",
            "又可以引发各种现象的装置，\x01",
            "但若未设置于导力器内部，\x01",
            "便发挥不出功效。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C742")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8C0")
    MenuTitle(-1, 25, 0, "古代遗物")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0612
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与导力器同样都是利用导力运作，\x01",
            "但运转原理不尽相同，是古代文明的导力器。\x02\x03",

            "据说是『古代塞姆里亚文明』时代\x01",
            "的产物，仅凭现代技术\x01",
            "是无法对其进行解析的。\x02\x03",

            "古代遗物在大陆各地的遗迹中都\x01",
            "有过少量发现，其中有不少遗物\x01",
            "甚至拥有超越常理的强大力量。\x02\x03",

            "因此七耀教会将古代遗物\x01",
            "定义为『女神过早的馈赠』，\x01",
            "并负责将其回收管理。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8C0")

    Jump("loc_C16B")

    label("loc_C8C5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_45_C154 end

    def Function_46_C8D2(): pass

    label("Function_46_C8D2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBA5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 肆 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【七耀教会】\x01",      # 0
            "【七耀石】\x01",        # 1
            "【放弃】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA6B")
    MenuTitle(-1, 25, 0, "七耀教会")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "信奉在塞姆里亚大陆上拥有最多信徒的\x01",
            "『空之女神爱德丝』的宗教组织。\x01",
            "其总部位于亚尔特利亚法典国。\x02\x03",

            "自导力革命之后，虽然影响力略有降低，\x01",
            "但目前在大陆上仍然拥有很强的影响力，\x01",
            "该组织一般通过知识、教育、医疗等领域\x01",
            "来启蒙民众。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBA0")
    MenuTitle(-1, 25, 0, "七耀石")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0614
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "散布于全大陆的七种珍贵宝石。\x01",
            "该宝石自古以来\x01",
            "就被视为某种神秘的象征而极其珍贵。\x02\x03",

            "近代出现了一种技术，\x01",
            "能够将体积过小，无法打磨成宝石的七耀石碎片\x01",
            "『耀晶片』进行精制·加工，制成结晶回路，\x01",
            "这项发明使七耀石资源的重要性\x01",
            "在大陆各国间陡然增大。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBA0")

    Jump("loc_C8E9")

    label("loc_CBA5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_46_C8D2 end

    def Function_47_CBB2(): pass

    label("Function_47_CBB2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D218")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 伍 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【大崩坏】\x01",        # 0
            "【钓公师团】\x01",      # 1
            "【导力革命】\x01",      # 2
            "【导力器】\x01",        # 3
            "【放弃】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD25")
    MenuTitle(-1, 25, 0, "大崩坏")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0615
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "指发生于一千两百年前，古代塞姆里亚文明\x01",
            "的毁灭。有资料称它是由天地异变所引发的，\x01",
            "但具体原因仍然不明。\x02\x03",

            "『大崩坏』导致文明消失之后，\x01",
            "人们度过了漫长的『黑暗时代』。\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CD25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE7F")
    MenuTitle(-1, 25, 0, "钓公师团")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0616
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旨在普及钓鱼文化，\x01",
            "是垂钓界的专业组织。\x01",
            "该组织由一位原为贵族的钓鱼爱好者\x01",
            "Ｈ·费瑟尔先生所发起，\x01",
            "其总部位于利贝尔王国的格兰赛尔市。\x02\x03",

            "主要活动对垂钓场所的探访、调查、开发，\x01",
            "并致力于发掘培养新一代钓师，\x01",
            "另外，钓公师团近年也开始着手开发钓具、鱼饵等，\x01",
            "其活动领域正在逐年扩大。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CE7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D09D")
    MenuTitle(-1, 25, 0, "导力革命")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0617
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大约在五十年前，\x01",
            "导力器的发明\x01",
            "引发了全大陆的技术革新。\x02\x03",

            "虽然导力器是划时代的发明，\x01",
            "但当时人们却对其持怀疑态度，\x01",
            "直到爱普斯泰恩财团的导力通讯器及\x01",
            "ＺＣＦ的导力飞船问世后，\x01",
            "其实用性才被全大陆所承认。\x02\x03",

            "现在，从取暖设备与照明设备等日用品，\x01",
            "到列车、飞船、战车及大炮等兵器，\x01",
            "所有设备都已经得到导力化，\x01",
            "导力器对人们来说，\x01",
            "已经变得必不可少。\x02\x03",

            "近几年，随着导力机械的小型化，\x01",
            "乌尔努公司和莱恩福尔特公司对\x01",
            "高性能导力驱动车的开发也在不断进步，\x01",
            "其产品已经开始在一般民众间普及开来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D09D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D213")
    MenuTitle(-1, 25, 0, "导力器")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0618
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由Ｃ·爱普斯泰恩博士发明，\x01",
            "通过引出七耀石中的导力，\x01",
            "来引发种种现象的机械的总称。\x02\x03",

            "导力器利用其内在构造及齿轮运转，\x01",
            "使由七耀石加工而来的结晶回路互相干涉，\x01",
            "从而引发无数种现象。\x02\x03",

            "导力器的实用性之强，\x01",
            "不仅在于能引发各种现象，并且『随时间流逝内部的\x01",
            "导力会逐渐恢复』，从经济效率上看远远\x01",
            "高于外燃、内燃机械。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D213")

    Jump("loc_CBC9")

    label("loc_D218")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_47_CBB2 end

    def Function_48_D225(): pass

    label("Function_48_D225")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D23C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D626")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 陆 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【导力魔法】\x01",          # 0
            "【导力网络计划】\x01",      # 1
            "【东方人街】\x01",          # 2
            "【放弃】\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3B2")
    MenuTitle(-1, 25, 0, "导力魔法")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0619
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通过将结晶回路装入爱普斯泰恩财团\x01",
            "特别设计的『战术导力器』中，\x01",
            "从而得以发动的『魔法』。\x02\x03",

            "一般被称为『导力魔法』，\x01",
            "只要经过训练，每个人都能使用，\x01",
            "因此广泛普及于军队、警察、游击士协会等组织。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4F5")
    MenuTitle(-1, 25, 0, "导力网络计划")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0620
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "爱普斯泰恩财团正在开发研究的，\x01",
            "具有革命性意义的信息网络计划。\x01",
            "此计划以导力缆线连接各终端，\x01",
            "让交换以及处理大量信息成为可能。\x02\x03",

            "虽然原本与利贝尔的ＺＣＦ\x01",
            "共同推进此计划，但现在\x01",
            "由于接受了ＩＢＣ的资金援助，所以开始正\x01",
            "式在克洛斯贝尔市进行了导入实验。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D4F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D621")
    MenuTitle(-1, 25, 0, "东方人街")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0621
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "位于卡尔瓦德共和国，\x01",
            "是东方移民所筑起的大规模街道。\x01",
            "东方人街汇聚了各种文化、人种、物资，\x01",
            "被誉为『东西文化的交叉点』。\x02\x03",

            "充满异国情调的建筑物鳞次栉比，\x01",
            "是享有盛名的观光地，但遗憾的是\x01",
            "据传闻说，东方人街中也存在庞大的黑手党组织。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D621")

    Jump("loc_D23C")

    label("loc_D626")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_48_D225 end

    def Function_49_D633(): pass

    label("Function_49_D633")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D64A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA60")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 柒 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【百日战役】\x01",          # 0
            "【互不侵犯条约】\x01",      # 1
            "【放弃】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8BB")
    MenuTitle(-1, 25, 0, "百日战役")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0622
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "百日战役是七耀历１１９２年，埃雷波尼亚帝国\x01",
            "向利贝尔王国发动的一场侵略战争。\x01",
            "因为从帝国宣战开始，到七耀教会\x01",
            "协调双方结束战争，\x01",
            "大约进行了一百天，\x01",
            "所以被称为『百日战役』。\x02\x03",

            "当时利贝尔处于绝对劣势，\x01",
            "领土大半都已被帝国军队占领，\x01",
            "但在使用当时最先进的警备飞艇\x01",
            "发起闪电般的反击战后，\x01",
            "战况瞬间便被颠覆。\x02\x03",

            "关于开战理由，\x01",
            "因为两国都对此保持沉默，\x01",
            "所以至今仍然是个迷。\x01",
            "战争结束之后，帝国政府将其称为\x01",
            "『由不幸的误会而产生的错误』，\x01",
            "并向利贝尔发表了正式的谢罪声明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D8BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA5B")
    MenuTitle(-1, 25, 0, "互不侵犯条约")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0623
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《互不侵犯条约》是七耀历１２０２年，利贝尔王国、\x01",
            "埃雷波尼亚帝国和卡尔瓦德共和国\x01",
            "三国间签订的一则国际条约。\x01",
            "该条约由利贝尔的艾莉茜雅女王发起，\x01",
            "在该国的艾尔贝离宫签订。\x02\x03",

            "该条约虽然不具备法律强制力，\x01",
            "但条约签订后，帝国和共和国便终止了\x01",
            "在克洛斯贝尔自治州近郊举行的\x01",
            "大规模军事演习，\x01",
            "使紧张的局势大为缓和，\x01",
            "可以说，此条约起到了立竿见影的效果。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA5B")

    Jump("loc_D64A")

    label("loc_DA60")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_49_D633 end

    def Function_50_DA6D(): pass

    label("Function_50_DA6D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE00")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 捌 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【米修拉姆】\x01",        # 0
            "【游击士协会】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBFC")
    MenuTitle(-1, 25, 0, "米修拉姆")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0624
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "米修拉姆是位于艾尔姆湖东南边的一处高级疗养地，\x01",
            "两年前，ＩＢＣ开始着手进行开发后，\x01",
            "此地便建成了度假酒店和主题公园等，\x01",
            "并成为大受欢迎的观光旅游地点。\x02\x03",

            "被称为『咪西』\x01",
            "的当地吉祥物，\x01",
            "也十分受市民和游客的欢迎。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DBFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDFB")
    MenuTitle(-1, 25, 0, "游击士协会")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "为了保护地区和平与普通人的安全，\x01",
            "游击士们所成立的民间团体。  \x01",
            "由于协会在塞姆里亚大陆全境都设有分部，\x01",
            "所以影响力与发言力也不容小觑。\x02\x03",

            "协会的理念可以说是\x01",
            "以保护平民的安全为优先，\x01",
            "但相对的，为了不威胁到平民的安全，\x01",
            "所以协会无法行使对国家与政府权力者的\x01",
            "搜查权和逮捕权，这是其组织守则上的弱点之一。\x02\x03",

            "而且克洛斯贝尔分部所接到的国际性案件较多，\x01",
            "因此集中于此处的人才都尤其优秀，\x01",
            "其中，『风之剑圣』亚里欧斯·马克莱因\x01",
            "更是获得了市民的极大支持。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DDFB")

    Jump("loc_DA84")

    label("loc_DE00")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_50_DA6D end

    def Function_51_DE0D(): pass

    label("Function_51_DE0D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DE24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E57F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "【 玖 】")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【莱恩福尔特公司】\x01",      # 0
            "【雷米菲利亚公国】\x01",      # 1
            "【列曼自治州】\x01",          # 2
            "【利贝尔王国】\x01",          # 3
            "【猎兵团】\x01",              # 4
            "【放弃】\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E00B")
    MenuTitle(-1, 25, 0, "莱恩福尔特公司")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0626
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总部位于埃雷波尼亚帝国，\x01",
            "是一家巨大的综合技术制造商。\x01",
            "前身是专门制造使用火药的\x01",
            "大炮以及重型武器的兵器工房。\x02\x03",

            "自从导力器问世之后，\x01",
            "便转而制造导力枪与导力兵器，\x01",
            "并涉足导力列车与飞船等领域，\x01",
            "最终发展为与卡尔瓦德共和国的『乌尔努公司』\x01",
            "齐名的，世界两大制造商之一。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E00B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E19A")
    MenuTitle(-1, 25, 0, "雷米菲利亚公国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0627
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雷米菲利亚公国位于塞姆里亚大陆北部。\x01",
            "虽然处于自然环境严酷的北方，\x01",
            "但有着茂密的森林与清澈的湖泊，\x01",
            "风光明媚、景色秀丽，\x01",
            "吸引了众多游客前来观光。\x02\x03",

            "雷米菲利亚公国同时也是著名的医疗发达国家，\x01",
            "集中了全大陆的顶尖医疗器械制造商，\x01",
            "并且培养了许多优秀的医生。\x01",
            "克洛斯贝尔自治州的圣乌尔斯拉医科大学\x01",
            "也是由雷米菲利亚公国协助设立的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E19A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E28A")
    MenuTitle(-1, 25, 0, "列曼自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0628
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "列曼自治州位于塞姆里亚大陆中部。\x01",
            "不仅是爱普斯泰恩财团的总部所在地，\x01",
            "同时也是Ｃ·爱普斯泰恩博士的故乡。\x02\x03",

            "除此之外，在全大陆都设有分部的\x01",
            "游击士协会的总部也设于该国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E475")
    MenuTitle(-1, 25, 0, "利贝尔王国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "利贝尔王国位于塞姆里亚大陆西南部。\x01",
            "自古以来就拥有丰富绚丽的自然风光，\x01",
            "现在，利贝尔王国在老女王艾莉茜雅Ⅱ世的治理下，\x01",
            "局势稳定，以和平著称。\x02\x03",

            "虽然与周边诸国相比，国力稍显逊色，\x01",
            "但凭借丰富的七耀石资源和先进的技术，\x01",
            "加上灵活的外交政策，\x01",
            "使其与各国建立了平等友好的关系。\x02\x03",

            "去年，在王国中央的瓦雷利亚湖上\x01",
            "出现了神秘的巨大物体（详情不明），\x01",
            "并使王国全境的导力全部停止运转，\x01",
            "所幸，此危机最后被军队和游击士协会\x01",
            "顺利解决了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E57A")
    MenuTitle(-1, 25, 0, "猎兵团")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0630
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "指代大陆各国的佣兵部队中\x01",
            "最优秀的部队时所使用的称号。\x02\x03",

            "雇主可依据规模和目的与其灵活地订立合同，\x01",
            "再加上猎兵拥有着强大的战斗力，\x01",
            "因此常作为私人武装被雇佣，\x01",
            "但有的国家也明令禁止其在境内活动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E57A")

    Jump("loc_DE24")

    label("loc_E57F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_51_DE0D end

    def Function_52_E58C(): pass

    label("Function_52_E58C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0631
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《黑市医生格伦》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读第13卷】\x01",      # 0
            "【阅读第14卷】\x01",      # 1
            "【放弃】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E61E")
    UseItem(0x2D2, 0xFF)

    label("loc_E61E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E632")
    UseItem(0x2D3, 0xFF)

    label("loc_E632")

    TalkEnd(0xFF)
    Return()

    # Function_52_E58C end

    def Function_53_E636(): pass

    label("Function_53_E636")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0632
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《黑市医生格伦》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读第９卷】\x01",      # 0
            "【阅读第10卷】\x01",      # 1
            "【阅读第11卷】\x01",      # 2
            "【阅读第12卷】\x01",      # 3
            "【放弃】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6E6")
    UseItem(0x2CE, 0xFF)

    label("loc_E6E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6FA")
    UseItem(0x2CF, 0xFF)

    label("loc_E6FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E70E")
    UseItem(0x2D0, 0xFF)

    label("loc_E70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E722")
    UseItem(0x2D1, 0xFF)

    label("loc_E722")

    TalkEnd(0xFF)
    Return()

    # Function_53_E636 end

    def Function_54_E726(): pass

    label("Function_54_E726")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0633
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《黑市医生格伦》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读第５卷】\x01",      # 0
            "【阅读第６卷】\x01",      # 1
            "【阅读第７卷】\x01",      # 2
            "【阅读第８卷】\x01",      # 3
            "【放弃】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7D6")
    UseItem(0x2CA, 0xFF)

    label("loc_E7D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7EA")
    UseItem(0x2CB, 0xFF)

    label("loc_E7EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7FE")
    UseItem(0x2CC, 0xFF)

    label("loc_E7FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E812")
    UseItem(0x2CD, 0xFF)

    label("loc_E812")

    TalkEnd(0xFF)
    Return()

    # Function_54_E726 end

    def Function_55_E816(): pass

    label("Function_55_E816")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0634
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上放置着《黑市医生格伦》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读第１卷】\x01",      # 0
            "【阅读第２卷】\x01",      # 1
            "【阅读第３卷】\x01",      # 2
            "【阅读第４卷】\x01",      # 3
            "【放弃】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8C6")
    UseItem(0x2C6, 0xFF)

    label("loc_E8C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8DA")
    UseItem(0x2C7, 0xFF)

    label("loc_E8DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8EE")
    UseItem(0x2C8, 0xFF)

    label("loc_E8EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E902")
    UseItem(0x2C9, 0xFF)

    label("loc_E902")

    TalkEnd(0xFF)
    Return()

    # Function_55_E816 end

    SaveToFile()

Try(main)
