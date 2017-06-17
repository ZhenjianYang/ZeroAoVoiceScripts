from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "キャサル",               # 1
        "ノバース",               # 2
        "シャーナ",               # 3
        "アビー",                 # 4
        "マイルズ",               # 5
        "ニールセン",             # 6
        "キーア",                 # 7
        "レイテ",                 # 8
        "キャサル",               # 9
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
        "Function_5_DC4",          # 05, 5
        "Function_6_1A9E",         # 06, 6
        "Function_7_27BC",         # 07, 7
        "Function_8_28FD",         # 08, 8
        "Function_9_2B84",         # 09, 9
        "Function_10_35C6",        # 0A, 10
        "Function_11_37C5",        # 0B, 11
        "Function_12_3DFE",        # 0C, 12
        "Function_13_3E60",        # 0D, 13
        "Function_14_3F95",        # 0E, 14
        "Function_15_5498",        # 0F, 15
        "Function_16_5587",        # 10, 16
        "Function_17_57BF",        # 11, 17
        "Function_18_593B",        # 12, 18
        "Function_19_59EC",        # 13, 19
        "Function_20_5B64",        # 14, 20
        "Function_21_5EC4",        # 15, 21
        "Function_22_5F87",        # 16, 22
        "Function_23_5FE4",        # 17, 23
        "Function_24_63D1",        # 18, 24
        "Function_25_67B3",        # 19, 25
        "Function_26_6BD7",        # 1A, 26
        "Function_27_76D9",        # 1B, 27
        "Function_28_7AC9",        # 1C, 28
        "Function_29_7B25",        # 1D, 29
        "Function_30_A6EE",        # 1E, 30
        "Function_31_B5A0",        # 1F, 31
        "Function_32_B6AC",        # 20, 32
        "Function_33_B93D",        # 21, 33
        "Function_34_C084",        # 22, 34
        "Function_35_CA7A",        # 23, 35
        "Function_36_CF70",        # 24, 36
        "Function_37_D047",        # 25, 37
        "Function_38_D0CE",        # 26, 38
        "Function_39_D157",        # 27, 39
        "Function_40_D1DA",        # 28, 40
        "Function_41_D25D",        # 29, 41
        "Function_42_D309",        # 2A, 42
        "Function_43_D396",        # 2B, 43
        "Function_44_D78E",        # 2C, 44
        "Function_45_E066",        # 2D, 45
        "Function_46_E90A",        # 2E, 46
        "Function_47_EC26",        # 2F, 47
        "Function_48_F3BD",        # 30, 48
        "Function_49_F85C",        # 31, 49
        "Function_50_FD0A",        # 32, 50
        "Function_51_10114",       # 33, 51
        "Function_52_1092B",       # 34, 52
        "Function_53_109D7",       # 35, 53
        "Function_54_10AC9",       # 36, 54
        "Function_55_10BBB",       # 37, 55
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
            "『一分クッキング・お菓子編』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_DC0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『軽快ポップコーン』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DC0")

    TalkEnd(0xFF)
    Return()

    # Function_4_D0F end

    def Function_5_DC4(): pass

    label("Function_5_DC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAA")

    #C0003
    ChrTalk(
        0xFE,
        (
            "こんにちは、\x01",
            "クロスベル市立図書館へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "……ふう、今日は利用者も\x01",
            "さすがに多くはありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "あのような大樹も現れた事ですし、\x01",
            "外出自体を控えている人も\x01",
            "多いのではないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F31")

    label("loc_EAA")


    #C0006
    ChrTalk(
        0xFE,
        (
            "今日は利用者も\x01",
            "さすがに多くはありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "図書館の司書として、\x01",
            "借りにきてくれる方々には\x01",
            "誠意をもって対応させて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F31")

    Jump("loc_1A9A")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FCA")

    #C0008
    ChrTalk(
        0xFE,
        (
            "以前、猟兵が街を襲ってきた時と\x01",
            "同じくらいの恐怖を感じています。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "どうしてこんな事に……\x01",
            "そんな理不尽な気持ちでいっぱいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1088")

    #C0010
    ChrTalk(
        0xFE,
        (
            "『クロスベル独立国』……\x01",
            "とうとう後戻りできない所まで\x01",
            "来てしまった気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "２大国はこの宣言を受けて、\x01",
            "どういう態度に出るんでしょうか。\x01",
            "……正直不安で一杯です……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1180")

    #C0012
    ChrTalk(
        0xFE,
        (
            "襲撃の夜は、既に仕事を終えて\x01",
            "ここを離れてはいたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "この行政区は警察本部を\x01",
            "中心に、本当に恐ろしい\x01",
            "被害に遭ったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "もう１週間経ちますけど……\x01",
            "街が炎で包まれた\x01",
            "あの夜の事は忘れられません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1203")

    label("loc_1180")


    #C0015
    ChrTalk(
        0xFE,
        (
            "もう１週間経ちますけど……\x01",
            "街が炎で包まれた\x01",
            "あの夜の事は忘れられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "これも独立提唱への\x01",
            "警告だというのでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1203")

    Jump("loc_1A9A")

    label("loc_1208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1286")

    #C0017
    ChrTalk(
        0xFE,
        (
            "当たり前のことですが……\x01",
            "警察本部の方が慌しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "マインツの件、無事に\x01",
            "解決するとよいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_139C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1351")

    #C0019
    ChrTalk(
        0xFE,
        (
            "今日は市民会館の方で\x01",
            "市民フォーラムが\x01",
            "開催されているらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "国家独立の是非……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "住民投票も近付いていますし、\x01",
            "そろそろ自分の意見を\x01",
            "固めないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1397")

    label("loc_1351")


    #C0022
    ChrTalk(
        0xFE,
        (
            "国家独立の是非……\x01",
            "そろそろ自分の意見を\x01",
            "固めないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1397")

    Jump("loc_1A9A")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1444")

    #C0023
    ChrTalk(
        0xFE,
        (
            "えっと、この本は学術書だから\x01",
            "あちらの棚に戻して、と……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "ふふ、本棚の隙間に\x01",
            "本を戻すのって、どうして\x01",
            "こんなに楽しいんでしょうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C5")

    label("loc_1444")


    #C0025
    ChrTalk(
        0xFE,
        (
            "本を本棚に戻すのって\x01",
            "少しパズルに似ていますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "丁度ピッタリ隙間なく\x01",
            "収められた時とかは、\x01",
            "ちょっと感動ものなんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C5")

    Jump("loc_1A9A")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_161F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1599")

    #C0027
    ChrTalk(
        0xFE,
        (
            "こんにちは。\x01",
            "クロスベル市立図書館へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "現在貸し出し中の本でも\x01",
            "言ってくだされば、\x01",
            "予約だって出来ますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "私でも館長でも、いつでも\x01",
            "お気軽にご相談ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_161A")

    label("loc_1599")


    #C0030
    ChrTalk(
        0xFE,
        (
            "現在貸し出し中の本でも\x01",
            "言ってくだされば、\x01",
            "予約だって出来ますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "私でも館長でも、いつでも\x01",
            "お気軽にご相談ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161A")

    Jump("loc_1A9A")

    label("loc_161F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_162D")
    Jump("loc_1A9A")

    label("loc_162D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16CF")

    #C0032
    ChrTalk(
        0xFE,
        (
            "各国の首脳たちは、\x01",
            "昨晩はミシュラムの\x01",
            "迎賓館に宿泊されたそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "ふふ、さぞかし\x01",
            "豪華で美味しいお食事を\x01",
            "お召しになられたんでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_16CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1768")

    #C0034
    ChrTalk(
        0xFE,
        (
            "通商会議のおかげで\x01",
            "今日は何だか、お祭りみたいな\x01",
            "ムードが漂っていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "ふふ、何をするでなくても\x01",
            "少し楽しい気分になって来ます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184C")

    #C0036
    ChrTalk(
        0xFE,
        (
            "星見の塔に大量の古文書が\x01",
            "あったという話を聞いて\x01",
            "館長が大喜びなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "出来れば、こちらに\x01",
            "全てを運び出す\x01",
            "つもりらしいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "うちの地下書庫にスペース的な\x01",
            "余裕ってあったでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18D7")

    label("loc_184C")


    #C0039
    ChrTalk(
        0xFE,
        (
            "どうやら館長は、古文書の\x01",
            "全てをこちらに運び出す\x01",
            "つもりらしいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "うちの地下書庫にスペース的な\x01",
            "余裕ってあったでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D7")

    Jump("loc_1A9A")

    label("loc_18DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_197F")

    #C0041
    ChrTalk(
        0xFE,
        (
            "ニールセンさんは、\x01",
            "フリー記者として大陸中を\x01",
            "忙しく飛び回っているそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "何でも今回は、およそ３年ぶりの\x01",
            "帰郷だって喜んでおられました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_197F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A1D")

    #C0043
    ChrTalk(
        0xFE,
        (
            "館長ったら、今日は\x01",
            "ニールセンさんが来るからって\x01",
            "そわそわしてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ふふ、よほど\x01",
            "ニールセンさんとお話するのが\x01",
            "お好きみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A9A")

    label("loc_1A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1A9A")

    #C0045
    ChrTalk(
        0xFE,
        (
            "こんにちは。\x01",
            "クロスベル市立図書館へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "何かお探しの本等ございましたら\x01",
            "いつでもお声掛けくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9A")

    TalkEnd(0xFE)
    Return()

    # Function_5_DC4 end

    def Function_6_1A9E(): pass

    label("Function_6_1A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1AAF")
    Jump("loc_27B8")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCA")

    #C0047
    ChrTalk(
        0xFE,
        (
            "一部はまだまだだけど……\x01",
            "ようやく街の復興も\x01",
            "落ち着いて来たみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "幸い、駅や空港には一切被害が\x01",
            "なかったから、またクロスベルに\x01",
            "来ていられるわけだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "交通機関を狙った襲撃だって\x01",
            "十分考えられるんだよな。\x01",
            "……そう考えると、恐ろしいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C44")

    label("loc_1BCA")


    #C0050
    ChrTalk(
        0xFE,
        (
            "クロスベルの歴史の研究に\x01",
            "この図書館は必須だからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "そろそろレマンの研究室に\x01",
            "缶詰でもいいかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")

    Jump("loc_27B8")

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFD")

    #C0052
    ChrTalk(
        0xFE,
        (
            "マインツで襲撃事件……\x01",
            "それも今も占拠してるだなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "帝国の仕業？　それとも共和国？\x01",
            "はっきり言って、どちらの線だって\x01",
            "十分に考えられるけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D7F")

    label("loc_1CFD")


    #C0054
    ChrTalk(
        0xFE,
        (
            "帝国にしても共和国にしても\x01",
            "マインツの状況は恰好の攻撃材料だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "はっきり言って、どちらの線だって\x01",
            "十分に考えられるけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7F")

    Jump("loc_27B8")

    label("loc_1D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E88")

    #C0056
    ChrTalk(
        0xFE,
        (
            "最近クロスベルの各地で、\x01",
            "いわゆる普通の魔獣と異なる\x01",
            "怪物が出現しているそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "何でも、教会の聖典に描かれて\x01",
            "いるような魔物を見かけた\x01",
            "とかいう噂もあるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "一体、このクロスベルに\x01",
            "何が起こっているんだろうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F40")

    label("loc_1E88")


    #C0059
    ChrTalk(
        0xFE,
        (
            "古代ゼムリア文明の知識が\x01",
            "現代に残っていれば、それこそ\x01",
            "何でも判るんだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "ふぅ、僕って奴はダメダメだね。\x01",
            "ない物ねだりなんてした所で、\x01",
            "見える物なんて何もないってのに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F40")

    Jump("loc_27B8")

    label("loc_1F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2003")

    #C0061
    ChrTalk(
        0xFE,
        (
            "ふむ、次は古今東西の独立を\x01",
            "テーマに論文をまとめてみるのも\x01",
            "面白いかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "そこから見出された共通点が、\x01",
            "何か他の歴史を紐解くことにも\x01",
            "つながるかもしれないしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B8")

    label("loc_2003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F8")

    #C0063
    ChrTalk(
        0xFE,
        "国家独立の提唱、か……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "クロスベルの歴史を中世の時代まで\x01",
            "振り返ると……過去にもそういう話が\x01",
            "なかったわけじゃないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "現代の状況を見ても判る通り、\x01",
            "それが成功した事は\x01",
            "かつて一度たりともないんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21CA")

    label("loc_20F8")


    #C0066
    ChrTalk(
        0xFE,
        (
            "とは言うものの、これまでも\x01",
            "ダメだったから今回もダメ……\x01",
            "そう言い切れないのが今日の世の中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "この提唱がいずれ大陸全体を揺り動かす\x01",
            "ムーブメントにまで発展すれば……\x01",
            "あるいはうまく行くのかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CA")

    Jump("loc_27B8")

    label("loc_21CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_21F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EA")
    Call(0, 20)
    Jump("loc_21ED")

    label("loc_21EA")

    Call(0, 21)

    label("loc_21ED")

    Jump("loc_27B8")

    label("loc_21F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_236D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D7")

    #C0068
    ChrTalk(
        0xFE,
        (
            "この子が本を漁ってたから、\x01",
            "探すのを手伝ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "いやー、しかし感心だなあ。\x01",
            "こんな小さいのに歴史に\x01",
            "興味を持ってくれるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "歴史を研究している者にとって\x01",
            "これほど嬉しいことはないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2368")

    label("loc_22D7")


    #C0071
    ChrTalk(
        0xFE,
        (
            "いやー、しかし感心だなあ。\x01",
            "こんな小さいのに歴史に\x01",
            "興味を持ってくれるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "歴史を研究している者にとって\x01",
            "これほど嬉しいことはないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2368")

    Jump("loc_27B8")

    label("loc_236D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2525")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_239A")
    Call(0, 7)
    Jump("loc_2520")

    label("loc_239A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")

    #C0073
    ChrTalk(
        0xFE,
        "西ゼムリア通商会議、か。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "このクロスベルで\x01",
            "ここまでの規模の国際会議が\x01",
            "開かれるのは一体何年ぶりだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "とにかく、この３日間の出来事は\x01",
            "後の世に“大陸の歴史”として\x01",
            "伝わる事は間違いないだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2520")

    label("loc_247E")


    #C0076
    ChrTalk(
        0xFE,
        (
            "この３日間の出来事は、\x01",
            "後の世に“大陸の歴史”として\x01",
            "伝わる事は間違いないはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "そんな歴史の一場面を\x01",
            "こうして傍で眺められる事を\x01",
            "素直に喜ばしく思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2520")

    Jump("loc_27B8")

    label("loc_2525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_254A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2542")
    Call(0, 7)
    Jump("loc_2545")

    label("loc_2542")

    Call(0, 8)

    label("loc_2545")

    Jump("loc_27B8")

    label("loc_254A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25F3")

    #C0078
    ChrTalk(
        0xFE,
        (
            "雨の日って何でか判らないけど、\x01",
            "すごく研究がはかどるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "雨音を聞いていると余計な事を\x01",
            "考えないで済むというか……\x01",
            "とにかく集中できるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B8")

    label("loc_25F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_27B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2711")

    #C0080
    ChrTalk(
        0xFE,
        (
            "僕はレマン自治州にある\x01",
            "州立大学の学生でね。\x01",
            "そこで歴史学を研究しているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "ちなみに僕は、これまでに二度\x01",
            "博士号の取得に挑戦したんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "一度目は論文が認められずに完敗。\x01",
            "二度目は期限内に提出できず不戦敗。\x01",
            "……とまあ、見事に連敗中なんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27B8")

    label("loc_2711")


    #C0083
    ChrTalk(
        0xFE,
        (
            "今は来年のチャンスに向けて、\x01",
            "再び論文を練り直している所なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "……別に博士号を取らなくても\x01",
            "大学自体は修了できるんだけどさ。\x01",
            "こうなるともはや意地だよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B8")

    TalkEnd(0xFE)
    Return()

    # Function_6_1A9E end

    def Function_7_27BC(): pass

    label("Function_7_27BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2881")

    #C0085
    ChrTalk(
        0xFE,
        (
            "星見の塔の調査は、君たちが\x01",
            "担当してくれたんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "大量の本が急になくなるだなんて、\x01",
            "どういうことか気になるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "とにかく、一冊でも\x01",
            "本が残っていて良かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28FC")

    label("loc_2881")


    #C0088
    ChrTalk(
        0xFE,
        (
            "とにかく、一冊でも\x01",
            "本が残っていて良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "マイルズさんに言って\x01",
            "僕も改めて、後日調査させて\x01",
            "もらうつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FC")

    Return()

    # Function_7_27BC end

    def Function_8_28FD(): pass

    label("Function_8_28FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF5")

    #C0090
    ChrTalk(
        0xFE,
        (
            "どうやら星見の塔に\x01",
            "大量の古文書が\x01",
            "残されていたんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "正直、本の状態はあまり\x01",
            "よくないらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "とまあ、それはともかく\x01",
            "そんな貴重な資料がこれまでに\x01",
            "ずっと放置され続けて来たなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "歴史を探求する者として、\x01",
            "管理をお座なりにして来た\x01",
            "警備隊に強い憤りを感じるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x109,
        (
            "#10106F（……確かに仰る通りですよね。\x01",
            "  耳の痛い話です……）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#00303F（まあな。\x01",
            "  ただ、塔の管理については\x01",
            "  全て前司令の責任だ。）\x02\x03",

            "#00302F（俺たちが気に病んでも\x01",
            "  仕方ねえと思うぜ？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B83")

    label("loc_2AF5")


    #C0096
    ChrTalk(
        0xFE,
        (
            "どうやら星見の塔に\x01",
            "大量の古文書が\x01",
            "残されていたんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "正直、本の状態はあまり\x01",
            "よくないらしいけど……\x01",
            "とにかく早く見てみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B83")

    Return()

    # Function_8_28FD end

    def Function_9_2B84(): pass

    label("Function_9_2B84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C23")

    #C0098
    ChrTalk(
        0xFE,
        (
            "あの事件でアビーが\x01",
            "不安がるので、楽しい本でも\x01",
            "読んであげようと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "やっぱり定番の\x01",
            "《マルクと深き森の魔女》が\x01",
            "いいかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_2C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C31")
    Jump("loc_35C2")

    label("loc_2C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D37")

    #C0100
    ChrTalk(
        0xFE,
        (
            "ディーターさんの演説……\x01",
            "凄くショッキングな内容でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "まさかとは思いましたが、\x01",
            "２大国の暗闘というものが\x01",
            "平気で行われていたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "この子たちの未来を守るには、\x01",
            "このまま独立の主張を\x01",
            "続けるしかないのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DE3")

    label("loc_2D37")


    #C0103
    ChrTalk(
        0xFE,
        (
            "まさかとは思いましたが、\x01",
            "２大国の暗闘というものが\x01",
            "平気で行われていたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "この子たちの未来を守るには、\x01",
            "このまま独立の主張を\x01",
            "続けるしかないのでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE3")

    Jump("loc_35C2")

    label("loc_2DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF6")
    Jump("loc_35C2")

    label("loc_2DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECF")

    #C0105
    ChrTalk(
        0xFE,
        (
            "鉱山町の方で恐ろしい事件が\x01",
            "起こっているらしいですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "町には、それこそ\x01",
            "アビーくらいの子供も\x01",
            "大勢いると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "とにかく、一刻も早く皆さんを\x01",
            "無事に解放して欲しいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F50")

    label("loc_2ECF")


    #C0108
    ChrTalk(
        0xFE,
        (
            "町には、それこそ\x01",
            "アビーくらいの子供も\x01",
            "大勢いると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "とにかく、一刻も早く皆さんを\x01",
            "無事に解放して欲しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F50")

    Jump("loc_35C2")

    label("loc_2F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F7B")

    #C0110
    ChrTalk(
        0xFE,
        "うん、それはね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FDA")

    #C0111
    ChrTalk(
        0xFE,
        (
            "あら、ママも\x01",
            "気付かなかったけど本当ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "お買い物にでも行ったのかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_2FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3061")

    #C0113
    ChrTalk(
        0xFE,
        (
            "今日もキーアちゃんは熱心に\x01",
            "調べ物をしているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "ふふ、アビーには\x01",
            "それが羨ましくって\x01",
            "しょうがないみたい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_3061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3141")

    #C0115
    ChrTalk(
        0xFE,
        (
            "うちのアビーも来年にもなれば、\x01",
            "日曜学校に通える年齢になるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "この子はご本が好きだから、\x01",
            "お勉強がよく出来るんじゃないかと\x01",
            "思うんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "ふふ、そう考えるのは親バカでしょうか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31CF")

    label("loc_3141")


    #C0118
    ChrTalk(
        0xFE,
        (
            "アビーには、とにかく元気よく\x01",
            "そして真っ直ぐに育って欲しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "私がこの子に何かを求めるとしたら、\x01",
            "詰まる所はそれ以外にないですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CF")

    Jump("loc_35C2")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328A")

    #C0120
    ChrTalk(
        0xFE,
        "ふふ、アビーはお利口さんね。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "よ～し、それじゃ\x01",
            "今日は帰りに寄り道して\x01",
            "アイスクリームを買ってあげるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        (
            "ほんと！？\x01",
            "やった、うれしいなーっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32D3")

    label("loc_328A")


    #C0123
    ChrTalk(
        0xFE,
        (
            "ふふ、それじゃ\x01",
            "お味は何がいいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        "んー、じゃあメロン味っ！\x02",
    )

    CloseMessageWindow()

    label("loc_32D3")

    Jump("loc_35C2")

    label("loc_32D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3382")

    #C0125
    ChrTalk(
        0xFE,
        (
            "ふふ、アビーったら\x01",
            "除幕式の見物で疲れちゃって、\x01",
            "オネムさんになっちゃったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "こんなに安心そうな顔をして……\x01",
            "本当に可愛いわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33CE")

    label("loc_3382")


    #C0127
    ChrTalk(
        0xFE,
        (
            "ふふ、アビーったら\x01",
            "こんなに安心そうな顔をして……\x01",
            "本当に可愛いわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CE")

    Jump("loc_35C2")

    label("loc_33D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3454")

    #C0128
    ChrTalk(
        0xFE,
        (
            "この図書館は本当に静かで\x01",
            "心地よいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "それに、古書独特の匂いが\x01",
            "何とも気分を\x01",
            "落ち着けてくれるんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_3454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350B")

    #C0130
    ChrTalk(
        0xFE,
        "そして空の女神#8Rエ イ ド ス#さまの流した涙は……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(18, 0, 70, 0)
    Sleep(300)

    #C0131
    ChrTalk(
        0xFE,
        (
            "大地に降りそそぎ、\x01",
            "せかい中に染み渡りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "人々はその光景をただただ眺め……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_353C")

    label("loc_350B")


    #C0133
    ChrTalk(
        0xFE,
        (
            "人々はその光景をただただ眺め……\x01",
            "そして……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353C")

    Jump("loc_35C2")

    label("loc_3541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_35C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355C")
    Call(0, 10)
    Jump("loc_35C2")

    label("loc_355C")


    #C0134
    ChrTalk(
        0xFE,
        (
            "うちのアビーは、\x01",
            "キーアちゃんのことが\x01",
            "本当に大好きなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        "ふふ、もちろん私もですけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_35C2")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B84 end

    def Function_10_35C6(): pass

    label("Function_10_35C6")


    #C0136
    ChrTalk(
        0xA,
        "あら、皆さんは……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "あっ、キーアおねーちゃんの\x01",
            "おにーちゃんとおねーちゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "ねえねえ、きょうは\x01",
            "キーアおねえちゃんは来ないのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00002Fああ、ごめんな。\x01",
            "今日は日曜学校に行ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#00102Fちゃんとキーアちゃんにも伝えておくから\x01",
            "今日のところは我慢してくれる？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        "うん、わかったよ！\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "それじゃあ、\x01",
            "キーアおねーちゃんに\x01",
            "よろしくね～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#00109Fふふ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10304Fなるほど、彼女はこんな所でも\x01",
            "人気者みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x109,
        (
            "#10102Fうん、流石は\x01",
            "キーアちゃんって感じだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 0)
    Return()

    # Function_10_35C6 end

    def Function_11_37C5(): pass

    label("Function_11_37C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3801")

    #C0146
    ChrTalk(
        0xFE,
        (
            "わくわくっ……\x01",
            "ママー、早く読んで～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_380F")
    Jump("loc_3DF6")

    label("loc_380F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3865")

    #C0147
    ChrTalk(
        0xFE,
        (
            "ねえ、ママ。\x01",
            "みんなお外で何か言ってるけど、\x01",
            "どういうことなのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3873")
    Jump("loc_3DF6")

    label("loc_3873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_38C7")

    #C0148
    ChrTalk(
        0xFE,
        (
            "ねえ、ママ……\x01",
            "お顔のいろがわるいけど、\x01",
            "どうかしちゃったの……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_38C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3908")

    #C0149
    ChrTalk(
        0xFE,
        (
            "ねえねえ、ママ。\x01",
            "この言葉はどういうイミなの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C5")

    #C0150
    ChrTalk(
        0xFE,
        (
            "あれ、キーアおねえちゃん、\x01",
            "いつの間にか、帰っちゃったんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "う～ん、気付いていたら\x01",
            "ちゃんとバイバイしたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        "ま、また会えるからいいよね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A24")

    label("loc_39C5")


    #C0153
    ChrTalk(
        0xFE,
        (
            "う～ん、気付いていたら\x01",
            "ちゃんとバイバイしたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "ま、また会えるからいいよね。\x02",
    )

    CloseMessageWindow()

    label("loc_3A24")

    Jump("loc_3DF6")

    label("loc_3A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AA6")

    #C0155
    ChrTalk(
        0xFE,
        (
            "キーアおねーちゃん、\x01",
            "ひとりだけで\x01",
            "ご本を読めてすごいな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "う～ん、ぼくも\x01",
            "おべんきょうしなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B5B")

    #C0157
    ChrTalk(
        0xFE,
        (
            "ぼくも、もうすぐしたら\x01",
            "キーアおねーちゃんと同じように\x01",
            "にちよーがっこうに行けるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "えへへ、にちよーがっこうに行っても\x01",
            "おねーちゃんに会えるといいなっ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BE5")

    #C0159
    ChrTalk(
        0xFE,
        (
            "あのね、キーアおねーちゃん、\x01",
            "きょうは調べものがあるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "だから、おねーちゃんの\x01",
            "ジャマをしちゃダメなんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C60")

    #C0161
    ChrTalk(
        0xFE,
        "……すーすー……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "ねー、ママ……\x01",
            "ひとがいっぱいですごかったね……\x01",
            "……むにゃむにゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C78")

    label("loc_3C60")


    #C0163
    ChrTalk(
        0xFE,
        "……すーすー………\x02",
    )

    CloseMessageWindow()

    label("loc_3C78")

    Jump("loc_3DF6")

    label("loc_3C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D30")

    #C0164
    ChrTalk(
        0xFE,
        (
            "ママは、ご本から\x01",
            "いい匂いがするって言うけど……\x01",
            "ぼくにはわからないや。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "だって、ママのほうが\x01",
            "ずっとずっとやさしくって\x01",
            "いい匂いがするんだもん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D5B")

    label("loc_3D30")


    #C0166
    ChrTalk(
        0xFE,
        (
            "ご本から、いい匂いなんて\x01",
            "するかなぁ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5B")

    Jump("loc_3DF6")

    label("loc_3D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D90")

    #C0167
    ChrTalk(
        0xFE,
        "ドキドキッ、それでそれで～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DF6")

    label("loc_3D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAB")
    Call(0, 10)
    Jump("loc_3DF6")

    label("loc_3DAB")


    #C0168
    ChrTalk(
        0xFE,
        (
            "キーアおねーちゃんに\x01",
            "よろしくね～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "ぼく、ここでまってるから。\x02",
    )

    CloseMessageWindow()

    label("loc_3DF6")

    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_37C5 end

    def Function_12_3DFE(): pass

    label("Function_12_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E0F")
    Call(0, 14)
    Jump("loc_3E5F")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E20")
    Call(0, 13)
    Jump("loc_3E5F")

    label("loc_3E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E31")
    Call(0, 14)
    Jump("loc_3E5F")

    label("loc_3E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_3E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E54")
    Call(0, 13)
    Jump("loc_3E57")

    label("loc_3E54")

    Call(0, 14)

    label("loc_3E57")

    Jump("loc_3E5F")

    label("loc_3E5C")

    Call(0, 14)

    label("loc_3E5F")

    Return()

    # Function_12_3DFE end

    def Function_13_3E60(): pass

    label("Function_13_3E60")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F15")

    #C0170
    ChrTalk(
        0x8,
        (
            "館長たち、今日は星見の塔で\x01",
            "発見された古文書を\x01",
            "調べてみるんだそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "皆さん、まるで少年のように\x01",
            "生き生きとした表情をするので\x01",
            "何だか可愛らしく思えます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F91")

    label("loc_3F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_3F91")

    #C0172
    ChrTalk(
        0x8,
        (
            "館長ったら、\x01",
            "またニールセンさんと\x01",
            "話し込んでいるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "もう休憩時間は\x01",
            "終わっているんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F91")

    TalkEnd(0x8)
    Return()

    # Function_13_3E60 end

    def Function_14_3F95(): pass

    label("Function_14_3F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 7)), scpexpr(EXPR_END)), "loc_3FC8")
    Call(0, 32)
    Return()

    label("loc_3FC8")

    Call(0, 30)
    Return()

    label("loc_3FCC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_416E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CB")

    #C0174
    ChrTalk(
        0xC,
        (
            "街は一通り普段の様相を\x01",
            "取り戻したようだが……\x01",
            "やはり不安もあるようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "あんな不気味な大樹が現れたんじゃ\x01",
            "仕方のないことだと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "市民たちにはしばらく家で\x01",
            "ゆっくりと読書でもして、\x01",
            "心を落ち着けて欲しいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4169")

    label("loc_40CB")


    #C0177
    ChrTalk(
        0xC,
        (
            "街は一通り普段の様相を\x01",
            "取り戻したようだが……\x01",
            "やはり不安もあるようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "市民たちにはしばらく家で\x01",
            "ゆっくりと読書でもして、\x01",
            "心を落ち着けて欲しいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4169")

    Jump("loc_5494")

    label("loc_416E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437A")
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0179
    ChrTalk(
        0xC,
        (
            "おお、ロイド君……\x01",
            "無事だったんだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00002Fおじさんの方こそ……\x01",
            "顔を見られて安心したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xC,
        "ああ、まったくだ。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "ロイド君が指名手配されたと\x01",
            "聞いた時は驚いたが……\x01",
            "それは間違いだって信じているからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "おじさん……\x01",
            "どうもありがとう。\x02\x03",

            "#00001F話したいことは色々あるんだけど、\x01",
            "今はとにかく時間がないんだ。\x02\x03",

            "とりあえず、外の様子が落ち着くまで\x01",
            "建物から出ないようにして欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xC,
        "ああ……了解だ。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "ロイド君、君たちの方こそ\x01",
            "どうか気を付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 4)
    Jump("loc_441E")

    label("loc_437A")


    #C0186
    ChrTalk(
        0xC,
        (
            "実は丁度、図書館に来ていた\x01",
            "ニールセンさんも\x01",
            "閉じ込められてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "まったくとんでもない状況に\x01",
            "なったものだ……ロイド君たちも\x01",
            "どうか気を付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441E")

    Jump("loc_5494")

    label("loc_4423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_465F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CE")

    #C0188
    ChrTalk(
        0xC,
        (
            "ロ、ロイド君。\x01",
            "聞いたかい、ディーター市長の演説を。\x01",
            "それに国防軍って……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00001Fうん、俺たちも\x01",
            "ただただ驚いている状況でさ。\x01",
            "今色々と調べている所なんだ。\x02\x03",

            "とにかく、おじさん。\x01",
            "今は落ち着いて成り行きを\x01",
            "見守っていて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        "あ、ああ、分かった。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xC,
        (
            "色々と不安だけど、\x01",
            "まずは落ち着かない事には\x01",
            "仕方ないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        "ロイド君たちも、頑張るんだよ。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#00002Fうん、ありがとう、おじさん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_465A")

    label("loc_45CE")


    #C0194
    ChrTalk(
        0xC,
        (
            "色々と不安だけど……\x01",
            "まずは落ち着かない事には仕方ないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "でも一体、どうしてディーターさんは\x01",
            "こんな強硬的な手段に出たんだろう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_465A")

    Jump("loc_5494")

    label("loc_465F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F4")

    #C0196
    ChrTalk(
        0xC,
        (
            "市と商工会が催してくれた\x01",
            "チャリティイベントは\x01",
            "随分盛り上がっているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xC,
        "ふむ、僕も後で寄付をしてこないと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4751")

    label("loc_46F4")


    #C0198
    ChrTalk(
        0xC,
        (
            "何といっても人間、\x01",
            "助け合いの精神が肝要だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xC,
        "ふむ、僕も後で寄付をしてこないと。\x02",
    )

    CloseMessageWindow()

    label("loc_4751")

    Jump("loc_5494")

    label("loc_4756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_47F6")

    #C0200
    ChrTalk(
        0xC,
        (
            "武装集団が何者かは知らないけど……\x01",
            "まったく、本当に愚かなことだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xC,
        (
            "暴力で人を支配しようだなんて……\x01",
            "間違っているし、とても許せないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5494")

    label("loc_47F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_486A")

    #C0202
    ChrTalk(
        0xC,
        "ふむ、外は雨だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "湿気が入り込まないように、\x01",
            "今日は地下書庫に入るのは\x01",
            "止めておこうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5494")

    label("loc_486A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_48DB")

    #C0204
    ChrTalk(
        0xC,
        (
            "母さんのお弁当、今日も\x01",
            "相変わらずいい仕事をしていたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        "おかげで午後からも頑張れそうだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5494")

    label("loc_48DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_495B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F6")
    Call(0, 15)
    Jump("loc_4956")

    label("loc_48F6")


    #C0206
    ChrTalk(
        0xC,
        (
            "いやぁ、僕としたことが\x01",
            "愛妻弁当を忘れるとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        (
            "でも母さんが\x01",
            "届けてくれて助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4956")

    Jump("loc_5494")

    label("loc_495B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_497E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4976")
    Call(0, 20)
    Jump("loc_4979")

    label("loc_4976")

    Call(0, 21)

    label("loc_4979")

    Jump("loc_5494")

    label("loc_497E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_49B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49A4")
    Call(0, 18)
    Jump("loc_49B0")

    label("loc_49A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_49B0")
    Call(0, 17)

    label("loc_49B0")

    Jump("loc_4B4F")

    label("loc_49B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9F")

    #C0208
    ChrTalk(
        0xC,
        "いや、キーア君は実に勉強熱心だね。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xC,
        (
            "うちでは１人につき一度に\x01",
            "３冊までしか貸してあげられないのが\x01",
            "心苦しいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xC,
        (
            "ふむ、優良利用者に限って\x01",
            "貸与数を増やす事のできる制度でも\x01",
            "今度、本気で検討してみるかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B4F")

    label("loc_4A9F")


    #C0211
    ChrTalk(
        0xC,
        (
            "うちでは１人につき一度に\x01",
            "３冊までしか貸してあげられないのが\x01",
            "心苦しいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        (
            "ふむ、優良利用者に限って\x01",
            "貸与数を増やす事のできる制度でも\x01",
            "今度、本気で検討してみるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B4F")

    Jump("loc_5494")

    label("loc_4B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B7A")
    Call(0, 18)
    Jump("loc_4B86")

    label("loc_4B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4B86")
    Call(0, 17)

    label("loc_4B86")

    Jump("loc_4D83")

    label("loc_4B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD3")

    #C0213
    ChrTalk(
        0xC,
        (
            "ふむ、各国のＶＩＰというのも\x01",
            "流石にそうそうたる顔ぶれだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "中でも、僕が注目したいのは\x01",
            "やっぱりオリヴァルト皇子だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "リベールの異変への貢献に始まり、\x01",
            "あの《アルセイユ号》を\x01",
            "使っての帝都への帰還など……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "鉄血宰相とはまた違った意味で\x01",
            "世間を驚かせてくれるから、\x01",
            "一挙一動に目が離せないんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D83")

    label("loc_4CD3")


    #C0217
    ChrTalk(
        0xC,
        (
            "各国の名だたるＶＩＰの中でも\x01",
            "僕が注目したいのは\x01",
            "やっぱりオリヴァルト皇子だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xC,
        (
            "鉄血宰相とはまた違った意味で\x01",
            "世間を驚かせてくれるから、\x01",
            "一挙一動に目が離せないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D83")

    Jump("loc_5494")

    label("loc_4D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DB6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DA5")
    Call(0, 18)
    Jump("loc_4DB1")

    label("loc_4DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_END)), "loc_4DB1")
    Call(0, 17)

    label("loc_4DB1")

    Jump("loc_5494")

    label("loc_4DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_4F06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDD")
    Call(0, 16)
    Jump("loc_4E85")

    label("loc_4DDD")


    #C0219
    ChrTalk(
        0xC,
        (
            "彼がフューリッツァ賞を取って\x01",
            "一躍その名を上げてから、\x01",
            "もう１０年以上になるのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "いつまた自治州を離れるかは\x01",
            "分からないけど、\x01",
            "戻ってきてくれて実に嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E85")

    Jump("loc_4F01")

    label("loc_4E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_4EF3")

    #C0221
    ChrTalk(
        0xC,
        (
            "ふむ、ニールセンさんが来ると\x01",
            "どうしても話し込んでしまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        "さて仕事仕事、と……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F01")

    label("loc_4EF3")

    Call(0, 26)
    TalkEnd(0xC)
    OP_93(0xC, 0x10E, 0x0)
    Return()

    label("loc_4F01")

    Jump("loc_5494")

    label("loc_4F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_516A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F7")

    #C0223
    ChrTalk(
        0xC,
        (
            "今日はこれから、特別な\x01",
            "お客さんが顔を出してくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xC,
        "ふふ、話をするのが楽しみだよ。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        "#00005F特別なお客さん？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "ああ、ニールセンさんと言って\x01",
            "国際的に活躍している\x01",
            "ジャーナリストの方なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "たぶん、もうしばらくすれば\x01",
            "来ると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "もしよければ、ロイド君たちにも\x01",
            "紹介してあげるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#00003F国際的に活躍している\x01",
            "ジャーナリストか……\x01",
            "確かに興味深いかもしれないな。\x02\x03",

            "#00002Fうん、それじゃ暇があったら\x01",
            "あとで立ち寄らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 2)
    SetScenarioFlags(0x0, 4)
    Jump("loc_5165")

    label("loc_50F7")


    #C0230
    ChrTalk(
        0xC,
        (
            "ニールセンさんは、\x01",
            "あとしばらくすれば来るはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "もしよければ、ロイド君たちにも\x01",
            "紹介してあげるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5165")

    Jump("loc_5494")

    label("loc_516A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5422")

    #C0232
    ChrTalk(
        0xC,
        "おや、ロイド君じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        (
            "仲間と一緒ということは、\x01",
            "ついに特務支援課の\x01",
            "活動再開というわけだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#00000Fうん、おかげ様でね。\x02\x03",

            "おじさんも何かあったら、\x01",
            "またいつでも俺たちを\x01",
            "頼ってくれると嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        "ああ、その時は是非お願いするよ。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "それにしても、以前にも増して\x01",
            "ますます頼もしくなったみたいだね。\x01",
            "僕も本当に嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#00006Fいや、そんな……\x01",
            "まだまだこれからだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "ふむ、個人的にはもっと\x01",
            "胸を張っていいと思うんだけど。\x01",
            "だが、それでこそロイド君だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xC,
        (
            "今後とも応援しているからね。\x01",
            "家の方にも、またいつでも\x01",
            "遠慮なく遊びに来てくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00002Fうん。\x01",
            "ありがとう、おじさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#00104F（セシルさんのお父さん……\x01",
            "  とても暖かい方ね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x133, 5)
    Jump("loc_5494")

    label("loc_5422")


    #C0242
    ChrTalk(
        0xC,
        (
            "君たち特務支援課のことは\x01",
            "いつでも応援してるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "家の方にも、またいつでも\x01",
            "遠慮なく遊びに来てくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5494")

    TalkEnd(0xC)
    Return()

    # Function_14_3F95 end

    def Function_15_5498(): pass

    label("Function_15_5498")


    #C0244
    ChrTalk(
        0xC,
        (
            "なんだ母さん。\x01",
            "何か用事でもあったかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "あらあら、なんだとは失礼ねえ。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xF,
        (
            "ふふ、お弁当を忘れていったから\x01",
            "届けにきてあげたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "おや！？\x01",
            "そりゃあ気付かなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "すまないね。\x01",
            "届けてくれて助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    Return()

    # Function_15_5498 end

    def Function_16_5587(): pass

    label("Function_16_5587")


    #C0249
    ChrTalk(
        0xC,
        (
            "ふむ、ロイド君。\x01",
            "どうやら話は終わったようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xC,
        "有意義な話はできたかい？\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00004Fうん、まあね。\x01",
            "色々と勉強させてもらったよ。\x02\x03",

            "#00000Fところで、おじさんは\x01",
            "ニールセンさんのことを\x01",
            "以前から知っていたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        (
            "ああ、ニールセンさんは\x01",
            "元々クロスベルの出身だしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "彼がクロスベル通信社に\x01",
            "在籍していた頃から\x01",
            "仲良くさせてもらっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xC,
        (
            "ちなみに、ガイ君ともけっこう\x01",
            "付き合いが深かったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#00002Fああ、そうみたいだね。\x02\x03",

            "#00003F（俺たちとグレイスさんの\x01",
            "  関係に近かったのかな。）\x02\x03",

            "（……当然ノリなんかは\x01",
            "  ぜんぜん違うんだろうけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 6)
    Return()

    # Function_16_5587 end

    def Function_17_57BF(): pass

    label("Function_17_57BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B9")

    #C0256
    ChrTalk(
        0xC,
        (
            "ウルスラ間道のはずれにある\x01",
            "『星見の塔』の調査を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        (
            "あの場所には、沢山の古文書が\x01",
            "放置されているらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "君たちの目で、本の回収に\x01",
            "どれだけ費用がかかりそうか\x01",
            "見極めてきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xC,
        "それじゃ、よろしく頼んだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_593A")

    label("loc_58B9")


    #C0260
    ChrTalk(
        0xC,
        (
            "星見の塔があるのは、\x01",
            "南のウルスラ間道の途中の\x01",
            "林を抜けたところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "塔にあるという古文書の調査、\x01",
            "よろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_593A")

    Return()

    # Function_17_57BF end

    def Function_18_593B(): pass

    label("Function_18_593B")


    #C0262
    ChrTalk(
        0xC,
        (
            "塔の本を全て回収\x01",
            "できなかったのは\x01",
            "残念極まりないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "この魔導書だけでも\x01",
            "かなり貴重なものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "ありがとうな、ロイドくんたち。\x01",
            "また何かあったらよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_593B end

    def Function_19_59EC(): pass

    label("Function_19_59EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_5A0C")
    Call(0, 28)
    Return()

    label("loc_5A0C")

    Call(0, 26)
    Return()

    label("loc_5A10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5AAC")

    #C0265
    ChrTalk(
        0xFE,
        (
            "突然の戒厳令……\x01",
            "これは大統領が追い詰められている\x01",
            "証拠とも言えるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "圧制は長く続かない……\x01",
            "これは世の常というものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B60")

    label("loc_5AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5B42")

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
            "（大陸最強の猟兵団……\x01",
            "  その背後にいるのは一体……）\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "（帝国と決め付けてしまうのは\x01",
            "  簡単ですが……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B60")

    label("loc_5B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5D")
    Call(0, 20)
    Jump("loc_5B60")

    label("loc_5B5D")

    Call(0, 21)

    label("loc_5B60")

    TalkEnd(0xFE)
    Return()

    # Function_19_59EC end

    def Function_20_5B64(): pass

    label("Function_20_5B64")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0270
    ChrTalk(
        0x9,
        (
            "うん、やはりこの魔導書は\x01",
            "中世における古代遺物#8Rアーティファクト#の研究書……\x01",
            "そう言えるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xC,
        (
            "なるほど……\x01",
            "それで著者についての\x01",
            "詳しい情報は分かるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "ええ、かつて《塔》を築いた\x01",
            "錬金術師が残したものであることは\x01",
            "間違いないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "彼らの素性について新たに\x01",
            "判明することはなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x9,
        (
            "まあ、それでも貴重な資料には\x01",
            "違いありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xD,
        (
            "ふむ、しかし残ったものが\x01",
            "これだけなのが悔やまれますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xD,
        (
            "もっとも、中性の錬金術師は\x01",
            "当時から謎の多い存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xD,
        (
            "彼らの素性につながる書物が\x01",
            "あったかどうかは怪しいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        "ええ、確かに仰る通りですね。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "う～ん、本がごっそり\x01",
            "なくなっていた件といい\x01",
            "謎は深まるばかりですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5EB8")

    #C0280
    ChrTalk(
        0x101,
        (
            "#00000F（おじさんたち……\x01",
            "  俺たちが見つけてきた本を\x01",
            "  調べているみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x102,
        (
            "#00100F（ええ、どうやら目新しい発見には\x01",
            "  つながらなかったみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EB8")

    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x16B, 4)
    Return()

    # Function_20_5B64 end

    def Function_21_5EC4(): pass

    label("Function_21_5EC4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0282
    ChrTalk(
        0xC,
        (
            "ふむ、中世の錬金術師か……\x01",
            "謎は深まるばかりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xD,
        (
            "ええ、ですがこの魔導書は\x01",
            "非常に興味深いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        (
            "そうですね、\x01",
            "まだ解析の余地もありますし\x01",
            "さらに詳しく見てみます。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_21_5EC4 end

    def Function_22_5F87(): pass

    label("Function_22_5F87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA5")
    Call(0, 15)
    Jump("loc_5FE0")

    label("loc_5FA5")


    #C0285
    ChrTalk(
        0xFE,
        (
            "ふふ、お父さんったら\x01",
            "たまにお弁当を忘れちゃうのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE0")

    TalkEnd(0xFE)
    Return()

    # Function_22_5F87 end

    def Function_23_5FE4(): pass

    label("Function_23_5FE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_61C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6002")
    Call(0, 25)
    Jump("loc_61BB")

    label("loc_6002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6143")

    #C0286
    ChrTalk(
        0xE,
        (
            "#01105F……あ、そういえば\x01",
            "夕飯の買い物行くの忘れてたー！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#00002Fはは、夜までは時間があるし\x01",
            "ゆっくりで大丈夫だよ。\x02\x03",

            "そんなことより、\x01",
            "シズクちゃんのお見舞いの本を\x01",
            "しっかり選んであげるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xE,
        (
            "#01109Fうん、ありがとーロイド。\x02\x03",

            "#01110Fでも、ちゃんと買い物も行くから\x01",
            "みんな楽しみにしててねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_61BB")

    label("loc_6143")


    #C0289
    ChrTalk(
        0xE,
        (
            "#01103Fうーん、シズクのお見舞いに\x01",
            "持って行く本、どれがいいかなー。\x02\x03",

            "#01109F（すりすり……）\x01",
            "うん、これも面白そー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61BB")

    Jump("loc_63CD")

    label("loc_61C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_63CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DB")
    Call(0, 24)
    Jump("loc_63CD")

    label("loc_61DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633F")

    #C0290
    ChrTalk(
        0xE,
        (
            "#01109F見て見て、ロイドー。\x01",
            "こっちの本には中央広場にある\x01",
            "おっきな鐘の絵がのってるよ。\x02\x03",

            "#01100Fあの鐘は、もともと\x01",
            "《太陽の砦》にあったんだってー。\x02\x03",

            "#01111Fうーん、あんな大きいのに……\x01",
            "運ぶの大変じゃなかったのかなー？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00002F（はは、キーアの知的好奇心は\x01",
            "  俺たちの想像以上みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x109,
        "#10109F（ふふ、将来が楽しみですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_63CD")

    label("loc_633F")


    #C0293
    ChrTalk(
        0xE,
        (
            "#01100F中央広場にあるおっきな鐘、\x01",
            "《太陽の砦》にあったんだってー。\x02\x03",

            "#01111Fうーん、あんな大きいのに……\x01",
            "運ぶの大変じゃなかったのかなー？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63CD")

    TalkEnd(0xFE)
    Return()

    # Function_23_5FE4 end

    def Function_24_63D1(): pass

    label("Function_24_63D1")

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
        "#5P#01101Fえーっとー……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0295
    ChrTalk(
        0xE,
        (
            "#5P#01110Fあっ、これこれー。\x01",
            "……ひょいっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#00002Fキーア……\x01",
            "何か調べ物をしてるのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x0, 500)
    Sleep(300)

    #C0297
    ChrTalk(
        0xE,
        (
            "#01109Fあ、みんなー。\x02\x03",

            "#01110Fうん、ちょっと昔話とかが\x01",
            "のった本を集めてみてるんだー。\x02\x03",

            "一冊読んでたら、\x01",
            "色々と気になってきちゃってー。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#00102Fえっと、どれどれ……\x02\x03",

            "#00105F《クロスベル中世史》に\x01",
            "《遺跡から見るクロスベルの足跡》……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x109,
        (
            "#6P#10105Fむ、昔話って言うよりは\x01",
            "ちゃんとした歴史書や論文みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        "#12P#00202Fキーア、スゴすぎです……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        (
            "#6P#00300Fハハ、将来は学者かなにかに\x01",
            "なっちまったりしてな？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xE,
        "#01100Fえー、キーアそうなのかなー？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x105,
        "#12P#10302Fフフ、親バカここに極まれりだね。\x02",
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

    # Function_24_63D1 end

    def Function_25_67B3(): pass

    label("Function_25_67B3")

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
        "#01110Fあ、みんなー。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#00000Fキーア、何の本を読んでるんだ？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        (
            "#01109Fうん、今度シズクに\x01",
            "お見舞いに持ってく本を\x01",
            "探してたんだー。\x02\x03",

            "#01111Fどれにしよーかなー。\x01",
            "この本とか、とっても\x01",
            "面白いみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        (
            "#00105Fあれ、でもその棚って……\x01",
            "点字の本のコーナーじゃない？\x02\x03",

            "“面白いみたい”って……\x01",
            "もしかしてキーアちゃん、\x01",
            "この本が読めるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xE,
        "#01105Fうん、読めるけどー？\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x104,
        (
            "#6P#00306F読めるけどーってお前、\x01",
            "そんな軽く……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x105,
        "#6P#10302F日曜学校で習ったのかい？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        (
            "#01100Fううん、シズクと遊んでるうちに\x01",
            "覚えちゃったんだー。\x02\x03",

            "『マルクと深き森の魔女』とかも\x01",
            "点字の本に訳されてたから、\x01",
            "結構カンタンだったよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00005Fそりゃあ、知ってる本だと\x01",
            "覚えも早いのかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        (
            "#12P#00202Fふふ、この飲み込みの早さは\x01",
            "キーアならではですね。\x02",
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

    # Function_25_67B3 end

    def Function_26_6BD7(): pass

    label("Function_26_6BD7")

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
            "なるほど……\x01",
            "それは面白い考え方ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6CA0():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6CA0)
    Sleep(50)
    TurnDirection(0xD, 0x102, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_6DC0")

    #C0315
    ChrTalk(
        0xC,
        (
            "おお、ロイド君たちじゃないか。\x01",
            "丁度いいところに来たね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "こちらにいらっしゃるのが、\x01",
            "さっき話したニールセンさんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#00005Fこの方がジャーナリストの……\x02\x03",

            "#00000Fあの、はじめまして。\x01",
            "クロスベル警察・特務支援課の\x01",
            "ロイド・バニングスと言います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F10")

    label("loc_6DC0")


    #C0318
    ChrTalk(
        0xC,
        "おお、ロイド君たちじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#00005Fおじさん、その方は……？\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        "ああ、彼はニールセンさんといってね。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "国際的に活躍している\x01",
            "有名なジャーナリストの方なんだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0322
    ChrTalk(
        0xC,
        (
            "ささ、ニールセンさん。\x01",
            "彼らが最近何かと評判の\x01",
            "クロスベル警察の特務支援課です。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00002Fあの、はじめまして。\x01",
            "ロイド・バニングスと言います。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    label("loc_6F10")


    #C0324
    ChrTalk(
        0xD,
        (
            "ふむ、あの特務支援課の。\x01",
            "そしてあなたが\x01",
            "リーダーのロイドさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xD,
        "ふふ、清潔感のある良い声だ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0326
    ChrTalk(
        0x101,
        "#00001F失礼ですが……もしかして目が？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xD,
        (
            "ええ、むかし怪我を負いましてね。\x01",
            "その時に光を失いました。\x02",
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
            "館長、まだこんな所に\x01",
            "いらしたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "休憩時間はもうとっくに\x01",
            "過ぎてますよ？\x02",
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
            "すまないね、どうやらまた\x01",
            "話し込んでしまったようだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0331
    ChrTalk(
        0xC,
        (
            "というわけで、すみません。\x01",
            "私は仕事に戻りますので……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    #C0332
    ChrTalk(
        0xD,
        (
            "ええ、またよければ\x01",
            "情報交換させて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "はい、その時はいつでも\x01",
            "いらっしゃって下さい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    TurnDirection(0xD, 0x102, 500)

    #C0334
    ChrTalk(
        0xC,
        (
            "それじゃ、ロイド君たちも。\x01",
            "後のことは任せたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#00005Fあ、うん……\x02",
    )

    CloseMessageWindow()

    def lambda_721B():
        OP_95(0x8, 24560, 4019, 80, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_721B)
    OP_93(0xC, 0x0, 0x1F4)
    OP_95(0xC, 13110, 30, -2100, 2000, 0x0)

    def lambda_7250():
        OP_95(0xC, 4570, 40, -1570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7250)
    Sleep(1000)
    OP_68(12280, 1000, -5990, 2000)
    OP_6F(0x1)

    #C0336
    ChrTalk(
        0x102,
        "#00105Fええっと……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xD,
        (
            "ええ、改めて\x01",
            "自己紹介させて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "はじめまして。\x01",
            "フリーで記者をさせてもらっている\x01",
            "ニールセンと言う者です。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        "#00000Fはい、こちらこそお願いします。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        (
            "#00108F（ニールセンさん――\x01",
            "  どこかで聞いたことが\x01",
            "  あるような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xD,
        (
            "ふむ、支援課の皆さんとは\x01",
            "ぜひ一度お会いしたいと\x01",
            "思っていたので実に光栄です。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        (
            "突然で申し訳ないのですが、\x01",
            "皆さんにお願いしたいことが\x01",
            "あるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        "少々お時間を頂けないでしょうか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0344
    ChrTalk(
        0x101,
        "#00005Fええ、何でしょう？\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xD,
        (
            "はい、実は今\x01",
            "例の教団事件について\x01",
            "調査を行っているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xD,
        (
            "その内容でいくつか\x01",
            "不明な箇所がありましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xD,
        (
            "事件解決の立役者として\x01",
            "本件に関わりの深い皆さんに\x01",
            "取材させて頂きたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x109,
        "#10101F教団事件の取材、ですか……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x105,
        (
            "#10302Fふふ、何やら色々と\x01",
            "掴んでいそうな口ぶりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x102,
        (
            "#00101F（ロイド、どうするの？）\x02\x03",

            "（内容が内容だし、\x01",
            "  あまり余計なことは\x01",
            "  言えないと思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00001F（そうだな……）\x02\x03",

            "#00003F（取材に付き合うことで、\x01",
            "  事件について改めて整理できる\x01",
            "  かもしれないけど……）\x02",
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

    # Function_26_6BD7 end

    def Function_27_76D9(): pass

    label("Function_27_76D9")

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
            "ニールセンの取材に協力する\x01",      # 0
            "いったん考える\x01",                  # 1
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
        (0, "loc_7753"),
        (1, "loc_79D8"),
        (SWITCH_DEFAULT, "loc_7AC8"),
    )


    label("loc_7753")


    #C0352
    ChrTalk(
        0x101,
        (
            "#00001F分かりました、俺たちで\x01",
            "よければ協力させて頂きます。\x02\x03",

            "ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xD,
        (
            "ええ、立場もあるでしょうし、\x01",
            "仰りにくい事に関しては\x01",
            "伏せて頂いて構いません。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xD,
        (
            "それに、ここで伺ったことは\x01",
            "原則オフレコにさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        (
            "#00002Fなるほど……\x01",
            "ご理解ありがとうございます。\x02\x03",

            "#00005Fでも場所はどうしましょう。\x01",
            "ここだと問題がありそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xD,
        (
            "ええ、それなら２階にある\x01",
            "談話スペースはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xD,
        (
            "人が来たらすぐに分かりますし、\x01",
            "絶好の場所だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#00000F確かにそうですね。\x01",
            "では早速行きましょう。\x02",
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
            "クエスト【教団事件に関する取材協力】\x07\x00",
            "を開始した！\x02",
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
    Jump("loc_7AC8")

    label("loc_79D8")


    #C0360
    ChrTalk(
        0x101,
        (
            "#00006Fすみません。\x01",
            "今は他にも案件を抱えていて……\x02\x03",

            "#00001F後から引き受けても結構ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xD,
        (
            "ええ、まだしばらくは\x01",
            "ここにいるので\x01",
            "それでも構いませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xD,
        (
            "では都合が付いたら、\x01",
            "いつでも声を掛けて下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC0")
    EventEnd(0x5)

    label("loc_7AC0")

    SetScenarioFlags(0x133, 3)
    Jump("loc_7AC8")

    label("loc_7AC8")

    Return()

    # Function_27_76D9 end

    def Function_28_7AC9(): pass

    label("Function_28_7AC9")

    TalkBegin(0xD)

    #C0363
    ChrTalk(
        0xD,
        "……ロイドさんですね。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xD,
        (
            "教団事件に関する取材、\x01",
            "付き合って頂けますか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Call(0, 27)
    TalkEnd(0xD)
    Return()

    # Function_28_7AC9 end

    def Function_29_7B25(): pass

    label("Function_29_7B25")

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
            "#11Pこの度は取材に付き合って頂き、\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xD,
        (
            "#11Pでは、最初に状況整理から\x01",
            "始めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xD,
        (
            "#11P女神を否定し、\x01",
            "悪魔を崇拝することを\x01",
            "その教義とするＤ∴Ｇ教団──\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xD,
        (
            "#11P１０数年前より、大陸の各地で\x01",
            "幼い子供たちの拉致を繰り返した\x01",
            "最悪の犯罪集団――\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xD,
        (
            "#11Pまずは、この拉致事件が\x01",
            "一旦の収束をみた６年前に\x01",
            "遡りたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xD,
        (
            "当時、大陸各地に点在した教団の\x01",
            "ロッジを一斉検挙・摘発する\x01",
            "大規模な作戦が行われたわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xD,
        (
            "#11Pこの作戦を実行した勢力については\x01",
            "皆さんもご存知ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        "#00003F#6Pええ、それは――\x02",
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
            "#1K６年前に、Ｄ∴Ｇ教団の\x01",
            "一斉検挙作戦を実行した勢力とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "各国の軍隊・警察組織\x01",      # 0
            "各国の遊撃士協会\x01",          # 1
            "その両方\x01",                  # 2
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
        (0, "loc_7F32"),
        (1, "loc_7FBC"),
        (2, "loc_804A"),
        (SWITCH_DEFAULT, "loc_8098"),
    )


    label("loc_7F32")


    #C0374
    ChrTalk(
        0x101,
        (
            "#00000F#6P各国の軍隊・警察組織ですね。\x02\x03",

            "#00006F……いや、それだけじゃない。\x02\x03",

            "#00001F各国の遊撃士協会も\x01",
            "協力したと聞いています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8098")

    label("loc_7FBC")


    #C0375
    ChrTalk(
        0x101,
        (
            "#00000F#6P各国の遊撃士協会ですね。\x02\x03",

            "#00006F……いや、当然それだけじゃない。\x02\x03",

            "#00001F各国の軍隊・警察組織も\x01",
            "協力したと聞いています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8098")

    label("loc_804A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0376
    ChrTalk(
        0x101,
        (
            "#00001F#6P各国の軍隊・警察組織、\x01",
            "そして遊撃士協会ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8098")

    label("loc_8098")


    #C0377
    ChrTalk(
        0x102,
        (
            "#00100F#6P確か、事件の規模の\x01",
            "大きさをかんがみて国際的な\x01",
            "捜査体制が設立されたのですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xD,
        "#11Pええ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xD,
        (
            "#11Pそして、そんな体制の中、\x01",
            "遊撃士カシウス・ブライトが\x01",
            "総指揮を執り――\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0380
    ChrTalk(
        0x102,
        (
            "#00105F#6Pす、すみません。\x01",
            "ちょっといいですか？\x02\x03",

            "#00101Fカシウス・ブライトというと……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x109,
        (
            "#10111F#12Pも、もしかして――\x01",
            "リベール王国軍司令の\x01",
            "カシウス准将のことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xD,
        "#11Pええ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xD,
        (
            "#11P一度、王国軍を退役した後、\x01",
            "１０年ほど遊撃士として活躍し、\x01",
            "再び王国軍に復帰したそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x105,
        (
            "#10302F#12Pふぅん、なかなか\x01",
            "面白い経歴の持ち主みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x102,
        (
            "#00106F#6Pそ、それもそうだけど――\x02\x03",

            "#00108F今まで気付かなかったけど\x01",
            "もしかして『ブライト』って……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#00003F#6P――ああ、俺も一課の研修中に\x01",
            "捜査資料を見て知った時は驚いたよ。\x02\x03",

            "#00001Fカシウス・ブライト准将は、\x01",
            "エステル・ブライトの実の父親だ。\x02\x03",

            "ヨシュアの方は養子みたいだけどね。\x02",
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
        "#00105F#6Pや、やっぱり……\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x109,
        "#10105F#12P予想外の繋がりですね……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x105,
        (
            "#10304F#11Pチェイスバトルの時も\x01",
            "かなりのものだと思わされたけど……\x02\x03",

            "#10302Fまさかそんな有名人の\x01",
            "娘さんだったとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xD,
        (
            "#11Pふむ、皆さんはカシウス准将の\x01",
            "娘さんとお知り合いでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xD,
        (
            "#11P私も記者として、\x01",
            "彼女の活躍は知る所ですが……\x02",
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
        "#00002F#6Pまあ、色々と縁がありまして。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x102,
        (
            "#00106F#6Pすみません、\x01",
            "話の腰を折ってしまって……\x02\x03",

            "#00100Fどうぞ続けてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xD,
        "#11Pええ、それでは。\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xD,
        (
            "#11Pそうして、当時遊撃士だった\x01",
            "カシウス・ブライトの総指揮により\x01",
            "実行された検挙作戦ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        (
            "#11Pその作戦によって、\x01",
            "教団勢力のおよそ９割が\x01",
            "壊滅したと言われています。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xD,
        (
            "#11Pちなみに当時、\x01",
            "このクロスベルから参加したのが\x01",
            "クロスベル警察のセルゲイ班――\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xD,
        (
            "#11P現在あなたたち特務支援課の\x01",
            "課長であるセルゲイさんと、\x01",
            "規格外の新人とされた２人――\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        (
            "#11Pあのアリオス・マクレインと\x01",
            "ロイドさんのお兄さんである\x01",
            "ガイさんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#00003F#6P……どうやら事件について\x01",
            "かなり深い所まで\x01",
            "調べていらっしゃるんですね。\x02\x03",

            "#00008Fそれに俺と兄貴との関係まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        (
            "#00105F#6P確かに、その辺りの情報は\x01",
            "警察の中でも一部にしか\x01",
            "知られていないはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "#11Pええまあ、この商売も\x01",
            "長く続けていると色々な方面に\x01",
            "顔が利くようになりますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xD,
        (
            "#11Pそれにガイさんとは\x01",
            "何度か取材を通じて親しくさせて\x01",
            "頂いていましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        "#00005F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        (
            "#11P……ええ、ガイさんには生前\x01",
            "色々とお世話になったものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xD,
        (
            "#11P……ふむ、\x01",
            "話を元に戻しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xD,
        (
            "#11Pそれから\x01",
            "クロスベルからはもう１人――\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xD,
        (
            "#11P民間アドバイザーとして\x01",
            "イアン・グリムウッド弁護士が\x01",
            "関わっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "#11Pイアン弁護士は当時から\x01",
            "人権問題に詳しい方として\x01",
            "有名でしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xD,
        (
            "#11P各国の拉致被害者の情報収集に\x01",
            "貢献したと伺っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x102,
        (
            "#00104F#6Pそういえば、\x01",
            "先生自身も仰っていました。\x02\x03",

            "#00100Fなるほど、そういう形で協力を。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xD,
        (
            "#11Pまた、本件には\x01",
            "教会関係者や謎の組織による\x01",
            "介入も密かにあったと言われ――\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xD,
        (
            "#11Pそれらの働きによって、残る勢力も\x01",
            "完全に駆逐されたと言われています。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#00003F#6P（教会関係者か……）\x02",
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
            "#10101F#12P（確か、アルタイル・ロッジで\x01",
            "  会ったケビン神父も\x01",
            "  関わっていたという話でしたね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        (
            "#00101F#6P（ちなみに、謎の組織というのは\x01",
            "  例の《結社》のことでしょうね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x105,
        (
            "#10302F#11P（フフ、どちらもいまいち\x01",
            "  実体の掴めない連中だよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xD,
        "#11Pふむ……\x02",
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
            "#11Pともかく――\x01",
            "そうして教団事件は\x01",
            "終わりを迎えたはずでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xD,
        (
            "#11Pですが数ヶ月前、事件は\x01",
            "まだ終わっていなかったことが\x01",
            "判明します。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xD,
        "#11P理由は、皆さんもご承知の通り……\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x101,
        (
            "#00006F#6Pええ、教団の残党である\x01",
            "ヨアヒム・ギュンターの存在が\x01",
            "明るみに出たためですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xD,
        "#11Pええ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xD,
        (
            "#11Pちなみに彼は、教団の様々な\x01",
            "裏事情に詳しかったようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xD,
        (
            "#11P果たしてヨアヒム・ギュンターは、\x01",
            "教団の指導者だったのでしょうか？\x02",
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
            "#1Kヨアヒム・ギュンターは\x01",
            "Ｄ∴Ｇ教団の指導者だったのか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "その通り\x01",            # 0
            "幹部司祭の一人\x01",      # 1
            "単なる教団員\x01",        # 2
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
        (0, "loc_9011"),
        (1, "loc_90BD"),
        (2, "loc_9105"),
        (SWITCH_DEFAULT, "loc_919C"),
    )


    label("loc_9011")


    #C0427
    ChrTalk(
        0x101,
        (
            "#00001F#6Pその通りです、彼は実質\x01",
            "教団のトップに位置し――\x02\x03",

            "#00011F（――じゃないだろ。\x01",
            "  俺は何を言ってるんだ。）\x02\x03",

            "#00006F――ではなく、\x01",
            "彼は幹部司祭の一人です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_919C")

    label("loc_90BD")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0428
    ChrTalk(
        0x101,
        (
            "#00001F#6Pいえ、違います。\x01",
            "彼は幹部司祭の一人です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_919C")

    label("loc_9105")


    #C0429
    ChrTalk(
        0x101,
        (
            "#00001F#6Pいえ、彼は単なる教団員――\x02\x03",

            "#00011F（――じゃないだろ。\x01",
            "  俺は何を言ってるんだ。）\x02\x03",

            "#00006F――ではなく、\x01",
            "彼は幹部司祭の一人です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_919C")

    label("loc_919C")


    #C0430
    ChrTalk(
        0x102,
        (
            "#00103F#6Pええ、それは\x01",
            "本人も認めるところでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#00003F#6Pただし、彼は研究者の顔を持ち、\x01",
            "数々の実験の統括者でもありました。\x02\x03",

            "#00001Fだからこそ、教団の様々な\x01",
            "内部事情に詳しかったんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xD,
        "#11Pふむ、納得の行く理屈ですね。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xD,
        (
            "#11Pそして、そんな立場にいた\x01",
            "彼は各地で行った儀式の\x01",
            "結果を元に研究を重ね……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xD,
        (
            "#11P６年前の摘発事件からは\x01",
            "難を逃れることに成功し、\x01",
            "人知れず潜伏。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xD,
        (
            "#11Pその後、『楽園』なる施設での\x01",
            "ハルトマン元議長の弱味を握って\x01",
            "クロスベルに落ち延びた。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xD,
        (
            "#11Pそうして、ついには\x01",
            "『真なる叡智』の名を持つ薬物、\x01",
            "《グノーシス》を完成させた。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xD,
        (
            "#11P仔細は判りかねますが……\x01",
            "教団の大望とやらを遂げるために。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x102,
        (
            "#00101F#6P教団の大望……\x02\x03",

            "#00108F（確か、キーアちゃんを\x01",
            "  《神》にするとか\x01",
            "  言っていたけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        (
            "#00008F#6P（ああ、それに紅いグノーシスを\x01",
            "  服用したヨアヒムには何かが\x01",
            "  見えていたみたいだったが……）\x02\x03",

            "#00006F（俺たちも結局、詳しいことは\x01",
            "  なにも分かっていないんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xD,
        (
            "#11P……ふむ、相変わらず\x01",
            "不明な箇所も多いわけですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xD,
        (
            "#11Pここまでの話で、\x01",
            "事件の概要については\x01",
            "大分整理が出来たと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xD,
        (
            "#11Pでは最後にそれらを踏まえて、\x01",
            "Ｄ∴Ｇ教団のルーツ――\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xD,
        (
            "#11Pそれを考察してみたいのですが\x01",
            "宜しいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x101,
        "#00005F#6P教団のルーツ……\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xD,
        (
            "#11Pはい、ちなみにロイドさんは、\x01",
            "教団のルーツは一体何年以上前に\x01",
            "遡るとお考えですかね？\x02",
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
            "#1KＤ∴Ｇ教団のルーツは\x01",
            "何年以上前に遡ると考えられる？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "１２００年以上前\x01",      # 0
            "５００年以上前\x01",        # 1
            "５０年以上前\x01",          # 2
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
        (0, "loc_9779"),
        (1, "loc_9866"),
        (2, "loc_98BE"),
        (SWITCH_DEFAULT, "loc_9982"),
    )


    label("loc_9779")


    #C0447
    ChrTalk(
        0x101,
        (
            "#00008F#6P（１２００年以上前……\x01",
            "  いや、例えそうだったとしても\x01",
            "  そこまでは知りようがない。）\x02\x03",

            "#00003F（これまでに得た情報から\x01",
            "  確実に言えることは……）\x02\x03",

            "#00001Fおそらく５００年以上前――\x01",
            "中世の時代にまで遡ると考えられます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9982")

    label("loc_9866")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0448
    ChrTalk(
        0x101,
        (
            "#00001F#6Pおそらく５００年以上前――\x01",
            "中世の時代にまで遡るはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9982")

    label("loc_98BE")


    #C0449
    ChrTalk(
        0x101,
        (
            "#00011F#6P（５０年前……\x01",
            "  いや、そんな最近のはずがない。）\x02\x03",

            "#00003F（これまでに得た情報から\x01",
            "  確実に言えることは……）\x02\x03",

            "#00001Fおそらく５００年以上前――\x01",
            "中世の時代にまで遡るはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9982")

    label("loc_9982")


    #C0450
    ChrTalk(
        0xD,
        "#11Pふむ、それはどうしてですか？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        (
            "#00003F#6P……いえ、実は俺たちは\x01",
            "直接ヨアヒムから聞いているんです。\x02\x03",

            "#00008F５００年前、この地に存在していた\x01",
            "錬金術師たちの一団――\x02\x03",

            "#00001F教団は、当時から\x01",
            "彼らの技術を利用していたと。\x02\x03",

            "#00006Fもっとも、それ以前の\x01",
            "前身については不明ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xD,
        (
            "#11Pなるほど、ヨアヒム・\x01",
            "ギュンターがそんなことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xD,
        (
            "#11Pこの地に存在した錬金術師――\x01",
            "つまりは《星見の塔》を\x01",
            "建造したとされる者たちですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xD,
        (
            "#11Pあくまで伝承的だった知識が\x01",
            "こんな形で裏付けされるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x105,
        "#10304F#12Pフフ、確かに驚きだよね。\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xD,
        (
            "#11Pふむ、そしてつまりは\x01",
            "ロイドさんたちが\x01",
            "預かっている少女――\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xD,
        (
            "#11P彼女もその時代の出身であると\x01",
            "考えられるわけですね？\x02",
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
            "#00108F#6P一体、事件のことを\x01",
            "どこまでご存知なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xD,
        (
            "#11Pすみません、今のは少々、\x01",
            "デリカシーに欠ける発言でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xD,
        (
            "#11Pこれは私が持っていた情報に\x01",
            "皆さんから伺った情報を合わせて\x01",
            "ふと湧き上がった『妄想』です。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xD,
        (
            "#11P女神に誓って\x01",
            "触れ回ったりする事はないので\x01",
            "どうか安心してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        "#00006F#6Pい、いえ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    #C0464
    ChrTalk(
        0xD,
        (
            "#11P……ふむ、とりあえず\x01",
            "取材の方はこんな所でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xD,
        (
            "#11P今日は本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xD,
        (
            "#11Pおかげさまで、\x01",
            "有意義な情報が得られました。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x102,
        "#00104F#6P……いえ、こちらこそ。\x02",
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
            "#11Pそうこうしている間に\x01",
            "そろそろ次の取材に向かわないと\x01",
            "いけない時間になってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xD,
        "#11Pでは失礼ながら私はこれで。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xD,
        (
            "#11Pまた皆さんとお話できる\x01",
            "機会を楽しみにしています。\x02",
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

    def lambda_9FE9():
        OP_95(0xD, 28680, 4019, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_9FE9)
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

    def lambda_A032():
        OP_95(0xD, 9240, -490, 20, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_A032)
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
            "#10105F#12P目が見えないという話でしたけど、\x01",
            "随分軽やかな足取りですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x105,
        "#10300F#11Pふむ、ほんと大したものだね。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x101,
        (
            "#00006F#6Pなんていうか……\x01",
            "色々と驚かされる人だったな。\x02\x03",

            "#00000Fキーアの件については\x01",
            "どうやら信用できそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x102,
        "#00108F#5Pそうね……\x02",
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
        "#00105F#5Pあっ――！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)

    #C0476
    ChrTalk(
        0x101,
        "#00005F#12Pどうかしたか、エリィ？\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x102,
        (
            "#00101F#5Pやっと思い出したの。\x01",
            "今の人はマルセル・ニールセン――\x02\x03",

            "１０年ほど前にフューリッツァ賞を\x01",
            "受賞した、クロスベル出身の著名な\x01",
            "ジャーナリストよ。\x02",
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
            "#10305F#11Pへえ、あんまり詳しくないけど\x01",
            "フューリッツァ賞って言うと……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        (
            "#00003F#6Pああ、毎年最も優秀な\x01",
            "ジャーナリストに贈られる\x01",
            "国際的な賞だったはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x109,
        (
            "#10101F#12Pなるほど……\x01",
            "それであの洞察力ですか。\x02\x03",

            "#10105Fけど、クロスベル出身ってことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#00103F#5Pええ、かつては\x01",
            "クロスベルタイムズで\x01",
            "記者をしていたはずよ。\x02\x03",

            "#00108Fそして、まさに賞を取った取材――\x01",
            "その時の戦場取材で、\x01",
            "目の光を失ってしまったらしいの。\x02\x03",

            "#00100Fけれど、その後も積極的に\x01",
            "大陸各地を巡っては取材を続け、\x01",
            "数多の報道誌に寄稿しているという。\x02\x03",

            "#00104Fジャーナリストとしては\x01",
            "知る人ぞ知る――そんな人物よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x105,
        (
            "#10302F#11Pふぅん、それはまたとんでもなく\x01",
            "大した人物じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#00004F#12Pニールセンさんか……\x02\x03",

            "#00000F機会があれば、\x01",
            "今後も話を伺ってみたいかもな。\x02",
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
            "クエスト【教団事件に関する取材協力】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A671")
    OP_2C(0x6E, 0x2)
    Jump("loc_A685")

    label("loc_A671")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A685")
    OP_2C(0x6E, 0x1)

    label("loc_A685")

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

    # Function_29_7B25 end

    def Function_30_A6EE(): pass

    label("Function_30_A6EE")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A816")
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
    Jump("loc_A875")

    label("loc_A816")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_A875")

    FadeToBright(1000, 0)
    OP_0D()

    #C0485
    ChrTalk(
        0x101,
        "#00000Fこんにちは、マイルズおじさん。\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xC,
        (
            "やあ、ロイド君。\x01",
            "もしかして、依頼をみて\x01",
            "来てくれたのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        (
            "#00002Fああ、そういうこと。\x02\x03",

            "よかったら、事情を聞かせて\x01",
            "もらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x102,
        (
            "#00100F確か、星見の塔に残された\x01",
            "古文書を回収したいとの事でしたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xC,
        "ああ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xC,
        (
            "ウルスラ間道のはずれに\x01",
            "『星見の塔』という遺跡が\x01",
            "あるのは知っているだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xC,
        (
            "あそこは以前、警備隊によって\x01",
            "調査が禁止されていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        (
            "最近になって、許可さえあれば\x01",
            "調査できるようになったらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x109,
        (
            "#10103Fたしかに、最近は\x01",
            "そういう風になってますね。\x02\x03",

            "#10100Fあの場所は前司令が未調査のまま\x01",
            "放っておいた場所ですから……\x02\x03",

            "情報収集のために、民間人でも\x01",
            "レポートの提出を条件に\x01",
            "調査ができるようになったんです。\x02\x03",

            "最近じゃ、魔獣も\x01",
            "出なくなっているみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x101,
        "#00005Fへえ、そうなのか……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACF3")

    #C0495
    ChrTalk(
        0xC,
        (
            "うむ、それでこの間、\x01",
            "例のニールセンさんが\x01",
            "調査に入ったそうなんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xC,
        (
            "そこで面白いものを\x01",
            "見つけたらしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x101,
        (
            "#00000Fあの記者さんが……\x02\x03",

            "#00005Fで、でもニールセンさんって、\x01",
            "たしか目が……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xC,
        (
            "ああ、そうなんだが……\x01",
            "その時はクロスベルタイムズの\x01",
            "記者さんを連れて行ったようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        "いや、本当に行動力のあるお人だよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFC9")

    label("loc_ACF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 2)), scpexpr(EXPR_END)), "loc_AE7F")

    #C0500
    ChrTalk(
        0xC,
        (
            "うむ、それでこの間、\x01",
            "例のニールセンさんが\x01",
            "調査に入ったそうなんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xC,
        (
            "そこで面白いものを\x01",
            "見つけたらしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x101,
        (
            "#00000Fニールセンさん……\x01",
            "前におじさんが言っていた\x01",
            "ジャーナリストの人だっけ。\x02\x03",

            "そんな場所にわざわざ\x01",
            "調査に入るなんて、\x01",
            "行動力がある人みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        (
            "ああ、実は彼は\x01",
            "目が不自由なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xC,
        (
            "その時はクロスベルタイムズの\x01",
            "記者さんを連れて行ったようだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFC9")

    label("loc_AE7F")


    #C0505
    ChrTalk(
        0xC,
        (
            "うむ、それでこの間、\x01",
            "私の知り合いのニールセンさんという\x01",
            "記者の方が調査に入ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "そこで面白いものを\x01",
            "見つけたらしいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000Fへえ、そんな場所にわざわざ\x01",
            "調査に入るなんて、\x01",
            "行動力がある人みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xC,
        (
            "ああ、実は彼は\x01",
            "目が不自由なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xC,
        (
            "その時はクロスベルタイムズの\x01",
            "記者さんを連れて行ったようだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFC9")


    #C0510
    ChrTalk(
        0x105,
        (
            "#10300Fで、その“面白いもの”っていうのが、\x01",
            "依頼にあった『古文書』ってわけだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x104,
        (
            "#00303Fそういや……\x01",
            "前に《銀》を追っていた時に、\x01",
            "見かけた気がするな。\x02",
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
            "#00300F《星見の塔》の\x01",
            "途中の階と最上階にあった\x01",
            "やたらとデカイ本棚……\x02\x03",

            "あそこに収められてたのが\x01",
            "古文書だったってわけか。\x02",
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
            "おお、行ったことがあるのかね！\x01",
            "それは話が早いじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xC,
        (
            "図書館としては、貴重な古文書が\x01",
            "そんな場所に放置されているのを\x01",
            "見過ごす事は出来ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        "どうだね、頼めないかな？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#00103F確かに、図書館の重要な役目の\x01",
            "一つともいうべき仕事ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x109,
        (
            "#10101Fでも……あんな大量の本を\x01",
            "あたし達だけで運ぶのは、\x01",
            "さすがに無理じゃないですか？\x02\x03",

            "#10106F運び出そうと思ったら、\x01",
            "何往復することになるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        "#00005Fそ、それもそうだな。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xC,
        (
            "ああ、さすがにそこまで\x01",
            "お願いするつもりはないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xC,
        (
            "君たちには本を運び出すための\x01",
            "前準備として、かかる労力と費用を\x01",
            "調査してきて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xC,
        (
            "警備隊や市庁舎のほうにも\x01",
            "すでに許可はとってあるしね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B453")

    #C0522
    ChrTalk(
        0x103,
        "#00202Fなるほど、そういうことですか。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x105,
        (
            "#10300Fその調査結果をもとに、\x01",
            "本の回収計画を進めるわけだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4B8")

    label("loc_B453")


    #C0524
    ChrTalk(
        0x105,
        (
            "#10304Fなるほど、そういうことか。\x02\x03",

            "#10300Fその調査結果をもとに、\x01",
            "本の回収計画を進めるわけだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4B8")


    #C0525
    ChrTalk(
        0x102,
        (
            "#00100Fたしかに、一度\x01",
            "《塔》を上った私たちなら\x01",
            "適任かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xC,
        "どうだい、引き受けてくれるかな？\x02",
    )

    CloseMessageWindow()
    OP_29(0x71, 0x1, 0x0)
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B544")
    Call(0, 33)

    label("loc_B544")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B57E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B588")

    label("loc_B57E")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B588")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_A6EE end

    def Function_31_B5A0(): pass

    label("Function_31_B5A0")

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
            "引き受ける\x01",      # 0
            "やめる\x01",          # 1
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
        (0, "loc_B602"),
        (1, "loc_B607"),
        (SWITCH_DEFAULT, "loc_B6AB"),
    )


    label("loc_B602")

    Jump("loc_B6AB")

    label("loc_B607")


    #C0527
    ChrTalk(
        0x101,
        (
            "#00000Fごめん、おじさん。\x01",
            "今はちょっと\x01",
            "手が離せなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xC,
        (
            "う～ん、そうか。\x01",
            "なら仕方ないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xC,
        (
            "それでは、\x01",
            "もし手が空いたら\x01",
            "また声をかけてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x152, 7)
    Jump("loc_B6AB")

    label("loc_B6AB")

    Return()

    # Function_31_B5A0 end

    def Function_32_B6AC(): pass

    label("Function_32_B6AC")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    CreatePortrait(1, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B7A8")
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
    Jump("loc_B807")

    label("loc_B7A8")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_B807")

    FadeToBright(1000, 0)
    OP_0D()

    #C0530
    ChrTalk(
        0xC,
        (
            "君たちには《星見の塔》に\x01",
            "置いてあるという古文書の\x01",
            "調査をしてもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "本を運び出すための前準備として、\x01",
            "かかる労力と費用を知りたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xC,
        "どうだね、引き受けてくれるかな？\x02",
    )

    CloseMessageWindow()
    Call(0, 31)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E1")
    Call(0, 33)

    label("loc_B8E1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B91B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B925")

    label("loc_B91B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B925")

    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_B6AC end

    def Function_33_B93D(): pass

    label("Function_33_B93D")


    #C0533
    ChrTalk(
        0x101,
        (
            "#00002Fうん、分かった。\x01",
            "引き受けさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xC,
        "ありがとう、助かるよ。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xC,
        (
            "それじゃ、ちょっと待ってくれ。\x01",
            "警備隊のほうに連絡して、\x01",
            "星見の塔の封鎖を解いてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x109,
        (
            "#10100Fあ、それなら\x01",
            "自分にお任せください。\x02\x03",

            "直接ソーニャ司令に\x01",
            "連絡したほうが早いでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA55():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA55)
    Sleep(50)

    def lambda_BA65():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BA65)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA90")

    def lambda_BA85():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BA85)
    Sleep(50)

    label("loc_BA90")


    def lambda_BA95():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA95)
    Sleep(50)

    def lambda_BAA5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BAA5)
    Sleep(300)

    #C0537
    ChrTalk(
        0x104,
        (
            "#00300Fだな。\x01",
            "その方が手っ取り早そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xC,
        "おお、ならよろしく頼むよ。\x02",
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
    SetChrName("ソーニャの声")

    #A0539
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──はい、\x01",
            "こちらソーニャ・ベルツ。\x02",
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
            "#10100F司令、お疲れ様です。\x01",
            "ノエル・シーカーです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ソーニャの声")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あら、ノエル。\x01",
            "何かあったのかしら？\x02",
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
            "#10103Fええ、実は……\x02",
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
            "ノエルは星見の塔の調査を\x01",
            "引き受けたことを説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ソーニャの声")

    #A0544
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、例の件ね。\x02\x03",

            "こちらにも話が届いているわ。\x01",
            "確かにあなたたちなら\x01",
            "適任といえるでしょう。\x02\x03",

            "すぐに封鎖を解いておくよう、\x01",
            "周辺を巡回している部隊に\x01",
            "連絡しておくわ。\x02",
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
            "#10101Fはっ、ありがとうございます！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ソーニャの声")

    #A0546
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "くれぐれも気をつけるように。\x01",
            "……では、失礼するわね。\x07\x00\x02",
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
        "#10100F……はい、これで大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        "#00002Fありがとう、ノエル。\x02",
    )

    CloseMessageWindow()

    def lambda_BEA2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEA2)
    Sleep(50)

    def lambda_BEB2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEB2)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEDD")

    def lambda_BED2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BED2)
    Sleep(50)

    label("loc_BEDD")


    def lambda_BEE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEE2)
    Sleep(50)

    def lambda_BEF2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEF2)
    Sleep(300)

    #C0549
    ChrTalk(
        0xC,
        (
            "はあ、えらくスムーズに\x01",
            "ことが運ぶもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xC,
        (
            "この顔の広さも\x01",
            "特務支援課ならではかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、そうですね。\x02\x03",

            "それじゃあ、さっそく\x01",
            "星見の塔に向かいましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x101,
        (
            "#00004Fああ、そうしよう。\x02\x03",

            "#00002Fマイルズおじさん、\x01",
            "楽しみに待っててよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xC,
        "ああ、気をつけてな。\x02",
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
            "クエスト【塔の古文書調査】\x07\x00",
            "を開始した！\x02",
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

    # Function_33_B93D end

    def Function_34_C084(): pass

    label("Function_34_C084")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6520, 1000, 8200, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C14D")
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
    Jump("loc_C1AC")

    label("loc_C14D")

    SetChrPos(0x101, 5000, 30, 8500, 90)
    SetChrPos(0x102, 5000, 30, 7500, 90)
    SetChrPos(0x104, 3800, 30, 8000, 90)
    SetChrPos(0x109, 4000, 30, 9000, 90)
    SetChrPos(0x105, 4000, 30, 7000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_C1AC")

    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0555
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは本棚の本が\x01",
            "消えていた事をマイルズに報告した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0556
    ChrTalk(
        0x101,
        "#00003F……と、いうわけなんだ。\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0xC,
        (
            "ま、まさか、そんな大量の本を\x01",
            "誰が持っていったっていうんだ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xC,
        (
            "それも、誰にも気づかれずになんて……\x01",
            "常識的に考えられないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#00008F……残念だけど\x01",
            "俺たちにも見当がつかないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xC,
        "……はあ、仕方ないか……\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xC,
        (
            "せめて、どんな本があるか\x01",
            "だけでも知りたかった所だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x104,
        (
            "#00302Fああいや、\x01",
            "一応数冊は残ってたんッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x102,
        (
            "#00102F一応それだけは\x01",
            "回収できましたし……\x02\x03",

            "他の本の傾向くらいは\x01",
            "分かるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xC,
        "ほ、本当かいっ！？\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#00000Fただ、内容は俺たちには\x01",
            "ちんぷんかんぷんなんだ。\x02\x03",

            "価値のあるものかは\x01",
            "分からないけど……\x01",
            "とりあえず渡しておくよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0566
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塔で回収した本を\x01",
            "マイルズに渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0567
    ChrTalk(
        0xC,
        "こ、これは……\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x105,
        (
            "#10300Fどうやら、\x01",
            "中世の時代の本みたいだね。\x02\x03",

            "古びてすすけてるから、\x01",
            "字の判別はつかないかも\x01",
            "知れないけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0569
    ChrTalk(
        0x109,
        "#10105Fど、どうかなさったんですか？\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xC,
        (
            "す、すごい……\x01",
            "こっちも、こっちも……\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xC,
        "この本は、中世の魔導書だよ！\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x102,
        "#00105F魔導書……というと？\x02",
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xC,
        (
            "昔の人が書き記した、\x01",
            "錬金術や魔導具の\x01",
            "扱い方が載った本さ！\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xC,
        (
            "解読しないと判らないけど、\x01",
            "載ってる図解を見る限り\x01",
            "まず間違いないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x101,
        (
            "#00002Fへえ……\x01",
            "結構貴重な本なんだね。\x02\x03",

            "#00003Fでも、あの場所に\x01",
            "残っていたということは……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C76C")

    #C0576
    ChrTalk(
        0x103,
        (
            "#00200F本を持っていった者には\x01",
            "あまり重要な本じゃなかった、\x01",
            "ということでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x105,
        (
            "#10300Fこの本からその人物の手がかりを\x01",
            "見つけるのは難しそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7FA")

    label("loc_C76C")


    #C0578
    ChrTalk(
        0x105,
        (
            "#10300F本を持っていった者には\x01",
            "あまり重要な本じゃなかった……\x01",
            "ってところかな？\x02\x03",

            "この本からその人物の手がかりを\x01",
            "見つけるのは難しそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7FA")


    #C0579
    ChrTalk(
        0x101,
        "#00001Fああ……\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x102,
        "#00108F不可解な謎が残ってしまったわね……\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xC,
        (
            "いやいや、\x01",
            "貴重な本を回収してくれた\x01",
            "ことには変わりない。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xC,
        (
            "君たちはよくやってくれたよ。\x01",
            "やはり依頼して正解だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x109,
        "#10100Fあはは……恐縮です。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xC,
        (
            "この本は地下の書庫に\x01",
            "大切に保存させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xC,
        (
            "ニールセンさんたちとも\x01",
            "色々と考察することができそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xC,
        (
            "ありがとうな、ロイドくんたち。\x01",
            "また何かあったらよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        (
            "#00002Fあ、うん。\x01",
            "いつでもお待ちしてるよ。\x02",
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
            "クエスト【塔の古文書調査】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA44")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_CA4E")

    label("loc_CA44")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_CA4E")

    OP_29(0x71, 0x1, 0x5)
    OP_29(0x71, 0x1, 0x6)
    OP_29(0x71, 0x4, 0x10)
    SetScenarioFlags(0x0, 5)
    SetChrPos(0x0, 5000, 30, 8000, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_34_C084 end

    def Function_35_CA7A(): pass

    label("Function_35_CA7A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CB69")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0589
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　図書館ニュース　～\x01",
            "  皆様のリクエストに応え、\x01",
            "  以下書籍を追加しました。\x01",
            "  ・闇医者グレン１３巻\x01",
            "  ・闇医者グレン１４巻\x01",
            "※１階の本棚に入っております。\x01",
            "　興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CB69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC7D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　図書館ニュース　～\x01",
            "  皆様のリクエストに応え、\x01",
            "  以下書籍を追加しました。\x01",
            "  ・闇医者グレン９巻\x01",
            "  ・闇医者グレン１０巻\x01",
            "  ・闇医者グレン１１巻\x01",
            "  ・闇医者グレン１２巻\x01",
            "※１階の本棚に入っております。\x01",
            "  興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CC7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CD56")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0591
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　図書館ニュース　～\x01",
            "  皆様のリクエストに応え、\x01",
            "  以下書籍を追加しました。\x01",
            "  ・１分クッキング（お菓子編）\x01",
            "※１階の本棚に入っております。\x01",
            "  興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CD56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CE64")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0592
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　図書館ニュース　～\x01",
            "  皆様のリクエストに応え、\x01",
            "  以下書籍を追加しました。\x01",
            "  ・闇医者グレン５巻\x01",
            "  ・闇医者グレン６巻\x01",
            "  ・闇医者グレン７巻\x01",
            "  ・闇医者グレン８巻\x01",
            "※１階の本棚に入っております。\x01",
            "  興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_CF6D")

    label("loc_CE64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CF6D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0593
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　～　図書館ニュース　～\x01",
            "  皆様のリクエストに応え、\x01",
            "  以下書籍を追加しました。\x01",
            "  ・闇医者グレン１巻\x01",
            "  ・闇医者グレン２巻\x01",
            "  ・闇医者グレン３巻\x01",
            "  ・闇医者グレン４巻\x01",
            "※１階の本棚に入っております。\x01",
            "  興味のある方は是非どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_CF6D")

    EventEnd(0x3)
    Return()

    # Function_35_CA7A end

    def Function_36_CF70(): pass

    label("Function_36_CF70")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0594
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『マルクと深き森の魔女』がある。\x02",
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
            "【上巻を読む】\x01",      # 0
            "【中巻を読む】\x01",      # 1
            "【下巻を読む】\x01",      # 2
            "【やめる】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D01B")
    UseItem(0x2D6, 0xFF)

    label("loc_D01B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02F")
    UseItem(0x2DD, 0xFF)

    label("loc_D02F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D043")
    UseItem(0x2DE, 0xFF)

    label("loc_D043")

    TalkEnd(0xFF)
    Return()

    # Function_36_CF70 end

    def Function_37_D047(): pass

    label("Function_37_D047")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0595
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『大陸を動かした美人たち』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0CA")
    UseItem(0x2D7, 0xFF)

    label("loc_D0CA")

    TalkEnd(0xFF)
    Return()

    # Function_37_D047 end

    def Function_38_D0CE(): pass

    label("Function_38_D0CE")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『余った五分の有効な使い方』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D153")
    UseItem(0x2D8, 0xFF)

    label("loc_D153")

    TalkEnd(0xFF)
    Return()

    # Function_38_D0CE end

    def Function_39_D157(): pass

    label("Function_39_D157")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『鉄道マニアのススメ』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D6")
    UseItem(0x2D5, 0xFF)

    label("loc_D1D6")

    TalkEnd(0xFF)
    Return()

    # Function_39_D157 end

    def Function_40_D1DA(): pass

    label("Function_40_D1DA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0598
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『クロスベル怪奇全集』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D259")
    UseItem(0x2D9, 0xFF)

    label("loc_D259")

    TalkEnd(0xFF)
    Return()

    # Function_40_D1DA end

    def Function_41_D25D(): pass

    label("Function_41_D25D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『聖女と白い狼』がある。\x02",
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
            "【上巻を読む】\x01",      # 0
            "【下巻を読む】\x01",      # 1
            "【やめる】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2F1")
    UseItem(0x2DF, 0xFF)

    label("loc_D2F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D305")
    UseItem(0x2E0, 0xFF)

    label("loc_D305")

    TalkEnd(0xFF)
    Return()

    # Function_41_D25D end

    def Function_42_D309(): pass

    label("Function_42_D309")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0600
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『アルカンシェル・ファンブック』がある。\x02",
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
            "【本を読む】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D392")
    UseItem(0x2DA, 0xFF)

    label("loc_D392")

    TalkEnd(0xFF)
    Return()

    # Function_42_D309 end

    def Function_43_D396(): pass

    label("Function_43_D396")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D781")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "Ａ～Ｚ")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ＩＢＣ】\x01",      # 0
            "【ＺＣＦ】\x01",      # 1
            "【やめる】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5B4")
    SetChrName("")
    MenuTitle(-1, 25, 0, "ＩＢＣ（International Bank of Crossbell）")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0601
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《クロスベル国際銀行》の略称。\x01",
            "大陸全土から集まってくる莫大な資産を\x01",
            "管理・運用する巨大銀行で、\x01",
            "クロスベルのみならず、国際的な金融・\x01",
            "経済市場を長年に渡って支えてきた。\x02\x03",

            "投資活動や金融商品の開発のみならず、\x01",
            "テーマパークの運営なども手がけており、\x01",
            "エプスタイン財団の《導力ネットワーク計画》にも\x01",
            "積極的な資金提供を行っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D5B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77C")
    MenuTitle(-1, 25, 0, "ＺＣＦ（Zeiss Central Factory）")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0602
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《ツァイス中央工房》の略称。\x01",
            "リベール王国のツァイス市に拠点を構え、\x01",
            "オーブメントの発明者、エプスタイン博士の\x01",
            "直弟子であるＡ・ラッセル博士によって、\x01",
            "ツァイス時計師組合と協同で設立された\x01",
            "「ツァイス技術工房」を前身とする。\x02\x03",

            "世界に先駆けて導力飛行船の開発に\x01",
            "成功した大陸有数の導力器メーカーで、\x01",
            "近年ではリベール王国軍所属の\x01",
            "高速巡洋艦《アルセイユ》を完成させた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D77C")

    Jump("loc_D3AD")

    label("loc_D781")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_43_D396 end

    def Function_44_D78E(): pass

    label("Function_44_D78E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E059")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "ア行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【アルカンシェル】\x01",        # 0
            "【アルテリア法国】\x01",        # 1
            "【ヴェルヌ社】\x01",            # 2
            "【エレボニア帝国】\x01",        # 3
            "【エプスタイン財団】\x01",      # 4
            "【やめる】\x01",                # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D995")
    MenuTitle(-1, 25, 0, "アルカンシェル")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0603
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州に存在する\x01",
            "国際的にも有名な劇団。\x02\x03",

            "アクロバティックなパフォーマンスと\x01",
            "華麗かつ情熱的な舞台で\x01",
            "多くの観客を魅了し続けている。\x02\x03",

            "《炎の舞姫》の異名で知られる\x01",
            "現在の看板女優イリア・プラティエは\x01",
            "特に人気が高く、周辺諸国にも\x01",
            "熱狂的なファンが多い。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D995")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAFA")
    MenuTitle(-1, 25, 0, "アルテリア法国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0604
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀教会の総本山にあたる都市国家。\x01",
            "ゼムリア大陸の中心部に位置しており、\x01",
            "大陸全土から大勢の信徒や宗教関係者が\x01",
            "集まる聖地としても知られている。\x02\x03",

            "祭儀全般を監督する『典礼省』、\x01",
            "女神の秘蹟を管理するという『封聖省』、\x01",
            "都市の防衛を担当する『僧兵庁』など、\x01",
            "様々な組織が存在している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DAFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC87")
    MenuTitle(-1, 25, 0, "ヴェルヌ社")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0605
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カルバード共和国に本拠を置く\x01",
            "巨大総合技術メーカー。\x02\x03",

            "エレボニア帝国のラインフォルト社と\x01",
            "双璧をなす武器・兵器開発の老舗として有名だが、\x01",
            "オーブメントが発明されてからは、\x01",
            "あらゆる導力製品の研究・開発を行っている。\x02\x03",

            "中でも導力駆動車の分野においては、\x01",
            "導力バスを始め、自家用車から特殊車両に至るまで\x01",
            "様々な製品を開発している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEB7")
    MenuTitle(-1, 25, 0, "エレボニア帝国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0606
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州の西に位置する、\x01",
            "《黄金の軍馬》の紋章を掲げる巨大帝国。\x01",
            "現皇帝はユーゲント・ライゼ・アルノール。\x02\x03",

            "大貴族の支配する旧い体制の国家だが、\x01",
            "《鉄血宰相》の異名で知られる軍部出身の\x01",
            "ギリアス・オズボーン宰相の指揮の下、\x01",
            "全土に鉄道が敷かれ、近代化されつつある。\x02\x03",

            "機甲化された正規軍の他、大貴族の私設軍など\x01",
            "巨大な軍事力を保持しており、\x01",
            "周辺諸国に常に緊張を強いている。\x02\x03",

            "なお、昨年リベールで起きた異変の解決に\x01",
            "皇帝の子息、オリヴァルト皇子が協力。\x01",
            "帝国内で大きな話題となった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DEB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E054")
    MenuTitle(-1, 25, 0, "エプスタイン財団")
    SetMessageWindowPos(-1, 70, -1, -1)

    #A0607
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを発明した天才導力学者、\x01",
            "Ｃ・エプスタイン博士の業績を受け継いだ財団。\x01",
            "研究機関、メーカーとしての側面も強く、\x01",
            "通信・情報処理などの分野に特に優れている。\x02\x03",

            "魔法#4Rアーツ#を発動できる《戦術オーブメント》を\x01",
            "開発している唯一のメーカーである他、\x01",
            "近年では通信・情報処理技術を発展させた\x01",
            "《導力ネットワーク計画》に力を入れている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E054")

    Jump("loc_D7A5")

    label("loc_E059")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_44_D78E end

    def Function_45_E066(): pass

    label("Function_45_E066")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E07D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8FD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "カ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【怪盗Ｂ】\x01",                          # 0
            "【カルバード共和国】\x01",                # 1
            "【クロスベル自治州】\x01",                # 2
            "【結晶回路／クオーツ】\x01",              # 3
            "【古代遺物／アーティファクト】\x01",      # 4
            "【やめる】\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E320")
    MenuTitle(-1, 25, 0, "怪盗Ｂ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0608
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大陸を叉に掛ける神出鬼没の大泥棒。\x01",
            "宝石から、果ては導力戦車に至るまで、\x01",
            "国・個人を問わず、数多の盗みを働き、\x01",
            "その鮮やかで華麗な手口から、一部では熱狂的な\x01",
            "ファンまで存在するほど評判となっている。\x02\x03",

            "趣向に富んだメッセージを各所に送りつけ、\x01",
            "仮面と白マントを纏って姿を晒すこともあるが、\x01",
            "その正体は謎に包まれている。\x01",
            "近年では、本人自ら「美の解放活動」を語り、\x01",
            "エレボニア帝国で実行された、不可解ながらも\x01",
            "華麗な一連の犯行が話題に新しい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E487")
    MenuTitle(-1, 25, 0, "カルバード共和国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0609
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "百年ほど前に民主化を成し遂げた\x01",
            "クロスベル自治州の東に位置する共和国。\x01",
            "現元首はロックスミス大統領。\x02\x03",

            "広大な国土を持ち、\x01",
            "東方からの移民を受け入れてきたため\x01",
            "多様な文化背景を持つ。\x02\x03",

            "《不戦条約》締結後は沈静化を\x01",
            "見せているが、歴史上エレボニア帝国と\x01",
            "幾度となく衝突を繰り返してきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E609")
    MenuTitle(-1, 25, 0, "クロスベル自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0610
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸西部にある自治州。\x01",
            "エレボニア帝国、カルバード共和国という\x01",
            "２大国に挟まれており、\x01",
            "熾烈な領土争いの対象となってきたが、\x01",
            "７０年前に自治州として成立した。\x02\x03",

            "現在、中心のクロスベル市は大陸有数の\x01",
            "巨大貿易都市に成長を遂げており、\x01",
            "帝国～共和国を結ぶ大陸横断鉄道や\x01",
            "国際定期飛行船の中継点となっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E609")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E716")
    MenuTitle(-1, 25, 0, "結晶回路／クオーツ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0611
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀石の欠片《セピス》を精製・加工した\x01",
            "結晶構造を持つ回路。\x02\x03",

            "エネルギー源であると同時に、\x01",
            "様々な現象を起こすデバイスでもあるが、\x01",
            "オーブメントの内部にセットされないと\x01",
            "効果を発揮しない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F8")
    MenuTitle(-1, 25, 0, "古代遺物／アーティファクト")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0612
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントと同じ導力で稼動しながらも\x01",
            "異なる作動原理を持つ、古代文明の導力器。\x02\x03",

            "《古代ゼムリア文明》の時代に\x01",
            "生み出されたと言われ、現代の技術では\x01",
            "解析は不可能とされている。\x02\x03",

            "大陸各地の遺跡から稀に発見されることがあり、\x01",
            "今なお人智を超えた強大な力を\x01",
            "発揮するものも少なくない。\x02\x03",

            "そのため七耀教会ではアーティファクトを\x01",
            "『早すぎた女神の贈り物』と定義し、\x01",
            "その回収・管理を責務としているという。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E8F8")

    Jump("loc_E07D")

    label("loc_E8FD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_45_E066 end

    def Function_46_E90A(): pass

    label("Function_46_E90A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E921")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC19")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "サ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【七耀教会】\x01",                # 0
            "【七耀石／セプチウム】\x01",      # 1
            "【やめる】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAC5")
    MenuTitle(-1, 25, 0, "七耀教会")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸で最も広く信仰されている\x01",
            "《空の女神エイドス》を奉じる宗教組織。\x01",
            "アルテリア法国に総本山を持つ。\x02\x03",

            "導力革命以降、影響力は低下したものの\x01",
            "今なお大陸全土に強い影響力を持ち、\x01",
            "学問・教育・医療などの分野を通して、\x01",
            "民衆を啓蒙する立場にある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EAC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC14")
    MenuTitle(-1, 25, 0, "七耀石／セプチウム")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0614
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大陸全般に分布する７種類の貴石群。\x01",
            "古くから宝石として、\x01",
            "神秘の象徴として珍重されてきた。\x02\x03",

            "近代になって、宝石にするには小さすぎる\x01",
            "欠片《セピス》を精製・加工して\x01",
            "クオーツを作る技術が発明された事により、\x01",
            "七耀石資源の重要性は\x01",
            "大陸諸国間で一気に高まった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC14")

    Jump("loc_E921")

    label("loc_EC19")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_46_E90A end

    def Function_47_EC26(): pass

    label("Function_47_EC26")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3B0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "タ行・上")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【大崩壊】\x01",                    # 0
            "【釣公師団】\x01",                  # 1
            "【導力革命】\x01",                  # 2
            "【導力器／オーブメント】\x01",      # 3
            "【やめる】\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC3")
    MenuTitle(-1, 25, 0, "大崩壊")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0615
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "約１２００年前に起こったとされる、\x01",
            "古代ゼムリア文明の崩壊のこと。\x01",
            "天変地異が原因とも言われているが詳細は不明。\x02\x03",

            "《大崩壊》によって文明が失われた後、\x01",
            "人々は長きに渡る《暗黒時代》を辿った。\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EDC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF4D")
    MenuTitle(-1, 25, 0, "釣公師団")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0616
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣り文化の普及を目的に活動している、\x01",
            "釣りのプロフェッショナル集団。\x01",
            "元貴族の釣り愛好家、\x01",
            "Ｈ・フィッシャー氏によって発足され、\x01",
            "リベール王国のグランセル市に本部を構える。\x02\x03",

            "釣り場の探訪・調査・開拓にはじまり、\x01",
            "新世代の釣師の発掘や教育、さらに近年では\x01",
            "釣り道具・釣りエサの開発にも携わるなど、\x01",
            "年々その活動の幅を広げている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1D7")
    MenuTitle(-1, 25, 0, "導力革命")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0617
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "およそ５０年ほど前、\x01",
            "オーブメントが発明されることで起きた\x01",
            "大陸規模での技術革新のこと。\x02\x03",

            "画期的な発明であるにも関わらず\x01",
            "当時の人々は懐疑的だったが、\x01",
            "エプスタイン財団の導力通信器や\x01",
            "ＺＣＦの導力飛行船が世に出るにつれ、\x01",
            "その有用性は大陸全土に認知されていった。\x02\x03",

            "現在では暖房や照明などの日用品から\x01",
            "鉄道や飛行船、戦車や大砲などの兵器まで\x01",
            "ありとあらゆるものが導力化され、\x01",
            "もはやオーブメントは人々にとって\x01",
            "なくてはならないものとなっている。\x02\x03",

            "なお近年、導力機関の小型化に伴い、\x01",
            "ヴェルヌ社やラインフォルト社によって\x01",
            "高性能な導力駆動車の開発が進んでおり、\x01",
            "一般層への普及も始まっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F1D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3AB")
    MenuTitle(-1, 25, 0, "導力器／オーブメント")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0618
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ｃ・エプスタイン博士によって\x01",
            "発明された、七耀石から導力を引き出し、\x01",
            "様々な現象を引き起こす機械の総称。\x02\x03",

            "オーブメント内の構造・歯車の動きで、\x01",
            "七耀石を加工した結晶回路を相互干渉せることで\x01",
            "無数のバリエーションの現象を発現させる。\x02\x03",

            "オーブメントの有用性は、バリエーションの\x01",
            "豊富さに加えて、『時間が経てば内部の\x01",
            "導力が回復する』ことにあり、外燃・内燃機関と\x01",
            "較べると経済効率が遙かに高い。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3AB")

    Jump("loc_EC3D")

    label("loc_F3B0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_47_EC26 end

    def Function_48_F3BD(): pass

    label("Function_48_F3BD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F84F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "タ行・下")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【導力魔法／オーバルアーツ】\x01",      # 0
            "【導力ネットワーク計画】\x01",          # 1
            "【東方人街】\x01",                      # 2
            "【やめる】\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5A5")
    MenuTitle(-1, 25, 0, "導力魔法／オーバルアーツ")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0619
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エプスタイン財団によって特別に設計された\x01",
            "《戦術オーブメント》に結晶回路#8Rク オ ー ツ#を組み込むことで\x01",
            "発動することができる“魔法”。\x02\x03",

            "一般的には“アーツ”と呼ばれ、\x01",
            "訓練次第で誰もが使える技術として\x01",
            "軍隊・警察・ギルドなどに普及している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F712")
    MenuTitle(-1, 25, 0, "導力ネットワーク計画")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0620
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エプスタイン財団が研究開発を進めている\x01",
            "革新的な情報ネットワーク計画。\x01",
            "端末同士を導力ケーブルで結び、\x01",
            "莫大な情報のやり取りと処理を可能にしている。\x02\x03",

            "元々はリベールのＺＣＦと共同で開発が\x01",
            "進められていたが、現在はＩＢＣの\x01",
            "資金提供を受け、クロスベル市への\x01",
            "本格的な試験導入が始まった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F84A")
    MenuTitle(-1, 25, 0, "東方人街")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0621
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カルバード共和国に存在する、\x01",
            "東方系移民が築き上げた大規模な街。\x01",
            "様々な文化、人々、物資が行き交い、\x01",
            "“東西文化の交差点”と呼ばれている。\x02\x03",

            "エキゾチックな建物が建ち並ぶ\x01",
            "観光地としても有名だが、東方系の\x01",
            "巨大シンジケートの存在も囁かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F84A")

    Jump("loc_F3D4")

    label("loc_F84F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_48_F3BD end

    def Function_49_F85C(): pass

    label("Function_49_F85C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F873")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCFD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "ナ・ハ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【百日戦役】\x01",      # 0
            "【不戦条約】\x01",      # 1
            "【やめる】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB28")
    MenuTitle(-1, 25, 0, "百日戦役")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0622
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀暦１１９２年、エレボニア帝国・\x01",
            "リベール王国間で起きた侵略戦争。\x01",
            "帝国による宣戦布告から、七耀教会の\x01",
            "仲立ちで実現した戦争終結まで、\x01",
            "およそ百日で決着をみたことから\x01",
            "こう呼ばれる。\x02\x03",

            "当初リベールは劣勢を強いられ、\x01",
            "国土の大半を帝国軍に占領されたが、\x01",
            "当時の最先端を誇る警備飛行艇を\x01",
            "用いた電撃的な反攻作戦によって\x01",
            "瞬く間にその戦況を覆した。\x02\x03",

            "そもそもの開戦理由については、\x01",
            "両国とも沈黙を保ったため\x01",
            "結局明かされることはなかったが、\x01",
            "後に「不幸な誤解から生じた過ち」\x01",
            "という表現で、帝国政府からリベールに\x01",
            "正式な謝罪声明が出された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCF8")
    MenuTitle(-1, 25, 0, "不戦条約")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0623
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "七耀暦１２０２年、リベール王国・\x01",
            "エレボニア帝国・カルバード共和国の\x01",
            "３国間で締結された国際条約。\x01",
            "リベールのアリシア女王により提唱され、\x01",
            "同国のエルベ離宮にて調印式が執り行われた。\x02\x03",

            "本条約には法的な強制力はないが、\x01",
            "条約締結後は、クロスベル自治州近郊で\x01",
            "展開されていた帝国・共和国それぞれによる\x01",
            "大規模な軍事演習が撤収されるなど、\x01",
            "緊張状態が大幅に緩和しており、\x01",
            "確実に効果が現れていると言える。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FCF8")

    Jump("loc_F873")

    label("loc_FCFD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_49_F85C end

    def Function_50_FD0A(): pass

    label("Function_50_FD0A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10107")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "マ・ヤ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ミシュラム】\x01",                        # 0
            "【遊撃士協会／ブレイサーギルド】\x01",      # 1
            "【やめる】\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEC7")
    MenuTitle(-1, 25, 0, "ミシュラム")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0624
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エルム湖南東に位置する高級保養地。\x01",
            "２年前、ＩＢＣが開発に着手してからは\x01",
            "リゾートホテルやテーマパークなどが\x01",
            "建ち並ぶ人気スポットとなった。\x02\x03",

            "《みっしぃ》と呼ばれる\x01",
            "ご当地マスコットキャラクターも\x01",
            "市民や観光客から人気を集めている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FEC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10102")
    MenuTitle(-1, 25, 0, "遊撃士協会／ブレイサーギルド")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0625
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "地域の平和と民間人の保護のために働く\x01",
            "遊撃士#6Rブレイサー#たちの民間団体。\x01",
            "ゼムリア大陸各地に支部があるため、\x01",
            "少なからぬ影響力・発言力を持っている。\x02\x03",

            "何よりも民間人の安全を優先して\x01",
            "行動する理念は理想的とも言えるが、\x01",
            "逆に民間人の安全が脅かされない限り、\x01",
            "国家・公的権力に対して捜査権・逮捕権を\x01",
            "行使できないという組織規約上の弱点もある。\x02\x03",

            "ここクロスベルにおいては、\x01",
            "国際的な案件を多く抱えることから\x01",
            "《風の剣聖》アリオス・マクレインを始め\x01",
            "優秀な人材が集まり、市民の支持を得ている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10102")

    Jump("loc_FD21")

    label("loc_10107")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_50_FD0A end

    def Function_51_10114(): pass

    label("Function_51_10114")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1012B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1091E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuTitle(-1, 25, 0, "ラ行")
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【ラインフォルト社】\x01",        # 0
            "【レミフェリア公国】\x01",        # 1
            "【レマン自治州】\x01",            # 2
            "【リベール王国】\x01",            # 3
            "【猟兵団／イェーガー】\x01",      # 4
            "【やめる】\x01",                  # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_DD()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1035A")
    MenuTitle(-1, 25, 0, "ラインフォルト社")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0626
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレボニア帝国に本拠を置く\x01",
            "巨大総合技術メーカー。\x01",
            "元々は火薬を使った大砲・重火器の\x01",
            "製造を専門に行っていた兵器工房だった。\x02\x03",

            "オーブメントが発明されてからは、\x01",
            "導力銃・導力兵器のみならず、\x01",
            "導力鉄道や飛行船などの分野にも手を広げ、\x01",
            "カルバード共和国の《ヴェルヌ社》と並んで、\x01",
            "世界二大メーカーと称されるまでに成長した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1035A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104FB")
    MenuTitle(-1, 25, 0, "レミフェリア公国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0627
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸北部に位置する公国。\x01",
            "厳しい北国ではあるものの、\x01",
            "豊かな森と湖に恵まれており、\x01",
            "その風光明媚な景色に魅せられ、\x01",
            "観光目的で訪れる者も多い。\x02\x03",

            "また医療先進国としても有名で、\x01",
            "大陸を代表する医療機器メーカーが集中し、\x01",
            "多くの優秀な医師を輩出している。\x01",
            "クロスベル自治州の聖ウルスラ医科大学も\x01",
            "レミフェリア公国の協力によって設立された。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_104FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105EF")
    MenuTitle(-1, 25, 0, "レマン自治州")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0628
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸中部にある自治州。\x01",
            "エプスタイン財団の本部があり、\x01",
            "Ｃ・エプスタイン博士の故郷でもある。\x02\x03",

            "その他、大陸各地に支部を持つ\x01",
            "遊撃士協会の総本部がある事でも有名。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_105EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107F2")
    MenuTitle(-1, 25, 0, "リベール王国")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0629
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ゼムリア大陸南西部に位置する王国。\x01",
            "豊かな自然に彩られた伝統ある国家で、\x01",
            "現在は、老女王アリシアⅡ世の治世の下、\x01",
            "誇り高き平和を保っている。\x02\x03",

            "周辺諸国より国力では劣るが、\x01",
            "豊富な七耀石資源と優れた技術、\x01",
            "巧みな外交政策によって\x01",
            "対等な関係を築いてきた。\x02\x03",

            "昨年、王国中央にあるヴァレリア湖上に\x01",
            "謎の巨大構造物（詳細不明）が出現し、\x01",
            "王国全土の導力が停止するという異変が\x01",
            "起きたが、軍や遊撃士協会の働きにより\x01",
            "無事解決され、落ち着きを取り戻している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_107F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10919")
    MenuTitle(-1, 25, 0, "猟兵団／イェーガー")
    SetMessageWindowPos(-1, 70, -1, -1)
    SetChrName("")

    #A0630
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大陸諸国で活動する傭兵部隊の中でも\x01",
            "特に優秀な部隊を指して使われる称号。\x02\x03",

            "規模や目的に応じた柔軟な契約が行え、\x01",
            "高い戦闘力を期待できることから、\x01",
            "私兵として使われることが多く、\x01",
            "その運用を法律で禁じる国も存在する。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_DD()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10919")

    Jump("loc_1012B")

    label("loc_1091E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_51_10114 end

    def Function_52_1092B(): pass

    label("Function_52_1092B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0631
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『闇医者グレン』がある。\x02",
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
            "【13巻を読む】\x01",      # 0
            "【14巻を読む】\x01",      # 1
            "【やめる】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109BF")
    UseItem(0x2D2, 0xFF)

    label("loc_109BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109D3")
    UseItem(0x2D3, 0xFF)

    label("loc_109D3")

    TalkEnd(0xFF)
    Return()

    # Function_52_1092B end

    def Function_53_109D7(): pass

    label("Function_53_109D7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0632
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『闇医者グレン』がある。\x02",
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
            "【９巻を読む】\x01",      # 0
            "【10巻を読む】\x01",      # 1
            "【11巻を読む】\x01",      # 2
            "【12巻を読む】\x01",      # 3
            "【やめる】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A89")
    UseItem(0x2CE, 0xFF)

    label("loc_10A89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A9D")
    UseItem(0x2CF, 0xFF)

    label("loc_10A9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AB1")
    UseItem(0x2D0, 0xFF)

    label("loc_10AB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AC5")
    UseItem(0x2D1, 0xFF)

    label("loc_10AC5")

    TalkEnd(0xFF)
    Return()

    # Function_53_109D7 end

    def Function_54_10AC9(): pass

    label("Function_54_10AC9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0633
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『闇医者グレン』がある。\x02",
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
            "【５巻を読む】\x01",      # 0
            "【６巻を読む】\x01",      # 1
            "【７巻を読む】\x01",      # 2
            "【８巻を読む】\x01",      # 3
            "【やめる】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B7B")
    UseItem(0x2CA, 0xFF)

    label("loc_10B7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8F")
    UseItem(0x2CB, 0xFF)

    label("loc_10B8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BA3")
    UseItem(0x2CC, 0xFF)

    label("loc_10BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BB7")
    UseItem(0x2CD, 0xFF)

    label("loc_10BB7")

    TalkEnd(0xFF)
    Return()

    # Function_54_10AC9 end

    def Function_55_10BBB(): pass

    label("Function_55_10BBB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0634
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『闇医者グレン』がある。\x02",
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
            "【１巻を読む】\x01",      # 0
            "【２巻を読む】\x01",      # 1
            "【３巻を読む】\x01",      # 2
            "【４巻を読む】\x01",      # 3
            "【やめる】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C6D")
    UseItem(0x2C6, 0xFF)

    label("loc_10C6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C81")
    UseItem(0x2C7, 0xFF)

    label("loc_10C81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C95")
    UseItem(0x2C8, 0xFF)

    label("loc_10C95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CA9")
    UseItem(0x2C9, 0xFF)

    label("loc_10CA9")

    TalkEnd(0xFF)
    Return()

    # Function_55_10BBB end

    SaveToFile()

Try(main)
