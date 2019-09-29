from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0010.bin",                # FileName
        "c0010",                    # MapName
        "c0010",                    # Location
        0x0003,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0010",                  # 0
        "站员卢克斯",             # 1
        "站员莉莎",               # 2
        "站员艾姆",               # 3
        "站员仙莉",               # 4
        "站员玛吉斯",             # 5
        "库瓦特罗安检官",         # 6
        "菲伊",                   # 7
        "比利",                   # 8
        "商务人士",               # 9
        "游客",                   # 10
        "游客",                   # 11
        "老人",                   # 12
        "老婆婆",                 # 13
        "游客",                   # 14
        "游客",                   # 15
        "男孩",                   # 16
        "穆拉",                   # 17
        "马洛安检官",             # 18
        "雷蒙德搜查官",           # 19
        "东方打扮的男子",         # 20
        "东方打扮的男子",         # 21
    ))

    AddCharChip((
        "chr/ch46600.itc",                   # 00
        "chr/ch46400.itc",                   # 01
        "chr/ch30200.itc",                   # 02
        "chr/ch12500.itc",                   # 03
        "chr/ch31500.itc",                   # 04
        "chr/ch00100.itc",                   # 05
        "chr/ch00200.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch03000.itc",                   # 09
        "chr/ch28300.itc",                   # 0A
        "chr/ch28400.itc",                   # 0B
        "chr/ch28500.itc",                   # 0C
        "chr/ch32700.itc",                   # 0D
        "chr/ch27600.itc",                   # 0E
        "chr/ch32200.itc",                   # 0F
        "chr/ch32400.itc",                   # 10
        "chr/ch33000.itc",                   # 11
        "chr/ch20900.itc",                   # 12
        "chr/ch22100.itc",                   # 13
        "chr/ch22000.itc",                   # 14
        "chr/ch22200.itc",                   # 15
        "chr/ch32202.itc",                   # 16
        "chr/ch32402.itc",                   # 17
        "chr/ch33002.itc",                   # 18
        "chr/ch20902.itc",                   # 19
        "chr/ch22102.itc",                   # 1A
        "chr/ch22002.itc",                   # 1B
        "chr/ch22202.itc",                   # 1C
        "chr/ch27602.itc",                   # 1D
        "chr/ch23600.itc",                   # 1E
    ))

    DeclNpc(4750,    0,       7500,    180,  257,  0x0, 0,   10,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(9500,    0,       7500,    180,  257,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(33000,   4000,    8000,    270,  257,  0x0, 0,   11,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(33000,   4000,    -8000,   270,  257,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(18260,   0,       10229,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  385,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-53380,  0,       52599,   270,  385,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(2809,    29,      2299,    45,   389,  0x0, 0,   30,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   14,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   17,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   18,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   20,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(29500,   4000,    1350,    90,   389,  0x0, 0,   21,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(19209,   0,       -4150,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(28000,   4000,    10000,   180,  385,  0x0, 0,   1,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(14090,   29,      19,      90,   385,  0x0, 0,   2,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(15550,   0,       9319,    90,   385,  0x0, 0,   3,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(16600,   0,       9319,    270,  385,  0x0, 0,   4,   0,   0,   0,   0,   31,  255,  0)

    DeclActor(4750,    0,       6500,    1000,    4750,    1500,    7500,    0x007E, 0,  4,  0x0000)
    DeclActor(9500,    0,       6500,    1000,    9500,    1500,    7500,    0x007E, 0,  7,  0x0000)
    DeclActor(32000,   4000,    8000,    1000,    33000,   5500,    8000,    0x007E, 0,  11, 0x0000)
    DeclActor(32000,   4000,    -8000,   1000,    33000,   5500,    -8000,   0x007E, 0,  13, 0x0000)
    DeclActor(20560,   0,       4090,    1000,    20560,   1500,    4090,    0x007C, 0,  51, 0x0000)
    DeclActor(20130,   0,       -4810,   1000,    20130,   1500,    -4810,   0x007C, 0,  52, 0x0000)
    DeclActor(31150,   4000,    1130,    1000,    31150,   5500,    1130,    0x007C, 0,  53, 0x0000)
    DeclActor(28100,   4000,    11510,   1000,    28100,   5500,    11510,   0x007C, 0,  54, 0x0000)
    DeclActor(30940,   4000,    -1900,   1000,    30940,   5500,    -1900,   0x007C, 0,  55, 0x0000)
    DeclActor(3250,    0,       -8800,   1200,    3250,    400,     -8800,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1448, 0)                                       # 0

    ScpFunction((
        "Function_0_5A8",          # 00, 0
        "Function_1_660",          # 01, 1
        "Function_2_AE6",          # 02, 2
        "Function_3_BBC",          # 03, 3
        "Function_4_C62",          # 04, 4
        "Function_5_C66",          # 05, 5
        "Function_6_FF4",          # 06, 6
        "Function_7_113F",         # 07, 7
        "Function_8_1143",         # 08, 8
        "Function_9_154A",         # 09, 9
        "Function_10_1673",        # 0A, 10
        "Function_11_1946",        # 0B, 11
        "Function_12_194A",        # 0C, 12
        "Function_13_1C36",        # 0D, 13
        "Function_14_1C3A",        # 0E, 14
        "Function_15_21AA",        # 0F, 15
        "Function_16_22D0",        # 10, 16
        "Function_17_22DA",        # 11, 17
        "Function_18_2446",        # 12, 18
        "Function_19_2612",        # 13, 19
        "Function_20_271A",        # 14, 20
        "Function_21_2831",        # 15, 21
        "Function_22_2A81",        # 16, 22
        "Function_23_2BA3",        # 17, 23
        "Function_24_2D00",        # 18, 24
        "Function_25_2E2A",        # 19, 25
        "Function_26_2F1D",        # 1A, 26
        "Function_27_2FAB",        # 1B, 27
        "Function_28_31BD",        # 1C, 28
        "Function_29_31F4",        # 1D, 29
        "Function_30_3241",        # 1E, 30
        "Function_31_324B",        # 1F, 31
        "Function_32_3255",        # 20, 32
        "Function_33_32C2",        # 21, 33
        "Function_34_3AEC",        # 22, 34
        "Function_35_42DC",        # 23, 35
        "Function_36_44FF",        # 24, 36
        "Function_37_468C",        # 25, 37
        "Function_38_4778",        # 26, 38
        "Function_39_48B9",        # 27, 39
        "Function_40_4BF8",        # 28, 40
        "Function_41_4F1C",        # 29, 41
        "Function_42_4F52",        # 2A, 42
        "Function_43_5939",        # 2B, 43
        "Function_44_5AAA",        # 2C, 44
        "Function_45_639A",        # 2D, 45
        "Function_46_64B3",        # 2E, 46
        "Function_47_64D2",        # 2F, 47
        "Function_48_64F1",        # 30, 48
        "Function_49_651D",        # 31, 49
        "Function_50_6566",        # 32, 50
        "Function_51_6E4D",        # 33, 51
        "Function_52_6EC1",        # 34, 52
        "Function_53_6F37",        # 35, 53
        "Function_54_6F76",        # 36, 54
        "Function_55_7002",        # 37, 55
        "Function_56_703D",        # 38, 56
    ))


    def Function_0_5A8(): pass

    label("Function_0_5A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5E8"),
        (1, "loc_5F4"),
        (2, "loc_600"),
        (3, "loc_60C"),
        (4, "loc_618"),
        (5, "loc_624"),
        (6, "loc_630"),
        (SWITCH_DEFAULT, "loc_63C"),
    )


    label("loc_5E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_5F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_600")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_60C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_618")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_624")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_630")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_63C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_648")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_648")

    label("loc_65F")

    Return()

    # Function_0_5A8 end

    def Function_1_660(): pass

    label("Function_1_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_687")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_A77")

    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7A0")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, 1940, 0, 3880, 45)
    SetChrPos(0x13, 5700, 0, 3470, 315)
    SetChrPos(0x17, 4900, 30, 1340, 315)
    SetChrPos(0x14, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x14, 0x19)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrPos(0x15, 19240, 30, -7910, 90)
    SetChrPos(0x16, 30700, 4019, 9620, 135)
    SetChrPos(0x10, 4400, 0, 5200, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x11, 10570, 0, 5190, 0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0xC, 18260, 0, 10230, 270)
    SetChrPos(0xE, 16980, 0, 10250, 90)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)
    Jump("loc_A77")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_911")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_875")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 5790, 200, -5340, 0)
    SetChrChipByIndex(0x10, 0x1D)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x13, 0x18)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 12490, 200, -9000, 0)
    SetChrChipByIndex(0x16, 0x1B)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 29290, 4000, -450, 90)
    SetChrFlags(0x17, 0x10)
    Jump("loc_8D9")

    label("loc_875")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 29680, 4000, 1320, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x12, 0x17)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x14, 0x19)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)

    label("loc_8D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90C")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1C, 0x10)

    label("loc_90C")

    Jump("loc_A77")

    label("loc_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9C4")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 29680, 4000, 1320, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x12, 0x17)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 12490, 200, -9000, 0)
    SetChrChipByIndex(0x17, 0x1C)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BF")
    ClearChrFlags(0x19, 0x80)

    label("loc_9BF")

    Jump("loc_A77")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A77")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 13490, 200, -9000, 0)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 29680, 4000, 1320, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 3750, 200, -5340, 0)
    SetChrChipByIndex(0x14, 0x19)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 11000, 200, -5560, 0)
    SetChrChipByIndex(0x16, 0x1B)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A77")
    ClearChrFlags(0x18, 0x80)

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA0")
    SetMapFlags(0x10000000)
    Event(0, 35)

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_AB4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 40)
    Jump("loc_AE5")

    label("loc_AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_AC8")
    ClearScenarioFlags(0x22, 1)
    Event(0, 50)
    Jump("loc_AE5")

    label("loc_AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AE5")
    ClearScenarioFlags(0x22, 2)
    SetChrPos(0x0, 19270, 30, 7590, 270)

    label("loc_AE5")

    Return()

    # Function_1_660 end

    def Function_2_AE6(): pass

    label("Function_2_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B25")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6E")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B87")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_B87")

    ClearMapObjFlags(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA1")
    SetMapObjFlags(0x2, 0x10)

    label("loc_BA1")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBB")
    SetMapObjFlags(0x1, 0x10)

    label("loc_BBB")

    Return()

    # Function_2_AE6 end

    def Function_3_BBC(): pass

    label("Function_3_BBC")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着导力车杂志《副刊 导力车明星》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x373, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5E")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『闪耀色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x373, 1)

    label("loc_C5E")

    TalkEnd(0xFF)
    Return()

    # Function_3_BBC end

    def Function_4_C62(): pass

    label("Function_4_C62")

    Call(0, 5)
    Return()

    # Function_4_C62 end

    def Function_5_C66(): pass

    label("Function_5_C66")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C7A")
    Call(0, 6)
    Jump("loc_FF0")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1D")

    #C0003
    ChrTalk(
        0x8,
        (
            "感谢各位今日\x01",
            "前来克洛斯贝尔\x01",
            "车站搭乘列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "前往共和国和\x01",
            "帝国的列车\x01",
            "即将依次发车。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "请各位乘客\x01",
            "尽早购买车票。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D68")

    label("loc_D1D")


    #C0006
    ChrTalk(
        0x8,
        (
            "前往共和国和\x01",
            "帝国的列车\x01",
            "即将依次发车。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "请各位乘客\x01",
            "尽早购买车票。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D68")

    Jump("loc_DDE")

    label("loc_D6D")


    #C0008
    ChrTalk(
        0x8,
        (
            "听说有逃犯\x01",
            "飞身跳上了列车车顶时，\x01",
            "我简直不敢相信自己的耳朵。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "今后可要多加注意，\x01",
            "以防再次出现这样的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDE")

    Jump("loc_FF0")

    label("loc_DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E99")

    #C0010
    ChrTalk(
        0x8,
        (
            "感谢各位今日\x01",
            "前来克洛斯贝尔\x01",
            "车站搭乘列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "在通商会议进行期间，\x01",
            "帝国军将会加强\x01",
            "站台的警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "安检等事项会比平时更加严格，\x01",
            "敬请各位乘客谅解。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F02")

    label("loc_E99")


    #C0013
    ChrTalk(
        0x8,
        (
            "在通商会议进行期间，\x01",
            "帝国军将会加强\x01",
            "站台的警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "安检等事项会比平时更加严格，\x01",
            "请各位乘客谅解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F02")

    Jump("loc_FF0")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA1")

    #C0015
    ChrTalk(
        0x8,
        (
            "感谢各位今日\x01",
            "前来克洛斯贝尔\x01",
            "车站搭乘列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "在通商会议期间，\x01",
            "铁路列车会照常运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "如需购票，\x01",
            "请去二层的\x01",
            "购票处。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF0")

    label("loc_FA1")


    #C0018
    ChrTalk(
        0x8,
        (
            "在通商会议期间，\x01",
            "铁路列车会照常运营。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "如需购票，\x01",
            "请去二层的\x01",
            "购票处。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF0")

    TalkEnd(0x8)
    Return()

    # Function_5_C66 end

    def Function_6_FF4(): pass

    label("Function_6_FF4")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B7")

    #C0020
    ChrTalk(
        0x8,
        (
            "开往帝国和\x01",
            "共和国的列车\x01",
            "现在都暂停运行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "给乘客们造成了很大麻烦，\x01",
            "真是非常抱歉……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x10,
        (
            "怎么可以这样！\x01",
            "我还有一宗很重要的生意等着谈，\x01",
            "正急着赶往帝国呢……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1136")

    label("loc_10B7")


    #C0023
    ChrTalk(
        0x8,
        (
            "实在是非常抱歉，\x01",
            "目前还不能确定\x01",
            "恢复通车的具体时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "请各位乘客\x01",
            "多加谅解……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x10,
        "这可怎么办！我的生意！生意啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_1136")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_6_FF4 end

    def Function_7_113F(): pass

    label("Function_7_113F")

    Call(0, 8)
    Return()

    # Function_7_113F end

    def Function_8_1143(): pass

    label("Function_8_1143")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1150")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1546")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1250")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11BF")
    OP_AF(0x8B)
    Jump("loc_1241")

    label("loc_11BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_11CF")
    OP_AF(0x8A)
    Jump("loc_1241")

    label("loc_11CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11DF")
    OP_AF(0x89)
    Jump("loc_1241")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11EF")
    OP_AF(0x88)
    Jump("loc_1241")

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11FF")
    OP_AF(0x87)
    Jump("loc_1241")

    label("loc_11FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_120F")
    OP_AF(0x86)
    Jump("loc_1241")

    label("loc_120F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_121F")
    OP_AF(0x85)
    Jump("loc_1241")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_122F")
    OP_AF(0x84)
    Jump("loc_1241")

    label("loc_122F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_123F")
    OP_AF(0x83)
    Jump("loc_1241")

    label("loc_123F")

    OP_AF(0x82)

    label("loc_1241")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1541")

    label("loc_1250")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1264")
    Jump("loc_1541")

    label("loc_1264")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1541")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_128E")
    Call(0, 9)
    Jump("loc_1541")

    label("loc_128E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1372")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F6")

    #C0026
    ChrTalk(
        0x9,
        "要来一份旅途必备的盒饭吗？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔时代周刊的最新一期\x01",
            "也到了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136D")

    label("loc_12F6")


    #C0028
    ChrTalk(
        0x9,
        (
            "竟然同时抓住了\x01",
            "逃犯和恐怖分子……\x01",
            "这种事可是闻所未闻的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "或许是各种偶然赶在了一起，\x01",
            "才导致了这样的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    Jump("loc_1541")

    label("loc_1372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143A")

    #C0030
    ChrTalk(
        0x9,
        (
            "安检官马洛先生是\x01",
            "共和国军派来的专员。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "听说他和帝国军派来的\x01",
            "安检官库瓦特罗先生的\x01",
            "关系不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "毕竟帝国和共和国之间\x01",
            "纷争不断，他们不能\x01",
            "融洽相处也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14B7")

    label("loc_143A")


    #C0033
    ChrTalk(
        0x9,
        (
            "听说马洛安检官和库瓦特罗\x01",
            "安检官之间的关系不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "毕竟帝国和共和国之间\x01",
            "纷争不断，他们不能\x01",
            "融洽相处也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B7")

    Jump("loc_1541")

    label("loc_14BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1541")

    #C0035
    ChrTalk(
        0x9,
        (
            "今天早上，帝国出版社\x01",
            "『帝国时报社』的记者们\x01",
            "也到这里取材了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔即将\x01",
            "举办国际性会议，\x01",
            "自然广受各国关注啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1541")

    Jump("loc_1150")

    label("loc_1546")

    TalkEnd(0x9)
    Return()

    # Function_8_1143 end

    def Function_9_154A(): pass

    label("Function_9_154A")

    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1605")

    #N0037
    NpcTalk(
        0x11,
        "市民",
        (
            "可恶，这可不是全额\x01",
            "退回票款就能了事的问题！\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x11,
        "市民",
        (
            "你知道我为今天这趟旅行\x01",
            "准备了多久吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "真、真是非常抱歉。\x01",
            "我们也在努力确认事情的原委……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_166A")

    label("loc_1605")


    #N0040
    NpcTalk(
        0x11,
        "市民",
        (
            "真是的，每次都是\x01",
            "我们这些乘客倒霉！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "真、真是非常抱歉。\x01",
            "我们也在努力确认事情的原委……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166A")

    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_154A end

    def Function_10_1673(): pass

    label("Function_10_1673")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1687")
    Call(0, 17)
    Jump("loc_1942")

    label("loc_1687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1703")

    #C0042
    ChrTalk(
        0xFE,
        (
            "那位警察小哥\x01",
            "好像一直心神不宁。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "难道正在追捕罪犯吗？\x01",
            "但我也没看到有\x01",
            "可疑人物进来啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F0")

    label("loc_1703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179A")

    #C0044
    ChrTalk(
        0xFE,
        (
            "光是假货商也就罢了，\x01",
            "居然还有恐怖分子……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "不知道他们长什么样子，\x01",
            "竟然可以轻易混在\x01",
            "普通民众之中吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "总觉得很可怕啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_17F0")

    label("loc_179A")


    #C0047
    ChrTalk(
        0xFE,
        (
            "光是假货商也就罢了，\x01",
            "但恐怖分子竟然能\x01",
            "轻易混在人群中……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "总觉得很可怕啊……\x02",
    )

    CloseMessageWindow()

    label("loc_17F0")

    Jump("loc_1942")

    label("loc_17F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1874")

    #C0049
    ChrTalk(
        0xFE,
        (
            "帝国政府的专用列车\x01",
            "停靠在三号月台，\x01",
            "帝国军正在那里严密守备。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "看看热闹倒没什么，\x01",
            "但千万不要随意靠近啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_1874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1942")

    #C0051
    ChrTalk(
        0xFE,
        (
            "今天早上，帝国政府的专用列车\x01",
            "『艾森古拉夫号』\x01",
            "抵达一号月台。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "为了不妨碍普通列车进站，\x01",
            "已经把它移到三号月台了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "那辆列车可不是轻易就能见到的，\x01",
            "如果你有机会去月台，\x01",
            "不妨好好参观一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1942")

    TalkEnd(0xFE)
    Return()

    # Function_10_1673 end

    def Function_11_1946(): pass

    label("Function_11_1946")

    Call(0, 12)
    Return()

    # Function_11_1946 end

    def Function_12_194A(): pass

    label("Function_12_194A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19D1")

    #C0054
    ChrTalk(
        0xA,
        (
            "实在非常抱歉，\x01",
            "为了处理列车事故的相关事项，\x01",
            "目前十分忙乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "暂时无法办理车票的\x01",
            "销售、预约等业务，\x01",
            "请您谅解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C32")

    label("loc_19D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B66")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A87")

    #C0056
    ChrTalk(
        0xA,
        (
            "刚才有个看上去非常\x01",
            "慈祥和蔼的老婆婆买了张\x01",
            "前往帝国的车票。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "她好像是个\x01",
            "长年经商的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "虽然我不了解详细情况，\x01",
            "但希望她能成功呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1AF6")

    label("loc_1A87")


    #C0059
    ChrTalk(
        0xA,
        (
            "刚才有个看上去非常\x01",
            "慈祥和蔼的老婆婆买了张\x01",
            "前往帝国的车票。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "听说她要去帝国做生意，\x01",
            "真希望她能成功啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF6")

    Jump("loc_1B61")

    label("loc_1AFB")


    #C0061
    ChrTalk(
        0xA,
        (
            "听说在阿尔泰尔市\x01",
            "被捕的那个假货商\x01",
            "是个老婆婆。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "难道就是之前\x01",
            "在这里买车票的\x01",
            "那位老婆婆吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B61")

    Jump("loc_1C32")

    label("loc_1B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BEE")

    #C0063
    ChrTalk(
        0xA,
        (
            "为了加强警备，\x01",
            "现在正在清查各位乘客\x01",
            "入站时携带的行李。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "给大家造成了一些不便，\x01",
            "敬请谅解，\x01",
            "并尽量配合我们的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C32")

    label("loc_1BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C32")

    #C0065
    ChrTalk(
        0xA,
        (
            "这里是出售车票的\x01",
            "柜台。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        "如果需要购票，请来这里。\x02",
    )

    CloseMessageWindow()

    label("loc_1C32")

    TalkEnd(0xA)
    Return()

    # Function_12_194A end

    def Function_13_1C36(): pass

    label("Function_13_1C36")

    Call(0, 14)
    Return()

    # Function_13_1C36 end

    def Function_14_1C3A(): pass

    label("Function_14_1C3A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D09")

    #C0067
    ChrTalk(
        0xB,
        (
            "啊……不好意思，\x01",
            "请您稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "由于西克洛斯贝尔街道\x01",
            "发生了脱轨事故，\x01",
            "列车已经暂时停运了。\x02\x03",

            "而且修复工作未必\x01",
            "能在今天之内完成。\x01",
            "敬请谅解。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D62")

    label("loc_1D09")


    #C0069
    ChrTalk(
        0xB,
        (
            "要办理退票手续，\x01",
            "还要播放站内广播……\x01",
            "真是忙不过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "希望铁路\x01",
            "尽快修复完毕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D62")

    Jump("loc_21A6")

    label("loc_1D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1A")

    #C0071
    ChrTalk(
        0xB,
        (
            "啊……不好意思，\x01",
            "请您稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "前往共和国和帝国的列车\x01",
            "即将发车。\x02\x03",

            "请您不要奔跑上车，\x01",
            "以免造成危险。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E88")

    label("loc_1E1A")


    #C0073
    ChrTalk(
        0xB,
        (
            "奔跑上车是造成\x01",
            "人身事故的隐患，\x01",
            "非常危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "如果没能赶上列车，\x01",
            "请不要着急，\x01",
            "耐心等待下一班列车到来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E88")

    Jump("loc_1F04")

    label("loc_1E8D")


    #C0075
    ChrTalk(
        0xB,
        (
            "奔跑上车也就罢了，\x01",
            "听说还有人跳到了列车的车顶，\x01",
            "真是难以置信……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "……是不是该用站内广播\x01",
            "提醒大家注意一下呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F04")

    Jump("loc_21A6")

    label("loc_1F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE7")

    #C0077
    ChrTalk(
        0xB,
        (
            "啊……不好意思，\x01",
            "请您稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "根据大陆铁道公司的规章，\x01",
            "各位乘客要在克洛斯贝尔车站\x01",
            "接受安检。\x02\x03",

            "前往帝国或共和国的乘客\x01",
            "请填写入境申请书，\x01",
            "并交给安检官检查。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_204C")

    label("loc_1FE7")


    #C0079
    ChrTalk(
        0xB,
        (
            "由克洛斯贝尔车站\x01",
            "前往帝国、共和国的乘客\x01",
            "必须接受安检。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xB,
        (
            "给大家增添了一些麻烦，\x01",
            "请多加谅解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204C")

    Jump("loc_21A6")

    label("loc_2051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213F")

    #C0081
    ChrTalk(
        0xB,
        (
            "啊……不好意思，\x01",
            "请您稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "由于帝国政府的专用列车\x01",
            "『艾森古拉夫号』于今日抵达本站，\x01",
            "站内的警备力度已经增强。\x02\x03",

            "因此请各位注意，\x01",
            "不要进入该列车所在的\x01",
            "三号月台，谢谢合作。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_21A6")

    label("loc_213F")


    #C0083
    ChrTalk(
        0xB,
        (
            "您好，我是负责\x01",
            "站内广播的站员。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "各位对乘车方面的事项\x01",
            "有不解之处吗？\x01",
            "如果有需要，请尽管咨询。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A6")

    TalkEnd(0xB)
    Return()

    # Function_14_1C3A end

    def Function_15_21AA(): pass

    label("Function_15_21AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2240")

    #C0085
    ChrTalk(
        0xFE,
        (
            "我有多久没见过\x01",
            "宰相阁下和\x01",
            "奥利维特皇子了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "作为一名帝国军人，\x01",
            "能够亲自迎接政府要人，\x01",
            "实在是无上的光荣。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2277")

    label("loc_2240")


    #C0087
    ChrTalk(
        0xFE,
        (
            "……嗯？总觉得站在一楼的\x01",
            "那个黑衣大汉有些眼熟……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2277")

    Jump("loc_22CC")

    label("loc_227C")


    #C0088
    ChrTalk(
        0xFE,
        (
            "那个黑衣大汉\x01",
            "不知在何时离开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "难道他是……\x01",
            "唔，应该只是我多心了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CC")

    TalkEnd(0xFE)
    Return()

    # Function_15_21AA end

    def Function_16_22D0(): pass

    label("Function_16_22D0")

    TalkBegin(0xFE)
    Call(0, 17)
    TalkEnd(0xFE)
    Return()

    # Function_16_22D0 end

    def Function_17_22DA(): pass

    label("Function_17_22DA")

    OP_4B(0xE, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DB")

    #C0090
    ChrTalk(
        0xE,
        (
            "列车的受损状况\x01",
            "如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "根据接到的联络所说，\x01",
            "车辆的状况相当糟糕。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "如果处理不当，说不定\x01",
            "整辆列车都要报废……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xE,
        (
            "唔……既然如此，\x01",
            "也只能先安排\x01",
            "其它列车顶替了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xE,
        (
            "总之，现在最重要的事，\x01",
            "就是争取让\x01",
            "铁路尽快恢复通车。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_243D")

    label("loc_23DB")


    #C0095
    ChrTalk(
        0xE,
        (
            "轨道损毁的可能性\x01",
            "也相当高。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        (
            "移除列车的工作结束后，\x01",
            "马上赶赴现场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        "嗯，我明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_243D")

    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_22DA end

    def Function_18_2446(): pass

    label("Function_18_2446")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_245A")
    Call(0, 9)
    Jump("loc_260E")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_24B6")

    #C0098
    ChrTalk(
        0xFE,
        (
            "唔，列车好像\x01",
            "马上就要发车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "没办法，先去逛逛街，\x01",
            "回来等下一班吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_260E")

    label("loc_24B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24C4")
    Jump("loc_260E")

    label("loc_24C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_260E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2587")

    #C0100
    ChrTalk(
        0xFE,
        (
            "我来自共和国最西边的港湾都市\x01",
            "阿尔泰尔市。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "话说回来，克洛斯贝尔的发展速度\x01",
            "真是让人惊叹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "共和国也算是繁荣之地，\x01",
            "但和克洛斯贝尔相比，\x01",
            "简直就像乡下一样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_260E")

    label("loc_2587")


    #C0103
    ChrTalk(
        0xFE,
        (
            "我来自共和国最西边的港湾都市\x01",
            "阿尔泰尔市。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "话说回来，克洛斯贝尔的发展速度\x01",
            "真是让人惊叹啊。\x01",
            "相比之下，共和国简直就像乡下一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260E")

    TalkEnd(0xFE)
    Return()

    # Function_18_2446 end

    def Function_19_2612(): pass

    label("Function_19_2612")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2626")
    Call(0, 6)
    Jump("loc_2716")

    label("loc_2626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26A5")

    #C0105
    ChrTalk(
        0xFE,
        (
            "听站务员说……\x01",
            "恐怖分子的余党都在共和国\x01",
            "被抓捕归案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "他们已经潜伏了好一段时间，\x01",
            "这下总算让人放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_26A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_270D")

    #C0107
    ChrTalk(
        0xFE,
        "我正要去帝国出差。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "虽然很关注会议的情况……\x01",
            "但『帝国时报』应该\x01",
            "会做特辑报道的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2716")

    label("loc_270D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2716")

    label("loc_2716")

    TalkEnd(0xFE)
    Return()

    # Function_19_2612 end

    def Function_20_271A(): pass

    label("Function_20_271A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2760")

    #C0109
    ChrTalk(
        0xFE,
        "竟、竟发生了脱轨事故……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我丈夫\x01",
            "没事吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_2760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27AC")

    #C0111
    ChrTalk(
        0xFE,
        "终于抵达克洛斯贝尔了～\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "稍微休息一下，就开始观光吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_27AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2824")

    #C0113
    ChrTalk(
        0xFE,
        (
            "这孩子真是的，\x01",
            "居然在车上把在阿尔泰尔买的\x01",
            "炒栗子全部吃掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "如果一会\x01",
            "吃不下晚饭，\x01",
            "我可不管哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_2824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_282D")

    label("loc_282D")

    TalkEnd(0xFE)
    Return()

    # Function_20_271A end

    def Function_21_2831(): pass

    label("Function_21_2831")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28A9")

    #C0115
    ChrTalk(
        0xFE,
        (
            "是发生了落石吗？\x01",
            "还是人为造成的？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "如果真的是人为事故……\x01",
            "我一定会向犯人索取\x01",
            "一笔巨额赔偿金。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7D")

    label("loc_28A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_292A")

    #C0117
    ChrTalk(
        0xFE,
        (
            "听说边境大门的状况\x01",
            "一直都很紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "都是因为提出什么独立，\x01",
            "才会搞成这样。\x01",
            "年轻人，一定要认清自己的能力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7D")

    label("loc_292A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2938")
    Jump("loc_2A7D")

    label("loc_2938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A31")

    #C0119
    ChrTalk(
        0xFE,
        (
            "听说帝国的奥斯本宰相\x01",
            "和自治州议会的前议长\x01",
            "哈尔特曼一直有所勾结。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "不过，在哈尔特曼逃亡期间，\x01",
            "帝国政府下达的驱逐令\x01",
            "也是宰相在暗中发布的。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "一旦损害到自己的利益，\x01",
            "就毫不犹豫地抛弃。\x01",
            "『铁血宰相』就是这样的男人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A7D")

    label("loc_2A31")


    #C0122
    ChrTalk(
        0xFE,
        (
            "一旦损害到自己的利益，\x01",
            "就毫不犹豫地抛弃。\x01",
            "『铁血宰相』就是这样的男人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7D")

    TalkEnd(0xFE)
    Return()

    # Function_21_2831 end

    def Function_22_2A81(): pass

    label("Function_22_2A81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AD9")

    #C0123
    ChrTalk(
        0xFE,
        (
            "铁道居然停止了运营，\x01",
            "这到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "我还能安全回国吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B9F")

    label("loc_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B60")

    #C0125
    ChrTalk(
        0xFE,
        (
            "那个金头发的家伙是怎么回事？\x01",
            "总觉得他的举动很古怪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "……什么？他是警察吗？\x01",
            "看上去很不可靠啊，\x01",
            "真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9F")

    label("loc_2B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B6E")
    Jump("loc_2B9F")

    label("loc_2B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B9F")

    #C0127
    ChrTalk(
        0xFE,
        "列车还没抵达吗？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "我都等烦了。\x02",
    )

    CloseMessageWindow()

    label("loc_2B9F")

    TalkEnd(0xFE)
    Return()

    # Function_22_2A81 end

    def Function_23_2BA3(): pass

    label("Function_23_2BA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2C2B")

    #C0129
    ChrTalk(
        0xFE,
        (
            "列车一直不发车，\x01",
            "我还在奇怪……\x01",
            "原来发生了脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "今天只好留宿在克洛斯贝尔了。\x01",
            "不知能否订到酒店的房间……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFC")

    label("loc_2C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C93")

    #C0131
    ChrTalk(
        0xFE,
        (
            "我正要和男朋友一起\x01",
            "去共和国旅游呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "东方人街，还有温泉……\x01",
            "一定要好好享受一番！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFC")

    label("loc_2C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CF3")

    #C0133
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔也有不少\x01",
            "观光景点呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "乘巴士也能到达那些地方，\x01",
            "到处去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFC")

    label("loc_2CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CFC")

    label("loc_2CFC")

    TalkEnd(0xFE)
    Return()

    # Function_23_2BA3 end

    def Function_24_2D00(): pass

    label("Function_24_2D00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D57")

    #C0135
    ChrTalk(
        0xFE,
        (
            "我已经办完了\x01",
            "退票手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "本打算去旅游，\x01",
            "但这次也只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_2D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2DBD")

    #C0137
    ChrTalk(
        0xFE,
        (
            "我要带女朋友\x01",
            "去旅游……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "居然要逛这么多地方啊。\x01",
            "如果钱不够用了，该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_2DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DCB")
    Jump("loc_2E26")

    label("loc_2DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E26")

    #C0139
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "正在举行那个\x01",
            "通商会议吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "要不要去看看\x01",
            "那传闻中的\x01",
            "兰花塔呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E26")

    TalkEnd(0xFE)
    Return()

    # Function_24_2D00 end

    def Function_25_2E2A(): pass

    label("Function_25_2E2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E53")

    #C0141
    ChrTalk(
        0xFE,
        "发生什么事了吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F19")

    label("loc_2E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E98")

    #C0142
    ChrTalk(
        0xFE,
        (
            "滴答滴答……滴答滴答……\x01",
            "时钟在……转啊转转转……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F19")

    label("loc_2E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F10")

    #C0143
    ChrTalk(
        0xFE,
        (
            "（打嗝）……\x01",
            "我在阿尔泰尔市玩得好开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "那里有一条叫丘利河的大河流，\x01",
            "很多船在上面开来开去呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F19")

    label("loc_2F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F19")

    label("loc_2F19")

    TalkEnd(0xFE)
    Return()

    # Function_25_2E2A end

    def Function_26_2F1D(): pass

    label("Function_26_2F1D")

    TalkBegin(0xFE)

    #C0145
    ChrTalk(
        0xFE,
        (
            "喂喂，这是真的吗……\x01",
            "那些来自共和国的货物怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "总之，得先和老爸商量一下，\x01",
            "另外还要联络收货人……\x01",
            "呜呜，这下可有得忙了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_2F1D end

    def Function_27_2FAB(): pass

    label("Function_27_2FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FD0")
    Call(0, 33)
    Return()

    label("loc_2FD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EC")

    #C0147
    ChrTalk(
        0xFE,
        (
            "#12400F奥利维尔·朗海姆是个\x01",
            "身穿白色大衣，随身带着\x01",
            "鲁特琴的演奏家。\x02\x03",

            "他应该会跑到那些\x01",
            "不三不四的热闹地方，\x01",
            "或是餐厅之类的地方。\x02\x03",

            "在各位刚刚列举的地点里，\x01",
            "旧城区、后巷、港湾区\x01",
            "这几个地方的可能性相当高。\x02\x03",

            "如果他一直不配合，\x01",
            "让他吃点苦头也没关系。\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_31B9")

    label("loc_30EC")


    #C0148
    ChrTalk(
        0xFE,
        (
            "#12400F奥利维尔应该会去\x01",
            "一些不三不四的热闹地方，\x01",
            "或是餐厅之类的地方。\x02\x03",

            "在各位刚刚列举的地点里，\x01",
            "旧城区、后巷、港湾区\x01",
            "这几个地方的可能性相当高。\x02\x03",

            "如果他一直不配合，\x01",
            "让他吃点苦头也没关系。\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B9")

    TalkEnd(0xFE)
    Return()

    # Function_27_2FAB end

    def Function_28_31BD(): pass

    label("Function_28_31BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31EF")
    Call(0, 36)
    Jump("loc_31F2")

    label("loc_31EF")

    Call(0, 37)

    label("loc_31F2")

    Return()

    label("loc_31F3")

    Return()

    # Function_28_31BD end

    def Function_29_31F4(): pass

    label("Function_29_31F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3227")
    Call(0, 42)
    Jump("loc_322A")

    label("loc_3227")

    Call(0, 43)

    label("loc_322A")

    Return()

    label("loc_322B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323D")
    Jump("loc_323D")

    label("loc_323D")

    TalkEnd(0xFE)
    Return()

    # Function_29_31F4 end

    def Function_30_3241(): pass

    label("Function_30_3241")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_30_3241 end

    def Function_31_324B(): pass

    label("Function_31_324B")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_31_324B end

    def Function_32_3255(): pass

    label("Function_32_3255")

    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)

    #C0149
    ChrTalk(
        0x1B,
        (
            "……那些家伙果然\x01",
            "想乘坐列车逃跑啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x1C,
        (
            "……哼，愚蠢……\x01",
            "竟然妄想从我们手中逃脱……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    Return()

    # Function_32_3255 end

    def Function_33_32C2(): pass

    label("Function_33_32C2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3309")
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12400.itp")
    Jump("loc_330E")

    label("loc_3309")

    Fade(500)

    label("loc_330E")

    OP_4B(0x18, 0xFF)
    OP_68(17080, 1300, -3920, 0)
    MoveCamera(48, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15930, 0)
    SetChrPos(0x101, 17430, 0, -3570, 90)
    SetChrPos(0x102, 17390, 0, -4750, 90)
    SetChrPos(0x104, 15510, 0, -4080, 90)
    SetChrPos(0x109, 15980, 0, -3030, 90)
    SetChrPos(0x105, 15960, 0, -5340, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B2")
    FadeToBright(500, 0)

    label("loc_33B2")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397B")

    #N0151
    NpcTalk(
        0x18,
        "黑衣壮男",
        "#12400F…………………………\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        (
            "#6P#00305F（喂，罗伊德……\x01",
            "  那家伙的气势\x01",
            "  很惊人啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#6P#00003F（莫非这次的\x01",
            "  委托人就是……）\x02\x03",

            "#00000F您好，打扰一下。\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0154
    NpcTalk(
        0x18,
        "黑衣壮男",
        (
            "#12404F……我正等着你们，\x01",
            "非常感谢各位的到来。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("黑衣壮男")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            "我的名字是穆拉……\x01",
            "是来自帝国的\x01",
            "音乐经纪人。\x02\x03",

            "相处的时间大概不会太久，\x01",
            "但还请各位多多指教。\x02",
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
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x101,
        (
            "#6P#00006F音、音乐经纪人吗……？\x01",
            "（看起来完全不像啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        (
            "#6P#10101F（散发出来的气息\x01",
            "  更像是保镖之类的人士……）\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#6P#00105F（而且好像在什么地方\x01",
            "  听到过类似的职业……）\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x18,
        "#12405F……怎么了？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0160
    ChrTalk(
        0x101,
        (
            "#6P#00012F没、没什么……\x02\x03",

            "#00000F既、既然如此……\x01",
            "您可以详细说明\x01",
            "委托的内容吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x105,
        (
            "#6P#10304F好像是有一位\x01",
            "『演奏家』失踪了？\x02\x03",

            "#10302F如果没猜错，应该就是您\x01",
            "负责照料的演奏家吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x18,
        (
            "#12400F嗯，正是。\x02\x03",

            "我们为了旅行演奏\x01",
            "而来到克洛斯贝尔……\x02\x03",

            "#12406F稍不留神，\x01",
            "就和那个演奏家走散了。\x02\x03",

            "#12400F我对这个城市毫无了解，\x01",
            "想找也无从找起，实在是非常伤脑筋。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        (
            "#6P#00105F确实很麻烦呢……\x01",
            "毕竟克洛斯贝尔市这么大。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x18,
        (
            "#12401F嗯，也有这方面的因素……\x01",
            "但还有更麻烦的问题。\x02\x03",

            "#12400F各位可以帮我找到他吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x76, 0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Jump("loc_39D2")

    label("loc_397B")


    #C0165
    ChrTalk(
        0x18,
        (
            "#12400F我想委托各位\x01",
            "在市内寻找一位\x01",
            "行踪不明的『演奏家』。\x02\x03",

            "你们可以帮我找到他吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D2")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A20")
    Call(0, 34)
    Jump("loc_3ACA")

    label("loc_3A20")


    #C0166
    ChrTalk(
        0x101,
        (
            "#6P#00006F这……\x01",
            "实在抱歉。\x02\x03",

            "我们还有其它工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x18,
        (
            "#12405F是吗……\x01",
            "那真是很遗憾。\x02\x03",

            "#12400F等你们有空以后，\x01",
            "请再来和我说一声吧。\x02\x03",

            "我实在是很着急，\x01",
            "拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x156, 1)

    label("loc_3ACA")

    SetChrPos(0x0, 17460, 0, -4190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_32C2 end

    def Function_34_3AEC(): pass

    label("Function_34_3AEC")


    #C0168
    ChrTalk(
        0x101,
        (
            "#6P#00000F明白了，\x01",
            "交给我们吧。\x02\x03",

            "#00000F那么，您可以\x01",
            "详细描述一下那位\x01",
            "『演奏家』的具体情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x18,
        (
            "#12400F没问题。\x02\x03",

            "演奏家的名字是……\x01",
            "『奥利维尔·朗海姆』。\x02\x03",

            "是个二十多岁的金发男人，\x01",
            "身穿白色大衣，\x01",
            "随身带着一把鲁特琴。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x105,
        (
            "#6P#10305F哦？身上带着乐器，\x01",
            "应该会很显眼。\x02\x03",

            "#10300F找起来应该\x01",
            "不会很困难。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x18,
        (
            "#12400F嗯，如果只是这样，\x01",
            "想把他带回来\x01",
            "应该不难……\x02\x03",

            "#12406F但奥利维尔的性格\x01",
            "有些问题。\x02\x03",

            "明明事情和他没关系，\x01",
            "但他却总爱胡乱插手，\x01",
            "并引出各种麻烦。\x02\x03",

            "#12400F老实说，\x01",
            "实在是个很棘手的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x102,
        "#6P#00105F这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x18,
        (
            "#12400F我本想尽快找到他，\x01",
            "以免影响到旅行演奏的行程……\x01",
            "但现在也不敢抱太大希望了。\x02\x03",

            "#12406F只要在他做出引人注目的蠢事之前\x01",
            "把他抓到就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#6P#00306F身、身为经纪人，\x01",
            "这话说得可真不客气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#6P#00003F总、总之，我们已经大致\x01",
            "掌握了他的情况。\x02\x03",

            "#00000F请问，您觉得他会去\x01",
            "什么样的地方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x18,
        (
            "#12405F嗯，简单来说……\x02\x03",

            "#12400F他挺喜欢去那种\x01",
            "不三不四的地方，\x01",
            "还有热闹的地方。\x02\x03",

            "#12406F也有可能会装成美食家，\x01",
            "跑到一些餐厅……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x109,
        (
            "#6P#10101F总之，就是有可能\x01",
            "惹出麻烦的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x105,
        (
            "#6P#10300F也就是说……\x01",
            "旧城区、欢乐街、后巷……\x01",
            "这类地方的可能性比较高呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x18,
        (
            "#12404F嗯，很有可能……\x02\x03",

            "#12400F……不过，我已经在\x01",
            "欢乐街找过一遍了，\x01",
            "所以可以把这个地方排除。\x02\x03",

            "#12406F他恐怕猜到了我的行动，\x01",
            "所以刻意避开了某些场所吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#6P#00106F原、原来如此……\x02\x03",

            "#00100F说到热闹的地方，\x01",
            "今天的港湾区也算是其中一处。\x02\x03",

            "#00100F我记得公园里正在举办\x01",
            "咪西的外出表演活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x18,
        (
            "#12400F嗯……\x01",
            "总之，我能提供的\x01",
            "线索也就这么多了。\x02\x03",

            "#12406F抱歉，如果能提供更有用的\x01",
            "情报就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00012F哪里，这些情报很有参考价值。\x02\x03",

            "#00000F那我们这就\x01",
            "开始搜索了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x18,
        (
            "#12400F拜托各位了。\x02\x03",

            "如果他太不配合，\x01",
            "稍微让他吃点苦头\x01",
            "也没关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0184
    ChrTalk(
        0x101,
        (
            "#6P#00006F明、明白了……\x01",
            "（他们到底是什么关系呢？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找演奏家】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x156, 0)
    OP_29(0x76, 0x1, 0x1)
    Return()

    # Function_34_3AEC end

    def Function_35_42DC(): pass

    label("Function_35_42DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5320, 1330, 440, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, 1500, 0, -500, 90)
    SetChrPos(0x102, 1550, 0, 500, 90)
    SetChrPos(0x103, 0, 0, -500, 90)
    SetChrPos(0x104, -250, 0, 500, 90)
    SetChrPos(0x109, 1200, 0, 1500, 90)
    SetChrPos(0x105, 500, 0, -1500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(18910, 2000)

    def lambda_439E():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_439E)
    Sleep(50)

    def lambda_43BB():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43BB)
    Sleep(50)

    def lambda_43D8():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43D8)
    Sleep(50)

    def lambda_43F5():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43F5)
    Sleep(50)

    def lambda_4412():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4412)
    Sleep(50)

    def lambda_442F():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_442F)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x104, 1)

    #C0186
    ChrTalk(
        0x101,
        (
            "#00000F好，到达\x01",
            "克洛斯贝尔车站了……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00100F委托人是\x01",
            "车站的安检官吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00000F没错，赶快去问问吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x156, 5)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 2400, 30, -10, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_35_42DC end

    def Function_36_44FF(): pass

    label("Function_36_44FF")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x19, 0xFF)
    OP_68(27700, 5500, 8150, 0)
    MoveCamera(46, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0x101, 28020, 4000, 8480, 0)
    SetChrPos(0x102, 28930, 4000, 8280, 0)
    SetChrPos(0x103, 27000, 4000, 8080, 0)
    SetChrPos(0x104, 27960, 4000, 7100, 0)
    SetChrPos(0x109, 27060, 4000, 6800, 0)
    SetChrPos(0x105, 28850, 4000, 6940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    TurnDirection(0x19, 0x101, 0)
    OP_0D()

    #C0189
    ChrTalk(
        0x19,
        (
            "哦，你们就是\x01",
            "特别任务支援科吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#00000F是的，我们前来受理\x01",
            "支援请求。\x02\x03",

            "您就是共和国的\x01",
            "安检官吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x19,
        (
            "嗯，我是卡尔瓦德共和国军\x01",
            "派来的安检官马洛。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x19,
        (
            "我想立刻说明工作内容，\x01",
            "你们可以接受委托吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_36_44FF end

    def Function_37_468C(): pass

    label("Function_37_468C")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x19, 0xFF)
    OP_68(27700, 5500, 8150, 0)
    MoveCamera(46, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0x101, 28020, 4000, 8480, 0)
    SetChrPos(0x102, 28930, 4000, 8280, 0)
    SetChrPos(0x103, 27000, 4000, 8080, 0)
    SetChrPos(0x104, 27960, 4000, 7100, 0)
    SetChrPos(0x109, 27060, 4000, 6800, 0)
    SetChrPos(0x105, 28850, 4000, 6940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    TurnDirection(0x19, 0x101, 0)
    OP_0D()

    #C0193
    ChrTalk(
        0x19,
        (
            "哦，是你们啊。\x01",
            "现在可以接受委托了吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_37_468C end

    def Function_38_4778(): pass

    label("Function_38_4778")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480C")

    #C0194
    ChrTalk(
        0x101,
        "#00000F是的，请您说明一下吧。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x19,
        (
            "十分感谢，\x01",
            "那我这就开始说明。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 39)
    Jump("loc_48B8")

    label("loc_480C")


    #C0196
    ChrTalk(
        0x101,
        (
            "#00003F抱歉，\x01",
            "我们还有其它工作……\x02\x03",

            "稍后再来可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x19,
        (
            "唔，虽说时间\x01",
            "还不算太紧……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x19,
        (
            "但我们非常忙碌，\x01",
            "请你们尽快吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x156, 6)
    SetChrPos(0x0, 27760, 4000, 8020, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x19, 0xFF)

    label("loc_48B8")

    Return()

    # Function_38_4778 end

    def Function_39_48B9(): pass

    label("Function_39_48B9")


    #C0199
    ChrTalk(
        0x19,
        (
            "要拜托你们的事情\x01",
            "很简单。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x19,
        (
            "那就是对开往共和国的列车\x01",
            "进行安检。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49B9")

    #C0201
    ChrTalk(
        0x101,
        (
            "#00005F列车安检吗？\x02\x03",

            "#00000F我们以前协助过\x01",
            "帝国的安检官，\x01",
            "熟悉安检工作的基本流程。\x02\x03",

            "就是调查列车上\x01",
            "是否有可疑人物\x01",
            "或可疑物品吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x19,
        (
            "没错，\x01",
            "有工作经验就更好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A20")

    label("loc_49B9")


    #C0203
    ChrTalk(
        0x101,
        (
            "#00003F安检……\x02\x03",

            "#00000F就是调查列车上\x01",
            "是否有可疑人物\x01",
            "或可疑物品吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x19,
        (
            "没错，\x01",
            "你们理解得很快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A20")


    #C0205
    ChrTalk(
        0x19,
        (
            "现在毕竟是通商会议期间，\x01",
            "各地的警备力度都比\x01",
            "平时强化了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x19,
        (
            "不仅要比平时更加严格地检查，\x01",
            "还要协助警察的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x19,
        (
            "我们这些安检官\x01",
            "实在是忙不过来了。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("站员的声音")

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……前往共和国的列车\x01",
            "即将抵达一号月台。\x02",
        )
    )

    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请各位乘客\x01",
            "小心脚下，\x01",
            "尽快抵达月台。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x3E8)

    #C0210
    ChrTalk(
        0x19,
        (
            "需要安检的列车\x01",
            "已经到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x19,
        (
            "详细情况就到\x01",
            "月台上说吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助共和国的安检官】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0xFF, 0xF9, 0x0)
    SetScenarioFlags(0x22, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_48B9 end

    def Function_40_4BF8(): pass

    label("Function_40_4BF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2500, 0, -500, 90)
    SetChrPos(0x102, 2250, 0, 500, 90)
    SetChrPos(0x103, 2250, 0, -1600, 90)
    SetChrPos(0x104, 750, 0, 500, 90)
    SetChrPos(0xF4, 750, 0, -800, 90)
    SetChrPos(0xF5, 750, 0, -2000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(30000, 3300, 500, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(31000, 0)
    OP_68(4500, 1300, 500, 8000)
    MoveCamera(45, 13, 0, 8000)
    SetCameraDistance(19000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    BeginChrThread(0x101, 3, 0, 41)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 4)), scpexpr(EXPR_END)), "loc_4DE0")

    #C0213
    ChrTalk(
        0x101,
        (
            "#5P#00006F之前入口明明\x01",
            "还上着锁啊……\x02\x03",

            "#00013F看来是被雾香小姐他们\x01",
            "打开的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D93")

    #C0214
    ChrTalk(
        0x10A,
        (
            "#00601F#6P哼，虽说现在是特殊时期，\x01",
            "但他们竟然如此乱来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DE0")

    #C0215
    ChrTalk(
        0x109,
        (
            "#10108F#6P再怎么说，这也是违法行为，\x01",
            "实在是难以恭维……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE0")


    #C0216
    ChrTalk(
        0x104,
        (
            "#6P#00306F话说回来，一个人都没有啊。\x02\x03",

            "#00301F倒也难怪，\x01",
            "毕竟铁道列车已经停运了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#5P#00106F是啊……铁道公司的职员，\x01",
            "还有帝国和共和国的安检官\x01",
            "都被驱逐了。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        (
            "#6P#00200F雾香小姐和雷克特先生\x01",
            "在三号月台的列车上等着我们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#5P#00001F没错……\x01",
            "我们去月台吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 2000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1A5, 6)
    EventEnd(0x5)
    Return()

    # Function_40_4BF8 end

    def Function_41_4F1C(): pass

    label("Function_41_4F1C")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(600)

    def lambda_4F35():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4F35)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_41_4F1C end

    def Function_42_4F52(): pass

    label("Function_42_4F52")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_68(12070, 1530, -290, 0)
    MoveCamera(43, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, 12590, 30, 60, 90)
    SetChrPos(0x102, 12400, 30, 1030, 90)
    SetChrPos(0x103, 12300, 30, -870, 90)
    SetChrPos(0x104, 11250, 30, 60, 90)
    SetChrPos(0x109, 10940, 30, 1050, 90)
    SetChrPos(0x105, 10920, 30, -950, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x1A, 0x10E, 0x0)
    OP_0D()

    #C0220
    ChrTalk(
        0x1A,
        "……啊，是你们啊～！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x1A,
        (
            "太好了，你们是为\x01",
            "委托而来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00000F辛苦您了，\x01",
            "雷蒙德警官。\x02\x03",

            "#00005F……咦，只有您一个人吗？\x01",
            "多诺邦警督呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x1A,
        (
            "哦，他还有点\x01",
            "别的事情～\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x1A,
        (
            "先让我简单说明一下\x01",
            "委托情况如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#00100F麻烦您了。\x02\x03",

            "#00101F委托内容似乎是\x01",
            "追捕假货商吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x1A,
        "嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1A,
        (
            "由于新市长对法律做了修正，\x01",
            "我们现在终于可以\x01",
            "严厉管制假货商了。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x1A,
        (
            "二科也已经加强了\x01",
            "查办力度。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x1A,
        (
            "就在最近，\x01",
            "那个假货商又\x01",
            "来到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x1A,
        (
            "经过不懈追踪，\x01",
            "我们终于成功在现场取缔了\x01",
            "他们的交易。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10103F假货商……\x01",
            "就是当时从唐古拉姆门前来，\x01",
            "混在旅客之中的那个人吧？\x02\x03",

            "#10105F对了，\x01",
            "那个假货商到底是个怎样的人？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00000F说起来，诺艾尔当时\x01",
            "还帮我们引导了乘客们呢。\x02\x03",

            "#00003F嗯，怎么说呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x1A)

    #C0233
    ChrTalk(
        0x103,
        "#00200F嘴巴很毒。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#00106F而且嗓门大得\x01",
            "惊人。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#00303F奔跑速度简直可以\x01",
            "媲美短跑运动员。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#00012F总之，如果用一句话来形容，\x01",
            "那就是一个『惊人的老婆婆』……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0237
    ChrTalk(
        0x109,
        "#10105F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，听起来很有趣，\x01",
            "真想见见她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#00309F……话说回来，\x01",
            "你们的表现还真是出色啊。\x02\x03",

            "竟然能把那位老婆婆\x01",
            "逼上绝境！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x1A,
        (
            "嗯，是啊……\x01",
            "开始时还算顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x1A,
        (
            "但她最后还是\x01",
            "凭着惊人的速度\x01",
            "逃掉了……\x02",
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

    #C0242
    ChrTalk(
        0x103,
        "#00206F那位老婆婆真是不知悔改啊……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x105,
        (
            "#10300F这么说……\x01",
            "逃脱的假货商\x01",
            "就在这个车站里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x1A,
        (
            "嗯，正是！\x01",
            "你的洞察力真强～\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1A,
        (
            "她似乎是想\x01",
            "逃往帝国。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1A,
        (
            "呵呵，她肯定以为自己\x01",
            "已经把警察彻底甩掉了～\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x1A,
        (
            "我刚才去二号月台看了看，\x01",
            "她正在悠闲地等待列车抵达呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#00100F开往帝国的列车\x01",
            "再过一段时间才会到站……\x01",
            "现在就是抓捕她的大好时机啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        (
            "#00305F……嗯？\x01",
            "既然准备工作已经\x01",
            "做得这么完善了……\x02\x03",

            "#00303F好像也不需要\x01",
            "我们帮忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1A,
        "这、这个嘛～\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x1A,
        (
            "因为多诺邦警督很忙，\x01",
            "所以就把这个任务全权交托给我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x1A,
        (
            "可是……光靠我一个人，\x01",
            "实在是没有抓到\x01",
            "那个假货商的自信……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#00006F嗯……\x01",
            "抛开自信的问题不说，\x01",
            "人手确实不够啊。\x02\x03",

            "#00001F在这个宽广的车站内，\x01",
            "如果不建起严密的包围网，\x01",
            "很有可能会被她逃脱的。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x1A,
        (
            "对吧～？\x01",
            "所以我才会\x01",
            "请你们来援助嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x1A,
        (
            "希望你们协助\x01",
            "我一起抓捕\x01",
            "那个假货商。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x1A,
        (
            "另外还要做好监视工作，\x01",
            "不要让她逃出\x01",
            "这个车站。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x1A,
        (
            "毕竟你们以前抓到过那个\x01",
            "假货商，肯定没问题的。\x01",
            "如何？愿意帮帮我吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x0)
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_42_4F52 end

    def Function_43_5939(): pass

    label("Function_43_5939")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_68(12070, 1530, -290, 0)
    MoveCamera(43, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, 12590, 30, 60, 90)
    SetChrPos(0x102, 12400, 30, 1030, 90)
    SetChrPos(0x103, 12300, 30, -870, 90)
    SetChrPos(0x104, 11250, 30, 60, 90)
    SetChrPos(0x109, 10940, 30, 1050, 90)
    SetChrPos(0x105, 10920, 30, -950, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x1A, 0x10E, 0x0)
    OP_0D()

    #C0258
    ChrTalk(
        0x1A,
        (
            "希望你们协助\x01",
            "我一起抓捕\x01",
            "那个假货商。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1A,
        (
            "另外还要做好监视工作，\x01",
            "不要让她逃出\x01",
            "这个车站。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1A,
        (
            "毕竟你们以前抓到过那个\x01",
            "假货商，肯定没问题的。\x01",
            "如何？愿意帮帮我吗～？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_43_5939 end

    def Function_44_5AAA(): pass

    label("Function_44_5AAA")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF5")
    Jump("loc_5BD4")

    label("loc_5AF5")


    #C0261
    ChrTalk(
        0x101,
        (
            "#00006F……抱歉，\x01",
            "我们还有其它工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x1A,
        (
            "唔，这样啊～\x01",
            "那就没办法了……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1A,
        (
            "那么，\x01",
            "我会在这里继续\x01",
            "等待机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x1A,
        (
            "如果你们有空了，\x01",
            "一定要来\x01",
            "帮帮我哦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x173, 4)
    SetChrPos(0x0, 11560, 30, -10, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_93(0x1A, 0x5A, 0x0)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    OP_69(0xFF, 0x0)
    Return()

    label("loc_5BD4")


    #C0265
    ChrTalk(
        0x101,
        (
            "#00000F……好的，我明白了，\x01",
            "我们会提供协助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x1A,
        (
            "哦哦，太好了！\x01",
            "真是感激不尽～\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x1A,
        (
            "那么……先分出一个小组，\x01",
            "随我一起去抓捕\x01",
            "那个假货商吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x1A,
        (
            "谁跟我\x01",
            "一起去？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x01",
            "该怎么分配呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#00203F最好让有搜查官资格的\x01",
            "罗伊德前辈同行。\x02\x03",

            "#00211F……如果只有雷蒙德警官一位搜查官，\x01",
            "总觉得有点不放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x1A,
        "别、别这么说嘛……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1A,
        (
            "……但话说回来，你的提议\x01",
            "确实比较稳妥～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0273
    ChrTalk(
        0x101,
        (
            "#00012F那、那么……\x01",
            "就由两名搜查官带队吧。\x02\x03",

            "#00000F另外再找一个人支援，\x01",
            "剩下的四个人就负责\x01",
            "监视站内吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        (
            "#00100F那么……\x01",
            "要带谁一起去？\x02",
        )
    )

    CloseMessageWindow()
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
            "带上艾莉\x01",        # 0
            "带上缇欧\x01",        # 1
            "带上兰迪\x01",        # 2
            "带上诺艾尔\x01",      # 3
            "带上瓦吉\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ED1")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 500)

    #C0275
    ChrTalk(
        0x101,
        "#00000F艾莉，跟我来吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0276
    ChrTalk(
        0x102,
        "#00100F好的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x1)
    Jump("loc_604D")

    label("loc_5ED1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F32")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    #C0277
    ChrTalk(
        0x101,
        "#00000F缇欧，跟我来吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0278
    ChrTalk(
        0x103,
        "#00200F明白。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x2)
    Jump("loc_604D")

    label("loc_5F32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F93")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x104, 500)

    #C0279
    ChrTalk(
        0x101,
        "#00000F兰迪，跟我来吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0280
    ChrTalk(
        0x104,
        "#00309F好啊。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x3)
    Jump("loc_604D")

    label("loc_5F93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FFA")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x109, 500)

    #C0281
    ChrTalk(
        0x101,
        "#00000F诺艾尔，跟我来吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0282
    ChrTalk(
        0x109,
        "#10100F是，队长！\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x4)
    Jump("loc_604D")

    label("loc_5FFA")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x105, 500)

    #C0283
    ChrTalk(
        0x101,
        "#00000F瓦吉，跟我来吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0284
    ChrTalk(
        0x105,
        "#10304F遵命，队长。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x5)

    label("loc_604D")

    TurnDirection(0x101, 0x104, 500)

    #C0285
    ChrTalk(
        0x101,
        (
            "#00003F剩下的各位就负责\x01",
            "监视车站的出入口吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_608B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_608B)
    Sleep(50)

    def lambda_609B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_609B)
    Sleep(50)

    def lambda_60AB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_60AB)
    Sleep(50)

    def lambda_60BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_60BB)
    Sleep(100)

    #C0286
    ChrTalk(
        0x101,
        (
            "#00001F目标毕竟是那位老婆婆，\x01",
            "为了预防万一，\x01",
            "请大家打起十二分精神。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x102, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 45)
    Sleep(50)
    BeginChrThread(0x1A, 1, 0, 45)
    Sleep(1500)
    OP_68(15530, 1530, 8500, 3000)
    MoveCamera(43, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(18860, 3000)
    BeginChrThread(0x1B, 1, 0, 46)
    BeginChrThread(0x1C, 1, 0, 47)
    OP_6F(0x79)
    Sleep(1000)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)

    def lambda_619A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_619A)

    def lambda_61A7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_61A7)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)

    #C0287
    ChrTalk(
        0x1B,
        (
            "……没在站内\x01",
            "看到那些家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x1C,
        (
            "说不定已经乘上\x01",
            "列车了。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x1C,
        "……赶快行动吧。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 1, 0, 48)
    BeginChrThread(0x1C, 1, 0, 49)
    Sleep(1000)
    OP_68(20050, 1530, 7050, 2000)
    MoveCamera(45, 20, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(20000, 2000)
    OP_6F(0x79)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A, 0x1)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x1A)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【追捕假货商】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x173, 5)
    SetChrPos(0x0, 11650, 30, -510, 90)
    OP_93(0x1A, 0x5A, 0x0)
    OP_4C(0x1A, 0xFF)
    OP_69(0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6324")
    AddParty(0x1, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 3)
    Jump("loc_637C")

    label("loc_6324")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_633F")
    AddParty(0x2, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 4)
    Jump("loc_637C")

    label("loc_633F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_635A")
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 5)
    Jump("loc_637C")

    label("loc_635A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6375")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 6)
    Jump("loc_637C")

    label("loc_6375")

    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 7)

    label("loc_637C")

    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_44_5AAA end

    def Function_45_639A(): pass

    label("Function_45_639A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64B2")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_63DD"),
        (1, "loc_63F7"),
        (2, "loc_6411"),
        (3, "loc_642B"),
        (4, "loc_6445"),
        (5, "loc_645F"),
        (6, "loc_6479"),
        (SWITCH_DEFAULT, "loc_6493"),
    )


    label("loc_63DD")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_64AD")

    label("loc_63F7")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_64AD")

    label("loc_6411")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_64AD")

    label("loc_642B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_64AD")

    label("loc_6445")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_64AD")

    label("loc_645F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_64AD")

    label("loc_6479")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_64AD")

    label("loc_6493")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_64AD")

    label("loc_64AD")

    Jump("Function_45_639A")

    label("loc_64B2")

    Return()

    # Function_45_639A end

    def Function_46_64B3(): pass

    label("Function_46_64B3")

    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_46_64B3 end

    def Function_47_64D2(): pass

    label("Function_47_64D2")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    Return()

    # Function_47_64D2 end

    def Function_48_64F1(): pass

    label("Function_48_64F1")

    Sleep(600)
    OP_95(0xFE, 19770, 30, 7340, 2000, 0x0)
    OP_95(0xFE, 23810, 0, 7440, 2000, 0x0)
    Return()

    # Function_48_64F1 end

    def Function_49_651D(): pass

    label("Function_49_651D")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19710, 30, 8420, 2000, 0x0)
    Sound(100, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_95(0xFE, 23490, 0, 8520, 2000, 0x0)
    Return()

    # Function_49_651D end

    def Function_50_6566(): pass

    label("Function_50_6566")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13600, 1330, -370, 0)
    MoveCamera(38, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17100, 0)
    LoadChrToIndex("chr/ch30200.itc", 0x1F)
    SetChrChipByIndex(0x1A, 0x1F)
    EndChrThread(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x101, 14910, 30, 670, 270)
    SetChrPos(0x102, 15040, 30, -640, 270)
    SetChrPos(0x103, 14090, 30, 1470, 225)
    SetChrPos(0x104, 14050, 30, -1590, 315)
    SetChrPos(0x109, 12820, 30, 1230, 145)
    SetChrPos(0x105, 12790, 30, -1260, 45)
    SetChrPos(0x1A, 12140, 30, 30, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_674E")

    #C0291
    ChrTalk(
        0x104,
        (
            "#00306F听说你们跑到\x01",
            "共和国时，\x01",
            "我真是吓了一跳……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#00200F原来发生了那种事啊。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，没有联络大家，\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#00012F还好抓到那个\x01",
            "假货商了，\x01",
            "结果还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x105,
        "#10300F呵呵，说的也是。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        "#10109F哈哈，我也这么想。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B56")

    label("loc_674E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_685A")

    #C0297
    ChrTalk(
        0x102,
        (
            "#00106F听说你们跑到\x01",
            "共和国时，\x01",
            "我真是吓了一跳……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#00300F真是的，居然发生了\x01",
            "那种事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#00203F当时应该先和大家联络才对，\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#00012F还好抓到那个\x01",
            "假货商了，\x01",
            "结果还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x105,
        "#10300F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x109,
        "#10109F哈哈，我也这么想。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B56")

    label("loc_685A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_695C")

    #C0303
    ChrTalk(
        0x109,
        (
            "#10106F听说你们跑到\x01",
            "共和国时，\x01",
            "我真是吓了一跳……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x105,
        (
            "#10300F真是的，居然发生了\x01",
            "那种事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，抱歉抱歉，\x01",
            "毕竟事态紧急嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00012F还好抓到那个\x01",
            "假货商了，\x01",
            "结果还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#00100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x103,
        "#00204F我也这么想。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B56")

    label("loc_695C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_6A60")

    #C0309
    ChrTalk(
        0x105,
        (
            "#10306F听说你们跑到\x01",
            "共和国时，\x01",
            "连我都吃了一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#00300F真是的，居然发生了\x01",
            "那种事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10109F啊哈哈……\x01",
            "抱歉，没有及时联络大家。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00012F还好抓到那个\x01",
            "假货商了，\x01",
            "结果还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#00100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#00204F我也这么想。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B56")

    label("loc_6A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_6B56")

    #C0315
    ChrTalk(
        0x109,
        (
            "#10106F听说你们跑到\x01",
            "共和国时，\x01",
            "我真是吓了一跳……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#00300F真是的，居然发生了\x01",
            "那种事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x105,
        "#10309F呵呵，当时的事态很紧急呢。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#00012F还好抓到那个\x01",
            "假货商了，\x01",
            "结果还算不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        "#00100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#00204F我也这么想。\x02",
    )

    CloseMessageWindow()

    label("loc_6B56")


    #C0321
    ChrTalk(
        0x1A,
        (
            "好了，我得赶快返回二科，\x01",
            "趴在办公桌上写报告书……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x1A,
        "就先告辞啦。\x02",
    )

    CloseMessageWindow()

    def lambda_6BA4():

        label("loc_6BA4")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_6BA4")

    QueueWorkItem2(0x103, 1, lambda_6BA4)

    def lambda_6BB6():

        label("loc_6BB6")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_6BB6")

    QueueWorkItem2(0x104, 1, lambda_6BB6)

    def lambda_6BC8():

        label("loc_6BC8")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_6BC8")

    QueueWorkItem2(0x109, 1, lambda_6BC8)

    def lambda_6BDA():

        label("loc_6BDA")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_6BDA")

    QueueWorkItem2(0x105, 1, lambda_6BDA)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_6C15")

    #C0323
    ChrTalk(
        0x102,
        "#00109F呵呵，您辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CB6")

    label("loc_6C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_6C3A")

    #C0324
    ChrTalk(
        0x103,
        "#00202F您辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CB6")

    label("loc_6C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_6C63")

    #C0325
    ChrTalk(
        0x104,
        "#00309F哈哈，辛苦啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CB6")

    label("loc_6C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_6C92")

    #C0326
    ChrTalk(
        0x109,
        "#10109F呵呵，您真是辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CB6")

    label("loc_6C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_6CB6")

    #C0327
    ChrTalk(
        0x105,
        "#10302F呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_6CB6")


    #C0328
    ChrTalk(
        0x1A,
        (
            "哪里哪里，多亏你们\x01",
            "一直帮我到最后。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x1A,
        (
            "如果只有我一个人，\x01",
            "肯定抓不到\x01",
            "那位老婆婆。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x1A,
        "今天真是谢谢你们了！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00004F哪里，客气了。\x02\x03",

            "#00000F如果以后还有什么困难，\x01",
            "请联络我们支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x1A,
        "嗯，到时就拜托了！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)

    def lambda_6D9A():
        OP_95(0xFE, 3980, 30, 220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6D9A)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x1A, 0x80)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0333
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【追捕假货商】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x81, 0x1, 0x8)
    OP_29(0x81, 0x1, 0x9)
    OP_29(0x81, 0x4, 0x10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 13970, 30, -400, 270)
    EventEnd(0x5)
    Return()

    # Function_50_6566 end

    def Function_51_6E4D(): pass

    label("Function_51_6E4D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "←前往共和国方向·一号线月台\x01",
            "　　　共和国阿尔泰尔市　３５分\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_51_6E4D end

    def Function_52_6EC1(): pass

    label("Function_52_6EC1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "前往帝国方向·二号线月台→\x01",
            "　　　　帝国卡雷利亚要塞　　３２分\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_6EC1 end

    def Function_53_6F37(): pass

    label("Function_53_6F37")

    TalkBegin(0xFF)
    SetChrName("")

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是克洛斯贝尔自治州\x01",
            "及周边地区的列车时刻表。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_53_6F37 end

    def Function_54_6F76(): pass

    label("Function_54_6F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F8D")
    Call(0, 56)
    Return()

    label("loc_6F8D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※※　安检官办公室　※※\x01",
            "        无关人员\x01",
            "        严禁入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_54_6F76 end

    def Function_55_7002(): pass

    label("Function_55_7002")

    TalkBegin(0xFF)
    SetChrName("")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是克洛斯贝尔自治州\x01",
            "及周边地区的线路图。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_55_7002 end

    def Function_56_703D(): pass

    label("Function_56_703D")

    EventBegin(0x0)
    Fade(500)
    OP_68(27750, 5100, 10310, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18910, 0)
    SetChrPos(0x101, 28770, 4000, 9430, 0)
    SetChrPos(0x102, 26280, 4000, 8830, 45)
    SetChrPos(0x103, 27490, 4000, 8660, 0)
    SetChrPos(0x104, 28740, 4000, 8290, 315)
    SetChrPos(0xF4, 25940, 4000, 7480, 0)
    SetChrPos(0xF5, 27640, 4000, 7700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0339
    ChrTalk(
        0x103,
        (
            "#12P#00200F……里面果然\x01",
            "空无一人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        (
            "#6P#00103F铁路已经停运，\x01",
            "帝国和共和国的安检官\x01",
            "也都被驱逐了。\x02\x03",

            "#00100F站员们现在应该\x01",
            "都在不同的地方\x01",
            "避难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#12P#00303F嗯，显然没有继续留在\x01",
            "这种地方的理由啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#5P#00000F我们还是赶快去见\x01",
            "雾香小姐他们吧。\x02\x03",

            "从下层的入口就能\x01",
            "抵达月台。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 27770, 4000, 9430, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1CD, 7)
    EventEnd(0x5)
    Return()

    # Function_56_703D end

    SaveToFile()

Try(main)
