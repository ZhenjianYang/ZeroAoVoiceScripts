from ScenarioHelper import *

def main():
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
        "琪尔修宿舍长",           # 1
        "实习医生芙萝拉",         # 2
        "实习医生米修",           # 3
        "探视者",                 # 4
        "探视者",                 # 5
        "探视者",                 # 6
        "探视者",                 # 7
        "探视者",                 # 8
        "珀利塞",                 # 9
        "塔普",                   # 10
        "探视者",                 # 11
        "男性",                   # 12
        "探视者",                 # 13
        "塞茜尔",                 # 14
        "神狼蔡特",               # 15
        "游击士林",               # 16
        "游击士艾欧莉娅",         # 17
        "芙兰",                   # 18
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
        "Function_8_1818",         # 08, 8
        "Function_9_1DF1",         # 09, 9
        "Function_10_2684",        # 0A, 10
        "Function_11_2B00",        # 0B, 11
        "Function_12_2BE7",        # 0C, 12
        "Function_13_2CAA",        # 0D, 13
        "Function_14_2CF2",        # 0E, 14
        "Function_15_2D6A",        # 0F, 15
        "Function_16_2DDA",        # 10, 16
        "Function_17_2F30",        # 11, 17
        "Function_18_30FD",        # 12, 18
        "Function_19_32E5",        # 13, 19
        "Function_20_35EB",        # 14, 20
        "Function_21_36F8",        # 15, 21
        "Function_22_386C",        # 16, 22
        "Function_23_39D3",        # 17, 23
        "Function_24_3A50",        # 18, 24
        "Function_25_3B0E",        # 19, 25
        "Function_26_430C",        # 1A, 26
        "Function_27_4370",        # 1B, 27
        "Function_28_43DE",        # 1C, 28
        "Function_29_56DE",        # 1D, 29
        "Function_30_572C",        # 1E, 30
        "Function_31_5B30",        # 1F, 31
        "Function_32_6666",        # 20, 32
        "Function_33_6A2A",        # 21, 33
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1814")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B51")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B70")
    OP_AF(0x5F)
    Jump("loc_B92")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B80")
    OP_AF(0x5E)
    Jump("loc_B92")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B90")
    OP_AF(0x5D)
    Jump("loc_B92")

    label("loc_B90")

    OP_AF(0x5C)

    label("loc_B92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180F")

    label("loc_BA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180F")

    label("loc_BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD5")
    Jump("loc_180F")

    label("loc_BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_C7C")

    #C0001
    ChrTalk(
        0x8,
        (
            "呵呵，我们的\x01",
            "久煮炖菜很棒吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "患者们和外来的客人都赞不绝口，\x01",
            "说吃了之后就精神十足呢。\x01",
            "以后有机会就再来吃吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3F")

    label("loc_C7C")


    #C0003
    ChrTalk(
        0x8,
        (
            "我们这里的推荐料理\x01",
            "需要花很多时间来\x01",
            "久煮慢炖。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF9")

    #C0004
    ChrTalk(
        0x8,
        (
            "要等到两天之后\x01",
            "才能完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "到时候别忘了\x01",
            "再来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3F")

    label("loc_CF9")


    #C0006
    ChrTalk(
        0x8,
        (
            "要等到明天\x01",
            "才能完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "再等一天就可以了，\x01",
            "明天别忘了再来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3F")

    Jump("loc_180F")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_EB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1E")

    #C0008
    ChrTalk(
        0x8,
        (
            "刚才接到了哈罗德先生的联络，\x01",
            "他稍后就会来医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "我拜托他多带些\x01",
            "阿尔摩利卡产的蔬菜，\x01",
            "这下总算能做点像样的料理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "丰盛的食物比什么都重要嘛。\x01",
            "这样一来，患者们\x01",
            "应该也会精神一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB0")

    label("loc_E1E")


    #C0011
    ChrTalk(
        0x8,
        (
            "我拜托哈罗德先生多带些\x01",
            "阿尔摩利卡产的蔬菜，\x01",
            "这下总算能做点像样的料理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "丰盛的食物比什么都重要嘛。\x01",
            "这样一来，患者们\x01",
            "应该也会精神一些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB0")

    Jump("loc_180F")

    label("loc_EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F1A")

    #C0013
    ChrTalk(
        0x8,
        (
            "滞留在这里的\x01",
            "外来客人们\x01",
            "似乎越来越疲劳了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "希望他们能尽快回到\x01",
            "克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180F")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE5")

    #C0015
    ChrTalk(
        0x8,
        (
            "市里虽然\x01",
            "配发了粮食，\x01",
            "但大多都是储藏食品。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "唉唉，要做病号餐的话，\x01",
            "营养终究还是\x01",
            "不平衡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "也许是心理作用吧，\x01",
            "患者和外来客人们的表情都好阴沉……\x01",
            "我得想想办法啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1055")

    label("loc_FE5")


    #C0018
    ChrTalk(
        0x8,
        (
            "光靠市里配给的粮食，\x01",
            "营养终究还是\x01",
            "不平衡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "要是能像以前一样，\x01",
            "从阿尔摩利卡村进到\x01",
            "新鲜的蔬菜就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055")

    Jump("loc_180F")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_117D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1112")

    #C0020
    ChrTalk(
        0x8,
        (
            "那两个市里来的孩子\x01",
            "好像是彩虹剧团的忠实支持者。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "他们原本是来探望伊莉娅的，\x01",
            "自从独立宣言发表以后，\x01",
            "就留在医院帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "呵呵，真是好心的孩子啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1178")

    label("loc_1112")


    #C0023
    ChrTalk(
        0x8,
        (
            "自从独立宣言发表以后，\x01",
            "那两个伊莉娅的忠实支持者\x01",
            "就留在医院帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "呵呵，真是好心的孩子啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1178")

    Jump("loc_180F")

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1235")

    #C0025
    ChrTalk(
        0x8,
        (
            "病号餐的菜单\x01",
            "是由我负责的……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "在这次的住院患者中，\x01",
            "有不少人受了重伤，\x01",
            "连饭都无法吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "食物是活力之源，\x01",
            "真希望他们尽快恢复到\x01",
            "可以进餐的程度啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A0")

    label("loc_1235")


    #C0028
    ChrTalk(
        0x8,
        (
            "虽然会通过给他们\x01",
            "打点滴来补充营养……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "但食物是活力之源，\x01",
            "真希望他们尽快恢复到\x01",
            "可以进餐的程度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A0")

    Jump("loc_180F")

    label("loc_12A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1389")

    #C0030
    ChrTalk(
        0x8,
        (
            "昨天出动了好多急救车，\x01",
            "我还在想，到底出了什么事。\x01",
            "没想到是列车脱轨事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "铁道公司为了赔偿之类的事情，\x01",
            "应该已经忙乱不堪了，\x01",
            "没有人遇难，真是万幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "话说回来……\x01",
            "究竟是什么原因造成的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13E6")

    label("loc_1389")


    #C0033
    ChrTalk(
        0x8,
        (
            "列车事故究竟是\x01",
            "什么原因造成的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "没有人遇难，\x01",
            "倒也算是万幸，\x01",
            "但还是很令人在意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E6")

    Jump("loc_180F")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_149C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1466")

    #C0035
    ChrTalk(
        0x8,
        (
            "亚里欧斯先生\x01",
            "昨天晚上就回协会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "虽然小滴正处在关键时期，\x01",
            "但他实在太忙，也没有办法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1497")

    label("loc_1466")


    #C0037
    ChrTalk(
        0x8,
        (
            "好了，今天给寄宿的孩子们\x01",
            "做点什么吃的呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1497")

    Jump("loc_180F")

    label("loc_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_15DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1559")

    #C0038
    ChrTalk(
        0x8,
        (
            "亚里欧斯先生\x01",
            "为了小滴的手术，\x01",
            "在这里住了一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "有这么出色的父亲\x01",
            "陪着她，\x01",
            "小滴也能安心不少吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "只是手术的结果\x01",
            "很令人遗憾。\x01",
            "唉……真叫人难过啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15D9")

    label("loc_1559")


    #C0041
    ChrTalk(
        0x8,
        (
            "亚里欧斯先生为了陪小滴，\x01",
            "在这里住了一段时间，\x01",
            "应该能让她安心不少吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "只是手术的结果\x01",
            "很令人遗憾。\x01",
            "唉……真叫人难过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D9")

    Jump("loc_180F")

    label("loc_15DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1663")

    #C0043
    ChrTalk(
        0x8,
        (
            "游击士艾欧莉娅小姐\x01",
            "今天过来工作，\x01",
            "我请她吃了个午餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "医院经常接受\x01",
            "她的帮助，\x01",
            "这也算是些回礼吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A7")

    label("loc_1663")


    #C0045
    ChrTalk(
        0x8,
        (
            "医院经常受到\x01",
            "游击士的关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "所以偶尔也该\x01",
            "请她吃个午餐嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A7")

    Jump("loc_180F")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_172B")

    #C0047
    ChrTalk(
        0x8,
        (
            "阿尔伯特大公\x01",
            "年纪轻轻，就成为\x01",
            "雷米菲利亚的国家元首了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "听说国民们都很仰慕他……\x01",
            "一定是位优秀的人物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_180F")

    label("loc_172B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_180F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D8")

    #C0049
    ChrTalk(
        0x8,
        (
            "医院里新来了\x01",
            "一批实习医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "看，那边那个孩子叫米修。\x01",
            "听说他是在克洛斯贝尔市\x01",
            "自学成才的。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "我最喜欢勤奋的人了，\x01",
            "要多给他些优惠才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_180F")

    label("loc_17D8")


    #C0052
    ChrTalk(
        0x8,
        "我最喜欢勤奋的人了。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "要多给新人些\x01",
            "优惠才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180F")

    Jump("loc_AF2")

    label("loc_1814")

    TalkEnd(0x8)
    Return()

    # Function_7_AA0 end

    def Function_8_1818(): pass

    label("Function_8_1818")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_187B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1836")
    Call(0, 9)
    Jump("loc_1876")

    label("loc_1836")


    #C0054
    ChrTalk(
        0x9,
        (
            "米修，多吃点，\x01",
            "要吃饱哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "哎呀，吃那么快，\x01",
            "会噎着的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    Jump("loc_1DED")

    label("loc_187B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_18E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")
    Call(0, 9)
    Jump("loc_18E2")

    label("loc_1896")


    #C0056
    ChrTalk(
        0x9,
        (
            "……总之，我们对此\x01",
            "也无能为力……\x01",
            "现在还是集中精力，做好医院的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E2")

    Jump("loc_1DED")

    label("loc_18E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1952")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1902")
    Call(0, 9)
    Jump("loc_194D")

    label("loc_1902")


    #C0057
    ChrTalk(
        0x9,
        (
            "米修也越来\x01",
            "越成熟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "之前还吵着说，\x01",
            "看着这种书\x01",
            "怎么能吃得下饭。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194D")

    Jump("loc_1DED")

    label("loc_1952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_19E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196D")
    Call(0, 9)
    Jump("loc_19E1")

    label("loc_196D")


    #C0059
    ChrTalk(
        0x9,
        (
            "学习贵在坚持。\x01",
            "要是偷懒一天，\x01",
            "需要三天才能补回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "即使担心市里的情况，\x01",
            "也还是要努力学习。\x01",
            "……明白了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E1")

    Jump("loc_1DED")

    label("loc_19E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A01")
    Call(0, 9)
    Jump("loc_1A4C")

    label("loc_1A01")


    #C0061
    ChrTalk(
        0x9,
        (
            "……来，米修，你也坐下。\x01",
            "为了在下午保持充沛精力，必须要填饱肚子才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4C")

    Jump("loc_1DED")

    label("loc_1A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6C")
    Call(0, 9)
    Jump("loc_1AF3")

    label("loc_1A6C")


    #C0062
    ChrTalk(
        0x9,
        (
            "只要做好自己的事情，\x01",
            "就一定会得到公正的评价……\x01",
            "至于工作，就算不想干，也会不断增多的。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "总之，伤员们能得救，\x01",
            "就该感到开心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF3")

    Jump("loc_1DED")

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B5C")

    #C0064
    ChrTalk(
        0x9,
        (
            "好了，距离今天的讲义\x01",
            "还有点时间～\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "米修还没有来，\x01",
            "我就一边吃早饭一边自习吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DED")

    label("loc_1B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B77")
    Call(0, 9)
    Jump("loc_1BF8")

    label("loc_1B77")


    #C0066
    ChrTalk(
        0x9,
        (
            "从跟随前任指导教授的时候开始，\x01",
            "利顿就一直在拼命用功。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "要论学习，我也不会输给他，\x01",
            "但他在现场那么努力，\x01",
            "没有成长才怪呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF8")

    Jump("loc_1DED")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C18")
    Call(0, 9)
    Jump("loc_1C90")

    label("loc_1C18")


    #C0068
    ChrTalk(
        0x9,
        (
            "（嚼嚼）……\x01",
            "嗯，身为实习医生，\x01",
            "这是每个人的必经之路啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "今后也不可能\x01",
            "一直不吃午饭吧？\x01",
            "呵呵，很快就会习惯的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C90")

    Jump("loc_1DED")

    label("loc_1C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB0")
    Call(0, 9)
    Jump("loc_1D03")

    label("loc_1CB0")


    #C0070
    ChrTalk(
        0x9,
        (
            "米修是第一次\x01",
            "去手术现场旁观吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        "呵呵……就让我见识一下他的心理素质吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1D03")

    Jump("loc_1DED")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA0")

    #C0072
    ChrTalk(
        0x9,
        (
            "我被委任指导\x01",
            "新来的米修。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "嗯，虽然学习时间\x01",
            "减少了……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "不过，这也算是学习的一环嘛。\x01",
            "机会难得，我可要严加管教。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DED")

    label("loc_1DA0")


    #C0075
    ChrTalk(
        0x9,
        (
            "嗯，指导可爱的后辈\x01",
            "也算是学习的一环嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "机会难得，我可要严加管教。\x02",
    )

    CloseMessageWindow()

    label("loc_1DED")

    TalkEnd(0x9)
    Return()

    # Function_8_1818 end

    def Function_9_1DF1(): pass

    label("Function_9_1DF1")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EB8")

    #C0077
    ChrTalk(
        0x9,
        (
            "米修，有很多伤员\x01",
            "被送来了医院，\x01",
            "赶快填饱肚子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "今天你也要去现场\x01",
            "努力工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "是、是！\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "好，要加油了～！！\x01",
            "（狼吞虎咽）……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "啊哈哈，吃那么快，\x01",
            "会噎着哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_1EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F9D")

    #C0082
    ChrTalk(
        0x9,
        (
            "独立无效宣言吗……\x01",
            "今后到底会变成怎样呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "真担心旧城区\x01",
            "公寓里的各位啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "回市里的申请似乎\x01",
            "也暂时没人受理……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "……总之，我们对此\x01",
            "也无能为力……\x01",
            "现在还是集中精神，做好医院的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        "……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_1F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2098")

    #C0087
    ChrTalk(
        0x9,
        (
            "（嚼嚼）……\x01",
            "然后呢，如这个图解所示，\x01",
            "人的内脏是……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "（咬咬）……\x01",
            "唔，原来如此……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "……呵呵，话说回来，\x01",
            "米修也越来\x01",
            "越成熟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "之前还吵着说，\x01",
            "看着这种书\x01",
            "怎么能吃得下饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "（嚼嚼）……\x01",
            "哈哈，这多亏了\x01",
            "前辈的教育啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_2098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_217E")

    #C0092
    ChrTalk(
        0x9,
        (
            "米修，\x01",
            "最近有没有努力学习？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "这个……\x01",
            "其实精神有点难以集中。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔变成这样，\x01",
            "我很担心公寓里的各位……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "是吗……\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "不过，等你镇定下来之后，\x01",
            "还是要好好学习哦。\x01",
            "……明白吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_217E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2274")

    #C0097
    ChrTalk(
        0xA,
        (
            "在袭击事件的受害者中，\x01",
            "有些人最终还是伤重不治……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        "前辈……我觉得好沮丧。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "……我明白你的心情。\x01",
            "可是，就算想诉苦抱怨，\x01",
            "也等到一切都结束之后吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "现在要是有那个空闲，\x01",
            "不如尽量多救治一个伤员。\x01",
            "这才是我们的职责。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_267C")

    label("loc_2274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2373")

    #C0101
    ChrTalk(
        0x9,
        "呼，终于可以喘口气了。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "话说回来，\x01",
            "米修也很努力地\x01",
            "帮了忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "哪、哪里……\x01",
            "我还差得远。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "说是帮忙，\x01",
            "也只不过是打打杂而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "不要谦虚，\x01",
            "打杂也是重要的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "最近你好像已经\x01",
            "不晕血了……\x01",
            "也算是成长了一些。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_267C")

    label("loc_2373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_245D")

    #C0107
    ChrTalk(
        0xA,
        (
            "利顿前辈经常去\x01",
            "手术现场做助手，\x01",
            "或是负责巡诊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xA,
        (
            "唉，我这个新人\x01",
            "果然没法\x01",
            "和他比啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "毕竟从跟随前任指导教授的时候开始，\x01",
            "利顿就一直在拼命用功。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "好啦，不要着急，不要着急。\x01",
            "想成长就要努力学习啦。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_267C")

    label("loc_245D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2588")

    #C0111
    ChrTalk(
        0x9,
        "（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "……怎么了？米修，\x01",
            "不去点餐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "不、不……\x01",
            "今早不是有外科手术的\x01",
            "实地研修吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "我第一次观看真正的手术，\x01",
            "总觉得完全没有食欲了……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        "啊～果然是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "（嚼嚼）……\x01",
            "嗯，这是每个人的必经之路啦，\x01",
            "很快就会习惯的。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "……呜呕……\x01",
            "希、希望如此吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267C")

    label("loc_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_267C")

    #C0118
    ChrTalk(
        0x9,
        (
            "对了，米修，\x01",
            "你明天要参加盖里教授的\x01",
            "外科手术实地研修吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "这好像还是你第一次\x01",
            "观看真正的手术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        "嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "嘿嘿，感觉真正的医生\x01",
            "学习终于开始了～\x01",
            "我现在就开始期待了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x9,
        (
            "呵呵……气势不错。\x01",
            "嗯，你就多多加油吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)

    label("loc_267C")

    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_1DF1 end

    def Function_10_2684(): pass

    label("Function_10_2684")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A2")
    Call(0, 9)
    Jump("loc_26CB")

    label("loc_26A2")


    #C0123
    ChrTalk(
        0xA,
        (
            "（嚼嚼嚼嚼）……！！\x01",
            "咳、咳……！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26CB")

    Jump("loc_2AFC")

    label("loc_26D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_273A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EB")
    Call(0, 9)
    Jump("loc_2735")

    label("loc_26EB")


    #C0124
    ChrTalk(
        0xA,
        (
            "是啊……回不了市里\x01",
            "也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "希望事态能\x01",
            "稍微有些好转……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2735")

    Jump("loc_2AFC")

    label("loc_273A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")
    Call(0, 9)
    Jump("loc_2783")

    label("loc_2755")


    #C0126
    ChrTalk(
        0xA,
        (
            "（嚼嚼）……\x01",
            "哈哈，这多亏了\x01",
            "前辈的教育。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2783")

    Jump("loc_2AFC")

    label("loc_2788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2802")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A3")
    Call(0, 9)
    Jump("loc_27FD")

    label("loc_27A3")


    #C0127
    ChrTalk(
        0xA,
        (
            "是啊……\x01",
            "虽然很担心公寓里的各位……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "但如果以此为借口而不学习，\x01",
            "或许就是任性了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FD")

    Jump("loc_2AFC")

    label("loc_2802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281D")
    Call(0, 9)
    Jump("loc_2871")

    label("loc_281D")


    #C0129
    ChrTalk(
        0xA,
        "……前辈说的对啊……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "总而言之，\x01",
            "现在应该考虑的事情是\x01",
            "如何救治更多的患者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2871")

    Jump("loc_2AFC")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2891")
    Call(0, 9)
    Jump("loc_28C8")

    label("loc_2891")


    #C0131
    ChrTalk(
        0xA,
        (
            "嗯，我也不能光做杂事，\x01",
            "要成长到能够身肩重任才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C8")

    Jump("loc_2AFC")

    label("loc_28CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28DB")
    Jump("loc_2AFC")

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2962")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F6")
    Call(0, 9)
    Jump("loc_295D")

    label("loc_28F6")


    #C0132
    ChrTalk(
        0xA,
        (
            "嗯……确实如此，\x01",
            "心急也无济于事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "……话虽如此，前辈，\x01",
            "还是不要在吃饭时\x01",
            "看解剖学的书了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295D")

    Jump("loc_2AFC")

    label("loc_2962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297D")
    Call(0, 9)
    Jump("loc_29D7")

    label("loc_297D")


    #C0134
    ChrTalk(
        0xA,
        (
            "呜呜，前辈在手术之后，\x01",
            "竟然还吃得下这种\x01",
            "肉做的料理啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        "呜，一想起来就作呕……\x02",
    )

    CloseMessageWindow()

    label("loc_29D7")

    Jump("loc_2AFC")

    label("loc_29DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F7")
    Call(0, 9)
    Jump("loc_2A34")

    label("loc_29F7")


    #C0136
    ChrTalk(
        0xA,
        "哈哈，放心吧！\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "我会努力学习，\x01",
            "争取不给前辈丢脸的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A34")

    Jump("loc_2AFC")

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC4")

    #C0138
    ChrTalk(
        0xA,
        (
            "芙萝拉前辈虽然有些严厉，\x01",
            "但是教学方法很巧妙，\x01",
            "学识也相当渊博。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "能够遇到这么\x01",
            "好的前辈，\x01",
            "真是太幸运了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2AFC")

    label("loc_2AC4")


    #C0140
    ChrTalk(
        0xA,
        (
            "芙萝拉前辈能不能\x01",
            "不要在吃饭的时候\x01",
            "看解剖的书呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFC")

    TalkEnd(0xA)
    Return()

    # Function_10_2684 end

    def Function_11_2B00(): pass

    label("Function_11_2B00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BBC")

    #C0141
    ChrTalk(
        0xFE,
        (
            "我们的儿子\x01",
            "在那起袭击事件中受了重伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "虽然保住一命，\x01",
            "但是现在还在集中治疗室里……\x01",
            "探望也只能看很短一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "唉，女神啊……\x01",
            "请救救我儿子吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2BE3")

    label("loc_2BBC")


    #C0144
    ChrTalk(
        0xFE,
        (
            "唉，女神啊……\x01",
            "请救救我儿子吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE3")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B00 end

    def Function_12_2BE7(): pass

    label("Function_12_2BE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6C")

    #C0145
    ChrTalk(
        0xFE,
        (
            "我儿子是与武装集团作战的\x01",
            "警备队员之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "……早知道会有这种事，\x01",
            "当初就该反对他\x01",
            "加入警备队……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2CA6")

    label("loc_2C6C")


    #C0147
    ChrTalk(
        0xFE,
        (
            "……早知道会有这种事，\x01",
            "当初就该反对他\x01",
            "加入警备队……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA6")

    TalkEnd(0xFE)
    Return()

    # Function_12_2BE7 end

    def Function_13_2CAA(): pass

    label("Function_13_2CAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CEE")

    #C0148
    ChrTalk(
        0xFE,
        (
            "爸爸妈妈好像\x01",
            "非常难过。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "哥哥现在\x01",
            "怎么样了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CEE")

    TalkEnd(0xFE)
    Return()

    # Function_13_2CAA end

    def Function_14_2CF2(): pass

    label("Function_14_2CF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D66")

    #C0150
    ChrTalk(
        0xFE,
        (
            "袭击事件之后，我的儿子和儿媳\x01",
            "就在这家医院里住院。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "虽然确认了他们的安全……\x01",
            "可还是放心不下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D66")

    TalkEnd(0xFE)
    Return()

    # Function_14_2CF2 end

    def Function_15_2D6A(): pass

    label("Function_15_2D6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DD6")

    #C0152
    ChrTalk(
        0xFE,
        (
            "发生了那种事，\x01",
            "警察局和警备队都遭受了巨大损害……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔今后\x01",
            "究竟会变成怎样呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD6")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D6A end

    def Function_16_2DDA(): pass

    label("Function_16_2DDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DEB")
    Jump("loc_2F2C")

    label("loc_2DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2E57")

    #C0154
    ChrTalk(
        0x10,
        (
            "我要去伊莉娅小姐的病房\x01",
            "送病号餐了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x10,
        (
            "怎、怎么办……\x01",
            "见到她以后，我该说什么好！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2C")

    label("loc_2E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2EC3")

    #C0156
    ChrTalk(
        0x10,
        (
            "好想大喊伊莉娅小姐的名字，\x01",
            "让她在病房也能听到。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x10,
        (
            "但这里是医院……\x01",
            "必须要忍耐才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2C")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2F2C")

    #C0158
    ChrTalk(
        0x10,
        (
            "伊莉娅小姐恢复意识了，\x01",
            "真是太好了！\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x10,
        (
            "我没有回市里，一直在这里\x01",
            "祈祷她恢复，终于奏效了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2C")

    TalkEnd(0xFE)
    Return()

    # Function_16_2DDA end

    def Function_17_2F30(): pass

    label("Function_17_2F30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F41")
    Jump("loc_30F9")

    label("loc_2F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2FDB")

    #C0160
    ChrTalk(
        0x11,
        (
            "冷、冷静点，珀利塞……\x01",
            "还要给其他患者\x01",
            "送饭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x11,
        (
            "要是一不小心，连伊莉娅小姐的餐\x01",
            "都给打翻，那就不得了啦。\x01",
            "平常心，要保持平常心……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F9")

    label("loc_2FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3081")

    #C0162
    ChrTalk(
        0x11,
        (
            "为了让伊莉娅小姐尽快康复，\x01",
            "我们决定留在这里帮忙，也算是祈愿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x11,
        (
            "虽然那位宿舍长阿姨很会使唤人……\x01",
            "但只要想到是为了伊莉娅小姐，这就不算什么了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F9")

    label("loc_3081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_30F9")

    #C0164
    ChrTalk(
        0x11,
        (
            "现在是非常时期，\x01",
            "必须要把探望\x01",
            "伊莉娅小姐的想法忍耐住。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x11,
        (
            "同时，还要在医院努力帮忙，\x01",
            "多少发挥一些作用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F9")

    TalkEnd(0xFE)
    Return()

    # Function_17_2F30 end

    def Function_18_30FD(): pass

    label("Function_18_30FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_310E")
    Jump("loc_32E1")

    label("loc_310E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_311C")
    Jump("loc_32E1")

    label("loc_311C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_312A")
    Jump("loc_32E1")

    label("loc_312A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3138")
    Jump("loc_32E1")

    label("loc_3138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_32E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315B")
    Call(0, 19)
    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_315B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325E")

    #C0166
    ChrTalk(
        0x15,
        (
            "#01300F和蔡特在一起，\x01",
            "心情就会很平静。\x02\x03",

            "#01304F虽然并没有见过几次面，但不知为何，\x01",
            "见到它就会觉得很安心……\x02\x03",

            "#01300F就像看到了老朋友一样，\x01",
            "有种令人怀念的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        (
            "#10400F哈哈，简直像是\x01",
            "命中注定的恋人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        "#00003F（有点羡慕啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_32D9")

    label("loc_325E")


    #C0169
    ChrTalk(
        0x15,
        (
            "#01300F有蔡特在身边，\x01",
            "心情就会很平静。\x02\x03",

            "#01304F不知为何，感觉非常安心……\x01",
            "就像见到了老朋友一样，\x01",
            "有种令人怀念的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D9")

    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_32E1")

    TalkEnd(0xFE)
    Return()

    # Function_18_30FD end

    def Function_19_32E5(): pass

    label("Function_19_32E5")

    OP_4B(0x16, 0xFF)

    #C0170
    ChrTalk(
        0x15,
        (
            "#01300F说起来，自总统演讲那天之后，\x01",
            "就一直没有见过蔡特了。\x02\x03",

            "#01303F你追着被亚里欧斯先生\x01",
            "带走的琪雅，\x01",
            "然后就消失了踪影……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x16,
        (
            "#3C#01200F嗯，我虽然追了过去……\x01",
            "但那『剑圣』驾船驶入湖中，\x01",
            "把我彻底甩开了。\x02\x03",

            "虽然对不起罗伊德他们，\x01",
            "但为了今后能卷土重来，\x01",
            "我回到了部下们的身边。\x02\x03",

            "#01203F如今想来，真是让当时在场的你\x01",
            "担了不必要的心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x15,
        (
            "#01302F嘻嘻，不用担心我啦。\x01",
            "蔡特没事\x01",
            "就再好不过了。\x02\x03",

            "#01300F而且你现在不是也在拼命\x01",
            "帮助罗伊德和瓦吉吗～\x02\x03",

            "#01304F呵呵，谢谢你。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塞茜尔温柔地抚摸了蔡特的头。\x07\x00\x02",
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
            "#01303F呵呵，不知为什么，只要和蔡特\x01",
            "在一起，心情就会很平静呢。\x02\x03",

            "#01305F啊……对不起。\x01",
            "我这样随便抚摸你，\x01",
            "会让你不高兴吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x16,
        (
            "#3C#01200F……呵呵，不会。\x01",
            "完全没有不舒服的感觉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 1)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_19_32E5 end

    def Function_20_35EB(): pass

    label("Function_20_35EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_36F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3609")
    Call(0, 19)
    Jump("loc_36F4")

    label("loc_3609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A7")

    #C0177
    ChrTalk(
        0x16,
        "#3C#01203F……呵呵………………\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F（蔡特怎么了？\x01",
            "  突然就沉默下来……）\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00200F（是被塞茜尔小姐抚摸，\x01",
            "  感到害羞了吗？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_36F4")

    label("loc_36A7")


    #C0180
    ChrTalk(
        0x16,
        (
            "#3C#01200F……为了不吓到患者们，\x01",
            "我就在这里等着。\x02\x03",

            "你们几个去探望就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F4")

    TalkEnd(0xFE)
    Return()

    # Function_20_35EB end

    def Function_21_36F8(): pass

    label("Function_21_36F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EE")

    #C0181
    ChrTalk(
        0xFE,
        (
            "不久前，我丈夫的老毛病发作了，\x01",
            "我急忙叫了急救车，把他送到这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "虽说申请顺利通过了……\x01",
            "但是审查流程非常严格，如果当时\x01",
            "没能批准，可就……想想真是后怕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "呼……像现在这样待在医院，\x01",
            "说不定反而更加安心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3868")

    label("loc_37EE")


    #C0184
    ChrTalk(
        0xFE,
        (
            "不久前，我丈夫的老毛病发作了，\x01",
            "我急忙叫了急救车，把他送到这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "呼……像现在这样待在医院，\x01",
            "说不定反而更加安心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3868")

    TalkEnd(0xFE)
    Return()

    # Function_21_36F8 end

    def Function_22_386C(): pass

    label("Function_22_386C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_39CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3945")

    #C0186
    ChrTalk(
        0xFE,
        (
            "因为不能来医院，\x01",
            "我把家里的药吃完以后，\x01",
            "老毛病就又发作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "禁行令到底有多麻烦，\x01",
            "我这次可真是切身体会到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "要想回市里，还得等到\x01",
            "国防军下次过来……\x01",
            "暂时就在这里放松一阵吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_39CF")

    label("loc_3945")


    #C0189
    ChrTalk(
        0xFE,
        (
            "通过这次进医院的事情，\x01",
            "我真是切身体会到了\x01",
            "禁行令到底有多麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "要想回市里，还得等到\x01",
            "国防军下次过来……\x01",
            "暂时就在这里放松一阵吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CF")

    TalkEnd(0xFE)
    Return()

    # Function_22_386C end

    def Function_23_39D3(): pass

    label("Function_23_39D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3A4C")

    #C0191
    ChrTalk(
        0xFE,
        (
            "本打算今天回市里……\x01",
            "这到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "无效宣言和我又没关系，\x01",
            "把我一个人带回市里\x01",
            "总不会有问题吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4C")

    TalkEnd(0xFE)
    Return()

    # Function_23_39D3 end

    def Function_24_3A50(): pass

    label("Function_24_3A50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A61")
    Jump("loc_3B0A")

    label("loc_3A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7C")
    Call(0, 30)
    Jump("loc_3B0A")

    label("loc_3A7C")


    #C0193
    ChrTalk(
        0xFE,
        (
            "为了调查报告中的『蓝花』\x01",
            "和幻兽之间的因果关系，\x01",
            "我们要去乌尔斯拉间道的河滩。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "哦，不用担心我们。\x01",
            "你们只要专心\x01",
            "做好自己的工作就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0A")

    TalkEnd(0xFE)
    Return()

    # Function_24_3A50 end

    def Function_25_3B0E(): pass

    label("Function_25_3B0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B1F")
    Jump("loc_4308")

    label("loc_3B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3A")
    Call(0, 30)
    Jump("loc_3C93")

    label("loc_3B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1E")

    #C0195
    ChrTalk(
        0xFE,
        (
            "咳咳，说起来，\x01",
            "关于那种蓝花……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "你们在报告书上提到，\x01",
            "它似乎是『真知』的\x01",
            "原材料啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "听说主谋约亚西姆·琼塔\x01",
            "在教团事件中大量\x01",
            "制造了那种药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "他所用的原料『灵智之草』\x01",
            "又是从哪里弄到手的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3C93")

    label("loc_3C1E")


    #C0199
    ChrTalk(
        0xFE,
        (
            "听说主谋约亚西姆·琼塔\x01",
            "在教团事件中大量\x01",
            "制造了那种药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "他所用的原料『灵智之草』\x01",
            "又是从哪里弄到手的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C93")

    Jump("loc_4308")

    label("loc_3C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3CA6")
    Jump("loc_4308")

    label("loc_3CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB6")

    #C0201
    ChrTalk(
        0x101,
        "#00005F咦，艾欧莉娅小——\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D84")
    Jump("loc_3DCE")

    label("loc_3D84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DCE")

    label("loc_3DA4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DC4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3DCE")

    label("loc_3DC4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3DCE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0202
    ChrTalk(
        0xFE,
        (
            "#4S小、小缇欧……\x01",
            "你终于回来了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x103,
        "#00202F……你好，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "啊啊……\x01",
            "这一天……我已经期盼很久了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "快过来，小缇欧！\x01",
            "让姐姐亲亲！！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        "#00203F……容我坚决拒绝。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "啊啊，这种感觉也好久没有过了……⊥\x02",
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
            "#00211F（……好像比以前\x01",
            "  更难对付了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00012F（哈、哈哈……这么久没见，\x01",
            "  大概积蓄了很多思念吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1C0, 7)
    Jump("loc_4308")

    label("loc_3FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B4")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4051")
    Jump("loc_409B")

    label("loc_4051")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4071")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_409B")

    label("loc_4071")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4091")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_409B")

    label("loc_4091")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_409B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0210
    ChrTalk(
        0xFE,
        (
            "我接受委托，来这里送货，\x01",
            "竟然能遇到小缇欧……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        "这难道是命中注定的吗！？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#00211F不是。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "唔，回答得好干脆……⊥\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        (
            "#00309F艾欧莉娅小姐，\x01",
            "不然就由我来代替……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "哦，不要⊥\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#00306F（打击）……\x01",
            "回答得一样干脆！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4304")

    label("loc_41B4")

    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4245")
    Jump("loc_428F")

    label("loc_4245")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4265")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428F")

    label("loc_4265")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4285")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428F")

    label("loc_4285")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_428F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0217
    ChrTalk(
        0xFE,
        (
            "呵呵，小缇欧，\x01",
            "下次要让我亲密接触哦⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#00203F（依然需要多加小心……）\x02",
    )

    CloseMessageWindow()

    label("loc_4304")

    SetChrSubChip(0xFE, 0x0)

    label("loc_4308")

    TalkEnd(0xFE)
    Return()

    # Function_25_3B0E end

    def Function_26_430C(): pass

    label("Function_26_430C")

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
            "三层：女性职员宿舍→\x01\x01",
            "←二层：男性职员宿舍\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_430C end

    def Function_27_4370(): pass

    label("Function_27_4370")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            " 探病者·门诊患者用住宿设施\x01",
            "※需要使用时，请向宿舍长申请\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_4370 end

    def Function_28_43DE(): pass

    label("Function_28_43DE")

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
        "#00206F#5P……竟然有这种事……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x19,
        (
            "#06406F#5P真、真相实在太过惊人了，\x01",
            "我一时还不能理清……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x15,
        (
            "#01303F#5P只有一件事可以确定……\x02\x03",

            "#01308F我们所居住的克洛斯贝尔，\x01",
            "正因为经历了那些过往之事，才会走到今天。\x02\x03",

            "#01301F而如今这种状况，以及小琪雅的事情，也都由此而起……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#00008F#12P……嗯。\x02\x03",

            "#00003F我只有两个愿望──\x02\x03",

            "亲手解明至今未能\x01",
            "水落石出的真相。\x02\x03",

            "#00013F以及解救大家，\x01",
            "夺回琪雅。\x02",
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
            "#10409F#12P呵呵，虽说只有两个愿望，\x01",
            "但似乎极其艰难呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x107,
        "#01203F#11P#3C唔，这就是本性吧。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x103,
        (
            "#00202F#5P呵呵……\x01",
            "这才是罗伊德前辈嘛。\x02\x03",

            "#00204F我的想法与\x01",
            "罗伊德前辈一样。\x02\x03",

            "#00203F我也是支援科的成员……\x02\x03",

            "#00201F更是琪雅的监护人，\x01",
            "请带我一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#00004F#12P谢谢你，缇欧，\x01",
            "那我就不客气地借助你的力量啦。\x02\x03",

            "#00005F话说回来，缇欧为什么\x01",
            "会被带到这里？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x103,
        (
            "#00206F#5P……多半是玛丽亚贝尔小姐\x01",
            "或亚里欧斯先生的指示。\x02\x03",

            "#00208F将支援科的成员分别隔离\x01",
            "在不同场所，并进行监视……\x02\x03",

            "#00201F他们恐怕担心，如果随意把\x01",
            "我们放在一起，我们就会\x01",
            "团结一致，对琪雅造成影响吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00006F#12P原来如此……\x02\x03",

            "#00008F也就是说，艾莉和兰迪\x01",
            "应该也都在不同的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x105,
        (
            "#10406F#12P唔……如果是在克洛斯贝尔市内，\x01",
            "就很难解救他们了……\x02\x03",

            "#10402F不过，既然缇欧在这里，\x01",
            "就说明他们在市外的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x15,
        (
            "#01306F#5P是啊……因为总统肯定想\x01",
            "尽量避免你们四人接近琪雅。\x02",
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

    def lambda_4A8D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_4A8D)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0233
    ChrTalk(
        0x19,
        (
            "#06403F#5P那、那个……！\x02\x03",

            "#06401F能不能把我也\x01",
            "一起带去！？\x02",
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
        "#00005F#6P芙兰……？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x15,
        "#01305F#5P芙兰小姐？\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x19,
        (
            "#06406F#5P虽、虽然我不能像大家\x01",
            "一样上场战斗……\x02\x03",

            "#06403F但作为熟悉终端操作的通讯员，\x01",
            "应该可以发挥一些作用！\x02\x03",

            "#06401F毕竟你们要乘坐瓦吉先生的\x01",
            "飞艇行动，所以……\x02\x03",

            "拜托了……！\x01",
            "我很想帮上忙！\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        "#00001F#6P芙兰……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0238
    ChrTalk(
        0x103,
        "#00208F#5P罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x105,
        (
            "#10406F#12P嗯，『梅尔卡瓦』上的确人手不足，\x01",
            "你如果来帮忙，自然再好不过。\x02\x03",

            "#10400F不过，这个问题还是\x01",
            "要由罗伊德来决定。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    #C0240
    ChrTalk(
        0x101,
        "#00006F#6P……这个嘛。\x02",
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
            "#00003F#6P芙兰，你的姐姐\x01",
            "正在为国防军效力。\x02\x03",

            "#00008F你如果跟我们一起行动，\x01",
            "就意味着与诺艾尔对立……\x02\x03",

            "#00001F你明白吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x19,
        (
            "#06406F#5P……明、明白……！\x02\x03",

            "#06408F我当然不想\x01",
            "和姐姐对立……\x02\x03",

            "#06401F但即使如此……我也是\x01",
            "克洛斯贝尔警察局的一员！\x02\x03",

            "面对这种危急情况……\x01",
            "我绝不能置之不理！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#00003F#6P是吗……\x02\x03",

            "#00002F明白了，\x01",
            "那就拜托你帮忙了。\x02",
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
        "#06409F#5P非、非常感谢！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    #C0245
    ChrTalk(
        0x103,
        (
            "#00202F#5P芙兰小姐……\x01",
            "太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x105,
        (
            "#10404F#12P呵呵，看来阿巴斯的工作\x01",
            "也可以轻松些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x15,
        (
            "#01309F#5P呵呵……\x01",
            "看来你们已经商量好了呢。\x02",
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
            "#00000F#12P嗯……\x01",
            "我们这就要走了，塞茜尔姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x15,
        (
            "#01304F#5P嗯，千万要多加小心哦。\x02\x03",

            "#01303F虽然无法直接\x01",
            "协助大家……\x02\x03",

            "#01302F但我会在这里一边努力工作，\x01",
            "一边祈祷大家平安无事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#00004F#12P谢谢，\x01",
            "这就足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x103,
        (
            "#00202F#5P……塞茜尔小姐，\x01",
            "承蒙您这段时间的照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x19,
        (
            "#06411F#11P我、我也是……\x01",
            "一直蒙受您的照顾。\x02\x03",

            "#06406F#30W呜……呜呜……\x02",
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
            "#01309F#5P呵呵，别哭，太浪费那张可爱的小脸啦。\x02\x03",

            "#01305F对了，芙兰小姐，\x01",
            "你不用去收拾行李吗？\x02\x03",

            "#01302F像换洗衣物之类的东西，\x01",
            "还是带上为好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x19,
        "#06405F#11P是、是的，我得赶紧去收拾了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 500)

    #C0255
    ChrTalk(
        0x19,
        (
            "#06412F#5P请、请大家\x01",
            "稍等我一下！\x02",
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
        "#00002F#12P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x107,
        (
            "#01203F#11P#3C唔，好像\x01",
            "越来越热闹了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x105,
        (
            "#10402F#12P梅尔卡瓦里\x01",
            "也会多点亮色呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x15,
        "#01304F#5P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0260
    ChrTalk(
        0x15,
        (
            "#01305F#5P对了……\x02\x03",

            "#01300F如果各位方便，要不要趁现在\x01",
            "去和伊莉娅，还有多诺邦警督\x01",
            "打个招呼？\x02",
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
            "#00005F#12P哎……！？\x01",
            "难道他们二位都……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x15,
        "#01304F#5P嗯，已经恢复意识了。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#00206F#5P伊莉娅小姐\x01",
            "目前还不能走动……\x02\x03",

            "#00202F多诺邦警督则\x01",
            "恢复得很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00009F#12P是吗……太好了。\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x105,
        (
            "#10402F#12P在这里干等着也是浪费时间，\x01",
            "不如去打扰一下吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        "#00000F#12P嗯，我们走吧。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x103,
        "#00204F#5P我也陪你们一起去。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x107,
        (
            "#01200F#11P#3C唔，我可能会吓到患者，\x01",
            "还是在这里等你们吧。\x02",
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
            "蔡特暂时离队。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧加入队伍。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5699")
    SetChrFlags(0x15, 0x10)

    label("loc_5699")

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

    # Function_28_43DE end

    def Function_29_56DE(): pass

    label("Function_29_56DE")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x8000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x138, 0x3E80, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x10B, 0x1F40, 0x1388, 0x1)
    Return()

    # Function_29_56DE end

    def Function_30_572C(): pass

    label("Function_30_572C")

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
        "#5P哎呀，是你们。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#11P#00000F林小姐、艾欧莉娅小姐……\x01",
            "你们来乌尔斯拉医院了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        "#11P#00100F接到了什么委托吗？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x17,
        (
            "#6P不，我们打算去调查幻兽，\x01",
            "所以正在做准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x17,
        (
            "#6P接下来，要去你们消灭过幻兽的\x01",
            "地点——乌尔斯拉间道河滩。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x17,
        (
            "#6P调查一下报告中提到的『蓝花』\x01",
            "与幻兽之间的因果关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x18,
        (
            "#5P顺带一提，亚里欧斯先生已经\x01",
            "重新投身工作，现在动身出发\x01",
            "去消灭其它幻兽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        "#5P#10105F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        "#11P#00300F有没有什么事情需要我们帮忙？\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x18,
        "#5P没有，放心交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x18,
        (
            "#5P不过，回来的时候，\x01",
            "如果能让我和小缇欧亲密接触一下，\x01",
            "我就会更有干劲了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        "#4S#11P#00203F我拒绝。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x18,
        "#5P呀，怎么能这样……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        "#10302F啊哈哈，还是老样子呢。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x17,
        "#6P嗯，总之不用担心啦。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x17,
        (
            "#6P你们就专心做好\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#11P#00000F嗯，明白了，\x01",
            "你们也加油。\x02",
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

    # Function_30_572C end

    def Function_31_5B30(): pass

    label("Function_31_5B30")

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
            "#5P#01300F……也就是说，\x01",
            "小缇欧还要再过\x01",
            "一阵子才能回来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，她似乎\x01",
            "很忙碌。\x02\x03",

            "#00002F现在一定正在\x01",
            "列曼自治州努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x15,
        (
            "#5P#01304F是吗……\x01",
            "那就期待她的归来了。\x02\x03",

            "#01309F呵呵，等她回来以后，\x01",
            "可要多打听些旅行见闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#12P#00009F哈哈……是啊。\x02\x03",

            "#00000F缇欧也一定\x01",
            "很期待再见到塞茜尔姐姐。\x02",
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
        "#6P#10105F嘿……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        "#5P#10304F嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    #C0294
    ChrTalk(
        0x101,
        "#12P#00005F你、你们两个怎么了？\x02",
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
            "#6P#10109F不，没什么啦……\x01",
            "之前就已有所耳闻了，如今看来，\x01",
            "你们的感情确实很好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x105,
        (
            "#5P#10302F外人完全没有介入的机会，\x01",
            "真是有点嫉妒。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x101,
        "#12P#00006F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#6P#00306F啧，这小子\x01",
            "一直都是这么气人～\x02\x03",

            "#00301F一般来说，能和这样的\x01",
            "大姐姐从小一起长大，\x01",
            "就已经够幸运的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        (
            "#5P#00106F说的没错……\x02\x03",

            "#00111F如果你认为一切都是理所当然的，\x01",
            "迟早会遭到报应哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x101,
        "#12P#00006F你、你们真是莫名其妙……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x15,
        "#5P#01309F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    #C0302
    ChrTalk(
        0x15,
        (
            "#5P#01305F啊，一不小心\x01",
            "就光顾着聊天了……\x02\x03",

            "#01300F你们今天来医院\x01",
            "有什么事吗？\x02",
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
            "#12P#00005F哦……对了。\x02\x03",

            "#00000F……其实……\x01",
            "有位名叫赛兰德的教授\x01",
            "给支援科发来了委托。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x109,
        (
            "#6P#10100F好像是来接任\x01",
            "药物学·神经科的医生吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x15,
        (
            "#5P#01302F嗯，是的。\x02\x03",

            "#01303F约亚西姆医生制造了\x01",
            "可怕药物一事被公开之后，\x01",
            "引起了一阵轩然大波。\x02\x03",

            "#01308F有一段时期，教授们\x01",
            "在工作之余还得负责\x01",
            "患者的疗后调养工作……\x02\x03",

            "#01300F直到最近，总算挽回了\x01",
            "患者们对医院的信赖。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#12P#00303F这……\x01",
            "还真是很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x15,
        (
            "#5P#01309F呵呵……\x01",
            "还好总算撑过去了。\x02\x03",

            "#01300F那起事件留下的伤痕已经平复，\x01",
            "乌尔斯拉医院终于\x01",
            "迈出了新的一步。\x02\x03",

            "作为复兴工作的一环，\x01",
            "医院特意从雷米菲利亚\x01",
            "聘来了赛兰德教授。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x102,
        (
            "#5P#00100F那位教授应该与著名医疗器械厂商\x01",
            "赛兰德公司有些关系吧……？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    #C0309
    ChrTalk(
        0x15,
        (
            "#11P#01300F嗯，好像是\x01",
            "创始人的亲戚。\x02\x03",

            "#01304F虽然是位女性，\x01",
            "但感觉很有威严，\x01",
            "非常帅气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#12P#00309F哦哦，女医生吗！？\x01",
            "这可真是值得期待啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#12P#00006F感、感觉什么的暂且不提……\x02\x03",

            "#00000F至少在身份方面，\x01",
            "总算有安全\x01",
            "保证了。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        (
            "#5P#10300F唔，既然是教授，\x01",
            "本事应该相当了得吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x15,
        (
            "#11P#01300F嗯，据说她在雷米菲利亚\x01",
            "也是著名的药物学·神经科研究者。\x02\x03",

            "#01304F就在前一阵子，\x01",
            "还给重病住院的米海尔\x01",
            "顺利完成了手术。\x02\x03",

            "#01300F她现在正在准备\x01",
            "给小滴做手术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        "#5P#00105F给小滴……！\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#00000F是吗……\x01",
            "看来的确是个很厉害的医生。\x02\x03",

            "你知道赛兰德教授\x01",
            "现在在哪里吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    #C0316
    ChrTalk(
        0x15,
        (
            "#5P#01300F嗯，她一般都待在\x01",
            "研究楼的研究室里。\x02\x03",

            "只要和接待处的塞拉小姐说一声，\x01",
            "她就会帮你们联系的。\x02\x03",

            "#01309F呵呵，机会难得，\x01",
            "我就带你们过去好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，真是帮大忙啦，\x01",
            "那我们这就走吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1530", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5B30 end

    def Function_32_6666(): pass

    label("Function_32_6666")

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
            "哎呀，欢迎光临，\x01",
            "要吃点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#00000F打扰了，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0320
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

    #C0321
    ChrTalk(
        0x8,
        (
            "啊，美食向导啊，\x01",
            "我听通讯社的人说过。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        "……不过，真是伤脑筋呢。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x102,
        "#00105F有什么问题吗？\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        (
            "我们这里的推荐料理需要\x01",
            "花很长时间久煮慢炖……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "但以前的存货又刚好\x01",
            "卖完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "现在还没法\x01",
            "请你们吃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        "#00303F嗯，那就没办法啦。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x103,
        (
            "#00200F要多久才能\x01",
            "做好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6927")

    #C0329
    ChrTalk(
        0x8,
        (
            "这个嘛，从昨晚\x01",
            "就开始准备了……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "要到两天之后才能完成，\x01",
            "也就是后天了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6964")

    label("loc_6927")


    #C0331
    ChrTalk(
        0x8,
        (
            "这个嘛，从前天\x01",
            "就开始准备了……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        "要到明天才能完成。\x02",
    )

    CloseMessageWindow()

    label("loc_6964")


    #C0333
    ChrTalk(
        0x109,
        "#10105F要、要煮整整三天吗……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，那肯定会相当入味吧，\x01",
            "真期待它的完成啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "嗯，一定很美味的，\x01",
            "到时候别忘了再来啊。\x02",
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

    # Function_32_6666 end

    def Function_33_6A2A(): pass

    label("Function_33_6A2A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_6BE7")

    #C0336
    ChrTalk(
        0x8,
        (
            "啊，是你们啊，\x01",
            "看来你们还没忘呢。\x02",
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
        "#00005F如此说来……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "嗯，我们的推荐料理\x01",
            "『三日久煮炖菜』\x01",
            "终于完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x8,
        "你们赶快尝尝吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D09")

    label("loc_6BE7")


    #C0340
    ChrTalk(
        0x8,
        (
            "哎呀，欢迎光临，\x01",
            "要吃点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#00000F打扰了，\x01",
            "我们是特别任务支援科的成员……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0342
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

    #C0343
    ChrTalk(
        0x8,
        (
            "啊，美食向导啊，\x01",
            "我听通讯社的人说过。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        "哎呀，你们来得正是时候。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "我们这里的推荐料理\x01",
            "『三日久煮炖菜』\x01",
            "刚刚做好。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        "你们赶快尝尝吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6D09")


    #C0347
    ChrTalk(
        0x103,
        "#00200F嗯，那就麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "好，稍等一下，\x01",
            "我这就给你们每人准备一份。\x02",
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
            "罗伊德等人品尝了三日久煮炖菜。\x07\x00\x02",
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
        "#10105F#4S……真、真美味……！！\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x104,
        (
            "#00309F嗯……煮得入口即化，\x01",
            "而且相当入味啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_6EC4")

    #C0352
    ChrTalk(
        0x105,
        "#10302F呵呵，不枉我们等这么久啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EF6")

    label("loc_6EC4")


    #C0353
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，在这种雨天，\x01",
            "真是最棒的美食啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF6")


    #C0354
    ChrTalk(
        0x102,
        (
            "#00100F嗯，确实……\x01",
            "如此美味的炖菜……\x01",
            "恐怕是有生以来第一次吃到呢！\x02\x03",

            "#00103F既可以暖身子，又有丰富的营养，\x01",
            "肯定很有益于健康吧。\x02\x03",

            "#00109F就算是病人，吃下它之后\x01",
            "大概也能立刻恢复精神。\x02",
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
        "#00009F好像很幸福的表情啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    #C0356
    ChrTalk(
        0x8,
        "啊哈哈，真是个夸张的孩子。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0357
    ChrTalk(
        0x103,
        (
            "#00200F艾莉前辈好像\x01",
            "非常中意呢……\x01",
            "这道料理的报道就交给她来写吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，是啊。\x01",
            "艾莉，那就交给你了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0359
    ChrTalk(
        0x102,
        "#00100F嗯，请务必让我来写。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x173, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_7106")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_7123")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_7136")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_7149")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_7166")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_7179")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_7196")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_71A9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_71C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_71D9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_71F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71F6")

    OP_29(0x80, 0x1, 0xA)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72CB")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0360
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72C2")

    #A0361
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

    label("loc_72C2")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_72CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738E")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0362
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

    #A0363
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

    label("loc_738E")

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

    # Function_33_6A2A end

    SaveToFile()

Try(main)
