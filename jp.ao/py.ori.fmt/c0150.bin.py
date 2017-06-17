from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ホイストフ",             # 1
        "ブラウン",               # 2
        "セルテオ",               # 3
        "ノンノ",                 # 4
        "フロテ",                 # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "市民",                   # 8
        "市民",                   # 9
        "市民",                   # 10
        "市民",                   # 11
        "観光客",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "市民",                   # 16
        "市民",                   # 17
        "ヨナ",                   # 18
        "ロバーツ主任",           # 19
        "アベル",                 # 20
        "ミミ",                   # 21
        "サリー",                 # 22
        "キリカ補佐官",           # 23
        "ジロンド",               # 24
        "クライド",               # 25
        "マーガレット夫人",       # 26
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
        "Function_5_EC5",          # 05, 5
        "Function_6_EC9",          # 06, 6
        "Function_7_272D",         # 07, 7
        "Function_8_2731",         # 08, 8
        "Function_9_3E69",         # 09, 9
        "Function_10_4DFA",        # 0A, 10
        "Function_11_60B7",        # 0B, 11
        "Function_12_6ED7",        # 0C, 12
        "Function_13_7FDF",        # 0D, 13
        "Function_14_80A0",        # 0E, 14
        "Function_15_8190",        # 0F, 15
        "Function_16_822D",        # 10, 16
        "Function_17_82F2",        # 11, 17
        "Function_18_8417",        # 12, 18
        "Function_19_84E7",        # 13, 19
        "Function_20_85EB",        # 14, 20
        "Function_21_8781",        # 15, 21
        "Function_22_8998",        # 16, 22
        "Function_23_8BFB",        # 17, 23
        "Function_24_8CEF",        # 18, 24
        "Function_25_8E55",        # 19, 25
        "Function_26_90B8",        # 1A, 26
        "Function_27_933D",        # 1B, 27
        "Function_28_94F2",        # 1C, 28
        "Function_29_966B",        # 1D, 29
        "Function_30_96F0",        # 1E, 30
        "Function_31_A7F3",        # 1F, 31
        "Function_32_B3EB",        # 20, 32
        "Function_33_B6D8",        # 21, 33
        "Function_34_C341",        # 22, 34
        "Function_35_D2BA",        # 23, 35
        "Function_36_D2EA",        # 24, 36
        "Function_37_D330",        # 25, 37
        "Function_38_D376",        # 26, 38
        "Function_39_D3AD",        # 27, 39
        "Function_40_D3E4",        # 28, 40
        "Function_41_D42A",        # 29, 41
        "Function_42_D46E",        # 2A, 42
        "Function_43_D4B2",        # 2B, 43
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
            "＝新メニュー・ハーブパスタ＝\x01",
            " ・お客様の懐かしの味を再現\x01",
            " ・爽やかなハーブを生かす\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハーブパスタのレシピが書かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_EC1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ハーブパスタ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_EC1")

    TalkEnd(0xFF)
    Return()

    # Function_4_DB1 end

    def Function_5_EC5(): pass

    label("Function_5_EC5")

    Call(0, 6)
    Return()

    # Function_5_EC5 end

    def Function_6_EC9(): pass

    label("Function_6_EC9")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A2")

    #C0004
    ChrTalk(
        0x1F,
        "よう、特務支援課の。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x1F,
        (
            "セルゲイから聞いてるが、\x01",
            "いよいよ再始動するんだってな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0006
    ChrTalk(
        0x1F,
        (
            "ん？　赤毛の兄ちゃんと\x01",
            "魔導杖の嬢ちゃんは、\x01",
            "まだいねえみてえだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00000Fええ、２人はまだ\x01",
            "用事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x1F,
        "フン、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x1F,
        (
            "で、そこの２人が\x01",
            "新メンバーってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x1F,
        (
            "得物の話はセルゲイから聞いてる。\x01",
            "ま、適当に見て行ってくんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x105,
        "#10302Fフフ、随分根回しがいいんだね。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        "#10102Fどうも、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 2)

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AE")
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0013
    ChrTalk(
        0x1F,
        (
            "よお、おめえらか……\x01",
            "よく来やがったな！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000Fジロンドさん、\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_128E")

    #C0015
    ChrTalk(
        0x1F,
        (
            "へへっ、頼もしそうな\x01",
            "面構えで何よりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x1F,
        (
            "だがダドリーも一緒とは……\x01",
            "いよいよ動き出すってわけだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x10A,
        (
            "#00603Fええ、少々騒がしくなると\x01",
            "思いますが、ご容赦ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x1F,
        (
            "へっ、んなもん\x01",
            "今さら気にするかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x1F,
        (
            "ま、とりあえず、\x01",
            "店の方は色々あたって\x01",
            "何とか品は揃えてある状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1F,
        (
            "大したもんはねえが、\x01",
            "適当に見て行ってくれや。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_128E")


    #C0021
    ChrTalk(
        0x1F,
        (
            "へへっ、頼もしそうな\x01",
            "面構えで何よりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x1F,
        (
            "ちなみに警察の連中から\x01",
            "話は色々聞いてるからな。\x01",
            "多くを語る必要はねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x1F,
        (
            "ま、とりあえず\x01",
            "店の方は色々あたって\x01",
            "何とか品は揃えてある状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x1F,
        (
            "大したもんはねえが、\x01",
            "適当に見て行ってくれや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1382")


    #C0025
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 0)

    label("loc_13AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2729")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1416")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1416")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1435")
    OP_AF(0x5)
    Jump("loc_1477")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1445")
    OP_AF(0x4)
    Jump("loc_1477")

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1455")
    OP_AF(0x3)
    Jump("loc_1477")

    label("loc_1455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1465")
    OP_AF(0x2)
    Jump("loc_1477")

    label("loc_1465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1475")
    OP_AF(0x1)
    Jump("loc_1477")

    label("loc_1475")

    OP_AF(0x0)

    label("loc_1477")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2724")

    label("loc_1486")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149A")
    Jump("loc_2724")

    label("loc_149A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2724")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_155D")

    #C0026
    ChrTalk(
        0x1F,
        (
            "ふぅ、あの不気味な大樹はともかく、\x01",
            "ようやく街も落ち着いたって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x1F,
        (
            "ま、これからがまさに大変なわけだが……\x01",
            "こうなりゃトコトン足掻くだけだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_155D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15D9")

    #C0028
    ChrTalk(
        0x1F,
        (
            "へっ、しかしまたこうして\x01",
            "特務支援課の顔を拝めるたあな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x1F,
        (
            "とにかくお前ら、\x01",
            "今後とも気合い入れてけよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_15D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")

    #C0030
    ChrTalk(
        0x1F,
        (
            "国防軍たあ、ディーター・クロイスも\x01",
            "また大それたことをしたもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x1F,
        (
            "ご丁寧に制服まで用意しくさって、\x01",
            "随分とまあ用意周到な話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x1F,
        (
            "武器や兵器なんてモンは\x01",
            "本当は持たねえ方がいいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1F,
        (
            "ま、そんなことばかりも\x01",
            "言ってられないのが現実ってヤツか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179E")

    label("loc_16FC")


    #C0034
    ChrTalk(
        0x1F,
        (
            "武器や兵器なんてモンは\x01",
            "本当は持たねえ方がいいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1F,
        (
            "ま、そんなことばかりも\x01",
            "言ってられないのが現実ってヤツか。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x1F,
        "やれやれ……先が思いやられるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_179E")

    Jump("loc_2724")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A3")

    #C0037
    ChrTalk(
        0x1F,
        (
            "この前のマインツの騒ぎのせいで、\x01",
            "市民が武器を買いたいって\x01",
            "店に押しかけて来るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x1F,
        (
            "許可証がなきゃ\x01",
            "売れねえっつってんだが……\x01",
            "中にはしつこいヤツもいるんだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1F,
        (
            "まあ、こんな状況だから\x01",
            "気持ちが分からんでもないが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1932")

    label("loc_18A3")


    #C0040
    ChrTalk(
        0x1F,
        (
            "とかく、武器ってモンを扱うにゃあ\x01",
            "そいつに見合っただけの\x01",
            "責任と覚悟ってヤツがいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1F,
        (
            "いい機会だ。\x01",
            "お前らも改めて肝に銘じておけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1932")

    Jump("loc_2724")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A03")

    #C0042
    ChrTalk(
        0x1F,
        (
            "よお、今日はまた随分と\x01",
            "辛気臭いツラしてやがんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x1F,
        (
            "もしもこれから危険な場所に\x01",
            "踏み込むってんなら、\x01",
            "決して準備を怠るンじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x1F,
        "客が死ぬのは趣味じゃねえからな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A7D")

    label("loc_1A03")


    #C0045
    ChrTalk(
        0x1F,
        (
            "もしもこれから危険な場所に\x01",
            "踏み込むってんなら、\x01",
            "決して準備を怠るンじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x1F,
        "客が死ぬのは趣味じゃねえからな。\x02",
    )

    CloseMessageWindow()

    label("loc_1A7D")

    Jump("loc_2724")

    label("loc_1A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7C")

    #C0047
    ChrTalk(
        0x1F,
        (
            "昨日起きた列車事故ってのは、\x01",
            "何でも鬼みてえな\x01",
            "化物の仕業だって噂じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1F,
        (
            "へっ、鬼だなんて簡単に言うが、\x01",
            "一体何のことだって話だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x1F,
        (
            "まさか人間が化けたって\x01",
            "ワケでもねえだろうし……\x01",
            "とにかく物騒な話だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C09")

    label("loc_1B7C")


    #C0050
    ChrTalk(
        0x1F,
        (
            "へっ、鬼だなんて簡単に言うが、\x01",
            "一体何のことだって話だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1F,
        (
            "まさか人間が化けたって\x01",
            "ワケでもねえだろうし……\x01",
            "とにかく物騒な話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C09")

    Jump("loc_2724")

    label("loc_1C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C98")

    #C0052
    ChrTalk(
        0x1F,
        (
            "はあ、サイレンの音が\x01",
            "やかましいったらありゃしねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x1F,
        (
            "事件か事故かは知らんが……\x01",
            "まったくこの街は騒がしいモンだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D81")

    #C0054
    ChrTalk(
        0x1F,
        "おう、お前らか。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x1F,
        (
            "何でもいいから\x01",
            "パパッと選んでけよ、パパッと。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x1F,
        (
            "あんまり居座られると、\x01",
            "雑誌が読みにくくて仕方ねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00006F（……相変わらず、まともに\x01",
            "  仕事をする気がないんだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DFD")

    label("loc_1D81")


    #C0058
    ChrTalk(
        0x1F,
        (
            "何が欲しいのか知らねえが、\x01",
            "とにかくパパッと選んでけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x1F,
        (
            "あんまり居座られると、\x01",
            "雑誌が読みにくくて仕方ねえからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFD")

    Jump("loc_2724")

    label("loc_1E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EA2")

    #C0060
    ChrTalk(
        0x1F,
        (
            "はあ、２大国サマの要求を呑むわけには\x01",
            "いかんとはいえ、ここで独立の提唱か。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x1F,
        (
            "ま、何にせよ、この先戦争沙汰に\x01",
            "ならねえことだけを祈ってるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_1EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_22BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224C")

    #C0062
    ChrTalk(
        0x1F,
        (
            "よう、嬢ちゃん。\x01",
            "ついに支援課に復帰したみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x1F,
        (
            "あの男が魔導杖を置いていったから\x01",
            "そろそろ来るんじゃねえかと思ってたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00005Fあ、あの男って……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#00203Fええ、おそらくでなくとも主任です。\x02\x03",

            "#00211Fこの先回り感が、\x01",
            "そこはかとなくウザイです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#00109Fま、まあ、それだけ\x01",
            "心配しているという事でしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そんなに\x01",
            "悪い人じゃないっていうか、\x01",
            "かなり良い人だと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#00206F……その点は認めなくもないですが、\x01",
            "それだけに余計、性質#4Rた ち#が悪いかと。\x02\x03",

            "#00200Fそもそもお節介がすぎる上に\x01",
            "不器用で無駄話も多くて……\x01",
            "とても付き合いきれません。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2126")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2126")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214C")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_214C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2172")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2172")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2198")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2198")

    Sleep(1000)

    #C0069
    ChrTalk(
        0x109,
        (
            "#10103Fな、なるほど、\x01",
            "ティオちゃんにも色々あるんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x1F,
        (
            "ふははっ、よく分からねえが\x01",
            "これからは魔導杖の取り扱いも再開だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x1F,
        "入用だったらいつでも言ってくれや。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 5)
    Jump("loc_22B6")

    label("loc_224C")


    #C0072
    ChrTalk(
        0x1F,
        (
            "嬢ちゃんが復帰したもんで、\x01",
            "魔導杖の取り扱いも再開だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x1F,
        (
            "ま、入用だったら\x01",
            "いつでも声掛けてくれや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B6")

    Jump("loc_2724")

    label("loc_22BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E7")

    #C0074
    ChrTalk(
        0x1F,
        (
            "よう、ダドリーじゃねえか。\x01",
            "支援課と仲良くお散歩かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x10A,
        (
            "#00603Fいえ、少々気になる事がありまして。\x02\x03",

            "#00600Fこいつらだけでは\x01",
            "頼りないので同行しているだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x1F,
        "へっ、お前も相変わらずだな。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x1F,
        (
            "まあいい、そろそろ店仕舞いなもんで\x01",
            "見るならチャッチャと見てくれや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2454")

    label("loc_23E7")


    #C0078
    ChrTalk(
        0x1F,
        (
            "そろそろ店仕舞いなモンだからよ。\x01",
            "見るならチャッチャと見てくれや。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x1F,
        "早く上がって、一杯やりてえんだ。\x02",
    )

    CloseMessageWindow()

    label("loc_2454")

    Jump("loc_2724")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2525")

    #C0080
    ChrTalk(
        0x1F,
        (
            "通商会議だか何だか知らんが、\x01",
            "２大国サマには舐められないように\x01",
            "してもらいてえもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x1F,
        (
            "ヤツラ、こっちがちょっとでも\x01",
            "甘いツラを見せようモンなら、\x01",
            "すぐに付け上がって来やがるからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_2525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E9")

    #C0082
    ChrTalk(
        0x1F,
        (
            "ルバーチェがいなくなって、\x01",
            "裏でのドンパチは減ってるみてえだが……\x01",
            "逆に不気味で仕方ねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x1F,
        (
            "このまま、ずっと何も起こらなきゃ\x01",
            "世話ねえんだが……ユメ見すぎかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2651")

    label("loc_25E9")


    #C0084
    ChrTalk(
        0x1F,
        (
            "せっかく、最近はちょいと\x01",
            "暇になって来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x1F,
        (
            "女神様よ、頼むから\x01",
            "俺に仕事をさせてくれるなよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2651")

    Jump("loc_2724")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26CC")

    #C0086
    ChrTalk(
        0x1F,
        (
            "はあ、今日はまた\x01",
            "随分としけた天気みてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1F,
        (
            "ま、この閉め切った\x01",
            "店内には関係のねえこったが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_26CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2724")

    #C0088
    ChrTalk(
        0x1F,
        (
            "お前らが扱う武器は\x01",
            "一通り用意してある。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x1F,
        "ま、適当に見て行ってくんな。\x02",
    )

    CloseMessageWindow()

    label("loc_2724")

    Jump("loc_13B8")

    label("loc_2729")

    TalkEnd(0x1F)
    Return()

    # Function_6_EC9 end

    def Function_7_272D(): pass

    label("Function_7_272D")

    Call(0, 8)
    Return()

    # Function_7_272D end

    def Function_8_2731(): pass

    label("Function_8_2731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2768")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2768")
    Call(0, 33)
    Return()

    label("loc_2768")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29EF")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x8,
        "おや、あなたたちは警察の。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "確か国防軍とは別で独自に\x01",
            "動いておられると聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00000Fはい、何とかして\x01",
            "この事態を収束させようと\x01",
            "動いている所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#00100Fこちらの方は、\x01",
            "何か不都合等ありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "ええ、ここにはお客様が少々と\x01",
            "スタッフがいるだけですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "他の場所に比べても\x01",
            "落ち着いている方だと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "レストランなので、\x01",
            "食事に困ることもありませんしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど、\x01",
            "確かにその辺は安心ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#00103Fいずれにしても、\x01",
            "今外に出るのは危険です。\x02\x03",

            "#00100F店長さんはこのまま皆さんと\x01",
            "店内に待機していてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        "ええ、かしこまりました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 7)
    TalkEnd(0x8)
    Return()

    label("loc_29EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E65")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A57")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A76")
    OP_AF(0x9)
    Jump("loc_2A78")

    label("loc_2A76")

    OP_AF(0x8)

    label("loc_2A78")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E60")

    label("loc_2A87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A9B")
    Jump("loc_3E60")

    label("loc_2A9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E60")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2B20")

    #C0100
    ChrTalk(
        0x8,
        (
            "今度は是非、沢山の方々と\x01",
            "お越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "またのご来店を\x01",
            "お待ちしておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_2B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C01")

    #C0102
    ChrTalk(
        0x8,
        (
            "セルテオとノンノ、\x01",
            "この２人に任せておけば\x01",
            "ヴァンセットも安泰ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "まあ、ただその前に\x01",
            "クロスベル全体が困難を\x01",
            "乗り越えなければいけませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "なに、皆で力を合わせれば\x01",
            "出来ない事はありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_2C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2CD2")

    #C0105
    ChrTalk(
        0x8,
        (
            "ふむ、しかし警察の方に\x01",
            "声を掛けて頂けると\x01",
            "非常に安心できますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "とにかく、\x01",
            "この場は店長として\x01",
            "責任を持って預かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "皆さんも、外を出歩かれる際は\x01",
            "くれぐれもお気を付けください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDF")

    #C0108
    ChrTalk(
        0x8,
        (
            "ＩＢＣの資産凍結が宣言され……\x01",
            "そして今朝から大陸横断鉄道は\x01",
            "事実上、運行停止状態ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "ふむ、こうなるともはや、\x01",
            "何が起きても不思議ではありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "可能な限り営業は続けるつもりですが……\x01",
            "正直な所、不安な気持ちで一杯です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E8E")

    label("loc_2DDF")


    #C0111
    ChrTalk(
        0x8,
        (
            "ＩＢＣの資産凍結が宣言され……\x01",
            "そして今朝から大陸横断鉄道は\x01",
            "事実上、運行停止状態ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "可能な限り営業は続けるつもりですが……\x01",
            "正直な所、不安な気持ちで一杯です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8E")

    Jump("loc_3E60")

    label("loc_2E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE7")

    #C0113
    ChrTalk(
        0x8,
        (
            "あのような事件もあり、\x01",
            "セルテオとノンノの料理対決は\x01",
            "先送りにしようと思ったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "２人の強い要望もあって、\x01",
            "昨日の閉店後に決行しましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "結果――\x01",
            "どちらも本当に素晴らしい出来で\x01",
            "まさに感涙ものでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "いやはや、後進の成長を\x01",
            "目の当たりにするというのは、\x01",
            "こんなに素晴らしいことなのですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_306C")

    label("loc_2FE7")


    #C0117
    ChrTalk(
        0x8,
        (
            "ふむ、やはりノンノの腕を\x01",
            "このまま眠らせておくのは\x01",
            "勿体無いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "厨房の３人体制……\x01",
            "本格的に検討することに致しましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306C")

    Jump("loc_3E60")

    label("loc_3071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3109")

    #C0119
    ChrTalk(
        0x8,
        (
            "当店をご利用下さるお客様の中には\x01",
            "当然マインツの方もいらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "顔なじみの方も多いので……\x01",
            "本当に心苦しくてたまりません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_3109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_329A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FC")

    #C0121
    ChrTalk(
        0x8,
        (
            "フフ、どうやらセルテオは\x01",
            "随分と考え込んでるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "私もかつてそうでしたが、\x01",
            "答えというものは、悩んで悩んで\x01",
            "悩み抜いた先にこそあるもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "セルテオには、この経験を\x01",
            "良い糧にしてもらいたいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3295")

    label("loc_31FC")


    #C0124
    ChrTalk(
        0x8,
        (
            "私もかつてそうでしたが、\x01",
            "答えというものは、悩んで悩んで\x01",
            "悩み抜いた先にこそあるもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "セルテオには、この経験を\x01",
            "良い糧にしてもらいたいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3295")

    Jump("loc_3E60")

    label("loc_329A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33F0")

    #C0126
    ChrTalk(
        0x8,
        (
            "何でも、西クロスベル街道の方で\x01",
            "列車事故が起こったと聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "よもや落石でもあったのでしょうか。\x01",
            "怪我人も多数出ているみたいですし、\x01",
            "心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33EB")

    #C0128
    ChrTalk(
        0x101,
        (
            "#00008F（ここでグルメガイドの取材が\x01",
            "  出来そうだけど……）\x02\x03",

            "#00003F（今はそれどころじゃない。\x01",
            "  後で忘れずに来るとしよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EB")

    Jump("loc_3E60")

    label("loc_33F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_353C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B9")

    #C0129
    ChrTalk(
        0x8,
        (
            "最近、セルテオの勤務態度が\x01",
            "見違えるほど良くなって来たんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "綺麗な女性のお客さんに対して\x01",
            "過剰反応する事もなくなりましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        "ふむ、何とも結構なことですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3537")

    label("loc_34B9")


    #C0132
    ChrTalk(
        0x8,
        (
            "今まで女性にばかり向かっていた\x01",
            "セルテオの情熱が、次第に\x01",
            "料理に向き始めたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        "ふむ、何とも結構なことですよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3537")

    Jump("loc_3E60")

    label("loc_353C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35B1")

    #C0134
    ChrTalk(
        0x8,
        (
            "ふふ、どうやらセルテオも\x01",
            "ようやく本気になったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        "これは勝負の行方が楽しみですよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_35B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3686")

    #C0136
    ChrTalk(
        0x8,
        (
            "ブラウンがノンノに調理を\x01",
            "任せると聞いて、流石のセルテオも\x01",
            "焦りを感じたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "ふむ……どうやらセルテオに\x01",
            "足りなかったのはライバルのような\x01",
            "存在だったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_373E")

    label("loc_3686")


    #C0138
    ChrTalk(
        0x8,
        (
            "思えば私も、現役時代は\x01",
            "常にブラウンと腕を競い合い、\x01",
            "そして磨き合って来たものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "ふむ……どうやらセルテオに\x01",
            "足りなかったのはライバルのような\x01",
            "存在だったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373E")

    Jump("loc_3E60")

    label("loc_3743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3822")

    #C0140
    ChrTalk(
        0x8,
        (
            "ブラウンから聞いたのですが、\x01",
            "どうやらノンノには料理人の\x01",
            "センスがあるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "当初は簡単な手伝いを\x01",
            "してもらうだけのつもりでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "ふむ、これは\x01",
            "思わぬ収穫かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3892")

    label("loc_3822")


    #C0143
    ChrTalk(
        0x8,
        (
            "ノンノには簡単な手伝いを\x01",
            "してもらうだけのつもりでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "ふむ、これは\x01",
            "思わぬ収穫かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3892")

    Jump("loc_3E60")

    label("loc_3897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F2")

    #C0145
    ChrTalk(
        0x8,
        (
            "あのセルテオに接客を任せるのも\x01",
            "勇気がいったのですが、どうやら存外\x01",
            "うまくやってくれているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "大好きな女性に声を掛ける時も\x01",
            "最低限の節度は守っているようですし、\x01",
            "これなら心配はなさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "ふむ、あとはどうやって\x01",
            "料理人の基本的な心構えを\x01",
            "気付かせるかですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        "やはり、こちらは少々難題ですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AA8")

    label("loc_39F2")


    #C0149
    ChrTalk(
        0x8,
        (
            "セルテオは料理を作る際、\x01",
            "いつもサプライズばかりに拘って\x01",
            "突飛な発想ばかりするんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x8,
        (
            "そのせいかオーソドックスを\x01",
            "極端に嫌うのですが……どうすれば\x01",
            "考えを改めてくれますかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA8")

    Jump("loc_3E60")

    label("loc_3AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B46")

    #C0151
    ChrTalk(
        0x8,
        (
            "仕事を取り上げれば、さぞかし\x01",
            "ショックを受けると思ったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "ふむ、どうやら\x01",
            "アテがはずれてしまったようですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BF0")

    label("loc_3B46")


    #C0153
    ChrTalk(
        0x8,
        (
            "何だかんだでセルテオをはずすと、\x01",
            "ブラウンへの負担が\x01",
            "かなりのものになるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "こんなことを無意味に\x01",
            "続けるわけにも行きませんし……\x01",
            "ふむ、どうしたものですかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF0")

    Jump("loc_3E60")

    label("loc_3BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C90")

    #C0155
    ChrTalk(
        0x8,
        (
            "う～む、どうにもウチのセルテオは\x01",
            "放っておくだけでは伸びないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "ふむ……ここはひとつ\x01",
            "荒療治と行きましょうかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CFC")

    label("loc_3C90")


    #C0157
    ChrTalk(
        0x8,
        (
            "ふむ……ここはひとつ\x01",
            "荒療治と行きましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "これでセルテオが\x01",
            "変わってくれると良いのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFC")

    Jump("loc_3E60")

    label("loc_3D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEB")

    #C0159
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "《ヴァンセット》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "当店では年に数回、時節に合わせて\x01",
            "一部メニューの改定を行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "当店自慢のシェフ・ブラウンが考案した\x01",
            "新作メニューを是非ご賞味下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E60")

    label("loc_3DEB")


    #C0162
    ChrTalk(
        0x8,
        (
            "当店では年に数回、時節に合わせて\x01",
            "一部メニューの改定を行っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        "よろしければ、是非ご賞味下さいませ。\x02",
    )

    CloseMessageWindow()

    label("loc_3E60")

    Jump("loc_29F9")

    label("loc_3E65")

    TalkEnd(0x8)
    Return()

    # Function_8_2731 end

    def Function_9_3E69(): pass

    label("Function_9_3E69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EEE")

    #C0164
    ChrTalk(
        0xFE,
        (
            "セルテオの奴、\x01",
            "なんか急に吹っ切れやがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "へへっ、だがまあいい傾向だな。\x01",
            "なんつうか、俺も一安心だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3FA2")

    #C0166
    ChrTalk(
        0xFE,
        (
            "作った食事を喜んで\x01",
            "食べてもらえる……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "やっぱ、料理人の幸せってのは\x01",
            "これ以外にねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "こんな状況でも\x01",
            "食事を振舞う客がいるだけで\x01",
            "何か力が湧いてくるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402E")

    #C0169
    ChrTalk(
        0xFE,
        "今朝から鉄道便が完全にストップしてな。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "輸入食材の代わりをどうするか……\x01",
            "こいつがウチの当面の課題だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40CD")

    label("loc_402E")


    #C0171
    ChrTalk(
        0xFE,
        (
            "何だかキナ臭い感じがするが……\x01",
            "今のところ、俺たち料理人に\x01",
            "やれることは一つしかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "輸入食材の代わりをどうするか……\x01",
            "こいつがウチの当面の課題だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40CD")

    Jump("loc_4DF6")

    label("loc_40D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_42BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4204")

    #C0173
    ChrTalk(
        0xFE,
        (
            "セルテオの奴、どうやら\x01",
            "一皮剥けたみたいで安心したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "あいつの作ったパスタソースは\x01",
            "トマトベースに魚介の風味を\x01",
            "効かせたモンだったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "他にも隠し味に、数種類のスパイスを\x01",
            "絶妙に仕込んでいてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "味は抜群だったし、それなりに\x01",
            "新鮮味もあって良い出来だったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42B6")

    label("loc_4204")


    #C0177
    ChrTalk(
        0xFE,
        (
            "以前のセルテオは、\x01",
            "定番とされる食材の組み合わせを\x01",
            "とにかく毛嫌いする傾向があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "そのせいで逆に視野が\x01",
            "狭くなっちまってたんだが……\x01",
            "どうやら少しは成長したようだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42B6")

    Jump("loc_4DF6")

    label("loc_42BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4351")

    #C0179
    ChrTalk(
        0xFE,
        (
            "ふむ、心なしか今日はいつもより\x01",
            "少し客足が鈍いみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "ま……昨日の今日であんな事件が\x01",
            "起こっちまったんだから仕方ねえよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43CF")

    #C0181
    ChrTalk(
        0xFE,
        "それにしても料理対決、か。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "ノンノもセルテオもそれぞれ\x01",
            "真剣に取り組んでいるみたいで、\x01",
            "結構なこったぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_43CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_44E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445B")

    #C0183
    ChrTalk(
        0xFE,
        "さっきから救急車の音がうるせえな。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "おかげで揚げ物の音が聞こえねえモンで、\x01",
            "少しばかり焦がしちまったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44DB")

    label("loc_445B")


    #C0185
    ChrTalk(
        0xFE,
        (
            "おっと、焦がしたフライは\x01",
            "客には出さねえから安心してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "あとで、セルテオの奴に\x01",
            "まかないで食わせるつもりだからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44DB")

    Jump("loc_4DF6")

    label("loc_44E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4578")

    #C0187
    ChrTalk(
        0xFE,
        (
            "ふむ、ノンノの手際も最初に\x01",
            "比べりゃ随分良くなったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "こりゃあホール係を新たに雇って\x01",
            "厨房を３人体制にするのもアリかもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_476C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EF")

    #C0189
    ChrTalk(
        0xFE,
        "へへっ、ホイストフもよくやるぜ。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "何でも、ノンノの成果に焦る\x01",
            "セルテオの気持ちを利用して\x01",
            "料理人として成長させるっつってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "何と、コックの座を賭けて\x01",
            "１週間後に２人に\x01",
            "料理対決をさせるっつうんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "ま、そんなのは口実で、\x01",
            "やる気さえあれば本当はどっちにも\x01",
            "コックをやって欲しいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "おっと、今の話はセルテオには内緒だぜ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4767")

    label("loc_46EF")


    #C0194
    ChrTalk(
        0xFE,
        "へへっ、ホイストフもよくやるぜ。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "だがまあ、セルテオの奴も\x01",
            "やる気を出しているみたいだし、\x01",
            "名案だとは思うがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4767")

    Jump("loc_4DF6")

    label("loc_476C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_481B")

    #C0196
    ChrTalk(
        0xFE,
        (
            "ははっ、ノンノの奴、\x01",
            "流石に戸惑っているみたいだが、\x01",
            "何だかんだ結構やる気みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "いいよなあ、初々しいあの感じ。\x01",
            "若かりし頃の修行時代を思い出すぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_481B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4871")

    #C0198
    ChrTalk(
        0xFE,
        (
            "よしっ、いっそのこと\x01",
            "明日は思い切って\x01",
            "ノンノに調理を任せてみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4940")

    #C0199
    ChrTalk(
        0xFE,
        (
            "さてさて、今朝ノンノに\x01",
            "頼んでおいたブイヨンの調子はっと。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "……驚いた、こいつは予想以上だな。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "家で料理はしてるって聞いたが……\x01",
            "これならもっと任せてみてもいいかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49CE")

    label("loc_4940")


    #C0202
    ChrTalk(
        0xFE,
        (
            "ふむ、このブイヨン。\x01",
            "しっかりと素材の旨みを引き出せてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "家で料理はしてるって聞いたが……\x01",
            "これならもっと任せてみてもいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CE")

    Jump("loc_4DF6")

    label("loc_49D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB0")

    #C0204
    ChrTalk(
        0xFE,
        (
            "ふうむ、しかしホイストフも\x01",
            "思い切ったことをするよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "まさか現場から遠ざけちまうとは\x01",
            "思わなかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "ただまあ、確かにあいつの場合、\x01",
            "そのくらいの事をしないと\x01",
            "変われないかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B24")

    label("loc_4AB0")


    #C0207
    ChrTalk(
        0xFE,
        (
            "それにしても、セルテオの奴は\x01",
            "まったく堪えていないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "あいつ、今の自分の立場を\x01",
            "分かっているのか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B24")

    Jump("loc_4DF6")

    label("loc_4B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C23")

    #C0209
    ChrTalk(
        0xFE,
        (
            "料理でも何でも、まずは基本を\x01",
            "押さえねえことにはどうしようもねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "例えば絵の世界でも、有名な抽象画家は\x01",
            "そりゃあ見事な写実画を描くモンなんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "セルテオの奴にもそろそろ\x01",
            "その辺りの事を分かって欲しいんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4CAF")

    label("loc_4C23")


    #C0212
    ChrTalk(
        0xFE,
        (
            "料理でも何でも、まずは基本を\x01",
            "押さえねえことにはどうしようもねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "セルテオの奴にもそろそろ\x01",
            "その辺りの事を分かって欲しいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CAF")

    Jump("loc_4DF6")

    label("loc_4CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D84")

    #C0214
    ChrTalk(
        0xFE,
        (
            "以前セルテオの奴に課した\x01",
            "新作メニュー作りは\x01",
            "結局失敗に終わったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "あいつは決して筋は悪くないんだが……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "今の調子じゃあ、一人前になれるのは\x01",
            "まだまだ当分先の話だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4DF6")

    label("loc_4D84")


    #C0217
    ChrTalk(
        0xFE,
        (
            "セルテオの奴は\x01",
            "決して筋は悪くないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "今の調子じゃあ、一人前になれるのは\x01",
            "まだまだ当分先の話だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF6")

    TalkEnd(0xFE)
    Return()

    # Function_9_3E69 end

    def Function_10_4DFA(): pass

    label("Function_10_4DFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE7")

    #C0219
    ChrTalk(
        0xFE,
        (
            "街がこの先どうなろうが、\x01",
            "料理人に出来るのはただ一つ……\x01",
            "うまい飯を提供することだけだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "今後は食材も限られるだろうけど、\x01",
            "そこは工夫で乗り越えられるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "よ～し、今日もバリバリ頑張るぜ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F50")

    label("loc_4EE7")


    #C0222
    ChrTalk(
        0xFE,
        (
            "料理人に出来るのはただ一つ……\x01",
            "うまい飯を提供することだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "よ～し、今日もバリバリ頑張るぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_4F50")

    Jump("loc_60B3")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_50FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506F")

    #C0224
    ChrTalk(
        0xFE,
        (
            "こんな時でないと気付けない\x01",
            "自分が情けないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "ブラウンさんの言ってることが\x01",
            "何だか本当によく分かるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "そうなんだよな、料理人ってのは\x01",
            "お客さんあってこそ……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "これまで自己満足の料理ばかり\x01",
            "作ってきた自分が\x01",
            "つくづく恥ずかしく思えるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50FA")

    label("loc_506F")


    #C0228
    ChrTalk(
        0xFE,
        (
            "そうなんだよな、料理人ってのは\x01",
            "お客さんあってこそ……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "これまで自己満足の料理ばかり\x01",
            "作ってきた自分が\x01",
            "つくづく恥ずかしく思えるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FA")

    Jump("loc_60B3")

    label("loc_50FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5197")

    #C0230
    ChrTalk(
        0xFE,
        (
            "ディーター大統領の演説、\x01",
            "さすがに凄ぇ迫力があったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "なんつうか、あの人の言葉を聞いてると\x01",
            "勇気と誇りをもらえる気分になるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_5197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5248")

    #C0232
    ChrTalk(
        0xFE,
        "ったく、店長も人が悪いよな。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "始めから勝敗を決める\x01",
            "つもりはなかった、なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "へっ、これじゃ何のために\x01",
            "苦心したのか分からないっつの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52D5")

    label("loc_5248")


    #C0235
    ChrTalk(
        0xFE,
        (
            "にしても……\x01",
            "最近、色々と物騒すぎるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "だが、その意味で考えると、\x01",
            "今こうやって普通に働けてることが\x01",
            "すげえ幸せなことに感じるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D5")

    Jump("loc_60B3")

    label("loc_52DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5366")

    #C0237
    ChrTalk(
        0xFE,
        (
            "占領事件だなんて……\x01",
            "恐ろしいけど、全く馬鹿げた話だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "暴力なんかで人を支配して\x01",
            "一体何が楽しいんだ、って話だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_5366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5450")

    #C0239
    ChrTalk(
        0xFE,
        (
            "くそっ、方針すら定まらないまま\x01",
            "ただただ時間だけが過ぎちまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "早いとこ、パスタに絡める\x01",
            "ソースの方向性くらいは固めねえと。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "トマトベースか、クリームベースか、\x01",
            "それとも未知のソースにするか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54BE")

    label("loc_5450")


    #C0242
    ChrTalk(
        0xFE,
        (
            "だあっ、だから\x01",
            "未知のソースって一体何だよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "はあ……何となく、\x01",
            "自分の欠点が見えてきた気がするな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54BE")

    Jump("loc_60B3")

    label("loc_54C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_54F9")

    #C0244
    ChrTalk(
        0xFE,
        "ん？　何だかやけに外が騒がしいな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_566D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FC")

    #C0245
    ChrTalk(
        0xFE,
        (
            "とにかく美味いって言っても、\x01",
            "料理である以上、見た目は重要だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "ってか、今回の対決テーマだと\x01",
            "別に真新しさは重要じゃなさそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "とりあえず、基本は\x01",
            "定番のメニューにしておいて\x01",
            "アレンジを加える方向で考えるかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5668")

    label("loc_55FC")


    #C0248
    ChrTalk(
        0xFE,
        (
            "はぁ、しかしどうにも\x01",
            "定番って言葉は嫌いなんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "だって、定番なら\x01",
            "うまいのは当たり前だろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5668")

    Jump("loc_60B3")

    label("loc_566D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5701")

    #C0250
    ChrTalk(
        0xFE,
        (
            "……まさかノンノと\x01",
            "料理対決をすることになるなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "とにかく美味いパスタ料理、か……\x01",
            "まずは何を方針にするかが悩み所だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_5701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_584D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57CF")

    #C0252
    ChrTalk(
        0xFE,
        (
            "ノ、ノンノが調理をするって、\x01",
            "何だか展開が早すぎねえか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "っていうか、まさか俺って\x01",
            "このまま干されちまうんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "って、いやいやいや、\x01",
            "そんなのありえねえからっ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5848")

    label("loc_57CF")


    #C0255
    ChrTalk(
        0xFE,
        (
            "ノンノがいくら料理ができるっつっても\x01",
            "客に出す料理を作るなんて早すぎだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        "っていうか、俺の立場はどうなるんだ？\x02",
    )

    CloseMessageWindow()

    label("loc_5848")

    Jump("loc_60B3")

    label("loc_584D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58FE")

    #C0257
    ChrTalk(
        0xFE,
        (
            "全然気にしてなかったけど、\x01",
            "ノンノの奴、いつの間にか仕込みまで\x01",
            "任されるようになってたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "まさか、このままコックに\x01",
            "なっちまうってことはねえよなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_58FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59CD")

    #C0259
    ChrTalk(
        0xFE,
        (
            "いらっしゃい、店内でお召し上がりなら\x01",
            "どこでも空いたテーブルに付いてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "ご希望だったら、今なら\x01",
            "予約優先の２階席も案内できるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        "気軽に声を掛けてくれよなっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A54")

    label("loc_59CD")


    #C0262
    ChrTalk(
        0xFE,
        (
            "いや～、接客って\x01",
            "こんなに楽しいものなんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "お客さん……特に美人の\x01",
            "女性客の笑顔ってのは\x01",
            "何物にも替え難いエネルギー源だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A54")

    Jump("loc_60B3")

    label("loc_5A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C12")

    #C0264
    ChrTalk(
        0xFE,
        (
            "店長から、しばらく\x01",
            "ウェイターをしろって言われたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "どういうつもりかは知らないけど、\x01",
            "たまにはこういう仕事もいいもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "女性客は見放題だし、\x01",
            "おまけに堂々とナンパできるからね。\x02",
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
            "#00006F（お客さんをナンパは\x01",
            "  流石にまずいような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        (
            "#00103F（ええ、それに見られるのも\x01",
            "  落ち着かないわ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5C9E")

    label("loc_5C12")


    #C0269
    ChrTalk(
        0xFE,
        (
            "店長もどういうつもりかは知らないけど、\x01",
            "たまにはウェイターもいいもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "女性客は見放題だし、\x01",
            "おまけに堂々とナンパできるからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C9E")

    Jump("loc_60B3")

    label("loc_5CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5DDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5B")

    #C0271
    ChrTalk(
        0xFE,
        (
            "料理ってのは芸術だ。\x01",
            "何といっても独創性が大切なのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "次また新メニューの話が来た時は、\x01",
            "きっと世間をアッと驚かせる\x01",
            "究極のメニューを創造してやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DD5")

    label("loc_5D5B")


    #C0273
    ChrTalk(
        0xFE,
        (
            "ちなみに今のお客さんは……\x01",
            "入口側のテーブルに女子２名か。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "へへっ、待っててね～。\x01",
            "今、料理を運びますからねっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD5")

    Jump("loc_60B3")

    label("loc_5DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F09")

    #C0275
    ChrTalk(
        0xFE,
        (
            "う～ん、俺の新作メニューは\x01",
            "一体どこがいけなかったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "味と見た目はちゃんとまとめたし、\x01",
            "何より、あのギュリッとした食感が\x01",
            "画期的だったと思うんだけどな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#00012F（『ギュリッ』……？）\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#00106F（よく分からないけど、\x01",
            "  食べてみたいとは思わないわね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_60B3")

    label("loc_5F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6066")

    #C0279
    ChrTalk(
        0xFE,
        (
            "『魔獣目玉のドロ沼地獄煮込み』……\x01",
            "新境地を拓けたと思ったんだけどな～。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F86")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5F86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FAC")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5FAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FD2")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5FD2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FF8")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5FF8")

    Sleep(1000)

    #C0280
    ChrTalk(
        0x109,
        "#10105F（す、凄いネーミングですね。）\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x105,
        (
            "#10304F（フフ、とんだ\x01",
            "  ゲテモノ料理みたいだね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_60B3")

    label("loc_6066")


    #C0282
    ChrTalk(
        0xFE,
        (
            "『魔獣目玉のドロ沼地獄煮込み』……\x01",
            "新境地を拓けたと思ったんだけどな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B3")

    TalkEnd(0xFE)
    Return()

    # Function_10_4DFA end

    def Function_11_60B7(): pass

    label("Function_11_60B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6140")

    #C0283
    ChrTalk(
        0xFE,
        (
            "ふふ、セルテオさん。\x01",
            "何だか気合いが入ってますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "不安だらけの状況ですけど……\x01",
            "ちょっぴり元気をもらいました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6206")

    #C0285
    ChrTalk(
        0xFE,
        (
            "今、街で起きている異常事態……\x01",
            "これは政府自らが\x01",
            "起こした出来事なんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "その辺りの事情を、もっと早く詳しく\x01",
            "教えて頂ければ、もう少し\x01",
            "混乱も抑えられたはずなんですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_629A")

    #C0287
    ChrTalk(
        0xFE,
        (
            "大統領演説は聞いていて\x01",
            "とても素晴らしいと思ったんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "店長の言う通り、正直不安な\x01",
            "要素が多すぎて困惑してしまいますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_629A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6372")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62CC")
    Call(0, 43)
    Return()

    label("loc_62CC")


    #C0289
    ChrTalk(
        0xFE,
        (
            "１ヶ月ちょっとの間でしたけど、\x01",
            "厨房に立てて嬉しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "店長にも言われているんですけど、\x01",
            "私、この際一度本気で料理人を\x01",
            "目指してみようかと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_63CA")

    #C0291
    ChrTalk(
        0xFE,
        "マインツの人たち……心配ですよね。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "お腹は空いていないかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_63CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647C")

    #C0293
    ChrTalk(
        0xFE,
        (
            "お料理対決用のレシピ、\x01",
            "何やらセルテオさんは色々と\x01",
            "考えているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "私は単純に、普段から作り慣れている\x01",
            "得意料理をぶつけるつもりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64FC")

    label("loc_647C")


    #C0295
    ChrTalk(
        0xFE,
        (
            "私、パスタだとカルボナーラが得意で\x01",
            "よく家族に作って上げるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "なので、料理対決では\x01",
            "それを振舞おうと思っています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64FC")

    Jump("loc_6ED3")

    label("loc_6501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_656A")

    #C0297
    ChrTalk(
        0xFE,
        (
            "サイレンの音って、\x01",
            "物凄くよく通りますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        "厨房にいても、はっきり聞こえました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_656A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6601")

    #C0299
    ChrTalk(
        0xFE,
        "ふんふんふ～ん♪\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "バジルにペッパー、それに\x01",
            "お塩を少々振りかけまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "うん、これで\x01",
            "お肉の下味はバッチリね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6662")

    label("loc_6601")


    #C0302
    ChrTalk(
        0xFE,
        "ふんふんふ～ん♪\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "次にこれを３０分ほど寝かせまして……\x01",
            "その間にお野菜を切っちゃいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6662")

    Jump("loc_6ED3")

    label("loc_6667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BC")

    #C0304
    ChrTalk(
        0xFE,
        (
            "本当はそろそろホールの方に\x01",
            "戻る予定だったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "店長に頼まれて、もうしばらく\x01",
            "厨房で働くことになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "おまけにセルテオさんの\x01",
            "今後のためにということで、\x01",
            "料理対決に付き合うことになって……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "ふふ、セルテオさんを\x01",
            "騙しているみたいで悪いんですけど、\x01",
            "楽しそうだから引き受けちゃいました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6861")

    label("loc_67BC")


    #C0308
    ChrTalk(
        0xFE,
        (
            "それにしても、元々は家事の\x01",
            "延長でやっていた料理なんですが、\x01",
            "こうして厨房に立てるのは楽しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "ふふ、こうなったら\x01",
            "本気で料理人を目指してみようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6861")

    Jump("loc_6ED3")

    label("loc_6866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6933")

    #C0310
    ChrTalk(
        0xFE,
        (
            "今朝、突然ブラウンさんに頼まれて\x01",
            "調理をやってみる事になったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "本当に私なんかでいいのかしら。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "も、もちろん、期待には\x01",
            "全力でお応えするつもりですけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_698C")

    label("loc_6933")


    #C0313
    ChrTalk(
        0xFE,
        (
            "えっと、まずは\x01",
            "材料に下味を付けて、と……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "うう、調理なんて流石に緊張しますね。\x02",
    )

    CloseMessageWindow()

    label("loc_698C")

    Jump("loc_6ED3")

    label("loc_6991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6A0B")

    #C0315
    ChrTalk(
        0xFE,
        (
            "この仕込みを終えたら\x01",
            "次はお皿を洗って、と。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "ふう……やっぱりウチの\x01",
            "ディナータイムは忙しいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AAE")

    #C0317
    ChrTalk(
        0xFE,
        (
            "えっと、このお野菜は\x01",
            "火が通りにくいから\x01",
            "隠し包丁を入れた方が良いわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "サクッサクッ、スーッ……\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        "うん、これでよしっと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6AF4")

    label("loc_6AAE")


    #C0320
    ChrTalk(
        0xFE,
        "トントントントンッ……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        "うん、みじん切りはこんなものかしら。\x02",
    )

    CloseMessageWindow()

    label("loc_6AF4")

    Jump("loc_6ED3")

    label("loc_6AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6B9C")

    #C0322
    ChrTalk(
        0xFE,
        (
            "セルテオさんの代わりに\x01",
            "少し厨房を手伝うことになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "といっても基本はお皿洗いで、\x01",
            "あとは簡単な仕込みのお手伝いが\x01",
            "いい所ですけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7E")

    #C0324
    ChrTalk(
        0xFE,
        (
            "セルテオさん、相変わらず\x01",
            "厨房から出てきてはテーブル席の\x01",
            "様子を窺っているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "今日もまた、頼まれてもいないのに\x01",
            "自分で料理を運ぶつもりかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "ふう、あの人も懲りないんだから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D00")

    label("loc_6C7E")


    #C0327
    ChrTalk(
        0xFE,
        (
            "セルテオさん、相変わらず\x01",
            "厨房から出てきてはテーブル席の\x01",
            "様子を窺っているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        "ふう、あの人も懲りないんだから。\x02",
    )

    CloseMessageWindow()

    label("loc_6D00")

    Jump("loc_6ED3")

    label("loc_6D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E11")

    #C0329
    ChrTalk(
        0xFE,
        (
            "奥の席にいるフロテさんは\x01",
            "このお店の常連さんなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "いつも開店と同時にお店に来て\x01",
            "そのまま一日中、居座ることも\x01",
            "珍しくないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "混雑時には席を外してくれたり、\x01",
            "たまに追加注文してくれたり、\x01",
            "結構気を遣ってくれるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6ED3")

    label("loc_6E11")


    #C0332
    ChrTalk(
        0xFE,
        (
            "フロテさんはいつも開店と同時に\x01",
            "お店に来て、そのまま一日中\x01",
            "居座ることも珍しくないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "混雑時には席を外してくれたり、\x01",
            "たまに追加注文してくれたり、\x01",
            "結構気を遣ってくれるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED3")

    TalkEnd(0xFE)
    Return()

    # Function_11_60B7 end

    def Function_12_6ED7(): pass

    label("Function_12_6ED7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_701A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F8E")

    #C0334
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "青白い大樹、か……\x01",
            "最近何が現実で何が夢なのか、\x01",
            "少し自信がなくなって来たわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "……もう少し\x01",
            "カフェインを取っておこうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7015")

    label("loc_6F8E")


    #C0337
    ChrTalk(
        0xFE,
        (
            "青白い大樹、か……\x01",
            "最近何が現実で何が夢なのか、\x01",
            "少し自信がなくなって来たわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "……もう少し\x01",
            "カフェインを取っておこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7015")

    Jump("loc_7FDB")

    label("loc_701A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_71DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7137")

    #C0339
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "……トイレに行っている間に\x01",
            "モヤが出てきて外に出られないって\x01",
            "どういうこと？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "というより、どうして\x01",
            "あんな人型の兵器みたいなのが\x01",
            "街をうろついてるわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "たとえ２大国から\x01",
            "街を守るためなんだとしても、\x01",
            "ちゃんとした説明を要求するわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_71DA")

    label("loc_7137")


    #C0343
    ChrTalk(
        0xFE,
        (
            "《神機》とかいう兵器にしても\x01",
            "街を覆っていた結界にしても、\x01",
            "ちゃんとした説明を要求するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "これじゃ街を守るどころか、\x01",
            "むしろ危険にさらしてるんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71DA")

    Jump("loc_7FDB")

    label("loc_71DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72DD")

    #C0345
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "クロスベル独立国にディーター大統領、\x01",
            "そしてアリオス国防長官、か。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "名前や肩書きだけは立派みたいだけど、\x01",
            "ちゃんと私たちを守ってくれるのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "……見せ掛けだけじゃ、\x01",
            "本当に洒落にならないわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_738C")

    label("loc_72DD")


    #C0349
    ChrTalk(
        0xFE,
        (
            "独立国とか大統領とか国防長官とか……\x01",
            "名前や肩書きだけは立派みたいだけど、\x01",
            "ちゃんと私たちを守ってくれるのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "……見せ掛けだけじゃ、\x01",
            "本当に洒落にならないわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_738C")

    Jump("loc_7FDB")

    label("loc_7391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_756D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7493")

    #C0351
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "なんか先日の襲撃事件を受けて\x01",
            "独立賛成派が盛り上がってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "ま、気持ちは判らないでもないけど、\x01",
            "もう少し理知的に議論できないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "感情論は身を滅ぼす……\x01",
            "って、誰かが言ってた気がするしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7568")

    label("loc_7493")


    #C0355
    ChrTalk(
        0xFE,
        (
            "なんか先日の襲撃事件を受けて\x01",
            "独立賛成派が盛り上がってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "ま、気持ちは判らないでもないけど、\x01",
            "もう少し理知的に議論できないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "感情論は身を滅ぼす……\x01",
            "って、誰かが言ってた気がするしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7568")

    Jump("loc_7FDB")

    label("loc_756D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7622")

    #C0358
    ChrTalk(
        0xFE,
        (
            "マインツに謎の武装集団……\x01",
            "既に一部で噂になってるけど、\x01",
            "やっぱり帝国の陰謀なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "『助ける代わりに軍の駐留を認めろ』\x01",
            "……笑えないけどありそうな主張ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_7622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_774D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_770D")

    #C0360
    ChrTalk(
        0xFE,
        (
            "今日は朝から、市民会館の方で\x01",
            "国家独立がテーマの市民フォーラムが\x01",
            "開催されているらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "別にフォーラムなんか参加しなくても\x01",
            "独立の要点は分かっているつもりだけど、\x01",
            "少しだけ顔を出してみようかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7748")

    label("loc_770D")


    #C0362
    ChrTalk(
        0xFE,
        (
            "市民フォーラムか……\x01",
            "少しだけ顔を出してみようかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7748")

    Jump("loc_7FDB")

    label("loc_774D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_77A3")

    #C0363
    ChrTalk(
        0xFE,
        "何だか外が騒がしいわね。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        "落ち着いてコーヒーも飲めやしないわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_77A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_78EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7873")

    #C0365
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのリニューアル版って\x01",
            "確か明後日が公開日だったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "私もチケット狙ってたのに……\x01",
            "向こう２ヶ月分があっという間に\x01",
            "完売ってどういうことよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_78E5")

    label("loc_7873")


    #C0368
    ChrTalk(
        0xFE,
        (
            "ふ、ふん……別に\x01",
            "アルカンシェルなんか観なくても\x01",
            "人間死なないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        "うぅ、でも死ぬほど観たかったわ。\x02",
    )

    CloseMessageWindow()

    label("loc_78E5")

    Jump("loc_7FDB")

    label("loc_78EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7978")

    #C0370
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "国家独立ねえ。\x01",
            "単純に事が運べば世話はないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        "私はとにかく安全保障の面が心配よ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7A23")

    label("loc_7978")


    #C0373
    ChrTalk(
        0xFE,
        (
            "個人的には、帝国と共和国に\x01",
            "安全保障を委ねることも\x01",
            "決して悪い事だとは思わないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "まあ、これまでの歴史も歴史だし、\x01",
            "そう簡単にうまく行かないのが現実よね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A23")

    Jump("loc_7FDB")

    label("loc_7A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC4")

    #C0375
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        "それにしても、街が物々しいわね。\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "あんな風に警察官に居られたんじゃ、\x01",
            "おちおち散歩もできないじゃない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7B1D")

    label("loc_7AC4")


    #C0378
    ChrTalk(
        0xFE,
        "その点、お店の中は落ち着くわ。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "さてと、今日も\x01",
            "有意義な読書タイムを過ごすわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B1D")

    Jump("loc_7FDB")

    label("loc_7B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7BC6")

    #C0380
    ChrTalk(
        0xFE,
        (
            "ふう、今日はついつい読書に熱中して\x01",
            "久しぶりに日が暮れるまで居ちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "流石にお店の人にも悪いから、\x01",
            "このまま夕飯でも食べて行こうかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_7BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CA7")

    #C0382
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "除幕式なんてどうせ近くで\x01",
            "見れないのに、みんなわざわざ\x01",
            "外に出てご苦労なことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "私はここでコーヒーを片手に\x01",
            "次のクロスベルタイムズ誌面で、\x01",
            "優雅に拝見させてもらうつもりよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D5B")

    label("loc_7CA7")


    #C0385
    ChrTalk(
        0xFE,
        (
            "除幕式なんてどうせ近くで\x01",
            "見れないのに、みんなわざわざ\x01",
            "外に出てご苦労なことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "私はここでコーヒーを片手に\x01",
            "次のクロスベルタイムズ誌面で、\x01",
            "優雅に拝見させてもらうつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D5B")

    Jump("loc_7FDB")

    label("loc_7D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DC9")

    #C0387
    ChrTalk(
        0xFE,
        (
            "どうして今日は、あのうざいコックが\x01",
            "注文を取っているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xFE,
        "理解に苦しむわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_7DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E74")

    #C0389
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "雨の日の店内は、いつもとは\x01",
            "また違う趣きがあって素敵ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "店の喧騒と雨音が交じり合って\x01",
            "最高のＢＧＭって感じがするわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7EF2")

    label("loc_7E74")


    #C0392
    ChrTalk(
        0xFE,
        (
            "雨の日の店内は、いつもとは\x01",
            "また違う趣きがあって素敵ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "店の喧騒と雨音が交じり合って\x01",
            "最高のＢＧＭって感じがするわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EF2")

    Jump("loc_7FDB")

    label("loc_7EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9A")

    #C0394
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        (
            "ふう、やっぱり\x01",
            "このお店は読書するのに最適ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "程好い喧騒が雑念を、そして\x01",
            "コーヒーが眠気を払ってくれるのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7FDB")

    label("loc_7F9A")


    #C0397
    ChrTalk(
        0xFE,
        (
            "さあ、今日も粘りに粘って\x01",
            "図書館で借りた本を読破するわよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FDB")

    TalkEnd(0xFE)
    Return()

    # Function_12_6ED7 end

    def Function_13_7FDF(): pass

    label("Function_13_7FDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8052")

    #C0398
    ChrTalk(
        0xFE,
        (
            "や～ん、雨が降るだなんて\x01",
            "聞いてないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "せっかくの旅行なのに\x01",
            "どうしてくれるのよぉ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_809C")

    label("loc_8052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_809C")

    #C0400
    ChrTalk(
        0xFE,
        (
            "だね～、それに値段も高すぎないし。\x01",
            "通いたくなっちゃうかも。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809C")

    TalkEnd(0xFE)
    Return()

    # Function_13_7FDF end

    def Function_14_80A0(): pass

    label("Function_14_80A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8125")

    #C0401
    ChrTalk(
        0xFE,
        (
            "はいはい、分かったから\x01",
            "愚痴に私を巻き込まないでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "雨なら雨で屋内で楽しむ方法を\x01",
            "考えればいいだけでしょ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818C")

    label("loc_8125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_818C")

    #C0403
    ChrTalk(
        0xFE,
        (
            "このお店、\x01",
            "割とフランクに入れるのに\x01",
            "料理はかなり本格的なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "ふふ、気に入ったわ。\x02",
    )

    CloseMessageWindow()

    label("loc_818C")

    TalkEnd(0xFE)
    Return()

    # Function_14_80A0 end

    def Function_15_8190(): pass

    label("Function_15_8190")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_81C1")

    #C0405
    ChrTalk(
        0xFE,
        "ふふ、あなたおいしいわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8229")

    label("loc_81C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8229")

    #C0406
    ChrTalk(
        0xFE,
        (
            "あなた、私のためにわざわざ\x01",
            "席を予約してくれてありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "いつも感謝しているわよ。\x02",
    )

    CloseMessageWindow()

    label("loc_8229")

    TalkEnd(0xFE)
    Return()

    # Function_15_8190 end

    def Function_16_822D(): pass

    label("Function_16_822D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8289")

    #C0408
    ChrTalk(
        0xFE,
        "わはは、そうじゃな。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "まあ、もっとも\x01",
            "お前の手料理には負けるがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EE")

    label("loc_8289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_82EE")

    #C0410
    ChrTalk(
        0xFE,
        "わはは、なんのなんの。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        (
            "こちらこそ、\x01",
            "いつも家のことをしてくれて\x01",
            "感謝しているぞい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82EE")

    TalkEnd(0xFE)
    Return()

    # Function_16_822D end

    def Function_17_82F2(): pass

    label("Function_17_82F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8360")

    #C0412
    ChrTalk(
        0xFE,
        (
            "メニューを開いてパッと\x01",
            "指差したヤツ、それを頼むぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        "よ～し、まずは目をつむって……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8413")

    label("loc_8360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_836E")
    Jump("loc_8413")

    label("loc_836E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_83D1")

    #C0414
    ChrTalk(
        0xFE,
        "よしっ、今日は魚にするぞ！\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "あれ、でも今日は\x01",
            "こちらのセットがお得なのか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8413")

    label("loc_83D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8413")

    #C0416
    ChrTalk(
        0xFE,
        (
            "えー、何にしようかな。\x01",
            "う～む、どれも食べたいが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8413")

    TalkEnd(0xFE)
    Return()

    # Function_17_82F2 end

    def Function_18_8417(): pass

    label("Function_18_8417")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8459")

    #C0417
    ChrTalk(
        0xFE,
        (
            "あなた……\x01",
            "どうでもいいから早くして下さる？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84E3")

    label("loc_8459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8467")
    Jump("loc_84E3")

    label("loc_8467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_849D")

    #C0418
    ChrTalk(
        0xFE,
        "はぁ、あなたって本当に優柔不断ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84E3")

    label("loc_849D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_84E3")

    #C0419
    ChrTalk(
        0xFE,
        (
            "あなた……早くして下さる？\x01",
            "私はもう決めたのですけれど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84E3")

    TalkEnd(0xFE)
    Return()

    # Function_18_8417 end

    def Function_19_84E7(): pass

    label("Function_19_84E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8547")

    #C0420
    ChrTalk(
        0xFE,
        (
            "えー、初日と\x01",
            "言ってることが違うじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        "ぶーぶー、かっこ悪いぞぉ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E7")

    label("loc_8547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8555")
    Jump("loc_85E7")

    label("loc_8555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_85AD")

    #C0422
    ChrTalk(
        0xFE,
        "モグモグ……あー、しあわせ♪\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        "やっぱり、旅行の醍醐味は食事よね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E7")

    label("loc_85AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_85E7")

    #C0424
    ChrTalk(
        0xFE,
        (
            "ふふ、やったぁ♪\x01",
            "流石は愛すべきダーリンね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E7")

    TalkEnd(0xFE)
    Return()

    # Function_19_84E7 end

    def Function_20_85EB(): pass

    label("Function_20_85EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_867D")

    #C0425
    ChrTalk(
        0xFE,
        (
            "え、えっとですね。\x01",
            "非常に言いにくいんだけど\x01",
            "旅費が結構カツカツでして……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "だから、なるべく\x01",
            "リーズナブルなメニューを……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_877D")

    label("loc_867D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_868B")
    Jump("loc_877D")

    label("loc_868B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8717")

    #C0427
    ChrTalk(
        0xFE,
        (
            "う～ん、しかしまた\x01",
            "高価なメニューを次から次へと……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "ま、まあ、せっかくの旅行だし。\x01",
            "細かいことは気にしないでおこう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_877D")

    label("loc_8717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_877D")

    #C0429
    ChrTalk(
        0xFE,
        (
            "さあ、好きな物を好きなだけ\x01",
            "じゃんじゃん頼んでくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        "せっかくの旅行なんだからね。\x02",
    )

    CloseMessageWindow()

    label("loc_877D")

    TalkEnd(0xFE)
    Return()

    # Function_20_85EB end

    def Function_21_8781(): pass

    label("Function_21_8781")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_87CD")

    #C0431
    ChrTalk(
        0xFE,
        (
            "う～ん、まさか旅行中に\x01",
            "こんな事件が起こるなんてなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_87CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8827")

    #C0432
    ChrTalk(
        0xFE,
        (
            "う～ん、今日は\x01",
            "街道方面へ出かけるのは諦めて\x01",
            "街で買い物でもするかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_8827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_887B")

    #C0433
    ChrTalk(
        0xFE,
        (
            "救急車かぁ、\x01",
            "何台か通ったみたいだから\x01",
            "病人ではなさそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_887B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_88FD")

    #C0434
    ChrTalk(
        0xFE,
        (
            "さてと、今日も\x01",
            "色んな場所を見て回るぞ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "まずは感光クオーツを補充しに、\x01",
            "オーバルストアに寄っていくかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_88FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8994")

    #C0436
    ChrTalk(
        0xFE,
        (
            "最近のクロスベルの治安を考えると、\x01",
            "旅行はどうかとも思ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "やっぱり来て正解だったよ。\x01",
            "彼女もすごく喜んでくれているしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8994")

    TalkEnd(0xFE)
    Return()

    # Function_21_8781 end

    def Function_22_8998(): pass

    label("Function_22_8998")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8A2B")

    #C0438
    ChrTalk(
        0xFE,
        (
            "今日はマインツの方を\x01",
            "見に行く予定だったんだけど……\x01",
            "この状況じゃ行けるわけないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        "とにかく、住民の皆さんが心配だわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8AB4")

    #C0440
    ChrTalk(
        0xFE,
        (
            "はぁ、まさか\x01",
            "郊外に出かけようって日に\x01",
            "雨に降られちゃうなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        (
            "私ってもしかして雨女？\x01",
            "……それとも、彼が雨男？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8AFF")

    #C0442
    ChrTalk(
        0xFE,
        (
            "さっきのって救急車の音よね。\x01",
            "一体、何があったのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8B8B")

    #C0443
    ChrTalk(
        0xFE,
        (
            "昨日はオルキスタワーの写真を\x01",
            "街の色んな場所から撮ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "ふふ、気付いたら感光クオーツを\x01",
            "２つも使っちゃってたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8BF7")

    #C0445
    ChrTalk(
        0xFE,
        "ふふ、クロスベルっていい所ね。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "なるべく色んな場所に行って、\x01",
            "いっぱい思い出を作るわよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF7")

    TalkEnd(0xFE)
    Return()

    # Function_22_8998 end

    def Function_23_8BFB(): pass

    label("Function_23_8BFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8C76")

    #C0447
    ChrTalk(
        0xFE,
        (
            "ディーター大統領の演説、\x01",
            "ずごく心に響いたわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "私たち国民も、出来ることは\x01",
            "何でも協力しないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CEB")

    label("loc_8C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8CEB")

    #C0449
    ChrTalk(
        0xFE,
        (
            "何でもあの襲撃事件は、\x01",
            "帝国の仕業だったらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "ホント許せないっ。\x01",
            "一体、何様のつもりなの！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CEB")

    TalkEnd(0xFE)
    Return()

    # Function_23_8BFB end

    def Function_24_8CEF(): pass

    label("Function_24_8CEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8DA6")

    #C0451
    ChrTalk(
        0xFE,
        (
            "独立か……もちろん\x01",
            "これからが大変なんだろうけど\x01",
            "今の気分は悪くないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "俺たちはこれから真の自由を\x01",
            "掴み取るんだって思うと、\x01",
            "心の奥底から勇気が湧いてくるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8E51")

    #C0453
    ChrTalk(
        0xFE,
        (
            "武装集団を雇って\x01",
            "街を襲わせるなんて……\x01",
            "マジでやることが汚ねぇよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "たまに忘れかけちまうけど、\x01",
            "エレボニア帝国ってのはやっぱ\x01",
            "とんでもない侵略国家だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E51")

    TalkEnd(0xFE)
    Return()

    # Function_24_8CEF end

    def Function_25_8E55(): pass

    label("Function_25_8E55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E6A")
    Call(0, 30)
    Jump("loc_90B4")

    label("loc_8E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9078")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F05")
    Jump("loc_8F4F")

    label("loc_8F05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F25")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4F")

    label("loc_8F25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F45")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4F")

    label("loc_8F45")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F4F")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0455
    ChrTalk(
        0x19,
        (
            "#02306Fくう、主任に四六時中見張られるなんて\x01",
            "ウザいことこの上ないっつの……\x02\x03",

            "#02310F覚えてろよ、ティオ……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0456
    ChrTalk(
        0x103,
        "#00203Fさて、行きましょうかみなさん。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x19,
        "#02306Fお、おい、無視すんなっ！\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x109,
        "#10109F（さ、さすがティオちゃん……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    Jump("loc_90B4")

    label("loc_9078")

    SetChrSubChip(0x19, 0x0)

    #C0459
    ChrTalk(
        0x19,
        (
            "#02306Fい、いいってば……\x01",
            "自分で食べるっつーの！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90B4")

    TalkEnd(0xFE)
    Return()

    # Function_25_8E55 end

    def Function_26_90B8(): pass

    label("Function_26_90B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90CD")
    Call(0, 30)
    Jump("loc_9339")

    label("loc_90CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C7")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9168")
    Jump("loc_91B2")

    label("loc_9168")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9188")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B2")

    label("loc_9188")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91A8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B2")

    label("loc_91A8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91B2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0460
    ChrTalk(
        0xFE,
        "ティオ君、心配しないでくれよ！\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "ヨナ君のことは、僕が責任を持って\x01",
            "面倒を見させてもらうからね！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 500)

    #C0462
    ChrTalk(
        0x103,
        "#00202Fよろしくお願いします、主任。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#00006F（ティオ、主任の扱い方が\x01",
            "  上手くなってる気がするなあ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_9339")

    label("loc_92C7")

    SetChrSubChip(0xFE, 0x0)

    #C0464
    ChrTalk(
        0xFE,
        (
            "ほらほら、ヨナ君！\x01",
            "ピーマンもニンジンも美味しいよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xFE,
        (
            "なんだったら、\x01",
            "僕が“あ～ん”してあげようか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9339")

    TalkEnd(0xFE)
    Return()

    # Function_26_90B8 end

    def Function_27_933D(): pass

    label("Function_27_933D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9436")

    #C0466
    ChrTalk(
        0xFE,
        (
            "市の職員として\x01",
            "避難誘導をしていたら\x01",
            "私自身が避難しそびれてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xFE,
        (
            "それを見越してか、\x01",
            "妻がミミと一緒に私の所へ\x01",
            "やって来たんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xFE,
        (
            "安全のことを考えると\x01",
            "家で待っていて欲しかったけど……\x01",
            "正直家族で居られるのは嬉しいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_94EE")

    label("loc_9436")


    #C0469
    ChrTalk(
        0xFE,
        (
            "安全のことを考えると\x01",
            "家で待っていて欲しかったけど……\x01",
            "正直家族で居られるのは嬉しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xFE,
        (
            "レストランの人たちも\x01",
            "暖かくて良い人たちばかりだし、\x01",
            "こんな状況でも気持ちが救われるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94EE")

    TalkEnd(0xFE)
    Return()

    # Function_27_933D end

    def Function_28_94F2(): pass

    label("Function_28_94F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9615")

    #C0471
    ChrTalk(
        0xFE,
        (
            "旦那の帰りが遅いので\x01",
            "子供と一緒に迎えに出たんですが……\x01",
            "あのモヤには本当に驚かされました。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xFE,
        (
            "どうやら、あの不気味な人形は\x01",
            "市民を認識して襲わないように\x01",
            "出来ているみたいなんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        (
            "それでも、あの人形に\x01",
            "視線を送られた時の恐怖は\x01",
            "何とも言い難いものでしたね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_9667")

    label("loc_9615")


    #C0474
    ChrTalk(
        0xFE,
        (
            "ふふ、それにしても\x01",
            "やっぱり子供は可愛いですね。\x01",
            "こんな時でも幸せを感じます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9667")

    TalkEnd(0xFE)
    Return()

    # Function_28_94F2 end

    def Function_29_966B(): pass

    label("Function_29_966B")

    TalkBegin(0xFE)

    #C0475
    ChrTalk(
        0xFE,
        (
            "あのね、あのねー。\x01",
            "お店の人がミミたちのために\x01",
            "ゴハンをご馳走してくれたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        "とってもとっても、おいしかったのっ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_966B end

    def Function_30_96F0(): pass

    label("Function_30_96F0")

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
            "#11Pやあ、ティオ君たち\x01",
            "じゃないか～！\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9868")
    Jump("loc_98B2")

    label("loc_9868")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9888")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98B2")

    label("loc_9888")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98A8")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98B2")

    label("loc_98A8")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_98B2")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0478
    ChrTalk(
        0x19,
        "#5P#02302Fよっ、久しぶり。\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        "#6P#00000Fロバーツ主任、それにヨナ。\x02",
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x103,
        "#6P#00200F２人で食事に来てたんですか？\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x1A,
        (
            "#11Pああ、ヨナ君にもたまには\x01",
            "栄養のバランスがいいものを\x01",
            "食べてもらいたいからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x1A,
        (
            "#11P何せヨナ君ときたら、\x01",
            "レマンの財団本部でも\x01",
            "ピザばっかり食べてたそうだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x103,
        "#6P#00203Fああ、そういえばそうでしたね。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x105,
        (
            "#6P#10302Fその割には、あまり野菜とかには\x01",
            "手をつけてないみたいだけど？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x19, 500)

    #C0485
    ChrTalk(
        0x102,
        (
            "#12P#00105Fあら、ほんと。\x01",
            "ピーマンもニンジンも残して……\x02\x03",

            "#00106Fヨナ君、好き嫌いはよくないわよ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B6F")
    Jump("loc_9BB9")

    label("loc_9B6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B8F")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BB9")

    label("loc_9B8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BAF")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BB9")

    label("loc_9BAF")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9BB9")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0486
    ChrTalk(
        0x19,
        (
            "#5P#02306Fフン、ボクがなにを食おうと勝手だろ。\x02\x03",

            "だいたい、わざわざレストランに来て\x01",
            "ナイフとフォークで食べるなんて、\x01",
            "時間の無駄もいーとこだぜ。\x02\x03",

            "#02309Fやっぱ、端末を操作しながらでも\x01",
            "手軽に食べられるピザの方が……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    #C0487
    ChrTalk(
        0x1A,
        (
            "#11Pそ、そんな……\x01",
            "こんなに美味しい野菜たちが\x01",
            "ヨナ君の口に合わなかったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x1A,
        (
            "#11Pああっ、僕のせいだ！\x01",
            "せっかくヨナ君にいいものを\x01",
            "食べさせてあげられると思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x1A,
        (
            "#11Pこうなったら、大陸中のシェフを集めて\x01",
            "何としてもヨナ君の口に合うように\x01",
            "野菜を料理してもらうしか……！！\x02",
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
            "#5P#02301F……あーもう、\x01",
            "めんどくせーオッサンだな！\x02\x03",

            "好き嫌いせずに\x01",
            "食えばいいんだろ、食えば！\x02\x03",

            "#02306Fぱくぱく……ぐう、苦い……\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x109,
        "#6P#10109Fあはは、相変わらずみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x103,
        "#6P#00206F……やれやれです。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A00E")
    Jump("loc_A058")

    label("loc_A00E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A02E")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A058")

    label("loc_A02E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A04E")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A058")

    label("loc_A04E")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A058")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    #C0493
    ChrTalk(
        0x19,
        (
            "#5P#02305Fもぐもぐ……ごくん。\x01",
            "……ああ、そうだ。\x02\x03",

            "#02301Fあんたら、ミシュラムで\x01",
            "タワーの事件に関わっていた\x01",
            "《道化師》の行方を知らないか？\x02",
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

    def lambda_A181():
        TurnDirection(0x0, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A181)
    Sleep(50)

    def lambda_A191():
        TurnDirection(0x1, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_A191)
    Sleep(50)

    def lambda_A1A1():
        TurnDirection(0x2, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_A1A1)
    Sleep(50)

    def lambda_A1B1():
        TurnDirection(0x3, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_A1B1)
    Sleep(50)

    def lambda_A1C1():
        TurnDirection(0x4, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_A1C1)
    Sleep(50)

    def lambda_A1D1():
        TurnDirection(0x5, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x5, 0, lambda_A1D1)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    WaitChrThread(0x4, 0)
    WaitChrThread(0x5, 0)

    #C0494
    ChrTalk(
        0x101,
        "#6P#00003F……いや、知らないな。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#6P#10108F（ミシュラムで会いましたけど……\x01",
            "  さすがにベラベラと\x01",
            "  言うことでもないですよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x19,
        (
            "#5P#02306Fチッ、そうか……まあいいや。\x02\x03",

            "#02310Fあの《道化師》、タワーの事件以来\x01",
            "導力ネットに姿を現してないんだ。\x02\x03",

            "アイツにはボクのベースを\x01",
            "メチャクチャにしてくれた礼を\x01",
            "たっぷりしてやんねーといけないし……\x02\x03",

            "あんたら、何か掴んだら\x01",
            "ボクにも情報を流してくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#12P#00103Fうーん、さすがにそれは\x01",
            "約束できないけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x19,
        (
            "#5P#02306Fケチくせーなあ……\x01",
            "データベースに入力しといて\x01",
            "くれるだけでいいんだって。\x02\x03",

            "#02309Fあとは勝手にハッキングして\x01",
            "見させてもらうからさ。\x02",
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
        "#12P#00306Fおいおい……\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    #C0500
    ChrTalk(
        0x103,
        (
            "#6P#00206F……今はＩＢＣビルの支部に\x01",
            "お世話になっているみたいですし、\x01",
            "少しはおとなしくしているべきかと。\x02\x03",

            "#00200F主任、ヨナをきちんと\x01",
            "見張っておくようお願いします。\x02\x03",

            "#00203F導力ネット基本法が施行された現在、\x01",
            "露骨なハッキング行為を発見した場合は\x01",
            "さすがに見逃せませんので。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x1)

    #C0501
    ChrTalk(
        0x1A,
        "#11Pわ、分かったよティオ君！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    #C0502
    ChrTalk(
        0x1A,
        (
            "#11Pヨナ君、僕が責任を持って\x01",
            "四六時中見守らせてもらうからね！\x02",
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
            "#5P#02305Fお、おいティオ……\x01",
            "さすがにこれはひどくねえ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    #C0504
    ChrTalk(
        0x103,
        "#5P#00203Fでは、行きましょう皆さん。\x02",
    )

    CloseMessageWindow()

    def lambda_A71D():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A71D)
    Sleep(50)

    def lambda_A72D():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A72D)
    Sleep(50)

    def lambda_A73D():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A73D)
    Sleep(50)

    def lambda_A74D():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A74D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0505
    ChrTalk(
        0x101,
        "#12P#00005Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x105,
        "#6P#10302F（フフ、体よく主任を押し付けたねえ。）\x02",
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

    # Function_30_96F0 end

    def Function_31_A7F3(): pass

    label("Function_31_A7F3")

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
        "#11P#00305Fおおっ、キリカさんじゃないッスか！\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        "#00000Fお久しぶりです、キリカさん。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        (
            "#6P#12002Fあら、あなたたち……\x02\x03",

            "#12004Fフフ、ごきげんよう。\x01",
            "こんな所で会うなんて奇遇ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0510
    ChrTalk(
        0x101,
        (
            "#00003F目撃証言を追ってきたら\x01",
            "ここに辿り着きました。\x02\x03",

            "#00001F『競売会』以来ですね。\x01",
            "……ロックスミス機関室長、\x01",
            "キリカ・ロウラン殿。\x02",
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
            "そうね、以前会った時とは\x01",
            "立場も違うし――改めて\x01",
            "自己紹介させてもらおうかしら。\x02\x03",

            "カルバード共和国で\x01",
            "大統領補佐官を務めている、\x01",
            "キリカ・ロウランよ。\x02\x03",

            "他にも肩書きはあるけど……\x01",
            "まあ敢えて語ることではないわね。\x02",
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
            "#00100Fちなみに、以前仰っていた\x01",
            "芸能プロデューサーというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x1E,
        (
            "#6P#12004Fふふ、それも\x01",
            "確かな肩書きの１つよ。\x02\x03",

            "#12002F事務所だって当然、\x01",
            "共和国に存在しているしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x101,
        (
            "#00003F――なるほど。\x01",
            "その辺に抜かりはないんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x105,
        (
            "#10302F（ふふ、表の顔を\x01",
            "  複数使い分ける女諜報員か。）\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        (
            "#11P#00309F（う～ん、そんなミステリアスな\x01",
            "  キリカさんも素敵かもな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x109,
        (
            "#10106F（先輩、流石にその発言は\x01",
            "  緊張感に欠けるような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#00105Fところで……\x01",
            "大統領の補佐官として訪れている\x01",
            "貴女がどうしてこんなところに？\x02\x03",

            "今日はロックスミス大統領が\x01",
            "ＩＢＣを視察されていると\x01",
            "聞いていましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        (
            "#6P#12004Fその大統領にちょっとした\x01",
            "お使いを頼まれてしまってね。\x02\x03",

            "#12000Fお忍びでの買い物がてら、\x01",
            "ここで遅めの昼食を\x01",
            "取らせてもらっているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x109,
        "#10105Fお使い……ですか？\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xFE,
        "#6P#12004Fこれよ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キリカは風車#4Rかざぐるま#を取り出して\x01",
            "ふう、と息を吹きかけた。\x02",
        )
    )

    CloseMessageWindow()

    #A0523
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "風車の羽根がくるくる回った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0524
    ChrTalk(
        0x109,
        "#10105Fか、風車……？\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "#6P#12000F行きのリムジンで露店が目に入って、\x01",
            "無性に欲しくなってしまわれたそうよ。\x02\x03",

            "明日の本会議に臨む前に、\x01",
            "リラックスアイテムとして\x01",
            "手元に置いておきたいらしいわ。\x02\x03",

            "#12004Fついでに、今晩の会食のデザートに\x01",
            "果物なんかを一緒にね。\x02",
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
            "#11P#00306Fな、なんつうか……\x01",
            "本当にお使いじゃないッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、さすが庶民派で知られる\x01",
            "ロックスミス大統領って感じだね。\x02\x03",

            "#10304Fそれが、あなたが街に出てきた\x01",
            "本当の目的だったら#8R㈲　㈲　㈲　㈲#、の話だけど。\x02",
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
            "#6P#12004Fフフ、ご想像にお任せするわ。\x02\x03",

            "#12000Fさて、食事も終わった事だし\x01",
            "私はそろそろ失礼させてもらうわね。\x02\x03",

            "あなたたちも、通商会議中の警備を\x01",
            "頑張ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        (
            "#00105Fは、はい。\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1800, 6500, 17260, 1000)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2610, 5000, 17800, 180)
    Sleep(1200)

    def lambda_B2B0():

        label("loc_B2B0")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2B0")

    QueueWorkItem2(0x101, 2, lambda_B2B0)

    def lambda_B2C2():

        label("loc_B2C2")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2C2")

    QueueWorkItem2(0x102, 2, lambda_B2C2)

    def lambda_B2D4():

        label("loc_B2D4")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2D4")

    QueueWorkItem2(0x104, 2, lambda_B2D4)

    def lambda_B2E6():

        label("loc_B2E6")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2E6")

    QueueWorkItem2(0x109, 2, lambda_B2E6)

    def lambda_B2F8():

        label("loc_B2F8")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2F8")

    QueueWorkItem2(0x105, 2, lambda_B2F8)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_B39D")
    Call(0, 32)
    Jump("loc_B3A0")

    label("loc_B39D")

    Sleep(1000)

    label("loc_B3A0")

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

    # Function_31_A7F3 end

    def Function_32_B3EB(): pass

    label("Function_32_B3EB")

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
            "#00003Fレクターさん、キリカさん……\x02\x03",

            "帝国と共和国の諜報員が、\x01",
            "似たようなタイミングで\x01",
            "市内に出てきていた。\x02\x03",

            "#00001F……みんな、どう思う？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_B4CB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B4CB)
    Sleep(50)

    def lambda_B4DB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B4DB)
    Sleep(50)

    def lambda_B4EB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B4EB)
    Sleep(50)

    def lambda_B4FB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B4FB)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0532
    ChrTalk(
        0x109,
        "#10103F……なんだかキナ臭いですね。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、だったらこのまま\x01",
            "彼らを追跡してみるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x102,
        (
            "#00108Fそれも難しいんじゃないかしら。\x02\x03",

            "#00103Fどちらも、私たちが辿り着くのは\x01",
            "分かっていたような雰囲気だったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#00003F……ダドリーさんたちに\x01",
            "報告しに行ってみないか？\x02\x03",

            "#00000F捜査一課の情報と合わせれば\x01",
            "何か分かるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x109,
        "#10105Fあ……よさそうですね。\x02",
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x104,
        (
            "#00300Fよっしゃ、そうと決まれば\x01",
            "警察本部に行ってみるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_32_B3EB end

    def Function_33_B6D8(): pass

    label("Function_33_B6D8")

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
            "いらっしゃいませ。\x01",
            "《ヴァンセット》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        "ご予約のお客様でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0542
    ChrTalk(
        0x8,
        (
            "おや、皆様がそうでしたか。\x01",
            "お話は聞かせて頂いていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x8,
        (
            "それでは、空いているテーブルに\x01",
            "おつき下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x8,
        (
            "当店の今季の新作、『ハーブパスタ』を\x01",
            "ご用意させていただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        "#00100Fふふ、よろしくお願いします。\x02",
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
            "ロイドたちはテーブル席につき、\x01",
            "ハーブパスタを食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0547
    ChrTalk(
        0x103,
        "#00200Fもぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        (
            "ふふ、当店のシェフ\x01",
            "自慢のパスタはいかがですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x109,
        "#10109Fええ、とっても美味しいです！\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、コクがあるのに\x01",
            "後味もさっぱりしてるね。\x02\x03",

            "#10300Fハーブが効いてて涼しげな\x01",
            "食感を楽しめるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        (
            "#00309Fああ、このレストランは\x01",
            "やっぱ鉄板の美味さだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x8,
        (
            "はは、堪能していただけて\x01",
            "なによりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、今度はキーアちゃんも\x01",
            "連れてこなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        "#00000Fああ、是非そうしよう。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x8,
        (
            "ふふ、職員一同、\x01",
            "またの来店をお待ちしておりますよ。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_BEC3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_BEE0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_BEF3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BF06")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BF23")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BF36")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BF53")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BF66")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BF83")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BF96")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BFB3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFB3")

    OP_29(0x80, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0B6")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0556
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C0AD")

    #A0557
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C0AD")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_C0B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C187")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0558
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0559
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_C187")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C1A9")
    Jump("loc_C311")

    label("loc_C1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C1CE")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_C311")

    label("loc_C1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C1DC")
    Jump("loc_C311")

    label("loc_C1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C1EA")
    Jump("loc_C311")

    label("loc_C1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C226")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C262")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C29E")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C2DA")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C311")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)

    label("loc_C311")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -510, 0, 9440, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_B6D8 end

    def Function_34_C341(): pass

    label("Function_34_C341")

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
        "#00005Fあ……\x02",
    )

    CloseMessageWindow()

    def lambda_C564():
        OP_93(0x102, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C564)
    Sleep(50)

    def lambda_C574():
        OP_93(0x103, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C574)
    Sleep(50)

    def lambda_C584():
        OP_93(0x104, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C584)
    Sleep(50)

    def lambda_C594():
        OP_93(0x109, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C594)
    Sleep(50)

    def lambda_C5A4():
        OP_93(0x105, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C5A4)
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
        "ホスト？",
        (
            "……ハハ、マーガレットさんは\x01",
            "さすがの慧眼をお持ちですね。\x02",
        )
    )

    CloseMessageWindow()

    #N0562
    NpcTalk(
        0x20,
        "ホスト？",
        (
            "こんなことを言ってはなんですが、\x01",
            "やはり今の旦那様にはもったいない。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x21,
        (
            "オホホ……\x01",
            "相変わらずお上手なんだから、\x01",
            "クライドさんは……\x02",
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
            "#00100F……どうやら、副局長の奥様は\x01",
            "あの人で間違いなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x105,
        (
            "#10305Fとすると、向かいに座ってるのが\x01",
            "ホストと思しき『クライド』か。\x02\x03",

            "#10303Fうーん、やっぱり見覚えはないなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x101,
        (
            "#00003Fとにかく、怪しまれないように\x01",
            "近くのテーブルに座ろう。\x02\x03",

            "#00001F何か情報が聞けるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x103,
        "#00200Fがってんです。\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x109,
        (
            "#10100Fそれじゃあ、適当に分かれて\x01",
            "座ることにしましょう。\x02",
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
            "そうそう、この間もらった\x01",
            "パンフレットを見させてもらったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x21,
        "写真を見て、一目で気に入ったわ。\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x20,
        "はは、光栄ですよ。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x20,
        (
            "それじゃあ、是非今度\x01",
            "ご一緒に行ってみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x20,
        (
            "お望みでしたらホテルも\x01",
            "こちらで手配しますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x21,
        "ホホホ、それには及ばないわ。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x21,
        (
            "実は、下見にはもう行っているのよ。\x01",
            "なかなかの景色だし文句はないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x20,
        "おお、そうですか！\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x20,
        (
            "いや、私も助かりますよ！\x01",
            "でしたら約束も早めて……\x02",
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
        "#00001F（……かなり和やかに話しているな。）\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x102,
        (
            "#00103F（一緒にミシュラムへ旅行にいく\x01",
            "  算段を立てているようにも見えるけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x103,
        (
            "#00200F（それにしては、様子が\x01",
            "  おかしい気もしますが。）\x02",
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
            "#00303F（男の方が\x01",
            "  やたら丁寧語なのも\x01",
            "  なんだか気になるぜ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x109,
        (
            "#10106F（でも決定的なことは\x01",
            "  まだ分かりませんね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、まあもう少し\x01",
            "  聞き耳を立ててみるとしようよ。）\x02",
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
        "……それじゃあ、今日は失礼しますよ。\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x21,
        (
            "ええ、分かったわ。\x01",
            "それじゃあ後で、あのお店にね。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x20,
        (
            "歓楽街の《ノイエ＝ブラン》ですね。\x01",
            "フフ、分かっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x20,
        (
            "奥さんのお望みの物を持って\x01",
            "馳せ参じるとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x21,
        "ええ、お待ちしてるわ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x20, 1, 0, 41)
    Sleep(300)
    BeginChrThread(0x21, 1, 0, 42)
    Sleep(300)
    OP_68(-650, 1550, 7560, 3000)
    WaitChrThread(0x20, 1)
    Sleep(800)

    def lambda_CFC6():
        OP_95(0x20, 4230, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_CFC6)
    Sleep(200)
    WaitChrThread(0x21, 1)

    def lambda_CFE7():
        OP_95(0x21, 4230, 0, 7840, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_CFE7)
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

    def lambda_D064():
        OP_95(0x20, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D064)

    def lambda_D07E():
        OP_95(0x21, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D07E)
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
        "#00001F（どうやら店を出るみたいだな……）\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x102,
        "#00100F（どうするの、ロイド？）\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#00200F（まだ決定的な情報は\x01",
            "  得られていませんが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#00003F（……彼らを尾行してみよう。）\x02\x03",

            "#00000F（俺とワジ、ランディは\x01",
            "  あのクライドという男を。）\x02\x03",

            "（エリィとティオ、ノエルは\x01",
            "  マーガレット夫人を追ってくれ。）\x02\x03",

            "（ただし、気づかれないように\x01",
            "  極力注意をしてくれ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x109,
        "#10101F（……分かりました！）\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x104,
        "#00300F（それじゃあ行ってみるとすっか。）\x02",
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x105,
        "#10302F（フフ、面白くなってきたじゃない。）\x02",
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

    # Function_34_C341 end

    def Function_35_D2BA(): pass

    label("Function_35_D2BA")


    def lambda_D2BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D2BF)

    def lambda_D2D0():
        OP_95(0x101, 10110, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D2D0)
    WaitChrThread(0x101, 1)
    Return()

    # Function_35_D2BA end

    def Function_36_D2EA(): pass

    label("Function_36_D2EA")


    def lambda_D2EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D2EF)

    def lambda_D300():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D300)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, 10600, 0, 10450, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_36_D2EA end

    def Function_37_D330(): pass

    label("Function_37_D330")


    def lambda_D335():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D335)

    def lambda_D346():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D346)
    WaitChrThread(0x103, 1)
    OP_95(0xFE, 11310, 0, 7580, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_D330 end

    def Function_38_D376(): pass

    label("Function_38_D376")


    def lambda_D37B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D37B)

    def lambda_D38C():
        OP_95(0xFE, 11630, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D38C)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_38_D376 end

    def Function_39_D3AD(): pass

    label("Function_39_D3AD")


    def lambda_D3B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D3B2)

    def lambda_D3C3():
        OP_95(0xFE, 12860, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D3C3)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_D3AD end

    def Function_40_D3E4(): pass

    label("Function_40_D3E4")


    def lambda_D3E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D3E9)

    def lambda_D3FA():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D3FA)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, 12200, 0, 10670, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_D3E4 end

    def Function_41_D42A(): pass

    label("Function_41_D42A")

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

    # Function_41_D42A end

    def Function_42_D46E(): pass

    label("Function_42_D46E")

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

    # Function_42_D46E end

    def Function_43_D4B2(): pass

    label("Function_43_D4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D691")

    #C0596
    ChrTalk(
        0xB,
        "あ、いらっしゃいませ～。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xB,
        (
            "お好きな席にお座りください。\x01",
            "あとで注文にうかがいますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        (
            "#00003F（この人ならミスコンの\x01",
            "  『ウェイトレス』枠に\x01",
            "  誘えるかもしれないな。）\x02\x03",

            "#00000Fあの、すみません。\x01",
            "ちょっと相談なのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0600
    ChrTalk(
        0xB,
        (
            "え、ええ？\x01",
            "ミスコンへの参加ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xB,
        (
            "う～～ん……\x01",
            "申し訳ないんですけど……\x01",
            "ちょっと興味がないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x101,
        (
            "#00012Fそ、そうですか……\x01",
            "それは失礼しました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 5)
    Jump("loc_D706")

    label("loc_D691")


    #C0603
    ChrTalk(
        0xB,
        (
            "ミスコンの参加には\x01",
            "特に興味はないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xB,
        (
            "ウェイトレスとして\x01",
            "お手伝いするだけなら\x01",
            "いいかもしれませんけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D706")

    TalkEnd(0xB)
    Return()

    # Function_43_D4B2 end

    SaveToFile()

Try(main)
