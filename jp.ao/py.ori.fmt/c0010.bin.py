from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "駅員ルクス",             # 1
        "駅員リサ",               # 2
        "駅員エイム",             # 3
        "駅員シェンリー",         # 4
        "駅員マッジス",           # 5
        "臨検官クワトロ",         # 6
        "フェイ",                 # 7
        "ビリー",                 # 8
        "ビジネスマン",           # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "老人",                   # 12
        "老婆",                   # 13
        "観光客",                 # 14
        "観光客",                 # 15
        "男の子",                 # 16
        "ミュラー",               # 17
        "臨検官マーロウ",         # 18
        "レイモンド捜査官",       # 19
        "東方風の男",             # 20
        "東方風の男",             # 21
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
        "Function_4_C63",          # 04, 4
        "Function_5_C67",          # 05, 5
        "Function_6_115B",         # 06, 6
        "Function_7_12C6",         # 07, 7
        "Function_8_12CA",         # 08, 8
        "Function_9_17B1",         # 09, 9
        "Function_10_1922",        # 0A, 10
        "Function_11_1CB7",        # 0B, 11
        "Function_12_1CBB",        # 0C, 12
        "Function_13_2085",        # 0D, 13
        "Function_14_2089",        # 0E, 14
        "Function_15_277D",        # 0F, 15
        "Function_16_2915",        # 10, 16
        "Function_17_291F",        # 11, 17
        "Function_18_2AEB",        # 12, 18
        "Function_19_2D03",        # 13, 19
        "Function_20_2E43",        # 14, 20
        "Function_21_2F94",        # 15, 21
        "Function_22_327E",        # 16, 22
        "Function_23_33E8",        # 17, 23
        "Function_24_3583",        # 18, 24
        "Function_25_371D",        # 19, 25
        "Function_26_3832",        # 1A, 26
        "Function_27_38C6",        # 1B, 27
        "Function_28_3B5A",        # 1C, 28
        "Function_29_3B91",        # 1D, 29
        "Function_30_3BDE",        # 1E, 30
        "Function_31_3BE8",        # 1F, 31
        "Function_32_3BF2",        # 20, 32
        "Function_33_3C73",        # 21, 33
        "Function_34_45C3",        # 22, 34
        "Function_35_4F87",        # 23, 35
        "Function_36_51DA",        # 24, 36
        "Function_37_53A9",        # 25, 37
        "Function_38_549B",        # 26, 38
        "Function_39_562E",        # 27, 39
        "Function_40_5A7F",        # 28, 40
        "Function_41_5DD3",        # 29, 41
        "Function_42_5E09",        # 2A, 42
        "Function_43_6A00",        # 2B, 43
        "Function_44_6BA5",        # 2C, 44
        "Function_45_7637",        # 2D, 45
        "Function_46_7750",        # 2E, 46
        "Function_47_776F",        # 2F, 47
        "Function_48_778E",        # 30, 48
        "Function_49_77BA",        # 31, 49
        "Function_50_7803",        # 32, 50
        "Function_51_830A",        # 33, 51
        "Function_52_8382",        # 34, 52
        "Function_53_83FA",        # 35, 53
        "Function_54_8433",        # 36, 54
        "Function_55_84C6",        # 37, 55
        "Function_56_84FF",        # 38, 56
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
            "車雑誌『別冊クルマスター』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x373, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『シャインカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x373, 1)

    label("loc_C5F")

    TalkEnd(0xFF)
    Return()

    # Function_3_BBC end

    def Function_4_C63(): pass

    label("Function_4_C63")

    Call(0, 5)
    Return()

    # Function_4_C63 end

    def Function_5_C67(): pass

    label("Function_5_C67")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C7B")
    Call(0, 6)
    Jump("loc_1157")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E8C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D66")

    #C0003
    ChrTalk(
        0x8,
        (
            "本日もクロスベル駅を\x01",
            "ご利用いただき、\x01",
            "誠にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "間もなく共和国行きが、\x01",
            "それに続いて帝国行きが\x01",
            "順次発車予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "お急ぎの方は、お早めに\x01",
            "チケットをご購入ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE3")

    label("loc_D66")


    #C0006
    ChrTalk(
        0x8,
        (
            "間もなく共和国行きが、\x01",
            "それに続いて帝国行きが\x01",
            "順次発車予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "お急ぎの方は、お早めに\x01",
            "チケットをご購入ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE3")

    Jump("loc_E87")

    label("loc_DE8")


    #C0008
    ChrTalk(
        0x8,
        (
            "逃走犯が列車の屋根に\x01",
            "飛び移ったなんて聞いたときは、\x01",
            "さすがに耳を疑いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "今後、真似をするような人が出ないよう\x01",
            "注意しておく必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E87")

    Jump("loc_1157")

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")

    #C0010
    ChrTalk(
        0x8,
        (
            "本日もクロスベル駅を\x01",
            "ご利用いただき、\x01",
            "誠にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "通商会議期間中は、\x01",
            "帝国軍によりホームの警備が\x01",
            "強化されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "臨検なども厳しくなりますので\x01",
            "どうかご了承ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEB")

    label("loc_F6C")


    #C0013
    ChrTalk(
        0x8,
        (
            "通商会議期間中は、\x01",
            "帝国軍によりホームの警備が\x01",
            "強化されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "臨検なども厳しくなりますので\x01",
            "どうかご了承ください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEB")

    Jump("loc_1157")

    label("loc_FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D4")

    #C0015
    ChrTalk(
        0x8,
        (
            "本日もクロスベル駅を\x01",
            "ご利用いただき、\x01",
            "誠にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "通商会議期間中ですが、\x01",
            "鉄道は通常通り運行中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "チケットは２階スペースで\x01",
            "お買い求めいただけますので、\x01",
            "そちらへどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1157")

    label("loc_10D4")


    #C0018
    ChrTalk(
        0x8,
        (
            "通商会議期間中ですが、\x01",
            "鉄道は通常通り運行中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "チケットは２階スペースで\x01",
            "お買い求めいただけますので、\x01",
            "そちらへどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1157")

    TalkEnd(0x8)
    Return()

    # Function_5_C67 end

    def Function_6_115B(): pass

    label("Function_6_115B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122A")

    #C0020
    ChrTalk(
        0x8,
        (
            "今現在、列車の運行は\x01",
            "帝国行き・共和国行き共に\x01",
            "見合わせております。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "お客様には大変な\x01",
            "ご迷惑をおかけしますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x10,
        (
            "そんな、困るよ！\x01",
            "帝国で大事な商談が\x01",
            "あるってのに……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12BD")

    label("loc_122A")


    #C0023
    ChrTalk(
        0x8,
        (
            "申し訳ありませんが、\x01",
            "復旧時刻も現在未定と\x01",
            "なっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "お客様にはどうか\x01",
            "ご理解をいただきたく……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x10,
        "そんな、商談が、商談がぁ……！\x02",
    )

    CloseMessageWindow()

    label("loc_12BD")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_6_115B end

    def Function_7_12C6(): pass

    label("Function_7_12C6")

    Call(0, 8)
    Return()

    # Function_7_12C6 end

    def Function_8_12CA(): pass

    label("Function_8_12CA")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1335")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1354")
    OP_AF(0x8B)
    Jump("loc_13D6")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1364")
    OP_AF(0x8A)
    Jump("loc_13D6")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1374")
    OP_AF(0x89)
    Jump("loc_13D6")

    label("loc_1374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1384")
    OP_AF(0x88)
    Jump("loc_13D6")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1394")
    OP_AF(0x87)
    Jump("loc_13D6")

    label("loc_1394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13A4")
    OP_AF(0x86)
    Jump("loc_13D6")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_13B4")
    OP_AF(0x85)
    Jump("loc_13D6")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C4")
    OP_AF(0x84)
    Jump("loc_13D6")

    label("loc_13C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13D4")
    OP_AF(0x83)
    Jump("loc_13D6")

    label("loc_13D4")

    OP_AF(0x82)

    label("loc_13D6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A8")

    label("loc_13E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F9")
    Jump("loc_17A8")

    label("loc_13F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1423")
    Call(0, 9)
    Jump("loc_17A8")

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1531")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1497")

    #C0026
    ChrTalk(
        0x9,
        "旅のお供に駅弁はいかがですか？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "クロスベルタイムズの最新号も\x01",
            "入荷していますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152C")

    label("loc_1497")


    #C0028
    ChrTalk(
        0x9,
        (
            "逃走犯とテロリストの逮捕……\x01",
            "そんな事が一度に起こるなんて\x01",
            "なかなか聞かない話ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "いくつもの偶然が重なった、\x01",
            "ということなのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152C")

    Jump("loc_17A8")

    label("loc_1531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1643")

    #C0030
    ChrTalk(
        0x9,
        (
            "臨検官のマーロウさんは、\x01",
            "共和国軍から出向されている方です。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "帝国軍から出向された\x01",
            "臨検官のクワトロさんとは、\x01",
            "あまり仲がよろしくないんだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "曲がりなりにも帝国と共和国は\x01",
            "紛争で争ってきた間柄ですから、\x01",
            "仕方ないことかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16F0")

    label("loc_1643")


    #C0033
    ChrTalk(
        0x9,
        (
            "臨検官のマーロウさんとクワトロさんは、\x01",
            "あまり仲がよろしくないんだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "曲がりなりにも帝国と共和国は\x01",
            "紛争で争ってきた間柄ですから、\x01",
            "仕方ないことかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F0")

    Jump("loc_17A8")

    label("loc_16F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17A8")

    #C0035
    ChrTalk(
        0x9,
        (
            "今朝は帝国の出版社である\x01",
            "《帝国時報社》の記者の方々も\x01",
            "取材に来られていたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            "クロスベルで行われる\x01",
            "国際会議ということで、\x01",
            "注目度もかなり高いんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A8")

    Jump("loc_12D7")

    label("loc_17AD")

    TalkEnd(0x9)
    Return()

    # Function_8_12CA end

    def Function_9_17B1(): pass

    label("Function_9_17B1")

    OP_4B(0x9, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")

    #N0037
    NpcTalk(
        0x11,
        "市民",
        (
            "ええい、チケットの払い戻しが\x01",
            "できればいいという話じゃないんだ！\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x11,
        "市民",
        (
            "俺は今日の旅行の為に、\x01",
            "せっせと準備をだなあ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "ほ、本当に申し訳ありません。\x01",
            "私どもも今現在、事実関係の確認を……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1919")

    label("loc_1898")


    #N0040
    NpcTalk(
        0x11,
        "市民",
        (
            "全く、ソンをするのは\x01",
            "いつも客のほうじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "ほ、本当に申し訳ありません。\x01",
            "私どもも今現在、事実関係の確認を……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1919")

    OP_4C(0x9, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_17B1 end

    def Function_10_1922(): pass

    label("Function_10_1922")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1936")
    Call(0, 17)
    Jump("loc_1CB3")

    label("loc_1936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D8")

    #C0042
    ChrTalk(
        0xFE,
        (
            "あの警察の兄さん、\x01",
            "なんだかキョロキョロしてたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "誰かを追ってるのか？\x01",
            "特に怪しいやつが入ってきた\x01",
            "ようには見えなかったが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_19D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A99")

    #C0044
    ChrTalk(
        0xFE,
        (
            "偽ブランド商だけならまだしも、\x01",
            "テロリストまでいたとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "顔を知らなかったのもあるが、\x01",
            "そうまで一般人に紛れ込める\x01",
            "ものなんだろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "ある意味恐ろしい話だよ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1B11")

    label("loc_1A99")


    #C0047
    ChrTalk(
        0xFE,
        (
            "偽ブランド商だけならまだしも、\x01",
            "テロリストまで一般人に\x01",
            "紛れ込めるものなんだろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "ある意味恐ろしい話だよ……\x02",
    )

    CloseMessageWindow()

    label("loc_1B11")

    Jump("loc_1CB3")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BB7")

    #C0049
    ChrTalk(
        0xFE,
        (
            "帝国政府専用列車が\x01",
            "停車している３番ホームは、\x01",
            "帝国軍が厳重に警備している。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "見物くらいは構わないだろうけど、\x01",
            "不用意に近づかないようにな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB3")

    label("loc_1BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CB3")

    #C0051
    ChrTalk(
        0xFE,
        (
            "今朝、帝国政府専用列車\x01",
            "《アイゼングラーフ号》が\x01",
            "１番ホームに到着してな。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "通常の列車の運行もあるから、\x01",
            "今は３番ホームに移動してもらってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "滅多に見られるもんじゃないし、\x01",
            "ホームに下りる機会があるなら\x01",
            "是非とも見物していくといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB3")

    TalkEnd(0xFE)
    Return()

    # Function_10_1922 end

    def Function_11_1CB7(): pass

    label("Function_11_1CB7")

    Call(0, 12)
    Return()

    # Function_11_1CB7 end

    def Function_12_1CBB(): pass

    label("Function_12_1CBB")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D5E")

    #C0054
    ChrTalk(
        0xA,
        (
            "申し訳ありませんが、\x01",
            "現在列車事故の対応で\x01",
            "大変混雑しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "チケットの購入・ご予約等は\x01",
            "お受けできませんので、\x01",
            "ご了承くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2081")

    label("loc_1D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F81")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E54")

    #C0056
    ChrTalk(
        0xA,
        (
            "先ほど帝国行きのチケットを\x01",
            "買っていったお婆さん、\x01",
            "とても優しそうな方でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xA,
        (
            "なんでも長年ある商売を\x01",
            "続けている方なんだそうで。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "詳しくはお聞きしませんでしたが、\x01",
            "是非とも頑張ってほしいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EE3")

    label("loc_1E54")


    #C0059
    ChrTalk(
        0xA,
        (
            "先ほど帝国行きのチケットを\x01",
            "買っていったお婆さん、\x01",
            "とても優しそうな方でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "帝国へは商売へ行くとか。\x01",
            "是非とも頑張ってほしいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE3")

    Jump("loc_1F7C")

    label("loc_1EE8")


    #C0061
    ChrTalk(
        0xA,
        (
            "アルタイル市で捕まった\x01",
            "偽ブランド商って、\x01",
            "お婆さんだったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "もしかして、あのとき\x01",
            "チケットを買っていた\x01",
            "お婆さんだったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7C")

    Jump("loc_2081")

    label("loc_1F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2021")

    #C0063
    ChrTalk(
        0xA,
        (
            "現在、警備上の観点から\x01",
            "入場時の手荷物検査を\x01",
            "徹底させて頂いております。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "お手数をお掛けしますが、\x01",
            "どうかご理解と\x01",
            "ご協力をお願い致します。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2081")

    label("loc_2021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2081")

    #C0065
    ChrTalk(
        0xA,
        (
            "こちらはチケットカウンターに\x01",
            "なっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        "ご購入の際は仰ってくださいね。\x02",
    )

    CloseMessageWindow()

    label("loc_2081")

    TalkEnd(0xA)
    Return()

    # Function_12_1CBB end

    def Function_13_2085(): pass

    label("Function_13_2085")

    Call(0, 14)
    Return()

    # Function_13_2085 end

    def Function_14_2089(): pass

    label("Function_14_2089")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A4")

    #C0067
    ChrTalk(
        0xB,
        (
            "あっ……すみません、\x01",
            "少しお待ちいただけますか。\x02",
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
            "現在、西クロスベル街道で発生した\x01",
            "脱線事故により、列車の運行を\x01",
            "見合わせております。\x02\x03",

            "なお、本日中の復旧は\x01",
            "今だ見通しが立っていない状態です。\x01",
            "どうかご了承くださいませ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2213")

    label("loc_21A4")


    #C0069
    ChrTalk(
        0xB,
        (
            "払い戻し対応に\x01",
            "構内のアナウンス……\x01",
            "さすがに大変です。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "早く鉄道が復旧して\x01",
            "くれるといいんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2213")

    Jump("loc_2779")

    label("loc_2218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_242A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230B")

    #C0071
    ChrTalk(
        0xB,
        (
            "あっ……すみません、\x01",
            "少しお待ちいただけますか。\x02",
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
            "共和国行き、帝国行きの列車が\x01",
            "間もなく発車する予定です。\x02\x03",

            "駆け込み乗車などなさらぬよう\x01",
            "充分にお気をつけくださいませ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_238D")

    label("loc_230B")


    #C0073
    ChrTalk(
        0xB,
        (
            "駆け込み乗車は\x01",
            "人身事故の元になり、\x01",
            "大変危険なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "間に合わない場合は、\x01",
            "落ち着いて次に来る列車を\x01",
            "お待ちくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238D")

    Jump("loc_2425")

    label("loc_2392")


    #C0075
    ChrTalk(
        0xB,
        (
            "駆け込み乗車ならまだしも、\x01",
            "列車の屋根に乗る方がいるなんて\x01",
            "びっくりしました……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "……アナウンスで注意したほうが\x01",
            "いいものなんでしょうかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2425")

    Jump("loc_2779")

    label("loc_242A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_253E")

    #C0077
    ChrTalk(
        0xB,
        (
            "あっ……すみません、\x01",
            "少しお待ちいただけますか。\x02",
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
            "クロスベル駅では、\x01",
            "太陸鉄道公社規約に基づいて\x01",
            "臨検を行っております。\x02\x03",

            "帝国・共和国方面に向かわれる方は\x01",
            "入国申請書をご記入の上、\x01",
            "臨検官への提出をお願いいたします。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_25C3")

    label("loc_253E")


    #C0079
    ChrTalk(
        0xB,
        (
            "クロスベル駅から\x01",
            "帝国・共和国に行くには、\x01",
            "臨検を受ける必要があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xB,
        (
            "少々面倒ですけど、\x01",
            "どうかご理解をお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C3")

    Jump("loc_2779")

    label("loc_25C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E8")

    #C0081
    ChrTalk(
        0xB,
        (
            "あっ……すみません、\x01",
            "少しお待ちいただけますか。\x02",
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
            "本日、帝国政府専用列車\x01",
            "《アイゼングラーフ号》の到着により\x01",
            "警備体制を強化しております。\x02\x03",

            "つきましては、停車中の\x01",
            "第３ホームには立ち入らないよう、\x01",
            "お客様のご理解をお願いします。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2779")

    label("loc_26E8")


    #C0083
    ChrTalk(
        0xB,
        (
            "失礼しました、私は構内の\x01",
            "アナウンス担当なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "もし鉄道のご利用について\x01",
            "不明な点がございますでしょうか？\x01",
            "お気軽にお尋ねくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2779")

    TalkEnd(0xB)
    Return()

    # Function_14_2089 end

    def Function_15_277D(): pass

    label("Function_15_277D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2841")

    #C0085
    ChrTalk(
        0xFE,
        (
            "宰相閣下とオリヴァルト皇子、\x01",
            "お二方の姿を拝見するのは\x01",
            "いつ以来であったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "いち帝国軍人として\x01",
            "政府要人のお出迎えができたこと、\x01",
            "全くもって光栄の極みだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2888")

    label("loc_2841")


    #C0087
    ChrTalk(
        0xFE,
        (
            "……ム？　あの一階に立っている\x01",
            "黒服の大男、どこかで見たような……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")

    Jump("loc_2911")

    label("loc_288D")


    #C0088
    ChrTalk(
        0xFE,
        (
            "いつのまにか、あの黒服の大男が\x01",
            "どこかに行ってしまったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "まさかとは思ったが……\x01",
            "ふむ、おそらく気のせいであろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2911")

    TalkEnd(0xFE)
    Return()

    # Function_15_277D end

    def Function_16_2915(): pass

    label("Function_16_2915")

    TalkBegin(0xFE)
    Call(0, 17)
    TalkEnd(0xFE)
    Return()

    # Function_16_2915 end

    def Function_17_291F(): pass

    label("Function_17_291F")

    OP_4B(0xE, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5E")

    #C0090
    ChrTalk(
        0xE,
        (
            "それで、列車の破損状況は\x01",
            "どうなんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "連絡を受けた限りでは、\x01",
            "かなり酷い状態みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "下手すると、列車そのものが\x01",
            "ダメになってるかもしれません……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xE,
        (
            "ふむ……そうなると、\x01",
            "ひとまずは別の列車を\x01",
            "手配するしかないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xE,
        (
            "今はとにかく、\x01",
            "鉄道の運行再開を\x01",
            "最優先に考えないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AE2")

    label("loc_2A5E")


    #C0095
    ChrTalk(
        0xE,
        (
            "線路自体が破損した可能性も\x01",
            "充分にあるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        (
            "列車の撤去作業が終わり次第、\x01",
            "現場に向かうとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        "ええ、了解です。\x02",
    )

    CloseMessageWindow()

    label("loc_2AE2")

    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_291F end

    def Function_18_2AEB(): pass

    label("Function_18_2AEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AFF")
    Call(0, 9)
    Jump("loc_2CFF")

    label("loc_2AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B79")

    #C0098
    ChrTalk(
        0xFE,
        (
            "うーむ、列車はすぐにも\x01",
            "出てしまいそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "仕方ない、買出しにでも行って\x01",
            "次の列車を待つとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFF")

    label("loc_2B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B87")
    Jump("loc_2CFF")

    label("loc_2B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C68")

    #C0100
    ChrTalk(
        0xFE,
        (
            "私は共和国最西端の港湾都市、\x01",
            "アルタイル市からやってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "しかし、クロスベルは\x01",
            "やはり物凄く発展してるなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "共和国もかなり栄えてるけど、\x01",
            "クロスベルに比べると\x01",
            "田舎に思えちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2CFF")

    label("loc_2C68")


    #C0103
    ChrTalk(
        0xFE,
        (
            "私は共和国最西端の港湾都市、\x01",
            "アルタイル市からやってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "しかし、クロスベルは\x01",
            "やはり物凄く発展してるなあ。\x01",
            "共和国が田舎に思えちゃうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFF")

    TalkEnd(0xFE)
    Return()

    # Function_18_2AEB end

    def Function_19_2D03(): pass

    label("Function_19_2D03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D17")
    Call(0, 6)
    Jump("loc_2E3F")

    label("loc_2D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2DAA")

    #C0105
    ChrTalk(
        0xFE,
        (
            "駅員が話していたが……\x01",
            "共和国でテロリストの残党が\x01",
            "捕まったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "しばらく潜伏してたようだが、\x01",
            "ひとまずは安心できるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3F")

    label("loc_2DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E36")

    #C0107
    ChrTalk(
        0xFE,
        "今から帝国方面に出張なのだよ。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "本会議の様子は気になるが……\x01",
            "向こうの《帝国時報》で\x01",
            "特集されるだろうし、問題ないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3F")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E3F")

    label("loc_2E3F")

    TalkEnd(0xFE)
    Return()

    # Function_19_2D03 end

    def Function_20_2E43(): pass

    label("Function_20_2E43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E9D")

    #C0109
    ChrTalk(
        0xFE,
        "だ、脱線事故だなんて……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "主人は、主人は\x01",
            "どうなったんですの！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EF3")

    #C0111
    ChrTalk(
        0xFE,
        "ようやくクロスベルについたわー。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "一休みしたらさっそく観光ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F87")

    #C0113
    ChrTalk(
        0xFE,
        (
            "この子ったら、\x01",
            "アルタイル土産の焼き栗を\x01",
            "列車の中で全部食べちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "もう、晩御飯が\x01",
            "食べられなくなっても\x01",
            "知りませんからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F90")

    label("loc_2F90")

    TalkEnd(0xFE)
    Return()

    # Function_20_2E43 end

    def Function_21_2F94(): pass

    label("Function_21_2F94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_303E")

    #C0115
    ChrTalk(
        0xFE,
        (
            "落石でも起こったのか？\x01",
            "それとも、人為的なものなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "もし人為的なものなのだとしたら……\x01",
            "目玉が飛び出るような賠償金を\x01",
            "犯人に請求してやるわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_303E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30DD")

    #C0117
    ChrTalk(
        0xFE,
        (
            "なんでも、国境門では\x01",
            "緊張状態が続いているようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "独立提唱なんてするから\x01",
            "そういうことになるんじゃ。\x01",
            "分を弁えねばならんぞ、若いの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327A")

    label("loc_30DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_30EB")
    Jump("loc_327A")

    label("loc_30EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_327A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3222")

    #C0119
    ChrTalk(
        0xFE,
        (
            "帝国のオズボーン宰相は、\x01",
            "自治州議会の前議長である\x01",
            "ハルトマンとつながっていたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "だが、ハルトマンが亡命した際に\x01",
            "帝国が追放処分を出した裏には、\x01",
            "宰相の根回しがあったと囁かれている。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "自分の不利益になりそうならば、\x01",
            "容赦なく切り捨てる。\x01",
            "《鉄血宰相》とはそういう男だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_327A")

    label("loc_3222")


    #C0122
    ChrTalk(
        0xFE,
        (
            "自分の不利益になりそうならば、\x01",
            "容赦なく切り捨てる。\x01",
            "《鉄血宰相》とはそういう男だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327A")

    TalkEnd(0xFE)
    Return()

    # Function_21_2F94 end

    def Function_22_327E(): pass

    label("Function_22_327E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32F6")

    #C0123
    ChrTalk(
        0xFE,
        (
            "鉄道が止まってしまうなんて、\x01",
            "一体どうなってしまうのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "ちゃんと国には帰れるのかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33E4")

    label("loc_32F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_338B")

    #C0125
    ChrTalk(
        0xFE,
        (
            "なんだい、あの金髪の子は。\x01",
            "さっきから妙に挙動不審だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "……なに、警察なのかい？\x01",
            "えらく頼りなさそうだけど\x01",
            "大丈夫なのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E4")

    label("loc_338B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3399")
    Jump("loc_33E4")

    label("loc_3399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33E4")

    #C0127
    ChrTalk(
        0xFE,
        "列車はまだ来ないのかねえ。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "いい加減待ちくたびれたわい。\x02",
    )

    CloseMessageWindow()

    label("loc_33E4")

    TalkEnd(0xFE)
    Return()

    # Function_22_327E end

    def Function_23_33E8(): pass

    label("Function_23_33E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_348A")

    #C0129
    ChrTalk(
        0xFE,
        (
            "列車がいつまでたっても\x01",
            "発車しないと思ったら……\x01",
            "脱線事故なんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "今日はクロスベルに泊まりかしら。\x01",
            "ホテルの部屋が取れるといいけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357F")

    label("loc_348A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34FE")

    #C0131
    ChrTalk(
        0xFE,
        (
            "今からカレシと一緒に\x01",
            "共和国に旅行なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "東方人街に温泉に……\x01",
            "たくさん楽しんでこなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357F")

    label("loc_34FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3576")

    #C0133
    ChrTalk(
        0xFE,
        (
            "クロスベルも、観光名所が\x01",
            "結構あるみたいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "バスも通ってるみたいだし、\x01",
            "色々行ってみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357F")

    label("loc_3576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_357F")

    label("loc_357F")

    TalkEnd(0xFE)
    Return()

    # Function_23_33E8 end

    def Function_24_3583(): pass

    label("Function_24_3583")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3600")

    #C0135
    ChrTalk(
        0xFE,
        (
            "一足先にチケットの\x01",
            "払い戻しを済ませたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "せっかくの旅行の予定だけど、\x01",
            "今回ばかりは仕方ないよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3719")

    label("loc_3600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3680")

    #C0137
    ChrTalk(
        0xFE,
        (
            "今からカノジョを\x01",
            "旅行に連れてくんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "そんなに色々回れるかなあ。\x01",
            "ミラが足りなかったらどうしよう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3719")

    label("loc_3680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_368E")
    Jump("loc_3719")

    label("loc_368E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3719")

    #C0139
    ChrTalk(
        0xFE,
        (
            "今、クロスベルでは\x01",
            "通商会議ってのを\x01",
            "やってるんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "噂になってた\x01",
            "オルキスタワーってやつ、\x01",
            "見に行ってみようかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3719")

    TalkEnd(0xFE)
    Return()

    # Function_24_3583 end

    def Function_25_371D(): pass

    label("Function_25_371D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_374E")

    #C0141
    ChrTalk(
        0xFE,
        "ねえねえ、何かあったの～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_374E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3793")

    #C0142
    ChrTalk(
        0xFE,
        (
            "ちくたく……ちくたく……\x01",
            "時計が……まわるるる……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_3793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3825")

    #C0143
    ChrTalk(
        0xFE,
        (
            "げっぷ……\x01",
            "アルタイル市、すっごく楽しかったー。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "キュレー河っていうおっきな河があってね、\x01",
            "お船もいっぱい通ってるんだよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_382E")

    label("loc_3825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_382E")

    label("loc_382E")

    TalkEnd(0xFE)
    Return()

    # Function_25_371D end

    def Function_26_3832(): pass

    label("Function_26_3832")

    TalkBegin(0xFE)

    #C0145
    ChrTalk(
        0xFE,
        (
            "おいおい、マジかよ……\x01",
            "共和国からの貨物はどうするんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "ひとまずオヤジに相談して\x01",
            "配送先にも連絡して……\x01",
            "うう、忙しくなりそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_3832 end

    def Function_27_38C6(): pass

    label("Function_27_38C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38EB")
    Call(0, 33)
    Return()

    label("loc_38EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4B")

    #C0147
    ChrTalk(
        0xFE,
        (
            "#12400Fオリビエ・レンハイムは、\x01",
            "白いコートにリュートという\x01",
            "出で立ちをした演奏家だ。\x02\x03",

            "いかがわしい場所、\x01",
            "賑やかな場所や食事処などが\x01",
            "行き先として考えられるだろう。\x02\x03",

            "先ほど諸君が挙げてくれた、\x01",
            "旧市街、裏通り、港湾区などは\x01",
            "いい線だと言えるはずだ。\x02\x03",

            "連れてくるのに苦労するなら\x01",
            "多少、痛い目にあわせて構わない。\x01",
            "どうかよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3B56")

    label("loc_3A4B")


    #C0148
    ChrTalk(
        0xFE,
        (
            "#12400Fオリビエの行き先としては、\x01",
            "いかがわしい場所、賑やかな場所や\x01",
            "食事処などが考えられるだろう。\x02\x03",

            "先ほど諸君が挙げてくれた、\x01",
            "旧市街、裏通り、港湾区などは\x01",
            "いい線だと言えるはずだ。\x02\x03",

            "連れてくるのに苦労するなら\x01",
            "多少、痛い目にあわせて構わない。\x01",
            "どうかよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B56")

    TalkEnd(0xFE)
    Return()

    # Function_27_38C6 end

    def Function_28_3B5A(): pass

    label("Function_28_3B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8C")
    Call(0, 36)
    Jump("loc_3B8F")

    label("loc_3B8C")

    Call(0, 37)

    label("loc_3B8F")

    Return()

    label("loc_3B90")

    Return()

    # Function_28_3B5A end

    def Function_29_3B91(): pass

    label("Function_29_3B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC4")
    Call(0, 42)
    Jump("loc_3BC7")

    label("loc_3BC4")

    Call(0, 43)

    label("loc_3BC7")

    Return()

    label("loc_3BC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDA")
    Jump("loc_3BDA")

    label("loc_3BDA")

    TalkEnd(0xFE)
    Return()

    # Function_29_3B91 end

    def Function_30_3BDE(): pass

    label("Function_30_3BDE")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_30_3BDE end

    def Function_31_3BE8(): pass

    label("Function_31_3BE8")

    TalkBegin(0xFE)
    Call(0, 32)
    TalkEnd(0xFE)
    Return()

    # Function_31_3BE8 end

    def Function_32_3BF2(): pass

    label("Function_32_3BF2")

    OP_4B(0x1B, 0xFF)
    OP_4B(0x1C, 0xFF)

    #C0149
    ChrTalk(
        0x1B,
        (
            "……やはりやつらは\x01",
            "列車で逃げるつもりのようだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x1C,
        (
            "……フン、浅はかな……\x01",
            "我々から逃げられるとでも……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)
    OP_4C(0x1C, 0xFF)
    Return()

    # Function_32_3BF2 end

    def Function_33_3C73(): pass

    label("Function_33_3C73")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBA")
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12400.itp")
    Jump("loc_3CBF")

    label("loc_3CBA")

    Fade(500)

    label("loc_3CBF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D63")
    FadeToBright(500, 0)

    label("loc_3D63")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4408")

    #N0151
    NpcTalk(
        0x18,
        "黒服の大男",
        "#12400F…………………………\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        (
            "#6P#00305F（おいロイド……\x01",
            "  なんだかすげえ雰囲気の\x01",
            "  ヤツがいるみてえだが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#6P#00003F（もしかして、\x01",
            "  今回の依頼者って……）\x02\x03",

            "#00000Fあの、すみません。\x01",
            "特務支援課の者ですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0154
    NpcTalk(
        0x18,
        "黒服の大男",
        (
            "#12404F……お待ちしていた。\x01",
            "来てくれて感謝する。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("黒服の大男")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            "自分の名はミュラー……\x01",
            "帝国で音楽マネージャーを\x01",
            "している者だ。\x02\x03",

            "短い間だが、\x01",
            "どうかお見知りおき願おう。\x02",
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
            "#6P#00006Fお、音楽マネージャー……ですか。\x01",
            "（全然そうは見えないけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        (
            "#6P#10101F（どちらかというと\x01",
            "  ＳＰって感じの雰囲気ですよね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#6P#00105F（それに前にも似たような肩書きを\x01",
            "  聞いた事があるような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x18,
        "#12405F……どうかしたのかね？\x02",
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
            "#6P#00012Fい、いえ……\x02\x03",

            "#00000Fえ、えっと……\x01",
            "それでは依頼について\x01",
            "詳しく説明をいただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x105,
        (
            "#6P#10304F確か『演奏家』が行方不明に\x01",
            "なったとかいう話だったね。\x02\x03",

            "#10302F察するに、あなたが\x01",
            "マネジメントしている人なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x18,
        (
            "#12400Fああ、その通り。\x02\x03",

            "自分たちは、演奏旅行のため\x01",
            "クロスベル入りしたのだが……\x02\x03",

            "#12406F少し目を離した隙に、\x01",
            "その演奏家とはぐれてしまってな。\x02\x03",

            "#12400F勝手の分からない街で探すアテもなく、\x01",
            "困っていたところだったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそれは、確かに大変そうですね……\x01",
            "クロスベル市は広いですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x18,
        (
            "#12401Fああ、それもあるが……\x01",
            "少々厄介な問題もある。\x02\x03",

            "#12400F早速、捜索を頼めるだろうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x76, 0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Jump("loc_4473")

    label("loc_4408")


    #C0165
    ChrTalk(
        0x18,
        (
            "#12400F君たちには、\x01",
            "市内で行方不明になった\x01",
            "『演奏家』の捜索を頼みたい。\x02\x03",

            "早速、捜索を頼めるだろうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4473")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C9")
    Call(0, 34)
    Jump("loc_45A1")

    label("loc_44C9")


    #C0166
    ChrTalk(
        0x101,
        (
            "#6P#00006Fその……\x01",
            "申し訳ありません。\x02\x03",

            "今、他に仕事を抱えていまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x18,
        (
            "#12405Fふむ……\x01",
            "それは残念だ。\x02\x03",

            "#12400Fもし手が空いたら\x01",
            "声をかけてくれると助かる。\x02\x03",

            "なにせ、こっちも急ぎでな。\x01",
            "どうかよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x156, 1)

    label("loc_45A1")

    SetChrPos(0x0, 17460, 0, -4190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_33_3C73 end

    def Function_34_45C3(): pass

    label("Function_34_45C3")


    #C0168
    ChrTalk(
        0x101,
        (
            "#6P#00000F了解しました、\x01",
            "お任せください。\x02\x03",

            "#00000Fそれでは、捜索する\x01",
            "『演奏家』について\x01",
            "詳しくお聞かせ願えますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x18,
        (
            "#12400Fうむ、よかろう。\x02\x03",

            "演奏家の名は……\x01",
            "『オリビエ・レンハイム』。\x02\x03",

            "２０代の金髪の男で、\x01",
            "白いコートを羽織り\x01",
            "リュートを携えている。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x105,
        (
            "#6P#10305Fふむ、楽器を持ってるとなると\x01",
            "なかなか目立ちそうだね。\x02\x03",

            "#10300F探すのはそこまで難しく\x01",
            "なさそうな気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x18,
        (
            "#12400Fああ、それだけなら\x01",
            "探して連れ帰るのには\x01",
            "さほど問題はないのだが……\x02\x03",

            "#12406Fオリビエは、\x01",
            "少々性格に問題があってな。\x02\x03",

            "頼んでもいないのに\x01",
            "自ら面倒事に首を突っ込み、\x01",
            "更なる面倒事にしてしまう。\x02\x03",

            "#12400F正直言って、厄介な人物と\x01",
            "言ってしまっていいだろう。\x02",
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
        "#6P#00105Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x18,
        (
            "#12400F演奏旅行に支障がないよう、\x01",
            "速やかに探し出して欲しいが……\x01",
            "まあ、そこまで高望みはすまい。\x02\x03",

            "#12406Fせめて、悪目立ちする前に\x01",
            "ふん捕まえてくれると助かるが。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#6P#00306Fマ、マネージャーにしちゃ\x01",
            "随分な物言いッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#6P#00003Fと、とりあえずイメージは\x01",
            "ある程度つかめました。\x02\x03",

            "#00000Fあとは、行きそうな場所に\x01",
            "心当たりはないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x18,
        (
            "#12405Fそうだな、強いて言うなら……\x02\x03",

            "#12400Fいかがわしい場所、\x01",
            "あるいは賑やかな場所を\x01",
            "好む傾向にあるだろう。\x02\x03",

            "#12406F美食家ぶって、どこぞの食事処に\x01",
            "居座っている可能性もあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x109,
        (
            "#6P#10101Fとにかくトラブルの火種が\x01",
            "ありそうな場所ってことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x105,
        (
            "#6P#10300Fだとすると、\x01",
            "旧市街や歓楽街、裏通り……\x01",
            "そのあたりが考えられそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x18,
        (
            "#12404Fああ、いい線だと言えるが……\x02\x03",

            "#12400F……実は、歓楽街は\x01",
            "すでに一通り探し終えていてな。\x01",
            "探索範囲から外して構わないはずだ。\x02\x03",

            "#12406Fおそらく俺が探しに来ると踏んで\x01",
            "いかにもな場所は避けているのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#6P#00106Fな、なるほど……\x02\x03",

            "#00100Fでも、賑やかそうな場所といったら\x01",
            "今日は港湾区も入るかもしれませんね。\x02\x03",

            "#00100F確か、公園でみっしぃの\x01",
            "出張イベントをやっているはずですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x18,
        (
            "#12400Fふむ……\x01",
            "まあ絞り込めそうなのは\x01",
            "そんなところだろうか。\x02\x03",

            "#12406Fすまない、もう少し大した情報を\x01",
            "提供できればよかったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00012Fいえ、参考になりました。\x02\x03",

            "#00000Fそれでは、早速捜査に\x01",
            "当たらせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x18,
        (
            "#12400Fどうかよろしく頼む。\x02\x03",

            "連れてくるのに苦労するなら\x01",
            "多少、痛い目にあわせても\x01",
            "構わないからな。\x02",
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
            "#6P#00006Fりょ、了解しました……\x01",
            "（ほんと、どんな関係なんだ？）\x02",
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
            "クエスト【演奏家の捜索】\x07\x00",
            "を開始した！\x02",
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

    # Function_34_45C3 end

    def Function_35_4F87(): pass

    label("Function_35_4F87")

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

    def lambda_5049():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5049)
    Sleep(50)

    def lambda_5066():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5066)
    Sleep(50)

    def lambda_5083():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5083)
    Sleep(50)

    def lambda_50A0():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_50A0)
    Sleep(50)

    def lambda_50BD():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_50BD)
    Sleep(50)

    def lambda_50DA():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50DA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x104, 1)

    #C0186
    ChrTalk(
        0x101,
        (
            "#00000Fさてと、クロスベル駅に\x01",
            "やって来たわけだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00100F確か、駅の臨検官さんが\x01",
            "支援要請を出していたのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00000Fああ、さっそく訪ねよう。\x02",
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

    # Function_35_4F87 end

    def Function_36_51DA(): pass

    label("Function_36_51DA")

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
            "おや、もしかして\x01",
            "君たちが特務支援課かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#00000Fはい、支援要請を見て\x01",
            "伺いました。\x02\x03",

            "共和国臨検官の方で\x01",
            "よろしかったですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x19,
        (
            "いかにも、カルバード共和国軍から\x01",
            "出向している臨検官のマーロウだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x19,
        (
            "さっそく仕事の説明したいんだが、\x01",
            "依頼を受けてくれるんだね？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_36_51DA end

    def Function_37_53A9(): pass

    label("Function_37_53A9")

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
            "ふむ、君たちか。\x01",
            "依頼を受けてくれるんだね？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    EventEnd(0x5)
    Return()

    # Function_37_53A9 end

    def Function_38_549B(): pass

    label("Function_38_549B")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "依頼を受ける\x01",      # 0
            "やめておく\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5543")

    #C0194
    ChrTalk(
        0x101,
        "#00000Fはい、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x19,
        (
            "ありがたい。\x01",
            "では説明させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 39)
    Jump("loc_562D")

    label("loc_5543")


    #C0196
    ChrTalk(
        0x101,
        (
            "#00003Fすみません、\x01",
            "今は他にも仕事を抱えていて……\x02\x03",

            "また後で伺ってもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x19,
        (
            "ふむ、まあ多少であれば\x01",
            "融通は利くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x19,
        (
            "何分こちらも忙しくてね。\x01",
            "なるべく早めにお願いするよ。\x02",
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

    label("loc_562D")

    Return()

    # Function_38_549B end

    def Function_39_562E(): pass

    label("Function_39_562E")


    #C0199
    ChrTalk(
        0x19,
        (
            "さて、君たちに\x01",
            "頼みたいのは他でもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x19,
        (
            "共和国行き列車の臨検作業、\x01",
            "その手伝いをお願いしたいんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5796")

    #C0201
    ChrTalk(
        0x101,
        (
            "#00005F列車の臨検、ですか。\x02\x03",

            "#00000F以前に一度、帝国臨検官の\x01",
            "仕事を手伝ったことがあるので\x01",
            "大体分かると思います。\x02\x03",

            "不審者や不審物の類いが\x01",
            "列車に乗っていないかを\x01",
            "チェックするんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x19,
        (
            "その通りだ。\x01",
            "経験があるなら話は早いな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_582D")

    label("loc_5796")


    #C0203
    ChrTalk(
        0x101,
        (
            "#00003F臨検、というと……\x02\x03",

            "#00000F不審者や不審物の類いが\x01",
            "列車に乗っていないかを\x01",
            "チェックするわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x19,
        (
            "その通りだ。\x01",
            "理解が早くて助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582D")


    #C0205
    ChrTalk(
        0x19,
        (
            "なにせ、今は通商会議で\x01",
            "どこもかしこも警戒レベルが\x01",
            "上がっている状況だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x19,
        (
            "普段より厳密な確認態勢に加えて\x01",
            "警察への協力などもあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x19,
        (
            "今は臨検官の手がいくらあっても\x01",
            "足りない状況なんだよ。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0x1F4)
    Sound(801, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("駅員の声")

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……まもなく、１番ホームに\x01",
            "共和国行き列車が到着いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ご乗車の方は\x01",
            "足もとにお気をつけの上、\x01",
            "ホームにお急ぎ下さいませ。\x07\x00\x02",
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
            "どうやら目的の列車が\x01",
            "来たようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x19,
        (
            "詳しくは、ホームで\x01",
            "話をさせてもらうよ。\x02",
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
            "クエスト【共和国臨検官の作業補助】\x07\x00",
            "を開始した！\x02",
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

    # Function_39_562E end

    def Function_40_5A7F(): pass

    label("Function_40_5A7F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 4)), scpexpr(EXPR_END)), "loc_5C7B")

    #C0213
    ChrTalk(
        0x101,
        (
            "#5P#00006Fさっきは入口に\x01",
            "鍵が掛かっていたけど……\x02\x03",

            "#00013Fどうやらキリカさんたちが\x01",
            "外したみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C36")

    #C0214
    ChrTalk(
        0x10A,
        (
            "#00601F#6Pフン、非常事とはいえ、\x01",
            "相変わらず勝手なことを……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C7B")

    #C0215
    ChrTalk(
        0x109,
        (
            "#10108F#6P違法ですから\x01",
            "感心はできませんけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7B")


    #C0216
    ChrTalk(
        0x104,
        (
            "#6P#00306Fしっかし誰もいねぇな。\x02\x03",

            "#00301F大陸横断鉄道が\x01",
            "止まってるなら仕方ねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#5P#00106Fそうね……鉄道公社の人や\x01",
            "帝国・共和国の臨検官も\x01",
            "国外退去させられたみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        (
            "#6P#00200Fキリカさんとレクターさんは\x01",
            "３番ホームの列車でしたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#5P#00001Fああ……\x01",
            "ホームに降りてみよう。\x02",
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

    # Function_40_5A7F end

    def Function_41_5DD3(): pass

    label("Function_41_5DD3")

    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(900)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(600)

    def lambda_5DEC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DEC)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_41_5DD3 end

    def Function_42_5E09(): pass

    label("Function_42_5E09")

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
        "……あっ、君たち～！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x1A,
        (
            "良かった、依頼を見て\x01",
            "来てくれたんだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00000Fお疲れ様です、\x01",
            "レイモンドさん。\x02\x03",

            "#00005F……あれ、お１人ですか？\x01",
            "ドノバン警部は……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x1A,
        (
            "ああ、ちょっと\x01",
            "いろいろあってね～……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x1A,
        (
            "手短に、事情を\x01",
            "話させてもらっていいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#00100Fよろしくお願いします。\x02\x03",

            "#00101F依頼では、また偽ブランド商を\x01",
            "追いかけているらしいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x1A,
        "ああ、そうなんだ。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1A,
        (
            "新市長が行った法改正で\x01",
            "偽ブランド商をきちんと\x01",
            "取り締まれる決まりができてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x1A,
        (
            "二課でも本腰を入れて\x01",
            "取締りが強化されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x1A,
        (
            "そんな中、\x01",
            "例の偽ブランド商が\x01",
            "クロスベル入りしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x1A,
        (
            "粘り強く張り込んだおかげで、\x01",
            "ついにその取引現場を\x01",
            "抑えることに成功したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10103F偽ブランド商……\x01",
            "あの、タングラム門経由で来た\x01",
            "旅行客の誰かでしたよね。\x02\x03",

            "#10105Fそういえば結局、\x01",
            "どういう人物だったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00000Fそういえば、乗客の誘導には\x01",
            "ノエルに手伝ってもらったっけ。\x02\x03",

            "#00003Fうーん、そうだな……\x02",
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
        "#00200F口が悪いです。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#00106Fビックリするくらい\x01",
            "声が大きいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#00303Fスプリンター並に\x01",
            "足が速ぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#00012Fとにかく、一言で表すなら\x01",
            "“とんでもない人”……かな。\x02",
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
        "#10105Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、面白そうだし\x01",
            "是非とも会ってみたいものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#00309F……まあ、なんにしろ\x01",
            "大金星じゃねえか！\x02\x03",

            "あのバーさんを\x01",
            "追い詰めちまうなんてよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x1A,
        (
            "うん、まあ……\x01",
            "そこまではよかったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x1A,
        (
            "そのあと、結局\x01",
            "逃げられちゃったんだよね。\x01",
            "……すんごいスピードで。\x02",
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
        "#00206Fあのお婆さんも懲りませんね……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x105,
        (
            "#10300Fそれで……\x01",
            "逃げた偽ブランド商が\x01",
            "この駅の中にいるってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x1A,
        (
            "ああ、そのとおり！\x01",
            "さすが、察しがいいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1A,
        (
            "どうやら彼女、帝国方面に\x01",
            "高飛びするつもりらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1A,
        (
            "ふふ、完全に警察を撒いたと\x01",
            "思ってるんじゃないかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x1A,
        (
            "２番ホームをのぞいたけど、\x01",
            "悠々と列車を待ってるみたいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#00100F帝国行きが到着するまで\x01",
            "まだ時間があるし……\x01",
            "捕まえるには絶好の機会ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        (
            "#00305F……ん？\x01",
            "そこまでお膳立てが\x01",
            "整ってるってことは……\x02\x03",

            "#00303F俺たちがやることなんて\x01",
            "ほとんどないんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1A,
        "そ、そこなんだけどね～。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x1A,
        (
            "ドノバン警部が忙しいらしくて、\x01",
            "この件は僕に一任されたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x1A,
        (
            "だけど……どうも僕一人で\x01",
            "あの偽ブランド商を抑える\x01",
            "自信がなくってさあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#00006Fう、うーん。\x01",
            "自信の有り無しは置いといても……\x01",
            "人手不足なのは確かですね。\x02\x03",

            "#00001Fこの広い駅の中だと、\x01",
            "ちゃんと包囲網を敷かないと\x01",
            "逃げられる可能性が高そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x1A,
        (
            "だろ～？\x01",
            "だから、君たちに応援を\x01",
            "要請したってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x1A,
        (
            "頼みたいのは、\x01",
            "僕と一緒に偽ブランド商を\x01",
            "逮捕するサポート役。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x1A,
        (
            "それと、偽ブランド商が\x01",
            "駅から出られないように\x01",
            "見張る役だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x1A,
        (
            "一度偽ブランド商を捕まえた\x01",
            "君たちなら、と思ったんだけど、\x01",
            "手伝ってもらえるかな～？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x0)
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_42_5E09 end

    def Function_43_6A00(): pass

    label("Function_43_6A00")

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
            "頼みたいのは、\x01",
            "僕と一緒に偽ブランド商を\x01",
            "逮捕するサポート役。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1A,
        (
            "それと、偽ブランド商が\x01",
            "駅から出られないように\x01",
            "見張る役だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1A,
        (
            "一度偽ブランド商を捕まえた\x01",
            "君たちなら、と思ったんだけど、\x01",
            "手伝ってもらえるかな～？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 44)
    EventEnd(0x5)
    Return()

    # Function_43_6A00 end

    def Function_44_6BA5(): pass

    label("Function_44_6BA5")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

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
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BF8")
    Jump("loc_6D19")

    label("loc_6BF8")


    #C0261
    ChrTalk(
        0x101,
        (
            "#00006F……すみません、\x01",
            "今は他の仕事がありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x1A,
        (
            "うーん、そっか～。\x01",
            "それは仕方ないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1A,
        (
            "それじゃあ、\x01",
            "僕はもう少しここで\x01",
            "機を待つことにするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x1A,
        (
            "時間が空いたら、\x01",
            "是非手伝いにきてくれると\x01",
            "助かるかな～。\x02",
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

    label("loc_6D19")


    #C0265
    ChrTalk(
        0x101,
        (
            "#00000F……そうですね、分かりました。\x01",
            "是非、協力させてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x1A,
        (
            "おお、ありがとう！\x01",
            "恩に着るよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x1A,
        (
            "それじゃあ……まずは\x01",
            "僕と一緒に偽ブランド商を\x01",
            "逮捕するグループを決めよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x1A,
        (
            "こちら側には誰が\x01",
            "ついてきてくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#00003Fええっと……\x01",
            "振り分けはどうしようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#00203Fロイドさんは、捜査官として\x01",
            "同行したほうがいいと思います。\x02\x03",

            "#00211F……レイモンドさんだけでは\x01",
            "微妙に心配ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x1A,
        "そ、そりゃないよ～……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1A,
        (
            "……と言いたいところだけど、\x01",
            "確かにそのほうが安心かな～。\x02",
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
            "#00012Fえ、えっと……\x01",
            "一応捜査官２人体制ってことか。\x02\x03",

            "#00000Fもう一人サポートにきてもらって、\x01",
            "残りの４人で駅の見張りを\x01",
            "固めるのがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        (
            "#00100Fそれじゃあ……\x01",
            "あとは誰を連れていく？\x02",
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
            "エリィを連れて行く\x01",        # 0
            "ティオを連れて行く\x01",        # 1
            "ランディを連れて行く\x01",      # 2
            "ノエルを連れて行く\x01",        # 3
            "ワジを連れて行く\x01",          # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70FE")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x102, 500)

    #C0275
    ChrTalk(
        0x101,
        "#00000Fエリィ、ついて来てくれ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0276
    ChrTalk(
        0x102,
        "#00100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x1)
    Jump("loc_72AE")

    label("loc_70FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716B")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x103, 500)

    #C0277
    ChrTalk(
        0x101,
        "#00000Fティオ、ついて来てくれ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0278
    ChrTalk(
        0x103,
        "#00200F了解です。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x2)
    Jump("loc_72AE")

    label("loc_716B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D8")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x104, 500)

    #C0279
    ChrTalk(
        0x101,
        "#00000Fランディ、ついて来てくれ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0280
    ChrTalk(
        0x104,
        "#00309Fあいよ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x3)
    Jump("loc_72AE")

    label("loc_71D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7249")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x109, 500)

    #C0281
    ChrTalk(
        0x101,
        "#00000Fノエル、ついて来てくれ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0282
    ChrTalk(
        0x109,
        "#10100Fイエス・サー！\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x4)
    Jump("loc_72AE")

    label("loc_7249")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x105, 500)

    #C0283
    ChrTalk(
        0x101,
        "#00000Fワジ、ついて来てくれ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0284
    ChrTalk(
        0x105,
        "#10304F仰せのままに、リーダー。\x02",
    )

    CloseMessageWindow()
    OP_29(0x81, 0x1, 0x5)

    label("loc_72AE")

    TurnDirection(0x101, 0x104, 500)

    #C0285
    ChrTalk(
        0x101,
        (
            "#00003F残りのみんなは\x01",
            "駅の出入りを監視してくれ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_72F0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72F0)
    Sleep(50)

    def lambda_7300():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7300)
    Sleep(50)

    def lambda_7310():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7310)
    Sleep(50)

    def lambda_7320():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7320)
    Sleep(100)

    #C0286
    ChrTalk(
        0x101,
        (
            "#00001Fあのお婆さんのことだから\x01",
            "万が一ってこともありうる。\x01",
            "十分に注意をしてくれ。\x02",
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

    def lambda_740D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_740D)

    def lambda_741A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_741A)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)

    #C0287
    ChrTalk(
        0x1B,
        (
            "……やつら、構内には\x01",
            "見当たらないようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x1C,
        (
            "すでに列車に\x01",
            "乗っているのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x1C,
        "……急ぐぞ。\x02",
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
            "クエスト【偽ブランド商の追跡】\x07\x00",
            "を開始した！\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C1")
    AddParty(0x1, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 3)
    Jump("loc_7619")

    label("loc_75C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75DC")
    AddParty(0x2, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 4)
    Jump("loc_7619")

    label("loc_75DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F7")
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 5)
    Jump("loc_7619")

    label("loc_75F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7612")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 6)
    Jump("loc_7619")

    label("loc_7612")

    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x179, 7)

    label("loc_7619")

    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_44_6BA5 end

    def Function_45_7637(): pass

    label("Function_45_7637")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_774F")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_767A"),
        (1, "loc_7694"),
        (2, "loc_76AE"),
        (3, "loc_76C8"),
        (4, "loc_76E2"),
        (5, "loc_76FC"),
        (6, "loc_7716"),
        (SWITCH_DEFAULT, "loc_7730"),
    )


    label("loc_767A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_7694")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_774A")

    label("loc_76AE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_774A")

    label("loc_76C8")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_76E2")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_774A")

    label("loc_76FC")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_774A")

    label("loc_7716")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_7730")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_774A")

    label("loc_774A")

    Jump("Function_45_7637")

    label("loc_774F")

    Return()

    # Function_45_7637 end

    def Function_46_7750(): pass

    label("Function_46_7750")

    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_46_7750 end

    def Function_47_776F(): pass

    label("Function_47_776F")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1000)
    Return()

    # Function_47_776F end

    def Function_48_778E(): pass

    label("Function_48_778E")

    Sleep(600)
    OP_95(0xFE, 19770, 30, 7340, 2000, 0x0)
    OP_95(0xFE, 23810, 0, 7440, 2000, 0x0)
    Return()

    # Function_48_778E end

    def Function_49_77BA(): pass

    label("Function_49_77BA")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 19710, 30, 8420, 2000, 0x0)
    Sound(100, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_95(0xFE, 23490, 0, 8520, 2000, 0x0)
    Return()

    # Function_49_77BA end

    def Function_50_7803(): pass

    label("Function_50_7803")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_7A39")

    #C0291
    ChrTalk(
        0x104,
        (
            "#00306Fロイドたちが\x01",
            "共和国に行っちまったって\x01",
            "聞いた時は驚いたもんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#00200Fそんなことになってたんですね。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、連絡もいれずに\x01",
            "ごめんなさいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#00012Fまあ、とりあえず\x01",
            "偽ブランド商は捕まったし\x01",
            "結果オーライってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x105,
        "#10300Fフフ、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        "#10109Fあはは、よしとしましょうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_7B9B")

    #C0297
    ChrTalk(
        0x102,
        (
            "#00106Fロイドたちが\x01",
            "共和国に行ってしまったと\x01",
            "聞いた時は驚いたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#00300Fやれやれ、そんなことに\x01",
            "なってたとはなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#00203F連絡を入れればよかったですね。\x01",
            "申し訳ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        (
            "#00012Fまあ、とりあえず\x01",
            "偽ブランド商は捕まったし\x01",
            "結果オーライってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x105,
        "#10300Fフフ、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x109,
        "#10109Fあはは、よしとしましょうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_7CFB")

    #C0303
    ChrTalk(
        0x109,
        (
            "#10106Fロイドさんたちが\x01",
            "共和国に行ってしまったと\x01",
            "聞いた時は驚きましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x105,
        (
            "#10300Fやれやれ、まさか\x01",
            "そんなことになってたとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x104,
        (
            "#00309Fはは、ワリワリ。\x01",
            "緊急事態だったもんでよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00012Fまあ、とりあえず\x01",
            "偽ブランド商は捕まったし\x01",
            "結果オーライってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#00100Fふふ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x103,
        "#00204Fまあ、よしとしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_7E51")

    #C0309
    ChrTalk(
        0x105,
        (
            "#10306Fロイドたちが\x01",
            "共和国に行ったって聞いた時は\x01",
            "流石の僕も驚いたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#00300Fやれやれ、そんなことに\x01",
            "なってたとはなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10109Fあはは……\x01",
            "すみません、連絡もいれずに。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#00012Fまあ、とりあえず\x01",
            "偽ブランド商は捕まったし\x01",
            "結果オーライってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#00100Fふふ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#00204Fまあ、よしとしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F9B")

    label("loc_7E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_7F9B")

    #C0315
    ChrTalk(
        0x109,
        (
            "#10106Fロイドさんたちが\x01",
            "共和国に行ってしまったと\x01",
            "聞いた時は驚きましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#00300Fやれやれ、そんなことに\x01",
            "なってたとはなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x105,
        "#10309Fフフ、非常事態だったからね。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#00012Fまあ、とりあえず\x01",
            "偽ブランド商は捕まったし\x01",
            "結果オーライってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        "#00100Fふふ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#00204Fまあ、よしとしましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_7F9B")


    #C0321
    ChrTalk(
        0x1A,
        (
            "さて、僕も捜査二課のデスクで\x01",
            "調書を作らないといけないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x1A,
        "この辺で失礼させてもらうよ。\x02",
    )

    CloseMessageWindow()

    def lambda_8003():

        label("loc_8003")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8003")

    QueueWorkItem2(0x103, 1, lambda_8003)

    def lambda_8015():

        label("loc_8015")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8015")

    QueueWorkItem2(0x104, 1, lambda_8015)

    def lambda_8027():

        label("loc_8027")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8027")

    QueueWorkItem2(0x109, 1, lambda_8027)

    def lambda_8039():

        label("loc_8039")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_8039")

    QueueWorkItem2(0x105, 1, lambda_8039)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 3)), scpexpr(EXPR_END)), "loc_807A")

    #C0323
    ChrTalk(
        0x102,
        "#00109Fふふ、お疲れ様でした。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_807A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 4)), scpexpr(EXPR_END)), "loc_80AB")

    #C0324
    ChrTalk(
        0x103,
        "#00202Fどうもお疲れ様でした。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_80AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 5)), scpexpr(EXPR_END)), "loc_80D4")

    #C0325
    ChrTalk(
        0x104,
        "#00309Fはは、お疲れ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_80D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 6)), scpexpr(EXPR_END)), "loc_8105")

    #C0326
    ChrTalk(
        0x109,
        "#10109Fふふっ、お疲れ様です！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8131")

    label("loc_8105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 7)), scpexpr(EXPR_END)), "loc_8131")

    #C0327
    ChrTalk(
        0x105,
        "#10302Fフフ、お疲れだったね。\x02",
    )

    CloseMessageWindow()

    label("loc_8131")


    #C0328
    ChrTalk(
        0x1A,
        (
            "いや、今回は君たちに\x01",
            "最後まで助けられちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x1A,
        (
            "僕一人じゃ絶対に\x01",
            "あのお婆さんを捕まえられは\x01",
            "しなかったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x1A,
        "今日は本当にありがとう！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00004Fいえ、こちらこそ。\x02\x03",

            "#00000Fまた何かあったら\x01",
            "支援課までご連絡ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x1A,
        "ああ、よろしく頼むよ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)

    def lambda_8245():
        OP_95(0xFE, 3980, 30, 220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8245)
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
            "クエスト【偽ブランド商の追跡】\x07\x00",
            "を達成した！\x02",
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

    # Function_50_7803 end

    def Function_51_830A(): pass

    label("Function_51_830A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "←共和国方面行き・１番線ホーム\x01",
            "　　　共和国アルタイル市　３５分\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_51_830A end

    def Function_52_8382(): pass

    label("Function_52_8382")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "帝国方面行き・２番線ホーム→\x01",
            "　　　　帝国ガレリア要塞　　３２分\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_8382 end

    def Function_53_83FA(): pass

    label("Function_53_83FA")

    TalkBegin(0xFF)
    SetChrName("")

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州周辺の\x01",
            "時刻表がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_53_83FA end

    def Function_54_8433(): pass

    label("Function_54_8433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_844A")
    Call(0, 56)
    Return()

    label("loc_844A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※※　臨検官事務所　※※\x01",
            " 関係者以外の立ち入りを\x01",
            "      固く禁ずる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_54_8433 end

    def Function_55_84C6(): pass

    label("Function_55_84C6")

    TalkBegin(0xFF)
    SetChrName("")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州周辺の\x01",
            "路線図がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_55_84C6 end

    def Function_56_84FF(): pass

    label("Function_56_84FF")

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
            "#12P#00200F……やっぱり中には\x01",
            "誰もいないみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        (
            "#6P#00103F鉄道も運行が休止されて、\x01",
            "帝国、共和国の臨検官は\x01",
            "軒並み退去させられたんでしょう。\x02\x03",

            "#00100F駅員さんたちも、\x01",
            "今はそれぞれ別の場所に\x01",
            "避難しているんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#12P#00303Fまあ、こんな場所に残る理由も\x01",
            "あんまりねえだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#5P#00000F今はキリカさんたちに\x01",
            "会いに行こう。\x02\x03",

            "ホームへは下の階の入口から\x01",
            "降りられるはずだ。\x02",
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

    # Function_56_84FF end

    SaveToFile()

Try(main)
