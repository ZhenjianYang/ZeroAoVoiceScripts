from ScenarioHelper import *

def main():
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
        "接待小姐塞拉",           # 1
        "克拉克事务长",           # 2
        "兰护士",                 # 3
        "拉格教授",               # 4
        "实习医生利顿",           # 5
        "实习医生古恩",           # 6
        "盖里教授",               # 7
        "阿修拉主任",             # 8
        "实习医生夏鲁鲁",         # 9
        "门诊患者",               # 10
        "门诊患者",               # 11
        "门诊患者",               # 12
        "门诊患者",               # 13
        "门诊患者",               # 14
        "门诊患者",               # 15
        "门诊患者",               # 16
        "门诊患者",               # 17
        "患者",                   # 18
        "患者",                   # 19
        "患者",                   # 20
        "艾达护士",               # 21
        "赛兰德教授",             # 22
        "警备员托尼",             # 23
        "奎因老人",               # 24
        "亚米萨",                 # 25
        "亚里欧斯",               # 26
        "阿尔伯特大公",           # 27
        "比利",                   # 28
        "患者",                   # 29
        "游击士艾欧莉娅",         # 30
        "塞茜尔",                 # 31
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
        "Function_8_251E",         # 08, 8
        "Function_9_2522",         # 09, 9
        "Function_10_36FC",        # 0A, 10
        "Function_11_4259",        # 0B, 11
        "Function_12_4E40",        # 0C, 12
        "Function_13_542D",        # 0D, 13
        "Function_14_5B07",        # 0E, 14
        "Function_15_6384",        # 0F, 15
        "Function_16_6C8F",        # 10, 16
        "Function_17_6D75",        # 11, 17
        "Function_18_79D8",        # 12, 18
        "Function_19_7B45",        # 13, 19
        "Function_20_86E1",        # 14, 20
        "Function_21_89ED",        # 15, 21
        "Function_22_8CD6",        # 16, 22
        "Function_23_9089",        # 17, 23
        "Function_24_93F4",        # 18, 24
        "Function_25_9475",        # 19, 25
        "Function_26_9654",        # 1A, 26
        "Function_27_9907",        # 1B, 27
        "Function_28_9A45",        # 1C, 28
        "Function_29_9B6C",        # 1D, 29
        "Function_30_9BDB",        # 1E, 30
        "Function_31_9C1A",        # 1F, 31
        "Function_32_9C80",        # 20, 32
        "Function_33_9CDE",        # 21, 33
        "Function_34_A608",        # 22, 34
        "Function_35_A6A3",        # 23, 35
        "Function_36_A772",        # 24, 36
        "Function_37_A7FF",        # 25, 37
        "Function_38_A970",        # 26, 38
        "Function_39_AA1B",        # 27, 39
        "Function_40_AA8D",        # 28, 40
        "Function_41_AAC3",        # 29, 41
        "Function_42_AB4E",        # 2A, 42
        "Function_43_ACC6",        # 2B, 43
        "Function_44_ACCD",        # 2C, 44
        "Function_45_AF04",        # 2D, 45
        "Function_46_AF0B",        # 2E, 46
        "Function_47_B182",        # 2F, 47
        "Function_48_B883",        # 30, 48
        "Function_49_D850",        # 31, 49
        "Function_50_E36A",        # 32, 50
        "Function_51_E6AE",        # 33, 51
        "Function_52_E6AF",        # 34, 52
        "Function_53_EB8E",        # 35, 53
        "Function_54_F01F",        # 36, 54
        "Function_55_F0B2",        # 37, 55
        "Function_56_F0FF",        # 38, 56
        "Function_57_F14C",        # 39, 57
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1564")

    #C0001
    ChrTalk(
        0x8,
        (
            "之前一段时间一直不能接收门诊患者，\x01",
            "如今总算恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "虽然暂时要忙上一段时间，\x01",
            "但真是松了一口气……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "这多亏你们的努力，\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F9")

    label("loc_1564")


    #C0004
    ChrTalk(
        0x8,
        (
            "之前一段时间一直不能接收门诊患者，\x01",
            "如今总算恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "虽然暂时要忙上一段时间，\x01",
            "但身为医院的职员，\x01",
            "我一定会以最诚恳耐心的态度来接待大家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F9")

    Jump("loc_251A")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B2")

    #C0006
    ChrTalk(
        0x8,
        (
            "据传闻说，受那个无效宣言的影响，\x01",
            "市内的一些地区好像\x01",
            "发生了暴动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "虽然很快就被国防军镇压了……\x01",
            "但还是很让人担心呢，不知道有没有造成人员伤亡。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1720")

    label("loc_16B2")


    #C0008
    ChrTalk(
        0x8,
        (
            "受那个无效宣言的影响，\x01",
            "市内的一些地区好像\x01",
            "发生了暴动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "不知道有没有造成人员伤亡，真让人担心呢……\x02",
    )

    CloseMessageWindow()

    label("loc_1720")

    Jump("loc_251A")

    label("loc_1725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_183C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")

    #C0010
    ChrTalk(
        0x8,
        (
            "我们正在与国防军进行交涉，\x01",
            "以便可以给以前来医院就诊\x01",
            "的非住院患者配送处方药。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "但患者的数量实在太多……\x01",
            "很难一一顾及到。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "……真是没办法啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1837")

    label("loc_17D9")


    #C0013
    ChrTalk(
        0x8,
        (
            "既然已经无法接收门诊患者了，\x01",
            "至少也想把药给市内的\x01",
            "患者们送去……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "……真是没办法啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1837")

    Jump("loc_251A")

    label("loc_183C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_19C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1940")

    #C0015
    ChrTalk(
        0x8,
        (
            "受『幻兽』的影响，\x01",
            "医院现在已经暂停接待门诊患者了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "现在只有重病与重伤患者\x01",
            "才能在国防军的护卫下，\x01",
            "被急救车送来医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "这种体制已经违背了\x01",
            "乌尔斯拉医院一直以来的存在价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……总之，实在是很担心\x01",
            "市内的那些患者啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19BF")

    label("loc_1940")


    #C0019
    ChrTalk(
        0x8,
        (
            "受『幻兽』的影响，\x01",
            "医院现在已经暂停接待门诊患者了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "只有重病与重伤患者\x01",
            "才能得到救治……\x01",
            "真是很担心市内的那些患者啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BF")

    Jump("loc_251A")

    label("loc_19C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C40")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A77")

    #C0021
    ChrTalk(
        0x8,
        (
            "医疗物资能顺利送达，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "虽有僭越之嫌，但请容我\x01",
            "代表医院向大家表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "各位，\x01",
            "真是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACB")

    label("loc_1A77")


    #C0024
    ChrTalk(
        0x8,
        (
            "虽有僭越之嫌，但请容我\x01",
            "代表医院向大家表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "各位，\x01",
            "真是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACB")

    Jump("loc_1C3B")

    label("loc_1AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1B52")

    #C0026
    ChrTalk(
        0x8,
        (
            "已经向雷米菲利亚那边说明了情况，\x01",
            "他们会把医疗物资\x01",
            "重新送来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "虽然多少会有些延误……\x01",
            "但这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C3B")

    label("loc_1B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE3")

    #C0028
    ChrTalk(
        0x8,
        (
            "负责警备的托尼先生\x01",
            "刚才向事务长报告了些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "他们两人正在\x01",
            "诊疗室的门前\x01",
            "和赛兰德教授谈话……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "莫非出了什么事吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C3B")

    label("loc_1BE3")


    #C0031
    ChrTalk(
        0x8,
        (
            "警备员托尼先生和事务长\x01",
            "正在诊疗室的门前\x01",
            "和赛兰德教授谈话。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "莫非出了什么事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1C3B")

    Jump("loc_1D2A")

    label("loc_1C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD2")

    #C0033
    ChrTalk(
        0x8,
        (
            "芙兰小姐的病房是\x01",
            "三楼的３０１室。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "她的情况基本已经稳定了，\x01",
            "只是体力还没有\x01",
            "恢复……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "请各位面带笑容地\x01",
            "去探望她吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D2A")

    label("loc_1CD2")


    #C0036
    ChrTalk(
        0x8,
        (
            "芙兰小姐已经在\x01",
            "几天前恢复了意识。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "她受了很严重的伤呢……\x01",
            "能醒过来真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2A")

    Jump("loc_251A")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4C")

    #C0038
    ChrTalk(
        0x8,
        (
            "昨天发生列车事故之后，\x01",
            "很多患者都被送到了医院，\x01",
            "其中还有一些外国人。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "乌尔斯拉医院对救治\x01",
            "外国人的工作也有充足准备，\x01",
            "治疗进程可以确保顺利……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "但在那些医疗不太发达的国家，\x01",
            "如果发生了这样的情况，\x01",
            "又该如何是好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "光是想想，就让人心头一紧呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EDC")

    label("loc_1E4C")


    #C0042
    ChrTalk(
        0x8,
        (
            "但在那些医疗不太发达的国家，\x01",
            "如果发生了这样的情况，\x01",
            "又该如何是好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "那些患者几乎都是轻伤，\x01",
            "从某种意义上说，\x01",
            "或许也算是运气不错吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDC")

    Jump("loc_251A")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2070")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F96")

    #C0044
    ChrTalk(
        0x8,
        "那个包裹是送错地方了啊？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "玛萨护士长还以为是\x01",
            "某个护士工作失误，下错了定单，\x01",
            "一直在训人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "总之，你们先去\x01",
            "二楼问问吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FED")

    label("loc_1F96")


    #C0047
    ChrTalk(
        0x8,
        (
            "你们已经顺利取到\x01",
            "误送的包裹了吧？\x01",
            "呵呵，太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "请大家在回去时\x01",
            "一路小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FED")

    Jump("loc_206B")

    label("loc_1FF2")


    #C0049
    ChrTalk(
        0x8,
        (
            "欢迎来到乌尔斯拉医院，\x01",
            "外来就诊、探视慰问方面的问题请来此咨询。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "如需复诊，可以在\x01",
            "导力网络上预约，\x01",
            "请多加利用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206B")

    Jump("loc_251A")

    label("loc_2070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2160")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2107")

    #C0051
    ChrTalk(
        0x8,
        (
            "……不行啊，\x01",
            "全体职员好像\x01",
            "都开始陷入消沉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "大家一直都很期待\x01",
            "给小滴做好手术，\x01",
            "如今出了这种事，也是可以理解的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_215B")

    label("loc_2107")


    #C0053
    ChrTalk(
        0x8,
        (
            "……我们这些职员\x01",
            "总不能一直消沉下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "无论如何也要尽快\x01",
            "摆脱失落的情绪……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215B")

    Jump("loc_251A")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2213")

    #C0055
    ChrTalk(
        0x8,
        (
            "米海尔好像已经\x01",
            "确定要下周出院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "他已经住院很久了，突然要离开，\x01",
            "我总觉得有些失落呢……\x01",
            "不过这真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "到时候，大家会一起\x01",
            "欢送他的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_225F")

    label("loc_2213")


    #C0058
    ChrTalk(
        0x8,
        (
            "米海尔很快就要出院了，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "到时候，大家会一起\x01",
            "欢送他的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225F")

    Jump("loc_251A")

    label("loc_2264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23E4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22FC")

    #C0060
    ChrTalk(
        0x8,
        (
            "阿尔伯特大公阁下\x01",
            "好像已经返回市里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "呵呵，大家也辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "在患者出院之前，\x01",
            "我们会担负起责任，认真为他治疗的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_22FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236E")

    #C0063
    ChrTalk(
        0x8,
        (
            "刚才阿尔伯特大公阁下\x01",
            "和亚里欧斯先生来医院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "他们现在好像已经\x01",
            "视察完毕，\x01",
            "去探望小滴了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23DF")

    label("loc_236E")


    #C0065
    ChrTalk(
        0x8,
        (
            "阿尔伯特大公阁下\x01",
            "和亚里欧斯先生\x01",
            "一起去内科诊疗室了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "他们已经结束了视察，\x01",
            "大概还要和教授谈上一阵子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DF")

    Jump("loc_251A")

    label("loc_23E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_251A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2459")

    #C0067
    ChrTalk(
        0x8,
        (
            "各位帮忙回收问诊表，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "如果以后有什么事情\x01",
            "需要帮忙，\x01",
            "欢迎随时过来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251A")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CE")

    #C0069
    ChrTalk(
        0x8,
        (
            "赛兰德教授\x01",
            "正在药物学·神经科\x01",
            "的研究室。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "登上楼顶就能看到研究楼，\x01",
            "进入之后上四层就是了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_251A")

    label("loc_24CE")


    #C0071
    ChrTalk(
        0x8,
        (
            "赛兰德教授\x01",
            "正在研究室。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "药物学·神经科的研究室\x01",
            "在研究楼的四层哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251A")

    TalkEnd(0x8)
    Return()

    # Function_7_1478 end

    def Function_8_251E(): pass

    label("Function_8_251E")

    Call(0, 9)
    Return()

    # Function_8_251E end

    def Function_9_2522(): pass

    label("Function_9_2522")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F2")

    #C0073
    ChrTalk(
        0x9,
        (
            "如今的医疗物资十分有限，\x01",
            "情况绝对不容乐观……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "但只要能重新恢复\x01",
            "接收门诊患者，患者得到救治的\x01",
            "可能性还是比不能来医院要高多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "我们这些职员\x01",
            "也必须要继续努力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2684")

    label("loc_25F2")


    #C0076
    ChrTalk(
        0x9,
        (
            "现状虽然很艰难，\x01",
            "但只要和雷米菲利亚那边再次合作，\x01",
            "一定能解决医疗物资方面的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "总算可以重新\x01",
            "接收门诊患者了……\x01",
            "必须要继续努力才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2684")

    Jump("loc_36F8")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_27E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2762")

    #C0078
    ChrTalk(
        0x9,
        (
            "有关克洛斯贝尔市的情报，\x01",
            "如今已经断绝了\x01",
            "一切了解渠道。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "恐怕是由于无效宣言的影响，\x01",
            "使政府部门有意\x01",
            "遮掩所有情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "这样一来，我们就无法\x01",
            "救治急病患者了。\x01",
            "……真担心市里的人们啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27E2")

    label("loc_2762")


    #C0081
    ChrTalk(
        0x9,
        (
            "有关克洛斯贝尔市的情报，\x01",
            "如今已经断绝了\x01",
            "一切了解渠道。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "这样一来，我们就无法\x01",
            "救治急病患者了。\x01",
            "……真担心市里的人们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E2")

    Jump("loc_36F8")

    label("loc_27E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_295A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CB")

    #C0083
    ChrTalk(
        0x9,
        (
            "整个克洛斯贝尔地区都遭到了情报管制，\x01",
            "现在几乎得不到市里的任何情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "顶多也就是偶尔接到有急救患者\x01",
            "需要救治的情报，而且往往还因为\x01",
            "延误了时机，导致应对工作很被动……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        "呼，真是糟糕的状况啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2955")

    label("loc_28CB")


    #C0086
    ChrTalk(
        0x9,
        (
            "整个克洛斯贝尔地区都遭到了情报管制，\x01",
            "现在几乎得不到市里的任何情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "应对工作也经常被延误，导致很被动……\x01",
            "呼，真是糟糕的状况啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2955")

    Jump("loc_36F8")

    label("loc_295A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4A")

    #C0088
    ChrTalk(
        0x9,
        (
            "缇欧在调整导力网络的\x01",
            "工作中帮了很多忙，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "为了确保能以万全的状态\x01",
            "应对特殊事态，\x01",
            "导力网络可是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "请容我在此向你\x01",
            "正式表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#00202F呵呵，哪里……\x01",
            "我只是帮了点小忙而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AD8")

    label("loc_2A4A")


    #C0092
    ChrTalk(
        0x9,
        (
            "缇欧在调整导力网络的\x01",
            "工作中帮了很多忙，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "但这样的状况如果一直持续，\x01",
            "对医院而言实在是非常糟糕。\x01",
            "必须要努力想些对策……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD8")

    Jump("loc_36F8")

    label("loc_2ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8E")

    #C0094
    ChrTalk(
        0x9,
        (
            "我们已经联络了\x01",
            "空港的利卡尔德先生，\x01",
            "通知他物资安全送到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "他总算也安下心了，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "但愿以后别再发生\x01",
            "这样的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BE4")

    label("loc_2B8E")


    #C0097
    ChrTalk(
        0x9,
        (
            "利卡尔德先生总算也松了一口气，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "但愿以后别再发生\x01",
            "这样的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE4")

    TalkEnd(0x9)
    Return()

    label("loc_2BED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2C4E")

    #C0099
    ChrTalk(
        0x9,
        (
            "这次的事情，\x01",
            "责任并不在大家。\x01",
            "请不要沮丧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "总之，我们会\x01",
            "想些办法的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    label("loc_2C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C71")
    Call(0, 35)
    Jump("loc_2CC7")

    label("loc_2C71")


    #C0101
    ChrTalk(
        0x9,
        (
            "说不定是运输工具\x01",
            "出现了什么问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "总、总之，我会再次尝试\x01",
            "联络相关人员的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC7")

    Jump("loc_2E7D")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF3")

    #C0103
    ChrTalk(
        0x9,
        (
            "这段时间，有无数人\x01",
            "申请来医院探望\x01",
            "伊莉娅小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "但由于伊莉娅小姐一直都没有恢复意识，\x01",
            "所以除了相关人士之外，我们全都婉言回绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "即使如此，\x01",
            "送来点心等慰问品的人\x01",
            "仍然接连不断……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "对居民们来说，伊莉娅小姐\x01",
            "一直都是无比重要的人，\x01",
            "如今我再次深刻体会到了这一点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E7D")

    label("loc_2DF3")


    #C0107
    ChrTalk(
        0x9,
        (
            "给伊莉娅小姐送来点心\x01",
            "等慰问品的人\x01",
            "一直接连不断。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "对居民们来说，伊莉娅小姐\x01",
            "一直都是无比重要的人，\x01",
            "如今我再次深刻体会到了这一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7D")

    Jump("loc_36F8")

    label("loc_2E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F79")

    #C0109
    ChrTalk(
        0x9,
        (
            "从昨天开始，众多身在帝国或共和国\x01",
            "的事故伤员家属就接连不断地\x01",
            "发来通讯，咨询家人的安危状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "自己的家人在国外住院，\x01",
            "自然会非常\x01",
            "担心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "再加上自从\x01",
            "前几天发表了独立提案之后，\x01",
            "克洛斯贝尔就一直处于紧张状态……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FEA")

    label("loc_2F79")


    #C0112
    ChrTalk(
        0x9,
        (
            "自己的家人在国外住院，\x01",
            "肯定会非常\x01",
            "担心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "为了让他们尽早平安回国，\x01",
            "我们一定会诚心诚意地做好本职工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEA")

    Jump("loc_36F8")

    label("loc_2FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3137")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C3")

    #C0114
    ChrTalk(
        0x9,
        (
            "多亏导力网络方面的法规\x01",
            "做了整改，在网络上预约\x01",
            "复诊的人越来越多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "如果克洛斯贝尔能独立，\x01",
            "像这种有用的法案应该就\x01",
            "更容易通过了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "但居民投票的结果\x01",
            "最后究竟会如何呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3132")

    label("loc_30C3")


    #C0117
    ChrTalk(
        0x9,
        (
            "如果克洛斯贝尔能独立，\x01",
            "一些有用的法案应该就\x01",
            "更容易通过了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "但居民投票的结果\x01",
            "最后究竟会如何呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3132")

    Jump("loc_36F8")

    label("loc_3137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_32B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3221")

    #C0119
    ChrTalk(
        0x9,
        (
            "几天前给小滴做的那场手术，\x01",
            "采用了赛兰德教授\x01",
            "首创的划时代手术方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "医患人员也对此非常关注，\x01",
            "医院前一段时间下跌的信赖度\x01",
            "已经完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "……但是，毕竟手术没有彻底成功，\x01",
            "仍旧无法高兴起来啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32AC")

    label("loc_3221")


    #C0122
    ChrTalk(
        0x9,
        (
            "尝试了划时代的手术方案之后，\x01",
            "医院前一段时间下跌的信赖度\x01",
            "已经完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "……但是，毕竟手术没有彻底成功，\x01",
            "仍旧无法高兴起来啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AC")

    Jump("loc_36F8")

    label("loc_32B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337E")

    #C0124
    ChrTalk(
        0x9,
        (
            "在不久后，\x01",
            "赛兰德教授\x01",
            "将会执刀一场重要的手术。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            "阿尔伯特大公在昨天的视察中决定，\x01",
            "雷米菲利亚也将提供\x01",
            "全面的支援。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "为了让手术取得成功，\x01",
            "我们也一定要竭尽\x01",
            "自己所能啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33EA")

    label("loc_337E")


    #C0127
    ChrTalk(
        0x9,
        (
            "在不久后，\x01",
            "赛兰德教授\x01",
            "将会执刀一场重要的手术。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "为了让手术取得成功，\x01",
            "我们也一定要竭尽\x01",
            "自己所能啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EA")

    Jump("loc_36F8")

    label("loc_33EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_352C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BA")

    #C0129
    ChrTalk(
        0x9,
        (
            "刚才阿尔伯特大公前来视察，\x01",
            "向一直辛苦工作的医护人员表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "大公也是医院的赞助人之一，\x01",
            "从以前开始，就一直给我们可靠的支援。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        "我们这些职员真是得到了很大鼓舞啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3527")

    label("loc_34BA")


    #C0132
    ChrTalk(
        0x9,
        (
            "大公也是医院的赞助人之一，\x01",
            "从以前开始，就一直给我们可靠的支援。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        "我们这些职员真是得到了很大鼓舞啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3527")

    Jump("loc_36F8")

    label("loc_352C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3672")

    #C0134
    ChrTalk(
        0x9,
        (
            "遭受了『教团事件』的负面影响，\x01",
            "医院长久以来辛苦积累的\x01",
            "信赖感瞬间跌落到了谷底。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "医院中的医生滥用药物，\x01",
            "使整个地区陷入混乱。\x01",
            "……发生了这种事，民众觉得担心也是没办法的。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "经过警察的严密调查，\x01",
            "已经确定了约亚西姆平时\x01",
            "所开的处方药并无问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "但有些患者对医院的不信任感\x01",
            "仍然挥之不去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36F8")

    label("loc_3672")


    #C0138
    ChrTalk(
        0x9,
        (
            "虽然对药物的疑惑已经消解，\x01",
            "但仍然有不少患者\x01",
            "对医院保持着不信任感。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "今后一定要让医疗过程\x01",
            "更加透明，争取逐渐挽回\x01",
            "大家的信赖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F8")

    TalkEnd(0x9)
    Return()

    # Function_9_2522 end

    def Function_10_36FC(): pass

    label("Function_10_36FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_387B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DF")

    #C0140
    ChrTalk(
        0xA,
        (
            "警察弟弟，还有各位……\x01",
            "虽然情况的确很糟糕，\x01",
            "但绝对不能放弃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "等到事情结束，一切都恢复平静之后，\x01",
            "我们还要一起去玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#00309F嗯，包在我身上吧！\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#00000F哈哈，我们一定会努力的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3876")

    label("loc_37DF")


    #C0144
    ChrTalk(
        0xA,
        (
            "等到事情结束，一切都恢复平静之后，\x01",
            "我们还要一起去玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "到时候叫上艾达、菲利亚、希伦和梅菲尔，\x01",
            "连玛萨护士长也要一起叫上，\x01",
            "大家一起玩个痛快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3876")

    Jump("loc_4255")

    label("loc_387B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_39D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3951")

    #C0146
    ChrTalk(
        0xA,
        (
            "那些不得不留在医院\x01",
            "的外来访客们的精神压力\x01",
            "已经渐渐接近顶点……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "但由于市里发生了那样的事，\x01",
            "大家似乎又重新燃起\x01",
            "回去的希望了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "还不知道接下来将会如何，\x01",
            "希望大家都能顺利回去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39D0")

    label("loc_3951")


    #C0149
    ChrTalk(
        0xA,
        (
            "市里发生了那样的事，\x01",
            "那些被迫留在医院的\x01",
            "外来访客们似乎又重燃希望了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "还不知道接下来将会如何，\x01",
            "希望大家都能顺利回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D0")

    Jump("loc_4255")

    label("loc_39D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3B10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAA")

    #C0151
    ChrTalk(
        0xA,
        (
            "伊莉娅·普拉提耶的情况不容乐观，\x01",
            "如今似乎还看不到\x01",
            "痊愈的希望呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "……不过没问题的。\x01",
            "我们医院的医生\x01",
            "都是非常优秀的。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "虽然可能要花些时间，\x01",
            "但各位医生一定\x01",
            "能把伊莉娅治好的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B0B")

    label("loc_3AAA")


    #C0154
    ChrTalk(
        0xA,
        (
            "我们医院的医生\x01",
            "都是非常优秀的。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        (
            "虽然可能要花些时间，\x01",
            "但各位医生一定\x01",
            "能把伊莉娅治好的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0B")

    Jump("loc_4255")

    label("loc_3B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE2")

    #C0156
    ChrTalk(
        0xA,
        (
            "虽然发生了这种状况……\x01",
            "但医院中的各位\x01",
            "却意外地积极呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        (
            "究其原因，大概是由于一直都\x01",
            "昏迷不醒的伊莉娅·普拉提耶\x01",
            "终于恢复了意识吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xA,
        (
            "这么一想，我们也必须要\x01",
            "继续加油才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C4D")

    label("loc_3BE2")


    #C0159
    ChrTalk(
        0xA,
        (
            "伊莉娅·普拉提耶\x01",
            "终于恢复了意识，\x01",
            "这真是久违的好消息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "这么一想，我们也必须要\x01",
            "继续加油才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4D")

    Jump("loc_4255")

    label("loc_3C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CE3")

    #C0161
    ChrTalk(
        0xA,
        (
            "呼，真是太累了，\x01",
            "快要坚持不下去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xA,
        (
            "……不、不行，在这种时候应该想想患者，\x01",
            "患者们现在比我更加难受，\x01",
            "我可不能说丧气话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4255")

    label("loc_3CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D5E")

    #C0163
    ChrTalk(
        0xA,
        (
            "受昨天那起列车事故的影响，\x01",
            "我们这里也非常忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "看样子，暂时是没机会\x01",
            "玩乐了……\x01",
            "必须要努力工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4255")

    label("loc_3D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DDA")

    #C0165
    ChrTalk(
        0xA,
        (
            "小滴一直都是那样坚强，\x01",
            "她的坚强也能给我们带来活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "我们这些护士也必须要满怀希望，\x01",
            "支撑着小滴才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4255")

    label("loc_3DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E92")

    #C0167
    ChrTalk(
        0xA,
        (
            "小滴至今为止已经接受过\x01",
            "好几次眼部手术了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "医院中的医生虽然很优秀，\x01",
            "但也始终无法取得进展……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "那个孩子，还有亚里欧斯先生，\x01",
            "肯定都感到很不安吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F11")

    label("loc_3E92")


    #C0170
    ChrTalk(
        0xA,
        (
            "小滴至今为止已经接受过\x01",
            "好几次眼部手术了，\x01",
            "但一直都没能顺利恢复……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "那个孩子，还有亚里欧斯先生，\x01",
            "肯定都感到很不安吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F11")

    Jump("loc_4255")

    label("loc_3F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC3")

    #C0172
    ChrTalk(
        0xA,
        (
            "听说赛兰德教授\x01",
            "最近要执刀一起\x01",
            "重要的大手术……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "在这所医院里，\x01",
            "需要动那种手术的人，\x01",
            "似乎也只有『那孩子』了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        "但愿手术能顺利成功。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_401F")

    label("loc_3FC3")


    #C0175
    ChrTalk(
        0xA,
        (
            "在这所医院里，\x01",
            "需要动那种大手术的人\x01",
            "似乎也只有『那孩子』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xA,
        "但愿手术能顺利成功。\x02",
    )

    CloseMessageWindow()

    label("loc_401F")

    Jump("loc_4255")

    label("loc_4024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40AE")

    #C0177
    ChrTalk(
        0xA,
        (
            "拉格教授今天\x01",
            "出差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "好像是要出席外国的\x01",
            "一场学术讨论会。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "所以赛兰德教授今天\x01",
            "代替他在内科值班。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_410E")

    label("loc_40AE")


    #C0180
    ChrTalk(
        0xA,
        (
            "拉格教授今天\x01",
            "去出席外国的学术讨论会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "难得大公阁下前来，\x01",
            "却没能见到面，真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410E")

    Jump("loc_4255")

    label("loc_4113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420A")

    #C0182
    ChrTalk(
        0xA,
        (
            "哎，这不是兰迪先生\x01",
            "和警察弟弟吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x104,
        "#00309F兰小姐，好久不见啦。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#00000F久疏问候。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "这么一说，\x01",
            "好像还真是很久没见了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "难得重逢，\x01",
            "本想和你们多聊聊，\x01",
            "但我现在还要工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        "下次有机会再来找我吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 6)
    Jump("loc_4255")

    label("loc_420A")


    #C0188
    ChrTalk(
        0xA,
        (
            "虽然想和你们多聊聊，\x01",
            "但我现在还要工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        "下次有机会再来找我吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4255")

    TalkEnd(0xFE)
    Return()

    # Function_10_36FC end

    def Function_11_4259(): pass

    label("Function_11_4259")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_42D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4277")
    Call(0, 12)
    Jump("loc_42CB")

    label("loc_4277")


    #C0190
    ChrTalk(
        0xB,
        (
            "咳咳，我的好对手\x01",
            "就是要这样才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "好了，不能让患者久等，\x01",
            "赶快开始诊疗吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42CB")

    Jump("loc_4E3C")

    label("loc_42D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_447B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C6")

    #C0192
    ChrTalk(
        0xB,
        (
            "我和赛兰德一起\x01",
            "查阅了旧医书……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "以生长在自治州内的药草为原料，\x01",
            "应该可以在此调配出\x01",
            "包括麻醉药在内的多种药品。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xB,
        (
            "与雷米菲利亚断绝外交，\x01",
            "医疗物资严重不足的情况虽然还是没有改变……\x01",
            "但似乎已经看到了一点点光明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4476")

    label("loc_43C6")


    #C0195
    ChrTalk(
        0xB,
        (
            "通过和赛兰德一起调查，\x01",
            "发现数种储备不足的药品\x01",
            "都可以在克洛斯贝尔配制。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "与雷米菲利亚断绝外交，\x01",
            "医疗物资严重不足的情况虽然还是没有改变……\x01",
            "但似乎已经看到了一点点光明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4476")

    Jump("loc_4E3C")

    label("loc_447B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4496")
    Call(0, 12)
    Jump("loc_452E")

    label("loc_4496")


    #C0197
    ChrTalk(
        0xB,
        (
            "现在就算留在医院也没有多少事情可做，\x01",
            "本以为盖里教授会因为担心妻儿，\x01",
            "干脆回家去……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "嗯，但他毕竟是个专业医生啊。\x01",
            "……看来我的担心\x01",
            "只是多余的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_452E")

    Jump("loc_4E3C")

    label("loc_4533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_46AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4616")

    #C0199
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔大圣堂\x01",
            "好像也和城市一起\x01",
            "被笼罩在结界中了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "本来还有很多事情\x01",
            "想和艾拉尔达大主教谈谈……\x01",
            "但如今联络不上，也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x105,
        (
            "#10403F（艾拉尔达大主教吗……\x01",
            "  不知他现在正在做些什么。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46A5")

    label("loc_4616")


    #C0202
    ChrTalk(
        0xB,
        (
            "本来还有很多事情\x01",
            "想和艾拉尔达大主教谈谈……\x01",
            "但如今联络不上，也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "或许这也是女神给我们的考验吧。\x01",
            "为了患者们，必须要竭尽全力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46A5")

    Jump("loc_4E3C")

    label("loc_46AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4756")

    #C0204
    ChrTalk(
        0xB,
        (
            "袭击事件中的受害者\x01",
            "并非只有那些\x01",
            "负伤人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "还有不少人受到严重刺激，\x01",
            "从而引发了胃痛\x01",
            "等症状。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        (
            "精神与肉体之间\x01",
            "存在着很紧密的联系呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47C4")

    label("loc_4756")


    #C0207
    ChrTalk(
        0xB,
        (
            "有些人一旦承受过于严重的精神负担，\x01",
            "身体就会产生一些异常状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "精神与肉体之间\x01",
            "存在着很紧密的联系呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C4")

    Jump("loc_4E3C")

    label("loc_47C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4978")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D1")

    #C0209
    ChrTalk(
        0xB,
        (
            "以前，我对用手术刀切割人类身体\x01",
            "这种行为持怀疑态度。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        (
            "但随着时代的进步，文明的发展，\x01",
            "有很多病症，单靠内科是无法处理的。\x01",
            "……就像这次的列车事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xB,
        (
            "既然在医院工作，\x01",
            "不断接受新型医疗方式也是很重要的，\x01",
            "我再次深刻体会到了这一点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4973")

    label("loc_48D1")


    #C0212
    ChrTalk(
        0xB,
        (
            "如今想想，原来那种不接受外科\x01",
            "医疗手术的想法的确是\x01",
            "过于陈腐，缺乏变通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "既然在医院工作，\x01",
            "不断接受新型医疗方式也是很重要的，\x01",
            "我再次深刻体会到了这一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4973")

    Jump("loc_4E3C")

    label("loc_4978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A55")

    #C0214
    ChrTalk(
        0xB,
        (
            "人类身体本身\x01",
            "就拥有治愈外伤与病症\x01",
            "的自愈能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        (
            "内科所开出的处方药，\x01",
            "大多都是以促进这种\x01",
            "『自愈能力』为原理。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xB,
        (
            "在这方面，教会拥有极致的技术。\x01",
            "我们内科医疗就是以教会\x01",
            "的技术为基础的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AE3")

    label("loc_4A55")


    #C0217
    ChrTalk(
        0xB,
        (
            "人类身体本身\x01",
            "就拥有治愈外伤与病症的能力……\x01",
            "也就是所谓的『自愈能力』。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "内科所开出的处方药，\x01",
            "大多都是以促进这种\x01",
            "『自愈能力』为原理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE3")

    Jump("loc_4E3C")

    label("loc_4AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4B31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B03")
    Call(0, 12)
    Jump("loc_4B2C")

    label("loc_4B03")


    #C0219
    ChrTalk(
        0xB,
        (
            "……呼，必须要\x01",
            "冷静一下头脑才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B2C")

    Jump("loc_4E3C")

    label("loc_4B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B4C")
    Call(0, 12)
    Jump("loc_4B62")

    label("loc_4B4C")


    #C0220
    ChrTalk(
        0xB,
        "这个大胡子……！\x02",
    )

    CloseMessageWindow()

    label("loc_4B62")

    Jump("loc_4E3C")

    label("loc_4B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B75")
    Jump("loc_4E3C")

    label("loc_4B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DB4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4CF3")
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0221
    ChrTalk(
        0xB,
        (
            "哦，各位不是警察局的\x01",
            "特别任务支援科成员吗？\x01",
            "你们来得正好。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        (
            "我通过研究『羽扇豆草』\x01",
            "而完成的论文，\x01",
            "明天就要拿到学术讨论会中发表了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xB,
        (
            "正想把这件事情\x01",
            "通知给你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00000F说起羽扇豆草……\x01",
            "就是您以前委托我们去取的那种药草吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        "#00100F呵呵，祝贺您完成了论文。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "嗯，当时多亏有你们帮忙，\x01",
            "请容我再次道谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAC")

    label("loc_4CF3")


    #C0227
    ChrTalk(
        0xB,
        (
            "咳咳，\x01",
            "我是内科的\x01",
            "主任拉格。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        (
            "我通过研究『羽扇豆草』\x01",
            "而完成的论文，\x01",
            "明天就要拿到学术讨论会中发表了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xB,
        (
            "呵呵，真是让人倍感光荣啊。\x01",
            "一定要好好休息，以最佳状态参加学术讨论会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAC")

    SetScenarioFlags(0x159, 7)
    Jump("loc_4E3C")

    label("loc_4DB4")


    #C0230
    ChrTalk(
        0xB,
        (
            "我明天要去外国参加学术讨论会，\x01",
            "并发表关于『羽扇豆草』的论文。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "虽然有位重要的客人要在明天来访医院……\x01",
            "但这次实在是没机会见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3C")

    TalkEnd(0xFE)
    Return()

    # Function_11_4259 end

    def Function_12_4E40(): pass

    label("Function_12_4E40")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FB3")

    #C0232
    ChrTalk(
        0xB,
        (
            "盖里教授，这次的手术\x01",
            "就由我来担任你的助手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xE,
        (
            "那新调制出的麻醉药\x01",
            "就拜托你准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xE,
        (
            "……呵呵，\x01",
            "你今天除了那秃头之外，\x01",
            "其它地方似乎也闪闪发亮呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xB,
        (
            "啧啧，你那一脸\x01",
            "脏兮兮的胡子也一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        (
            "怎么？\x01",
            "难道想让自己看上去像\x01",
            "『黑市医生格伦』一样吗？\x02",
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
            "……呵呵，那就赶快\x01",
            "开始手术吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xB,
        "嗯！\x02",
    )

    CloseMessageWindow()
    Jump("loc_540E")

    label("loc_4FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5158")

    #C0239
    ChrTalk(
        0xB,
        (
            "咳咳，盖里教授。\x01",
            "……那个……该怎么说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "你的妻子和儿子好像\x01",
            "住在克洛斯贝尔市吧……\x01",
            "与他们取得联络了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xE,
        "……不，还没有。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xB,
        "是吗……真让人担心啊。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "……不然你就和\x01",
            "国防军交涉一下，\x01",
            "先回市里如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xE,
        (
            "不……我的妻子和琴兹\x01",
            "都有能力照顾好自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xE,
        (
            "在这个不知道什么时候会有\x01",
            "重伤患者被送到医院的时候，\x01",
            "我绝不能离开这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        "拉格教授，你也一样吧？\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xB,
        (
            "……嗯，说的对。\x01",
            "看来是我多事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_540E")

    label("loc_5158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52B0")

    #C0248
    ChrTalk(
        0xB,
        (
            "赛兰德的手术方案\x01",
            "已经是现在能想出来的\x01",
            "最佳方案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xB,
        (
            "……手术之所以会失败，\x01",
            "主要还是因为你技术不佳吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xE,
        (
            "你说什么……！？明明是你的错吧！\x01",
            "从没做过这种大手术，紧张得\x01",
            "手发抖，所以才造成失误！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xB,
        "#4S你说什么！？\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xE,
        "#4S想打架吗！？\x02",
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
        "……这次暂且作罢吧。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        "……也对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_540E")

    label("loc_52B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_540E")

    #C0255
    ChrTalk(
        0xB,
        (
            "在昨天的学术讨论会上，\x01",
            "我的论文获得了很高评价。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        (
            "哎呀呀，真想让你们也看到\x01",
            "我当时的英姿啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "昨天来医院视察的\x01",
            "阿尔伯特大公\x01",
            "当面激励了我呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "『外科医疗的未来\x01",
            "  就担负在你的肩膀上了』……\x01",
            "哎呀呀，真是让我惶恐万分。\x02",
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
        "#4S别得意忘形，你这胡子脸！\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xE,
        "#4S那是我的台词，你这秃子！\x02",
    )

    CloseMessageWindow()

    label("loc_540E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5421")
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)

    label("loc_5421")

    SetScenarioFlags(0x2, 0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_4E40 end

    def Function_13_542D(): pass

    label("Function_13_542D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C8")

    #C0261
    ChrTalk(
        0xC,
        (
            "发生了如此异常的事态，\x01",
            "导致一些人的身体由于不安而出了问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "处理心理问题并非医生的专长，\x01",
            "但我会尽力陪\x01",
            "患者们谈心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5532")

    label("loc_54C8")


    #C0263
    ChrTalk(
        0xC,
        "心理方面的问题本来是教会所擅长的领域……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "但既然患者特意来医院求助，\x01",
            "我会尽我所能的\x01",
            "陪他们谈心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5532")

    Jump("loc_5B03")

    label("loc_5537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_55D7")

    #C0265
    ChrTalk(
        0xC,
        (
            "为了帮上教授们的忙，\x01",
            "我们已经把保存在研究楼内的\x01",
            "药草样本全部拿出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "虽然如今是特殊时期，\x01",
            "但做些力所能及的事情，\x01",
            "总比什么都不干要好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B03")

    label("loc_55D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_55E5")
    Jump("loc_5B03")

    label("loc_55E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_55F3")
    Jump("loc_5B03")

    label("loc_55F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5601")
    Jump("loc_5B03")

    label("loc_5601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5691")

    #C0267
    ChrTalk(
        0xC,
        (
            "昨天有很多患者被送来，\x01",
            "所以我一直工作到了现在，\x01",
            "体力几乎已经到了极限。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "是不是应该回宿舍\x01",
            "稍微小睡一会呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56EB")

    label("loc_5691")


    #C0269
    ChrTalk(
        0xC,
        (
            "话说回来，\x01",
            "虽然一直在工作，\x01",
            "但教授却仍然充满干劲……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        "我的体力也必须要加强才行。\x02",
    )

    CloseMessageWindow()

    label("loc_56EB")

    Jump("loc_5B03")

    label("loc_56F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_56FE")
    Jump("loc_5B03")

    label("loc_56FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5719")
    Call(0, 37)
    Jump("loc_57B1")

    label("loc_5719")


    #C0271
    ChrTalk(
        0xC,
        (
            "去剧院观赏舞剧，尽兴而归。\x01",
            "回来复查时，发现病已经好了……\x01",
            "我听说过一些这样的病例。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "您最近一直与\x01",
            "孙女一起开心度日，\x01",
            "说不定对身体产生了益处呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57B1")

    Jump("loc_5B03")

    label("loc_57B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_57C4")
    Jump("loc_5B03")

    label("loc_57C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58F2")

    #C0273
    ChrTalk(
        0xC,
        (
            "当得知约亚西姆医生\x01",
            "是那起事件的主谋时，\x01",
            "我真是大受打击呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "新上司赛兰德医生\x01",
            "就任之后，\x01",
            "我还是没有从失落中走出……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "但赛兰德医生这样教导了我——\x01",
            "『只要还有等待救治的患者，\x01",
            "　我们便没有消沉的时间。』\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        (
            "总之，现在我打算在赛兰德医生的\x01",
            "教导下努力工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_596F")

    label("loc_58F2")


    #C0277
    ChrTalk(
        0xC,
        (
            "赛兰德医生给我指派了\x01",
            "很多工作呢。\x01",
            "拜其所赐，连消沉的时间都没有了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xC,
        (
            "哈哈，这种严格的态度\x01",
            "或许也是温柔的一种体现吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596F")

    Jump("loc_5A92")

    label("loc_5974")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A1B")

    #C0279
    ChrTalk(
        0xC,
        (
            "调配出来的药很有效，\x01",
            "状况已经稳定下来了。\x01",
            "这样一来，就可以暂时放心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        (
            "话说回来，大公阁下\x01",
            "似乎拥有相当深厚的医学知识呢。\x01",
            "真想多和他学学啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A92")

    label("loc_5A1B")


    #C0281
    ChrTalk(
        0xC,
        (
            "大公阁下和赛兰德教授\x01",
            "好像很早以前就认识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xC,
        (
            "赛兰德教授就用平时的语气\x01",
            "和大公阁下说话，\x01",
            "总让人觉得有些紧张……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A92")

    Jump("loc_5B03")

    label("loc_5A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AB2")
    Call(0, 39)
    Jump("loc_5B03")

    label("loc_5AB2")


    #C0283
    ChrTalk(
        0xC,
        (
            "奎因爷爷愿意\x01",
            "服用药物，\x01",
            "我真是很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "这也多亏了亚米萨\x01",
            "一直努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B03")

    TalkEnd(0xFE)
    Return()

    # Function_13_542D end

    def Function_14_5B07(): pass

    label("Function_14_5B07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BA3")

    #C0285
    ChrTalk(
        0xD,
        (
            "一下子有这么多患者入院，\x01",
            "实在是非常繁忙……但我会努力的！\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "虽然我现在还差得很远，\x01",
            "但总有一天会成为像\x01",
            "赛兰德教授那样出色的女医生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6380")

    label("loc_5BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5C13")

    #C0287
    ChrTalk(
        0xD,
        (
            "没想到，民间疗法似乎\x01",
            "也有一定参考价值呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xD,
        (
            "宿舍的书架上应该还放着一些，\x01",
            "稍后去找找好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6380")

    label("loc_5C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CBE")

    #C0289
    ChrTalk(
        0xD,
        (
            "我正在整理国防军\x01",
            "配发的药品……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xD,
        (
            "感觉完全就是一些外行人\x01",
            "选配的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xD,
        (
            "虽然医院现在还能\x01",
            "勉强应付，\x01",
            "但终究无法医治那些重病患者……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5D36")

    label("loc_5CBE")


    #C0292
    ChrTalk(
        0xD,
        (
            "国防军配发的药品\x01",
            "完全就是一些外行人\x01",
            "选配的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xD,
        (
            "虽然医院现在还能\x01",
            "勉强应付，\x01",
            "但终究无法医治那些重病患者……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D36")

    Jump("loc_6380")

    label("loc_5D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5DAA")

    #C0294
    ChrTalk(
        0xD,
        (
            "虽说医院现在暂停接待门诊患者了，\x01",
            "但重病患者随时都有可能被送来。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xD,
        "仍然要做好充分的准备。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6380")

    label("loc_5DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA5")

    #C0296
    ChrTalk(
        0xD,
        (
            "『身为医生，在这种特殊时期\x01",
            "　就更要表现得沉着冷静』——\x01",
            "拉格教授是这样教导我的。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xD,
        (
            "如果连我们都一脸惊慌，\x01",
            "患者们就会被那种负面情绪感染了。\x01",
            "必须要注意这一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xD,
        (
            "从某种意义上说，\x01",
            "不安其实也是一种\x01",
            "类似疾病的东西。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F21")

    label("loc_5EA5")


    #C0299
    ChrTalk(
        0xD,
        (
            "『身为医生，在这种特殊时期\x01",
            "　就更要表现得沉着冷静』……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xD,
        (
            "……我虽然心里也明白这一点，\x01",
            "但想实际做到，还是很难啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F21")

    Jump("loc_6380")

    label("loc_5F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6034")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD4")

    #C0301
    ChrTalk(
        0xD,
        (
            "如果被雨淋湿，\x01",
            "就很容易感冒。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xD,
        (
            "这是因为自身的免疫系统\x01",
            "由于气温寒冷而\x01",
            "停止了运作。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        (
            "你们回家以后，\x01",
            "可别忘了换上干衣服，\x01",
            "好好暖暖身体。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_602F")

    label("loc_5FD4")


    #C0304
    ChrTalk(
        0xD,
        (
            "如果被雨淋湿，\x01",
            "就很容易感冒。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xD,
        (
            "你们回家以后，\x01",
            "可别忘了换上干衣服，\x01",
            "好好暖暖身体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602F")

    Jump("loc_6380")

    label("loc_6034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_60B7")

    #C0306
    ChrTalk(
        0xD,
        (
            "利顿最近好像\x01",
            "经常负责去病房巡诊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xD,
        (
            "唔唔唔，我也不能输给他啊。\x01",
            "我一定会成为一名\x01",
            "深受患者信赖的优秀女医生！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6380")

    label("loc_60B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_60C5")
    Jump("loc_6380")

    label("loc_60C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6164")

    #C0308
    ChrTalk(
        0xD,
        (
            "哎呀呀，两位教授\x01",
            "又吵起来了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xD,
        (
            "在这种时候，\x01",
            "外人不过去插嘴劝架，\x01",
            "反而会更快结束呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "我不如趁现在\x01",
            "整理整理病历吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_61AE")

    label("loc_6164")


    #C0311
    ChrTalk(
        0xD,
        (
            "我已经对两位教授的争吵\x01",
            "习以为常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xD,
        (
            "不如趁现在\x01",
            "整理整理病历吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61AE")

    Jump("loc_6380")

    label("loc_61B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_625F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621D")

    #C0313
    ChrTalk(
        0xD,
        (
            "教授果然\x01",
            "很棒啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xD,
        (
            "……不行不行，\x01",
            "我现在必须要做好\x01",
            "自己该做的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_625A")

    label("loc_621D")


    #C0315
    ChrTalk(
        0xD,
        (
            "说起来，\x01",
            "我可真是丢脸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xD,
        "必须要更加努力学习才行。\x02",
    )

    CloseMessageWindow()

    label("loc_625A")

    Jump("loc_6380")

    label("loc_625F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6324")

    #C0317
    ChrTalk(
        0xD,
        (
            "最近这段时间，同宿舍的芙萝拉\x01",
            "似乎在照料新人实习医生呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xD,
        (
            "是叫米修吧……\x01",
            "不知为何，让我想起了\x01",
            "新人时代的自己呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xD,
        (
            "哈，但我如今也仍在学习，\x01",
            "这一点倒是没有变。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6380")

    label("loc_6324")


    #C0320
    ChrTalk(
        0xD,
        (
            "一看到米修，\x01",
            "不知为何，就让我想起了\x01",
            "新人时代的自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xD,
        "哈，不过我如今也仍在学习呢。\x02",
    )

    CloseMessageWindow()

    label("loc_6380")

    TalkEnd(0xFE)
    Return()

    # Function_14_5B07 end

    def Function_15_6384(): pass

    label("Function_15_6384")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_641A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63A2")
    Call(0, 12)
    Jump("loc_6415")

    label("loc_63A2")


    #C0322
    ChrTalk(
        0xE,
        (
            "我虽然讨厌拉格教授，\x01",
            "但没有比他更加值得信赖\x01",
            "的协助者了。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xE,
        (
            "呵呵，无论是什么样的手术，\x01",
            "如今也都不足为惧了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6415")

    Jump("loc_6C8B")

    label("loc_641A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C5")

    #C0324
    ChrTalk(
        0xE,
        (
            "听说内科和神经·药物学科的\x01",
            "医生们准备想办法解决\x01",
            "医疗物资不足的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xE,
        (
            "……如今没有手术要做，\x01",
            "不如趁着工作的闲暇，\x01",
            "去帮帮阿修拉他们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_652B")

    label("loc_64C5")


    #C0326
    ChrTalk(
        0xE,
        (
            "我就趁着工作的闲暇，\x01",
            "去帮帮阿修拉他们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xE,
        (
            "必须要做好万全的准备，\x01",
            "从而保证随时可以开始手术。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_652B")

    Jump("loc_6C8B")

    label("loc_6530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_65B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654B")
    Call(0, 12)
    Jump("loc_65B0")

    label("loc_654B")


    #C0328
    ChrTalk(
        0xE,
        (
            "……拉格教授偶尔也会\x01",
            "说些体贴的话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xE,
        (
            "呼，我的妻子和琴兹\x01",
            "一定都没问题，\x01",
            "所以不必担心他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65B0")

    Jump("loc_6C8B")

    label("loc_65B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6678")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6621")

    #C0330
    ChrTalk(
        0xE,
        (
            "……生活在市里的\x01",
            "妻子和琴兹\x01",
            "现在不知过得怎样。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xE,
        (
            "但愿他们别生\x01",
            "什么病……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6673")

    label("loc_6621")


    #C0332
    ChrTalk(
        0xE,
        "……呼，应该不需要担心。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xE,
        (
            "既然没被送到这里，\x01",
            "我妻子和琴兹\x01",
            "就一定很健康。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6673")

    Jump("loc_6C8B")

    label("loc_6678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_676F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671E")

    #C0334
    ChrTalk(
        0xE,
        (
            "我在医院工作了这么多年，\x01",
            "还是第一次看到\x01",
            "入院患者把病房挤满的情况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xE,
        (
            "这可真算是前所未有的事态啊，\x01",
            "无论如何也要想办法渡过难关……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_676A")

    label("loc_671E")


    #C0336
    ChrTalk(
        0xE,
        (
            "这种状况……\x01",
            "真可以称得上是前所未有啊，\x01",
            "无论如何也要想办法渡过难关……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676A")

    Jump("loc_6C8B")

    label("loc_676F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6823")

    #C0337
    ChrTalk(
        0xE,
        (
            "呼……大部分的手术总算在不久之前\x01",
            "告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xE,
        (
            "毕竟患者的数量实在太多了，\x01",
            "一直处理到了天亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xE,
        (
            "等今天的诊断工作结束以后，\x01",
            "真想蒙头睡个够啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_688F")

    label("loc_6823")


    #C0340
    ChrTalk(
        0xE,
        (
            "手术一直做到了天亮，实在是很累……\x01",
            "但不能让患者等待。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xE,
        (
            "在今天的诊断工作结束之前，\x01",
            "一定要坚持下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_688F")

    Jump("loc_6C8B")

    label("loc_6894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_69C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6947")

    #C0342
    ChrTalk(
        0xE,
        (
            "我儿子琴兹最近\x01",
            "好像正在烦恼着什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xE,
        (
            "呼，医院的工作太忙了，\x01",
            "要操心的事真多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xE,
        (
            "若是处理不善，\x01",
            "说不定就会落得让拉格教授\x01",
            "治疗胃痛的窘境了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_69BC")

    label("loc_6947")


    #C0345
    ChrTalk(
        0xE,
        (
            "哎呀呀，无论公私，\x01",
            "都有数不清的事情让人操心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xE,
        (
            "若是处理不善，\x01",
            "说不定就会落得让拉格教授\x01",
            "治疗胃痛的窘境了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69BC")

    Jump("loc_6C8B")

    label("loc_69C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69DC")
    Call(0, 12)
    Jump("loc_6A57")

    label("loc_69DC")


    #C0347
    ChrTalk(
        0xE,
        (
            "我们也参加了手术，\x01",
            "这次真是深刻\x01",
            "体会到了自己的无能啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        (
            "这次的失败是否会让患者陷入绝望……\x01",
            "我最在意的只有这件事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A57")

    Jump("loc_6C8B")

    label("loc_6A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A77")
    Call(0, 12)
    Jump("loc_6A99")

    label("loc_6A77")


    #C0349
    ChrTalk(
        0xE,
        "不要得意忘形，你这秃子……！\x02",
    )

    CloseMessageWindow()

    label("loc_6A99")

    Jump("loc_6C8B")

    label("loc_6A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B6E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6AFF")

    #C0350
    ChrTalk(
        0xE,
        "听说大公阁下已经走了……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xE,
        (
            "哎呀呀……\x01",
            "阿修拉也真是让人头疼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B69")

    label("loc_6AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B11")
    Call(0, 16)
    Jump("loc_6B69")

    label("loc_6B11")


    #C0352
    ChrTalk(
        0xE,
        (
            "大公阁下难得来视察，\x01",
            "她却还是那样我行我素……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xE,
        (
            "必须要严厉批评\x01",
            "阿修拉才行……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B69")

    Jump("loc_6C8B")

    label("loc_6B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1F")

    #C0354
    ChrTalk(
        0xE,
        (
            "可恶的拉格教授，\x01",
            "竟敢如此得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xE,
        (
            "每次见面，\x01",
            "都不忘记炫耀一番。\x01",
            "真是的，那个死秃子……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xE,
        (
            "……呼，不过那家伙的研究\x01",
            "确实有值得赞赏之处。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C8B")

    label("loc_6C1F")


    #C0357
    ChrTalk(
        0xE,
        (
            "我也不得不承认\x01",
            "拉格教授的研究成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xE,
        (
            "虽然他那副得意忘形的嘴脸让人生气……\x01",
            "哼，但这次就忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C8B")

    TalkEnd(0xFE)
    Return()

    # Function_15_6384 end

    def Function_16_6C8F(): pass

    label("Function_16_6C8F")

    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0359
    ChrTalk(
        0xE,
        (
            "夏、夏鲁鲁，\x01",
            "阿修拉又睡过头了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x10,
        (
            "嗯，应该是。\x01",
            "……她昨天在研究室里\x01",
            "一直研究到很晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xE,
        (
            "大、大公阁下\x01",
            "特意前来视察，\x01",
            "她竟然如此不成体统……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xE,
        (
            "可恶！无论用什么办法，\x01",
            "也要给我把她叫醒！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_16_6C8F end

    def Function_17_6D75(): pass

    label("Function_17_6D75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E1E")

    #C0363
    ChrTalk(
        0xF,
        (
            "出现在湿地附近的那棵\x01",
            "巨树真是惊人啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "它是凭借什么原理，又是为了何种\x01",
            "目的而出现在那里的呢……\x01",
            "其中的科学性真是让我兴趣十足啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6EA1")

    label("loc_6E1E")


    #C0365
    ChrTalk(
        0xF,
        (
            "……呼，一不小心就得意忘形了。\x01",
            "抱歉，在这种时期，真是不应该……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xF,
        (
            "总之，现在要专心接待患者，\x01",
            "以及维护各种医疗设备，\x01",
            "对吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EA1")

    Jump("loc_79D4")

    label("loc_6EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F3D")

    #C0367
    ChrTalk(
        0xF,
        "（昏昏欲睡）……\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xF,
        (
            "为了预防新式医疗设备损坏，\x01",
            "我正在检查旧式设备～\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xF,
        (
            "呼啊啊啊～虽然很困，\x01",
            "但必须要坚持下去啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6FD2")

    label("loc_6F3D")


    #C0370
    ChrTalk(
        0xF,
        (
            "（昏昏欲睡）……\x01",
            "话说回来，没想到这些\x01",
            "旧式设备竟然如此结实～\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xF,
        (
            "旧式设备大多都体积巨大，外形粗糙，\x01",
            "如果躺在上面睡觉，大概会非常冰凉舒服吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FD2")

    Jump("loc_79D4")

    label("loc_6FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7124")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709C")

    #C0372
    ChrTalk(
        0xF,
        (
            "总算找到老化零件\x01",
            "的备用品了～\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xF,
        (
            "不过这都是些特殊的零件，\x01",
            "下次如果再需要，就只能\x01",
            "从雷米菲利亚进口才能得到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xF,
        (
            "呼，真是让人头疼啊。\x01",
            "必须要万分小心地使用了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_711F")

    label("loc_709C")


    #C0375
    ChrTalk(
        0xF,
        (
            "医院中所使用的医疗设备都包含特殊零件，\x01",
            "必须要从雷米菲利亚进口\x01",
            "才能得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xF,
        (
            "呼，真是让人头疼啊。\x01",
            "必须要万分小心地使用了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_711F")

    Jump("loc_79D4")

    label("loc_7124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7345")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72BD")
    TurnDirection(0xFE, 0x103, 0)

    #C0377
    ChrTalk(
        0xF,
        "啊，小缇欧。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xF,
        (
            "我正在维护\x01",
            "医疗设备……\x01",
            "你对这个数值有何看法？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x103,
        (
            "#00200F嗯……耐久力似乎比\x01",
            "规定值低了一些呢。\x02\x03",

            "#00203F恐怕是运转部位的零件\x01",
            "由于常年磨损，出现了老化现象。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xF,
        (
            "果然是这样啊。\x01",
            "嗯……真让人头疼啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#00000F（缇欧经过这段时期的医院生活，\x01",
            "  似乎已经和大家相处得十分融洽了呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x105,
        (
            "#10402F（呵呵，在导力器械的领域，\x01",
            "  她应该能发挥很大作用吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7340")

    label("loc_72BD")


    #C0383
    ChrTalk(
        0xF,
        (
            "嗯，这可难办了。\x01",
            "这是赛兰德公司制造的产品，\x01",
            "目前无法获得新品……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xF,
        (
            "不过，总要试着想想办法啊。\x01",
            "总之，我这就去找找备用零件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7340")

    Jump("loc_79D4")

    label("loc_7345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_746B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73F6")

    #C0385
    ChrTalk(
        0xF,
        (
            "嗯……接下来还要去研究楼\x01",
            "的集中治疗室巡诊……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xF,
        (
            "另外，必须要去检查\x01",
            "多诺邦警督使用的\x01",
            "人工呼吸机。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xF,
        (
            "呼，工作一下增加了这么多，\x01",
            "真是太忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7466")

    label("loc_73F6")


    #C0388
    ChrTalk(
        0xF,
        (
            "呼，工作一下增加了这么多，\x01",
            "真是太忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xF,
        (
            "要想回归原来那种全心沉浸于研究的生活，\x01",
            "恐怕要等上好一阵子了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7466")

    Jump("loc_79D4")

    label("loc_746B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74E7")

    #C0390
    ChrTalk(
        0xF,
        (
            "手术用的医疗器械\x01",
            "在昨天派上了很大用场。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xF,
        (
            "我平时一直都拜托\x01",
            "夏鲁鲁用心维护，\x01",
            "真是太好了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7521")

    label("loc_74E7")


    #C0392
    ChrTalk(
        0xF,
        (
            "各位实习医生\x01",
            "都是很优秀的孩子，\x01",
            "实在是帮了我的大忙～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7521")

    Jump("loc_79D4")

    label("loc_7526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_766D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_760E")

    #C0393
    ChrTalk(
        0xF,
        (
            "（昏昏欲睡）……\x01",
            "……啊，对了！\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xF,
        (
            "应用感光回路的原理，\x01",
            "制作将视觉情报传送到脑部的装置，\x01",
            "说不定就可以实现模拟视力……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xF,
        (
            "（敲击键盘……）\x01",
            "……嗯～果然不行。\x01",
            "如果这样，开发工作大概要耗费几十年……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7668")

    label("loc_760E")


    #C0396
    ChrTalk(
        0xF,
        (
            "不行啊～\x01",
            "我果然还是不行吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xF,
        (
            "……不！还是不能放弃。\x01",
            "为了小滴，我也要继续努力！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7668")

    Jump("loc_79D4")

    label("loc_766D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_779C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_772E")

    #C0398
    ChrTalk(
        0xF,
        (
            "在小滴的这场手术中所使用\x01",
            "的设备，可以称得上现代医疗\x01",
            "史上最先进的设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xF,
        (
            "但最后却还是失败了……\x01",
            "呜呜，实在难以接受啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xF,
        (
            "真是对不起那么\x01",
            "信任我们的小滴……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7797")

    label("loc_772E")


    #C0401
    ChrTalk(
        0xF,
        (
            "科学会给人带来幸福……\x01",
            "所以我一直坚持\x01",
            "在医疗器械科进行研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xF,
        (
            "真是对不起那么\x01",
            "信任我们的小滴……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7797")

    Jump("loc_79D4")

    label("loc_779C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_784E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77B7")
    Call(0, 18)
    Jump("loc_7849")

    label("loc_77B7")

    OP_4B(0x10, 0xFF)

    #C0403
    ChrTalk(
        0xF,
        (
            "……嗯，非常完美！\x01",
            "这次进展得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xF,
        (
            "呵呵，照这个势头，\x01",
            "今天大概就能进展到耐久测试阶段了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x10,
        "（今天大概又要通宵了吧……）\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_7849")

    Jump("loc_79D4")

    label("loc_784E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_785C")
    Jump("loc_79D4")

    label("loc_785C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_79D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7957")

    #C0406
    ChrTalk(
        0xF,
        (
            "在听说赛兰德教授\x01",
            "要来这里任职的时候，\x01",
            "我真是高兴得快要跳起来了～\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xF,
        (
            "由于工作原因，\x01",
            "每天都要接触到『赛兰德公司』\x01",
            "这个一流医疗器械公司的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xF,
        (
            "据说赛兰德教授是经理的亲戚……\x01",
            "呵呵呵，希望她能给我\x01",
            "讲一些公司的秘闻。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_79D4")

    label("loc_7957")


    #C0409
    ChrTalk(
        0xF,
        (
            "不过……不知为何，\x01",
            "总觉得赛兰德教授有点可怕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xF,
        (
            "虽然很想打听有关\x01",
            "赛兰德公司的各种内幕……\x01",
            "但总是找不到开口的机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79D4")

    TalkEnd(0xFE)
    Return()

    # Function_17_6D75 end

    def Function_18_79D8(): pass

    label("Function_18_79D8")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0411
    ChrTalk(
        0xF,
        (
            "好，夏鲁鲁，\x01",
            "我已经准备完毕啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xF,
        (
            "现在就要打开开关，\x01",
            "导力压的调整就拜托你了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0413
    ChrTalk(
        0x10,
        (
            "知道了，\x01",
            "……希望这次\x01",
            "别再爆炸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xF,
        (
            "就算爆炸也不要在意¤\x01",
            "失败是成功之母嘛。\x02",
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
            "#00211F（……虽然说的没错，\x01",
            "  但真是很危险呢。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x2, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x5A, 0x0)
    Return()

    # Function_18_79D8 end

    def Function_19_7B45(): pass

    label("Function_19_7B45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BF5")

    #C0416
    ChrTalk(
        0x10,
        (
            "主任本想小睡一阵，\x01",
            "但看到那棵大树出现之后，\x01",
            "马上就变得精神十足了。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x10,
        (
            "这样的话，主任大概是要\x01",
            "连续工作三天三夜了吧。\x01",
            "我也必须要努力撑下去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7C64")

    label("loc_7BF5")


    #C0418
    ChrTalk(
        0x10,
        (
            "帝国的内战，\x01",
            "还有那棵蓝白色的大树……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x10,
        (
            "虽然很多事情都让人担心，\x01",
            "但现在还是集中精神，\x01",
            "协助主任工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C64")

    Jump("loc_86DD")

    label("loc_7C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7D78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D1A")

    #C0420
    ChrTalk(
        0x10,
        (
            "唔……虽然性能很低，\x01",
            "但在关键时刻应该也能当作替代品。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x10,
        (
            "要检查的零件太多了，\x01",
            "所以工作了整整一通宵……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x10,
        "……呼，还好我已经习惯熬夜工作了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D73")

    label("loc_7D1A")


    #C0423
    ChrTalk(
        0x10,
        (
            "已经工作了一个通宵，\x01",
            "阿修拉主任都快睡着了。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x10,
        "……呼，还好我已经习惯熬夜工作了。\x02",
    )

    CloseMessageWindow()

    label("loc_7D73")

    Jump("loc_86DD")

    label("loc_7D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7E14")

    #C0425
    ChrTalk(
        0x10,
        (
            "盖里教授肯定很担心自己的家人，\x01",
            "但他仍然能集中精神，\x01",
            "专心处理医院的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x10,
        (
            "……我也要相信自己家人平安无事，\x01",
            "专心协助\x01",
            "阿修拉主任工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86DD")

    label("loc_7E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF3")

    #C0427
    ChrTalk(
        0x10,
        (
            "在克洛斯贝尔独立之前，\x01",
            "帝国曾发来了撤离通告，\x01",
            "但我还是留在了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x10,
        (
            "因为我还有很多东西要学习，\x01",
            "绝不能现在就\x01",
            "回归家乡。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x10,
        (
            "……不过，也有些担心\x01",
            "帝国发生的内战呢。\x01",
            "但愿家人们平安无事……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7F65")

    label("loc_7EF3")


    #C0430
    ChrTalk(
        0x10,
        (
            "事到如今，我并不会为留在\x01",
            "克洛斯贝尔的选择感到后悔。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x10,
        (
            "……但还是很担心帝国的内战。\x01",
            "但愿家人们平安无事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F65")

    Jump("loc_86DD")

    label("loc_7F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_80B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_803D")

    #C0432
    ChrTalk(
        0x10,
        (
            "很多人都在暗中议论，\x01",
            "说这次的袭击事件\x01",
            "是帝国政府策动的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x10,
        (
            "这场导致无数人受伤入院\x01",
            "的事件难道是帝国策动的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x10,
        (
            "虽然并不想说家乡的坏话，\x01",
            "但如果这是真的，我会深感鄙视。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_80AF")

    label("loc_803D")


    #C0435
    ChrTalk(
        0x10,
        (
            "我的目标本是在故乡——\x01",
            "帝国经营一家医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x10,
        (
            "但如果这场阴谋真的是由帝国政府策动的，\x01",
            "我会鄙视自己的故乡。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80AF")

    Jump("loc_86DD")

    label("loc_80B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_81DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8191")

    #C0437
    ChrTalk(
        0x10,
        (
            "医疗器械这种东西，\x01",
            "在平时就必须要\x01",
            "坚持维护。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x10,
        (
            "如果由于医疗器械的故障\x01",
            "而导致患者出了什么问题，\x01",
            "那可就真是本末倒置了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x10,
        (
            "为了确保随时都可以\x01",
            "救治被送来的患者，\x01",
            "必须要认真维护设备才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_81D5")

    label("loc_8191")


    #C0440
    ChrTalk(
        0x10,
        (
            "为了确保随时都可以\x01",
            "救治被送来的患者，\x01",
            "必须要认真维护设备才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81D5")

    Jump("loc_86DD")

    label("loc_81DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_831C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82A3")

    #C0441
    ChrTalk(
        0x10,
        (
            "自从小滴的手术结束之后，\x01",
            "主任就一直在不眠不休地研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x10,
        (
            "好像是在摸索\x01",
            "使用导力器来治疗\x01",
            "小滴眼睛的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x10,
        (
            "主任果然很了不起啊……\x01",
            "那种超前的想法，我连想都没有想过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8317")

    label("loc_82A3")


    #C0444
    ChrTalk(
        0x10,
        (
            "使用导力器来恢复视力吗……\x01",
            "我真是连想都没有想过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x10,
        (
            "不过，这涉及了神经科的领域……\x01",
            "实现起来恐怕很困难吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8317")

    Jump("loc_86DD")

    label("loc_831C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83D8")

    #C0446
    ChrTalk(
        0x10,
        (
            "在那场手术中，教授们\x01",
            "全都尽到了最大努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x10,
        (
            "但即使如此，小滴的视力也没能完全恢复，\x01",
            "唯一可说的也只有遗憾了……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x10,
        (
            "但就我个人来说，\x01",
            "希望大家不要太消沉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8432")

    label("loc_83D8")


    #C0449
    ChrTalk(
        0x10,
        (
            "在那场手术中，教授们\x01",
            "都已经尽到最大努力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x10,
        (
            "就我个人来说，\x01",
            "希望大家不要太消沉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8432")

    Jump("loc_86DD")

    label("loc_8437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_84CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8452")
    Call(0, 18)
    Jump("loc_84C6")

    label("loc_8452")


    #C0451
    ChrTalk(
        0x10,
        (
            "阿修拉主任无论\x01",
            "经过多少次失败也都不会放弃的。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x10,
        (
            "身为医疗器械的研究员，\x01",
            "这种永不放弃的精神或许是最该学习的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84C6")

    Jump("loc_86DD")

    label("loc_84CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_85B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_855C")

    #C0453
    ChrTalk(
        0x10,
        (
            "阿修拉主任\x01",
            "最后也没能赶上呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x10,
        (
            "算了，毕竟主任昨天工作了\x01",
            "一个通宵，让她在大公视察\x01",
            "的时间起床终究是不太可能。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85B2")

    label("loc_855C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856E")
    Call(0, 16)
    Jump("loc_85B2")

    label("loc_856E")


    #C0455
    ChrTalk(
        0x10,
        (
            "阿修拉主任经常\x01",
            "彻夜进行研究。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x10,
        (
            "现在大概还在\x01",
            "宿舍里睡觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85B2")

    Jump("loc_86DD")

    label("loc_85B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_86DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8685")

    #C0457
    ChrTalk(
        0x10,
        (
            "阿修拉主任是\x01",
            "医疗器械的专家。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x10,
        (
            "她以前好像曾在自己老家——\x01",
            "列曼自治州的爱普斯泰恩财团总部\x01",
            "学习过导力器械的基础知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x10,
        (
            "我在主任的指导下，\x01",
            "帮忙研究各种各样的\x01",
            "医疗器械。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_86DD")

    label("loc_8685")


    #C0460
    ChrTalk(
        0x10,
        (
            "医疗器械在现代医疗技术中\x01",
            "必不可缺。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x10,
        (
            "我深信这方面的研究\x01",
            "可以拓展医学界的未来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86DD")

    TalkEnd(0xFE)
    Return()

    # Function_19_7B45 end

    def Function_20_86E1(): pass

    label("Function_20_86E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8757")

    #C0462
    ChrTalk(
        0x11,
        "医院能再次接收门诊患者，总算可以安心了。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x11,
        (
            "原本一直都在担心，\x01",
            "如果之前拿的药用完了该怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E9")

    label("loc_8757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8765")
    Jump("loc_89E9")

    label("loc_8765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8773")
    Jump("loc_89E9")

    label("loc_8773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_87FB")

    #C0464
    ChrTalk(
        0x11,
        (
            "嗯……一直都没叫我去见医生……\x01",
            "看来有相当多的人在等待诊断呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x11,
        (
            "发生了那样的袭击事件，\x01",
            "医生们应该也非常忙碌吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E9")

    label("loc_87FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8809")
    Jump("loc_89E9")

    label("loc_8809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_886C")

    #C0466
    ChrTalk(
        0x11,
        "我今天一大早就预约好问诊了。\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x11,
        (
            "使用导力网络就可以完成预约，\x01",
            "的确是很方便呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E9")

    label("loc_886C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_887A")
    Jump("loc_89E9")

    label("loc_887A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8914")

    #C0468
    ChrTalk(
        0x11,
        (
            "在昨天的揭幕式上，\x01",
            "我一直抬头仰望\x01",
            "那个兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x11,
        (
            "但好像是身体挺得太用力了，\x01",
            "一不小心把腰给扭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x11,
        "疼疼疼疼疼……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_895B")

    label("loc_8914")


    #C0471
    ChrTalk(
        0x11,
        (
            "参观兰花塔时一直在仰视，\x01",
            "一不小心把腰给扭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x11,
        "疼疼疼疼疼……\x02",
    )

    CloseMessageWindow()

    label("loc_895B")

    Jump("loc_89E9")

    label("loc_8960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_896E")
    Jump("loc_89E9")

    label("loc_896E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_89E9")

    #C0473
    ChrTalk(
        0x11,
        (
            "教团事件结束之后，\x01",
            "医院迅速展开调查，\x01",
            "证明了自身的清白。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x11,
        (
            "如此一来，\x01",
            "就可以放心来医院了，\x01",
            "真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89E9")

    TalkEnd(0xFE)
    Return()

    # Function_20_86E1 end

    def Function_21_89ED(): pass

    label("Function_21_89ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8A75")

    #C0475
    ChrTalk(
        0x12,
        (
            "对我们这些上了年纪的人来说，\x01",
            "能否来医院看病\x01",
            "可是一个很重要的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x12,
        (
            "如今终于可以放心来医院了，\x01",
            "真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD2")

    label("loc_8A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8A83")
    Jump("loc_8CD2")

    label("loc_8A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8A91")
    Jump("loc_8CD2")

    label("loc_8A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8AE6")

    #C0477
    ChrTalk(
        0x12,
        (
            "呼……克洛斯贝尔\x01",
            "真的没问题吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x12,
        "太过不安，晚上都睡不着……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CD2")

    label("loc_8AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8B3E")

    #C0479
    ChrTalk(
        0x12,
        (
            "竟然发生了列车事故……\x01",
            "真是让人震惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x12,
        (
            "不知那些乘客\x01",
            "是否安好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD2")

    label("loc_8B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8B4C")
    Jump("loc_8CD2")

    label("loc_8B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8BB2")

    #C0481
    ChrTalk(
        0x12,
        (
            "短时间内，我还要继续\x01",
            "来医院检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x12,
        (
            "医生们的手术做得很好，\x01",
            "我可以放心前来检查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD2")

    label("loc_8BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8BC0")
    Jump("loc_8CD2")

    label("loc_8BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8C3B")

    #C0483
    ChrTalk(
        0x12,
        (
            "我经常找的拉格医生\x01",
            "今天好像休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x12,
        (
            "那个叫赛兰德的医生\x01",
            "虽然是名教授，但也太年轻了，\x01",
            "不会有问题吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CD2")

    label("loc_8C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8CD2")

    #C0485
    ChrTalk(
        0x12,
        (
            "约亚西姆医生竟然\x01",
            "会引起那么恐怖的事件，\x01",
            "我直到现在都难以相信。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x12,
        (
            "啊啊，好可怕啊……\x01",
            "别人的脑子里究竟在想些什么，\x01",
            "真是完全都猜不到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD2")

    TalkEnd(0xFE)
    Return()

    # Function_21_89ED end

    def Function_22_8CD6(): pass

    label("Function_22_8CD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8D83")

    #C0487
    ChrTalk(
        0x13,
        (
            "在迪塔总统被拘捕之前，\x01",
            "如果只是小病，\x01",
            "就不允许去医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x13,
        (
            "但在父母眼里，就算孩子只是\x01",
            "患上感冒，也是很严重的问题。\x01",
            "当时真的很希望他能更体贴市民一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9085")

    label("loc_8D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8D91")
    Jump("loc_9085")

    label("loc_8D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8D9F")
    Jump("loc_9085")

    label("loc_8D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8DD8")

    #C0489
    ChrTalk(
        0x13,
        "喂……安静些。\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x13,
        (
            "不能影响到\x01",
            "别人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9085")

    label("loc_8DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8E73")

    #C0491
    ChrTalk(
        0x13,
        (
            "我们也乘坐了那辆\x01",
            "脱轨的列车……\x01",
            "但运气还不错，只是受了点轻伤而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x13,
        (
            "只休养了一天就可以出院，算是值得庆幸。\x01",
            "自那之后，铁路怎样了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9085")

    label("loc_8E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8E81")
    Jump("loc_9085")

    label("loc_8E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5F")

    #C0493
    ChrTalk(
        0x13,
        (
            "之前做健康检查时，\x01",
            "查出我吃的甜食太多，\x01",
            "还遭到警告了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x13,
        (
            "如果再这样下去，恐怕对身体很不好，\x01",
            "必须要改正不良生活习惯了。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x13,
        (
            "话是这么说，但我一看到\x01",
            "甜食就忍不住想吃。\x01",
            "必须得克制自己了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8FAB")

    label("loc_8F5F")


    #C0496
    ChrTalk(
        0x13,
        (
            "我一看到甜食\x01",
            "就忍不住想吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x13,
        (
            "身体毕竟是自己的，\x01",
            "必须得小心在意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FAB")

    Jump("loc_9085")

    label("loc_8FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8FBE")
    Jump("loc_9085")

    label("loc_8FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_907C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9023")

    #C0498
    ChrTalk(
        0x13,
        "嗯～这个味道真好闻。\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x13,
        (
            "这种香气大概可以\x01",
            "缓和患者们的情绪吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_9077")

    label("loc_9023")


    #C0500
    ChrTalk(
        0x13,
        (
            "我是来医院\x01",
            "照顾母亲的。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x13,
        (
            "这里好像有很多稀奇的东西，\x01",
            "不然就去探险一番好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9077")

    Jump("loc_9085")

    label("loc_907C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9085")

    label("loc_9085")

    TalkEnd(0xFE)
    Return()

    # Function_22_8CD6 end

    def Function_23_9089(): pass

    label("Function_23_9089")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_90F4")

    #C0502
    ChrTalk(
        0x14,
        (
            "总算来到医院了，\x01",
            "但这里的人还真多啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x14,
        (
            "医生们想必也很辛苦吧，\x01",
            "希望他们能加油。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93F0")

    label("loc_90F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9102")
    Jump("loc_93F0")

    label("loc_9102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9110")
    Jump("loc_93F0")

    label("loc_9110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_911E")
    Jump("loc_93F0")

    label("loc_911E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_91A3")

    #C0504
    ChrTalk(
        0x14,
        (
            "话说回来，\x01",
            "这还真是一起恐怖的事故啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x14,
        (
            "由于发生得太过突然，\x01",
            "直到现在我都不明原委……\x01",
            "事故的原因究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93F0")

    label("loc_91A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9230")

    #C0506
    ChrTalk(
        0x14,
        (
            "做了些家务事之后，\x01",
            "腰就开始痛了。\x01",
            "真是不愿意变老啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x14,
        (
            "你们也要注意哦。\x01",
            "到了三四十岁以后，就能明显感觉到身体开始衰退。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93F0")

    label("loc_9230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_923E")
    Jump("loc_93F0")

    label("loc_923E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_92A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9259")
    Call(0, 24)
    Jump("loc_929D")

    label("loc_9259")


    #C0508
    ChrTalk(
        0x14,
        (
            "唔～鼻涕怎么都\x01",
            "止不住啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x14,
        (
            "在叫到号之前，\x01",
            "只能安静等着了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_929D")

    Jump("loc_93F0")

    label("loc_92A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_92B0")
    Jump("loc_93F0")

    label("loc_92B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_93F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9380")

    #C0510
    ChrTalk(
        0x14,
        (
            "最近这段时间，药品的说明\x01",
            "好像写得比以前更加详细了。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x14,
        (
            "这应该是为了让我们这些\x01",
            "患者安心才做出的改变吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x14,
        (
            "但老实说，像药物成分之类的说明，\x01",
            "我们这些外行人根本就看不懂啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_93F0")

    label("loc_9380")


    #C0513
    ChrTalk(
        0x14,
        (
            "最近这段时间，药品的说明\x01",
            "好像写得比以前更加详细了。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x14,
        (
            "虽然完全看不懂说明内容……\x01",
            "但多少也能放心一些了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93F0")

    TalkEnd(0xFE)
    Return()

    # Function_23_9089 end

    def Function_24_93F4(): pass

    label("Function_24_93F4")


    #C0515
    ChrTalk(
        0x14,
        (
            "嗯～烧还是没有退，\x01",
            "而且一直在流鼻涕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x14,
        (
            "来，用妈妈的手帕\x01",
            "擤擤鼻涕吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x18,
        "#4S……（用力擤）\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x14,
        "……擤出来了呢～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Return()

    # Function_24_93F4 end

    def Function_25_9475(): pass

    label("Function_25_9475")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_94E6")

    #C0519
    ChrTalk(
        0x15,
        (
            "终于可以来医院\x01",
            "探望住院的朋友了。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x15,
        (
            "那家伙在这段日子应该也很不安，\x01",
            "我要和他好好聊一聊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9650")

    label("loc_94E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_94F4")
    Jump("loc_9650")

    label("loc_94F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9502")
    Jump("loc_9650")

    label("loc_9502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9560")

    #C0521
    ChrTalk(
        0x15,
        (
            "我的朋友也被\x01",
            "卷进了袭击事件，\x01",
            "不幸受伤住院……\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x15,
        "希望他的伤能早点好……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9650")

    label("loc_9560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_956E")
    Jump("loc_9650")

    label("loc_956E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_957C")
    Jump("loc_9650")

    label("loc_957C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_95E0")

    #C0523
    ChrTalk(
        0x15,
        (
            "初诊时间延后了，\x01",
            "大概还要等一等\x01",
            "才能叫到号。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x15,
        "啊啊，医院可真是让人不耐烦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9650")

    label("loc_95E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9639")

    #C0525
    ChrTalk(
        0x15,
        "呜呜呜，肚子好疼……\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x15,
        (
            "只能看着护士小姐幻想，\x01",
            "转移一下注意力了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9650")

    label("loc_9639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9647")
    Jump("loc_9650")

    label("loc_9647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9650")

    label("loc_9650")

    TalkEnd(0xFE)
    Return()

    # Function_25_9475 end

    def Function_26_9654(): pass

    label("Function_26_9654")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_96BB")

    #C0527
    ChrTalk(
        0x16,
        "我今天来接出院的妈妈。\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x16,
        (
            "她已经有一段时间\x01",
            "没能离开医院了，\x01",
            "我想赶快带她回家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9903")

    label("loc_96BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_96C9")
    Jump("loc_9903")

    label("loc_96C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_96D7")
    Jump("loc_9903")

    label("loc_96D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_96E5")
    Jump("loc_9903")

    label("loc_96E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977F")

    #C0529
    ChrTalk(
        0x16,
        (
            "这只是我在市里听到的传闻而已……\x01",
            "据说在发生列车事故的时候，\x01",
            "出现了神秘的巨大怪物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x16,
        (
            "莫非那就是\x01",
            "事故发生的原因吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_981D")

    label("loc_977F")


    #C0531
    ChrTalk(
        0x16,
        (
            "这只是我在市里听到的传闻而已……\x01",
            "据说在发生列车事故的时候，\x01",
            "出现了神秘的巨大怪物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x16,
        (
            "……如果真的出现了那种东西，\x01",
            "我们这种普通人\x01",
            "根本就无力对抗啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_981D")

    Jump("loc_9903")

    label("loc_9822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9830")
    Jump("loc_9903")

    label("loc_9830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_98A9")

    #C0533
    ChrTalk(
        0x16,
        (
            "医生们好像正在\x01",
            "诊疗室的门前吵架呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x16,
        (
            "仔细一看，医院里的人\x01",
            "似乎也都很消沉……\x01",
            "是不是发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9903")

    label("loc_98A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_98B7")
    Jump("loc_9903")

    label("loc_98B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_98FA")

    #C0535
    ChrTalk(
        0x16,
        "好了好了，安静些哦。\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x16,
        (
            "大姐姐正在\x01",
            "看着你呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9903")

    label("loc_98FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9903")

    label("loc_9903")

    TalkEnd(0xFE)
    Return()

    # Function_26_9654 end

    def Function_27_9907(): pass

    label("Function_27_9907")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9935")

    #C0537
    ChrTalk(
        0x17,
        (
            "我都已经等得\x01",
            "不耐烦了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A41")

    label("loc_9935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9943")
    Jump("loc_9A41")

    label("loc_9943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9951")
    Jump("loc_9A41")

    label("loc_9951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_998F")

    #C0538
    ChrTalk(
        0x17,
        "啊啊～好无聊啊～\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x17,
        "怎么还不快点叫到我～\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A41")

    label("loc_998F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_999D")
    Jump("loc_9A41")

    label("loc_999D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_99AB")
    Jump("loc_9A41")

    label("loc_99AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_99B9")
    Jump("loc_9A41")

    label("loc_99B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_99C7")
    Jump("loc_9A41")

    label("loc_99C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9A07")

    #C0540
    ChrTalk(
        0x17,
        "哇哇～打针好可怕啊～！！\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x17,
        "我要回家～～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A41")

    label("loc_9A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A41")

    #C0542
    ChrTalk(
        0x17,
        (
            "呼……\x01",
            "等得都快烦死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x17,
        "还没到我吗～？\x02",
    )

    CloseMessageWindow()

    label("loc_9A41")

    TalkEnd(0xFE)
    Return()

    # Function_27_9907 end

    def Function_28_9A45(): pass

    label("Function_28_9A45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9A7D")

    #C0544
    ChrTalk(
        0x18,
        (
            "咳咳、咳咳……\x01",
            "讨厌，这药好苦啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B68")

    label("loc_9A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9A8B")
    Jump("loc_9B68")

    label("loc_9A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9A99")
    Jump("loc_9B68")

    label("loc_9A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9AA7")
    Jump("loc_9B68")

    label("loc_9AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9AB5")
    Jump("loc_9B68")

    label("loc_9AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9B00")

    #C0545
    ChrTalk(
        0x18,
        (
            "我今天是自己一个人\x01",
            "坐巴士来的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x18,
        "嘿嘿，很厉害吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B68")

    label("loc_9B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9B0E")
    Jump("loc_9B68")

    label("loc_9B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B29")
    Call(0, 24)
    Jump("loc_9B4C")

    label("loc_9B29")


    #C0547
    ChrTalk(
        0x18,
        (
            "（吸）……\x01",
            "一直在流鼻涕啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B4C")

    Jump("loc_9B68")

    label("loc_9B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9B5F")
    Jump("loc_9B68")

    label("loc_9B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9B68")

    label("loc_9B68")

    TalkEnd(0xFE)
    Return()

    # Function_28_9A45 end

    def Function_29_9B6C(): pass

    label("Function_29_9B6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9BD7")

    #C0548
    ChrTalk(
        0x19,
        (
            "城市……\x01",
            "城市化为一片火海……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x19,
        (
            "真是恐怖的景象……\x01",
            "甚至让我回想起了\x01",
            "几十年前的战争……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD7")

    TalkEnd(0xFE)
    Return()

    # Function_29_9B6C end

    def Function_30_9BDB(): pass

    label("Function_30_9BDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9C16")

    #C0550
    ChrTalk(
        0x1A,
        "呜、呜呜……\x02",
    )

    CloseMessageWindow()

    #A0551
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "她好像在做噩梦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9C16")

    TalkEnd(0xFE)
    Return()

    # Function_30_9BDB end

    def Function_31_9C1A(): pass

    label("Function_31_9C1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9C7C")

    #C0552
    ChrTalk(
        0x1B,
        (
            "呜呜……我在那起袭击事件中\x01",
            "双腿骨折了。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x1B,
        (
            "可恶……\x01",
            "为什么我会遭遇到这种事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C7C")

    TalkEnd(0xFE)
    Return()

    # Function_31_9C1A end

    def Function_32_9C80(): pass

    label("Function_32_9C80")

    TalkBegin(0xFE)

    #C0554
    ChrTalk(
        0x1C,
        (
            "那好，\x01",
            "拜托你去联络那位\x01",
            "共和国患者的家属吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x1C,
        (
            "我去把病历送到\x01",
            "赛兰德教授那里。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_9C80 end

    def Function_33_9CDE(): pass

    label("Function_33_9CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D0D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D0D")
    Call(0, 48)
    Return()

    label("loc_9D0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA2")

    #C0556
    ChrTalk(
        0x1D,
        (
            "我听到了一些传闻……\x01",
            "据说滴·马克莱因的眼睛\x01",
            "已经彻底治好了？\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x1D,
        (
            "身为她以前的主治医生，\x01",
            "也许应该感到高兴才对……\x01",
            "但如今的心情真是复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x1D,
        (
            "通过这一连串的事件来分析，\x01",
            "她的眼睛恐怕也是使用某种\x01",
            "不可思议的力量治好的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x1D,
        (
            "身为一名现代医疗技术者，\x01",
            "被那种超越常识的东西彻底击败，\x01",
            "真是感到十分不甘心。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x1D,
        (
            "……对不起，忘了我刚才的话吧。\x01",
            "这只是我心里的一点无聊纠结而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_9F58")

    label("loc_9EA2")


    #C0561
    ChrTalk(
        0x1D,
        (
            "……对不起，忘了我刚才说的话吧。\x01",
            "这只是身为一名现代医疗技术者，\x01",
            "心里的一点无聊纠结而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x1D,
        (
            "滴·马克莱因的双眼恢复了光明，\x01",
            "这件事情本身自然还是值得高兴的。\x01",
            "还是坦然祝福她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F58")

    Jump("loc_A604")

    label("loc_9F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9F6B")
    Jump("loc_A604")

    label("loc_9F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9F79")
    Jump("loc_A604")

    label("loc_9F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9F87")
    Jump("loc_A604")

    label("loc_9F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A1A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A19F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FB3")
    Call(0, 35)
    Jump("loc_A19A")

    label("loc_9FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A038")

    #C0563
    ChrTalk(
        0x1D,
        (
            "接下来，\x01",
            "要全力救治那些\x01",
            "在袭击事件中负伤的伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x1D,
        (
            "我们一定会充分利用你们帮忙\x01",
            "取回的医疗物资。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_A094")

    label("loc_A038")


    #C0565
    ChrTalk(
        0x1D,
        (
            "嗯……\x01",
            "马上就要给下一位患者做手术了。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x1D,
        (
            "我们一定会充分利用你们帮忙\x01",
            "取回的医疗物资。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A094")

    Jump("loc_A19A")

    label("loc_A099")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_A121")

    #C0567
    ChrTalk(
        0x1D,
        (
            "在这种特殊状况下，\x01",
            "医疗物资还被人盗走，\x01",
            "的确是令人痛心……\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x1D,
        (
            "但我们绝不能示弱。\x01",
            "无论如何，也要想办法解决困难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19A")

    label("loc_A121")


    #C0569
    ChrTalk(
        0x1D,
        (
            "……如今医疗物资不足，\x01",
            "实在是非常难办。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x1D,
        (
            "如果实在没办法，\x01",
            "也只能如实说明事情原委，\x01",
            "请求对方再送一批替代物资了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19A")

    Jump("loc_A19F")

    label("loc_A19F")

    Jump("loc_A604")

    label("loc_A1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A27C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A246")
    OP_4B(0xC, 0xFF)

    #C0571
    ChrTalk(
        0x1D,
        (
            "利顿，\x01",
            "稍后还要去病房给患者们复诊哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x1D,
        (
            "这次的事故导致很多人负伤，\x01",
            "虽说手术已经结束，\x01",
            "但还是不能松懈。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0xC,
        "是、是的！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 6)
    Jump("loc_A277")

    label("loc_A246")


    #C0574
    ChrTalk(
        0x1D,
        (
            "这次的事故导致很多人负伤，\x01",
            "我们绝不能松懈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A277")

    Jump("loc_A604")

    label("loc_A27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A28A")
    Jump("loc_A604")

    label("loc_A28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A298")
    Jump("loc_A604")

    label("loc_A298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A2A6")
    Jump("loc_A604")

    label("loc_A2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A5FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3AF")

    #C0575
    ChrTalk(
        0x1D,
        (
            "阿尔伯特在视察\x01",
            "结束之后，\x01",
            "好像会到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x1D,
        (
            "明天就要召开会议了，\x01",
            "没必要在这种特殊时期\x01",
            "来这里视察吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x1D,
        (
            "哎呀呀……\x01",
            "他还是老样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x101,
        (
            "#00006F（阿、阿尔伯特……\x01",
            "  竟然直呼其名吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x109,
        "#10100F（可能是老交情吧……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_A3FE")

    label("loc_A3AF")


    #C0580
    ChrTalk(
        0x1D,
        (
            "阿尔伯特在视察\x01",
            "结束之后，\x01",
            "好像会到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x1D,
        (
            "哎呀呀……\x01",
            "他还是老样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A5F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A534")

    #C0582
    ChrTalk(
        0x1D,
        (
            "导致『蝴蝶菇中毒』的原因\x01",
            "是食用了产自外国的蘑菇，\x01",
            "这在克洛斯贝尔属于稀有症状。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x1D,
        (
            "我曾经考虑过各种可能性，\x01",
            "而阿尔伯特可以直接做出判定，\x01",
            "显然是拥有相当渊博的知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x1D,
        (
            "这次算是欠他一个人情吧……\x01",
            "不过话说回来，他毕竟是管理着整个雷米菲利亚的男人，\x01",
            "总不能连这点本事都没有嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_A5F6")

    label("loc_A534")


    #C0585
    ChrTalk(
        0x1D,
        (
            "阿尔伯特当场就可以断定\x01",
            "患者的病症是『蝴蝶菇中毒』，\x01",
            "显然是拥有相当渊博的知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x1D,
        (
            "这次算是欠他一个人情吧……\x01",
            "不过话说回来，他毕竟是管理着整个雷米菲利亚\x01",
            "的男人，总不能连这点本事都没有嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5F6")

    Jump("loc_A604")

    label("loc_A5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A604")

    label("loc_A604")

    TalkEnd(0xFE)
    Return()

    # Function_33_9CDE end

    def Function_34_A608(): pass

    label("Function_34_A608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A69F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A69F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A637")
    Call(0, 35)
    Jump("loc_A69A")

    label("loc_A637")


    #C0587
    ChrTalk(
        0x1E,
        (
            "送到空港的医疗物资本应由\x01",
            "『莱姆斯运输公司』的人\x01",
            "送到这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x1E,
        (
            "嗯……莫非出了\x01",
            "什么差错吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A69A")

    Jump("loc_A69F")

    label("loc_A69F")

    TalkEnd(0xFE)
    Return()

    # Function_34_A608 end

    def Function_35_A6A3(): pass

    label("Function_35_A6A3")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0589
    ChrTalk(
        0x1D,
        (
            "……雷米菲利亚发来的\x01",
            "医疗物资还没到？\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x1E,
        (
            "嗯，明明早就过了预定的\x01",
            "送达时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x9,
        (
            "是不是遇到了\x01",
            "什么麻烦呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x1D,
        (
            "嗯……可能是雷米菲利亚那边\x01",
            "或空港发生了什么情况吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x10)
    SetScenarioFlags(0x18F, 0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_35_A6A3 end

    def Function_36_A772(): pass

    label("Function_36_A772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A787")
    Call(0, 37)
    Jump("loc_A7FB")

    label("loc_A787")


    #C0593
    ChrTalk(
        0x1F,
        (
            "老实说，我原本只是想听听医生能说出些什么，\x01",
            "才勉强来医院的……\x01",
            "真没想到会是这样的结果啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x1F,
        "这多亏了亚米萨。\x02",
    )

    CloseMessageWindow()

    label("loc_A7FB")

    TalkEnd(0xFE)
    Return()

    # Function_36_A772 end

    def Function_37_A7FF(): pass

    label("Function_37_A7FF")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)

    #C0595
    ChrTalk(
        0xC,
        "嗯，这真是让人吃惊啊……\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xC,
        (
            "奎因先生，\x01",
            "和上次住院时相比，\x01",
            "您的症状已经减轻了不少。\x02",
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
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xC,
        (
            "当然，还是需要\x01",
            "持续观察。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xC,
        (
            "但至少不需要\x01",
            "住院了。\x02",
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
        "太好啦，爷爷！\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x20,
        (
            "您的身体已经好了！\x01",
            "而且不需要住院！\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x1F,
        "啊……嗯嗯……是啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    ClearChrFlags(0x20, 0x10)
    SetScenarioFlags(0x2, 4)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_37_A7FF end

    def Function_38_A970(): pass

    label("Function_38_A970")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A9D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A98E")
    Call(0, 37)
    Jump("loc_A9D3")

    label("loc_A98E")


    #C0603
    ChrTalk(
        0x20,
        (
            "真是太好了啊，\x01",
            "爷爷！\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x20,
        (
            "嘿嘿嘿，\x01",
            "让您按时吃药果然\x01",
            "是正确的¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9D3")

    Jump("loc_AA17")

    label("loc_A9D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AA17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F3")
    Call(0, 39)
    Jump("loc_AA17")

    label("loc_A9F3")


    #C0605
    ChrTalk(
        0x20,
        (
            "以后我也会\x01",
            "继续给爷爷\x01",
            "送药的¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA17")

    TalkEnd(0xFE)
    Return()

    # Function_38_A970 end

    def Function_39_AA1B(): pass

    label("Function_39_AA1B")

    OP_4B(0xC, 0xFF)

    #C0606
    ChrTalk(
        0xC,
        (
            "给，亚米萨，\x01",
            "已经把你平时来取的药包好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xC,
        "路上小心点哦。\x02",
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x20,
        (
            "嗯，\x01",
            "谢谢您，医生。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x2, 3)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_39_AA1B end

    def Function_40_AA8D(): pass

    label("Function_40_AA8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AABC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AABC")
    Call(0, 48)
    Return()

    label("loc_AABC")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_40_AA8D end

    def Function_41_AAC3(): pass

    label("Function_41_AAC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAE2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE2")
    Call(0, 48)
    Return()

    label("loc_AAE2")

    TalkBegin(0xFE)

    #C0609
    ChrTalk(
        0x22,
        (
            "我在这里等你们把\x01",
            "纳迪利亚菇带回来。\x02\x03",

            "有你们和亚里欧斯联手行动，\x01",
            "一定能顺利找到吧。\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_AAC3 end

    def Function_42_AB4E(): pass

    label("Function_42_AB4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AC4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABEA")

    #C0610
    ChrTalk(
        0x24,
        (
            "我吃了从外国\x01",
            "带回来的蘑菇，\x01",
            "味道非常好……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x24,
        (
            "但没想到竟会是毒蘑菇，\x01",
            "真是太不小心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x24,
        (
            "今后必须要\x01",
            "注意些才行啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC45")

    label("loc_ABEA")


    #C0613
    ChrTalk(
        0x24,
        (
            "我吃了从外国\x01",
            "带回来的蘑菇，\x01",
            "味道非常好，但没想到……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0x24,
        (
            "今后必须要\x01",
            "注意些才行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC45")

    Jump("loc_ACC2")

    label("loc_AC4A")


    #C0615
    ChrTalk(
        0x24,
        (
            "呜、呜呜……\x01",
            "不知为什么，肚子疼得越来越厉害了……\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x24,
        (
            "大概是在飞船上\x01",
            "吃的那个东西有问题吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x24,
        "呼………………\x02",
    )

    CloseMessageWindow()

    label("loc_ACC2")

    TalkEnd(0xFE)
    Return()

    # Function_42_AB4E end

    def Function_43_ACC6(): pass

    label("Function_43_ACC6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_43_ACC6 end

    def Function_44_ACCD(): pass

    label("Function_44_ACCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE4D")

    #C0618
    ChrTalk(
        0xFE,
        (
            "我正在帮忙运送之前由于管制\x01",
            "而无法入院的患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "人数真是好多啊，\x01",
            "今天大概还要往返\x01",
            "很多次。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x101,
        "#00005F那可真是很辛苦呢……\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0x103,
        "#00203F请不要太勉强自己。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0622
    ChrTalk(
        0xFE,
        (
            "啊啊，竟然得到了\x01",
            "小缇欧的关心……\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        (
            "平时一直都冷若冰霜，\x01",
            "今天这难道是发生突变了吗！？\x02",
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
            "#00211F（……越来越像罗伯兹主任\x01",
            "  的同类了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 2)
    Jump("loc_AF00")

    label("loc_AE4D")


    #C0625
    ChrTalk(
        0xFE,
        (
            "好～有了小缇欧\x01",
            "的鼓励，\x01",
            "我精神百倍，勇气十足！\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "小缇欧，等一切都平息下来之后，\x01",
            "要让我好好抱一抱哟⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x103,
        (
            "#00211F（……看样子，即使一切都平息下来，\x01",
            "  也仍然不能安心呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF00")

    TalkEnd(0xFE)
    Return()

    # Function_44_ACCD end

    def Function_45_AF04(): pass

    label("Function_45_AF04")

    Sound(160, 0, 100, 0)
    Return()

    # Function_45_AF04 end

    def Function_46_AF0B(): pass

    label("Function_46_AF0B")

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
            "#11P啊，诺艾尔小姐，\x01",
            "还有支援科的各位……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x8,
        (
            "#11P大家是来探望\x01",
            "芙兰小姐的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x109,
        "#10100F#6P是的，现在方便吗？\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x8,
        "#11P嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x8,
        (
            "#11P……你的妹妹恢复了意识，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x109,
        (
            "#10104F#6P……是的，\x01",
            "谢谢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0A8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B0A8)
    WaitChrThread(0x109, 3)
    Sleep(150)

    #C0634
    ChrTalk(
        0x109,
        (
            "#10102F#11P我们走吧，\x01",
            "是三楼的３０１室。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        "#00002F#6P嗯，那就去打扰一下吧。\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x102,
        "#00104F#6P失陪了，塞拉小姐。\x02",
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

    # Function_46_AF0B end

    def Function_47_B182(): pass

    label("Function_47_B182")

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
        "……嗯……嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x8,
        (
            "……好的，\x01",
            "打扰您了。\x02",
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
            "已经和赛兰德教授\x01",
            "确认过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "她让你们马上去\x01",
            "研究楼的办公室。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x26,
        "#01309F谢啦，塞拉小姐。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x101,
        "#6P#00000F帮大忙了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x101, 500)

    #C0643
    ChrTalk(
        0x26,
        (
            "#01300F……各位，\x01",
            "休息时间快要结束了，\x01",
            "我就先失陪啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B3F2():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B3F2)
    Sleep(50)

    def lambda_B402():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B402)
    Sleep(50)

    def lambda_B412():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B412)
    Sleep(50)

    def lambda_B422():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B422)
    Sleep(50)

    def lambda_B432():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B432)
    WaitChrThread(0x105, 2)

    #C0644
    ChrTalk(
        0x101,
        "#12P#00000F嗯，谢谢啦。\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x109,
        "#6P#10102F多谢帮忙。\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x26,
        (
            "#01300F哪里，不用客气。\x02\x03",

            "#01309F你们接下来的工作\x01",
            "肯定也会很辛苦……\x01",
            "加油哦，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x101,
        "#12P#00009F嗯，你也一样。\x02",
    )

    CloseMessageWindow()

    def lambda_B4F3():
        OP_95(0xFE, 12030, 0, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B4F3)
    Sleep(50)

    def lambda_B510():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B510)
    Sleep(50)

    def lambda_B520():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B520)
    WaitChrThread(0x26, 1)

    def lambda_B531():
        OP_97(0xFE, 0x0, 0x564, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B531)
    Sleep(1000)

    def lambda_B54E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_B54E)
    WaitChrThread(0x26, 2)
    SetChrFlags(0x26, 0x80)
    OP_0D()
    OP_68(13870, 1000, 6330, 3000)
    OP_6F(0x1)

    #C0648
    ChrTalk(
        0x104,
        (
            "#12P#00310F……可恶～你这家伙\x01",
            "总是这么惹人讨厌！\x02\x03",

            "#00309F『加油哦，罗伊德⊥』\x01",
            "……这算什么啊！什么啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    #C0649
    ChrTalk(
        0x101,
        (
            "#00006F本、本来并没有\x01",
            "那个桃心符号吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B620():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B620)
    Sleep(100)

    def lambda_B630():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B630)
    Sleep(500)

    #C0650
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，既然你这么说，\x01",
            "是不是也觉得有点遗憾呢？\x02\x03",

            "传闻中的超～热情拥抱，\x01",
            "这次没能目睹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x102,
        "#00105F哦，说起来……\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x109,
        "#10105F哎，还发生过那种事吗……！？\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x101,
        (
            "#00003F啊啊，够了！\x01",
            "别再说这些了，\x01",
            "我们赶快去找教授吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x3E8)
    Sleep(500)

    #C0654
    ChrTalk(
        0x101,
        (
            "#12P#00001F研究楼建在医院的楼顶，\x01",
            "药物学研究室在研究楼的四层！\x01",
            "好了，赶快出发！\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x104,
        (
            "#12P#00309F（哎呀呀，就被他\x01",
            "  这样用气势蒙混过去了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x105,
        (
            "#6P#10302F（呵呵，正是因为他的反应很有趣，\x01",
            "  我们才喜欢戏弄他啊。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    #C0657
    ChrTalk(
        0x101,
        "#00003F……喂！我都听到了！\x02",
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

    # Function_47_B182 end

    def Function_48_B883(): pass

    label("Function_48_B883")

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
        "唔……有客人来了啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C076")

    #C0659
    ChrTalk(
        0x22,
        "哦，你们是……\x02",
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
            "#00005F您是雷、雷米菲利亚公国的\x01",
            "阿尔伯特大公阁下……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x109,
        "#10105F而且亚里欧斯先生也在……\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x21,
        (
            "#01405F嗯，真是巧遇啊。\x02\x03",

            "#01400F阁下，他们就是我曾经和您\x01",
            "提到过的『特别任务支援科』成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0663
    ChrTalk(
        0x22,
        "哦哦，原来就是他们啊。\x02",
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x22,
        "……初次见面，支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x22,
        (
            "我的名字是阿尔伯特·冯·巴尔特罗梅斯，\x01",
            "雷米菲利亚的国家元首。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x22,
        (
            "为了克洛斯贝尔，希望各位\x01",
            "今后也继续努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        "#00000F是、是的，请多指教。\x02",
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x22,
        (
            "呵呵，我听亚里欧斯\x01",
            "说起过你们，\x01",
            "一直都想见上一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x22,
        "还有艾莉，我们也好久没见了啊。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，久疏问候。\x01",
            "看来大公阁下的身体十分安康……\x02\x03",

            "#00103F不过，真没想到\x01",
            "能在医院\x01",
            "与您偶遇呢。\x02\x03",

            "#00105F您今天是来\x01",
            "视察的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x22,
        (
            "嗯，毕竟雷米菲利亚公国是\x01",
            "这所医院的资助方之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x22,
        (
            "而且，我也十分想看看\x01",
            "来此赴任的赛兰德。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0673
    ChrTalk(
        0x21,
        (
            "#01403F关于这一点，\x01",
            "我个人认为您还是应该\x01",
            "多带些护卫人员。\x02\x03",

            "#01400F此次出行，只有我和司机陪同，\x01",
            "未免有些草率了……\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x22,
        (
            "呵呵，亚里欧斯，\x01",
            "这是因为我很信任\x01",
            "你的能力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x22,
        (
            "而且只不过是一次视察而已，\x01",
            "如果带上过多护卫人员，\x01",
            "难免会影响到医院的正常工作。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    #C0676
    ChrTalk(
        0x1D,
        "真是的，根本就是多此一举。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x1D,
        (
            "视察又不是什么重要的急事，\x01",
            "何必非要赶在这次过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x1D,
        (
            "如今应该把精力集中在\x01",
            "通商会议上吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x1D,
        (
            "身为国家首脑，\x01",
            "难道就不能有点基本的自觉性吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0680
    ChrTalk(
        0x22,
        (
            "哈哈哈，赛兰德还是老样子，\x01",
            "真是严厉啊。\x02",
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
            "#00003F（阿尔伯特大公……\x01",
            "  似乎是个交友范围很广阔的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x109,
        (
            "#10100F（嗯，他和艾莉小姐、\x01",
            "  亚里欧斯先生……\x01",
            "  还有赛兰德教授好像都是旧识。）\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x105,
        (
            "#10300F（呵呵，面对着一国首脑，\x01",
            "  还能用那种口气说话，真是让人甘拜下风啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C39F")

    label("loc_C076")


    #C0684
    ChrTalk(
        0x22,
        "哦，这不是特别任务支援科的各位吗。\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x101,
        (
            "#00000F阿尔伯特大公阁下，\x01",
            "还有亚里欧斯先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        (
            "#00100F二位探望过小滴之后，\x01",
            "又到这里来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x21,
        (
            "#01400F嗯，我们来和赛兰德教授\x01",
            "打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x22,
        (
            "呵呵，因为我十分想看看\x01",
            "来此赴任的赛兰德。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    #C0689
    ChrTalk(
        0x1D,
        "真是的，根本就是多此一举。\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x1D,
        (
            "视察又不是什么重要的急事，\x01",
            "何必非要赶在这次过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x1D,
        (
            "如今应该把精力集中在\x01",
            "通商会议上吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x1D,
        (
            "身为国家首脑，\x01",
            "难道就不能有点基本的自觉性吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0693
    ChrTalk(
        0x22,
        (
            "哈哈哈，赛兰德还是老样子，\x01",
            "真是严厉啊。\x02",
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
            "#00003F（阿尔伯特大公……\x01",
            "  真是个交友范围广阔的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x109,
        (
            "#10100F（嗯，他和赛兰德教授\x01",
            "  好像也是旧识呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x105,
        (
            "#10300F（呵呵，面对着一国首脑，\x01",
            "  还能用那种口气说话，真是让人甘拜下风啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C39F")

    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(300, -1, -1, -1)
    SetChrName("声音")

    #A0697
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5S医、医生！\x07\x00\x02",
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

    def lambda_C4A4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4A4)
    Sleep(50)

    def lambda_C4B4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C4B4)
    Sleep(50)

    def lambda_C4C4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C4C4)
    Sleep(50)

    def lambda_C4D4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C4D4)
    Sleep(50)

    def lambda_C4E4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C4E4)
    Sleep(50)

    def lambda_C4F4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_C4F4)
    Sleep(50)

    def lambda_C504():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_C504)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 54100, 0, 55910, 4000, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_6F(0x1)

    #C0698
    ChrTalk(
        0x1D,
        "怎么了，利顿，为什么这么慌张？\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0699
    ChrTalk(
        0xC,
        "有、有急症患者！\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0xC,
        (
            "刚才有位患者\x01",
            "倒在了大厅……\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0xC,
        "目前已经失去意识了，情况很严重！\x02",
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
        "唔……那可真是不妙啊。\x02",
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x22,
        (
            "你赶快去把患者\x01",
            "抬到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0xC,
        "是、是！\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_68(50330, 1000, 58210, 3000)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 49800, 0, 51590, 4000, 0x0)
    OP_95(0xC, 49560, 0, 49150, 4000, 0x0)
    OP_6F(0x1)
    SetChrSubChip(0x1D, 0x1)

    def lambda_C756():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C756)
    Sleep(50)

    def lambda_C766():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C766)
    Sleep(50)

    def lambda_C776():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C776)
    Sleep(50)

    def lambda_C786():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C786)
    Sleep(50)

    def lambda_C796():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C796)
    Sleep(50)

    def lambda_C7A6():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_C7A6)
    Sleep(300)

    #C0705
    ChrTalk(
        0x101,
        "#00000F亚里欧斯先生，我们……\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x21,
        (
            "#01400F嗯，也许会打搅到诊疗工作，\x01",
            "还是离开为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x22,
        "不，请各位留在这里吧。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0708
    ChrTalk(
        0x22,
        (
            "说不定你们也能\x01",
            "帮上一些忙呢。\x02",
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
        "………呜……唔…………………\x02",
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x1D,
        "……嗯……\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x101,
        "#00005F情况如何……\x02",
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x104,
        "#00301F看起来好像很痛苦……\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x1D,
        "……情况不容乐观啊。\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x1D,
        (
            "已经做过了各种检查，\x01",
            "肯定是内科症状没错，\x01",
            "但目前还没有查出任何原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x1D,
        (
            "如果能确定病症，\x01",
            "就可以调配对应的药物了……\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1D,
        (
            "但目前来看，还不知道患者能不能撑到\x01",
            "那个时候，状况相当严重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x102,
        "#00105F竟、竟然那么严重吗……\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xC,
        "到、到底该怎么办才好……！\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x22,
        (
            "唔，\x01",
            "可以让我看看吗？\x02",
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

    def lambda_CBC6():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBC6)
    Sleep(50)

    def lambda_CBD6():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CBD6)
    Sleep(50)

    def lambda_CBE6():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CBE6)
    Sleep(50)

    def lambda_CBF6():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CBF6)
    Sleep(50)

    def lambda_CC06():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CC06)
    Sleep(50)

    def lambda_CC16():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_CC16)
    Sleep(50)

    def lambda_CC26():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_CC26)
    Sleep(50)

    def lambda_CC36():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CC36)
    Sleep(300)

    #C0720
    ChrTalk(
        0x21,
        "#01405F阁下，您要做什么？\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x22,
        (
            "赛兰德，\x01",
            "从这种症状来看……\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x22,
        (
            "或许是\x01",
            "『蝴蝶菇中毒』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0723
    ChrTalk(
        0x1D,
        "……原来如此，『蝴蝶菇中毒』啊。\x02",
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x1D,
        (
            "虽然这种病症从不会出现在克洛斯贝尔，\x01",
            "但如此看来，可能性的确很高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x105,
        (
            "#10305F『蝴蝶菇中毒』……？\x01",
            "从没听说过这种病呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    #C0726
    ChrTalk(
        0x22,
        (
            "这是一种由于误食了生长在\x01",
            "大陆边境地带的珍奇野生毒蘑菇\x01",
            "而引发的中毒症状。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x22,
        (
            "用普通的诊断方法\x01",
            "是很难检查出这种毒性的。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x22,
        (
            "但从其目前的状况来看，\x01",
            "与『蝴蝶菇中毒』的症状似乎完全一致吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x1D,
        "嗯，应该没错。\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x1D,
        (
            "说不定是食用了\x01",
            "从自治州境外带进来的毒蘑菇。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x104,
        (
            "#00305F教授也同意这种观点吗？\x02\x03",

            "#00300F大公阁下好厉害啊，\x01",
            "竟然一眼就能\x01",
            "确定病症。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x22,
        "哈哈，这没什么了不起的。\x02",
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x22,
        "虽然确定了病症，但还是不容乐观。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0734
    ChrTalk(
        0x22,
        (
            "赛兰德，\x01",
            "医院里是否储备了\x01",
            "清除『蝴蝶菇毒性』的特效药？\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x1D,
        (
            "……很不巧，有些材料\x01",
            "正好用完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x1D,
        (
            "如果材料足够，马上就能\x01",
            "将药调制出来，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x109,
        "#10103F这可糟糕了……\x02",
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x22,
        "唔，既然如此……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    #C0739
    ChrTalk(
        0x22,
        "亚里欧斯，还有特别任务支援科的诸位。\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x22,
        (
            "我在此发起紧急委托，\x01",
            "希望各位帮忙采集调制药物所需的材料……\x01",
            "你们可以接受吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x21,
        "#01400F是……谨遵吩咐。\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x101,
        (
            "#00001F事态紧急，\x01",
            "我们当然要接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x105,
        (
            "#10305F具体要采集\x01",
            "什么材料呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x22,
        "嗯，我来简单说明一下。\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x22,
        (
            "治疗『蝴蝶菇中毒』的特效药\x01",
            "主要由两种材料调制而成。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x22,
        (
            "其中之一是生长在玛因兹山岳地带，\x01",
            "名为『安提草』的药草……\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x22,
        (
            "另一种则是生长在\x01",
            "乌尔斯拉间道的森林地带，\x01",
            "叫做『阿鲁玛菇』的蘑菇。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x109,
        (
            "#10100F『安提草』和『阿鲁玛菇』……\x01",
            "在参加警备队的生存训练时，\x01",
            "我好像见过那种东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x22,
        (
            "『安提草』的采集工作，\x01",
            "我希望由亚里欧斯来负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x22,
        (
            "如果要前往人烟稀少的\x01",
            "山岳地带采集药草，\x01",
            "身为游击士的你应该是合适人选。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x21,
        "#01400F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x22,
        "至于『阿鲁玛菇』……\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x22,
        (
            "就由我和特别任务支援科的各位同行，\x01",
            "一起去采集吧。\x02",
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
        "#00005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x102,
        "#00105F大公阁下……也要一起去吗？\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x22,
        "嗯，因为……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x22,
        (
            "在『阿鲁玛菇』的生长地带，\x01",
            "还生长着很多种外形近似\x01",
            "的其它蘑菇。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x22,
        (
            "一般人非常容易搞混，\x01",
            "最好还是有专业人士同行。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x105,
        (
            "#10303F嗯，看来的确是\x01",
            "应该一起去找啊。\x02\x03",

            "#10300F不过……要接替\x01",
            "亚里欧斯先生，担当大公阁下\x01",
            "的护卫人员，总有些不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x104,
        "#00306F的确是责任重大啊。\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x21,
        (
            "#01401F我作为阁下的护卫，\x01",
            "也觉得有些不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x22,
        (
            "但当务之急是尽快救治患者，\x01",
            "我们必须争分夺秒，\x01",
            "已经没有其它办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x22,
        (
            "支援科各位的实力\x01",
            "不是得到过你的认可吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x22,
        (
            "我自己也会多加小心的，\x01",
            "不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x22,
        (
            "只要你也\x01",
            "快去快回，\x01",
            "就没有任何问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x21,
        (
            "#01404F嗯……明白了。\x02\x03",

            "#01400F那我立即前往\x01",
            "玛因兹的山岳地带。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    #C0767
    ChrTalk(
        0x21,
        (
            "#01400F保护阁下的任务就拜托你们了，\x01",
            "特别任务支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        "#00001F是……！\x02",
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x102,
        "#00100F我们一定会完成护卫工作。\x02",
    )

    CloseMessageWindow()

    #C0770
    ChrTalk(
        0x22,
        (
            "呵呵，那我们就赶快\x01",
            "前往间道的森林地带吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    #C0771
    ChrTalk(
        0x22,
        (
            "赛兰德，你们继续\x01",
            "观察患者的状况，\x01",
            "同时做好调制药物的准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x1D,
        "嗯，明白。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0773
    ChrTalk(
        0xC,
        (
            "特别任务支援科的各位，\x01",
            "你们也要加油！\x02",
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
            "就这样，罗伊德等人\x01",
            "接受了阿尔伯特大公的紧急请求……\x07\x00\x02",
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
            "与亚里欧斯分头行动，\x01",
            "开始采集调制药物所需的材料。\x07\x00\x02",
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
            "任务【筹集解毒药的材料】\x07\x00",
            "开始！\x02",
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

    # Function_48_B883 end

    def Function_49_D850(): pass

    label("Function_49_D850")

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
            "#1P我吃了从外国\x01",
            "带回来的蘑菇，\x01",
            "味道非常好……\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x24,
        (
            "#1P呼，但没想到竟会是毒蘑菇，\x01",
            "真是太不小心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0779
    ChrTalk(
        0x1D,
        (
            "味道鲜美也是\x01",
            "带有『蝴蝶菇毒性』的毒蘑菇的\x01",
            "危险特点之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x1D,
        (
            "今后可一定不能\x01",
            "再乱吃一些奇怪的东西了。\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x1D,
        (
            "另外，虽然你保住了性命，\x01",
            "但我还是建议你在研究楼\x01",
            "的病房中住院一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x24,
        (
            "#1P明、明白了。\x01",
            "万一有什么后遗症的话，\x01",
            "的确很恐怖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x24,
        (
            "#1P不过，多亏您相救，我已经舒服多了。\x01",
            "谢谢您了，医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xC,
        (
            "如果要道谢，还是去谢\x01",
            "阿尔伯特大公阁下、亚里欧斯先生，\x01",
            "还有特别任务支援科的各位成员吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0xC,
        (
            "正是他们帮你搜集\x01",
            "到了药物的材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0x24,
        (
            "#1P啊……是、是吗，\x01",
            "太感谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x24,
        (
            "#1P真没想到，竟然会得到\x01",
            "阿尔伯特大公阁下的救助……\x01",
            "真是让人惶恐不已啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x22,
        (
            "哪里哪里，我只不过是\x01",
            "鉴定了蘑菇的品种而已。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DC7B():
        TurnDirection(0x22, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DC7B)

    #C0789
    ChrTalk(
        0x22,
        (
            "要说真正的功劳者，显然还是亚里欧斯\x01",
            "和支援科的各位啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x0)

    def lambda_DCC7():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_DCC7)
    Sleep(50)

    def lambda_DCD7():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DCD7)

    def lambda_DCE4():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DCE4)
    Sleep(50)

    def lambda_DCF4():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DCF4)

    def lambda_DD01():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_DD01)
    Sleep(50)

    def lambda_DD11():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DD11)
    Sleep(50)

    def lambda_DD21():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DD21)
    Sleep(300)

    #C0790
    ChrTalk(
        0x21,
        (
            "#01402F您太谦逊了……\x02\x03",

            "#01403F我听说您曾和\x01",
            "赛兰德医生一起学习，\x01",
            "并获得了医师资格。\x02\x03",

            "#01400F无论是经验还是技术，\x01",
            "都不逊于活跃在一线\x01",
            "的职业医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x104,
        "#00305F哎哎……是吗！？\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x105,
        (
            "#10300F真不愧是医疗技术发达的国家——\x01",
            "雷米菲利亚的大公阁下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0793
    ChrTalk(
        0x22,
        "哈哈，我一直都很喜欢学习。\x02",
    )

    CloseMessageWindow()

    #C0794
    ChrTalk(
        0x22,
        (
            "赛兰德身在雷米菲利亚的时候，\x01",
            "我经常去参观由她负责的手术。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x22,
        (
            "在当时学习的知识，\x01",
            "这次只是正巧派上了用场而已……\x01",
            "受到如此夸赞，实在是不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x22,
        (
            "在这次的任务中，\x01",
            "我仅仅是起到点协助作用而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x22,
        (
            "多亏亚里欧斯、支援科的各位，\x01",
            "还有医院的各位职员共同努力，\x01",
            "才能使患者迅速得到治疗。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x22,
        "嗯，真是一次有意义的视察啊。\x02",
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x1D,
        (
            "哎呀呀……\x01",
            "还是老样子，这么爱讲死理。\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x1D,
        (
            "总之，视察就算是\x01",
            "告一段落了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x1D,
        (
            "你明天还要出席通商会议，\x01",
            "还是尽快回去准备\x01",
            "为好吧？\x02",
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
            "哈哈哈，还是一样严厉啊。\x01",
            "不过，你的话一向很有道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x22,
        (
            "那我们就先\x01",
            "告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x22,
        (
            "亚里欧斯，回去时的护卫工作\x01",
            "也麻烦你了，没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x21,
        "#01400F嗯，当然。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    #C0806
    ChrTalk(
        0x21,
        (
            "#01400F……那么，特别任务支援科的各位。\x02\x03",

            "#01403F在明天的通商会议召开之前，\x01",
            "仍然不能有丝毫松懈。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    #C0807
    ChrTalk(
        0x101,
        (
            "#00000F啊……是，\x01",
            "我们会铭记在心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x109,
        "#10100F您也辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x22,
        (
            "各位，今后也请\x01",
            "继续努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x22,
        "我会默默给你们加油的。\x02",
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x102,
        "#00100F呵呵，谢谢您。\x02",
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
            "任务【筹集解毒药的材料】\x07\x00",
            "完成！\x02",
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

    # Function_49_D850 end

    def Function_50_E36A(): pass

    label("Function_50_E36A")

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
            "支援科的各位……\x01",
            "欢迎来到乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x8,
        (
            "今天有\x01",
            "什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x101,
        (
            "#00000F嗯，\x01",
            "有点事情\x01",
            "想打听一下……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0816
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德说明了\x01",
            "包裹送错的情况。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0817
    ChrTalk(
        0x8,
        (
            "哦哦……那件包裹\x01",
            "原来是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0818
    ChrTalk(
        0x8,
        (
            "玛萨护士长还以为是\x01",
            "某个护士工作失误，下错了定单，\x01",
            "一直在训人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0819
    ChrTalk(
        0x103,
        "#00205F下错定单吗……\x02",
    )

    CloseMessageWindow()

    #C0820
    ChrTalk(
        0x8,
        (
            "嗯，因为以前也曾\x01",
            "发生过好几次类似的情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0821
    ChrTalk(
        0x101,
        "#00006F呼……\x02",
    )

    CloseMessageWindow()

    #C0822
    ChrTalk(
        0x109,
        (
            "#10100F那……发错的包裹\x01",
            "现在应该在护士中心吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0823
    ChrTalk(
        0x8,
        (
            "嗯，\x01",
            "正是如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0824
    ChrTalk(
        0x8,
        "请各位上二楼吧。\x02",
    )

    CloseMessageWindow()

    #C0825
    ChrTalk(
        0x104,
        "#00300F那我们就走吧。\x02",
    )

    CloseMessageWindow()

    #C0826
    ChrTalk(
        0x105,
        (
            "#10300F无端遭受冤枉，\x01",
            "那个被训的人很可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0827
    ChrTalk(
        0x101,
        (
            "#00006F是、是啊……\x01",
            "我们快点过去吧。\x02",
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

    # Function_50_E36A end

    def Function_51_E6AE(): pass

    label("Function_51_E6AE")

    Return()

    # Function_51_E6AE end

    def Function_52_E6AF(): pass

    label("Function_52_E6AF")

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
            "接到空港的利卡尔德先生\x01",
            "的联络时，我真是吃了一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x9,
        (
            "本以为只是医疗物资还没有送到，\x01",
            "没想到发生了这样的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x1E,
        "真是个恶劣的家伙啊……\x02",
    )

    CloseMessageWindow()

    #C0831
    ChrTalk(
        0x8,
        (
            "不过，医疗物资能顺利送到，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0832
    ChrTalk(
        0x1D,
        (
            "不管怎么说，\x01",
            "现在总算可以救治\x01",
            "在袭击事件中负伤的伤员了。\x02",
        )
    )

    CloseMessageWindow()

    #C0833
    ChrTalk(
        0x1D,
        (
            "真是多亏你们的帮忙啊，\x01",
            "请容我正式道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0834
    ChrTalk(
        0x102,
        (
            "#00100F哪里，我们只是做了些\x01",
            "分内之事而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0835
    ChrTalk(
        0x104,
        (
            "#00301F嗯，再怎么说，\x01",
            "也不能放过那种趁火打劫的\x01",
            "卑劣之徒嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0836
    ChrTalk(
        0x105,
        (
            "#10303F话说回来，这次多亏有\x01",
            "那个穿铠甲的家伙相助。\x02",
        )
    )

    CloseMessageWindow()

    #C0837
    ChrTalk(
        0x1E,
        "穿铠甲的家伙……那是谁？\x02",
    )

    CloseMessageWindow()

    #C0838
    ChrTalk(
        0x109,
        "#10100F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x103,
        (
            "#00203F……没什么，\x01",
            "请不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0840
    ChrTalk(
        0x101,
        (
            "#00000F如果以后还有什么事情，\x01",
            "请随时和我们联系。\x02",
        )
    )

    CloseMessageWindow()

    #C0841
    ChrTalk(
        0x8,
        (
            "嗯……\x01",
            "真是太谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0842
    ChrTalk(
        0x23,
        (
            "我也要向你们道谢，\x01",
            "真是太感谢了！\x02",
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
            "任务【寻找医疗物资】\x07\x00",
            "完成！\x02",
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

    # Function_52_E6AF end

    def Function_53_EB8E(): pass

    label("Function_53_EB8E")

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
            "接到空港的利卡尔德先生\x01",
            "的联络时，我真是吃了一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x9,
        (
            "本以为只是医疗物资还没有送到，\x01",
            "没想到发生了这样的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x1E,
        "真是个恶劣的家伙啊……\x02",
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x101,
        (
            "#00003F我们力有不逮，\x01",
            "真是很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0848
    ChrTalk(
        0x102,
        (
            "#00108F我们很想将犯人抓捕，\x01",
            "已经拼尽了全力，但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0849
    ChrTalk(
        0x23,
        (
            "我也有责任，\x01",
            "如果我当时早点去取货，\x01",
            "就不会发生这种事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0850
    ChrTalk(
        0x9,
        (
            "不，这并不怪各位……\x01",
            "请大家不要自责了。\x02",
        )
    )

    CloseMessageWindow()

    #C0851
    ChrTalk(
        0x9,
        (
            "总之，我们接下来\x01",
            "会努力想想办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0852
    ChrTalk(
        0x8,
        (
            "至于已经被盗的物资，\x01",
            "再去想它也无济于事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x8,
        (
            "现在必须要尽早调配\x01",
            "追加的物资。\x02",
        )
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x1D,
        (
            "在物资送到之前，\x01",
            "也只能想办法撑过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x101,
        (
            "#00003F对不起……\x01",
            "接下来的事情就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x23,
        (
            "（唉，回去以后，\x01",
            "  大概又要被老爹暴揍一顿了……）\x02",
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
            "任务【寻找医疗物资】\x07\x00",
            "失败了……\x02",
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

    # Function_53_EB8E end

    def Function_54_F01F(): pass

    label("Function_54_F01F")

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
            "　　ＩＣＵ（集中治疗室）\x01",
            "未经许可者禁止入内。\x01",
            "※入室者必须进行等级２\x01",
            "  以上的杀菌处理。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_54_F01F end

    def Function_55_F0B2(): pass

    label("Function_55_F0B2")

    EventBegin(0x1)

    #C0859
    ChrTalk(
        0x101,
        (
            "#00000F我们先去接待处吧，\x01",
            "办完手续之后再去病房。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 59460, 0, 3330, 225)
    EventEnd(0x4)
    Return()

    # Function_55_F0B2 end

    def Function_56_F0FF(): pass

    label("Function_56_F0FF")

    EventBegin(0x1)

    #C0860
    ChrTalk(
        0x101,
        (
            "#00000F我们先去接待处吧，\x01",
            "办完手续之后再去病房。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11970, 0, 10190, 135)
    EventEnd(0x4)
    Return()

    # Function_56_F0FF end

    def Function_57_F14C(): pass

    label("Function_57_F14C")

    EventBegin(0x1)

    #C0861
    ChrTalk(
        0x101,
        (
            "#00000F芙兰的病房是３０１室，\x01",
            "赶快去看看她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1120, 50, -440, 89)
    EventEnd(0x4)
    Return()

    # Function_57_F14C end

    SaveToFile()

Try(main)
