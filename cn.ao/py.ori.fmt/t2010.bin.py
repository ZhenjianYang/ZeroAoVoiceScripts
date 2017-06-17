from ScenarioHelper import *

def main():
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
        "柯纳斯队员",             # 1
        "西格队员",               # 2
        "史黛拉",                 # 3
        "库雷斯队员",             # 4
        "比约德",                 # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "女孩",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "罗梅奥队员",             # 12
        "米蕾优三尉",             # 13
        "哈罗德",                 # 14
        "游击士斯克特",           # 15
        "游击士温蔡尔",           # 16
        "导力车",                 # 17
        "索妮亚司令",             # 18
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
    DeclNpc(-99449,  50,      2230,    270,  452,  0x0, 0,   21,  0,   255, 255, 0,   26,  255,  0)
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
        "Function_9_1772",         # 09, 9
        "Function_10_200F",        # 0A, 10
        "Function_11_2013",        # 0B, 11
        "Function_12_2B1F",        # 0C, 12
        "Function_13_35D4",        # 0D, 13
        "Function_14_35D8",        # 0E, 14
        "Function_15_4286",        # 0F, 15
        "Function_16_44E3",        # 10, 16
        "Function_17_471A",        # 11, 17
        "Function_18_4961",        # 12, 18
        "Function_19_4A44",        # 13, 19
        "Function_20_4B8E",        # 14, 20
        "Function_21_4D05",        # 15, 21
        "Function_22_4F4F",        # 16, 22
        "Function_23_50A5",        # 17, 23
        "Function_24_5677",        # 18, 24
        "Function_25_5703",        # 19, 25
        "Function_26_583D",        # 1A, 26
        "Function_27_5A1B",        # 1B, 27
        "Function_28_5EF3",        # 1C, 28
        "Function_29_66AF",        # 1D, 29
        "Function_30_700D",        # 1E, 30
        "Function_31_72BE",        # 1F, 31
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
    SetChrPos(0x10, -94700, 200, 4190, 90)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")

    #N0001
    NpcTalk(
        0x8,
        "士兵柯纳斯",
        (
            "虽说通往帝国国境的大桥\x01",
            "仍未修复，但我们还是\x01",
            "严密警戒着帝国军的动静。\x02",
        )
    )

    CloseMessageWindow()

    #N0002
    NpcTalk(
        0x8,
        "士兵柯纳斯",
        (
            "一旦他们发动侵略，\x01",
            "区区一座断桥，\x01",
            "肯定马上就能修好了。\x02",
        )
    )

    CloseMessageWindow()

    #N0003
    NpcTalk(
        0x8,
        "士兵柯纳斯",
        (
            "不知这是否算是幸运，帝国正在持续内战……\x01",
            "我们得趁此机会，\x01",
            "认真做好应对准备。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F38")

    label("loc_E92")


    #N0004
    NpcTalk(
        0x8,
        "士兵柯纳斯",
        (
            "一旦帝国军发动侵略，\x01",
            "区区一座断桥，\x01",
            "肯定马上就能修好了。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "士兵柯纳斯",
        (
            "不知这是否算是幸运，帝国正在持续内战……\x01",
            "我们得趁此机会，\x01",
            "认真做好应对准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F38")

    Jump("loc_176E")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FE3")

    #C0006
    ChrTalk(
        0x8,
        (
            "鉴于最近的紧张局势，\x01",
            "有不少外国人都离开了\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "就算没有出现这种紧张局势，\x01",
            "最近也是骚乱事件接连不断……\x01",
            "大家选择离开，也是可以理解的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176E")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B5")

    #C0008
    ChrTalk(
        0x8,
        (
            "听说米蕾优三尉率领的部队\x01",
            "昨天目击到了一只巨大的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "为了堤防那头已经逃走的怪物，\x01",
            "暂时会派一个中队在\x01",
            "自治州内巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "局势都已经这么紧张了，\x01",
            "事情却越来越多。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1131")

    label("loc_10B5")


    #C0011
    ChrTalk(
        0x8,
        (
            "为了堤防那头已经逃走的怪物，\x01",
            "暂时会派一个中队在\x01",
            "自治州内巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "真是的……\x01",
            "局势都已经这么紧张了，\x01",
            "事情却越来越多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1131")

    Jump("loc_176E")

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11B1")

    #C0013
    ChrTalk(
        0x8,
        (
            "刚才从这里经过的帝国商人\x01",
            "一直在谈论关于\x01",
            "克洛斯贝尔独立的话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "看来帝国那边也在对\x01",
            "这件事议论纷纷。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176E")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A9")

    #C0015
    ChrTalk(
        0x8,
        (
            "最近，帝国军在要塞内部\x01",
            "举行了如同炫耀般的\x01",
            "军事演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "他们恐怕是想通过这种方式，\x01",
            "对我们警备队……不，应该是\x01",
            "对迪塔市长施加压力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "话虽如此，但和签订《互不侵犯条约》\x01",
            "之前的紧张局势比起来，这根本算不了什么。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1334")

    label("loc_12A9")


    #C0018
    ChrTalk(
        0x8,
        (
            "最近，帝国军在要塞内部\x01",
            "举行了如同炫耀般的\x01",
            "军事演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "话虽如此，但和签订《互不侵犯条约》\x01",
            "之前的紧张局势比起来，这根本算不了什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1334")

    Jump("loc_176E")

    label("loc_1339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1451")

    #C0020
    ChrTalk(
        0x8,
        (
            "有情报称，恐怖分子将会发动袭击，\x01",
            "所以上级下令要更加严密地\x01",
            "执行检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "从今天的警戒体制来看，\x01",
            "恐怖分子想从陆路进入\x01",
            "是绝对不可能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "至于航空方面，\x01",
            "也有人员在附近的\x01",
            "特殊设施严密警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "虽然警备队没有飞艇，\x01",
            "但还是要尽力做好我们能做的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14B1")

    label("loc_1451")


    #C0024
    ChrTalk(
        0x8,
        (
            "受自治州法的规定所限，\x01",
            "我们警备队不能拥有飞艇。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "为了领空的警备，\x01",
            "真希望能配备飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B1")

    Jump("loc_176E")

    label("loc_14B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")

    #C0026
    ChrTalk(
        0x8,
        (
            "前来参加通商会议的奥斯本宰相\x01",
            "一般被称为『铁血宰相』。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "之所以会有这个外号，是因为他的\x01",
            "信条正是『国家的安定要靠铁与血，\x01",
            "即兵器与兵力』。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "以这番话为基础，\x01",
            "他指挥帝国的军队，\x01",
            "靠武力吞并了好几个自治州。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "对于克洛斯贝尔自治州来说，\x01",
            "他毫无疑问是最需要注意的\x01",
            "危险人物之一。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_167E")

    label("loc_15EE")


    #C0030
    ChrTalk(
        0x8,
        (
            "帝国以武力吞并了好几个\x01",
            "自治州，而其中多是因为\x01",
            "『铁血宰相』的动作。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "对于克洛斯贝尔自治州来说，\x01",
            "他毫无疑问是最需要注意的\x01",
            "危险人物之一。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167E")

    Jump("loc_176E")

    label("loc_1683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_176E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171E")

    #C0032
    ChrTalk(
        0x8,
        (
            "穿过那边的铁栅，\x01",
            "用不了多久就能抵达帝国的\x01",
            "『卡雷利亚要塞』。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "如想前往，请务必注意。\x01",
            "因为帝国对出入境的检查\x01",
            "相当严格。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_176E")

    label("loc_171E")


    #C0034
    ChrTalk(
        0x8,
        (
            "帝国对出入境的检查\x01",
            "十分严格。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "如想前往『卡雷利亚要塞』，\x01",
            "请务必注意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176E")

    TalkEnd(0x8)
    Return()

    # Function_8_D7B end

    def Function_9_1772(): pass

    label("Function_9_1772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_18D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1857")

    #N0036
    NpcTalk(
        0x9,
        "士兵西格",
        (
            "独立无效宣言公开发表，\x01",
            "国防长官下落不明……\x01",
            "现在连总统都被拘捕了。\x02",
        )
    )

    CloseMessageWindow()

    #N0037
    NpcTalk(
        0x9,
        "士兵西格",
        (
            "我们继续以国防军的身份工作，\x01",
            "真的妥当吗……\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x9,
        "士兵西格",
        (
            "……在这种情况下，\x01",
            "再怎么思考也无法理清头绪。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18CD")

    label("loc_1857")


    #N0039
    NpcTalk(
        0x9,
        "士兵西格",
        (
            "我们继续以国防军的身份工作，\x01",
            "真的妥当吗……\x02",
        )
    )

    CloseMessageWindow()

    #N0040
    NpcTalk(
        0x9,
        "士兵西格",
        (
            "……在这种情况下，\x01",
            "再怎么思考也无法理清头绪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CD")

    Jump("loc_200B")

    label("loc_18D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1960")

    #C0041
    ChrTalk(
        0xFE,
        (
            "无论帝国今后动用\x01",
            "什么样的手段，\x01",
            "我们也绝不会屈服。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "我们绝不能让同伴们的\x01",
            "死亡变得毫无意义。\x01",
            "……怎么能让他们白白牺牲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200B")

    label("loc_1960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A00")

    #C0043
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "在昨晚的抢修工作中积存的疲惫，\x01",
            "直到现在都没有完全消除呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "目前的状况如此紧张，\x01",
            "也不知道今后会发生什么事，\x01",
            "还是趁现在打个盹吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200B")

    label("loc_1A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFB")

    #C0045
    ChrTalk(
        0xFE,
        (
            "其实我们警备队很想\x01",
            "亲自去调查那些\x01",
            "名为『幻兽』的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "但由于发表了独立提案的缘故，\x01",
            "如今的局势十分紧张，\x01",
            "实在是无法顾及那方面的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "……所以只能交给你们了，兰迪。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#00300F没问题，你们也要\x01",
            "好好加油哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B8D")

    label("loc_1AFB")


    #C0049
    ChrTalk(
        0xFE,
        (
            "其实我们警备队很想\x01",
            "亲自去调查那些\x01",
            "名为『幻兽』的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "但由于发表了独立提案的缘故，\x01",
            "如今的局势十分紧张，\x01",
            "实在是无法顾及那方面的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8D")

    Jump("loc_200B")

    label("loc_1B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C30")

    #C0051
    ChrTalk(
        0xFE,
        (
            "不久前，米蕾优准尉\x01",
            "晋升为三尉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "如果是在其他国家的军队里，\x01",
            "三尉就等同于少尉级别了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "真期待三尉今后的\x01",
            "活跃表现啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C9B")

    label("loc_1C30")


    #C0054
    ChrTalk(
        0xFE,
        (
            "以她的实力来看，\x01",
            "此次晋升实在是来得太晚了……\x01",
            "总之，真是可喜可贺。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "真期待三尉今后的\x01",
            "活跃表现啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9B")

    Jump("loc_200B")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D0C")

    #C0056
    ChrTalk(
        0xFE,
        (
            "探测器没有任何反应。\x01",
            "……看来并未运载危险物品。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "但保险起见，\x01",
            "还是调查一下车下吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200B")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E21")

    #C0058
    ChrTalk(
        0xFE,
        (
            "索妮亚司令安排的\x01",
            "通商会议警备措施\x01",
            "实在是非常合理。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "她不仅懂得选择能力适合的人选，\x01",
            "而且只在每个岗位安排最低限度的人手，\x01",
            "多亏如此，才能同时顾及边境地带的警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "和前任司令相比，真是完全不同啊。\x01",
            "看来确实存在司令这种\x01",
            "天生拥有领导才能的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E8B")

    label("loc_1E21")


    #C0061
    ChrTalk(
        0xFE,
        (
            "我一定会不断积累成绩，\x01",
            "争取有朝一日坐上司令的宝座……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "但只要索妮亚司令还在，\x01",
            "我就根本没机会呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8B")

    Jump("loc_200B")

    label("loc_1E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_200B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7B")

    #C0063
    ChrTalk(
        0xFE,
        (
            "前司令通过哈尔特曼\x01",
            "结识了约亚西姆，\x01",
            "以至于在教团事件时被对方利用。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "之后他被免职，\x01",
            "索妮亚副司令成为新司令，\x01",
            "完全是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "从今以后，警备队的运作模式\x01",
            "肯定会比以前强得多。\x01",
            "这真是让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_200B")

    label("loc_1F7B")


    #C0066
    ChrTalk(
        0xFE,
        (
            "都是因为前司令无能，\x01",
            "才会使米蕾优准尉\x01",
            "一直背负着那么沉重的担子……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "从今以后，警备队的运作模式\x01",
            "肯定会比以前强得多。\x01",
            "这真是让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200B")

    TalkEnd(0xFE)
    Return()

    # Function_9_1772 end

    def Function_10_200F(): pass

    label("Function_10_200F")

    Call(0, 11)
    Return()

    # Function_10_200F end

    def Function_11_2013(): pass

    label("Function_11_2013")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203C")
    Call(0, 28)
    Return()

    label("loc_203C")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2049")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2099")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2099")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B9")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B16")

    label("loc_20B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20CD")
    Jump("loc_2B16")

    label("loc_20CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B16")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2160")

    #C0068
    ChrTalk(
        0xA,
        (
            "贝尔加德门警备队员专享的\x01",
            "『大饱口福锅』十分美味吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "这里经常召开火锅派对，\x01",
            "最后总会变成抢肉大战～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B16")

    label("loc_2160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220B")

    #C0070
    ChrTalk(
        0xA,
        (
            "虽然大家都感到很不安……\x01",
            "但我一点都不害怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "因为库雷斯\x01",
            "说他一定会\x01",
            "保护好我的。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "既然如此，我一定要尽己所能，\x01",
            "用乐观精神感染大家。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2282")

    label("loc_220B")


    #C0073
    ChrTalk(
        0xA,
        (
            "因为那棵莫名其妙的巨树，\x01",
            "还有总统被拘捕的消息，\x01",
            "大家都感到十分不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "我一定要尽己所能，\x01",
            "用乐观精神感染大家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2282")

    Jump("loc_2B16")

    label("loc_2287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234F")

    #C0075
    ChrTalk(
        0xA,
        (
            "与帝国的关系如此紧张……\x01",
            "让人不禁想起了签订\x01",
            "《互不侵犯条约》之前的情况呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "当帝国的『列车炮』\x01",
            "瞄准这里的时候，\x01",
            "真是让人十分恐惧……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "真希望别再发生\x01",
            "那种事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_23BA")

    label("loc_234F")


    #C0078
    ChrTalk(
        0xA,
        (
            "在签署《互不侵犯条约》之前，\x01",
            "帝国曾在演习过程中\x01",
            "开出过那台『列车炮』。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "真希望别再发生\x01",
            "那种事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23BA")

    Jump("loc_2B16")

    label("loc_23BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2518")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2494")

    #C0080
    ChrTalk(
        0xA,
        (
            "今天下起了讨厌的雨。\x01",
            "正在外面警备的队员们肯定十分辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "在这种日子，就该吃些\x01",
            "可以让身体暖起来的菜式。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "干脆就把昨天给库雷斯做的\x01",
            "那种超辣炖菜改良一下，\x01",
            "给大家做个火锅吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2513")

    label("loc_2494")


    #C0083
    ChrTalk(
        0xA,
        (
            "在这种下雨天，\x01",
            "最适合吃些可以让身体暖起来的菜式。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "干脆就把昨天给库雷斯做的\x01",
            "那种超辣炖菜改良一下，\x01",
            "给大家做个火锅吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2513")

    Jump("loc_2B16")

    label("loc_2518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D5")

    #C0085
    ChrTalk(
        0xA,
        (
            "库雷斯最近一直都没什么精神，\x01",
            "为了让他振奋起来，\x01",
            "我给他做了一道超辣炖菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xA,
        (
            "一开始我还担心\x01",
            "味道太辣了……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        (
            "但看他吃得那么香，\x01",
            "应该是没有问题呢，呵呵。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2641")

    label("loc_25D5")


    #C0088
    ChrTalk(
        0xA,
        (
            "呵呵，看他吃得\x01",
            "那么高兴，我也\x01",
            "觉得很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "既然已经开始交往了，\x01",
            "今后也多为他做些\x01",
            "特别的菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2641")

    Jump("loc_2B16")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    #C0090
    ChrTalk(
        0xA,
        (
            "库雷斯最近好像\x01",
            "没什么精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "好！那我就给他做些\x01",
            "能让他打起精神的\x01",
            "菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "虽说这个男朋友还在试用期，\x01",
            "但我还是得做点份内之事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2754")

    label("loc_26EF")


    #C0093
    ChrTalk(
        0xA,
        (
            "我就给他做些\x01",
            "能让他打起精神的\x01",
            "菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "虽说这个男朋友还在试用期，\x01",
            "但我还是得做点份内之事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2754")

    Jump("loc_2B16")

    label("loc_2759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27D4")

    #C0095
    ChrTalk(
        0xA,
        (
            "听说恐怖分子\x01",
            "可能会入侵\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xA,
        (
            "边境大门的警戒力度比之前更强了，\x01",
            "不知道各位队员能不能撑得住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B16")

    label("loc_27D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_291A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AA")

    #C0097
    ChrTalk(
        0xA,
        (
            "试着跟库雷斯交往以来，\x01",
            "已经过了好一段时日了。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "不过，虽说正在交往，\x01",
            "但平时却没有什么特别的……\x01",
            "交往就是这么一回事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "对男人来说，\x01",
            "『正在交往』这个事实\x01",
            "也许才是最重要的呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2915")

    label("loc_28AA")


    #C0100
    ChrTalk(
        0xA,
        (
            "我在这方面也没什么经验，\x01",
            "所以不大懂……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "但对男人来说，\x01",
            "『正在交往』这个事实\x01",
            "也许才是最重要的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2915")

    Jump("loc_2B16")

    label("loc_291A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA4")
    TurnDirection(0xA, 0x104, 0)

    #C0102
    ChrTalk(
        0xA,
        (
            "哎呀，欢迎来……\x01",
            "什么啊，这不是兰迪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "复健训练不是\x01",
            "已经结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，是啊……\x01",
            "我只是想来见一见\x01",
            "可爱的你呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "啊哈哈，你还是老样子，\x01",
            "总爱说这种玩笑话。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "不过，你以后要是再敢对我搭讪，\x01",
            "库雷斯可是会生气的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00006F……兰迪，\x01",
            "坐在位子上的队员正在\x01",
            "恶狠狠地盯着你呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00306F……好、好像确实会惹上麻烦啊，\x01",
            "我记住了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B16")

    label("loc_2AA4")


    #C0109
    ChrTalk(
        0xA,
        (
            "呵呵，先不说这个了……\x01",
            "难得来一回，吃点什么吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "如果你能像复健训练时那样\x01",
            "狼吞虎咽地吃饭，我看着也高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B16")

    Jump("loc_2049")

    label("loc_2B1B")

    TalkEnd(0xA)
    Return()

    # Function_11_2013 end

    def Function_12_2B1F(): pass

    label("Function_12_2B1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B48")
    Call(0, 27)
    Return()

    label("loc_2B48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0D")

    #N0111
    NpcTalk(
        0xB,
        "士兵库雷斯",
        (
            "老实说，我也不知道\x01",
            "该怎么办才好。\x02",
        )
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0xB,
        "士兵库雷斯",
        (
            "但我必须要亲手\x01",
            "保护我爱的人。\x02",
        )
    )

    CloseMessageWindow()

    #N0113
    NpcTalk(
        0xB,
        "士兵库雷斯",
        (
            "好……\x01",
            "总之还是先吃饭吧！\x01",
            "吃得饱饱的，让自己充满力量！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C82")

    label("loc_2C0D")


    #N0114
    NpcTalk(
        0xB,
        "士兵库雷斯",
        "再怎么说，饿着肚子也无法上战场啊。\x02",
    )

    CloseMessageWindow()

    #N0115
    NpcTalk(
        0xB,
        "士兵库雷斯",
        (
            "为了保护我爱的人……\x01",
            "我一定得多吃！吃得饱饱的！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C82")

    Jump("loc_35D0")

    label("loc_2C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5C")

    #C0116
    ChrTalk(
        0xFE,
        (
            "不久前，有好几个同伴在\x01",
            "玛因兹的战斗中牺牲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "如果我们拥有性能强劲的战车，\x01",
            "说不定就能减少一些损伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "为了能在今后继续保护\x01",
            "史黛拉和其他重要的人，\x01",
            "独立也许真的是有必要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2DF0")

    label("loc_2D5C")


    #C0119
    ChrTalk(
        0xFE,
        (
            "如果我们拥有性能强劲的战车，\x01",
            "说不定就能使玛因兹战役中的\x01",
            "伤亡降低……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "为了能在今后继续保护\x01",
            "史黛拉和其他重要的人，\x01",
            "独立也许真的是有必要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF0")

    Jump("loc_35D0")

    label("loc_2DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA3")

    #C0121
    ChrTalk(
        0xFE,
        (
            "昨天吃了史黛拉为我\x01",
            "烹调的超辣炖菜后，\x01",
            "感觉身体状态非常棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "呵呵呵……\x01",
            "这就是爱情的力量吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "……不过，实在是不想再次体验那种劲辣了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F24")

    label("loc_2EA3")


    #C0124
    ChrTalk(
        0xFE,
        (
            "昨天吃了史黛拉为我\x01",
            "烹调的超辣炖菜后，\x01",
            "感觉身体状态非常棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "真该好好感谢她啊。\x01",
            "……不过，实在是不想再次体验那种劲辣了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F24")

    Jump("loc_35D0")

    label("loc_2F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE1")

    #C0126
    ChrTalk(
        0xFE,
        (
            "呼……呼……\x01",
            "哇哇！好、好辣，太辣了……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "不、不行，这可是我的甜心\x01",
            "为我特地烹调的。\x01",
            "吃得一滴不剩才是真汉子。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        "呜喔喔喔～（狼吞虎咽）……！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3041")

    label("loc_2FE1")


    #C0129
    ChrTalk(
        0xFE,
        (
            "呼……呼……\x01",
            "果、果然还是好、好辣……！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "但、但我一定会吃完它的！\x01",
            "（狼吞虎咽）……！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3041")

    Jump("loc_35D0")

    label("loc_3046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_310D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CA")

    #C0131
    ChrTalk(
        0xFE,
        (
            "唉……这段时间的紧张局势\x01",
            "真是让人十分疲惫。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "……不行不行，\x01",
            "史黛拉正看着我呢，\x01",
            "我得挺起腰杆来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3108")

    label("loc_30CA")


    #C0133
    ChrTalk(
        0xFE,
        (
            "最近真的好累……\x01",
            "但史黛拉正在看着我呢，\x01",
            "我得挺起腰杆来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3108")

    Jump("loc_35D0")

    label("loc_310D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_318B")

    #C0134
    ChrTalk(
        0xFE,
        (
            "今天一定要认真做好警备工作，\x01",
            "让史黛拉看看我的帅气之处。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "恐怖分子也好，别的什么也好，\x01",
            "统统放马过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D0")

    label("loc_318B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3242")

    #C0136
    ChrTalk(
        0xFE,
        (
            "我终于开始和\x01",
            "史黛拉交往了，\x01",
            "但连一次像样的约会都没有过。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "虽说通商会议即将召开，\x01",
            "最近一直很忙也占了一部分原因，\x01",
            "但我好像根本就没有邀约的胆量呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_326C")

    label("loc_3242")


    #C0138
    ChrTalk(
        0xFE,
        (
            "可恶～\x01",
            "真想和史黛拉\x01",
            "进一步发展啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326C")

    Jump("loc_35D0")

    label("loc_3271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3372")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332F")

    #C0139
    ChrTalk(
        0xB,
        (
            "啧……就不能\x01",
            "听我说\x01",
            "几句吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "只要是有关史黛拉的话题，\x01",
            "我可以连续说上几个小时！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        "#00309F我先走啦，前辈。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        "听我说几句啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_336D")

    label("loc_332F")


    #C0143
    ChrTalk(
        0xB,
        (
            "啧……\x01",
            "只要是有关史黛拉的话题，\x01",
            "我可以连续说上几个小时！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336D")

    Jump("loc_35D0")

    label("loc_3372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_33DF")

    #C0144
    ChrTalk(
        0xFE,
        (
            "兰迪……！！\x01",
            "你这家伙，居然敢对我的甜心……！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        (
            "#00309F冷、冷静点，\x01",
            "我可什么都没干啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D0")

    label("loc_33DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354E")

    #C0146
    ChrTalk(
        0xFE,
        (
            "呵呵，史黛拉……\x01",
            "我的甜心……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00006F（我、我的甜心……？）\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        (
            "#00300F对了，前辈……\x01",
            "你好像说过，不久之前已经\x01",
            "开始和史黛拉『试着』交往了吧？\x02\x03",

            "#00309F哈哈，有什么进展了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "这、这个嘛……\x01",
            "那当然是甜甜蜜蜜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "我每天都在这里吃饭，\x01",
            "目不转睛地望着史黛拉……\x01",
            "每天都很幸福。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#00306F（……也就是说，\x01",
            "  至今都没有任何进展啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_35D0")

    label("loc_354E")


    #C0152
    ChrTalk(
        0xFE,
        (
            "史、史黛拉和我的恋情\x01",
            "才刚要开始呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "兰迪，你可不要向\x01",
            "史黛拉搭讪哦。\x01",
            "……算我求求你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#00306F（这也太没自信了。）\x02",
    )

    CloseMessageWindow()

    label("loc_35D0")

    TalkEnd(0xFE)
    Return()

    # Function_12_2B1F end

    def Function_13_35D4(): pass

    label("Function_13_35D4")

    Call(0, 14)
    Return()

    # Function_13_35D4 end

    def Function_14_35D8(): pass

    label("Function_14_35D8")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4282")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3635")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3635")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3655")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_427D")

    label("loc_3655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3669")
    Jump("loc_427D")

    label("loc_3669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373A")

    #C0155
    ChrTalk(
        0xC,
        (
            "在这种时候，\x01",
            "精神上的负担非常要命。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xC,
        (
            "能休息的时候，就要好好休息，\x01",
            "让自己的心情平静下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "……话虽如此，但我其实也很不安。\x01",
            "和平时代还会回来吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37AE")

    label("loc_373A")


    #C0158
    ChrTalk(
        0xC,
        (
            "能休息的时候，就要好好休息，\x01",
            "让自己的心情平静下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "……话虽如此，但我其实也很不安。\x01",
            "和平时代还会回来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AE")

    Jump("loc_427D")

    label("loc_37B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_392A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A1")

    #C0160
    ChrTalk(
        0xC,
        (
            "那个在克洛斯贝尔为所欲为，\x01",
            "最后不知跑到哪里去的『赤色星座』，\x01",
            "似乎拥有飞艇呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xC,
        (
            "而且连警备队的对空雷达\x01",
            "都捕捉不到他们的行踪……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        (
            "……老实说，就算有钱，\x01",
            "应该也买不到那种技术。\x01",
            "他们到底是什么人……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3925")

    label("loc_38A1")


    #C0163
    ChrTalk(
        0xC,
        (
            "连警备队的对空雷达\x01",
            "都无法捕捉到\x01",
            "『赤色星座』的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xC,
        (
            "……老实说，就算有钱，\x01",
            "应该也买不到那种技术。\x01",
            "他们到底是什么人……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3925")

    Jump("loc_427D")

    label("loc_392A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3D")

    #C0165
    ChrTalk(
        0xC,
        (
            "我也听说昨天那起事故了，\x01",
            "据说是一只巨大的怪物用蛮力硬撞，\x01",
            "才会造成那起列车事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "那辆列车是由以开发兵器而闻名的\x01",
            "帝国莱恩福尔特公司制造的。\x01",
            "应该有着装甲车般的强度……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "所以，我虽然没有亲眼目睹，\x01",
            "但也可以想象那是一头\x01",
            "多么可怕的怪物了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3ADF")

    label("loc_3A3D")


    #C0168
    ChrTalk(
        0xC,
        (
            "那辆列车可是由以开发兵器而闻名的\x01",
            "帝国莱恩福尔特公司制造的，\x01",
            "居然能靠撞击它造成列车事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        (
            "虽然我没有亲眼目睹，\x01",
            "但也可以想象那是一头\x01",
            "多么可怕的怪物了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADF")

    Jump("loc_427D")

    label("loc_3AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1B")

    #C0170
    ChrTalk(
        0xC,
        (
            "各国军队都在渐渐走向机甲化，\x01",
            "近年来，尤为重视的就是航空战术。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "比如说，在十二年前的『百日战役』中，\x01",
            "帝国以压倒性的军事力量\x01",
            "侵略了利贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xC,
        (
            "但在战争的最后，利贝尔凭借\x01",
            "最新开发的飞艇，\x01",
            "一下子就扭转了战局。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xC,
        (
            "两大国之所以不允许警备队拥有飞艇，\x01",
            "恐怕也是出于这个原因吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CA8")

    label("loc_3C1B")


    #C0174
    ChrTalk(
        0xC,
        (
            "各国军队都在渐渐走向机甲化，\x01",
            "近年来，尤为重视的就是航空战术。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "如果独立之后，警备队重组为军队，\x01",
            "真希望上面能赶快\x01",
            "给他们配备飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA8")

    Jump("loc_427D")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D89")

    #C0176
    ChrTalk(
        0xC,
        (
            "如果克洛斯贝尔真的独立了，\x01",
            "警备队也会重组为\x01",
            "正式的军队吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "到时候，队员们应该也能\x01",
            "换上比现在更加强力的武装。\x01",
            "说不定还会配备战车呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "唔～身为一名狂热军事爱好者，\x01",
            "真是万分期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E21")

    label("loc_3D89")


    #C0179
    ChrTalk(
        0xC,
        (
            "如果克洛斯贝尔独立之后，\x01",
            "警备队重组为正式军队，\x01",
            "装备一定会比现在更好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xC,
        (
            "说不定还会配备战车呢。\x01",
            "唔～身为一名狂热军事爱好者，\x01",
            "真是万分期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E21")

    Jump("loc_427D")

    label("loc_3E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF5")

    #C0181
    ChrTalk(
        0xC,
        (
            "正式会议今天终于\x01",
            "要在兰花塔召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "考虑到帝国和共和国，\x01",
            "警备队无法光明正大地\x01",
            "前去警备……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "但那毕竟是十分重要的国际会议，\x01",
            "即使警备队只能暗中守卫，也要保证顺利召开。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F69")

    label("loc_3EF5")


    #C0184
    ChrTalk(
        0xC,
        (
            "正式会议今天终于\x01",
            "要在兰花塔召开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "那可是十分重要的国际会议，\x01",
            "即使警备队只能暗中守卫，也要保证顺利召开。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F69")

    Jump("loc_427D")

    label("loc_3F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_40FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407F")

    #C0186
    ChrTalk(
        0xC,
        (
            "配备了新型装甲车之后，\x01",
            "已经过去一段时日了……\x01",
            "哎呀呀，果然非常棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "车身装载了威力强大的导弹发射台，\x01",
            "装甲也有了大幅度的强化。\x01",
            "它无疑是警备队最棒的武装。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "与其它国家的飞艇、战车相比，\x01",
            "自然还是有所不及，\x01",
            "但它也有自身独具的机能之美。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40FA")

    label("loc_407F")


    #C0189
    ChrTalk(
        0xC,
        (
            "新型装甲车无疑是\x01",
            "警备队最棒的武装。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        (
            "与其它国家的飞艇、战车相比，\x01",
            "自然还是有所不及，\x01",
            "但它也有自身独具的机能之美。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40FA")

    Jump("loc_427D")

    label("loc_40FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_427D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E9")

    #C0191
    ChrTalk(
        0xC,
        (
            "我是个军事爱好者……\x01",
            "也就是所谓的军事迷。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        (
            "我太喜欢军事方面的事物了，\x01",
            "之所以会在这里工作，\x01",
            "主要也是出于兴趣爱好。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xC,
        (
            "严格来说，克洛斯贝尔的警备队\x01",
            "并不能算作军队……\x01",
            "但对我来说，已经十分有魅力了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_427D")

    label("loc_41E9")


    #C0194
    ChrTalk(
        0xC,
        (
            "我是个军事迷。\x01",
            "之所以会在这里工作，\x01",
            "主要也是出于兴趣爱好。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "严格来说，克洛斯贝尔的警备队\x01",
            "并不能算作军队……\x01",
            "但对我来说，已经十分有魅力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_427D")

    Jump("loc_35E5")

    label("loc_4282")

    TalkEnd(0xC)
    Return()

    # Function_14_35D8 end

    def Function_15_4286(): pass

    label("Function_15_4286")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4297")
    Jump("loc_44DF")

    label("loc_4297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4378")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4329")

    #C0196
    ChrTalk(
        0xFE,
        (
            "我被卷进昨天\x01",
            "那起列车事故了。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "幸好只受了点轻伤，\x01",
            "现在让女儿来接我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "哇哇！疼疼疼……\x01",
            "现在还有点疼呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4373")

    label("loc_4329")


    #C0199
    ChrTalk(
        0xFE,
        (
            "哇哇！疼疼疼……\x01",
            "现在还有点疼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "是不是应该在\x01",
            "医院多住几天呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4373")

    Jump("loc_44DF")

    label("loc_4378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_43F3")

    #C0201
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔居然想独立……\x01",
            "真是不知天高地厚。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "在帝国人看来，\x01",
            "这就像是被自己养的狗\x01",
            "给反咬了一口一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DF")

    label("loc_43F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4401")
    Jump("loc_44DF")

    label("loc_4401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4458")

    #C0203
    ChrTalk(
        0xFE,
        "能不能快点检查完毕啊？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "反恐对策和我有什么关系，\x01",
            "真是麻烦透顶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44DF")

    label("loc_4458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4466")
    Jump("loc_44DF")

    label("loc_4466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_44DF")

    #C0205
    ChrTalk(
        0xFE,
        (
            "在通商会议上，宰相阁下\x01",
            "肯定会让会议通过一些\x01",
            "对帝国有益的决定。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "呵呵，对我们帝国人来说，可是件好事啊。\x02",
    )

    CloseMessageWindow()

    label("loc_44DF")

    TalkEnd(0xFE)
    Return()

    # Function_15_4286 end

    def Function_16_44E3(): pass

    label("Function_16_44E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_456E")

    #C0207
    ChrTalk(
        0xFE,
        (
            "那起袭击事件之后，我曾犹豫过一段时间……\x01",
            "最后还是决定返回故乡帝国。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "不管怎么说，我可不想\x01",
            "再次被卷进那种事件了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4716")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_457C")
    Jump("loc_4716")

    label("loc_457C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_458A")
    Jump("loc_4716")

    label("loc_458A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_45E8")

    #C0209
    ChrTalk(
        0xFE,
        (
            "独立？\x01",
            "白日做梦也要有个限度啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔只要继续\x01",
            "被帝国榨取就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4716")

    label("loc_45E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_45F6")
    Jump("loc_4716")

    label("loc_45F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4677")

    #C0211
    ChrTalk(
        0xFE,
        (
            "哎呀，兰花塔恐怕\x01",
            "并不值得我这么急着赶过来看。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "不过，那东西最近\x01",
            "在帝国也是热门话题，\x01",
            "所以倒也想亲眼看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4716")

    label("loc_4677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4716")

    #C0213
    ChrTalk(
        0xFE,
        (
            "听说大家最近议论纷纷的\x01",
            "奥利维特皇子会以皇帝代理人的\x01",
            "身份来克洛斯贝尔参加通商会议。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "不过，皇帝陛下应该也\x01",
            "只是让他给『铁血宰相』\x01",
            "打打下手吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4716")

    TalkEnd(0xFE)
    Return()

    # Function_16_44E3 end

    def Function_17_471A(): pass

    label("Function_17_471A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47CF")

    #C0215
    ChrTalk(
        0xF,
        (
            "虽说帝国正在持续内战，\x01",
            "但我还是很想回到祖国，\x01",
            "所以才会到这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xF,
        (
            "但真没想到大桥\x01",
            "居然会毁坏成\x01",
            "那个样子……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xF,
        (
            "……今后到底该\x01",
            "怎么办才好呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_482E")

    label("loc_47CF")


    #C0218
    ChrTalk(
        0xF,
        (
            "爸爸说『我要去高处\x01",
            "看看那座断桥』，\x01",
            "然后就去楼上了……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xF,
        (
            "……看来还是无法\x01",
            "回到帝国啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_482E")

    Jump("loc_495D")

    label("loc_4833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4841")
    Jump("loc_495D")

    label("loc_4841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_484F")
    Jump("loc_495D")

    label("loc_484F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48BD")

    #C0220
    ChrTalk(
        0xFE,
        (
            "总觉得警备队的队员们\x01",
            "全都紧张得有些神经质。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "我可不想在这种地方久留，\x01",
            "还是早点回去吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_495D")

    label("loc_48BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48CB")
    Jump("loc_495D")

    label("loc_48CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_48D9")
    Jump("loc_495D")

    label("loc_48D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4954")

    #C0222
    ChrTalk(
        0xFE,
        (
            "我们是专程来看看那座\x01",
            "大家议论纷纷的超高大楼——\x01",
            "兰花塔的。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "到底是座什么样的大楼呢？\x01",
            "真让人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_495D")

    label("loc_4954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_495D")

    label("loc_495D")

    TalkEnd(0xFE)
    Return()

    # Function_17_471A end

    def Function_18_4961(): pass

    label("Function_18_4961")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_49CE")

    #C0224
    ChrTalk(
        0xFE,
        (
            "我原本还想在克洛斯贝尔\x01",
            "再玩上一阵子……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "但最近的情况实在是很可怕，\x01",
            "真没办法啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A40")

    label("loc_49CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_49DC")
    Jump("loc_4A40")

    label("loc_49DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_49EA")
    Jump("loc_4A40")

    label("loc_49EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49F8")
    Jump("loc_4A40")

    label("loc_49F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A29")

    #C0226
    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "我还想早点到城市里去呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A40")

    label("loc_4A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A37")
    Jump("loc_4A40")

    label("loc_4A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A40")

    label("loc_4A40")

    TalkEnd(0xFE)
    Return()

    # Function_18_4961 end

    def Function_19_4A44(): pass

    label("Function_19_4A44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4A55")
    Jump("loc_4B8A")

    label("loc_4A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4AD5")

    #C0227
    ChrTalk(
        0xFE,
        (
            "可恶，居然下起雨来了……\x01",
            "早知如此，真应该坐铁路列车啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "但不久前刚刚发生过列车事故，\x01",
            "心理上总有些抵触。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8A")

    label("loc_4AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4AE3")
    Jump("loc_4B8A")

    label("loc_4AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4AF1")
    Jump("loc_4B8A")

    label("loc_4AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4AFF")
    Jump("loc_4B8A")

    label("loc_4AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B81")

    #C0229
    ChrTalk(
        0xFE,
        (
            "今天早上，由于交通管制的缘故，\x01",
            "铁路列车暂时停运了。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "不过，毕竟要给首脑的专用列车让行，\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B8A")

    label("loc_4B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B8A")

    label("loc_4B8A")

    TalkEnd(0xFE)
    Return()

    # Function_19_4A44 end

    def Function_20_4B8E(): pass

    label("Function_20_4B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C14")

    #C0231
    ChrTalk(
        0xFE,
        (
            "我从克洛斯贝尔车站\x01",
            "运送货物过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "那里现在\x01",
            "一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "但在这种情况下，也是无可奈何的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4C59")

    label("loc_4C14")


    #C0234
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔车站\x01",
            "一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        "但在这种情况下，也是无可奈何的。\x02",
    )

    CloseMessageWindow()

    label("loc_4C59")

    Jump("loc_4D01")

    label("loc_4C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D01")

    #C0236
    ChrTalk(
        0x13,
        (
            "在边境大门的地下，\x01",
            "有一条货运专线。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x13,
        (
            "我在克洛斯贝尔车站检查了\x01",
            "货运列车，刚刚回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x13,
        (
            "……你们想去地下吗？\x01",
            "下面也没什么可看的，\x01",
            "要小心列车哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D01")

    TalkEnd(0xFE)
    Return()

    # Function_20_4B8E end

    def Function_21_4D05(): pass

    label("Function_21_4D05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E70")

    #C0239
    ChrTalk(
        0x104,
        (
            "#00301F米蕾优……\x01",
            "看来你很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x14,
        (
            "#07901F嗯，因为帝国的卡雷利亚要塞\x01",
            "似乎有什么动静。\x02\x03",

            "#07903F老实说，目前的局势实在是相当紧张。\x01",
            "……简直可以和两年前，也就是签订\x01",
            "《互不侵犯条约》之前的那段时期相比了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#00005F居然有这么严重……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#00303F……你可要多加小心啊，米蕾优。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x14,
        (
            "#07902F……嗯，我知道。\x01",
            "这里的事就交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4F13")

    label("loc_4E70")


    #C0244
    ChrTalk(
        0x14,
        (
            "#07903F帝国的卡雷利亚要塞\x01",
            "似乎有什么动静。\x02\x03",

            "#07901F老实说，目前的局势实在是相当紧张。\x01",
            "……简直可以和两年前，也就是签订\x01",
            "《互不侵犯条约》之前的那段时期相比了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F13")

    Jump("loc_4F4B")

    label("loc_4F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4F26")
    Jump("loc_4F4B")

    label("loc_4F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F34")
    Jump("loc_4F4B")

    label("loc_4F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F42")
    Jump("loc_4F4B")

    label("loc_4F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F4B")

    label("loc_4F4B")

    TalkEnd(0xFE)
    Return()

    # Function_21_4D05 end

    def Function_22_4F4F(): pass

    label("Function_22_4F4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FC9")

    #C0245
    ChrTalk(
        0xFE,
        (
            "没想到在事件发生之后的\x01",
            "这一个星期内，\x01",
            "形势会变得如此恶劣。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "我得赶快带女儿\x01",
            "一起离开克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A1")

    label("loc_4FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_500C")

    #C0247
    ChrTalk(
        0xFE,
        "爸爸，没事吧？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "要不要在食堂\x01",
            "稍微休息一会？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A1")

    label("loc_500C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_501A")
    Jump("loc_50A1")

    label("loc_501A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_507C")

    #C0249
    ChrTalk(
        0xFE,
        (
            "听说最近出现了一些\x01",
            "来历不明的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "总觉得很危险呢……\x01",
            "还是赶快回帝国吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A1")

    label("loc_507C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_508A")
    Jump("loc_50A1")

    label("loc_508A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5098")
    Jump("loc_50A1")

    label("loc_5098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50A1")

    label("loc_50A1")

    TalkEnd(0xFE)
    Return()

    # Function_22_4F4F end

    def Function_23_50A5(): pass

    label("Function_23_50A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5522")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5265")

    #C0251
    ChrTalk(
        0x15,
        (
            "#03600F昨天发生在阿尔摩利卡村的\x01",
            "那起事件能够顺利解决，真是太好了。\x02\x03",

            "#03603F如果没有大家的帮助，\x01",
            "真不知事情会变成什么样……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#00001F无德商人敏涅斯……\x01",
            "真是个不好对付的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#00200F不过，他现在已经被通缉，\x01",
            "抓住他也只是时间问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，这可难说。\x01",
            "那家伙可相当\x01",
            "难对付呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#00303F说的也是，在真正抓住他之前，\x01",
            "实在无法彻底放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x15,
        (
            "#03608F是啊……\x01",
            "在那之前，希望别再出现\x01",
            "新的受害者了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_551A")

    label("loc_5265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_5409")

    #C0257
    ChrTalk(
        0x15,
        (
            "#03605F哦，是你们啊……\x02\x03",

            "#03600F对了，说起敏涅斯在\x01",
            "阿尔摩利卡村做的那件事……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#00003F……我们当时没能\x01",
            "继续调查下去，真是对不起。\x02\x03",

            "#00008F因为之后接到了\x01",
            "更加紧急的工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x15,
        (
            "#03600F哪里哪里，不必放在心上。\x01",
            "在伊安律师的协助下，\x01",
            "那件事情已经完美解决了……\x02\x03",

            "#03604F而且，各位之前取得的调查成果\x01",
            "也起到了很重要的作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#00000F是、是吗……\x01",
            "那可真是太好了。\x02\x03",

            "#00003F（当时真应该\x01",
            "  调查到底啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_551A")

    label("loc_5409")


    #C0261
    ChrTalk(
        0x15,
        (
            "#03600F对了，阿尔摩利卡村昨天\x01",
            "发生了一起严重的事件。\x02\x03",

            "#03603F但那起事件关系到了村长他们的名誉，\x01",
            "所以不能把详情透露给大家……\x02\x03",

            "#03600F总之，如果没有伊安律师的帮助，\x01",
            "那起事件肯定无法\x01",
            "顺利解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00005F（听起来似乎是很严重的事件呢……\x01",
            "  我们当时要是去帮忙就好了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_551A")

    SetScenarioFlags(0x17C, 1)
    Jump("loc_5673")

    label("loc_5522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F5")

    #C0263
    ChrTalk(
        0x15,
        (
            "#03600F我今天是自己开车，\x01",
            "经由西克洛斯贝尔街道来到这里的……\x02\x03",

            "#03603F一想到脱轨事件刚过去一天，\x01",
            "总会有些不放心呢。\x02\x03",

            "#03600F另外，据传言说，\x01",
            "当时还出现了巨大的怪物。\x01",
            "看来还是多加小心为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5673")

    label("loc_55F5")


    #C0264
    ChrTalk(
        0x15,
        (
            "#03600F我今天是自己开车，\x01",
            "经由西克洛斯贝尔街道来到这里的……\x02\x03",

            "据传言说，\x01",
            "当时还出现了巨大的怪物。\x01",
            "看来还是多加小心为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5673")

    TalkEnd(0xFE)
    Return()

    # Function_23_50A5 end

    def Function_24_5677(): pass

    label("Function_24_5677")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568C")
    Call(0, 25)
    Jump("loc_56FF")

    label("loc_568C")


    #C0265
    ChrTalk(
        0xFE,
        (
            "边境地区的局势真紧张……\x01",
            "但愿别发生什么意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "为了普通民众的安全，\x01",
            "我们协会也得好好\x01",
            "确认一下现在的状态。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FF")

    TalkEnd(0xFE)
    Return()

    # Function_24_5677 end

    def Function_25_5703(): pass

    label("Function_25_5703")

    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    #C0267
    ChrTalk(
        0x16,
        (
            "……原来如此，看来边境地区的\x01",
            "状况确实不容忽视。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x16,
        (
            "在这种时候，真希望能和\x01",
            "帝国协会同心协力，共渡难关。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x17,
        (
            "……可惜的是，帝国协会\x01",
            "在军方的压力下日渐衰退。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x17,
        (
            "虽然有几个有骨气的家伙……\x01",
            "但连整个组织都已陷入那种状况，\x01",
            "现在也指望不上他们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x16,
        "是吗……那真是没办法啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_25_5703 end

    def Function_26_583D(): pass

    label("Function_26_583D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_58FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_585B")
    Call(0, 25)
    Jump("loc_58F7")

    label("loc_585B")


    #C0272
    ChrTalk(
        0xFE,
        (
            "如果可以与帝国协会联手，\x01",
            "说不定就能以中立的立场\x01",
            "来缓和如今的紧张局势了……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "……可惜的是，帝国协会\x01",
            "在军方的压力下日渐衰退，\x01",
            "现在根本无法指望他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58F7")

    Jump("loc_5A17")

    label("loc_58FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B1")

    #C0274
    ChrTalk(
        0xFE,
        (
            "今天斯克特和我分头行动，\x01",
            "我把这附近的通缉魔兽消灭掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "通商会议开始之后，\x01",
            "我们游击士肯定也会相当忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "在那之前，必须要尽最大努力\x01",
            "完成手头的委托。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5A17")

    label("loc_59B1")


    #C0277
    ChrTalk(
        0xFE,
        (
            "通商会议开始之后，\x01",
            "我们游击士肯定也会相当忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "在那之前，必须要尽最大努力\x01",
            "完成手头的委托。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A17")

    TalkEnd(0xFE)
    Return()

    # Function_26_583D end

    def Function_27_5A1B(): pass

    label("Function_27_5A1B")

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
        "#12P#00309F你好啊，库雷斯前辈。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xB,
        "#5P哇……兰迪！？\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xB,
        (
            "#5P复健训练不是\x01",
            "已经结束了吗？\x01",
            "你来这里干什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        "#12P#00000F是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0283
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将接受教授的委托，\x01",
            "前来收取问诊表的事情做了说明。\x07\x00\x02",
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
            "#5P问诊表……啊！\x01",
            "我完全忘了这回事了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    #C0285
    ChrTalk(
        0xB,
        (
            "#5P你们稍等一下，\x01",
            "我记得就在这里……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    #C0286
    ChrTalk(
        0xB,
        "#5P给，就是这个吧？\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '库雷斯队员的问诊表'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('库雷斯队员的问诊表', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0288
    ChrTalk(
        0x101,
        "#12P#00000F是的，就是它。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "#5P哎呀～真是抱歉，\x01",
            "害得你们特地\x01",
            "跑来取。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "#5P我最近实在是太幸福了，\x01",
            "所以完全忘了这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        "#12P#00105F幸福……？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "#5P没错，我和史黛拉\x01",
            "每天都恩恩爱爱地……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0293
    ChrTalk(
        0x104,
        (
            "#6P#00304F好了，罗伊德，\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        "#12P#10300F嗯，反正已经把正事办完了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0295
    ChrTalk(
        0x101,
        (
            "#11P#00012F……是、是啊。\x01",
            "（如果听他说下去，恐怕会很耗时间……）\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xB,
        (
            "#5P喂、喂！你们几个！？\x01",
            "就不能听我说说吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        "#12P#10100F啊哈哈……抱歉。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 6)
    OP_29(0x70, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC0")

    #A0298
    AnonymousTalk(
        0x101,
        (
            "#00003F好，我们已经把所有\x01",
            "问诊表都收回来了。\x02\x03",

            "#00000F赶快给赛兰德教授\x01",
            "送去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_5EC0")

    SetChrPos(0xB, -97470, 150, -3950, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -94400, 0, -3950, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_5A1B end

    def Function_28_5EF3(): pass

    label("Function_28_5EF3")

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
            "啊，是兰迪……\x01",
            "还有支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        "#00309F哟，史黛拉。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，我们今天\x01",
            "是为了工作而来的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0302
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

    #C0303
    ChrTalk(
        0xA,
        (
            "啊，说起来……\x01",
            "我也听说过这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xA,
        (
            "好，那我就给你们做一份\x01",
            "贝尔加德门警备队员专享的\x01",
            "『大饱口福锅』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#10105F哦？这里的部队还有\x01",
            "这种待遇啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x103,
        "#00200F那就麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xA,
        (
            "没问题，我这就去准备你们\x01",
            "所有人的量，请稍等一下哦。\x02",
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
            "罗伊德等人品尝了『大饱口福锅』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0309
    ChrTalk(
        0x102,
        (
            "#00100F（大吃大嚼）……\x01",
            "嗯，吃完之后，身体感觉很暖和。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#00009F是啊，肉量充足，\x01",
            "还有大量野菜，很有营养。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x109,
        (
            "#10104F嗯，因为警备队的演习十分辛苦，\x01",
            "如果不吃这种菜来补充体力，\x01",
            "根本就撑不住。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        "#10300F呵呵，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xA,
        (
            "这里经常召开火锅派对，\x01",
            "最后总会变成抢肉大战～\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xA,
        (
            "兰迪在这里的时候，\x01",
            "甚至还会抢别人\x01",
            "盘子里的东西呢。\x02",
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
            "#00211F……你怎么能干那种事，\x01",
            "兰迪前辈。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0316
    ChrTalk(
        0x104,
        "#00309F哈哈，这就是所谓的弱肉强食嘛。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x173, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_63F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_63F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_6414")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_6427")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_643A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_643A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_6457")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_646A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_646A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_6487")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_649A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_649A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_64B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_64CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_64E7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_64E7")

    OP_29(0x80, 0x1, 0xB)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65BC")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0317
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_65B3")

    #A0318
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

    label("loc_65B3")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_65BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_667F")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0319
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

    #A0320
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

    label("loc_667F")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -103610, 0, 2100, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_5EF3 end

    def Function_29_66AF(): pass

    label("Function_29_66AF")

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

    def lambda_678D():
        OP_95(0x101, 21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_678D)
    Sleep(30)

    def lambda_67AA():
        OP_95(0x102, 21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67AA)
    Sleep(40)

    def lambda_67C7():
        OP_95(0x104, 21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67C7)
    Sleep(800)

    def lambda_67E4():
        OP_95(0x109, 23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67E4)
    Sleep(30)

    def lambda_6801():
        OP_95(0x103, 23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6801)
    Sleep(10)

    def lambda_681E():
        OP_95(0x105, 23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_681E)
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
            "#00001F那辆黑色运输车\x01",
            "应该就在这里……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_6925")

    #C0322
    ChrTalk(
        0x103,
        (
            "#00203F……据弗兰茨先生所说，\x01",
            "那辆运输车不是开往\x01",
            "共和国方向了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#00011F啊……说来也是。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#00106F但不知不觉就跑到\x01",
            "贝尔加德门了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6991")

    label("loc_6925")


    #C0325
    ChrTalk(
        0x103,
        (
            "#00205F……并没有发现\x01",
            "那样的车啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        (
            "#00100F唔……\x01",
            "干脆去找个队员\x01",
            "问问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        "#00003F说的也是……\x02",
    )

    CloseMessageWindow()

    label("loc_6991")


    def lambda_6996():
        OP_95(0xFE, 17460, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6996)
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
        "#07900F啊……是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        "#00300F哟，米蕾优。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        "#10100F您辛苦了，米蕾优三尉！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x14,
        (
            "#07902F各位也辛苦了。\x02\x03",

            "#07906F……呼……\x01",
            "你们今天来这里有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        "#10300F你看上去好像很疲惫啊。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x14,
        (
            "#07901F是啊……因为现在与\x01",
            "帝国之间的关系很紧张。\x02\x03",

            "#07903F而且，偏偏在这种时候，\x01",
            "唐古拉姆门那边还发生了骚乱……\x02",
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
        "#00005F唐古拉姆门那边发生了什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x14,
        (
            "#07901F听说有一辆帝国制造的黑色\x01",
            "运输车，明明手续不全，\x01",
            "却硬是闯过去了。\x02\x03",

            "#07903F不过，那边的队员已经对那辆车\x01",
            "做了最基本的检查，\x01",
            "我想应该不会有问题……\x02\x03",

            "#07901F但这件事让警备队丢尽了面子，\x01",
            "真是可恶……！\x02",
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
        "#07900F……嗯？你们怎么了？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        "#00006F没、没什么……\x02",
    )

    CloseMessageWindow()

    def lambda_6D6B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D6B)
    Sleep(10)

    def lambda_6D7B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6D7B)
    Sleep(50)

    def lambda_6D8B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6D8B)
    Sleep(10)

    def lambda_6D9B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6D9B)
    Sleep(30)

    def lambda_6DAB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6DAB)
    Sleep(10)

    def lambda_6DBB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6DBB)
    WaitChrThread(0x105, 2)

    #C0338
    ChrTalk(
        0x102,
        "#00101F刚、刚才说的难道就是……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#00006F……是的，\x01",
            "看来我们找错\x01",
            "地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        (
            "#00306F既然犯人已经成功逃往共和国，\x01",
            "我们也就无可奈何了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_6EEA")

    #C0341
    ChrTalk(
        0x101,
        (
            "#00001F虽然这个结果很遗憾……\x01",
            "但也只能去向比利先生\x01",
            "和乌尔斯拉医院如实报告了。\x02\x03",

            "#00006F唉……要是把弗兰茨的话\x01",
            "放在心上就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3F")

    label("loc_6EEA")


    #C0342
    ChrTalk(
        0x101,
        (
            "#00006F虽然这个结果很遗憾…\x01",
            "但我们也只能去向比利先生\x01",
            "和乌尔斯拉医院如实报告了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F3F")


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
            "罗伊德等人向正在克洛斯贝尔空港\x01",
            "等候的比利和利卡尔德\x01",
            "说明了事情的详细经过……\x02",
        )
    )

    CloseMessageWindow()

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后又和比利一同前往\x01",
            "乌尔斯拉医院，\x01",
            "交代了事情的原委。\x02",
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

    # Function_29_66AF end

    def Function_30_700D(): pass

    label("Function_30_700D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41800.itc", 0x20)
    LoadChrToIndex("chr/ch41402.itc", 0x21)
    LoadChrToIndex("chr/ch41502.itc", 0x22)
    LoadChrToIndex("chr/ch12200.itc", 0x23)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
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
    SetChrName("麦克道尔议长")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W各项手续的正当性\x01",
            "与其它问题暂且不谈……\x02\x03",

            "我最想向大家提出的\x01",
            "疑问其实是……\x02\x03",

            "如今这种状况，\x01",
            "这种体制，\x01",
            "以及我们自身的生存方式……\x02\x03",

            "真的是『正确』的吗？\x07\x00\x02",
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

    # Function_30_700D end

    def Function_31_72BE(): pass

    label("Function_31_72BE")

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
            "前方是警备队专用货运线路\x01",
            "  　无关人员禁止入内\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_72BE end

    SaveToFile()

Try(main)
