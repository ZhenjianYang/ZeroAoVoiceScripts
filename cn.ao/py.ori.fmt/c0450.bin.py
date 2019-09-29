from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0450.bin",                # FileName
        "c0450",                    # MapName
        "c0450",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0450",                  # 0
        "接待员凯尔",             # 1
        "德莉丝",                 # 2
        "亚伦",                   # 3
        "雷缇希亚经理",           # 4
        "敏涅斯",                 # 5
        "游客",                   # 6
        "游客",                   # 7
        "市民",                   # 8
        "女孩",                   # 9
        "市民",                   # 10
        "市民",                   # 11
        "游客",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "市民",                   # 15
        "迪利克",                 # 16
    ))

    AddCharChip((
        "chr/ch45200.itc",                   # 00
        "chr/ch22000.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch27500.itc",                   # 03
        "chr/ch27900.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch32402.itc",                   # 06
        "chr/ch22002.itc",                   # 07
        "chr/ch22300.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch21300.itc",                   # 0A
        "chr/ch33000.itc",                   # 0B
        "chr/ch21002.itc",                   # 0C
        "chr/ch20302.itc",                   # 0D
        "chr/ch23800.itc",                   # 0E
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   2,   0,   0,   2,   0,   15,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   3,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(168410,  0,       5519,    180,  389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(60049,   150,     65010,   180,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(61630,   150,     65010,   180,  389,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(189949,  500,     58349,   90,   389,  0x0, 0,   7,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(190759,  0,       61840,   45,   389,  0x0, 0,   8,   0,   0,   4,   0,   19,  255,  0)
    DeclNpc(153649,  0,       61220,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(153639,  0,       60250,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(115000,  0,       62779,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(112550,  500,     6699,    0,    389,  0x0, 0,   12,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(112550,  500,     9300,    180,  389,  0x0, 0,   13,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(115000,  0,       8409,    45,   389,  0x0, 0,   14,  0,   0,   5,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(68130,   10,      11650,   1200,    68130,   1500,    11650,   0x007C, 0,  26, 0x0000)
    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  10, 0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  12, 0x0000)
    DeclActor(117500,  0,       4000,    1200,    117500,  650,     4000,    0x007C, 0,  8,  0x0000)
    DeclActor(68130,   10,      11650,   1200,    68130,   1500,    11650,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A0",          # 01, 1
        "Function_2_501",          # 02, 2
        "Function_3_52C",          # 03, 3
        "Function_4_557",          # 04, 4
        "Function_5_582",          # 05, 5
        "Function_6_5AD",          # 06, 6
        "Function_7_735",          # 07, 7
        "Function_8_8DA",          # 08, 8
        "Function_9_986",          # 09, 9
        "Function_10_AD0",         # 0A, 10
        "Function_11_AD4",         # 0B, 11
        "Function_12_1ACF",        # 0C, 12
        "Function_13_1AD3",        # 0D, 13
        "Function_14_2883",        # 0E, 14
        "Function_15_33C3",        # 0F, 15
        "Function_16_3C06",        # 10, 16
        "Function_17_3CEE",        # 11, 17
        "Function_18_3DCF",        # 12, 18
        "Function_19_3E3F",        # 13, 19
        "Function_20_3E90",        # 14, 20
        "Function_21_3EB7",        # 15, 21
        "Function_22_3ED6",        # 16, 22
        "Function_23_3FFD",        # 17, 23
        "Function_24_4078",        # 18, 24
        "Function_25_40D9",        # 19, 25
        "Function_26_40FE",        # 1A, 26
        "Function_27_4133",        # 1B, 27
        "Function_28_4155",        # 1C, 28
        "Function_29_4C7E",        # 1D, 29
        "Function_30_6604",        # 1E, 30
        "Function_31_664F",        # 1F, 31
        "Function_32_6693",        # 20, 32
        "Function_33_66DE",        # 21, 33
        "Function_34_6729",        # 22, 34
        "Function_35_6774",        # 23, 35
        "Function_36_67BF",        # 24, 36
        "Function_37_680A",        # 25, 37
        "Function_38_6855",        # 26, 38
        "Function_39_68A0",        # 27, 39
        "Function_40_68EB",        # 28, 40
        "Function_41_6936",        # 29, 41
        "Function_42_6981",        # 2A, 42
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_428"),
        (1, "loc_434"),
        (2, "loc_440"),
        (3, "loc_44C"),
        (4, "loc_458"),
        (5, "loc_464"),
        (6, "loc_470"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_428")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_434")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_440")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_44C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_458")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_464")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_47C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_488")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_49F")

    Return()

    # Function_0_3F0 end

    def Function_1_4A0(): pass

    label("Function_1_4A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_500")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_4A0")

    label("loc_500")

    Return()

    # Function_1_4A0 end

    def Function_2_501(): pass

    label("Function_2_501")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52B")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_501")

    label("loc_52B")

    Return()

    # Function_2_501 end

    def Function_3_52C(): pass

    label("Function_3_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_556")
    OP_94(0xFE, 0xFAD1, 0x141E, 0x11B66, 0x2652, 0x3E8)
    Sleep(300)
    Jump("Function_3_52C")

    label("loc_556")

    Return()

    # Function_3_52C end

    def Function_4_557(): pass

    label("Function_4_557")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581")
    OP_94(0xFE, 0x2E158, 0xEA92, 0x2F5B2, 0xF604, 0x3E8)
    Sleep(300)
    Jump("Function_4_557")

    label("loc_581")

    Return()

    # Function_4_557 end

    def Function_5_582(): pass

    label("Function_5_582")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AC")
    OP_94(0xFE, 0x1BEC2, 0x1E0A, 0x1C6E2, 0x2AD0, 0x3E8)
    Sleep(300)
    Jump("Function_5_582")

    label("loc_5AC")

    Return()

    # Function_5_582 end

    def Function_6_5AD(): pass

    label("Function_6_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BB")
    Jump("loc_734")

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_624")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jump("loc_734")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_632")
    Jump("loc_734")

    label("loc_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_640")
    Jump("loc_734")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_64E")
    Jump("loc_734")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_65C")
    Jump("loc_734")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_66A")
    Jump("loc_734")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_678")
    Jump("loc_734")

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_696")
    ClearChrFlags(0xC, 0x80)

    label("loc_696")

    Jump("loc_734")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_734")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B7")
    Jump("loc_734")

    label("loc_6B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C5")
    Jump("loc_734")

    label("loc_6C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6FF")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    Jump("loc_734")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_734")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)

    label("loc_734")

    Return()

    # Function_6_5AD end

    def Function_7_735(): pass

    label("Function_7_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_751")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_780")
    Jump("loc_7CF")

    label("loc_780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7CF")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7CF")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FD")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x0, 0x1)

    label("loc_7FD")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82C")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x4, 0x1)

    label("loc_82C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_84B")
    OP_10(0x0, 0x0)
    OP_10(0x12, 0x1)
    OP_10(0x11, 0x0)
    OP_10(0x13, 0x1)
    Jump("loc_857")

    label("loc_84B")

    OP_10(0x0, 0x1)
    OP_10(0x12, 0x0)
    OP_10(0x11, 0x1)
    OP_10(0x13, 0x0)

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_89D")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c0450:Layer15", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D9")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c0450:Layer15", 0x0, 0x1)

    label("loc_8D9")

    Return()

    # Function_7_735 end

    def Function_8_8DA(): pass

    label("Function_8_8DA")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着《美味锅类料理 高压锅篇》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_982")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_982")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『大饱口福锅』\x07\x00",
            "的食谱已经记下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_982")

    TalkEnd(0xFF)
    Return()

    # Function_8_8DA end

    def Function_9_986(): pass

    label("Function_9_986")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D")

    #C0003
    ChrTalk(
        0xC,
        (
            "哦，各位……\x01",
            "还有什么事要找我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xC,
        (
            "我们昆西公司和阿尔摩利卡村\x01",
            "联手推行的『阿尔摩利卡·甜蜜商社』计划\x01",
            "正在逐步进展中。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xC,
        (
            "希望各位也能尽情期待\x01",
            "今后的发展。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_ACC")

    label("loc_A4D")


    #C0006
    ChrTalk(
        0xC,
        (
            "我们昆西公司和阿尔摩利卡村\x01",
            "联手推行的『阿尔摩利卡·甜蜜商社』计划\x01",
            "正在逐步进展中。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "希望各位也能尽情期待\x01",
            "今后的发展。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACC")

    TalkEnd(0xFE)
    Return()

    # Function_9_986 end

    def Function_10_AD0(): pass

    label("Function_10_AD0")

    Call(0, 11)
    Return()

    # Function_10_AD0 end

    def Function_11_AD4(): pass

    label("Function_11_AD4")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CED")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0008
    ChrTalk(
        0xB,
        "啊，各位是警察局的……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00000F嗯，可以向我们说明一下\x01",
            "这里的状况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "嗯，本酒店现在除了\x01",
            "之前来投宿的客人之外，\x01",
            "还接纳了很多避难者。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "食物储备还有一些，\x01",
            "估计可以支撑一个月左右……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "总之，由于目前\x01",
            "无法了解到详细情况，\x01",
            "使大家感到很不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "虽然现在已经把混乱抑制在最低限度了，\x01",
            "但如果这样的状况长期持续下去的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00104F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00001F我们马上就会展开行动，\x01",
            "争取平息目前的事态。\x02\x03",

            "所以请各位暂时留在此地，\x01",
            "继续观望局势。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "嗯，明白了，\x01",
            "请各位多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 6)

    label("loc_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E22")

    #C0017
    ChrTalk(
        0xB,
        "欢迎光临『千禧酒店』。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "呵呵呵，\x01",
            "本酒店会尽力满足\x01",
            "客人们的一切要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "如果有什么需要，\x01",
            "欢迎您随时吩咐。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆住宿\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在普通酒馆可以回复ＣＰ１００，\x01",
            "在高级酒店可以回复ＣＰ２００。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")
    SetScenarioFlags(0x0, 0)

    label("loc_E1F")

    SetScenarioFlags(0x136, 5)

    label("loc_E22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACB")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9C")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AC6")

    label("loc_E9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB0")
    Jump("loc_1AC6")

    label("loc_EB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FAD")

    #C0022
    ChrTalk(
        0xB,
        (
            "在接到总统被拘捕的通知之后，\x01",
            "避难者们已经纷纷\x01",
            "返回自己的家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        (
            "虽然还不了解有关大树的详细情况……\x01",
            "但至少雾气已经散去，\x01",
            "城市总算是恢复了原有的平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "即便如此，\x01",
            "我们还是要趁现在\x01",
            "做好各方面的准备工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_110E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AD")

    #C0025
    ChrTalk(
        0xB,
        (
            "在接到戒严令与禁止外出令的通告之后，\x01",
            "本酒店立刻商讨了\x01",
            "有关收容避难者的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "那种雾气与盔甲士兵的出现\x01",
            "实在是预想之外的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "看样子，大家对总统的不满情绪\x01",
            "已经到了极限……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "但大家现在最主要的\x01",
            "感觉还是不安吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1109")

    label("loc_10AD")


    #C0029
    ChrTalk(
        0xB,
        (
            "看样子，大家对总统的不满情绪\x01",
            "已经到了极限……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "但大家现在最主要的\x01",
            "感觉还是不安吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1109")

    Jump("loc_1AC6")

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_126E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B6")

    #C0031
    ChrTalk(
        0xB,
        (
            "我们已经通过\x01",
            "酒店的导力网络\x01",
            "观看了演说……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "由外国而来\x01",
            "的客人们自然\x01",
            "感到非常震惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xB,
        (
            "要是大家能顺利回到本国，\x01",
            "自然是再好不过……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1269")

    label("loc_11B6")


    #C0034
    ChrTalk(
        0xB,
        (
            "但听说过了今天，\x01",
            "导力铁路就要停止运行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "不管怎么说，总不能告诉客人没有\x01",
            "回国的方法，必须努力为客人想想办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xB,
        (
            "连同飞船的航行状况在内，\x01",
            "我必须要彻底搜集一切情报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1269")

    Jump("loc_1AC6")

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1300")

    #C0037
    ChrTalk(
        0xB,
        (
            "被夕阳与战火染红的欢乐街……\x01",
            "那一天的景象\x01",
            "简直如同噩梦一般。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "……不管怎么说，\x01",
            "现在一定要拼命努力，\x01",
            "争取早日恢复正常生活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_136B")

    #C0039
    ChrTalk(
        0xB,
        (
            "听说警备队的各位\x01",
            "如今仍在玛因兹地区\x01",
            "拼命奋战啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "警备队的各位真是\x01",
            "我们市民的骄傲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1469")

    #C0041
    ChrTalk(
        0xB,
        (
            "受列车事故的影响，\x01",
            "昨天的铁路运行时刻被完全打乱了……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "最后，有些人不得不在\x01",
            "克洛斯贝尔多滞留一天。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "不过，铁路总算在今天早上\x01",
            "完全恢复了，这真是万幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "我们今早已经把那些被迫\x01",
            "滞留在这里的客人们\x01",
            "全部平安送走了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C8")

    label("loc_1469")


    #C0045
    ChrTalk(
        0xB,
        (
            "我们今早已经把那些被迫\x01",
            "滞留在这里的客人们\x01",
            "全部平安送走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "这多亏了警备队\x01",
            "的各位啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C8")

    Jump("loc_1AC6")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1558")

    #C0047
    ChrTalk(
        0xB,
        (
            "据说西克洛斯贝尔街道那边\x01",
            "发生了列车事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "为了不让那些准备在今天\x01",
            "踏上归程的客人陷入惊慌，\x01",
            "必须要收集详细情报啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1621")

    #C0049
    ChrTalk(
        0xB,
        (
            "托各位的福，导力网络上的\x01",
            "预约服务广受好评。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "虽然现在使用它的人\x01",
            "还比较少……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "但我相信，随着导力网络的\x01",
            "不断普及，网络预约的数量\x01",
            "今后一定会超越通讯器的预约数量。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A7")

    label("loc_1621")


    #C0052
    ChrTalk(
        0xB,
        (
            "导力网络的便利之处就在于，\x01",
            "即使是在非接待时间\x01",
            "也可以顺利完成预约。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "和通讯器不同，\x01",
            "每天二十四小时，\x01",
            "随时都可以收发导力邮件。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A7")

    Jump("loc_1AC6")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1718")

    #C0054
    ChrTalk(
        0xB,
        "独立的利弊吗……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "虽然这是个相当复杂的问题，\x01",
            "但我认为听取市民的意见\x01",
            "是非常有意义的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_176C")

    #C0056
    ChrTalk(
        0xB,
        (
            "呵呵呵，正式会议\x01",
            "终于要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "迪塔市长可一定\x01",
            "要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_176C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1810")

    #C0058
    ChrTalk(
        0xB,
        (
            "在我成为这里的经理之前，\x01",
            "本酒店就已拥有接待过\x01",
            "各界要人的成绩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        (
            "这次无法接待各国首脑，\x01",
            "自然是十分遗憾，\x01",
            "希望以后能有机会让他们来这里下榻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_1810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18A8")

    #C0060
    ChrTalk(
        0xB,
        (
            "从明天开始的通商会议\x01",
            "与酒店业也息息相关，\x01",
            "所以我们也十分关注。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "毕竟在会议中所商定的内容\x01",
            "可是会影响到今后来此观光\x01",
            "的游客数量呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC6")

    label("loc_18A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_19CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1936")

    #C0062
    ChrTalk(
        0xB,
        "今天是个雨天呢。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "本酒店可以为您介绍一些\x01",
            "在下雨天也可以\x01",
            "愉快游玩的场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            "如有需要，\x01",
            "请尽管前来咨询。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19C6")

    label("loc_1936")


    #C0065
    ChrTalk(
        0xB,
        (
            "一般来说，就算遇到下雨天，\x01",
            "欢乐街的绝大部分娱乐场所\x01",
            "也是不受影响的。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "不过，如果客人因此而不愿外出，\x01",
            "本酒店也可以提供各种\x01",
            "客房服务哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C6")

    Jump("loc_1AC6")

    label("loc_19CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5B")

    #C0067
    ChrTalk(
        0xB,
        "欢迎光临『千禧酒店』。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "呵呵呵，\x01",
            "本酒店会尽力满足\x01",
            "客人们的一切要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "如果有什么需要，\x01",
            "欢迎您随时吩咐。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AC6")

    label("loc_1A5B")


    #C0070
    ChrTalk(
        0xB,
        (
            "全身美容、室内餐饮、\x01",
            "各种订票服务，\x01",
            "以及导力网络预约服务……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        (
            "本酒店会尽力满足\x01",
            "客人们的一切要求。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC6")

    Jump("loc_E2C")

    label("loc_1ACB")

    TalkEnd(0xB)
    Return()

    # Function_11_AD4 end

    def Function_12_1ACF(): pass

    label("Function_12_1ACF")

    Call(0, 13)
    Return()

    # Function_12_1ACF end

    def Function_13_1AD3(): pass

    label("Function_13_1AD3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BEC")

    #C0072
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "本服务台也受理\x01",
            "当日的住宿预约服务，\x01",
            "如有需要，请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在酒店或酒馆住宿\x01",
            "可以回复ＣＰ。\x02",
        )
    )

    CloseMessageWindow()

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在普通酒馆可以回复ＣＰ１００，\x01",
            "在高级酒店可以回复ＣＰ２００。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x136, 5)

    label("loc_1BEC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C46")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1C46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C66")
    OP_AF(0x45)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_287A")

    label("loc_1C66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C7A")
    Jump("loc_287A")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D5F")

    #C0076
    ChrTalk(
        0x8,
        (
            "遵照经理的指示，\x01",
            "为了预防特殊情况，\x01",
            "将会进一步强化准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "不过，在储备物资方面，\x01",
            "也不能过度抢购\x01",
            "自治州内有限的商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "我们打算和政府商谈，\x01",
            "尽快寻找到\x01",
            "从外国采购物资的手段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287A")

    label("loc_1D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E2C")

    #C0079
    ChrTalk(
        0x8,
        (
            "在雾气出现之后，\x01",
            "有不少人冲进了本酒店，\x01",
            "他们的情绪相当慌乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "在了解到盔甲士兵并没有\x01",
            "袭击过市民之后，\x01",
            "大家稍微平静了一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "但不管怎么说，还是希望\x01",
            "这样的状况能早点平息下来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287A")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9B")

    #C0082
    ChrTalk(
        0x8,
        (
            "……今天早上的演说\x01",
            "真是让我吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "我虽然也能理解\x01",
            "总统的主张，可是……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFD")

    label("loc_1E9B")


    #C0084
    ChrTalk(
        0x8,
        (
            "……嗯，算了，\x01",
            "我也不应该\x01",
            "多说些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "不管怎么说……\x01",
            "暂时也只能继续\x01",
            "观望局势的发展了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFD")

    Jump("loc_287A")

    label("loc_1F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FB8")

    #C0086
    ChrTalk(
        0x8,
        (
            "在发生袭击事件的那天，本酒店\x01",
            "万幸没有遭受到重大损失……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "但彩虹剧团却……\x01",
            "真是太残酷了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "虽然不知道他们有何目的……\x01",
            "但居然做出如此恶行，\x01",
            "实在是不可饶恕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287A")

    label("loc_1FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2043")

    #C0089
    ChrTalk(
        0x8,
        (
            "好像有不少人都怀疑\x01",
            "玛因兹发生的那起事件\x01",
            "是帝国策划的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "如果真的是这样……\x01",
            "那《互不侵犯条约》究竟还有什么意义？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287A")

    label("loc_2043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20FB")

    #C0091
    ChrTalk(
        0x8,
        (
            "受昨天那起事故的影响，\x01",
            "我们接到了很多要求\x01",
            "取消住宿预约的联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "对我们来说，横贯大陆铁道简直就\x01",
            "如同生命线一般……\x01",
            "能将损害抑制在最小限度，总算是让人松了口气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287A")

    label("loc_20FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2165")

    #C0093
    ChrTalk(
        0x8,
        "唔，列车事故吗……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "这在克洛斯贝尔\x01",
            "还是比较罕见的……\x01",
            "事故发生的原因究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287A")

    label("loc_2165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220B")

    #C0095
    ChrTalk(
        0x8,
        (
            "德莉丝小姐的工作能力\x01",
            "在最近有了很大提高。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "扫除的能力自不必说，\x01",
            "客人们对她的评价也很不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "这也多亏了\x01",
            "亚伦先生的耐心指导啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2261")

    label("loc_220B")


    #C0098
    ChrTalk(
        0x8,
        (
            "德莉丝小姐的工作能力\x01",
            "在最近有了很大提高。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "这也多亏了\x01",
            "亚伦先生的耐心指导啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2261")

    Jump("loc_287A")

    label("loc_2266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2348")

    #C0100
    ChrTalk(
        0x8,
        (
            "我是克洛斯贝尔人，\x01",
            "但以前曾在帝国的酒店\x01",
            "工作过一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "这样说可能有些不妥当，\x01",
            "但我在帝国工作的时候，\x01",
            "都快被那些贵族折磨到精神崩溃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "自从来到这里之后，\x01",
            "工作时的心情真是轻松愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23D1")

    label("loc_2348")


    #C0103
    ChrTalk(
        0x8,
        (
            "在帝国的酒店可以学习到\x01",
            "很不错的服务技术，\x01",
            "但在那里工作，精神上也是相当疲劳的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "自从来到这里之后，\x01",
            "工作时的心情真是轻松愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D1")

    Jump("loc_287A")

    label("loc_23D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2483")

    #C0105
    ChrTalk(
        0x8,
        (
            "我昨天下班回家时，\x01",
            "远远地眺望了一下\x01",
            "兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "哎呀呀，真是比传闻中更有\x01",
            "压迫感啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "下次一定要走到那附近，\x01",
            "体验一下仰望大楼的感觉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F3")

    label("loc_2483")


    #C0108
    ChrTalk(
        0x8,
        (
            "只是远远望了一眼，就被兰花塔\x01",
            "那雄伟的压迫感所折服了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "下次一定要走到那附近，\x01",
            "体验一下仰望大楼的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F3")

    Jump("loc_287A")

    label("loc_24F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2594")

    #C0110
    ChrTalk(
        0x8,
        (
            "客人，您去观看\x01",
            "揭幕式了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "据说当时还放了烟花，\x01",
            "是一场很有观赏价值的仪式呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "兰花塔的威容……\x01",
            "我也想尽快一见啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25EE")

    label("loc_2594")


    #C0113
    ChrTalk(
        0x8,
        (
            "据说在揭幕式上还放了烟花，\x01",
            "很有观赏价值呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "兰花塔的威容……\x01",
            "我也想尽快一见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25EE")

    Jump("loc_287A")

    label("loc_25F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A9")

    #C0115
    ChrTalk(
        0x8,
        (
            "欢迎光临，\x01",
            "今天的天气也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "虽然有警察在\x01",
            "市里巡逻，\x01",
            "但仍是个观光的好日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "如果您正在寻找观光景点，\x01",
            "我可以根据您的要求\x01",
            "提供一些建议哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2710")

    label("loc_26A9")


    #C0118
    ChrTalk(
        0x8,
        (
            "欢迎光临，\x01",
            "今天的天气也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "如果您正在寻找观光景点，\x01",
            "我可以根据您的要求\x01",
            "提供一些建议哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2710")

    Jump("loc_287A")

    label("loc_2715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_280E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A9")

    #C0120
    ChrTalk(
        0x8,
        (
            "早上好，\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "如果您想在下雨天外出，\x01",
            "只要来这里说一声，\x01",
            "我们就可以提供雨伞。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        "请不必客气，尽管索要。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2809")

    label("loc_27A9")


    #C0123
    ChrTalk(
        0x8,
        (
            "如果您想在下雨天外出，\x01",
            "只要来这里说一声，\x01",
            "我们就可以提供雨伞。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        "请不必客气，尽管索要。\x02",
    )

    CloseMessageWindow()

    label("loc_2809")

    Jump("loc_287A")

    label("loc_280E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_287A")

    #C0125
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎光临『千禧酒店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "本服务台也受理\x01",
            "当日的住宿预约服务，\x01",
            "如有需要，请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287A")

    Jump("loc_1BF6")

    label("loc_287F")

    TalkEnd(0x8)
    Return()

    # Function_13_1AD3 end

    def Function_14_2883(): pass

    label("Function_14_2883")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_292C")

    #C0127
    ChrTalk(
        0xFE,
        (
            "雷缇希亚经理刚才表示，\x01",
            "准备暂时采取无视\x01",
            "盈利状况的营业方式。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "如今是整个克洛斯贝尔的困难时期……\x01",
            "我也要活用至今积累的一切经验，\x01",
            "全力协助经理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_292C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_29B7")

    #C0129
    ChrTalk(
        0xFE,
        (
            "通过酒店这次的无偿提供措施，\x01",
            "我发现在经理的眼里，\x01",
            "人远比金钱更重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "能在这样的人手下工作，\x01",
            "真是一件很幸福的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_29B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A75")

    #C0131
    ChrTalk(
        0xFE,
        (
            "自从独立宣言发表之后，\x01",
            "客人的数量就一天比一天少……\x01",
            "而今天早上的演说更是起到了决定性的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "虽然在这种时候说这些不太合适……\x01",
            "不过，本酒店也只能\x01",
            "重新制定经营方针了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B26")

    #C0133
    ChrTalk(
        0xFE,
        (
            "袭击事件给城市留下的\x01",
            "创伤实在是相当大。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "警备队遭到重创，\x01",
            "连伊莉娅小姐都……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "绝不能再让这样的事情\x01",
            "发生第二次……\x01",
            "这是我现在唯一的想法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B8F")

    label("loc_2B26")


    #C0136
    ChrTalk(
        0xFE,
        (
            "警备队遭到重创，\x01",
            "连伊莉娅小姐都……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "绝不能再让这样的事情\x01",
            "发生第二次……\x01",
            "这是我现在唯一的想法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8F")

    Jump("loc_33BF")

    label("loc_2B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2BF9")

    #C0138
    ChrTalk(
        0xFE,
        (
            "昨天发生的袭击事件……\x01",
            "似乎仍然没有\x01",
            "平息的迹象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "真是很担心\x01",
            "玛因兹的居民。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_2BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C8E")

    #C0140
    ChrTalk(
        0xFE,
        (
            "听说脱轨事故是\x01",
            "一只不可思议的魔兽造成的……\x01",
            "这传闻真是让人不安啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "真是不愿意这样去想，\x01",
            "但这该不会是什么不详之事的前兆吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_2C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D2B")

    #C0142
    ChrTalk(
        0xFE,
        (
            "已经快要到预约的客人\x01",
            "前来登记的时间了，可现在却……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "看来列车事故造成的影响\x01",
            "这么快就开始显现了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "但愿大家都能\x01",
            "平安抵达这里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DA1")

    #C0145
    ChrTalk(
        0xFE,
        (
            "在这段时期，\x01",
            "豪华套间无人居住\x01",
            "并不是很少见的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "也就是说，\x01",
            "如果想住住看，\x01",
            "现在正是好机会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E94")

    #C0147
    ChrTalk(
        0xFE,
        (
            "说到独立问题的利弊……\x01",
            "虽然赞同独立的意见占多数，\x01",
            "但还是存在各种不同观点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "像我这种上了年纪的人，\x01",
            "只会考虑到\x01",
            "两大国的威胁……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "但和本酒店一样，\x01",
            "克洛斯贝尔自治州如今似乎\x01",
            "也到了必须要有所改变的时期了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F1A")

    label("loc_2E94")


    #C0150
    ChrTalk(
        0xFE,
        (
            "像我这种上了年纪的人，\x01",
            "只会考虑到\x01",
            "两大国的威胁……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "但和本酒店一样，\x01",
            "克洛斯贝尔自治州如今似乎\x01",
            "也到了必须要有所改变的时期了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1A")

    Jump("loc_33BF")

    label("loc_2F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F94")

    #C0152
    ChrTalk(
        0xFE,
        (
            "通商会议的正式会议\x01",
            "终于要正式开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "哎呀呀，\x01",
            "真是太期待迪塔市长\x01",
            "和麦克道尔议长的表现了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_2F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_300C")

    #C0154
    ChrTalk(
        0xFE,
        (
            "听说兰花塔内的所有楼层\x01",
            "都连接了导力网络。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "呵呵，本酒店的导力网络预约服务\x01",
            "大概也会越来越火爆了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BF")

    label("loc_300C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_313B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B3")

    #C0156
    ChrTalk(
        0xFE,
        (
            "德莉丝小姐在不久之前\x01",
            "还有些靠不住，\x01",
            "但最近却让人放心多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "对担任教导工作的人而言，\x01",
            "再没有比切身感受到后辈成长\x01",
            "更加开心的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3136")

    label("loc_30B3")


    #C0158
    ChrTalk(
        0xFE,
        (
            "德莉丝小姐能有如此明显的成长，\x01",
            "我真是感到很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "对担任教导工作的人而言，\x01",
            "再没有比切身感受到后辈成长\x01",
            "更加开心的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3136")

    Jump("loc_33BF")

    label("loc_313B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_329B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321E")

    #C0160
    ChrTalk(
        0xFE,
        (
            "虽然现在并没有纪念庆典时那么热闹，\x01",
            "但前来光顾本酒店的客人\x01",
            "一直在逐渐增多。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "经理花费大量精力而推出的导力网络\x01",
            "预约系统也获得了很不错的反响……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "哎呀呀，『千禧酒店』的未来\x01",
            "真是一片光明呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3296")

    label("loc_321E")


    #C0163
    ChrTalk(
        0xFE,
        (
            "传统与革新的融合……\x01",
            "这是雷缇希亚经理\x01",
            "经营本酒店的理念。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "我在最初也感到有些困惑，\x01",
            "但如今已经\x01",
            "彻底信赖经理了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3296")

    Jump("loc_33BF")

    label("loc_329B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334C")

    #C0165
    ChrTalk(
        0xFE,
        (
            "今年是本酒店开业６０周年……\x01",
            "顺便一说，我在这里工作\x01",
            "已经超过３０年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "不知不觉间，就变成这里最老的员工了。\x01",
            "哎呀呀，时光的流逝\x01",
            "真是太快了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33BF")

    label("loc_334C")


    #C0167
    ChrTalk(
        0xFE,
        (
            "我在这家酒店\x01",
            "已经工作３０年以上了。\x01",
            "不知不觉间，就变成这里最老的员工了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "哎呀呀，时光的流逝\x01",
            "真是太快了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BF")

    TalkEnd(0xFE)
    Return()

    # Function_14_2883 end

    def Function_15_33C3(): pass

    label("Function_15_33C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3445")

    #C0169
    ChrTalk(
        0xFE,
        (
            "总算已经把全部避难者都\x01",
            "安全送走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "虽然处在这种特殊状况下……\x01",
            "但在接受大家的谢意时，\x01",
            "真是感到很高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_34C8")

    #C0171
    ChrTalk(
        0xFE,
        (
            "先不说现在的状况……\x01",
            "酒店还真是很久都没有\x01",
            "繁忙到这种程度了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "身为千禧酒店的一员，\x01",
            "我一定会全力为大家服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_34C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3554")

    #C0173
    ChrTalk(
        0xFE,
        (
            "我虽然并没有\x01",
            "完全理解如今的事态……\x01",
            "但现在的心情实在是非常复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "我们的确通过投票\x01",
            "而赞成了独立意见……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35AF")

    label("loc_3554")


    #C0175
    ChrTalk(
        0xFE,
        (
            "……只要一闲下来，就会不由自主地\x01",
            "胡思乱想，这可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        "好了……必须要努力工作。\x02",
    )

    CloseMessageWindow()

    label("loc_35AF")

    Jump("loc_3C02")

    label("loc_35B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3695")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35E6")
    Call(0, 42)
    Return()

    label("loc_35E6")


    #C0177
    ChrTalk(
        0xFE,
        (
            "魔兽的咆哮声、枪击的声音，\x01",
            "还有警备队员的怒吼与惨叫……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "……直到现在，每当回想起袭击那天\x01",
            "的景象时，我仍然止不住颤抖……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "为什么这座城市会遭遇到这种事情……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36E0")

    #C0180
    ChrTalk(
        0xFE,
        (
            "玛因兹的事件……\x01",
            "真是很惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        "希望能尽早解决……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_36E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3766")

    #C0182
    ChrTalk(
        0xFE,
        (
            "听说昨天的列车事故\x01",
            "使很多人负伤，\x01",
            "但幸好无人遇难。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "不过，其中有些人\x01",
            "伤得非常重……\x01",
            "总之，希望他们能早点恢复。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_37B7")

    #C0184
    ChrTalk(
        0xFE,
        (
            "竟然发生了列车事故……\x01",
            "真是可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        "……好担心那些乘客。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382B")

    #C0186
    ChrTalk(
        0xFE,
        "好了，今天也要努力工作。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "哦，对了，在客人面前，\x01",
            "一定不能忘记面带微笑。（微笑）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3894")

    label("loc_382B")


    #C0188
    ChrTalk(
        0xFE,
        (
            "为了他人而努力劳动\x01",
            "的感觉真好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "在这种时候，可以充分感觉到\x01",
            "自己是被别人需要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3894")

    Jump("loc_3C02")

    label("loc_3899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3909")

    #C0190
    ChrTalk(
        0xFE,
        (
            "彩虹剧团新版舞剧\x01",
            "的公演日终于已经\x01",
            "临近了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "虽然想尽办法\x01",
            "也买不到票，\x01",
            "但还是很期待呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A3")

    #C0192
    ChrTalk(
        0xFE,
        (
            "客人，您去过『时代』百货店的\x01",
            "楼顶了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "听说那里是眺望\x01",
            "兰花塔的绝佳观景地点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "如果还没有去过，\x01",
            "就去看看如何？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A00")

    label("loc_39A3")


    #C0195
    ChrTalk(
        0xFE,
        (
            "听说『时代』百货店的楼顶\x01",
            "是眺望兰花塔的\x01",
            "绝佳观景地点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "客人，您也过去\x01",
            "看看如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A00")

    Jump("loc_3C02")

    label("loc_3A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A9F")

    #C0197
    ChrTalk(
        0xFE,
        (
            "在揭幕式结束之后，\x01",
            "众位首脑好像要\x01",
            "分别前往不同场所访问。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "要是能在什么地方见到\x01",
            "他们就好了……\x01",
            "不过安保措施很严密，恐怕很难见到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B1B")

    #C0199
    ChrTalk(
        0xFE,
        (
            "我最近已经很少被\x01",
            "亚伦先生斥责了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "这是否说明我有所成长了呢？\x01",
            "呵呵，如果真是如此，实在是让人高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3BA7")

    #C0201
    ChrTalk(
        0xFE,
        (
            "在下雨天，\x01",
            "鞋底肯定会沾上泥污，\x01",
            "所以打扫地毯非常费力。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "不过，只要看看那些\x01",
            "已经打扫干净的部分，\x01",
            "就会感觉相当爽快呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C02")

    label("loc_3BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C02")

    #C0203
    ChrTalk(
        0xFE,
        (
            "早上好，\x01",
            "您是前来住宿的客人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "在外出的时候，\x01",
            "请不要忘记给房门上锁哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C02")

    TalkEnd(0xFE)
    Return()

    # Function_15_33C3 end

    def Function_16_3C06(): pass

    label("Function_16_3C06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C77")

    #C0205
    ChrTalk(
        0xFE,
        "唔，今天要如何度过呢？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "听从经理的建议，\x01",
            "充分享受一下酒店的服务，\x01",
            "说不定也会很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEA")

    label("loc_3C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3CEA")

    #C0207
    ChrTalk(
        0xFE,
        (
            "这家酒店不仅房间无可挑剔，\x01",
            "服务也是一流的。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "嗯，今后再来克洛斯贝尔旅行的时候，\x01",
            "还要在这里住宿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CEA")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C06 end

    def Function_17_3CEE(): pass

    label("Function_17_3CEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D4B")

    #C0209
    ChrTalk(
        0xFE,
        (
            "呵呵，在酒店里度过\x01",
            "一天确实也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "虽然我还是很想\x01",
            "去巴鲁卡玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DCB")

    label("loc_3D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3DCB")

    #C0211
    ChrTalk(
        0xFE,
        (
            "呵呵，我这次是乘坐\x01",
            "导力列车来的，\x01",
            "不过旅途的疲惫已经完全消除了。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "虽然这里的费用有点高，\x01",
            "但确实是物超所值呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DCB")

    TalkEnd(0xFE)
    Return()

    # Function_17_3CEE end

    def Function_18_3DCF(): pass

    label("Function_18_3DCF")

    TalkBegin(0xFE)

    #C0213
    ChrTalk(
        0xFE,
        (
            "我和妹妹在回家的途中\x01",
            "突然被雾气所笼罩，\x01",
            "于是就跑进这家酒店避难。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "……真有点\x01",
            "死里逃生的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3DCF end

    def Function_19_3E3F(): pass

    label("Function_19_3E3F")

    TalkBegin(0xFE)

    #C0215
    ChrTalk(
        0xFE,
        (
            "在出现雾气的时候，\x01",
            "哥哥把我背在身上\x01",
            "拼命跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "嘿嘿嘿，哥哥好帅⊥\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3E3F end

    def Function_20_3E90(): pass

    label("Function_20_3E90")

    TalkBegin(0xFE)

    #C0217
    ChrTalk(
        0xFE,
        "大家现在都很担心我们吧……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3E90 end

    def Function_21_3EB7(): pass

    label("Function_21_3EB7")

    TalkBegin(0xFE)

    #C0218
    ChrTalk(
        0xFE,
        "真想早点回家啊……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3EB7 end

    def Function_22_3ED6(): pass

    label("Function_22_3ED6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9F")

    #C0219
    ChrTalk(
        0xFE,
        (
            "可以保卫城市的结界\x01",
            "怎么不见了……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "还有，那种恐怖的怪物\x01",
            "究竟是什么东西……！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "我只是没有在总统发表演说的那天\x01",
            "及时回国，结果就落得这种下场……\x01",
            "这未免也太过分了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3FF9")

    label("loc_3F9F")


    #C0222
    ChrTalk(
        0xFE,
        (
            "我只是没有在总统发表演说的那天\x01",
            "及时回国，结果就落得这种下场……\x01",
            "这未免也太过分了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF9")

    TalkEnd(0xFE)
    Return()

    # Function_22_3ED6 end

    def Function_23_3FFD(): pass

    label("Function_23_3FFD")

    TalkBegin(0xFE)

    #C0223
    ChrTalk(
        0xFE,
        (
            "要是早知道会变成这样，\x01",
            "我一定会在第一时间\x01",
            "回家的……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "算了，能免费住在\x01",
            "这么棒的房间里，\x01",
            "倒也真是很幸运呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_3FFD end

    def Function_24_4078(): pass

    label("Function_24_4078")

    TalkBegin(0xFE)

    #C0225
    ChrTalk(
        0xFE,
        (
            "能在酒店中避难\x01",
            "可真是不幸中的万幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "不过……\x01",
            "这种状况究竟会持续到什么时候呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4078 end

    def Function_25_40D9(): pass

    label("Function_25_40D9")

    TalkBegin(0xFE)

    #C0227
    ChrTalk(
        0xFE,
        "嘿嘿嘿，这个房间好大啊¤\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_40D9 end

    def Function_26_40FE(): pass

    label("Function_26_40FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4132")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 6)), scpexpr(EXPR_END)), "loc_412F")
    Call(0, 29)
    Jump("loc_4132")

    label("loc_412F")

    Call(0, 28)

    label("loc_4132")

    Return()

    # Function_26_40FE end

    def Function_27_4133(): pass

    label("Function_27_4133")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_27_4133 end

    def Function_28_4155(): pass

    label("Function_28_4155")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    LoadChrToIndex("chr/ch32300.itc", 0x1E)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 68000, 0, 12400, 315)
    OP_68(68140, 1500, 9270, 0)
    MoveCamera(312, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21270, 0)
    SetChrPos(0x101, 67400, 0, 9530, 0)
    SetChrPos(0x102, 68780, 0, 9180, 0)
    SetChrPos(0x103, 66670, 0, 8520, 0)
    SetChrPos(0x104, 68370, 0, 8240, 0)
    SetChrPos(0x109, 67410, 0, 7270, 0)
    SetChrPos(0x105, 69430, 0, 7040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0229
    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──嗯，那就明天见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x17,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今后也请多多关照啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x17, 68000, 0, 13400, 315)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)

    def lambda_433A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_433A)

    def lambda_434B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF79A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_434B)
    WaitChrThread(0x17, 1)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sound(104, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0231
    ChrTalk(
        0x17,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00000F那个……打扰一下。\x02\x03",

            "您是阿尔摩利卡村的\x01",
            "迪利克先生吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x17,
        (
            "嗯，正是……\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，没有及时表明身份……\x01",
            "我们是警察局特别任务支援科的成员。\x02\x03",

            "可以询问您几句话吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    #C0235
    ChrTalk(
        0x17,
        "……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x17,
        (
            "你们是村长……\x01",
            "是我爸爸派来的帮手吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x17,
        (
            "竟然把警察都叫来了……\x01",
            "哼，他可真是不嫌累啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        "#00105F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x17,
        (
            "……我了解你们的来意。\x01",
            "你们是想调查\x01",
            "我最近的行动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x17,
        (
            "我并没做什么\x01",
            "见不得光的事情，\x01",
            "有什么问题就尽管问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x105,
        "#10303F（唔……这种反应倒是让人意外啊。）\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00003F……那我就开门见山地直接问了。\x02\x03",

            "#00001F听说您最近与一位\x01",
            "名叫敏涅斯的先生\x01",
            "有所来往……\x02\x03",

            "请问你们究竟要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x17,
        (
            "……呼，也罢。\x01",
            "事到如今，就算告诉你们，\x01",
            "我爸爸也已经无计可施了。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x17,
        (
            "从不久前开始，我请敏涅斯先生\x01",
            "帮忙推行一项计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x17,
        "计划的主要内容就是村子的改革。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0246
    ChrTalk(
        0x109,
        "#10105F村、村子的改革吗……？\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00005F那、那么重要的事情，\x01",
            "竟然瞒着村长\x01",
            "进行吗？\x02\x03",

            "#00006F再怎么说，\x01",
            "这也不太好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x17,
        (
            "我至今为止，已经和村长……\x01",
            "和我爸爸商量过很多次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x17,
        (
            "但他的回答永远都是\x01",
            "『不能迷失村子应有的状态』或\x01",
            "『不能太过激进地求变』……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x17,
        (
            "可是，如果就这么维持现状，\x01",
            "我并不认为那种乡下村落\x01",
            "有未来可言。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x17,
        (
            "为了让村子存续发展，\x01",
            "改革绝对是必要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x17,
        (
            "但我爸爸却始终\x01",
            "都不明白这一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#00203F原来如此……\x01",
            "在这种情况下，您结识了\x01",
            "那位名叫敏涅斯的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x17,
        (
            "……他和爸爸不同，\x01",
            "会认真与我交流。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x17,
        (
            "而且还帮我发现了\x01",
            "阿尔摩利卡村养蜂业\x01",
            "的巨大发展前途。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x17,
        (
            "我计划与他合作，\x01",
            "在近期展开一项\x01",
            "大事业。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        (
            "#00306F该、该说什么好呢，\x01",
            "真是很让人吃惊啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x17,
        (
            "哼……\x01",
            "我要说的就是这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x17,
        (
            "已经够了吧？\x01",
            "我差不多也该回村子了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A46():
        OP_95(0xFE, 74620, 0, 5690, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A46)
    Sleep(2000)

    def lambda_4A63():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A63)
    Sleep(50)

    def lambda_4A73():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A73)
    Sleep(50)

    def lambda_4A83():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A83)
    Sleep(50)

    def lambda_4A93():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4A93)
    Sleep(50)

    def lambda_4AA3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4AA3)
    Sleep(50)

    def lambda_4AB3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4AB3)
    WaitChrThread(0x17, 1)
    SetChrFlags(0x17, 0x80)
    OP_0D()

    #C0260
    ChrTalk(
        0x102,
        "#00105F啊……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x109,
        "#10106F他走了……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_68(68210, 1500, 8580, 2000)
    OP_6F(0x1)

    #C0262
    ChrTalk(
        0x101,
        (
            "#00003F总之……\x01",
            "既然已经来酒店了。\x02\x03",

            "#00000F接下来，\x01",
            "我们也去和那位名叫\x01",
            "敏涅斯的男人当面谈谈吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4B84():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B84)
    Sleep(50)

    def lambda_4B94():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4B94)
    Sleep(50)

    def lambda_4BA4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4BA4)
    Sleep(50)

    def lambda_4BB4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4BB4)
    Sleep(50)

    def lambda_4BC4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4BC4)

    #C0263
    ChrTalk(
        0x104,
        (
            "#00303F有道理……\x01",
            "说不定能了解到不少内情呢。\x02\x03",

            "#00300F好，那我们就\x01",
            "赶快行动吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 6)
    OP_29(0x82, 0x1, 0x6)
    OP_D7(0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 50740, 0, 9750, 90)
    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0x0, 68510, 0, 9710, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_28_4155 end

    def Function_29_4C7E(): pass

    label("Function_29_4C7E")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    OP_4B(0xC, 0xFF)
    OP_68(68560, 1500, 10330, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20260, 0)
    SetChrPos(0x101, 67900, 0, 11200, 0)
    SetChrPos(0x102, 69690, 0, 9980, 315)
    SetChrPos(0x103, 66720, 0, 10430, 45)
    SetChrPos(0x104, 68370, 0, 9740, 0)
    SetChrPos(0x109, 67410, 0, 8770, 0)
    SetChrPos(0x105, 69430, 0, 8540, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00001F那么……\x01",
            "我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("中年人的声音")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊……\x01",
            "是哪位？\x02\x03",

            "我好像并没有\x01",
            "要求送餐……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00000F您就是敏涅斯先生吧……？\x02\x03",

            "#00004F突然打扰，实在是不好意思。\x01",
            "我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "#00000F我们有两三个问题想问问您，\x01",
            "不知可否……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("中年人的声音")

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎呀呀，\x01",
            "警察竟然特意……\x02\x03",

            "既然如此，\x01",
            "那就请进吧。\x01",
            "门没有锁。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x104,
        (
            "#00305F（竟、竟然这么爽快\x01",
            "  就让我们进去了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        (
            "#00003F（对方的精明程度说不定\x01",
            "  在我们的预想之上……）\x02\x03",

            "#00005F嗯……\x01",
            "那我们就打扰了。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    OP_68(169250, 1500, 2800, 0)
    MoveCamera(311, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19200, 0)
    SetChrPos(0xC, 168410, 0, 5520, 180)
    SetChrPos(0x101, 168960, 0, -2080, 0)
    SetChrPos(0x102, 168960, 0, -2080, 0)
    SetChrPos(0x103, 168960, 0, -2080, 0)
    SetChrPos(0x104, 168960, 0, -2080, 0)
    SetChrPos(0x109, 168960, 0, -2080, 0)
    SetChrPos(0x105, 168960, 0, -2080, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_68(169610, 1500, 3430, 3000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 34)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 35)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)

    #C0270
    ChrTalk(
        0xC,
        (
            "#11P初次见面，\x01",
            "我就是敏涅斯……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xC,
        (
            "#11P各位今天\x01",
            "有何贵干？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#00003F如刚才所说……\x01",
            "我们有几个问题\x01",
            "想问您。\x02\x03",

            "#00001F可以配合一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xC,
        (
            "#11P当然没问题。\x01",
            "只要我能帮得上忙，一定会全力配合……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "#11P怎么回事，莫非这一带\x01",
            "发生什么事件了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        (
            "#00003F不……\x01",
            "我们想问的问题\x01",
            "是关于您的。\x02\x03",

            "您的身份是什么，\x01",
            "在阿尔摩利卡村\x01",
            "准备做些什么……\x02\x03",

            "#00001F以上问题，还请您做个说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xC,
        "#11P哦……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0277
    ChrTalk(
        0xC,
        (
            "#11P呼，好吧。\x01",
            "这种事情，告诉你们也无所谓。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0278
    ChrTalk(
        0xC,
        (
            "#11P咳咳……我是在某家公司中\x01",
            "任职的董事。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "#11P工作内容从商品开发到具体营业，\x01",
            "负责范围比较广泛。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xC,
        (
            "#11P至于我前往阿尔摩利卡村，是因为本公司……\x01",
            "『昆西公司』准备开展一项重要的业务，\x01",
            "所以派我前来访问。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x102,
        (
            "#00105F什……什么！\x01",
            "是昆西公司吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53A8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53A8)
    Sleep(50)

    def lambda_53B8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_53B8)
    Sleep(50)

    def lambda_53C8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53C8)
    Sleep(50)

    def lambda_53D8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_53D8)
    Sleep(300)

    #C0282
    ChrTalk(
        0x104,
        (
            "#00305F我还是第一次听到这名字……\x01",
            "大小姐知道这公司吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    Sleep(300)

    #C0283
    ChrTalk(
        0x102,
        (
            "#00105F嗯……昆西公司是\x01",
            "外国一家著名的糕点制造公司。\x02\x03",

            "#00104F在糕点制造业内是个相当大的企业，\x01",
            "克洛斯贝尔也进口了\x01",
            "它的商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00005F哦，这么一说，\x01",
            "我小时候好像经常买\x01",
            "这个牌子的巧克力吃呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#00303F唔……我一般都不太\x01",
            "注意品牌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        (
            "#11P呵呵，这也是\x01",
            "可以理解的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5545():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5545)
    Sleep(50)

    def lambda_5555():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5555)
    Sleep(50)

    def lambda_5565():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5565)
    Sleep(50)

    def lambda_5575():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5575)
    Sleep(50)

    def lambda_5585():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5585)
    Sleep(300)

    #C0287
    ChrTalk(
        0xC,
        (
            "#11P说起来，虽然我现在从事着\x01",
            "这种职业，但我其实很讨厌甜食，\x01",
            "以前从来都不沾这些东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xC,
        (
            "#11P不过，由于我常年在营业工作中\x01",
            "表现突出，能力得到了认可，\x01",
            "所以才有了如今的地位……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        (
            "#11P……哦，一不小心，\x01",
            "好像把话题扯远了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#00005F啊……哪、哪里。\x01",
            "是我们打断您了，不好意思。\x02\x03",

            "#00003F……咳咳。\x01",
            "您之前好像说到了在\x01",
            "阿尔摩利卡村的『业务』吧？\x02\x03",

            "#00001F那项『业务』……\x01",
            "就是与村长的儿子\x01",
            "迪利克先生商讨的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x102,
        (
            "#00100F听说与村子的发展\x01",
            "息息相关……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "#11P啊……\x01",
            "原来你们都知道这么多了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xC,
        (
            "#11P唔，既然迪利克先生\x01",
            "已经将情报吐露了，\x01",
            "我就没必要隐瞒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xC,
        (
            "#11P呵呵，我确实和他\x01",
            "缔结了友好关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x103,
        "#00203F果然如此……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#00001F可以将详情透露给我们吗？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        "#11P呵呵，好吧。\x02",
    )

    CloseMessageWindow()
    OP_68(167980, 1500, 3640, 3000)

    def lambda_585D():
        OP_95(0xFE, 164960, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_585D)
    Sleep(500)

    def lambda_587A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_587A)
    Sleep(50)

    def lambda_588A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_588A)
    Sleep(50)

    def lambda_589A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_589A)
    Sleep(50)

    def lambda_58AA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58AA)
    Sleep(50)

    def lambda_58BA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_58BA)
    Sleep(50)

    def lambda_58CA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58CA)
    WaitChrThread(0xC, 1)
    OP_6F(0x1)

    #C0298
    ChrTalk(
        0xC,
        (
            "#5P我们昆西公司\x01",
            "为了糕点制造业的未来，\x01",
            "一直都在不断钻研。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xC,
        (
            "#5P而我则肩负着公司\x01",
            "所赋予的某项使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xC,
        (
            "#5P这项使命就是\x01",
            "在克洛斯贝尔寻找立足点，\x01",
            "使昆西公司进驻此地。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#00105F也就是说……\x01",
            "昆西公司要在克洛斯贝尔\x01",
            "成立子公司吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xC,
        "#5P呵呵，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xC,
        (
            "#5P随后，就在我进入市内的百货店，\x01",
            "开始寻找启发时……\x01",
            "我发现了一件很不错的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xC,
        (
            "#5P那就是出产自阿尔摩利卡村，\x01",
            "品质极其优秀的『蜂蜜』。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x109,
        (
            "#10100F蜂蜜……在阿尔摩利卡村\x01",
            "的花田中酿造的蜂蜜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00003F连哈罗德先生都对其\x01",
            "品质予以肯定……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(169610, 1500, 3430, 3000)

    def lambda_5AEF():
        OP_95(0xFE, 168410, 0, 5520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5AEF)
    Sleep(500)

    def lambda_5B0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B0C)
    Sleep(50)

    def lambda_5B1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B1C)
    Sleep(50)

    def lambda_5B2C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B2C)
    Sleep(50)

    def lambda_5B3C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B3C)
    Sleep(50)

    def lambda_5B4C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B4C)
    Sleep(50)

    def lambda_5B5C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B5C)
    WaitChrThread(0xC, 1)

    def lambda_5B6D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5B6D)
    OP_6F(0x1)
    Sleep(300)

    #C0307
    ChrTalk(
        0xC,
        (
            "#11P富饶的天然之地，\x01",
            "世代相传的花田……\x01",
            "蜂蜜就是出产自这样的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xC,
        (
            "#11P在看到村中环境的第一眼之后，\x01",
            "我就像接到了上天启示一般，脑海中立刻\x01",
            "浮现了一项创立全新糕点制造品牌的计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xC,
        (
            "#11P它的名字就是……\x01",
            "『阿尔摩利卡·甜蜜商社』计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        "#10105F阿尔摩利卡·甜蜜商社……\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x104,
        "#00306F听、听起来好像很厉害啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0312
    ChrTalk(
        0xC,
        (
            "#11P简单来说，也就是大量使用\x01",
            "阿尔摩利卡村出产的蜂蜜，\x01",
            "用于制造糕点。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xC,
        (
            "#11P不过，如果想实现这项计划，\x01",
            "当地村民的协助\x01",
            "是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xC,
        (
            "#11P所以我就向阿尔摩利卡村\x01",
            "的下任村长迪利克先生\x01",
            "介绍了这项计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xC,
        (
            "#11P询问他是否愿意建造糕点制造工厂，\x01",
            "并经营这家新公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00005F让迪利克先生\x01",
            "经营昆西公司的子公司……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        (
            "#11P至于相关的专业知识，以及销售渠道，\x01",
            "本公司均会提供支援。而花田则会由\x01",
            "我们的工作人员负责管理……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xC,
        (
            "#11P我提出的条件不会给村民带来任何麻烦，\x01",
            "而且还可以使村民们\x01",
            "的辛劳程度明显降低。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        (
            "#00105F不过，说到工厂……\x01",
            "您准备建造在\x01",
            "什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xC,
        (
            "#11P经过我们这段时间的探讨，\x01",
            "准备借用\x01",
            "村子的那片私有地。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xC,
        (
            "#11P那片土地原本也只是\x01",
            "用于放置杂物，\x01",
            "所以迪利克先生爽快地答应了我的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x105,
        (
            "#10304F条件如此有诱惑力，\x01",
            "对方会答应下来\x01",
            "也不足为奇。\x02\x03",

            "迪利克一直希望村子改革，\x01",
            "就更是不会拒绝了……\x02\x03",

            "#10302F这项计划对您与\x01",
            "迪利克双方而言，\x01",
            "都是一件好事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xC,
        "#11P呵呵，没错。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xC,
        (
            "#11P他有着出众的才能与强烈的责任感，\x01",
            "也值得我与之合作。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "#11P……呵呵，我要说的就是这些了。\x01",
            "各位已经理解了吧？\x02",
        )
    )

    CloseMessageWindow()
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

    #C0326
    ChrTalk(
        0x101,
        (
            "#00003F……感谢您\x01",
            "和我们说了这么多。\x02\x03",

            "#00000F听了您的介绍，\x01",
            "我已经了解到了不少\x01",
            "之前一无所知的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        "#11P哦，说到这里就可以了吗？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#00000F嗯，占用了您的时间，\x01",
            "真是不好意思。\x02\x03",

            "我们这就\x01",
            "告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xC,
        (
            "#11P哪里哪里，这点小事不值一提。\x01",
            "以后要是有机会，\x01",
            "随时欢迎各位再过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "#11P回去时\x01",
            "请一路小心啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(68880, 1500, 9870, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 68000, 0, 13400, 180)
    SetChrPos(0x102, 68000, 0, 13400, 180)
    SetChrPos(0x103, 68000, 0, 13400, 180)
    SetChrPos(0x104, 68000, 0, 13400, 180)
    SetChrPos(0x109, 68000, 0, 13400, 180)
    SetChrPos(0x105, 68000, 0, 13400, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearMapObjFlags(0x1, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x105, 3, 0, 41)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 40)
    Sleep(500)
    OP_68(69520, 1500, 7610, 3000)
    BeginChrThread(0x104, 3, 0, 39)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 37)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 36)
    WaitChrThread(0x101, 3)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)

    #C0331
    ChrTalk(
        0x102,
        (
            "#00106F呼……\x01",
            "该说什么好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，听到了很惊人\x01",
            "的内情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        (
            "#00203F那个名叫敏涅斯的男人……\x01",
            "似乎比想象中还要精干呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        (
            "#00306F要完全理解他的话有点困难，\x01",
            "但好像的确很有发展前途呢……\x02\x03",

            "#00301F不过，哎……\x02",
        )
    )

    CloseMessageWindow()
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

    #C0335
    ChrTalk(
        0x109,
        (
            "#10101F……不管怎么说，我们已经\x01",
            "掌握了事情的大致情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x01",
            "暂且返回阿尔摩利卡村吧。\x02\x03",

            "#00001F还要向特鲁塔村长报告呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4C7E end

    def Function_30_6604(): pass

    label("Function_30_6604")


    def lambda_6609():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6609)

    def lambda_661A():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_661A)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 167730, 0, 2860, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_30_6604 end

    def Function_31_664F(): pass

    label("Function_31_664F")


    def lambda_6654():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6654)

    def lambda_6665():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6665)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 169150, 0, 2870, 2000, 0x0)
    Return()

    # Function_31_664F end

    def Function_32_6693(): pass

    label("Function_32_6693")


    def lambda_6698():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6698)

    def lambda_66A9():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_66A9)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 170230, 0, 1900, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_32_6693 end

    def Function_33_66DE(): pass

    label("Function_33_66DE")


    def lambda_66E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_66E3)

    def lambda_66F4():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_66F4)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 167400, 0, 1860, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_33_66DE end

    def Function_34_6729(): pass

    label("Function_34_6729")


    def lambda_672E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_672E)

    def lambda_673F():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_673F)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 168250, 0, 1200, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_34_6729 end

    def Function_35_6774(): pass

    label("Function_35_6774")


    def lambda_6779():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6779)

    def lambda_678A():
        OP_98(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_678A)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 169670, 0, 1220, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_35_6774 end

    def Function_36_67BF(): pass

    label("Function_36_67BF")


    def lambda_67C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67C4)

    def lambda_67D5():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67D5)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 68440, 0, 10210, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_36_67BF end

    def Function_37_680A(): pass

    label("Function_37_680A")


    def lambda_680F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_680F)

    def lambda_6820():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6820)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 67120, 0, 8910, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_37_680A end

    def Function_38_6855(): pass

    label("Function_38_6855")


    def lambda_685A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_685A)

    def lambda_686B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_686B)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 70510, 0, 9150, 2000, 0x0)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_38_6855 end

    def Function_39_68A0(): pass

    label("Function_39_68A0")


    def lambda_68A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_68A5)

    def lambda_68B6():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68B6)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 67540, 0, 7130, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_39_68A0 end

    def Function_40_68EB(): pass

    label("Function_40_68EB")


    def lambda_68F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_68F0)

    def lambda_6901():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6901)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 69250, 0, 6220, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_40_68EB end

    def Function_41_6936(): pass

    label("Function_41_6936")


    def lambda_693B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_693B)

    def lambda_694C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_694C)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 70730, 0, 7540, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_41_6936 end

    def Function_42_6981(): pass

    label("Function_42_6981")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B06")

    #C0337
    ChrTalk(
        0x9,
        "好了，扫除扫除……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00003F（要不要邀请她来担当\x01",
            "  职业女性选秀活动中的『女仆』呢……？）\x02\x03",

            "#00000F那个，不好意思。\x01",
            "有点事情想和你商量……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0339
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

    #C0340
    ChrTalk(
        0x9,
        "职、职业女性选秀吗……？\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x9,
        (
            "那、那个，对不起……\x01",
            "虽然很感谢各位的好意，\x01",
            "但我还有工作在身，不能离开……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x01",
            "不好意思，真是打扰了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 7)
    Jump("loc_6B6C")

    label("loc_6B06")


    #C0343
    ChrTalk(
        0x9,
        (
            "我不方便参加那个\x01",
            "职业女性选秀活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x9,
        (
            "虽然很感谢各位的好意，\x01",
            "但我还有工作在身，不能离开……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B6C")

    TalkEnd(0x9)
    Return()

    # Function_42_6981 end

    SaveToFile()

Try(main)
