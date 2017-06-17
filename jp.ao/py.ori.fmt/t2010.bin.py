from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2010.bin",                # FileName
        "t2010",                    # MapName
        "t2010",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 5, 0, 6],
    )

    BuildStringList((
        "t2010",                  # 0
        "コナーズ隊員",           # 1
        "シグ隊員",               # 2
        "ステラ",                 # 3
        "クレス隊員",             # 4
        "ビヨンド",               # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "女の子",                 # 9
        "観光客",                 # 10
        "観光客",                 # 11
        "ロメオ隊員",             # 12
        "ミレイユ三尉",           # 13
        "ハロルド",               # 14
        "遊撃士スコット",         # 15
        "遊撃士ヴェンツェル",     # 16
        "導力車",                 # 17
        "ソーニャ司令",           # 18
    ))

    AddCharChip((
        "chr/ch31202.itc",                   # 00
        "chr/ch24900.itc",                   # 01
        "chr/ch31200.itc",                   # 02
        "chr/ch24800.itc",                   # 03
        "chr/ch33000.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch33100.itc",                   # 06
        "chr/ch33102.itc",                   # 07
        "chr/ch33302.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch34402.itc",                   # 0A
        "chr/ch32400.itc",                   # 0B
        "chr/ch32402.itc",                   # 0C
        "chr/ch32600.itc",                   # 0D
        "chr/ch33200.itc",                   # 0E
        "chr/ch33202.itc",                   # 0F
        "chr/ch41400.itc",                   # 10
        "chr/ch41402.itc",                   # 11
        "chr/ch33300.itc",                   # 12
        "chr/ch09300.itc",                   # 13
        "chr/ch27202.itc",                   # 14
        "chr/ch27302.itc",                   # 15
    ))

    DeclNpc(-6590,   0,       7079,    200,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(16079,   0,       3700,    90,   261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(-105500, 0,       2099,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-97470,  150,     -3950,   270,  325,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-162110, 0,       -2500,   90,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   453,  0x0, 0,   5,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(579,     0,       4179,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-94669,  150,     2319,    90,   453,  0x0, 0,   8,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-3150,   0,       2960,    180,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-3500,   0,       3180,    145,  389,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-92129,  150,     4190,    270,  453,  0x0, 0,   15,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(3289,    0,       -8239,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(14180,   0,       -5670,   135,  389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-102099, 150,     2230,    90,   452,  0x0, 0,   20,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-99449,  150,     2230,    270,  452,  0x0, 0,   21,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-6600,   0,       6140,    1000,    -6590,   1500,    7080,    0x007E, 0,  7,  0x0000)
    DeclActor(-103650, 0,       1450,    1000,    -105500, 1500,    2100,    0x007E, 0,  10, 0x0000)
    DeclActor(-161140, 0,       -2700,   1000,    -162110, 1500,    -2500,   0x007E, 0,  13, 0x0000)
    DeclActor(3130,    0,       -12500,  1000,    3130,    1500,    -12500,  0x007C, 0,  31, 0x0000)

    ChipFrameInfo(1012, 0)                                       # 0

    ScpFunction((
        "Function_0_3F4",          # 00, 0
        "Function_1_4A4",          # 01, 1
        "Function_2_541",          # 02, 2
        "Function_3_5F2",          # 03, 3
        "Function_4_67B",          # 04, 4
        "Function_5_718",          # 05, 5
        "Function_6_ACA",          # 06, 6
        "Function_7_D77",          # 07, 7
        "Function_8_D7B",          # 08, 8
        "Function_9_18FC",         # 09, 9
        "Function_10_229B",        # 0A, 10
        "Function_11_229F",        # 0B, 11
        "Function_12_2FF7",        # 0C, 12
        "Function_13_3C9C",        # 0D, 13
        "Function_14_3CA0",        # 0E, 14
        "Function_15_4B2C",        # 0F, 15
        "Function_16_4DDF",        # 10, 16
        "Function_17_5074",        # 11, 17
        "Function_18_5339",        # 12, 18
        "Function_19_542C",        # 13, 19
        "Function_20_557E",        # 14, 20
        "Function_21_576B",        # 15, 21
        "Function_22_599B",        # 16, 22
        "Function_23_5B3B",        # 17, 23
        "Function_24_6195",        # 18, 24
        "Function_25_6243",        # 19, 25
        "Function_26_63A3",        # 1A, 26
        "Function_27_65D3",        # 1B, 27
        "Function_28_6AFF",        # 1C, 28
        "Function_29_73AB",        # 1D, 29
        "Function_30_7DE7",        # 1E, 30
        "Function_31_80B2",        # 1F, 31
    ))


    def Function_0_3F4(): pass

    label("Function_0_3F4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_42C"),
        (1, "loc_438"),
        (2, "loc_444"),
        (3, "loc_450"),
        (4, "loc_45C"),
        (5, "loc_468"),
        (6, "loc_474"),
        (SWITCH_DEFAULT, "loc_480"),
    )


    label("loc_42C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_438")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_444")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_450")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_45C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_468")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_4A3")

    Return()

    # Function_0_3F4 end

    def Function_1_4A4(): pass

    label("Function_1_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_540")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    Jump("Function_1_4A4")

    label("loc_540")

    Return()

    # Function_1_4A4 end

    def Function_2_541(): pass

    label("Function_2_541")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F1")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, -4560, 0, 4400, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_2_541")

    label("loc_5F1")

    Return()

    # Function_2_541 end

    def Function_3_5F2(): pass

    label("Function_3_5F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67A")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_3_5F2")

    label("loc_67A")

    Return()

    # Function_3_5F2 end

    def Function_4_67B(): pass

    label("Function_4_67B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_717")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    Jump("Function_4_67B")

    label("loc_717")

    Return()

    # Function_4_67B end

    def Function_5_718(): pass

    label("Function_5_718")

    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78C")
    SetChrChipByIndex(0x8, 0x10)
    SetChrChipByIndex(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 2)
    SetChrChipByIndex(0xB, 0x11)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x12)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, -3840, 0, -130, 270)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_A9B")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_889")
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x14)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x15)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DA")
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)

    label("loc_7DA")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x9, -3730, 0, -170, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0xB, 0x2)
    ClearChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 14120, 0, 3660, 180)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6110, 0, 5040, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -970, 0, 2740, 180)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -94700, 0, 4190, 90)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_A9B")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_918")
    BeginChrThread(0x9, 0, 0, 3)
    SetChrChipByIndex(0xD, 0x4)
    SetChrPos(0xD, -1100, 0, 3450, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrChipByIndex(0x12, 0xE)
    SetChrPos(0x12, 80, 0, 3450, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x40)
    BeginChrThread(0x12, 0, 0, 0)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -94670, 150, 2320, 90)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_A9B")

    label("loc_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_95D")
    BeginChrThread(0x9, 0, 0, 3)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -2190, 400, 9210, 152)
    Jump("loc_A9B")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_98C")
    BeginChrThread(0x9, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_A9B")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A0F")
    SetChrPos(0x9, -3730, 0, -170, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0xD, 0x4)
    SetChrPos(0xD, -1670, 0, 2760, 225)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0A")
    ClearChrFlags(0x13, 0x80)

    label("loc_A0A")

    Jump("loc_A9B")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A54")
    BeginChrThread(0x9, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -92130, 150, 2320, 270)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_A9B")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A9B")
    BeginChrThread(0x9, 0, 0, 3)
    TurnDirection(0xA, 0xB, 0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x15)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_AAA")
    ClearScenarioFlags(0x22, 0)
    Event(0, 30)

    label("loc_AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC9")
    Event(0, 29)

    label("loc_AC9")

    Return()

    # Function_5_718 end

    def Function_6_ACA(): pass

    label("Function_6_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF8")

    label("loc_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF8")

    SetMapObjFrame(0x8, "chukin", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B42")
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B7E")
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC6")
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    Jump("loc_C9D")

    label("loc_BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C02")
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C3E")
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetChrPos(0x18, -760, 100, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C7A")
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C8E")
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_C9D")

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C9D")
    ClearMapObjFlags(0x7, 0x4)

    label("loc_C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    SetMapObjFlags(0x5, 0x4)

    label("loc_CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE5")
    SetMapObjFlags(0x5, 0x4)

    label("loc_CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0B")
    SetMapObjFlags(0x5, 0x4)

    label("loc_D0B")

    OP_66(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D39")
    SetMapObjFlags(0xA, 0x4)
    OP_65(0x3, 0x1)

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D4C")
    SetMapObjFlags(0xA, 0x4)
    OP_65(0x3, 0x1)

    label("loc_D4C")

    OP_70(0x5, 0x8C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D76")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_D76")

    Return()

    # Function_6_ACA end

    def Function_7_D77(): pass

    label("Function_7_D77")

    Call(0, 8)
    Return()

    # Function_7_D77 end

    def Function_8_D7B(): pass

    label("Function_8_D7B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBC")

    #N0001
    NpcTalk(
        0x8,
        "兵士コナーズ",
        (
            "国境にかかる渡り橋は、\x01",
            "いまだに落ちたままだが、\x01",
            "帝国軍への警戒は厳重にしてる。\x02",
        )
    )

    CloseMessageWindow()

    #N0002
    NpcTalk(
        0x8,
        "兵士コナーズ",
        (
            "奴らが侵攻を始めようと思ったら、\x01",
            "落ちた橋なんてすぐにでも\x01",
            "修繕しちまえるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #N0003
    NpcTalk(
        0x8,
        "兵士コナーズ",
        (
            "幸か不幸か、帝国は内戦中……\x01",
            "今のうちに俺たちも\x01",
            "体勢を整えておかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F80")

    label("loc_EBC")


    #N0004
    NpcTalk(
        0x8,
        "兵士コナーズ",
        (
            "帝国軍が侵攻を始めようと思ったら、\x01",
            "落ちた橋なんてすぐにでも\x01",
            "修繕しちまえるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "兵士コナーズ",
        (
            "幸か不幸か、帝国は内戦中……\x01",
            "今のうちに俺たちも\x01",
            "体勢を整えておかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F80")

    Jump("loc_18F8")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_102F")

    #C0006
    ChrTalk(
        0x8,
        (
            "最近の緊張状態を鑑みて、\x01",
            "クロスベルを離れる外国人も\x01",
            "少なからずいるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "それでなくても、\x01",
            "物騒な事件が続いたからな……\x01",
            "仕方がないってところか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F8")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112D")

    #C0008
    ChrTalk(
        0x8,
        (
            "昨日、ミレイユ三尉の連れた部隊が\x01",
            "巨大な化物を目撃したそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "逃げてしまった化物の警戒に、\x01",
            "しばらくは一個中隊単位で\x01",
            "自治州内をパトロールするらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "やれやれ……\x01",
            "緊張状態も続いている中で\x01",
            "忙しさは増す一方だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11CB")

    label("loc_112D")


    #C0011
    ChrTalk(
        0x8,
        (
            "逃げてしまった化物の警戒に、\x01",
            "しばらくは一個中隊単位で\x01",
            "自治州内をパトロールするらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "やれやれ……\x01",
            "緊張状態も続いている中で\x01",
            "忙しさは増す一方だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CB")

    Jump("loc_18F8")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1271")

    #C0013
    ChrTalk(
        0x8,
        (
            "さっき、ここを通った帝国商人が、\x01",
            "クロスベルの独立について\x01",
            "色々と話していたようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "この話題は、帝国のほうでも\x01",
            "物議を醸してるみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F8")

    label("loc_1271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1371")

    #C0015
    ChrTalk(
        0x8,
        (
            "最近は、帝国の要塞内部で\x01",
            "これ見よがしに演習なんかが\x01",
            "行われているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "俺たち警備隊……\x01",
            "いや、今回の場合はディーター市長に\x01",
            "プレッシャーをかけてるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "『不戦条約』直前の\x01",
            "緊張状態に比べれば可愛いもんだがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13FC")

    label("loc_1371")


    #C0018
    ChrTalk(
        0x8,
        (
            "最近は、帝国の要塞内部で\x01",
            "これ見よがしな演習なんかが\x01",
            "行われているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "『不戦条約』直前の\x01",
            "緊張状態に比べれば可愛いもんだがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FC")

    Jump("loc_18F8")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")

    #C0020
    ChrTalk(
        0x8,
        (
            "テロリストの情報があったから、\x01",
            "チェックを厳重にしろとの\x01",
            "命令があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "今日の警戒体制なら、\x01",
            "陸路からの進入は\x01",
            "まず不可能なはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "それに、空路のほうも、\x01",
            "近くにある特別な施設から\x01",
            "警戒を続けているのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "飛行艇を配備できない警備隊でも、\x01",
            "出来る限りのことをやらなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15B5")

    label("loc_153F")


    #C0024
    ChrTalk(
        0x8,
        (
            "警備隊は、自治州法の規定で\x01",
            "飛行艇の所持が許可されないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "空の警備のためには\x01",
            "是非ほしいところなんだがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B5")

    Jump("loc_18F8")

    label("loc_15BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171E")

    #C0026
    ChrTalk(
        0x8,
        (
            "通商会議に来ているオズボーン宰相は、\x01",
            "俗に《鉄血宰相》と呼ばれている。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "これは、『国の安定は鉄と血、\x01",
            "即ち兵器と兵力によるべし』という\x01",
            "彼の信条に由来していてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "この言葉のもとに、\x01",
            "彼はいくつもの自治州を\x01",
            "帝国に武力併合してきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "クロスベル自治州にとって、\x01",
            "最も注意すべき人物の１人なのは\x01",
            "間違いないだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17D0")

    label("loc_171E")


    #C0030
    ChrTalk(
        0x8,
        (
            "帝国はいくつもの自治州を\x01",
            "武力併合してきたが、その多くに\x01",
            "《鉄血宰相》が関わっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "クロスベル自治州にとって、\x01",
            "最も注意すべき人物の１人なのは\x01",
            "間違いないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D0")

    Jump("loc_18F8")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")

    #C0032
    ChrTalk(
        0x8,
        (
            "そこの鉄柵を抜けると、\x01",
            "帝国の《ガレリア要塞》までは\x01",
            "あっという間だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "行くつもりなら注意してくれよ。\x01",
            "帝国は出入国者のチェックが\x01",
            "かなり厳重だからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18F8")

    label("loc_188E")


    #C0034
    ChrTalk(
        0x8,
        (
            "帝国は出入国者のチェックが\x01",
            "かなり厳重なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "《ガレリア要塞》に\x01",
            "行くつもりなら注意してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F8")

    TalkEnd(0x8)
    Return()

    # Function_8_D7B end

    def Function_9_18FC(): pass

    label("Function_9_18FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A05")

    #N0036
    NpcTalk(
        0x9,
        "兵士シグ",
        (
            "独立の無効宣言が出され、\x01",
            "国防長官は行方不明……\x01",
            "大統領も拘束されたと聞いた。\x02",
        )
    )

    CloseMessageWindow()

    #N0037
    NpcTalk(
        0x9,
        "兵士シグ",
        (
            "俺たちは、これからも国防軍として\x01",
            "働いていていいのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x9,
        "兵士シグ",
        (
            "……こんな状況じゃ、\x01",
            "いくら考えても迷いは晴れないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A95")

    label("loc_1A05")


    #N0039
    NpcTalk(
        0x9,
        "兵士シグ",
        (
            "俺たちは、これからも国防軍として\x01",
            "働いていていいのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #N0040
    NpcTalk(
        0x9,
        "兵士シグ",
        (
            "……こんな状況じゃ、\x01",
            "いくら考えても迷いは晴れないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A95")

    Jump("loc_2297")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B2E")

    #C0041
    ChrTalk(
        0xFE,
        (
            "この先、帝国が\x01",
            "何を仕掛けてきても、\x01",
            "俺たちは絶対に屈しないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "仲間たちの死は、\x01",
            "絶対に無駄にしない。\x01",
            "……して、なるものか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_1B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BD2")

    #C0043
    ChrTalk(
        0xFE,
        (
            "ふう……\x01",
            "昨夜の復旧作業の疲れが\x01",
            "まだ残っているみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "この緊張した状況下じゃ\x01",
            "何が起こるかわからないし、\x01",
            "今のうちに仮眠をとるとするか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCF")

    #C0045
    ChrTalk(
        0xFE,
        (
            "《幻獣》なるものの調査は、\x01",
            "我々警備隊で引き受けたい\x01",
            "ところだったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "独立提唱の関係で\x01",
            "緊張が続いている状態では\x01",
            "仕方ないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "……任せたぞ、ランディたち。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#00300Fおう、そっちもまあ\x01",
            "がんばってくれや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D5D")

    label("loc_1CCF")


    #C0049
    ChrTalk(
        0xFE,
        (
            "《幻獣》なるものの調査は、\x01",
            "我々警備隊で引き受けたい\x01",
            "ところだったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "独立提唱の関係で\x01",
            "緊張が続いている状態では\x01",
            "仕方ないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5D")

    Jump("loc_2297")

    label("loc_1D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1E")

    #C0051
    ChrTalk(
        0xFE,
        (
            "この間、ミレイユ准尉が\x01",
            "三尉へと昇進したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "三尉とは、他国の軍隊で言えば\x01",
            "少尉と同等の階級だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "今後の活躍をぜひとも\x01",
            "期待させてもらいたい所だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EA7")

    label("loc_1E1E")


    #C0054
    ChrTalk(
        0xFE,
        (
            "彼女の実力を考えれば、\x01",
            "この昇進は遅すぎるほどだが……\x01",
            "まあ、めでたいことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "今後の活躍をぜひとも\x01",
            "期待させてもらいたい所だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA7")

    Jump("loc_2297")

    label("loc_1EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F22")

    #C0056
    ChrTalk(
        0xFE,
        (
            "探知機には反応なし。\x01",
            "……危険物は載ってないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "念のため車体の下も\x01",
            "調べておくとするか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_1F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2037")

    #C0058
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令の指揮する\x01",
            "通商会議中の警備は、\x01",
            "実に理に適っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "適切な能力を持つ人員を\x01",
            "必要最低限に割り振ることで、\x01",
            "国境警備も上手くフォローしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "前の司令とはえらい違いだ。\x01",
            "やはり、人の上に立つべき人物とは\x01",
            "かくあるべきだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_20BD")

    label("loc_2037")


    #C0061
    ChrTalk(
        0xFE,
        (
            "俺もいずれは実績を積んで\x01",
            "司令職に就ければと思っているが……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令の目の黒いうちは\x01",
            "到底無理であろうことを実感したよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BD")

    Jump("loc_2297")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E9")

    #C0063
    ChrTalk(
        0xFE,
        (
            "前司令は、ハルトマンを通じて\x01",
            "ヨアヒムとつながりを持ち、\x01",
            "教団事件の際にも利用されていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "奴が懲戒免職され、\x01",
            "ソーニャ副司令が司令になったのは\x01",
            "全くもって当然の流れだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "これからは警備隊という組織が\x01",
            "より正しく運用されることだろう。\x01",
            "本当に喜ばしいことだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2297")

    label("loc_21E9")


    #C0066
    ChrTalk(
        0xFE,
        (
            "前司令の無能のせいで、\x01",
            "今まではミレイユ准尉ばかりに\x01",
            "負担が掛かっていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "これからは警備隊という組織が\x01",
            "より正しく運用されることだろう。\x01",
            "本当に喜ばしいことだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2297")

    TalkEnd(0xFE)
    Return()

    # Function_9_18FC end

    def Function_10_229B(): pass

    label("Function_10_229B")

    Call(0, 11)
    Return()

    # Function_10_229B end

    def Function_11_229F(): pass

    label("Function_11_229F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22C8")
    Call(0, 28)
    Return()

    label("loc_22C8")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2333")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2353")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FEE")

    label("loc_2353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2367")
    Jump("loc_2FEE")

    label("loc_2367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FEE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_241C")

    #C0068
    ChrTalk(
        0xA,
        (
            "ベルガード門の警備隊員御用達の\x01",
            "『満腹寄せ鍋』は美味しかったでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "よく鍋パーティなんかやるけど、\x01",
            "ほんと肉の争奪戦になるのよねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_241C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FF")

    #C0070
    ChrTalk(
        0xA,
        (
            "みんな不安になってるけど……\x01",
            "私はきっと大丈夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "だって、クレスさんが\x01",
            "絶対に守ってくれるって\x01",
            "言ってくれたんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "だったら私は、私にできる事をして\x01",
            "みんなに元気を分けてあげなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_259E")

    label("loc_24FF")


    #C0073
    ChrTalk(
        0xA,
        (
            "ワケの分からない巨大な木とか、\x01",
            "大統領の拘束の噂だとかで\x01",
            "みんな不安になっているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "私は、私にできる事をして\x01",
            "みんなに元気を分けてあげなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_259E")

    Jump("loc_2FEE")

    label("loc_25A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268B")

    #C0075
    ChrTalk(
        0xA,
        (
            "帝国との緊張状態……\x01",
            "どうしても不戦条約の\x01",
            "締結前を思い出しちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "あの帝国の《列車砲》が\x01",
            "こっちを向いた時は、\x01",
            "本当に怖かったんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "また、あんなことが\x01",
            "起こらなければいいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_270E")

    label("loc_268B")


    #C0078
    ChrTalk(
        0xA,
        (
            "不戦条約の締結前、\x01",
            "帝国は演習で《列車砲》を\x01",
            "持ち出したことがあったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "また、あんなことが\x01",
            "起こらなければいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270E")

    Jump("loc_2FEE")

    label("loc_2713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EC")

    #C0080
    ChrTalk(
        0xA,
        (
            "今日は生憎の雨ねえ。\x01",
            "外で警備してる隊員さんは大変そう。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "こういう日は、\x01",
            "身体が温まる料理がいいわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "昨日クレスさんに出した\x01",
            "激辛煮込みを応用して\x01",
            "鍋でもつくってあげようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_286F")

    label("loc_27EC")


    #C0083
    ChrTalk(
        0xA,
        (
            "こんな雨の日は、\x01",
            "身体が温まる料理がいいわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "昨日クレスさんに出した\x01",
            "激辛煮込みを応用して\x01",
            "鍋でもつくってあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286F")

    Jump("loc_2FEE")

    label("loc_2874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295B")

    #C0085
    ChrTalk(
        0xA,
        (
            "最近クレスさんの気が抜けてたから、\x01",
            "目が覚めるような\x01",
            "激辛の煮込みを作ってあげたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "最初は、ちょっと辛く\x01",
            "作りすぎたと思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        (
            "ちゃんと食べてくれてるし、\x01",
            "ふふ、大丈夫だったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29ED")

    label("loc_295B")


    #C0088
    ChrTalk(
        0xA,
        (
            "ふふ、あんなに喜んで\x01",
            "食べてくれると、\x01",
            "やっぱり嬉しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "折角付き合ってるんだし、\x01",
            "これからもちょくちょく\x01",
            "特別に料理してあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29ED")

    Jump("loc_2FEE")

    label("loc_29F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACB")

    #C0090
    ChrTalk(
        0xA,
        (
            "クレスさん、最近なんだか\x01",
            "気が抜けてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "よし、ここはいっちょ\x01",
            "気合が入るような料理でも\x01",
            "作ってあげようかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "まだまだお試しのカレシだけど、\x01",
            "これくらいはしたげないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B56")

    label("loc_2ACB")


    #C0093
    ChrTalk(
        0xA,
        (
            "いっちょクレスさんに\x01",
            "気合が入るような料理でも\x01",
            "作ってあげようかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "まだまだお試しのカレシだけど、\x01",
            "これくらいはしたげないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B56")

    Jump("loc_2FEE")

    label("loc_2B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BF2")

    #C0095
    ChrTalk(
        0xA,
        (
            "なんでも、テロリストが\x01",
            "クロスベルに侵入する\x01",
            "可能性があるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "門でも警戒が高まってるけど、\x01",
            "隊員のみんなは大丈夫かしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF4")

    #C0097
    ChrTalk(
        0xA,
        (
            "クレスさんとお試しで\x01",
            "お付き合いを初めて、結構経つのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "でも、付き合ってるからって\x01",
            "別段何をしてくるわけでもなし……\x01",
            "こんなもんなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "男の人にとっちゃ、\x01",
            "“付き合ってる”って事実自体が\x01",
            "大事なのかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D81")

    label("loc_2CF4")


    #C0100
    ChrTalk(
        0xA,
        (
            "あたしも、あんまり経験ないから\x01",
            "よくわかんないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "男の人にとっちゃ、\x01",
            "“付き合ってる”って事実自体が\x01",
            "大事なのかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D81")

    Jump("loc_2FEE")

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6C")
    TurnDirection(0xA, 0x104, 0)

    #C0102
    ChrTalk(
        0xA,
        (
            "あら、いらっしゃー……\x01",
            "ってランディくんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "リハビリ訓練って\x01",
            "もう終わったんじゃなかったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x104,
        (
            "#00302Fはは、まあそうなんだが……\x01",
            "キュートなお前を\x01",
            "一目見たくなっちまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "あはは、相変わらず\x01",
            "冗談ばっかり言ってるわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "それに、今のあたしを口説いたら\x01",
            "クレスさんが怒っちゃうかもよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00006F……ランディ、\x01",
            "席に座ってる隊員さんが\x01",
            "スゴい形相なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00306F……た、確かに面倒そうだな。\x01",
            "肝に銘じとくとするぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FEE")

    label("loc_2F6C")


    #C0109
    ChrTalk(
        0xA,
        (
            "ふふ、まあそれはともかく……\x01",
            "折角だから何か食べてってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "リハビリ訓練のときみたいに\x01",
            "がつがつ食べてくれるとうれしいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEE")

    Jump("loc_22D5")

    label("loc_2FF3")

    TalkEnd(0xA)
    Return()

    # Function_11_229F end

    def Function_12_2FF7(): pass

    label("Function_12_2FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3020")
    Call(0, 27)
    Return()

    label("loc_3020")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_318B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3109")

    #N0111
    NpcTalk(
        0xB,
        "兵士クレス",
        (
            "正直俺も、\x01",
            "どうしていいかわかんないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0xB,
        "兵士クレス",
        (
            "でも、大事なものは\x01",
            "この手で守っていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #N0113
    NpcTalk(
        0xB,
        "兵士クレス",
        (
            "よ、よーし……\x01",
            "ひとまず俺は、食う！\x01",
            "食いまくって力をつけるぞ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3186")

    label("loc_3109")


    #N0114
    NpcTalk(
        0xB,
        "兵士クレス",
        "腹が減ってちゃ戦はできぬ、だ。\x02",
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0xB,
        "兵士クレス",
        (
            "大事なものを守るためにも……\x01",
            "俺は食う！　食いまくってやる！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3186")

    Jump("loc_3C98")

    label("loc_318B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3292")

    #C0116
    ChrTalk(
        0xFE,
        (
            "この間のマインツでの戦闘で、\x01",
            "仲間が何人もやられちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "もし俺たちに強力な戦車でもあれば、\x01",
            "被害はもっと抑えられたかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "ステラちゃんや大事な人々を\x01",
            "これからも守っていくには、\x01",
            "やっぱり独立は必要かもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_334C")

    label("loc_3292")


    #C0119
    ChrTalk(
        0xFE,
        (
            "もし俺たちに強力な戦車でもあれば、\x01",
            "マインツでの被害は\x01",
            "もっと抑えられたかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ステラちゃんや大事な人々を\x01",
            "これからも守っていくには、\x01",
            "やっぱり独立は必要かもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334C")

    Jump("loc_3C98")

    label("loc_3351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_34AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3415")

    #C0121
    ChrTalk(
        0xFE,
        (
            "昨日ステラちゃんの\x01",
            "激辛煮込みを食べてから、\x01",
            "なんだか身体の調子がいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "フフフ……\x01",
            "これぞ愛のパゥワーってやつかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "……あの辛さはもうこりごりだけど。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_34A8")

    label("loc_3415")


    #C0124
    ChrTalk(
        0xFE,
        (
            "昨日ステラちゃんの\x01",
            "激辛煮込みを食べてから、\x01",
            "なんだか身体の調子がいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "彼女には感謝しなくちゃな。\x01",
            "……あの辛さはもうこりごりだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A8")

    Jump("loc_3C98")

    label("loc_34AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3585")

    #C0126
    ChrTalk(
        0xFE,
        (
            "ハフッハフッ……\x01",
            "ヒ～、か、辛い、辛すぎる……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "い、いや、せっかくマイスウィートが\x01",
            "俺のために作ってくれたんだ。\x01",
            "ぺろりと平らげるのが漢……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "うおおお～、ガツガツガツ……！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_35E9")

    label("loc_3585")


    #C0129
    ChrTalk(
        0xFE,
        (
            "ハフッハフッ……\x01",
            "や、やっぱり、辛い……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "だ、だが完食してみせる！\x01",
            "ガツガツガツ……！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E9")

    Jump("loc_3C98")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3694")

    #C0131
    ChrTalk(
        0xFE,
        (
            "はあ……最近の緊張状態で\x01",
            "どうも疲れちまっていけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "……いかんいかん、\x01",
            "ステラちゃんが見てるんだから\x01",
            "キリっとしてなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36E4")

    label("loc_3694")


    #C0133
    ChrTalk(
        0xFE,
        (
            "最近、疲れてるけど……\x01",
            "ステラちゃんが見てるんだ、\x01",
            "キリっとしてなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E4")

    Jump("loc_3C98")

    label("loc_36E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3785")

    #C0134
    ChrTalk(
        0xFE,
        (
            "今日はビシッと警備して、\x01",
            "ステラちゃんにいいトコ見せないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "テロリストだかなんだか知らねえが、\x01",
            "どこからでも来てみやがれってんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C98")

    label("loc_3785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_389F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3854")

    #C0136
    ChrTalk(
        0xFE,
        (
            "折角ステラちゃんと\x01",
            "お付き合いを始めたってのに、\x01",
            "ろくにデートすら誘えてないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "最近は通商会議の関係で\x01",
            "忙しいっていうのもあるけど、\x01",
            "そもそも俺って甲斐性がないのかも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_389A")

    label("loc_3854")


    #C0138
    ChrTalk(
        0xFE,
        (
            "ちくしょ～……\x01",
            "なんとかステラちゃんと\x01",
            "進展したいんだけどなあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389A")

    Jump("loc_3C98")

    label("loc_389F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397D")

    #C0139
    ChrTalk(
        0xB,
        (
            "ちぇ……少しくらい\x01",
            "話を聞いてくれても\x01",
            "いいじゃないかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "ステラちゃんのことなら、\x01",
            "俺は何時間でも語れるのにさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        "#00309Fそれじゃな、先輩。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        "聞けっての！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_39BD")

    label("loc_397D")


    #C0143
    ChrTalk(
        0xB,
        (
            "ちっ……\x01",
            "ステラちゃんのことなら、\x01",
            "何時間でも語れるのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BD")

    Jump("loc_3C98")

    label("loc_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A47")

    #C0144
    ChrTalk(
        0xFE,
        (
            "ランディィィィ……\x01",
            "貴様、俺のマイ・スウィーツに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        (
            "#00309Fま、まーまー落ち着いて。\x01",
            "なんもしてねッスから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C98")

    label("loc_3A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFE")

    #C0146
    ChrTalk(
        0xFE,
        (
            "フフ、ステラちゃん……\x01",
            "俺のマイ・スウィート……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00006F（ま、まい・すうぃーと……）\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#00300Fああ、そういや先輩……\x01",
            "この間からステラと『お試し』で\x01",
            "付き合ってるとか言ってたッスね。\x02\x03",

            "#00309Fハハ、ちょっとは進展したッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "……ま、まあな。\x01",
            "そりゃもう、ラブラブだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "毎日ここでメシを食って、\x01",
            "ステラちゃんを眺めて……\x01",
            "幸せな毎日さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#00306F（……つまり、いまだに\x01",
            "  何にも進展してねぇんだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C98")

    label("loc_3BFE")


    #C0152
    ChrTalk(
        0xFE,
        (
            "ス、ステラちゃんと俺は\x01",
            "これからなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "ランディ、ステラちゃんを\x01",
            "横から口説いたりするなよ。\x01",
            "……お願いだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#00306F（ダメだこりゃ。）\x02",
    )

    CloseMessageWindow()

    label("loc_3C98")

    TalkEnd(0xFE)
    Return()

    # Function_12_2FF7 end

    def Function_13_3C9C(): pass

    label("Function_13_3C9C")

    Call(0, 14)
    Return()

    # Function_13_3C9C end

    def Function_14_3CA0(): pass

    label("Function_14_3CA0")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B28")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "休憩をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D09")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3D09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D29")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B23")

    label("loc_3D29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D3D")
    Jump("loc_4B23")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B23")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1A")

    #C0155
    ChrTalk(
        0xC,
        (
            "こういうときは\x01",
            "精神の負荷が特に厄介だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xC,
        (
            "休憩するならゆっくりと休んで、\x01",
            "心を落ち着けるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "……とはいえ、僕も不安だ。\x01",
            "平和な時は戻ってくるんだろうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E98")

    label("loc_3E1A")


    #C0158
    ChrTalk(
        0xC,
        (
            "休憩するならゆっくりと休んで、\x01",
            "心を落ち着けるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "……とはいえ、僕も不安だよ。\x01",
            "平和な時は戻ってくるんだろうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E98")

    Jump("loc_4B23")

    label("loc_3E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4070")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FBB")

    #C0160
    ChrTalk(
        0xC,
        (
            "クロスベルで好き放題やって\x01",
            "どこかへ去っていった《赤い星座》は、\x01",
            "飛行艇を持っていたそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xC,
        (
            "しかも、警備隊の対空レーダーにも\x01",
            "引っかからなかったそうだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        (
            "……正直、資金力さえあれば\x01",
            "手に入るという技術でもないはずだ。\x01",
            "一体彼らは何者なんだ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_406B")

    label("loc_3FBB")


    #C0163
    ChrTalk(
        0xC,
        (
            "《赤い星座》の飛行艇は、\x01",
            "警備隊の対空レーダーにも\x01",
            "引っかからなかったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xC,
        (
            "……正直、資金力さえあれば\x01",
            "手に入るという技術でもないはずだ。\x01",
            "一体彼らは何者なんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_406B")

    Jump("loc_4B23")

    label("loc_4070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A3")

    #C0165
    ChrTalk(
        0xC,
        (
            "昨日の事故の話を聞いたんだが、\x01",
            "巨大な化物が力任せに殴ったせいで\x01",
            "列車事故が起こったそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "あの列車は兵器開発で有名な\x01",
            "帝国ラインフォルト社製だ。\x01",
            "装甲車くらいの強度はあるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "僕は姿を直接見てはいないけど、\x01",
            "どれだけ恐ろしい化物かは\x01",
            "なんとなく分かってしまうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4261")

    label("loc_41A3")


    #C0168
    ChrTalk(
        0xC,
        (
            "あの列車は兵器開発で有名な\x01",
            "帝国ラインフォルト社製なのに、\x01",
            "殴って列車事故を起こさせるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        (
            "僕は姿を直接見てはいないけど、\x01",
            "どれだけ恐ろしい化物かは\x01",
            "なんとなく分かってしまうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4261")

    Jump("loc_4B23")

    label("loc_4266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DD")

    #C0170
    ChrTalk(
        0xC,
        (
            "各国の軍が機甲化されていく中で\x01",
            "近年、重要視されているのが航空戦術だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "例えば１２数年前の《百日戦役》では、\x01",
            "帝国が圧倒的な軍事力で\x01",
            "リベールを侵攻していたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "戦争の終盤で、リベールが\x01",
            "新しく開発した飛行艇によって、\x01",
            "戦局が一気に覆されてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xC,
        (
            "警備隊が飛行艇の所持を許されないのは、\x01",
            "そのあたりの事情があるんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_447E")

    label("loc_43DD")


    #C0174
    ChrTalk(
        0xC,
        (
            "近年、各国の軍が機甲化されていく中で\x01",
            "重要視されてきたのが航空戦術だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "独立にあたって警備隊が\x01",
            "軍隊になったら、ぜひともまずは\x01",
            "飛行艇を配備してほしいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447E")

    Jump("loc_4B23")

    label("loc_4483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_463C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4587")

    #C0176
    ChrTalk(
        0xC,
        (
            "クロスベルが独立したら、\x01",
            "警備隊も正式に軍として\x01",
            "運用されることになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "隊員たちの武装も今までより\x01",
            "強力なものに変わるだろう。\x01",
            "戦車なんかも配備されたりしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "う～ん、ミリタリーオタクとしては\x01",
            "興味をそそられるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4637")

    label("loc_4587")


    #C0179
    ChrTalk(
        0xC,
        (
            "クロスベルが独立して\x01",
            "警備隊が正式に軍になったら、\x01",
            "装備も今より充実するだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "戦車なんかも配備されたりして……\x01",
            "う～ん、ミリタリーオタクとしては\x01",
            "興味をそそられるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4637")

    Jump("loc_4B23")

    label("loc_463C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_479E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4723")

    #C0181
    ChrTalk(
        0xC,
        (
            "今日はいよいよ、\x01",
            "オルキスタワーでの本会議だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "帝国や共和国への配慮があるから、\x01",
            "警備隊は表立った警備は\x01",
            "できないとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "大事な国際会議だ、縁の下からでも\x01",
            "何とか守りぬいてほしいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4799")

    label("loc_4723")


    #C0184
    ChrTalk(
        0xC,
        (
            "今日はいよいよ、\x01",
            "オルキスタワーでの本会議だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "大事な国際会議だ、縁の下からでも\x01",
            "何とか守りぬいてほしいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4799")

    Jump("loc_4B23")

    label("loc_479E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_496D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D3")

    #C0186
    ChrTalk(
        0xC,
        (
            "新型装甲車が、正式に配備されて\x01",
            "しばらく経つけど……\x01",
            "いやはや、やはり素敵だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "強力なミサイルポッドもあるし、\x01",
            "装甲もかなり強化されている。\x01",
            "間違いなく警備隊で最高の武装だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "他国の飛行艇や戦車に比べたら\x01",
            "そりゃあ見劣りはするけど、\x01",
            "機能美みたいなものはあると思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4968")

    label("loc_48D3")


    #C0189
    ChrTalk(
        0xC,
        (
            "新型装甲車は、間違いなく\x01",
            "警備隊で最高の武装だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        (
            "他国の飛行艇や戦車に比べたら\x01",
            "そりゃあ見劣りはするけど、\x01",
            "機能美みたいなものはあると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4968")

    Jump("loc_4B23")

    label("loc_496D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A73")

    #C0191
    ChrTalk(
        0xC,
        (
            "僕は、ミリタリーオタク……\x01",
            "略してミリオタってやつでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        (
            "軍事関係のことが大好きで、\x01",
            "この門で働いているのも\x01",
            "趣味が高じてって感じなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xC,
        (
            "まあ、クロスベル警備隊は\x01",
            "厳密に言えば軍ではないけど……\x01",
            "僕にとっては充分魅力的だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B23")

    label("loc_4A73")


    #C0194
    ChrTalk(
        0xC,
        (
            "僕は、ミリオタってやつでね。\x01",
            "この門で働いているのも\x01",
            "趣味が高じてって感じなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "まあ、クロスベル警備隊は\x01",
            "厳密に言えば軍ではないけど……\x01",
            "僕にとっては充分魅力的だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B23")

    Jump("loc_3CAD")

    label("loc_4B28")

    TalkEnd(0xC)
    Return()

    # Function_14_3CA0 end

    def Function_15_4B2C(): pass

    label("Function_15_4B2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B3D")
    Jump("loc_4DDB")

    label("loc_4B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BED")

    #C0196
    ChrTalk(
        0xFE,
        (
            "昨日の列車事故に\x01",
            "巻き込まれてしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "一応、軽傷で済んだので\x01",
            "娘に迎えにきてもらったのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "おー、いつつつ……\x01",
            "まだ少し痛むわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4C49")

    label("loc_4BED")


    #C0199
    ChrTalk(
        0xFE,
        (
            "おー、いつつつ……\x01",
            "まだ少し痛むわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "もう少し入院させてもらえば\x01",
            "よかったかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C49")

    Jump("loc_4DDB")

    label("loc_4C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CDF")

    #C0201
    ChrTalk(
        0xFE,
        (
            "クロスベルが独立しようなど……\x01",
            "身の程を知るがいいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "帝国人にしてみれば、\x01",
            "飼い犬に手を噛まれるような\x01",
            "思いなのだからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDB")

    label("loc_4CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CED")
    Jump("loc_4DDB")

    label("loc_4CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D56")

    #C0203
    ChrTalk(
        0xFE,
        "さっさと検分が終わらぬかのう。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "テロ対策だかなんだかしらんが\x01",
            "面倒なもんじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDB")

    label("loc_4D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D64")
    Jump("loc_4DDB")

    label("loc_4D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DDB")

    #C0205
    ChrTalk(
        0xFE,
        (
            "通商会議では、宰相閣下が\x01",
            "きっと帝国に有益な取り決めを\x01",
            "通してくれるに違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "フフ、結構な事だな。\x02",
    )

    CloseMessageWindow()

    label("loc_4DDB")

    TalkEnd(0xFE)
    Return()

    # Function_15_4B2C end

    def Function_16_4DDF(): pass

    label("Function_16_4DDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E7A")

    #C0207
    ChrTalk(
        0xFE,
        (
            "あの襲撃事件以来、迷っていたけど……\x01",
            "故郷の帝国に帰ることにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "あんなのに、また巻き込まれたら\x01",
            "たまったもんじゃないからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5070")

    label("loc_4E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E88")
    Jump("loc_5070")

    label("loc_4E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E96")
    Jump("loc_5070")

    label("loc_4E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F0E")

    #C0209
    ChrTalk(
        0xFE,
        (
            "国家独立だなんて、\x01",
            "幻想も大概にするんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "クロスベルは帝国のために\x01",
            "搾取されていればいいんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5070")

    label("loc_4F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F1C")
    Jump("loc_5070")

    label("loc_4F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4FBD")

    #C0211
    ChrTalk(
        0xFE,
        (
            "やれやれ、急いで見に来る\x01",
            "ほどのものでもないだろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "まあ、オルキスタワーは\x01",
            "帝国でも話題になってたから、\x01",
            "俺も見てみたかったんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5070")

    label("loc_4FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5070")

    #C0213
    ChrTalk(
        0xFE,
        (
            "通商会議には、皇帝名代として\x01",
            "話題のオリヴァルト皇子が\x01",
            "クロスベル入りするって話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "まあ、皇帝陛下としては\x01",
            "《鉄血宰相》のお手伝いって程度の\x01",
            "任命なんだろうがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5070")

    TalkEnd(0xFE)
    Return()

    # Function_16_4DDF end

    def Function_17_5074(): pass

    label("Function_17_5074")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516D")

    #C0215
    ChrTalk(
        0xF,
        (
            "帝国では内戦が起こっていますが、\x01",
            "それでも祖国に帰りたいと思って\x01",
            "きたところなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xF,
        (
            "でも、橋があんな風に\x01",
            "完全に落ちてしまっているなんて\x01",
            "思いもよりませんでした……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xF,
        (
            "……これからどうすれば\x01",
            "いいんでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_51F6")

    label("loc_516D")


    #C0218
    ChrTalk(
        0xF,
        (
            "お父様が『バルコニーから\x01",
            "落ちた橋を上から見てくる』と\x01",
            "階段を上っていきましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xF,
        (
            "……やっぱり帝国には\x01",
            "戻れないんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F6")

    Jump("loc_5335")

    label("loc_51FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5209")
    Jump("loc_5335")

    label("loc_5209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5217")
    Jump("loc_5335")

    label("loc_5217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_529B")

    #C0220
    ChrTalk(
        0xFE,
        (
            "なんだか、警備隊の人たちが\x01",
            "みんなピリピリしてるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "こんなとこ長居したくないし、\x01",
            "さっさと帰ろっかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5335")

    label("loc_529B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52A9")
    Jump("loc_5335")

    label("loc_52A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_52B7")
    Jump("loc_5335")

    label("loc_52B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_532C")

    #C0222
    ChrTalk(
        0xFE,
        (
            "噂の超高層ビル、\x01",
            "オルキスタワーとやらを\x01",
            "見に来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "一体どんなビルなのかしら。\x01",
            "楽しみねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5335")

    label("loc_532C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5335")

    label("loc_5335")

    TalkEnd(0xFE)
    Return()

    # Function_17_5074 end

    def Function_18_5339(): pass

    label("Function_18_5339")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_53B0")

    #C0224
    ChrTalk(
        0xFE,
        (
            "もうちょっとクロスベルで\x01",
            "遊んでたかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "最近、なんだかコワイもん。\x01",
            "仕方ないよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5428")

    label("loc_53B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53BE")
    Jump("loc_5428")

    label("loc_53BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_53CC")
    Jump("loc_5428")

    label("loc_53CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_53DA")
    Jump("loc_5428")

    label("loc_53DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5411")

    #C0226
    ChrTalk(
        0xFE,
        (
            "あ～あ、\x01",
            "早く街に行きたいですのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5428")

    label("loc_5411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_541F")
    Jump("loc_5428")

    label("loc_541F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5428")

    label("loc_5428")

    TalkEnd(0xFE)
    Return()

    # Function_18_5339 end

    def Function_19_542C(): pass

    label("Function_19_542C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_543D")
    Jump("loc_557A")

    label("loc_543D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54CF")

    #C0227
    ChrTalk(
        0xFE,
        (
            "ああ、雨が降ってしまうなんて……\x01",
            "やっぱり鉄道を使えばよかったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "事故の直後だから、\x01",
            "あんまり使いたくなかったのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_54CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54DD")
    Jump("loc_557A")

    label("loc_54DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54EB")
    Jump("loc_557A")

    label("loc_54EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54F9")
    Jump("loc_557A")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5571")

    #C0229
    ChrTalk(
        0xFE,
        (
            "今朝は交通規制で\x01",
            "鉄道が利用できなかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "まあ、あの専用列車が\x01",
            "通るんだから仕方ないけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_5571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_557A")

    label("loc_557A")

    TalkEnd(0xFE)
    Return()

    # Function_19_542C end

    def Function_20_557E(): pass

    label("Function_20_557E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_568E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_562C")

    #C0231
    ChrTalk(
        0xFE,
        (
            "今、物資の輸送がてら\x01",
            "戻ってきたところだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "クロスベル駅でも\x01",
            "やはり混乱が続いているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "この情勢じゃ仕方のないことだがな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5689")

    label("loc_562C")


    #C0234
    ChrTalk(
        0xFE,
        (
            "クロスベル駅でも\x01",
            "やはり混乱が続いているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        "この情勢じゃ仕方のないことだがな。\x02",
    )

    CloseMessageWindow()

    label("loc_5689")

    Jump("loc_5767")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5767")

    #C0236
    ChrTalk(
        0x13,
        (
            "門の地下には、鉄道の\x01",
            "貨物用路線が通っててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x13,
        (
            "今、貨物列車の検分が終わって、\x01",
            "クロスベル駅から帰ってきた所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x13,
        (
            "……地下に降りるつもりか？\x01",
            "大したモンは無いと思うが\x01",
            "列車には気をつけてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5767")

    TalkEnd(0xFE)
    Return()

    # Function_20_557E end

    def Function_21_576B(): pass

    label("Function_21_576B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58CE")

    #C0239
    ChrTalk(
        0x104,
        (
            "#00301Fミレイユ……\x01",
            "かなり忙しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x14,
        (
            "#07901Fええ、帝国のガレリア要塞に\x01",
            "何か動きがあるらしくてね。\x02\x03",

            "#07903F正直、かつてない緊張状態よ。\x01",
            "……２年前の不戦条約締結前に\x01",
            "匹敵するくらいのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#00005Fそこまで……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#00303F……気をつけろよ、ミレイユ。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x14,
        (
            "#07902F……ええ、分かってる。\x01",
            "ここは任せてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_595F")

    label("loc_58CE")


    #C0244
    ChrTalk(
        0x14,
        (
            "#07903F帝国のガレリア要塞で\x01",
            "何か動きがあるらしいわ。\x02\x03",

            "#07901F正直、かつてない緊張状態よ。\x01",
            "……２年前の不戦条約締結前に\x01",
            "匹敵するくらいのね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_595F")

    Jump("loc_5997")

    label("loc_5964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5972")
    Jump("loc_5997")

    label("loc_5972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5980")
    Jump("loc_5997")

    label("loc_5980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_598E")
    Jump("loc_5997")

    label("loc_598E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5997")

    label("loc_5997")

    TalkEnd(0xFE)
    Return()

    # Function_21_576B end

    def Function_22_599B(): pass

    label("Function_22_599B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A27")

    #C0245
    ChrTalk(
        0xFE,
        (
            "事件からの一週間で、\x01",
            "こんな情勢が悪くなるなんて\x01",
            "思いもしなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "早く娘といっしょに\x01",
            "クロスベルを離れないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5A7A")

    #C0247
    ChrTalk(
        0xFE,
        "お父さん、大丈夫？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "食堂でちょっと\x01",
            "休憩していきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A88")
    Jump("loc_5B37")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B12")

    #C0249
    ChrTalk(
        0xFE,
        (
            "なんでも、最近得体の知れない\x01",
            "魔獣が増えているそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "なんだか物騒だし……\x01",
            "さっさと帝国に帰るとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B20")
    Jump("loc_5B37")

    label("loc_5B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B2E")
    Jump("loc_5B37")

    label("loc_5B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B37")

    label("loc_5B37")

    TalkEnd(0xFE)
    Return()

    # Function_22_599B end

    def Function_23_5B3B(): pass

    label("Function_23_5B3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5D1B")

    #C0251
    ChrTalk(
        0x15,
        (
            "#03600F昨日のアルモリカ村の事件……\x01",
            "本当に解決してよかったです。\x02\x03",

            "#03603F皆さんがいなかったら\x01",
            "どうなっていたことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00001F悪徳商人ミンネス……\x01",
            "手強い男でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#00200F一応、指名手配されましたし\x01",
            "捕まるのは時間の問題かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、どうかな？\x01",
            "ずいぶんしつこそうな顔を\x01",
            "してたしねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#00303F確かに、フン捕まえるまでは\x01",
            "安心できなそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x15,
        (
            "#03608Fそうですね……\x01",
            "それまでに、また別の被害が\x01",
            "出なければいいのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6014")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_5F05")

    #C0257
    ChrTalk(
        0x15,
        (
            "#03605Fおや、みなさん……\x02\x03",

            "#03600Fそうそう、例のアルモリカ村での\x01",
            "ミンネスの事件ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#00003F……途中で捜査から\x01",
            "抜けてしまってすみませんでした。\x02\x03",

            "#00008F他に優先度の高い仕事が\x01",
            "入ってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x15,
        (
            "#03600Fいえいえ、とんでもない。\x01",
            "イアン先生の協力もあって\x01",
            "なんとか解決に至りましたし……\x02\x03",

            "#03604Fそれまでの皆さんの捜査も\x01",
            "充分役に立ちましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#00000Fそ、そうですか……\x01",
            "それはその、よかったです。\x02\x03",

            "#00003F（やっぱり、最後まで\x01",
            "  やっておけばよかったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6014")

    label("loc_5F05")


    #C0261
    ChrTalk(
        0x15,
        (
            "#03600F村長たちの名誉があるので\x01",
            "詳しくは言えませんが……\x02\x03",

            "#03603F昨日、アルモリカ村で\x01",
            "大変な事件があったのです。\x02\x03",

            "#03600Fイアン先生がいなければ、\x01",
            "あの事件は解決に\x01",
            "至らなかったでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00005F（大変な事件だったみたいだな……\x01",
            "  何か手伝えればよかったけど。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6014")

    SetScenarioFlags(0x17C, 1)
    Jump("loc_6191")

    label("loc_601C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6103")

    #C0263
    ChrTalk(
        0x15,
        (
            "#03600F今日は西クロスベル街道を\x01",
            "運転してきたのですが……\x02\x03",

            "#03603F脱線事故の翌日だと考えると\x01",
            "少し心配になってしまいます。\x02\x03",

            "#03600F巨大な化物が出たという\x01",
            "噂も流れていますし、\x01",
            "注意した方がいいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6191")

    label("loc_6103")


    #C0264
    ChrTalk(
        0x15,
        (
            "#03600F今日は西クロスベル街道を\x01",
            "運転してきたのですが……\x02\x03",

            "巨大な化物が出たという\x01",
            "噂も流れていますし、\x01",
            "注意した方がいいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6191")

    TalkEnd(0xFE)
    Return()

    # Function_23_5B3B end

    def Function_24_6195(): pass

    label("Function_24_6195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61AA")
    Call(0, 25)
    Jump("loc_623F")

    label("loc_61AA")


    #C0265
    ChrTalk(
        0xFE,
        (
            "この国境の緊張状態……\x01",
            "何事も起こらなければいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "とにかく、民間人の安全のために\x01",
            "俺たちギルドの方でも\x01",
            "状況は確認していかなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_623F")

    TalkEnd(0xFE)
    Return()

    # Function_24_6195 end

    def Function_25_6243(): pass

    label("Function_25_6243")

    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    #C0267
    ChrTalk(
        0x16,
        (
            "……なるほど、確かに国境は\x01",
            "抜き差しならない状態のようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x16,
        (
            "こういう時、帝国のギルドとも\x01",
            "連携をとっていければいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x17,
        (
            "……帝国のギルドは、\x01",
            "軍部の圧力で衰退している。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x17,
        (
            "骨のある奴は何人かいるが……\x01",
            "組織自体がそういう状況である今、\x01",
            "あまり当てにはできないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x16,
        "そうか……それは仕方ないな。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_25_6243 end

    def Function_26_63A3(): pass

    label("Function_26_63A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C1")
    Call(0, 25)
    Jump("loc_6473")

    label("loc_63C1")


    #C0272
    ChrTalk(
        0xFE,
        (
            "帝国のギルドと協力できれば、\x01",
            "中立の立場からこの緊張状態を\x01",
            "緩和できたかもしれないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "……帝国のギルドは、\x01",
            "軍部の圧力で衰退している。\x01",
            "あまり当てにはできないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6473")

    Jump("loc_65CF")

    label("loc_6478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6551")

    #C0274
    ChrTalk(
        0xFE,
        (
            "今日は、スコットとは別行動でな。\x01",
            "この付近の手配魔獣を退治していた。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "通商会議が始まれば、我々遊撃士も\x01",
            "相当な忙しさになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "その前に、一つでも多くの依頼を\x01",
            "こなしておかなければな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_65CF")

    label("loc_6551")


    #C0277
    ChrTalk(
        0xFE,
        (
            "通商会議が始まれば、我々遊撃士も\x01",
            "相当な忙しさになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "その前に、一つでも多くの依頼を\x01",
            "こなしておかなければな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CF")

    TalkEnd(0xFE)
    Return()

    # Function_26_63A3 end

    def Function_27_65D3(): pass

    label("Function_27_65D3")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0xB, -97000, 150, -3950, 90)
    SetChrSubChip(0xB, 0x2)
    OP_68(-95990, 750, -3740, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26060, 0)
    SetChrPos(0x101, -95150, 0, -3250, 270)
    SetChrPos(0x104, -95210, 0, -4670, 270)
    SetChrPos(0x102, -93870, 0, -4040, 270)
    SetChrPos(0x109, -93620, 0, -2840, 270)
    SetChrPos(0x105, -93480, 0, -5210, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0279
    ChrTalk(
        0x104,
        "#12P#00309Fいよっ、クレス先輩。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        "#5Pハッ……ランディ！？\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xB,
        (
            "#5Pリハビリ訓練は\x01",
            "終わったってのに、\x01",
            "何しにきたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        "#12P#00000Fえっと、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0283
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは教授の依頼で\x01",
            "問診表を回収している事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xB, 0x0)

    #C0284
    ChrTalk(
        0xB,
        (
            "#5P問診表……あっ！\x01",
            "すっかり忘れてたぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0285
    ChrTalk(
        0xB,
        (
            "#5Pちょっと待ってくれ、\x01",
            "たしかここに……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    #C0286
    ChrTalk(
        0xB,
        "#5Pほい、これだろ？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0287
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0288
    ChrTalk(
        0x101,
        "#12P#00000Fはい、確かに。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "#5Pいや～、悪いね。\x01",
            "わざわざ取りに来て\x01",
            "もらっちゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "#5P最近幸せすぎて、\x01",
            "すっかり忘れちゃっててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        "#12P#00105F幸せって……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "#5Pそう、つまり俺と\x01",
            "ステラちゃんのラブラブな──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0293
    ChrTalk(
        0x104,
        (
            "#6P#00304Fよしロイド、\x01",
            "そろそろ行くとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        "#12P#10300Fま、目的も済んだことだしね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0295
    ChrTalk(
        0x101,
        (
            "#11P#00012F……だ、だな。\x01",
            "（長くなりそうだし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xB,
        (
            "#5Pお、おいコラ！？\x01",
            "聞いてくれないのかよ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        "#12P#10100Fあはは……すみません。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 6)
    OP_29(0x70, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ACC")

    #A0298
    AnonymousTalk(
        0x101,
        (
            "#00003Fこれで全ての問診表を\x01",
            "回収し終わったな。\x02\x03",

            "#00000Fさっそくセイランド教授に\x01",
            "届けにいくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_6ACC")

    SetChrPos(0xB, -97470, 150, -3950, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -94400, 0, -3950, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_65D3 end

    def Function_28_6AFF(): pass

    label("Function_28_6AFF")

    EventBegin(0x0)
    Fade(500)
    OP_68(-105030, 750, 2240, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26060, 0)
    SetChrPos(0x101, -103240, 0, 2040, 270)
    SetChrPos(0x104, -103250, 0, 3150, 270)
    SetChrPos(0x102, -103260, 0, 880, 270)
    SetChrPos(0x109, -103100, 0, -280, 315)
    SetChrPos(0x103, -102080, 0, 700, 270)
    SetChrPos(0x105, -101780, 0, -540, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0299
    ChrTalk(
        0xA,
        (
            "あら、ランディ君に……\x01",
            "支援課の皆さんだったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        "#00309Fよっ、ステラ。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、今日は仕事で\x01",
            "来たんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0302
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

    #C0303
    ChrTalk(
        0xA,
        (
            "あっ、そういえば……\x01",
            "そんな話も来てたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xA,
        (
            "そうね、それじゃあ\x01",
            "ベルガード門の警備隊員御用達の\x01",
            "『満腹寄せ鍋』でも作ろっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#10105Fへえ、こっちの部隊では\x01",
            "そういうものがあったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x103,
        "#00200Fそれでは、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xA,
        (
            "ええ、人数分よそうから\x01",
            "ちょっと待っててね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0308
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは満腹寄せ鍋を食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0309
    ChrTalk(
        0x102,
        (
            "#00100Fもぐもぐ……\x01",
            "ううん、体がポカポカしてきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#00009Fああ、肉のボリュームもすごいし、\x01",
            "山菜も沢山入ってて栄養満点だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10104Fまあ、警備隊も演習がハードですし、\x01",
            "こういうので力をつけないと\x01",
            "持ちませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        "#10300Fフフ、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xA,
        (
            "よく鍋パーティなんかやるけど、\x01",
            "ほんと肉の争奪戦になるのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xA,
        (
            "ランディ君がいた頃なんかは、\x01",
            "他人がとった取り皿から奪ったりとか\x01",
            "めちゃくちゃやってたんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x103, 0x104, 500)

    #C0315
    ChrTalk(
        0x103,
        (
            "#00211F……何をやってるんですか、\x01",
            "ランディさん。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0316
    ChrTalk(
        0x104,
        "#00309Fハハ、弱肉強食ってやつだっての。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x173, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_70B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_70D4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_70E7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_70FA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_7117")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_712A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_712A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_7147")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_715A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_715A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_7177")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_718A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_718A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_71A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71A7")

    OP_29(0x80, 0x1, 0xB)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72AA")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0317
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72A1")

    #A0318
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

    label("loc_72A1")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_72AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_737B")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0319
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

    #A0320
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

    label("loc_737B")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -103610, 0, 2100, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_6AFF end

    def Function_29_73AB(): pass

    label("Function_29_73AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x5, 0x4)
    OP_68(20630, 1000, -340, 0)
    MoveCamera(315, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20760, 0)
    SetChrPos(0x101, 28060, 0, 0, 270)
    SetChrPos(0x102, 28260, 0, -1200, 270)
    SetChrPos(0x104, 28260, 0, 1200, 270)
    SetChrPos(0x109, 29460, 0, 0, 270)
    SetChrPos(0x103, 29260, 0, -1200, 270)
    SetChrPos(0x105, 29260, 0, 1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x14, 5870, 0, 0, 90)
    OP_4B(0x14, 0xFF)
    SetChrFlags(0x14, 0x8000)

    def lambda_7489():
        OP_95(0x101, 21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7489)
    Sleep(30)

    def lambda_74A6():
        OP_95(0x102, 21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74A6)
    Sleep(40)

    def lambda_74C3():
        OP_95(0x104, 21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_74C3)
    Sleep(800)

    def lambda_74E0():
        OP_95(0x109, 23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74E0)
    Sleep(30)

    def lambda_74FD():
        OP_95(0x103, 23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_74FD)
    Sleep(10)

    def lambda_751A():
        OP_95(0x105, 23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_751A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0321
    ChrTalk(
        0x101,
        (
            "#00001Fさて、件の黒い運搬車は\x01",
            "おそらくここにいるはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_765D")

    #C0322
    ChrTalk(
        0x103,
        (
            "#00203F……フランツさんによれば、\x01",
            "運搬車は共和国方面に\x01",
            "向かったという話では……？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#00011Fあ……そういえばそうだったな。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#00106Fついベルガード門の方に\x01",
            "来てしまったわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F5")

    label("loc_765D")


    #C0325
    ChrTalk(
        0x103,
        (
            "#00205F……それらしい車は\x01",
            "見当たりませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        (
            "#00100Fうーん、\x01",
            "隊員のだれかに聞いてみたら\x01",
            "いいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        "#00003Fそれもそうだな……\x02",
    )

    CloseMessageWindow()

    label("loc_76F5")


    def lambda_76FA():
        OP_95(0xFE, 17460, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_76FA)
    Sleep(2000)
    OP_68(20630, 1000, -340, 3000)
    MoveCamera(306, 19, 0, 3000)
    OP_6E(470, 3000)
    SetCameraDistance(20760, 3000)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)

    #C0328
    ChrTalk(
        0x14,
        "#07900Fあら……あなたたち。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        "#00300Fいよっ、ミレイユ。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        "#10100Fお疲れ様です、ミレイユ三尉！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x14,
        (
            "#07902Fお疲れ様です。\x02\x03",

            "#07906F……ふう。\x01",
            "今日は何の用で来たの？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        "#10300Fなんだかお疲れみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x14,
        (
            "#07901Fええ……帝国方面への\x01",
            "緊張状態が続いているから。\x02\x03",

            "#07903Fこんな時に、タングラム門の方では\x01",
            "一騒ぎあったっていうし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0334
    ChrTalk(
        0x101,
        "#00005Fタングラム門で何かあったんですか？\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x14,
        (
            "#07901F何でも帝国製の黒い運搬車が、\x01",
            "書類不備のまま強引に\x01",
            "ゲートを通っていったみたい。\x02\x03",

            "#07903F一応、最低限のチェックは\x01",
            "済ませてるから問題には\x01",
            "ならないと思うんだけど……\x02\x03",

            "#07901F警備隊の面目が丸潰れだわ、\x01",
            "まったく……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x103)
    OP_64(0x105)
    OP_64(0x109)
    Sleep(500)
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0336
    ChrTalk(
        0x14,
        "#07900F……どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        "#00006Fい、いえ……\x02",
    )

    CloseMessageWindow()

    def lambda_7AF9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AF9)
    Sleep(10)

    def lambda_7B09():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B09)
    Sleep(50)

    def lambda_7B19():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B19)
    Sleep(10)

    def lambda_7B29():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B29)
    Sleep(30)

    def lambda_7B39():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7B39)
    Sleep(10)

    def lambda_7B49():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7B49)
    WaitChrThread(0x105, 2)

    #C0338
    ChrTalk(
        0x102,
        "#00101Fねえ、今の話って……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#00006F……ああ、どうやら俺たちは\x01",
            "見当違いのほうを\x01",
            "探してしまったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        (
            "#00306Fすでに共和国に逃げられたんじゃ\x01",
            "もう手の出しようはなさそうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_7CBC")

    #C0341
    ChrTalk(
        0x101,
        (
            "#00001Fビリーさんやウルスラ病院には\x01",
            "申し訳ないけど……\x01",
            "そう報告するしかなさそうだな。\x02\x03",

            "#00006Fはあ……フランツの話を\x01",
            "ちゃんと聞いておけばよかったか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D17")

    label("loc_7CBC")


    #C0342
    ChrTalk(
        0x101,
        (
            "#00006Fビリーさんやウルスラ病院には\x01",
            "申し訳ないけど……\x01",
            "そう報告するしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D17")


    #C0343
    ChrTalk(
        0x14,
        "#07900F？？？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは事の顛末を\x01",
            "クロスベル空港で待つ\x01",
            "ビリーとリカルドに伝え……\x02",
        )
    )

    CloseMessageWindow()

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ビリーと共に\x01",
            "ウルスラ病院へ事情を\x01",
            "伝えに行くのだった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x93, 0x1, 0x2)
    SetScenarioFlags(0x22, 2)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_73AB end

    def Function_30_7DE7(): pass

    label("Function_30_7DE7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41800.itc", 0x20)
    LoadChrToIndex("chr/ch41402.itc", 0x21)
    LoadChrToIndex("chr/ch41502.itc", 0x22)
    LoadChrToIndex("chr/ch12200.itc", 0x23)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -105500, 0, 2100, 45)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -101900, 50, 2200, 90)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -99600, 50, 2200, 270)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x2)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -99600, 50, 4000, 270)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -100200, 0, 400, 0)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -99200, 0, 700, 0)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -98100, 0, 2600, 315)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -103500, 0, -700, 45)
    OP_68(-101000, 2300, 3300, 0)
    MoveCamera(293, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-101000, 1300, 3300, 10000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(180, 120, -1, -1)
    SetChrName("マクダエル議長")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30Wそして、そうした手続きの\x01",
            "正当性よりも何よりも……\x02\x03",

            "私が皆さんに問いたいのは\x01",
            "他でもありません。\x02\x03",

            "果たしてこの状況は、\x01",
            "今の体制は、私たちの在り方は、\x01",
            "“正しい”のか？\x02\x03",

            "ただ──それだけであります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0302", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_7DE7 end

    def Function_31_80B2(): pass

    label("Function_31_80B2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "この先、警備隊専用貨物線路\x01",
            "  関係者以外立ち入り禁止\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_80B2 end

    SaveToFile()

Try(main)
