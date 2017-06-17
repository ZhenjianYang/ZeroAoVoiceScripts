from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1510.bin",                # FileName
        "t1510",                    # MapName
        "t1510",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1510",                  # 0
        "キルシュ寮長",           # 1
        "研修医フローラ",         # 2
        "研修医ミショー",         # 3
        "見舞い客",               # 4
        "見舞い客",               # 5
        "見舞い客",               # 6
        "見舞い客",               # 7
        "見舞い客",               # 8
        "ポリセ",                 # 9
        "タップ",                 # 10
        "見舞い客",               # 11
        "男性",                   # 12
        "見舞い客",               # 13
        "セシル",                 # 14
        "神狼ツァイト",           # 15
        "遊撃士リン",             # 16
        "遊撃士エオリア",         # 17
        "フラン",                 # 18
    ))

    AddCharChip((
        "chr/ch05302.itc",                   # 00
        "chr/ch02710.itc",                   # 01
        "chr/ch24300.itc",                   # 02
        "chr/ch29502.itc",                   # 03
        "chr/ch45300.itc",                   # 04
        "chr/ch45302.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch23000.itc",                   # 08
        "chr/ch20800.itc",                   # 09
        "chr/ch20902.itc",                   # 0A
        "chr/ch21900.itc",                   # 0B
        "chr/ch21000.itc",                   # 0C
        "chr/ch36300.itc",                   # 0D
        "chr/ch24400.itc",                   # 0E
        "chr/ch02702.itc",                   # 0F
        "chr/ch32002.itc",                   # 10
        "chr/ch32100.itc",                   # 11
        "chr/ch32102.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-4809,   0,       11600,   225,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-12069,  150,     14399,   180,  261,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-10409,  0,       13079,   322,  261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(59330,   300,     -3079,   180,  389,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(59630,   0,       -4260,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(55229,   0,       -800,    135,  389,  0x0, 0,   8,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(55909,   0,       53659,   225,  389,  0x0, 0,   9,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(51729,   600,     52340,   180,  389,  0x0, 0,   10,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(3480,    0,       8439,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3500,    0,       6590,    0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(55250,   0,       -2039,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(55250,   0,       -1039,   180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(56090,   0,       53569,   225,  389,  0x0, 0,   9,   0,   0,   3,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-12069,  0,       3589,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-9579,   0,       7340,    45,   389,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-6100,   0,       10440,   1000,    -4810,   1500,    11600,   0x007E, 0,  6,  0x0000)
    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  26, 0x0000)
    DeclActor(5830,    0,       11730,   1200,    5830,    1500,    11730,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(1016, 0)                                       # 0

    ScpFunction((
        "Function_0_3F8",          # 00, 0
        "Function_1_4A8",          # 01, 1
        "Function_2_4D3",          # 02, 2
        "Function_3_4FE",          # 03, 3
        "Function_4_529",          # 04, 4
        "Function_5_909",          # 05, 5
        "Function_6_A9C",          # 06, 6
        "Function_7_AA0",          # 07, 7
        "Function_8_1BC2",         # 08, 8
        "Function_9_22AD",         # 09, 9
        "Function_10_2DA0",        # 0A, 10
        "Function_11_32FA",        # 0B, 11
        "Function_12_3415",        # 0C, 12
        "Function_13_34FA",        # 0D, 13
        "Function_14_3568",        # 0E, 14
        "Function_15_35EE",        # 0F, 15
        "Function_16_3682",        # 10, 16
        "Function_17_3826",        # 11, 17
        "Function_18_3A11",        # 12, 18
        "Function_19_3C55",        # 13, 19
        "Function_20_4009",        # 14, 20
        "Function_21_415C",        # 15, 21
        "Function_22_42FC",        # 16, 22
        "Function_23_44B9",        # 17, 23
        "Function_24_456A",        # 18, 24
        "Function_25_4654",        # 19, 25
        "Function_26_4F5C",        # 1A, 26
        "Function_27_4FBC",        # 1B, 27
        "Function_28_503B",        # 1C, 28
        "Function_29_65D3",        # 1D, 29
        "Function_30_6621",        # 1E, 30
        "Function_31_6AD7",        # 1F, 31
        "Function_32_780B",        # 20, 32
        "Function_33_7CC1",        # 21, 33
    ))


    def Function_0_3F8(): pass

    label("Function_0_3F8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_430"),
        (1, "loc_43C"),
        (2, "loc_448"),
        (3, "loc_454"),
        (4, "loc_460"),
        (5, "loc_46C"),
        (6, "loc_478"),
        (SWITCH_DEFAULT, "loc_484"),
    )


    label("loc_430")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_43C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_448")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_454")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_460")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_46C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_484")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_490")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_4A7")

    Return()

    # Function_0_3F8 end

    def Function_1_4A8(): pass

    label("Function_1_4A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D2")
    OP_94(0xFE, 0xDE12, 0x122, 0xD0C0, 0xFFFFF07E, 0x3E8)
    Sleep(300)
    Jump("Function_1_4A8")

    label("loc_4D2")

    Return()

    # Function_1_4A8 end

    def Function_2_4D3(): pass

    label("Function_2_4D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FD")
    OP_94(0xFE, 0xDFFC, 0xDC82, 0xD548, 0xC922, 0x3E8)
    Sleep(300)
    Jump("Function_2_4D3")

    label("loc_4FD")

    Return()

    # Function_2_4D3 end

    def Function_3_4FE(): pass

    label("Function_3_4FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_528")
    OP_94(0xFE, 0xDFCA, 0xDB74, 0xD4DA, 0xC454, 0x3E8)
    Sleep(300)
    Jump("Function_3_4FE")

    label("loc_528")

    Return()

    # Function_3_4FE end

    def Function_4_529(): pass

    label("Function_4_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_574")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    Jump("loc_8E0")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5B6")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_8E0")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_60B")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_8E0")

    label("loc_60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6A1")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -12040, 150, 6900, 180)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrPos(0x16, -10490, 0, 6320, 315)
    SetChrFlags(0x16, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_692")
    SetChrFlags(0x15, 0x10)

    label("loc_692")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_8E0")

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_70F")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF")
    SetChrFlags(0xA, 0x10)

    label("loc_6CF")

    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_8E0")

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_764")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_75F")

    Jump("loc_8E0")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_788")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x80)
    Jump("loc_8E0")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7E9")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x10)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -12040, 150, 6900, 180)
    SetChrChipByIndex(0x18, 0x12)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_8E0")

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_81C")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_817")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_817")

    Jump("loc_8E0")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_893")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -12040, 150, 6900, 180)
    SetChrFlags(0x18, 0x10)
    SetChrChipByIndex(0x18, 0x12)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_8E0")

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8C6")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BC")
    SetChrFlags(0x9, 0x10)

    label("loc_8BC")

    SetChrFlags(0xA, 0x10)
    Jump("loc_8E0")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8E0")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_8F4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_908")

    label("loc_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_908")
    ClearScenarioFlags(0x22, 1)
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_908")

    Return()

    # Function_4_529 end

    def Function_5_909(): pass

    label("Function_5_909")

    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_92D")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_93B")
    Jump("loc_A0F")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_954")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_96D")
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_97B")
    Jump("loc_A0F")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_994")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_A0F")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9C6")
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9D4")
    Jump("loc_A0F")

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9F8")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A06")
    Jump("loc_A0F")

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A0F")

    label("loc_A0F")

    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_A42")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A52")
    ClearMapObjFlags(0x2, 0x10)

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A5F")
    OP_65(0x2, 0x1)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A9B")

    Return()

    # Function_5_909 end

    def Function_6_A9C(): pass

    label("Function_6_A9C")

    Call(0, 7)
    Return()

    # Function_6_A9C end

    def Function_7_AA0(): pass

    label("Function_7_AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AD7")
    Call(0, 33)
    Return()

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5")
    Call(0, 32)
    Return()

    label("loc_AE5")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "休憩をする\x01",        # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B65")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B84")
    OP_AF(0x5F)
    Jump("loc_BA6")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B94")
    OP_AF(0x5E)
    Jump("loc_BA6")

    label("loc_B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA4")
    OP_AF(0x5D)
    Jump("loc_BA6")

    label("loc_BA4")

    OP_AF(0x5C)

    label("loc_BA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB9")

    label("loc_BB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD5")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB9")

    label("loc_BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE9")
    Jump("loc_1BB9")

    label("loc_BE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_C9C")

    #C0001
    ChrTalk(
        0x8,
        (
            "ふふ、ウチの煮込みシチューは\x01",
            "最高だったろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "患者さんや外来のお客さんにも\x01",
            "元気が出るって評判なんだ。\x01",
            "また食べにおいで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D87")

    label("loc_C9C")


    #C0003
    ChrTalk(
        0x8,
        (
            "ウチのお勧め料理は\x01",
            "かなりの時間、\x01",
            "煮込む必要があるんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D39")

    #C0004
    ChrTalk(
        0x8,
        (
            "完成するのは\x01",
            "２日後ってところだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "その頃になったら\x01",
            "忘れずにおいで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D87")

    label("loc_D39")


    #C0006
    ChrTalk(
        0x8,
        (
            "完成するのは\x01",
            "明日ってところだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "もうすぐだから、\x01",
            "忘れずにおいで。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D87")

    Jump("loc_1BB9")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAC")

    #C0008
    ChrTalk(
        0x8,
        (
            "ハロルドさんから連絡があってね。\x01",
            "後で病院の方に来てくれるらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "アルモリカ産の野菜を\x01",
            "沢山持ってきてくれるよう頼んだし、\x01",
            "ようやくまともな食事が作れそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "豊かな食事は何より大切だからね。\x01",
            "これで患者さんたちも\x01",
            "元気になってくれるだろうさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F74")

    label("loc_EAC")


    #C0011
    ChrTalk(
        0x8,
        (
            "ハロルドさんにアルモリカ産の野菜を\x01",
            "沢山持ってきてくれるよう頼んだし、\x01",
            "ようやくまともな食事が作れそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "豊かな食事は何より大切だからね。\x01",
            "これで患者さんたちも\x01",
            "元気になってくれるだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F74")

    Jump("loc_1BB9")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1016")

    #C0013
    ChrTalk(
        0x8,
        (
            "こっちに留まってる\x01",
            "外来さんたちにも、だんだんと\x01",
            "疲れが溜まってるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "早いところクロスベル市に\x01",
            "戻してあげられるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB9")

    label("loc_1016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110B")

    #C0015
    ChrTalk(
        0x8,
        (
            "街から食糧は\x01",
            "支給されてるんだが、\x01",
            "基本的に保存食が多くてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "やれやれ、病院食を作るにも\x01",
            "どうにも栄養のバランスが\x01",
            "悪くなっちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "心なしか患者さんや\x01",
            "外来客さんの表情も暗いし……\x01",
            "なんとかしたいねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B1")

    label("loc_110B")


    #C0018
    ChrTalk(
        0x8,
        (
            "街から支給される食糧だけじゃ\x01",
            "どうにも栄養のバランスが\x01",
            "悪くなっちまうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "以前みたいにアルモリカ村の\x01",
            "新鮮な野菜が仕入れられるように\x01",
            "なればいいんだけどねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")

    Jump("loc_1BB9")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_131D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129A")

    #C0020
    ChrTalk(
        0x8,
        (
            "あっちの方にいる街の子たち、\x01",
            "アルカンシェルのファンらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "イリアのお見舞いに来てたんだが、\x01",
            "独立宣言から病院に残って\x01",
            "色々と手伝ってくれてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "ふふ、親切な子たちもいたものだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1318")

    label("loc_129A")


    #C0023
    ChrTalk(
        0x8,
        (
            "イリアのファンの子たちが、\x01",
            "独立宣言から病院に残って\x01",
            "色々と手伝ってくれてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "ふふ、親切な子たちもいたものだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1318")

    Jump("loc_1BB9")

    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_148B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140B")

    #C0025
    ChrTalk(
        0x8,
        (
            "あたしゃ病院食のメニューも\x01",
            "担当しているんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "今回の入院患者さんには、\x01",
            "ご飯も食べられないほどの\x01",
            "怪我してる人も多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "食は活力につながるんだ。\x01",
            "なんとか食べれるように\x01",
            "なってほしいもんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1486")

    label("loc_140B")


    #C0028
    ChrTalk(
        0x8,
        (
            "一応、点滴で栄養は\x01",
            "とれてるんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "食は活力につながるんだ。\x01",
            "なんとか食べれるように\x01",
            "なってほしいもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1486")

    Jump("loc_1BB9")

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1589")

    #C0030
    ChrTalk(
        0x8,
        (
            "やたらと救急車が出て行って\x01",
            "昨日は何事かと思ってたが、\x01",
            "まさか列車の脱線事故とはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "補償やらなにやらで\x01",
            "鉄道公社も大慌てだろうが、\x01",
            "人死にがなくて本当によかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "それにしても……\x01",
            "一体何が原因だったんだろうね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1600")

    label("loc_1589")


    #C0033
    ChrTalk(
        0x8,
        (
            "列車事故は、\x01",
            "一体何が原因だったんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "人死にが出なかったのは\x01",
            "何よりだったけど、\x01",
            "なんだか気になるねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1600")

    Jump("loc_1BB9")

    label("loc_1605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169E")

    #C0035
    ChrTalk(
        0x8,
        (
            "アリオスさんなら、\x01",
            "昨日の夜にギルドに戻っていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "シズクちゃんが大変なときだが、\x01",
            "やっぱり忙しいお人みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D5")

    label("loc_169E")


    #C0037
    ChrTalk(
        0x8,
        (
            "さてと、今晩寮生に出す食事は\x01",
            "何にしようかねえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D5")

    Jump("loc_1BB9")

    label("loc_16DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_189E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E7")

    #C0038
    ChrTalk(
        0x8,
        (
            "アリオスさんは、\x01",
            "シズクちゃんの手術のため\x01",
            "しばらくここに宿泊してたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "立派なお父さんが\x01",
            "付き添ってくれてたんだ、\x01",
            "シズクちゃんも心強かったろうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "ただ、手術自体は残念な結果に\x01",
            "なっちまったそうでね。\x01",
            "はあ……やりきれないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1899")

    label("loc_17E7")


    #C0041
    ChrTalk(
        0x8,
        (
            "アリオスさんは、しばらく滞在して\x01",
            "シズクちゃんに付き添ってたんだ。\x01",
            "さぞ、心強かったろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "ただ、手術自体は残念な結果に\x01",
            "なっちまったそうでね。\x01",
            "はあ……やりきれないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1899")

    Jump("loc_1BB9")

    label("loc_189E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1963")

    #C0043
    ChrTalk(
        0x8,
        (
            "今日は遊撃士のエオリアさんが\x01",
            "仕事で来てたみたいだから、\x01",
            "ランチをサービスしたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "病院はあの子たちに\x01",
            "大分お世話になってるからね。\x01",
            "せめてものお礼ってやつさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CD")

    label("loc_1963")


    #C0045
    ChrTalk(
        0x8,
        (
            "病院は、遊撃士にも\x01",
            "大分お世話になってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "たまにはランチのサービスくらい\x01",
            "してやらないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CD")

    Jump("loc_1BB9")

    label("loc_19D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A71")

    #C0047
    ChrTalk(
        0x8,
        (
            "アルバート大公ってのは、\x01",
            "あの若さでレミフェリアの\x01",
            "国家元首なんだってねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "国民にも慕われてるらしいし……\x01",
            "さぞ優秀なお方なんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB9")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5E")

    #C0049
    ChrTalk(
        0x8,
        (
            "病院にも新しい研修医が\x01",
            "増えたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "ほら、そこにいるミショーって子。\x01",
            "なんでも、クロスベル市で\x01",
            "独学で勉強してたんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "あたしゃ、がんばり屋は大好きだよ。\x01",
            "ドカンとサービスしなきゃねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BB9")

    label("loc_1B5E")


    #C0052
    ChrTalk(
        0x8,
        "あたしゃ、がんばり屋は大好きだよ。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "新入りくんには\x01",
            "ドカンとサービスしなきゃねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB9")

    Jump("loc_AF2")

    label("loc_1BBE")

    TalkEnd(0x8)
    Return()

    # Function_7_AA0 end

    def Function_8_1BC2(): pass

    label("Function_8_1BC2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE0")
    Call(0, 9)
    Jump("loc_1C4A")

    label("loc_1BE0")


    #C0054
    ChrTalk(
        0x9,
        (
            "ミショー君、たくさん\x01",
            "腹ごしらえしときなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "ほらほら、落ち着いて食べないと\x01",
            "喉に詰まらすわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4A")

    Jump("loc_22A9")

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6A")
    Call(0, 9)
    Jump("loc_1CC4")

    label("loc_1C6A")


    #C0056
    ChrTalk(
        0x9,
        (
            "……とにかく、私たちには\x01",
            "どうすることもできないし……\x01",
            "今は病院の事に集中しましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC4")

    Jump("loc_22A9")

    label("loc_1CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")
    Call(0, 9)
    Jump("loc_1D5B")

    label("loc_1CE4")


    #C0057
    ChrTalk(
        0x9,
        (
            "ミショー君も\x01",
            "サマになってきたじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "こんな本を読みながら\x01",
            "食事なんてできないって、\x01",
            "前はうるさかったのに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5B")

    Jump("loc_22A9")

    label("loc_1D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7B")
    Call(0, 9)
    Jump("loc_1E09")

    label("loc_1D7B")


    #C0059
    ChrTalk(
        0x9,
        (
            "勉強は継続が大事よ。\x01",
            "１日サボったら取り戻すのに\x01",
            "３日はかかるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "街は心配だろうけど、\x01",
            "ちゃんとやっておくこと。\x01",
            "……いいわね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E09")

    Jump("loc_22A9")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E29")
    Call(0, 9)
    Jump("loc_1E6E")

    label("loc_1E29")


    #C0061
    ChrTalk(
        0x9,
        (
            "……さ、ミショー君も座って。\x01",
            "午後のためにも腹ごしらえしなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6E")

    Jump("loc_22A9")

    label("loc_1E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8E")
    Call(0, 9)
    Jump("loc_1F1B")

    label("loc_1E8E")


    #C0062
    ChrTalk(
        0x9,
        (
            "まあ、評価なんて\x01",
            "後から付いてくるもんだし……\x01",
            "仕事なんてイヤでも増えるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "とりあえずは患者さんたちが\x01",
            "助かった事を喜ばないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1B")

    Jump("loc_22A9")

    label("loc_1F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1FA8")

    #C0064
    ChrTalk(
        0x9,
        (
            "さてと、今日の講義まで\x01",
            "ちょっと時間があるわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "ミショー君もまだ来てないし、\x01",
            "朝食とりながら自習といきますか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A9")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC3")
    Call(0, 9)
    Jump("loc_2062")

    label("loc_1FC3")


    #C0066
    ChrTalk(
        0x9,
        (
            "リットンは、前の指導教授の時から\x01",
            "死に物狂いで努力してたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "私も勉強なら負けないけど、\x01",
            "現場であれだけ努力してたら\x01",
            "成長しないほうがおかしいわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2062")

    Jump("loc_22A9")

    label("loc_2067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_211B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2082")
    Call(0, 9)
    Jump("loc_2116")

    label("loc_2082")


    #C0068
    ChrTalk(
        0x9,
        (
            "もぐもぐ……\x01",
            "まあ、研修医やってたら\x01",
            "誰もが通る道だって。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "これから先、ずっとお昼を\x01",
            "抜くわけにもいかないでしょ？\x01",
            "ふふ、そのうち慣れるわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2116")

    Jump("loc_22A9")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_218C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2136")
    Call(0, 9)
    Jump("loc_2187")

    label("loc_2136")


    #C0070
    ChrTalk(
        0x9,
        (
            "ミショー君、\x01",
            "初めて手術を生で見るのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        "ふふ……ま、お手並み拝見ね。\x02",
    )

    CloseMessageWindow()

    label("loc_2187")

    Jump("loc_22A9")

    label("loc_218C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_22A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2252")

    #C0072
    ChrTalk(
        0x9,
        (
            "新入りのミショー君の\x01",
            "指導を任されちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "うーん、勉強の時間が\x01",
            "削られちゃうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "まあ、これも勉強のうちだわね。\x01",
            "せっかくだしビシビシやるわよー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22A9")

    label("loc_2252")


    #C0075
    ChrTalk(
        0x9,
        (
            "まあ、かわいい後輩の指導も\x01",
            "勉強のうちよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "せっかくだしビシビシやるわよー。\x02",
    )

    CloseMessageWindow()

    label("loc_22A9")

    TalkEnd(0x9)
    Return()

    # Function_8_1BC2 end

    def Function_9_22AD(): pass

    label("Function_9_22AD")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23B6")

    #C0077
    ChrTalk(
        0x9,
        (
            "ミショー君、\x01",
            "患者さんがたくさん来たから\x01",
            "腹ごしらえしときなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "今日はキミにも現場で\x01",
            "バリバリ働いてもらうわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "はっ、はい！\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "よーし、やるぞ～！！\x01",
            "もぐもぐもぐもぐっ……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "あはは、落ち着いて食べないと\x01",
            "喉に詰まらすわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_23B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_24E3")

    #C0082
    ChrTalk(
        0x9,
        (
            "独立国の無効宣言か……\x01",
            "これから一体どうなるのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "とにかく、旧市街の\x01",
            "アパートの人たちが心配ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "街に戻る申請も、しばらくは\x01",
            "受け付けられないみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "……とにかく、私たちには\x01",
            "どうすることもできないし……\x01",
            "今は病院の事に集中しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        "……ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2626")

    #C0087
    ChrTalk(
        0x9,
        (
            "もぐもぐ……\x01",
            "でね、この図説にある通り\x01",
            "人間の内臓って言うのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "ぱくぱく……\x01",
            "ふむ、なるほど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……ふふ、それにしても\x01",
            "ミショー君も\x01",
            "サマになってきたじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "こんな本を読みながら\x01",
            "食事なんてできないって、\x01",
            "前はうるさかったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "もぐもぐ……\x01",
            "ハハ、これも先輩の\x01",
            "教育のたまものですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_2626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_273E")

    #C0092
    ChrTalk(
        0x9,
        (
            "ミショー君、\x01",
            "最近ちゃんと勉強できてる？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "それが……\x01",
            "ちょっと手についてなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "クロスベルがこんなときで、\x01",
            "アパートの人たちも心配ですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "そっかー……\x01",
            "まあ仕方ないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "でも、落ち着いたら\x01",
            "ちゃんとやっておくこと。\x01",
            "……いいわね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_273E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_286A")

    #C0097
    ChrTalk(
        0xA,
        (
            "襲撃事件の被害者さんの中には、\x01",
            "どうしても助けられなかった人もいて……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        "先輩……俺、心がくじけそうです。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "……気持ちは分かるわ。\x01",
            "でも、泣き言を言うのは\x01",
            "全部終わってからにしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "そんな暇があったら、\x01",
            "１人でも多くの患者を助ける。\x01",
            "それが私たちの仕事なんだから。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2D98")

    label("loc_286A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29DB")

    #C0101
    ChrTalk(
        0x9,
        "はあ、ようやく一息ついたわね。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "それにしても、\x01",
            "ミショー君もなかなか頑張って\x01",
            "手伝ってたみたいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "い、いやー……\x01",
            "俺なんてまだまだですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "手伝ったって言っても、\x01",
            "雑用みたいなもんでしたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "謙遜しないしない。\x01",
            "雑用だって大事な仕事よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "最近は血を見ても平気に\x01",
            "なってきたみたいだし……\x01",
            "ちょっとは成長したんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2D98")

    label("loc_29DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AF9")

    #C0107
    ChrTalk(
        0xA,
        (
            "リットン先輩って、\x01",
            "よく手術の助手とか回診に\x01",
            "駆りだされてますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "はあ、やっぱり\x01",
            "新入りの俺なんかとは\x01",
            "デキが違うなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "リットンは、前の指導教授の時から\x01",
            "死に物狂いで努力してたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "まー、あせらないあせらない。\x01",
            "成長したかったら勉強勉強よ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2D98")

    label("loc_2AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C64")

    #C0111
    ChrTalk(
        0x9,
        "ぱくぱく、もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "……どしたの、ミショー君。\x01",
            "何か注文すれば？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "い、いえその……\x01",
            "今朝、外科手術の実地研修が\x01",
            "あったじゃないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "初めて本物の手術を見て、\x01",
            "なんだか食欲が無いって言うか……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "あ～やっぱりそうなったか。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "もぐもぐ……\x01",
            "まあ、誰もが通る道だし\x01",
            "そのうち慣れるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "……うぷ……\x01",
            "だ、だといいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_2C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D98")

    #C0118
    ChrTalk(
        0x9,
        (
            "そういえばミショーくん、\x01",
            "明日はゲイリー教授の\x01",
            "外科手術の研修でしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "確か、本物の手術を見るの\x01",
            "初めてだったわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        "ええ、そうなんですよ。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "いやあ、本格的に医者の勉強が\x01",
            "始まるって感じですよね～。\x01",
            "今から楽しみだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "ふふ……威勢がいいわね。\x01",
            "ま、せいぜい頑張るといいわ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)

    label("loc_2D98")

    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_22AD end

    def Function_10_2DA0(): pass

    label("Function_10_2DA0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DBE")
    Call(0, 9)
    Jump("loc_2DF5")

    label("loc_2DBE")


    #C0123
    ChrTalk(
        0xA,
        (
            "もぐもぐもぐもぐっ……！！\x01",
            "げふっ、げふっ……！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    Jump("loc_32F6")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E15")
    Call(0, 9)
    Jump("loc_2E77")

    label("loc_2E15")


    #C0124
    ChrTalk(
        0xA,
        (
            "ですね……街に戻れないのも\x01",
            "仕方ない状況ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "少しは事態が好転すれば\x01",
            "いいんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E77")

    Jump("loc_32F6")

    label("loc_2E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E97")
    Call(0, 9)
    Jump("loc_2ED3")

    label("loc_2E97")


    #C0126
    ChrTalk(
        0xA,
        (
            "もぐもぐ……\x01",
            "ハハ、これも先輩の\x01",
            "教育のたまものですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED3")

    Jump("loc_32F6")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF3")
    Call(0, 9)
    Jump("loc_2F5F")

    label("loc_2EF3")


    #C0127
    ChrTalk(
        0xA,
        (
            "そうですね……\x01",
            "アパートの人も心配ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "それを理由に勉強しないのは\x01",
            "甘えなのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5F")

    Jump("loc_32F6")

    label("loc_2F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7F")
    Call(0, 9)
    Jump("loc_2FE1")

    label("loc_2F7F")


    #C0129
    ChrTalk(
        0xA,
        "……先輩の言うとおりだな……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "今はとにかく、\x01",
            "１人でも多くの患者を\x01",
            "助ける事を考えないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE1")

    Jump("loc_32F6")

    label("loc_2FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3001")
    Call(0, 9)
    Jump("loc_304E")

    label("loc_3001")


    #C0131
    ChrTalk(
        0xA,
        (
            "うーん、俺も雑用ばかりじゃなくて\x01",
            "重要な仕事を任されるようにならないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304E")

    Jump("loc_32F6")

    label("loc_3053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3061")
    Jump("loc_32F6")

    label("loc_3061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307C")
    Call(0, 9)
    Jump("loc_30F9")

    label("loc_307C")


    #C0132
    ChrTalk(
        0xA,
        (
            "そうか……確かに\x01",
            "焦っても始まらないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "……それにしたって先輩、\x01",
            "食事時に解剖学の本は\x01",
            "やっぱりやめたほうが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F9")

    Jump("loc_32F6")

    label("loc_30FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_318C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3119")
    Call(0, 9)
    Jump("loc_3187")

    label("loc_3119")


    #C0134
    ChrTalk(
        0xA,
        (
            "うう、先輩は手術のあとで\x01",
            "よくそんな肉料理なんか\x01",
            "食べられますよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        "うっ、思い出したら吐き気が……\x02",
    )

    CloseMessageWindow()

    label("loc_3187")

    Jump("loc_32F6")

    label("loc_318C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A7")
    Call(0, 9)
    Jump("loc_3202")

    label("loc_31A7")


    #C0136
    ChrTalk(
        0xA,
        "はは、任してくださいよ！\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "先輩の顔にドロを塗らないよう、\x01",
            "しっかり勉強してきます！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3202")

    Jump("loc_32F6")

    label("loc_3207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A8")

    #C0138
    ChrTalk(
        0xA,
        (
            "フローラ先輩は\x01",
            "ちょっと厳しいけど、\x01",
            "教え方がとてもうまくてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "知識も相当深いし、\x01",
            "ほんと、いい先輩に\x01",
            "巡り合えてよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32F6")

    label("loc_32A8")


    #C0140
    ChrTalk(
        0xA,
        (
            "フローラ先輩、食事時にまで\x01",
            "解剖の本を開くのは\x01",
            "なんとかしてくれないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F6")

    TalkEnd(0xA)
    Return()

    # Function_10_2DA0 end

    def Function_11_32FA(): pass

    label("Function_11_32FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DC")

    #C0141
    ChrTalk(
        0xFE,
        (
            "私たちの息子は、\x01",
            "あの襲撃事件で大怪我をしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "命は助かったのですが、\x01",
            "集中治療室に入っていて……\x01",
            "面会も少ししかできませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "ああ、女神様……\x01",
            "どうか息子をお助けください……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3411")

    label("loc_33DC")


    #C0144
    ChrTalk(
        0xFE,
        (
            "ああ、女神様……\x01",
            "どうか息子をお助けください……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    TalkEnd(0xFE)
    Return()

    # Function_11_32FA end

    def Function_12_3415(): pass

    label("Function_12_3415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AE")

    #C0145
    ChrTalk(
        0xFE,
        (
            "息子は、武装集団と戦った\x01",
            "警備隊員の一人でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "……こんなことになるなら、\x01",
            "警備隊に入るなんて\x01",
            "反対すべきだった……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_34F6")

    label("loc_34AE")


    #C0147
    ChrTalk(
        0xFE,
        (
            "……こんなことになるなら、\x01",
            "警備隊に入るなんて\x01",
            "反対すべきだった……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F6")

    TalkEnd(0xFE)
    Return()

    # Function_12_3415 end

    def Function_13_34FA(): pass

    label("Function_13_34FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3564")

    #C0148
    ChrTalk(
        0xFE,
        (
            "パパもママも、なんだか\x01",
            "ずっと悲しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "お兄ちゃん……\x01",
            "どうしちゃったのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3564")

    TalkEnd(0xFE)
    Return()

    # Function_13_34FA end

    def Function_14_3568(): pass

    label("Function_14_3568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35EA")

    #C0150
    ChrTalk(
        0xFE,
        (
            "襲撃事件以来、息子夫婦が\x01",
            "ここに入院していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "ひとまず安全は確認できたが……\x01",
            "やはり気持ちが落ち着かんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EA")

    TalkEnd(0xFE)
    Return()

    # Function_14_3568 end

    def Function_15_35EE(): pass

    label("Function_15_35EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_367E")

    #C0152
    ChrTalk(
        0xFE,
        (
            "あんな事件が起こってしまって、\x01",
            "警察も警備隊も酷い被害をだして……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "クロスベルはこれから、\x01",
            "どうなってしまうんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367E")

    TalkEnd(0xFE)
    Return()

    # Function_15_35EE end

    def Function_16_3682(): pass

    label("Function_16_3682")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3693")
    Jump("loc_3822")

    label("loc_3693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3711")

    #C0154
    ChrTalk(
        0x10,
        (
            "イリア様の病室に病院食を\x01",
            "届けることになっちゃった……！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x10,
        (
            "ど、どうしよ……\x01",
            "会ったら何を話せばいいの！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_3711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_37A1")

    #C0156
    ChrTalk(
        0x10,
        (
            "本当なら、病室に届くように\x01",
            "イリア様のお名前を叫びたいくらいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x10,
        (
            "だけどここは病院……\x01",
            "ガマンしないとダメよね、さすがに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_37A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3822")

    #C0158
    ChrTalk(
        0x10,
        (
            "イリア様の意識が戻って\x01",
            "本当に良かったわよねっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x10,
        (
            "街に帰らないで、ずっとここで\x01",
            "回復を祈っていた甲斐があったわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3822")

    TalkEnd(0xFE)
    Return()

    # Function_16_3682 end

    def Function_17_3826(): pass

    label("Function_17_3826")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3837")
    Jump("loc_3A0D")

    label("loc_3837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_38DB")

    #C0160
    ChrTalk(
        0x11,
        (
            "お、落ち着けポリセ……\x01",
            "他の入院患者の分も\x01",
            "届けなきゃいけないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x11,
        (
            "焦ってイリア様の分まで\x01",
            "こぼしちゃったらコトだぜ。\x01",
            "平常心、平常心だ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0D")

    label("loc_38DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3981")

    #C0162
    ChrTalk(
        0x11,
        (
            "イリア様が一日でも早く治るよう、\x01",
            "願掛けも込めて手伝いをしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x11,
        (
            "あの寮長さんは人使いが荒いけど……\x01",
            "イリア様のためを思えば屁のカッパだぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0D")

    label("loc_3981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A0D")

    #C0164
    ChrTalk(
        0x11,
        (
            "今は大変なときだし、\x01",
            "イリア様のお見舞いに行くのは\x01",
            "ガマンしないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x11,
        (
            "その分、病院の手伝いをして\x01",
            "少しでも役に立たないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0D")

    TalkEnd(0xFE)
    Return()

    # Function_17_3826 end

    def Function_18_3A11(): pass

    label("Function_18_3A11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3A22")
    Jump("loc_3C51")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_3C51")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3A3E")
    Jump("loc_3C51")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3A4C")
    Jump("loc_3C51")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A6F")
    Call(0, 19)
    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_3A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA8")

    #C0166
    ChrTalk(
        0x15,
        (
            "#01300Fツァイト君と一緒にいると、\x01",
            "とても落ち着くのよね。\x02\x03",

            "#01304Fそんなに何度も会ってないのに、\x01",
            "何だか居心地がいいっていうか……\x02\x03",

            "#01300F昔からの友達だったみたいな、\x01",
            "そんな懐かしい感じがするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        (
            "#10400Fアハハ、まるで\x01",
            "運命の恋人同士みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#00003F（ちょっと羨ましいかも……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3C49")

    label("loc_3BA8")


    #C0169
    ChrTalk(
        0x15,
        (
            "#01300Fツァイト君が近くにいると、\x01",
            "とても落ち着くのよね。\x02\x03",

            "#01304F何だか居心地がいいっていうか……\x01",
            "昔からの友達だったみたいな、\x01",
            "そんな懐かしい感じがするの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C49")

    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_3C51")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A11 end

    def Function_19_3C55(): pass

    label("Function_19_3C55")

    OP_4B(0x16, 0xFF)

    #C0170
    ChrTalk(
        0x15,
        (
            "#01300Fそういえばツァイト君とは\x01",
            "あの大統領演説の日以来だったわね。\x02\x03",

            "#01303Fアリオスさんに連れられた\x01",
            "キーアちゃんを追っていって、\x01",
            "そのまま行方が分からなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x16,
        (
            "#3C#01200Fうむ、追跡していたが……\x01",
            "あの《剣聖》が湖に出たことで、\x01",
            "完全に振り切られてしまってな。\x02\x03",

            "ロイドたちには悪いと思ったが、\x01",
            "一度態勢を整えるために\x01",
            "部下たちの元へ戻っていたのだ。\x02\x03",

            "#01203F思えば、あの場にいたおぬしには\x01",
            "いらぬ心配をかけてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x15,
        (
            "#01302Fくすっ、私は大丈夫よ。\x01",
            "それよりもツァイト君が\x01",
            "無事でよかったわ。\x02\x03",

            "#01300Fそれに、今もロイドやワジ君を\x01",
            "一所懸命助けてくれてるのよね。\x02\x03",

            "#01304Fふふ、ありがとう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セシルはツァイトの頭を優しく撫でた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0xFFFFFDA8, 2100, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0174
    ChrTalk(
        0x16,
        "#3C#01200F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x15,
        (
            "#01303Fふふ、ツァイト君と一緒にいると、\x01",
            "何故だかとても落ち着くのよね。\x02\x03",

            "#01305Fあっ……ごめんなさい。\x01",
            "こんな気安く撫でてしまって、\x01",
            "気を悪くさせたかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x16,
        (
            "#3C#01200F……フフ、いや。\x01",
            "悪い心地はしなかった。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 1)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_19_3C55 end

    def Function_20_4009(): pass

    label("Function_20_4009")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4027")
    Call(0, 19)
    Jump("loc_4158")

    label("loc_4027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E9")

    #C0177
    ChrTalk(
        0x16,
        "#3C#01203F……フフ……………………\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F（ツァイト、どうしたんだろう？\x01",
            "  黙り込んじゃったけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00200F（セシルさんに撫でられて\x01",
            "  照れてるんでしょうか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4158")

    label("loc_40E9")


    #C0180
    ChrTalk(
        0x16,
        (
            "#3C#01200F……病人を混乱させないよう、\x01",
            "私はここで待っているとしよう。\x02\x03",

            "おぬしらは見舞いをしてくるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4158")

    TalkEnd(0xFE)
    Return()

    # Function_20_4009 end

    def Function_21_415C(): pass

    label("Function_21_415C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_42F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426E")

    #C0181
    ChrTalk(
        0xFE,
        (
            "この前、主人に持病の発作が出てね。\x01",
            "急いで救急車でこっちに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "なんとか申請が通ってよかったけど……\x01",
            "かなり審査が厳密だったから、\x01",
            "もしダメだったらとヒヤヒヤしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "はあ……このまま病院に居た方が\x01",
            "むしろ安心なんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_42F8")

    label("loc_426E")


    #C0184
    ChrTalk(
        0xFE,
        (
            "この前、主人に持病の発作が出てね。\x01",
            "急いで救急車でこっちに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "はあ……このまま病院に居た方が\x01",
            "むしろ安心なんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F8")

    TalkEnd(0xFE)
    Return()

    # Function_21_415C end

    def Function_22_42FC(): pass

    label("Function_22_42FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_44B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4403")

    #C0186
    ChrTalk(
        0xFE,
        (
            "病院に通院できなかったせいで、\x01",
            "持病の薬が切れて、\x01",
            "発作を起こしてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "街道の移動制限というものが\x01",
            "いかに厄介か、身に染みたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "街に戻るには次に国防軍が来るのを\x01",
            "待つ必要があるし……\x01",
            "しばらくゆっくりしてようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_44B5")

    label("loc_4403")


    #C0189
    ChrTalk(
        0xFE,
        (
            "今回病院に運ばれたことで、\x01",
            "街道の移動制限というものが\x01",
            "いかに厄介か、身に染みたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "街に戻るには次に国防軍が来るのを\x01",
            "待つ必要があるし……\x01",
            "しばらくゆっくりしてようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B5")

    TalkEnd(0xFE)
    Return()

    # Function_22_42FC end

    def Function_23_44B9(): pass

    label("Function_23_44B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4566")

    #C0191
    ChrTalk(
        0xFE,
        (
            "今日には街に帰れる予定だったのに……\x01",
            "一体どうなっとるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "無効宣言がなんだか知らんが、\x01",
            "ワシ１人くらい街に連れてってくれても\x01",
            "バチはあたらんだろうに。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4566")

    TalkEnd(0xFE)
    Return()

    # Function_23_44B9 end

    def Function_24_456A(): pass

    label("Function_24_456A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_457B")
    Jump("loc_4650")

    label("loc_457B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4596")
    Call(0, 30)
    Jump("loc_4650")

    label("loc_4596")


    #C0193
    ChrTalk(
        0xFE,
        (
            "報告にあった『蒼い花』と\x01",
            "幻獣との因果関係を調べるために、\x01",
            "ウルスラ間道の中州に行くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "ま、私たちのことは心配いらない。\x01",
            "アンタたちはアンタたちの仕事に\x01",
            "専念するといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4650")

    TalkEnd(0xFE)
    Return()

    # Function_24_456A end

    def Function_25_4654(): pass

    label("Function_25_4654")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4665")
    Jump("loc_4F58")

    label("loc_4665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_484E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4680")
    Call(0, 30)
    Jump("loc_4849")

    label("loc_4680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B2")

    #C0195
    ChrTalk(
        0xFE,
        (
            "コホン、そういえば、\x01",
            "その蒼い花のことだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "あなたたちの報告書では、\x01",
            "あの《グノーシス》の材料に\x01",
            "なっていたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "首謀者のヨアヒム・ギュンターは\x01",
            "教団事件でその薬を大量に\x01",
            "製造していたらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "その材料となる《プレロマ草》は\x01",
            "どこで仕入れていたのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4849")

    label("loc_47B2")


    #C0199
    ChrTalk(
        0xFE,
        (
            "ヨアヒム・ギュンターは\x01",
            "教団事件で大量のグノーシスを\x01",
            "製造していたらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "その材料となる《プレロマ草》は\x01",
            "どこで仕入れていたのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4849")

    Jump("loc_4F58")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_485C")
    Jump("loc_4F58")

    label("loc_485C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD0")

    #C0201
    ChrTalk(
        0x101,
        "#00005Fあれ、エオリアさ──\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_493C")
    Jump("loc_4986")

    label("loc_493C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_495C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4986")

    label("loc_495C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_497C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4986")

    label("loc_497C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4986")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0202
    ChrTalk(
        0xFE,
        (
            "#4Sティ、ティオちゃんっ……\x01",
            "やっと帰ってきたのねっ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x103,
        "#00202F……どうも、ご無沙汰してます。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "ああっ……\x01",
            "何度この日を夢見たことか！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "こっちにおいで、ティオちゃん！\x01",
            "お姉さんがちゅっちゅしたげる！！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        "#00203F……断固、拒否します。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "あんっ、この感じも久しぶりっ……㈱\x02",
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

    #C0208
    ChrTalk(
        0x103,
        (
            "#00211F（……なぜだか、以前より\x01",
            "  強敵になった気がします。）\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00012F（は、はは……会えなかった間に\x01",
            "  想いが積もり積もってたんだろうな。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1C0, 7)
    Jump("loc_4F58")

    label("loc_4BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF2")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C6B")
    Jump("loc_4CB5")

    label("loc_4C6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C8B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB5")

    label("loc_4C8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CAB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB5")

    label("loc_4CAB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CB5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0210
    ChrTalk(
        0xFE,
        (
            "依頼で荷物を届けに来た先で\x01",
            "ティオちゃんに会えるなんてっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        "もう、これは運命じゃないかしら！？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#00211F違います。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "あんっ、即答っ……㈱\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        (
            "#00309Fエオリアさん、\x01",
            "そんじゃ代わりに俺と……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "ううん、いらない㈱\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#00306Fガクッ……\x01",
            "こっちも即答ッ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4F54")

    label("loc_4DF2")

    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E83")
    Jump("loc_4ECD")

    label("loc_4E83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EA3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ECD")

    label("loc_4EA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EC3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ECD")

    label("loc_4EC3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4ECD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0217
    ChrTalk(
        0xFE,
        (
            "ふふ、ティオちゃん。\x01",
            "また今度スキンシップさせてね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#00203F（依然、注意が必要……と。）\x02",
    )

    CloseMessageWindow()

    label("loc_4F54")

    SetChrSubChip(0xFE, 0x0)

    label("loc_4F58")

    TalkEnd(0xFE)
    Return()

    # Function_25_4654 end

    def Function_26_4F5C(): pass

    label("Function_26_4F5C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "３階：女性職員寮→\x01\x01",
            "←２階：男性職員寮\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_4F5C end

    def Function_27_4FBC(): pass

    label("Function_27_4FBC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　お見舞い・外来患者用宿泊施設　　\x01",
            "※ご利用の際は寮長にお申し付け下さい\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_4FBC end

    def Function_28_503B(): pass

    label("Function_28_503B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch03102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch08500.itc", 0x21)
    LoadChrToIndex("chr/ch08502.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -13250, 100, 3800, 0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, -12250, 100, 3800, 0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, -13650, 100, 6800, 180)
    ClearChrFlags(0x15, 0x80)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, -12900, 100, 6800, 180)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -12150, 100, 6800, 180)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x107, 0xF)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x107, -10500, 0, 4500, 315)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    OP_68(3690, 1500, 8400, 0)
    MoveCamera(36, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26610, 0)
    FadeToBright(1000, 0)
    OP_68(-12150, 1500, 5120, 7000)
    MoveCamera(47, 28, 0, 7000)
    OP_6E(440, 7000)
    SetCameraDistance(26610, 7000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-13080, 1500, 4550, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18910, 0)
    OP_0D()
    Sleep(300)

    #C0221
    ChrTalk(
        0x103,
        "#00206F#5P……そんな事が……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x19,
        (
            "#06406F#5Pな、何だか壮大すぎて\x01",
            "ピンと来ませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x15,
        (
            "#01303F#5P私たちの住むクロスベル……\x02\x03",

            "#01308F過去に色々な経緯があって\x01",
            "今があるという事は分かったわ。\x02\x03",

            "#01301Fこの状況も、キーアちゃんの事も。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00008F#12P……ああ。\x02\x03",

            "#00003F俺の望むことは２つだけだ。\x02\x03",

            "未だ見えていない真実を\x01",
            "この目で確かめること──\x02\x03",

            "#00013Fそしてみんなを解放して\x01",
            "キーアを取り戻すことだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(150)

    #C0225
    ChrTalk(
        0x105,
        (
            "#10409F#12Pフフ、２つだけとか言いながら\x01",
            "とんでもなく大変そうだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x107,
        "#01203F#11P#3Cまあ、性分なのだろう。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x103,
        (
            "#00202F#5Pふふっ……\x01",
            "それがロイドさんだから。\x02\x03",

            "#00204F──わたしの心も\x01",
            "ロイドさんと同じです。\x02\x03",

            "#00203F支援課のメンバーとして……\x02\x03",

            "#00201F何よりキーアの保護者として\x01",
            "どうか連れて行ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#00004F#12Pありがとう、ティオ。\x01",
            "遠慮なく力を貸してもらうよ。\x02\x03",

            "#00005Fでも、どうしてティオは\x01",
            "ここに連れて来られたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x103,
        (
            "#00206F#5P……多分、マリアベルさんか\x01",
            "アリオスさんの指示だと思います。\x02\x03",

            "#00208F支援課のメンバーは分断して\x01",
            "それぞれ別の場所で監視する……\x02\x03",

            "#00201F下手に一緒の場所に置いておくと\x01",
            "団結してキーアに働きかけかねないと\x01",
            "思われたんでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00006F#12Pなるほど……\x02\x03",

            "#00008Fとなるとエリィとランディも\x01",
            "それぞれ別の場所に居そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x105,
        (
            "#10406F#12Pうーん、クロスベル市にいたら\x01",
            "解放するのは不可能だけど……\x02\x03",

            "#10402Fティオがここにいたってことは、\x01",
            "市外にいる可能性は高そうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x15,
        (
            "#01306F#5Pそうね……４人をキーアちゃんに\x01",
            "近づけないようにしているみたいだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x19)
    Sleep(500)
    MoveCamera(34, 18, 0, 1000)
    Sound(812, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x19, 0x21)
    SetChrPos(0x19, -12150, 0, 6400, 180)
    OP_0D()

    def lambda_5796():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_5796)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0233
    ChrTalk(
        0x19,
        (
            "#06403F#5Pあ、あのっ……！\x02\x03",

            "#06401Fわたしも一緒に\x01",
            "連れていってくれませんか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x15, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)

    #C0234
    ChrTalk(
        0x101,
        "#00005F#6Pフラン……？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x15,
        "#01305F#5Pフランさん？\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x19,
        (
            "#06406F#5Pわ、わたしは皆さんみたいに\x01",
            "戦えるわけじゃないですけど……\x02\x03",

            "#06403Fそれでもオペレーターなら\x01",
            "そこそこ出来ると思うんですっ！\x02\x03",

            "#06401F何でもワジさんの飛行艇で\x01",
            "移動しているそうですし……\x02\x03",

            "どうか……！\x01",
            "お手伝いさせて欲しいんですっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        "#00001F#6Pフラン……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0238
    ChrTalk(
        0x103,
        "#00208F#5Pロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x105,
        (
            "#10406F#12Pうーん、確かに《メルカバ》も\x01",
            "人手不足だから助かるんだけど。\x02\x03",

            "#10400Fこればっかりは\x01",
            "ロイドに決めてもらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    #C0240
    ChrTalk(
        0x101,
        "#00006F#6P……そうだな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0241
    ChrTalk(
        0x101,
        (
            "#00003F#6Pフラン──君のお姉さんは\x01",
            "現在、国防軍で働いている。\x02\x03",

            "#00008F俺たちに付いて来るということは\x01",
            "彼女#4Rノエル#と対立すること……\x02\x03",

            "#00001Fそれは分かっているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x19,
        (
            "#06406F#5P……は、はい……！\x02\x03",

            "#06408Fもちろんお姉ちゃんと\x01",
            "争いたくなんてないですけど……\x02\x03",

            "#06401Fそれでも……わたしだって\x01",
            "クロスベル警察の警察官です！\x02\x03",

            "こんな危機的な状況……\x01",
            "放っておくわけにはいきません！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#00003F#6Pそうか……\x02\x03",

            "#00002F──分かった。\x01",
            "よろしく協力を頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0244
    ChrTalk(
        0x19,
        "#06409F#5Pあ、ありがとうございますっ！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0245
    ChrTalk(
        0x103,
        (
            "#00202F#5Pフランさん……\x01",
            "よかったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x105,
        (
            "#10404F#12Pフフ、アッバスの仕事も\x01",
            "少しは楽になりそうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x15,
        (
            "#01309F#5Pふふっ……\x01",
            "話がまとまったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    OP_93(0x19, 0x10E, 0x1F4)

    #C0248
    ChrTalk(
        0x101,
        (
            "#00000F#12Pああ……\x01",
            "そろそろ行くよ、セシル姉。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x15,
        (
            "#01304F#5Pええ、くれぐれも気を付けてね。\x02\x03",

            "#01303F私は直接、みんなの力に\x01",
            "なってあげる事はできないけど……\x02\x03",

            "#01302Fここで仕事をしながら\x01",
            "みんなの無事を祈っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00004F#12Pありがとう。\x01",
            "……それで十分だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x103,
        (
            "#00202F#5P……セシルさん。\x01",
            "どうもお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x19,
        (
            "#06411F#11Pわ、わたしなんて……\x01",
            "ずっとお世話になりっぱなしで。\x02\x03",

            "#06406F#30Wぐすっ……ううっ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x15, 0x1)
    Sleep(150)

    #C0253
    ChrTalk(
        0x15,
        (
            "#01309F#5Pふふっ、可愛い顔が台無しよ？\x02\x03",

            "#01305Fそういえばフランさん、\x01",
            "荷物をまとめなくていいの？\x02\x03",

            "#01302F着替えくらいは持っていった方が\x01",
            "いいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x19,
        "#06405F#11Pい、急いで荷造りしなくちゃ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 500)

    #C0255
    ChrTalk(
        0x19,
        (
            "#06412F#5Pちょ、ちょっとだけ\x01",
            "待っててくださいね！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x19, 0, 0, 29)
    OP_68(-12440, 1500, 5080, 3500)
    MoveCamera(62, 19, 0, 3500)
    OP_6E(440, 3500)
    SetCameraDistance(21000, 3500)
    Sleep(200)
    SetChrSubChip(0x105, 0x2)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(3800)
    OP_68(-13080, 1500, 4550, 3000)
    MoveCamera(39, 20, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(18910, 3000)
    Sleep(1000)
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x15, 0x0)
    OP_6F(0x79)

    #C0256
    ChrTalk(
        0x101,
        "#00002F#12Pはは……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x107,
        (
            "#01203F#11P#3Cフム、なかなか\x01",
            "賑やかになりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x105,
        (
            "#10402F#12Pメルカバの中も\x01",
            "少しは華やぎそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x15,
        "#01304F#5Pふふっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0260
    ChrTalk(
        0x15,
        (
            "#01305F#5Pそういえば……\x02\x03",

            "#01300Fよかったら待っている間、\x01",
            "イリアとドノバンさんに\x01",
            "挨拶でもしていく？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0261
    ChrTalk(
        0x101,
        (
            "#00005F#12Pえ……！？\x01",
            "もしかして２人とも……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x15,
        "#01304F#5Pええ、無事目を覚ましたわ。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#00206F#5Pイリアさんの方は\x01",
            "まだ歩けないみたいですが……\x02\x03",

            "#00202Fドノバン警部の方は\x01",
            "順調に回復しているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00009F#12Pそうか……よかった。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x105,
        (
            "#10402F#12Pただ待ってるのも何だし\x01",
            "お邪魔してみようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        "#00000F#12Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x103,
        "#00204F#5Pわたしもお付き合いします。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x107,
        (
            "#01200F#11P#3Cフム、病人を混乱させそうなので\x01",
            "私はここで待っているとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19160, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ツァイトがパーティから一時離脱しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_32(0xFF, 0xF9, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -12040, 150, 6900, 180)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrPos(0x16, -10490, 0, 6320, 315)
    SetChrFlags(0x16, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658E")
    SetChrFlags(0x15, 0x10)

    label("loc_658E")

    SetChrPos(0x0, -10000, 0, 2500, 90)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    SetScenarioFlags(0x1A0, 5)
    OP_29(0xAF, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_503B end

    def Function_29_65D3(): pass

    label("Function_29_65D3")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x8000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x138, 0x3E80, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x10B, 0x1F40, 0x1388, 0x1)
    Return()

    # Function_29_65D3 end

    def Function_30_6621(): pass

    label("Function_30_6621")

    EventBegin(0x0)
    Fade(500)
    OP_68(-10410, 1400, 5420, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18740, 0)
    SetChrPos(0x101, -9460, 0, 4970, 277)
    SetChrPos(0x102, -8430, 0, 6280, 277)
    SetChrPos(0x103, -9710, 0, 6350, 277)
    SetChrPos(0x104, -8540, 0, 5090, 277)
    SetChrPos(0x109, -9270, 0, 7610, 232)
    SetChrPos(0x105, -8750, 0, 3940, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x17, 0x2)
    SetChrSubChip(0x18, 0x1)
    OP_0D()

    #C0271
    ChrTalk(
        0x18,
        "#5Pあら、あなたたち。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#11P#00000Fリンさん、エオリアさん……\x01",
            "ウルスラ病院に来てたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        "#11P#00100F何かの依頼があったんですか？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x17,
        (
            "#6Pいや、今から幻獣の調査に行くから、\x01",
            "その準備を整えてたところさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x17,
        (
            "#6Pこれから、アンタたちが幻獣を退治した\x01",
            "ウルスラ間道の中州に行くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x17,
        (
            "#6P報告にあった『蒼い花』と\x01",
            "幻獣との因果関係を調べるためにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x18,
        (
            "#5Pちなみに復帰したアリオスさんは、\x01",
            "目撃された残りの幻獣の\x01",
            "退治に当たっているところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        "#5P#10105Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#11P#00300F何か、手伝えることはあるッスか？\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x18,
        "#5Pううん、任せてもらって平気よ。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x18,
        (
            "#5Pでもそうね、帰ってきた時に\x01",
            "ティオちゃんとスキンシップできるなら、\x01",
            "いくらでも頑張れると思うわ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        "#4S#11P#00203Fお断りします。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x18,
        "#5Pきゃん、そんな～……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        "#10302Fアハハ、相変わらずだね。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x17,
        "#6Pま、心配はいらないってことさ。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x17,
        (
            "#6Pアンタたちはアンタたちの\x01",
            "できることをやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#11P#00000Fええ、分かりました。\x01",
            "そちらも頑張ってください。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -9520, 0, 6040, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_6621 end

    def Function_31_6AD7(): pass

    label("Function_31_6AD7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(-12750, 2200, 5380, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x15, -11900, 200, 6850, 180)
    SetChrPos(0x105, -12800, 200, 6850, 180)
    SetChrPos(0x102, -13700, 200, 6850, 180)
    SetChrPos(0x101, -11900, 200, 3600, 0)
    SetChrPos(0x109, -12800, 200, 3600, 0)
    SetChrPos(0x104, -13700, 200, 3600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-12750, 1000, 5380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    #C0288
    ChrTalk(
        0x15,
        (
            "#5P#01300F……それじゃあ、\x01",
            "ティオちゃんはもう少しの間\x01",
            "帰ってこれないのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ、色々と\x01",
            "忙しいみたいでさ。\x02\x03",

            "#00002Fきっと今頃、レマン自治州で\x01",
            "がんばってるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x15,
        (
            "#5P#01304Fそっかあ……\x01",
            "それじゃ、会えるのが楽しみねえ。\x02\x03",

            "#01309Fふふ、帰ってきたら\x01",
            "色々と土産話を聞かせてもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#12P#00009Fはは……そうだね。\x02\x03",

            "#00000Fティオもきっと、\x01",
            "セシル姉に会えたら喜ぶと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrSubChip(0x109, 0x2)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)
    OP_64(0x109)

    #C0292
    ChrTalk(
        0x109,
        "#6P#10105Fへえ……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        "#5P#10304Fふぅん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    #C0294
    ChrTalk(
        0x101,
        "#12P#00005Fな、なんだよ２人とも。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    #C0295
    ChrTalk(
        0x109,
        (
            "#6P#10109Fい、いやあ……\x01",
            "噂には聞いてましたけど、\x01",
            "本当に仲がいいんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x105,
        (
            "#5P#10302Fなかなか間に入れなくて\x01",
            "ちょっと妬けるねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x101,
        "#12P#00006Fあ、あのなあ……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#6P#00306Fちっ、コイツは\x01",
            "これだからよ～。\x02\x03",

            "#00301F普通、こんなお姉さんと\x01",
            "子供の頃から知り合いってだけでも\x01",
            "とんだラッキー野郎だっつのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        (
            "#5P#00106Fほんと、その通りよね……\x02\x03",

            "#00111Fそれを当然だと思ってたら\x01",
            "いつかバチがあたるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#12P#00006Fい、意味分かんないから……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x15,
        "#5P#01309Fふふ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #C0302
    ChrTalk(
        0x15,
        (
            "#5P#01305Fあ、そういえば\x01",
            "つい話し込んじゃったけど……\x02\x03",

            "#01300F今日は何の用で病院に\x01",
            "来たんだったかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)

    #C0303
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあ……そうだった。\x02\x03",

            "#00000F……コホン、実は……\x01",
            "セイランド教授っていう人から\x01",
            "支援課に依頼が来てたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x109,
        (
            "#6P#10100F確か、薬学・神経科の後任の方が\x01",
            "来られたんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x15,
        (
            "#5P#01302Fええ、そうなの。\x02\x03",

            "#01303Fヨアヒム先生が得体のしれない\x01",
            "薬を作っていたことが公表されて、\x01",
            "病院は一時騒然としていたわ。\x02\x03",

            "#01308F教授たちはしばらく、\x01",
            "仕事の傍らアフターケアに\x01",
            "奔走していたけど……\x02\x03",

            "#01300F最近になって、ようやく\x01",
            "患者さんの信頼を取り戻せてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#12P#00303Fそりゃあ……\x01",
            "大変だったッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x15,
        (
            "#5P#01309Fふふ……\x01",
            "おかげさまで何とかなったわね。\x02\x03",

            "#01300Fあの事件の傷跡も癒えてきて、\x01",
            "ようやくウルスラ病院は\x01",
            "新しい一歩を踏み出したわ。\x02\x03",

            "その一環として、\x01",
            "新しくレミフェリアから\x01",
            "呼ばれたのがセイランド教授なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x102,
        (
            "#5P#00100Fあの有名な医療機器メーカー、\x01",
            "セイランド社の関係者……ですね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    #C0309
    ChrTalk(
        0x15,
        (
            "#11P#01300Fええ、創業者の親戚筋に\x01",
            "あたるはずよ。\x02\x03",

            "#01304F女性の方なんだけど、\x01",
            "雰囲気が凛としていて\x01",
            "とってもかっこいいんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#12P#00309Fおお、女医センセイッスか！\x01",
            "こりゃあ期待大だぜェ！\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#12P#00006Fふ、雰囲気はともかく……\x02\x03",

            "#00000Fなるほど、今度は\x01",
            "身元もばっちり\x01",
            "保証されてるわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        (
            "#5P#10300Fフム、教授というからには、\x01",
            "腕も確かなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x15,
        (
            "#11P#01300Fレミフェリアでも\x01",
            "有名な薬学・神経科の研究者みたい。\x02\x03",

            "#01304Fついこの間も、重い病気で\x01",
            "入院していたミハイル君の手術を\x01",
            "見事に成功させたのよ。\x02\x03",

            "#01300F今は、シズクちゃんの手術に向けて\x01",
            "準備を進めているのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        "#5P#00105Fシズクちゃんの……！\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#00000Fそうか……\x01",
            "確かに凄い先生みたいだね。\x02\x03",

            "そのセイランド教授だけど……\x01",
            "今、どこにいるか分かるかな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0316
    ChrTalk(
        0x15,
        (
            "#5P#01300Fええ、たいてい研究棟の\x01",
            "研究室にこもってるわ。\x02\x03",

            "受付でセラさんに言えば、\x01",
            "取り次いでもらえると思う。\x02\x03",

            "#01309Fふふ、せっかくだから\x01",
            "そこまで一緒に行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、助かるよ。\x01",
            "……それじゃあ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1530", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6AD7 end

    def Function_32_780B(): pass

    label("Function_32_780B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6500, 1000, 9690, 0)
    MoveCamera(72, 25, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -7150, 0, 9330, 45)
    SetChrPos(0x102, -8240, 0, 9720, 45)
    SetChrPos(0x103, -6600, 0, 8189, 45)
    SetChrPos(0x109, -8980, 0, 8720, 45)
    SetChrPos(0x105, -7760, 0, 7150, 45)
    SetChrPos(0x104, -7950, 0, 8280, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0318
    ChrTalk(
        0x8,
        (
            "あらま、いらっしゃい。\x01",
            "何か食べていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0320
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

    #C0321
    ChrTalk(
        0x8,
        (
            "ああ、グルメガイドの話かい。\x01",
            "通信社の人から聞いてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        "……でも、困ったねえ。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x102,
        "#00105F何か、問題でもあるんですか？\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        (
            "ウチのお勧め料理はかなりの時間、\x01",
            "煮込む必要があるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "この前、ちょうどその取り置きが\x01",
            "無くなっちゃってねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "悪いんだけど、今はまだ\x01",
            "あんたたちに振舞う準備が\x01",
            "整っていないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        "#00303Fんー、それじゃあ仕方ねえか。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x103,
        (
            "#00200F出来上がるまでには\x01",
            "どれくらいかかりそうですか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B84")

    #C0329
    ChrTalk(
        0x8,
        (
            "そうさね、昨晩から\x01",
            "仕込み始めた所だから……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "完成するのは２日後、\x01",
            "明後日ってところだろうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD3")

    label("loc_7B84")


    #C0331
    ChrTalk(
        0x8,
        (
            "そうさね、一昨日から\x01",
            "仕込み始めた所だから……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        "完成するのは明日だね。\x02",
    )

    CloseMessageWindow()

    label("loc_7BD3")


    #C0333
    ChrTalk(
        0x109,
        "#10105Fみ、３日も煮込むんですか……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、さぞ味が染みてそうだ。\x01",
            "これは完成が楽しみだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "ああ、きっと美味しいはずさ。\x01",
            "完成する頃になったら忘れずにおいで。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    OP_29(0x80, 0x1, 0x9)
    SetScenarioFlags(0x179, 1)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6960, 0, 9540, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_32_780B end

    def Function_33_7CC1(): pass

    label("Function_33_7CC1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6500, 1000, 9690, 0)
    MoveCamera(72, 25, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -7150, 0, 9330, 45)
    SetChrPos(0x102, -8240, 0, 9720, 45)
    SetChrPos(0x103, -6600, 0, 8189, 45)
    SetChrPos(0x109, -8980, 0, 8720, 45)
    SetChrPos(0x105, -7760, 0, 7150, 45)
    SetChrPos(0x104, -7950, 0, 8280, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_7EA8")

    #C0336
    ChrTalk(
        0x8,
        (
            "ああ、あんたたち。\x01",
            "忘れずに来たみたいだね。\x02",
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

    #C0337
    ChrTalk(
        0x101,
        "#00005Fと、いうことは……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "ああ、うちのお勧め料理\x01",
            "『三日煮込みシチュー』が\x01",
            "ようやく完成したのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        "早速食べていくかい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8014")

    label("loc_7EA8")


    #C0340
    ChrTalk(
        0x8,
        (
            "あらま、いらっしゃい。\x01",
            "何か食べていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "特務支援課の者なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0342
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

    #C0343
    ChrTalk(
        0x8,
        (
            "ああ、グルメガイドの話かい。\x01",
            "通信社の人から聞いてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        "いや、丁度いいところに来たね。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "ついさっき、うちのお勧め料理\x01",
            "『三日煮込みシチュー』が\x01",
            "完成した所なのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        "早速食べていくかい？\x02",
    )

    CloseMessageWindow()

    label("loc_8014")


    #C0347
    ChrTalk(
        0x103,
        "#00200Fええ、是非よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "それじゃあ、ちょっとお待ち。\x01",
            "今、人数分よそってあげるからね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6E(380, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは三日煮込みシチューを食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0350
    ChrTalk(
        0x109,
        "#10105F#4S……お、美味しいッ……！！\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x104,
        (
            "#00309Fああ……すっげえトロトロで、\x01",
            "めちゃくちゃ味が染みてるな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_8215")

    #C0352
    ChrTalk(
        0x105,
        "#10302Fフフ、待った甲斐があったね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8253")

    label("loc_8215")


    #C0353
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、こんな雨の日には\x01",
            "最高の食事かもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8253")


    #C0354
    ChrTalk(
        0x102,
        (
            "#00100Fええ、本当に……\x01",
            "こんなに美味しいシチュー、\x01",
            "生まれて初めてかもしれないわ……！\x02\x03",

            "#00103F体も温まるし、栄養もたっぷりで\x01",
            "とっても体にいいんじゃないかしら。\x02\x03",

            "#00109F病気の人も、これを食べただけで\x01",
            "たちまち元気になってしまいそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(500)
    TurnDirection(0x101, 0x102, 500)
    Sleep(500)

    #C0355
    ChrTalk(
        0x101,
        "#00009Fとても幸せそうな顔だなあ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0356
    ChrTalk(
        0x8,
        "あはは、大袈裟な子だねえ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0357
    ChrTalk(
        0x103,
        (
            "#00200Fエリィさんがものすごく\x01",
            "気に入ったみたいですし……\x01",
            "ここの記事は任せてよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#00000Fはは、そうだな。\x01",
            "エリィ、頼めるか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0359
    ChrTalk(
        0x102,
        "#00100Fええ、是非とも任せてちょうだい。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x173, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_84C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_84E4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_84F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_850A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_850A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8527")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_853A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_853A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8557")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_856A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_856A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8587")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_859A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_859A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_85B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85B7")

    OP_29(0x80, 0x1, 0xA)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86BA")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0360
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_86B1")

    #A0361
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

    label("loc_86B1")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_86BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_878B")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0362
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

    #A0363
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

    label("loc_878B")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0xE1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6960, 0, 9540, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_7CC1 end

    SaveToFile()

Try(main)
