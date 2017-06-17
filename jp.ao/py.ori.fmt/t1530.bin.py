from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1530.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1530",                  # 0
        "受付嬢セラ",             # 1
        "クラーク事務長",         # 2
        "看護師ラン",             # 3
        "ラゴー教授",             # 4
        "研修医リットン",         # 5
        "研修医グェン",           # 6
        "ゲイリー教授",           # 7
        "アーシュラ主任",         # 8
        "研修医シャルール",       # 9
        "外来患者",               # 10
        "外来患者",               # 11
        "外来患者",               # 12
        "外来患者",               # 13
        "外来患者",               # 14
        "外来患者",               # 15
        "外来患者",               # 16
        "外来患者",               # 17
        "患者",                   # 18
        "患者",                   # 19
        "患者",                   # 20
        "看護師エイダ",           # 21
        "セイランド教授",         # 22
        "警備員トニー",           # 23
        "クワイン老人",           # 24
        "アミサ",                 # 25
        "アリオス",               # 26
        "アルバート大公",         # 27
        "ビリー",                 # 28
        "患者",                   # 29
        "遊撃士エオリア",         # 30
        "セシル",                 # 31
        "女性",                   # 32
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28000.itc",                   # 01
        "chr/ch29700.itc",                   # 02
        "chr/ch29202.itc",                   # 03
        "chr/ch29200.itc",                   # 04
        "chr/ch29402.itc",                   # 05
        "chr/ch29400.itc",                   # 06
        "chr/ch29500.itc",                   # 07
        "chr/ch32702.itc",                   # 08
        "chr/ch32700.itc",                   # 09
        "chr/ch32900.itc",                   # 0A
        "chr/ch32800.itc",                   # 0B
        "chr/ch20002.itc",                   # 0C
        "chr/ch23302.itc",                   # 0D
        "chr/ch21002.itc",                   # 0E
        "chr/ch21000.itc",                   # 0F
        "chr/ch20302.itc",                   # 10
        "chr/ch20402.itc",                   # 11
        "chr/ch44202.itc",                   # 12
        "chr/ch23002.itc",                   # 13
        "chr/ch23000.itc",                   # 14
        "chr/ch24702.itc",                   # 15
        "apl/ch50132.itc",                   # 16
        "apl/ch50138.itc",                   # 17
        "apl/ch50140.itc",                   # 18
        "chr/ch29800.itc",                   # 19
        "chr/ch44800.itc",                   # 1A
        "chr/ch28600.itc",                   # 1B
        "chr/ch24000.itc",                   # 1C
        "chr/ch21502.itc",                   # 1D
        "chr/ch21500.itc",                   # 1E
        "chr/ch02400.itc",                   # 1F
        "chr/ch11800.itc",                   # 20
        "chr/ch20402.itc",                   # 21
        "apl/ch51277.itc",                   # 22
        "chr/ch23600.itc",                   # 23
        "chr/ch44802.itc",                   # 24
        "chr/ch32100.itc",                   # 25
        "apl/ch51278.itc",                   # 26
    ))

    DeclNpc(17209,   0,       7429,    266,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(19739,   0,       4889,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(10539,   0,       -4489,   325,  261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(50979,   119,     59069,   300,  261,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(53970,   0,       51840,   135,  261,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(58849,   0,       58389,   0,    261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(49930,   119,     -59340,  260,  261,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(56430,   0,       -55270,  90,   261,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(60270,   0,       -56930,  90,   261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   16,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   20,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   21,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(59209,   699,     59900,   0,    469,  0x0, 0,   22,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(59209,   699,     54900,   0,    469,  0x0, 0,   23,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(56889,   800,     -58500,  0,    469,  0x0, 0,   24,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   25,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   27,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   28,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   30,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   31,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   32,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   35,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   38,  0,   255, 255, 0,   42,  255,  0)
    DeclNpc(22510,   0,       1299,    225,  389,  0x0, 0,   37,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(16000,   0,       7000,    2000,    17210,   1500,    7430,    0x007E, 0,  6,  0x0000)
    DeclActor(19680,   0,       3710,    2000,    19740,   1500,    4890,    0x007E, 0,  8,  0x0000)
    DeclActor(65800,   0,       2430,    1200,    65800,   1500,    2430,    0x007C, 0,  54, 0x0000)

    ChipFrameInfo(1540, 0)                                       # 0

    ScpFunction((
        "Function_0_604",          # 00, 0
        "Function_1_6B4",          # 01, 1
        "Function_2_765",          # 02, 2
        "Function_3_790",          # 03, 3
        "Function_4_7BB",          # 04, 4
        "Function_5_1398",         # 05, 5
        "Function_6_1474",         # 06, 6
        "Function_7_1478",         # 07, 7
        "Function_8_2878",         # 08, 8
        "Function_9_287C",         # 09, 9
        "Function_10_3D4C",        # 0A, 10
        "Function_11_4A79",        # 0B, 11
        "Function_12_582C",        # 0C, 12
        "Function_13_5F0B",        # 0D, 13
        "Function_14_6725",        # 0E, 14
        "Function_15_7176",        # 0F, 15
        "Function_16_7BF7",        # 10, 16
        "Function_17_7D07",        # 11, 17
        "Function_18_8B42",        # 12, 18
        "Function_19_8CDB",        # 13, 19
        "Function_20_9A71",        # 14, 20
        "Function_21_9DF7",        # 15, 21
        "Function_22_A14C",        # 16, 22
        "Function_23_A599",        # 17, 23
        "Function_24_A958",        # 18, 24
        "Function_25_A9F1",        # 19, 25
        "Function_26_AC1A",        # 1A, 26
        "Function_27_AF35",        # 1B, 27
        "Function_28_B0A5",        # 1C, 28
        "Function_29_B1E8",        # 1D, 29
        "Function_30_B269",        # 1E, 30
        "Function_31_B2B6",        # 1F, 31
        "Function_32_B328",        # 20, 32
        "Function_33_B3A4",        # 21, 33
        "Function_34_BDA2",        # 22, 34
        "Function_35_BE5B",        # 23, 35
        "Function_36_BF64",        # 24, 36
        "Function_37_BFFD",        # 25, 37
        "Function_38_C1DC",        # 26, 38
        "Function_39_C2CD",        # 27, 39
        "Function_40_C369",        # 28, 40
        "Function_41_C39F",        # 29, 41
        "Function_42_C442",        # 2A, 42
        "Function_43_C62A",        # 2B, 43
        "Function_44_C631",        # 2C, 44
        "Function_45_C910",        # 2D, 45
        "Function_46_C917",        # 2E, 46
        "Function_47_CBE8",        # 2F, 47
        "Function_48_D3A9",        # 30, 48
        "Function_49_F7AC",        # 31, 49
        "Function_50_1048E",       # 32, 50
        "Function_51_10870",       # 33, 51
        "Function_52_10871",       # 34, 52
        "Function_53_10DDE",       # 35, 53
        "Function_54_112F3",       # 36, 54
        "Function_55_1139C",       # 37, 55
        "Function_56_113F1",       # 38, 56
        "Function_57_11446",       # 39, 57
    ))


    def Function_0_604(): pass

    label("Function_0_604")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_63C"),
        (1, "loc_648"),
        (2, "loc_654"),
        (3, "loc_660"),
        (4, "loc_66C"),
        (5, "loc_678"),
        (6, "loc_684"),
        (SWITCH_DEFAULT, "loc_690"),
    )


    label("loc_63C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_648")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_654")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_660")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_66C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_678")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_684")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_690")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_69C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_6B3")

    Return()

    # Function_0_604 end

    def Function_1_6B4(): pass

    label("Function_1_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_764")
    OP_95(0xFE, 7400, 0, -1600, 1500, 0x0)
    OP_95(0xFE, 7400, 0, 1420, 1500, 0x0)
    OP_95(0xFE, 10380, 0, 4530, 1500, 0x0)
    OP_95(0xFE, 13330, 0, 4550, 1500, 0x0)
    OP_95(0xFE, 16420, 0, 1470, 1500, 0x0)
    OP_95(0xFE, 16420, 0, -1430, 1500, 0x0)
    OP_95(0xFE, 13440, 0, -4490, 1500, 0x0)
    OP_95(0xFE, 10540, 0, -4490, 1500, 0x0)
    Jump("Function_1_6B4")

    label("loc_764")

    Return()

    # Function_1_6B4 end

    def Function_2_765(): pass

    label("Function_2_765")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78F")
    OP_94(0xFE, 0x1932, 0x148C, 0x1DBA, 0xDCA, 0x3E8)
    Sleep(400)
    Jump("Function_2_765")

    label("loc_78F")

    Return()

    # Function_2_765 end

    def Function_3_790(): pass

    label("Function_3_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BA")
    OP_94(0xFE, 0x4556, 0xFFFFF1F0, 0x3E4E, 0xFFFFE926, 0x3E8)
    Sleep(400)
    Jump("Function_3_790")

    label("loc_7BA")

    Return()

    # Function_3_790 end

    def Function_4_7BB(): pass

    label("Function_4_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_958")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_7FA")

    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 21840, 120, -7220, 270)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 21840, 120, -8200, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 16800, 120, -6890, 0)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 16950, 0, -5000, 0)
    BeginChrThread(0x17, 0, 0, 3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 7680, 120, 6840, 180)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 6680, 120, 6840, 180)
    SetChrChipByIndex(0x18, 0x15)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2000, 120, 4140, 90)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 7750, 120, 9800, 180)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_132F")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9AA")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xC, 50900, 0, 57650, 270)
    SetChrPos(0xD, 49700, 0, 57650, 90)
    Jump("loc_132F")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A04")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E9")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_9E9")

    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 51850, 0, 58000, 90)
    Jump("loc_132F")

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A39")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xC, 0x80)
    Jump("loc_132F")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BDF")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 16800, 120, -6890, 0)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 21840, 120, -4430, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5100, 120, 4740, 90)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 7400, 0, 3740, 270)
    BeginChrThread(0x17, 0, 0, 2)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2000, 120, 7880, 90)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB1")
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6A")
    SetChrFlags(0x1E, 0x10)

    label("loc_B6A")

    SetChrPos(0x1E, 55400, 0, 1000, 135)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 56600, 0, 0, 270)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0x9, 55400, 0, -1000, 45)
    SetChrFlags(0x9, 0x10)
    Jump("loc_BDA")

    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDA")
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 65800, 0, 1700, 180)

    label("loc_BDA")

    Jump("loc_132F")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D09")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 55650, 0, 500, 180)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0xC, 55650, 0, -620, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 8160, 0, 400, 180)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0xA, 8160, 0, -630, 0)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 2000, 120, 4140, 90)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 18850, 120, -4310, 270)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 18850, 120, -5220, 270)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 7520, 120, 6840, 180)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_132F")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DC9")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x10, 56280, 0, -56460, 45)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7400, 120, 6850, 180)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 19660, 120, -9970, 0)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 16560, 120, -9980, 0)
    SetChrChipByIndex(0x18, 0x15)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_132F")

    label("loc_DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F19")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E08")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_E08")

    SetChrPos(0xC, 50980, 120, 59070, 300)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 49270, 0, 59090, 90)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 49900, 0, 58070, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E73")
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)

    label("loc_E73")

    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 18910, 120, -5350, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 2000, 120, 7510, 90)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 7750, 120, 9800, 180)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 16810, 120, -6920, 0)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_132F")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_101A")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F67")
    SetChrFlags(0x10, 0x10)

    label("loc_F67")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 16800, 120, -9960, 0)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 8340, 120, 9890, 180)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x14, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 7550, 120, 9800, 180)
    SetChrChipByIndex(0x18, 0x15)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x10)
    SetChrSubChip(0x18, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 21840, 120, -4430, 270)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jump("loc_132F")

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_121C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xE, 59270, 0, -57930, 90)
    SetChrPos(0x10, 60270, 0, -57930, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1068")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_1068")

    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5100, 120, 4740, 90)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 9940, 0, 1990, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")
    SetChrFlags(0x13, 0x10)

    label("loc_10B4")

    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 21840, 120, -7320, 270)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x10)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 21840, 120, -8100, 270)
    SetChrChipByIndex(0x17, 0x13)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_1217")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A9")
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 48860, 0, 59410, 90)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 49210, 0, 57900, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 18850, 120, -3970, 270)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    Jump("loc_1217")

    label("loc_11A9")

    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 56950, 0, 60000, 90)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 270)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)

    label("loc_1217")

    Jump("loc_132F")

    label("loc_121C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_132F")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 16050, 100, -6990, 0)
    SetChrChipByIndex(0x20, 0x1D)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrPos(0xC, 16050, 0, -5480, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_1293")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4090, 120, 9890, 180)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 19730, 120, -9960, 0)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 5110, 120, 5170, 90)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5110, 120, 4330, 90)
    SetChrChipByIndex(0x17, 0x13)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)

    label("loc_132F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1348")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 47)
    Jump("loc_137F")

    label("loc_1348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_135C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 52)
    Jump("loc_137F")

    label("loc_135C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1370")
    ClearScenarioFlags(0x22, 2)
    Event(0, 53)
    Jump("loc_137F")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_137F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 49)

    label("loc_137F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1397")
    ClearScenarioFlags(0x25, 1)
    Call(0, 45)

    label("loc_1397")

    Return()

    # Function_4_7BB end

    def Function_5_1398(): pass

    label("Function_5_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_13AA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13AA")

    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_13E2")
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_140C")
    OP_65(0x1, 0x1)

    label("loc_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1448")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1460")
    OP_1B(0x2, 0x0, 0x37)
    OP_1B(0x1, 0x0, 0x38)

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1473")
    OP_1B(0x0, 0x0, 0x39)

    label("loc_1473")

    Return()

    # Function_5_1398 end

    def Function_6_1474(): pass

    label("Function_6_1474")

    Call(0, 7)
    Return()

    # Function_6_1474 end

    def Function_7_1478(): pass

    label("Function_7_1478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148A")
    Call(0, 46)
    Return()

    label("loc_148A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B3")
    Call(0, 50)
    Return()

    label("loc_14B3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158E")

    #C0001
    ChrTalk(
        0x8,
        (
            "ストップしていた外来も、\x01",
            "ようやく再開できることになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "しばらく忙しくなりそうですが、\x01",
            "本当に安心しました……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "これも皆さんのおかげですね。\x01",
            "本当にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_162B")

    label("loc_158E")


    #C0004
    ChrTalk(
        0x8,
        (
            "ストップしていた外来も、\x01",
            "ようやく再開できることになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "しばらく忙しくなりそうですが、\x01",
            "病院職員として懇切丁寧な\x01",
            "対応を心がけたいところです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162B")

    Jump("loc_2874")

    label("loc_1630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_177B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FA")

    #C0006
    ChrTalk(
        0x8,
        (
            "噂によると、件の無効宣言を受けて\x01",
            "市内の一部で暴動のようなものも\x01",
            "起こってしまったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "国防軍が早々に鎮圧したそうですが……\x01",
            "怪我人などが出ていないか心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1776")

    label("loc_16FA")


    #C0008
    ChrTalk(
        0x8,
        (
            "件の無効宣言を受けて\x01",
            "市内の一部で暴動のようなものも\x01",
            "起こってしまったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "怪我人が出ていないか心配ですね……\x02",
    )

    CloseMessageWindow()

    label("loc_1776")

    Jump("loc_2874")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_18D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")

    #C0010
    ChrTalk(
        0x8,
        (
            "以前、通院していた患者さんに\x01",
            "処方された薬が行き届くよう、\x01",
            "国防軍と交渉しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ですが、あまりに数が多くて……\x01",
            "なかなか手配が出来ない状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "……ままなりませんね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CB")

    label("loc_184F")


    #C0013
    ChrTalk(
        0x8,
        (
            "外来受付がストップしている以上、\x01",
            "薬だけでも市内の患者さんに\x01",
            "届けて差し上げたいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "……ままなりませんね。\x02",
    )

    CloseMessageWindow()

    label("loc_18CB")

    Jump("loc_2874")

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A00")

    #C0015
    ChrTalk(
        0x8,
        (
            "病院では《幻獣》の発生の影響で\x01",
            "外来の受付をストップしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "現在は、重病・重傷患者のみが\x01",
            "国防軍の護衛がついた救急車で\x01",
            "搬送されて来ている状態で……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "こんな体制は、伝統ある\x01",
            "ウルスラ病院の意義に反します。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……なにより、\x01",
            "市内の患者さんがとても心配です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA1")

    label("loc_1A00")


    #C0019
    ChrTalk(
        0x8,
        (
            "病院では《幻獣》の発生の影響で\x01",
            "外来の受付をストップしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "重病・重傷しか治療して\x01",
            "差し上げられないなんて……\x01",
            "市内の患者さんがとても心配です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA1")

    Jump("loc_2874")

    label("loc_1AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DBA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B73")

    #C0021
    ChrTalk(
        0x8,
        (
            "医療物資が届いて\x01",
            "本当によかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "僭越ながら、病院を代表して\x01",
            "お礼を言わせて頂きますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "みなさん、本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDD")

    label("loc_1B73")


    #C0024
    ChrTalk(
        0x8,
        (
            "僭越ながら、病院を代表して\x01",
            "お礼を言わせて頂きますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "みなさん、本当に\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    Jump("loc_1DB5")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1C8A")

    #C0026
    ChrTalk(
        0x8,
        (
            "レミフェリア方面に事情を説明して、\x01",
            "改めて医療物資を送ってもらうよう\x01",
            "手配しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "多少遅れてしまいますが……\x01",
            "済んだ事は仕方ありませんよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB5")

    label("loc_1C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D41")

    #C0028
    ChrTalk(
        0x8,
        (
            "先ほど、警備のトニーさんが\x01",
            "事務長に何か報告していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "今は診察室前で、\x01",
            "セイランド教授と３人で\x01",
            "相談しているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "何かあったのでしょうか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB5")

    label("loc_1D41")


    #C0031
    ChrTalk(
        0x8,
        (
            "警備のトニーさんと事務長が、\x01",
            "診察室前でセイランド教授と\x01",
            "相談しているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "何かあったのでしょうか。\x02",
    )

    CloseMessageWindow()

    label("loc_1DB5")

    Jump("loc_1ED0")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6A")

    #C0033
    ChrTalk(
        0x8,
        (
            "フランさんの病室は\x01",
            "３階の３０１号室です。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "大分安定してきましたが、\x01",
            "まだ体力が戻っていない\x01",
            "ようですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "どうか元気づけて\x01",
            "差し上げてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ED0")

    label("loc_1E6A")


    #C0036
    ChrTalk(
        0x8,
        (
            "フランさんは、つい先日\x01",
            "意識が戻られたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "大変な怪我でしたが……\x01",
            "本当に良かったですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED0")

    Jump("loc_2874")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200C")

    #C0038
    ChrTalk(
        0x8,
        (
            "昨日の列車事故で、\x01",
            "外国人を含む多数の患者が\x01",
            "運び込まれてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ウルスラ病院は外国人の\x01",
            "受け入れ態勢が整っているので、\x01",
            "スムーズに対応できたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "医療がまだ発達していない\x01",
            "他国で事故が起こっていたら\x01",
            "どうなっていたでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "考えるとゾッとしてしまいますね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20B4")

    label("loc_200C")


    #C0042
    ChrTalk(
        0x8,
        (
            "医療がまだ発達していない\x01",
            "他国で事故が起こっていたら\x01",
            "どうなっていたことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "ほとんどは軽傷で済みましたし、\x01",
            "そういう意味では\x01",
            "運が良かったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B4")

    Jump("loc_2874")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_229A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2188")

    #C0044
    ChrTalk(
        0x8,
        "あの荷物は誤配だったんですね。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "看護師の１人が\x01",
            "発注ミスをしたのではと\x01",
            "マーサ師長が騒いでいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "とにかく、\x01",
            "一旦２階を訪ねてみてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F9")

    label("loc_2188")


    #C0047
    ChrTalk(
        0x8,
        (
            "無事に荷物を\x01",
            "受け取られたようですね。\x01",
            "ふふ、よかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "皆さん、どうかお気をつけて\x01",
            "お帰り下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F9")

    Jump("loc_2295")

    label("loc_21FE")


    #C0049
    ChrTalk(
        0x8,
        (
            "ウルスラ病院へようこそ。\x01",
            "外来・お見舞いの受付はこちらです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "再診の方は導力ネットでの\x01",
            "ご予約も受け付けていますので、\x01",
            "ぜひご活用くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2295")

    Jump("loc_2874")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2357")

    #C0051
    ChrTalk(
        0x8,
        (
            "……いけませんね。\x01",
            "なんだか職員全体に落ち込んだ\x01",
            "ムードが広がっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "シズクちゃんの手術には\x01",
            "期待がかかってましたし、\x01",
            "仕方がないかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B9")

    label("loc_2357")


    #C0053
    ChrTalk(
        0x8,
        (
            "……私たち職員が\x01",
            "こんな事ではいけませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "なんとか落ち込んだムードを\x01",
            "払拭しないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B9")

    Jump("loc_2874")

    label("loc_23BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248F")

    #C0055
    ChrTalk(
        0x8,
        (
            "ミハイル君の退院が\x01",
            "来週に決まったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "長い間入院していましたから、\x01",
            "なんだか寂しくなりますが……\x01",
            "本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "当日は、みんなで見送って\x01",
            "あげたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24F3")

    label("loc_248F")


    #C0058
    ChrTalk(
        0x8,
        (
            "ミハイル君の退院が決まって\x01",
            "本当によかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "当日は、みんなで見送って\x01",
            "あげたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F3")

    Jump("loc_2874")

    label("loc_24F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25BA")

    #C0060
    ChrTalk(
        0x8,
        (
            "アルバート大公閣下は街の方へ\x01",
            "お戻りになられたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "ふふ、皆さんもお疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "患者さんのほうは退院まで\x01",
            "責任を持って治療させていただきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26ED")

    label("loc_25BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265A")

    #C0063
    ChrTalk(
        0x8,
        (
            "先ほど、アルバート大公閣下が\x01",
            "アリオスさんといらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "今は一通り視察を終えて、\x01",
            "シズクちゃんのお見舞いを\x01",
            "しているようですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26ED")

    label("loc_265A")


    #C0065
    ChrTalk(
        0x8,
        (
            "現在、アルバート大公閣下が\x01",
            "アリオスさんと一緒に\x01",
            "内科の診察室に行っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "一通り視察が終わったので、\x01",
            "少しお話をされているようですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26ED")

    Jump("loc_2874")

    label("loc_26F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2874")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2775")

    #C0067
    ChrTalk(
        0x8,
        (
            "皆さん、問診表の回収\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "また何かありましたら\x01",
            "いつでもいらっしゃって\x01",
            "くださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2874")

    label("loc_2775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2810")

    #C0069
    ChrTalk(
        0x8,
        (
            "セイランド教授は\x01",
            "薬学・神経科の研究室に\x01",
            "いらっしゃいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "屋上に出ると研究棟がありますので、\x01",
            "そこから４階へお向かい下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2874")

    label("loc_2810")


    #C0071
    ChrTalk(
        0x8,
        (
            "セイランド教授は\x01",
            "研究室にいらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "薬学・神経科の研究室は、\x01",
            "研究棟の４階ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2874")

    TalkEnd(0x8)
    Return()

    # Function_7_1478 end

    def Function_8_2878(): pass

    label("Function_8_2878")

    Call(0, 9)
    Return()

    # Function_8_2878 end

    def Function_9_287C(): pass

    label("Function_9_287C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296A")

    #C0073
    ChrTalk(
        0x9,
        (
            "医療物資が限られている現状、\x01",
            "決して楽観視はできませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "こうして外来の対応を\x01",
            "再開できただけでも、患者を救える\x01",
            "可能性はかなり違ってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "私たち職員も、\x01",
            "なんとか頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A24")

    label("loc_296A")


    #C0076
    ChrTalk(
        0x9,
        (
            "現状は難しいでしょうが、\x01",
            "再びレミフェリア方面と連携できれば\x01",
            "医療物資の問題も解決できます。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "ようやく外来の対応も\x01",
            "出来るようになりましたし……\x01",
            "なんとか頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A24")

    Jump("loc_3D48")

    label("loc_2A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B24")

    #C0078
    ChrTalk(
        0x9,
        (
            "現状、クロスベル市方面の\x01",
            "一切の情報が\x01",
            "途絶えてしまっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "おそらく無効宣言の影響で\x01",
            "意図的に情報を\x01",
            "遮断しているのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "こうなると、急病人などの\x01",
            "対応をすることもできません。\x01",
            "……街の皆さんが心配です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BBE")

    label("loc_2B24")


    #C0081
    ChrTalk(
        0x9,
        (
            "現状、クロスベル市方面の\x01",
            "一切の情報が\x01",
            "途絶えてしまっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "こうなると、急病人などの\x01",
            "対応をすることもできません。\x01",
            "……街の皆さんが心配です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBE")

    Jump("loc_3D48")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9B")

    #C0083
    ChrTalk(
        0x9,
        (
            "クロスベル全土で情報規制がされ、\x01",
            "市内の情報は殆ど入ってきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "ときどき救急患者の情報が\x01",
            "送られてくるくらいで、\x01",
            "対応も後手後手になっていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        "ふう、よくない状況です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D23")

    label("loc_2C9B")


    #C0086
    ChrTalk(
        0x9,
        (
            "クロスベル全土で情報規制がされ、\x01",
            "市内の情報は殆ど入ってきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "対応も後手後手になっていまして……\x01",
            "ふう、よくない状況です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D23")

    Jump("loc_3D48")

    label("loc_2D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E54")

    #C0088
    ChrTalk(
        0x9,
        (
            "ティオさんには、\x01",
            "導力ネットの整備関連で\x01",
            "大変お世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "万が一の受け入れ態勢を\x01",
            "万全なものにするためにも、\x01",
            "導力ネットは欠かせませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "この場を借りて、改めて\x01",
            "お礼を言わせていただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#00202Fふふ、いえ……\x01",
            "大したことではありませんから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EF2")

    label("loc_2E54")


    #C0092
    ChrTalk(
        0x9,
        (
            "ティオさんには\x01",
            "導力ネットの整備関連で\x01",
            "大変お世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "とはいえ、この状況が続くのは\x01",
            "病院として大変まずいです。\x01",
            "なんとか対応を考えないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF2")

    Jump("loc_3D48")

    label("loc_2EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3376")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_304B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD6")

    #C0094
    ChrTalk(
        0x9,
        (
            "空港のリカルドさんには、\x01",
            "改めて物資が届いたことを\x01",
            "連絡させていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "あちらも安心したようで、\x01",
            "よかったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "もうこのような事は\x01",
            "無い様にしたいものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3042")

    label("loc_2FD6")


    #C0097
    ChrTalk(
        0x9,
        (
            "リカルドさんも安心したようで、\x01",
            "よかったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "もうこのような事は\x01",
            "無い様にしたいものですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3042")

    TalkEnd(0x9)
    Return()

    label("loc_304B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_30E4")

    #C0099
    ChrTalk(
        0x9,
        (
            "今回の件はみなさんの\x01",
            "せいではありませんから、\x01",
            "どうか気を落とさないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "とにかく、あとはこちら側で\x01",
            "なんとかしてみます。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    label("loc_30E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_318E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3107")
    Call(0, 35)
    Jump("loc_3189")

    label("loc_3107")


    #C0101
    ChrTalk(
        0x9,
        (
            "もしかしたら、交通機関になにか\x01",
            "影響が出たのかもしれませんね……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "と、とにかく、もう一度各方面に\x01",
            "連絡を取ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3189")

    Jump("loc_3371")

    label("loc_318E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E1")

    #C0103
    ChrTalk(
        0x9,
        (
            "一時期は、イリアさんの\x01",
            "お見舞いをしたいと言う方が\x01",
            "沢山来られていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "イリアさんは意識不明のため、\x01",
            "関係者以外はお断りしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "それでも、お見舞いの品だけでもと\x01",
            "お菓子などを差し入れされる方は\x01",
            "後を絶たない様子……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "イリアさんが住民たちにとって\x01",
            "いかに大きな存在であったか、\x01",
            "改めて感じています。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3371")

    label("loc_32E1")


    #C0107
    ChrTalk(
        0x9,
        (
            "イリアさんに\x01",
            "お菓子などを差し入れされる方は\x01",
            "後を絶ちません。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "彼女が住民たちにとって\x01",
            "いかに大きな存在であったか、\x01",
            "改めて感じています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3371")

    Jump("loc_3D48")

    label("loc_3376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3479")

    #C0109
    ChrTalk(
        0x9,
        (
            "昨日から、帝国や共和国より\x01",
            "事故被害者の家族から\x01",
            "安否確認が相次いでいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "やはり、外国で入院となると\x01",
            "ご心配になられる方が\x01",
            "多いようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "それでなくてもクロスベルは\x01",
            "先日の独立提唱から\x01",
            "緊張状態が続いていますから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3500")

    label("loc_3479")


    #C0112
    ChrTalk(
        0x9,
        (
            "やはり、外国で入院となると\x01",
            "ご心配になられる方が\x01",
            "多いようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "一刻も早く帰国できるよう、\x01",
            "誠心誠意対応していきたい所です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3500")

    Jump("loc_3D48")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F9")

    #C0114
    ChrTalk(
        0x9,
        (
            "導力ネットワークの法整備が\x01",
            "整ってきたおかげで、ネットでの\x01",
            "再診予約も増えてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "クロスベルが独立すれば\x01",
            "このような有用な法案も\x01",
            "通りやすくなると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "実際、住民投票は\x01",
            "どうなるのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_366E")

    label("loc_35F9")


    #C0117
    ChrTalk(
        0x9,
        (
            "クロスベルが独立すれば\x01",
            "有用な法案も通りやすくなる\x01",
            "と思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "実際、住民投票は\x01",
            "どうなるのでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366E")

    Jump("loc_3D48")

    label("loc_3673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378D")

    #C0119
    ChrTalk(
        0x9,
        (
            "先日のシズクちゃんの手術では、\x01",
            "セイランド教授の考案した\x01",
            "画期的な術式が施されたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "医療関係者からの関心も高く、\x01",
            "一時期落ち込みかけていた信頼は\x01",
            "完全に回復したと言えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "……しかし、手放しでは喜べません。\x01",
            "成功して欲しかったものです……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3830")

    label("loc_378D")


    #C0122
    ChrTalk(
        0x9,
        (
            "画期的な手術を試みたことで、\x01",
            "一時期落ち込みかけていた信頼は\x01",
            "完全に回復したと言えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "……しかし、手放しでは喜べません。\x01",
            "成功して欲しかったものです……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3830")

    Jump("loc_3D48")

    label("loc_3835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393C")

    #C0124
    ChrTalk(
        0x9,
        (
            "近いうちに、\x01",
            "セイランド教授によって\x01",
            "大きな手術が行われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "昨日のアルバート大公の視察で\x01",
            "レミフェリアからも全面的に\x01",
            "支援して頂けることになりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "私たちも、手術の成功に向けて\x01",
            "できる限りの事をしなければ\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_39CA")

    label("loc_393C")


    #C0127
    ChrTalk(
        0x9,
        (
            "近いうちに、\x01",
            "セイランド教授によって\x01",
            "大きな手術が行われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "私たちも、手術の成功に向けて\x01",
            "できる限りの事をしなければ\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CA")

    Jump("loc_3D48")

    label("loc_39CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA0")

    #C0129
    ChrTalk(
        0x9,
        (
            "アルバート大公から\x01",
            "労#2Rねぎら#いの言葉をいただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "病院のスポンサーでもある大公には、\x01",
            "以前から力強く支援していただいています。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        "職員一同、本当に励まされますよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B17")

    label("loc_3AA0")


    #C0132
    ChrTalk(
        0x9,
        (
            "病院のスポンサーでもある大公には、\x01",
            "以前から力強く支援していただいています。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        "職員一同、本当に励まされますよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3B17")

    Jump("loc_3D48")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8A")

    #C0134
    ChrTalk(
        0x9,
        (
            "『教団事件』のスキャンダルで、\x01",
            "病院が築き上げてきた信頼は\x01",
            "一度、地に落ちてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "病院の医師が薬品を用いて\x01",
            "この地を混乱に陥れたのです。\x01",
            "……無理からぬ話でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "警察の綿密な調査によって\x01",
            "普段、彼が処方していた薬は\x01",
            "問題ないことが証明されましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "患者さんの中には、いまだに\x01",
            "不信感を拭えない方も居るようです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D48")

    label("loc_3C8A")


    #C0138
    ChrTalk(
        0x9,
        (
            "疑惑が払拭されたとはいえ、\x01",
            "いまだに病院に対して不信感を\x01",
            "抱えている方もいらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "これからは、より開かれた医療を\x01",
            "目指して、徐々に信頼を取り戻して\x01",
            "いかなければいけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D48")

    TalkEnd(0x9)
    Return()

    # Function_9_287C end

    def Function_10_3D4C(): pass

    label("Function_10_3D4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3D")

    #C0140
    ChrTalk(
        0xA,
        (
            "弟君たち……\x01",
            "すっごく大変そうだけど、\x01",
            "絶対にヘコたれちゃだめよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "何もかも終わって落ち着いたら\x01",
            "きっとまた一緒に遊びましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#00309Fああ、任せてくれ！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#00000Fはは、頑張らせていただきます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EE8")

    label("loc_3E3D")


    #C0144
    ChrTalk(
        0xA,
        (
            "何もかも終わって落ち着いたら\x01",
            "きっとまた一緒に遊びましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "エイダやフィリア、シロンにメイファ、\x01",
            "それにこの際マーサ師長も誘って、\x01",
            "みんなでパーッとやりましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE8")

    Jump("loc_4A75")

    label("loc_3EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FED")

    #C0146
    ChrTalk(
        0xA,
        (
            "病院に残らざるをえなくなった\x01",
            "外来客たちのストレスも、\x01",
            "段々ピークに達してきてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "街であんな事があって、\x01",
            "もしかしたら帰れるかもって\x01",
            "希望を持ち始めたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "どうなるか分からないけど、\x01",
            "本当に帰れるといいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4080")

    label("loc_3FED")


    #C0149
    ChrTalk(
        0xA,
        (
            "街であんな事があって、\x01",
            "病院に残らざるをえなくなった\x01",
            "外来客も希望を持ち始めたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "どうなるか分からないけど、\x01",
            "本当に帰れるといいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4080")

    Jump("loc_4A75")

    label("loc_4085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4184")

    #C0151
    ChrTalk(
        0xA,
        (
            "イリア・プラティエは、\x01",
            "今のところ、完治の見込みが\x01",
            "たっていないみたいなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "……でも、大丈夫。\x01",
            "ウチの病院の先生方は\x01",
            "とっても優秀だもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "時間はかかるかもしれないけど、\x01",
            "先生方なら絶対に\x01",
            "イリアを治してくれるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4201")

    label("loc_4184")


    #C0154
    ChrTalk(
        0xA,
        (
            "ウチの病院の先生方は\x01",
            "とっても優秀だもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        (
            "時間はかかるかもしれないけど、\x01",
            "先生方なら絶対に\x01",
            "イリアを治してくれるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4201")

    Jump("loc_4A75")

    label("loc_4206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F4")

    #C0156
    ChrTalk(
        0xA,
        (
            "こんな状況だけど……\x01",
            "病院にいる人たちは\x01",
            "意外と前向きなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        (
            "なんたって、意識不明だった\x01",
            "イリア・プラティエが\x01",
            "ようやく眼を覚ましたんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xA,
        (
            "そう考えたら、あたしたちも\x01",
            "頑張らなくちゃって思うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_437D")

    label("loc_42F4")


    #C0159
    ChrTalk(
        0xA,
        (
            "イリア・プラティエが\x01",
            "意識を取り戻したなんて、\x01",
            "久々の明るいニュースよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "そう考えたら、あたしたちも\x01",
            "頑張らなくちゃって思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437D")

    Jump("loc_4A75")

    label("loc_4382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4421")

    #C0161
    ChrTalk(
        0xA,
        (
            "はあ、いくらなんでも\x01",
            "疲れてきたわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "……ううん、患者さんたちは\x01",
            "もっと苦しい思いをしてるんだもの。\x01",
            "泣き言なんて言ってられないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_4421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_44AC")

    #C0163
    ChrTalk(
        0xA,
        (
            "昨日の列車事故の影響で\x01",
            "私たちも大忙しよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "しばらくは遊んだりできる\x01",
            "雰囲気でもないし……\x01",
            "しっかりと仕事しなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_44AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4540")

    #C0165
    ChrTalk(
        0xA,
        (
            "シズクちゃんの芯の強さには\x01",
            "いつもこっちが元気付けられてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "私たち看護師も希望を持って\x01",
            "シズクちゃんを支えていかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_4540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_46A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460C")

    #C0167
    ChrTalk(
        0xA,
        (
            "シズクちゃん、今までにも\x01",
            "何度か目の手術を受けているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "でも、優秀な病院の先生たちでも\x01",
            "いつも上手くいかなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "あの子も、アリオスさんも\x01",
            "本当に不安でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_469B")

    label("loc_460C")


    #C0170
    ChrTalk(
        0xA,
        (
            "シズクちゃん、今までにも\x01",
            "何度か目の手術を受けているけど、\x01",
            "いつも上手くいかなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "あの子も、アリオスさんも\x01",
            "本当に不安でしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469B")

    Jump("loc_4A75")

    label("loc_46A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476F")

    #C0172
    ChrTalk(
        0xA,
        (
            "噂じゃセイランド教授が、\x01",
            "近いうちに大きな手術を\x01",
            "やるって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "この病院でそんな手術が\x01",
            "必要になるのって\x01",
            "“あの子”以外ないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        "治ってくれるといいんだけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47D9")

    label("loc_476F")


    #C0175
    ChrTalk(
        0xA,
        (
            "この病院で大きな手術が\x01",
            "必要になるのって\x01",
            "“あの子”以外ないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        "治ってくれるといいんだけど。\x02",
    )

    CloseMessageWindow()

    label("loc_47D9")

    Jump("loc_4A75")

    label("loc_47DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489C")

    #C0177
    ChrTalk(
        0xA,
        (
            "今日はラゴー教授が\x01",
            "出張でいらっしゃらないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "なんでも、外国の学会に\x01",
            "出席してるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "代わりにセイランド教授が\x01",
            "今日の内科を受け持ってるわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4910")

    label("loc_489C")


    #C0180
    ChrTalk(
        0xA,
        (
            "今日はラゴー教授、\x01",
            "外国の学会に出張しているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "せっかく大公さまが来るのに\x01",
            "挨拶できないって嘆いてたわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4910")

    Jump("loc_4A75")

    label("loc_4915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A24")

    #C0182
    ChrTalk(
        0xA,
        (
            "あれ、ランディさんに\x01",
            "弟君じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x104,
        "#00309Fランちゃん、久しぶりだな。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#00000Fご無沙汰してます。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "そういえば\x01",
            "久しぶりだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "せっかくだから\x01",
            "もっと話してたいけど、\x01",
            "今は仕事中なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        "また今度声かけてちょうだい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 6)
    Jump("loc_4A75")

    label("loc_4A24")


    #C0188
    ChrTalk(
        0xA,
        (
            "もっと話してたいけど、\x01",
            "今は仕事中なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        "また今度声かけてちょうだい。\x02",
    )

    CloseMessageWindow()

    label("loc_4A75")

    TalkEnd(0xFE)
    Return()

    # Function_10_3D4C end

    def Function_11_4A79(): pass

    label("Function_11_4A79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A97")
    Call(0, 12)
    Jump("loc_4B05")

    label("loc_4A97")


    #C0190
    ChrTalk(
        0xB,
        (
            "ウォッホン、私の好敵手は\x01",
            "こうでなくてはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "さあ、患者は待ってくれん。\x01",
            "さっそく取り掛かるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B05")

    Jump("loc_5828")

    label("loc_4B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C36")

    #C0192
    ChrTalk(
        0xB,
        (
            "セイランド君と一緒に\x01",
            "旧い医学書をあたってみたのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "自治州内に生えている薬草などで、\x01",
            "麻酔などのいくつかの薬品は\x01",
            "ここでの調合も可能らしいのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "レミフェリアとの外交が絶たれ、\x01",
            "医療物資が足りない事には変わりないが……\x01",
            "少しだけ光明が見えてきたかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D0E")

    label("loc_4C36")


    #C0195
    ChrTalk(
        0xB,
        (
            "セイランド君と一緒に調べたところ、\x01",
            "いくつかの不足している薬品は\x01",
            "クロスベルだけで賄えそうなのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "レミフェリアとの外交が絶たれ、\x01",
            "医療物資が足りない事には変わりないが……\x01",
            "少しだけ光明が見えてきたかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D0E")

    Jump("loc_5828")

    label("loc_4D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D2E")
    Call(0, 12)
    Jump("loc_4DD4")

    label("loc_4D2E")


    #C0197
    ChrTalk(
        0xB,
        (
            "妻や息子の心配で\x01",
            "何も手につかないようなら、\x01",
            "いっそ帰るべきと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "フム、彼もプロの医者だからな。\x01",
            "……柄にもなく、いらぬ気遣いを\x01",
            "してしまったようだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD4")

    Jump("loc_5828")

    label("loc_4DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED6")

    #C0199
    ChrTalk(
        0xB,
        (
            "クロスベル大聖堂も、\x01",
            "街と共に結界の中へと\x01",
            "包まれてしまったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "エラルダ大司教にも\x01",
            "色々と相談したかったのだが……\x01",
            "連絡がつかぬのは仕方あるまいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x105,
        (
            "#10403F（エラルダ大司教か……\x01",
            "  彼は今どうしているのやら。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F6D")

    label("loc_4ED6")


    #C0202
    ChrTalk(
        0xB,
        (
            "エラルダ大司教にも\x01",
            "色々と相談したかったのだが……\x01",
            "連絡がつかぬのは仕方あるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "これも女神の与えた試練だろう。\x01",
            "患者達の為にも尽力せねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6D")

    Jump("loc_5828")

    label("loc_4F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5052")

    #C0204
    ChrTalk(
        0xB,
        (
            "襲撃事件の被害者は、\x01",
            "何も怪我を負った者たち\x01",
            "だけではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "事件にショックを感じ、\x01",
            "それが元で胃を痛めたり\x01",
            "する者も多いのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        (
            "精神と肉体は極めて密接に\x01",
            "関係していると言えるだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50C6")

    label("loc_5052")


    #C0207
    ChrTalk(
        0xB,
        (
            "精神的な負担によって\x01",
            "身体に異常をきたす者もいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "精神と肉体は極めて密接に\x01",
            "関係していると言えるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C6")

    Jump("loc_5828")

    label("loc_50CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_52B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51FF")

    #C0209
    ChrTalk(
        0xB,
        (
            "私は以前、人の身体にメスをいれる\x01",
            "行為自体に猜疑#4Rさいぎ#的なものを感じていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "だが、時代が進み文明が発達すれば\x01",
            "内科だけで対応しきれないことも多い。\x01",
            "……今回の列車事故のようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xB,
        (
            "病院に勤める以上は、\x01",
            "新しい医療の形を受け入れることが\x01",
            "重要なのだと、改めて感じたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52AF")

    label("loc_51FF")


    #C0212
    ChrTalk(
        0xB,
        (
            "人の身体にメスをいれる……\x01",
            "それを拒むことは旧く、\x01",
            "柔軟性に欠ける考えなのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "病院に勤める以上は、\x01",
            "新しい医療の形を受け入れることが\x01",
            "重要なのだと、改めて感じたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52AF")

    Jump("loc_5828")

    label("loc_52B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_546E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C5")

    #C0214
    ChrTalk(
        0xB,
        (
            "人間の身体には、\x01",
            "怪我や病気を治癒する力が\x01",
            "もともと備わっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "内科で処方する薬の多くは、\x01",
            "この“自己治癒力”を促進して\x01",
            "治療を行うというものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        (
            "この辺りの極意は教会にあってね。\x01",
            "私たち内科医はそれをもとに\x01",
            "施術を行っているのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5469")

    label("loc_53C5")


    #C0217
    ChrTalk(
        0xB,
        (
            "人間の身体には、\x01",
            "怪我や病気を治癒する力……\x01",
            "“自己治癒力”が備わっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "内科で処方する薬の多くは、\x01",
            "それを促進することで\x01",
            "自然な治療を行うものなのだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5469")

    Jump("loc_5828")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5489")
    Call(0, 12)
    Jump("loc_54BA")

    label("loc_5489")


    #C0219
    ChrTalk(
        0xB,
        (
            "……ふう、いい加減\x01",
            "頭を冷やさねばならんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54BA")

    Jump("loc_5828")

    label("loc_54BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DA")
    Call(0, 12)
    Jump("loc_54F4")

    label("loc_54DA")


    #C0220
    ChrTalk(
        0xB,
        "このヒゲがぁあ……！\x02",
    )

    CloseMessageWindow()

    label("loc_54F4")

    Jump("loc_5828")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5507")
    Jump("loc_5828")

    label("loc_5507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_56C1")
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0221
    ChrTalk(
        0xB,
        (
            "おや、諸君は確か\x01",
            "警察の特務支援課だったな。\x01",
            "いや、いい所に来た。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        (
            "実は明日、研究していた\x01",
            "『ルピナス草』についての論文を\x01",
            "学会で発表する事になってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xB,
        (
            "君たちにも報告したいと\x01",
            "思っていたところだったのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00000Fルピナス草といえば……\x01",
            "以前依頼で扱った薬草でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        "#00100Fふふ、おめでとうございます。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "ああ、君たちのおかげだ。\x01",
            "改めて御礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_56C1")


    #C0227
    ChrTalk(
        0xB,
        (
            "うぉっほん！\x01",
            "私は内科を受け持つ\x01",
            "ラゴーという者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        (
            "実は明日、研究していた\x01",
            "『ルピナス草』という薬草の論文を\x01",
            "学会で発表する事になってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xB,
        (
            "フフ、実に光栄なことだよ。\x01",
            "体調を万全にして臨まなければな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5794")

    SetScenarioFlags(0x159, 7)
    Jump("loc_5828")

    label("loc_579C")


    #C0230
    ChrTalk(
        0xB,
        (
            "明日、外国で行われる学会にて\x01",
            "『ルピナス草』の論文を発表するのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "実は、病院に大事な来客もあるのだが……\x01",
            "今回は致し方あるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5828")

    TalkEnd(0xFE)
    Return()

    # Function_11_4A79 end

    def Function_12_582C(): pass

    label("Function_12_582C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_59DF")

    #C0232
    ChrTalk(
        0xB,
        (
            "ゲイリー教授、君の手術は\x01",
            "私が助手を務めさせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xE,
        (
            "新しく調合したという\x01",
            "麻酔薬の用意もお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xE,
        (
            "……フフ。\x01",
            "今日はそのハゲ頭以外も\x01",
            "輝いているようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xB,
        (
            "フン、君のその\x01",
            "汚らしいヒゲ面もな。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        (
            "どうしたことか、今日は\x01",
            "『闇医者グレン』のような\x01",
            "貫禄が見られる気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    OP_64(0xE)

    #C0237
    ChrTalk(
        0xE,
        (
            "……フフ、ではさっそく\x01",
            "手術にとりかかりましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xB,
        "ウム！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EEC")

    label("loc_59DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5BE0")

    #C0239
    ChrTalk(
        0xB,
        (
            "ウォッホン、ゲイリー教授。\x01",
            "……その、なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "君の妻と息子はクロスベル市に\x01",
            "住んでいるそうだが……\x01",
            "連絡は取れているのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xE,
        "……いえ、ここの所は。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        "そうか……心配だな。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "……なんだったらキミ、\x01",
            "国防軍に交渉して\x01",
            "街に帰ってはどうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xE,
        (
            "いや……妻もキーンツも、\x01",
            "自分の面倒は自分で見られるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xE,
        (
            "重傷患者がいつ運び込まれるか\x01",
            "分からない状態で、病院を\x01",
            "離れることなどできません。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        "それはラゴー教授も同じでしょう？\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xB,
        (
            "……ウム、そうだな。\x01",
            "いらぬ気遣いをしたようだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEC")

    label("loc_5BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D5E")

    #C0248
    ChrTalk(
        0xB,
        (
            "セイランド君の術式は\x01",
            "現時点で考えられる\x01",
            "最善のものであったはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xB,
        (
            "……手術が失敗した原因は、\x01",
            "君の不手際にあったんじゃないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xE,
        (
            "なっ……そういうあなたこそ、\x01",
            "慣れない手術に手が震えて\x01",
            "ミスでもやらかしたのでは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xB,
        "#4Sなにをぉう！？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xE,
        "#4Sやるのか！？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    OP_64(0xE)

    #C0253
    ChrTalk(
        0xE,
        "……よしましょう、今回は。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        "……そうだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EEC")

    label("loc_5D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5EEC")

    #C0255
    ChrTalk(
        0xB,
        (
            "昨日の学会で、\x01",
            "私の論文が絶賛されてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "いやはや、君にも\x01",
            "あの勇姿をみせたかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "私も昨日、病院の視察に来た\x01",
            "アルバート大公直々に、\x01",
            "激励の言葉を頂きましてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "『今後の外科医療の発展は\x01",
            "  君の双肩にかかっている』……\x01",
            "いや、本当にありがたい事ですよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    OP_64(0xE)

    #C0259
    ChrTalk(
        0xB,
        "#4S調子にのるなよ、このヒゲ！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xE,
        "#4Sこっちのセリフだ、このハゲ！\x02",
    )

    CloseMessageWindow()

    label("loc_5EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5EFF")
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)

    label("loc_5EFF")

    SetScenarioFlags(0x2, 0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_582C end

    def Function_13_5F0B(): pass

    label("Function_13_5F0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_605D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FCA")

    #C0261
    ChrTalk(
        0xC,
        (
            "このおかしな事態への不安で\x01",
            "体調を崩してる人もいるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "病院では心の分野は専門外だけど、\x01",
            "そういう患者さんの相談にも\x01",
            "できるだけ乗ってあげないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6058")

    label("loc_5FCA")


    #C0263
    ChrTalk(
        0xC,
        "心の分野は本来、教会の分野だけど……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "せっかく病院を頼って来てくれるんだ、\x01",
            "そういう患者さんの相談にも\x01",
            "できるだけ乗ってあげないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6058")

    Jump("loc_6721")

    label("loc_605D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_611D")

    #C0265
    ChrTalk(
        0xC,
        (
            "教授たちの手伝いで、\x01",
            "研究棟に保管してる薬草のサンプルを\x01",
            "ありったけ引っ張り出して来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "色々大変な時期だけど、\x01",
            "何もせずに日和見してるよりは\x01",
            "出来ることをしないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6721")

    label("loc_611D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_612B")
    Jump("loc_6721")

    label("loc_612B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6139")
    Jump("loc_6721")

    label("loc_6139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6147")
    Jump("loc_6721")

    label("loc_6147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61EF")

    #C0267
    ChrTalk(
        0xC,
        (
            "昨日、たくさんの患者が\x01",
            "運びこまれてから働き通しでね。\x01",
            "そろそろ体力が限界だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "もうちょっとしたら\x01",
            "寮の方に仮眠を取りにいこうかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_624F")

    label("loc_61EF")


    #C0269
    ChrTalk(
        0xC,
        (
            "それにしても、\x01",
            "ずっと働き通しなのに\x01",
            "教授はタフだなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        "僕ももっと体力つけないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_624F")

    Jump("loc_6721")

    label("loc_6254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6262")
    Jump("loc_6721")

    label("loc_6262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_627D")
    Call(0, 37)
    Jump("loc_632F")

    label("loc_627D")


    #C0271
    ChrTalk(
        0xC,
        (
            "劇や舞台などを楽しんだ後、\x01",
            "再検査したら病気が治った……\x01",
            "そんな話を聞いた事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "もしかすると、ここ最近\x01",
            "お孫さんと楽しく過ごした事が\x01",
            "良かったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632F")

    Jump("loc_6721")

    label("loc_6334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6342")
    Jump("loc_6721")

    label("loc_6342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A6")

    #C0273
    ChrTalk(
        0xC,
        (
            "ヨアヒム先生が例の事件の\x01",
            "首謀者だったって知った時は、\x01",
            "本当にショックでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "セイランド先生が\x01",
            "新しい上司として着任してからも、\x01",
            "しばらく落ち込んでたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "『患者がいるかぎり、\x01",
            "　私たちに落ち込んでる暇はない。』\x01",
            "……そう先生に教えられてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "今はとにかく、先生の教えの下で\x01",
            "あくせく働いていくつもりさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6531")

    label("loc_64A6")


    #C0277
    ChrTalk(
        0xC,
        (
            "セイランド先生は、\x01",
            "僕にガンガン仕事を回すからね。\x01",
            "お陰で落ち込んでる暇もないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xC,
        (
            "はは、あの厳しさも\x01",
            "先生の優しさの内なのかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6531")

    Jump("loc_667C")

    label("loc_6536")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65E7")

    #C0279
    ChrTalk(
        0xC,
        (
            "調合した薬が効いて、\x01",
            "容態が安定してきたよ。\x01",
            "これでひとまずは安心だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        (
            "それにしても、大公閣下は\x01",
            "相当医学の知識が深いみたいだね。\x01",
            "見習いたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667C")

    label("loc_65E7")


    #C0281
    ChrTalk(
        0xC,
        (
            "大公閣下とセイランド教授、\x01",
            "結構昔からの知り合いみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        (
            "セイランド教授が大公閣下に\x01",
            "いつもの雰囲気で話してて、\x01",
            "なんだかヒヤヒヤするよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_667C")

    Jump("loc_6721")

    label("loc_6681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669C")
    Call(0, 39)
    Jump("loc_6721")

    label("loc_669C")


    #C0283
    ChrTalk(
        0xC,
        (
            "クワインさんがお薬を\x01",
            "飲んでくれるようになって、\x01",
            "僕も本当に嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "これも全て、アミサちゃんが\x01",
            "頑張ってくれたおかげだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6721")

    TalkEnd(0xFE)
    Return()

    # Function_13_5F0B end

    def Function_14_6725(): pass

    label("Function_14_6725")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_67CB")

    #C0285
    ChrTalk(
        0xD,
        (
            "患者さんがどっと入ってきて\x01",
            "かなり忙しいけど……やってやるわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "今はまだまだだけど、\x01",
            "きっとセイランド教授みたいな\x01",
            "デキる女医になるんだから！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_67CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_684F")

    #C0287
    ChrTalk(
        0xD,
        (
            "案外、民間療法のたぐいも\x01",
            "参考になるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "寮の本棚に置いてたはずだから\x01",
            "あとで探してみようっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_684F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_69E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6934")

    #C0289
    ChrTalk(
        0xD,
        (
            "国防軍から支給があった薬品を\x01",
            "整理しているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xD,
        (
            "ほんと、素人が揃えましたって\x01",
            "感じの品揃えなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "当面はなんとかなるだろうけど、\x01",
            "難病の患者さんがきたら\x01",
            "さすがに対処できないわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69E0")

    label("loc_6934")


    #C0292
    ChrTalk(
        0xD,
        (
            "国防軍から支給があった薬品は\x01",
            "ほんと、素人が揃えましたって\x01",
            "感じの品揃えなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "当面はなんとかなるだろうけど、\x01",
            "難病の患者さんがきたら\x01",
            "さすがに対処できないわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69E0")

    Jump("loc_7172")

    label("loc_69E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6A68")

    #C0294
    ChrTalk(
        0xD,
        (
            "外来の受付が止まってるとはいえ、\x01",
            "重病の患者がいつ来るか分からないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        "準備だけはきちんとしておかなきゃね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_6A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7B")

    #C0296
    ChrTalk(
        0xD,
        (
            "『医者はこういうときこそ\x01",
            "沈んだ表情を見せてはならない……』\x01",
            "ラゴー教授が教えてくれたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        (
            "私たちまで不安な顔をしてたら\x01",
            "患者にそれが伝染するものね。\x01",
            "気をつけないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xD,
        (
            "不安って言うのは、ある意味\x01",
            "病気みたいなものなのかも\x01",
            "しれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BF5")

    label("loc_6B7B")


    #C0299
    ChrTalk(
        0xD,
        (
            "『医者はこういうときこそ\x01",
            "沈んだ表情を見せてはならない……』\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "……頭では分かってるんだけど、\x01",
            "私には難しいかも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF5")

    Jump("loc_7172")

    label("loc_6BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CEA")

    #C0301
    ChrTalk(
        0xD,
        (
            "雨に当たって濡れたりすると、\x01",
            "風邪を引きやすいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "これは、身体が冷えることで\x01",
            "本来持っている免疫力が\x01",
            "働かなくなるのが原因みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        (
            "あなたたちも家に帰ったら、\x01",
            "ちゃんと着替えて\x01",
            "暖まらないとダメよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D6B")

    label("loc_6CEA")


    #C0304
    ChrTalk(
        0xD,
        (
            "雨に当たって濡れたりすると、\x01",
            "風邪を引きやすいのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xD,
        (
            "あなたたちも家に帰ったら、\x01",
            "ちゃんと着替えて\x01",
            "暖まらないとダメよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D6B")

    Jump("loc_7172")

    label("loc_6D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6E11")

    #C0306
    ChrTalk(
        0xD,
        (
            "リットン君、なんだか最近\x01",
            "回診に行く事が多いみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xD,
        (
            "むむむ、私も負けてられないわ。\x01",
            "患者さんに信用してもらえる\x01",
            "デキる女医になるんだから！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_6E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E1F")
    Jump("loc_7172")

    label("loc_6E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE2")

    #C0308
    ChrTalk(
        0xD,
        (
            "やれやれ、教授たちはまた\x01",
            "喧嘩してるみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xD,
        (
            "こういうときは、\x01",
            "ヘタに止めに入らないほうが\x01",
            "早く終わるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "今のうちにカルテの整理でも\x01",
            "しとこうかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F42")

    label("loc_6EE2")


    #C0311
    ChrTalk(
        0xD,
        (
            "教授たちの喧嘩には\x01",
            "いい加減慣れちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xD,
        (
            "今のうちにカルテの整理でも\x01",
            "しとこうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F42")

    Jump("loc_7172")

    label("loc_6F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_701D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FCF")

    #C0313
    ChrTalk(
        0xD,
        (
            "やっぱり教授は\x01",
            "すごいなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xD,
        (
            "……いけないいけない、\x01",
            "今は自分にやれることを\x01",
            "しっかりやらないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7018")

    label("loc_6FCF")


    #C0315
    ChrTalk(
        0xD,
        (
            "それにしても、\x01",
            "私ってば情けないなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xD,
        "もっと勉強しなくっちゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_7018")

    Jump("loc_7172")

    label("loc_701D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7102")

    #C0317
    ChrTalk(
        0xD,
        (
            "この間から、寮で同室のフローラが\x01",
            "新人研修医の面倒みてるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xD,
        (
            "ミショー君って言ったっけ……\x01",
            "なんだか自分が新人だった頃を\x01",
            "思い出しちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xD,
        (
            "ま、いまだ勉強中なのは\x01",
            "変わらないんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7172")

    label("loc_7102")


    #C0320
    ChrTalk(
        0xD,
        (
            "ミショー君を見てると、\x01",
            "なんだか自分が新人だった頃を\x01",
            "思い出しちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xD,
        "ま、私もいまだ勉強中だけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_7172")

    TalkEnd(0xFE)
    Return()

    # Function_14_6725 end

    def Function_15_7176(): pass

    label("Function_15_7176")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7194")
    Call(0, 12)
    Jump("loc_720F")

    label("loc_7194")


    #C0322
    ChrTalk(
        0xE,
        (
            "ラゴー教授など嫌いだが、\x01",
            "彼のサポート以上に\x01",
            "信頼できるものはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xE,
        (
            "フフ、今ならどんな手術も\x01",
            "こなせる気がするな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_720F")

    Jump("loc_7BF3")

    label("loc_7214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D9")

    #C0324
    ChrTalk(
        0xE,
        (
            "足りない医療物資は\x01",
            "内科と神経・薬学科で\x01",
            "なんとかしてみるつもりらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xE,
        (
            "……今は手術も入っていないし、\x01",
            "仕事の合間にアーシュラ君たちの\x01",
            "手伝いをしているとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_735D")

    label("loc_72D9")


    #C0326
    ChrTalk(
        0xE,
        (
            "仕事の合間にアーシュラ君たちの\x01",
            "手伝いをしているとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xE,
        (
            "いつ手術が入ってもいいように、\x01",
            "万全の準備を整えておかなければ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735D")

    Jump("loc_7BF3")

    label("loc_7362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737D")
    Call(0, 12)
    Jump("loc_7404")

    label("loc_737D")


    #C0328
    ChrTalk(
        0xE,
        (
            "……ラゴー教授も、たまには\x01",
            "気の利いたことが言えるのだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xE,
        (
            "まあ、妻とキーンツは\x01",
            "きっと大丈夫だから、\x01",
            "心配などしていないがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7404")

    Jump("loc_7BF3")

    label("loc_7409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_748D")

    #C0330
    ChrTalk(
        0xE,
        (
            "……街に残してきた\x01",
            "妻とキーンツは\x01",
            "どうしているだろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xE,
        (
            "病気などしていなければ\x01",
            "いいんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7503")

    label("loc_748D")


    #C0332
    ChrTalk(
        0xE,
        "……ふう、心配はよそう。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xE,
        (
            "ここに運び込まれてこないんだ、\x01",
            "妻とキーンツはきっと健康に\x01",
            "過ごしているに違いない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7503")

    Jump("loc_7BF3")

    label("loc_7508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B8")

    #C0334
    ChrTalk(
        0xE,
        (
            "長年病院に勤めているが、\x01",
            "病室を埋めてしまうほどの\x01",
            "入院患者が来たのは初めてだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xE,
        (
            "まさに未曾有の事態と言えるな。\x01",
            "何とか乗り越えていかねば……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7604")

    label("loc_75B8")


    #C0336
    ChrTalk(
        0xE,
        (
            "この状況……\x01",
            "まさに未曾有の事態と言える。\x01",
            "何とか乗り越えていかねば……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7604")

    Jump("loc_7BF3")

    label("loc_7609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76D3")

    #C0337
    ChrTalk(
        0xE,
        (
            "ふう……先ほど、\x01",
            "一通りの手術が終わったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xE,
        (
            "何分、患者の数が多くてな。\x01",
            "処置が朝までかかってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xE,
        (
            "今日の診察が一通り終わったら、\x01",
            "泥のように眠りこけたいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7743")

    label("loc_76D3")


    #C0340
    ChrTalk(
        0xE,
        (
            "朝までの手術で疲れたが……\x01",
            "患者は待ってくれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xE,
        (
            "今日の診察が終わるまでは\x01",
            "しっかりとしていないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7743")

    Jump("loc_7BF3")

    label("loc_7748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7819")

    #C0342
    ChrTalk(
        0xE,
        (
            "最近、息子のキーンツが\x01",
            "何か悩んでいるらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xE,
        (
            "はあ、病院の仕事も忙しいし\x01",
            "心配事が尽きんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        (
            "下手をすると、ラゴー教授に\x01",
            "胃痛の治療を受ける羽目に\x01",
            "なるかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7892")

    label("loc_7819")


    #C0345
    ChrTalk(
        0xE,
        (
            "やれやれ、公私ともに\x01",
            "心配事が尽きんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xE,
        (
            "下手をすると、ラゴー教授に\x01",
            "胃痛の治療を受ける羽目に\x01",
            "なるかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7892")

    Jump("loc_7BF3")

    label("loc_7897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78B2")
    Call(0, 12)
    Jump("loc_7943")

    label("loc_78B2")


    #C0347
    ChrTalk(
        0xE,
        (
            "私たちも手術に参加したが、\x01",
            "今回ばかりは無力さを\x01",
            "思い知らされてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        (
            "この失敗に患者が絶望してないか……\x01",
            "それだけが気がかりだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7943")

    Jump("loc_7BF3")

    label("loc_7948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_798A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7963")
    Call(0, 12)
    Jump("loc_7985")

    label("loc_7963")


    #C0349
    ChrTalk(
        0xE,
        "調子にのるな、ハゲェエ……！\x02",
    )

    CloseMessageWindow()

    label("loc_7985")

    Jump("loc_7BF3")

    label("loc_798A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7A9A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A05")

    #C0350
    ChrTalk(
        0xE,
        "大公閣下がお帰りになったそうだな……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        (
            "はあ、やれやれ……\x01",
            "アーシュラ君にも困ったものだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A95")

    label("loc_7A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A17")
    Call(0, 16)
    Jump("loc_7A95")

    label("loc_7A17")


    #C0352
    ChrTalk(
        0xE,
        (
            "大公閣下が視察にきているというのに、\x01",
            "なんというマイペースな……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "アーシュラ君にはキツいお灸を\x01",
            "据えてやらんとな……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A95")

    Jump("loc_7BF3")

    label("loc_7A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B7B")

    #C0354
    ChrTalk(
        0xE,
        (
            "ラゴー教授め、どうも\x01",
            "有頂天になっているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xE,
        (
            "会うたび会うたび\x01",
            "これ見よがしに自慢しおって。\x01",
            "まったく、あのハゲ頭め……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "……まあ、確かにヤツの研究は\x01",
            "賞賛に値するものではあるがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7BF3")

    label("loc_7B7B")


    #C0357
    ChrTalk(
        0xE,
        (
            "ラゴー教授の研究成果は\x01",
            "認めざるを得まい。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xE,
        (
            "ヤツの有頂天ぶりは癪に障るが……\x01",
            "フン、今回くらいは我慢してやるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BF3")

    TalkEnd(0xFE)
    Return()

    # Function_15_7176 end

    def Function_16_7BF7(): pass

    label("Function_16_7BF7")

    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0359
    ChrTalk(
        0xE,
        (
            "シャ、シャルール君、\x01",
            "アーシュラ君は寝坊か！？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x10,
        (
            "ええ、おそらくは。\x01",
            "……昨日も遅くまで研究室に\x01",
            "こもってらしたようですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xE,
        (
            "た、大公が視察に\x01",
            "きているというのに、\x01",
            "なんとだらしない……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xE,
        (
            "ええい、なんとしても\x01",
            "叩き起こしてきたまえ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_16_7BF7 end

    def Function_17_7D07(): pass

    label("Function_17_7D07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DB4")

    #C0363
    ChrTalk(
        0xF,
        (
            "湿地帯付近に出現した巨大な樹、\x01",
            "スゴすぎますね～……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "どういう原理で、何の為に\x01",
            "あの場所に現れたのか……\x01",
            "科学的な興味が尽きませんよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7E51")

    label("loc_7DB4")


    #C0365
    ChrTalk(
        0xF,
        (
            "……はっ、つい浮かれちゃいました。\x01",
            "すみません、こんな時に……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xF,
        (
            "今はとにかく、患者さんの対応と\x01",
            "医療機器のメンテナンスを\x01",
            "きちんとやらないと、ですね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E51")

    Jump("loc_8B3E")

    label("loc_7E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F17")

    #C0367
    ChrTalk(
        0xF,
        "うつらうつら……\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xF,
        (
            "新品の医療機器が壊れたときのために、\x01",
            "旧式の機器のチェックをしてるんです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xF,
        (
            "ふわああ～あ……眠いけど、\x01",
            "ちゃんとやっておかないと～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7FAC")

    label("loc_7F17")


    #C0370
    ChrTalk(
        0xF,
        (
            "うつらうつら……\x01",
            "それにしても旧いものって\x01",
            "意外に頑丈にできてますよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xF,
        (
            "大型で無骨な形のものも多いし、\x01",
            "上で寝たらひんやり気持ちよさそ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FAC")

    Jump("loc_8B3E")

    label("loc_7FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_813A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_809C")

    #C0372
    ChrTalk(
        0xF,
        (
            "劣化してた部品のスペア、\x01",
            "なんとか見つかりましたよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xF,
        (
            "でも、特殊な部品だから\x01",
            "次はレミフェリアから取り寄せないと\x01",
            "手に入らないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xF,
        (
            "ふう、困っちゃいます。\x01",
            "大事に大事に使っていかないと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8135")

    label("loc_809C")


    #C0375
    ChrTalk(
        0xF,
        (
            "病院で使ってる医療機器の部品は\x01",
            "レミフェリアから取り寄せないと\x01",
            "手に入らないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xF,
        (
            "ふう、困っちゃいます。\x01",
            "大事に大事に使っていかないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8135")

    Jump("loc_8B3E")

    label("loc_813A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_838F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F9")
    TurnDirection(0xFE, 0x103, 0)

    #C0377
    ChrTalk(
        0xF,
        "あ、ティオちゃん。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xF,
        (
            "今、医療機器のメンテを\x01",
            "してるんだけど……\x01",
            "この数値、どう思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x103,
        (
            "#00200Fふむ……耐久力が規定値を\x01",
            "若干下回っていますね。\x02\x03",

            "#00203Fおそらくは稼動部の部品が\x01",
            "経年劣化しているのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xF,
        (
            "やっぱりそっかあ。\x01",
            "うーん、困ったなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#00000F（ティオもここに居る間、\x01",
            "  かなり馴染んでたみたいだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x105,
        (
            "#10402F（フフ、導力機器の分野だったら\x01",
            "  かなり役立ってたんじゃない？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_838A")

    label("loc_82F9")


    #C0383
    ChrTalk(
        0xF,
        (
            "うーん、困ったなあ。\x01",
            "セイランド社製だから\x01",
            "新品は取り寄せられないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xF,
        (
            "でも、なんとかするしかないよね。\x01",
            "とりあえずスペアを探そうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_838A")

    Jump("loc_8B3E")

    label("loc_838F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_84BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_844A")

    #C0385
    ChrTalk(
        0xF,
        (
            "えーと、あとで研究棟の\x01",
            "集中治療室に回診……と。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xF,
        (
            "ドノバンさんの\x01",
            "人工呼吸器のチェックにも\x01",
            "行かないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xF,
        (
            "ふう、一気に仕事が増えて\x01",
            "本当に忙しいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_84B8")

    label("loc_844A")


    #C0388
    ChrTalk(
        0xF,
        (
            "ふう、一気に仕事が増えて\x01",
            "本当に忙しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xF,
        (
            "研究漬けの日々に戻れるのは\x01",
            "先の話になりそうですね～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84B8")

    Jump("loc_8B3E")

    label("loc_84BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_85B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8563")

    #C0390
    ChrTalk(
        0xF,
        (
            "昨日は手術用の医療機器が\x01",
            "大活躍してくれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xF,
        (
            "日ごろからシャルールくんに\x01",
            "メンテナンスを頼んでおいて、\x01",
            "本当に良かったですよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_85AD")

    label("loc_8563")


    #C0392
    ChrTalk(
        0xF,
        (
            "研修医のみなさんは\x01",
            "優秀な子たちばっかりで、\x01",
            "私も助けられてますよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85AD")

    Jump("loc_8B3E")

    label("loc_85B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C0")

    #C0393
    ChrTalk(
        0xF,
        (
            "うつら、うつら……\x01",
            "……あっそうだっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xF,
        (
            "感光クオーツの原理を応用して\x01",
            "視覚情報を脳に送る仕組みを作れば\x01",
            "擬似的に視力の補助が可能かも……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xF,
        (
            "（カタカタカタカタカタカタ……）\x01",
            "……う～ん、やっぱりだめ。\x01",
            "これじゃ開発に何十年かかるやら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_873E")

    label("loc_86C0")


    #C0396
    ChrTalk(
        0xF,
        (
            "だめだぁ～……\x01",
            "やっぱり私にはムリなのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xF,
        (
            "……ううん、諦めちゃあダメよね。\x01",
            "シズクちゃんのためにもファイト、私！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_873E")

    Jump("loc_8B3E")

    label("loc_8743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_88AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8822")

    #C0398
    ChrTalk(
        0xF,
        (
            "シズクちゃんの手術には、\x01",
            "現代医療で最高と言える設備を\x01",
            "整えた上で臨んだんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xF,
        (
            "それが失敗してしまうなんて……\x01",
            "うう、納得がいきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xF,
        (
            "信じてくれたシズクちゃんに\x01",
            "申し訳ないです……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_88A7")

    label("loc_8822")


    #C0401
    ChrTalk(
        0xF,
        (
            "科学で人を幸せにする……\x01",
            "そのために私は医療機器科で\x01",
            "研究を続けてきたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xF,
        (
            "信じてくれたシズクちゃんに\x01",
            "申し訳ないです……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88A7")

    Jump("loc_8B3E")

    label("loc_88AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_896C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88C7")
    Call(0, 18)
    Jump("loc_8967")

    label("loc_88C7")

    OP_4B(0x10, 0xFF)

    #C0403
    ChrTalk(
        0xF,
        (
            "……うん、上出来上出来！\x01",
            "今回はうまくいったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xF,
        (
            "ふふ、今日はこの調子で\x01",
            "耐久テストまで進めちゃおっかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x10,
        "（今日も貫徹コースかな……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_8967")

    Jump("loc_8B3E")

    label("loc_896C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_897A")
    Jump("loc_8B3E")

    label("loc_897A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA5")

    #C0406
    ChrTalk(
        0xF,
        (
            "セイランド教授が\x01",
            "こちらに赴任されると聞いた時は、\x01",
            "ほんと飛び上がりそうでしたよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xF,
        (
            "職業柄、大手医療機器メーカー\x01",
            "『セイランド社』の名前は\x01",
            "毎日、目にしてましたからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xF,
        (
            "彼女は社長の親戚らしいですし……\x01",
            "うふふ、会社の裏話とかを\x01",
            "教えてもらえたらいいですねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8B3E")

    label("loc_8AA5")


    #C0409
    ChrTalk(
        0xF,
        (
            "でも、セイランド教授って\x01",
            "なんだかコワいんですよねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xF,
        (
            "セイランド社の話とか\x01",
            "色々と聞いてみたいんですけど……\x01",
            "タイミングがなかなか掴めないです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B3E")

    TalkEnd(0xFE)
    Return()

    # Function_17_7D07 end

    def Function_18_8B42(): pass

    label("Function_18_8B42")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0411
    ChrTalk(
        0xF,
        (
            "ようし、シャルール君。\x01",
            "こっちは準備オッケーよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xF,
        (
            "スイッチをいれるから、\x01",
            "導力圧の調整をお願いね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0413
    ChrTalk(
        0x10,
        (
            "了解です。\x01",
            "……今度は爆発しないと\x01",
            "いいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xF,
        (
            "しても気にしない♪\x01",
            "失敗は成功の母なんだから。\x02",
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

    #C0415
    ChrTalk(
        0x103,
        (
            "#00211F（……間違ってませんが、\x01",
            "  危なっかしいですね。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x2, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x5A, 0x0)
    Return()

    # Function_18_8B42 end

    def Function_19_8CDB(): pass

    label("Function_19_8CDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DAD")

    #C0416
    ChrTalk(
        0x10,
        (
            "主任はしばらく眠そうだったのに、\x01",
            "あの樹の出現を見てから\x01",
            "ずっとあのテンションなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x10,
        (
            "ああなったら主任は三日三晩は\x01",
            "フル稼働することになるだろう。\x01",
            "僕もついていかなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8E26")

    label("loc_8DAD")


    #C0418
    ChrTalk(
        0x10,
        (
            "帝国の内戦の事、\x01",
            "あの青白い大樹のこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x10,
        (
            "色んな心配はあるけど、\x01",
            "今は主任についていくことに\x01",
            "専念するとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E26")

    Jump("loc_9A6D")

    label("loc_8E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EF2")

    #C0420
    ChrTalk(
        0x10,
        (
            "ふむ、さすがに性能は低いけど\x01",
            "いざというときは代用がききそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x10,
        (
            "数が多いから夜通しのチェックに\x01",
            "なってしまったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x10,
        "……まあ、いつものことだからいいか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8F5B")

    label("loc_8EF2")


    #C0423
    ChrTalk(
        0x10,
        (
            "夜通しのチェックだったから、\x01",
            "アーシュラ主任も眠そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x10,
        "……まあ、いつものことだからいいか。\x02",
    )

    CloseMessageWindow()

    label("loc_8F5B")

    Jump("loc_9A6D")

    label("loc_8F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_901E")

    #C0425
    ChrTalk(
        0x10,
        (
            "ゲイリー教授も家族の心配は\x01",
            "あるだろうに、病院の仕事に\x01",
            "とても集中しているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x10,
        (
            "……僕も家族の安全を信じて、\x01",
            "今はアーシュラ主任の手伝いに\x01",
            "入れ込むことにするかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A6D")

    label("loc_901E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_91B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913B")

    #C0427
    ChrTalk(
        0x10,
        (
            "クロスベル独立の直前、\x01",
            "帝国から退去通告が来ていたけど\x01",
            "僕はここに残る事にしたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x10,
        (
            "まだまだ学ばなきゃいけない\x01",
            "ことがあるのに、故郷になんて\x01",
            "帰ることはできないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x10,
        (
            "……でも、帝国で起こった\x01",
            "内戦の事は少し心配だな。\x01",
            "家族が無事だといいけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_91B1")

    label("loc_913B")


    #C0430
    ChrTalk(
        0x10,
        (
            "クロスベルに残った事自体に\x01",
            "今さら後悔はないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x10,
        (
            "……でも、帝国の内戦は心配だな。\x01",
            "家族が無事だといいけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91B1")

    Jump("loc_9A6D")

    label("loc_91B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_928F")

    #C0432
    ChrTalk(
        0x10,
        (
            "今回の襲撃事件は、\x01",
            "帝国政府の陰謀だと\x01",
            "囁かれているそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x10,
        (
            "沢山の人が病院に運び込まれた\x01",
            "あの事件が帝国の仕業……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x10,
        (
            "故郷のことは悪く言いたくないけど、\x01",
            "もし本当なら軽蔑するよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9303")

    label("loc_928F")


    #C0435
    ChrTalk(
        0x10,
        (
            "将来、故郷の帝国で\x01",
            "開業することが目標だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x10,
        (
            "帝国政府の陰謀がもし本当なら、\x01",
            "僕は故郷を軽蔑するよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9303")

    Jump("loc_9A6D")

    label("loc_9308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_944C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93FB")

    #C0437
    ChrTalk(
        0x10,
        (
            "医療機器は日ごろからの\x01",
            "細やかなメンテナンスが\x01",
            "欠かせないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x10,
        (
            "もし医療機器の故障で\x01",
            "患者になにかあったりしたら\x01",
            "本末転倒だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x10,
        (
            "またいつ患者が\x01",
            "運ばれてきてもいいように、\x01",
            "きちんと整備しとかないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9447")

    label("loc_93FB")


    #C0440
    ChrTalk(
        0x10,
        (
            "またいつ患者が\x01",
            "運ばれてきてもいいように、\x01",
            "きちんと整備しとかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9447")

    Jump("loc_9A6D")

    label("loc_944C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_95D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_953F")

    #C0441
    ChrTalk(
        0x10,
        (
            "主任は、シズクちゃんの手術から\x01",
            "不眠不休で何かを研究していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x10,
        (
            "どうやら、導力器を用いて\x01",
            "シズクちゃんの目を治す方法を\x01",
            "模索しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x10,
        (
            "やっぱり主任はすごいな……\x01",
            "僕はそんな事、考えもしなかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_95CB")

    label("loc_953F")


    #C0444
    ChrTalk(
        0x10,
        (
            "導力器を使って視力を回復か……\x01",
            "僕はそんな事、考えもしなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x10,
        (
            "ただ、神経科の分野も絡むからね……\x01",
            "実現は難しいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95CB")

    Jump("loc_9A6D")

    label("loc_95D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96A6")

    #C0446
    ChrTalk(
        0x10,
        (
            "あの手術に関して、教授たちは\x01",
            "みんな最善を尽くしたと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x10,
        (
            "それでも完治に至らなかったのは\x01",
            "残念と言わざるを得ないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x10,
        (
            "個人的には、あまり落ち込まないで\x01",
            "ほしいところだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_971E")

    label("loc_96A6")


    #C0449
    ChrTalk(
        0x10,
        (
            "あの手術に関して、教授たちは\x01",
            "みんな最善を尽くしたと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x10,
        (
            "個人的には、あまり落ち込まないで\x01",
            "ほしいところだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971E")

    Jump("loc_9A6D")

    label("loc_9723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_97BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_973E")
    Call(0, 18)
    Jump("loc_97BA")

    label("loc_973E")


    #C0451
    ChrTalk(
        0x10,
        (
            "アーシュラ主任は\x01",
            "どれだけ失敗してもめげないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x10,
        (
            "医療機器の研究者としての根性、\x01",
            "大いに見習うべきかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97BA")

    Jump("loc_9A6D")

    label("loc_97BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_98F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9864")

    #C0453
    ChrTalk(
        0x10,
        (
            "結局アーシュラ主任は\x01",
            "間に合わなかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x10,
        (
            "まあ、昨日も徹夜した主任が\x01",
            "視察に間に合うなんて、\x01",
            "これっぽっちも思わなかったけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98EC")

    label("loc_9864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9876")
    Call(0, 16)
    Jump("loc_98EC")

    label("loc_9876")


    #C0455
    ChrTalk(
        0x10,
        (
            "アーシュラ主任は、夜を徹して\x01",
            "研究に励むことが多いからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x10,
        (
            "今はまだ、寮の方で寝ている\x01",
            "最中なんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98EC")

    Jump("loc_9A6D")

    label("loc_98F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F5")

    #C0457
    ChrTalk(
        0x10,
        (
            "アーシュラ主任は\x01",
            "医療機器の専門家でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x10,
        (
            "以前は主任の出身地でもある\x01",
            "レマン自治州の、エプスタイン財団本部で\x01",
            "導力機器の基礎を学んでいたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x10,
        (
            "僕はそんな主任の下で、\x01",
            "様々な医療機器の研究を\x01",
            "手伝っているというわけなのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9A6D")

    label("loc_99F5")


    #C0460
    ChrTalk(
        0x10,
        (
            "医療機器は、近代医療において\x01",
            "欠かすことのできないものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x10,
        (
            "僕は、この研究こそが\x01",
            "医学の未来を拓くと信じてるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A6D")

    TalkEnd(0xFE)
    Return()

    # Function_19_8CDB end

    def Function_20_9A71(): pass

    label("Function_20_9A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9AEB")

    #C0462
    ChrTalk(
        0x11,
        "外来受付が再開して安心したゾイ。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x11,
        (
            "前にもらっとった薬が切れて\x01",
            "どうしようかと思っておったんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9AF9")
    Jump("loc_9DF3")

    label("loc_9AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9B07")
    Jump("loc_9DF3")

    label("loc_9B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9BA7")

    #C0464
    ChrTalk(
        0x11,
        (
            "うーむ、一向に呼ばれん所を見ると……\x01",
            "診察はかなり滞っておるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x11,
        (
            "あんな襲撃事件があったのだ、\x01",
            "先生たちも相当忙しいじゃろうな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9BB5")
    Jump("loc_9DF3")

    label("loc_9BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9C30")

    #C0466
    ChrTalk(
        0x11,
        "今日は朝イチで予約をしてるんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x11,
        (
            "予約には導力ネットを利用したのだが、\x01",
            "やはり便利なもんじゃのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9C3E")
    Jump("loc_9DF3")

    label("loc_9C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CE6")

    #C0468
    ChrTalk(
        0x11,
        (
            "昨日の除幕式で\x01",
            "あのオルキスタワーを\x01",
            "見上げてたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x11,
        (
            "背中の伸びが過ぎてな。\x01",
            "うっかり腰をやってしもうた。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x11,
        "おーいたたた……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9D3D")

    label("loc_9CE6")


    #C0471
    ChrTalk(
        0x11,
        (
            "オルキスタワーを見上げすぎて、\x01",
            "うっかり腰をやってしもうた。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x11,
        "おーいたたた……\x02",
    )

    CloseMessageWindow()

    label("loc_9D3D")

    Jump("loc_9DF3")

    label("loc_9D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9D50")
    Jump("loc_9DF3")

    label("loc_9D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9DF3")

    #C0473
    ChrTalk(
        0x11,
        (
            "教団事件のあと、\x01",
            "病院は迅速な調査を行って\x01",
            "その潔白を証明してくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x11,
        (
            "こうして安心して\x01",
            "通院できるようになったのは、\x01",
            "本当にありがたいことじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DF3")

    TalkEnd(0xFE)
    Return()

    # Function_20_9A71 end

    def Function_21_9DF7(): pass

    label("Function_21_9DF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E8F")

    #C0475
    ChrTalk(
        0x12,
        (
            "私たち年寄りにとって、\x01",
            "病院に行ける環境があるかは\x01",
            "とっても大事なことなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x12,
        (
            "こうして来れるようになって、\x01",
            "本当によかったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_9E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9E9D")
    Jump("loc_A148")

    label("loc_9E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9EAB")
    Jump("loc_A148")

    label("loc_9EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9F0A")

    #C0477
    ChrTalk(
        0x12,
        (
            "はあ……クロスベルは\x01",
            "本当に大丈夫なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x12,
        "不安で夜も眠れないわ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_9F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9F76")

    #C0479
    ChrTalk(
        0x12,
        (
            "列車事故だなんて……\x01",
            "本当にびっくりしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x12,
        (
            "乗客のみなさんは\x01",
            "大丈夫だったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_9F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9F84")
    Jump("loc_A148")

    label("loc_9F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A006")

    #C0481
    ChrTalk(
        0x12,
        (
            "あたしゃ、この病院には\x01",
            "しばらく通院してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x12,
        (
            "先生たちは手術も上手だし、\x01",
            "安心して通わせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_A006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A014")
    Jump("loc_A148")

    label("loc_A014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A0A5")

    #C0483
    ChrTalk(
        0x12,
        (
            "私のかかりつけのラゴー先生、\x01",
            "今日はお休みらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x12,
        (
            "セイランドという先生は\x01",
            "教授にしてはお若いけど、\x01",
            "大丈夫かしらねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_A0A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A148")

    #C0485
    ChrTalk(
        0x12,
        (
            "ヨアヒム先生があんな\x01",
            "大それた事件を起こしたなんて、\x01",
            "未だに信じられないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x12,
        (
            "ああ、怖い怖い……\x01",
            "人が何を考えているかなんて\x01",
            "分からないものだねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A148")

    TalkEnd(0xFE)
    Return()

    # Function_21_9DF7 end

    def Function_22_A14C(): pass

    label("Function_22_A14C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A221")

    #C0487
    ChrTalk(
        0x13,
        (
            "ディーター大統領が拘束される前は、\x01",
            "ちょっとした病気じゃ\x01",
            "病院に行かせてくれなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x13,
        (
            "でも、親にとって子供の病気は\x01",
            "たかが風邪だろうと一大事だ。\x01",
            "彼にはもう少し思いやりが欲しかったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A595")

    label("loc_A221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A22F")
    Jump("loc_A595")

    label("loc_A22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A23D")
    Jump("loc_A595")

    label("loc_A23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A296")

    #C0489
    ChrTalk(
        0x13,
        "ほら……静かにしてなさい。\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x13,
        (
            "他の人たちに\x01",
            "迷惑をかけちゃいかんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A595")

    label("loc_A296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A32F")

    #C0491
    ChrTalk(
        0x13,
        (
            "私たちは脱線した列車に\x01",
            "乗っていたのだが……\x01",
            "運良く軽傷で済んでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x13,
        (
            "１日で退院できて嬉しいけど、\x01",
            "あれから鉄道はどうなったのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A595")

    label("loc_A32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A33D")
    Jump("loc_A595")

    label("loc_A33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A49E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A42F")

    #C0493
    ChrTalk(
        0x13,
        (
            "この間、人間ドックで\x01",
            "甘い物を食べ過ぎてると\x01",
            "注意されてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x13,
        (
            "このままじゃ身体に悪いってんで、\x01",
            "生活習慣の見直しをしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x13,
        (
            "とはいえ、甘い物って\x01",
            "ついつい手が出ちゃうんだよね。\x01",
            "気をつけないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A499")

    label("loc_A42F")


    #C0496
    ChrTalk(
        0x13,
        (
            "甘い物って\x01",
            "ついつい手が出ちゃうんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x13,
        (
            "自分の身体のことなんだし、\x01",
            "気をつけないといけないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A499")

    Jump("loc_A595")

    label("loc_A49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A4AC")
    Jump("loc_A595")

    label("loc_A4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A58C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A525")

    #C0498
    ChrTalk(
        0x13,
        "う～ん、いい香りがするなあ。\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x13,
        (
            "こういうので患者の気持ちを\x01",
            "和らげてるんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_A587")

    label("loc_A525")


    #C0500
    ChrTalk(
        0x13,
        (
            "おふくろの付き添いで\x01",
            "病院に来てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x13,
        (
            "珍しいものも多そうだし、\x01",
            "探検でもしてみるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A587")

    Jump("loc_A595")

    label("loc_A58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A595")

    label("loc_A595")

    TalkEnd(0xFE)
    Return()

    # Function_22_A14C end

    def Function_23_A599(): pass

    label("Function_23_A599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A620")

    #C0502
    ChrTalk(
        0x14,
        (
            "ようやく病院に来れたけど、\x01",
            "すっごく混んでるわね～……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x14,
        (
            "先生たちも大変でしょうけど、\x01",
            "どうか頑張ってほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A954")

    label("loc_A620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A62E")
    Jump("loc_A954")

    label("loc_A62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A63C")
    Jump("loc_A954")

    label("loc_A63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A64A")
    Jump("loc_A954")

    label("loc_A64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A6D7")

    #C0504
    ChrTalk(
        0x14,
        (
            "それにしても、\x01",
            "恐ろしい事故でしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x14,
        (
            "突然のことで何が起こったか\x01",
            "分からないままで……\x01",
            "一体何が原因だったのでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A954")

    label("loc_A6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A76E")

    #C0506
    ChrTalk(
        0x14,
        (
            "家事をしてたら\x01",
            "腰を痛めちゃってね。\x01",
            "ほんと、歳はとりたくないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x14,
        (
            "あなた達も気をつけなさいよ。\x01",
            "３０や４０なんてすぐなんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A954")

    label("loc_A76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A77C")
    Jump("loc_A954")

    label("loc_A77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A7F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A797")
    Call(0, 24)
    Jump("loc_A7ED")

    label("loc_A797")


    #C0508
    ChrTalk(
        0x14,
        (
            "う～ん、ほんと\x01",
            "鼻水が止まらないわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x14,
        (
            "順番がくるまで\x01",
            "じっとしてなさいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7ED")

    Jump("loc_A954")

    label("loc_A7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A800")
    Jump("loc_A954")

    label("loc_A800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8D4")

    #C0510
    ChrTalk(
        0x14,
        (
            "最近は、薬の説明なんかが\x01",
            "以前よりも詳しくなったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x14,
        (
            "私たち患者が安心できるようにって\x01",
            "配慮なんだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x14,
        (
            "正直、成分だのなんだのって\x01",
            "素人にはちんぷんかんぷんよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A954")

    label("loc_A8D4")


    #C0513
    ChrTalk(
        0x14,
        (
            "最近は、薬の説明なんかが\x01",
            "以前よりも詳しくなったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x14,
        (
            "内容はちんぷんかんぷんだけど……\x01",
            "まあ安心はできるからいっか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A954")

    TalkEnd(0xFE)
    Return()

    # Function_23_A599 end

    def Function_24_A958(): pass

    label("Function_24_A958")


    #C0515
    ChrTalk(
        0x14,
        (
            "う～ん、まだお熱があるし、\x01",
            "鼻水も止まらないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x14,
        (
            "ほら、ママのハンカチで\x01",
            "チーンってしなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x18,
        "#4S……ぢーんっ！\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x14,
        "……出たわね～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Return()

    # Function_24_A958 end

    def Function_25_A9F1(): pass

    label("Function_25_A9F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AA78")

    #C0519
    ChrTalk(
        0x15,
        (
            "入院してる友達の見舞いに\x01",
            "ようやく来る事ができたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x15,
        (
            "あいつも心細かったろうし、\x01",
            "いろいろおしゃべりしたいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_AA78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_AA86")
    Jump("loc_AC16")

    label("loc_AA86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AA94")
    Jump("loc_AC16")

    label("loc_AA94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AB0E")

    #C0521
    ChrTalk(
        0x15,
        (
            "俺のダチも、\x01",
            "襲撃事件に巻き込まれちまって\x01",
            "入院してるんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x15,
        "早く治ってくれるといいんだけどな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_AB0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB1C")
    Jump("loc_AC16")

    label("loc_AB1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AB2A")
    Jump("loc_AC16")

    label("loc_AB2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_ABA4")

    #C0523
    ChrTalk(
        0x15,
        (
            "初診は後回しなんだってさ。\x01",
            "順番が来るまでしばらく\x01",
            "かかりそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x15,
        "あー、病院ってかったるいなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_ABA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_ABFF")

    #C0525
    ChrTalk(
        0x15,
        "ぐぐぐ、腹が痛い……\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x15,
        (
            "看護師さんの事でも考えて\x01",
            "気を紛らすしかっ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_ABFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AC0D")
    Jump("loc_AC16")

    label("loc_AC0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AC16")

    label("loc_AC16")

    TalkEnd(0xFE)
    Return()

    # Function_25_A9F1 end

    def Function_26_AC1A(): pass

    label("Function_26_AC1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ACAB")

    #C0527
    ChrTalk(
        0x16,
        "今日退院するお母さんを迎えに来たのよ。\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x16,
        (
            "しばらく病院から\x01",
            "出られなかったみたいだし、\x01",
            "はやく家に連れて帰ってあげたいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF31")

    label("loc_ACAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ACB9")
    Jump("loc_AF31")

    label("loc_ACB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_ACC7")
    Jump("loc_AF31")

    label("loc_ACC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ACD5")
    Jump("loc_AF31")

    label("loc_ACD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AE26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD7F")

    #C0529
    ChrTalk(
        0x16,
        (
            "街で噂を聞いたんだけど……\x01",
            "列車事故のとき、得体の知れない\x01",
            "巨大な化物が現れたそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x16,
        (
            "もしかして、それが\x01",
            "事故の原因だったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_AE21")

    label("loc_AD7F")


    #C0531
    ChrTalk(
        0x16,
        (
            "街で噂を聞いたんだけど……\x01",
            "列車事故のとき、得体の知れない\x01",
            "巨大な化物が現れたそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x16,
        (
            "……そんなものが出てきたら\x01",
            "私たち一般人には\x01",
            "対処しようがないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE21")

    Jump("loc_AF31")

    label("loc_AE26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AE34")
    Jump("loc_AF31")

    label("loc_AE34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AEC7")

    #C0533
    ChrTalk(
        0x16,
        (
            "診察室の前で、なんだか\x01",
            "先生たちが喧嘩してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x16,
        (
            "よく見たら病院の人たちも\x01",
            "なんだか暗い感じだし……\x01",
            "何かあったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF31")

    label("loc_AEC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AED5")
    Jump("loc_AF31")

    label("loc_AED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AF28")

    #C0535
    ChrTalk(
        0x16,
        "よしよし、静かにね？\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x16,
        (
            "お姉ちゃんが後ろで\x01",
            "見ててあげるから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF31")

    label("loc_AF28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AF31")

    label("loc_AF31")

    TalkEnd(0xFE)
    Return()

    # Function_26_AC1A end

    def Function_27_AF35(): pass

    label("Function_27_AF35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AF6B")

    #C0537
    ChrTalk(
        0x17,
        (
            "待ってるの、\x01",
            "飽きちゃったよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A1")

    label("loc_AF6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_AF79")
    Jump("loc_B0A1")

    label("loc_AF79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AF87")
    Jump("loc_B0A1")

    label("loc_AF87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AFD5")

    #C0538
    ChrTalk(
        0x17,
        "あ～あ、つまんないな～。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x17,
        "早く順番がくればいいのに～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0A1")

    label("loc_AFD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AFE3")
    Jump("loc_B0A1")

    label("loc_AFE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AFF1")
    Jump("loc_B0A1")

    label("loc_AFF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AFFF")
    Jump("loc_B0A1")

    label("loc_AFFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B00D")
    Jump("loc_B0A1")

    label("loc_B00D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B05B")

    #C0540
    ChrTalk(
        0x17,
        "うわ～ん、お注射怖いよ～！！\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x17,
        "ぼく、おうちかえる～～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0A1")

    label("loc_B05B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B0A1")

    #C0542
    ChrTalk(
        0x17,
        (
            "ふあ～……\x01",
            "待ってるの飽きちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x17,
        "順番まだ～？\x02",
    )

    CloseMessageWindow()

    label("loc_B0A1")

    TalkEnd(0xFE)
    Return()

    # Function_27_AF35 end

    def Function_28_B0A5(): pass

    label("Function_28_B0A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B0E7")

    #C0544
    ChrTalk(
        0x18,
        (
            "けほ、けほ……\x01",
            "ニガいお薬だったらヤダな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1E4")

    label("loc_B0E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B0F5")
    Jump("loc_B1E4")

    label("loc_B0F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B103")
    Jump("loc_B1E4")

    label("loc_B103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B111")
    Jump("loc_B1E4")

    label("loc_B111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B11F")
    Jump("loc_B1E4")

    label("loc_B11F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B17A")

    #C0545
    ChrTalk(
        0x18,
        (
            "今日はね、ひとりで\x01",
            "バスに乗ってきたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x18,
        "えへへ、えらいでしょ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1E4")

    label("loc_B17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B188")
    Jump("loc_B1E4")

    label("loc_B188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B1CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A3")
    Call(0, 24)
    Jump("loc_B1C8")

    label("loc_B1A3")


    #C0547
    ChrTalk(
        0x18,
        (
            "ずび……\x01",
            "ハナがとまんにゃい……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1C8")

    Jump("loc_B1E4")

    label("loc_B1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B1DB")
    Jump("loc_B1E4")

    label("loc_B1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B1E4")

    label("loc_B1E4")

    TalkEnd(0xFE)
    Return()

    # Function_28_B0A5 end

    def Function_29_B1E8(): pass

    label("Function_29_B1E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B265")

    #C0548
    ChrTalk(
        0x19,
        (
            "街が……\x01",
            "街が燃えていたんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x19,
        (
            "恐ろしい光景じゃった……\x01",
            "まるで数十年前の紛争を\x01",
            "思い出すようじゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B265")

    TalkEnd(0xFE)
    Return()

    # Function_29_B1E8 end

    def Function_30_B269(): pass

    label("Function_30_B269")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B2B2")

    #C0550
    ChrTalk(
        0x1A,
        "う、うう……\x02",
    )

    CloseMessageWindow()

    #A0551
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うなされてしまっているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B2B2")

    TalkEnd(0xFE)
    Return()

    # Function_30_B269 end

    def Function_31_B2B6(): pass

    label("Function_31_B2B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B324")

    #C0552
    ChrTalk(
        0x1B,
        (
            "うう……あの襲撃事件で\x01",
            "両足が骨折しちまってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x1B,
        (
            "ちくしょう……\x01",
            "なんで俺がこんな目に……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B324")

    TalkEnd(0xFE)
    Return()

    # Function_31_B2B6 end

    def Function_32_B328(): pass

    label("Function_32_B328")

    TalkBegin(0xFE)

    #C0554
    ChrTalk(
        0x1C,
        (
            "それじゃあ、\x01",
            "そっちの共和国の患者さんの\x01",
            "ご家族へ連絡をお願い。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x1C,
        (
            "私はセイランド教授に\x01",
            "カルテを届けてくるわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_B328 end

    def Function_33_B3A4(): pass

    label("Function_33_B3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3D3")
    Call(0, 48)
    Return()

    label("loc_B3D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B57C")

    #C0556
    ChrTalk(
        0x1D,
        (
            "風の噂で聞いたのだが……\x01",
            "シズク・マクレインの目が\x01",
            "完治していたそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x1D,
        (
            "元担当医としては\x01",
            "喜ぶべきなのかもしれないが……\x01",
            "複雑な気分でもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x1D,
        (
            "今回の一連の事件を見る限り、\x01",
            "彼女の目にも何らかの不可思議な力が\x01",
            "使われたと見ていいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x1D,
        (
            "近代医療に携わる者として、\x01",
            "そのようなものに遅れを取る事は\x01",
            "ただ、悔しいかぎりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x1D,
        (
            "……すまない、忘れてくれ。\x01",
            "下らない意地のようなものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B632")

    label("loc_B57C")


    #C0561
    ChrTalk(
        0x1D,
        (
            "……すまない、忘れてくれ。\x01",
            "近代医療に携わる者としての、\x01",
            "下らない意地のようなものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x1D,
        (
            "シズク・マクレインの目が\x01",
            "治ったこと自体は、喜ばしいことだ。\x01",
            "素直に祝福させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B632")

    Jump("loc_BD9E")

    label("loc_B637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B645")
    Jump("loc_BD9E")

    label("loc_B645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_B653")
    Jump("loc_BD9E")

    label("loc_B653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B661")
    Jump("loc_BD9E")

    label("loc_B661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B8CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B68D")
    Call(0, 35)
    Jump("loc_B8C0")

    label("loc_B68D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B79D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B734")

    #C0563
    ChrTalk(
        0x1D,
        (
            "ひとまずはこれで、\x01",
            "襲撃事件の患者たちに\x01",
            "十分な対応がとれるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x1D,
        (
            "君たちの取り返した医療物資は\x01",
            "有効活用させてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B798")

    label("loc_B734")


    #C0565
    ChrTalk(
        0x1D,
        (
            "さて……\x01",
            "そろそろ次の患者の手術だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x1D,
        (
            "君たちの取り返した医療物資は\x01",
            "有効活用させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B798")

    Jump("loc_B8C0")

    label("loc_B79D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_B833")

    #C0567
    ChrTalk(
        0x1D,
        (
            "この状況で医療物資が\x01",
            "盗まれてしまったことは、\x01",
            "確かに痛いが……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x1D,
        (
            "弱音を吐いてはいられん。\x01",
            "なんとか工夫するしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8C0")

    label("loc_B833")


    #C0569
    ChrTalk(
        0x1D,
        (
            "……医療物資が足りていない\x01",
            "この状況は如何ともしがたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x1D,
        (
            "もしもの時は、事情を説明して\x01",
            "代わりの物資を送ってもらうしか\x01",
            "ないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8C0")

    Jump("loc_B8C5")

    label("loc_B8C5")

    Jump("loc_BD9E")

    label("loc_B8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B97E")
    OP_4B(0xC, 0xFF)

    #C0571
    ChrTalk(
        0x1D,
        (
            "リットン、\x01",
            "次は患者たちの回診に向かうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x1D,
        (
            "今回の事故は患者が多い。\x01",
            "手術が終わったからと言って\x01",
            "気を抜くんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xC,
        "は、はいっ！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 6)
    Jump("loc_B9B3")

    label("loc_B97E")


    #C0574
    ChrTalk(
        0x1D,
        (
            "今回の事故は患者が多い。\x01",
            "気を抜くんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9B3")

    Jump("loc_BD9E")

    label("loc_B9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B9C6")
    Jump("loc_BD9E")

    label("loc_B9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B9D4")
    Jump("loc_BD9E")

    label("loc_B9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B9E2")
    Jump("loc_BD9E")

    label("loc_B9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BD95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB25")

    #C0575
    ChrTalk(
        0x1D,
        (
            "アルバート……\x01",
            "視察が終わった後に\x01",
            "ここに来るつもりらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x1D,
        (
            "本会議を明日に控える今、\x01",
            "わざわざ視察に来る\x01",
            "必要性は低いだろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x1D,
        (
            "やれやれ……\x01",
            "あの男も相変わらずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x101,
        (
            "#00006F（ア、アルバートって……\x01",
            "  呼び捨てにしてるのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x109,
        "#10100F（知り合いか何かでしょうか……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_BB8E")

    label("loc_BB25")


    #C0580
    ChrTalk(
        0x1D,
        (
            "アルバートは、\x01",
            "視察が終わった後に\x01",
            "ここに来るつもりらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x1D,
        (
            "やれやれ……\x01",
            "あの男も相変わらずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BD90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCD6")

    #C0582
    ChrTalk(
        0x1D,
        (
            "『リボテン中毒』は外国産の\x01",
            "キノコが原因である以上、それ自体が\x01",
            "クロスベルでは発生しづらい症例だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x1D,
        (
            "私も色々と可能性は考えたが、\x01",
            "一言で言い当てたアルバートの知識は\x01",
            "やはり相当に深いと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x1D,
        (
            "今回は借りを作ってしまったが……\x01",
            "仮にもレミフェリアを束ねる者なのだ、\x01",
            "そうでなくてはな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_BD90")

    label("loc_BCD6")


    #C0585
    ChrTalk(
        0x1D,
        (
            "『リボテン中毒』を\x01",
            "一言で言い当てたアルバートの知識は\x01",
            "やはり相当に深いと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x1D,
        (
            "今回は借りを作ってしまったが……\x01",
            "仮にもレミフェリアを束ねる者なのだ、\x01",
            "そうでなくてはな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD90")

    Jump("loc_BD9E")

    label("loc_BD95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD9E")

    label("loc_BD9E")

    TalkEnd(0xFE)
    Return()

    # Function_33_B3A4 end

    def Function_34_BDA2(): pass

    label("Function_34_BDA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDD1")
    Call(0, 35)
    Jump("loc_BE52")

    label("loc_BDD1")


    #C0587
    ChrTalk(
        0x1E,
        (
            "空港に届いた医療物資を\x01",
            "『ライムス運送』さんが\x01",
            "運んでくれる手筈なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x1E,
        (
            "うーん、何か手違いでも\x01",
            "あったんですかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE52")

    Jump("loc_BE57")

    label("loc_BE57")

    TalkEnd(0xFE)
    Return()

    # Function_34_BDA2 end

    def Function_35_BE5B(): pass

    label("Function_35_BE5B")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0589
    ChrTalk(
        0x1D,
        (
            "……レミフェリアからの\x01",
            "医療物資がまだ届かない、だと？\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x1E,
        (
            "ええ、荷物の到着予定時間は\x01",
            "とっくに過ぎてるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x9,
        (
            "何かトラブルでも\x01",
            "あったんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x1D,
        (
            "ふむ、レミフェリアか空港の方で\x01",
            "何かあったのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x10)
    SetScenarioFlags(0x18F, 0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_35_BE5B end

    def Function_36_BF64(): pass

    label("Function_36_BF64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF79")
    Call(0, 37)
    Jump("loc_BFF9")

    label("loc_BF79")


    #C0593
    ChrTalk(
        0x1F,
        (
            "正直何を言われるかと思い、\x01",
            "イヤイヤの来院じゃったが……\x01",
            "まさかこんな結果になるとはの。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x1F,
        "これも全てアミサのおかげじゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_BFF9")

    TalkEnd(0xFE)
    Return()

    # Function_36_BF64 end

    def Function_37_BFFD(): pass

    label("Function_37_BFFD")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)

    #C0595
    ChrTalk(
        0xC,
        "ふむ、これは驚いたな……\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xC,
        (
            "クワインさん、\x01",
            "以前入院していた頃よりも\x01",
            "症状が良くなっていますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0597
    ChrTalk(
        0x1F,
        "そ、それは本当かの！？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xC,
        (
            "ええ、それでも勿論\x01",
            "経過を見る必要はありまけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xC,
        (
            "ただ、少なくとも\x01",
            "入院の必要性はなさそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0600
    ChrTalk(
        0x20,
        "良かったね、おじいちゃん！\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x20,
        (
            "お身体、良くなったんだって！\x01",
            "それに入院しなくて大丈夫だって！\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x1F,
        "あ、ああ……そうじゃな。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    ClearChrFlags(0x20, 0x10)
    SetScenarioFlags(0x2, 4)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_37_BFFD end

    def Function_38_C1DC(): pass

    label("Function_38_C1DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1FA")
    Call(0, 37)
    Jump("loc_C26B")

    label("loc_C1FA")


    #C0603
    ChrTalk(
        0x20,
        (
            "本当に、本当に良かったね、\x01",
            "おじいちゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x20,
        (
            "ふふふ、やっぱり\x01",
            "ちゃんとお薬を飲んでもらって\x01",
            "正解だったな♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C26B")

    Jump("loc_C2C9")

    label("loc_C270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C2C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C28B")
    Call(0, 39)
    Jump("loc_C2C9")

    label("loc_C28B")


    #C0605
    ChrTalk(
        0x20,
        (
            "今日もこれから\x01",
            "おじいちゃんの所に\x01",
            "お薬を持っていくんだ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2C9")

    TalkEnd(0xFE)
    Return()

    # Function_38_C1DC end

    def Function_39_C2CD(): pass

    label("Function_39_C2CD")

    OP_4B(0xC, 0xFF)

    #C0606
    ChrTalk(
        0xC,
        (
            "それじゃ、アミサちゃん。\x01",
            "いつものお薬包んでおいたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xC,
        "気を付けて持って行くんだよ。\x02",
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x20,
        (
            "うんっ。\x01",
            "いつもありがとう、先生。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x2, 3)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_39_C2CD end

    def Function_40_C369(): pass

    label("Function_40_C369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C398")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C398")
    Call(0, 48)
    Return()

    label("loc_C398")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_40_C369 end

    def Function_41_C39F(): pass

    label("Function_41_C39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3BE")
    Call(0, 48)
    Return()

    label("loc_C3BE")

    TalkBegin(0xFE)

    #C0609
    ChrTalk(
        0x22,
        (
            "ナデリア茸を\x01",
            "持って来るのを待っているよ。\x02\x03",

            "君たちとアリオス君なら\x01",
            "きっとやり遂げてくれるだろう。\x01",
            "どうか、よろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_C39F end

    def Function_42_C442(): pass

    label("Function_42_C442")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C59E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C516")

    #C0610
    ChrTalk(
        0x24,
        (
            "外国のお土産に\x01",
            "持って帰ってきたキノコ、\x01",
            "すごく美味しかったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x24,
        (
            "まさか毒キノコだったなんて、\x01",
            "うかつでしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x24,
        (
            "今後はもう少し、\x01",
            "気をつけないといけませんね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C599")

    label("loc_C516")


    #C0613
    ChrTalk(
        0x24,
        (
            "外国のお土産に\x01",
            "持って帰ってきたキノコ、\x01",
            "すごく美味しかったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x24,
        (
            "今後はもう少し、\x01",
            "気をつけないといけませんね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C599")

    Jump("loc_C626")

    label("loc_C59E")


    #C0615
    ChrTalk(
        0x24,
        (
            "う、うう……\x01",
            "なんだか腹痛がヒドくなってきた……\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x24,
        (
            "やっぱり、飛行船で食べた\x01",
            "アレが良くなかったのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x24,
        "うぐぐ………………\x02",
    )

    CloseMessageWindow()

    label("loc_C626")

    TalkEnd(0xFE)
    Return()

    # Function_42_C442 end

    def Function_43_C62A(): pass

    label("Function_43_C62A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_43_C62A end

    def Function_44_C631(): pass

    label("Function_44_C631")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C833")

    #C0618
    ChrTalk(
        0xFE,
        (
            "規制で病院に行けていなかった\x01",
            "患者たちの搬送を手伝ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "やっぱりかなりの数がいるから、\x01",
            "今日中にもう何往復かは\x01",
            "しなきゃいけないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x101,
        "#00005Fかなり大変そうですね……\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x103,
        "#00203Fどうか、無理をしすぎないで下さい。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0622
    ChrTalk(
        0xFE,
        (
            "ああんっ、ティオちゃんから\x01",
            "そんな言葉がもらえるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        (
            "いつもひんやりな反応なのに、\x01",
            "これが噂のクーデレってやつかしら！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0624
    ChrTalk(
        0x103,
        (
            "#00211F（……だんだんロバーツ主任と\x01",
            "  同類に見えてきました。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 2)
    Jump("loc_C90C")

    label("loc_C833")


    #C0625
    ChrTalk(
        0xFE,
        (
            "よ～し……ティオちゃんから\x01",
            "応援してもらえたことだし、\x01",
            "元気百倍、勇気りんりんよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "ティオちゃん、全てが終わったら\x01",
            "きゅっとハグハグさせてね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x103,
        (
            "#00211F（……全てが終わっても、\x01",
            "  安心はできなさそうですね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C90C")

    TalkEnd(0xFE)
    Return()

    # Function_44_C631 end

    def Function_45_C910(): pass

    label("Function_45_C910")

    Sound(160, 0, 100, 0)
    Return()

    # Function_45_C910 end

    def Function_46_C917(): pass

    label("Function_46_C917")

    EventBegin(0x0)
    Fade(500)
    OP_68(15440, 600, 7240, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x109, 14410, 0, 6710, 90)
    SetChrPos(0x101, 12500, 0, 6000, 90)
    SetChrPos(0x102, 12750, 0, 7400, 90)
    SetChrPos(0x104, 11750, 0, 7950, 90)
    SetChrPos(0x105, 11400, 0, 6600, 90)
    SetChrPos(0x103, 11500, 0, 5500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0628
    ChrTalk(
        0x8,
        (
            "#11Pあら、ノエルさん。\x01",
            "それに支援課の皆さん……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x8,
        (
            "#11Pフランさんのお見舞いに\x01",
            "いらっしゃったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x109,
        "#10100F#6Pはい、今、大丈夫ですか？\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x8,
        "#11Pええ、もちろんですよ。\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x8,
        (
            "#11P……でも良かったですね。\x01",
            "妹さんの意識が戻られて。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x109,
        (
            "#10104F#6P……はい。\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CAFC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CAFC)
    WaitChrThread(0x109, 3)
    Sleep(150)

    #C0634
    ChrTalk(
        0x109,
        (
            "#10102F#11P行きましょう。\x01",
            "３階の３０１号室です。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        "#00002F#6Pああ、お邪魔させてもらうよ。\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x102,
        "#00104F#6P失礼します、セラさん。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 14000, 0, 6500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x180, 6)
    OP_29(0xAC, 0x1, 0x3)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x0, 0x0, 0x39)
    EventEnd(0x5)
    Return()

    # Function_46_C917 end

    def Function_47_CBE8(): pass

    label("Function_47_CBE8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x3C)
    SetChrPos(0x8, 20770, 0, 9100, 45)
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(15920, 900, 7500, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27430, 0)
    SetChrChipByIndex(0x26, 0x3C)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 0, 8550, 90)
    SetChrPos(0x101, 13910, 0, 6710, 45)
    SetChrPos(0x102, 13790, 0, 5540, 45)
    SetChrPos(0x104, 13100, 0, 4120, 45)
    SetChrPos(0x109, 12280, 0, 6290, 45)
    SetChrPos(0x105, 12230, 0, 5090, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24940, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0637
    ChrTalk(
        0x8,
        "……はい……はい、そうです。\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x8,
        (
            "……それでは\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_68(14190, 1000, 7310, 3000)
    MoveCamera(41, 21, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(20470, 3000)
    OP_95(0x8, 17210, 0, 7430, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x109, 0x5A, 0x0)
    OP_93(0x105, 0x5A, 0x0)
    OP_93(0x26, 0x87, 0x0)
    OP_0D()
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    #C0639
    ChrTalk(
        0x8,
        (
            "セイランド教授にも\x01",
            "確認がとれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "すぐに、研究棟の部屋に\x01",
            "来るようにとのことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x26,
        "#01309Fありがとう、セラさん。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x101,
        "#6P#00000F助かります。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x101, 500)

    #C0643
    ChrTalk(
        0x26,
        (
            "#01300F……それじゃあみんな。\x01",
            "休憩もそろそろ終わるし、\x01",
            "私はこれで失礼するわね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CEAA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEAA)
    Sleep(50)

    def lambda_CEBA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CEBA)
    Sleep(50)

    def lambda_CECA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CECA)
    Sleep(50)

    def lambda_CEDA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CEDA)
    Sleep(50)

    def lambda_CEEA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CEEA)
    WaitChrThread(0x105, 2)

    #C0644
    ChrTalk(
        0x101,
        "#12P#00000Fああ、色々ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x109,
        "#6P#10102Fお世話になりました。\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x26,
        (
            "#01300Fううん、どういたしまして。\x02\x03",

            "#01309Fそれじゃ、これからも\x01",
            "色々と大変だと思うけど……\x01",
            "がんばってね、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        "#12P#00009Fああ、そっちもね。\x02",
    )

    CloseMessageWindow()

    def lambda_CFDF():
        OP_95(0xFE, 12030, 0, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_CFDF)
    Sleep(50)

    def lambda_CFFC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CFFC)
    Sleep(50)

    def lambda_D00C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D00C)
    WaitChrThread(0x26, 1)

    def lambda_D01D():
        OP_97(0xFE, 0x0, 0x564, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D01D)
    Sleep(1000)

    def lambda_D03A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D03A)
    WaitChrThread(0x26, 2)
    SetChrFlags(0x26, 0x80)
    OP_0D()
    OP_68(13870, 1000, 6330, 3000)
    OP_6F(0x1)

    #C0648
    ChrTalk(
        0x104,
        (
            "#12P#00310F……く～っ、常々\x01",
            "憎たらしいやつだなお前は！\x02\x03",

            "#00309F『がんばってね、ロイド㈱』\x01",
            "……だってよ、だってよ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    #C0649
    ChrTalk(
        0x101,
        (
            "#00006Fべ、別にハートマークは\x01",
            "ついてなかっただろ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D124():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D124)
    Sleep(100)

    def lambda_D134():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D134)
    Sleep(500)

    #C0650
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、そんなことを言って\x01",
            "少し残念なんじゃないのかい？\x02\x03",

            "噂の熱～い抱擁#4Rハ　グ#も\x01",
            "今回は見られなかったみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x102,
        "#00105Fああ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x109,
        "#10105Fえっ、そんなことをっ……！？\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x101,
        (
            "#00003Fああ、もう！\x01",
            "いいからさっさと\x01",
            "教授のところに行こう！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x3E8)
    Sleep(500)

    #C0654
    ChrTalk(
        0x101,
        (
            "#12P#00001F研究棟は病院の屋上から、\x01",
            "薬学研究室は研究棟の４階！\x01",
            "さあ、行くぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x104,
        (
            "#12P#00309F（やれやれ、勢いで\x01",
            "  ごまかしちまってまあ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x105,
        (
            "#6P#10302F（ふふ、これだから\x01",
            "  からかい甲斐があるよね。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    #C0657
    ChrTalk(
        0x101,
        "#00003F……聞こえてるぞ、そこっ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x3C)
    SetScenarioFlags(0x152, 1)
    OP_29(0x70, 0x1, 0x0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x80)
    BeginChrThread(0xA, 0, 0, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13200, 0, 5700, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_47_CBE8 end

    def Function_48_D3A9(): pass

    label("Function_48_D3A9")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x22, 0xB4, 0x0)
    OP_93(0x21, 0x87, 0x0)
    OP_4B(0x22, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(50330, 1000, 58210, 0)
    MoveCamera(69, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 50460, 0, 56980, 315)
    SetChrPos(0x102, 49370, 0, 56120, 0)
    SetChrPos(0x109, 50910, 0, 55870, 0)
    SetChrPos(0x105, 51820, 0, 56620, 315)
    SetChrPos(0x104, 52140, 0, 55580, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xC, 49800, 0, 51590, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x1D, 0x1)

    #C0658
    ChrTalk(
        0x1D,
        "む……客人のようだな。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCDA")

    #C0659
    ChrTalk(
        0x22,
        "おや、君たちは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0660
    ChrTalk(
        0x101,
        (
            "#00005Fレ、レミフェリア公国の\x01",
            "アルバート大公閣下……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x109,
        "#10105Fそれに、アリオスさんまで……\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x21,
        (
            "#01405Fふむ、奇遇だな。\x02\x03",

            "#01400F閣下、彼らが以前話した\x01",
            "『特務支援課』の者たちです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0663
    ChrTalk(
        0x22,
        "おお、そうだったのか。\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x22,
        "……はじめまして、支援課の諸君。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x22,
        (
            "私の名はアルバート・フォン・バルトロメウス。\x01",
            "レミフェリアの国家元首を務めている者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x22,
        (
            "これからもクロスベルの為、\x01",
            "一所懸命に頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        "#00000Fよ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x22,
        (
            "フフ、君たちのことは、\x01",
            "アリオス君から聞いていてね。\x01",
            "是非お会いしたいと思っていたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x22,
        "それと、エリィ君の方は久しぶりだね。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、お久しぶりです。\x01",
            "大公閣下もお元気そうで……\x02\x03",

            "#00103Fでも、ちょうど病院に\x01",
            "お見えになっていたとは\x01",
            "知りませんでした。\x02\x03",

            "#00105F今日は視察にいらっしゃって\x01",
            "いたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x22,
        (
            "うむ、レミフェリア公国はこの病院の\x01",
            "スポンサーの１つだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x22,
        (
            "それに、赴任したセイランド君の様子も\x01",
            "是非見ておきたかったし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0673
    ChrTalk(
        0x21,
        (
            "#01403Fそれに関しては、個人的には\x01",
            "もう少し護衛をつけさせて\x01",
            "頂きたかったところです。\x02\x03",

            "#01400F私とリムジンの運転士だけ、\x01",
            "というのはいかがなものかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x22,
        (
            "フフ、アリオス君のことを\x01",
            "信用しているからこそだと\x01",
            "思ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x22,
        (
            "それに、私の視察くらいで\x01",
            "ぞろぞろ護衛を連れて、病院の業務を\x01",
            "妨げるわけにもいかないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    #C0676
    ChrTalk(
        0x1D,
        "まったく、わざわざご苦労な事だ。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x1D,
        (
            "視察も別に今回来なくては\x01",
            "いけないというものでもないのだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x1D,
        (
            "今回くらいは通商会議に\x01",
            "集中していればよかったものを。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x1D,
        (
            "国賓である自覚を\x01",
            "もう少し持つべきではないのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0680
    ChrTalk(
        0x22,
        (
            "はっはっは、セイランド君は\x01",
            "相変わらず手厳しいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0681
    ChrTalk(
        0x101,
        (
            "#00003F（アルバート大公……\x01",
            "  随分交友が広い人みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x109,
        (
            "#10100F（ええ、エリィさんやアリオスさん……\x01",
            "  それにセイランド教授とも\x01",
            "  以前から知り合いみたいですし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x105,
        (
            "#10300F（フフ、一国の首脳相手でも\x01",
            "  あんな口ぶりなんだから恐れ入るよ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E073")

    label("loc_DCDA")


    #C0684
    ChrTalk(
        0x22,
        "おや、君たちは特務支援課の。\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#00000Fアルバート大公閣下、\x01",
            "それにアリオスさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        (
            "#00100Fシズクちゃんのお見舞いのあと、\x01",
            "こちらに来ていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x21,
        (
            "#01400Fああ、今はセイランド教授に\x01",
            "挨拶に来ていたところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x22,
        (
            "ふふ、赴任したセイランド君の様子を\x01",
            "是非見ておきたかったからね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    #C0689
    ChrTalk(
        0x1D,
        "まったく、わざわざご苦労な事だ。\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1D,
        (
            "視察も別に今回来なくては\x01",
            "いけないというものでもないのだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x1D,
        (
            "今回くらいは通商会議に\x01",
            "集中していればよかったものを。\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x1D,
        (
            "国賓である自覚を\x01",
            "もう少し持つべきではないのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0693
    ChrTalk(
        0x22,
        (
            "はっはっは、セイランド君は\x01",
            "相変わらず手厳しいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0694
    ChrTalk(
        0x101,
        (
            "#00003F（アルバート大公……\x01",
            "  本当に交友が広いんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x109,
        (
            "#10100F（ええ、セイランド教授とも\x01",
            "  知り合いみたいですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x105,
        (
            "#10300F（フフ、一国の首脳相手でも\x01",
            "  あんな口ぶりなんだから恐れ入るよ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E073")

    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(300, -1, -1, -1)
    SetChrName("声")

    #A0697
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5Sせ、先生っ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1D, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(51580, 1000, 57460, 3000)
    SetChrSubChip(0x1D, 0x1)

    def lambda_E178():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E178)
    Sleep(50)

    def lambda_E188():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E188)
    Sleep(50)

    def lambda_E198():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E198)
    Sleep(50)

    def lambda_E1A8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E1A8)
    Sleep(50)

    def lambda_E1B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E1B8)
    Sleep(50)

    def lambda_E1C8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E1C8)
    Sleep(50)

    def lambda_E1D8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_E1D8)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 54100, 0, 55910, 4000, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_6F(0x1)

    #C0698
    ChrTalk(
        0x1D,
        "どうした、騒々しいぞリットン。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0699
    ChrTalk(
        0xC,
        "きゅ、急患です！\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0xC,
        (
            "ついさっき、ロビーにいた患者が\x01",
            "倒れてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0xC,
        "意識不明の重体なんです！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0702
    ChrTalk(
        0x22,
        "ふむ、それはいかんな。\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x22,
        (
            "君、さっそくここに\x01",
            "運んできたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xC,
        "は、はいっ！\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_68(50330, 1000, 58210, 3000)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 49800, 0, 51590, 4000, 0x0)
    OP_95(0xC, 49560, 0, 49150, 4000, 0x0)
    OP_6F(0x1)
    SetChrSubChip(0x1D, 0x1)

    def lambda_E444():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E444)
    Sleep(50)

    def lambda_E454():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E454)
    Sleep(50)

    def lambda_E464():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E464)
    Sleep(50)

    def lambda_E474():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E474)
    Sleep(50)

    def lambda_E484():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E484)
    Sleep(50)

    def lambda_E494():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_E494)
    Sleep(300)

    #C0705
    ChrTalk(
        0x101,
        "#00000Fアリオスさん、俺たちは……\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x21,
        (
            "#01400Fああ、診察の邪魔になりそうだし\x01",
            "離れていた方がいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x22,
        "いや、同席してくれたまえ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0708
    ChrTalk(
        0x22,
        (
            "もしかしたら、君たちも\x01",
            "役に立つことがあるかもしれん。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 59700, 0, 58450, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 58750, 0, 58400, 0)
    SetChrChipByIndex(0x24, 0x22)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 0)
    OP_68(58990, 1000, 59760, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25400, 0)
    SetChrPos(0x22, 56950, 0, 60000, 90)
    SetChrPos(0x21, 56050, 0, 58600, 90)
    SetChrPos(0x101, 56950, 0, 56650, 0)
    SetChrPos(0x102, 57950, 0, 56650, 0)
    SetChrPos(0x109, 58950, 0, 56650, 0)
    SetChrPos(0x104, 55950, 0, 57500, 45)
    SetChrPos(0x105, 55700, 0, 56350, 45)
    OP_4B(0x1D, 0xFF)
    OP_4B(0xC, 0xFF)
    SetCameraDistance(21940, 3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0709
    ChrTalk(
        0x24,
        "………う……ぐ…………………\x02",
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x1D,
        "……ふむ……\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x101,
        "#00005Fどうですか？　容態は……\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x104,
        "#00301F随分苦しそうだが……\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x1D,
        "……あまり思わしくないな。\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x1D,
        (
            "色々と検査をしてみたが、\x01",
            "内科的な症状には間違いないのに\x01",
            "原因が何も検出されなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x1D,
        (
            "病名を突き止めれば\x01",
            "薬を調合することができるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1D,
        (
            "それまで患者が持つかどうか、\x01",
            "現時点ではかなり厳しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x102,
        "#00105Fそ、そんなに重体なんですか……\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xC,
        "い、一体どうすれば……！\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x22,
        (
            "──ふむ。\x01",
            "ちょっといいかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E916():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E916)
    Sleep(50)

    def lambda_E926():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E926)
    Sleep(50)

    def lambda_E936():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E936)
    Sleep(50)

    def lambda_E946():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E946)
    Sleep(50)

    def lambda_E956():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E956)
    Sleep(50)

    def lambda_E966():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E966)
    Sleep(50)

    def lambda_E976():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_E976)
    Sleep(50)

    def lambda_E986():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E986)
    Sleep(300)

    #C0720
    ChrTalk(
        0x21,
        "#01405F閣下、どうなさいました？\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x22,
        (
            "セイランド君、\x01",
            "端から見ていて思ったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x22,
        (
            "この症状はもしや、\x01",
            "『リボテン中毒』ではないかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0723
    ChrTalk(
        0x1D,
        "……なるほど、リボテン中毒。\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x1D,
        (
            "クロスベルにはない症例だが、\x01",
            "その可能性は高そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x105,
        (
            "#10305F『リボテン中毒』……？\x01",
            "聞いた事のない名前だね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    #C0726
    ChrTalk(
        0x22,
        (
            "大陸辺境に自生する\x01",
            "珍しい毒キノコによって\x01",
            "引き起こされる症状だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x22,
        (
            "その毒は、通常の方法では\x01",
            "なかなか検出が難しくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x22,
        (
            "だが、症状そのものは\x01",
            "あれとそっくりではないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x1D,
        "ああ、間違いないだろう。\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x1D,
        (
            "外から持ち込まれたものを\x01",
            "摂取したのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x104,
        (
            "#00305F教授先生のお墨付きか。\x02\x03",

            "#00300Fすげえッスね、大公サン。\x01",
            "そんなもんを一発で\x01",
            "見抜いちまうなんてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x22,
        "ハハ、大したことではないさ。\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x22,
        "だが、まだ安心はできまい。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0734
    ChrTalk(
        0x22,
        (
            "セイランド君、\x01",
            "リボテン中毒の特効薬の\x01",
            "備蓄はあるのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x1D,
        (
            "……いくつかの材料を\x01",
            "丁度、切らしてしまっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x1D,
        (
            "材料さえあればすぐにでも\x01",
            "調合できるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x109,
        "#10103Fそれはまずそうですね……\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x22,
        "ふむ……それならば。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    #C0739
    ChrTalk(
        0x22,
        "アリオス君、そして特務支援課の諸君。\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x22,
        (
            "君たちに、私から薬の材料調達を\x01",
            "緊急に依頼したいと思うのだが……\x01",
            "引き受けてくれるかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x21,
        "#01400Fはっ……仰せのままに。\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x101,
        (
            "#00001F緊急事態ですし、もちろん\x01",
            "引き受けさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x105,
        (
            "#10305Fそれで、なにを入手してくれば\x01",
            "いいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x22,
        "うむ、今から段取りを説明しよう。\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x22,
        (
            "『リボテン中毒』の特効薬は、\x01",
            "主に２つの材料で調合を行う。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x22,
        (
            "一つはマインツの山岳地帯にある\x01",
            "『アンテ草』と呼ばれる薬草……\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x22,
        (
            "そしてもう一つは、\x01",
            "ウルスラ間道の森林地帯にある\x01",
            "『アルマ茸』というキノコだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x109,
        (
            "#10100F『アンテ草』に『アルマ茸』……\x01",
            "警備隊のサバイバル訓練で\x01",
            "見たことがある気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x22,
        (
            "このうち、『アンテ草』の回収には\x01",
            "アリオス君に向かってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x22,
        (
            "人の手が入っていない\x01",
            "山岳地帯で薬草を探すなら、\x01",
            "遊撃士である君が適任だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x21,
        "#01400Fええ、了解しました。\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x22,
        "そして、『アルマ茸』だが……\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x22,
        (
            "こちらは私が、特務支援課の諸君に\x01",
            "同行してもらう形で探したいと思う。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0754
    ChrTalk(
        0x101,
        "#00005Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x102,
        "#00105F大公閣下と一緒に、ですか？\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x22,
        "うむ、というのも……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x22,
        (
            "『アルマ茸』というキノコが\x01",
            "生息する場所には、形がよく似た\x01",
            "別のキノコも多く生息しているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x22,
        (
            "非常に間違えやすいから、\x01",
            "知識のある者が同行した方がいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x105,
        (
            "#10303Fふむ、確かに一緒に\x01",
            "探した方がよさそうだね。\x02\x03",

            "#10300Fアリオスさんの護衛を\x01",
            "僕らに引き継ぐのが\x01",
            "不安じゃないなら、だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x104,
        "#00306F確かに責任は重大そうだなあ。\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x21,
        (
            "#01401F私も閣下の護衛を引き受けた手前、\x01",
            "いささか心配せざるをえませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x22,
        (
            "この患者を一刻も早く\x01",
            "治療することを優先するなら、\x01",
            "これ以外の方法はないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x22,
        (
            "支援課の諸君については、\x01",
            "君も実力を認めているんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x22,
        (
            "私も十分に気をつけるし\x01",
            "心配はいらないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x22,
        (
            "それに、アリオス君が\x01",
            "急いで帰ってきてくれれば、\x01",
            "何も問題はないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x21,
        (
            "#01404Fフ……了解しました。\x02\x03",

            "#01400Fそれでは、私は早速マインツの\x01",
            "山岳地帯に向かいます。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    #C0767
    ChrTalk(
        0x21,
        (
            "#01400F閣下の護衛のことは\x01",
            "よろしく頼んだぞ、特務支援課。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        "#00001Fはい……！\x02",
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x102,
        "#00100F必ず護衛を成し遂げてみせます。\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x22,
        (
            "フフ、それでは私たちも\x01",
            "間道の森林地帯に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0771
    ChrTalk(
        0x22,
        (
            "セイランド君たちは、\x01",
            "患者の経過を見つつ調合の準備を\x01",
            "整えておいてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x1D,
        "うむ、心得た。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0773
    ChrTalk(
        0xC,
        (
            "特務支援課の皆も、\x01",
            "どうかがんばってくれ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0774
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして、ロイドたちは\x01",
            "アルバート大公の緊急要請を引き受け……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0775
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アリオスと二手に分かれて\x01",
            "薬の材料調達に向かうのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0776
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【解毒薬の材料調達】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x78, 0x4, 0x2)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("r1580", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_D3A9 end

    def Function_49_F7AC(): pass

    label("Function_49_F7AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(58000, 1000, 58480, 0)
    MoveCamera(58, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21610, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 59700, 0, 58450, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 58750, 0, 58400, 0)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x1)
    ClearChrFlags(0x24, 0x2)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 270)
    OP_68(58990, 2000, 59760, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21940, 0)
    RemoveParty(0x76, 0xFF)
    SetChrPos(0x22, 56950, 0, 60000, 90)
    SetChrPos(0x21, 56050, 0, 58600, 90)
    SetChrPos(0x101, 56950, 0, 56650, 0)
    SetChrPos(0x102, 57950, 0, 56650, 0)
    SetChrPos(0x109, 58950, 0, 56650, 0)
    SetChrPos(0x104, 55950, 0, 57500, 45)
    SetChrPos(0x105, 55700, 0, 56350, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(58990, 1000, 59760, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0777
    ChrTalk(
        0x24,
        (
            "#1P外国のお土産に\x01",
            "持って帰ってきたキノコ、\x01",
            "すごく美味しかったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x24,
        (
            "#1Pふう、まさか毒キノコだったなんて、\x01",
            "うかつでしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x1D,
        (
            "食べて美味なのも\x01",
            "『リボテン中毒』を持つキノコの\x01",
            "危険な性質の一つだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x1D,
        (
            "今後は安易にそういったものを\x01",
            "口にしないようにすることだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x1D,
        (
            "それと、一命は取り留めたとはいえ\x01",
            "しばらくは研究棟の中にある病棟に\x01",
            "入院してもらうからそのつもりで。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x24,
        (
            "#1Pわ、分かりました。\x01",
            "確かに後遺症とかあったら\x01",
            "怖いですもんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x24,
        (
            "#1Pでも、おかげで大分楽になりました。\x01",
            "ありがとうございます、先生方。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xC,
        (
            "お礼なら、アルバート大公閣下と\x01",
            "アリオスさん、そして特務支援課の\x01",
            "人たちに言ってあげて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0xC,
        (
            "薬の材料を持ってきてくれたのは\x01",
            "他でもない彼らですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x24,
        (
            "#1Pあ……そ、そうですね。\x01",
            "皆さんもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x24,
        (
            "#1Pまさかあのアルバート大公閣下に\x01",
            "助けていただけるなんて……\x01",
            "なんだか恐れ多いですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x22,
        (
            "いやいや、私など所詮は\x01",
            "キノコを見定めたくらいのものだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FCA1():
        TurnDirection(0x22, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FCA1)

    #C0789
    ChrTalk(
        0x22,
        (
            "やはり功績はアリオス君と\x01",
            "支援課の諸君にあるだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x0)

    def lambda_FCEB():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_FCEB)
    Sleep(50)

    def lambda_FCFB():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FCFB)

    def lambda_FD08():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FD08)
    Sleep(50)

    def lambda_FD18():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FD18)

    def lambda_FD25():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_FD25)
    Sleep(50)

    def lambda_FD35():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD35)
    Sleep(50)

    def lambda_FD45():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD45)
    Sleep(300)

    #C0790
    ChrTalk(
        0x21,
        (
            "#01402Fご謙遜を……\x02\x03",

            "#01403F閣下はセイランド先生と\x01",
            "共に学んで医師免許を\x01",
            "とったと聞きます。\x02\x03",

            "#01400F経験、技術等のあらゆる面で\x01",
            "一線で活躍する医師に\x01",
            "見劣りはしないのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x104,
        "#00305Fへええ……そうだったんッスか。\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x105,
        (
            "#10300F流石は医療先進国レミフェリアの\x01",
            "大公さまと言ったところかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x22,
        "はは、私はこれでも勉強熱心でね。\x02",
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x22,
        (
            "セイランド君がレミフェリアにいた頃は\x01",
            "よく手術などを見学させてもらっていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x22,
        (
            "そうして培ってきた知識が、\x01",
            "今回たまたま役に立っただけなのだが……\x01",
            "そう言われると照れてしまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x22,
        (
            "だが、今回の件については\x01",
            "私は横から口出ししたに過ぎん。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x22,
        (
            "アリオス君と支援課の諸君、\x01",
            "そして病院の職員たちの協力が\x01",
            "迅速な治療へと向かわせたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x22,
        "うむ、実に有意義な視察だったな。\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x1D,
        (
            "やれやれ……\x01",
            "相変わらず理屈っぽいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x1D,
        (
            "ともかく、これで視察は\x01",
            "一通り終わったのだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x1D,
        (
            "明日の通商会議にむけて\x01",
            "そろそろ準備に戻った方が\x01",
            "いいのではないのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x22,
        (
            "はっはっは、君は本当に手厳しいな。\x01",
            "だが、言う事はいつも合理的で確かだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x22,
        (
            "それでは、私たちは\x01",
            "これで失礼させてもらうとするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x22,
        (
            "アリオス君、帰りの護衛も\x01",
            "お願いしてもいいかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x21,
        "#01400Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    #C0806
    ChrTalk(
        0x21,
        (
            "#01400F……それではな、特務支援課。\x02\x03",

            "#01403F明日の通商会議まで、\x01",
            "気を抜かずにいることだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    #C0807
    ChrTalk(
        0x101,
        (
            "#00000Fあ……はい。\x01",
            "肝に銘じておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x109,
        "#10100Fお疲れ様でした！\x02",
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x22,
        (
            "諸君、これからも\x01",
            "一層精進をしてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x22,
        "陰ながら応援させていただくよ。\x02",
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x102,
        "#00100Fふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0812
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【解毒薬の材料調達】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x78, 0x1, 0x1)
    OP_29(0x78, 0x1, 0x2)
    OP_29(0x78, 0x4, 0x10)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x24, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 56950, 0, 60000, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 54710, 0, 55500, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_49_F7AC end

    def Function_50_1048E(): pass

    label("Function_50_1048E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14780, 1000, 6910, 0)
    MoveCamera(58, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21660, 0)
    SetChrPos(0x101, 14490, 0, 7430, 90)
    SetChrPos(0x102, 15120, 0, 5850, 45)
    SetChrPos(0x103, 13530, 0, 8000, 90)
    SetChrPos(0x109, 12940, 0, 6840, 90)
    SetChrPos(0x104, 13810, 0, 6210, 45)
    SetChrPos(0x105, 13710, 0, 5020, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0813
    ChrTalk(
        0x8,
        (
            "支援課の皆様……\x01",
            "ウルスラ病院へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x8,
        (
            "本日はどういった\x01",
            "ご用件でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x101,
        (
            "#00000Fええと、ちょっと\x01",
            "お尋ねしたいことが\x01",
            "あって来たんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0816
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは荷物の誤配が\x01",
            "あったことについて尋ねた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0817
    ChrTalk(
        0x8,
        (
            "ああ……あの荷物は\x01",
            "そういうことでしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x8,
        (
            "看護師の１人が\x01",
            "発注ミスをしたのではと\x01",
            "マーサ師長が騒いでいましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x103,
        "#00205F発注ミス……ですか。\x02",
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x8,
        (
            "ええ、以前にも何度か\x01",
            "こういうことがありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x109,
        (
            "#10100Fそれでは、荷物は今\x01",
            "ナースステーションに？\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x8,
        (
            "ええ、そういうことに\x01",
            "なりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x8,
        "一旦２階を訪ねてみてください。\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x104,
        "#00300Fそんじゃ、そうするとすっか。\x02",
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x105,
        (
            "#10300F濡れ衣で怒られてるとしたら\x01",
            "かわいそうだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x101,
        (
            "#00006Fそ、そうだな……\x01",
            "早速行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x175, 7)
    OP_29(0x85, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 14410, 0, 7430, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_50_1048E end

    def Function_51_10870(): pass

    label("Function_51_10870")

    Return()

    # Function_51_10870 end

    def Function_52_10871(): pass

    label("Function_52_10871")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(8130, 1000, 530, 0)
    MoveCamera(65, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x8, 9100, 0, 1500, 270)
    SetChrPos(0x9, 9100, 0, 500, 270)
    SetChrPos(0x1E, 9100, 0, -500, 270)
    SetChrPos(0x1D, 9100, 0, -1500, 270)
    SetChrPos(0x23, 7140, 0, 2160, 135)
    SetChrPos(0x101, 6500, 0, 0, 90)
    SetChrPos(0x102, 6300, 0, 1000, 90)
    SetChrPos(0x104, 6300, 0, -1000, 90)
    SetChrPos(0x109, 4900, 0, 0, 90)
    SetChrPos(0x105, 5100, 0, 1000, 90)
    SetChrPos(0x103, 5100, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x23, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0828
    ChrTalk(
        0x9,
        (
            "空港のリカルドさんから\x01",
            "連絡があった時は驚きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x9,
        (
            "医療物資が届かないと思ったら\x01",
            "まさか、そんなことになっていたとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x1E,
        "悪いヤツがいるもんだねえ……\x02",
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x8,
        (
            "でも、医療物資が届いて\x01",
            "本当によかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x1D,
        (
            "ひとまずはこれで、\x01",
            "襲撃事件の患者たちに\x01",
            "十分な対応がとれるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x1D,
        (
            "君たちには何かと助けられるな。\x01",
            "改めて礼を言わせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x102,
        (
            "#00100Fいえ、当然のことを\x01",
            "したまでですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x104,
        (
            "#00301F火事場泥棒みたいな\x01",
            "卑劣な野郎を許すわけには\x01",
            "いかないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x105,
        (
            "#10303Fま、今回はあの鎧に\x01",
            "助けられちゃったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x1E,
        "鎧……って何だい？\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x109,
        "#10100Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x103,
        (
            "#00203F……こちらの話です、\x01",
            "あまり気にしないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x101,
        (
            "#00000Fそれでは、また何かあったら\x01",
            "いつでもご相談ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x8,
        (
            "ええ……\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x23,
        (
            "俺の方からも礼を言わせてもらうぜ。\x01",
            "本当にありがとうな！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0843
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【医療物資の捜索】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x1, 0x7)
    OP_29(0x93, 0x1, 0x8)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x93, 0x4, 0x10)
    OP_2C(0x93, 0x2)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, 19740, 0, 4890, 180)
    ClearChrFlags(0x9, 0x10)
    OP_66(0x1, 0x1)
    OP_4C(0x1D, 0xFF)
    SetChrPos(0x1D, 65800, 0, 1700, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5950, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_10871 end

    def Function_53_10DDE(): pass

    label("Function_53_10DDE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(8130, 1000, 530, 0)
    MoveCamera(65, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x8, 9100, 0, 1500, 270)
    SetChrPos(0x9, 9100, 0, 500, 270)
    SetChrPos(0x1E, 9100, 0, -500, 270)
    SetChrPos(0x1D, 9100, 0, -1500, 270)
    SetChrPos(0x23, 7140, 0, 2160, 135)
    SetChrPos(0x101, 6500, 0, 0, 90)
    SetChrPos(0x102, 6300, 0, 1000, 90)
    SetChrPos(0x104, 6300, 0, -1000, 90)
    SetChrPos(0x109, 4900, 0, 0, 90)
    SetChrPos(0x105, 5100, 0, 1000, 90)
    SetChrPos(0x103, 5100, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x23, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0844
    ChrTalk(
        0x9,
        (
            "空港のリカルドさんから\x01",
            "連絡があった時は驚きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x9,
        (
            "医療物資が届かないと思ったら\x01",
            "まさか、そんなことになっていたとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x1E,
        "悪いヤツがいるもんだねえ……\x02",
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x101,
        (
            "#00003F力及ばず、本当に\x01",
            "申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x102,
        (
            "#00108F何としても\x01",
            "捕まえたかったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0x23,
        (
            "俺も、もっと早く\x01",
            "荷物を受け取りに行ってれば\x01",
            "こんなことには……\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x9,
        (
            "いえ、みなさんのせいでは……\x01",
            "どうか気を落とさないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x9,
        (
            "とにかく、あとはこちら側で\x01",
            "なんとかしてみますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x8,
        (
            "盗まれてしまったものは\x01",
            "もう仕方ないですものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x8,
        (
            "急いで追加の物資を\x01",
            "送ってもらえるよう手配しないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x1D,
        (
            "それまでは何とか、\x01",
            "工夫しつつやるしかないだろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x101,
        (
            "#00003Fすみません……\x01",
            "後はよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x23,
        (
            "（はあ、こりゃ親父にゲンコを\x01",
            "  食らっちまいそうだな……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0857
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【医療物資の捜索】\x07\x00",
            "に失敗した……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x1, 0x9)
    OP_29(0x93, 0x4, 0x40)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, 19740, 0, 4890, 180)
    ClearChrFlags(0x9, 0x10)
    OP_66(0x1, 0x1)
    OP_4C(0x1D, 0xFF)
    SetChrPos(0x1D, 65800, 0, 1700, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5950, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_53_10DDE end

    def Function_54_112F3(): pass

    label("Function_54_112F3")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0858
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　ＩＣＵ（集中治療室）\x01",
            "許可なき者の立ち入りを禁ずる。\x01",
            "※入室者はレベル２以上の\x01",
            "  滅菌処理を行ってください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_54_112F3 end

    def Function_55_1139C(): pass

    label("Function_55_1139C")

    EventBegin(0x1)

    #C0859
    ChrTalk(
        0x101,
        (
            "#00000Fまずは受付に行こう。\x01",
            "病室を訪ねるのはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 59460, 0, 3330, 225)
    EventEnd(0x4)
    Return()

    # Function_55_1139C end

    def Function_56_113F1(): pass

    label("Function_56_113F1")

    EventBegin(0x1)

    #C0860
    ChrTalk(
        0x101,
        (
            "#00000Fまずは受付に行こう。\x01",
            "病室を訪ねるのはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11970, 0, 10190, 135)
    EventEnd(0x4)
    Return()

    # Function_56_113F1 end

    def Function_57_11446(): pass

    label("Function_57_11446")

    EventBegin(0x1)

    #C0861
    ChrTalk(
        0x101,
        (
            "#00000Fフランの病室は３０１号室だったな。\x01",
            "早いところ様子を見に行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1120, 50, -440, 89)
    EventEnd(0x4)
    Return()

    # Function_57_11446 end

    SaveToFile()

Try(main)
