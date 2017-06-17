from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0150.bin",                # FileName
        "c0150",                    # MapName
        "c0150",                    # Location
        0x0007,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0150",                  # 0
        "霍伊斯托夫",             # 1
        "布拉温",                 # 2
        "赛尔缇欧",               # 3
        "侬诺",                   # 4
        "弗罗缇",                 # 5
        "游客",                   # 6
        "游客",                   # 7
        "市民",                   # 8
        "市民",                   # 9
        "市民",                   # 10
        "市民",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "市民",                   # 16
        "市民",                   # 17
        "约纳",                   # 18
        "罗伯兹主任",             # 19
        "亚贝尔",                 # 20
        "米米",                   # 21
        "萨莉",                   # 22
        "雾香辅佐官",             # 23
        "基隆德",                 # 24
        "克莱德",                 # 25
        "玛格丽特夫人",           # 26
        "料理",                   # 27
        "料理",                   # 28
        "料理",                   # 29
        "料理",                   # 30
        "料理",                   # 31
        "料理",                   # 32
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch24502.itc",                   # 06
        "chr/ch21302.itc",                   # 07
        "chr/ch21702.itc",                   # 08
        "chr/ch21602.itc",                   # 09
        "chr/ch21002.itc",                   # 0A
        "chr/ch20302.itc",                   # 0B
        "chr/ch33202.itc",                   # 0C
        "chr/ch33102.itc",                   # 0D
        "chr/ch32302.itc",                   # 0E
        "chr/ch22102.itc",                   # 0F
        "chr/ch20502.itc",                   # 10
        "chr/ch24402.itc",                   # 11
        "chr/ch06102.itc",                   # 12
        "chr/ch29302.itc",                   # 13
        "chr/ch20202.itc",                   # 14
        "chr/ch20702.itc",                   # 15
        "chr/ch34602.itc",                   # 16
        "chr/ch13302.itc",                   # 17
    ))

    DeclNpc(-509,    0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-52029,  0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  325,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   6,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(2430,    5150,    17639,   180,  453,  0x0, 0,   8,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(2430,    5150,    13430,   0,    453,  0x0, 0,   9,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(3230,    150,     -1789,   180,  453,  0x0, 0,   10,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(5440,    150,     -3990,   270,  453,  0x0, 0,   11,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(6360,    5150,    17639,   180,  453,  0x0, 0,   12,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(6360,    5150,    13439,   0,    453,  0x0, 0,   13,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   14,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   15,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(3230,    150,     -1789,   180,  453,  0x0, 0,   16,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(5440,    150,     -3990,   270,  453,  0x0, 0,   17,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-1649,   5150,    17649,   180,  453,  0x0, 0,   18,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(-1649,   5150,    13439,   0,    453,  0x0, 0,   19,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(3190,    150,     -6150,   0,    389,  0x0, 0,   20,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(5440,    150,     -3990,   270,  389,  0x0, 0,   21,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3230,    150,     -1789,   180,  389,  0x0, 0,   22,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(-1679,   5150,    17739,   180,  453,  0x0, 0,   23,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-3200,   699,     3349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-3200,   699,     1350,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4199,   699,     2349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-2200,   699,     2349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4000,   699,     1549,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-4000,   699,     3150,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  5,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  7,  0x0000)
    DeclActor(-39700,  0,       7810,    2000,    -39700,  1700,    7810,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1424, 0)                                       # 0

    ScpFunction((
        "Function_0_590",          # 00, 0
        "Function_1_648",          # 01, 1
        "Function_2_6E5",          # 02, 2
        "Function_3_D37",          # 03, 3
        "Function_4_DB1",          # 04, 4
        "Function_5_E99",          # 05, 5
        "Function_6_E9D",          # 06, 6
        "Function_7_22D8",         # 07, 7
        "Function_8_22DC",         # 08, 8
        "Function_9_3580",         # 09, 9
        "Function_10_42BD",        # 0A, 10
        "Function_11_52AE",        # 0B, 11
        "Function_12_5DC6",        # 0C, 12
        "Function_13_6C5A",        # 0D, 13
        "Function_14_6CE9",        # 0E, 14
        "Function_15_6DB9",        # 0F, 15
        "Function_16_6E48",        # 10, 16
        "Function_17_6EE9",        # 11, 17
        "Function_18_6FF0",        # 12, 18
        "Function_19_709E",        # 13, 19
        "Function_20_7184",        # 14, 20
        "Function_21_72B6",        # 15, 21
        "Function_22_7477",        # 16, 22
        "Function_23_7670",        # 17, 23
        "Function_24_7734",        # 18, 24
        "Function_25_785A",        # 19, 25
        "Function_26_7A95",        # 1A, 26
        "Function_27_7CBA",        # 1B, 27
        "Function_28_7E4F",        # 1C, 28
        "Function_29_7F80",        # 1D, 29
        "Function_30_7FCD",        # 1E, 30
        "Function_31_8EDE",        # 1F, 31
        "Function_32_9954",        # 20, 32
        "Function_33_9BD3",        # 21, 33
        "Function_34_A73A",        # 22, 34
        "Function_35_B4E9",        # 23, 35
        "Function_36_B519",        # 24, 36
        "Function_37_B55F",        # 25, 37
        "Function_38_B5A5",        # 26, 38
        "Function_39_B5DC",        # 27, 39
        "Function_40_B613",        # 28, 40
        "Function_41_B659",        # 29, 41
        "Function_42_B69D",        # 2A, 42
        "Function_43_B6E1",        # 2B, 43
    ))


    def Function_0_590(): pass

    label("Function_0_590")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5D0"),
        (1, "loc_5DC"),
        (2, "loc_5E8"),
        (3, "loc_5F4"),
        (4, "loc_600"),
        (5, "loc_60C"),
        (6, "loc_618"),
        (SWITCH_DEFAULT, "loc_624"),
    )


    label("loc_5D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_5DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_5E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_5F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_600")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_60C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_618")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_624")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_630")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_647")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_647")

    Return()

    # Function_0_590 end

    def Function_1_648(): pass

    label("Function_1_648")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_648")

    label("loc_6E4")

    Return()

    # Function_1_648 end

    def Function_2_6E5(): pass

    label("Function_2_6E5")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_704")
    Jump("loc_D0E")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_76B")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x14)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x16)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x15)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    Jump("loc_D0E")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7A5")
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x10)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x11)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_D0E")

    label("loc_7A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7DF")
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x10)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x11)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_D0E")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_847")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8AF")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_8AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_917")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_97F")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A13")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x12)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x13)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    Jump("loc_D0E")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AB1")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jump("loc_D0E")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_ABF")
    Jump("loc_D0E")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B86")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B05")
    SetChrFlags(0xB, 0x10)

    label("loc_B05")

    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B81")
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0x17)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)

    label("loc_B81")

    Jump("loc_D0E")

    label("loc_B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C24")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jump("loc_D0E")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C94")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_D0E")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D0E")
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)

    label("loc_D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D36")
    SetMapFlags(0x10000000)
    Event(0, 34)

    label("loc_D36")

    Return()

    # Function_2_6E5 end

    def Function_3_D37(): pass

    label("Function_3_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D6A")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D93")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_D93")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DB0")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_DB0")

    Return()

    # Function_3_D37 end

    def Function_4_DB1(): pass

    label("Function_4_DB1")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  新料理·香草面\x01",
            " ·客人怀念的味道再次重现\x01",
            " ·清爽的香草口味\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书写着香草面的食谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_E95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E95")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『香草面』\x07\x00",
            "的食谱已经记住了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E95")

    TalkEnd(0xFF)
    Return()

    # Function_4_DB1 end

    def Function_5_E99(): pass

    label("Function_5_E99")

    Call(0, 6)
    Return()

    # Function_5_E99 end

    def Function_6_E9D(): pass

    label("Function_6_E9D")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1028")

    #C0004
    ChrTalk(
        0x1F,
        "哟，特别任务支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x1F,
        (
            "我听赛尔盖说了，\x01",
            "你们终于恢复工作了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0006
    ChrTalk(
        0x1F,
        (
            "嗯？那个红毛小哥\x01",
            "和那个拿魔导杖的小姑娘\x01",
            "没在啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00000F嗯，他们两个\x01",
            "还有点事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x1F,
        "嗯，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x1F,
        (
            "那两位就是\x01",
            "你们的新成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x1F,
        (
            "武器的事情，赛尔盖已经和我交代过了。\x01",
            "你们就随便挑挑吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x105,
        "#10302F呵呵，事前准备工作做得真不错啊。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        "#10102F谢谢您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 2)

    label("loc_1028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12B4")
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0013
    ChrTalk(
        0x1F,
        (
            "哦，是你们啊……\x01",
            "你们总算来了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000F基隆德先生，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11D2")

    #C0015
    ChrTalk(
        0x1F,
        (
            "嘿嘿，看你们一脸信心十足的表情，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x1F,
        (
            "不过，竟然连达德利也在一起……\x01",
            "看来终于要正式行动了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x10A,
        (
            "#00603F嗯，也许会引起一些\x01",
            "骚乱，还请谅解。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x1F,
        (
            "嘿，事到如今，\x01",
            "谁还会在意那些。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x1F,
        (
            "总之，\x01",
            "店里目前还有\x01",
            "不少品种的存货。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1F,
        (
            "虽然没有特别好的东西，\x01",
            "但你们不妨随便挑挑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1296")

    label("loc_11D2")


    #C0021
    ChrTalk(
        0x1F,
        (
            "嘿嘿，看你们一脸信心十足的表情，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x1F,
        (
            "我听那些警察\x01",
            "说了不少消息，\x01",
            "已经没必要再多说了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x1F,
        (
            "总之，\x01",
            "店里目前还有\x01",
            "不少品种的存货。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x1F,
        (
            "虽然没有特别好的东西，\x01",
            "但你们不妨随便挑挑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1296")


    #C0025
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 0)

    label("loc_12B4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_130E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_130E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_132D")
    OP_AF(0x5)
    Jump("loc_136F")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_133D")
    OP_AF(0x4)
    Jump("loc_136F")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_134D")
    OP_AF(0x3)
    Jump("loc_136F")

    label("loc_134D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_135D")
    OP_AF(0x2)
    Jump("loc_136F")

    label("loc_135D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_136D")
    OP_AF(0x1)
    Jump("loc_136F")

    label("loc_136D")

    OP_AF(0x0)

    label("loc_136F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22CF")

    label("loc_137E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1392")
    Jump("loc_22CF")

    label("loc_1392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22CF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_142B")

    #C0026
    ChrTalk(
        0x1F,
        (
            "呼，那棵诡异的大树暂且不说，\x01",
            "至少市里总算恢复平静了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x1F,
        (
            "今后的情况应该很麻烦吧……\x01",
            "但我们一定要拼到最后。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CF")

    label("loc_142B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_149B")

    #C0028
    ChrTalk(
        0x1F,
        (
            "嘿，话说回来，没想到又能见到\x01",
            "特别任务支援科的各位了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x1F,
        (
            "总之，你们今后也要\x01",
            "多加努力啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CF")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1578")

    #C0030
    ChrTalk(
        0x1F,
        (
            "国防军吗，迪塔·库罗伊斯\x01",
            "又做出了惊人之举啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x1F,
        (
            "竟然连制服都准备好了，\x01",
            "还真是万分周到。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x1F,
        (
            "武器和兵器这种东西，\x01",
            "要是根本不存在就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1F,
        (
            "呼，但也不能说得这么绝对，\x01",
            "这就是现实吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15FE")

    label("loc_1578")


    #C0034
    ChrTalk(
        0x1F,
        (
            "武器和兵器这种东西，\x01",
            "要是根本不存在就好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1F,
        (
            "呼，但也不能说得这么绝对，\x01",
            "这就是现实吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x1F,
        "哎呀呀……未来真是让人担心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_15FE")

    Jump("loc_22CF")

    label("loc_1603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_174B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E9")

    #C0037
    ChrTalk(
        0x1F,
        (
            "由于玛因兹之前的那起骚乱，\x01",
            "市民们纷纷跑到我的店里，\x01",
            "要求购买武器。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x1F,
        (
            "如果对方没有许可证，\x01",
            "我是不能出售武器的……\x01",
            "但有些人实在是纠缠不休。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1F,
        (
            "当然啦，在这种状况下，\x01",
            "也不是不能理解他们的心情……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1746")

    label("loc_16E9")


    #C0040
    ChrTalk(
        0x1F,
        (
            "总之，要想使用武器，\x01",
            "需要拥有与之相应的\x01",
            "责任感与觉悟。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1F,
        (
            "你们也把这句话\x01",
            "牢记在心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1746")

    Jump("loc_22CF")

    label("loc_174B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1846")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E5")

    #C0042
    ChrTalk(
        0x1F,
        (
            "哦，你们今天好像\x01",
            "也很焦躁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x1F,
        (
            "如果准备前往\x01",
            "危险的场所，\x01",
            "准备工作一定不能怠慢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x1F,
        "我可不希望听到顾客死亡的消息啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1841")

    label("loc_17E5")


    #C0045
    ChrTalk(
        0x1F,
        (
            "如果准备前往\x01",
            "危险的场所，\x01",
            "准备工作一定不能怠慢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x1F,
        "我可不希望听到顾客死亡的消息啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1841")

    Jump("loc_22CF")

    label("loc_1846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_198E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1918")

    #C0047
    ChrTalk(
        0x1F,
        (
            "有传闻说，昨天发生的\x01",
            "那起列车事故是由一只\x01",
            "恶鬼般的怪物所引起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1F,
        (
            "恶鬼般的……说得倒是简单，\x01",
            "但实际上到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x1F,
        (
            "总不能是人类\x01",
            "化成的吧……\x01",
            "总之，真是让人不安啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1989")

    label("loc_1918")


    #C0050
    ChrTalk(
        0x1F,
        (
            "恶鬼般的……说得倒是简单，\x01",
            "但实际上到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1F,
        (
            "总不能是人类\x01",
            "化成的吧……\x01",
            "总之，真是让人不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1989")

    Jump("loc_22CF")

    label("loc_198E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19EE")

    #C0052
    ChrTalk(
        0x1F,
        (
            "呼，警笛声真是\x01",
            "吵死人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x1F,
        (
            "不知道是事件还是事故……\x01",
            "这城市真是太喧闹了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CF")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABB")

    #C0054
    ChrTalk(
        0x1F,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x1F,
        (
            "想买什么都可以，\x01",
            "尽量快点挑就行了，越快越好。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x1F,
        (
            "你们要是一直不走，\x01",
            "我就没法专心看杂志了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00006F（……店主还是老样子，\x01",
            "  完全不想认真工作呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B15")

    label("loc_1ABB")


    #C0058
    ChrTalk(
        0x1F,
        (
            "我不知道你们想买什么，\x01",
            "总之快点挑吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x1F,
        (
            "你们要是一直不走，\x01",
            "我就没法专心看杂志了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B15")

    Jump("loc_22CF")

    label("loc_1B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1BA8")

    #C0060
    ChrTalk(
        0x1F,
        (
            "哎呀，虽说不能无条件地接受两大国\x01",
            "的所有要求，但竟在这种时候提议独立……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x1F,
        (
            "呼，不管怎么说，先祈祷\x01",
            "接下来不要发生战争吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CF")

    label("loc_1BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE7")

    #C0062
    ChrTalk(
        0x1F,
        (
            "哟，小姑娘，\x01",
            "你总算回归支援科了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x1F,
        (
            "那个男人把魔导杖放到我这里的时候，\x01",
            "我就猜到你差不多该回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00005F那、那个男人难道是……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#00203F嗯，不用说，肯定是罗伯兹主任。\x02\x03",

            "#00211F这种被提前算计到的感觉\x01",
            "真是让人很不爽。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#00109F算、算啦，\x01",
            "他只是关心你而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00000F嗯，我也觉得\x01",
            "他是个很好的人，\x01",
            "并没有恶意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#00206F……的确不能否认这一点，\x01",
            "但说不定就是因为这样，更让人觉得讨厌。\x02\x03",

            "#00200F他特别爱多管闲事，\x01",
            "明明很笨，却还经常说些没用的话……\x01",
            "我和他实在是合不来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCD")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1DCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF3")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1DF3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E19")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E19")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E3F")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1E3F")

    Sleep(1000)

    #C0069
    ChrTalk(
        0x109,
        (
            "#10103F是、是吗……\x01",
            "缇欧也有很多自己的理由啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x1F,
        (
            "哈哈哈哈，虽然听不太明白，\x01",
            "但总而言之，今后我会恢复魔导杖的销售。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x1F,
        "如果有需要，可以随时来找我。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 5)
    Jump("loc_1F3F")

    label("loc_1EE7")


    #C0072
    ChrTalk(
        0x1F,
        (
            "因为小姑娘归队，\x01",
            "我又恢复魔导杖的销售了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x1F,
        (
            "总之，如果有需要，\x01",
            "可以随时来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3F")

    Jump("loc_22CF")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2054")

    #C0074
    ChrTalk(
        0x1F,
        (
            "哟，这不是达德利嘛。在和支援科\x01",
            "的人一起散步？关系真好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x10A,
        (
            "#00603F不，只是有些让人比较在意的事情。\x02\x03",

            "#00600F光靠这几个家伙实在是不放心，\x01",
            "所以我要与他们同行。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x1F,
        "嘿，你还是老样子啊。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x1F,
        (
            "好啦，我马上就要关店了，\x01",
            "如果想买东西就赶快吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20AB")

    label("loc_2054")


    #C0078
    ChrTalk(
        0x1F,
        (
            "我差不多也该关店了，\x01",
            "如果想买东西就赶快吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x1F,
        "我还想早点收工，好好喝上一杯呢。\x02",
    )

    CloseMessageWindow()

    label("loc_20AB")

    Jump("loc_22CF")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_213C")

    #C0080
    ChrTalk(
        0x1F,
        (
            "我不懂什么通商会议，\x01",
            "但总之不能让两大国\x01",
            "看扁我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x1F,
        (
            "那些家伙一贯嚣张，\x01",
            "只要我们稍稍有些示弱，\x01",
            "他们马上就会得寸进尺。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CF")

    label("loc_213C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_222D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E6")

    #C0082
    ChrTalk(
        0x1F,
        (
            "鲁巴彻覆灭以后，\x01",
            "暗地里的争斗好像有所减少……\x01",
            "却反而让人觉得很不安啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x1F,
        (
            "如果能一直这样安稳下去，\x01",
            "自然是再好不过……但这显然不可能吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2228")

    label("loc_21E6")


    #C0084
    ChrTalk(
        0x1F,
        (
            "最近难得稍微\x01",
            "清闲些。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x1F,
        (
            "女神啊，拜托了，\x01",
            "请不要让我工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2228")

    Jump("loc_22CF")

    label("loc_222D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_228F")

    #C0086
    ChrTalk(
        0x1F,
        (
            "呼，今天又下\x01",
            "大雨了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1F,
        (
            "不过，这里门窗都紧闭着，\x01",
            "下雨倒是和我没什么关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22CF")

    label("loc_228F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_22CF")

    #C0088
    ChrTalk(
        0x1F,
        (
            "你们使用的武器，\x01",
            "这里一应俱全。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x1F,
        "随便看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_22CF")

    Jump("loc_12BE")

    label("loc_22D4")

    TalkEnd(0x1F)
    Return()

    # Function_6_E9D end

    def Function_7_22D8(): pass

    label("Function_7_22D8")

    Call(0, 8)
    Return()

    # Function_7_22D8 end

    def Function_8_22DC(): pass

    label("Function_8_22DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2313")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2313")
    Call(0, 33)
    Return()

    label("loc_2313")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F4")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x8,
        "哦，你们是警察局的……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "听说你们不受国防军的管制，\x01",
            "而是独自行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00000F是的，我们正在\x01",
            "努力平息如今\x01",
            "的事态。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#00100F你们这里遇到\x01",
            "什么麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "哦，这里只有少量客人\x01",
            "和工作人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "和其它地方相比，\x01",
            "应该还算是安稳吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "而且这里是餐厅，\x01",
            "食物问题倒是不用发愁。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00003F原来如此，\x01",
            "那就让人放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00103F不管怎么说，\x01",
            "现在外出是很危险的。\x02\x03",

            "#00100F请店长和大家\x01",
            "暂时留在店内。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 7)
    TalkEnd(0x8)
    Return()

    label("loc_24F4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_254E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_254E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_256D")
    OP_AF(0x9)
    Jump("loc_256F")

    label("loc_256D")

    OP_AF(0x8)

    label("loc_256F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3577")

    label("loc_257E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2592")
    Jump("loc_3577")

    label("loc_2592")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3577")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_25F7")

    #C0100
    ChrTalk(
        0x8,
        (
            "期待您再度\x01",
            "光临本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "下次请多带些朋友\x01",
            "一起来用餐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3577")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26AE")

    #C0102
    ChrTalk(
        0x8,
        (
            "凡事只要交给\x01",
            "赛尔缇欧和侬诺，\x01",
            "温赛特餐厅就不用担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "呼，但更重要的是，\x01",
            "克洛斯贝尔要先\x01",
            "渡过这个困境……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "总之，只要大家能齐心协力，\x01",
            "就没有办不到的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3577")

    label("loc_26AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2743")

    #C0105
    ChrTalk(
        0x8,
        (
            "嗯，和警察\x01",
            "谈过以后，\x01",
            "真是安心很多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "总之，\x01",
            "身为这里的店长，\x01",
            "我一定会担负起责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "各位在外面走动的时候\x01",
            "也请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3577")

    label("loc_2743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2822")

    #C0108
    ChrTalk(
        0x8,
        (
            "政府发布了冻结各国在ＩＢＣ资产的宣言……\x01",
            "而且铁道列车\x01",
            "即将正式停止通行……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "唔，这样下去，无论再\x01",
            "发生什么事情都不足为奇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "我很想尽可能地维持正常营业……\x01",
            "但老实说，现在真是很不安。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B1")

    label("loc_2822")


    #C0111
    ChrTalk(
        0x8,
        (
            "政府发布了冻结各国在ＩＢＣ资产的宣言……\x01",
            "而且铁道列车\x01",
            "即将正式停止通行……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "我很想尽可能地维持正常营业……\x01",
            "但老实说，现在真是很不安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B1")

    Jump("loc_3577")

    label("loc_28B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29CE")

    #C0113
    ChrTalk(
        0x8,
        (
            "毕竟发生了那样的事件，\x01",
            "我本想让赛尔缇欧和\x01",
            "侬诺的料理对决计划延期……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "但在他们两人的强烈要求之下，\x01",
            "还是在昨天关店之后展开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "结果两人都做出了\x01",
            "相当完美的料理，\x01",
            "让我感动得要流泪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "哎呀呀，亲眼见证\x01",
            "后辈人的成长，\x01",
            "感觉竟是如此美妙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A41")

    label("loc_29CE")


    #C0117
    ChrTalk(
        0x8,
        (
            "嗯，如果让侬诺的\x01",
            "烹饪技术就这样埋没下去，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "三厨师体制的构想……\x01",
            "确实有必要仔细考虑一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A41")

    Jump("loc_3577")

    label("loc_2A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2AC4")

    #C0119
    ChrTalk(
        0x8,
        (
            "在光顾本店的客人之中，\x01",
            "自然也有玛因兹的居民。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "不少客人都和我很熟……\x01",
            "得知他们陷入危难，真是十分痛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3577")

    label("loc_2AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B81")

    #C0121
    ChrTalk(
        0x8,
        (
            "呵呵，看样子，\x01",
            "赛尔缇欧思考得很用心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "我以前也是这样。\x01",
            "不厌其烦地思索再思索，\x01",
            "最终才可以得到答案……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "希望这些经验能成为赛尔缇欧\x01",
            "的一笔精神财富。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BF6")

    label("loc_2B81")


    #C0124
    ChrTalk(
        0x8,
        (
            "我以前也是这样。\x01",
            "不厌其烦地思索再思索，\x01",
            "最终才可以得到答案……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "希望这些经验能成为赛尔缇欧\x01",
            "的一笔精神财富。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF6")

    Jump("loc_3577")

    label("loc_2BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D13")

    #C0126
    ChrTalk(
        0x8,
        (
            "据说西克洛斯贝尔街道那边\x01",
            "发生了列车事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "难道是遭遇到落石了吗？\x01",
            "好像有很多人受了伤，\x01",
            "真让人担心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D0E")

    #C0128
    ChrTalk(
        0x101,
        (
            "#00008F（在这里似乎可以进行\x01",
            "  美食向导的取材……）\x02\x03",

            "#00003F（但现在不是做这种事的时候，\x01",
            "  以后别忘了再来一趟。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0E")

    Jump("loc_3577")

    label("loc_2D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC4")

    #C0129
    ChrTalk(
        0x8,
        (
            "赛尔缇欧最近的工作态度有了很大的改善，\x01",
            "简直就像变了个人一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "在面对漂亮的女性客人时，\x01",
            "也不再有过剩反应了……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        "嗯，这真是很让人欣慰啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E30")

    label("loc_2DC4")


    #C0132
    ChrTalk(
        0x8,
        (
            "赛尔缇欧以前只对女性有兴趣。\x01",
            "如今，这份热情终于开始\x01",
            "渐渐转向料理技术了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        "嗯，这真是很让人欣慰啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2E30")

    Jump("loc_3577")

    label("loc_2E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E88")

    #C0134
    ChrTalk(
        0x8,
        (
            "呵呵，看样子，\x01",
            "赛尔缇欧总算要认真了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        "真是期待比赛的结果。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3577")

    label("loc_2E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2F")

    #C0136
    ChrTalk(
        0x8,
        (
            "在听说布拉温让侬诺负责\x01",
            "烹饪之后，赛尔缇欧\x01",
            "终于也开始感到焦虑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "嗯……看样子，说不定\x01",
            "赛尔缇欧所缺少的，\x01",
            "其实是一个好的竞争对手。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FBF")

    label("loc_2F2F")


    #C0138
    ChrTalk(
        0x8,
        (
            "现在想想，我当年\x01",
            "也一直和布拉温比拼竞争，\x01",
            "因此才磨练出了一手好技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "嗯……看样子，说不定\x01",
            "赛尔缇欧所缺少的，\x01",
            "其实是一个好的竞争对手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FBF")

    Jump("loc_3577")

    label("loc_2FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_30B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305D")

    #C0140
    ChrTalk(
        0x8,
        (
            "我听布拉温说了，\x01",
            "侬诺似乎很有\x01",
            "烹饪的天赋啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "当初只是想让她\x01",
            "帮忙做点简单的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "嗯，这可真是\x01",
            "预料之外的收获。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30AB")

    label("loc_305D")


    #C0143
    ChrTalk(
        0x8,
        (
            "当初只是想让侬诺\x01",
            "帮忙做点简单的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "嗯，这可真是\x01",
            "预料之外的收获。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AB")

    Jump("loc_3577")

    label("loc_30B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_327C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D5")

    #C0145
    ChrTalk(
        0x8,
        (
            "当初决定派赛尔缇欧为客人服务时，\x01",
            "我拿出了相当的勇气。但现在看来，\x01",
            "他干得真是意外出色呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "在同最喜欢的女性交谈时，\x01",
            "他也可以保持最基本的礼节，\x01",
            "这样就不用担心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "唔，接下来要做的，\x01",
            "就是让他察觉到\x01",
            "自己身为一个厨师的那份骄傲感……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        "这实在是个难题呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3277")

    label("loc_31D5")


    #C0149
    ChrTalk(
        0x8,
        (
            "赛尔缇欧制作料理的时候，\x01",
            "很希望给别人带来惊喜，\x01",
            "因此总是突发奇想。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x8,
        (
            "大概正是由于这个缘故吧，\x01",
            "他非常讨厌正统派的烹饪方法……\x01",
            "怎么才能让他改变那种想法呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3277")

    Jump("loc_3577")

    label("loc_327C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3386")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F7")

    #C0151
    ChrTalk(
        0x8,
        (
            "本以为撤掉赛尔缇欧的厨师工作\x01",
            "能让他受到一些打击的……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "唔，看样子，\x01",
            "我的计划落空了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3381")

    label("loc_32F7")


    #C0153
    ChrTalk(
        0x8,
        (
            "把赛尔缇欧从厨师的位置上撤下来，\x01",
            "布拉温的负担\x01",
            "可就变得相当重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "这种无意义的尝试\x01",
            "终究不能一直持续下去……\x01",
            "唔，到底该怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3381")

    Jump("loc_3577")

    label("loc_3386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3405")

    #C0155
    ChrTalk(
        0x8,
        (
            "唔～看样子，如果放着赛尔缇欧不管，\x01",
            "他是无法得到成长的。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "嗯……不然就采取些\x01",
            "非常的手段吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_344F")

    label("loc_3405")


    #C0157
    ChrTalk(
        0x8,
        (
            "嗯……不然就采取些\x01",
            "非常的手段吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "但愿能让赛尔缇欧\x01",
            "有所改变……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_344F")

    Jump("loc_3577")

    label("loc_3454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3514")

    #C0159
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临『温赛特餐厅』。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "本店每年都会根据时节的变化，\x01",
            "对菜单中的部分菜式进行数次调整。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "请一定要尝尝由本店引以为傲的厨师\x01",
            "布拉温所研制的新菜式。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3577")

    label("loc_3514")


    #C0162
    ChrTalk(
        0x8,
        (
            "本店每年都会根据时节的变化，\x01",
            "对菜单中的部分菜式进行数次调整。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        "如果有兴趣，请一定尝尝看。\x02",
    )

    CloseMessageWindow()

    label("loc_3577")

    Jump("loc_24FE")

    label("loc_357C")

    TalkEnd(0x8)
    Return()

    # Function_8_22DC end

    def Function_9_3580(): pass

    label("Function_9_3580")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3607")

    #C0164
    ChrTalk(
        0xFE,
        (
            "不知是怎么回事，赛尔缇欧那小子\x01",
            "突然就干劲十足了。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不过这是个好的倾向。\x01",
            "怎么说呢，我也可以暂时放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_36B7")

    #C0166
    ChrTalk(
        0xFE,
        (
            "看着客人开心地\x01",
            "吃着自己做的料理……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "对厨师来说，\x01",
            "最大的幸福莫过于此了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "即使是在这种状况下，\x01",
            "只要有前来用餐的客人，\x01",
            "我的身体里就会有力量不断涌现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_36B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_37CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3739")

    #C0169
    ChrTalk(
        0xFE,
        "从今天早上开始，铁路货运完全停止了。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "要用什么来代替进口食材呢……\x01",
            "这是我们现在最重要的问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37C6")

    label("loc_3739")


    #C0171
    ChrTalk(
        0xFE,
        (
            "总觉得形势很紧张呢……\x01",
            "在这种情况下，我们这些厨师\x01",
            "能做的事情就只有一件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "要用什么来代替进口食材呢……\x01",
            "这是我们现在最重要的问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C6")

    Jump("loc_42B9")

    label("loc_37CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_394E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C5")

    #C0173
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧那家伙好像总算是\x01",
            "成熟起来了，我终于可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "那小子制作的薏面用调味酱\x01",
            "以番茄酱为主料，\x01",
            "还加入了鱼贝等海鲜原料……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "除此之外，还巧妙地\x01",
            "添加了多种调味料。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "不但吃起来美味无比，\x01",
            "而且十分有新鲜感。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3949")

    label("loc_38C5")


    #C0177
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧以前\x01",
            "总是毫无缘由地厌恶\x01",
            "传统的食材搭配方式。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "正因如此，反而使自己的\x01",
            "视野变得越发狭窄……\x01",
            "看来他终于稍许成长了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3949")

    Jump("loc_42B9")

    label("loc_394E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39CC")

    #C0179
    ChrTalk(
        0xFE,
        (
            "唔，是我的心理作用吗，\x01",
            "今天的客人好像比平时要少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "呼……毕竟昨天刚刚发生过那种事情，\x01",
            "这也可以理解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_39CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A30")

    #C0181
    ChrTalk(
        0xFE,
        "话说回来，料理对决吗……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "侬诺和赛尔缇欧\x01",
            "好像都在全力准备，\x01",
            "这真是件好事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB4")

    #C0183
    ChrTalk(
        0xFE,
        "从刚才开始，急救车的警笛声就吵得要死。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "拜其所赐，连炸东西的声音都听不到了，\x01",
            "结果炸得有些焦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B08")

    label("loc_3AB4")


    #C0185
    ChrTalk(
        0xFE,
        (
            "哦，炸焦的食品是不会端给客人的，\x01",
            "放心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "待会给赛尔缇欧那小子\x01",
            "吃就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B08")

    Jump("loc_42B9")

    label("loc_3B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B8D")

    #C0187
    ChrTalk(
        0xFE,
        (
            "唔，侬诺的手艺\x01",
            "比一开始强多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "这样的话，可以考虑雇一个新的服务员，\x01",
            "让侬诺到厨房工作，变为三厨师体制。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_3B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD6")

    #C0189
    ChrTalk(
        0xFE,
        "嘿嘿，霍伊斯托夫真是很有一套啊。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "竟能利用侬诺的成果，\x01",
            "使赛尔缇欧感到焦急，\x01",
            "从而在厨师的道路上得到成长。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "一周之后，那两人\x01",
            "要以厨师的职位为赌注，\x01",
            "展开料理对决。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "哈，不过那也只是名义上的说法罢了。\x01",
            "只要他们有干劲，我是希望\x01",
            "让他们两个都当厨师的。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "对了，这些话可要对赛尔缇欧保密哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D32")

    label("loc_3CD6")


    #C0194
    ChrTalk(
        0xFE,
        "嘿嘿，霍伊斯托夫真是很有一套啊。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧那小子\x01",
            "好像很有干劲，\x01",
            "这主意可真是成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D32")

    Jump("loc_42B9")

    label("loc_3D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DBC")

    #C0196
    ChrTalk(
        0xFE,
        (
            "哈哈，侬诺自然是\x01",
            "感到很疑惑，\x01",
            "不过仍然很有干劲。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "真不错，年轻人就是单纯啊。\x01",
            "让我想起了自己年轻时的修行时代。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_3DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3E00")

    #C0198
    ChrTalk(
        0xFE,
        (
            "好，索性就下定决心，\x01",
            "明天把料理工作\x01",
            "交给侬诺吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EC7")

    #C0199
    ChrTalk(
        0xFE,
        (
            "哎呀呀，说起今天早上\x01",
            "交给侬诺制作的那道汤……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "……真让人吃惊，做得比我想象中还要好。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "听说她在家里也会做做饭……\x01",
            "这样的话，似乎可以再多交给她一些料理工作啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F43")

    label("loc_3EC7")


    #C0202
    ChrTalk(
        0xFE,
        (
            "唔，这道汤……\x01",
            "充分发挥出了食材的味道啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "听说她在家里也会做做饭……\x01",
            "这样的话，似乎可以再多交给她一些料理工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F43")

    Jump("loc_42B9")

    label("loc_3F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_406E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400F")

    #C0204
    ChrTalk(
        0xFE,
        (
            "嗯，说起来，霍伊斯托夫\x01",
            "那家伙还真是做了个非常大胆的决定啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "没想到他竟然会\x01",
            "让赛尔缇欧离开厨房……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "不过，对那小子\x01",
            "如果不用些非常手段，\x01",
            "恐怕也无法起到效果吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4069")

    label("loc_400F")


    #C0207
    ChrTalk(
        0xFE,
        (
            "话说回来，赛尔缇欧那小子\x01",
            "真是完全扶不上墙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "难道他还不了解\x01",
            "自己如今的立场吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4069")

    Jump("loc_42B9")

    label("loc_406E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_419D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4130")

    #C0209
    ChrTalk(
        0xFE,
        (
            "不管是锻炼厨艺，还是做别的事情，\x01",
            "扎实的基本功都是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "比如说绘画，那些著名的抽象派画家\x01",
            "也都能画好写实派的作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "真希望赛尔缇欧\x01",
            "尽快想通这一点……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4198")

    label("loc_4130")


    #C0212
    ChrTalk(
        0xFE,
        (
            "不管是锻炼厨艺，还是做别的事情，\x01",
            "扎实的基本功都是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "真希望赛尔缇欧\x01",
            "尽快想通这一点……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4198")

    Jump("loc_42B9")

    label("loc_419D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_42B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4253")

    #C0214
    ChrTalk(
        0xFE,
        (
            "以前交给赛尔缇欧来创作\x01",
            "的新菜式，\x01",
            "最后还是以失败告终了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "那小子的天赋绝对不差……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "但如果再照这种样子下去，\x01",
            "实在是很难成长到独当一面的水平。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42B9")

    label("loc_4253")


    #C0217
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧那小子的\x01",
            "天赋绝对不差……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "但如果再照这种样子下去，\x01",
            "实在是很难成长到独当一面的水平。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42B9")

    TalkEnd(0xFE)
    Return()

    # Function_9_3580 end

    def Function_10_42BD(): pass

    label("Function_10_42BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A2")

    #C0219
    ChrTalk(
        0xFE,
        (
            "不管市里今后会变得怎样，\x01",
            "身为厨师，能做的事情只有一件……\x01",
            "那就是为大家提供可口的饭菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "虽然今后的食材供应大概会继续受到限制，\x01",
            "但只要想想办法，一定可以克服困难。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "好～今天也要全力加油！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4403")

    label("loc_43A2")


    #C0222
    ChrTalk(
        0xFE,
        (
            "身为厨师，能做的事情就只有一件……\x01",
            "那就是为大家提供可口的饭菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "好～今天也要全力加油！\x02",
    )

    CloseMessageWindow()

    label("loc_4403")

    Jump("loc_52AA")

    label("loc_4408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_459C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450C")

    #C0224
    ChrTalk(
        0xFE,
        (
            "非要到这种时候才能醒悟，\x01",
            "真是惭愧无比……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "但我如今总算是明白了\x01",
            "布拉温先生所说的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "正如他所说，身为一名厨师，\x01",
            "让客人满意才是最大的目标……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "一直以来，我只是在创作\x01",
            "让自己满意的料理而已，\x01",
            "现在想想，实在是太羞愧了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4597")

    label("loc_450C")


    #C0228
    ChrTalk(
        0xFE,
        (
            "正如他所说，身为一名厨师，\x01",
            "让客人满意才是最大的目标……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "一直以来，我只是在创作\x01",
            "让自己满意的料理而已，\x01",
            "现在想想，实在是太羞愧了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4597")

    Jump("loc_52AA")

    label("loc_459C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_460A")

    #C0230
    ChrTalk(
        0xFE,
        (
            "迪塔总统的演说\x01",
            "真是魄力十足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "该怎么说好呢，听了他的话，\x01",
            "似乎就获得了勇气和自豪感呢\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52AA")

    label("loc_460A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_472B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AD")

    #C0232
    ChrTalk(
        0xFE,
        "真是的，店长也够坏的。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "竟然从一开始就没打算\x01",
            "让我们决出个高低……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "嘿，既然如此，费尽心思\x01",
            "设计这种事情，究竟是为了什么啊？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4726")

    label("loc_46AD")


    #C0235
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "最近的形势真是太乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "不过，从这个角度来想，\x01",
            "我还能像现在这样正常工作，\x01",
            "就已经是很幸福的生活了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4726")

    Jump("loc_52AA")

    label("loc_472B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_47A9")

    #C0237
    ChrTalk(
        0xFE,
        (
            "竟然发生了占领事件……\x01",
            "虽然很可怕，但仔细想想，可真是荒谬啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "倚仗暴力来支配他人，\x01",
            "到底有什么乐趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52AA")

    label("loc_47A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4859")

    #C0239
    ChrTalk(
        0xFE,
        (
            "可恶，连基本方针都还没想好，\x01",
            "时间就一点一点流逝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "至少得尽快把用于比试的\x01",
            "薏面酱种类决定下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "番茄？奶油？\x01",
            "还是其它的未知酱料呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48AD")

    label("loc_4859")


    #C0242
    ChrTalk(
        0xFE,
        (
            "不对不对！\x01",
            "未知酱料是个什么东西啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "呼……我总算察觉到\x01",
            "自己的不足之处了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AD")

    Jump("loc_52AA")

    label("loc_48B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_48E6")

    #C0244
    ChrTalk(
        0xFE,
        "嗯？怎么回事？外面怎么这么吵闹。\x02",
    )

    CloseMessageWindow()
    Jump("loc_52AA")

    label("loc_48E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A7")

    #C0245
    ChrTalk(
        0xFE,
        (
            "虽然味道是最关键的，\x01",
            "但料理的外观也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "话说回来，在这次的对决中，\x01",
            "创新度似乎并不是很重要……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "总之，还是以传统料理\x01",
            "为基础，再加上些\x01",
            "小改动吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A03")

    label("loc_49A7")


    #C0248
    ChrTalk(
        0xFE,
        (
            "呼，但我真是很讨厌\x01",
            "传统这个词啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "因为，既然是传统，\x01",
            "美味不就成了理所当然的了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A03")

    Jump("loc_52AA")

    label("loc_4A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A76")

    #C0250
    ChrTalk(
        0xFE,
        (
            "……真没想到要和侬诺\x01",
            "进行料理对决啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "美味的面条料理吗……\x01",
            "我正在为制作方针而烦恼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52AA")

    label("loc_4A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B18")

    #C0252
    ChrTalk(
        0xFE,
        (
            "侬、侬诺制作料理！？\x01",
            "这也太早了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "话说回来，难道我从此\x01",
            "就会被冷落排挤了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "呃，不对不对不对，\x01",
            "才不会有那种事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B7D")

    label("loc_4B18")


    #C0255
    ChrTalk(
        0xFE,
        (
            "就算侬诺再怎么会做菜，\x01",
            "让她给客人做料理，也未免太早了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        "话说回来，我的立场究竟摆在哪里？\x02",
    )

    CloseMessageWindow()

    label("loc_4B7D")

    Jump("loc_52AA")

    label("loc_4B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4C0D")

    #C0257
    ChrTalk(
        0xFE,
        (
            "虽然我一点都不在乎……\x01",
            "但侬诺那家伙不知从何时开始，\x01",
            "兼任起料理的准备工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "难道说，她会就此转职为\x01",
            "正式厨师吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52AA")

    label("loc_4C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBE")

    #C0259
    ChrTalk(
        0xFE,
        (
            "欢迎光临，如果想在本店用餐，\x01",
            "请随意挑选空位就坐吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "本店二层是需要提前预约的特别席位，\x01",
            "但现在刚好空着。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "如果您需要，我也可以带您去哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D2D")

    label("loc_4CBE")


    #C0262
    ChrTalk(
        0xFE,
        (
            "呀～接待客人\x01",
            "原来这么有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "客人们……尤其是美貌\x01",
            "女性客人的笑脸，\x01",
            "对我来说就是无可替代的能量源泉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2D")

    Jump("loc_52AA")

    label("loc_4D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EBF")

    #C0264
    ChrTalk(
        0xFE,
        (
            "店长让我暂时\x01",
            "从事服务员的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "虽然不知道他有什么打算，\x01",
            "但偶尔做点这样的工作也不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "不但能随意欣赏女性客人，\x01",
            "还可以堂堂正正地与她们搭话了。\x02",
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

    #C0267
    ChrTalk(
        0x101,
        (
            "#00006F（与客人搭话……\x01",
            "  实在是有点不妥啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        (
            "#00103F（嗯，而且盯着客人看\x01",
            "  也会让客人很不自在吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F39")

    label("loc_4EBF")


    #C0269
    ChrTalk(
        0xFE,
        (
            "虽然不知道店长有什么打算，\x01",
            "但偶尔做点这样的工作也不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "不但能随意欣赏女性客人，\x01",
            "还可以堂堂正正地与她们搭话了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F39")

    Jump("loc_52AA")

    label("loc_4F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FCA")

    #C0271
    ChrTalk(
        0xFE,
        (
            "制作料理是一门艺术，\x01",
            "独创性是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "下次创作新菜式的时候，\x01",
            "我一定会做出让世人\x01",
            "大吃一惊的终极料理。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_502C")

    label("loc_4FCA")


    #C0273
    ChrTalk(
        0xFE,
        (
            "嗯，这道菜是要端给……\x01",
            "入口那边座位上的两个女孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "嘿嘿，等着我哦～\x01",
            "我这就把菜端过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502C")

    Jump("loc_52AA")

    label("loc_5031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_52AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5114")

    #C0275
    ChrTalk(
        0xFE,
        (
            "唔～我的新作料理究竟\x01",
            "哪里出了问题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "味道和外观都很不错，\x01",
            "而且这又粘又滑的口感\x01",
            "简直就是划时代的创举啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#00012F（『又粘又滑』……？）\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#00106F（虽然不太明白，\x01",
            "  但完全不想尝……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52AA")

    label("loc_5114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5265")

    #C0279
    ChrTalk(
        0xFE,
        (
            "『魔兽眼球之泥沼地狱锅』……\x01",
            "本以为这道料理开拓了烹饪的新境界～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5189")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5189")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51AF")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_51AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51D5")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_51D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51FB")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_51FB")

    Sleep(1000)

    #C0280
    ChrTalk(
        0x109,
        "#10105F（好、好厉害的名字啊。）\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x105,
        (
            "#10304F（呵呵，听起来好像是\x01",
            "  非常低级趣味的料理。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_52AA")

    label("loc_5265")


    #C0282
    ChrTalk(
        0xFE,
        (
            "『魔兽眼球之泥沼地狱锅』……\x01",
            "本以为这道料理开拓了烹饪的新境界～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52AA")

    TalkEnd(0xFE)
    Return()

    # Function_10_42BD end

    def Function_11_52AE(): pass

    label("Function_11_52AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5337")

    #C0283
    ChrTalk(
        0xFE,
        (
            "呵呵，赛尔缇欧先生\x01",
            "好像非常有干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "虽然目前的状况很让人不安……\x01",
            "但受他的影响，我也觉得稍微恢复了些精神呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_5337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_53BD")

    #C0285
    ChrTalk(
        0xFE,
        (
            "市里现在的异常事态……\x01",
            "全都是政府自己\x01",
            "引发的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "如果早点把详情告诉大家，\x01",
            "也许就不会造成\x01",
            "这么严重的混乱了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_53BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_543D")

    #C0287
    ChrTalk(
        0xFE,
        (
            "听了总统的演说之后，\x01",
            "确实觉得他说得很精彩动人……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "但正如店长所说，不安的要素\x01",
            "实在太多了，真是令人困惑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_543D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546F")
    Call(0, 43)
    Return()

    label("loc_546F")


    #C0289
    ChrTalk(
        0xFE,
        (
            "虽然只经过一个月的时间，\x01",
            "但在厨房工作真是开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "我准备一鼓作气，\x01",
            "从此以真正的厨师为目标。\x01",
            "店长也支持我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_54E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_552D")

    #C0291
    ChrTalk(
        0xFE,
        "真担心玛因兹的人啊……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "他们肚子会不会很饿……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_552D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CB")

    #C0293
    ChrTalk(
        0xFE,
        (
            "说起在料理对决中使用的食谱……\x01",
            "赛尔缇欧先生似乎\x01",
            "考虑了很多种方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "但我的想法很单纯，\x01",
            "选择平时做得最熟练的料理就可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_562D")

    label("loc_55CB")


    #C0295
    ChrTalk(
        0xFE,
        (
            "我擅长做肉酱薏面和奶酪沙司薏面，\x01",
            "在家里经常给家人做。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "所以我在料理对决中\x01",
            "也准备做这个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562D")

    Jump("loc_5DC2")

    label("loc_5632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_567D")

    #C0297
    ChrTalk(
        0xFE,
        (
            "警笛声一直\x01",
            "接连不断。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        "待在厨房里，都听得清清楚楚。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_567D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56FA")

    #C0299
    ChrTalk(
        0xFE,
        "啦啦啦～¤\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "香草、胡椒，\x01",
            "然后稍微再放点盐……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "嗯，这样一来，\x01",
            "肉的调味工作就做好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5743")

    label("loc_56FA")


    #C0302
    ChrTalk(
        0xFE,
        "啦啦啦¤\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "然后再把它放上３０分钟左右……\x01",
            "趁此时间，我先去切菜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5743")

    Jump("loc_5DC2")

    label("loc_5748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_58E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5865")

    #C0304
    ChrTalk(
        0xFE,
        (
            "按照预定，我已经差不多\x01",
            "该返回大堂去工作了……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "但店长拜托我\x01",
            "再在厨房工作一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "顺便再与赛尔缇欧先生\x01",
            "进行一次料理对决。\x01",
            "据说这是为了赛尔缇欧先生的将来……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "呵呵，欺骗了赛尔缇欧先生，\x01",
            "总有点对不起他，\x01",
            "但听起来好像很有趣，所以我就接受了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_58E0")

    label("loc_5865")


    #C0308
    ChrTalk(
        0xFE,
        (
            "话说回来，烹饪原本只是\x01",
            "家务活的延伸，\x01",
            "但在厨房里工作倒是挺有趣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "呵呵，既然如此，\x01",
            "不如就以真正的厨师为目标吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E0")

    Jump("loc_5DC2")

    label("loc_58E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5984")

    #C0310
    ChrTalk(
        0xFE,
        (
            "布拉温先生今天早上突然来拜托我，\x01",
            "让我帮忙负责烹饪工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "我真的可以吗？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "为、为了回应他的期待，\x01",
            "我自然会全力以赴的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_59CF")

    label("loc_5984")


    #C0313
    ChrTalk(
        0xFE,
        (
            "嗯，首先是\x01",
            "食材的调味……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "呜呜，让我制作料理，终究是有些紧张啊。\x02",
    )

    CloseMessageWindow()

    label("loc_59CF")

    Jump("loc_5DC2")

    label("loc_59D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5A38")

    #C0315
    ChrTalk(
        0xFE,
        (
            "准备工作结束之后，\x01",
            "就该去洗盘子了，然后还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "呼……晚餐时间\x01",
            "果然很忙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_5A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AAF")

    #C0317
    ChrTalk(
        0xFE,
        (
            "嗯，这种蔬菜\x01",
            "比较难熟，\x01",
            "最好在背面多切几刀。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "（嚓嚓嚓）……\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        "嗯，这样就行了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5AE3")

    label("loc_5AAF")


    #C0320
    ChrTalk(
        0xFE,
        "（咚咚咚）……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        "嗯，切成这么碎就可以了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5AE3")

    Jump("loc_5DC2")

    label("loc_5AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B67")

    #C0322
    ChrTalk(
        0xFE,
        (
            "我现在代替赛尔缇欧先生，\x01",
            "暂时在厨房帮些忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "话虽如此，但主要任务只是\x01",
            "洗盘子和一些简单的\x01",
            "准备工作而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC2")

    label("loc_5B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C07")

    #C0324
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧先生还是老样子，\x01",
            "总是离开厨房，\x01",
            "去窥视用餐的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "他今天大概还会自行\x01",
            "把料理端给客人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "呼，真是完全学不乖。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C61")

    label("loc_5C07")


    #C0327
    ChrTalk(
        0xFE,
        (
            "赛尔缇欧先生还是老样子，\x01",
            "总是离开厨房，\x01",
            "去窥视用餐的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        "呼，真是完全学不乖。\x02",
    )

    CloseMessageWindow()

    label("loc_5C61")

    Jump("loc_5DC2")

    label("loc_5C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D34")

    #C0329
    ChrTalk(
        0xFE,
        (
            "坐在里面席位的弗罗缇小姐\x01",
            "是本店的常客。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "她总是在刚开店时就进来，\x01",
            "经常就那么坐上\x01",
            "一整天……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "但在用餐高峰期，她也会暂时离席，\x01",
            "有时还会再多点些东西，\x01",
            "真是很体贴我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5DC2")

    label("loc_5D34")


    #C0332
    ChrTalk(
        0xFE,
        (
            "弗罗缇小姐总是在刚开店时就进来，\x01",
            "经常就那么坐上\x01",
            "一整天……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "但在用餐高峰期，她也会暂时离席，\x01",
            "有时还会再多点些东西，\x01",
            "真是很体贴我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC2")

    TalkEnd(0xFE)
    Return()

    # Function_11_52AE end

    def Function_12_5DC6(): pass

    label("Function_12_5DC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5EDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E65")

    #C0334
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "蓝白色的大树吗……\x01",
            "这究竟是现实还是梦境？\x01",
            "我最近都有些分不清了。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "……干脆再多喝些咖啡，\x01",
            "清醒一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5ED6")

    label("loc_5E65")


    #C0337
    ChrTalk(
        0xFE,
        (
            "蓝白色的大树吗……\x01",
            "这究竟是现实还是梦境呢？\x01",
            "我最近都有些分不清了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "……干脆再多喝些咖啡，\x01",
            "清醒一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED6")

    Jump("loc_6C56")

    label("loc_5EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FDE")

    #C0339
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "……我只是去了个洗手间，\x01",
            "回来之后就一片雾气，而且不能出去了。\x01",
            "这到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "更重要的是，\x01",
            "那样的智能兵器\x01",
            "为何会在街上徘徊？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "就算是为了抵抗两大国，\x01",
            "保卫城市的安全，\x01",
            "我也希望政府能给个正式的说明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6073")

    label("loc_5FDE")


    #C0343
    ChrTalk(
        0xFE,
        (
            "有关那个名为『神机』的兵器，\x01",
            "还有笼罩城市的结界，\x01",
            "我希望政府能给个正式的说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "再这么下去，与其说是保卫城市，\x01",
            "倒不如说是给我们带来危险吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6073")

    Jump("loc_6C56")

    label("loc_6078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_61C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6144")

    #C0345
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立国，迪塔总统，\x01",
            "还有亚里欧斯国防长官……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "名字和官衔倒是很威风，\x01",
            "但真的可以保障我们的安全吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "……从现状来看，\x01",
            "真是不能让人放心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_61C3")

    label("loc_6144")


    #C0349
    ChrTalk(
        0xFE,
        (
            "独立国、总统、国防长官……\x01",
            "名字和官衔倒是很威风，\x01",
            "但真的可以保障我们的安全吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "……从现状来看，\x01",
            "真是不能让人放心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61C3")

    Jump("loc_6C56")

    label("loc_61C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_633C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6294")

    #C0351
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "经过前些天的袭击事件，\x01",
            "赞成独立的气氛十分高涨。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "呼，这种心情倒也可以理解，\x01",
            "但不能稍微理性些吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "好像有人曾经这样说过，\x01",
            "感情用事只会自取灭亡……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6337")

    label("loc_6294")


    #C0355
    ChrTalk(
        0xFE,
        (
            "经过前些天的袭击事件，\x01",
            "赞成独立的气氛十分高涨。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "呼，这种心情倒也可以理解，\x01",
            "但不能稍微理性些吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "呃，好像有人曾经这样说过。\x01",
            "感情用事只会自取灭亡……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6337")

    Jump("loc_6C56")

    label("loc_633C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_63FF")

    #C0358
    ChrTalk(
        0xFE,
        (
            "现在流传着这样的传闻……\x01",
            "据说神秘武装集团出现在玛因兹\x01",
            "一事是帝国策划的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "『我军可以提供援助，但作为回报，要同意我国驻军』……\x01",
            "帝国很可能会提出这种让人笑不出来的主张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C56")

    label("loc_63FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_64DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64AE")

    #C0360
    ChrTalk(
        0xFE,
        (
            "从今天早上开始，\x01",
            "要在市民会馆召开以独立\x01",
            "为主题的市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "就算不参加什么座谈会，\x01",
            "我也很清楚独立的各种利弊。\x01",
            "不过，要不要过去听听看呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_64D9")

    label("loc_64AE")


    #C0362
    ChrTalk(
        0xFE,
        (
            "市民座谈会吗……\x01",
            "要不要过去听听看呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64D9")

    Jump("loc_6C56")

    label("loc_64DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6528")

    #C0363
    ChrTalk(
        0xFE,
        "不知为何，外面很吵闹呢。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        "想安静地喝杯咖啡都不行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C56")

    label("loc_6528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6619")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C6")

    #C0365
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的新版舞剧\x01",
            "好像要在后天公演啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "我虽然也想买张票……\x01",
            "但转瞬之间，两个月之内的票\x01",
            "就全部卖光了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6614")

    label("loc_65C6")


    #C0368
    ChrTalk(
        0xFE,
        (
            "哼……\x01",
            "不看彩虹剧团的表演\x01",
            "又不会死人。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "呜呜，但我真是想看得要死啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6614")

    Jump("loc_6C56")

    label("loc_6619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669D")

    #C0370
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "独立啊……\x01",
            "单说这件事情本身，倒是没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "但我很担心安全保障方面的问题。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_671E")

    label("loc_669D")


    #C0373
    ChrTalk(
        0xFE,
        (
            "就我个人来看，\x01",
            "让帝国和共和国来保障我们的安全\x01",
            "也不是什么坏事……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "呼，但历史是历史，\x01",
            "现实是现实啊，有些事情没那么简单。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_671E")

    Jump("loc_6C56")

    label("loc_6723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A3")

    #C0375
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        "话说回来，街上真是戒备森严啊。\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "到处都有警察在巡逻，\x01",
            "想轻松散个步都不行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_67E8")

    label("loc_67A3")


    #C0378
    ChrTalk(
        0xFE,
        "相比之下，店里真是安静多了。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "好，今天也读些\x01",
            "有意义的书吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67E8")

    Jump("loc_6C56")

    label("loc_67ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6883")

    #C0380
    ChrTalk(
        0xFE,
        (
            "呼，今天看书看得太投入，不知不觉\x01",
            "就待到太阳下山了，已经好久没有这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "真是有点对不起店里的人，\x01",
            "不然就在这里把晚饭也吃了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C56")

    label("loc_6883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6A19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6962")

    #C0382
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "反正也不可能站在近处\x01",
            "观赏到揭幕式，何必还特意外出。\x01",
            "大家可真是不嫌累啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "等下一期的克洛斯贝尔时代周刊发售之后，\x01",
            "我就坐在这里，一手拿咖啡杯，\x01",
            "一手优雅地翻阅杂志就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6A14")

    label("loc_6962")


    #C0385
    ChrTalk(
        0xFE,
        (
            "反正也不可能站在近处\x01",
            "观赏到揭幕式，何必还特意外出。\x01",
            "大家可真是不嫌累啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "等下一期的克洛斯贝尔时代周刊发售之后，\x01",
            "我就坐在这里，一手拿咖啡杯，\x01",
            "一手优雅地翻阅杂志就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A14")

    Jump("loc_6C56")

    label("loc_6A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6A66")

    #C0387
    ChrTalk(
        0xFE,
        (
            "今天为什么是那个烦人的厨师\x01",
            "过来服务？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        "真是难以理解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C56")

    label("loc_6A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B0F")

    #C0389
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "在下雨天，店里的感觉与平时不同，\x01",
            "另有一番情趣呢，真是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "店内的喧嚣与雨声交织在一起，\x01",
            "简直就是最棒的背景音乐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B8B")

    label("loc_6B0F")


    #C0392
    ChrTalk(
        0xFE,
        (
            "在下雨天，店里的感觉与平时不同，\x01",
            "另有一番情趣呢，真是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "店内的喧嚣与雨声交织在一起，\x01",
            "简直就是最棒的背景音乐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8B")

    Jump("loc_6C56")

    label("loc_6B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6C56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C21")

    #C0394
    ChrTalk(
        0xFE,
        "（啜饮）……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "呼，这家店果然是\x01",
            "最适合读书的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "恰到好处的喧闹消除了我的杂念，\x01",
            "又有咖啡可以驱散睡意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6C56")

    label("loc_6C21")


    #C0397
    ChrTalk(
        0xFE,
        (
            "好，今天也要多待一阵，\x01",
            "把从图书馆借来的书读完～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C56")

    TalkEnd(0xFE)
    Return()

    # Function_12_5DC6 end

    def Function_13_6C5A(): pass

    label("Function_13_6C5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6CAB")

    #C0398
    ChrTalk(
        0xFE,
        (
            "讨厌～没听说\x01",
            "要下雨啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "难得来旅行，\x01",
            "为什么会这样啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CE5")

    label("loc_6CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6CE5")

    #C0400
    ChrTalk(
        0xFE,
        (
            "是啊～而且菜价也不是很高，\x01",
            "让人还想多来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CE5")

    TalkEnd(0xFE)
    Return()

    # Function_13_6C5A end

    def Function_14_6CE9(): pass

    label("Function_14_6CE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6D66")

    #C0401
    ChrTalk(
        0xFE,
        (
            "好了好了，我也知道下雨了，\x01",
            "就别对着我不停抱怨了。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "既然下了雨，只要想个\x01",
            "在室内娱乐的方法就好了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DB5")

    label("loc_6D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6DB5")

    #C0403
    ChrTalk(
        0xFE,
        (
            "老实说，真没想到\x01",
            "这家店的料理\x01",
            "如此正宗啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "呵呵，我很喜欢。\x02",
    )

    CloseMessageWindow()

    label("loc_6DB5")

    TalkEnd(0xFE)
    Return()

    # Function_14_6CE9 end

    def Function_15_6DB9(): pass

    label("Function_15_6DB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6DF2")

    #C0405
    ChrTalk(
        0xFE,
        "呵呵，亲爱的，这里的料理很好吃啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E44")

    label("loc_6DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6E44")

    #C0406
    ChrTalk(
        0xFE,
        (
            "亲爱的，你还特意为我预约座位，\x01",
            "真是谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "你总是这么照顾我。\x02",
    )

    CloseMessageWindow()

    label("loc_6E44")

    TalkEnd(0xFE)
    Return()

    # Function_15_6DB9 end

    def Function_16_6E48(): pass

    label("Function_16_6E48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6E90")

    #C0408
    ChrTalk(
        0xFE,
        "哇哈哈，是嘛。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "不过，还是比不上\x01",
            "你做的菜啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EE5")

    label("loc_6E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6EE5")

    #C0410
    ChrTalk(
        0xFE,
        "哇哈哈，哪里哪里。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "你总是为了这个家\x01",
            "操劳不断，\x01",
            "我应该感谢你才对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EE5")

    TalkEnd(0xFE)
    Return()

    # Function_16_6E48 end

    def Function_17_6EE9(): pass

    label("Function_17_6EE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6F55")

    #C0412
    ChrTalk(
        0xFE,
        (
            "今天干脆这样吧，打开菜单，\x01",
            "随便伸手一指，指到哪个就点哪个！\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        "好～先把眼睛闭上……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FEC")

    label("loc_6F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6F63")
    Jump("loc_6FEC")

    label("loc_6F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6FB6")

    #C0414
    ChrTalk(
        0xFE,
        "嗯，今天就吃鱼吧！\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "哎，不过今天吃\x01",
            "这个套餐好像很划算啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FEC")

    label("loc_6FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6FEC")

    #C0416
    ChrTalk(
        0xFE,
        (
            "嗯，该选哪个呢？\x01",
            "唔～哪个都想尝尝啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FEC")

    TalkEnd(0xFE)
    Return()

    # Function_17_6EE9 end

    def Function_18_6FF0(): pass

    label("Function_18_6FF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_702C")

    #C0417
    ChrTalk(
        0xFE,
        (
            "老公……\x01",
            "点哪个都可以，能不能快些呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_709A")

    label("loc_702C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_703A")
    Jump("loc_709A")

    label("loc_703A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7064")

    #C0418
    ChrTalk(
        0xFE,
        "呼，你可真是优柔寡断。\x02",
    )

    CloseMessageWindow()
    Jump("loc_709A")

    label("loc_7064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_709A")

    #C0419
    ChrTalk(
        0xFE,
        (
            "老公……能不能快些啊？\x01",
            "我都已经决定了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709A")

    TalkEnd(0xFE)
    Return()

    # Function_18_6FF0 end

    def Function_19_709E(): pass

    label("Function_19_709E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_70EA")

    #C0420
    ChrTalk(
        0xFE,
        (
            "哎，和第一天说的\x01",
            "完全不一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        "呸呸，真差劲啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7180")

    label("loc_70EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_70F8")
    Jump("loc_7180")

    label("loc_70F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7152")

    #C0422
    ChrTalk(
        0xFE,
        "（大吃大嚼）……啊，真幸福¤\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        "出来旅行，最让人开心的还要属美食啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7180")

    label("loc_7152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7180")

    #C0424
    ChrTalk(
        0xFE,
        (
            "呵呵，太好了¤\x01",
            "真不愧是亲爱的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7180")

    TalkEnd(0xFE)
    Return()

    # Function_19_709E end

    def Function_20_7184(): pass

    label("Function_20_7184")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_71F8")

    #C0425
    ChrTalk(
        0xFE,
        (
            "那、那个……\x01",
            "虽然很难启齿，\x01",
            "但旅费已经所剩不多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "所以请你尽量\x01",
            "点些价格适中的东西……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B2")

    label("loc_71F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7206")
    Jump("loc_72B2")

    label("loc_7206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_726C")

    #C0427
    ChrTalk(
        0xFE,
        (
            "唔～接连不断地点一些\x01",
            "高价菜……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "算、算啦，难得出来旅行，\x01",
            "就不计较这种小事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B2")

    label("loc_726C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_72B2")

    #C0429
    ChrTalk(
        0xFE,
        (
            "好，想吃什么都行，\x01",
            "随便点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "毕竟是难得的旅行嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_72B2")

    TalkEnd(0xFE)
    Return()

    # Function_20_7184 end

    def Function_21_72B6(): pass

    label("Function_21_72B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_72F4")

    #C0431
    ChrTalk(
        0xFE,
        (
            "嗯～没想到会在旅行途中\x01",
            "遇到这种事件啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7473")

    label("loc_72F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7332")

    #C0432
    ChrTalk(
        0xFE,
        (
            "唔～今天就放弃\x01",
            "郊外活动，\x01",
            "在市里购购物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7473")

    label("loc_7332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_738C")

    #C0433
    ChrTalk(
        0xFE,
        (
            "刚才一下有好几辆\x01",
            "急救车开过去了，\x01",
            "看上去不像是通常运送患者的场面呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7473")

    label("loc_738C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_73E2")

    #C0434
    ChrTalk(
        0xFE,
        (
            "好，今天也去各种地方\x01",
            "转转吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "先去导力商店补充些\x01",
            "感光回路吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7473")

    label("loc_73E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7473")

    #C0436
    ChrTalk(
        0xFE,
        (
            "考虑到克洛斯贝尔最近的治安情况，\x01",
            "一直都很犹豫，不知是否应该来旅行……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "最后决定过来，真是正确的选择啊。\x01",
            "我的女朋友也非常开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7473")

    TalkEnd(0xFE)
    Return()

    # Function_21_72B6 end

    def Function_22_7477(): pass

    label("Function_22_7477")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_74E2")

    #C0438
    ChrTalk(
        0xFE,
        (
            "我们今天本打算\x01",
            "去玛因兹观光……\x01",
            "但现在显然是去不成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        "真是很担心那里的居民啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_766C")

    label("loc_74E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7557")

    #C0440
    ChrTalk(
        0xFE,
        (
            "唉，本想去郊外玩玩，\x01",
            "没想到偏偏赶在\x01",
            "今天下雨。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        (
            "莫非我就是所谓的雨女吗？\x01",
            "还是说……他是雨男？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_766C")

    label("loc_7557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7596")

    #C0442
    ChrTalk(
        0xFE,
        (
            "刚才那是急救车的声音吧。\x01",
            "究竟发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_766C")

    label("loc_7596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7608")

    #C0443
    ChrTalk(
        0xFE,
        (
            "我昨天在市里的各个地点\x01",
            "拍下了兰花塔的照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "呵呵，等我察觉时，\x01",
            "已经把两个感光回路用掉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_766C")

    label("loc_7608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_766C")

    #C0445
    ChrTalk(
        0xFE,
        "呵呵，克洛斯贝尔真是个好地方啊。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "我想尽量多去一些地方看看，\x01",
            "留下很多美好的回忆～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_766C")

    TalkEnd(0xFE)
    Return()

    # Function_22_7477 end

    def Function_23_7670(): pass

    label("Function_23_7670")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_76CF")

    #C0447
    ChrTalk(
        0xFE,
        (
            "迪塔总统的演说\x01",
            "真是震撼人心啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "我们这些国民必须要\x01",
            "尽可能地协助他！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7730")

    label("loc_76CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7730")

    #C0449
    ChrTalk(
        0xFE,
        (
            "看样子，那起袭击事件\x01",
            "似乎是帝国搞的鬼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "真是不可饶恕。\x01",
            "他们究竟想干什么！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7730")

    TalkEnd(0xFE)
    Return()

    # Function_23_7670 end

    def Function_24_7734(): pass

    label("Function_24_7734")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_77D5")

    #C0451
    ChrTalk(
        0xFE,
        (
            "独立吗……今后自然会\x01",
            "遇到很多麻烦，\x01",
            "但现在的感觉真是不坏。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "只要一想到我们从此就可以\x01",
            "获得真正意义上的自由，\x01",
            "内心深处就会涌起无限勇气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7856")

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7856")

    #C0453
    ChrTalk(
        0xFE,
        (
            "竟然雇佣武装集团，\x01",
            "袭击城市……\x01",
            "真是太肮脏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "有时都已经淡忘了，\x01",
            "但埃雷波尼亚帝国\x01",
            "果然是个可恶的侵略国家啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7856")

    TalkEnd(0xFE)
    Return()

    # Function_24_7734 end

    def Function_25_785A(): pass

    label("Function_25_785A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786F")
    Call(0, 30)
    Jump("loc_7A91")

    label("loc_786F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A61")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_790A")
    Jump("loc_7954")

    label("loc_790A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_792A")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7954")

    label("loc_792A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_794A")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7954")

    label("loc_794A")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7954")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0455
    ChrTalk(
        0x19,
        (
            "#02306F可恶，竟然让主任从早到晚地看管我，\x01",
            "再也没有比这更烦人的了……\x02\x03",

            "#02310F你给我记着，缇欧……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0456
    ChrTalk(
        0x103,
        "#00203F好了，我们走吧，各位。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x19,
        "#02306F喂、喂！不要无视我！\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x109,
        "#10109F（不、不愧是缇欧……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    Jump("loc_7A91")

    label("loc_7A61")

    SetChrSubChip(0x19, 0x0)

    #C0459
    ChrTalk(
        0x19,
        (
            "#02306F好、好了……\x01",
            "我自己吃就行了！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A91")

    TalkEnd(0xFE)
    Return()

    # Function_25_785A end

    def Function_26_7A95(): pass

    label("Function_26_7A95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AAA")
    Call(0, 30)
    Jump("loc_7CB6")

    label("loc_7AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5C")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7B45")
    Jump("loc_7B8F")

    label("loc_7B45")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B65")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B8F")

    label("loc_7B65")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7B85")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B8F")

    label("loc_7B85")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B8F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0460
    ChrTalk(
        0xFE,
        "缇欧，不用担心哦！\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "我会负起责任，\x01",
            "看管好约纳的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 500)

    #C0462
    ChrTalk(
        0x103,
        "#00202F拜托您了，主任。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#00006F（缇欧好像开始懂得怎么\x01",
            "  对待主任了呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_7CB6")

    label("loc_7C5C")

    SetChrSubChip(0xFE, 0x0)

    #C0464
    ChrTalk(
        0xFE,
        (
            "稍微吃些嘛，约纳！\x01",
            "青椒和胡萝卜都很好吃哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "怎么，是不是\x01",
            "想让我喂你呢～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CB6")

    TalkEnd(0xFE)
    Return()

    # Function_26_7A95 end

    def Function_27_7CBA(): pass

    label("Function_27_7CBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DA9")

    #C0466
    ChrTalk(
        0xFE,
        (
            "身为市政府的职员，\x01",
            "我努力疏导市民们避难，\x01",
            "结果自己没能及时避难。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "我的妻子\x01",
            "似乎已经料到了这一点，\x01",
            "和米米一起过来找我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        (
            "从安全角度来考虑，\x01",
            "我自然还是希望她们留在家里……\x01",
            "但能和家人在一起，真是很开心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7E4B")

    label("loc_7DA9")


    #C0469
    ChrTalk(
        0xFE,
        (
            "从安全角度来考虑，\x01",
            "我自然还是希望她们留在家里……\x01",
            "但能和家人在一起，真是很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "餐厅的各位都是\x01",
            "热心又善良的好人。\x01",
            "虽然处在这种状况下，但我还算安心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E4B")

    TalkEnd(0xFE)
    Return()

    # Function_27_7CBA end

    def Function_28_7E4F(): pass

    label("Function_28_7E4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F3A")

    #C0471
    ChrTalk(
        0xFE,
        (
            "我老公回家晚了，\x01",
            "所以我就带孩子出去迎接他……\x01",
            "那雾气真是让人吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        (
            "看样子，那些诡异的智能兵器\x01",
            "似乎可以辨认市民，\x01",
            "并不会发动袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        (
            "话虽如此，但被那种智能兵器\x01",
            "盯着的感觉……\x01",
            "实在是恐怖得难以形容。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7F7C")

    label("loc_7F3A")


    #C0474
    ChrTalk(
        0xFE,
        (
            "呵呵，话说回来，\x01",
            "小孩子果然可爱啊。\x01",
            "在这种时候也能如此开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F7C")

    TalkEnd(0xFE)
    Return()

    # Function_28_7E4F end

    def Function_29_7F80(): pass

    label("Function_29_7F80")

    TalkBegin(0xFE)

    #C0475
    ChrTalk(
        0xFE,
        (
            "听我说哦，\x01",
            "店里的人特意\x01",
            "请我们吃了饭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        "真是非常非常美味。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_7F80 end

    def Function_30_7FCD(): pass

    label("Function_30_7FCD")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3800, 6500, 14680, 0)
    MoveCamera(44, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21010, 0)
    SetChrPos(0x103, -3900, 5000, 16250, 90)
    SetChrPos(0x101, -3900, 5000, 14750, 90)
    SetChrPos(0x102, -3900, 5000, 13250, 45)
    SetChrPos(0x104, -5120, 5000, 13150, 45)
    SetChrPos(0x109, -5110, 5000, 16160, 90)
    SetChrPos(0x105, -5110, 5000, 14750, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    OP_0D()
    SetChrSubChip(0x1A, 0x1)

    #C0477
    ChrTalk(
        0x1A,
        (
            "#11P呀，这不是缇欧\x01",
            "和大家吗～！\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_813F")
    Jump("loc_8189")

    label("loc_813F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_815F")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8189")

    label("loc_815F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_817F")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8189")

    label("loc_817F")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8189")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0478
    ChrTalk(
        0x19,
        "#5P#02302F哟，好久不见。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        "#6P#00000F罗伯兹主任，约纳。\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x103,
        "#6P#00200F两个人一起来吃饭吗？\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x1A,
        (
            "#11P嗯，偶尔也得带\x01",
            "约纳来吃些\x01",
            "营养均衡的好东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x1A,
        (
            "#11P约纳这孩子，\x01",
            "在列曼财团总部的时候，\x01",
            "也是整天只吃比萨。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x103,
        "#6P#00203F啊，这么一说，确实是这样呢。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x105,
        (
            "#6P#10302F蔬菜之类的东西对他而言，\x01",
            "远没有比萨那种吸引力吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x19, 500)

    #C0485
    ChrTalk(
        0x102,
        (
            "#12P#00105F啊，真的呢，\x01",
            "青椒和胡萝卜都剩下了……\x02\x03",

            "#00106F约纳，挑食可不好哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x102, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83E0")
    Jump("loc_842A")

    label("loc_83E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8400")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_842A")

    label("loc_8400")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8420")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_842A")

    label("loc_8420")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_842A")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0486
    ChrTalk(
        0x19,
        (
            "#5P#02306F哼，吃什么东西是我的自由吧。\x02\x03",

            "竟然还特意带我来西餐厅，\x01",
            "让我用刀叉吃这种东西，\x01",
            "实在是浪费时间。\x02\x03",

            "#02309F果然还是比萨这种简单的食物最好，\x01",
            "因为在吃的时候可以同时操作终端……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    #C0487
    ChrTalk(
        0x1A,
        (
            "#11P怎、怎么会……\x01",
            "如此美味的蔬菜\x01",
            "竟然不合约纳的胃口……\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x1A,
        (
            "#11P啊啊，这都是我的错！\x01",
            "我本想让约纳\x01",
            "吃些有营养的好东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x1A,
        (
            "#11P既然如此，我就要召集整个大陆的厨师，\x01",
            "无论如何也要让他们做出\x01",
            "合约纳胃口的蔬菜……！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    OP_63(0x19, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0490
    ChrTalk(
        0x19,
        (
            "#5P#02301F……啊啊，够了！\x01",
            "真是烦人的大叔！\x02\x03",

            "只要我吃掉就行了吧！？\x01",
            "我这就吃！\x02\x03",

            "#02306F（咀嚼）……呜，好苦……\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x109,
        "#6P#10109F啊哈哈，好像还是老样子呢。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x103,
        "#6P#00206F……哎呀呀。\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_87FB")
    Jump("loc_8845")

    label("loc_87FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_881B")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8845")

    label("loc_881B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_883B")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8845")

    label("loc_883B")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8845")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0493
    ChrTalk(
        0x19,
        (
            "#5P#02305F（咀嚼）……（吞咽）。\x01",
            "……啊，对了。\x02\x03",

            "#02301F你们在米修拉姆\x01",
            "有没有探查到和兰花塔事件\x01",
            "有所牵连的『小丑』的行踪？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_895E():
        TurnDirection(0x0, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_895E)
    Sleep(50)

    def lambda_896E():
        TurnDirection(0x1, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_896E)
    Sleep(50)

    def lambda_897E():
        TurnDirection(0x2, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_897E)
    Sleep(50)

    def lambda_898E():
        TurnDirection(0x3, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_898E)
    Sleep(50)

    def lambda_899E():
        TurnDirection(0x4, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_899E)
    Sleep(50)

    def lambda_89AE():
        TurnDirection(0x5, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x5, 0, lambda_89AE)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    WaitChrThread(0x4, 0)
    WaitChrThread(0x5, 0)

    #C0494
    ChrTalk(
        0x101,
        "#6P#00003F……不，并没探查到。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#6P#10108F（虽然在米修拉姆遇到了他……\x01",
            "  但这种事情还是\x01",
            "  不要轻易说出去为好。）\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x19,
        (
            "#5P#02306F啧，是吗……那就算了。\x02\x03",

            "#02310F那个『小丑』……自兰花塔事件之后，\x01",
            "就没在导力网络上现过身了。\x02\x03",

            "那家伙把我的基地\x01",
            "搞得乱七八糟，\x01",
            "必须要给他个回礼才行……\x02\x03",

            "你们以后要是掌握到了什么情报，\x01",
            "可要告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#12P#00103F唔……这实在是\x01",
            "不能答应你……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x19,
        (
            "#5P#02306F不要小气嘛……\x01",
            "你们只要输入到\x01",
            "数据库里就行了。\x02\x03",

            "#02309F我会通过黑客技术\x01",
            "自行查阅的。\x02",
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
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0499
    ChrTalk(
        0x104,
        "#12P#00306F喂喂……\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    #C0500
    ChrTalk(
        0x103,
        (
            "#6P#00206F……你现在已经在ＩＢＣ大楼\x01",
            "的分部任职了，\x01",
            "应该稍微安分些才对。\x02\x03",

            "#00200F主任，拜托您\x01",
            "仔细看管好约纳。\x02\x03",

            "#00203F导力网络的基本法规已经正式施行，\x01",
            "今后如果再发现露骨的黑客行为，\x01",
            "可就不能轻易姑息了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x1)

    #C0501
    ChrTalk(
        0x1A,
        "#11P我、我知道了，缇欧！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    #C0502
    ChrTalk(
        0x1A,
        (
            "#11P约纳，我一定会负起责任，\x01",
            "从早到晚看好你的！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0503
    ChrTalk(
        0x19,
        (
            "#5P#02305F喂、喂！缇欧……\x01",
            "你未免太过分了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    #C0504
    ChrTalk(
        0x103,
        "#5P#00203F好，我们走吧，各位。\x02",
    )

    CloseMessageWindow()

    def lambda_8E0E():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E0E)
    Sleep(50)

    def lambda_8E1E():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8E1E)
    Sleep(50)

    def lambda_8E2E():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E2E)
    Sleep(50)

    def lambda_8E3E():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8E3E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0505
    ChrTalk(
        0x101,
        "#12P#00005F啊……嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x105,
        "#6P#10302F（呵呵，漂亮地推给主任了呢。）\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x0, -3900, 5000, 14750, 180)
    SetScenarioFlags(0x16B, 1)
    EventEnd(0x5)
    Return()

    # Function_30_7FCD end

    def Function_31_8EDE(): pass

    label("Function_31_8EDE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -440, 5000, 17810, 225)
    SetChrPos(0x102, 120, 5000, 17030, 270)
    SetChrPos(0x104, -480, 5000, 18810, 225)
    SetChrPos(0x109, 750, 5000, 18280, 225)
    SetChrPos(0x105, 150, 5000, 16110, 270)
    LoadChrToIndex("chr/ch13300.itc", 0x1E)
    SetChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12000.itp")
    OP_68(-1200, 6500, 17340, 0)
    MoveCamera(19, 31, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22980, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0507
    ChrTalk(
        0x104,
        "#11P#00305F噢噢，这不是雾香小姐吗！\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        "#00000F好久不见了，雾香小姐。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        (
            "#6P#12002F啊，是你们……\x02\x03",

            "#12004F呵呵，大家好啊。\x01",
            "竟然在这种地方相遇，真巧呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0510
    ChrTalk(
        0x101,
        (
            "#00003F我们是通过目击证言\x01",
            "找到这里的。\x02\x03",

            "#00001F自『竞拍会』一别之后，真是好久不见啊。\x01",
            "……洛克史密斯机关的主任，\x01",
            "雾香·楼兰小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0511
    AnonymousTalk(
        0x1E,
        (
            "也对，我这次的身份与\x01",
            "之前见面时有所不同，\x01",
            "重新做个自我介绍吧。\x02\x03",

            "卡尔瓦德共和国\x01",
            "总统辅佐官，\x01",
            "雾香·楼兰。\x02\x03",

            "除此之外，还有其它身份……\x01",
            "就不一一说明了。\x02",
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

    #C0512
    ChrTalk(
        0x102,
        (
            "#00100F顺便一问，您以前所说的\x01",
            "演艺界制作人是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x1E,
        (
            "#6P#12004F呵呵，\x01",
            "那的确也是我的身份之一。\x02\x03",

            "#12002F至于我的事务所，\x01",
            "也确实存在于共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x101,
        (
            "#00003F原来如此，\x01",
            "这方面的安排也毫无漏洞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，拥有多重身份的\x01",
            "  女间谍吗。）\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        (
            "#11P#00309F（嗯～充满神秘感的\x01",
            "  雾香小姐也很有魅力呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x109,
        (
            "#10106F（前辈，这种发言\x01",
            "  未免太欠缺紧张感了吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#00105F说起来……\x01",
            "您以总统辅佐官的身份来访克洛斯贝尔，\x01",
            "为什么会在这种地方呢？\x02\x03",

            "听说洛克史密斯总统\x01",
            "今天的行程是\x01",
            "视察ＩＢＣ……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "#6P#12004F那是因为总统派我\x01",
            "买些东西。\x02\x03",

            "#12000F悄悄完成购物之后，\x01",
            "我就来此吃个\x01",
            "稍迟了些的午餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x109,
        "#10105F买东西吗……？\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        "#6P#12004F就是这个。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雾香取出风车，\x01",
            "并吹了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #A0523
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "风车咕噜噜地转动了起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0524
    ChrTalk(
        0x109,
        "#10105F风、风车……？\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "#6P#12000F我们乘坐的轿车经过露天摊子，\x01",
            "总统看到它之后，就非常想要呢。\x02\x03",

            "在明天的正式会议到来之前，\x01",
            "总统想把它当作放松心情的道具，\x01",
            "放在自己的手边。\x02\x03",

            "#12004F顺便还要买些水果，\x01",
            "作为今晚的餐后甜品。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0526
    ChrTalk(
        0x104,
        (
            "#11P#00306F听、听起来……\x01",
            "好像还真是出来买东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，这种风格……真不愧是\x01",
            "以庶民派而闻名的洛克史密斯总统啊。\x02\x03",

            "#10304F不过，前提是……刚才说的那些\x01",
            "确实是你上街的真实目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x101,
        "#00001F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "#6P#12004F呵呵，随各位想象吧。\x02\x03",

            "#12000F好了，我已经吃完了，\x01",
            "差不多也该告辞了。\x02\x03",

            "你们也要多多加油，\x01",
            "做好通商会议期间的警备工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        (
            "#00105F是、是的，\x01",
            "谢谢。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1800, 6500, 17260, 1000)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2610, 5000, 17800, 180)
    Sleep(1200)

    def lambda_9819():

        label("loc_9819")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_9819")

    QueueWorkItem2(0x101, 2, lambda_9819)

    def lambda_982B():

        label("loc_982B")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_982B")

    QueueWorkItem2(0x102, 2, lambda_982B)

    def lambda_983D():

        label("loc_983D")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_983D")

    QueueWorkItem2(0x104, 2, lambda_983D)

    def lambda_984F():

        label("loc_984F")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_984F")

    QueueWorkItem2(0x109, 2, lambda_984F)

    def lambda_9861():

        label("loc_9861")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_9861")

    QueueWorkItem2(0x105, 2, lambda_9861)
    OP_0D()
    OP_68(-2300, 6500, 15500, 2800)
    OP_95(0xFE, -3790, 5000, 17390, 2000, 0x1)
    OP_95(0xFE, -3790, 5000, 13140, 2000, 0x1)
    OP_68(1000, 6500, 15280, 5500)
    OP_95(0xFE, -2250, 5000, 11680, 2000, 0x1)
    OP_95(0xFE, 8000, 5000, 11660, 2000, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_9906")
    Call(0, 32)
    Jump("loc_9909")

    label("loc_9906")

    Sleep(1000)

    label("loc_9909")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -300, 5000, 17650, 225)
    ClearChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 0x17)
    OP_D7(0x1E)
    OP_CC(0x1, 0x0, 0x0)
    SetScenarioFlags(0x1C7, 0)
    OP_29(0xA3, 0x1, 0xB)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_8EDE end

    def Function_32_9954(): pass

    label("Function_32_9954")

    OP_68(-740, 6500, 17510, 2000)
    MoveCamera(45, 16, 0, 2000)
    OP_6E(360, 2000)
    SetCameraDistance(20440, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0xFFFF)

    #C0531
    ChrTalk(
        0x101,
        (
            "#00003F雷克特先生和雾香小姐……\x02\x03",

            "帝国与共和国的谍报人员\x01",
            "在同一时间段\x01",
            "出现在了市内。\x02\x03",

            "#00001F……各位，你们怎么想？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_9A1E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9A1E)
    Sleep(50)

    def lambda_9A2E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9A2E)
    Sleep(50)

    def lambda_9A3E():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9A3E)
    Sleep(50)

    def lambda_9A4E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9A4E)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0532
    ChrTalk(
        0x109,
        "#10103F……总觉得有些蹊跷呢。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，既然如此，\x01",
            "我们要继续追踪他们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x102,
        (
            "#00108F那应该很困难吧。\x02\x03",

            "#00103F在我们赶到的时候，\x01",
            "他们都是一副早已料到的样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#00003F……还是去向达德利警官\x01",
            "他们报告吧。\x02\x03",

            "#00000F结合搜查一科的情报，\x01",
            "说不定可以了解到什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x109,
        "#10105F啊……有道理呢。\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x104,
        (
            "#00300F好，既然决定了，\x01",
            "那我们就去警察总部吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_32_9954 end

    def Function_33_9BD3(): pass

    label("Function_33_9BD3")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    EventBegin(0x0)
    Fade(500)
    OP_68(-1300, 1500, 8730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x101, 110, 0, 9440, 0)
    SetChrPos(0x102, -1110, 0, 9440, 0)
    SetChrPos(0x103, 110, 0, 8240, 0)
    SetChrPos(0x104, -1110, 0, 8240, 0)
    SetChrPos(0x109, -1110, 0, 7040, 0)
    SetChrPos(0x105, 110, 0, 7040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0538
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临『温赛特餐厅』。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        "是预约席位的客人吗？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，我们是\x01",
            "特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将『美食向导』取材一事的\x01",
            "情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0542
    ChrTalk(
        0x8,
        (
            "啊，原来各位是为此而来的啊。\x01",
            "事情我已经听通讯社的人说过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x8,
        (
            "请大家先找个\x01",
            "空位子就坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x8,
        (
            "马上就为大家献上本店这个季度\x01",
            "的新料理『香草面』。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        "#00100F呵呵，那就麻烦您了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetChrPos(0x101, -1160, 200, 2350, 270)
    SetChrPos(0x103, -3250, 200, 180, 0)
    SetChrPos(0x104, -4460, 200, 840, 45)
    SetChrPos(0x105, -5400, 200, 2300, 90)
    SetChrPos(0x109, -4700, 200, 3800, 135)
    SetChrPos(0x102, -3140, 200, 4370, 180)
    SetChrPos(0x8, -720, 0, 4770, 240)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    OP_68(-3170, 1500, 2380, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x2)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x24)
    SetChrSubChip(0x24, 0x2)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x24)
    SetChrSubChip(0x25, 0x2)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x24)
    SetChrSubChip(0x26, 0x2)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x2)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0546
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人坐在席位上，\x01",
            "品尝了香草面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0547
    ChrTalk(
        0x103,
        "#00200F（咀嚼）……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        (
            "呵呵，本店的厨师引以为傲\x01",
            "的薏面如何呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x109,
        "#10109F嗯，非常好吃！\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，味道浓厚，\x01",
            "回味却很清香。\x02\x03",

            "#10300F有效利用了香草的味道，\x01",
            "口感清爽可口。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        (
            "#00309F嗯，这个餐厅的料理\x01",
            "果然美味啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x8,
        (
            "哈哈，能让大家\x01",
            "满意就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，下次一定要带\x01",
            "小琪雅一起来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        "#00000F嗯，一定。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x8,
        (
            "呵呵，本店所有职员\x01",
            "都会期待各位的再次光临。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 110, 0, 9440, 0)
    SetChrPos(0x102, -1110, 0, 9440, 0)
    SetChrPos(0x103, 110, 0, 8240, 0)
    SetChrPos(0x109, -1110, 0, 8240, 0)
    SetChrPos(0x105, 110, 0, 7040, 0)
    SetChrPos(0x104, -1110, 0, 7040, 0)
    SetChrPos(0x8, -510, 0, 12450, 180)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    OP_68(-1300, 1500, 8730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetScenarioFlags(0x1, 7)
    SetScenarioFlags(0x172, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A2F8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A315")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A328")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A33B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A358")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A36B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A388")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A39B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A3B8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A3CB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A3E8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3E8")

    OP_29(0x80, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4BD")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0556
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在六家饮食店完成了取材！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A4B4")

    #A0557
    AnonymousTalk(
        0x101,
        (
            "#00003F现在就可以去向\x01",
            "格蕾丝小姐报告了……\x02\x03",

            "#00000F不过，还没有把六个人\x01",
            "喜欢的美食全部找到。\x01",
            "不如再努努力吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A4B4")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_A4BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A580")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "找到了特别任务支援科\x01",
            "全体成员各自喜欢的美食。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0559
    AnonymousTalk(
        0x101,
        (
            "#00000F这样一来，已经找到\x01",
            "所有人喜欢的美食了啊。\x02\x03",

            "取材工作已经足够了，\x01",
            "马上去通讯社报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_A580")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A5A2")
    Jump("loc_A70A")

    label("loc_A5A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A5C7")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_A70A")

    label("loc_A5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A5D5")
    Jump("loc_A70A")

    label("loc_A5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A5E3")
    Jump("loc_A70A")

    label("loc_A5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A61F")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_A70A")

    label("loc_A61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A65B")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_A70A")

    label("loc_A65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A697")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_A70A")

    label("loc_A697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A6D3")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_A70A")

    label("loc_A6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A70A")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)

    label("loc_A70A")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -510, 0, 9440, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_9BD3 end

    def Function_34_A73A(): pass

    label("Function_34_A73A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47500.itc", 0x1E)
    LoadChrToIndex("chr/ch44000.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    LoadChrToIndex("chr/ch02902.itc", 0x24)
    LoadChrToIndex("chr/ch03002.itc", 0x25)
    LoadChrToIndex("chr/ch47502.itc", 0x26)
    LoadChrToIndex("chr/ch44002.itc", 0x27)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(10110, 3000, 8790, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x20, 0x26)
    SetChrChipByIndex(0x21, 0x27)
    SetChrSubChip(0x20, 0x0)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrPos(0x20, -3200, 80, 4500, 180)
    SetChrPos(0x21, -1000, 80, 2450, 270)
    SetChrPos(0x101, 15000, 0, 9000, 270)
    SetChrPos(0x102, 15000, 0, 9000, 270)
    SetChrPos(0x103, 15000, 0, 9000, 270)
    SetChrPos(0x104, 15000, 0, 9000, 270)
    SetChrPos(0x109, 15000, 0, 9000, 270)
    SetChrPos(0x105, 15000, 0, 9000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(10110, 1500, 8790, 2500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 35)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 36)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 37)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 39)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(50)

    #C0560
    ChrTalk(
        0x101,
        "#00005F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_A95D():
        OP_93(0x102, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A95D)
    Sleep(50)

    def lambda_A96D():
        OP_93(0x103, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A96D)
    Sleep(50)

    def lambda_A97D():
        OP_93(0x104, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A97D)
    Sleep(50)

    def lambda_A98D():
        OP_93(0x109, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A98D)
    Sleep(50)

    def lambda_A99D():
        OP_93(0x105, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A99D)
    Sleep(800)
    Fade(500)
    OP_68(-3200, 1500, 1900, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19960, 0)
    OP_0D()
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #N0561
    NpcTalk(
        0x20,
        "男公关？",
        (
            "……哈哈，玛格丽特夫人\x01",
            "真是独具慧眼啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0562
    NpcTalk(
        0x20,
        "男公关？",
        (
            "这样说也许有点失礼，\x01",
            "但您的丈夫真是配不上您。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x21,
        (
            "哦呵呵……\x01",
            "克莱德先生还是\x01",
            "这么会说话啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_64(0x20)
    OP_64(0x21)
    OP_0D()
    Fade(500)
    OP_68(10110, 1500, 8790, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_0D()

    #C0564
    ChrTalk(
        0x102,
        (
            "#00100F……看样子，副局长的太太\x01",
            "就是那个人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x105,
        (
            "#10305F也就是说，坐在她对面的那个人\x01",
            "就是疑似男公关的『克莱德』啊。\x02\x03",

            "#10303F唔，果然从没见过这张脸呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x101,
        (
            "#00003F总之，在不引起他们怀疑的前提下，\x01",
            "坐到他们附近吧。\x02\x03",

            "#00001F说不定能听到什么情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x103,
        "#00200F明白。\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x109,
        (
            "#10100F既然如此，我们就\x01",
            "分开坐吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    OP_68(3220, 1500, -160, 0)
    MoveCamera(48, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19960, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x24)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x25)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    SetChrPos(0x101, 6800, 50, 3640, 270)
    SetChrPos(0x102, 4550, 50, 5810, 180)
    SetChrPos(0x103, 4550, 50, 1600, 0)
    SetChrPos(0x109, 3330, 50, -6250, 0)
    SetChrPos(0x105, 1050, 50, -3900, 90)
    SetChrPos(0x104, 5340, 0, -4100, 270)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    Sleep(800)
    OP_68(2730, 1500, -2710, 3000)
    OP_0D()
    Sleep(3000)
    OP_68(-3200, 1500, 1900, 3000)
    MoveCamera(24, 24, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19960, 3000)
    OP_6F(0x79)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_64(0x20)
    OP_64(0x21)

    #C0569
    ChrTalk(
        0x21,
        (
            "对了对了，之前你给我的\x01",
            "那本宣传册……\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x21,
        "我看了照片之后，一眼就被吸引住了。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x20,
        "哈哈，这真是让人深感荣幸。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x20,
        (
            "既然如此，下次就\x01",
            "一起去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x20,
        (
            "如果有需要，\x01",
            "我会为您预定酒店的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x21,
        "呵呵呵，那倒不必。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x21,
        (
            "其实我已经去探查过了哦。\x01",
            "景色真是出众，简直无可挑剔。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x20,
        "哦哦！是吗！\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x20,
        (
            "哎呀，那真是太好了！\x01",
            "既然如此，就快点约定……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_64(0x20)
    OP_64(0x21)
    Sleep(500)
    Fade(500)
    OP_68(3690, 1500, 2080, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19760, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x2)
    OP_0D()

    #C0578
    ChrTalk(
        0x101,
        "#00001F（……聊得相当愉快啊。）\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x102,
        (
            "#00103F（听起来，好像是计划要\x01",
            "  一起去米修拉姆旅行……）\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x103,
        (
            "#00200F（不过总觉得\x01",
            "  有些奇怪。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2220, 1500, -5240, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19810, 0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x2)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    #C0581
    ChrTalk(
        0x104,
        (
            "#00303F（那个男人的\x01",
            "  语气过于恭敬，\x01",
            "  让人有点在意。）\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x109,
        (
            "#10106F（但我们还没有了解\x01",
            "  决定性的关键内容……）\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，那就再听\x01",
            "  一阵子吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(-3200, 1500, 1900, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19960, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    FadeToBright(2000, 0)
    OP_0D()

    #C0584
    ChrTalk(
        0x20,
        "……那我今天就先告辞了。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x21,
        (
            "嗯，好的。\x01",
            "稍后就在那家店里见面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x20,
        (
            "欢乐街的『诺艾·布朗』是吧？\x01",
            "呵呵，好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x20,
        (
            "我会带着夫人需要的东西\x01",
            "前去赴会的。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x21,
        "嗯，我等着你。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x20, 1, 0, 41)
    Sleep(300)
    BeginChrThread(0x21, 1, 0, 42)
    Sleep(300)
    OP_68(-650, 1550, 7560, 3000)
    WaitChrThread(0x20, 1)
    Sleep(800)

    def lambda_B253():
        OP_95(0x20, 4230, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B253)
    Sleep(200)
    WaitChrThread(0x21, 1)

    def lambda_B274():
        OP_95(0x21, 4230, 0, 7840, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B274)
    Sleep(1500)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    Fade(500)
    OP_68(2710, 1500, -1840, 0)
    MoveCamera(46, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22840, 0)
    SetChrPos(0x20, 11630, 0, 9250, 90)
    SetChrPos(0x21, 10110, 0, 8780, 90)

    def lambda_B2F1():
        OP_95(0x20, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B2F1)

    def lambda_B30B():
        OP_95(0x21, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B30B)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x2)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x1)
    OP_0D()
    Sleep(50)

    #C0589
    ChrTalk(
        0x101,
        "#00001F（好像要离开餐厅了……）\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x102,
        "#00100F（罗伊德，怎么办？）\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#00200F（还没有得到决定性\x01",
            "  的关键情报……）\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#00003F（……跟踪他们吧。）\x02\x03",

            "#00000F（我、瓦吉和兰迪\x01",
            "  去跟着那个叫克莱德的男子。）\x02\x03",

            "（艾莉、缇欧和诺艾尔\x01",
            "  去跟着玛格丽特夫人。）\x02\x03",

            "（一定要随时保持警觉，\x01",
            "  不要被对方发现。）\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x109,
        "#10101F（……明白了！）\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        "#00300F（那我们就出发吧。）\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x105,
        "#10302F（呵呵，越来越有趣了啊。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_34_A73A end

    def Function_35_B4E9(): pass

    label("Function_35_B4E9")


    def lambda_B4EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B4EE)

    def lambda_B4FF():
        OP_95(0x101, 10110, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4FF)
    WaitChrThread(0x101, 1)
    Return()

    # Function_35_B4E9 end

    def Function_36_B519(): pass

    label("Function_36_B519")


    def lambda_B51E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B51E)

    def lambda_B52F():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B52F)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, 10600, 0, 10450, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_36_B519 end

    def Function_37_B55F(): pass

    label("Function_37_B55F")


    def lambda_B564():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B564)

    def lambda_B575():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B575)
    WaitChrThread(0x103, 1)
    OP_95(0xFE, 11310, 0, 7580, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_B55F end

    def Function_38_B5A5(): pass

    label("Function_38_B5A5")


    def lambda_B5AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B5AA)

    def lambda_B5BB():
        OP_95(0xFE, 11630, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B5BB)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_38_B5A5 end

    def Function_39_B5DC(): pass

    label("Function_39_B5DC")


    def lambda_B5E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B5E1)

    def lambda_B5F2():
        OP_95(0xFE, 12860, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B5F2)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_B5DC end

    def Function_40_B613(): pass

    label("Function_40_B613")


    def lambda_B618():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B618)

    def lambda_B629():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B629)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, 12200, 0, 10670, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_B613 end

    def Function_41_B659(): pass

    label("Function_41_B659")

    Fade(500)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x20, -2700, 0, 4500, 90)
    OP_0D()
    OP_95(0x20, -370, 0, 9500, 1500, 0x0)
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(500)
    Return()

    # Function_41_B659 end

    def Function_42_B69D(): pass

    label("Function_42_B69D")

    Fade(500)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x21, -1160, 0, 2700, 0)
    OP_0D()
    Sleep(500)
    OP_95(0x21, -100, 0, 7840, 1500, 0x0)
    OP_93(0x21, 0x0, 0x1F4)
    Return()

    # Function_42_B69D end

    def Function_43_B6E1(): pass

    label("Function_43_B6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B872")

    #C0596
    ChrTalk(
        0xB,
        "啊，欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xB,
        (
            "请随意就坐吧，\x01",
            "马上就会来为您服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        (
            "#00003F（职业女性选秀活动\x01",
            "  中的『服务员』……\x01",
            "  让她来担当应该很不错吧？）\x02\x03",

            "#00000F那个，不好意思。\x01",
            "有点事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0599
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

    #C0600
    ChrTalk(
        0xB,
        (
            "哎？\x01",
            "让我参加职业女性选秀吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xB,
        (
            "唔～\x01",
            "虽然很不好意思……\x01",
            "但我确实没什么兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#00012F是、是吗……\x01",
            "真是打扰了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 5)
    Jump("loc_B8DB")

    label("loc_B872")


    #C0603
    ChrTalk(
        0xB,
        (
            "我对职业女性选秀活动\x01",
            "并不是很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xB,
        (
            "如果要我以服务员的身份\x01",
            "去活动现场帮些忙，\x01",
            "倒是没有问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8DB")

    TalkEnd(0xB)
    Return()

    # Function_43_B6E1 end

    SaveToFile()

Try(main)
